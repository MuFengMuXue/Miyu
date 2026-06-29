## Chapter 4. Installing the NVIDIA Driver

## Before you Begin

Before you begin the installation, exit the X server and terminate all OpenGL applications (note that it is possible that some OpenGL applications persist even after the X server has stopped). You should also set the default run level on your system such that it will boot to a VGA console, and not directly to X. Doing so will make it easier to recover if there is a problem during the installation process. See [Appendix I, *Tips for New Linux Users*](newusertips.html "Appendix I. Tips for New Linux Users") for details.

If you're installing on a system that is set up to use the Nouveau driver, then you should first disable it before attempting to install the NVIDIA driver. See [Q & A 8.1, “Interaction with the Nouveau Driver”](commonproblems.html#nouveau "Interaction with the Nouveau Driver") for details.

## Starting the Installer

After you have downloaded the file `NVIDIA-Linux-x86_64-580.105.08.run`, change to the directory containing the downloaded file, and as the `root` user run the executable:

``` screen
    # cd yourdirectory
    # sh NVIDIA-Linux-x86_64-580.105.08.run
```

The `.run` file is a self-extracting archive. When executed, it extracts the contents of the archive and runs the contained `nvidia-installer` utility, which provides an interactive interface to walk you through the installation.`nvidia-installer` will also install itself to `/usr/bin/nvidia-installer`, which may be used at some later time to uninstall drivers, auto-download updated drivers, etc. The use of this utility is detailed later in this chapter.

You may also supply command line options to the `.run` file. Some of the more common options are listed below.

### Common `.run` Options

- `--info`: Print embedded info about the `.run` file and exit.
- `--check`: Check integrity of the archive and exit.
- `--extract-only`: Extract the contents of `./NVIDIA-Linux-x86_64-580.105.08.run`, but do not run `nvidia-installer`.
- `--help`: Print usage information for the common commandline options and exit.
- `--advanced-options`: Print usage information for common command line options as well as the advanced options, and then exit.

## Installing the Kernel Interface

The NVIDIA kernel module has a kernel interface layer that must be compiled specifically for each kernel. NVIDIA distributes the source code to this kernel interface layer.

When the installer is run, it will check your system for the required kernel sources and compile the kernel interface. You must have the source code for your kernel installed for compilation to work. On most systems, this means that you will need to locate and install the correct kernel-source, kernel-headers, or kernel-devel package; on some distributions, no additional packages are required.

After the correct kernel interface has been compiled, the kernel interface will be linked with the closed-source portion of the NVIDIA kernel module. This requires that you have a linker installed on your system. The linker, usually `/usr/bin/ld`, is part of the binutils package. You must have a linker installed prior to installing the NVIDIA driver.

## Registering the NVIDIA Kernel Module with DKMS

The installer will check for the presence of DKMS on your system. If DKMS is found, you will be given the option of registering the kernel module with DKMS. On most systems with DKMS, DKMS will take care of automatically rebuilding registered kernel modules when installing a different Linux kernel. This is typically done by hooks that Linux distributions set up to be triggered as part of the kernel installation process. If your system is not configured to automatically run DKMS to rebuild kernel modules after installing a different kernel, you may run **`dkms autoinstall`** to trigger the process manually.

Note that while DKMS is useful for rebuilding the kernel modules after a minor kernel update, such as typical maintenance and security updates that Linux distributions may publish on a regular basis, a major kernel update may require installing a newer NVIDIA driver, as changes to the kernel APIs may not be compatible with the existing driver version.

On systems which require signed kernel modules, newer versions of DKMS may assist you in generating and enrolling a Machine Owner Key (MOK), so that future automated DKMS builds can reuse the already trusted signing keys. This is more convenient than having to create a new signature every time the kernel modules are rebuilt; however, it is slightly less secure, as the keys will be stored at a well-known location in your filesystem.

## Signing the NVIDIA Kernel Module

Some kernels may require that kernel modules be cryptographically signed by a key trusted by the kernel in order to be loaded. In particular, many distributions require modules to be signed when loaded into kernels running on UEFI systems with Secure Boot enabled. `nvidia-installer` includes support for signing the kernel module before installation, to ensure that it can be loaded on such systems. Note that not all UEFI systems have Secure Boot enabled, and not all kernels running on UEFI Secure Boot systems will require signed kernel modules, so if you are uncertain about whether your system requires signed kernel modules, you may try installing the driver without signing the kernel module, to see if the unsigned kernel module can be loaded.

