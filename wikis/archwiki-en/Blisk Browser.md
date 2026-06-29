# Blisk Browser

Blisk is a specialized web browser, made for web designers and web developers, made by Estonian company SyncUI OÜ. The browser is free to use with limited functionality, but in order to get full access to the development features, a paid subscription is required. The Blisk browser is based on Chrome, using Chromium as its base.

## Installation
Install the  package.

## Add-ons
Blisk is based on Chromium and has access to the Chrome Extension Store. However, while most extension should work just fine, there are possible issues, especially with more complex extensions, focusing on more Chrome specific functions and features. Hence, not all of these add-ons actually work with Blisk.

## Configuration
Configuration of Blisk is possible through the menu, in the same way as it works with Chromium. However, as with Chrome and other browsers, you can also access are more complex set of options and settings by using:

 chrome://settings

This gives access to some advanced and experimental settings, mainly meant for experimental features and debugging. Unless you know what you are doing, or are specifically told to change them, you can usually leave them alone.

## KDE integration
For integration into Plasma install . See KDE Plasma Browser Integration for more details.

## PDF viewer plugin
Blisk, like Chromium and Google Chrome are bundled with the Chromium PDF Viewer plugin. If you do not want to use this plugin, check Download PDFs in .

## Running on Xwayland
If you are using NVIDIA's proprietary driver, running Blisk on Xwayland may cause the GPU process to occasionally crash. To prevent the GPU process from crashing, add the following flags:

 --use-angle=vulkan --use-cmd-decoder=passthrough

## Native Wayland support
Blisk supports native Wayland, the same way Chromium does. This can be enabled with the following flags --ozone-platform-hint=auto

The flag is also available via browser flags menu.

This will select Wayland's Ozone backend when in wayland session. So you can use a single desktop entry, if you switch between X11 and Wayland often.

