**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Public_key_certificate "wikipedia:Public key certificate")

**Certificates**, also known as SSL certificates or TLS certificates, provide systems and users with a sound method for securely communicating with them or verifying those systems and users\' identity. They contain identification information (who or what the certificate belongs to) and a public key, and are signed by a third party called the *Certificate Authority*.

This article focuses on many details surrounding certificates on Gentoo Linux. Where needed, a slight introduction will be given to the actions or sections presented. The technical details about certificates are better served on different platforms, such as Wikipedia.

## Contents

-   [[1] [Certificate authority]](#Certificate_authority)
    -   [[1.1] [OpenSSL-compatible ca-certificates]](#OpenSSL-compatible_ca-certificates)
    -   [[1.2] [NSS]](#NSS)
    -   [[1.3] [Application-specific stores]](#Application-specific_stores)
-   [[2] [Adding trusted certificates]](#Adding_trusted_certificates)
    -   [[2.1] [Obtaining the certificate]](#Obtaining_the_certificate)
    -   [[2.2] [Including in the ca-certificates store]](#Including_in_the_ca-certificates_store)
    -   [[2.3] [Including in the NSS database]](#Including_in_the_NSS_database)
    -   [[2.4] [Including in browser stores]](#Including_in_browser_stores)
-   [[3] [Removing certificates]](#Removing_certificates)
    -   [[3.1] [Removing from ca-certificates store]](#Removing_from_ca-certificates_store)
    -   [[3.2] [Removing from NSS database files]](#Removing_from_NSS_database_files)
-   [[4] [Modifying CA trusts]](#Modifying_CA_trusts)
    -   [[4.1] [Modifying the OpenSSL-compatible ca-certificates]](#Modifying_the_OpenSSL-compatible_ca-certificates)
    -   [[4.2] [NSS-based modifications]](#NSS-based_modifications)
        -   [[4.2.1] [Manipulating the hard-coded list]](#Manipulating_the_hard-coded_list)
        -   [[4.2.2] [Modifying the NSS databases]](#Modifying_the_NSS_databases)
-   [[5] [ACME and automated certificates]](#ACME_and_automated_certificates)
    -   [[5.1] [Available ACME clients]](#Available_ACME_clients)
    -   [[5.2] [Installing and using Certbot]](#Installing_and_using_Certbot)
    -   [[5.3] [Installing and using acme.sh]](#Installing_and_using_acme.sh)
    -   [[5.4] [Integration with system certificate stores]](#Integration_with_system_certificate_stores)
    -   [[5.5] [Automated renewal]](#Automated_renewal)
-   [[6] [Debugging certificate issues]](#Debugging_certificate_issues)
    -   [[6.1] [Formats]](#Formats)
    -   [[6.2] [Fetching certificates from network services]](#Fetching_certificates_from_network_services)
    -   [[6.3] [Checking the certificate chain]](#Checking_the_certificate_chain)
-   [[7] [FAQ]](#FAQ)
    -   [[7.1] [How are new CA\'s added to Gentoo?]](#How_are_new_CA.27s_added_to_Gentoo.3F)
    -   [[7.2] [My certificate used to be recognized, but no longer is!]](#My_certificate_used_to_be_recognized.2C_but_no_longer_is.21)
    -   [[7.3] [Why is a certificate not recognized and/or marked as insecure?]](#Why_is_a_certificate_not_recognized_and.2For_marked_as_insecure.3F)
    -   [[7.4] [Can intermediate certificates be added to the truststore?]](#Can_intermediate_certificates_be_added_to_the_truststore.3F)
-   [[8] [See also]](#See_also)
-   [[9] [External resources]](#External_resources)

## [Certificate authority]

Certificate authorities (should) verify the identity of a user (or owner of a system) and, when verified, sign the certificate with their own private key. This signature is then used by others to assert that a presented certificate is valid and trustworthy. The idea here is that others trust the signature of a certificate authority, and through that trust also accept the presented certificate.

History has shown however that not all certificate authorities are equally trustworthy (take [DigiNotar](https://en.wikipedia.org/wiki/DigiNotar "wikipedia:DigiNotar") as a prime example). Also improvements in crypto-analysis show that some important parts (such as the hashing algorithm) can contain weaknesses. In 2008 for instance, it was proven that MD5 collisions can be used to create [a rogue CA certificate](http://www.win.tue.nl/hashclash/rogue-ca/). More recently, various CAs have been removed from browser trust stores due to security incidents. As such, keeping track of the trusted certificates and their current strength is advisable.

Whenever an application (including browsers) connects to systems over an [SSL/TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security "wikipedia:Transport Layer Security") connection, part of the handshake is to verify if the presented certificate is signed by a trusted certificate authority. Hence, systems need to track which CA certificates are trustworthy. The collection of trusted CA certificates is often called a *truststore*.

Managing the truststores on a Linux system is a complex task as applications can use different approaches for handling their certificate-based operations. In the subsequent few sections the most common CA certificate handling approaches are documented.

### [OpenSSL-compatible ca-certificates]

OpenSSL-compatible libraries use the [/etc/ssl/certs] directory as the (default) truststore. All trusted certificates are listed in this directory (generally through symbolic links to their actual location), together with a single [ca-certificates.crt] file which has all the trusted CA certificates listed.

** Note**\
Gentoo currently ships with [[[dev-libs/openssl-3.4.1]](https://packages.gentoo.org/packages/dev-libs/openssl-3.4.1)[]] which uses [/etc/ssl] as its default certificate directory (OPENSSLDIR).

By default, this directory is automatically managed through the [[[app-misc/ca-certificates]](https://packages.gentoo.org/packages/app-misc/ca-certificates)[]] package, which uses the CA certificates from [Mozilla\'s CA certificate store](https://www.mozilla.org/en-US/about/governance/policies/security-group/certs/) and repackages them for use with OpenSSL-based applications.

On most systems, this package will already be installed:

`root `[`#`]`emerge --ask app-misc/ca-certificates`

** Note**\
As of 2025, Gentoo ships with [[[app-misc/ca-certificates-20240203.3.98]](https://packages.gentoo.org/packages/app-misc/ca-certificates-20240203.3.98)[]] which includes approximately 148 trusted CA certificates from Mozilla\'s certificate store.

Upon installation, this package

1.  generates the [/etc/ca-certificates.conf] configuration file by listing all certificates inside [/usr/share/ca-certificates] inside the configuration file
2.  calls the [update-ca-certificates] script which reads in this configuration file and updates the [/etc/ssl/certs] directory accordingly

The [update-ca-certificates] script also checks if any admin-provided certificates are in [/usr/local/share/ca-certificates] and adds links to those certificates to the [/etc/ssl/certs] directory as well.

** Note**\
The [/usr/local/share/ca-certificates] directory may not exist by default and will need to be created if adding custom certificates.

Most users will be satisfied with the default certificate handling: it uses the CA certificate store from an upstream project that is actively pursuing the secure state of the certificates, and is automatically updated through Portage. However, administrators who want to have a more fine-grained control over which certificates are accepted for the truststore cannot update the [/etc/ca-certificates.conf] file manually.

New installations of the [[[app-misc/ca-certificates]](https://packages.gentoo.org/packages/app-misc/ca-certificates)[]] will rewrite this configuration file, and the file is explicitly marked as not governed by Portage\'s [configuration file protection](https://wiki.gentoo.org/wiki/Handbook:AMD64/Portage/Variables#Configuration_file_protection "Handbook:AMD64/Portage/Variables"):

`user `[`$`]`emerge --info | grep ca-certificate`

    CONFIG_PROTECT_MASK="/etc/ca-certificates.conf ..."

### [NSS]

Another popular library is [Mozilla\'s Network Security Services](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS) or NSS. Unlike the OpenSSL-based certificate support, NSS uses database files as the certificate store.

NSS starts off with a hard-coded list of trusted CA certificates inside the [libnssckbi.so] file, installed through the [[[dev-libs/nss]](https://packages.gentoo.org/packages/dev-libs/nss)[]] package. This list can be viewed from any of the applications using NSS capable of showing (and manipulating) the trust store, such as Chrome-compatible or Firefox-compatible browsers. However, another approach is to use the [certutil] application as provided by the [[[dev-libs/nss]](https://packages.gentoo.org/packages/dev-libs/nss)[]] package:

`user `[`$`]`ln -s /usr/lib64/libnssckbi.so $HOME/.pki/nssdb `

`user `[`$`]`certutil -L -d sql:$HOME/.pki/nssdb/ -h 'Builtin Object Token'`

    Certificate Nickname                                         Trust Attributes
                                                                 SSL,S/MIME,JAR/XPI

    Builtin Object Token:GlobalSign Root CA                      C,C,C
    Builtin Object Token:GlobalSign Root CA - R2                 C,C,C
    Builtin Object Token:Verisign Class 1 Public Primary Certification Authority - G3 ,C,
    ...

The trust attributes mentioned in the output show what trust level that attribute has and for which purpose. The [certutil] man page has some information about what each attribute means. The most important ones are:

-   `c`---Valid certificate authority
-   `C`---Trusted certificate authority (implies `c`)
-   `p`---Valid peer certificate (i.e. no need to validate if it is signed by a proper CA)
-   `P`---Trusted peer certificate (often used for self-signed certificates that need to be trusted)

The purpose of the trust attributes is for:

-   SSL---Secure communication over SSL/TLS channels
-   S/MIME---Encryption of messages and e-mail
-   JAR/XPI---Code signing

Alongside the hard-coded certificates, NSS supports a system-wide NSS databases located at [/etc/pki/nssdb], and user-specific NSS databases located at [\~/.pki/nssdb]. The system-wide NSS database can contain the additional CA certificates that should be accepted by all users as well as system applications (and daemons) running on the system, while the user-specific database is - as the name implies - for specific user accounts.

** Important**\
By default, Gentoo does not create the system-wide NSS database at [/etc/pki/nssdb]. This directory and database files must be created manually if needed (see instructions below).

** Note**\
Some applications that use the NSS library use a different certificate store than the recommended user one. Mozilla\'s own Firefox is a prime example of this.

To query the currently assigned CA certificates:

`user `[`$`]`certutil -d sql:$HOME/.pki/nssdb -L`

To list a certain certificate information in more detail, add the name:

`user `[`$`]`certutil -d sql:$HOME/.pki/nssdb -L -n "EssentialSSL CA"`

    Certificate:
        Data:
            Version: 3 (0x2)
            Serial Number:
                40:89:95:44:7e:5f:b1:19:d8:65:73:70:2f:8d:64:fc
            Signature Algorithm: PKCS #1 SHA-1 With RSA Encryption
            Issuer: "CN=COMODO Certification Authority,O=COMODO CA Limited,L=Salf
                ord,ST=Greater Manchester,C=GB"
            Validity:
                Not Before: Fri Dec 01 00:00:00 2006
                Not After : Tue Dec 31 23:59:59 2019
            Subject: "CN=EssentialSSL CA,O=COMODO CA Limited,L=Salford,ST=Greater
                 Manchester,C=GB"
    ...

### [Application-specific stores]

Some applications have their own certificate store.

## [Adding trusted certificates]

The most common operation against truststores is to add additional trusted certificates to it. Companies often have their own PKI (Public Key Infrastructure) setup which supports the internal certificate needs, and which might require the master certificate of this PKI to be trusted, or have it as an intermediate certificate deployed across the truststores in the organization. But even end users might want to add in additional trusted certificates who might not have made the \"final\" list yet as managed by Mozilla.

### [Obtaining the certificate]

First the certificate itself needs to be obtained. When an organization has its own PKI then this CA certificate can be easily provided by the responsible team, with the necessary additional precautions in place to validate that the certificate is the right one. Other CAs generally distribute their CA certificates on their websites.

End users can also obtain the certificate through the browser by reviewing the SSL/TLS connection information. For instance, with Firefox, this can be obtained through the page information, *Security* section, *View Certificate*.

Whatever the source of the certificate, it is recommended to validate the certificate itself by checking (for instance) the checksum of the certificate. Gentoo\'s infrastructure uses certificates from [DigiCert](https://www.digicert.com/), who has its CA certificates [published online](https://www.digicert.com/digicert-root-certificates.htm) together with the thumbprint information of the certificate.

For instance, the DigiCert High Assurance EV Root CA file has the following information published alongside the certificate itself:

-   *serial number*---a unique identifier for the certificate
-   *thumbprint*---an (in this case SHA1-based) checksum on the certificate

The downloaded file, which usually has a [.crt] or [.pem] suffix, can be validated through the [openssl] command.

To view certificate information (including the serial number):

`user `[`$`]`openssl x509 -in DigiCertHighAssuranceEVRootCA.crt -text`

    Certificate:
        Data:
            Version: 3 (0x2)
            Serial Number:
                02:ac:5c:26:6a:0b:40:9b:8f:0b:79:f2:ae:46:25:77
        Signature Algorithm: sha1WithRSAEncryption
            Issuer: C=US, O=DigiCert Inc, OU=www.digicert.com, CN=DigiCert High Assurance EV Root CA
            Validity
                Not Before: Nov 10 00:00:00 2006 GMT
                Not After : Nov 10 00:00:00 2031 GMT
            Subject: C=US, O=DigiCert Inc, OU=www.digicert.com, CN=DigiCert High Assurance EV Root CA
            Subject Public Key Info:
                Public Key Algorithm: rsaEncryption
    ...

To view the thumbprint:

`user `[`$`]`openssl x509 -in DigiCertHighAssuranceEVRootCA.crt -noout -sha1 -fingerprint`

    SHA1 Fingerprint=5F:B7:EE:06:33:E2:59:DB:AD:0C:4C:9A:E6:D3:8F:1A:61:C7:DC:25

### [Including in the ca-certificates store]

Once the certificate has been validated, store it in the [/usr/local/share/ca-certificates] location. You may need to create this directory first:

`root `[`#`]`mkdir -p /usr/local/share/ca-certificates`

** Note**\
Ensure that the certificate uses the [.crt] suffix as this is the only suffix checked by the [update-ca-certificates] script.

`root `[`#`]`cp DigiCertHighAssuranceEVRootCA.crt /usr/local/share/ca-certificates`

Run the [update-ca-certificates] command to update the [/etc/ssl/certs] location with the new certificate.

`root `[`#`]`update-ca-certificates`

    Updating certificates in /etc/ssl/certs/...
    1 added, 0 removed; done
    Running hooks in /etc/ca-certificates/update.d...
    done.

### [Including in the NSS database]

When applications use the NSS library and honor the [/etc/pki/nssdb] location, then the following steps can be taken to include this certificate in this system-wide NSS database.

** Important**\
Most applications that use NSS (including Firefox and Chromium) do **not** use the system-wide NSS database by default. They maintain their own certificate stores. This system-wide database is primarily useful for custom applications or specific enterprise configurations.

First, create the directory structure for the system-wide NSS database files:

`root `[`#`]`mkdir -p /etc/pki/nssdb`

Next, create a new database file set. A password will be asked to restrict editing of the database files to people who know the password. If all users on the system (and with access to the backups) are trustworthy, then this password can be kept empty.

`root `[`#`]`certutil -d sql:/etc/pki/nssdb -N`

    Enter a password which will be used to encrypt your keys.
    The password should be at least 8 characters long,
    and should contain at least one non-alphabetic character.

    Enter new password:
    Re-enter new password:

Ensure that the database files are readable by everyone:

`root `[`#`]`chmod go+r /etc/pki/nssdb/*`

** Note**\
The above instructions only apply if no system-wide NSS database file set exists yet. If one exists already, then it is vital to know the password on this database set (assuming it is password-protected of course).

With the NSS database files now available, add the certificate to the store as follows:

`root `[`#`]`certutil -d sql:/etc/pki/nssdb -A -i `*`certificateFile.crt`*` -n "`*`certificateName`*`" -t "C,,"`

The trust bits used in the above example mark the certificate as trustworthy for signing certificates used for SSL/TLS communication. The name used in the command is free to choose, but make sure to have it easily distinguished from other certificates in the store.

Similar instructions can be used to include the certificate only in the NSS database of a particular user:

`user `[`$`]`certutil -d sql:$HOME/.pki/nssdb -A -i `*`certificateFile.crt`*` -n "`*`certificateName`*`" -t "C,,"`

### [Including in browser stores]

A number of browsers, including Chromium and Firefox, do not use the system-wide CA certificate store. Most browsers have an intuitive interface to handle the certificates they manage. To add a custom certificate to Chromium (and to Chromium-based browsers), refer to [this section of the \'Chromium\' page](https://wiki.gentoo.org/wiki/Chromium#Local_certificates "Chromium"); to add a custom certificate to Firefox, refer to [this section of the \'Firefox\' page](https://wiki.gentoo.org/wiki/Firefox#Local_certificates "Firefox").

** Note**\
Firefox profiles are typically located at [\~/.mozilla/firefox/PROFILE.default-release/] where PROFILE is a random string. Use [firefox -P] to manage profiles or check [\~/.mozilla/firefox/profiles.ini] for profile locations.

Raphaël Barrois describes, on his blog, [how to get Firefox and Chromium to share the same [\~/.pki/nssdb/] location](http://blog.xelnor.net/firefox-systemcerts/).

## [Removing certificates]

Certificates that were manually added using the instructions above can be removed from the stores easily as well.

### [Removing from ca-certificates store]

To remove the certificate from the [/etc/ssl/certs] location, remove it from the [/usr/local/share/ca-certificates] location and run the [update-ca-certificates] command again.

`root `[`#`]`rm /usr/local/share/ca-certificates/`*`certificateFile.crt`*

`root `[`#`]`update-ca-certificates`

    Updating certificates in /etc/ssl/certs/...
    0 added, 1 removed; done
    Running hooks in /etc/ca-certificates/update.d...
    done.

### [Removing from NSS database files]

To remove the certificate from any NSS database, use the [certutil] command as follows. The example uses the system-wide NSS database location, but can be easily adjusted for the user-specific [\~/.pki/nssdb] locations.

`root `[`#`]`certutil -d sql:/etc/pki/nssdb -D -n "`*`certificateName`*`"`

## [Modifying CA trusts]

Although most administrators will be happy with the default CA handling, there will be situations where one wants to modify the default CA handling approaches. This could be due to - company policy requiring a fixed and company-approved list of CAs to be trusted, and nothing more - reports about trust issues with a root CA - the need or will to start off with an empty trust store and build up - requiring different trust stores per application

Whatever the reason, the next few sections will describe how to manipulate the previously discussed trust stores.

### [Modifying the OpenSSL-compatible ca-certificates]

To handle custom CA lists, a secondary CA certificates configuration file needs to be managed, and after every installation of the [[[app-misc/ca-certificates]](https://packages.gentoo.org/packages/app-misc/ca-certificates)[]] package the [ca-certificates.conf] file needs to be overwritten and [update-ca-certificates] needs to be executed again. This can be accomplished through Portage\' [[/etc/portage/env](https://wiki.gentoo.org/wiki//etc/portage/env "/etc/portage/env")] sourcing.

Assuming that the secondary CA certificates configuration file is called [/etc/custom-ca-certificates.conf]. To have this file copied over to the [ca-certificates.conf] file after every [[[app-misc/ca-certificates]](https://packages.gentoo.org/packages/app-misc/ca-certificates)[]] package installation, the following script can be used:

[FILE] **`/etc/portage/env/app-misc/ca-certificates`Overwriting the ca-certificates.conf file**

    #!/bin/bash

    # Execute this logic after the installation
    post_pkg_postinst() " ]] ; then
        echo "Redeploying custom ca-certificates.conf file."
        install -o root -g root -m 644 "$" "$" && \
        update-ca-certificates
      fi
    }

All that the administrator has to do now is to keep the [custom-ca-certificates.conf] file up to date with the certificates of the CAs he wants to trust on this system. For instance, to only trust Verisign:

[FILE] **`/etc/custom-ca-certificates.conf`Listing only Verisign\'s certificates**

    mozilla/VeriSign_Class_3_Public_Primary_Certification_Authority_-_G4.crt
    mozilla/VeriSign_Class_3_Public_Primary_Certification_Authority_-_G5.crt
    mozilla/VeriSign_Universal_Root_Certification_Authority.crt
    mozilla/Verisign_Class_1_Public_Primary_Certification_Authority_-_G3.crt
    mozilla/Verisign_Class_2_Public_Primary_Certification_Authority_-_G3.crt
    mozilla/Verisign_Class_3_Public_Primary_Certification_Authority_-_G3.crt

As was mentioned before, these entries are relative to the [/usr/share/ca-certificates] directory. Custom certificates can be added in [/usr/local/share/ca-certificates] and do not need to be listed in the [ca-certificates.conf] file for [update-ca-certificates] to take them into account.

### [NSS-based modifications]

The NSS library has three levels that might require any manipulations:

1.  the hard-coded list of trusted CAs (currently [[[dev-libs/nss-3.101.3]](https://packages.gentoo.org/packages/dev-libs/nss-3.101.3)[]] in Gentoo)
2.  the system-wide NSS databases
3.  the user- or application-specific NSS databases

#### [Manipulating the hard-coded list]

** Warning**\
Although common sense would imply that applications which use the NSS library would also consult the system-wide database, this is more exception than rule. Neither Chromium nor Firefox (or any of the derived browsers) support the system-wide database by default. Hence, the below instructions are generally ineffective on a system-wide basis, but can be altered to suit per-application specific databases.

The recommended method for manipulating the hard-coded list is to change the trust attributes for the selected certificates in the system-wide NSS database. While the certificates are still listed in the [libnssckbi.so] file, they are then no longer marked as trusted.

Link in the hard-coded list, and then modify the trust bits for the certificate that needs modifying:

`root `[`#`]`ln -s /usr/lib64/libnssckbi.so /etc/pki/nssdb `

`root `[`#`]`certutil -d sql:/etc/pki/nssdb -M -n "Builtin Object Token:`*`certificate name`*`" -t ",,"`

#### [Modifying the NSS databases]

Any manipulation to an NSS database file can be done through the [certutil] command. More fancy user interfaces are available as well, but the [certutil] commands are easy to use and to automate.

To remove a CA certificate from the store:

`user `[`$`]`certutil -d sql:$HOME/.pki/nssdb -D -n "`*`certificatename`*`"`

To add a root CA certificate to the store:

`user `[`$`]`certutil -d sql:$HOME/.pki/nssdb -A -t "C,," -n "`*`certificatename`*`" -i "`*`certificate_filename`*`"`

To add an intermediate CA certificate to the store:

`user `[`$`]`certutil -d sql:$HOME/.pki/nssdb -A -t ",," -n "`*`certificatename`*`" -i "`*`certificate_filename`*`"`

To add a self-signed certificate to the store:

`user `[`$`]`certutil -d sql:$HOME/.pki/nssdb -A -t "P,," -n "`*`certificatename`*`" -i "`*`certificate_filename`*`"`

To modify the trust attributes of a certificate:

`user `[`$`]`certutil -d sql:$HOME/.pki/nssdb -M -n "`*`certificatename`*`" -t "`*`attr1,attr2,attr3`*`"`

## [ACME and automated certificates]

ACME (Automatic Certificate Management Environment) is a protocol for automating the issuance and renewal of certificates, most notably used by [Let\'s Encrypt](https://letsencrypt.org/). While Gentoo does not include ACME clients by default, several options are available for automated certificate management.

### [Available ACME clients]

** Note**\
None of these ACME clients are installed by default on Gentoo. Choose the client that best fits your needs and install it manually.

Common ACME clients available for Gentoo include:

-   **Certbot** - The official Let\'s Encrypt client from the EFF
-   **acme.sh** - A lightweight shell script ACME client
-   **dehydrated** - A bash-based ACME client

### [Installing and using Certbot]

Certbot is available in the Gentoo repository as [[[app-crypt/certbot]](https://packages.gentoo.org/packages/app-crypt/certbot)[]]:

`root `[`#`]`emerge -a app-crypt/certbot`

[[[app-crypt/certbot-4.0.0-r2]](https://packages.gentoo.org/packages/app-crypt/certbot-4.0.0-r2)[]] includes support for various DNS providers and web servers through USE flags:

-   **certbot-apache** - Apache web server integration
-   **certbot-nginx** - Nginx web server integration
-   **certbot-dns-\*** - Various DNS providers (dnsimple, dnsmadeeasy, google, linode, ovh, route53, etc.)

To enable specific integrations:

`root `[`#`]`echo 'app-crypt/certbot certbot-nginx' >> /etc/portage/package.use`

`root `[`#`]`emerge -a app-crypt/certbot`

Check all available USE flags:

`user `[`$`]`emerge -pv app-crypt/certbot`

To obtain a certificate for a domain:

`root `[`#`]`certbot certonly --standalone -d example.com`

### [Installing and using acme.sh]

acme.sh is a lightweight alternative that can be installed manually:

`root `[`#`]`curl `[`https://get.acme.sh`](https://get.acme.sh)` | sh`

To issue a certificate:

`root `[`#`]`acme.sh --issue -d example.com --standalone`

### [Integration with system certificate stores]

ACME-obtained certificates are typically placed in dedicated directories and need to be integrated with system services:

[FILE] **`/etc/portage/env/post-acme-renewal.sh`Post-renewal hook example**

    #!/bin/bash
    # Copy Let's Encrypt certificates to system locations
    cp /etc/letsencrypt/live/example.com/fullchain.pem /etc/ssl/certs/
    cp /etc/letsencrypt/live/example.com/privkey.pem /etc/ssl/private/
    # Restart services that use the certificates
    systemctl reload nginx

### [Automated renewal]

Set up automated renewal using cron or systemd timers:

[FILE] **`/etc/cron.d/certbot`Cron entry for certificate renewal**

    0 2 * * * root certbot renew --quiet --post-hook "/path/to/post-renewal-script.sh"

For systemd-based systems:

[FILE] **`/etc/systemd/system/certbot-renewal.service`Systemd service for renewal**

    [Unit]
    Description=Certbot Renewal

    [Service]
    ExecStart=/usr/local/bin/certbot renew --quiet

[FILE] **`/etc/systemd/system/certbot-renewal.timer`Systemd timer for automatic renewal**

    [Unit]
    Description=Run certbot twice daily

    [Timer]
    OnCalendar=*-*-* 00,12:00:00
    RandomizedDelaySec=3600
    Persistent=true

    [Install]
    WantedBy=timers.target

Enable the timer:

`root `[`#`]`systemctl enable --now certbot-renewal.timer`

## [Debugging certificate issues]

** Note**\
This section is mostly for Gentoo developers to help with debugging common issues reported by users rather than a generic \"certificate problems\". That topic is much too large to reasonably tackle here, so if these tips don\'t help, please fallback to searching the internet like normal.

Certificate failures can be difficult to debug, not the least of which is due to the tools having hard-to-use interfaces. Here\'s some tips for debugging failures.

### [Formats]

Certificates come in many different file formats, often use inconsistent or incorrect file extensions, and tools might expect inputs in specific formats. Try not to assume too much based purely on the file extension. Start with a tool like `less` or `file` to try to figure out what format it\'s in.

[DER format](https://wiki.openssl.org/index.php/DER) is a binary format meant only for tools to read. It is usually possible to convert it to a [PEM format](https://wiki.openssl.org/index.php/PEM) that contains the same information, but as plain text. Some tools only accept PEM, so try converting it:

`user `[`$`]`openssl x509 -inform der -in "`*`DER file`*`" -out "`*`PEM file`*`"`

Once it\'s in the PEM format, view it:

`user `[`$`]`openssl x509 -hash -text -noout -in "`*`PEM file`*`"`

### [Fetching certificates from network services]

To see what certificates a site is presenting over the network, use OpenSSL to start a connection and dump various useful details:

`user `[`$`]`openssl s_client -showcerts -port 443 -CApath /etc/ssl/certs -host "`*`HOSTNAME`*`" </dev/null | less`

To save the certificates for further analysis, simply redirect the output, then use a typical pager.

** Note**\
When Less is given a `.pem` filename, it will automatically use OpenSSL to decode & display it, and OpenSSL will only decode the first certificate it finds (while ignoring all other lines). Using `<` bypasses that feature to view the full file contents.

`user `[`$`]`openssl s_client -showcerts -port 443 -CApath /etc/ssl/certs -host "`*`HOSTNAME`*`" </dev/null >bundle.pem`

`user `[`$`]`less bundle.pem`

`user `[`$`]`less <bundle.pem`

### [Checking the certificate chain]

** Note**\
The tools show subject (s) and issuer (i) lines with human readable entries so it\'s easy to track & correlate things. While that\'s not exactly how certificates are looked up (since anyone can spoof those fields), the examples here will assume the certificates are reasonable (i.e. not malicious) for the sake of brevity.

OpenSSL\'s `s_client` command will display the certificate chain. Look at example.com:

`user `[`$`]`openssl s_client -showcerts -port 443 -CApath /etc/ssl/certs -host example.com </dev/null`

    …
    Certificate chain
     0 s:C = US, ST = California, L = Los Angeles, O = Internet Corporation for Assigned Names and Numbers, CN = www.example.org
       i:C = US, O = DigiCert Inc, CN = DigiCert TLS RSA SHA256 2020 CA1
     1 s:C = US, O = DigiCert Inc, CN = DigiCert TLS RSA SHA256 2020 CA1
       i:C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert Global Root CA
     2 s:C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert Global Root CA
       i:C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert Global Root CA
    …

The first certificate \[subject\] `s:C = US, ST = California, L = Los Angeles, O = Internet Corporation for Assigned Names and Numbers, CN = www.example.org` is the example.com server. It\'s signed by the intermediate certificate \[issuer\] `C = US, O = DigiCert Inc, CN = DigiCert TLS RSA SHA256 2020 CA1` which is signed by the root certificate `C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert Global Root CA`. The root certificate then signs itself, and while self-signed certificates are normally not accepted, since it\'s in the truststore, it\'s trusted to do that.

OpenSSL\'s `verify` command can verify certificates manually, but it too only operates on the first certificate found in the file. Extract the individual certificates out and double check they extracted correctly:

`user `[`$`]`sed -n '/^ 0/,/-----END CERTIFICATE-----/p' bundle.pem > server.pem`

`user `[`$`]`openssl x509 -hash -text -noout -in server.pem | grep -E -e '(Issuer|Subject):'`

    Issuer: C = US, O = DigiCert Inc, CN = DigiCert TLS RSA SHA256 2020 CA1
    Subject: C = US, ST = California, L = Los Angeles, O = Internet Corporation for Assigned Names and Numbers, CN = www.example.org

`user `[`$`]`sed -n '/^ 1/,/-----END CERTIFICATE-----/p' bundle.pem > intermediate.pem`

`user `[`$`]`openssl x509 -hash -text -noout -in intermediate.pem | grep -E -e '(Issuer|Subject):'`

    Issuer: C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert Global Root CA
    Subject: C = US, O = DigiCert Inc, CN = DigiCert TLS RSA SHA256 2020 CA1

`user `[`$`]`sed -n '/^ 2/,/-----END CERTIFICATE-----/p' bundle.pem > root.pem`

`user `[`$`]`openssl x509 -hash -text -noout -in root.pem | grep -E -e '(Issuer|Subject):'`

    Issuer: C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert Global Root CA
    Subject: C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert Global Root CA

Finally the certificates can be verified. Walk back from the root certificate which should be accepted because it\'s in the truststore:

`user `[`$`]`openssl verify -CApath /etc/ssl/certs/ root.pem`

    root.pem: OK

Then the intermediate certificate should be accepted because its issuer is in the truststore:

`user `[`$`]`openssl verify -CApath /etc/ssl/certs/ intermediate.pem`

    intermediate.pem: OK

Then the server certificate should fail! This is because the verify command only checks the truststore, and while the root certificate is in there, the intermediate certificate is not.

`user `[`$`]`openssl verify -CApath /etc/ssl/certs/ server.pem`

    C = US, ST = California, L = Los Angeles, O = Internet Corporation for Assigned Names and Numbers, CN = www.example.org
    error 20 at 0 depth lookup: unable to get local issuer certificate
    error server.pem: verification failed

To verify the server certificate, provide the intermediate certificate at the same time. OpenSSL will take care of walking the chain of trust. Be sure to use `-untrusted` so the certificate isn\'t inadvertently added to the truststore.

`user `[`$`]`openssl verify -CApath /etc/ssl/certs/ -untrusted intermediate.pem server.pem`

    server.pem: OK

## [FAQ]

### [][How are new CA\'s added to Gentoo?]

Gentoo does not accept any custom certificate authorities. The project does not have the time, resources, or expertise to properly vet certificate authorities which is why we utilize NSS for its truststore.

To add a new root CA to the default Gentoo install, please go through [Mozilla\'s CA Certificate Program](https://wiki.mozilla.org/CA). Once it\'s accepted by Mozilla, updating Gentoo is pretty easy.

### [][My certificate used to be recognized, but no longer is!]

If a certificate used to work but no longer does, the root certificate might have been removed from the truststore because it had problems (e.g. was insecure). See [Mozilla\'s list of removed CA\'s](https://wiki.mozilla.org/CA/Removed_Certificates) for more information.

This could also explain why a website used to work but is now marked as insecure.

### [][Why is a certificate not recognized and/or marked as insecure?]

All certificates must be trusted by an entry in the truststore, either directly by a root certificate in the truststore (which is possible, but a bit uncommon), or indirectly by intermediate certificates that themselves chain back to a trusted root certificate. The [Wikipedia Chain of trust article](https://en.wikipedia.org/wiki/Chain_of_trust) goes into a lot more detail, as does [Let's Encrypt Chain of Trust article](https://letsencrypt.org/certificates/).

Usually when a certificate is unable to be verified, it\'s because an intermediate certificate is missing. For example, a service presented the last certificate in the chain (its own) and expected either to have the intermediate certificate already, or be able to fetch it from somewhere. Both of these assumptions are usually incorrect and the service should actually be providing a certificate bundle instead: not only their own certificate, but the intermediate certificates back to the relevant root certificate that is in the truststore. This way the client is able to follow the trust chain back to its own truststore.

If a certificate chain ends in a root certificate that is not in Gentoo\'s default truststore, see the previous FAQs.

### [][Can intermediate certificates be added to the truststore?]

See the previous FAQ about adding a new CA to Gentoo to start with. Building off of that answer, intermediate certificates are typically not included in the truststore. Maintaining the existing list of root certificates requires a lot of effort & toil and there\'s only \<150 of those. There are orders of magnitude more intermediate certificates out there (thousands, if not more) that individual certificate authorities create & destroy as makes sense for their needs & structure. Requiring review by Mozilla, and then updates rolling out to distros & users, adds a large amount of toil for no gain.

This is the status quo for all operating systems, browsers, distros, and system builders. Gentoo alone including an arbitrary intermediate certificate won\'t actually help any users on all those other systems, and servers would still have to provide them to keep everyone working.

## [See also]

The following articles on Gentoo\'s wiki are related to certificates as well.

-   [Local certificates](https://wiki.gentoo.org/wiki/Local_certificates "Local certificates") --- focuses on many details surrounding certificates on Gentoo Linux.
-   [SSL Certificates (Complete Virtual Mail Server)](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/SSL_Certificates "Complete Virtual Mail Server/SSL Certificates")---Creating private keys and associated certificates for use in a virtual mail server setup
-   [Certificates/Become your own CA](https://wiki.gentoo.org/wiki/Certificates/Become_your_own_CA "Certificates/Become your own CA")

## [External resources]

-   [Certificate Authorities (CA) in Google Chrome / Chromium and Firefox on Linux](https://rolandschnabel.de/blog/?p=276) on [Roland\'s Blog](https://rolandschnabel.de/blog/)
-   [Linux Cert Management](https://chromium.googlesource.com/chromium/src/+/HEAD/docs/linux/cert_management.md) in Chromium\'s developer documentation
-   [Certificate Authority FAQ](https://wiki.mozilla.org/CA:FAQ) on the Mozilla wiki
-   [Comparison of SSL/TSL libraries](https://curl.haxx.se/docs/ssl-compared.html) that libcurl can be built to use.