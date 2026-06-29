# BusyBox

BusyBox provides many common UNIX utilities in a single small executable for embedded systems. The package includes runit; see runit for more information.

## Installation
Install the  package.

Busybox commands are symbolic links to  and thus take very little space. This is especially interesting for low-footprint systems.

## Usage
## getty
The gettys are defined in the file . By default, getty is started on ttys 1 through 4.

In order to enable/disable gettys:

Just replace  with the tty you want getty to start on.
If you want init to ask you before starting getty, then replace  with .

## mdev
See Gentoo:mdev.

## runit
See runit.
