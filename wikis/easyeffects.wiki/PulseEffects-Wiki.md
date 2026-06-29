# PulseEffects Wiki

This page contains older documentation specific to PulseEffects and/or not converted to EasyEffects documentation. PulseEffects <= 4.8.7 is for PulseAudio users and is in maintenance mode.

If you use EasyEffects >= 6.0.0 you should not refer to this page, and instead look at the rest of the more actively maintained wiki.

This page is kept as one page for simplicity, although could be split into multiple pages if necessary.

# PulseEffects packages

The following packages are for PulseEffects and not EasyEffects.

## Debian / Ubuntu

### Ubuntu 19.10 and Newer, Debian 11 and Newer

Maintained inside Debian main repository by [hosiet](https://github.com/hosiet).

To install [pulseeffects](https://tracker.debian.org/pkg/pulseeffects) on latest Debian-based systems, run:
```
sudo apt install pulseeffects
```

### Ubuntu 18.04 and Newer, Debian 9 and Newer

Packages provided by [mikhailnov](https://github.com/mikhailnov).

To install PulseEffects on **Ubuntu** >= 18.04 (18.04, 18.10 etc.) and **Mint** >= 19 do:
```
sudo add-apt-repository ppa:mikhailnov/pulseeffects -y
sudo apt update
sudo apt install pulseeffects pulseaudio --install-recommends
```
PulseAudio >=12 is recommended (see [issue #99](https://github.com/wwmm/pulseeffects/issues/99)). It will be installed from this PPA. Ubuntu's patches are ported from Ubuntu 18.10 to 18.04.

**Restart the user session or reboot after this, because PulseAudio will be upgraded, and it may cause problems if you don't restart.**

These package _should_, but **probably won't** be compatible with recent releases of **Debian/Deepin** and other Debian-based distributions. To try installing PulseEffects on Debian/Deepin:
```
echo "deb http://ppa.launchpad.net/mikhailnov/pulseeffects/ubuntu bionic main" | sudo tee /etc/apt/sources.list.d/mikhailnov-ubuntu-pulseeffects-bionic.list
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys FE3AE55CF74041EAA3F0AD10D5B19A73A8ECB754 
echo -e "Package: * \nPin: release o=LP-PPA-mikhailnov-pulseeffects \nPin-Priority: 1" | sudo tee /etc/apt/preferences.d/mikhailnov-ubuntu-pulseeffects-ppa
sudo apt update
sudo apt install pulseeffects
```

## Gentoo

Packages provided by [prometheanfire](https://github.com/prometheanfire).

```
emerge media-sound/pulseeffects
```

## Flatpak

Provided by [Flathub](https://flathub.org/) and maintained by [AsavarTzeth](https://github.com/AsavarTzeth).

```
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install flathub com.github.wwmm.pulseeffects
```

The Flatpak manifest can be found here: <https://github.com/flathub/com.github.wwmm.pulseeffects>

## Mageia

PulseEffects will be available in the Mageia repositories from Mageia 7 onwards and may be installed directly from the Mageia Control Center.

## CRUX

PulseEffects is in the contrib repository, which needs to be activated on a clean install.
```
mv /etc/ports/contrib.rsync.inactive /etc/ports/contrib.rsync
ports -u contrib
prt-get depinst pulseeffects
```
Due to the nature of [CRUX](https://crux.nu), you might need to check the optional dependencies in the Pkgfile and install those when needed.

# HiDPI Display

The below section is a few years old--Wayland is default for KDE on Fedora as of October 2021.

In Windows and MacOS, display scaling is automatic and taken for granted. But in linux, it's a bit more complicated. Different Desktop Environments handle this differently and support is still relatively new with new display protocols like Wayland (fully supported on gnome, still spotty on kde, no other DE's supported yet) aiming to improve this situation (in addition to other things).

PulseEffects uses GTK 3 for the app GUI. Here is what you need to do to get proper scaling for PulseEffects on a HiDPI display

## KDE Plasma (Using XOrg - default for kde)
1. If monitor isn't already scaled, go to system settings -> Display and Monitor -> Displays -> Scale Display and move scale bar to 2. Otherwise, skip to step 2.
2. Run this in terminal so the panel will scale properly: `sudo sed -i 's/plasmashell/PLASMA_USE_QT_SCALING=1 plasmashell/g' /etc/xdg/autostart/org.kde.plasmashell.desktop`
3. Run this in terminal so GTK apps (like PulseEffects) scale properly: `echo -e "GDK_SCALE=2\nGDK_DPI_SCALE=-1" >> ~/.pam_environment`


# PulseEffects specific FAQ

Some of these are older questions that might not apply to EasyEffects, but maybe still apply to PulseEffects.


**Question 1**. When I try to [install from source](https://github.com/wwmm/easyeffects/wiki/Installation-from-Source) I get the following error: `wrong parameters to Project(), minimum project name and one language is required`. How do I solve this?

**Answer:** Your version of [Meson](http://mesonbuild.com/index.html) is too old. Try to install the latest one from the [Python Package Index](https://pypi.python.org/pypi/meson/). See the [official instructions for getting meson](http://mesonbuild.com/Getting-meson.html) for more information.

---

**Question 2**. Dark app theme doesn't work on KDE.

**Answer:** Go to System Settings -> Application Style -> Gnome Application Style (GTK). Check the GTK themes to your theme of choice, PulseEffects will follow the theme you set here. Then reboot and open PulseEffects, it should match that theme. However, if you do not wish to have a dark theme as a global default for GTK, you can alternatively use a light theme that comes with a dark pair (e.g. Breeze and its pair Breeze Dark). This will enable PulseEffects to toggle the dark mode on. 

---

**Question 3**. I can not enable effects for applications when using Deepin.

**Answer:** Try to disable audio from dconf (com.deepin.dde.daemon) and restart Deepin. See [#240](https://github.com/wwmm/easyeffects/issues/240)

--- 

**Question 4** - I don't want to use the CSD (Client Side Decoration) that comes with PulseEffects. 

**Answer:** You can install or compile [gtk3-nocsd](https://github.com/PCMan/gtk3-nocsd). You will still have the issue of having two windows titles so to solve this you can add `headerbar .title {color: transparent;}` into `~/.config/gtk-3.0/gtk.css`.

---

**Question 5** - I'm fine with CSD, but I'd like to get shadow or border around PulseEffects window in Plasma Desktop.

**Answer:** It's not possible to show a shadow for GTK CSD apps in Plasma Desktop, but you can draw a border adding `decoration {border: 1px solid black;}` into `~/.config/gtk-3.0/gtk.css`. You can also increase border size changing pixel value and use a custom color replacing `black` with another [CSS color name](https://www.w3schools.com/cssref/css_colors.asp). 

---

**Question 6** - After an upgrade PulseEffects stopped working. It crashes in the startup with a segfault.

**Answer:** This could be caused by a configuration problem. It is not clear yet why this is happening to some users after an upgrade. The command `dconf reset -f /com/github/wwmm/pulseeffects/` will reset PulseEffects configurations and may fix this.

---

**Question 7** - PulseEffects is available in my language, but I see it in English. Where do I can switch language?

**Answer:** You are probably using PulseEffects under Plasma 5 desktop environment. Sometimes Plasma makes a little mess with locale settings. Just delete `~/.config/plasma-locale-settings.sh` and restart the session.

---

**Question 8** - How to disable PulseEffects config when using headphones?

**Answer:** One solution for this is to create a preset where all plugins are disabled and create a preset autoloading profile that loads this preset when the headphone is plugged. 

---

**Question 9** - Input processing does not apply to Firefox - how to enable it?

**Answer:** See [this](https://github.com/wwmm/easyeffects/issues/957#issuecomment-830640221) comment. When Firefox asks which input device to use, choose "PulseEffects Source". Don't check "Remember this device", otherwise, the next time something uses your microphone, it'll use the default non-processed input, rather than PulseEffects Source.

# Community Presets

If you are a casual user simply searching for some bass boost, or you don't want to dive in the thousand of thousand options that PulseEffects offers, you'll be happy knowing that some users has created some presets, and maybe you could find the one you are searching for.

The following are the presets for Legacy PulseEffects (for output - speakers):

- https://github.com/Bundy01/EasyEffects-Presets (Bose, Music, Sony and Video)
- https://github.com/p-chan5/EasyPulse (A set of HQ presets for EasyEffects and PulseEffects)
- https://github.com/rkdhanda/PulseEffects-Preset
- https://github.com/Digitalone1/EasyEffects-Presets (Loudness Equalizer)
- https://github.com/eedeidk/PulseAudio-IRSs
- https://gist.github.com/Mlocik97/4e50977f27404fa62bde2d5f44e24581 (music preset, tested on Z333, old revision commit)
- https://github.com/Weeb-Linux/BambooSound
- https://github.com/qbarbosa/PulseEffects-Presets (music preset in gaming headset HyperX Cloud II)
- https://github.com/nick87720z/pulseeffect-dev-preset (device correction presets)
- https://github.com/herobrine30396/Pulseeffects-music-EQ (Crisp sound and bass-boosted)
- https://github.com/Rabcor/Heavy-Bass-EE/tree/pulseeffects

The following are the presets for Legacy PulseEffects (for input - microphone):
- https://gist.github.com/Mlocik97/03c87007af2a4af4ffc2f464e1e2b640 (laptops integrated mic)

# Installation
You can use the `Import Preset` button that is beside the `Add` preset button. But you can also do the process manually. Just copy the `.preset` files into the `PulseEffects` directory you can find in the local `config` directory. The location of that directory depends on how you installed the package. If you installed it through Flatpak, you can find it in `~/.var/app/com.github.wwmm.pulseeffects/config/easyeffects`, or if you used the PPA for Ubuntu (or the AUR package for Arch) it should be `~/.config/pulseeffects`

# Installation from Source

All commands in this section, unless otherwise specified, are expected to be run as an unprivileged user (not root). Whenever root privileges are necessary, `sudo` will be used. If `sudo` is unavailable you may become root using `su -`, at which point you may execute any command as the root user. Use `exit` to become a normal user again.

## Distribution Specifics

### Debian / Ubuntu

`The instructions for Debian based distributions are for PulseEffects. Help is needed to update these instructions for EasyEffects`

#### Debian >= 10 / Ubuntu >= 18.04

##### Building and Installing a Debian Package

###### 1. Clone the Repo

Clone the git repository and checkout the latest supported release. Unless you are testing the `master` branch of PulseEffects, you also want to checkout the [latest supported release](https://github.com/wwmm/pulseeffects/releases).

If you don't already have `git` installed, simply install it with `sudo apt install git`.

```
git clone https://github.com/wwmm/pulseeffects.git
cd pulseeffects
git checkout v4.7.2
```

*Substitute `v4.7.2` with the [latest release](https://github.com/wwmm/pulseeffects/releases).*

*Before building the package, check the version in [debian/changelog](https://github.com/wwmm/pulseeffects/blob/master/debian/changelog) and add a new changelog entry with the new version it if necessary.*
*Sidenote, v6.0.0 and up requires you to set changelog entries as `easyeffects` or else you will get a source package conflict error. Example:*
```
easyeffects (6.0.0) unstable; urgency=low
    * Changelog details
...
```

If you've made any changes, including `debian/changelog`, run `git add` to stage them in git, otherwise build deb will fail. You may run`git reset` after building the deb to unstage those changes in git.

Note that newest versions may not be buildable because debian specs are updated a bit later than other code.

###### 2. Install Build Dependencies

Install some Debian tools, needed for building the package.

```
sudo apt install devscripts equivs
```

Boost >= 1.72 is needed to build PulseEffects >= 4.7.2. If you are building on Ubuntu < 20.10, you will not find boost 1.72 in official repositories. You may add an [additional repository](https://launchpad.net/~mikhailnov/+archive/ubuntu/pulseeffects) where all build dependencies are available:

```
sudo add-apt-repository ppa:mikhailnov/pulseeffects
```

Now let's build and install a dummy package `pulseeffects-build-deps`, which will depend on all packages required to build the package.

```
sudo mk-build-deps --install debian/control
```

###### 3. Build the Package

To build your own package, simply run `debuild` from inside the source tree. `dpkg-buildpackage` options may be given on the command line.

Explanation of the options:

- The `-us -uc` flags builds the package without signing it. Since the package maintainer's private key is unavailable the package cannot be signed. Signing is unnecessary, unless a user plans to redistribute their package in their own repository.
- The `-i` flag will exclude the `.git` directory from the generated source tarball.

```
debuild -i.* -us -uc
```
*If `debuild` returns `dpkg-shlibdeps: error: no dependency information found for XXX` and you've built these dependencies from source, add this to the [debian/rules](https://github.com/wwmm/pulseeffects/blob/master/debian/rules) file*
```
override_dh_shlibdeps:
    dh_shlibdeps --dpkg-shlibdeps-params=--ignore-missing-info
```

*See the full `debuild` and `dpkg-buildpackage` manpage for more options.*

###### 4. Remove Build Dependencies (Optional)

At this point, you may remove the build dependencies if you wish to save some space. Although if you plan to build every release from source you might as well keep it.

```
sudo apt autoremove --purge pulseeffects-build-deps
```

###### 5. Install the Package

Build makes 3 deb packages located one directory bellow. Install all of them:

```
sudo apt install ../*pulseeffects*.deb
```

#### Debian <= 9 / Ubuntu <= 17.10

Old Debians and Ubuntus have old libraries, and PulseEffects cannot be compiled. Try using Flatpak or upgrading your distribution.