# Distcc

distcc is a program to distribute builds of C, C++, Objective C or Objective C++ code across several machines on a network to speed up building. It should always generate the same results as a local build, is simple to install and use, and is usually much faster than a local compile. Further, one can use it together with native Arch build tools such as makepkg.

This page uses the following terms:

; client: The client is the computer initiating the compilation.
; volunteer: The volunteer is the computer accepting compilation requests sent by the client. One can setup multiple volunteers or just a single one.

## Installation
Install the  package on all participating PCs in the distcc cluster. For other distributions, or even operating systems including Windows through using Cygwin, refer to the distcc docs or the included man pages  and . Be sure to allow traffic through the port on which distcc runs (the default is 3632/tcp), see Firewalls.

## Configuration
## Modes of operation
Distcc can be run in plain mode (default) or in pump mode. At a high level, the key difference is in how distcc deals with preprocessed source. Plain mode transfers the complete source and compiler arguments. Preprocessing is kept on the client. Pump mode distributes both preprocessing and compilation to the distcc cluster which, in many cases, is more efficient and faster. See  for more details.

## Volunteers
The configuration for the volunteer is stored in . At minimum, add the  switch to cover the IPv4 private network ranges (,  and ) aswell as localhost (). Or, if you have an IPv6 capable network, add  with your IPv6 CIDR. Logging to a file is also nice for troubleshooting if needed.

 DISTCC_ARGS="--allow-private --log-file /tmp/distccd.log"

Or if you need to allow IPv6 access and your network CIDR is /64:

 DISTCC_ARGS="--allow-private --allow aaaa:bbbb:cccc:dddd:eeee:::/64 --log-file /tmp/distccd.log"

If multiple interfaces are present on the machine, consider passing the  option as well. Other options can be defined. See also .

Start  on every participating volunteer. To have  start on boot, enable it.

## Client
## For use with makepkg
Edit  in the following sections:

# The  array will need to have distcc unbanged, i.e. remove its leading exclamation mark.
# Uncomment the  line and add the hostnames or IP addresses of the volunteers, seperated by whitespace. Optionally, follow an IP up with a forward slash and the maximum amount of threads it is to volunteer to the cluster. This list should be ordered from most to least powerful, in terms of processing power.
# Adjust the '  flag to be around double the amount of threads that will comprise the cluster. In the example below, that is 2*(9+5+5+3)=44.

It should be noted that there are no true universal configurations. Try one, test it, compare the results to other setups. The following are a few common setups:

## Plain mode example
 BUILDENV=(distcc color !ccache check !sign)
 MAKEFLAGS="-j44"
 DISTCC_HOSTS="localhost/9 192.168.10.2/5 192.168.10.3/5 192.168.10.4/3"

## Pump mode example
 BUILDENV=(distcc color !ccache check !sign)
 MAKEFLAGS="-j70"
 DISTCC_HOSTS="localhost/9 192.168.10.2,cpp,lzo 192.168.10.3,cpp,lzo 192.168.10.4,cpp,lzo"

Several things to call out here:

* Pump mode generally performs better with a high value for  than plain mode.
* In pump mode, the hostname or IP is suffixed with a literal ',cpp,lzo' as required by pump mode. Further, the localhost in this example was not. This means that distcc will load localhost with the 9 jobs defined and more aggressively distribute the code generation to the volunteers. It could be that in larger clusters, one might want to restrict the number of local jobs on the localhost to fewer to allow processing of distribution out to the cluster. One could also use the ,cpp,lzo suffix to the localhost as well.
* As mentioned above, there is not a single configuration that will work efficiently with all distcc clusters/determining the optimal settings are derived empirically through testing and benchmarking.

## For use without makepkg
## Plain mode example
The minimal configuration for distcc on the client includes the setting of the available volunteers and re-defining the .

 $ export PATH="/usr/lib/distcc/bin:$PATH"
 $ export DISTCC_HOSTS="localhost/9 192.168.10.2/5 192.168.10.3/5 192.168.10.4/3"

