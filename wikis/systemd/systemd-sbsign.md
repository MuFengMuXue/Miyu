## Name

systemd-sbsign — Sign PE binaries for EFI Secure Boot

## Synopsis

`systemd-sbsign` \[OPTIONS...\] {COMMAND}

## Description

**systemd-sbsign** can be used to sign PE binaries for EFI Secure Boot.

## Commands

`sign`  
Signs the given PE binary for EFI Secure Boot. Takes a path to a PE binary as its argument. If the PE binary already has a certificate table, the new signature will be added to it. Otherwise, a new certificate table will be created. The signed PE binary will be written to the path specified with `--output=`.

Added in version 257.

## Options

The following options are understood:

`--output=`*`PATH`*  
Specifies the path where to write the signed PE binary or the data to be signed offline when using the `--prepare-offline-signing` option.

Added in version 257.

`--private-key=`*`PATH/URI`*, `--private-key-source=`*`TYPE`*`[:`*`NAME`*`]`, `--certificate=`*`PATH`*, `--certificate-source=`*`TYPE`*`[:`*`NAME`*`]`  
Set the Secure Boot private key and certificate for use with the **sign** verb. The `--certificate=` option takes a path to a PEM-encoded X.509 certificate or a URI that's passed to the OpenSSL provider configured with `--certificate-source`. The `--certificate-source` option takes one of "`file`" or "`provider`", with the latter being followed by a specific provider identifier, separated with a colon, e.g. "`provider:pkcs11`". The `--private-key=` option takes a path or a URI that will be passed to the OpenSSL engine or provider, as specified by `--private-key-source=` as a "`type:name`" tuple, such as "`engine:pkcs11`". The specified OpenSSL signing engine or provider will be used to sign the PE binary.

Added in version 257.

`--prepare-offline-signing`  
When this option is specified, the **sign** command writes the data that should be signed to the path specified with `--output=` instead of writing the signed PE binary. This data can then be signed out of band after which the signature can be attached to the PE binary using the `--signed-data=` and `--signed-data-signature=` options.

Added in version 258.

`--signed-data=`*`PATH`*, `--signed-data-signature=`*`PATH`*  
Configure the signed data (as written to the path specified with `--output=` when using the `--prepare-offline-signing` option) and corresponding signature for the **sign** command.

Added in version 258.

`-h`, `--help`  
Print a short help text and exit.

`--version`  
Print a short version string and exit.

## Examples

**Example 1. Offline EFI secure boot signing of a PE binary**

The following does offline secure boot signing of systemd-boot:

``` programlisting
SD_BOOT="$(find /usr/lib/systemd/boot/efi/ -name "systemd-boot*.efi" | head -n1)"
# Extract the data that should be signed offline.
/usr/lib/systemd/systemd-sbsign \
    sign \
    --certificate=secure-boot-certificate.pem \
    --output=signed-data.bin \
    --prepare-offline-signing \
    "$SD_BOOT"
# Sign the data out-of-band. This step usually happens out-of-band on a separate system.
openssl dgst -sha256 -sign secure-boot-private-key.pem -out signed-data.sig signed-data.bin
# Attach the signed data and its signature to the systemd-boot PE binary.
/usr/lib/systemd/systemd-sbsign \
    sign \
    --certificate=secure-boot-certificate.pem \
    --output="$SD_BOOT.signed" \
    --signed-data=signed-data.bin \
    --signed-data-signature=signed-data.sig \
    "$SD_BOOT"
```

  

## See Also

bootctl(1)
