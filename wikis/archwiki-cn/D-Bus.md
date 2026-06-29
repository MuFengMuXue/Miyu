[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** Mention disabling of dbus services through use of `systemctl mask` and overrides in `/etc/dbus-1/services` (在 [Talk:D-Bus](<../zh-cn/Talk:D-Bus.html>) 中讨论)

[D-Bus](<https://en.wikipedia.org/wiki/D-Bus> "wikipedia:D-Bus") 是一个为进程间通信提供简单方法的消息总线系统。它由一个可为全系统加载或是为单个用户会话加载的守护进程和一系列供应用程序使用 D-Bus 的库组成。 

[dbus](<https://archlinux.org/packages/?name=dbus>)包 作为 [systemd](<https://archlinux.org/packages/?name=systemd>)包 的依赖被拉取和安装，并且用户会话总线会为每个用户[自动启动](<https://archlinux.org/news/d-bus-now-launches-user-buses/>)。 

##  替代实现

### dbus-broker

**dbus-broker** — A drop-in replacement for the _libdbus_ reference implementation, which aims "to provide high performance and reliability, while keeping compatibility to the D-Bus reference implementation". 

     <https://github.com/bus1/dbus-broker> || [dbus-broker](<https://archlinux.org/packages/?name=dbus-broker>)包

要将 _dbus-broker_ 作为系统总线启用，要先[禁用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "禁用") `dbus.service` 然后[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `dbus-broker.service`

要将其作为用户总线启用，可以为单个或全部用户启用`dbus-broker.service` [用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "用户单元")。 

最后要重启来让这些设置生效。 

##  提示与技巧

###  覆盖 dbus 服务

你可以在 `$XDG_DATA_HOME/dbus-1/services` 覆盖 dbus 服务。 

如果服务已经被启动了，覆盖工作不会立即生效。必须先杀死已有的服务进程，或者更早地启动服务。 

You can use this to always use a particular service when you have several installed providing the same well-known bus name. 

##  调试

  * **D-Feet** — Easy to use D-Bus debugger GUI tool. D-Feet can be used to inspect D-Bus interfaces of running programs and invoke methods on those interfaces.

     <https://wiki.gnome.org/Apps/DFeet> || [d-feet](<https://archlinux.org/packages/?name=d-feet>)包

  * **QDbusViewer** — GUI D-Bus debugger. Can be used to inspect D-Bus services and invoke methods on them.

     <https://doc.qt.io/qt-5/qdbusviewer.html> || [qt5-tools](<https://archlinux.org/packages/?name=qt5-tools>)包

你也可以用 [systemd](<../zh-cn/Systemd.html> "Systemd") 的 [busctl(1)](<https://man.archlinux.org/man/busctl.1>)。 

##  另见

  * <https://freedesktop.org/wiki/Software/dbus/>
  * <https://freedesktop.org/wiki/IntroductionToDBus/>
