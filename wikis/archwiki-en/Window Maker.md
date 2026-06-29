# Window Maker

Window Maker is a window manager (WM) for the X Window System. It is designed to emulate the NeXT user interface as an OpenStep-compatible environment, and is characterized by low memory demands and high flexibility. As one of the lighter WMs, it is well suited for machines with modest performance specifications.

## Installation
Install the  package. You may also wish to install the  package which contains a number of extra icons and themes.

## Starting
Run  with xinit.

## Configuration
## Files
All of the settings for Window Maker can be found in the  directory, under  and . They are simple text files which can be edited by hand, or you can use the  () GUI application to change the settings; in the default installation WPrefs can be started by double-clicking the icon in the top right corner of the workspace.

*  - The current Window Maker settings.
*  - Global settings for all WINGs applications.
*  - The desktop main menu. It uses a simple text format that can be edited by hand. For more details, see the menu editing section in the Preferences Utility application.
*  - Used to restore a Window Maker session.
*  - Individual application and window settings, such as application icon settings and title bar settings. You can also edit this by right clicking on any application or window icon and selecting "Attributes".
*  - Settings for the Preferences Utility.
*
*  - One of the default locations Window Maker looks for application icons. You can save your favorite icons here and use them by changing application or window attributes.
*  - Add here applications that you want to automatically start when Window Maker starts. Be sure to run them in the background by using "&".
*  - Same as autostart, but used when exiting.
*  - One of the default locations where Window Maker looks for desktop wallpapers.
*  - One of the default locations where Window Maker looks for styles.

## Styles
Styles are simple text property list files that change the appearance of Window Maker. They have the same layout as the  file. Whatever settings are in the style file will be applied to the  file. Here is an example style that gives Window Maker a blue and gray Arch Linux like look:

{{hc|Arch.style|2=
{
  FTitleBack = (solid, "#0088CC");
  FTitleColor = white;
  UTitleBack = (solid, "#333333");
  UTitleColor = "#999999";
  PTitleBack = (solid, "#333333");
  PTitleColor = "#999999";
  MenuTextBack = (solid, "#ECF2F5");
  MenuTextColor = black;
  IconTitleBack = "#333333";
  IconTitleColor = white;
  MenuTitleBack = (solid, "#0088CC");
  MenuTitleColor = white;
  HighlightTextColor = white;
  HighlightColor = "#333333";
  MenuDisabledColor = "#999999";
  ClipTitleColor = black;
  IconBack = (solid, "#ECF2F5");
  ResizebarBack = (solid, "#333333");
  MenuStyle = flat;
  WorkspaceBack = (solid, black);
  ClipTitleFont = "Arial:slant=0:weight=200:width=100:pixelsize=10";
  IconTitleFont = "Arial:slant=0:weight=80:width=100:pixelsize=9";
  LargeDisplayFont = "Arial:slant=0:weight=80:width=100:pixelsize=24";
  MenuTextFont = "Arial:slant=0:weight=80:width=100:pixelsize=12";
  MenuTitleFont = "Arial:slant=0:weight=200:width=100:pixelsize=12";
  WindowTitleFont = "Arial:slant=0:weight=200:width=100:pixelsize=12";
}
}}

Styles can also be edited by using the Preferences Utility application.

## HiDPI
Window Maker (git HEAD) has rudimentary HiDPI support (WMScaleX/WMScaleY) that scales Window elements according to the metrics of the default font. Open  and multiply the  value by your current scale factor, i.e. DPI divided by 96.

## Keyboard shortcuts
Window Maker allows keyboard shortcuts to be assigned both to window manager actions and to menu entries.

To assign a keyboard shortcut to a window manager action, start the WPrefs application and navigate to the Keyboard Shortcut Preferences tab. Choose an action, click the Capture button and hit the desired keyboard combination. Then click Save.

You can also assign keyboard shortcuts to menu entries. For instance, if one wishes to use GNOME Screensaver to lock the screen, one could create a Lock Screen menu entry which runs the command . To then assign a keyboard shortcut to this menu entry, start the WPrefs application and navigate to the Applications Menu Definition tab. In the root menu that appears on screen, click on the Lock Screen entry. In the WPrefs window, click the Capture button, hit the desired keyboard combination and then click Save.

