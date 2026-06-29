**翻译状态：**

  * 本文（或部分内容）译自 [Qt](<https://wiki.archlinux.org/title/Qt> "arch:Qt")，最近一次同步于 2022-12-19，若英文版本有所[更改](<https://wiki.archlinux.org/title/Qt?diff=0&oldid=750474>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Qt_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [KDE](<../zh-cn/KDE.html> "KDE")
  * [Uniform look for Qt and GTK applications](<../zh-cn/Uniform_look_for_Qt_and_GTK_applications.html> "Uniform look for Qt and GTK applications")
  * [GTK](<../zh-cn/GTK.html> "GTK")

[Qt](<https://www.qt.io/>) 是一个跨平台的应用程序和图形组件工具包，它使用标准C++，但同时对C++作出了功能拓展，通过使用特别的代码生成器（称为 [Meta Object Compiler](<https://doc.qt.io/qt-5.12/moc.html>) ，元对象编译器，简称 _moc_ ）以及数个宏来扩展语言的功能。它还包括以下几个更重要的特性： 

  * 支持各种主流桌面平台和部分手机平台。
  * 完善的国际化支持。
  * 提供 SQL 数据访问、XML 解析、线程管理、网络支持和统一的跨平台的文件处理API。

Qt 框架是 [KDE](<../zh-cn/KDE.html> "KDE") 软件社区和其它一些重要开源和闭源应用的基石，例如 [VLC](<../zh-cn/VLC_%E5%AA%92%E4%BD%93%E6%92%AD%E6%94%BE%E5%99%A8.html> "VLC")、[VirtualBox](<../zh-cn/VirtualBox.html> "VirtualBox")、[Mathematica](<../zh-cn/Mathematica.html> "Mathematica") 等等。 

##  安装

可以从[官方仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方仓库")安装 Qt 6.x 和 5.x 。旧版本的Qt （4.x 和 3.x）可以从 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 安装。具体通过如下的软件包[安装](<../zh-cn/Pacman.html> "Pacman")： 

  * **Qt 6.x** ：软件包 [qt6-base](<https://archlinux.org/packages/?name=qt6-base>)包，文档包 [qt6-doc](<https://archlinux.org/packages/?name=qt6-doc>)包。
  * **Qt 5.x** ：软件包 [qt5-base](<https://archlinux.org/packages/?name=qt5-base>)包，文档包 [qt5-doc](<https://archlinux.org/packages/?name=qt5-doc>)包。
  * **Qt 4.x** ：软件包 [qt4](<https://aur.archlinux.org/packages/qt4/>)AUR，文档包 [qt4-doc](<https://aur.archlinux.org/packages/qt4-doc/>)AUR。
  * **Qt 3.x** ：软件包 [qt3](<https://aur.archlinux.org/packages/qt3/>)AUR，文档包 [qt3-doc](<https://aur.archlinux.org/packages/qt3-doc/>)AUR。

##  默认 Qt 库

安装 [qtchooser](<https://aur.archlinux.org/packages/qtchooser/>)AUR 可以改变 `/usr/bin` Qt二进制文件（例如， _qmake_ ）的指向（它们默认指向Qt5版本的程序，例如 _qmake-qt5_ ），让它们指向旧版本的程序（例如， _qmake-qt4_ 或者 _qmake-qt3_ ）。 

**注意：** 现在 [qtchooser](<https://aur.archlinux.org/packages/qtchooser/>)AUR 与 [qt5-base](<https://archlinux.org/packages/?name=qt5-base>)包 相冲突，可以自行编译并安装到`/usr/local`。Arch 官方不支持这种方式[FS#51308](<https://bugs.archlinux.org/task/51308>)。

###  修改环境变量

可以通过 `QT_SELECT` [环境变量](<../zh-cn/Environment_variable.html> "Environment variable")设置默认的 QT. 例如要使用 Qt4，可以设置 `export QT_SELECT=4`。 

###  使用配置文件

创建 `~/.config/qtchooser/default.conf` 软链接，链接到`/etc/xdg/qtchooser/`目录中需要的 _.conf_ 文件上。例如要使用 Qt4，将 `/etc/xdg/qtchooser/4.conf` 软链接到 `~/.config/qtchooser/default.conf`。 
    
    $ ln -s /etc/xdg/qtchooser/4.conf ~/.config/qtchooser/default.conf
    
##  配置

###  Qt5 样式

Qt5基于当前使用的桌面环境来决定所使用的样式： 

  * 在 KDE Plasma 桌面环境中，呈现实际选择的Qt风格。可以在 _KDE System Settings_ （ _systemsettings_ ）中更改，这项设置的具体位置是 _外观 > 应用程序风格_。
  * 在 Cinnamon、GNOME、MATE、LXDE、Xfce 等桌面环境中，呈现GTK风格 ([QGtkStyle](<../zh-cn/Uniform_look_for_Qt_and_GTK_applications.html#QGtkStyle> "Uniform look for Qt and GTK applications"))。
  * 在其他桌面环境中，呈现 Fusion 风格。

如果要强制指定一种样式，你可以设置 `QT_STYLE_OVERRIDE` [环境变量](<../zh-cn/Environment_variable.html> "Environment variable")。特别的，如果你想要使用[GTK](<../zh-cn/GTK.html> "GTK")主题，把它设置成`gtk2`（注意：你将需要安装在下文中提到的Qt样式插件来获取GTK样式）。Qt5应用同时也支持`-style`标志，你可以用它来使用指定的样式运行一个Qt5应用程序。 

Qt5中自带两种样式: _Fusion_ 、 _Windows_ 。其他的可以通过官方仓库安装: 

  * **Breeze** — 来自Plasma桌面的Breeze视觉样式，包括了绘画、样式和素材。

     <https://invent.kde.org/plasma/breeze> || [breeze](<https://archlinux.org/packages/?name=breeze>)包

  * **Oxygen** — KDE 的 Oxygen 轻氧风格。

     <https://invent.kde.org/plasma/oxygen> || [oxygen](<https://archlinux.org/packages/?name=oxygen>)包

  * **Lightly** — Lightly是breeze主题的fork，它致力于现代风和极简风格。

     <https://github.com/Luwx/Lightly> || [lightly-git](<https://aur.archlinux.org/packages/lightly-git/>)AUR

  * **QtCurve** — 为KDE和Gtk编写的可配置的小部件样式。

     <https://invent.kde.org/system/qtcurve> || [qtcurve-qt5](<https://archlinux.org/packages/?name=qtcurve-qt5>)包

  * **Adwaita-Qt** — 让Qt应用程序看上去有GNOME风格。

     <https://github.com/MartinBriza/adwaita-qt> || [adwaita-qt5](<https://archlinux.org/packages/?name=adwaita-qt5>)包

  * **Qt style plugins** — Qt 5的附加样式，包含了 _GTK_ 、 _Cleanlooks_ 、 _Motif_ 、 _Plastique_ 。

     <https://code.qt.io/cgit/qt/qtstyleplugins.git> || [qt5-styleplugins](<https://aur.archlinux.org/packages/qt5-styleplugins/>)AUR

  * **Kvantum** — 可定制的基于 SVG 的主题引擎，具有多种内置样式，包括对一些流行的 GTK 主题的模仿，例如 _Adapta_ 、 _Arc_ 、 _Ambiance_ 。

     <https://github.com/tsujan/Kvantum/tree/master/Kvantum> || [kvantum](<https://archlinux.org/packages/?name=kvantum>)包

###  Qt4 样式

Qt4 应用程序会尝试模仿所运行的桌面环境的行为，除非碰到了某些问题或者进行了强制配置。 

  * 在 KDE Plasma 桌面环境中，呈现实际选择的Qt风格。可以在 _KDE System Settings_ （ _systemsettings_ ）中更改，这项设置的具体位置是 _外观 > 应用程序风格_。
  * 在 Cinnamon、GNOME、Xfce 等桌面环境中，呈现GTK风格 ([QGtkStyle](<../zh-cn/Uniform_look_for_Qt_and_GTK_applications.html#QGtkStyle> "Uniform look for Qt and GTK applications"))。
  * 在其他桌面环境中，呈现 Windows 风格。

要修改 Qt4 程序的外观，可以使用 [qt4](<https://aur.archlinux.org/packages/qt4/>)AUR 提供的 Qt 配置工具 _qtconfig-qt4_ 。这个程序可以配置 Qt4 程序的样式、颜色、字体等。 

**注意：** 如果使用 _GTK_ 样式，将忽略颜色和字体设置，直接使用 GTK2 的值。

Qt将所有的配置信息保存在`/etc/xdg/Trolltech.conf` (系统级别) 或者 `~/.config/Trolltech.conf` (只适用于特定用户)。这个文件很难浏览，因为它还包含许多与外观无关的信息，但是要更改它，您只需添加到文件末尾并覆盖任何以前的值（注意要把修改添加在[Qt]标题下）。 

例如要将主题更改为 QtCurve，请添加： 
    
    ~/.config/Trolltech.conf
    
    ...
    [Qt]
    style=QtCurve
    
Qt4 已经包含数种样式，例如 GTK 样式、Windows 样式、CDE 样式等，其它的主题（大多数为 KDE Plasma 桌面编写）可以从官方源或者 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 中安装： 

Qt4 自带这些样式: _CDE_ 、 _Cleanlooks_ 、 _GTK_ 、 _Motif_ 、 _Plastique_ 、 _Windows_ 。其它的主题（大多数为 KDE Plasma 桌面编写）可以单独安装： 

  * **Breeze** — 来自Plasma桌面的Breeze视觉样式，包括了绘画、样式和素材。

     <https://invent.kde.org/plasma/breeze> || [breeze-kde4](<https://aur.archlinux.org/packages/breeze-kde4/>)AUR

  * **Adwaita-Qt** — 让Qt应用程序看上去有GNOME风格。

     <https://github.com/MartinBriza/adwaita-qt> || [adwaita-qt4](<https://aur.archlinux.org/packages/adwaita-qt4/>)AUR

###  Qt 样式表

定制Qt程序的外观有一个有趣的方式，那就是通过Qt样式表，它们只是简单的CSS文件而已。通过样式表，你可以修改程序中所有组件的外观。 

想要用不同的风格运行程序，只需要执行： 
    
    $ qt_application -stylesheet _style.qss_
    
要了解关于Qt样式表的更多信息，请浏览[官方文档](<https://doc.qt.io/qt-5/stylesheet-reference.html>)或者其他的[教程](<http://thesmithfam.org/blog/2009/09/10/qt-stylesheets-tutorial/>)。Qt样式表的示例：[修改Dolphin的外观](<https://kde-apps.org/content/show.php/roxydoxy?content=125979>)。 

###  GTK+ 和 Qt

如果你有 GTK 和 Qt 应用程序，它们的外观可能无法融合到一起。如果你希望使 GTK 风格与 Qt 风格匹配，请阅读[统一 GTK 和 Qt 应用程序外观](<../zh-cn/Uniform_look_for_Qt_and_GTK_applications.html> "Uniform look for Qt and GTK applications"). 

###  在KDE Plasma以外的环境下配置Qt5应用程序

不像Qt4，Qt5并没有提供一个qtconfig实用程序来配置字体、图标或者风格。相应的，它会尝试使用桌面环境提供的配置。在KDE Plasma和GNOME下这个功能运行的很好，但对于其他的比较小众的桌面环境或者窗口管理器而言，这可能导致Qt5程序缺少图标。解决方案之一是通过设置变量 `XDG_CURRENT_DESKTOP=KDE` 或 `GNOME`来假装当前运行着的桌面环境，然后再使用相应的配置程序来配置想要的图标。 

另一个解决方案是安装 [qt5ct](<https://archlinux.org/packages/?name=qt5ct>)包，它提供了一个独立于桌面环境的 Qt5 QPA 和一个配置实用程序。安装完成后，运行 `qt5ct` 以设置图标主题，然后修改[环境变量](<../zh-cn/Environment_variable.html> "Environment variable") `QT_QPA_PLATFORMTHEME=qt5ct`，这样做出的配置才会被Qt程序读取。或者不修改环境变量，使用 `--platformtheme qt5ct` 作为Qt5程序的参数也可以达到目的。 

[qt5ct-kde](<https://aur.archlinux.org/packages/qt5ct-kde/>)AUR 提供了一个修改过的 _qt5ct_ ，它更好的整合了KDE程序，包括KDE QML 程序。 

如果遇到了下列错误，并且一些图标依然不在一些应用程序中出现，安装[oxygen](<https://archlinux.org/packages/?name=oxygen>)包和[oxygen-icons](<https://archlinux.org/packages/?name=oxygen-icons>)包： 
    
    Icon theme "oxygen" not found.
    Icon theme "oxygen" not found.
    Error: standard icon theme "oxygen" not found!
    
##  开发

###  支持的平台

Qt支持如今的绝大多数平台，甚至包括一些十分冷门的平台，而且每隔一段时间就会出现更多的移植。更加完整的平台列表请查阅[维基百科上的Qt](<https://en.wikipedia.org/wiki/Qt_\(framework\)#Platforms> "wikipedia:Qt \(framework\)")。 

#### Android

**注意：** Qt Creator 4.12或更高版本可以自动设置SDK工具、NDK和必要的软件包。有关更多信息，请参阅[Qt Creator:指定Android设备设置](<https://doc.qt.io/qtcreator/creator-developing-android.html#specifying-android-device-settings>)

首先从 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 或使用 [Android Studio](<../zh-cn/Android.html> "Android") 安装一个 [Android SDK](<../zh-cn/Android.html> "Android") 和 NDK。 

SDK 也需要 [OpenJDK](</wzh/index.php?title=OpenJDK&action=edit&redlink=1> "OpenJDK（页面不存在）")，版本要求也有不同，请查阅[这里](<https://doc.qt.io/qt-6/android-getting-started.html>)。 

接下来你需要安装Qt 5 for Android。你可以按下面描述的包从 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 安装，也可以自行构建。构建需要用到的命令可以从 Qt [wiki](<https://wiki.qt.io/Android>) 找到。 

如果遇到了问题，你可以需要查阅[已知问题](<https://wiki.qt.io/Qt_for_Android_known_issues>)。 

  * [android-armv7a-eabi-qt5](<https://aur.archlinux.org/packages/android-armv7a-eabi-qt5/>)AUR \- armeabi-v7a
  * [android-aarch64-qt5](<https://aur.archlinux.org/packages/android-aarch64-qt5/>)AUR \- aarch64
  * [android-x86-qt5](<https://aur.archlinux.org/packages/android-x86-qt5/>)AUR \- x86
  * [android-x86-64-qt5](<https://aur.archlinux.org/packages/android-x86-64-qt5/>)AUR \- x86_64

或者你也可以使用[官方 Qt 安装程序](<https://download.qt.io/official_releases/qt/>)进行安装。 

###  工具

以下是官方的Qt工具： 

  * **[Qt Creator](<https://en.wikipedia.org/wiki/Qt_Creator> "wikipedia:Qt Creator")** — 专为Qt设计的跨平台IDE，支持Qt所有的特性。

     <https://doc.qt.io/qtcreator/> || [qtcreator](<https://archlinux.org/packages/?name=qtcreator>)包

  * **Qt Linguist** — Qt程序的多语言支持工具集。

     <https://doc.qt.io/qt-5/qtlinguist-index.html> || Qt 5: [qt5-tools](<https://archlinux.org/packages/?name=qt5-tools>)包, Qt 4: [qt4](<https://aur.archlinux.org/packages/qt4/>)AUR

  * **Qt Assistant** — 可配置、可再分发的Qt _qch_ 文件阅读器。

     <https://doc.qt.io/qt-5/qtassistant-index.html> || Qt 5: [qt5-tools](<https://archlinux.org/packages/?name=qt5-tools>)包, Qt 4: [qt4](<https://aur.archlinux.org/packages/qt4/>)AUR

  * **Qt Designer** — 为Qt Widget程序编写的跨平台GUI设计、窗体构建工具。

     <https://doc.qt.io/qt-5/qtdesigner-manual.html> || Qt 5: [qt5-tools](<https://archlinux.org/packages/?name=qt5-tools>)包, Qt 4: [qt4](<https://aur.archlinux.org/packages/qt4/>)AUR

  * **Qt Quick Designer** — QML文件的可视化编辑器，支持WYSIWYG（所见即所得）。它能让你从零开始快速构建一个Qt Quick程序。

     <https://doc.qt.io/qtcreator/creator-using-qt-quick-designer.html>[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-22 ⓘ] || [qtcreator](<https://archlinux.org/packages/?name=qtcreator>)包

  * **qmlscene** — 可以用来加载QML文档的工具。这让开发和调试QML程序变得很快。

     <https://doc.qt.io/qt-5/qtquick-qmlscene.html> || Qt 5: [qt5-declarative](<https://archlinux.org/packages/?name=qt5-declarative>)包, Qt 4 QML Viewer: [qt4](<https://aur.archlinux.org/packages/qt4/>)AUR

  * **[qmake](<https://en.wikipedia.org/wiki/Qmake> "wikipedia:Qmake")** — 用来简化跨平台程序的构建过程的工具，与 [cmake](<https://en.wikipedia.org/wiki/CMake> "wikipedia:CMake") 相似，但提供的选项更少，同时是为Qt程序定制的。

     <https://doc.qt.io/qt-5/qmake-manual.html> || Qt 5: [qt5-base](<https://archlinux.org/packages/?name=qt5-base>)包, Qt 4: [qt4](<https://aur.archlinux.org/packages/qt4/>)AUR

  * **uic** — 读取 _*.ui_ XML文件并且生成相应的C++文件的工具。

     <https://doc.qt.io/qt-5/uic.html> || Qt 5: [qt5-base](<https://archlinux.org/packages/?name=qt5-base>)包, Qt 4: [qt4](<https://aur.archlinux.org/packages/qt4/>)AUR

  * **rcc** — 用于在构建过程中将资源（例如图片）嵌入到Qt应用程序中的工具。它生成包含在 Qt 资源 (.qrc) 文件中指定的数据的 C++ 源文件。

     <https://doc.qt.io/qt-5/rcc.html> || Qt 5: [qt5-base](<https://archlinux.org/packages/?name=qt5-base>)包, Qt 4: [qt4](<https://aur.archlinux.org/packages/qt4/>)AUR

  * **moc** — 用来处理Qt的C++语言功能拓展的工具（例如信号槽技术、运行时类型信息、动态属性系统等等）。

     <https://doc.qt.io/qt-5/moc.html> || Qt 5: [qt5-base](<https://archlinux.org/packages/?name=qt5-base>)包, Qt 4: [qt4](<https://aur.archlinux.org/packages/qt4/>)AUR

###  语言支持

Qt支持许多流行的编程语言，查阅 <https://wiki.qt.io/Language_Bindings> 以获取完整列表。 

下面的例子会在一个窗口中显示 'Hello world!'。 

####  C++

  * 包：[qt5-base](<https://archlinux.org/packages/?name=qt5-base>)包
  * 网站： <https://www.qt.io/developers/>
  * 构建：`g++ $(pkg-config --cflags --libs Qt5Widgets) -fPIC -o hello hello.cpp`
  * 运行：`./hello`

    hello.cpp
    
    #include <QApplication>
    #include <QLabel>
    
    int main(int argc, char **argv)
    {
        QApplication app(argc, argv);
        QLabel hello("Hello world!");
    
        hello.show();
        return app.exec();
    }
    
#### QML

  * 包：[qt5-declarative](<https://archlinux.org/packages/?name=qt5-declarative>)包.
  * 网站： <https://doc.qt.io/qt-5/qtquick-qmlscene.html>
  * 运行：`qmlscene hello.qml`

    hello.qml
    
    import QtQuick 2.3
    
    Rectangle {
        id: page
        width: 400; height: 100
        color: "lightgray"
    
        Text {
            id: helloText
            text: "Hello world!"
            anchors.horizontalCenter: page.horizontalCenter
            anchors.verticalCenter: page.verticalCenter
            font.pointSize: 24; font.bold: true
        }
    }
    
####  Python (PyQt)

  * 包：[python-pyqt5](<https://archlinux.org/packages/?name=python-pyqt5>)包 \- Python 3 bindings
  * 网站： <https://riverbankcomputing.com/software/pyqt/intro>
  * 运行：`python hello-pyqt.py`.

    hello-pyqt.py
    
    import sys
    from PyQt5 import QtWidgets
    
    app = QtWidgets.QApplication(sys.argv)
    label = QtWidgets.QLabel("Hello world!")
    
    label.show()
    sys.exit(app.exec_())
    
####  Python (PySide2)

  * 包：[pyside2](<https://archlinux.org/packages/?name=pyside2>)包
  * 网站： <https://wiki.qt.io/Qt_for_Python>
  * 运行：`python hello-pyside.py`

    hello-pyside2.py
    
    import sys
    from PySide2.QtWidgets import QApplication, QLabel
    
    app = QApplication(sys.argv)
    label = QLabel("Hello world!")
    
    label.show()
    sys.exit(app.exec_())
    
####  C#

查看 [QtSharp](<https://gitlab.com/ddobrev/QtSharp>)。 

##  解决问题

###  禁用/更改 Qt 日志行为

当使用 [KDE](<../zh-cn/KDE.html> "KDE") 和/或者任何其他Qt [桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")时，调试信息可能会频繁的输出到 [systemd日志](<../zh-cn/Systemd/Journal.html> "Systemd/日志")中。 

将 `QT_LOGGING_RULES` 设为[环境变量](<../zh-cn/Environment_variable.html> "Environment variable")来修改这个行为。例如，完全禁用所有日志： 
    
    /etc/environment
    
    QT_LOGGING_RULES='*=false'

若只想禁用调试信息的日志，请使用 `QT_LOGGING_RULES="*.debug=false"`。 

###  图标主题没有生效

从Qt 5.1开始，SVG支持被移动到了其他的模块。由于 [qt5-base](<https://archlinux.org/packages/?name=qt5-base>)包 不依赖于 [qt5-svg](<https://archlinux.org/packages/?name=qt5-svg>)包，可能会出现 [qt5-base](<https://archlinux.org/packages/?name=qt5-base>)包 安装上了，但未安装 [qt5-svg](<https://archlinux.org/packages/?name=qt5-svg>)包 的情况。这会导致欺骗性的图标行为。由于SVG不受支持，图标的绘制过程被安静地跳过了，因此图标主题可能处于未使用状态。手动安装 [qt5-svg](<https://archlinux.org/packages/?name=qt5-svg>)包 可以解决这个问题。 

###  主题对root下运行的程序无效

由于用户的主题配置文件 (`$XDG_CONFIG_HOME/Trolltech.conf`) 不被其他的用户读取，你选择的主题不会对 [root下运行的X程序](</wzh/index.php?title=Running_X_apps_as_root&action=edit&redlink=1> "Running X apps as root（页面不存在）")生效。以下是几个可能解决方案： 

  * 创建符号链接，例如 
        
        # ln -s /home/[username]/.config/Trolltech.conf /etc/xdg/Trolltech.conf

  * 配置系统级别的主题文件：`/etc/xdg/Trolltech.conf`
  * 将主题调整为root

###  Qt 4 风格未被考虑

如果纯Qt4程序（非KDE程序）不遵循你所选择的Qt4风格，那么你可能需要告诉Qt4如何找到KDE风格（Oxygen等）。只需要设置[环境变量](<../zh-cn/Environment_variable.html> "Environment variable") `QT_PLUGIN_PATH`即可。例如： 
    
    QT_PLUGIN_PATH=$HOME/.kde4/lib/kde4/plugins/:/usr/lib/kde4/plugins/
    
`qtconfig-qt4` 应该能够找到你的kde主题，从而解决这些问题。 

或者你也可以将Qt4风格文件夹软链接到KDE4风格文件夹： 
    
    # ln -s /usr/lib/{kde,qt}4/plugins/styles/_theme_name_
    
###  Qt5升级后所有基于Qt5的程序无法启动

如果你得到大概类似以下的报错信息： 
    
    Qt FATAL: Cannot mix incompatible Qt library (version 0x50900) with this library (version 0x50901)
    
那么很可能是因为你正使用着没有针对最新Qt5重新编译的Qt5主题或风格插件。它们通常使用Qt私有头文件，这意味着它们依赖于特定的Qt版本，而不仅仅是匹配的soname。通过检查 `QT_STYLE_OVERRIDE` 和 `QT_QPA_PLATFORMTHEME` 环境变量找出您正在使用的主题/样式，并重新构建提供它的AUR包。 

###  QXcbConnection: XCB error: 2 (BadValue)

创建含有如下内容的文件 [[1]](<https://bugzilla.redhat.com/show_bug.cgi?id=1497564#c6>): 
    
    /etc/xdg/QtProject/qtlogging.ini
    
    [Rules]
    qt.qpa.xcb.xcberror=false

###  图形未正确对齐或缩放不正确

查看 [HiDPI#Qt 5](<../zh-cn/HiDPI.html#Qt_5> "HiDPI")。 

###  死键在Qt程序中不工作

如果你进行了正确的键盘配置，并且死键在[GTK](<../zh-cn/GTK.html> "GTK")应用程序（或其他小部件工具包）中工作，但在[KDE](<../zh-cn/KDE.html> "KDE")或任何Qt应用程序中不起作用，那么你可能没有在[Xorg](<../zh-cn/Xorg.html> "Xorg")中加载正确的文件。 

去确认的一种方法： 

  1. launch a Qt app with `qt.xkb.compose.debug` logging rule enabled, eg. launching [qtqr](<https://archlinux.org/packages/?name=qtqr>)包: `QT_LOGGING_RULES=qt.xkb.compose.debug=true qtqr`
  2. then try to write a character using a dead key, eg. `<dead_circumflex> <e>` for `ê` (LATIN SMALL LETTER E WITH CIRCUMFLEX)
  3. if you encounter `qt.xkb.compose: failed to create compose table` then you probably have this issue.

To fix this, first identify your [locale](<../zh-cn/Locale.html> "Locale"). Then, if your locale doesn't have its own folder in `/usr/share/X11/locale/`, eg. `fr_FR.UTF-8`, look for it in the `compose.dir` mapping file to find the corresponding compose file (eg. `en_US.UTF-8/Compose`): 
    
    $ grep fr_FR.UTF-8 /usr/share/X11/locale/compose.dir
    
    en_US.UTF-8/Compose             fr_FR.UTF-8
    en_US.UTF-8/Compose:            fr_FR.UTF-8

Now create or edit `~/.XCompose` to include this compose file: 
    
    ~/.XCompose
    
    include "%S/en_US.UTF-8/Compose"

最后，重启Qt 软件, dead keys should be working and `qt.xkb.compose: failed to create compose table` error should have disappeared whenever you debug with `QT_LOGGING_RULES=qt.xkb.compose.debug=true`. 

##  参阅

  * [Qt官网](<https://qt.io/>)
  * [Qt文档](<https://doc.qt.io>)
  * [Planet Qt](<https://planet.qt.io>)
