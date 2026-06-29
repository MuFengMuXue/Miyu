**Resources**

[[]][Home](https://www.android.com/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Android_(operating_system) "wikipedia:Android (operating system)")

[[]][GitWeb](https://android.googlesource.com/)

[[]][GitHub](https://github.com/android)

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Android "Project:Android")][Project](https://wiki.gentoo.org/wiki/Project:Android "Project:Android")

**Android** is an operating system developed by the [Open Handset Alliance](https://www.openhandsetalliance.com/oha_overview.html), led by Google, and mainly used on smartphones, tablets and multimedia boxes. It mainly runs on the **[ARM]** 6 and 7 architecture, but it has also been ported to **[x86]** and **[MIPS]**. It uses the Linux kernel with a custom userland which is Apache licensed.

Gentoo has some Android-specific packages:

-   [[[app-mobilephone/heimdall]](https://packages.gentoo.org/packages/app-mobilephone/heimdall)[]]
-   [[[app-mobilephone/scrcpy]](https://packages.gentoo.org/packages/app-mobilephone/scrcpy)[]]
-   [[[app-mobilephone/qtadb]](https://packages.gentoo.org/packages/app-mobilephone/qtadb)[]]
-   [[[dev-util/android-sdk-cmdline-tools]](https://packages.gentoo.org/packages/dev-util/android-sdk-cmdline-tools)[]]
-   [[[dev-util/android-studio]](https://packages.gentoo.org/packages/dev-util/android-studio)[]]
-   [[[dev-util/android-tools]](https://packages.gentoo.org/packages/dev-util/android-tools)[]]
-   [[[sys-fs/android-file-transfer-linux]](https://packages.gentoo.org/packages/sys-fs/android-file-transfer-linux)[]]

## Contents

-   [[1] [Setting up an Android dev environment without Android Studio]](#Setting_up_an_Android_dev_environment_without_Android_Studio)
-   [[2] [apktool]](#apktool)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

### [Setting up an Android dev environment without Android Studio]

To set up a development environment for Android without installing Android Studio (e.g. because you\'d prefer to use [[[app-editors/vim]](https://packages.gentoo.org/packages/app-editors/vim)[]] or [[[app-editors/emacs]](https://packages.gentoo.org/packages/app-editors/emacs)[]] for development):

-   Ensure none of the packages listed at the start of this page are installed, in order to avoid duplicate installations and potential conflicts.

<!-- -->

-   Install the [[[dev-java/openjdk-bin]](https://packages.gentoo.org/packages/dev-java/openjdk-bin)[]] or [[[dev-java/openjdk]](https://packages.gentoo.org/packages/dev-java/openjdk)[]] package:

`root `[`#`]`emerge openjdk-bin`

-   Install the [[[app-eselect/eselect-java]](https://packages.gentoo.org/packages/app-eselect/eselect-java)[]] package:

`root `[`#`]`emerge app-eselect/eselect-java`

and select the appropriate Java VM as the user under which you\'ll be doing development:

`user `[`$`]`eselect java-vm list`

    Available Java Virtual Machines:
      [1]   openjdk-bin-8
      [2]   openjdk-bin-17

`user `[`$`]`eselect java-vm set user openjdk-bin-17`

-   Install the [[[acct-group/android]](https://packages.gentoo.org/packages/acct-group/android)[]] package:

`root `[`#`]`emerge acct-group/android`

-   Add that user to the `android` group:

`root `[`#`]`gpasswd -a <USER> android`

-   Create a directory for the Android SDK, e.g. [\~/android]:

`user `[`$`]`mkdir ~/android`

-   Download the latest version of the Android platform-tools for Linux from [https://developer.android.com/tools/releases/platform-tools](https://developer.android.com/tools/releases/platform-tools) and unpack them in the SDK directory:

`user `[`$`]`unzip -d ~/android/ platform-tools_r34.0.5-linux.zip`

-   Download the latest version of Android cmdline-tools for Linux from [https://developer.android.com/studio#command-line-tools-only](https://developer.android.com/studio#command-line-tools-only) and unpack them in the SDK directory:

`user `[`$`]`unzip -d ~/android/ commandlinetools-linux-11076708_latest.zip`

-   Configure the relevant path environment variables for your shell (e.g. in [\~/.bash_profile]):

[CODE]

    export ANDROID_HOME="$/android"
    export PATH="$:$/platform-tools";
    export PATH="$:$/cmdline-tools/bin";

Apply the group and environment changes by logging the dev user out of any existing sessions, then logging that user back in again.

-   Use [sdkamanager] to list available platform SDK versions, and install the latest platform:

`user `[`$`]`sdkmanager --sdk_root=$/android --list`

`user `[`$`]`sdkmanager --sdk_root=$/android --install "platforms;android-34"`

-   Install the appropriate version of Android build-tools for that platform, and refresh cmdline-tools:

`user `[`$`]`sdkmanager --sdk_root=$/android --install "build-tools;34.0.0"`

`user `[`$`]`sdkmanager --sdk_root=$/android --install "cmdline-tools;latest"`

-   Review and accept the relevant licenses:

`user `[`$`]`sdkmanager --sdk_root=$/android --licenses`

Detailed information about environment variables affecting the Android SDK can be found at [https://developer.android.com/tools/variables](https://developer.android.com/tools/variables).

## [apktool]

[apktool](https://apktool.org/), available in the Pentoo overlay ([[[devutil/apktool::pentoo]](https://repos.gentoo.org/#pentoo)[]]), is a tool for reverse-engineering APK files (MIME type `application/vnd.android.package-archive`), including examining their contents. For example:

`user `[`$`]`apktool d app.apk -o ./contents/`

will extract the APK\'s files into a folder in the current directory called [contents].

## [See also]

-   [Android/Devices](https://wiki.gentoo.org/wiki/Android/Devices "Android/Devices") --- a list of mobile devices tested via the [stage3 tarball](https://wiki.gentoo.org/wiki/Project:Android/tarball "Project:Android/tarball") provided by the [Android project](https://wiki.gentoo.org/wiki/Project:Android "Project:Android").
-   [Android USB tethering](https://wiki.gentoo.org/wiki/Android_USB_tethering "Android USB tethering") --- the sharing of a mobile device\'s Internet connection with other connected computers.
-   [mksh](https://wiki.gentoo.org/wiki/Mksh "Mksh") --- an actively developed free implementation of the Korn Shell programming language and a successor to the Public Domain Korn Shell
-   [Android/adb](https://wiki.gentoo.org/wiki/Android/adb "Android/adb") --- Android Debug Bridge
-   [Android/Fastboot](https://wiki.gentoo.org/wiki/Android/Fastboot "Android/Fastboot") - Android Bootloader
-   [[[app-emulation/genymotion-bin]](https://packages.gentoo.org/packages/app-emulation/genymotion-bin)[]] - old forum post about using [Genymotion](https://forums.gentoo.org/viewtopic-p-7682800.html#7682800) from other overlays. The main package repo is more up to date.
    -   Note: genymotion will require an external account to be made with the company to use the emulator
-   [Android/SharkBait](https://wiki.gentoo.org/wiki/Android/SharkBait "Android/SharkBait") --- A project to create a recognizable identity and foster development of [Portage-powered Android](https://wiki.gentoo.org/wiki/Google_Summer_of_Code/2018/Ideas/Portage_powered_Android "Google Summer of Code/2018/Ideas/Portage powered Android").

## [External resources]

-   [Home page for Android Studio](https://developer.android.com/studio/)
-   [Home page for Android NDK](https://developer.android.com/ndk/)