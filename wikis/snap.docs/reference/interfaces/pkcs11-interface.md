#  pkcs11 interface

The `pkcs11` interface enables the [PKCS#11 Cryptographic Token Interface Standard](https://thalesdocs.com/gphsm/ptk/5.9/docs/Content/PTK-C_Program/intro_PKCS11.htm) to be used with access to exposed tokens.

## Developer details

**[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/)**: no

**[Super-privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/)**: yes

### Code examples

The test code can be found in the snapd repository:
https://github.com/canonical/snapd/blob/master/interfaces/builtin/pkcs11_test.go

The source code for the interface is in the snapd repository:

https://github.com/canonical/snapd/blob/master/interfaces/builtin/pkcs11.go
