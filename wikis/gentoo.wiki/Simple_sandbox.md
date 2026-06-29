*Not to be confused with [Sandbox](https://wiki.gentoo.org/wiki/Sandbox "Sandbox").*

This article describes methods to set up tighter security for crucial applications with a method known as *sandboxing*, explaining how to set up **simple sandboxes** for these applications.

When running programs that risk being hijacked with code execution vulnerabilities, it is highly advised to sandbox/jail them. Sandboxes are virtual containers for computer programs to run in. Sandboxes make programs run more securely by giving them a \"playspace\" to run in, preventing them from affecting the broader system while still not greatly limiting their utility to the users. There are many sandboxing methods, from creating entire virtual machines to surround dangerous applications, to simple rules preventing a browser from modifying /etc/passwd. This article describes the oldest, simplest, and very widely used sandboxing method, namely running a program under a special sandbox user.

The above method is often setup by default on linux programs. For example, when installed, the Apache web server creates a new user called \"Apache\" that it runs under. That way, if compromised, an attacker would not gain root permissions on the device; only the same privileges that the \"Apache\" user was granted.

This sandboxing method relies solely on the Unix user and group permissions. It requires no kernel tweaking and little extra software ([[[app-admin/sudo]](https://packages.gentoo.org/packages/app-admin/sudo)[]] or [[[app-admin/doas]](https://packages.gentoo.org/packages/app-admin/doas)[]] and [[[x11-apps/xhost]](https://packages.gentoo.org/packages/x11-apps/xhost)[]]). It is also possible to avoid [sudo] or [doas] and use [su], but then a password is required each time a sandboxed program is executed.

At a minimum, this or another form of sandboxing should be used for software which:

-   Has a known security/privacy issue.
-   Has a history of security/privacy issues.
-   Is distributed in binary form (e.g. many games).
-   Has large codebase and thus attack surface (e.g. Libreoffice).
-   Is no longer maintained.
-   Is very young (brand new project).
-   Is unstable.
-   Accesses the network (email, web, torrent, etc.).

We assume (without loss of generality):

-   [[[www-client/firefox]](https://packages.gentoo.org/packages/www-client/firefox)[]] is the package we want to sandbox.
-   \'larry\' is our own everyday user.
-   \'Mallet\' is an attacker.
-   \'ff\' is the sandbox user used only to run [Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox").

Sandboxing Firefox is mandatory, as it matches multiple patterns on our list. Like all big graphical browsers, it has a history of vulnerabilities. In recent releases, it is distributed partially in binary form (includes binary Adobe DRM and installs binary Cisco codecs). It also has a \'huge\' codebase and accesses the network regularly.

Let\'s imagine Mallet can exploit a vulnerability in Firefox to access larry\'s files (emails, SSH keys, Bitcoin wallet, etc.). If larry runs Firefox under the ff user, then Mallet has only access to the resources available to ff, and would need a further exploit of privilege escalation to access larry\'s data. This obviously assumes tight permissions set on larry\'s files. This sandboxing method is not the most restrictive; Mallet could still learn a lot about our system, start new processes as ff, use the network, and do anything a low-level user can. But it is also possible to configure the permissions on our system so that Mallet can do very little as ff (such configuration is not explained here).

## Contents

-   [[1] [Create sandbox user]](#Create_sandbox_user)
-   [[2] [Install and configure sudo]](#Install_and_configure_sudo)
-   [[3] [Install and configure doas]](#Install_and_configure_doas)
-   [[4] [Configure X server access control (optional)]](#Configure_X_server_access_control_.28optional.29)
-   [[5] [larry runs firefox as sandbox user ff]](#larry_runs_firefox_as_sandbox_user_ff)
-   [[6] [Migrate config files (optional)]](#Migrate_config_files_.28optional.29)
-   [[7] [Adding shortcut icons.]](#Adding_shortcut_icons.)
-   [[8] [Allow larry to access ff\'s home]](#Allow_larry_to_access_ff.27s_home)
-   [[9] [Multiple humans]](#Multiple_humans)
-   [[10] [Disallow larry to run Firefox without sandbox (optional)]](#Disallow_larry_to_run_Firefox_without_sandbox_.28optional.29)
-   [[11] [Repeat for other packages]](#Repeat_for_other_packages)
    -   [[11.1] [Script to add sandbox]](#Script_to_add_sandbox)
    -   [[11.2] [Script to remove sandbox]](#Script_to_remove_sandbox)
-   [[12] [Configure Firefox to output sound to larry\'s PulseAudio daemon]](#Configure_Firefox_to_output_sound_to_larry.27s_PulseAudio_daemon)
-   [[13] [Firewall]](#Firewall)
-   [[14] [Drawbacks]](#Drawbacks)
-   [[15] [Missing icons]](#Missing_icons)
-   [[16] [GPG managment]](#GPG_managment)
    -   [[16.1] [Secret key import]](#Secret_key_import)
    -   [[16.2] [Secret key deletion]](#Secret_key_deletion)
    -   [[16.3] [Git signing commits]](#Git_signing_commits)
-   [[17] [Problem with autotools]](#Problem_with_autotools)
-   [[18] [See also]](#See_also)

## [Create sandbox user]

First, create the \'ff\' sandbox user:

`root `[`#`]`useradd --home=/home/ff --create-home --shell /bin/false --user-group ff`

If [su] to [sudo] or [doas] is preferred, use [/bin/bash] instead of [/bin/false].

## [Install and configure sudo]

`root `[`#`]`emerge --ask app-admin/sudo`

Allow larry to run Firefox as user ff, without need for password:

`root `[`#`]`echo 'larry ALL=(ff) NOPASSWD: /usr/bin/firefox' > /etc/sudoers.d/ff`

Since we regard ff as a kind of sub-user of larry, it is convenient to allow larry to run any command as ff. This is not necessary for Firefox, and does not follow the least-privilege rule, but could be useful for packages with many executables:

`root `[`#`]`echo 'larry ALL=(ff) NOPASSWD: ALL' > /etc/sudoers.d/ff`

If you prefer su to sudo, then instead set a password for ff:

`root `[`#`]`passwd ff`

## [Install and configure doas]

`root `[`#`]`emerge --ask app-admin/doas`

Allow larry to run Firefox as user ff, without need for password:

`root `[`#`]`echo 'permit nopass larry as ff cmd firefox' > /etc/doas.conf`

Since we regard ff as a kind of sub-user of larry, it is convenient to allow larry to run any command as ff. This is not necessary for Firefox, and does not follow the least-privilege rule, but could be useful for packages with many executables:

`root `[`#`]`echo 'permit nopass larry as ff' > /etc/doas.conf`

If you prefer su to sudo, then instead set a password for ff:

`root `[`#`]`passwd ff`

## [][Configure X server access control (optional)]

This step is only needed if the package is graphical and your X\'s access control is enabled.

In order to run Firefox as ff, we could of course start a new desktop session as user ff (login using our display manager), but that would be inconvenient. Instead, we would like to work as larry, but open a Firefox window as ff. For that, root installs xhost:

`root `[`#`]`emerge --ask --verbose x11-apps/xhost`

And larry allows ff to connect to larry\'s X server (to create windows):

`user `[`$`]`xhost si:localuser:ff`

## [larry runs firefox as sandbox user ff]

Finally, to run firefox under the ff user, larry enters the command:

`larry@gentoo $``sudo -u ff firefox`

If you prefer doas:

`larry@gentoo $``doas -u ff firefox`

If you prefer su:

`larry@gentoo $``su -c firefox ff -`

If all went well, Firefox is now running in a window on larry\'s desktop. The window title says \'Mozilla Firefox (as ff)\', to indicate that this window is run by ff.

## [][Migrate config files (optional)]

ff will have his own home directory for storing the Firefox profile, i.e. all browsing settings. All of the files firefox needs access to and is used save addons, cookies, history, etc., will be stored stored in a folder in ff\'s home directory. The precise configuration migration manual is very package-dependent and is beyond the scope of this article. However, assuming Firefox is the only Mozilla software larry has used, root can migrate larry\'s settings:

`root `[`#`]`mv ~larry/.mozilla ~ff/ `

`root `[`#`]`chown -R ff:ff ~ff/.mozilla `

## [Adding shortcut icons.]

Now larry can create icons or add Firefox to startup applications in his desktop environment. However, sometimes such graphical tools only allow to enter one command to be executed. We can conjoin xhost and sudo/doas into one command by using sh:

`user `[`$`]`sh -c 'xhost si:localuser:ff && sudo -u ff firefox'`

If you prefer doas:

`user `[`$`]`sh -c 'xhost si:localuser:ff && doas -u ff firefox'`

Alternatively, john could invoke xhost already when X session starts.

Here\'s a sample .desktop file, that could be placed at e.g. [\~larry/.local/share/applications/firefox.desktop], to add it to your desktop environment\'s Applications menu (the changes should be applied as soon as you create the file):

[FILE] **`~larry/.local/share/applications/firefox.desktop`**

    [Desktop Entry]
    Name=Mozilla Firefox (Sandboxed)
    Comment=Web Browser
    Exec=sh -c 'xhost si:localuser:ff && sudo -u ff firefox %u'
    Icon=firefox
    Terminal=false
    Type=Application
    MimeType=text/html;text/xml;application/xhtml+xml;application/vnd.mozilla.xul+xml;text/mml;x-scheme-handler/http;x-scheme-handler/https;
    Categories=Network;WebBrowser;

If you prefer doas:

[FILE] **`~larry/.local/share/applications/firefox.desktop`**

    [Desktop Entry]
    Name=Mozilla Firefox (Sandboxed)
    Comment=Web Browser
    Exec=sh -c 'xhost si:localuser:ff && doas -u ff firefox %u'
    Icon=firefox
    Terminal=false
    Type=Application
    MimeType=text/html;text/xml;application/xhtml+xml;application/vnd.mozilla.xul+xml;text/mml;x-scheme-handler/http;x-scheme-handler/https;
    Categories=Network;WebBrowser;

## [][Allow larry to access ff\'s home]

We don\'t want ff to access larry\'s files, but it is useful for larry to access ff\'s files:

`root `[`#`]`chgrp -R larry /home/ff `

`root `[`#`]`chmod -R 770 /home/ff `

For instance, when running Firefox as ff, downloaded files can only be saved in [/home/ff] or in [/tmp].

## [Multiple humans]

This method suffices if larry is the only person using this computer. Otherwise, we need to create a separate sandbox user for each real user in order to have separate sandboxed home directories for config files, e.g. ff_larry sandbox user for larry, ff_alice for alice, etc.

## [][Disallow larry to run Firefox without sandbox (optional)]

One problem is: larry can forget to run Firefox using sudo, and can run it directly as himself, e.g. by clicking the Firefox icon. For extra security, we tighten permissions of package files, so that only the sandbox user can run Firefox.

Disallow the owning user (root):

`root `[`#`]`qlist -eo firefox | xargs -d "\n" chmod u-x`

Disallow all other users (e.g. larry):

`root `[`#`]`qlist -eo firefox | xargs -d "\n" chmod o-o`

Let us set the group to ff, so ff user (the only one in ff group) can get access:

`root `[`#`]`qlist -eo firefox | xargs -d "\n" chown root:ff`

However, ff should not modify any package files:

`root `[`#`]`qlist -eo firefox | xargs -d "\n" chmod g-w`

Let\'s have a look at the results:

`root `[`#`]`qlist -eo firefox | xargs -d "\n" ls -l`

    -rw-r-x--- 1 root ff ... /usr/lib64/firefox/firefox

Great, now only ff can run (but not modify) Firefox.

These permissions would be lost on any package reinstall or upgrade. We create Portage hook that sets them after every (non-binary) installation:

`root `[`#`]`mkdir -p /etc/portage/env/www-client/`

    echo 'post_src_install()
      chown -R root:ff $
    }' > /etc/portage/env/www-client/firefox

If you use binary packages (buildpkg feature and \--usepkg=y), remember that this hook is NOT called when reinstalling a binary package, only when it is actually recompiled.

## [Repeat for other packages]

### [Script to add sandbox]

The script below can be used to quickly set up sandbox for any package (remember to uncomment the correct line for sudo or doas). Read the comments!

[FILE] **`sandbox_user.sh`**

    #!/bin/bash

    [ $# -ne 4 ] && echo "Usage: $0 cat/package sandboxUser sandboxUserHome mainUser" && exit 1
    # Example: sudo ./sandbox-user.sh www-client/firefox firefox /home/firefox larry
    # If the script filename is different, adjust accordingly!

    pkg=$1
    sbuser=$2
    home=$3
    user=$4

    # Create the sandbox user and it's home directory, set the shell to /bin/false
    # so that nobody can login as the sandbox user and create and set a group with
    # the same name as the username.
    useradd --home=$home --create-home --shell /bin/false --user-group $sbuser || exit 1

    # Change the group of the sandbox user's home directory to the
    # "main user's" main group so that you can access the files there without sudo.
    chgrp $user $home || exit 1

    # Change the permissions so that only you and the sandbox user
    # can access the sandbox user's home directory.
    chmod 770 $home || exit 1

    # Make sure that sudoers.d exists, before adding files to it.
    mkdir --parents /etc/sudoers.d || exit 1

    # Add a config file for sudo, which allows the "main user" to execute
    # commands as the "sandbox user".
    echo "$user ALL=($sbuser) NOPASSWD: ALL" > /etc/sudoers.d/$sbuser || exit 1
    # Doas users uncomment:
    # echo "permit nopass $user as $sbuser" >> /etc/doas.conf

    # Change the permissions of the package's files so that only the
    # sandbox user can read and execute them.
    qlist -eo --showdebug "$pkg" | xargs -d "\n" chmod u-x,g-w,o-o || exit 1
    qlist -eo --showdebug "$pkg" | xargs -d "\n" chown root:$sbuser || exit 1

    portage_env="/etc/portage/env/$pkg"

    # Create a config file for portage which is specific to this package.
    # The file changes the permissions to the ones we set above on
    # every merge/update of the package, so that we don't loose them.
    mkdir -p $(dirname $portage_env) || exit 1
    echo "post_src_install()
       chown -R root:$sbuser \$
    }" > $portage_env || exit 1

### [Script to remove sandbox]

The script below can be used to remove any sandbox setup by the previous script. Read the comments!

[FILE] **`sandbox_user-remove.sh`**

    #!/bin/bash

    # !!!
    # It's best to reinstall the package to make sure
    # that all permissions are fixed.
    # !!!
    # Keep in mind, this script will delete the home directory of
    # the sandbox user, meaning any settings or other files present there,
    # will be removed. Make sure to backup anything you need from there!
    # !!!

    [ $# -ne 2 ] && echo "Usage: $0 cat/package sandboxUser" && exit 1
    # Example: sudo ./sandbox-user-remove.sh www-client/firefox firefox
    # If the script filename is different, adjust accordingly!

    pkg=$1
    sbuser=$2

    # Remove sandbox user and it's home directory.
    userdel --remove $sbuser || exit 1

    # Remove config file for sudo, which allowed
    # the "main user" to run commands as the "sandbox user".
    rm /etc/sudoers.d/$sbuser || exit 1

    portage_env="/etc/portage/env/$pkg"
    portage_env_dir=$(dirname $portage_env)

    # Remove the file for portage which changes the permissions
    # of the package's files on merge/update so that
    # only the sandbox user can run and read the files.
    rm $portage_env || exit 1

    # Remove the directory containing the configs if it's empty.
    [ -z "$(ls -A $portage_env_dir)" ] && rmdir $portage_env_dir || exit 1

## [][Configure Firefox to output sound to larry\'s PulseAudio daemon]

Add a Unix socket interface to larry\'s PulseAudio daemon:

`larry@gentoo $`` echo -e ".include /etc/pulse/default.pa\nload-module module-native-protocol-unix auth-anonymous=1 socket=/tmp/pulse-socket" > ~larry/.config/pulse/default.pa`

Tell ff\'s PulseAudio client to connect over this socket:

`root `[`#`]`echo -e "default-server = unix:/tmp/pulse-socket" > ~ff/.config/pulse/client.conf `

`root `[`#`]`chown ff:ff ~ff/.config/pulse/client.conf `

`root `[`#`]`chmod 644 ~ff/.config/pulse/client.conf `

Restart larry\'s PulseAudio daemon and Firefox should now be able to output sound.

Another way is to run per user separate daemons with \"pulseaudio \--start\" with configured \"PULSE_RUNTIME_PATH\" environment variable.

## [Firewall]

An added benefit of sandboxing is that we can now easily create program-specific firewall rules, by matching the running user. For instance:

`root `[`#`]`iptables -A OUTPUT -p TCP --dport https -m owner --uid-owner ff -j ACCEPT`

## [Drawbacks]

When larry clicks on links in other programs, they cannot open in ff\'s Firefox window. Instead, as a work-around, larry must copy the link, and paste in ff\'s Firefox window.

## [Missing icons]

When sandboxing a package and changing its permissions, the \"normal user\" will not be able to access any installed icons. The simplest solution to this problem is to install an icon theme like [[[x11-themes/papirus-icon-theme]](https://packages.gentoo.org/packages/x11-themes/papirus-icon-theme)[]] and set the [desktop environment](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") to use that instead of the default.

## [GPG managment]

### [Secret key import]

[GPG](https://wiki.gentoo.org/wiki/GPG "GPG") might ask for a password when importing a secret key. The default is to use a GUI/curses interface which needs access to /dev/pts/X. When importing a key with a \"sandboxed user\" using [sudo](https://wiki.gentoo.org/wiki/Sudo "Sudo"), that user won\'t have access to the /dev/pts/X device and importing will fail. The way around this is to use [\--pinentry-mode=loopback]:

`user `[`$`]`gpg --import --pinentry-mode=loopback key.gpg`

This will make all requests go back to the caller, meaning a simple password prompt on the shell that called the command.

### [Secret key deletion]

The same problem as importing arises when deleting a secret key. The issue is that, [\--pinentry-mode=loopback] [doesn\'t work](https://dev.gnupg.org/T3465) for some versions of [GPG](https://wiki.gentoo.org/wiki/GPG "GPG") when deleting secret keys. The alternative is to use [\--yes]:

`user `[`$`]`gpg --delete-secret-keys --yes <key-id>`

### [Git signing commits]

When [Git](https://wiki.gentoo.org/wiki/Git "Git") uses [GPG](https://wiki.gentoo.org/wiki/GPG "GPG") to sign commits, it will bump into the same problem as when importing the keys. The solution is to create a config file:

[FILE] **`/home/sandbox-user/.gnupg/gpg.conf`**

    pinentry-mode loopback

## [Problem with autotools]

When a package is sandboxed using the script in [Repeat for other packages](https://wiki.gentoo.org/wiki/Simple_sandbox#Repeat_for_other_packages "Simple sandbox"), the permissions for the .m4 files will be changed and there will be an error similar to this in a file similar to /var/tmp/portage/package-category/package-1.2.3/temp/aclocal.out:

    ***** aclocal *****
    ***** PWD: /var/tmp/portage/dev-lang/python-3.10.10_p2/work/Python-3.10.10
    ***** aclocal --system-acdir=/var/tmp/portage/dev-lang/python-3.10.10_p2/temp/aclocal

    aclocal-1.16: error: cannot open /usr/share/aclocal/package-1.2.m4: Permission denied

If the permissions are already changed by the script, first they must be changed manually to match the other .m4 files. If this isn\'t done, any other packages that are using autotools will fail with the same error on update or install.

The way to avoid this, is by adding the following line to post_src_install(): find \\\$ -type f -iname \\\"\*.m4\\\" -exec chmod 644  \\;

The function can be found in the [Repeat for other packages](https://wiki.gentoo.org/wiki/Simple_sandbox#Repeat_for_other_packages "Simple sandbox") section. If the package is already sandboxed, the line must be added to the /etc/portage/env/package-category/package file as well! When the line is added directly to the portage env file, it must be in the following writing: find \$ -type f -iname \"\*.m4\" -exec chmod 644  \\;

The paths must be changed to the appropriate ones for each particular case.

## [See also]

-   [SELinux](https://wiki.gentoo.org/wiki/SELinux "SELinux")