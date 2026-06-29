# Jitsi-meet

Jitsi is a set of open-source projects that allows you to easily build and deploy secure videoconferencing solutions. At the heart of Jitsi are Jitsi Videobridge and Jitsi Meet, which let you have conferences on the internet, while other projects from the community enable other features such as audio, dial-in, recording, and simulcasting.

## Installation
Jitsi-meet consists of severals components:

* : the files for the webinterface, accessed via files served by a webserver
* : the prosody plugins for jitsi
* : the configs example to run a stun/turn server
* : the video bridging service providing video streams to all participants
* : the Jitsi conference focus determining who is speaking
* Prosody: a free XMPP server serving as the base of the setup

A graphical overview of the interfaces to the user and towards each other is given upstream.

You need those optional packages to run a standalone server:

*
*
*
*
*
*
*
*

## Configuration
If your server name is  then a common choice for your jitsi will be , but you can choose freely. It is however strongly encouraged from security standpoint to host webapps on their own subdomain. You will need to update DNS record for your server with an entry of your chosen subdomain, in the above example . The remainder assumes that you have done this.

Also you should have SSL/TLS certificates for your  domain, on how to obtain free certificates see certbot.

In the following, the following placeholders are used:

* : your  domain, e.g.
* : password for the videobridge
* : password for the authenticator

Passwords should be obtained in a safe way, e.g. via  or via . Make sure to use different and safe passwords!

## Configuration paths
{| class="wikitable"
|-
! Package
! Configuration path
|-
|
|
|-
|
|
|-
|
|
|-
|
|
|-
|
|
|}

## Loopback
Let us jitsi-meet components reach each other with local ip. It works even if your domain is behind a proxy like Cloudflare which does not return the real ip of the server.

In :

## Configure prosody
 is a prerequisite and you will need to add a configuration to it for your Jitsi services. If you do not already have a prosody server set up, install  and  now. The rest of the prosody configuration assumes you have a local install of prosody.

The package  provides a configuration you can easily customize:

Then add this at the end of:

Customize your configuration:

{{hc|/etc/prosody/conf.d/jitsi.cfg.lua|2=
-- replace all occurences of jitmeet.example.com by JITSIFQDN
-- replace all occurences of focusUser by focus
-- then add or update those section

VirtualHost "JITSIFQDN"
    ssl = {
        key = "/etc/prosody/certs/JITSIFQDN.key";
        certificate = "/etc/prosody/certs/JITSIFQDN.crt";
    }

VirtualHost "auth.JITSIFQDN"
    ssl = {
        key = "/etc/prosody/certs/auth.JITSIFQDN.key";
        certificate = "/etc/prosody/certs/auth.JITSIFQDN.crt";
    }
    authentication = "internal_hashed"
}}

You need now to generate the certificate for JITSIFQDN and auth.JITSIFQDN.

If you use certbot, you can import the certificate with:

 # prosodyctl --root cert import /etc/letsencrypt/live

If you want to use self generated certs, you can use:

