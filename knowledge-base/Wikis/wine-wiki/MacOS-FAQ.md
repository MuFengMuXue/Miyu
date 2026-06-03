See also the [general Wine FAQ](FAQ)

#### What is the difference between Wine and Darwine?

[Darwine](https://sourceforge.net/projects/darwine/) was the original
effort to port Wine to Macs Running macOS and consisted of 2 major
efforts.

1.  *PowerPC* Macs - attempted to integrate
    [QEMU](https://fabrice.bellard.free.fr/qemu/) into Wine for x86 CPU
    emulation
2.  *Intel x86*

Wine for macOS x86 has now merged into main Wine project, here at
WineHQ. Darwine is **no longer actively developed**.

#### What does Wine on macOS support? (DirectX, DirectSound, Direct3D...)

- [Sound](Sound) should be working just fine since Wine
  release 0.9.15.
- [MIDI](MIDI) output (via Apple's built-in software
  synthesizer) works.
- 3D (OpenGL Support) works. Note that due to Apple's X11 often being
  outdated, we recommend you install
  [XQuartz](https://xquartz.macosforge.org), available since 10.5
  Leopard, which closely follows Xorg development. Since macOS 10.5.7,
  Apple X11 may be good and recent enough for wine 3D usage.
- *Full screen mode* works in a Wine release as old as 1.1.24. However,
  there are too many restrictions to make it generally useful:
- Unlike CodeWeaver's X server packaged with their CrossOverMac product,
  Apple's X11.app will *not change the screen resolution*. So your app
  must support your monitor's likely huge native resolution, e.g.
  1600x1200. If your app knows only 800x600 and 1024x768, it will not
  start and may even crash.
- Some modern apps, although they may support your monitor's resolution
  during play, start with logos and intro animations that want to open a
  screen at 640x480 or 800x600. This will fail and may cause your
  application not to start at all or even crash. For instance, the game
  2weistein - Das Geheimnis des roten Drachen - works well in full
  screen, yet the screen stays black at start, trying to display the
  first intro animation, while the subsequent second logo, intro movie
  and game logo all scale nicely to full screen.
- The X11 menu bar will remain visible at all times. The app sees a
  screen resolution 22 pixel less than it really is, e.g. 1600x1178.
- The dock will stay in front of the fullscreen window. Use its
  auto-hide feature to get rid of it.
- "Always on top" windows remain atop Wine's fullscreen window, e.g.
  window \#3 of the CPU% activity meter -- exactly like they do in
  TimeMachine's full screen display. Just close or hide them.
- Running a Fullscreen program in a Wine Virtual Desktop window should
  work fine
- Starting in Xquartz 2.6.0 (available Oct-Nov 2010), RandR and
  resolution changing should be working on Macs.
- mcicda.dll does not work (bug #20323), so apps will
  not play music off CD tracks.
- Multi-CD installs work, using the \`wine eject\` command.
- More generally, CD-ROM support is incomplete, so Wine will not start
  many copy-protected apps.

#### How do I change settings?

- If you built a plain wine: run `/path/to/your/wine winecfg` as on any
  other UNIX.
- Audio output will only be enabled after you ran winecfg to configure
  it.

#### Where are Wine's settings stored?

In your home folder (`/Users/`<username>`/` resp. `~/`) in the hidden
folder `.wine`. You can get into (even hidden) folders in the Finder by
pressing Shift+Command+G and entering the path, for example `~/.wine`.

You can make the hidden folder "visible" by creating a symbolic link:
`ln -s ~/.wine wine` in Terminal.app.

#### How can I switch the locale?

This Wiki and other Wine documentation mention setting the environment
variable LANG. This works for UNIX but deliberately does not work with
Wine on MacOS for reasons enumerated in [this
comment](https://gitlab.winehq.org/wine/wine/-/blob/wine-4.0/dlls/kernel32/locale.c#L1027)
Instead, set the variable LC_MESSAGES, e.g. use
`LC_MESSAGES=ja_JP.UTF-8 wine japanese.exe` or `LC_MESSAGES=ja_JP.SJIS`
or `LC_MESSAGES=fr_FR.UTF-8`

#### Will there be a PowerPC version (or will there be a way to run Wine on a PowerPC processor)?

[Darwine](https://darwine.sourceforge.net/) was the effort to port Wine
to PowerPC processors. Darwine is **NO LONGER ACTIVELY DEVELOPED**.

#### Where can I get a working Wine for Intel Macs?

1.  WineHQ builds packages for macOS 10.8 and higher.
2.  You can compile wine from source with XCode and
    [XQuartz](https://xquartz.macosforge.org). See
    [macOS/Building](MacOS-Building) for additional
    troubleshooting and directions.
3.  If you are a [Fink](https://www.finkproject.org/) or
    [MacPorts](https://www.macports.org/) user, consider installing the
    wine or wine-devel package.
4.  You can also check out the [Third Party
    Applications](Third-Party-Applications) page for info
    about other Apps that use Wine that may be much easier to use than
    building Wine yourself. Note that these products are not supported
    here, so please do not file bugs, submit AppDB test reports, or ask
    for help on the forum or in IRC if using one.

#### All 16 bit applications crash in winevdm.

This is radar://5935237 bug in Apple's linker, which affects XCode older
than 3.2.x. It is reflected in bug #14920. 32bit apps are not affected.

Workarounds:

- Build wine yourself with win16 support
  - macOS 10.4 Tiger: compile using Xcode 2.x b. macOS 10.5 Leopard:
    patch Xcode linker bugs, then compile
  - download the ld64 linker patch as described in [Bug 14920
    comment 29](https://bugs.winehq.org/show_bug.cgi?id=14920#c29)
  - apply the ld64 linker patch as described in [Bug 14920
    comment 38](https://bugs.winehq.org/show_bug.cgi?id=14920#c38)
- macOS 10.6 Snow Leopard or later: compile using Xcode 3.2.x or later

#### How do I right-click in Wine on macOS?

Control-click, as you're probably used to, won't work in wine (so far?).
Workaround: Enable secondary click by tapping the trackpad with two
fingers. Therefor go to System Preferences \> Keyboard & Mouse \>
Trackpad and enable 'Tap trackpad using two fingers for secondary
click'. You can then do the right clicks by tapping the trackpad with
two fingers. Update: if you are running a current version of Xquartz,
you can go into the X11.app preferences when it's running and select
what you want to be modifier keys for right and middle clicks.

#### How come my keyboard shortcuts don't work like normal

Wine by default maps the keys differently than native macOS
applications. It's possible to change some of the keyboard mappings
depending on the version of wine being used.

- Since Wine 1.7.4 its possible to map Option as Alt by adding the
  following using regedit

  ```
  [HKEY_CURRENT_USER\Software\Wine\Mac Driver]
  "LeftOptionIsAlt"="Y"
  "RightOptionIsAlt"="Y"
  ```

- Since Wine 3.17 it's possible to map Command as Ctrl meaning
  CMD+C/CMD+V now functions like Native applications

  ```
  [HKEY_CURRENT_USER\Software\Wine\Mac Driver]
  "LeftCommandIsCtrl"="Y"
  "RightCommandIsCtrl"="Y"
  ```

#### How to launch wine from terminal instead of the wine application?

To do this we need to add the wine application to the PATH variable

To do that we do the following

    nano .profile

Then copy in the following

    #export PATH="/Applications/Wine Staging.app/Contents/Resources/wine/bin:$PATH"
    #export PATH="/Applications/Wine Devel.app/Contents/Resources/wine/bin:$PATH"
    export PATH="/Applications/Wine Stable.app/Contents/Resources/wine/bin:$PATH"
    export FREETYPE_PROPERTIES="truetype:interpreter-version=35"
    export DYLD_FALLBACK_LIBRARY_PATH="/usr/lib:/opt/X11/lib:$DYLD_FALLBACK_LIBRARY_PATH"

Comment out `Wine Stable` uncomment out the one you want to be added for
use within terminal. To save press Ctrl+X then press Enter to save the
file. Now any new terminal session will have `wine` from available the
chosen wine application for the current user.

#### How to create shortcut, launcher, or .app to start a given .exe?

##### Instructions on making .app file launcher

This is for real Wine, installed to /usr/local. It can be modified to
work with Macports Wine.

- Open up Apple's Script Editor
  - in macOS 10.6 to 10.9 this is "/Applications/Utilities/Applescript
    Editor.app"
  - in macOS 10.4 and 10.5 this is "/Applications/AppleScript/Script
    Editor.app"
  - in macOS 10.10 and up, this is "/Applications/Utilities/Script
    Editor.app"
- Copy and paste the following code into Script Editor:

    ```
    on run

       --edit this to be the correct location and file to run (typically only edit after the "drive_c")
       set toRun to "$WINEPREFIX/drive_c/Program Files/MyProgram/MyProgramName.exe"

       --edit winePrefix if you are not using the default prefix
       set winePrefix to "$HOME/.wine"

       --edit wineLocation if your wine install is not the default location
       set wineLocation to "/usr/local/bin"

       --edit dyldFallbackLibraryPath to your X11 lib folder, this one is set for XQuartz on 10.6+
       set dyldFallbackLibraryPath to "/opt/X11/lib"

      --Setting freetype rendering to 35 fixes blurred fonts when using newer freetype versions
      set freetypefix to "truetype:interpreter-version=35"
       -------------------------------------------------------
       --DO NOT EDIT ANYTHING BELOW THIS LINE
       -------------------------------------------------------
       set toRunPath to do shell script "WINEPREFIX=\"" & winePrefix & "\"; TEMPVAR=\"" & toRun & "\"; echo \"${TEMPVAR%/*}\""
       set toRunFile to do shell script "WINEPREFIX=\"" & winePrefix & "\"; TEMPVAR=\"" & toRun & "\"; TEMPVAR2=\"" & toRunPath & "\"; echo \"${TEMPVAR#$TEMPVAR2/}\""
       do shell script "PATH=\"" & wineLocation & ":$PATH\"; export WINEPREFIX=\"" & winePrefix & "\"; export DYLD_FALLBACK_LIBRARY_PATH=\"" & dyldFallbackLibraryPath & "\"; export FREETYPE_PROPERTIES=\"" & freetypefix & "\"; cd \"" & toRunPath & "\"; wine \"" & toRunFile & "\" > /dev/null 2>&1 &"

    end run
    ```

- Edit the program per the directions in the lines that start with --
- if everything is default, you only need to edit the "set toRun" line
- After you have edited it for your program, save it as an "Application"
  (not a script) in the script editor
- this will create a .app for you that you can double click to run what
  you specified.

It might start up a bit slow with no visual indicators... sometimes, be
patient

##### Instructions on making custom launcher what invokes Terminal

- Using TextEdit create text file with following contents:

```sh
#!/bin/sh
export WINEPREFIX="$HOME/.wine"
export DYLD_FALLBACK_LIBRARY_PATH=/usr/X11/lib
export FREETYPE_PROPERTIES="truetype:interpreter-version=35"
cd "/where/is/my/app/"
wine "myapp.exe"
```

- The $HOME, in the beginning of the path, will expand to the home
  directory, in case of user Me, it will expand to /Users/Me
- The dot(.) in the WINEPREFIX folder will make it invisible, you can
  omit the dot to leave folder visible and easier to work with
- By default, wine uses `/Users/YourUsername/.wine` prefix, you can be
  creative and use other prefixes and paths to store multiple prefixes
- If you need to define other constants for wine e.g.
  `export WINEDEBUG=fixme-d3d,warn+heap,+debugstr` or
  `export LC_ALL=ru_RU.UTF-8`, add all of them before the `cd` command.
- If the program is inside the wine prefix, `cd` might look something
  like this: `cd "$WINEPREFIX/drive_c/Program Files/theprogram/"`
- In case you want to use custom path to wine, you may replace \`wine\`
  on the last line with `/path/to/wine/wine`
- Some programs may still have trouble starting, you can try to replace
  `wine "myapp.exe"` with
  `wine start /unix "$HOME/where/is/my/app/myapp.exe"`

After making all customizations, save the launcher file as regular .txt
file. Next, in the Finder, click on saved launcer file, then press
Command+I (Get Info) and replace the `.txt` with `.command` which is an
extension that Mac OS uses for shell (and perl, Python, tcl) scripts.
Alternatively, you can remove file extension altogether.

Next, you need to give launcher file executive permissions. Open the
Terminal and execute `chmod +x path/to/my/something`, where
path/to/my/something is the path to the launcher file.

- You can always change the code of the launcher by opening it with the
  TextEdit again. After adding changes, simply save the launcher file
  without renaming.

**Optional: Changing the icon of the launcher file**

On the macOS, it is possible to change the icon of any file to anything
you desire.

**NOTE:** In some cases, your custom icon will not display if launcher
file has extension. Refer to previous steps on how to rename the
launcher.

Look into the hidden `~/.local/share/icons/` directory, where Wine
keeps the icons created by application installers (.xpm and .png files);
they would display on a Linux desktop.

In some cases, you will need to manually extract the icon from the .exe
file. This can be done using tools like Resource Hacker. This tutorial,
however, will not cover the process of doing it. It is assumed, that you
have the application icon in the `.ico` or `.png` format.

Now that you have your icon file ready, open it with the Preview. In
case of .ico it might have multiple frames/images inside, select
appropriate one. Press Command+C (Edit\>Copy). Next, in the Finder,
click on the launcher file, then press Command+I (Get Info). In the top
left corner of the launcher info, there will be a small image showing
current icon, click on it to highlight it. Press Command+V to paste your
icon. If everything goes well, the icon of your launcher will change.

#### Why is it building font metrics? This may take some time...

Actually, there are *two* bugs involved:

1.  Bug #17674 "wine recaching font metrics on every run", consuming upto 30 seconds at
    program start. This is fixed in wine-1.1.31.
2.  However, there is **no need to cache font metrics at all** as Wine
    should find a FreeType library greater than 2.0.5 because one is
    included in MacOS. If your Wine exhibits this problem, you probably
    need to set the `DYLD_FALLBACK_LIBRARY_PATH` environment variable
    before launching Wine.

Start wine (in a Terminal) as follows:

`DYLD_FALLBACK_LIBRARY_PATH=/usr/X11/lib wine myapp.exe `

or

`export DYLD_FALLBACK_LIBRARY_PATH=/usr/X11/lib wine myapp.exe `

You may [patch the main wine launcher
yourself](https://www.winehq.org/pipermail/wine-patches/2009-July/075290.html)
and forget about this variable. Save this patch file, then invoke
`patch -p1 < mypatch.txt` in a Terminal, while at the top of Wine's
source directory, see [macOS Building](MacOS-Building).

Both MacPorts and Fink use a wrapper to the wine launcher which sets
exactly this variable.

#### How do I switch between the Mac/X11 drivers?

As of 1.5.28, the Mac driver is the default driver. If on an older
release, you can force using the Mac driver by either:

```sh
$ unset DISPLAY
```

Or by editing the registry key "graphics" under
`HKCU\Software\Wine\Drivers`. It should specify the load order, e.g.,
"mac,x11"
