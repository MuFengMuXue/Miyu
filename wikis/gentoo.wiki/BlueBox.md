**Article status**

[[]]This article needs wikification.

[[]]This article has some todo items:\

-   [FreeSWITCH](#FreeSWITCH)
-   [Configuring a Dialplan](#Configuring_a_dialplan_.28TODO.29)

[BlueBox](https://www.2600hz.org/) is a web based PHP configuration and management GUI for [FreeSWITCH](https://freeswitch.com/) and [Asterisk](https://wiki.gentoo.org/wiki/Asterisk "Asterisk") switching libraries. It supports multi-tenancy, skinning, and is completely open-source.

BlueBox can be used with database and file replication to scale up to thousands of registered devices and simultaneous phone calls. It can operate in the cloud or on the premise.

It originally developed from [FreePBXv3](https://www.freepbx.org/).

The following two blogs on VOIP PBX useful may be useful:

-   [freeSWITCH](http://michigantelephone.wordpress.com/category/freeswitch/page/2/) \-\-- which covers Asterisk+FreePBX, FreeSWITCH+BlueBox and FreeSWITCH+FusionPBX
-   [FreeSWITCH Cookbook](http://michigantelephone.wordpress.com/category/freeswitch/)

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
    -   [[1.1] [FreeSWITCH]](#FreeSWITCH)
    -   [[1.2] [Web server]](#Web_server)
    -   [[1.3] [PHP]](#PHP)
    -   [[1.4] [Database]](#Database)
-   [[2] [Database setup]](#Database_setup)
-   [[3] [Installing Bluebox]](#Installing_Bluebox)
-   [[4] [Starting FreeSWITCH]](#Starting_FreeSWITCH)
-   [[5] [Configuring FreeSWITCH with BlueBox]](#Configuring_FreeSWITCH_with_BlueBox)
    -   [[5.1] [IPKall]](#IPKall)
    -   [[5.2] [NAT traversal for SIP]](#NAT_traversal_for_SIP)
-   [[6] [Configuring a dialplan (TODO)]](#Configuring_a_dialplan_.28TODO.29)
    -   [[6.1] [Auto attendant]](#Auto_attendant)
    -   [[6.2] [Time based routes]](#Time_based_routes)
    -   [[6.3] [Ring groups]](#Ring_groups)
    -   [[6.4] [Conferences]](#Conferences)
    -   [[6.5] [Feature codes]](#Feature_codes)
    -   [[6.6] [Trunks]](#Trunks)
-   [[7] [Saving the BlueBox configuration]](#Saving_the_BlueBox_configuration)

## [Prerequisites]

Install the following prerequisites:

-   [[[net-misc/freeswitch]](https://packages.gentoo.org/packages/net-misc/freeswitch)[]]-9999
-   [[[www-servers/apache]](https://packages.gentoo.org/packages/www-servers/apache)[]]-2.2.22-r1
-   [[[dev-lang/php]](https://packages.gentoo.org/packages/dev-lang/php)[]]-5.3.13
-   [[[dev-db/mysql]](https://packages.gentoo.org/packages/dev-db/mysql)[]]-5.1.62-r1

### [FreeSWITCH]

Please first install FreeSWITCH following the [FreeSWITCH Wiki](http://wiki.freeswitch.org/wiki/Installation:Gentoo)

There are many USE options for FreeSwitch. Not all of them compile for me.

\[TODO\] \-- Add list here of which work and which don\'t compile.

After installing FreeSWITCH, there is a post-installation message from portage that a backup of the default configuration files has been saved to: [/usr/share/doc/freeswitch-9999/conf]

But a \"diff -r /etc/freeswitch /usr/share/doc/freeswitch-9999/conf\" shows differences. So I made my own copy:

`root `[`#`]`cp -a /etc/freeswitch /etc/freeswitch.orig `

`root `[`#`]`ln -s /etc/freeswitch.orig /opt/freeswitch/conf.orig `

Also, portage seems to install the freeswitch configuration directory twice:

-   once into [/etc/freeswitch]
-   and a second time into [/etc/freeswitch/freeswitch]

A \"diff\" for each file/folder in /etc/freeswitch/\* and /etc/freeswitch/freeswitch/\* shows no differences. Is this a mistake?

**Double check FreeSWITCH permissions:** \-- I think during BlueBox installation I may have done a \"chown -R apache.freeswitch /opt/freeswitch\".

If apache needs read access to [/opt/freeswitch] during BlueBox installation, the ownership/permissions need to be reset as follows or you cannot run freeswitch as user \"freeswitch\":

[CODE] **Changing ownership/permissions**

    chown -R root:freeswitch "/etc/freeswitch"
            chmod -R u=rwX,g=rX,o=   "/etc/freeswitch"

            # prefix
            chown -R root:freeswitch "/opt/freeswitch"
            chmod -R u=rwX,g=rX,o=   "/opt/freeswitch"
            # allow read access for things like building external modules
            chmod -R u=rwx,g=rx,o=rx "/opt/freeswitch/"
            chmod    u=rwx,g=rx,o=rx "/opt/freeswitch"

            # directories owned by the freeswitch user
            for x in db run log cores storage recordings; do
                    chown -R freeswitch:freeswitch "/opt/freeswitch/$"
            done

Also, the [/etc/init.d/freeswitch] script tries to change the pid file from the default for FreeSwitch from [/opt/freeswitch/run/freeswitch.pid] to [/var/run/freeswitch.pid].

FreeSwitch insists on writing its pid to [/opt/freeswitch/run/freeswitch.pid], but the Gentoo init script looks for the pid in [/var/run/freeswitch.pid].

So my solution is to change the init script:

[CODE] **Updated init script**

    start() " ] && \
                    OPTS="$ -u $"

            [ -n "$" ] && \
                    OPTS="$ -g $"

            [ -n "$" ] && \
                    OPTS="$ $"

            ebegin "Starting Freeswitch"
            ulimit -s 240
            start-stop-daemon --start --quiet --exec $ \
                    --pidfile /opt/freeswitch/run/freeswitch.pid -- -nc $
            eend $?
    }

### [Web server]

Install a web server such one of the following:

-   [Apache](https://wiki.gentoo.org/wiki/Apache "Apache") --- an efficient, extensible [web server](https://wiki.gentoo.org/wiki/Category:Web_servers "Category:Web servers"). It is one of the most popular web servers used the Internet.
-   [nginx](https://wiki.gentoo.org/wiki/Nginx "Nginx") --- a robust, small, high performance [web server](https://wiki.gentoo.org/wiki/Category:Web_servers "Category:Web servers") and reverse proxy server.

### [PHP]

Install [PHP](https://wiki.gentoo.org/wiki/PHP "PHP").

### [Database]

Install a database backend such as:

-   [MySQL](https://wiki.gentoo.org/wiki/MySQL "MySQL")
-   [PostgreSQL](https://wiki.gentoo.org/wiki/PostgreSQL "PostgreSQL")
-   [[[dev-db/sqlite]](https://packages.gentoo.org/packages/dev-db/sqlite)[]]

## [Database setup]

Setup the MySQL database:

`root `[`#`]`mysql -u root -p`

`mysql>``CREATE USER 'bluebox'@'localhost' IDENTIFIED BY 'bluebox'; `

`mysql>``GRANT ALL PRIVILEGES ON bluebox.* TO 'bluebox'@'localhost'; `

`mysql>``SHOW GRANTS FOR bluebox@localhost; `

`mysql>``\q `

If you make a mistake and need to start over:

`root `[`#`]`mysql -u root -p`

`mysql>``REVOKE ALL PRIVILEGES, GRANT OPTION ON bluebox.* FROM 'bluebox'@'localhost'; `

`mysql>``DROP DATABASE bluebox; `

`mysql>``\q `

## [Installing Bluebox]

Adapted from [Bluebox FreeSwitch install guide (CentOS v5.x, Freeswitch v1.0.x, Bluebox)](https://powerpbx.org/content/centos-freeswitch-bluebox-v1).

Install BlueBox git source into top level root of web server:

`root `[`#`]`cd /var/www/localhost/htdocs `

`root `[`#`]`git clone `[`https://github.com/2600hz/bluebox.git`](https://github.com/2600hz/bluebox.git)` `

`root `[`#`]`chown -R freeswitch:freeswitch /var/www/localhost/htdocs/bluebox `

`root `[`#`]`cd /var/www/localhost/htdocs/bluebox `

`root `[`#`]`./preinstall.sh `

When the install asks you for the web user name change default (\"apache\") to \"freeswitch\" (without quotes). Everything else can remain at default (just repeatedly press [Enter] when it asks).

Increase the memory_limit for PHP:

`root `[`#`]`sed -i 's/memory_limit = 32M/memory_limit = 128M/g' /etc/php/apache2-php5.3/php.ini`

Restart apache:

`root `[`#`]`/etc/init.d/apache2 restart`

[/opt/freeswitch/conf] is a symlink to [/etc/freeswitch].

Ownership on the configuration files will need changed to allow apache to make changes before the BlueBox configuration GUI can run:

`root `[`#`]`chown -R apache.freeswitch /etc/freeswitch`

Browse to \"[http://your.web.server/bluebox/](http://your.web.server/bluebox/)\" and run the installer. I went with the defaults but changed the password and email address for the administrator. I also unchecked the option for installing sample data.

I got a warning about conflicting files:

[CODE] **Conflicts**

    Conflicting Files
     /opt/freeswitch/conf/directory/default.xml
     /opt/freeswitch/conf/autoload_configs/conference.conf.xml
     /opt/freeswitch/conf/autoload_configs/ivr.conf.xml
     /opt/freeswitch/conf/autoload_configs/acl.conf.xml
     /opt/freeswitch/conf/autoload_configs/xml_cdr.conf.xml
     /opt/freeswitch/conf/autoload_configs/callcenter.conf.xml
     /opt/freeswitch/conf/autoload_configs/distributor.conf.xml
     /opt/freeswitch/conf/autoload_configs/directory.conf.xml
     /opt/freeswitch/conf/autoload_configs/cdr_csv.conf.xml
     /opt/freeswitch/conf/sip_profiles/external.xml
     /opt/freeswitch/conf/sip_profiles/internal-ipv6.xml
     /opt/freeswitch/conf/sip_profiles/internal.xml
     Conflicting configuration files will be permanently erased if you continue!

I just continued.

After configuring BlueBox, my default configuration was as follows:

[FILE] **`/var/www/localhost/htdocs/bluebox/config/database.php`**

    'type'     => 'mysql',
     'user'     => 'bluebox',
     'pass'     => 'bluebox',
     'host'     => '127.0.0.1',
     'port'     => '3306',
     'socket'   => FALSE,
     'database' => 'bluebox'

You probably will want to change the password for the user \"bluebox\".

Next edit [/var/www/localhost/htdocs/bluebox/bluebox/config/config.php] and disable the installer:

[FILE] **`/var/www/localhost/htdocs/bluebox/bluebox/config/config.php`**

    config['installer_enabled'] = FALSE;

## [Starting FreeSWITCH]

There appears to be no man installation for FreeSWITCH. So use \--help to get freeswitch command line options:

`root `[`#`]`/opt/freeswitch/bin/freeswitch --help`

    These are the optional arguments you can pass to freeswitch
            -nf                    -- no forking
            -u [user]              -- specify user to switch to
            -g [group]             -- specify group to switch to
            -help                  -- this message
            -version               -- print the version and exit
            -waste                 -- allow memory waste
            -core                  -- dump cores
            -rp                    -- enable high(realtime) priority settings
            -lp                    -- enable low priority settings
            -np                    -- enable normal priority settings (system defaults)
            -vg                    -- run under valgrind
            -nosql                 -- disable internal sql scoreboard
            -heavy-timer           -- Heavy Timer, possibly more accurate but at a cost
            -nonat                 -- disable auto nat detection
            -nonatmap              -- disable auto nat port mapping
            -nocal                 -- disable clock calibration
            -nort                  -- disable clock clock_realtime
            -stop                  -- stop freeswitch
            -nc                    -- do not output to a console and background
            -ncwait                -- do not output to a console and background but wait until the system is ready before exiting (implies -nc)
            -c                     -- output to a console and stay in the foreground
            -conf [confdir]        -- specify an alternate config dir
            -log [logdir]          -- specify an alternate log dir
            -run [rundir]          -- specify an alternate run dir
            -db [dbdir]            -- specify an alternate db dir
            -mod [moddir]          -- specify an alternate mod dir
            -htdocs [htdocsdir]    -- specify an alternate htdocs dir
            -scripts [scriptsdir]  -- specify an alternate scripts dir

I got an error when starting FreeSWITCH:

`root `[`#`]`/opt/freeswitch/bin/freeswitch -c -rp -u freeswitch`

    Error: stacksize -1 is too large: run ulimit -s 240 from your shell before starting the application.
    auto-adjusting stack size for optimal performance...
    Cannot open pid file /opt/freeswitch/run/freeswitch.pid.

So I just added *ulimit -s 240* to the start routine of [/etc/init.d/freeswitch].

Some useful fs_cli (FreeSWITCH command line interface) for debugging, tracing:

     sofia status
     sofia status profile sipinterface_1
     sofia status profile sipinterface_1 reg
     sofia loglevel all 9
     sofia global siptrace on
     console loglevel debug
     eval$
     expand sofia contact <sip user account>

## [Configuring FreeSWITCH with BlueBox]

Browse to \"[http://your.web.server/bluebox/](http://your.web.server/bluebox/)\".

Install additional modules:

System-\>Package Manager A few modules have prerequisite modules so if you get an error, install the prerequisite. A few pairs of modules conflict, e.g.:

-   \"Freeswitch\" and \"Asterisk\"
-   \"Endpoint Manager\" and \"Provisioner\"
-   \"Media File\" and \"Media Manager\"

I chose \"Freeswitch\", \"Endpoint Manager\" and \"Media File\" and installed every remaining module except those for a call center.

Bluebox came pre-installed with three sip interfaces \"Connectivity\" -\> \"SIP Interface\"

    Authenticated SIP   Auto Detect    5060    Required    Edit|Delete
    Authenticated SIP - NAT Auto Detect 5070    Required    Edit|Delete
    Unauthenticated SIP  Auto Detect    5080    None        Edit|Delete

\
Use the FreeSWITCH CLI to see your interfaces:

    freeswitch@myhost> sofia status
                        Name          Type                                       Data      State
    =================================================================================================
              sipinterface_2       profile            sip:mod_sofia@192.168.1.40:5070      RUNNING (0)
                 voicemail_1         alias                             sipinterface_2      ALIASED
              sipinterface_1       profile            sip:mod_sofia@192.168.1.40:5060      RUNNING (0)
              sipinterface_3       profile            sip:mod_sofia@192.168.1.40:5080      RUNNING (0)
                192.168.1.40         alias                             sipinterface_1      ALIASED
    =================================================================================================
    3 profiles 2 aliases

\
Now configure users, devices, voicemail boxes, endpoints and assign numbers. It facilitates configuring your sip device if you first configure

-   the Users (\"Organization\" -\> \"User Manager\")
-   their Voicemail Boxes (\"Applications\" -\> \"Voicemail Boxes\")
-   the Endpoints (\"Applications\" -\> \"Endpoints\")

and then

-   the sip phones (\"Applications\" -\> \"Devices\")

The passwords for the users must be alphanumeric but the passwords for the sip devices and voicemail boxes need not be so. To keep things simple I used the same identifying string for device names, sip accounts, extensions. For example, Device Name \"101\" associated with user \"John Doe\" used sip account \"101\" and was assigned extension \"101\" and unanswered calls were transferred to the voicemail box for 101 (extension 201) All used the same password except for the the required alphanumeric password for the User Account for John Doe.

If you decide to have a default Multitenant system, then your sip registrations will use \"user@domain\" instead of just \"user\" for the User Account. Make sure that your user:password (or user@domain:password) for each Device in bluebox matches what you have configured for each sip phone.

First try to get sip registration working before attempting secure sip (sips) registration or encrypted media (srtp). FreeSWITCH also has support for end-to-end encryption using [zrtp](http://www.zrtp.org/) (see [FreeSWITCH Wiki: ZRTP](http://wiki.freeswitch.org/wiki/ZRTP)). But you must use a sip phone which supports zrtp such as the softphone [Zfone](http://zfoneproject.com/prod_zfone.html). Unfortunately, my Snom phones don\'t support zrtp and Snom has no plans to do so.

Note that bluebox adds your sip devices to [/etc/freeswitch/directory/default.xml]. So check and verify that your users have been added there.

Verify that your sip phones have registered with FreeSWITCH:

    sofia status profile sipinterface_1
    =================================================================================================
    Name                    sipinterface_1
    Domain Name             N/A
    Auto-NAT                false
    DBName
    Pres Hosts
    Dialplan                XML
    Context                 multitenant_routing_context
    Challenge Realm         auto_to
    RTP-IP                  192.168.1.40
    SIP-IP                  192.168.1.40
    URL                     sip:mod_sofia@192.168.1.40:5060
    BIND-URL                sip:mod_sofia@192.168.1.40:5060
    HOLD-MUSIC              N/A
    OUTBOUND-PROXY          N/A
    CODECS IN               G7221@32000h,G7221@16000h,G722,PCMU,PCMA,GSM
    CODECS OUT              G7221@32000h,G7221@16000h,G722,PCMU,PCMA,GSM
    TEL-EVENT               101
    DTMF-MODE               rfc2833
    CNG                     13
    SESSION-TO              0
    MAX-DIALOG              0
    NOMEDIA                 false
    LATE-NEG                false
    PROXY-MEDIA             false
    AGGRESSIVENAT           false
    STUN-ENABLED            true
    STUN-AUTO-DISABLE       false
    CALLS-IN                2
    FAILED-CALLS-IN         1
    CALLS-OUT               1
    FAILED-CALLS-OUT        1
    REGISTRATIONS           4

\
Show registrations for sipinterface:

    sofia status profile sipinterface_1 reg
    <... excerpt ..>
    Call-ID:        3c26701f3482-2ou8k0j6yqug
    User:           101@192.168.1.40
    Contact:        "John Doe" <sip:101@192.168.1.101:2048>
    Agent:          snom360/8.4.32
    Status:         Registered(UDP)(unknown) EXP(2012-05-18 20:26:09) EXPSECS(2869)
    Host:           pbx
    IP:             192.168.1.101
    Port:           2048
    Auth-User:      101
    Auth-Realm:     pbx.mydomain.com
    MWI-Account:    101@voicemail_1

\
Now that our phones have registered with FreeSWITCH, check that you have a dial tone and can dial an internal extension.

### [IPKall]

If you want to test SIP from outside your network, apply for a free [DID](https://en.wikipedia.org/wiki/Direct_inward_dialing "wikipedia:Direct inward dialing") from ~~[IPKall](http://www.ipkall.com/) (Washington State)~~.

Just select an area code and choose a \"SIP phone number\" which can be any alphanumeric string, eg. \"IPKall\". Enter the \"SIP Proxy\" for your FreeSWITCH server, eg. \"pbx.mydomain.com:5080\". Make sure you specify a SIP port of 5080 instead of the default 5060.

BlueBox uses different SIP ports to listen on for each different SIP interface, e.g.:

-   Authenticated SIP Auto Detect 5060
-   Authenticated SIP - NAT Auto Detect 5070
-   Unauthenticated SIP Auto Detect 5080

Then go to \"Routing -\> Number Manager\" and add your new number:

-   Manage -\> Number: \"IPKall\"
-   Manage -\> Type: Internal
-   Device (Pick a destination such as Device \"101\")
-   Contexts -\> Inbound Routes
-   Number Pools -\> Device

Now add a trunk for IPKall \"Connectivity -\> Trunk Manager\":

-   Trunk Name: \"IPKall\"
-   Trunk Type: \"SIP Interface\"
-   Server: \"voiper.ipkall.com\"
-   Bind To Interface: \"Unauthenticated SIP\"
-   Made from these Contexts: \"Inbound Routes\"
-   Caller ID Name: \"ipkall\"
-   Caller ID Number: \<DID number emailed to you by IPKall\>

Now try phoning the IPKall DID phone number emailed to you. I got a busy signal, so I had to edit \"Connectivity -\> SIP Interfaces -\> Unauthenticated SIP\" and change \"Inbound Calls -\> Default Incoming Context\" from \"AUTO(Multitenant)\" to \"Inbound Routes\" since I opted not to have a multitenant system.

### [NAT traversal for SIP]

See [NAT Traversal RTP SIP](https://wiki.gentoo.org/wiki/BlueBox/NAT "BlueBox/NAT")

## [][Configuring a dialplan (TODO)]

Now we need to configure various components for a dialplan. BlueBox\'s modules make configuring a dialplan rather straight forward. A few things from FreePBX seem to be missing:

-   A simple way to call an extension to record an IVR prompt for use with an AutoAttendant
    -   BB does however allow you to upload a pre-recorded media file

or to use text-to-speach (flite, cepstral) for your prompts

-   No iax or dahdi (freetdm) modules \-- only sip
    -   Early versions of FreePBX did not have a dahdi configuration utility for managing chan_dahdi_additional.conf, however you could still manually edit the chan_dahdi_custom.conf.

It should be possible to do something similar with FS+BB. The configuration files created by BB begin with \"bluebox\_\", can one though edit other configuration files and have them included in the BB dialplan? without getting clobbered by BB?

#### [Auto attendant]

-   AutoAttendant

#### [Time based routes]

-   Time Based Routes

#### [Ring groups]

-   Ring Groups

#### [Conferences]

-   Conferences

#### [Feature codes]

-   Feature Codes such as CheckingVoicemail, etc.

#### [Trunks]

-   Trunks: DAHDI (PSTN), SIP, IAX

## [Saving the BlueBox configuration]

The BlueBox configuration files are stored in [/opt/freeswitch/conf] -\> [/etc/freeswitch].

Make a copy:

`root `[`#`]`cp -a /etc/freeswitch /etc/bluebox`

Now make a symlink:

`root `[`#`]`ln -sf /etc/bluebox /opt/freeswitch/conf.bluebox`

If you also installed FusionPBX, then do similarly:

`root `[`#`]`ln -sf /etc/fusionpbx /opt/freeswitch/conf.fusionpbx`

Before starting freeswitch or using the GUI just remember to copy either [/etc/ to [/etc/freeswitch] or change the symlink:

`root `[`#`]`ln -sf /etc/bluebox /opt/freeswitch/conf`

     Authenticated SIP - NAT Auto Detect   5070    Required    Edit|Delete
    > /dev/null