# Activating numlock on bootup

## Console
## Early bootup (mkinitcpio)
You can enable numlock right after the kernel boots in the initramfs. This is the only way to ensure numlock is on even during full-disk encryption password entry. Install  and add the  mkinitcpio hook before  in the  HOOKS array:

Then regenerate the initramfs for the change to take effect.

An advantage of using this method is that the numlock setting will be replicated in the later boot process, and new virtual consoles will default to having numlock on.

## With systemd service
First install the  package.

Then create a script to set the numlock on relevant TTYs:

{{hc|/usr/local/bin/numlock|
#!/bin/bash

for tty in /dev/tty{1..6}
do
    /usr/bin/setleds -D +num  Input & Output > Keyboard, in the Hardware tab, in the NumLock on Plasma Startup'' section, choose the desired NumLock behavior.

For this to work, make sure that System Settings > System > Session > Background Services > Keyboard Daemon is enabled.

## GNOME
Run the following command:

 $ gsettings set org.gnome.desktop.peripherals.keyboard numlock-state true

In order to remember last state of numlock key (whether you disabled or enabled), use:

 $ gsettings set org.gnome.desktop.peripherals.keyboard remember-numlock-state true

Alternatively, you can use add  (from ) to a startup script or .

## GDM
Create the following dconf keyfile:

According to gsettings definitions,  decides whether to remember and restore the last state of numlock, and  provides an initial value. The mutter source code shows that if  is false, the  setting won't even be touched, and the query function will return a default false value directly.

To prevent GDM from updating the value of  (force a deterministic numlock state), create a  directory and lock it, as the guide says:

And run the following command:

 # dconf update

This is a general method and also suitable for GDM on Wayland.

## Xfce
In the file , make sure the following values are set to true:

## SDDM
In the file , under the  section, set :

 ...
 Numlock=on

## SLiM
In the file , find the line and uncomment it (remove the ):

## OpenBox
In the autostart file, add:

## LightDM
See LightDM#NumLock on by default.

## LXDM
Set the option in :

## LXQt
Set the option in :

## Wayland
## Sway
See Sway#Activating numlock on startup.

## Hyprland
Set the option in :

{{hc|~/.config/hypr/hyprland.conf|2=
input {
  numlock_by_default = true
  ...
}
}}

## Labwc
See Labwc#Activating numlock on startup.

## SDDM with KWIN (KDE Plasma)
Create or edit :

The file must be owned by

## Plasma Login Manager
Edit :

The file must be owned by

## DWL
Initialize the  struct with the  option:

{{hc|[dwl_source_root/config.def.h|2=
static const struct xkb_rule_names xkb_rules = {
  .options = "numpad:mac",
};
}}
