**翻译状态：**

  * 本文（或部分内容）译自 [Tomcat](<https://wiki.archlinux.org/title/Tomcat> "arch:Tomcat")，最近一次同步于 2022-11-23，若英文版本有所[更改](<https://wiki.archlinux.org/title/Tomcat?diff=0&oldid=753703>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Tomcat_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

Tomcat 是一个由 Apache Software Foundation 开发的开源的 Java [Servlet 容器](<https://en.wikipedia.org/wiki/Web_container> "wikipedia:Web container")。 

**注意：** 目前存在四个版本的稳定分支： [7](<https://tomcat.apache.org/download-70.cgi>), [8](<https://tomcat.apache.org/download-80.cgi>), [9](<https://tomcat.apache.org/download-90.cgi>) 和 [10](<https://tomcat.apache.org/download-10.cgi>), 。没一个版本能完全替代另一个。相反，[每个分支是一部分 "Servlet" 和 "JSP" Java 标准的实现](<https://tomcat.apache.org/whichversion.html#Apache_Tomcat_Versions>)。两个版本都被 Arch Linux 官方支持：[tomcat8](<https://archlinux.org/packages/?name=tomcat8>)包, [tomcat9](<https://archlinux.org/packages/?name=tomcat9>)包 and [tomcat10](<https://archlinux.org/packages/?name=tomcat10>)包。选用哪个版本主要由你的 web 程序的需求来决定的。

##  安装

安装 [tomcat8](<https://archlinux.org/packages/?name=tomcat8>)包, [tomcat9](<https://archlinux.org/packages/?name=tomcat9>)包, 或 [tomcat10](<https://archlinux.org/packages/?name=tomcat10>)包 中的一个。 

如果打算部署 Tomcat 到一个生产环境，请考虑安装 [tomcat-native](<https://archlinux.org/packages/?name=tomcat-native>)包 。Tomcat-native 将配置服务器来使用 Apache Portable Runtime (APR) 库的网络连接（socket）和 RNG 实现。它将使用原生的32位或64位代码来提升性能，对速度非常敏感的生产环境经常会用到。Tomcat 的安装不需要额外的配置。更多的信息请参阅 [Tomcat 官方文档](<https://tomcat.apache.org/native-doc/>)。 

使用 tomcat-native 将会移除位于 `catalina.err` 的下列警告： 
    
    INFO: The APR based Apache Tomcat Native library which allows optimal performance in production environments was not found on the java.library.path [...]
    
###  文件系统层次结构

将 `n` 用实际安装的版本 (8, 9, 10) 替代。 

路径 | 用途   
---|---  
`/etc/tomcat _n_` | 配置文件。包括： `tomcat-users.xml` (defines users allowed to use administration tools and their roles), `server.xml` (Main Tomcat configuration file), `catalina.policy` (security policies configuration file)   
`/usr/share/tomcat _n_` | Tomcat 主文件夹。包括脚本文件及到其它文件夹的链接   
`/usr/share/java/tomcat _n_` | Tomcat 的 Java 库（jar文件）   
`/var/log/tomcat _n_` |  **不** 被 `systemd` 记录的日志文件 (参阅 [#日志记录](<#%E6%97%A5%E5%BF%97%E8%AE%B0%E5%BD%95>))   
`/var/lib/tomcat _n_ /webapps` | Tomcat 部署你的 Web 程序的地方   
`/var/tmp/tomcat _n_` | Tomcat 存储你的 Web 程序数据的地方   
  
##  初始化配置

要使用 manager 和 admin 管理界面，请编辑下面这个文件 `/etc/tomcat _n_ /tomcat-users.xml`

取消 XML 声明中"role and user"这一块的注释，然后根据你的需要，修改并启用 `tomcat`, {{Ic|admin-{gui,script} }} 和 {{Ic|manager-{gui,script,jmx,status} }} 等角色（详情请参阅 [Configuring Manager Application Access](<https://tomcat.apache.org/tomcat-7.0-doc/manager-howto.html#Configuring_Manager_Application_Access>)）。 

简单来说，`tomcat` 用于运行 Tomcat 服务器，`manager-*` 用于管理 Tomcat 服务器上的 web 程序，`admin-*` 是 Tomcat 服务器的全权管理员。 

下面是一个配置文件的样例，里面定义了一些包含用户名和密码的角色（请务必修改把 [CHANGE_ME] 改成更为更安全的密码）： 
    
    /etc/tomcat _n_ /tomcat-users.xml
    
    <?xml version='1.0' encoding='utf-8'?>
    <tomcat-users>
      <role rolename="tomcat"/>
      <role rolename="manager-gui"/>
      <role rolename="manager-script"/>
      <role rolename="manager-jmx"/>
      <role rolename="manager-status"/>
      <role rolename="admin-gui"/>
      <role rolename="admin-script"/>
      <user username="tomcat" password="**[CHANGE_ME]** " roles="tomcat"/>
      <user username="manager" password="**[CHANGE_ME]** " roles="manager-gui,manager-script,manager-jmx,manager-status"/>
      <user username="admin" password="**[CHANGE_ME]** " roles="admin-gui"/>
    </tomcat-users>

请记住，每一次修改了这个文件都必须要重启 Tomcat 服务器。 

[这篇博文](<https://blog.techstacks.com/2010/07/new-manager-roles-in-tomcat-7-are-wonderful.html>)更好地介绍了这些角色。 

为了读取配置文件，以及为了和一些 IDE 更好地配合，需要加入 `tomcat _n_` [用户组](<../zh-cn/User_group.html> "User group")： 
    
     gpasswd -a <user> tomcat<number>
    
##  启动/停止 Tomcat

[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") `tomcat _n_.service` 服务。 

一旦 Tomcat 启动了，你可以通过访问这个页面来查看结果：<http://localhost:8080> 。如果显示了一个漂亮的 Tomcat 本地页面，表明你的 Servlet 容器正在运行，并且可以装载你的 web 程序了。如果启动脚本失败了，又或者你在浏览器里只看到了一个 Java 错误页面，你可以通过 [systemd 的 journalctl](<../zh-cn/Systemd/Journal.html> "Systemd/Journal") 命令来查看启动日志。Google 上有 Tomcat 日志里常见问题的解决办法。 

**注意：** To improve security, Arch Linux's Tomcat packages use the [jsvc](<https://commons.apache.org/daemon/jsvc.html>) binary from Apache's [common-daemons](<https://commons.apache.org/daemon/>). Tomcat's `systemd` service runs this Apache binary with root privileges which itself starts Tomcat with an underprivileged user (`tomcat _n_ :tomcat _n_` in Arch Linux). This prevents malicious code that could be executed in a bad web application from causing too much damage. This also enables the use of ports under 1024 if needed. See `man jsvc` for options available and pass them through the `CATALINA_OPTS` environment variable declared in `/etc/conf.d/tomcat _n_`.

###  备用“手动”方法

Tomcat 也能通过上游脚本来直接控制： 
    
    /usr/share/tomcat/bin/{startup.sh,shutdown.sh,..}
    
这种方法对于调试程序甚至调试 Tomcat 非常有帮助。但不要在首次启动 Tomcat 的时候用这种方法，因为这会导致一些权限错误，从而使一些程序停止运行。为了使用这些脚本，可能需要做一些额外的配置。并且使用这些脚本将会阻止上面所提到的 jsvc 安全优势。 

##  部署和处理 Web 程序

Tomcat 7 捆绑了5个已经部署了的 Web 程序（有必要的话，把 localhost 换成你的服务器的全称域名）： 

  * 默认主页: <http://localhost:8080/>
  * Tomcat 7 的本地文档: <http://localhost:8080/docs/>
  * Servlets 和 JSP 的示例: <http://localhost:8080/examples/>
  * 用于处理虚拟主机的 host-manager: [http://localhost:8080/host-manager/](<http://localhost:8080/host-manager>)
  * 用于管理 web 程序的 manager: [http://localhost:8080/manager/html/](<http://localhost:8080/manager/html>)

###  GUI 方法

最简单的方法是通过 manager 程序来部署 <http://localhost:8080/manager/html>。 使用你在 `tomcat-users.xml` 定义的 `manager` 角色的用户名和密码来登录。登录进去后，你将看到5个已经部署了的 Web 程序。通过 “Deploy” 区域来添加你自己的 Web 程序，通过 “Applications” 区域来停止/启动/取消部署。 

###  CLI 方法

你也可以通过复制程序的 WAR 文件到 `/usr/share/tomcat _n_ /webapps` 目录来部署。确保 `autoDeploy` 选项如下面所示，设置在了正确的主机： 
    
    /etc/tomcat _n_ /server.xml
    
    ...
    <Host name="localhost"  appBase="webapps"
          unpackWARs="true" **autoDeploy="true"** >
    ...

###  把项目部署在别的目录

你也可以通过设置 `Context` 来把你的项目部署在别的目录。 你需要在 `/etc/tomcat _n_ /Catalina/localhost/` 目录下创建你的 context。Context 是一个用于指定 tomcat 查找目录的 xml 文件，其基本格式如下： 
    
    /etc/tomcat _n_ /Catalina/localhost/whatShouldFollowLocalhost.xml
    
    <Context path="/whatSholdFollwLocalhost" docBase="/where/your/project/is/" reloadable="true"/>

假设项目放在用户 /home 目录下的某个文件夹里，则 context 像这样写： 
    
    /etc/tomcat _n_ /Catalina/localhost/myProject.xml
    
    <Context path="/myProject" docBase="/home/archie/code/jsp/myProject" reloadable="true"/>

现在项目文件可以放在 `/home/archie/code/jsp/myProject/` 目录下了。要想在浏览器里查看这个项目，访问 <http://localhost:8080/myProject> 。 如果 tomcat 无法加载这些文件，可能是遇到了权限问题，运行 `chmod o+x /home/archie/code/jsp/myProject` 应该可以解决这个问题。 

##  日志记录

如果使用的是 Arch Linux 官方的 Tomcat 包，则使用 [systemd 的 journalctl](<../zh-cn/Systemd/Journal.html> "Systemd/Journal") 来记录**启动日志** 。这意味着 `/var/log/tomcat _n_ /catalina.err` 和 `/var/log/tomcat _n_ /catalina.out` 将**不会** 被使用。而其它的日志，例如作为 `Valve` 定义在 `/etc/tomcat _n_ /server.xml` 里的 access logs 和 business logs 则默认会记录在 `/var/log/tomcat _n_ /` 目录下。 

为了保存上游风格的日志，把 systemd 文件 `/lib/systemd/system/tomcat _n_.service` 复制到 `/etc/systemd/system/tomcat _n_.service` ，然后把两处 `SYSLOG` 改为日志文件的绝对路径。 

##  进一步设置

基本的配置，可以通过虚拟主机管理程序来设置：<http://localhost:8080/host-manager/html> 。使用你在 `tomcat-users.xml` 中设置的用户名和密码来登录。其它选项可通过修改 `/etc/tomcat _n_` 下的配置文件来设置，最重要的莫过于 `server.xml`。对这些文件的修改已经超过了本入门页面的范围，请访问[官方 Tomcat 7 文档](<https://tomcat.apache.org/tomcat-7.0-doc/index.html>)来获得更多支持。 

###  从以前版本的 Tomcat 中迁移

正如介绍里说的，“Tomcat 8 并不替代 Tomcat 7”。他们都是 Servlet/JSP 标准的实现。因此，程序使用了哪个版本的 Servlet/JSP 决定了需要使用[哪个版本的](<https://tomcat.apache.org/whichversion.html#Apache_Tomcat_Versions>) Tomcat 。如果需要迁移，官方网站[会给你建议](<https://tomcat.apache.org/migration.html>)。 

###  使用不同版本的 JRE/JDK 来运行 Tomcat

除了安装需要的 JRE/JDK 外，唯一要做的就是设置 Tomcat `systemd` service 文件的 TOMCAT_JAVA_HOME 变量。 

安装后，使用 [drop-in file](<../zh-cn/Drop-in_file.html> "Drop-in file") 配置 `TOMCAT_JAVA_HOME`: 
    
    /etc/systemd/system/tomcat _n_.service.d/start.conf
    
    [Service]
    Environment=TOMCAT_JAVA_HOME=/usr/lib/jvm/java-8-openjdk

###  安全配置

本页面最低限度地使你的第一个 web 应用运行在 Tomcat 上，并不意味着这是一个管理 Tomcat （这是一项单独的工作）的明确的指导。Tomcat 官方网站提供了所有必须的官方事项。你也可以参考[这个 O'Reilly 页面](<https://oreilly.com/java/archive/tomcat-tips.html>)和 这个[页面](<https://www.unidata.ucar.edu/software/thredds/current/tds/reference/TomcatSecurity.html>)。这里还是提供了一些安全方面的建议： 

  * 保持你的 Tomcat 更新到了最新版，以便获得安全问题的最新修复
  * 移除不需要的默认程序，比如 `examples`，`docs`，默认的主页 `ROOT` ("_" 在 `manager` 程序里) 。这可以防止潜在的安全漏洞被利用。使用 `manager` 来管理。

为了更安全，你甚至可以删除 host-manager 和 manager 应用。但是别忘了，后者对部署 web 应用非常有用。 

  * 关闭 WAR 自动部署选项。这可以防止某些获得限制权限的人复制 WAR 文件到 `/usr/share/java/webapps` 来直接运行它。编辑 `server.xml` 并把 `autoDeploy` 设为 `false`：

    /etc/tomcat _n_ /server.xml
    
    ...
    <Host name="localhost"  appBase="webapps"
          unpackWARs="true" **autoDeploy="false"** >
    ...

  * 匿名化 Tomcat 的默认错误页面来防止潜在的攻击者取得 Tomcat 的版本。想知道 Tomcat 默认显示什么，只需要访问一个不存在的页面，比如 <http://localhost:8080/I_dont_exist> ，你将会看到一个404错误页面，最底下标明了 Tomcat 的版本。

要想匿名化这个，编辑或打开这个 JAR （像 `vim` 等编辑器能直接编辑 zip 文件） 
    
    /usr/share/tomcat _n_ /lib/catalina.jar
    
然后编辑这个文件 
    
    org/apache/catalina/util/ServerInfo.properties
    
    ...
    server.info=
    server.number=
    server.built=
    ...

  * 禁用 `server.xml` 里不使用的 `connectors`
  * 保持对 `/etc/tomcat _n_ /server.xml` 的访问限制。只有 `tomcat` 用户，和/或者 `root` 能读写这个文件
  * 保持 `jsvc` 的使用。不要使用上游启动脚本，除非有上文安全部分提到的特别原因。
  * 在 `tomcat-users.xml` 里为每个用户启用强壮并且不同的密码，给真正需要的用户角色，并且禁用你用不到的用户或者角色。

你还可以用使用下列上游脚本来加密 `tomcat-users.xml` 里的密码： 
    
    /usr/share/tomcat _n_ /bin/digest.sh -a SHA NEW_PASSWORD
    
这条命令将会输出类似于下面的信息： 
    
    NEW_PASSWORD:b7bbb48a5b7749f1f908eb3c0c021200c72738ce
    
然后用哈希的部分替换掉 `tomcat-users.xml` 里的密码部分，然后把下文加入到 `server.xml` 中： 
    
    /etc/tomcat _n_ /server.xml
    
    <Host
      ...
      <Realm
        ...
        **className="org.apache.catalina.realm.MemoryRealm" digest="SHA"**
        ...
      />
      ...
    />

注意，这个方法可能意义并不大。因为只有 root 和/或者 tomcat 能读写这个文件，而如果一个入侵者成功获得了 root 权限，那么他将不需要这些密码来混乱你的程序和数据。请确保对这个文件的读写限制！永远弄清楚你在部署什么。 

##  故障排除

###  Tomcat 服务已经启动，但是无法加载页面

首先，检查 `/etc/tomcat _n_ /tomcat-users.xml` 有没有语法错误。如果一切正常并且 `tomcat _n_` 正在运行，输入 `journalctl -r` 查看log，看看有没有抛出什么异常（参照 [Logging](<#Logging>) ）。 如果你看到有类似 `java.lang.Exception: Socket bind failed: [98] Address already in use` 的异常，说明其它服务正在监听这个端口。例如，有可能 [Apache](<../zh-cn/Apache_HTTP_Server.html> "Apache HTTP Server") 和 Tomcat 都在监听同一个端口（例如你在8080端口运行的 Apache 使用在80端口运行的[Nginx](<../zh-cn/Nginx.html> "Nginx") 作为代理）。如果是这种情况，编辑 `/etc/tomcat _n_ /server.xml` 文件，然后修改 `<Service name="Catalina">` 下的 Connector port 为其它的值： 
    
    /etc/tomcat _n_ /server.xml
    
    <?xml version='1.0' encoding='utf-8'?>
    ...
    ...
    <Service name="Catalina">
        <Connector executor="tomcatThreadPool"
                     port="8090" protocol="HTTP/1.1"
                     connectionTimeout="20000"
                     redirectPort="8443" />
    ...
    ...
    </Service>

最后[重启](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd") `tomcat _n_` 和 `httpd` 服务。 

如果还没有解决，而且是在虚拟机中，请尝试删除并重建 `/dev/random` (cf. [Solution: FUTEX_WAIT hangs Java on Linux / Ubuntu in vmware or virtual box](<https://www.nofluffjuststuff.com/blog/pratik_patel/2010/01/solution_futex_wait_hangs_java_on_linux__ubuntu_in_vmware_or_virtual_box>)): 
    
    # rm /dev/random 
    # mknod -m 644 /dev/random c 1 9
    
或者修改 `/usr/lib/jvm/java-8-openjdk/jre/lib/security/java.security` 为指向 `/dev/urandom`/ 
