# Xilinx Vivado

Arch Linux is not officially supported by Vivado, but as happens with Xilinx ISE WebPACK, most of its features can be used with a bit of hacking.

## Installation
Xilinx Vivado can be downloaded from its official website It is recommended to download "Vivado HLx .: All OS installer Single-File Download" tarball, but make sure not to be in a hurry, as it is a large download (over 70 GB). Update tarballs can also be downloaded and installed later. The other installer can also be used, but see the troubleshooting section below first.

## AUR Package
The  package can be used to create a Vivado installation managed by pacman. Since the download of the installer is locked behind a login wall, it needs to be downloaded manually as outlined above and placed in the same directory as the PKGBUILD. The package only builds the latest major version (.), not the minor updates (..); if these are required, install Vivado manually instead.

## Digilent USB-JTAG Drivers
To use Digilent Adept USB-JTAG adapters (e.g. the onboard JTAG adapter on the [https://www.zedboard.org ZedBoard) from Vivado, you need to install the Digilent Adept Runtime.

Make sure you have installed .

To install the Digilent Adept Runtime, it is recommended to install .

In addition, installing  may do good to configuring your board.

## Tips and tricks
## Enable display scaling
Start Vivado, then set the scaling rate through Tools > Setting > Display > Scaling.

## Disable WebTalk
The free WebPACK license does not let you disable this feature which uploads usage data to Xilinx's servers when generating a bitstream, but synthesis will complete just fine if the connection fails. A simple way to make it fail consistently for Vivado tools only is to set an invalid HTTPS proxy for it.

This method will not pollute your environment, only the temporary environment that is configured upon startup of the tools, so it should not break anything else.

## Troubleshooting
## HTML links under Help menu do not open in browser
See https://support.xilinx.com/s/article/76524?language=en_US

Create file

then configure the script at Window > Preferences > Web Browser.

## Vitis HLS no response or only splash screen visible
See https://support.xilinx.com/s/question/0D52E00006hpY4PSAU/vitishls-20202-not-starting-only-splash-screen-visible

When you run  (the path of Vitis_HLS in *.Desktop file), you may get

Then it is stuck here or exit directly.

To fix this issue, first change the file  line 40

from
 ----%r&-'%rl%&n$&lt'v-=
to
 ----%r&-'%rl%&n$&lt'v->

Then add
 osgi.locking=none
to file

## Synthesis segfaults
See https://support.xilinx.com/s/feed/0D52E00006hpUycSAE?language=en_US

You will need to recompile  (just take the PKGBUILD from the abs) with . Instead of patching the system libc in , copy the newly
compiled  and  to
Do not forget to repeat this when  gets upgraded.

## xsct, xsdb, xmd, and tclsh segfault
The Xilinx Vivado command-line tools xsct, xsdb, xmd, and tclsh may crash with a message similar to the following:

 Segmentation fault (core dumped) "$RDI_BINROOT"/unwrapped/"$RDI_PLATFORM$RDI_OPT_EXT"/rlwrap -rc -f "$RDI_APPROOT"/scripts/xsdb/xsdb/cmdlist -H "$HOME"/.xsctcmdhistory "$RDI_BINROOT"/loader -exec rdi_xsct "${RDI_ARGSThis is a problem with the rlwrap version bundled with Vivado, probably due to the lack of legacy vsyscall emulation in Arch Linux.
To fix this issue, either drop rlwrap altogether (losing command history and auto-completion), or install  and edit the path to the rlwrap binary in the affected command startup script(s) from:

{{hc|head=/opt/Xilinx/{Vivado,SDK}/YYYY.Q/bin/{xsct,xsdb,xmd,tclsh}|output=
# Use rlwrap to invoke the tool
"$RDI_BINROOT"/unwrapped/"$RDI_PLATFORM$RDI_OPT_EXT"/rlwrap ...
}}

To the following:

{{hc|head=/opt/Xilinx/{Vivado,SDK}/YYYY.Q/bin/{xsct,xsdb,xmd,tclsh}|output=
# Use rlwrap to invoke the tool
/usr/bin/rlwrap ...
# OR run the tool without rlwrap
#"$RDI_BINROOT"/loader -exec rdi_{xsct,xsdb,xmd,tclsh} "${RDI_ARGS[@}"
}}

## Vivado HLS testbench error with GCC
Vivado requires an older version of  (2.26).

The solution proposed in this thread from Xilinx forums suggests to update the fixed headers shipped by Xilinx.

Run:

  # /opt/Xilinx/Vivado/2018.1/lnx64/tools/gcc/libexec/gcc/x86_64-unknown-linux-gnu/4.6.3/install-tools/mkheaders /opt/Xilinx/Vivado/2018.1/lnx64/tools/gcc

## To update Vivado from 2020.1 to Vivado 2020.1.1
If your 2020.1 installation failed to launch and needed to be installed in batch mode, you will need to update using batch mode:

 # ./xsetup -b Update

If Vivado was originally installed by the root user, you will need to launch the update as the root user.

## Configuring an IP in Vivado 2021.2 causes a crash
See When editing an IP with Vivado 2021.2, Vivado may crash and report the following error:

This is due to a conflict between Vivado's and system's version of  library.

A possible workaround is to force Vivado to use the system , by renaming the

 # mv /opt/Xilinx/Vivado/2021.2/tps/lnx64/jre11.0.11_9/lib/libharfbuzz.so /opt/Xilinx/Vivado/2021.2/tps/lnx64/jre11.0.11_9/lib/libharfbuzz.so.bak

## Synthesis fails on certain locales
If your system locale does not use a dot  as the decimal seperator, but for example a comma  (e.g. ), synthesis may fail with errors such as wrong operator types for .

A possible workaround is to force Vivado to use  as the locale for numerics. This can be easily done by appending

 export LC_NUMERIC=en_US.UTF-8

to .

## Fonts ignore system anti-aliasing settings
With OpenJDK 11 and Vivado display scaling activated, the menu and other UI element fonts may render without any anti-antialiasing regardless of desktop environment settings.  This can be fixed by editing the Vivado launch script to append  to the JVM options.

Assuming Vivado is installed in the default location of  where  is the verion (i.e. 2020.2), modify  to include the following:

## Blank/grey window
See Java#Gray window, applications not resizing with WM, menus immediately closing.

## Vitis: cannot open libssl.so.10
While creating a new platform component, cmake errors on:

 cmake: error while loading shared libraries: libssl.so.10: cannot open shared object file: No such file or directory

As suggested in an [https://support.xilinx.com/s/question/0D54U00007j9lkvSAA/vitis-20232-cmake-error-while-loading-shared-libraries-libsslso10?language=en_US upstream support answer:

 # ln -sf /path/to/Vitis/2023.2/tps/lnx64/cmake-3.24.2/libs/Rhel/9/* /usr/lib

## Vitis: Can't load library: ... libswt-pi4-gtk.so ...
You run vitis:

 $ /tools/Xilinx/Vitis/2022.2/bin/vitis

You get error messages here

This problem is due to .

Make sure  has been installed in your computer:

 $ find /usr/lib -iname 'libstdc++.so.6'

Let's fix it:

 # cd /tools/Xilinx/Vitis/2022.2/lib/lnx64.o/Default/
 # mv libstdc++.so.6 libstdc++.so.6.bak
 # ln -sf /usr/lib/libstdc++.so.6 ./libstdc++.so.6

Above way should solve this problem when you run Vitis.

## The self-extracting web installer hangs at "Generating installed devices list"
Install .

## Error while loading shared libraries: libcrypt.so.1
Install .

## Segfault if an LDAP user compiles a Vitis kernel
Symptom: LDAP users encounter segmentation faults, but local users do not.

Example error when a Vitis kernel is compiled using :

 /opt/Xilinx/Vivado/2023.2/bin/rdiArgs.sh: line 369: ... Segmentation fault      (core dumped) "$RDI_PROG" "$@"
 segfault in /opt/Xilinx/Vivado/2023.2/bin/unwrapped/lnx64.o/vivado -exec vivado -notrace -mode batch -source run_ippack.tcl, exiting...
 ERROR: 213-28 Failed to generate IP.
 ...
 command 'ap_source' returned error code
    while executing
 "source vadd.tcl"
    ("uplevel" body line 1)
    invoked from within
 "uplevel \#0 source $tclfile "

If you remove  from the name service switch configuration file, the symptom is gone, however the LDAP users cannot login:

The workaround is to create local users.

## Vivado shows an empty screen on Sway
This behavior happens in versions 2024.{1,2}. Set  in your environment. See https://github.com/swaywm/sway/wiki#issues-with-java-applications.

## Missing libtinfo.so.5 library
When launching Vivado GUI, you may encounter:

 application-specific initialization failed: couldn't load file "libxv_commontasks.so": libtinfo.so.5: cannot open shared object file: No such file or directory

This occurs because Vivado requires an older version of the ncurses library, which can be installed from  .

Alternatively, you can try to create a symbolic link to the newer version:

 # ln -s /usr/lib/libtinfo.so.6 /usr/lib/libtinfo.so.5

## Licensing
Xilinx Vivado contains modules called Intelectual Property (IP) cores and as the name suggests, you should expect licenses to be required for these modules. Two modes of licensing are possible: Floating (server) or Nodelocked (license file).

## Floating License
Set the environment variable  to point to a floating server license. You will have to be on the same network as the server, so connecting with a VPN might be required.

## Nodeblocked License
Generate a license file at https://www.xilinx.com/getlicense . You will shortly receive an automatically generated email with the license file . Download this to {{ic|${HOME}/.Xilinx}} directory.
