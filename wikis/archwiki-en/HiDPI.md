# HiDPI

HiDPI (High Dots Per Inch) displays, also known by Apple's "Retina display" marketing name, are screens with a high resolution in a relatively small format. They are mostly found in high-end laptops and monitors.

Not all software behaves well in high-resolution mode yet. Here are listed most common tweaks which make work on a HiDPI screen more pleasant.

## Background
The terminology in this space can be misleading. Prior to HiDPI, the terms were:

* Dots per inch (DPI)—specifies the output density of ink droplets when printing a paper. Higher dots-per-inch correspond to a more dense output.
* Pixel density, pixels per inch (PPI)—specifies the input density of a digital image. [https://www.adobe.com/uk/creativecloud/photography/discover/pixels-per-inch-ppi-resolution.html Computed as .

Every display has an intrinsic PPI as the ratio of native screen resolution to physical screen size. Although some technical sources use the term "PPI", [https://github.com/hyprwm/Hyprland/blob/5ca48231287d67e75a3f21dbdbc47d6dc65752c4/src/helpers/Monitor.cpp#L563-L579 it is much more common to (inaccurately) refer to this ratio as DPI. 96 DPI screens are regarded as comfortable for most people to read ~12pt font on, and is about where most "low-DPI" monitors fall. HiDPI screens are around 192 DPI and greater, with some screens falling in the middle ("medium PPI").

When using a HiDPI screen on a DPI-unaware system which assumes a DPI of ~96, small fonts will be uncomfortable to read. Since font rendering is relatively easy to adjust, even "DPI-unaware" systems (such as #Wine applications) often provide a knob for adjusting the font DPI. Whenever a DPI setting is exposed as a number (as opposed to a multiplier or a percentage), it is likely referring to the text rendering alone.

Most modern GUI toolkits are capable of "integer scaling", rendering the UI at least 2x size. This is achieved by applying a different font DPI as well as providing HiDPI versions of assets. Some toolkits also support fractional scaling, with GTK #Fractional scaling using a combination of applying arbitrary font DPI and downscaling graphical resources.

On a desktop which is otherwise using UI scaling, applications that lack resolution independence (such as #Xwayland) may render at 1x scale and then be scaled up by the display server.

## Desktop environments
## GNOME
To enable HiDPI, navigate to Settings > Devices > Displays > Scale and choose an appropriate value. Or, use gsettings:

 $ gsettings set org.gnome.settings-daemon.plugins.xsettings overrides "}"
 $ gsettings set org.gnome.desktop.interface scaling-factor 2

## Fractional scaling
A setting of , , etc, which is all you can do with , may not be ideal for certain HiDPI displays and smaller screens (e.g. small tablets). Fractional scaling is possible on both Wayland and Xorg, though the process differs.

Implementation was mainly discussed and decided in GNOME fractional scaling hackfest 2017, check for more technical details.

## Wayland
Enable the experimental fractional scaling feature:

 $ gsettings set org.gnome.mutter experimental-features "['scale-monitor-framebuffer'"

then open Settings > Devices > Displays (the new options may only appear after a restart).

To enable the option for all users, create the following three files with the corresponding content

Then run  and restart the machine. This will permanently lock the option.

## Xwayland
As of Mutter 47.0 it is possible to enable native fractional scaling as an experimental feature.

Enable it by issuing:

 $ gsettings set org.gnome.mutter experimental-features "'xwayland-native-scaling'"

## Text Scaling
Alternatively, or in addition to changing the display scaling, you can separately scale text. This can be done by navigating to Fonts > Scaling Factor in Gnome Tweaks, or using gsettings. Note that the text scaling factor need not be limited to whole integers, for example:

 $ gsettings set org.gnome.desktop.interface text-scaling-factor 1.5

## GTK+ vs Gnome Shell elements on Xorg
Adjusting the text scaling as per the above only affects GTK+ elements of the GNOME desktop. This should cover everything on Wayland. However, those on an Xorg session may find that they need to make further adjustments on HiDPI environments, since the GNOME Shell UI (including the top bar, dock, application menus, etc.) relies separately on the St toolkit. Note that this is a long-standing issue to which a patch has been merged and available for Gnome Shell 3.35 onward. For older releases, Xorg users can resolve most of the Gnome shell scaling problems by manually editing the shell theme that they are currently using. The relevant CSS files are normally located at . Users should increase all "font-size" elements in this file in proportion to their display scaling (doubling font sizes for 200% scaling, etc.) For example, the top of an edited CSS file for the  shell theme might look like:

{{hc|/usr/share/themes/Adapta/gnome-shell/gnome-shell.css|2=
stage { font-size: 20pt; font-family: Roboto, Noto Sans, Sans-Serif; color: #263238; }
}}

Once these changes have been saved, activate them by switching to another theme (for example, using ) and then reverting back again. The top bar, application menus, calendar, and other shell elements should now be correctly scaled.

In addition to editing the relevant shell theme's CSS file, users on Xorg may also wish to increase the title bar font at the top of open applications. This can be done through the dconf editor (). Note that the  option should also be turned off. Alternatively, use gsettings:

 $ gsettings set org.gnome.desktop.wm.preferences titlebar-font 'Cantarell Bold 22' ## Change as needed
 $ gsettings set org.gnome.desktop.wm.preferences titlebar-uses-system-font false

## KDE Plasma
You can use Plasma's settings to fine tune font, icon, and widget scaling. This solution affects both Qt and GTK applications.

To adjust font, widget, and icon scaling together:

# System Settings > Display and Monitor > Display Configuration > Global Scale
# Drag the slider to the desired size
# Restart for the settings to take effect

However, using X11 session, Plasma ignores the Qt scaling settings by default, which affects panels and other desktop elements. To make Plasma respect the Qt settings, set .

## Cursor size
To adjust cursor size:

# System Settings > Appearance > Cursors > Size

## Font scaling
To adjust only font scaling:

# System Settings > Appearance > Fonts
# Check "Force fonts DPI" and adjust the DPI level to the desired value. This setting should take effect immediately for newly started applications. You will have to logout and login for it to take effect on Plasma desktop.

## Icon scaling
To adjust only icon scaling:

# System Settings > Appearance > Icons > Advanced
# Choose the desired icon size for each category listed. This should take effect immediately.

## Panel scaling
To adjust only panel scaling:

# Right click the panel, select Enter Edit Mode, and manually adjust Panel height.

## Xwayland
As of Plasma 5.26, the Xwayland scale method can be chosen at the bottom of the System Settings > Display and Monitor > Display Configuration page.

In "Scaled by the system" mode, the X application will be rendered at 1x and then magnified (scaled) by KDE. This works for all applications, but causes blurriness due to the magnification.

In "Apply scaling themselves" mode, the X application will have to render itself at the appropriate size. This will avoid blurriness, but applications which aren't HiDPI-aware will render themselves at 1x scale and therefore will appear small.

See this blog post for details.

## Xfce
Xfce supports HiDPI scaling which can be enabled using the settings manager:

# Go to Settings Manager > Appearance > Settings > Window Scaling and select 2 as the scaling factor.
# Go to Settings Manager > Window Manager > Style and select  theme.

Alternatively, it is possible to do the same from command line using xfconf-query:

 $ xfconf-query -c xsettings -p /Gdk/WindowScalingFactor -s 2
 $ xfconf-query -c xfwm4 -p /general/theme -s Default-xhdpi

After either of the above changes, fonts in some GTK applications may still not be scaled; you may additionally do the following (see #GDK 3 (GTK 3)):

# Go to Settings Manager > Appearance > Fonts > Custom DPI setting and change from 96 to 192
# Set the environment variable  to un-scale some fonts that would be scaled twice.

The steps above would set 2x scaled resolution for Xfce and other GTK 3 applications.

Scaling for Qt 5 applications should be set manually, see #Qt 5. Note that if you set a Custom DPI for fonts above, you likely need to set  to avoid double-scaling of fonts in Qt applications.

## Cinnamon
Has good support out of the box.

## Enlightenment
For E18, go to the E Setting panel. In Look > Scaling, you can control the UI scaling ratios. A ratio of 1.2 seems to work well for the native resolution of the MacBook Pro 15" screen.

## LXDE
In general, the generic X Server settings apply. To change the size of the mouse cursor, edit the file  and change the value of .

## Wayland compositors
## Sway
See Sway#HiDPI.

## Hyprland
See Hyprland#Setting screen resolution.

## X Resources
If you are not using a desktop environment such as KDE, Xfce, or other that manipulates the X settings for you, you can set the desired DPI setting manually via the  variable in Xresources:

For , using integer multiples of 96 usually works best, e.g. 192 for 200% scaling.

Make sure the settings are loaded properly when X starts, for instance in your  with  (see Xresources for more information).

This will make the font render properly in most toolkits and applications, it will however not affect things such as icon size!
Setting  at the same time as toolkit scale (e.g. ) may cause interface elements to be much larger than intended in some programs like firefox.

## X Server
Some programs may still interpret the DPI given by the X server (most interpret X Resources, though, directly or indirectly). Older versions of i3 (before 2017) and Chromium (before 2017) used to do this.

To verify that the X Server has properly detected the physical dimensions of your monitor, use the xdpyinfo utility from the  package:

This example uses inaccurate dimensions (423mm x 238mm, even though the Dell XPS 9530 has 346mm x 194mm) to have a clean multiple of 96 dpi, in this case 192 dpi. This tends to work better than using the correct DPI — Pango renders fonts crisper in i3 for example.

If the DPI displayed by xdpyinfo is not correct, see Xorg#Display size and DPI for how to fix it.

## GUI toolkits
## Qt 5
Since Qt 5.6, Qt 5 applications can be instructed to honor screen DPI by setting the  environment variable. Qt 5.14 introduced a new environment variable  which replaces the  variable. It is recommended to set both environment variables for maximum compatibility:

 $ export QT_AUTO_SCREEN_SCALE_FACTOR=1
 $ export QT_ENABLE_HIGHDPI_SCALING=1

If automatic detection of DPI does not produce the desired effect, scaling can be set manually per-screen (/) or globally (). For more details see the Qt blog post or Qt developer documentation.

An alternative is e.g.:

 $ QT_FONT_DPI=96 clementine

## GDK 3 (GTK 3)
Setting the GDK scale (in X11, not Wayland) will scale the UI; however, it will not scale icons. If you are using a minimal window manager where you are setting the dpi via Xft.dpi, GDK should scale perfectly fine with it. In other cases, do the following:

To scale UI elements by an integer only factor:

 $ export GDK_SCALE=2

GTK3 does not support fractional scaling currently, so fractional factors will be ignored. This environment variable is also ignored in mutter wayland sessions.

GTK4 supports fractional scaling since 4.14 under Wayland.

 can be used to scale text only. To undo scaling of text, fractional scale can be used:

 $ export GDK_DPI_SCALE=0.5

Under GTK3/4 it not currently possible to scale icon sizes, unless the application explicitly implements a way to do so. See bug report #4528. If you need this feature, use Qt when possible.

## GTK 2
Scaling of UI elements is not supported by the toolkit itself, however it is possible to generate a theme with elements pre-scaled for HiDPI display using .

## SDL
SDL3 windows are marked to the compositor as DPI-aware, by default. For incompatible applications, this can be disabled via the SDL_HINT_VIDEO_WAYLAND_SCALE_TO_DISPLAY hint. This is done either by the application itself via the SDL hint API, or by setting the environment variable:

 $ export SDL_VIDEO_WAYLAND_SCALE_TO_DISPLAY=1.

By default,  forces 1:1 scaling (non-DPI-aware) using this hint,with some per-application exceptions.[https://github.com/libsdl-org/sdl2-compat/blob/1c8ece4de9db96d01f99296c26a87a4cabb72f54/src/sdl2_compat.c#L492-L504

## Electron
Electron applications (e.g. , , etc.) can be configured to always use a custom scaling value by adding a  flag to the .desktop file. Electron packages in the official repositories and packages that use them, can be configured with a configuration file.

Desktop files are normally located at , and can normally be overridden on a per-user basis by copying it to . The flag should be added to the line beginning with "Exec=". For example:

## Elementary (EFL)
To scale UI elements by a factor of 1.5:

 export ELM_SCALE=1.5

For more details see https://phab.enlightenment.org/w/elementary/

## GNUstep
GNUstep applications that use its gui (AppKit) library accept a  property in their defaults (STEP preferences). To define a scaling factor of 1.5 for all applications:

 defaults write NSGlobalDomain GSScaleFactor 1.5

Note that you must also disable font hinting by setting the value of  to 17, else text rendering will look broken when rendering long lines.

 defaults write NSGlobalDomain GSFontHinting 17

Some automatic detection was possible back in 2011, but the code responsible for the X11 backend was commented out thereafter.

## FLTK
FLTK 1.3, the default FLTK version available in Arch Linux, does not support resolution scaling. Support will arrive when applications start using FLTK 1.4.

## AvaloniaUI (C# / .NET)
 can be used to scale. To undo scaling, fractional scale can be used:

 $ export AVALONIA_GLOBAL_SCALE_FACTOR=0.5

For per monitor configuring see avalonia wiki].

## Boot managers
## GRUB
## Lower the framebuffer resolution
Set a lower resolution for the framebuffer as explained in GRUB/Tips and tricks#Setting the framebuffer resolution.

## Change GRUB font size
Find a ttf font that you like in .

Convert the font to a format that GRUB can utilize:

 # grub-mkfont -s 30 -o /boot/grubfont.pf2 /usr/share/fonts/FontFamily/FontName.ttf

Edit  to set the new font as shown in GRUB/Tips and tricks#Background image and bitmap fonts:

 GRUB_FONT="/boot/grubfont.pf2"

Finally regenerate the main configuration file.

## systemd-boot
Set a lower resolution for the console through  as explained in systemd-boot#Loader configuration and .

## Applications
If you are running a Wayland session, but application is running via Xwayland (either because it does not support Wayland natively or because it uses X11 by default), you could still get blurry fonts and interface, even if the application supports HiDPI. See this bug report. See also Wayland#Detect Xwayland applications.

## Browsers
## Firefox
Firefox should use the #GDK 3 (GTK 3) settings. However, the suggested  suggestion does not consistently scale the entirety of Firefox, and does not work for fractional values (e.g., a factor of 158DPI/96DPI = 1.65 for a 1080p 14" laptop). You may want to use  instead. Another option, which will avoid Firefox-specific settings in many setups is to use the settings in #X Resources as Firefox should respect the  value defined there.

To view the internal UI scaling settings of Firefox, open the advanced preferences page () and check those parameters:

* : Set it to true to enable fractional scaling on wayland. Otherwise, on some desktop environments (e.g., KDE on wayland), Firefox may be double scaled. For example, if you set the screen scale to 150% in plasma system settings, Firefox will enlarge to 200% first and then be down-scaled to 150%, so all fonts look blurry.
* : The actual parameter that controls UI scaling.  for 125% scaling,  for 150%, and so on. Default is  (follow the system's HiDPI setting).

If you use a HiDPI monitor such as Retina display together with another monitor, you can use the ffreszoom add-on, which will adjust the page zoom if it detects you are using a large monitor (zoom level and threshold are configurable). Modifying the internal CSS DPI setting from an extension is currently unsupported ==== Chromium / Google Chrome ====

Chromium should use the #GDK 3 (GTK 3) settings.

To override those, use the  flag with a scaling value. This will scale all content and ui, including tab and font size. For example .

Using this option, a scaling factor of 1 would be normal scaling. Floating point values can be used. To make the change permanent, for Chromium, you can add it to :

To make this work for Chrome, add the same option to  instead.

If you use a HiDPI monitor such as Retina display together with another monitor, you can use the [https://chrome.google.com/webstore/detail/resolution-zoom/enjjhajnmggdgofagbokhmifgnaophmh reszoom extension in order to automatically adjust the zoom level for the active screen.

If using Wayland session, you should enable native wayland support to avoid blurriness. See also Chromium#Incorrect HiDPI rendering.

## Opera
Opera should use the #GDK 3 (GTK 3) settings.

To override those, use the  command line option, where X is the desired DPI. For example, with  Opera will assume that DPI is 144.  Newer versions of opera will auto detect the DPI using the font DPI setting (in KDE: the force font DPI setting.)

## Inkscape
To scale the icons to a "usable" size go to Preferences > Interface and set the icon size to Large or Larger=== Java applications ===

## AWT/Swing
Java applications using the AWT/Swing framework can be scaled by defining the  VM property when invoking . The value can be an integer percentage value, or a float value. For example,

 java -Dsun.java2d.uiScale=2 -jar some_swing_application.jar
 java -Dsun.java2d.uiScale=300% -jar some_swing_application.jar

Since Java 9 the  environment variable is used to scale Swing applications accordingly.

Note that at this point, Java AWT/Swing (up to including OpenJDK 13) only effectively supports integer values. A setting of  or  will be treated as if it were set to  resp. .

## JavaFX
Java applications using JavaFX can be scaled by defining the  VM property when invoking . The value can be an integer percentage value, an integer DPI value (where  represents a scale factor of , and for example  represents a scale factor of ), or a float value. For example,

 java -Dglass.gtk.uiScale=200% -jar some_jfx_application.jar
 java -Dglass.gtk.uiScale=192dpi -jar some_jfx_application.jar
 java -Dglass.gtk.uiScale=2.0 -jar some_jfx_application.jar

JavaFX perfectly well supports fractions. Using values like  or  will deliver the expected result.

## Mixed AWT/Swing and JavaFX
Some Java applications mix JavaFX and AWT/Swing (via ). In that case, the settings for AWT/Swing will also affect JavaFX, and setting  will have no effect.

## JetBrains IDEs
On Wayland, HiDPI with fractional scaling is experimentally supported since version 2024.2. The [https://blog.jetbrains.com/platform/2024/07/wayland-support-preview-in-2024-2/ Wayland support preview can be enabled, by adding  to the VM options (Help > Edit custom VM options).

JetBrains products (IntelliJ IDEA and other IDEs) support two HiDPI modes (JRE-managed and IDE-managed). The sequence for determining system scale factor is well documented at # Java property –
#  –  or
#  and
# Xresources –
# 1.0

For troubleshooting, consult the "Show HiDPI Info" dialog via [https://www.jetbrains.com/help/idea/searching-everywhere.html search everywhere "Shift Shift".

When using per-monitor scaling, an issue might occur where IntelliJ fails to recognize the real, original monitor resolution.
To remediate this problem some people have success by adding the  option to the  file (Help > Edit custom VM options).

If this does not work, the experimental GTK option  might be enabled on Wayland (see above) and the Wayland support preview might be disabled (see above). Currently JetBrains products run on Xwayland and thus have no full native Wayland support yet. This makes the rendering in JetBrains products incompatible with the monitor scaling framebuffer. Disabling the framebuffer thus might solve blurry font/rendering issues for JB products, but alas results in disabled fractional scaling. Another options is to enable the Wayland support preview.

## Maple
Maple can be scaled for HiDPI monitors using the AWT/Swing solution. But it has to be added inside your Maple installation directory to  to the :

Alternatively, the  environment variable can be used to start the application scaled:

 $ GDK_SCALE=2 maple-directory/bin/xmaple %f

## MATLAB
Recent versions (since R2017b) of MATLAB allow to set the scale factor==== Version R2024b and earlier ====

To adjust the scale factor, execute the following instructions in a MATLAB command window:

 >> s = settings;
 >> s.matlab.desktop.DisplayScaleFactor %Get current value
 >> s.matlab.desktop.DisplayScaleFactor.PersonalValue = 2 %Set personal value

The settings take effect after MATLAB is restarted.

This can become tedious if you need to change the scaling frequently. To simplify this, consider using the following script:

To change the display scaling to 3:

 $ matlab-scale 3

## Version R2025a and later
In the latest MATLAB versions, changing the DisplayScaleFactor property often has no effect. However, a newly introduced parameter enables varying the scale factor in real-time, with no need for restarting MATLAB:

 >> s = settings;
 >> s.matlab.desktop.Zoom %Get current value
 >> s.matlab.desktop.Zoom.PersonalValue=150 %Set personal value

## Mono applications
According to [https://bugzilla.xamarin.com/35/35870/bug.html, Mono applications should be scalable like GTK 3 applications. The precise method depends on the GUI library: GtkSharp obviouslys points back to Gtk, while the usual Windows Forms (libgdiplus) simply detects Xft settings.

## NetBeans
NetBeans allows the font size of its interface to be controlled using the  parameter during startup. To make this change permanent edit the  file and append the  parameter to the  property.The editor fontsize can be controlled from Tools > Option > Fonts & Colors.

The output window fontsize can be controlled from Tools > Options > Miscellaneous > Output

## OBS Studio
OBS 29 supports HiDPI setups without any extra configuration.

For older versions of OBS, the recommendation was to set the environment variable  to disable [https://doc.qt.io/qt-5/highdpi.html#migrate-existing-applications Qt’s hi-dpi migration mode and install the Yami theme. Do not use the Yami theme with OBS 29 or newer, as it is not necessary anymore and will cause buggy behavior.

## Rofi
Rofi defaults to 96 DPI and relies on its own configuration only

{{hc|~/.config/rofi/config.rasi|2=
configuration {
    …
    dpi: 150;
    …
}
}}

## Spotify
You can change scale factor by simple  for zoom in,  for zoom out and  for default scale. Scaling setting will be saved in , you may have to create this file by yourself:

Also Spotify can be launched with a custom scaling factor which will be multiplied with setting specified in , for example

 $ spotify --force-device-scale-factor=1.5

## Steam
## Official HiDPI support
* Starting on 25 of January 2018 in the beta program there is actual support for HiDPI and it should be automatically detected.
* Steam > Settings > Interface, check Enlarge text and icons based on monitor size (restart required)
* If it is not automatically detected, use  to set the desired scale factor.
* If the above fails, use  or set . As of the June 2023 UI overhaul, this parameter also supports non-integer scale factors, such as .
* You can also adjust the interface scale in Steam > Settings > Accessibility, though the slider does not display a number value.

## Unofficial
The [https://github.com/MoriTanosuke/HiDPI-Steam-Skin HiDPI-Steam-Skin can be installed to increase the font size of the interface. While not perfect, it does improve usability.

MetroSkin Unofficial Patch also helps with HiDPI on Steam with Linux.

## Sublime Text 3
Sublime Text 3 has full support for display scaling. Go to Preferences > Settings > User Settings and add  to your settings.

## Thunderbird
See #Firefox. To access , go to Edit > Preferences > Advanced >Config editor.

## VirtualBox
VirtualBox also applies the system-wide scaling to the virtual monitor, which reduces the maximum resolution inside VMs by your scaling factor (see This can be worked around by calculating the inverse of your scaling factor and manually setting this new scaling factor for the VirtualBox execution, e.g.

 $ QT_SCALE_FACTOR=0.5 VirtualBoxVM --startvm vm-name

## VMware
Text in the VMware application is rendered at an appropriate size following the system configuration, but icons are small and UI elements have little padding between them.

As described in #GDK 3 (GTK 3), you can use  to further scale up the entire UI (including icons & padding) and then use  to scale only the text back down to a reasonable size.

For example, to get a final 2x scale factor:

 $ GDK_SCALE=2 GDK_DPI_SCALE=0.5 vmware

## Wine applications
Run

 $ winecfg

and change the "dpi" setting found in the "Graphics" tab. This only affects the font size.

## Zathura document viewer
No modifications required for document viewing.

UI text scaling is specified via [https://pwmt.org/projects/zathura/documentation/ configuration file (note that "font" is a girara option):

 set font "monospace normal 20"

## Zoom
Set the  variable in .

For the Flatpak version, set the environment variable  (e.g. to 0.5 This can be easily done with [https://flathub.org/apps/details/com.github.tchx84.Flatseal Flatseal, if using a GUI tool is preferred.

## Gazebo
Gazebo only renders an upper left of a view instead of the whole view. To fix this a Qt environment variable must be set.

To run Gazebo:

 $ QT_SCREEN_SCALE_FACTORS=gazebo

To run a ROS simulation:

 $ TURTLEBOT3_MODEL=burger QT_SCREEN_SCALE_FACTORS=[1.0 roslaunch turtlebot3_gazebo turtlebot3_world.launch

Making an alias such as  works for the first case but not for the second.

## Fcitx
Fcitx preedit  can be changed in .

For Fcitx5, set  with a size inside double quotes in .

## Synthesizer V Studio Pro
Synthesizer V Studio Pro has support for UI scaling. It can setup the scaling automatically, but if it fails the scale can be adjusted with option --with-scaling:

 $ synthv-studio --with-scaling 2.0

## V2RayN, SourceGit and other AvaloniaUi C# / .NET applications
As described in #AvaloniaUI (C# / .NET), you can use .

## Unsupported applications, via a network layer
 includes a run_scaled script which can be used to scale applications.

Another approach is to run the application full screen and without decoration in its own VNC desktop. Then scale the viewer. With  you can set up a desktop per application, then start server and client with a simple command such as .

x11vnc has an experimental option , which opens one viewer per application window. Perhaps something could be hacked up with that.

## Unsupported applications, via Weston
There is a no-network, potentially GPU-accelerated solution to scale old/unsupported applications via Weston. The basic example goes as:

 $ weston --xwayland --socket=testscale --scale=2
 $ DISPLAY=:1 WAYLAND_DISPLAY=testscale your_app

Note 1: You can make it look nicer. Create a dedicated  and use it with :

 idle-time=0
 [shell
 panel-position=none
 locking=false

Note 2: Adjust your  according to your system,  is simply the default that comes after the main . Check files created in  to do that.

Note 3: If you want a separate window per each scaled app, adjust the  parameter to weston and  +  for each started app. Scripting that is not easy because Xorg display has to be a small-ish integer, but you can create a semi-safe script to infer it.

Note 4: It is not fully tested yet whether weston and xwayland truly off-board the heavy parts to the GPU. At least  advertises to do so, but no tests on that were done yet. Please edit if you make the GPU usage tests.

## Multiple displays
The HiDPI setting applies to the whole desktop, so non-HiDPI external displays show everything too large. However, note that setting different scaling factors for different monitors is already supported in Wayland.

## Side display
One workaround is to use xrandr's  option. To have a non-HiDPI monitor (on DP1) right of an internal HiDPI display (eDP1), one could run:

 $ xrandr --output eDP-1 --auto --output DP-1 --auto --scale 2x2 --right-of eDP-1

When extending above the internal display, you may see part of the internal display on the external monitor. In that case, specify the position manually.

You may adjust the  parameter on your monitor settings to adjust the blur level introduced with scaling.

## Multiple external monitors
There might be some problems in scaling more than one external monitors which have lower dpi than the built-in HiDPI display. In that case, you may want to try downscaling the HiDPI display instead, with e.g.

 $ xrandr --output eDP1 --scale 0.5x0.5 --output DP2 --right-of eDP1 --output HDMI1 --right-of DP2

In addition, when you downscale the HiDPI display, the font on the HiDPI display will be slightly blurry, but it is a different kind of blurriness compared with the one introduced by upscaling the external displays. You may compare and see which kind of blurriness is less problematic for you.

## Mirroring
If all you want is to mirror ("unify") displays, this is easy as well:

With AxB your native HiDPI resolution (for ex 3200x1800) and CxD your external screen resolution (e.g. 1920x1200)

 $ xrandr --output HDMI --scale In this example which is QHD (3200/1920 = 1.66 and 1800/1200 = 1.5)

 $ xrandr --output HDMI --scale 1.66x1.5

For UHD to 1080p (3840/1920=2 2160/1080=2)

 $ xrandr --output HDMI --scale 2x2

You may adjust the  parameter on your monitor settings to adjust the blur level introduced with scaling.

## Tools
There are several tools which automate the commands described above.

* [https://gist.github.com/wvengen/178642bbc8236c1bdb67 This script extend a non-HiDPI external display above a HiDPI internal display.
* xrandr-extend.
*  is a CLI front end for xrandr which detects and sets correct DPI: README

## Linux console (tty)
## In-kernel fonts
The Linux console changes the font to  (based on  from based on the vertical and horizontal pixel count of the display[https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=dfd19a5004eff03755967086aa04254c3d91b8ec regardless of its physical size. If your monitor is not recognised as HiDPI, the default font can be changed. In that case, specify  in the kernel command line.

## Fonts outside the kernel (tty)
The largest fonts present in the  package are  and . Other packages like  contain further alternatives, such as  (normal) and  (bold). See Linux console#Fonts for configuration details and Linux console#Persistent configuration in particular for applying the font setting during the early userspace boot sequence.

After changing the font, it is often garbled and unreadable when changing to other virtual consoles (–). To fix this you can force specific mode for KMS, such as  (substitute in the native resolution of your HiDPI display), and reboot. Using small resolutions will make the text look bigger, but also pixelated.

Users booting through UEFI may experience the console and boot loader being constrained to a low resolution despite correct KMS settings being set. This can be caused by legacy/BIOS boot being enabled in UEFI settings. Disabling legacy boot to bypass the compatibility layer should allow the system to boot at the correct resolution.

## Modern HiDPI support (kmscon)
For real HiDPI support, see KMSCON instead of changing the font size in the tty.
