# Ly

Ly is a lightweight TUI (ncurses-like) display manager for Linux and BSD, designed with portability in mind (e.g. it does not require systemd to run).

## Installation
Install the  package. for xserver support install

## Dependencies
For the full Ly experience, Optionally install  and  for screen brightness changer and custom animations.

## Usage
Two steps are required to start Ly at boot. First make sure to enable , then disable  where X stands for a number from 1 to 6.

If you use systemd-logind to dynamically start  instances when the switch to a new TTY occurs, any ly instances for TTYs except the default TTY need to be enabled using a different mechanism, see Ly documentation for instructions and systemd#Using units for information on template units.

## Configuration
System-wide ly configuration files are in  while user configuration files are in
