# Pkgstats

pkgstats sends a list of all installed packages, the architecture and the mirror you are using to the archlinux.de project. This information is anonymous and cannot be used to identify the user, but it will help Arch developers prioritize their efforts (source code). See also the project's Privacy policy.

## Installation
Install the  package.

## Usage
pkgstats is set up to automatically run every week using a systemd timer. Once installed, it will be activated after the next reboot.

If you do not want to wait for a reboot cycle, you can manually start .

pkgstats can also be run manually: see  for usage information.

## Results and reference
Statistics and documentation are available at https://pkgstats.archlinux.de/ and comparisons can be found at https://pkgstats.archlinux.de/fun .

There is a public JSON API to query statistics: API documentation.