In order to sign the kernel module, you will need a private signing key, and an X.509 certificate for the corresponding public key. The X.509 certificate must be trusted by the kernel before the module can be loaded: we recommend ensuring that the signing key be trusted before beginning the driver installation, so that the newly signed module can be used immediately. If you do not already have a key pair suitable for module signing use, you must generate one. Please consult your distribution's documentation for details on the types of keys suitable for module signing, and how to generate them. `nvidia-installer` can generate a key pair for you at install time, but it is preferable to have a key pair already generated and trusted by the kernel before installation begins.

Once you have a key pair ready, you can use that key pair in `nvidia-installer` by passing the keys to the installer on the command line with the `--module-signing-secret-key` and `--module-signing-public-key` options. As an example, it is possible to install the driver with a signed kernel module in silent mode (i.e., non-interactively) by running:

``` screen
 # sh ./NVIDIA-Linux-x86_64-580.105.08.run -s \
--module-signing-secret-key=/path/to/signing.key \
--module-signing-public-key=/path/to/signing.x509
```

In the example above, `signing.key` and `signing.x509` are a private/public key pair, and the public key is already enrolled in one of the kernel's trusted module signing key sources.

On UEFI systems with secure boot enabled, nvidia-installer will present a series of interactive prompts to guide users through the module signing process. As an alternative to setting the key paths on the command line, the paths can be provided interactively in response to the prompts. These prompts will also appear when building the NVIDIA kernel module against a kernel which has CONFIG_MODULE_SIG_FORCE enabled in its configuration, or if the installer is run in expert mode.

### Key Sources Trusted by the Kernel

In order to load a kernel module into a kernel that requires module signatures, the module must be signed by a key that the kernel trusts. There are several sources that a kernel may draw upon to build its pool of trusted keys. If you have generated a key pair, but it is not yet trusted by your kernel, you must add a certificate for your public key to a trusted key source before it can be used to verify signatures of signed kernel modules. These trusted sources include:

Certificates embedded into the kernel image
On kernels with `CONFIG_MODULE_SIG` set, a certificate for the public key used to sign the in-tree kernel modules is embedded, along with any additional module signing certificates provided at build time, into the kernel image. Modules signed by the private keys that correspond to the embedded public key certificates will be trusted by the kernel.

Since the keys are embedded at build time, the only way to add a new public key is to build a new kernel. On UEFI systems with Secure Boot enabled, the kernel image will, in turn, need to be signed by a key that is trusted by the bootloader, so users building their own kernels with custom embedded keys should have a plan for making sure that the bootloader will load the new kernel.

Certificates stored in the UEFI firmware database
On kernels with `CONFIG_MODULE_SIG_UEFI`, in addition to any certificates embedded into the kernel image, the kernel can use certificates stored in the `db`,`KEK`, or `PK` databases of the computer's UEFI firmware to verify the signatures of kernel modules, as long as they are not in the UEFI `dbx` blacklist.

Any user who holds the private key for the Secure Boot `PK`, or any of the keys in the `KEK` list should be able to add new keys that can be used by a kernel with `CONFIG_MODULE_SIG_UEFI`, and any user with physical access to the computer should be able to delete any existing Secure Boot keys, and install his or her own keys instead. Please consult the documentation for your UEFI-based computer system for details on how to manage the UEFI Secure Boot keys.

Certificates stored in a supplementary key database
Some distributions include utilities that allow for the secure storage and management of cryptographic keys in a database that is separate from the kernel's built-in key list, and the key lists in the UEFI firmware. A prominent example is the MOK (Machine Owner Key) database used by some versions of the `shim` bootloader, and the associated management utilities,`mokutil` and `MokManager`.

Such a system allows users to enroll additional keys without the need to build a new kernel or manage the UEFI Secure Boot keys. Please consult your distribution's documentation for details on whether such a supplementary key database is available, and if so, how to manage its keys.

### Generating Signing Keys in nvidia-installer

`nvidia-installer` can generate keys that can be used for module signing, if existing keys are not readily available. Note that a module signed by a newly generated key cannot be loaded into a kernel that requires signed modules until its key is trusted, and when such a module is installed on such a system, the installed driver will not be immediately usable, even if the installation was successful.

When `nvidia-installer` generates a key pair and uses it to sign a kernel module, an X.509 certificate containing the public key will be installed to disk, so that it can be added to one of the kernel's trusted key sources.`nvidia-installer` will report the location of the installed certificate: make a note of this location, and of the certificate's SHA1 fingerprint, so that you will be able to enroll the certificate and verify that it is correct, after the installation is finished.

By default, `nvidia-installer` will attempt to securely delete the generated private key with `shred -u` after the module is signed. This is to prevent the key from being exploited to sign a malicious kernel module, but it also means that the same key can't be used again to install a different driver, or even to install the same driver on a different kernel.`nvidia-installer` can optionally install the private signing key to disk, as it does with the public certificate, so that the key pair can be reused in the future.

