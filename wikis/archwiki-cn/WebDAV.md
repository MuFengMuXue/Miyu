[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 该页面于近日同步，正在翻译中。（在 [Talk:WebDAV#](<../zh-cn/Talk:WebDAV.html>) 中讨论）

**翻译状态：**

  * 本文（或部分内容）译自 [WebDAV](<https://wiki.archlinux.org/title/WebDAV> "arch:WebDAV")，最近一次同步于 2024-11-19，若英文版本有所[更改](<https://wiki.archlinux.org/title/WebDAV?diff=0&oldid=809710>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/WebDAV_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Davfs2](<../zh-cn/Davfs2.html> "Davfs2")

[WebDAV](<https://en.wikipedia.org/wiki/WebDAV> "wikipedia:WebDAV") （ _Web Distributed Authoring and Versioning_ ）是 HTTP/1.1 的扩展，因此可以作为一个协议考虑。它包含了一系列概念和由此产生的扩展方法，用以允许通过 HTTP/1.1 读写。WebDAV 不使用 [NFS](<../zh-cn/NFS.html> "NFS") 或 [SMB](<../zh-cn/Samba.html> "Samba")，而是通过HTTP传输文件。 

本指南目的是通过 [web 服务器](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E4%BA%92%E8%81%94%E7%BD%91.html#%E7%BD%91%E7%BB%9C%E6%9C%8D%E5%8A%A1%E5%99%A8> "应用程序列表/互联网")配置简单的WebDAV。 

##  服务器

### Apache

下载 [Apache HTTP 服务器](<../zh-cn/Apache_HTTP_%E6%9C%8D%E5%8A%A1%E5%99%A8.html> "Apache HTTP 服务器")。 

取消 DAV 和 auth_digest 这两个模块的注释： 
    
    LoadModule dav_module modules/mod_dav.so
    LoadModule dav_fs_module modules/mod_dav_fs.so
    LoadModule dav_lock_module modules/mod_dav_lock.so
    LoadModule auth_digest_module modules/mod_auth_digest.so
    
取消注释 `conf/extra/httpd-dav.conf` 文件中的行： 
    
    # Distributed authoring and versioning (WebDAV)
    Include conf/extra/httpd-dav.conf
    
检查文件 `/etc/httpd/conf/extra/httpd-dav.conf` 中的行： 
    
    DAVLockDB /etc/httpd/var/DavLock
    
确保你把上面的行放在了其它指令的外面，比如在 `DocumentRoot` 定义中： 

如果你希望进行干净的部署，可以考虑使用 `/srv/dav` 结构来替代默认的 `/etc/httpd/uploads`。（与原文有出入，请对照[英文页面](<https://wiki.archlinux.org/title/WebDAV> "en:WebDAV")阅读） 

接下来，检查 `/etc/httpd/conf/extra/httpd-dav.conf` 中别名相关的设置（同样要放在其它指令的外面）: 
    
    DavLockDB "/etc/httpd/var/DavLock"
    
    Alias /uploads "/etc/httpd/uploads"
    
    <Directory "/etc/httpd/uploads">
        Dav On
    
        AuthType Digest
        AuthName DAV-upload
        # You can use the htdigest program to create the password database:
        #   htdigest -c "/etc/httpd/user.passwd" DAV-upload admin
        AuthUserFile "/etc/httpd/user.passwd"
        AuthDigestProvider file
    
        # Allow universal read-access, but writes are restricted
        # to the admin user.
        <RequireAny>
            # require that these methods are used (PROPFIND allows directory listing) ...
            Require method GET POST OPTIONS PROPFIND
            # or that the user is admin (f.e. PUT is required to write a file, MKCOL for folders)
            Require user admin
            
            # -- Notes ---
            # more info on methods in the webdav rfc: <http://www.webdav.org/specs/rfc4918.html>
            # POST treated as PUT: <https://datatracker.ietf.org/doc/html/rfc5995>
           
        </RequireAny>
    </Directory>
    
创建目录： 
    
    # mkdir -p /etc/httpd/var
    
检查 DavLockDB 目录的权限并确保Web服务器[用户](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html> "用户和用户组") `http` 有权写入此目录： 
    
    # chown -R http:http /etc/httpd/var
    # mkdir -p /etc/httpd/uploads
    # chown -R http:http /etc/httpd/uploads
    
### nginx

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [nginx-mainline](<https://archlinux.org/packages/?name=nginx-mainline>)包 （[nginx](<../zh-cn/Nginx.html> "Nginx")的Mainline版本）和 [nginx-mainline-mod-dav-ext](<https://aur.archlinux.org/packages/nginx-mainline-mod-dav-ext/>)AUR。 

在 `/etc/nginx/nginx.conf` 文件的头部以及其它块的外面添加下面的行： 
    
    load_module /usr/lib/nginx/modules/ngx_http_dav_ext_module.so;
    
在 `server` 块中为WebDAV添加新的 `location` ，例如： 
    
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
    
上面的例子需要 `/srv/http/dav` 目录和 `/srv/client-temp` 目录存在。 

你也许希望通过使用绑定挂载来让其它目录也能通过WebDAV访问。 

### rclone

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") [rclone](<https://archlinux.org/packages/?name=rclone>)包 。它支持[使用 webdav](<https://rclone.org/commands/rclone_serve_webdav/>) 导出远程或本地目录。 

在不使用任何认证的情况下提供 `/srv/http` 目录下的内容： 
    
    $ rclone serve webdav /srv/http
    
### Caddy

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [caddy-webdav-git](<https://aur.archlinux.org/packages/caddy-webdav-git/>)AUR 或者先安装 [xcaddy-bin](<https://aur.archlinux.org/packages/xcaddy-bin/>)AUR 再使用 WebDAV 模块构建 [Caddy](<../zh-cn/Caddy.html> "Caddy") ： 
    
    $ xcaddy build --with github.com/mholt/caddy-webdav
    
若要使用80端口以 `dav` 路径提供 `/srv/webdav` 目录下的内容，将下面的内容添加到 [Caddyfile](<../zh-cn/Caddy.html#Configuration> "Caddy") ： 
    
    :80 {
        rewrite /dav /dav/
        webdav /dav/* {
           root /srv/webdav
           prefix /dav
        }
        file_server
    }
    
[运行 Caddy](<../zh-cn/Caddy.html#%E7%94%A8%E6%B3%95> "Caddy") ： 
    
    $ caddy run
    
## Client

### Cadaver

[Install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") the [cadaver](<https://archlinux.org/packages/?name=cadaver>)包 package. 

After installation, test the WebDAV server: 
    
    $ cadaver <http://localhost/dav>
    dav:/dav/> mkcol test
    Creating `test': succeeded.
    dav:/dav/> ls
    Listing collection `/dav/': succeeded.
    Coll: test
    
### Dolphin

To create a permanent WebDAV folder in [Dolphin](<../zh-cn/Dolphin.html> "Dolphin") select _Network_ in the _remotes_ section of the places sidebar, then press the _Add Network Folder_ button. The network folder wizard will appear. Select _WebFolder (webdav)_ , and fill in the subsequent form. 

Alternately just click the path bar and then enter the url with _webdav://_ protocol specifier. 

### Nautilus

[Install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") the [gvfs](<https://archlinux.org/packages/?name=gvfs>)包 and [gvfs-dnssd](<https://archlinux.org/packages/?name=gvfs-dnssd>)包 packages. 

In [Nautilus](</wzh/index.php?title=Nautilus&action=edit&redlink=1> "Nautilus（页面不存在）") choose "connect to server" and enter the address with `dav://` or `davs://` protocol specified: 
    
    dav://127.0.0.1/dav
    
**注意：** If you get a "HTTP Error: Moved permanently" with `dav://`, try to use `davs://` as the protocol instead.

### rclone

[rclone](<https://archlinux.org/packages/?name=rclone>)包 is a command line tool that lets you sync to/from, or [mount](<https://rclone.org/commands/rclone_mount/>) (with many caching options), remote file systems including WebDAV. 

### Thunar

[Install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") the [gvfs](<https://archlinux.org/packages/?name=gvfs>)包 and [gvfs-dnssd](<https://archlinux.org/packages/?name=gvfs-dnssd>)包 packages. 

In [Thunar](<../zh-cn/Thunar.html> "Thunar") press `Ctrl+l` and enter the address with _dav_ or _davs_ protocol specified: 
    
    davs://webdav.yandex.ru
    
## Authentication

There are numerous different protocols you can use: 

  * plain
  * digest
  * others

### Apache

Using [htdigest(1)](<https://man.archlinux.org/man/htdigest.1>) (remove the `-c` option if the file exists): 
    
    # htdigest -c /etc/httpd/conf/passwd WebDAV _username_
    
**注意：** Make sure digest authentication is enabled in `httpd.conf` by the presence of this entry: `LoadModule auth_digest_module modules/mod_auth_digest.so`

Using plain [htpasswd(1)](<https://man.archlinux.org/man/htpasswd.1>) (remove the `-c` option if the file exists): 
    
    # htpasswd -c /etc/httpd/conf/passwd _username_
    
Next, `httpd.conf` must be edited to enable authentication. One method would be to require the user `foo` for everything: 
    
    <Directory "/home/httpd/html/dav">
      DAV On
      AllowOverride None
      Options Indexes FollowSymLinks
      AuthType Digest # substitute "Basic" for "Digest" if you used htpasswd above
      AuthName "WebDAV"
      AuthUserFile /etc/httpd/conf/passwd
      Require user foo
    </Directory>
    
**注意：**`AuthName` must match the realm name passed when using the `htdigest` command for digest authentication. For basic/plain authentication, this line may be removed. Also, make sure that the `AuthUserFile` path matches that used with the `htdigest` or `htpasswd` commands above.

If you want to permit everybody to read, you could use this in your httpd.conf 
    
    <Directory "/home/httpd/html/dav">
      DAV On
      AllowOverride None
      Options Indexes FollowSymLinks
      AuthType Digest # substitute "Basic" for "Digest" if you used htpasswd above
      AuthName "WebDAV"
      AuthUserFile /etc/httpd/conf/passwd
      Require all granted
      <LimitExcept GET HEAD OPTIONS PROPFIND>
        Require user foo
      </LimitExcept>
    </Directory>
    
Do not forget to [restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `httpd.service` after making changes. 

**注意：** If you get an 405 error with Apache, add `DirectoryIndex disabled` to your `Directory` section.

## Troubleshooting

### Some file explorers cannot edit directories in nginx WebDAV

nginx WebDAV requires a directory path ends with a slash (`/`), but some file explorers does not append a `/` at the end of the path. 

This can be worked-around, by either removing the corresponding checking [code](<https://github.com/nginx/nginx/blob/master/src/http/modules/ngx_http_dav_module.c>) and recompile it, or by appending the following code in a nginx `server` block to add `/` at the end of a request, if needed: 
    
    # The configuration was based on: <https://nworm.icu/post/nginx-webdav-dolphin-deken/>
    # if the request method is MKCOL or is to a directory, add / at the end of the request if it was missing 
    if ($request_method = MKCOL) {
        rewrite ^(.*[^/])$ $1/ break; 
    }
    if (-d $request_filename) { 
        rewrite ^(.*[^/])$ $1/ break; 
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
        rewrite ^(.*[^/])$ $1/ break;
    }
