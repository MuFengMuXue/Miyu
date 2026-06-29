Other languages:

[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=KDE/tr "KDE (3% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=KDE/ru "KDE (100% translated)") • ‎[فارسی](//wiki.manjaro.org/index.php?title=KDE/fa "کِی‌دی‌ئی (KDE) (21% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Appearance]](#Appearance)
    -   [[2.1] [Desktop Settings]](#Desktop_Settings)
    -   [[2.2] [Lockscreen]](#Lockscreen)
-   [[3] [Tips and Tricks]](#Tips_and_Tricks)
    -   [[3.1] [File Manager]](#File_Manager)
    -   [[3.2] [KCMs]](#KCMs)
    -   [[3.3] [Single Click vs Double Click]](#Single_Click_vs_Double_Click)
    -   [[3.4] [Power]](#Power)
        -   [[3.4.1] [Block Power Management]](#Block_Power_Management)
        -   [[3.4.2] [Disable Hibernate]](#Disable_Hibernate)
        -   [[3.4.3] [Disable Suspend]](#Disable_Suspend)
        -   [[3.4.4] [End Session Commands]](#End_Session_Commands)
            -   [[3.4.4.1] [Prompt]](#Prompt)
            -   [[3.4.4.2] [Immediate]](#Immediate)
-   [[4] [See also]](#See_also)

# [Overview]

KDE is a software project currently comprised of a desktop environment known as Plasma, a collection of libraries and frameworks and several applications.

\

[![KDE-de-18.jpg](/images/thumb/9/92/KDE-de-18.jpg/600px-KDE-de-18.jpg)](//wiki.manjaro.org/index.php?title=File:KDE-de-18.jpg)

\

# [Appearance]

#### [Desktop Settings]

To reach desktop settings right click on the desktop and select *Configure Desktop*. If that option isn\'t available (it is configurable), you can use the keyboard shortcut `Alt+D,Alt+S`

**Layout**\
Under the *Wallpaper* tab there is a \'Layout\' option. `Desktop Settings -> Wallpaper -> Layout`\
\"Folder View\" will allow you to place and interact with items on the desktop.\
If you do not use desktop icons (or if you need encouragement for better organization) you can use \"Desktop\".\
\"Desktop\" layout will not allow items on the desktop and results in almost 20 MiB of memory savings in plasmashell.

\

#### [Lockscreen]

Basic settings such as delay and shortcut can be configured at the System Settings location\
`System Settings -> Security & Privacy -> Screen Locking`\
Selecting the `Configure Appearance` button in the top-right corner will present styling options.

\

# [Tips and Tricks]

#### [File Manager]

Dolphin is the default file manager for Plasma.\
See its dedicated page [here](//wiki.manjaro.org/index.php?title=Dolphin "Dolphin").

\

#### [KCMs]

Settings in Plasma are provided by KDE Configuration Modules (KCM). These are the various modules or sections of *System Settings*, but it should be noted that some KCMs are hidden from *System Settings*. All modules can be managed and launched via the utility *kcmshell6*.

To list available KCMs:

[user \$ ][ kcmshell6 \--list [COPY TO CLIPBOARD]]

\

To run a particular module (replacing *kcm_kded* with the desired module):

[user \$ ][ kcmshell6 kcm_kded [COPY TO CLIPBOARD]]

\

#### [Single Click vs Double Click]

In order to select between single and double click for opening files and folders you can use System Settings.\
`System Settings -> Workspace -> General Behavior -> "Clicking files or folders"`

\

#### [Power]

##### [Block Power Management]

The Plasma Power widget can be used to manually inhibit Screen Locking and Sleep but the *kde-inhibit* command can be used to manually block specific features. The following example will use all of them to inhibit each feature for as long as trailing command is running (in this case *spotify*).

[user \$ ][ kde-inhibit \--power \--screenSaver \--nightLight \--notifications spotify [COPY TO CLIPBOARD]]

\

##### [Disable Hibernate]

Hibernation can be disabled and it\'s menu entries hidden with the drop-in file */etc/polkit-1/rules.d/99-disable-hibernate.rules*.

/etc/polkit-1/rules.d/99-disable-hibernate.rules

    // Disable hibernate for all users
    polkit.addRule(function(action, subject)
    });
    polkit.addRule(function(action, subject)
    });

##### [Disable Suspend]

Suspend can be disabled and it\'s menu entries hidden with the drop-in file */etc/polkit-1/rules.d/99-disable-suspend.rules*.

/etc/polkit-1/rules.d/99-disable-suspend.rules

    // Disable suspend for all users
    polkit.addRule(function(action, subject)
    });
    polkit.addRule(function(action, subject)
    });

##### [End Session Commands]

Logging out or shutting down via a command can be useful whether for a non-graphical environment or inclusion in scripts. Whenever a plasma session is involved using the following commands should be preferred over more generic options such as *systemctl reboot*.

###### [Prompt]

DBUS provides methods to open a prompt to end a session (logout, reboot, shutdown).

[user \$ ][ qdbus6 org.kde.LogoutPrompt /LogoutPrompt promptLogout [COPY TO CLIPBOARD]]

\

[user \$ ][ qdbus6 org.kde.LogoutPrompt /LogoutPrompt promptReboot [COPY TO CLIPBOARD]]

\

[user \$ ][ qdbus6 org.kde.LogoutPrompt /LogoutPrompt promptShutDown [COPY TO CLIPBOARD]]

\

[user \$ ][ qdbus6 org.kde.LogoutPrompt /LogoutPrompt promptAll [COPY TO CLIPBOARD]]

\

###### [Immediate]

Similar commands can be used to initiate the process without any prompt.

[user \$ ][ qdbus6 org.kde.Shutdown /Shutdown savesession [COPY TO CLIPBOARD]]

\

[user \$ ][ qdbus6 org.kde.Shutdown /Shutdown logout [COPY TO CLIPBOARD]]

\

[user \$ ][ qdbus6 org.kde.Shutdown /Shutdown logoutAndReboot [COPY TO CLIPBOARD]]

\

[user \$ ][ qdbus6 org.kde.Shutdown /Shutdown logoutAndShutdown [COPY TO CLIPBOARD]]

\

\

# [See also]

[KDE.org](https://kde.org/)\
[Archwiki:KDE](https://wiki.archlinux.org/index.php/KDE)\
[Wikipedia:KDE](https://en.wikipedia.org/wiki/KDE)\
\