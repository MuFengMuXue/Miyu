Wine on Android was first presented at
[FOSDEM 2014](WineConf/FOSDEM-2014).

### Installing

Download the apk from our Download site and search the Internet for
"install apk android" for instructions how to sideload the apk on your
Android version.

### Building

In case you want to build it yourself, the raw steps are:

1.  Download the current Android NDK and SDK
2.  Use build/tools/make_standalone_toolchain.py in the NDK to create a
    toolchain
3.  Add the toolchain to your PATH and correctly set ANDROID_HOME and
    NDK_SYSROOT
4.  Crosscompile libpng and freetype for Android using the toolchain
5.  Run Wines configure with correct parameters for --host= and
    --with-wine-tools= as well as information how to find libpng and
    freetype built before
6.  After a successful "make" the apk can be found in
    dlls/wineandroid.drv/

### Keyboard Issue

Currently the Keyboard won't pop up by itself as you would expect it. A
workaround is to install the App ["Hacker's
Keyboard"](https://github.com/klausw/hackerskeyboard) from F-Droid or
the Play Store. Then open its settings and check "Use permanent
notification". Now, when running Wine you can swipe down the
notification area to enable the keyboard when you need it.

### Debugging

Search the Internet how to get adb shell access for your Android device.
In that shell you can then run "run-as org.winehq.wine" to get into the
correct folder and become the same user as the App files expect. Under
files/ you can then set debug channels (e.g. ddraw) by writing them into
a file called winedebug: "echo ddraw \> files/winedebug".

### Bugs

There are some bugs on newer Android Versions, which might not be fixed
soon.

  - #44245
  - #45060

### Running Windows/x86 Applications

See [Emulation](Emulation)

### See also

- [Presentation slides](/media/Wine-on-android-wineconf2014.pdf)
