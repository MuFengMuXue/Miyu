# Trusted Platform Module/1.2

TPM 1.2 uses the "TrouSerS" TSS (TCG software stack) by IBM, which is packaged as  (tcsd) and  (userspace). All software access the TPM through the tcsd daemon.

## Drivers
TPM drivers are natively supported in modern kernels, but might need to be loaded:

 # modprobe tpm

Depending on your chipset, you might also need to load one of the following:

 # modprobe -a tpm_{atmel,infineon,nsc,tis,crb}

## Usage
TPM 1.2 is managed by , a userspace daemon that manages Trusted Computing resources and should be (according to the TSS spec) the only portal to the TPM device driver.  is part of the  package, which was created and released by IBM, and can be configured via .

To start tcsd and watch the output, run:

 # tcsd -f

or simply start and enable .

Once  is running you might also want to install  which provides many of the command line tools for managing the TPM.

Some other tools of interest:

*
*

## Basics
Start off by getting basic version info:

 $ tpm_version

and running a selftest:

## Securing SSH keys
There are several methods to use TPM to secure keys, but here we show a simple method based on .

First, create a new directory and generate the key:

 $ mkdir ~/.simple-tpm-pk11
 $ stpm-keygen -o ~/.simple-tpm-pk11/my.key

Point the configuration to the key:

Now configure SSH to use the right PKCS11 provider:

It is now possible to generate keys with the PKCS11 provider:

 $ ssh-keygen -D /usr/lib/libsimple-tpm-pk11.so

## Troubleshooting
## tcsd.service failed to start
After installing , the  service may not start correctly due to permission issues.It is possible to fix this either by rebooting or by triggering the udev rule that is included in the  package:

 # udevadm control --reload-rules
 # udevadm trigger