If you elect to install the private key, please make sure that appropriate precautions are taken to ensure that it cannot be stolen. Some examples of precautions you may wish to take:

Prevent the key from being read by anybody without physical access to the computer
In general, physical access is required to install Secure Boot keys, including keys managed outside of the standard UEFI key databases, to prevent attackers who have remotely compromised the security of the operating system from installing malicious boot code. If a trusted key is available to remote users, even root, then it will be possible for an attacker to sign arbitrary kernel modules without first having physical access, making the system less secure.

One way to ensure that the key is not available to remote users is to keep it on a removable storage medium, which is disconnected from the computer except when signing modules.

Do not store the unencrypted private key
Encrypting the private key can add an extra layer of security: the key will not be useful for signing modules unless it can be successfully decrypted, first. Make sure not to store unencrypted copies of the key on persistent storage: either use volatile storage (e.g. a RAM disk), or securely delete any unencrypted copies of the key when not in use (e.g. using `shred` instead of `rm`). Note that using `shred` may not be sufficient to fully purge data from some storage devices, in particular, some types of solid state storage.

### Alternatives to the Installer's Module Signing Support

It is possible to load the NVIDIA kernel module on a system that requires signed modules, without using the installer's module signing support. Depending on your particular use case, you may find one of these alternatives more suitable than signing the module with `nvidia-installer`:

Disable UEFI Secure Boot, if applicable
On some kernels, a requirement for signed modules is only enforced when booted on a UEFI system with Secure Boot enabled. Some users of such kernels may find it more convenient to disable Secure Boot; however, note that this will reduce the security of your system by making it easier for malicious users to install potentially harmful boot code, kernels, or kernel modules.

Use a kernel that doesn't require signed modules
The kernel can be configured not to check module signatures, or to check module signatures, but allow modules without a trusted signature to be loaded, anyway. Installing a kernel configured in such a way will allow the installation of unsigned modules. Note that on Secure Boot systems, you will still need to ensure that the kernel be signed with a key trusted by the bootloader and/or boot firmware, and that a kernel that doesn't enforce module signature verification may be slightly less secure than one that does.

## Adding Precompiled Kernel Interfaces to the Installer Package

When `nvidia-installer` runs, it searches for a pre-compiled kernel interface layer for the target kernel: if one is found, then the complete kernel module can be produced by linking the precompiled interface with `nv-kernel.o`, instead of needing to compile the kernel interface on the target system.`nvidia-installer` includes a feature which allows users to add a precompiled interface to the installer package. This is useful in many use cases; for example, an administrator of a large group of similarly configured computers can prepare an installer package with a precompiled interface for the kernel running on those computers, then deploy the customized installer, which will be able to install the NVIDIA kernel module without needing to have the kernel development headers or a compiler installed on the target systems. (A linker is still required.)

To use this feature, simply invoke the `.run` installer package with the `--add-this-kernel` option; e.g.

``` screen
 # sh ./NVIDIA-Linux-x86_64-580.105.08.run --add-this-kernel
```

This will unpack `NVIDIA-Linux-x86_64-580.105.08.run`, compile a kernel interface layer for the currently running kernel (use the `--kernel-source-path` and `--kernel-output-path` options to specify a target kernel other than the currently running one), and create a new installer package with the kernel interface layer added.

Administrators of large groups of similarly configured computers that are configured to require trusted signatures in order to load kernel modules may find this feature especially useful when combined with the built-in support for module signing in `nvidia-installer`. To package a .run file with a precompiled kernel interface layer, plus a detached module signature for the linked module, just use the `--module-signing-secret-key` and `--module-signing-public-key` options alongside the `--add-this-kernel` option. The resulting package, besides being installable without kernel headers or a compiler on the target system, has the added benefit of being able to produce a signed module without needing access to the private key on the install target system. Note that the detached signature will only be valid if the result of linking the precompiled interface with `nv-kernel.o` on the target system is exactly the same as the result of linking those two files on the system that was used to create the custom installer. To ensure optimal compatibility, the linker used on both the package preparation system and the install target system should be the same.

## Other Features of the Installer

Without options, the `.run` file executes the installer after unpacking it. The installer can be run as a separate step in the process, or can be run at a later time to get updates, etc. Some of the more important commandline options of `nvidia-installer` are:

**`nvidia-installer` options**`--uninstall`
During installation, the installer will make backups of any conflicting files and record the installation of new files. The uninstall option undoes an install, restoring the system to its pre-install state.

`--ui=none`
The installer uses an ncurses-based user interface if it is able to locate the correct ncurses library. Otherwise, it will fall back to a simple commandline user interface. This option disables the use of the ncurses library.