## Pump mode example
 $ export PATH="/usr/lib/distcc/bin:$PATH"
 $ export DISTCC_HOSTS="localhost/9 192.168.10.2,cpp,lzo 192.168.10.3,cpp,lzo 192.168.10.4,cpp,lzo"

## Compile
## With makepkg
## Plain mode example
No special steps are needed once  has been configured. Simply call makepkg as normal.

## Pump mode example
The user must start pump prior to compiling whether with makepkg or on the shell. Since pump includes a check to make sure there is a set of  correctly configured, we need to first define a bogus  line. Remember that makepkg will use the values specified in .

 $ export DISTCC_HOSTS="localhost,cpp,lzo"
 $ eval $(pump --startup)

Now call  as normal.

When finished, optionally stop pump:

 $ pump --shutdown

## Without makepkg
## Plain mode example
After exporting the two variables described in #For use without makepkg, simply call the compiler:

 $ make -j44

Some programs may require one to define the CC and/or CXX variable to work properly:

 $ make -j44 CC=distcc CXX=distcc

## Pump mode example
Start pump as illustrated above. Compilation is no different than plain mode.

## With CMake
Use the following CMake options to build a CMake-based project with distcc:

 $ cmake -DCMAKE_C_COMPILER_LAUNCHER=distcc -DCMAKE_CXX_COMPILER_LAUNCHER=distcc ...

## Monitoring progress
 ships with a CLI monitor  one can use to check on compilation status.

The CLI monitor can continually query the status given a delay argument, that being the number of seconds inbetween queries.

## Cross compiling with distcc
One can use distcc to help cross compile:

* A machine running the target architecture must be used as the client.
* Non-native architecture volunteers will help compile but they require the corresponding toolchain to be installed and their distccd pointing to it.

## Arch Linux ARM as clients (x86_64 as volunteers)
This section details how to use Arch Linux (x86_64) volunteers to help an Arch ARM device cross-compile. See these tests for evidence that speed gains on the order of 2-4x can be realized with just a single x86_64 machine helping an ARM device compile.

## Volunteers
The Arch ARM developers highly recommend using the official project toolchains which should be installed on the x86_64 volunteer(s). Rather than manually managing these, the AUR provides two toolchains as well as configuration and systemd service units:

*
*

Setup on the volunteer containing the arm/arm64 toolchains is identical to #Volunteers except that the name of the configuration and systemd service file matches that of the respective package. For example, for armv7h the configuration file is  and the systemd service unit is .

Note that each of the toolchains runs on a unique port thus allowing all four of them to co-exist on the volunteer if needed. Be sure to allow traffic to the port on which distcc runs see Firewalls and .

{| class="wikitable" align="center"
|-
! Target architecture !! Distcc Port
|-
| armv7h || 3635
|-
| armv8h/aarch64 || 3636
|-
|}

## Client
The easiest method to setup the Arch ARM client is to use . It provides all four configurations and systemd service units covering all four flavors of Arch ARM. For example, if the Arch ARM client is running an armv7h image, optionally edit  and change the defaults therein. When ready to build, enable  and compile.

For a more detailed tutorial, see usage-examples.

If one would rather setup the client without using the AUR package mentioned above, manual setup of the client is identical to #Client except, one needs to modify the following two files to define the now non-standard port the volunteers are expected to use. Refer to the table above if using the AUR package.

# : example on an armv7h machine:
# : example on an armv7h machine:

## Note about localhost on ARM clients
When building on Arch ARM devices using x86_64 volunteers, it is highly recommended to exclude the  directive from  since many ARM devices do not have the needed processing power.

To illustrate this effect, consider the following example compiling the linux kernel version 5.10.44's Image target. The client is a RPi4B (aarch64) and the volunteer (192.168.1.288) is a quad core/hyper threaded Intel machine. Each compile job was run only once and  was run in between them.

