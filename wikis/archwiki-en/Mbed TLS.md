# Mbed TLS

According to Wikipedia:
:mbed TLS (previously PolarSSL) is an implementation of the TLS and SSL protocols and the respective cryptographic algorithms and support code required. It is dual-licensed with the Apache License version 2.0 (with GPLv2 also available). Stated on the website is that mbed TLS aims to be "easy to understand, use, integrate and expand".

## Installation
Install the  package.

## Usage
The command names start with "mbedtls_", for usage examples see the Knowledge Base.

## Generate an RSA private key
 $ mbedtls_gen_key rsa_keysize=keysize filename=filename

## Generate a certificate signing request
 $ mbedtls_cert_req filename=private_key subject_name=subject output_file=filename

Relevant how-to

## Generate a self-signed certificate
 $ mbedtls_cert_write selfsign=1 issuer_key=private_key issuer_name=subject not_before=YYYYMMDDHHMMSS not_after=YYYYMMDDHHMMSS is_ca=1 max_pathlen=0 output_file=file

Relevant how-to
