# Debuginfod

debuginfod is a service providing debug information over an HTTP API.

## Installation
 automatically tries to download debug files from servers specified in the  environment variable, which is a string of space separated URLs.

, a dependency of , ships with  and  scripts that set the variable on login, so there is no need to install additional packages. The scripts parse .urls files in  and set the environment variable to  by default.

You can optionally install the  package which provides the  utility. This package is required for debuginfod support in .

## Usage
## Manual download
If one wants to manually retrieve the debug symbols for , along with some source files, one can utilize debuginfod-find:

## Disabling
The debuginfod client service can be disabled by clearing :

 $ unset DEBUGINFOD_URLS

If one wants to use a local cache, with no attempt to contact any server, one can set  to a non-empty string, e.g. .

## Debugger support
Several debuggers support utilizing debuginfod to find debug symbol and source code listing.

{| class="wikitable"
|-
! Package !! Status !! Notes
|-
|  ||  ||
|-
|  ||  ||
|-
|KDE Crash Report ||  ||
|-
|  ||  ||
|-
| AddressSanitizer ||  || If the bug happens in an external library (e.g. a double-free or invalid free usage), there is no way for AddressSanitizer to fetch separate debug symbols and use them for its backtrace.
|}

## Cache
The cache for debuginfod is stored at the location specified by  if set. Otherwise, it will use  or  if  is set. The cache size can grow quite fast, depending on how many debugging sessions you have and which packages are involved.

There are 3 parameters that configure the cache behavior, as described in the man page of :

* : interval between each automatic clean (default is 86400, i.e. 1 day)
* : how long unused data is retained (default is 604800, i.e. one week)
* : how long to remember failed queries (default is 600, i.e. 10 minutes)

Each parameter is defined by a number in a file of the same name in the cache folder.

If you rarely use debuginfod, one can manually delete all directories in the cache (keeping the parameters files), or the complete cache directory.
