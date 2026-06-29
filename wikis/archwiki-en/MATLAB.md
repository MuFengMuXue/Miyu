# MATLAB

From the official website:

:MATLAB is a programming and numeric computing platform used by millions of engineers and scientists to analyze data, develop algorithms, and create models.

## Installation
MATLAB is proprietary software produced by The MathWorks and requires a license to obtain, install, and activate. New versions of MATLAB are released twice a year, release names are composed of , the year of the release and  or .

Arch Linux is not in the list of officially supported distributions.

A complete copy of the MATLAB software must be obtained before it can be installed. The MATLAB software is available to licenses holders on both a DVD and through the MathWorks website. In addition to the software a file installation key is required.

It is possible to install MATLAB either with the MATLAB Package Manager (), , or from the MATLAB installation software directly. The recommended and most robust method is by using the MATLAB Package Manager, as it automates the installation of both MATLAB and toolboxes. Since the standard MATLAB installer does not support Wayland, the MPM is the only way to install MATLAB if running Wayland. Please note that MATLAB itself will require .

## Installing with MATLAB Package Manager (MPM)
MATLAB Package Manager (MPM) offers a streamlined method to install MATLAB and accompanying MathWorks products on Linux systems, directly from the command line. This utility facilitates programmatic installation without necessitating user sign-in, a File Installation Key, or a pre-acquired license file, deferring activation and licensing to post-installation. MPM permits specification of MATLAB release version, additional toolboxes, and installation directory. Additionally, it serves well for constructing MATLAB Docker containers. As of 2023, the MATLAB installer does not support Wayland, and this is an easy way to install MATLAB via command-line.

