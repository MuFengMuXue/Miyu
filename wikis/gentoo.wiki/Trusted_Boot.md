Trusted Boot, specifically Intel Trusted Execution Technology (TXT) is Intel\'s implementation of the Dynamic Root of Trust. This technology can be used and enabled on Gentoo Linux.

** Warning**\
Using Trusted Boot on your system is currently only recommended for development purposes. In particular, the current implementation [[[sys-boot/tboot]](https://packages.gentoo.org/packages/sys-boot/tboot)[]] is implemented as Compatibility Source Module (CSM) and does not fully support UEFI. UEFI variables are not accessible. Trusted Boot is also incompatible with UEFI [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot").

## Contents

-   [[1] [TXT, TPM, and Trust Concepts]](#TXT.2C_TPM.2C_and_Trust_Concepts)
    -   [[1.1] [Trusted Platform Module]](#Trusted_Platform_Module)
    -   [[1.2] [Platform Configuration Registers (PCR)]](#Platform_Configuration_Registers_.28PCR.29)
    -   [[1.3] [Static Root of Trust]](#Static_Root_of_Trust)
    -   [[1.4] [Dynamic Root of Trust]](#Dynamic_Root_of_Trust)
    -   [[1.5] [TXT Errors]](#TXT_Errors)
    -   [[1.6] [Measured Launch Elements]](#Measured_Launch_Elements)
-   [[2] [Kernel and BIOS configuration]](#Kernel_and_BIOS_configuration)
    -   [[2.1] [Kernel Config]](#Kernel_Config)
    -   [[2.2] [BIOS/UEFI Config]](#BIOS.2FUEFI_Config)
-   [[3] [Install tboot and obtain ACM]](#Install_tboot_and_obtain_ACM)
    -   [[3.1] [Installation of tboot]](#Installation_of_tboot)
    -   [[3.2] [Downloading the Authenticated Code Mode (ACM)]](#Downloading_the_Authenticated_Code_Mode_.28ACM.29)
    -   [[3.3] [Run grub-install and reboot]](#Run_grub-install_and_reboot)
    -   [[3.4] [Run txt-stat]](#Run_txt-stat)
        -   [[3.4.1] [Create /etc/defaults/grub-tboot]](#Create_.2Fetc.2Fdefaults.2Fgrub-tboot)
-   [[4] [Setup tboot - TPM 1.2]](#Setup_tboot_-_TPM_1.2)
    -   [[4.1] [Install and start needed utilities and service]](#Install_and_start_needed_utilities_and_service)
    -   [[4.2] [Setting the Launch Control Policy]](#Setting_the_Launch_Control_Policy)
        -   [[4.2.1] [Step 1: Measuring tboot and the tboot command line]](#Step_1:_Measuring_tboot_and_the_tboot_command_line)
        -   [[4.2.2] [Step 2: Measure PCR (optional)]](#Step_2:_Measure_PCR_.28optional.29)
        -   [[4.2.3] [Step 3: Create Verified Launch Policy.]](#Step_3:_Create_Verified_Launch_Policy.)
        -   [[4.2.4] [Step 4: Create a TXT policy with the created elements]](#Step_4:_Create_a_TXT_policy_with_the_created_elements)
        -   [[4.2.5] [Step 5: Write to TPM and setup Verified Launch]](#Step_5:_Write_to_TPM_and_setup_Verified_Launch)
    -   [[4.3] [Completing GRUB configuration]](#Completing_GRUB_configuration)
-   [[5] [Setup tboot - TPM 2.0]](#Setup_tboot_-_TPM_2.0)
-   [[6] [Troubleshooting and FAQ]](#Troubleshooting_and_FAQ)
    -   [[6.1] [Diagnosing failure with txt-parse_err]](#Diagnosing_failure_with_txt-parse_err)
    -   [[6.2] [Reboot and hangs]](#Reboot_and_hangs)

## [][TXT, TPM, and Trust Concepts]

### [Trusted Platform Module]

This is the hardware (or, especially on newer computers, firmware) that can store measurements, data, as well as decrypt and sign data. The TPM is limited in power and storage - it can only handle small of data (keys, counters, bitmaps), a has small amount for NVRAM (around 16k is typical), and is slow - TPM operations have a noticeable delay.

### [][Platform Configuration Registers (PCR)]

Measurement are stored here. There are 24 PCRs, some of which are reserved. They can\'t be written to in the standard sense, instead, they are \"extended\", under the following formula:

[CODE] **PCR Extension formula**

    PCR(new) = H(PCR(old) || H(data))

H is a secure hash function like SHA-1 or SHA-256, \|\| is the concatenation operator (not logical OR). This operation is neither communicative nor associative. The only way to get a PCR to particular value to measure the same data in the same order as originally.

### [Static Root of Trust]

Under the Static Root of Trust, the first program run on the PC is *core root of trust measurement* (or CRTM). It then measures the BIOS and extends PCR0 with its contents (Note: Any identifying information, like serial numbers, asset tags, etc are omitted from the data measured. This a group of identical devices configured identically with have the same PCR values). The BIOS then measure other data and extends the appropriate PCRs. Then it invokes bootloader (which may, in turn, extend PCRs as well) and load the operating system. The trust of the system depends on each component above it.

### [Dynamic Root of Trust]

Under the Dynamic Root of Trust, everything starts out the same as the Static Root of Trust. However, after the operating system is chosen but before its loaded, a special program is loaded. A special program - called the Authenticated Code Module (ACM) is loaded. This program acts as a \"scout\", verifying the various firmware an creating a secure enclave (in processors that support SGX, that is used, if it doesn\'t it does so through an unspecified mechanism). If everything checks and and the area is secure, it resets PCRs 17-23 (something only this code is allowed to do - in TPM terms *Locality 4* is used, and proceeds with the step

### [TXT Errors]

TXT does not deal with mismatches or errors gracefully. If an error occurs any time during the TXT process, (until tboot gains control) a *TXT Abort* is executed. The does a soft restart of the computer. Fortunately, the TXT error register is NOT cleared upon a soft reboot, so its possible to retrieve the last TXT error and decode it.

### [Measured Launch Elements]

TXT works with a special structure that consists of Measured Launch Elements. There are 5 elements: *mle* (Measured Launch Environment) , *pcr* (Platform Control Register), *custom* (can be anything, but in this case is tboot-private data to set up the Verified Launch), *sbios*, and *stm* (SMI Transfer Monitor) but only the first 3 of them will be used. The other 2 elements are not useful in defining a Platform Owner policy. *sbios* only has an effect in the Platform Suppier policy, and *stm* element does not exist in production.

## [Kernel and BIOS configuration]

### [Kernel Config]

The important kernel options are:

[KERNEL] **TXT Configuration for Linux**

    CONFIG_HAVE_INTEL_TXT=y
    CONFIG_INTEL_TXT=y
    CONFIG_IOMMU_DMA=y
    CONFIG_INTEL_IOMMU=y

### [][BIOS/UEFI Config]

The wording will vary,but at least hardware virtualization, Intel VT-d, Intel TXT. For TPM 1.2 the TPM needs to be enabled and active. CSM support must also be enabled, due the way [[[sys-boot/tboot]](https://packages.gentoo.org/packages/sys-boot/tboot)[]] is implemented.

## [Install tboot and obtain ACM]

#### [Installation of tboot]

Installing tboot is simple:

`root `[`#`]`emerge sys-boot/tboot`

Note that [[[sys-boot/tboot]](https://packages.gentoo.org/packages/sys-boot/tboot)[]] does not have stable keywords, so please see [Knowledge Base:Accepting a keyword for a single package](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package "Knowledge Base:Accepting a keyword for a single package") .

### [][Downloading the Authenticated Code Mode (ACM)]

Download the appropriate ACM if its not already BIOS (no harm if it is, the newest version is automatically used). The official URL is [https://www.intel.com/content/www/us/en/developer/articles/tool/intel-trusted-execution-technology.html](https://www.intel.com/content/www/us/en/developer/articles/tool/intel-trusted-execution-technology.html). TXT-supporting processors not listed at that site have the ACM built into the BIOS. Extract the ACM from archive and extract into /boot . Note the name of the module is important so the grub scripts can find it.

### [Run grub-install and reboot]

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

`root `[`#`]`shutdown -r now`

### [Run txt-stat]

`root `[`#`]`txt-stat`

    Intel(r) TXT Configuration Registers:
        STS: 0x00018091
            senter_done: TRUE
            sexit_done: FALSE
            mem_config_lock: FALSE
            private_open: TRUE
            locality_1_open: TRUE
            locality_2_open: TRUE
        ESTS: 0x00
            txt_reset: FALSE
        E2STS: 0x0000000000000006
            secrets: TRUE
        ERRORCODE: 0x00000000
        DIDVID: 0x00000001b0018086
            vendor_id: 0x8086
            device_id: 0xb001
            revision_id: 0x1
        FSBIF: 0x0000000000000000
        QPIIF: 0x000000009d003000
        SINIT.BASE: 0xdf700000
        SINIT.SIZE: 131072B (0x20000)
        HEAP.BASE: 0xdf720000
        HEAP.SIZE: 917504B (0xe0000)
        DPR: 0x00000000df800041
            lock: TRUE
            top: 0xdf800000
            size: 4MB (4194304B)
        PUBLIC.KEY:
            99 9c 2b ef 5f c4 d8 82 77 43 42 10 f4 ae d4 02
            95 0d 33 33 50 b6 1c 3d db ff a1 6f 3f d5 d3 d1

    ***********************************************************
         TXT measured launch: TRUE
         secrets flag set: TRUE
    ***********************************************************

If the bottom says \"TXT measured launch: TRUE\" it worked. If it does not, sure the ACM is correct for the processor, that it is named properly, and is in /boot.

#### [][Create /etc/defaults/grub-tboot]

Optional, but we\'ll need it later:

[FILE] **`/etc/defaults/grub-tboot`Variables understood by the grub tboot scripts**

    #GRUB_CMDLINE_TBOOT='logging=serial,memory,vga'
    #GRUB_CMDLINE_LINUX_TBOOT='intel_iommu=on'
    #GRUB_TBOOT_POLICY_DATA=''

One change is recommend making is this:

[FILE] **`/etc/defaults/grub-tboot`**

    GRUB_CMDLINE_TBOOT='pcr_map=da logging=serial,memory,vga'

The addition of `pcr_map=da` changes the way PCR are filled. PCR 17 is extended with the details , and PCR 18 is extended with the authorities. Because the authorities rarely change, PCR 18 will be more stable and easier to seal under, whereas any configuration change will change PCR 17. Additionally old (legacy) way no longer supported by Intel.

## [Setup tboot - TPM 1.2]

### [Install and start needed utilities and service]

`root `[`#`]`emerge dev-crypt/tpm-utils`

Enable tscd (OpenRC)

`root `[`#`]`rc-update add tcsd default`

`root `[`#`]`rc-service tcsd start`

Enable tcsd (systemd)

`root `[`#`]`systemctl enable --now tcsd`

Take ownership of the TPM (to set an owner password, which should really be done, leave off the -y . The SRK MUST NOT have password, or tboot will hang on resume, so -z must remain

`user `[`$`]`tpm_takeownership -y -z`

To change the owner password later:

`user `[`$`]`tpm_changeownerauth -o -z # if an owner password exists drop -z. To clear the owner password, add -r`

\

### [Setting the Launch Control Policy]

Now here be dragons. There a lot of \"magic numbers\" beyond this point. Some will typed in blindly, without knowing what they means, others looked up in a table, and other guessed

First, lets create workspace for out output files. They\'ll be quite a few.

`user `[`$`]`mkdir ~/tboot-files`

`user `[`$`]`chmod 700 ~/tboot-files`

`user `[`$`]`cd ~/tboot-files`

##### [Step 1: Measuring tboot and the tboot command line]

First, we have to take a hash of the tboot command line and the tboot binary. By, default the options `"logging=serial,memory,vga"` are passed to tboot

`user `[`$`]`lcp2_mlehash --create --alg sha1 --cmdline "logging=serial,memory,vga" /boot/tboot.gz > mle_hash`

`user `[`$`]`lcp2_crtpolelt --create --type mle --minver 17 --out mle.elt mle_hash`

This defines the first Measured Launch Element. The `--minver 17`is a requirement of tboot.

##### [][Step 2: Measure PCR (optional)]

** Warning**\
The legacy PCONF element does NOT seem to work properly as of tboot-1.10.3, it results in a TXT abort (error 0xc0111c61 - something wrong with the size of the element) Therefore, skip this element for now.

Just like objects in the TPM, boot can \"locked\" certain PCR values. If the PCR values do not match, TXT will abort. It is recommend to protect at least PCR0, to protect against BIOS corruption attacks

`user `[`$`]`grep ^PCR-00 < /sys/class/tpm/tpm0/device/pcrs | sed -e 's/^PCR-0//' -e 's/[[:space:]]//g' > pcr0.txt`

`user `[`$`]`echo "locality:0x1f" | cat - pcr0.txt > pcrs.txt`

`user `[`$`]`lcp2_crtpolelt --create --type pconf pcrs.txt --out pconf.elt`

The value for \"Locality\" was fetched from the tboot sources as the default.

`user `[`$`]`grep ^PCR-00 < /sys/class/tpm/tpm0/device/pcrs | sed -e 's/^PCR-0//' -e 's/[[:space:]]//g' > pcr0.txt`

`user `[`$`]`grep ^PCR-07 < /sys/class/tpm/tpm0/device/pcrs | sed -e 's/^PCR-0//' -e 's/[[:space:]]//g' > pcr7.txt`

`user `[`$`]`echo "locality:0x1f" | cat - pcr0.txt pcr7.txt > pcrs.txt`

`user `[`$`]`lcp2_crtpolelt --create --type pconf pcrs.txt --out pconf.elt`

##### [Step 3: Create Verified Launch Policy.]

There is where tboot comes into play. The other 4 MLE types are parsed by the ACM, now tboot gets control and processes its elements. First to create an empty verified launch policy.

`user `[`$`]`tb_polgen --create --alg sha1 --type continue vl.pol`

Note that on a production machine one of the other types should be used, but for development purposes this is fine.

Now to tell tboot about the kernel and initramfs to be verified. Remember, that the tboot grub scripts will append `intel_iommu=on noefi` to the kernel command line. Unfortunately tboot can only verify a single kernel, thus its not possible to pick from multiple kernels with a single [list.data] .

`user `[`$`]`tb_polgen --add --num 0 --pcr 19 --hash image --cmdline "$(cut -d' ' -f2- </proc/cmdline)" --image "/boot/vmlinuz-$(uname -r)" vl.pol`

`user `[`$`]`tb_polgen --add --num 1 --pcr 20 --hash image --image "/boot/initramfs-$(uname -r).img" vl.pol`

The verified launch policy needs to be wrapped inside an element:

`user `[`$`]`lcp2_crtpolelt --create --type custom --out vl.elt --uuid tboot vl.pol`

##### [Step 4: Create a TXT policy with the created elements]

The elements needs to be combined into a list:

`user `[`$`]`lcp2_crtpollist --create --listver 0x100 --out list_unsig.lst mle.elt pconf.elt vl.elt`

The `--listver 0x100`is required here for TPM 1.2. This creates an unsigned list. Signed lists are preferred, otherwise, every time the policy is updated, the NVRAM of the TPM needs to be written to with the new hash of the list. With signed lists, a hash of the key is used instead of the list itself, thus only requiring the initial write. So create a keypair:

`user `[`$`]`openssl genpkey -out tboot.priv -algorithm rsa`

`user `[`$`]`openssl rsa -in tboot.priv -pubout -out tboot.pub`

Keep these keys secure, ideally there would be a password on them and maybe they\'d be stored in HSM (Hardware Security Module), but for now, this is suitable for a development platform.

Now sign the list:

`user `[`$`]`cp list_unsig.lst list_sig.lst`

`user `[`$`]`lcp2_crtpollist --sign --sigalg rsa --hashalg sha1 --pub tboot.pub --priv tboot.priv --out list_sig.lst`

Create the objects to be passed to tboot and written to the TPM:

`user `[`$`]`lcp2_crtpol --create --alg sha1 --polver 2.2 --type list --pol list.pol --data list.data list_sig.lst`

`--polver`MUST be specified (otherwise, it spits out `Error: LCPv3 signing alg mask not supported or not specified`) but its value depends on the CPU and BIOS. Its another \"magic number\" that may require some guessing. The version was provided in the provided ChangeLog for the ACM

#### [Step 5: Write to TPM and setup Verified Launch]

2 indexes must be defined in the TPM. This only needs to be done once.

`user `[`$`]`tpm_nvdefine -s 0x8 -i 0x20000002 -p 'AUTHREAD|AUTHWRITE' # Need to double check permissions`

`user `[`$`]`tpm_nvdefine -s 0x36 -i 0x40000001 -p OWNERWRITE -y # If the owner password is set, use the -o option instead`

More magic numbers. tboot stores the last TXT error at `0x20000002`. Defining it is optional but helpful. `0x40000001`is where TXT is going to look for the Platform Owner policy list. It is required.

Once done, the policy needs to be written to the TPM. If using signed lists, this only needs to be done once (unless the key is changed)

`user `[`$`]`tpm_nvwrite -f list.pol -i 0x40000001 -z # Use -p if the owner password set`

### [Completing GRUB configuration]

Copy list.data to boot. Note that contents of this file will change any time a policy changes.

`root `[`#`]`cp list.data /boot`

Edit [/etc/defaults/grub-tboot]

[FILE] **`/etc/defaults/grub-tboot`**

    GRUB_TBOOT_POLICY_DATA='list.data'

And finally, update the grub config file

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

Reboot the computer and choose the tboot option in GRUB, then pick the kernel for verified launch. If it works, the computer should come up normally. If it fails, a *TXT Abort* will likely occur, in which case, see below.

PCRs 17-20 should be populated from tboot.

`user `[`$`]`cat /sys/class/tpm/tpm0/pcrs`

    PCR-00: DB 35 EB 43 2E 21 C0 D5 DC D7 42 D2 DE E0 BD FF 78 3D 01 2B
    PCR-01: 3A 3F 78 0F 11 A4 B4 99 69 FC AA 80 CD 6E 39 57 C3 3B 22 75
    PCR-02: 91 AB 88 5F E7 30 1A 2C 47 71 D7 2D D9 2B 94 F4 BC AF A6 7A
    PCR-03: 3A 3F 78 0F 11 A4 B4 99 69 FC AA 80 CD 6E 39 57 C3 3B 22 75
    PCR-04: 72 8C B5 8B 6F A2 66 8E 39 1A 0D B7 7C 39 7E 31 8C DF 3B DA
    PCR-05: CC 39 98 2E 6C 40 9D 51 95 36 11 66 ED 63 21 75 D7 6F 0C 05
    PCR-06: 3A 3F 78 0F 11 A4 B4 99 69 FC AA 80 CD 6E 39 57 C3 3B 22 75
    PCR-07: A8 5E 4F BA 94 69 71 06 DF C0 37 14 A1 17 B5 6F 0B 65 53 70
    PCR-08: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
    PCR-09: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
    PCR-10: 03 6E E4 CB EF F3 36 63 C5 7C 44 FD 1A 43 9E 37 9E F7 42 55
    PCR-11: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
    PCR-12: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
    PCR-13: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
    PCR-14: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
    PCR-15: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
    PCR-16: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
    PCR-17: 11 B8 57 98 01 78 D8 5D B9 0C 65 74 8F A2 3E 2C 1C 1C 52 F4
    PCR-18: 1E 10 5F 83 D9 8E D9 43 FB 67 74 96 FD 30 4D 4D 43 85 1A 07
    PCR-19: F0 D9 19 62 5A 67 7C 75 5D 5A BD 99 72 CC EA 04 AB 37 31 A7
    PCR-20: 78 C7 7C 63 78 41 F6 E6 D6 42 E1 51 AA 7D 03 87 1E 00 38 FE
    PCR-21: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
    PCR-22: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
    PCR-23: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

The exact values will vary from system to system, of course. To seal some data using the SRK against PCR18 (make sure there\'s a backup)

`user `[`$`]`echo "secret" | tpm_sealdata -p18 -z`

## [Setup tboot - TPM 2.0]

TODO (Don\'t have the hardware)

## [Troubleshooting and FAQ]

### [Diagnosing failure with txt-parse_err]

If a *TXT Abort* occurs, fear not. Start the kernel without TXT. The error will be preserved across a reboot (but not a hard poweroff). Run the following:

`root `[`#`]`txt-parse_err`

    ERRORCODE: 0xc00b1c61
    AC module error : acm_type=0x1, progress=0x06, error=0x7

The archive that the ACM was extracted from contains a list of error code, of which this partially decodes. \"Progress\" corresponds to the \"Class Code\", \"Error\" corresponds to the \"Major Code\", the \"Minor Code\" isn\'t decoded, but in this case its 0xb. That corresponds to \"Invalid list version.\" This particular example was caused by the wrong list version (0x200 instead of 0x100).

### [Reboot and hangs]

Reboot is how TXT deals with errors. See above for getting the error code. Sometimes it\'ll hang. That usually means [/boot/list.data] doesn\'t reflect the current configuration - this will often happen after a configuration change. The last steps are to run `lcp2_crtpol` and copy the resulting file into /boot.