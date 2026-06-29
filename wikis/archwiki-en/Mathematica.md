# Mathematica

Mathematica is a commercial program used in scientific, engineering and mathematical fields. Here we explain how to install it.

## Installation
Since Mathematica is a non-free application and upgrades may incur costs, this section lists instructions for different available versions.

## Mathematica 6
## Mounting iso
One way to mount the Mathematica  is to create a  mount directory and add the following line to the fstab:
 /location/of/mathematica.iso /media/iso iso9660 exec,ro,user,noauto,loop=/dev/loop0   0 0
Now you can mount it with:
 # mount /media/iso

## Running the installer
Run MathInstaller with:

 # cd Unix/Installer
 # sh ./MathInstaller

## Fonts
Add the directories containing Type1 and BDF fonts to your FontPath.

## Mathematica 7
Mathematica 7 is much easier to install.

 # tar xf Mathematica-7.0.1.tar.gz
 # cd Unix/Installer
 # ./MathInstaller

Follow instructions.

For KDE users, the Mathematica icon may appear in the Lost & Found category. To solve this, execute the following as root:

 # ln -s /etc/xdg/menus/applications-merged /etc/xdg/menus/kde-applications-merged

## Mathematica 8
An issue with Mathematica 8 is a reproducible crash when performing WolframAlphafunctions. By default, Mathematica is configured to detect the system's proxy settings when configuring how to connect to the internet to fetch data. A "bug" exists that will eventually crash Mathematica when the calling library is used. A workaround is to avoid this library call altogether by configuring Mathematica to "directly connect" to the internet. (Edit > Preferences > Internet Connectivity > Proxy Settings). This bug has been reported to Wolfram.

## Mathematica 10
Install  (need historical version). The  installation script is required; you will need to download this separately from Wolfram.com, your university, etc. You will also need an activation key.

## Mathematica 11
Install . Obtain  from Wolfram Research, along with an activation key, and save it to the package build directory. Successful install may throw non-critical errors: xdg-icon-resource, mkdir, xdg-desktop-menu. For more details see the [https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=mathematica mathematica PKGBUILD file.

Mathematica 11 automatically creates a document folder 'Wolfram Mathematica' in $UserDocumentsDirectory, which is set by Mathematica according to XDG user directories.

## Mathematica 12
# Install the packages  and .
# Start/enable the service .
# Check that  contains either a static or transient hostname.
# Download the install script from Wolfram. The filename will be .
# Make  executable.
# Run the install script as root. When ran as user, the installer will ask for another installation directory.

 # ./Mathematica_12.XX.YY_LINUX.sh

## Mathematica 13
The installation steps are the same as Mathematica 12.

## Mathematica 14
The installation steps are the same as Mathematica 12.

## Troubleshooting
## Missing symbols
If you have font rendering problems where certain symbols do not show up (i.e.  appears as a square), try this solution. It also states the issue is fixed with Mathematica version 9.

Try having applications use anti-aliasing.
For KDE: System Settings > Application Appearance > Fonts > Use anti-aliasing (Enabled)

## HiDPI / Retina screens
If you have a HiDPI screen, such as an Apple Retina display, and the main text in Mathematica looks small when you open it, this can be fixed:

* Go to Edit > Preferences
* From the Advanced tab, click Open Option Inspector
* In the tree on the right, go to Formatting Options > Font Options > Font Properties
* Change the value for "ScreenResolution" to double its current setting, e.g. 72 to 144. You can also use  to get a more precise number (which will need to be doubled).

## Conflicts with system libraries
The Mathematica package includes a number of its own libraries, located in . They may lead to some compatibility issues and fallback to the system versions of some of these libraries may be necessary.

## Symbol lookup error: /usr/lib/libfontconfig.so.1: undefined symbol: FT_Done_MM_Var
Force Mathematica to use the system version of the freetype library.

 # cd /SystemFiles/Libraries/Linux-x86-64
 # mv libfreetype.so.6 libfreetype.so.6.old

## Mathematica/11.3/SystemFiles/Libraries/Linux-x86-64/libz.so.1: version `ZLIB_1.2.9' not found (required by /usr/lib/libpng16.so.16)
Force Mathematica to use the system version of the zlib library.

 # cd /SystemFiles/Libraries/Linux-x86-64
 # mv libz.so.1 libz.so.1.old

## Symbol lookup error: /usr/lib/libfreetype.so.6: undefined symbol: hb_ot_tags_from_script_and_language
Force Mathematica to use the system version of the harfbuzz library.

 # cd /SystemFiles/Libraries/Linux-x86-64
 # mv libharfbuzz.so.0 libharfbuzz.so.0.old
