# Hyprlock

Hyprlock is Hyprland's screen locker. It is highly customizable.

## Installation
Install the  package.

## Configuration
Configuration is done through the hyprlock.conf file in .

## Widgets
Hyprlock works on a widget-based system. Widgets can be created with the following format:

{{hc|~/.config/hypr/hyprlock.conf|2=
widget {
  property = value
  ...
}
}}

{{Note|As many of these can be put in the hyprlock.conf file as desired. For example:

{{hc|~/.config/hypr/hyprlock.conf|2=
label {
  ...
}
label {
  ...
}
input-field {
  ...
}
}}
}}

## Examples
The background of Hyprlock:

{{hc|~/.config/hypr/hyprlock.conf|2=
background {
  monitor = # monitor-agnostic
  path = ~/Pictures/mountain.jpg
  blur_passes = 1
  blur_size = 7
}
}}

An input field for the password:

{{hc|~/.config/hypr/hyprlock.conf|2=
input-field {
  monitor =
  size = 20%, 5%
  font_family = Noto Sans
  dots_size = 0.08
}
}}

A label that displays the time:

{{hc|~/.config/hypr/hyprlock.conf|2=
label {
  monitor =
  text = $TIME
  font_size = 100
  position = 0, -80
}
}}

The  that comes after  can be substituted for any other text, , , and , among others.
