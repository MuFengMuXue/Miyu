# Godot Engine

Godot Engine is an open-source game engine.

## Installation
Install the  package.

Install the  package for C# programming support.
## Preview versions
Several packages exist in the AUR that correspondent to the several Preview versions.

, ,  for the preview versions, depending on how stable you want, , ,  for packages with C# programming support.

## Legacy versions
To use version 3 of the engine, install the  package.

To use version 2 of the engine, install the  package.

## Export templates
To be able to export your project, you will need prebuilt binaries. If using the Git version, you will need to compile them yourself as described separately for each platform in the official documentation or use . If you are using the stable version, you can install the export templates provided by Godot. Install them by clicking on the engine settings icon in the top right corner, and then press "Install export templates" and provide the downloaded templates.

## Troubleshooting
## UI freezes in Wayland
Godot runs on Wayland using Xwayland, which causes a variety of UI issues, when not running in single window mode. To get around this, start Godot with , then open a project, and enable single window mode in the editor settings.

This issue has been resolved in Godot 4.1.1. [https://github.com/godotengine/godot/pull/79143#issuecomment-1629271532
This issue seems to have recurred in Godot 4.2 With Godot 4.3, Wayland can be used natively. [https://godotengine.org/article/dev-snapshot-godot-4-3-dev-3/#wayland-support-for-linux There are two ways to do this:

* Set the command-line argument .
* Enable the editor setting located at .

The above only makes Godot's client to run under native Wayland, but games still run under Xwayland. In order for games to run under native Wayland, go to project settings, click on "Display Server" at the sidebar, and at the option "Driver.linuxbsd" select wayland.
