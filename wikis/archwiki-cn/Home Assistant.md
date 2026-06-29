**翻译状态：**

  * 本文（或部分内容）译自 [Home Assistant](<https://wiki.archlinux.org/title/Home_Assistant> "arch:Home Assistant")，最近一次同步于 2025-08-26，若英文版本有所[更改](<https://wiki.archlinux.org/title/Home_Assistant?diff=0&oldid=835586>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Home_Assistant_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Home Assistant Supervised](<../zh-cn/Home_Assistant_Supervised.html> "Home Assistant Supervised")

[Home Assistant](<https://www.home-assistant.io/>) 是一个开源的家庭自动化软件，它把本地控制和隐私放在首位。由全球的 DIY 爱好者和技术爱好者组成的社区提供支持。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [home-assistant](<https://archlinux.org/packages/?name=home-assistant>)包 包。 

**注意：** Home Assistant Core 版本已被弃用，将不再由上游提供技术支持。参见 [[1]](<https://www.home-assistant.io/blog/2025/05/22/deprecating-core-and-supervised-installation-methods-and-32-bit-systems/>)

### Home Assistant Supervised

参见 [Home Assistant Supervised](<../zh-cn/Home_Assistant_Supervised.html> "Home Assistant Supervised"). 

##  配置

配置文件存储在 `/var/lib/hass/` 中。如果不存在配置，则在启动时将写入默认配置。 

##  用法

要启动 Home Assistant，请[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `home-assistant.service`。 

第一次启动可能需要 20 分钟，因为将下载并安装所需的软件包。[[2]](<https://www.home-assistant.io/docs/installation/>) 您可以在日志中看到进度。 

**提示：** 使用 [journalctl](<../zh-cn/Systemd/Journal.html> "Journalctl") 跟踪首次更新的过程：
    
    # journalctl -fu home-assistant
    
默认情况下，Web 界面位于 `<http://localhost:8123>`。 

备份还原功能在 Web 界面中不可用。如需还原备份，请以 hass 用户身份解压备份的 tar.gz 文件： 
    
    # tar --strip-components=1 -xzf homeassistant.tar.gz -C /var/lib/hass
    
###  使用 MariaDB

默认情况下，Home Assistant 的 recorder/history 集成使用 SQLite。使用 MariaDB 可显著提升性能（尤其在配置规模较大时）。Home Assistant 通过 SQLAlchemy 支持多种后端，例如 MySQL、MariaDB、PostgreSQL 或 MS SQL Server。此处仅介绍 MariaDB，其他后端请参考 [recorder 集成文档](<https://www.home-assistant.io/integrations/recorder/>)。 

如果尚未安装 MariaDB，请参考 [MariaDB](<../zh-cn/MariaDB.html> "MariaDB") 了解安装详情。 

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [python-mysqlclient](<https://archlinux.org/packages/?name=python-mysqlclient>)包 依赖包。 

创建新数据库，下面示例为每个服务创建一个用户名，并授予该用户名前缀的所有数据库通配符访问权限： 
    
    $ mysql -u root -p
    
    CREATE USER **username** @'localhost' IDENTIFIED BY **some_pass** ;
    CREATE DATABASE **username** ;
    GRANT ALL PRIVILEGES ON **username**.* TO **username** @'localhost';
    FLUSH PRIVILEGES;
    quit;

在配置文件中添加： 
    
    /var/lib/hass/configuration.yaml
    
    recorder:
      db_url: !secret recorder_mariadb_url
    
在 secrets 文件中添加（若未使用 Unix socket，请参考 [recorder 集成文档](<https://www.home-assistant.io/integrations/recorder/>) 了解其他 URL 格式）： 
    
    /var/lib/hass/secrets.yaml
    
    recorder_mariadb_url: "mysql://USER:PASSWORD@localhost/DATABASE?unix_socket=/var/run/mysqld/mysqld.sock&charset=utf8mb4"

最后，[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `home-assistant.service` 服务。数据库将开始填充数据。更多信息请参考 [recorder 集成文档](<https://www.home-assistant.io/integrations/recorder/>)。 

###  使用 PostgreSQL

你需要在 hass 的虚拟环境中安装名为 _psycopg2_ 的 Python 模块。 

你需要为 systemd 添加一个 [附加配置片段](<../zh-cn/Systemd.html#%E9%99%84%E5%8A%A0%E9%85%8D%E7%BD%AE%E7%89%87%E6%AE%B5> "附加配置片段")： 
    
    /etc/systemd/system/home-assistant.service.d/postgresql.conf
    
    [Service]
    ExecStartPre=/var/lib/hass/.venv/bin/python -m pip install psycopg2

这确保了 psycopg2 模块始终被安装。 

创建角色并建立数据库： 
    
    [postgres]$ createuser homeassistant
    [postgres]$ createdb homeassistant -O homeassistant
    
配置 Home Assistant，在配置文件中添加 PostgreSQL 数据库 URL： 
    
    /var/lib/hass/configuration.yaml
    
    recorder:
      db_url: !secret recorder_postgresql_url
    
在 secrets 文件中添加数据库 URL： 
    
    /var/lib/hass/secrets.yaml
    
    recorder_postgresql_url: "postgresql://homeassistant@127.0.0.1/homeassistant"

最后，[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `home-assistant.service` 服务。数据库将开始填充数据。 

##  故障排查

###  无法访问 USB 设备

在默认安装中，Home Assistant 可能没有足够权限访问某些设备（如 Zigbee USB 加密狗），因为这些设备受 `uucp` 系统组控制。 

[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "编辑") `home-assistant.service` 文件，在 `[Service]` 部分添加 `SupplementaryGroups=uucp`，使默认的 `hass` 用户拥有正确的权限组。 

然后，执行 [daemon-reload](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Daemon-reload") 并 [重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `home-assistant.service` 服务，即可正常运行。[[3]](<https://community.home-assistant.io/t/solved-zha-connection-failed-with-sonoff-zigbee-3-0-dongle/349855/12>)

###  日志中出现 ModuleNotFoundErrors

如果在系统软件包升级后 Home Assistant 出现异常，可能是系统软件包与 Home Assistant 管理的 Python 库之间不兼容导致的。要重置 Home Assistant 的 Python 库并重新安装，请删除 modules 目录： 
    
    # rm -r /var/lib/hass/deps/lib
    
然后 [重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `home-assistant.service` 服务。 

如果首次重启后仍出现 ModuleNotFoundErrors，可能需要再次重启。Home Assistant 会检测到缺失的模块并自动重新安装。 

##  参见

  * [Home Assistant 主页](<https://www.home-assistant.io/>)
  * [Home Assistant 文档](<https://www.home-assistant.io/docs/>)
