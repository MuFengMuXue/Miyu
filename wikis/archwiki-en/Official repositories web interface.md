# Official repositories web interface

This article provides documentation for the web interface through which it is possible to query the official repositories and obtain results in JSON format.

## Package information
Base URL:

## Details
Syntax:

Example: https://archlinux.org/packages/core/x86_64/coreutils/json/

## Files
Syntax:

Example: https://archlinux.org/packages/core/x86_64/coreutils/files/json/

## Package search
The interface supports the same query parameters as the HTML search form, except for .

Base URL:

## Name or description
Parameter:

Example: https://archlinux.org/packages/search/json/?q=pacman

## Exact name
Parameter:

Example: https://archlinux.org/packages/search/json/?name=coreutils

## Description
Parameter:

Example: https://archlinux.org/packages/search/json/?desc=pacman

## Repository
It is possible to use this parameter more than once in order to search in more than one repository (but note that omitting it altogether will search in all repositories).

Parameter:

Values: , , , , , .

Example: https://archlinux.org/packages/search/json/?q=cursor&repo=Core&repo=Extra

## Architecture
It is possible to use this parameter more than once in order to search for more than one architecture (but note that omitting it altogether will search for all architectures).

Parameter:

Values: ,

Example: https://archlinux.org/packages/search/json/?q=cursor&arch=any&arch=x86_64

## Maintainer
Parameter:

Example: https://archlinux.org/packages/search/json/?repo=Extra&maintainer=orphan

## Packager
Parameter:

## Flagged
Parameter:

Values: ,

Example: https://archlinux.org/packages/search/json/?arch=x86_64&flagged=Flagged
