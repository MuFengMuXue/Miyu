# Ccache

ccache is a compiler wrapper that stores on disk the compiled binaries and offers them back to speed up any eventual recompilation of the same code.  While it may take a few seconds longer to compile a program the first time, subsequent compiles will be much faster as no proper compilation is made, only a lookup through the previously stored binaries.  is compatible with GCC and Clang.

## Installation
Install the  package.

## Configuration
The default behavior can be overridden by configuration files. Priority of the configuration settings is as follows (where 1 is highest):

# Environment variables
# Cache-specific configuration file ()
# System-wide configuration file ()

See  for details.

## Enable ccache for makepkg
To enable ccache when using makepkg edit . In  uncomment  (remove the exclamation mark) to enable caching. For example:

## Enable for command line
If you are compiling your code from the command line, and not building packages, then you will still want to use ccache to help speed things up.

For that, you can prefix each compilation command with .

 $ ccache cc hello_world.c

Alternatively, change your  to include ccaches binaries before the path to your compiler:

 $ export PATH="/usr/lib/ccache/bin:$PATH"

You may want to set this line as an environment variable for regular usage.

## Enable with colorgcc
Since  is also a compiler wrapper, some care needs to be taken to ensure each wrapper is called in the correct sequence.

 export PATH="/usr/lib/colorgcc/bin/:$PATH"    # As per usual colorgcc installation, leave unchanged (don't add ccache)
 export CCACHE_PATH="/usr/bin"                 # Tell ccache to only use compilers here

Then colorgcc needs to be told to call ccache instead of the real compiler.  Edit  and change the  paths to  for all the compilers in :

Newer versions of ccache will always enable color for GCC when  is set. Color is enabled for Clang by default. If the output is not a TTY, ccache will ask the compiler to generate color, storing them in the cache, but stripping them from the output. There remains some issue in unifying -fdiagnostics-color.

## Misc
## Sloppiness
ccache by default uses a very conservative comparison that minimizes both false positives and, for some projects, actual positives. Some of the comparisons are deemed useless and can be changed:

 $ ccache --set-config=sloppiness=locale,time_macros

This tells ccache to ignore the  and time-related macros, which usually invalidate the cache and are considered harmful in reproducible builds. Locale differences are also ignored; ccache cares about it mainly because it determines the language of diagnostic messages.

The  environment variable can be exported to override any pre-existing sloppiness settings.

ccache also by default caches the current directory being used for each build, which means cache misses for build pipelines that use a new, random temporary directory each time it is called. See the Compiling in different directories section of the ccache manual.

## Change the cache directory
You may want to move the cache directory to a faster location than the default  directory, like an SSD or a ramdisk.

To change the cache location only in the current shell:

 $ export CCACHE_DIR=/ramdisk/ccache

Or to change the location by default:

## Set maximum cache size
The default value is 5 gigabyte. If this is too large for you it is possible to use a lower value. But with large projects like the kernel or Firefox this is likely to be too small so it is better to set a higher value:

 $ ccache --set-config max_size=50G

You can verify this worked by checking

 $ ccache --show-stats | grep size
  Cache size (GB):   5.4 /  50.0 (10.80%)

## Disable the cache via environment
If you wish to disable ccache, set the following environment variable:

 $ export CCACHE_DISABLE=1

## CLI
You can use the command-line utility ccache to show a statistics summary:

 $ ccache -s

Clear the cache completely:

 $ ccache -C

## makechrootpkg
It is also possible to use ccache with makechrootpkg from  package. To retain the cache when the chroot is cleaned the makechrootpkg option  can be used to bind the cache directory from the regular system into the chroot, e.g.:

 $ mkdir /path/of/chroot/ccache
 $ makechrootpkg -d /path/to/cache/:/ccache -r /path/of/chroot -- CCACHE_DIR=/ccache

Then ccache can be configured for the chroot in the same way as explained above for the regular system.

## Caveat
ccache is effective only when compiling exactly identical sources. (More exactly, preprocessed sources.)

In the Gentoo Linux community, a source based distribution, ccache has been notorious for its placebo effect, compilation failure (due to undesirable leftover objects), etc. Gentoo requires to turn off ccache before reporting compilation failure. See Gentoo:Handbook:Parts/Working/Features#Caching compilation objects and the blog post titled "Debunking ccache myths" by Diego Pettenò, an ex-Gentoo developer.
