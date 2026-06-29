[\<\< back to OpenVPN](https://wiki.gentoo.org/wiki/OpenVPN "OpenVPN")

The first step to setup a OpenVPN server is to create a [PKI (Public Key Infrastructure)](https://en.wikipedia.org/wiki/Public_key_infrastructure) from scratch. It consists of

-   A public master Certificate Authority (CA) certificate and a private key
-   A separate public certificate and private key pair (hereafter referred to as a certificate) for each server and each client.

We can use \'easy-rsa\' scripts to do this. Install them by running

`root `[`#`]`emerge --ask app-crypt/easy-rsa`

** Important**\
To create ***only*** a new client key, jump to [this step](#Generate_client_certificate_and_key).

## Contents

-   [[1] [Creating certificates]](#Creating_certificates)
    -   [[1.1] [Create CA certificate]](#Create_CA_certificate)
    -   [[1.2] [Generate Server Certificate Request and Key]](#Generate_Server_Certificate_Request_and_Key)
    -   [[1.3] [Sign Server Certificate Request]](#Sign_Server_Certificate_Request)
    -   [[1.4] [Generate Diffie-Hellman (DH) parameters]](#Generate_Diffie-Hellman_.28DH.29_parameters)
    -   [[1.5] [Generate client certificate and key]](#Generate_client_certificate_and_key)
    -   [[1.6] [Generate secret Hash-based Message Authentication Code (HMAC)]](#Generate_secret_Hash-based_Message_Authentication_Code_.28HMAC.29)

## [Creating certificates]

To keep creating process separate, we should copy scripts to a different place every time to do their job.

`root `[`#`]`cp -a /usr/share/easy-rsa /root/easy-rsa-example`

change directory:

`root `[`#`]`cd /root/easy-rsa-example`

`root `[`#`]`mv vars.example vars`

To ensure the consistent use of values when generating the PKI, set default values to be used by the PKI generating scripts. Edit /root/easy-rsa-example/vars and at a minimum set the

-   EASYRSA_DN \"org\"
-   EASYRSA_REQ_COUNTRY
-   EASYRSA_REQ_PROVINCE
-   EASYRSA_REQ_CITY
-   EASYRSA_REQ_ORG
-   EASYRSA_REQ_EMAIL

parameters (do not leave any of these parameters blank). Change the KEY_SIZE parameter to 2048 for the SSL/TLS to use 2048bit RSA keys for authentication.

[FILE] **`/root/easy-rsa-example/vars`**

    # Choices are:
    #   cn_only  - use just a CN value
    #   org      - use the "traditional" Country/Province/City/Org/OU/email/CN format

    set_var EASYRSA_DN      "org"

    # Organizational fields (used with 'org' mode and ignored in 'cn_only' mode.)
    # These are the default values for fields which will be placed in the
    # certificate.  Don't leave any of these fields blank, although interactively
    # you may omit any specific field by typing the "." symbol (not valid for
    # email.)

    set_var EASYRSA_REQ_COUNTRY     "US"
    set_var EASYRSA_REQ_PROVINCE    "CA"
    set_var EASYRSA_REQ_CITY        "SanFrancisco"
    set_var EASYRSA_REQ_ORG         "Fort-Funston"
    set_var EASYRSA_REQ_EMAIL       "mail@host.domain"

Delete any previously created certificates.

** Warning**\
This will delete any previously generated certificates stored in /root/easy-rsa-example/pki, including the Certificate Authority (CA) certificate.

`root `[`#`]` ./easyrsa init-pki`

### [Create CA certificate]

The option `build-ca` generates the Certificate Authority (CA) certificate.

`root `[`#`]`./easyrsa build-ca`

    Generating a 2048 bit RSA private key
    .............................+++
    ................+++
    writing new private key to 'ca.key'
    -----
    You are about to be asked to enter information that will be incorporated
    into your certificate request.
    What you are about to enter is what is called a Distinguished Name or a DN.
    There are quite a few fields but you can leave some blank
    For some fields there will be a default value,
    If you enter '.', the field will be left blank.
    -----
    Country Name (2 letter code) [US]:
    State or Province Name (full name) [CA]:
    Locality Name (eg, city) [SanFrancisco]:
    Organization Name (eg, company) [Fort-Funston]:
    Organizational Unit Name (eg, section) [changeme]:
    Common Name (eg, your name or your server's hostname) [changeme]:
    Name [changeme]:
    Email Address [mail@host.domain]:

### [Generate Server Certificate Request and Key]

The option `gen-req <server name> nopass` generates a server certificate request and key. Make sure that the server name (Common Name when running the script) is unique. Option nopass means no need to import password.

`root `[`#`]`./easyrsa gen-req example nopass`

    Generating a 2048 bit RSA private key
    .........+++
    ............................................+++
    writing new private key to 'example.key'
    -----
    You are about to be asked to enter information that will be incorporated
    into your certificate request.
    What you are about to enter is what is called a Distinguished Name or a DN.
    There are quite a few fields but you can leave some blank
    For some fields there will be a default value,
    If you enter '.', the field will be left blank.
    -----
    Country Name (2 letter code) [US]:
    State or Province Name (full name) [CA]:
    Locality Name (eg, city) [SanFrancisco]:
    Organization Name (eg, company) [Fort-Funston]:
    Organizational Unit Name (eg, section) [changeme]:
    Common Name (eg, your name or your server's hostname) [example]:
    Name [changeme]:
    Email Address [mail@host.domain]:

    Keypair and certificate request completed. Your files are:
    req: /root/easy-rsa-example/pki/reqs/example.req
    key: /root/easy-rsa-example/pki/private/example.key

### [Sign Server Certificate Request]

The option `sign-req server <server name>` signs the certificate .crt file needed by the server.

`root `[`#`]` ./easyrsa sign-req server example`

    Note: using Easy-RSA configuration from: ./vars

    You are about to sign the following certificate.
    Please check over the details shown below for accuracy. Note that this request
    has not been cryptographically verified. Please be sure it came from a trusted
    source or that you have verified the request checksum with the sender.

    Request subject, to be signed as a server certificate for 3650 days:

    subject=
        countryName               = US
        stateOrProvinceName       = CA
        localityName              = SanFrancisco
        organizationName          = Fort-Funston
        organizationalUnitName    = changeme
        commonName                = example
        emailAddress              = mail@host.domain

    Type the word 'yes' to continue, or any other input to abort.
      Confirm request details: yes
    Using configuration from /root/easy-rsa-example/openssl-1.0.cnf
    Enter pass phrase for /root/easy-rsa-example/pki/private/ca.key:
    Check that the request matches the signature
    Signature ok
    The Subject's Distinguished Name is as follows
    countryName           :PRINTABLE:'US'
    stateOrProvinceName   :ASN.1 12:'CA'
    localityName          :ASN.1 12:'SanFrancisco'
    organizationName      :ASN.1 12:'Fort-Funston'
    organizationalUnitName:ASN.1 12:'changeme'
    commonName            :ASN.1 12:'example'
    emailAddress          :IA5STRING:'mail@host.domain'
    Certificate is to be certified until Feb  5 02:32:49 2027 GMT (3650 days)

    Write out database with 1 new entries
    Data Base Updated

    Certificate created at: /root/easy-rsa-example/pki/issued/example.crt

### [][Generate Diffie-Hellman (DH) parameters]

The option `gen-dh` generates the Diffie-Hellman parameters .pem file needed by the server.

** Note**\
It would be better to generate a new one for each server, but you can use the same one if you want to.

`root `[`#`]` ./easyrsa gen-dh`

    Generating DH parameters, 2048 bit long safe prime, generator 2
    This is going to take a long time
    ...........................+...........+......................
    ................+
    ...........
    ...........+.......................++*++*

### [Generate client certificate and key]

The option `build-client-full <client name> nopass` generates a client certificate and key. Make sure that the client name (Common Name when running the script) is unique. Option nopass means there is no need to input a password.

** Note**\
Do not enter a challenge password or company name when the script prompts you for one.

** Important**\
Every time you create a new client\'s key, you would only do this step!

`root `[`#`]`./easyrsa build-client-full client1 nopass`

    Note: using Easy-RSA configuration from: ./vars
    Generating a 2048 bit RSA private key
    .................................................................+++
    ..+++
    writing new private key to '/root/easy-rsa-example/pki/private/client1.key.GIukBzmSVv'
    -----
    Using configuration from /root/easy-rsa-example/openssl-1.0.cnf
    Enter pass phrase for /root/easy-rsa-example/pki/private/ca.key:
    Check that the request matches the signature
    Signature ok
    The Subject's Distinguished Name is as follows
    countryName           :PRINTABLE:'US'
    stateOrProvinceName   :PRINTABLE:'CA'
    localityName          :PRINTABLE:'SanFrancisco'
    organizationName      :PRINTABLE:'Fort-Funston'
    organizationalUnitName:PRINTABLE:'changeme'
    commonName            :PRINTABLE:'client1'
    name                  :PRINTABLE:'changeme'
    emailAddress          :IA5STRING:'mail@host.domain'
    Certificate is to be certified until Jan 16 12:56:33 2027 GMT (3650 days)

    Write out database with 1 new entries
    Data Base Updated

### [][Generate secret Hash-based Message Authentication Code (HMAC)]

Generate a secret Hash-based Message Authentication Code (HMAC) by running

`root `[`#`]`openvpn --genkey secret /root/easy-rsa-example/pki/ta.key`

** Important**\
You would like to keep the `/root/easy-rsa-example` folder for further usage.

And now, you can go back to [setup the server configuration](https://wiki.gentoo.org/wiki/OpenVPN#Server_side "OpenVPN").

** Note**\
The option build-server-full `# ./easyrsa build-server-full <server name> nopass ` generates a server certificate and key(do the same thing as genreq and sign-req). Make sure that the Server name (Common Name when running the script) is unique. Option nopass means no need to input password. The command usage just like build-client-full.