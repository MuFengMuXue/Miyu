#  kernel-crypto-api interface

The `kernel-crypto-api` interface allows access to the [Linux kernel crypto API](https://www.kernel.org/doc/html/v4.11/crypto/index.html), which itself provides a set of cryptographic ciphers and other data transformation mechanisms.

## Developer details

**[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/)**: no

The kernel crypto API has been designed to be used by any process such that using it requires no special privileges. As this provides a kernel surface, and has a CVE history, this interface needs to be manually connected.

### Code examples

The test code can be found in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/kernel_crypto_api_test.go

The source code for the interface is in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/kernel_crypto_api.go
