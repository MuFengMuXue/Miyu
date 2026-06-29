# WebDAV

WebDAV (Web Distributed Authoring and Versioning) is an extension of HTTP/1.1 and therefore can be considered to be a protocol. It contains a set of concepts and accompanying extension methods to allow read and write across the HTTP/1.1 protocol. Instead of using NFS or SMB, WebDAV offers file transfers via HTTP.

The goal of this article is to setup a simple WebDAV configuration using a web server.

## Server
## Apache
Install the Apache HTTP Server.

Uncomment the modules for DAV and auth_digest:

Uncomment the include line for conf/extra/httpd-dav.conf:

Check the following line in :

Make sure you add it outside of any other directives, for instance right under the  definition.

If you want a clean setup consider a  structure instead of , but that's what i found at the default.

Next, check the aliases (also outside of any directives) in :

Create the directory:

 # mkdir -p /etc/httpd/var

Check the permissions of DavLockDB's directory and ensure it is writable by the webserver user :

 # chown -R http:http /etc/httpd/var
 # mkdir -p /etc/httpd/uploads
 # chown -R http:http /etc/httpd/uploads

## nginx
Install  (the mainline variant of nginx) and .

At the top of your  and outside any blocks, add:

Add a new  for WebDAV to your  block, for example:

{{bc|
location /dav {
    root   /srv/http;

    dav_methods PUT DELETE MKCOL COPY MOVE;
    dav_ext_methods PROPFIND OPTIONS;

    # Adjust as desired:
    dav_access user:rw group:rw all:r;
    client_max_body_size 0;
    create_full_put_path on;
    client_body_temp_path /srv/client-temp;
    autoindex on;

    allow 192.168.178.0/24;
    deny all;
}
}}

The above example requires the directories  and  to exist.

You may want to use bind mounts to make other directories accessible via WebDAV.

## rclone
Install the  package. It supports exporting a remote or local directory using webdav.

To serve the contents of  with no authentication:

 $ rclone serve webdav /srv/http

## Caddy
Install the  package, or use  and build Caddy with the WebDAV module:

 $ xcaddy build --with github.com/mholt/caddy-webdav

To serve the contents of  on the path  using port 80, add the following to your Caddyfile:

 :80 {
     rewrite /dav /dav/
     webdav /dav/* {
        root /srv/webdav
        prefix /dav
     }
     file_server
 }

Then run Caddy:

 $ caddy run

## Client
## Cadaver
Install the  package.

After installation, test the WebDAV server:

 $ cadaver http://localhost/dav
 dav:/dav/> mkcol test
 Creating `test': succeeded.
 dav:/dav/> ls
 Listing collection `/dav/': succeeded.
 Coll: test

## Dolphin
To create a permanent WebDAV folder in Dolphin select Network in the remotes section of the places sidebar, then press the Add Network Folder button. The network folder wizard will appear. Select WebFolder (webdav), and fill in the subsequent form.

Alternately just click the path bar and then enter the url with webdav:// protocol specifier.

## Nautilus
Install the  and  packages.

In Nautilus choose "connect to server" and enter the address with  or  protocol specified:

 dav://127.0.0.1/dav

## rclone
 is a command line tool that lets you sync to/from, or mount (with many caching options), remote file systems including WebDAV.

## Thunar
Install the  and  packages.

In Thunar press  and enter the address with dav or davs protocol specified:

 davs://webdav.yandex.ru

## Authentication
There are numerous different protocols you can use:

* plain
* digest
* others

## Apache
Using  (remove the  option if the file exists):

 # htdigest -c /etc/httpd/conf/passwd WebDAV username

Using plain  (remove the  option if the file exists):

 # htpasswd -c /etc/httpd/conf/passwd username

Next,  must be edited to enable authentication. One method would be to require the user  for everything:

If you want to permit everybody to read, you could use this in your httpd.conf

Do not forget to restart  after making changes.

## Troubleshooting
## Some file explorers cannot edit directories in nginx WebDAV
nginx WebDAV requires a directory path ends with a slash (), but some file explorers does not append a  at the end of the path.

This can be worked-around, by either removing the corresponding checking code and recompile it, or by appending the following code in a nginx  block to add  at the end of a request, if needed:

{{bc|1=# The configuration was based on: https://nworm.icu/post/nginx-webdav-dolphin-deken/
# if the request method is MKCOL or is to a directory, add / at the end of the request if it was missing
if ($request_method = MKCOL) {
    rewrite ^(.*$1/ break;
}
if (-d $request_filename) {
    rewrite ^(.*[^/)$ $1/ break;
}

# if the request method is copy or move a directory, add / at the end of the request if it was missing
set $is_copy_or_move 0;
set $is_dir 0;
if (-d $request_filename) {
    set $is_dir 1;
}
if ($request_method = COPY) {
    set $is_copy_or_move 1;
}
if ($request_method = MOVE) {
    set $is_copy_or_move 1;
}
set $is_rewrite "${is_dir}${is_copy_or_move}";
if ($is_rewrite = 11) {
    rewrite ^(.*^/)$ $1/ break;
}
}}
