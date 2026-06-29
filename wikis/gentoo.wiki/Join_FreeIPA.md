**Resources**

[[]][Home](https://www.freeipa.org/page/Main_Page)

[[]][Official documentation](https://www.freeipa.org/page/Documentation)

Gentoo is not a supported distribution of the FreeIPA server or client tools, but its possible to manually provision a Gentoo system. Setting up the server will not be discussed here.

** Note**\
For the examples below, the following will presumed

-   Domain is **internal.example.com**
-   Realm is **INTERNAL.EXAMPLE.COM**
-   FreeIPA server is **ipa1.internal.example.com**
-   Client hostname is **gentoo**, and its FQDN is **gentoo.internal.example.com**

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
    -   [[1.1] [Check hostname]](#Check_hostname)
        -   [[1.1.1] [OpenRC]](#OpenRC)
        -   [[1.1.2] [systemd]](#systemd)
    -   [[1.2] [Synchronize time]](#Synchronize_time)
        -   [[1.2.1] [OpenRC]](#OpenRC_2)
        -   [[1.2.2] [systemd]](#systemd_2)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
    -   [[2.2] [IPA Server part]](#IPA_Server_part)
    -   [[2.3] [Emerge]](#Emerge)
    -   [[2.4] [Get the CA certificate]](#Get_the_CA_certificate)
-   [[3] [Essential Configuration]](#Essential_Configuration)
    -   [[3.1] [Kerberos]](#Kerberos)
    -   [[3.2] [sssd]](#sssd)
    -   [[3.3] [PAM]](#PAM)
    -   [[3.4] [NSS]](#NSS)
-   [[4] [Starting sssd service]](#Starting_sssd_service)
    -   [[4.1] [OpenRC]](#OpenRC_3)
    -   [[4.2] [systemd]](#systemd_3)
-   [[5] [Ancillary services]](#Ancillary_services)
    -   [[5.1] [ssh]](#ssh)
    -   [[5.2] [ssl]](#ssl)
        -   [[5.2.1] [OpenSSL and gnutls]](#OpenSSL_and_gnutls)
        -   [[5.2.2] [NSS]](#NSS_2)
    -   [[5.3] [LDAP]](#LDAP)
-   [[6] [Usage]](#Usage)
-   [[7] [Troubleshooting]](#Troubleshooting)
-   [[8] [External resources]](#External_resources)

## [Prerequisites]

### [Check hostname]

The hostname must be set up on the client and match the hostname (not FQDN) used for enrollment.

#### [OpenRC]

The DNS hostname (NOT the FQDN) must in [/etc/hostname]

`root `[`#`]`printf "gentoo" > /etc/hostname`

#### [systemd]

Use [hostnamectl] to set static hostname (NOT the FQDN)

`root `[`#`]`hostnamectl hostname --static "gentoo"`

### [Synchronize time]

** Note**\
Virtualized hosts do not require time synchronization. This section should be skipped for virtual machines.

By default, FreeIPA does NOT provide a time server for clients. FreeIPA\'s preferred ntp client is [[[net-misc/chrony]](https://packages.gentoo.org/packages/net-misc/chrony)[]]. Any NTP client should work.

#### [OpenRC]

Install an NTP client. The default configuration should be fine. Don\'t forget to enable and start the service in OpenRC!

#### [systemd]

Use [timedatectl] to enable NTP:

`root `[`#`]`timedatectl set-ntp true`

## [Installation]

### [USE flags]

The following per-package USE flags are required:

[FILE] **`/etc/portage/package.use/sssd.conf`**

    sys-auth/sssd samba
    dev-libs/cyrus-sasl kerberos
    net-dns/bind gssapi
    net-nds/openldap experimental sasl
    net-fs/samba winbind

The following per-package USE flags are recommended:

[FILE] **`/etc/portage/package.use/sssd.conf (Excerpt)`**

    net-misc/openssh kerberos
    sys-auth/pambase sssd
    app-admin/sudo sssd

### [IPA Server part]

The provisioning for the new **gentoo** client must be done the server. The web ui can create the host entry, but the command line **on the FreeIPA server** must be used to create the Kerberos keytab.

`root `[`#`]`kinit admin `

`root `[`#`]`ipa host-add --force gentoo.internal.example.com `

`root `[`#`]`ipa-getkeytab -s ipa1.internal.example.com -p host/gentoo.internal.example.com -k /tmp/gentoo.keytab`

Copy the keytab file to the client\'s [/etc/krb5.keytab]. This may be difficult. If the client has a local user and has an ssh server, the FreeIPA server admin can \"push\" the keytab to the client with scp. If the client has no local users, because OpenSSH doesn\'t permit password authentication for root by default, this won\'t work. The root user on the FreeIPA server will need to choose user with ssh access to FreeIPA server (usually \"admin\"), copy the ticket to somewhere that user can access (like their home directory) and *chown* the keytab so that user can access the file. Then, on the client, \"pull\" the keytab from the server with scp.

### [Emerge]

`root `[`#`]`emerge --ask sys-auth/sssd`

`root `[`#`]`emerge --ask -auvDU @world`

### [Get the CA certificate]

The CA certificate is be needed for *sssd*, and may be required for other applications too (like Firefox)

`root `[`#`]`mkdir /etc/ipa `

`root `[`#`]`wget --no-check-certificate -O /etc/ipa/ca.crt `[`https://ipa1.internal.example.com/ipa/config/ca.crt`](https://ipa1.internal.example.com/ipa/config/ca.crt)

## [Essential Configuration]

The 4 most important things that need to be configured are Kerberos, SSSD, PAM and NSS. Because the configuration between hosts is same or similar, once the first host is configured, those files can be copied to a distribution point (webserver, thumb drive), then copied to the other machines, and edited.

### [Kerberos]

All the Kerberos file are identical on every host. First, a few directories need to be created

`root `[`#`]`mkdir /etc/krb5.conf.d `

`root `[`#`]`mkdir /var/lib/ipa-client`

On the client, use the **scp** utility to copy 2 files (these are the same for every host, and be added to the configuration ditrobution)

`root `[`#`]`scp -r admin@ipa1.internal.example.com:/var/lib/ipa-client/pki /var/lib/ipa-client`

The server\'s Kerberos configuration is different from the client, so it cannot be copied over. Either enroll on a client (like a Fedora Workstation VM) that supports *ipa-client-install* and copy the [/etc/krb5.conf] file and [/etc/krb5.conf.d] directory; or use the ones below:

[FILE] **`/etc/krb5.conf`**

    includedir /etc/krb5.conf.d/
    [libdefaults]
      default_realm = INTERNAL.EXAMPLE.COM
      dns_lookup_realm = true
      rdns = false
      dns_canonicalize_hostname = false
      dns_lookup_kdc = true
      ticket_lifetime = 24h
      forwardable = true
      udp_preference_limit = 0
      default_ccache_name = KEYRING:persistent:%

[FILE] **`/etc/krb5.conf.d/enable_sssd_conf_dir`**

    includedir /var/lib/sss/pubconf/krb5.include.d/

[FILE] **`/etc/krb5.conf.d/freeipa`**

    [libdefaults]
        spake_preauth_groups = edwards25519

[FILE] **`/etc/krb5.conf.d/freeipa-realm`**

    [realms]
     INTERNAL.EXAMPLE.COM =

    [domain_realm]
      .internal.example.com = INTERNAL.EXAMPLE.COM
      internal.example.com = INTERNAL.EXAMPLE.COM

The next file is only effective if [[[sys-auth/sssd]](https://packages.gentoo.org/packages/sys-auth/sssd)[]] was compiled with the [[[openid]](https://packages.gentoo.org/useflags/openid)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag

[FILE] **`/etc/krb5.conf.d/sssd_enable_idp`**

    [plugins]
     clpreauth =

     kdcpreauth =
    }

The next file is only effective if [[[sys-auth/sssd]](https://packages.gentoo.org/packages/sys-auth/sssd)[]] was compiled with the [[[passkey]](https://packages.gentoo.org/useflags/passkey)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag

[FILE] **`/etc/krb5.conf.d/sssd_enable_passkey`**

    [plugins]
     clpreauth =

     kdcpreauth =

### [sssd]

Note the **ipa_hostname** and **dyndns_iface** need to be customized for each client in the file below.

[FILE] **`/etc/sssd/sssd.conf`**

    [domain/internal.example.com]
    id_provider = ipa
    ipa_server = _srv_, ipa1.internal.example.com
    ipa_domain = internal.example.com
    ipa_hostname = gentoo.internal.example.com
    auth_provider = ipa
    chpass_provider = ipa
    access_provider = simple
    cache_credentials = True
    ldap_tls_cacert = /etc/ipa/ca.crt
    dyndns_update = True
    dyndns_iface = enp1s0
    krb5_store_password_if_offline = True
    fallback_homedir = /home/%u@%d
    default_shell = /bin/bash
    use_fully_qualified_names = False
    realmd_tags =

    [sssd]
    services = nss, pam, ssh, sudo
    domains = internal.example.com

    [nss]
    homedir_substring = /home

    [pam]

    [sudo]

    [autofs]

    [ssh]

    [pac]

    [ifp]

    [session_recording]

### [PAM]

If [[[sssd]](https://packages.gentoo.org/useflags/sssd)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] is set on [[[sys-auth/pambase]](https://packages.gentoo.org/packages/sys-auth/pambase)[]], PAM will be automatically configured for sssd. However, it does not create home directories on login. IF that is desired, the pam_mkhomedir module may be added to the appropriate spot in the PAM configuration (SELinux users: Use [[[app-misc/oddjob]](https://packages.gentoo.org/packages/app-misc/oddjob)[]] instead). PAM is very fragile, manual configuration of PAM is not recommended.

### [NSS]

Each host [/etc/nsswitch.conf] will look different, so the excerpt below will need to be adapted to the host, for example, \"systemd\" won\'t be present on non-systemd systems. Any nonpresent entries, like \"sudoers\" should be added.

[FILE] **`/etc/nsswitch.conf (excerpt)`**

    passwd:     files sss systemd
    group:      files [SUCCESS=merge] sss [SUCCESS=merge] systemd
    services:   files sss
    netgroup:   files sss
    sudoers:    files sss
    automount:  files sss

## [Starting sssd service]

### [OpenRC]

`root `[`#`]`rc-update add sssd default `

`root `[`#`]`rc-service sssd start`

### [systemd]

`root `[`#`]`systemctl enable --now sssd`

## [Ancillary services]

### [ssh]

[FILE] **`/etc/ssh/ssh_config.d/04-ipa.conf`**

    Match exec true
        KnownHostsCommand /usr/bin/sss_ssh_knownhosts %H

[FILE] **`/etc/ssh/sshd_config.d/04-ipa.conf`**

    PubkeyAuthentication yes
    KerberosAuthentication no
    GSSAPIAuthentication yes
    UsePAM yes
    ChallengeResponseAuthentication yes
    AuthorizedKeysCommand /usr/bin/sss_ssh_authorizedkeys
    AuthorizedKeysCommandUser nobody

### [ssl]

** Warning**\
Firefox, Chrome and their derivatives ignore the system credential store. Browsers must be configured separately

#### [OpenSSL and gnutls]

`root `[`#`]`cp /etc/ipa/ca.crt /usr/local/share/ca-certificates/INTERNAL.EXAMPLE.COM_IPA_CA.crt `

`root `[`#`]`update-ca-certififcates`

#### [NSS]

This assumes you have a (password protected) NSS database already created.

`root `[`#`]`ertutil -d sql:/etc/ipa/nssdb -A -n 'INTERNAL.EXAMPLE.COM IPA CA' -t 'CT,C,C' -a -f /etc/ipa/nssdb/pwdfile.txt < /etc/ipa/ca.crt`

### [LDAP]

[FILE] **`/etc/openldap/ldap.conf`**

    #
    # LDAP Defaults
    #

    # See ldap.conf(5) for details
    # This file should be world readable but not world writable.

    #BASE   dc=example,dc=com
    #URI    ldap://ldap.example.com ldap://ldap-master.example.com:666

    #SIZELIMIT  12
    #TIMELIMIT  15
    #DEREF      never

    # When no CA certificates are specified the Shared System Certificates
    # are in use. In order to have these available along with the ones specified
    # by TLS_CACERTDIR one has to include them explicitly:
    #TLS_CACERT /etc/pki/tls/cert.pem

    # System-wide Crypto Policies provide up to date cipher suite which should
    # be used unless one needs a finer grinded selection of ciphers. Hence, the
    # PROFILE=SYSTEM value represents the default behavior which is in place
    # when no explicit setting is used. (see openssl-ciphers(1) for more info)
    #TLS_CIPHER_SUITE PROFILE=SYSTEM

    # Turning this off breaks GSSAPI used with krb5 when rdns = false
    SASL_NOCANON    on

    URI ldaps://ipa1.internal.example.com
    BASE dc=internal,dc=example,dc=com
    SASL_MECH GSSAPI

## [Usage]

** Warning**\
If the host has no local users other than root, and root does not have a password, keep a root shell open and test other user sessions on another virtual terminal!

** Note**\
Any local users will \"shadow\" ones of the same name in the FreeIPA directory. Their local usernames/groups must first be removed with **userdel** and **groupdel**. Then, the user and group of their home directory will need to corrected. The [chown username: /home/username] command will fix it.

`root `[`#`]`kinit username`

Password for username@INTERNAL.EXAMPLE.COM:

This should aquire a ticket for *username*

`root `[`#`]`id username`

uid=1000000004(username) gid=1000000004(username) groups=1000000004(username)

Will print membership of *username* in both FreeIPA and local groups.

`root `[`#`]`sudo -ll -U username`

Will print sudo rules (if any) for *username*.

## [Troubleshooting]

As root, the **sssctl** command can be used to temporaily increase debugging. The logging may be increased on one subsystem or globally in sssd,

`root `[`#`]`sssctl debug-level --pam 0x00F0 # Additonally log pam_sss minor failures `

`root `[`#`]`sssctl debug-level 0x0070 # default level`

## [External resources]

-   [\[1\]](https://www.freeipa.org/page/Main_Page) FreeIPA project