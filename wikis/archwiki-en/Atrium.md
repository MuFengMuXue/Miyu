# Atrium

atrium is a Wayland display manager with first-class multiseat support. In a multiseat setup, multiple users share a single machine, each with their own monitor, keyboard, and mouse and an independent login session. atrium handles each seat automatically: it discovers seats, presents a login screen, authenticates users via PAM, and launches their Wayland compositor.

## Installation
Install .

## Configuration
atrium reads two configuration files at startup:

*  — daemon settings (compositor command, session policy, timeouts)
*  — greeter settings (font size, screen blanking timeout, passwordless users)

Both files are installed with commented-out defaults. Refer to the inline comments for available options.

atrium discovers available sessions from . Any installed Wayland compositor that provides a  file there will appear on the login screen automatically.

## Starting
To start atrium, enable  and restart.

## Multiseat
atrium has built-in multiseat support. Each seat requires its own GPU; atrium discovers seats via logind and launches an independent greeter on each one. Devices must be assigned to seats with , but no additional configuration is needed.

See Multiseat Setup Guide for a step-by-step device assignment guide.

## Known limitations
* Limited hotplug — GPU or seat removal/addition at runtime is not yet fully handled. Restart atrium to recover (this ends active sessions).
* No SIGKILL escalation — compositors that ignore SIGTERM are waited on indefinitely.
