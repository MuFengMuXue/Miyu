# Mailnag

mailnag is a Wayland e-mail notification daemon. It integrates well with  and  and comes with interactive configuration tooling, making setup very straight-forward.

## Installation
mailnag can be installed with the  package.

## Configuration
Run  to create an initial configuration at .

## Usage
Users can run mailnag from within a shell while running a Wayland or Xorg session, given that a notification daemon is running.

## Autostart
mailnag supports XDG Autostart out of the box. A systemd user service example has been included below as another option.

## systemd user unit
Users will probably want to run mailnag in a systemd unit. Provided below is an example user unit where user id is the numeric ID of the user where this service is installed.

Then start .

## XDG
The  package provides a  file for use with XDG Autostart that is supported by various desktop environments.
