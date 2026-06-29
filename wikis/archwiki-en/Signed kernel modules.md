# Signed kernel modules

Signed kernel modules provide a mechanism for the kernel to verify the integrity of a module.

## Overview
The Linux kernel distinguishes and keeps separate the verification of modules from requiring or forcing modules to verify before allowing them to be loaded. Kernel modules fall into 2 classes:

* Standard in-tree modules which come with the kernel source code. They are compiled during the normal kernel build.
* Out-of-tree modules which are not part of the kernel source distribution. They are built outside of the kernel tree, requiring the kernel headers package for each kernel they are to be built for. They can be built manually for a specific kernel and packaged, or they can be built whenever needed using DKMS.

During a standard kernel compilation, the kernel build tools create a private/public key pair and sign every in-tree module (using the private key). The public key is saved in the kernel itself. When a module is subsequently loaded, the public key can then be used to verify that the module is unchanged.

The kernel can be enabled to always verify modules and report any failures to standard logs. The choice to permit the loading and use of a module which could not be verified can be either compiled into kernel or turned on at runtime using a kernel parameter as explained below.

## Summary of what needs to be done
The starting point is based on a custom kernel package as outlined in Kernel/Arch build system. We will modify the build to sign the standard in-tree kernel modules and to provide the prerequisites for signing and verifying out-of-tree modules.

Each kernel build needs to made aware of the key pair to be used for signing out-of-tree modules. A kernel configuration parameter is now used to make the kernel aware of additional signing keys: .

Keys and signing tools will be stored in the current module build directory. Nothing needs to be done to clean this as removal is handled by the standard module cleanup. The private and public keys are both installed in .

## Kernel configuration
 will be updated automatically using the script  provided below. In addition, the following configuration options should be set either manually by editing the  file, or via  in the Linux  directory and subsequently copying the updated  file back to the build file . It is preferable to use elliptic curve type keys and zstd compression.

 CONFIG_MODULE_SIG=y
   Enable Loadable module suppot --->
   Module Signature Verification           -  activate

 CONFIG_MODULE_SIG_FORCE=n
   Require modules to be validly signed -> leave off (for now)

         This allows the decision to enforce verified modules only as boot command line.
         If you are comfortable all is working then by all means change this to 'y'
         Command line version of this is : module.sig_enforce=1

 CONFIG_MODULE_SIG_HASH=sha512
   Automatically sign all modules  - activate
   Which hash algorithm    -> SHA-512
   openssl 3.2+ and kernel 6.7+ bring support for SHA3-xxx (e.g. SHA3-512)

 CONFIG_MODULE_COMPRESS_ZSTD=y
   Compress modules on installation        - activate
   Compression algorithm (ZSTD)

 CONFIG_MODULE_SIG_KEY_TYPE_ECDSA=y
   Cryptographic API --->
   Certificates for Signature Checking --->
   Type of module signing key to be generated -> ECDSA

 CONFIG_MODULE_ALLOW_MISSING_NAMESPACE_IMPORTS=n
   Enable Loadable module support --->
   Allow loading of modules with missing namespace imports - set to no

## Kernel command line
When you have confirmed that the modules are being signed and that the kernel works as it should, you can enable the following kernel parameter to require that the kernel only permits verified modules to be loaded:

 module.sig_enforce=1

Before forcing verified modules on, please confirm that the system logs do not show any module signature failures being reported.

## Tools needed
## kernel build package
In the directory where the kernel package is built:

 $ mkdir certs-local

This directory will provide the tools to create the keys, as well as signing kernel modules.

Put these files into :

*
*
*
*
*
*
*
*
*
*
*

The file  and its companion configuration file  are used to create key pairs.

 also provides the kernel with the key information by updating the configuration file(s) used to build the kernel.

