**翻译状态：**

  * 本文（或部分内容）译自 [XWiki](<https://wiki.archlinux.org/title/XWiki> "arch:XWiki")，最近一次同步于 2024-7-30，若英文版本有所[更改](<https://wiki.archlinux.org/title/XWiki?diff=0&oldid=813212>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/XWiki_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[XWiki](<https://www.xwiki.org>) 是一个用 Java 编写的开源企业级维基，重点在于可扩展性。 

##  安装

请随时查看 [XWiki 安装指南](<https://www.xwiki.org/xwiki/bin/view/Documentation/AdminGuide/Installation/>)。 这些说明假定你将使用 [Tomcat](<../zh-cn/Tomcat.html> "Tomcat") 和 [PostgreSQL](<../zh-cn/PostgreSQL.html> "PostgreSQL")。将这些指南应用于其他组合应该不难。 

  * 安装 [PostgreSQL](<../zh-cn/PostgreSQL.html> "PostgreSQL")。
  * 为方便管理 PostgreSQL，请安装 [phpPgAdmin](<../zh-cn/PhpPgAdmin.html> "PhpPgAdmin")。
  * 安装[tomcat](<../zh-cn/Tomcat.html> "Tomcat")（不要忘记 [tomcat-native](<https://archlinux.org/packages/?name=tomcat-native>)包）。
  * 下载 XWiki WAR 文件
  * 将 WAR 文件重命名为 `xwiki` 。
  * 将 WAR 文件移至 `/var/lib/tomcat _n_ /webapps` 目录。
  * Tomcat 应该会自动解压缩 WAR 文件。如果没有，请重启 Tomcat。
  * 此时，您可能会发现 `data` 目录出现在 `/var/lib/tomcat _n_ /webapps` 中。删除它。
  * 作为 root:

    # cd /var/lib/tomcat _n_
    # mkdir data
    # chown tomcat _n_ :tomcat _n_ data
    
  * 在 `/var/lib/tomcat _n_ /webapps/xwiki/WEB-INF` 目录内： 
    * 打开 `xwiki.properties` 文件，修改 `environment.permanentDirectory` 字段为 `/var/lib/tomcat _n_ /data/xwiki`。
    * 打开 `hibernate.cfg.xml` 文件： 
      * 注释掉题为 "Configuration for the default database" 的部分。
      * 取消注释题为 "PostgreSQL Configuration" 的部分。
      * 根据需要修改数据库名称（在`connection.url`）、用户名和密码。
  * 在 PostgreSQL 中创建 role 和数据库，以匹配 hibernate 配置。
  * 从 [Arch 用户仓库](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E4%BB%93%E5%BA%93.html> "Arch 用户仓库")安装 [postgresql-jdbc](<https://aur.archlinux.org/packages/postgresql-jdbc/>)AUR。
  * 作为 root:

    # cd /usr/share/java/tomcat _n_
    # ln -s /usr/share/java/postgresql-jdbc/postgresql-jdbc41.jar
    
  * [重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `tomcat _n_.service`。
  * 在 Tomcat Manager 中点击 `/xwiki` 启动 XWiki 应用程序。
  * 通过 XWiki Wizard Guide 启动 XWiki，完成配置。

##  Nginx 代理配置 - 解决方案 1

用于 XWiki 的 Nginx 官方指南并不正确。有一个适用于 XWiki 的替代解决方案。 

  * 配置 nginx 网站 `xwiki` 配置文件。

    /etc/nginx/sites-available/xwiki
    
    server {
      listen 80 default_server;
      server_name xwiki.<domain-name>;
      return 301 https://$host$request_uri;
    }
    
    server {
      listen [::]:443 ssl;
      listen 443 ssl;
    
      server_name xwiki.<domain-name>;
    
      # SSL Certificate section
      ssl_certificate ...
      ssl_certificate_key ...
    
      location = / {
        return 301 https://$host/xwiki;
      }
    
      location /xwiki {
        proxy_set_header   X-Real-IP $remote_addr;
        proxy_set_header   Host      $host;
        proxy_http_version 1.1;
        proxy_set_header   Upgrade $http_upgrade;
        proxy_set_header   Connection 'upgrade';
        proxy_cache_bypass $http_upgrade;
        proxy_set_header   X-Forwarded-Host $host;
        proxy_set_header   X-Forwarded-Server $host;
        proxy_set_header   X-Real-IP $remote_addr;
        proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Proto $scheme;
        proxy_pass         http://127.0.0.1:8080/xwiki;
      }
    }
    
  * 激活 `sites-enabled` 目录 （`ln -s /etc/nginx/sites-available/xwiki /etc/nginx/sites-enabled/xwiki`） 中的服务器块。
  * 重启 Nginx。

##  Nginx 代理配置 - 解决方案 2

我发现指示nginx代理到`<http://localhost:8080/xwiki/>`不起作用：生成的URL不正确。与[XWiki 文档](<https://platform.xwiki.org/xwiki/bin/view/AdminGuide/Configuration#HReverseproxysetup>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2024-01-13 ⓘ] 中的说明相反，我无法通过使用 HTTP 标头使 URL 正确。 

目前我所知道的唯一解决方案是在 Tomcat 的 server.xml 文件中创建一个新的 Host 元素： 

  * 复制现有的 `Host` 元素，并将 `name` 属性改为 `xwiki`。
  * 修改 `appBase` 属性为 `/var/lib/tomcat7/webapps-xwiki`。
  * 将 `xwiki` 应用程序从 `/var/lib/tomcat7/webapps/xwiki` 移至 `/var/lib/tomcat7/webapps-xwiki/ROOT` 。
  * 重启 Tomcat。
  * 在 `/etc/hosts` 中添加 `xwiki` 作为 localhost 的别名。(添加到 127.0.0.1 行的末尾）。
  * 指示 Nginx 代理至 `<http://xwiki:8080/>`。