{{bc|1=
prosodyctl cert generate JITSIFQDN
[prosody$ prosodyctl cert generate auth.JITSIFQDN
# mv /var/lib/prosody/*.{crt,cnf,key} /etc/prosody/certs/
# trust anchor /etc/prosody/certs/JITSIFQDN.crt
# trust anchor /etc/prosody/certs/auth.JITSIFQDN.crt
# update-ca-trust
}}

Let us register the users jvb and focus:

Then restart  (or start/enable it if it was just installed).

## Configure jitsi-videobridge
The configuration for jitsi-videobridge.

For MUC_NICKNAME, use uuidgen command:

Then start/enable .

## Configure jicofo
The configuration for jicofo.

{{hc|/etc/jicofo/jicofo.conf|2=
jicofo {
  xmpp: {
    client: {
      client-proxy: "focus.JITSIFQDN"
      xmpp-domain: "JITSIFQDN"
      domain: "auth.JITSIFQDN"
      username: "focus"
      password: "SECRET_FOCUS_USER"
      conference-muc-jid = conference.JITSIFQDN
    }
    trusted-domains: [ "recorder.JITSIFQDN" ]
  }
  bridge: {
    brewery-jid: "JvbBrewery@internal.auth.JITSIFQDN"
  }
}
}}

Then start/enable .

## Configure jitsi-meet
The configuration for jitsi-meet webapps.

{{hc|/etc/webapps/jitsi-meet/config.js|2=
var config = {
  hosts: {
    domain: 'JITSIFQDN',
    // ...
    muc: 'conference.JITSIFQDN'
  },
  bosh: '//JITSIFQDN/http-bind',
  // ...
}
}}

## Configure nginx
Configure nginx with TLS as described in nginx#TLS.

Let us copy the provided example.

Then include it in your main configuration:

{{hc|/etc/nginx/nginx.conf|2=
http {
    // ...
    // this should be placed near to the close bracket of the http block
    include sites/*.conf;
}
}}

Then changes the jitsi configuration with yours:

{{hc|/etc/nginx/sites/jitsi.conf|2=
server {
  # ...
  server_name JITSIFQDN;

  # ...
  # use prosody path directly
  ssl_certificate /etc/prosody/certs/JITSIFQDN.crt;
  ssl_certificate_key /etc/prosody/certs/JITSIFQDN.key;
  # or use letencrypt path
  ssl_certificate /etc/letsencrypt/live/JITSIFQDN/fullchain.pem;
  ssl_certificate_key /etc/letsencrypt/live/JITSIFQDN/privkey.pem;

  # set the config path
  # replace alias /etc/jitsi/meet/jitmeet.example.com-config.js by
  location = /config.js {
    alias /etc/webapps/jitsi-meet/config.js;
  }
  # ...
  location ~ ^/({
    set $subdomain "$1.";
    set $subdir "$1/";
    alias /etc/webapps/jitsi-meet/config.js;
  }
}
}}

Then restart .

## Tips and tricks
## Running the server behind a NAT
The following ports need to be forwarded to your server:

HTTPS:

* TCP/443

Jitsi Videobridge:

* UDP/10000

## Jitsi gateway to SIP (Jigasi)
To interface the Jitsi-meet meetings with traditional SIP install  or  and edit the prosody config:

fill the SIP access credentials (  and )

To change the default room name SIP is connecting to, change  in the above config.

Then edit the jigasi configuration:

and then start/enable .

## Access restrictions for room creation
To restrict video conference room creation to authenticated users, you can do the following steps. Note that participants to the meeting are still not authenticated!

Add authentication to the jitsi domain in prosody and add a new virtual host for guests:

{{hc|/etc/prosody/conf.d/jitsi.cfg.lua|2=
-- change authentification of your domain
VirtualHost "JITSIFQDN"
    authentification = "internal_plain"

-- add guest virtual host to allow anonymous user to join your room
VirtualHost "guest.JITSIFQDN"
    authentication = "jitsi-anonymous"
    c2s_require_encryption = false
    modules_enabled = {
        -- copy the content of the modules_enabled
        -- of the VirtualHost "JITSIFQDN"
        -- remove only the module "muc_lobby_rooms" of the list
        -- example:
        "bosh";
        "pubsub";
        "ping"; -- Enable mod_ping
        "speakerstats";
        "external_services";
        "conference_duration";
    }
}}

Edit the configuration file for :

{{hc|/etc/webapps/jitsi-meet/config.js|2=
var config = {
  host: {
    // anonymous users need to use a dedicated muc without authentication
    anonymousdomain: 'guest.JITSIFQDN',
  },
}
}}

Add authentication for :

{{hc|/etc/jicofo/jicofo.conf|2=
jicofo {
  authentication {
    enabled = true
    type = XMPP
    login-url = JITSIFQDN
    enable-auto-login = true
  }
}
}}

Then create the desired users via

Only if you are using  (if you do not know, you do not) edit the SIP interface to not allow anonymous authentication:

These steps are taken from [https://github.com/jitsi/jicofo#secure-domain this guide.

## Access restrictions with JWT token
To restrict video conference room creation to users authenticate with a JWT token (external service for authentication), you can do the following steps. Note that participants to the meeting are still not authenticated!

Install those dependencies:

*
*
*
*
*

Add authentication to the jitsi domain in prosody and add a new virtual host for guests:

{{hc|/etc/prosody/conf.d/jitsi.cfg.lua|2=
-- change authentification of your domain
VirtualHost "JITSIFQDN"
    authentification = "token"
    app_id = "APP_ID"
    app_secret = "APP_SECRET"
    allow_empty_token = false
    modules_enabled = {
        -- keep existing modules and add
        "presence_identity";
    }
    c2s_require_encryption = false

-- add guest virtual host to allow anonymous user to join your room
VirtualHost "guest.JITSIFQDN"
    authentication = "jitsi-anonymous"
    c2s_require_encryption = false
    modules_enabled = {
        -- copy the content of the modules_enabled
        -- of the VirtualHost "JITSIFQDN"
        -- remove only the module "muc_lobby_rooms" of the list
        -- example:
        "bosh";
        "pubsub";
        "ping"; -- Enable mod_ping
        "speakerstats";
        "external_services";
        "conference_duration";
        "presence_identity";
    }

Component "conference.JITSIFQDN" "muc"
    modules_enabled = {
        -- add this to the modules_enabled
        "token_verification";
    }
}}

Edit the configuration file for :

{{hc|/etc/webapps/jitsi-meet/config.js|2=
var config = {
  host: {
    // anonymous users need to use a dedicated muc without authentication
    anonymousdomain: 'guest.JITSIFQDN',
  },
}
}}

Add authentication for :

{{hc|/etc/jicofo/jicofo.conf|2=
jicofo {
  authentication {
    enabled = true
    type = JWT
    login-url = JITSIFQDN
    enable-auto-login = true
  }
}
}}

Then restart  (or start/enable it if it was just installed).
And restart  (or start/enable it if it was just installed).

Now you can use a JWT token to authenticate an user.

You can read the spec here: Jitsi Meet Tokens

Here an quick example in nodejs:

{{bc|
const jwt = require('jsonwebtoken')
const crypto = require('crypto');
const words = require('random-words')
const yourDomain = "JITSIFQDN"
const appId = "APP_ID"
const appSecret = "APP_SECRET"
const userName = "YOUR_USERNAME"
const userEmail = "YOUR_EMAIL"

function getBody(domain, appId, name, email, room) {
    const md5Email = crypto.createHash('md5').update(email).digest("hex");
    const id = crypto.createHash('sha1').update(`${name}:${email}`).digest("hex")

    return {
        context: {
            user: {
                avatar: `https:/gravatar.com/avatar/${md5Email}`,
                name,
                email,
                id,
            },
            group: 'users'
        },
        "aud": "jitsi",
        "iss": appId,
        "sub": domain,
        room,
    }
}

const room = process.argv|| words({exactly: 3, join: '-'})

const data = getBody(
    yourDomain,
    appId,
    userName,
    userEmail,
    room,
)

const options = {
    algorithm: 'HS256',
    expiresIn: '2h',
}

const jwtToken = jwt.sign(data, appSecret, options)

console.log(`https://${yourDomain}/${room}?jwt=${jwtToken}`)
}}

## Log evaluation
For a publicly available IP address the above configuration leads to a public video conference server. To monitor server use one can use journalctl to get an at least vague idea of the usage:

 # journalctl --unit=jicofo.service --grep="created new conference" --output cat

shows all events of new chat room creation and

 # journalctl --unit=jicofo.service --grep="Stopped" --output cat

shows all events of chat room destruction.

Grepping for 'member' also gives you (anonymous!) information on the participants.

## Running own STUN server
By default, Jitsi Meet uses STUN servers from jitsi.org. You can easily run your own STUN server using  and setting it in jitsi-meet's config.

## Troubleshooting
## Check your logs
You can stop all service units (i.e., , , and ), start them one at a time, and follow new messages in the journal for each service unit to see if something is wrong. Most problems are due to password or configuration issues.

If you have an upgrade from a very different version, or you mess up with your config, start other. It will be faster than trying to findout which part is wrong.

## Ask help on Matrix rooms
You can join matrix rooms and ask help there:

* [https://matrix.to/#/#jitsimeet:matrix.org?via=matrix.org Jitsi Meet help and testing