Additionally, if you are having [https://bugs.chromium.org/p/chromium/issues/detail?id=1422087 trouble with input methods, which may or may not apply to Blisk, you may also want to force newer GTK:

 --gtk-version=4

If you are using Fcitx5 and it does not work properly using the above flags, try using the  flag instead of . --enable-wayland-ime --wayland-text-input-version=3

## Tips and tricks
The following tips and tricks should work for both Blisk and Chromium, unless explicitly stated.

## Browsing experience
## chrome:// URLs
A number of tweaks can be accessed via Chrome URLs. See chrome://chrome-urls for a complete list.

* chrome://flags - access experimental features such as WebGL and rendering webpages with GPU, etc.
* chrome://extensions - view, enable and disable the currently used Chromium extensions.
* chrome://gpu - status of different GPU options.
* chrome://sandbox - indicate sandbox status.
* chrome://version - display version and switches used to invoke the active .

An automatically updated, complete listing of Chromium / Blisk [https://peter.sh/experiments/chromium-command-line-switches/ command-line parameters is available.

## Blisk task manager
 can be used to bring up the browser task manager wherein memory, CPU, and network usage can be viewed. This is a helpful tool for developers or if your browser is running slow.

## Search engines
Make sites like wiki.archlinux.org and wikipedia.org easily searchable by first executing a search on those pages, then going to Settings > Search and click the Manage search engines.. button. From there, "Edit" the Wikipedia entry and change its keyword to w (or some other shortcut you prefer). Now searching Wikipedia for "Arch Linux" from the address bar is done simply by entering "w arch linux".

## Tmpfs
## Cache in tmpfs
To limit Blisk from writing its cache to a physical disk, it is possible to define an alternative location via the  flag:

 $ blisk --disk-cache-dir="$XDG_RUNTIME_DIR/chromium-cache"

Cache should be considered temporary and will not be saved after a reboot or hard lock. Another option is to setup the space in :

Alternatively, create a symbolic link to . Make sure to delete Blisks's cache folder before you run the command, to avoid any problems:

 $ ln -s /tmp /home/username/.cache/blisk

## Profile in tmpfs
Relocate the browser profile to a tmpfs filesystem, including , or  for improvements in application response as the entire profile is now stored in RAM.

Use an active profile management tool such as  for maximal reliability and ease of use. It symlinks or bind mounts and syncs the browser profile directories to RAM. For more, see Profile-sync-daemon.

## Launch a new browser instance
When you launch the browser, it first checks if another instance using the same data directory is already running. If there is one, the new window is associated with the old instance. If you want to launch an independent instance of the browser, you must specify a separate directory using the  parameter:

 $ blisk --user-data-dir=/path/to/some/directory

## Directly open *.torrent files and magnet links with a torrent client
By default, Blisk downloads  files directly and you need to click the notification from the bottom-left corner of the screen in order for the file to be opened with your default torrent client. This can be avoided with the following method:

* Download a  file.
* Right-click the notification displayed at the bottom-left corner of the screen.
* Check the "Always Open Files of This Type" checkbox.

See xdg-open to change the default association.

## Reduce memory usage
By default, Blisk uses a separate OS process for each instance of a visited website. However, you can specify command-line switches when starting Blisk to modify this behavior.

For example, to share one process for all instances of a website:

 $ blisk --process-per-site

To use a single process model:

 $ blisk --single-process

In addition, you can suspend or store inactive Tabs with extensions such as [https://chrome.google.com/webstore/detail/tab-suspender/fiabciakcmgepblmdkmemdbbkilneeeh?hl=en Tab Suspender and OneTab.

## User Agent
”The User Agent can be arbitrarily modified at the start of Blisks's base instance via its  parameter.

## DOM Distiller
Chromium has a similar reader mode to Firefox. In Blisk, this is called DOM Distiller, which is an open source project. It is disabled by default, but can be enabled using the  flag, which you can also make persistent.

Not only does DOM Distiller provide a better reading experience by distilling the content of the page, it also simplifies pages for print. Even though the latter checkbox option has been removed from the print dialog, you can still print the distilled page, which basically has the same effect.

After enabling the flag, you will find a new “Enter reader mode” menu item and corresponding icon in the address bar when Blisk thinks the website you are visiting could do with some distilling.

## Forcing specific GPU
In multi-GPU systems, Blisk automatically detects which GPU should be used for rendering (discrete or integrated). This works 99% of the time, except when it does not — if an unavailable GPU is picked (for example, discrete graphics on VFIO GPU passthrough-enabled systems),  will complain about not being able to initialize the GPU process. On the same page below Driver Information there will be multiple GPUs shown (GPU0, GPU1, ...). There is no way to switch between them in a user-friendly way, but you can read the device/vendor IDs present there and configure Blisk to use a specific GPU with flags:

 $ blisk --gpu-testing-vendor-id=0x8086 --gpu-testing-device-id=0x1912

...where  and  is replaced by the IDs of the GPU you want to use (as shown on the  page).

## Import bookmarks from Firefox
To ease the transition, you can import bookmarks from Firefox into Blisk.

Navigate Blisk to

If Firefox is already installed on your computer, you can directly import bookmarks as well as many other things from Firefox.

Make sure Mozilla Firefox is selected. Optionally, you can uncheck some unwanted items here. Click the Import and then Done. You are done with it.

If you import bookmarks from another PC, you have to export bookmarks from Firefox first.

 Import and Backup > Export Bookmarks To HTML in Firefox.

The procedure is pretty much the same. You need to go to . However, this time, in the From drop-down menu, select Bookmarks HTML File and click the Choose File button and upload the desired bookmark file.

## Enabling native notifications
Go to  and select Enabled.

## Enabling autoscroll with middle mouse button
The autoscroll is still an experimental feature It is intended to be disabled by default if Blisk or Chromium-based browsers are not a development build and is running on a Linux environment. [https://issues.chromium.org/issues/40811836

To enable this feature, launch your browser with the  flag. In case you want to make the option persistent, see Chromium#Making flags persistent.