Download  from the AUR (alternatively download it from https://www.mathworks.com/mpm/glnxa64/mpm, make it executable and add it to the PATH environment variable, see Environment variables#Examples).

To install MATLAB R2021b along with select toolboxes to a specified directory, the command could be for example:

 $ mpm install --release=R2021b --destination=~/matlab MATLAB Simulink Deep_Learning_Toolbox Parallel_Computing_Toolbox

The full list of correctly formatted product names can be found within the template input files.

After installation is complete, if you have an Academic Online license, please run
 $ ~/matlab/bin/glnxa64/MathWorksProductAuthorizer.sh
to activate your products.

## Installing from the MATLAB installation software
The MATLAB installation software is self contained and does not require any additional packages to install in silent mode. To install with the GUI a working Xorg graphical display is necessary. Wayland is not officially supported yet, so it will run in a Xwayland session. The installation is handled by the  script. You can run the script as root to install MATLAB system-wide or your user to install it only for you.

During the installation, you are asked if you want symlinks to be created. If you did not choose to do so, you can now manually create a symlink in  to make it easier to launch in terminal:

 # ln -s /{MATLAB}/bin/matlab /usr/local/bin

Or you could add  MATLAB install path to  environment variable.

## Desktop entry
Optionally create a desktop entry. The MIME type of MATLAB files is .

Start  with:

*  to run Matlab without a terminal.
*  to prevent the splash screen from showing up.
*  to use the folder specified by the Initial working folder preference In order for icons to appear correctly  needs to be set in the desktop entry. To find it out start MATLAB, run  and select the MATLAB window.

Example desktop entry:

If one need to set environment variable, one could prepend  in , for example, to system's libfreetype:

 Exec=env LD_PRELOAD=/usr/lib/libfreetype.so.6 matlab

One might want to use the system's .

## Running on Wayland
To make MATLAB run on Wayland, set the environment variable .

## Installing from the AUR package
The  package is designed to allow MATLAB to be integrated into and managed by Arch. The advantage of the  package is that it manages dependencies and some of the nuances of the installation process. Note however, that the package does not contain the installation files, and you are expected to place them in the cloned package folder yourself. It can be problematic to build the package using AUR helpers, so you are expected to do so manually. You can obtain the actual MATLAB software using the installer from [https://www.mathworks.com the MathWorks website.

* Clone the  package and  into it.
* Download the zip file containing the MATLAB installer from MathWorks into the current directory.
* Run the extracted installer with:
 $ ./matlab/install
* The installer gives you a choice of either installing the software now or only downloading selected modules. Choose the second option. This option may also be under the "Advanced Options" dropdown menu.
* The installer will give you an option to change the download path. You might want to change it to something temporary (like  if you have big enough ram disk) as you will soon move the contents to a different location.
* Wait for the download to finish and close the installer. Merge the downloaded archives into the extracted  subdirectory:
 $ rsync -a /selected/download/folder/YYYY_MM_DD_HH_MM_SS/ matlab
* Then package the directory into a tarball:
 $ tar -cvf matlab.tar matlab
* Download your licence:Go to your MathWorks account and click on the licence number you want to use. Then, go to the Install and activate tab and select Activate to retrieve licence File. Follow the instructions and download the licence file needed for the installation. Name the file  and place it in the AUR package directory. There will also be a File Installation Key (FIK) visible on the MathWorks website. Copy-paste it in a new file named  and save it next to  just like you did with the .
* Now, you will create a pacman package. You can customize the modules you want the package to contain by modifying the  or leave it at default:

* Finally, use  command to build and install the package:
 $ makepkg -sri

## Configuration
## Java
The MATLAB software is bundled with a JVM and therefore it is not necessary to install Java. The JVM version supported by MATLAB is listed in Versions of OpenJDK Compatible with MATLAB by Release or simply type  in MATLAB. One could set the  environment variable to use custom JVM, for example, to specify the  JRE, launch MATLAB with:

 $ env MATLAB_JAVA=/usr/lib/jvm/java-8-openjdk/jre matlab

## OpenGL acceleration
MATLAB can take advantage of hardware based 2D and 3D OpenGL acceleration. Support for hardware acceleration needs to be configured outside of MATLAB. Appropriate video drivers need to be installed along with the OpenGL utility library  package. If X11 forwarding is being used, the video drivers need to be installed on both the client and server. To check if MATLAB is making use of hardware based OpenGL acceleration run:

 $ matlab -nodesktop -nosplash -r "opengl info; exit" | grep Software

If "software rendering" is not "false", then there is a problem with your hardware acceleration. If this is the case make sure OpenGL is configured correctly on the system. This can be done with the  program from the  package:

 $ glxinfo | grep "direct rendering"

If "direct rendering" is not "yes", then there is likely a problem with your system configuration.

If glxinfo works but not matlab, you can try to run:

 $ export LD_PRELOAD=/usr/lib/libstdc++.so; export LD_LIBRARY_PATH=/usr/lib/xorg/modules/dri/; matlab -nodesktop -nosplash -r "opengl info; exit" | grep Software

If it works, you can edit Matlab launcher script to add:

 export LD_PRELOAD=/usr/lib/libstdc++.so
 export LD_LIBRARY_PATH=/usr/lib/dri/

After these changes, you may see low-level graphics errors in the MATLAB console such as:

 com.jogamp.opengl.GLException: X11GLXDrawableFactory - Could not initialize shared resources for X11GraphicsDevice.x11, connection :0, unitID 0, handle 0x0, owner false, ResourceToolkitLock[obj 0x76ddc7cd, isOwner false, [count 0, qsz 0, owner ]]
     at jogamp.opengl.x11.glx.X11GLXDrawableFactory$SharedResourceImplementation.createSharedResource(X11GLXDrawableFactory.java:326)
     at jogamp.opengl.SharedResourceRunner.run(SharedResourceRunner.java:297)
     at java.lang.Thread.run(Thread.java:748)
 Caused by: java.lang.NullPointerException
     at jogamp.opengl.GLContextImpl.makeCurrent(GLContextImpl.java:688)
     at jogamp.opengl.GLContextImpl.makeCurrent(GLContextImpl.java:580)
     at jogamp.opengl.x11.glx.X11GLXDrawableFactory$SharedResourceImplementation.createSharedResource(X11GLXDrawableFactory.java:297)
     ... 2 more

In that case, create a file with the name 'java.opts' in the directory where MATLAB is executed (for example ) with the following line:

## Sound
To confirm that MATLAB is able to use the default soundcard to present sounds run:

 $ matlab -nodesktop -nosplash -r "load handel; sound(y, Fs); pause(length(y)/Fs); exit" > /dev/null

This should play an except from Handel's "Hallelujah Chorus." If this fails make sure ALSA is properly configured. This can be done with the  program from the  package:

 $ speaker-test

If you do not hear anything, then there is likely a problem with your system configuration.

## GPU computing
MATLAB can take advantage of CUDA enabled GPUs to speed up applications. In order to take advantage of a supported GPU install the , , , and  packages. To check if MATLAB is able to utilize the GPU run:

 $ matlab -nodesktop -nosplash -r "x=rand(10, 'single'); g=gpuArray(x); Success=isequal(gather(g), x), exit"  | sed -ne '/Success =/,$p'

## Install supported compilers
In order to access the full functionality of MATLAB (e.g., to use Simulink, Builder JA, and MEX-file compilation), supported versions of the , , , and  compilers must be installed. Details about the supported compilers for the current release and previous releases are available online. Many of the supported , ,  compiler versions for past MATLAB releases are available from the AUR (e.g., , , , and ), while past versions of the  compilers are not packaged.

To use previous versions of the , , and  compilers with MEX files, edit {{ic|${MATLAB}/bin/mexopts.sh}} and replace all occurrences of  with ,  with , and  with , where  is the compiler version appropriate for the particular MATLAB release.

{{Note|
* Newer versions of Matlab (at least 2017a) does not seem to respect the {{ic|${MATLAB}/bin/mexopts.sh}} customization. Instead it uses {{ic|${MATLAB}/bin/glnxa64/mexopts/LANG_glnxa64.xml}} file.
* Though, it is not officially supported, one could still use higher version of compiler, and ignore the warnings.
}}

## Help browser
The help browser uses valuable slots in the dynamic thread vector and causes competition with core functionality provided by libraries like the BLAS that also depend on the dynamic thread vector. The help browser can be configured to use fewer slots in the dynamic thread vector with

 >> webutils.htmlrenderer('basic');

This is a persistent change and to reverse it use

 >> webutils.htmlrenderer('default');

## Serial port access
To successfully connect to any serial port, MATLAB expects to have write access directly to  which is not allowed on Arch Linux for security reasons. Instead of allowing this access just for MATLAB, you can work around this problem by redirecting device locking using . All you have to do is executing MATLAB like this:

 # lockdev-redirect /{MATLAB}/bin/matlab

If you have created a .desktop file as shortcut to MATLAB, then add "lockdev-redirect" as a prefix to your "Exec=" entry.

## HiDPI and 4k
See HiDPI#MATLAB.

## Troubleshooting
## Warning: Initializing MATLAB Graphics failed
This error seems to happen on multi-monitor setups, see this forum post.

## X11GLXDrawableFactory - Could not initialize shared resources for X11GraphicsDevice
Create a file java.opts in the folder where the matlab executable is:

or look at this forum post for other solutions

or disable hardware acceleration:

 >> opengl('save','software')

## Black screen in help browser and livescripts
In order to use help browser and livescripts install .

## Static TLS errors
MATLAB has a number of libraries that have been compiled with static thread local storage (TLS) including the help browser  and the BLAS libraries. For example,

 >> doc('help');
 >> ones(10)*randn(10);
 Error using  *
 BLAS loading error:
 dlopen: cannot load any more object with static TLS

is related to the bugs:

* 961964 for which patched libraries are available from MathWorks
* 1003952 for which workarounds exist

A more general solution of recompiling  has also been suggested. === Blank/grey UI when using WM (non-reparenting window manager) ===

See Java#Gray window, applications not resizing with WM, menus immediately closing.

## Corrupted text and fonts in menus and fields
If you notice that the menus or the input fields are corrupted or not appearing correctly then you can try to activate the "Use antialiasing to smooth desktop fonts" option in Matlab preferences, it seems to solve the problem. Go to Preferences > Matlab > Fonts and activate it. You will need to restart Matlab in order to take effect.

## Installation dependencies missing
Matlab might complain that it cannot find a package. Look at the package name and install it with Pacman, or in the case of x86_64 there are some libraries only in AUR.  contains a list of up-to-date dependencies for the newest Matlab version.

See also #Unable to launch the MATLABWindow application.

## Installation error: archive is not a ZIP archive
During the installation you can get:

 The following error was detected while installing package_name: archive is not a ZIP archive
 Would you like to retry installing package_name? If you press No, the installer will exit without completing the installation. More information can be found at /tmp/mathworks_root.log

Matlab downloads all packages to  directory which resides in RAM and is maximum size of half of available memory. In this case it is not enough for installation files and Matlab 2019a installer will warn you about this. If it did not, or if you ignored the warning, you will have got the above error.

You can either resize tmpfs (3,5 GB is not enough, 6 GB works), or remove packages from base install and add them later with built-in Matlab add-on installer.

## Install-time library errors
* Make sure that the symlink  is pointing to the correct version of  (which is also in the same directory and has numbers where 'xx' is). By default, it may be pointing to an older (and nonexistent) version (different value for 'xx').

* Make sure the device you are installing from is not mounted as

* If you downloaded the files from Mathworks' website, make sure they are not on an NTFS or FAT partition, because that can mess up the symlinks. Ext4 or Ext3 should work.

## Hangs on rendering or exiting with Intel graphics
Some users have reported issues with DRI3 enabled on Intel Graphics chips. A possible workaround is to disable DRI3 and run MATLAB with hardware rendering on DRI2; to do so, launch MATLAB with the environment variable LIBGL_DRI3_DISABLE set to 1:

 LIBGL_DRI3_DISABLE=1 /{MATLAB}/bin/matlab

If the previous workaround does not work, the issue can be circumvented by selecting software rendering with the MATLAB command (beware, performance may be very poor when doing e.g. big or complex 3D plots):

 opengl('save','software')

See [https://bugzilla.redhat.com/show_bug.cgi?id=1357571 and for more.

## LiveScript errors
If you get the error when attempting to load or create a LiveScript:

*It could be because of broken symlinks of  and other dependencies, after system updates. On the first start of the Live Editor the components are extracted and these libary symlinks are created (if not existing).
: A solution is to simply delete the whole folder containing the broken symlinks and the extracted components, which are in the installation directory:
 matlab_root/sys/jxbrowser-chromium
: Or, if the installation directory is not user writable, then in:
 ~/.matlab/R2017b/HtmlPanel
: Matlab will then regenerate the contents on the next Live Editor start.
: A better option is to replace libgcrypt symlink in this extraction directory with a less precise one. For example, after extraction, this link to /lib64/libgcrypt.so.20.2.4 is created. Replace it with e.g. /lib64/libgcrypt.so.20.
: Matlab R2020 does not contain a chromium directory anymore. Relinking the library file libcrypto.so.1.1 with the system file can resolve the issue. It is located in:
 matlab_root/bin/glnxa64
*Also the steps in #Unable to launch the MATLABWindow application may resolve the issue.
*It can also happen due to missing gconf package. Make sure  is installed.
*If the above does not help, execute in the command window
 >> com.mathworks.mde.liveeditor.widget.rtc.CachedLightweightBrowserFactory.createLightweightBrowser()
to get a more detailed error message.
* A debugging console can be opened with
 >> com.mathworks.mde.webbrowser.HtmlPanelDebugConsole.invoke;

## Using webcam/video device
Make sure the correct support package add-ons are installed (webcam or OS Generic Video Interface for example). If running matlab as a user, make sure your user has write permissions to wherever the support packages are being downloaded and installed.

Since MATLAB R2017a, Image Acqusition Toolbox is using GStreamer library version 1.0. It previously used version 0.10.

In general, USB Webcam Support Package does a better job working with UVC and built-in cameras than OS Generic Video Interface Support Package.

## MATLAB hangs for several minutes when closing Help Browser
Since upgrade of glibc from 2.24 to 2.25, MATLAB (at least R2017a) hangs when closing Help Browser. The issue is related to the particular version of jxbrowser-chromium shipped with MATLAB.
This issue is still present with glibc 2.26 and MATLAB R2017b and R2018a.

To fix this issue, download the [https://www.teamdev.com/jxbrowser latest jxbrowser and replace the following jars from MATLAB:

 matlab_root/java/jarext/jxbrowser-chromium/jxbrowser-chromium.jar
 matlab_root/java/jarext/jxbrowser-chromium/jxbrowser-linux64.jar

MATLAB should automatically unpack those jars into  when first opening Help Browser.
Remove  directory to make sure MATLAB uses the latest jxbrowser.

Unfortunately, this workaround does not work in R2017b anymore. Going deeper into investigation of this issue, it is related to a crash of one of jxbrowser-chromium processes. The parent process of jxbrowser-chromium then sits there and waits for response from a process that is already dead. This causes MATLAB main window to freeze. You can easily unfreeze MATLAB by manually killing all leftover jxbrowser-chromium processes.

I have come up with this simple script that uses inotify and waits for user to close Help browser in MATLAB. It triggers when user closes Help browser and sends kill signal to all leftover jxbrowser-chromium processes:

I run this script as part of my MATLAB start script like that:
 ~/bin/unfreeze_matlab.sh R2017b &

To make sure that this background job is killed when I exit MATLAB, I use this in the beginning of MATLAB start script:
 trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT

## Some dropdown menus cannot be selected
In some interfaces - such as Simulation Data Inspector or Simulink Test Manager - nothing happens when choosing an item in dropdown menu (for example, when trying to change a number of subplots in Simulation Data Inspector). To work around this issue, hold down the Shift key while clicking the item in dropdown menu.

## Not starting - licensing error
In case MATLAB will not start from a desktop environment by the call of its desktop file one should see the output as you start it from the terminal.

For a Licensing error such as:

A re-activation might solve the problem.

 /usr/local/MATLAB/R2017a/bin/activate_matlab.sh -javadir /usr/lib/jvm/java-8-openjdk/jre/

## MATLAB fails to run with "Unable to access services required to run MATLAB (error 5201)" on startup
If launching MATLAB from the desktop entry does nothing, and running it from a terminal results in the error:

this may be caused by a problem with the MathWorks Service Host. Reinstalling the service typically resolves the issue.

One solution is to use the reinstallation utility provided by MathWorks. See the following forum thread for download links and manual reinstallation instructions:

Reinstalling the MathWorks Service Host – MATLAB Central Answers

On Linux, simply downloading and running the installer executable was sufficient to restore functionality.

You could face this error trying to launch the installer:

This happens as the tool depends on GTK2, so install it to make it work normally:

 $ pacman -S gtk2

## MATLAB crashes with "Failure loading desktop class" on startup
In case MATLAB will not start and starting it from command line gives you the following error:

and you have the option -Dswing.defaultlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel set in your  environment variable, start MATLAB with

 $ _JAVA_OPTIONS= matlab

If this works, add the line

 export _JAVA_OPTIONS=

to your MATLAB launcher script. Optionally re-add other Java options.

## Unable to type in text fields of interfaces based on MATLABWindow
Since R2018a, it is not possible to type text in interfaces based on MATLABWindow - like Signal Editor, Add-Ons Explorer and others.
MATLABWindow and MATLAB's webwindow infrastructure is based on Chromium Embedded Framework, and it looks like a known and long standing bug: https://bitbucket.org/chromiumembedded/cef/issues/2026/multiple-major-keyboard-focus-issues-on

One possible workaround is to switch focus from the MATLABWindow to another window and then switch back - so that you can type.

To elaborate more on this workaround (since the problem is still there in R2018b), here is what i did in my Openbox config (note that the A-Middle keybinding already exist in default config):

Now, whenever it is not possible to type in a text field, I press Alt+Mouse middle mouse and then I can type again.

This problem is critical during installation.  After one clicks some elements in the installation window, he will not be able to type into any textbox anymore and switching between windows does not always work.  To circumvent the issue, one shall only use key-press, instead of mouse click during installation.  MATLAB installer has a poor support on Wayland, one may also consider using other WM instead during installation.

## Unable to launch the MATLABWindow application
In MATLAB versions R2018b until R2022b, the installer crashes as follows:

To find out why  is crashing, run it manually to get detailed information.

 is a symbol of , which indicates a library incompatibility between the MATLAB application and the Arch Linux packages. To fix this, put aside MATLAB's .

 $ rm ./bin/glnxa64/libfreetype.so*

You can also use  environment variable to force MATLAB use Arch Linux's libfreetype without removing the lib file.

 $ export LD_PRELOAD=/lib64/libfreetype.so
 $ ./install

Similarly, if the error is caused by , put aside MATLAB's . If the error is caused by , put aside MATLAB's .

## Cannot verify university login during installation
For total headcount license users, MATLAB will pop-up a window asking the user to login with their credentials in a web browser.  However, if run with , most browsers (especially chromium) will not run.  To circumvent this problem, one shall 'active the computer' through MATLAB's website using a browser by a normal user. [https://www.mathworks.com/matlabcentral/answers/326647-verify-university-login-not-open-browser See this issue

## Missing libcrypt.so.1
If you get this error when launching or installing MATLAB (R2020a and later), install .

## Running installer as root does not launch the GUI
If you run the installer as root and the GUI does not appear (but does appear without launching as root), try temporarily allowing the root user to access the X Server by running the following commands in order (where  is the command to run the installer as root):

 $ xhost +SI:localuser:root
 # ./install
 $ xhost -SI:localuser:root

Note that the last command should be executed upon finishing the installation process, and  is a string literal. See this support answer, and .

In addition, verify that the  environment variable is set.

An alternative is to install MATLAB as a local user.

## GUI installer is unable to create the target folder when installing as user
Make the folder manually (as root), and take ownership. The path is typically /usr/local/MATLAB
 # mkdir -p /path/to/MATLAB/R20XXx
 # chown -R $LOGNAME: /path/to/MATLAB/R20XXx

## MATLAB crashes when opening Simulink
When running from terminal the error message is:

 Inconsistency detected by ld.so: ../elf/dl-tls.c: 597: _dl_allocate_tls_init: Assertion `listp != NULL' failed!

See upstream bug report here: https://www.mathworks.com/support/bugreports/details/2632298

## MATLAB cannot open or create script files
See #Unable to launch the MATLABWindow application.

## Calls to mex fail
If calls from MATLAB or Simulink to mex (e.g. rapid accelerator) fail with the error , even though the resulting file is usable, it may help to edit  in either  or  by changing the  variable from its empty default: === Incompatibilities with some python libraries using MKL ===

Some python code running inside matlab may fail with an error mentioning . This can be avoided by calling
 py.sys.setdlopenflags(int32(bitor(int64(py.os.RTLD_NOW), int64(py.os.RTLD_DEEPBIND))));
or
 py.sys.setdlopenflags(int32(bitor(int64(py.os.RTLD_LAZY), int64(py.os.RTLD_DEEPBIND))));
directly before any calls to  and after calls to .
See [https://www.mathworks.com/matlabcentral/answers/358233-matlab-python-interface-broken?s_tid=email_ans_new_ans_ans_h#answer_283353 this support answer.

## Settings not persisting between MATLAB restarts
In some cases on recent Arch systems matlab is unable to export  files, preventing toolbox and some matlab settings from being saved to disk and persisted. These cases come from matlab trying to hard link new files from  directly to the preferences directory (usually  where  is the matlab version, e.g. ). As a workaround, run matlab with the  environment variable set to a folder on the same file system as the preferences directory. === "Unable to open this file in the current system configuration" ===

The error can be fixed by setting aside the l in . You may run the following command:

 cd matlab_root/bin/glnxa64/
 mv libfreetype.so.6 libfreetype.so.6.old

## Symbols in toolstrip menus are not diplayed properly
This issue can be fixed by installing .

## Blank screen on Xwayland
As suggested in Wayland#Java, this issue can be fixed by adding in the Matlab launcher script:
 export _JAVA_AWT_WM_NONREPARENTING=1

## Desktop Error with text not rendering
Launching MATLAB you get an error dialog with a message of "desktop error" and the text does not render.
The error log looks like this:

The error is related to missing fonts and can be fixed installing from the AUR the package ttf-ms-fonts

## Simulink on KDE Dark Theme has inappriopriate color scheme
When running Simulink module, the workspace window may render some dark border causing text and icons in corners not visible at all in some scenarios. According to [https://www.mathworks.com/matlabcentral/answers/1811255-r2022b-simulink-is-unusable-on-dark-themed-kde the potential solution it can be fixed by setting  and  environment variables with

 export XDG_CURRENT_DESKTOP=GNOME
 export GTK_THEME=Adwaita:light

## canberra message in terminal
Starting matlab from a terminal, one may receive a line like the following

 Gtk-Message: 20:01:53.344: Failed to load module "canberra-gtk-module"

According to this can be fixed by setting the environment variable . The packages  and  need to be installed of course.

 env GTK_PATH=/usr/lib/gtk-2.0

## executable stack error with MATLAB versions at or before R2024b
The recent release of [https://archlinux.org/news/glibc-241-corrupting-discord-installation/ glibc 2.41 also causes issues with MATLAB. MATLAB will throw an error similiar to the following:

Stricter security settings now require that executable stack permissions are disabled for the  shared object file. This can be done with .

 $ execstack -c ~/.MathWorks/ServiceHost/-mw_shared_installs/$version/bin/glnxa64/libmwfoundation_crash_handling.so

## Segmentation fault after MATLAB window appears, or silent segmentation fault when attempting to start installer
If the disk installer fails silently, run  to show some more information about the crash. If the window starts and shows normally, then it may be a library version mismatch. Use a debugger to trap on fault and show the stack trace. If you do manage to run the executable itself, you'll see a stack trace similar to this:

This can be fixed by installing an older version of gnutls into the library search location https://bbs.archlinux.org/viewtopic.php?pid=2254979#p2254979. For R2025a install gnutls 3.8.8-1 and copy the libraries to the directory where the MATLAB binary searches for libraries:
{{bc|
export MATLABPATH/usr/local/MATLAB/R2025a/bin/glnxa64
export GNUTLSPATH/tmp/gnutls-3.8.8-1-x86_64.pkg
# Download gnutls
mkdir -p "${GNUTLSPATH}"
wget -P /tmp/ https://archive.archlinux.org/packages/g/gnutls/gnutls-3.8.8-1-x86_64.pkg.tar.zst
tar -xvf /tmp/gnutls-3.8.8-1-x86_64.pkg.tar.zst -C ${GNUTLSPATH}
# Copy over to installation
mkdir "${MATLABPATH}"/gnutls
cp -a "${GNUTLSPATH}"/usr/lib/* "${MATLABPATH}"/gnutls/
# -f to overwrite files
ln -sf "${MATLABPATH}"/gnutls/* "${MATLABPATH}"/
}}

## MATLAB in a systemd-nspawn
MATLAB can be run within a systemd-nspawn container to maintain a static system and avoid the library issues that often plague matlab installs after significant updates to libraries in Arch. Refer to Systemd-nspawn for detailed information on setting up such containers.

The following instruction is to get a MATLAB R2021b installation running in a minimal Debian 11 environment. It assumes MATLAB is already installed as normal in "/usr/local/MATLAB/R2021b".

Use Xhost to allow the nspawn environment to use the existing X server instance, see also Systemd-nspawn#Use an X environment.

Create a minimal Debian environment in a directory ("deb11" here) with:

 $ debootstrap --include= --components=main,contrib bullseye deb11

Some dependencies might be:

* systemd-container
* matlab-support`: in the environment for some convenient integration.
* `mesa-utils`: support graphics acceleration; please add other drivers if necessary
* `usbutils` support usb interfaces for I/O with MATLAB.
* Install the following packages to have the required libraries in the nspawn environment for MATLAB: https://github.com/mathworks-ref-arch/container-images/raw/refs/heads/main/matlab-deps/r2021b/ubuntu24.04/base-dependencies.txt

Set a password for the root user and create regular user:

 # systemd-nspawn -D deb11
 passwd
 useradd -m username
 logout

and then boot the environment with:

 # systemd-nspawn --bind-ro=/dev/dri --bind-ro=/tmp/.X11-unix --bind=/dev/shm --bind=my/matlab/folder:/usr/local/MATLAB --setenv=DISPLAY=:N --bind=$XDG_RUNTIME_DIR/$WAYLAND_DISPLAY:/tmp/wayland.sock -b -D deb11

Where  is your display server.

MATLAB can be launched from within the environment normally by using the binary at .

Another way is to add something like:

 -u username -a /usr/local/MATLAB/bin/matlab -nosoftwareopengl -useStartupFolderPref

to the systemd-nspawn command above.