{| class="wikitable"
|+ Running make -j15 Image CC=distcc CXX=distcc
|-
! DISTCC_HOSTS= !! Time (mm:ss) !! Fold slower
|-
| "192.168.1.288:3636/9" || 6:50 || -
|-
| "localhost/5 192.168.1.288:3636/9" || 10:34 || 2.8x
|-
| "192.168.1.288:3636/9 localhost/5" || 10:13 || 2.7x
|}

## Arch Linux (x86_64) as clients (Arch ARM as volunteers)
This section details how to use Arch ARM volunteers to help an x86_64 client cross-compile. See these tests for evidence that compilation times can be significantly sped up using even 1 Arch ARM volunteer and that up to 2 can double that gain.

## Client
Setup of the client is identical to #Client with distcc running on the standard port 3632.

## Volunteers
 will provide a toolchain to install on the Arch ARM devices to enable cross compilation.

## Additional toolchains
* EmbToolkit: Tool for creating cross compilation tool chain; supports ARM and MIPS architectures; supports building of an LLVM based tool chain
* crosstool-ng: Similar to EmbToolkit; supports more architectures (see website for more information)
* Linaro: Provides tool chains for ARM development

The  provides a nice graphical configuration menu () for configuring the tool chain.

## Troubleshooting
## Quirks compiling the Arch Linux kernel package
If building the kernel from the official PKGBUILD (or many from the AUR), distcc will not work due to the fact that the kernel is hard-coded to use GCC plugins which cannot be supported by distccd due to technical reasons.

A workaround is to edit the kernel source removing the hard-coded requirement of GCC plugins. This can be accomplished with a sed one liner in the PKGBUILD itself inserted before the make step:

 sed -i '/HAVE_GCC_PLUGINS/d' arch/x86/Kconfig

Failure to do this will result in distcc not working during the build. See .

Another option is to pass the  and  variables as part of the build command:

 make all CC=distcc CXX=distcc

## Quirks compiling chromium
Compiling  which uses clang is currently affected by issue#386. In order to circumvent the bug, add the following to the  array in the PKGBUILD:

 'is_cfi=false'
 'use_gold=false'
 'clang_use_default_sample_profile=false'
 'chrome_pgo_phase=0'

## Journalctl
Use journalctl to find out what was going wrong:

 # journalctl $(which distccd) -e --since "5 min ago"

## Adjust log level
By default, distcc will log to  as it goes along. One trick (actually recommended in the distccd manpage) is to log to an alternative file directly. Again, one can locate this in RAM via /tmp. Another trick is to lower to log level of minimum severity of error that will be included in the log file. Useful if only wanting to see error messages rather than an entry for each connection. LEVEL can be any of the standard syslog levels, and in particular critical, error, warning, notice, info, or debug.

Either call distcc with the arguments mentioned here on the client or appended it to DISTCC_ARGS in  on the volunteers:

 DISTCC_ARGS="--allow 192.168.10.0/24 --log-level error --log-file /tmp/distccd.log"

## Limit HDD/SSD usage by relocating $HOME/.distcc
By default, distcc creates  which stores transient relevant info as it serves up work for volunteers to compile. This will avoid needless HDD read/writes and is particularly important for SSDs.

 $ export DISTCC_DIR=/tmp/distcc

## For distccd-alarm
## No such file or directory
Errors similar to the following indicate that the user is mistakenly running the distccd service provided by  and NOT provided by the distccd-alarm packages (i.e. , or .)

Be sure to start the correct service for the target architecture.

 distcc25479 (dcc_execvp) ERROR: failed to exec armv7l-unknown-linux-gnueabihf-g++: No such file or directory

## Avahi-daemon stops publishing when distccd.service starts
Launching  as a service might cause  to stop working. The fix is to create a lifecycle dependency to the  as shown below so  follows any start, stop and restart actions of the .
