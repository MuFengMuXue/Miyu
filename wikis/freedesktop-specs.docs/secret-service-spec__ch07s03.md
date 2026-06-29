## 7.3 Algorithm: dh-ietf1024-sha256-aes128-cbc-pkcs7

**Session algorithm:** *dh-ietf1024-sha256-aes128-cbc-pkcs7*

**[Session input](org.freedesktop.Secret.Service.md#org.freedesktop.Secret.Service.OpenSession "org.freedesktop.Secret.Service.OpenSession"):** Client DH pub key as an array of bytes

**[Session output](org.freedesktop.Secret.Service.md#org.freedesktop.Secret.Service.OpenSession "org.freedesktop.Secret.Service.OpenSession"):** Service DH pub key as an array of bytes

**[`Secret` parameter](types.md#type-Secret "14.1.1.  Secret"):** 16 byte AES initialization vector

DH key agreement \[[rfc2631](bi01.md#id-1.4.4)\] is used to create a secret key using 1024 bit parameters of the standard IETF 'Second Oakley Group' \[[rfc2409](bi01.md#id-1.4.3)\]. The secret key is then digested into a 128-bit key appropriate for AES. This is done using HKDF \[[rfc5869](bi01.md#id-1.4.5)\] with NULL salt and empty info, using the SHA-2 256 hash algorithm \[[fips-180-3.2008](bi01.md#id-1.4.6)\]. The secrets are encrypted using AES \[[fips-197.2001](bi01.md#id-1.4.7)\] in cipher block chaining mode with pkcs7 style padding \[[rfc2315](bi01.md#id-1.4.2)\].

The public keys are transferred as an array of bytes representing an unsigned integer of arbitrary size, most-significant byte first (e.g., the integer 32768 is represented as the 2-byte string 0x80 0x00)
