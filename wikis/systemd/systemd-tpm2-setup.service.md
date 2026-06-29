## Name

systemd-tpm2-setup.service, systemd-tpm2-setup-early.service, systemd-tpm2-setup — Set up the TPM2 Storage Root Key (SRK) and initialize NvPCRs at boot

## Synopsis

`systemd-tpm2-setup.service`

`/usr/lib/systemd/systemd-tpm2-setup`

## Description

`systemd-tpm2-setup.service` and `systemd-tpm2-setup-early.service` are services that generate the Storage Root Key (SRK) if it has not been generated yet, and stores it in the TPM. If NvPCRs (additional PCR registers in TPM NV Indexes) are defined, these are initialized with the anchoring secret.

The services will store the public key of the SRK key pair in a PEM file in `/run/systemd/tpm2-srk-public-key.pem` and `/var/lib/systemd/tpm2-srk-public-key.pem`. They will also store it in TPM2B_PUBLIC format in `/run/systemd/tpm2-srk-public-key.tpm2_public` and `/var/lib/systemd/tpm2-srk-public-key.tpm2b_public`.

`systemd-tpm2-setup-early.service` runs very early at boot (possibly in the initrd), and writes the SRK public key to `/run/systemd/tpm2-srk-public-key.*` (as `/var/` is generally not accessible this early yet), while `systemd-tpm2-setup.service` runs during a later boot phase and saves the public key to `/var/lib/systemd/tpm2-srk-public-key.*`.

## Files

`/run/systemd/tpm2-srk-public-key.pem`, `/run/systemd/tpm2-srk-public-key.tpm2b_public`  
The SRK public key in PEM and TPM2B_PUBLIC format, written during early boot.

Added in version 255.

`/var/lib/systemd/tpm2-srk-public-key.pem`, `/var/lib/systemd/tpm2-srk-public-key.tpm2_public`  
The SRK public key in PEM and TPM2B_PUBLIC format, written during later boot (once `/var/` is available).

Added in version 255.

`/usr/lib/nvpcr/*.nvpcr`  
Definition files for NvPCRs.

Added in version 259.

`/run/credentials/@encrypted/nvpcr-anchor.*`  
Encrypted NvPCR anchor secret, received into the system via system credentials.

Added in version 259.

`$BOOT/loader/credentials/nvpcr-anchor.*.cred`  
Encrypted NvPCR anchor secret, to be picked up by the kernel loader stub, i.e. systemd-stub(7).

Added in version 259.

## See Also

systemd(1)