The script  signs out-of-tree kernel modules. It can be run manually and is invoked by . It handles modules compressed with xzand gzip and depends on python-zstandard to help handle those compressed with zstd.

 will create the key pairs in a directory named by date-time

 will check and update kernel configs given by the --config config(s) option. It takes either a single config file, or a shell glob for multiple files. e.g. --config 'conf/config.*'. All configs will be updated with the same key. The default keytype is ec (elliptic curve) and the default hash is sha512. These can be changed with command line options. See  -h for more details.

It also creates a soft link  to the same directory holding the current key pairs.

 is to be called from the package_headers() function of PKGBUILD to install the signing keys. Example is given below.

These files are available and links are provided below.

## DKMS support
## Native DKMS method
DKMS natively supports signing built modules, as long as your kernel headers include the  program in the  directory (most archkernel based PKGBUILDs, including the official ones).

You then need to let it know where your signing key and x509 certificate (on a regular Kernel build, these will be in  and ) are in :

In this example, it'll look into the per-kernel  directory, so either put your signing key/cert there, or if you're using a custom PKGBUILD, just install it from the kernel:

{{hc|PKGBUILD|2=
_package-headers() {
   # ...

   # copy signing keys for dkms
   install -Dt "$builddir/certs" -m 400 certs/signing_key.*
}
}}

Depending on your level of security paranoia, you definitely don't want to distribute these keys, but that goes for the certs-local method as well.

## certs-local method
 $ mkdir certs-local/dkms

Add 2 files to the  directory:

*
*

These will be installed in  and provide the means for DKMS to automatically sign modules using the local key. This is the recommended way to sign out-of-tree kernel modules. As explained below, once this is installed, all that is needed is for DKMS to automatically sign modules is to make a soft link for each module to the configuration file.

 $ cd /etc/dkms
 # ln -s kernel-sign.conf module_name.conf

For example:

 # ln -s kernel-sign.conf vboxdrv.conf

The link creation can easily be added to an arch package to simplify further if desired.

## Modify PKGBUILD
We need to make changes to kernel build as follows:

## prepare()
Add the following to the top of the  function:

{{hc|PKGBUILD|
prepare() {

    msg2 "Rebuilding local signing key..."
    ../certs-local/genkeys.py -v --config config

    ...
}
}}

The default key regeneration refresh period is 7 days, but this can be changed on the command line. So if you want to create new keys monthly, then add "--refresh 30days" as an argument to genekeys.py. You can refresh on every build by using "--refresh always". Refresh units can be seconds,minutes,hours,days or weeks.

## _package-headers()
Add the following to the bottom of the  function:

{{hc|PKGBUILD|2=
_package-headers() {

    ...

    #
    # Out-of-tree module signing
    # This is run in the kernel source / build directory
    #
    msg2 "Local Signing certs for out-of-tree modules..."

    certs_local_src="../../certs-local"
    certs_local_dst="${builddir}/certs-local"
    $certs_local_src/install-certs.py $certs_local_dst

    # DKMS tools
    dkms_src="$certs_local_src/dkms"
    dkms_dst="${pkgdir}/etc/dkms"
    mkdir -p $dkms_dst

    rsync -a $dkms_src/{kernel-sign.conf,kernel-sign.sh} $dkms_dst/
}
}}

## Files required
The 5 supporting files referenced above are available for download from the github.com/gene-git/Arch-SKM repository:

* certs-local/x509.oot.genkey
* certs-local/genkeys.py
* certs-local/install-certs.py
* certs-local/sign_module.py
* certs-local/lib/signer_class.py
* certs-local/lib/utils.py
* certs-local/dkms/kernel-sign.conf
* certs-local/dkms/kernel-sign.sh

Remember to ensure that the scripts are executable.

## Helper scripts
 builds:
*
*
*
*
*

& other AUR kernels.

The ''abk helper script reduces the manual steps for building a fully signed custom kernel to 3 commands to Update / Build & Install'' the kernel:

 abk -u kernel-name
 abk -b kernel-name
 abk -i kernel-name

With signed kernel module support for:

*