## Background
To use an image as a background in Window Maker, copy the image to the  directory. Then, from the root menu, select Appearance -> Background -> Images -> image-name.

Alternatively, use a standalone background setter such as Nitrogen.

## Dock
The user interface of macOS evolved from the style of user interface that Window Maker uses. There is a "dock" that contains applications icons that are "pinned" to the dock by the user. Also, the dock can hold special small applications called "dockapps", which run only inside the dock. By default, all applications run in Window Maker will have an application icon, which you can use to run a new instance of the application, hide and unhide all windows of the application, or kill the application. The application icon does not represent a window. Instead, if you minimize a window, a small icon representing the window will appear on the desktop.

After starting any application, (for example, from the command line) the application icon will appear on the desktop. You can pin it to the dock by clicking and dragging the icon into the dock area. To remove the application icon from the dock, click and drag the icon away from the dock area. You change settings, such as making an application automatically start when Window Maker starts, by right clicking on the application icon in the dock.

The default action to activate application icons and window icons is to double click them. You can change a setting to allow you to activate them with a single click.

## Clip
The "clip" is a button that has the image of a paperclip on it. You can change the name of the current workspace by right clicking on the clip. You can change workspaces by clicking the arrows that are on the clip.

The clip also has similar functionality to the dock. Application icons that are added to the dock are visible on all workspaces, while application icons that are attached to the clip are only seen on the workspace where they are attached. This allows you to conveniently associate specific application icons with specific workspaces.

Double click the clip to hide and unhide the application icons that are attached to it.

## Dockapps
Dockapps are small applications that run in the dock. They can be useful for showing system information. Some useful dockapps include:

*  - Show CPU status and usage.
*  - Show network status. Usage:
*  - Show disk usage. Usage:

See the Window Maker website for more information about dockapps.

## System tray
Window Maker does not ship with a system tray; however, a number of standalone trays can be used with it.

;stalonetray
Since version 0.8 of , basic dockapp support for Window Maker can be enabled using the  command line option. The following options should also be used: .

;Tint2
tint2 is compatible with Window Maker. As well as a system tray it has an optional taskbar (duplicating the Window Maker feature) and applets showing the clock and the status of the battery.

;Dockapps for Window Maker
 is a system tray dockapp designed for Window Maker and reported to work well in other desktops.

;Peksystray
 is a system tray designed for the light window managers that support docking. Peksystray provides a window where icons will automatically add up, according to the requests from the applications. Both the size of the window and the size of the icons can be selected by the user. If the window is full, it can automatically display another window in order to display more icons.

## Tips and tricks
## Removing unwanted application icons
For some applications, you may not want Window Maker to display an application icon or appicon. To disable the appicon for an application, right click on the application's titlebar and choose Attributes... and from the drop down menu choose Application Specific. Tick the No application icon option and then hit Apply and Save.

## Troubleshooting
## Cannot disable smooth fonts
Delete (but keep a backup) the  directory and  file, then restart Window Maker.

## The dock is not covered by fullscreen windows
To correct this issue, right click on any pinned application and, from the Dock position submenu, choose Normal. Then start the WPrefs tool. Under the Window Handling Preferences tab, tick the ...do not cover dock option. This will ensure that maximised applications do not cover the dock but that fullscreen applications do.

## No application icons for some applications
Some applications such as Chromium will not display an application icon. For a workaround involving Chromium, see the following bug report.

## Window attributes not set persistently
If you find that window attributes that you have saved for a certain window are not persistent, this is probably because you are trying to override hints set by the application itself that change the way the window manager treats the window. For instance, a window might set a Motif hint requesting that the window manager does not decorate the window with a titlebar. However, when you untick the Disable titlebar option and hit Save in Window Attributes, you find that the window does not have a titlebar when it is next launched.

This problem arises because Window Maker will only write window settings to the settings file that it considers to be non-default. However, Window Maker will not update what it considers to be a default setting to take into account window hints. So for a window that has no titlebar, hitting the Save button after unticking Disable titlebar will do nothing because Window Maker incorrectly considers that to already be the default setting.

To work around this, open the Window Attributes dialogue for the window in question and, without making any changes whatsoever, hit the Save button. This will write the hint set settings that Window Maker considers to be non-default to file. Then, open  in a text editor and you should find the settings in question for that window written there. You can now change them to your preferred values, for instance: change  to
