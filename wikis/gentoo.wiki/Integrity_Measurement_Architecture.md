The Linux **I**ntegrity **M**easurement **A**rchitecture (IMA) subsystem is responsible for calculating the hashes of files and programs before they are loaded, and supports reporting on the hashes and validate if they adhere to a predefined list. This article introduces IMA technology and provides instructions on how it can be enabled and implemented in Gentoo Linux.

## Contents

-   [[1] [Purpose of IMA]](#Purpose_of_IMA)
    -   [[1.1] [Introduction]](#Introduction)
    -   [[1.2] [Trusted Computing Base]](#Trusted_Computing_Base)
-   [[2] [Setting up IMA]](#Setting_up_IMA)
    -   [[2.1] [Kernel configuration]](#Kernel_configuration)
    -   [[2.2] [Kernel command line options]](#Kernel_command_line_options)
    -   [[2.3] [Enable i_version mount option (optional)]](#Enable_i_version_mount_option_.28optional.29)
    -   [[2.4] [Registering the file hashes for the system]](#Registering_the_file_hashes_for_the_system)
    -   [[2.5] [Using digital signatures for immutable files]](#Using_digital_signatures_for_immutable_files)
-   [[3] [Using the IMA subsystem]](#Using_the_IMA_subsystem)
    -   [[3.1] [Reading the integrity log]](#Reading_the_integrity_log)
-   [[4] [Asked questions with answers]](#Asked_questions_with_answers)
    -   [[4.1] [How do I know IMA with appraisal is working?]](#How_do_I_know_IMA_with_appraisal_is_working.3F)
    -   [[4.2] [I was able to edit an \'immutable\' file and still run it. How come?]](#I_was_able_to_edit_an_.27immutable.27_file_and_still_run_it._How_come.3F)
    -   [[4.3] [How do I load a custom IMA policy?]](#How_do_I_load_a_custom_IMA_policy.3F)
    -   [[4.4] [Online resources tell me I can use head -n 1 to regenerate the hashes]](#Online_resources_tell_me_I_can_use_head_-n_1_to_regenerate_the_hashes)
-   [[5] [See also]](#See_also)

## [Purpose of IMA]

### [Introduction]

** Warning**\
Enabling IMA on a system is currently only recommended for *development* purposes.

The Linux IMA subsystem introduces hooks within the Linux kernel to support creating and collecting hashes of files when opened, before their contents are accessed for read or execute. The IMA subsystem has 2 subsystems within in it - **measure** and **appraise**. **Measurement** collects the hashes of files, while **appraisal** compares a collected hash to a stored hash and denies access in the event of a mismatch.

To support proven integrity of the files, the IMA measurement subsystem can interact with the TPM chip within the system to protect the collected hashes from tampering by a rogue administrator or application.

The IMA measurement subsystem was added in linux-2.6.30. Appraisal came later, in linux-3.7.

Protection of the extended attribute itself is handled by [EVM](https://wiki.gentoo.org/wiki/Extended_Verification_Module "Extended Verification Module").

### [Trusted Computing Base]

** Warning**\
The default policies are unsuitable for general-use systems. The [tcb] policy opens up a local DoS where a malicious user can fill the measurement log and make the kernel run out of memory. The [tcb_appraise] policy prevents Portage from working.

The Trusted Computing Base defines a set of rules that a properly, integrity-protected system should adhere to. Linux defines 2 policies for this: The [tcb] policy, which performs measurement, and [tcb_appraise] which performs appraisal.

## [Setting up IMA]

### [Kernel configuration]

First, enable the IMA subsystem in the Linux kernel configuration.

[KERNEL] **Linux kernel configuration for IMA**

    CONFIG_INTEGRITY=y
    CONFIG_IMA=y
    CONFIG_IMA_MEASURE_PCR_IDX=10
    CONFIG_IMA_LSM_RULES=y
    CONFIG_INTEGRITY_SIGNATURE=y
    CONFIG_IMA_APPRAISE=y

    # Since 4.13
    IMA_APPRAISE_BOOTPARAM=y

### [Kernel command line options]

There are 3 important IMA command line options: [lsm=integrity], [ima_appraise=], and [ima_policy=]

[lsm=integrity] turns on the integrity LSM. If this is not specified. the kernel will panic when **init** is run. If there are other LSMs that needed to be loaded, sperate them with a comma: [lsm=selinux,integrity]

[ima_appraise=] can take 1 of 4 values:

-   **enforce** causes IMA to appraise files according to policy. Access is denied to the appraised file if the store hash is missing or does not match the collected value. IMA generates new stored hashes for new files and changed files with valid hashes.
-   **log** is similar to **enforce** except access is not denied but only logged.
-   **off** disables all appraisal. The stored hashes aren\'t checked and new stored hashes are not generated or updated.
-   **fix** creates and updates the stored hashes of files that would otherwise be appraised.

[ima_policy=] can take 1 of 3 values:

-   **tcb** measures all executables run, all mmap\'d files for execution (such as shared libraries), all kernel modules loaded, and all firmware loaded. Additionally, a files opened for read by root are measured as well.
-   **appraise_tcb** appraises all files owned by root.
-   **secure_boot** appraises all loaded modules, firmware, kexec\'d kernel, and IMA policies. It also requires them to have an IMA signature as well. This is normally used with the `CONFIG_INTEGRITY_TRUSTED_KEYRING` option in the kernel in \"secure boot\" scenario, with the public key obtained from the OEM in firmware or via the MOK (Machine Owner Key) in *shim*.

[ima_policy=] can be specified multiple times, and the result is the union of the policies.

### [][Enable i_version mount option (optional)]

Mount all file systems with the [i_version] support (which, sadly, means it needs to added with [iversion] mount option - without the underscore). This is an optimization for IMA, allowing it to only recompute the hash of file when it actually changes instead of every time the file is opened.

[FILE] **`/etc/fstab`Enabling i_version on all mounts**

    # Example for a single partition, in /etc/fstab:
    /dev/vda1  /  ext4  noatime,iversion  1 2

For the root file system, it can be enabled through the [rootflags] kernel parameter as well so that it gets mounted immediately with i_version support when the Linux kernel mounts the root file system.

[FILE] **`/etc/default/grub`Using rootflags in the bootloader configuration**

    GRUB_CMDLINE_LINUX="rootflags=i_version dolvm lsm=integrity ima_appraise=enforce ima_policy=tcb ima_policy=appraise_tcb"

Note that the underscore needs to be present here, unlike in the fstab case.

### [Registering the file hashes for the system]

** Note**\
This is only applicable when IMA appraisal is enabled.

First boot with the [ima_appraise=fix] boot option. This will allow the system to boot up even when no (or wrong) hashes are registered.

** Important**\
[ima_appraise=fix] only creates and updates hashes on the files that would otherwise be appraised, so if using a custom IMA policy, that policy must be loaded *first*. If neither [ima_policy=appraise_tcb] or a custom policy is loaded, the default policy is to not appraise anything, and the below command will have no effect. Additionally, this process may need to be completed if there\'s a change in the IMA policy

Next, all files that will be appraised need to be opened for read. This process could take some time:

`root `[`#`]`time find / -fstype ext4 -type f -uid 0 -exec dd if='' of=/dev/null count=0 status=none \;`

    real 62m19.370s
    user    1m48.231s
    sys 3m42.958s

** Note**\
As find does not yet (or ever) support [btrfs] for the [-fstype] paramter, use the [-xdev] option instead

`root `[`#`]`time find / -xdev -type f -uid 0 -exec dd if='' of=/dev/null count=0 status=none \;`

When done, the stored hash value should show as an extended attribute:

`root `[`#`]`getfattr -m - -d /sbin/init`

    # file: sbin/init
    security.ima=0sAXr7Qmun5mkGDS286oZxCpdGEuKT
    security.selinux="system_u:object_r:init_exec_t"

Finally, reboot with [ima_appraise=enforce]. The system should now run with appraisal enabled, causing the system to validate the hash against the stored value before using it. If it doesn\'t match, then the file is not loaded and any access towards it will be denied with a *Permission denied* error.

Appraisal can be verified with [ima_appraise=off] and changing the contents of a root-owned file (or the value of the extended attribute) and reboot with [ima_appraise=enforce], or by directly editing virtual guest images.

### [Using digital signatures for immutable files]

The IMA appraisal code also supports immutable files. In this case, an RSA-key based signature is taken of the file and stored in the extended attribute. The private key is used to sign the files, whereas the public key is used to verify the signature. This provides additional protection against tampering as the private key does not need to be available on the system while its running (only during the initial marking).

To generate an unencrypted private key (non-protected):

`user `[`$`]`openssl genrsa -out rsa_private.pem 2048`

To generate the public key:

`user `[`$`]`openssl rsa -pubout -in rsa_private.pem -out rsa_public.pem`

To sign such immutable files (like kernel modules and application code), the [evmctl] command provided by the [[[app-crypt/ima-evm-utils]](https://packages.gentoo.org/packages/app-crypt/ima-evm-utils)[]] package needs be used. But first, setup the kernel keyring:

`root `[`#`]`evmctl import --rsa rsa_public.pem $(keyctl newring _ima @u)`

This allows the IMA subsystem to validate the signature (which is also needed when initially setting the signature) by loading the public key onto the IMA keyring. This needs to be done every time the system boots, so it makes sense to do so within an initramfs (early in the boot process).

To sign the all the kernel modules with an IMA signature:

`root `[`#`]`find /lib/modules -name \*.ko -type f -uid 0 -exec evmctl ima_sign --key rsa_private.pem '' \;`

Immutable file support is mainly used to digitally sign the Linux kernel and the kernel modules and is supported through the EVM technology but works well on ELF and other binaries as well.

## [Using the IMA subsystem]

### [Reading the integrity log]

To read the integrity log as registered by the IMA subsystem, look at the [/sys/kernel/security/ima/ascii_runtime_measurements] file:

`root `[`#`]`head /sys/kernel/security/ima/ascii_runtime_measurements`

    10 ddee6004dc3bd4ee300406cd93181c5a2187b59b ima-ng sha1:9797edf8d0eed36b1cf92547816051c8af4e45ee boot_aggregate
    10 180ecafba6fadbece09b057bcd0d55d39f1a8a52 ima-ng sha1:db82919bf7d1849ae9aba01e28e9be012823cf3a /init
    10 ac792e08a7cf8de7656003125c7276968d84ea65 ima-ng sha1:f778e2082b08d21bbc59898f4775a75e8f2af4db /bin/bash
    10 0a0d9258c151356204aea2498bbca4be34d6bb05 ima-ng sha1:b0ab2e7ebd22c4d17d975de0d881f52dc14359a7 /lib64/ld-2.27.so
    10 0d6b1d90350778d58f1302d00e59493e11bc0011 ima-ng sha1:ce8204c948b9fe3ae67b94625ad620420c1dc838 /etc/ld.so.cache
    10 d69ac2c1d60d28b2da07c7f0cbd49e31e9cca277 ima-ng sha1:8526466068709356630490ff5196c95a186092b8 /lib64/libreadline.so.7.0
    10 ef3212c12d1fbb94de9534b0bbd9f0c8ea50a77b ima-ng sha1:f80ba92b8a6e390a80a7a3deef8eae921fc8ca4e /lib64/libc-2.27.so
    10 f805861177a99c61eabebe21003b3c831ccf288b ima-ng sha1:261a3cd5863de3f2421662ba5b455df09d941168 /lib64/libncurses.so.6.1
    10 52f680881893b28e6f0ce2b132d723a885333500 ima-ng sha1:b953a3fa385e64dfe9927de94c33318d3de56260 /lib64/libnss_files-2.27.so
    10 4da8ce3c51a7814d4e38be55a2a990a5ceec8b27 ima-ng sha1:99a9c095c7928ecca8c3a4bc44b06246fc5f49de /etc/passwd

`root `[`#`]`tail /sys/kernel/security/ima/ascii_runtime_measurements`

    10 4848cf2c61234ab3f1b401393977672c9ddf06f1 ima-ng sha1:e3110d04ef7f0aa4bf202e26ab57922c850d26f8 /etc/pam.d/su
    10 38939fd3ae9f769d3161be0e2d64caaf6bba7c05 ima-ng sha1:45cc4ba2611a425143b907b85910cfd1dbc9e10c /lib64/security/pam_rootok.so
    10 a9a24168c14311a700f388e7d366c316c389e60a ima-ng sha1:07498365392e741def254e4cb11dd5f678a80716 /lib64/security/pam_wheel.so
    10 e671c9879c366c1e4e334a73a37f31c6314e4938 ima-ng sha1:31eb4b6be306e0d7d65760f14833791e457bfd70 /lib64/security/pam_xauth.so
    10 161dcb0153b5cfeab9a68e65c7373ddc6a69eaca ima-ng sha1:9d1344c4bd6ca2a507b1373eb4ba95fa1208bebb /etc/terminfo/x/xterm-256color
    10 85327b8f29876b2e849e796193fe0024d2343bb4 ima-ng sha1:025eb281bccf4fe970682b07a2b0617759d0bd90 /bin/head
    10 0be8f088844744f80eeb6daa89c82b5fc4499ba5 ima-ng sha1:810e9405ee37185d6eea6879c4a0e3369ac4e68e /bin/tail
    10 9ade4647fe649b36db4ec11ef7c56093dba9548b ima-ng sha1:1135bb946dd98cf7a171e2e4c9c043981b9858aa /bin/getfattr
    10 ad6bb7e7f79ee799244f15b6d9a253be744d79da ima-ng sha1:9fea4eb8658a8a06f2207a3e7b43acaa03a5aae9 /bin/ps
    10 661d2b076d842975ef0295b84f988519ca431507 ima-ng sha1:5bd1adcf179695cdd3468b363b2979609c08cbab /lib64/libprocps.so.7.1.0

The columns (from left to right) are:

-   **PCR (Platform Configuration Register)** in which the values are registered. This only makes sense if a TPM chip is in use.
-   **Template hash** of the entry, which is a hash that combines the length and values of the file content hash and the pathname
-   **Template** that registered the integrity value (ima-ng the case)
-   **File content** hash which is the hash of the file itself

The default hash algorithm is SHA-1.

## [Asked questions with answers]

### [][How do I know IMA with appraisal is working?]

This is as simple as finding a file that does not have its hash value stored as an extended attribute while ima_appraise is in enforcing mode.

`root `[`#`]`getfattr -m . -d /etc/mtab`

    getfattr: Removing leading '/' from absolute path names
    # file: etc/mtab
    security.selinux="system_u:object_r:etc_runtime_t"

`root `[`#`]`cat /etc/mtab`

    cat: /etc/mtab: Permission denied

`root `[`#`]`dmesg | tail -1`

    [  256.756465] type=1800 audit(1356637858.947:53): pid=3852 uid=0 auid=0 ses=2
    subj=root:sysadm_r:sysadm_t op="appraise_data" cause="missing-hash" comm="cat"
    name="/etc/mtab" dev="dm-2" ino=394144 res=0

In the above example, the IMA subsystem reports that the [/etc/mtab] file misses its hash value (which should be stored as [security.ima]) and as such is denying the [cat] application access to it.

When missing the file (such as with [/etc/mtab]) it removed and regenerated:

`root `[`#`]`rm /etc/mtab `

`root `[`#`]`cat /proc/mounts > /etc/mtab`

When using SELinux:

`root `[`#`]`restorecon /etc/mtab`

Next:

`root `[`#`]`evmctl ima_hash /etc/mtab `

`root `[`#`]`getfattr -m . -d /etc/mtab`

    getfattr: Removing leading '/' from absolute path names
    # file: etc/mtab
    security.ima=0sAUlIU5ffoobWOh0FsSIbgh9Ac8YK
    security.selinux="root:object_r:etc_runtime_t"

### [][I was able to edit an \'immutable\' file and still run it. How come?]

When using a digitally signed a script using [evmctl sign \--imasig \<file\> \] and then edited the file with [vim], then this behavior is to be expected. [vim] removes the original file and replaces it with a new one. The newly created file is given an appropriate hash (but no digital signature of course) and thus it can still be executed.

The use of digital signatures is more for kernel modules and ELF binaries. But below an example of how it does work when editing the file rather than replacing it.

`root `[`#`]`evmctl sign --imasig ./test.sh /root/rsa_private.pem `

`root `[`#`]`./test.sh`

    Hello World (again)

`root `[`#`]`echo "echo \"And now...\"" >> test.sh`

`root `[`#`]`./test.sh`

    bash: ./test.sh: Permission denied

`root `[`#`]`cat test.sh`

    cat: test.sh: Permission denied

`root `[`#`]`dmesg | tail -2`

    [  643.211490] type=1800 audit(1356639603.315:37): pid=3956 uid=0 auid=0 ses=3
    subj=root:sysadm_r:sysadm_t op="appraise_data" cause="invalid-signature"
    comm="bash" name="/bin/test.sh" dev="dm-2" ino=131466 res=0
    [  649.123917] type=1800 audit(1356639609.227:38): pid=3958 uid=0 auid=0 ses=3
    subj=root:sysadm_r:sysadm_t op="appraise_data" cause="invalid-signature"
    comm="cat" name="/bin/test.sh" dev="dm-2" ino=131466 res=0

### [][How do I load a custom IMA policy?]

It is possible, and recommended to use a custom IMA policy. A breakdown of the default rules and snippets to rules for be included can by found in [Integrity Measurement Architecture/Recipes](https://wiki.gentoo.org/wiki/Integrity_Measurement_Architecture/Recipes "Integrity Measurement Architecture/Recipes").

Make sure no empty lines are in the policy; if so, the policy will be refused. Check the output of [dmesg] for hints on why the policy was refused (it shows what was accepted, so the next line would be a not-accepted line). Alternatively check the audit logs ([auditd] will need to be running). When seeing lines such as *audit_printk_skb: XX callbacks suppressed* then the system may not be displaying all the needed information.

Have the policy be loaded in as soon as possible, either in an initramfs or early in the boot process through an init script in the *sysinit* runlevel. I keep my policy in [/etc/ima] and use the following small init script to load it early on:

[CODE] **Init script to load a custom ima policy**

    #!/sbin/openrc-run
    # Copyright 1999-2012 Gentoo Foundation
    # Distributed under the terms of the GNU General Public License v2
    # $Header: /var/cvsroot/gentoo/xml/htdocs/proj/en/hardened/integrity/docs/ima-guide.xml,v 1.11 2013/03/09 13:55:21 swift Exp $

    description="Load in custom IMA policy"

    depend()

    start()

** Warning**\
When using an initramfs, be aware that [/usr] may not properly mounted. This is because busybox mount does not support the iversion mount option which is required. Update the initramfs to mount without iversion, and remount it as soon as possible later.

### [Online resources tell me I can use head -n 1 to regenerate the hashes]

I have bad experiences with this method. Some files are left without a hash, or when I later enable EVM the EVM hash itself remains missing. The use of the [evmctl] command does the trick pretty well.

## [See also]

-   [Integrity Measurement Architecture/Recipes](https://wiki.gentoo.org/wiki/Integrity_Measurement_Architecture/Recipes "Integrity Measurement Architecture/Recipes") --- introduces Integrity Measurement Architecture recipes for the Linux kernel.
-   [Extended Verification Module](https://wiki.gentoo.org/wiki/Extended_Verification_Module "Extended Verification Module") --- used to validate security-sensitive extended attributes before allowing operations on the files.