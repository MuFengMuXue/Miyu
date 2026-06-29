相关文章

  * [Gogs](</wzh/index.php?title=Gogs&action=edit&redlink=1> "Gogs（页面不存在）")
  * [Git](<../zh-cn/Git.html> "Git")

**翻译状态：**

  * 本文（或部分内容）译自 [SonarQube](<https://wiki.archlinux.org/title/SonarQube> "arch:SonarQube")，最近一次同步于 2024-8-1，若英文版本有所[更改](<https://wiki.archlinux.org/title/SonarQube?diff=0&oldid=813648>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/SonarQube_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[SonarQube](<https://www.sonarsource.com/products/sonarqube/>) 是用于改进代码的代码质量工具，以 LGPL3 许可发布。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [sonarqube-bin](<https://aur.archlinux.org/packages/sonarqube-bin/>)AUR 软件包。 

SonarQube 默认使用 H2 数据库（不推荐）。 或需要使用数据库后端，支持以下数据库： 

  * [MariaDB](<../zh-cn/MariaDB.html> "MariaDB")/[MySQL](<../zh-cn/MySQL.html> "MySQL")
  * [PostgreSQL](<../zh-cn/PostgreSQL.html> "PostgreSQL")
  * [Oracle](<../zh-cn/Category:Oracle.html> "Oracle")
  * MSSQL

##  配置

用户配置文件位于 `/etc/webapps/sonarqube/sonar.properties` 中。 

更多配置示例请参阅 [SonarQube docs](<https://docs.sonarsource.com/sonarqube/latest/analyzing-source-code/analysis-parameters>)。 

### PostgreSQL

[安装](<../zh-cn/PostgreSQL.html#%E5%AE%89%E8%A3%85> "PostgreSQL")并[配置](<../zh-cn/PostgreSQL.html#%E5%88%9D%E5%A7%8B%E5%8C%96%E9%85%8D%E7%BD%AE> "PostgreSQL") [PostgreSQL](<../zh-cn/PostgreSQL.html> "PostgreSQL")。 

SonarQube 似乎只支持 TCP Socket 。 

####  使用 TCP 套接字

连接 postgresql： 
    
    [postgres]$ psql
    
以 `postgres` 用户身份连接服务器时创建新用户（系统会提示输入新用户密码）： 
    
    postgres=# CREATE USER sonarqube WITH PASSWORD **password** ;
    
创建 Gitea 数据库，由 `gitea` 用户拥有： 
    
    postgres=# CREATE DATABASE sonarqube OWNER sonarqube;
    postgres=#GRANT ALL PRIVILEGES ON DATABASE sonarqube TO sonarqube;
    
[配置 PostgreSQL，使其可从远程主机访问](<../zh-cn/PostgreSQL.html#Configure_PostgreSQL_to_be_accessible_from_remote_hosts> "PostgreSQL")

验证其工作状态： 
    
    $ psql --host=_ip_address_ --dbname=sonarqube --username=sonarqube --password
    
通过更新 `sonar.properties` 配置 SonarQube： 
    
    /etc/webapps/sonarqube/sonar.properties
    
    sonar.jdbc.url=jdbc:postgresql://localhost/sonarqube
    sonar.jdbc.username=sonarqube
    sonar.jdbc.password=**password**
    sonar.web.javaOpts=-Xmx512m -Xms128m -XX:+HeapDumpOnOutOfMemoryError
    sonar.web.javaAdditionalOpts=-server
    sonar.web.host=0.0.0.0
    sonar.web.port=9000
    sonar.log.level=INFO
    sonar.path.logs=logs

##  升级

升级 SonarQube 后，请按照以下步骤操作： 

  * 更新 `sonar.properties` 文件以匹配新版本。
  * SonarQube 运行后，会出现一个页面提示您升级。详细说明请访问[升级向导](<https://docs.sonarsource.com/sonarqube/latest/setup-and-upgrade/upgrade-the-server/upgrade/>)。
  * 导航至 SonarQube 服务器的设置页面 `https://_ip_ :_port_ /setup` 并点击升级按钮。
  * 升级过程完成后，将显示正常的登录页面。

##  用法

[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `sonarqube.service`，网络接口应在 `http://localhost:9000` 上监听。 

默认证书为 `admin/admin`。 

**注意：**

  * 您可能需要配置一个反向代理进行远程访问，例如 [nginx](<../zh-cn/Nginx.html> "Nginx")。
  * 如果不想让 Sonarqube 监听所有接口，请在 `/etc/webapps/sonarqube/sonar.properties` 中将 `sonar.web.host` 设置为 127.0.0.1 等。

###  与 maven 一起使用
    
    $ mvn clean verify sonar:sonar -Dsonar.projectKey=_project key_ -Dsonar.projectName=_project_ -Dsonar.host.url=_<http://localhost:9000>_ -Dsonar.token=_token_
    
**注意：** _project key_ 、 _project_ 和 _token_ 的值可在网络界面创建。

###  与 sonar-scanner 一起使用

有一个软件包 [sonar-scanner](<https://aur.archlinux.org/packages/sonar-scanner/>)AUR。用法如下 
    
    $ /opt/sonar-scanner/bin/sonar-scanner -Dsonar.projectKey=_project key_ -Dsonar.sources=. -Dsonar.host.url=<http://localhost:9000> -Dsonar.token=_token_
    
**注意：** _project key_ 和 _token_ 的值可在网络界面创建。

##  问题解决

您可以查看[单元状态](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "单元状态")或 [journal](<../zh-cn/Systemd/Journal.html> "Journal")。 还有 sonarqube 日志： 
    
    # /var/log/sonarqube/
    
如果 sonarqube 未激活，其中一个日志将包含错误信息。 

##  参见

  * [Sonarqube Documentation](<https://docs.sonarsource.com/sonarqube/latest/>)
  * [sonarqube 安装手册](<https://www.atlantic.net/dedicated-server-hosting/how-to-install-sonarqube-on-arch-linux/>)
