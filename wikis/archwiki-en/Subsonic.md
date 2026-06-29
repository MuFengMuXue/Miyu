# Subsonic

Subsonic was a music server that let you store your music on one machine and play it from other machines, cell phones, via a web interface, or various other applications. It is no longer maintained. However, a maintained fork () exists.

## Installation
The old, unmaintained version of  is still available. In addition, as of version 6, the software was not open source. Hence it is recommended for users to instead install the open-source fork .

## Configuration
After performing any configuration, remember to restart .

## Install transcoders
By default, Subsonic uses FFmpeg to transcode videos and songs to an appropriate format and bitrate on-the-fly. After installation, you can change these defaults so that, for example, Subsonic will transcode FLAC files using FLAC and LAME instead of FFmpeg. You should therefore install the , and you may also want to install  and .

For security reasons, Subsonic will not search the system for any transcoders. Instead, the user must create symlinks to the transcoders in the  folder. Create the symlinks like so:

 $ cd /var/lib/subsonic/transcode
 # for transcoder in ffmpeg flac lame; do ln -s "$(which $transcoder)"; done

## HTTPS Setup
## With Subsonic
To enable HTTPS browsing and streaming, edit  and change the port from 0 to 8443:

## With nginx
If you already have multiple web services running, it might be easier to use a single SSL configuration everywhere. The following nginx configuration runs Subsonic under :

{{bc|
server {
    listen              443 default ssl;
    server_name         example.com;
    ssl_certificate     cert.pem
    ssl_certificate_key key.pem

    location /subsonic {
      proxy_set_header X-Real-IP         $remote_addr;
      proxy_set_header X-Forwarded-For   $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Proto https;
      proxy_set_header Host              $http_host;
      proxy_max_temp_file_size           0;
      proxy_pass                         http://127.0.0.1:4040;
      proxy_redirect                     http:// https://;
    }
}
}}

To run Subsonic under a different path, you have to set the following options:

## With lighttpd
The following configuration makes lighttpd accept HTTPS connections and proxies them to localhost. An advantage of this approach is that Subsonic does not need to be aware of SSL settings, and it can be left with default settings. This configuration is also designed to play well with the case where lighttpd is hosting multiple sites at a single IP address.

{{hc|/etc/lighttpd.conf|
# Documentation at: https://redmine.lighttpd.net/projects/lighttpd/wiki/Docs
# Check for errors: lighttpd -t -f /path/to/config
server.modules += ("mod_proxy", "mod_redirect")
server.username       =  "http"
server.groupname      =  "http"
server.pid-file       =  "/var/run/lighttpd.pid"
server.errorlog       =  "/var/log/lighttpd/error.log"
server.document-root  = "/srv/http/"
index-file.names = ("index.html")
mimetype.assign = (
    ".avi"       =>  "video/x-msvideo",
    ".css"       =>  "text/css",
    ".html"      =>  "text/html",
    ".jpg"       =>  "image/jpeg",
    ".log"        =>  "text/plain",
    ".markdown"  =>  "text/plain",
    ".md"        =>  "text/plain",  # markdown
    ".mkv"       =>  "video/x-matroska",
    ".mp4"       =>  "video/mp4",
    ".nfo"        =>  "text/plain",
    ".png"       =>  "image/png",
    ".rc"        =>  "text/plain",
    ".rst"       =>  "text/plain",  # reStructuredText
    ".svg"       =>  "image/svg+xml",
    ".txt"       =>  "text/plain",
    ".xml"       =>  "application/xml",
    ""           =>  "application/octet-stream"
)

$SERVER== ":80" {
    $HTTP["host" == "subsonic.example.com" {
        url.redirect = ("^/(.*)" => "https://subsonic.example.com/$1")
    }
}

$SERVER== ":443" {
    # A default ssl.pemfile is required. It can be overridden in specific host
    # blocks. It *may* also be possible to override ssl.ca-file, but this has
    # not been tested.
    ssl.engine  = "enable"
    ssl.use-sslv3 = "disable"
    ssl.ca-file = "/etc/lighttpd/ssl/GandiStandardSSLCA2.pem"
    ssl.pemfile = "/etc/lighttpd/ssl/subsonic.example.com.pem"

    $HTTP["host" == "subsonic.example.com" {
        ssl.pemfile = "/etc/lighttpd/ssl/subsonic.example.com.pem"
        proxy.server = (
            # This proxying is completely transparent to clients. We load
            # balance requests for this path or extension...
            "" => (
                # ... among the following servers. The string naming each server
                # is just a label, and it has little functional impact. (It
                # might affect log file output?)
                ("host" => "127.0.0.1", "port" => 4040)
            )
        )
    }
}
}}

## Troubleshooting
## FLAC playback
The FFmpeg transcoder does not handle FLAC files well, and clients will often fail to play the resultant streams. Using FLAC and LAME instead of FFmpeg may solve this issue. This workaround requires that the FLAC and LAME transcoders have been installed, as explained in #Install transcoders.

Start Subsonic and go to settings > transcoding. Ensure that the default FFmpeg transcoder does not get used on .flac files, then add a new entry. You will end up with something like this:

{| class="wikitable"
! Name !! Convert from !! Convert to !! Step 1 !! Step 2
|-
| mp3 default || ... NOT flac ... || mp3 || ffmpeg ... || &nbsp;
|-
| mp3 flac || flac || mp3 || flac --silent --decode --stdout %s || lame --silent -h -b %b -
|}

## Accessing the database
Subsonic stores all its data inside a HyperSQL database in . You can access it with a simple web interface by going to http://localhost:4040/db.view (replace with your Subsonic URL).

You can also use the SQLTool command-line tool from the HyperSQL distribution, found in .

This command can be run interactively without other arguments :

It can also run commands non-interactively. This command exports all the contents in the  table :

This command exports the whole database as a SQL file :

## Subsonic-compatible servers
## Libresonic/Airsonic
Subsonic was subsequently forked as Libresonic. This was also open-source, but had removed the paid-licence checks, hence was also free as in free beer. However neither Subsonic nor Libresonic are maintained. The current fork continues with the name Airsonic-Advanced.

## Madsonic
 is a (non-free) fork of Subsonic with extra features.

Once you start the server, pay close attention to the Transcoding options, as you will probably have to change the command from "Audioffmpeg" to "ffmpeg".

## Gonic
 is a lightweight music streaming server which implements the Subsonic API

## Navidrome
 is also a modern and good alternative music server which implements the Subsonic API. It is written in Go and it works on a variety of platforms including Raspberry PIs == Clients ==

## Feishin
 (previously maintained as ) is a cross platform, desktop Subsonic API client player

## Strawberry Music Player
 has the ability to playback music from Subsonic API servers

## Sublime Music
 is a native, graphical Subsonic client.

## stmps
 is a Subsonic client for the terminal.
