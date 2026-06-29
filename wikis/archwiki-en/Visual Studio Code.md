# Visual Studio Code

Code is a cross-platform text editor developed by Microsoft, built on the Electron framework. Visual Studio Code is a binary distribution of the MIT-licensed Code - OSS repository, with Microsoft specific customizations and released under a proprietary license. For details on the mixed licensing, see this GitHub comment. There is also a community-driven, MIT-licensed binary release called VSCodium with telemetry disabled by default.

## Installation
The following flavors of Visual Studio Code are available:

*
*
*

These different flavors are all built from the Code - OSS repository, but with different licensing and default configurations. Notably, only the proprietary builds are permitted to use Microsoft's marketplace and use Microsoft proprietary extensions such as the OmniSharp C# Debugger. The latter is enforced by a handshake mechanism, and cannot be circumvented. For more info on the differences between open source and proprietary "Visual Studio Code" branded builds, consult the Code - OSS GitHub wiki.

## Extensions support
One of Code's main strengths is its flexible API and rich extension ecosystem hosted on the Visual Studio Marketplace. However, the terms of use of the marketplace only permit it to be used with the Microsoft branded releases. As a result, the Code - OSS source does not include a configured marketplace. The open-source releases above add the Open VSX extension registry, but this does not offer the same breadth of extensions. It is possible to bypass this limitation.

Known workarounds are:
* ask the maintainer to upload its extension to the Open VSX registry;
* add the Microsoft Visual Studio Code Marketplace by using  (or  for VSCodium). The package installs a Pacman hook that patches  as shown in this Github comment after every package update.

## Usage
Run  to start the application (or  for VSCodium).

If for any reason you wish to launch multiple instances of Visual Studio Code, the  flag can be used.

## Configuration
## Launch configuration
Per-user configuration can be set in the following files. Note that this is specific to these packages, as they use a patched loader script that reads these options.

Using these files, one can add flags for Visual Studio Code, Electron, or Chromium.

{| class="wikitable"
|-
! Package !! Location
|-
|  ||
|-
|  ||
|-
|  || Not supported
|}

## Application configuration
VSC stores settings in  and the extension data in an XDG-nonstandard  directory, using variables from .

This translates to the following default paths in various versions:

*  stores settings in  and extensions in

*  stores settings in  and extensions in

*  stores settings in  and extensions in

When migrating from Code to Codium (or vice versa), the settings directory can be copied or moved. Since they share most of their codebase, the settings are compatible.

## Integrated terminal
View > Integrated Terminal or  opens up an integrated terminal.
By default, Bash is used with no additional arguments, although this can be changed.
 sets the default shell to be used and
 sets the arguments to be passed to the shell.

Example:

You might face weird prompts after setting the integrated shell arguments with an external terminal. Remove the line to solve the problem or use an external terminal.

## External terminal
If you are using Terminator as default terminal for Arch and you have an error on Visual Studio Code: , you can change the terminal that will be used by Visual Studio to another terminal (e.g. ).

 sets the default terminal to be used for exec debug.

Example:

## Running natively under Wayland
Visual Studio Code uses Electron, see Wayland#Electron for more information on how to run it natively under Wayland.

Keep in mind that some applications bring their own copy of Electron and will not read the standard Electron flags file. You can set flags separately in each application's configuration file.

 does not load config files. It provides a dedicated  desktop entry file, which appears as "VSCodium - Wayland" in the menu.

## Native file dialog
If using Plasma, by default VS Codium opens GTK file dialogs. To fix that, ensure that KDE desktop portal () is installed and set the  environment variable.

## Remote SSH
The official "Remote - SSH" extension is not working with  (VSCode-OSS).

There are two options:

* install

* install the Open Remote-SSH extension (there is a PR to make it work with VSCode-OSS).

## Troubleshooting
## Global menu not working in KDE/Plasma
Visual Studio Code uses DBus to pass the menu to Plasma, try installing . === Unable to move items to trash ===

By default, [https://www.electronjs.org/ Electron applications use  to delete files.  is automatically selected instead if Plasma is detected. Different trash implementations can be used by setting the  environment variable.

For example, for deleting files using :

 $ ELECTRON_TRASH=trash-cli code

At the time of writing, Electron supports , , ,  (default) and  (deprecated). More info is available at this documentation page.

## Unable to debug C#
If you want to debug C#.NET (using the OmniSharp extension) then you need to install the Microsoft branded release (from the AUR).  This is apparently because the .NET Core debugger is only licensed to be used with official Microsoft products - see this github discussion.

When using the open-source package, debugging fails fairly quietly. The debug console will just show the initial message:

For debugging with the open-source package,  can be used. To run it in VS Code, add this configuration to .NET Core launch configuration of the project:

{{hc|./.vscode/launch.json|
"configurations": [
    {
...
    "pipeTransport": {
        "pipeCwd": "${workspaceFolder}",
        "pipeProgram": "/usr/bin/bash",
        "pipeArgs": "debuggerPath": "/usr/bin/netcoredbg"
    }
...
}}

This is stable, actively maintained, and the preferred method for open-source VS Code users.

## Unable to open .csproj with OmniSharp server, invalid Microsoft.Common.props location
You have to switch from mono to proper SDK version props.

{{hc|/opt/dotnet/sdk/{VERSION}/Sdks/Microsoft.NET.Sdk/Sdk/Sdk.props|
$(MSBuildExtensionsPath)\$(MSBuildToolsVersion)\Microsoft.Common.props
}}

Modify import to look like this:

{{hc|/opt/dotnet/sdk/{VERSION}/Sdks/Microsoft.NET.Sdk/Sdk/Sdk.props|
/opt/dotnet/sdk/{VERSION}/Current/Microsoft.Common.props
}}

## Error from OmniSharp that MSBuild cannot be located
It is noted in the [https://github.com/OmniSharp/omnisharp-roslyn#introduction OmniSharp introduction that Arch Linux users should install the  package.  Without it, you might get an error like:

You might be able to build anyway (possibly depending whether you have  installed too).

Omnisharp ships with its own mono version, so, if it is unable to locate the installed one, if you want to tell omnisharp to look for a "global" mono installed in your machine, put this in your settings.json:

## Saving with "Retry as Sudo" does not work
This feature does not work in the  package, because Microsoft does not support the way the Arch package is packaged (native instead of bundled Electron). See  and the upstream bug report for more information.

The binary release  does not have this issue, and the feature works there.

## Keyboard variants or keymappings do not map
As per the wiki on GitHub:

: Switching keyboard layouts under some Linux window managers does not result in a change in the low level X window APIs VS Code uses to read the current keyboard layout. This means that VS Code ends up sometimes reading one of the other configured keyboard layouts and not the current active one. PR welcome...

Per the wiki, there are two possible solutions:

# make sure  returns as the first keyboard layout the one you want to work with in VS Code.
# use  in your settings and restart VS Code. This will prevent VS Code from trying to determine your keyboard layout whatsoever.

## Command "..." not found
In the Microsoft branded releases, the  file lists the extensions that are allowed to use certain proposed APIs accessed by extensions. Code - OSS and VSCodium distributions lack these values, though this does not appear to be due to licensing. Unlike the forced Marketplace enabling, this workaround is endorsed by Microsoft This issue can be resolved by installing a Pacman hook that patches the file on every package update:

* For , install
* For , install

You can also manually add the relevant entries to the  section in the  file:

* For , edit
* For , edit

An example of a manual configuration that would make Live Share work is [https://docs.microsoft.com/en-us/visualstudio/liveshare/reference/linux#vs-code-oss-issues:

Finally, you can also enable these options using command line flags, as described for the GitHub pull request extension.

## VS Live Share missing API
Use either the solution above by editing the , or open VS Code with:

 $ code --enable-proposed-api ms-vsliveshare.vsliveshare

Also note that for this extension to work, you need to install dependencies listed here ==== Command 'remote-containers.openFolder' not found ====

Open VS Code enabling remote-containers API as commented in :

 $ code-oss --enable-proposed-api ms-vscode-remote.remote-containers

## Command 'GitHub Pull Requests: Configure Remotes...' resulted in an error (command 'pr.configureRemotes' not found)
Open VS Code with:

 $ code --enable-proposed-api GitHub.vscode-pull-request-github

## Git: ssh_askpass: exec(/usr/lib/ssh/ssh-askpass): No such file or directory
This error is a result of an encrypted ssh-key and inability to use ssh agent, see [https://github.com/microsoft/vscode/issues/57488 bug report. The issue can be solved by installing a dialogue provider like SSH keys#x11-ssh-askpass or the alternatives listed there (e.g.  for KDE).

One thing to note is that for ksshaskpass you would either need to link it from  to get VSCode to find it:

 # ln /usr/bin/ksshaskpass /usr/lib/ssh/ssh-askpass

or set the following environment variables for your shell, see GIT_ASKPASS=ksshaskpass
 SSH_ASKPASS=ksshaskpass
 SSH_ASKPASS_REQUIRE=prefer

To disable VSCode's internal git-askpass, add:

{{hc|~/.config/Code - OSS/User/settings.json|2=
{
    "git.useIntegratedAskPass": false
}
}}

## Cutoff characters in integrated Terminal
Characters that are too wide can end up clipping. For example the italic bold text of Deno stack-traces.

This can be avoided by setting "terminal.integrated.rendererType" to "experimentalWebgl".

## Blurry text under Wayland
Visual Studio Code defaults to run under Xwayland, which may cause blurry text if you are using HiDPI screens. To fix this issue, try forcing Electron to run under Wayland—see #Running natively under Wayland.

Alternatively, if your Wayland environment provides the option to run Xwayland applications unscaled, you can circumvent this issue. You may then run Visual Studio Code with the  option to achieve an appropriate scale for your screen.

For example, for a scaling factor of 2:
 $ code --force-device-scale-factor=2

## No such interface“org.freedesktop.Secret.Collection”
See [https://code.visualstudio.com/docs/editor/settings-sync#_troubleshooting-keychain-issues settings-sync#_troubleshooting-keychain-issues

## Authentication with Github failed while using VSCodium
When connecting a Github account, change "vscodium" to "vscode" in the URL as seen in this comment. Then copy the identification token into VSCodium. Should it still fail, install a keyring like  or create a new keyring as mentioned here in the Visual Studio Code docs and here on Github.

## An OS keyring couldn't be identified
On some desktop environments like i3, VSCode fails to detect the keyring. If you are using gnome-keyring, you can add the following line to force VSCode to use that keyring:

{{hc|~/.vscode-oss/argv.json|2=
{
    ...
    "password-store": "gnome-libsecret",
}
}}

The example path above is for the official  package. You might have to adjust the  directory path depending if you have a different one installed.

## Interface fonts differ from the fonts chosen in the system settings
To render its interface VSCode uses the fonts chosen in the system settings. If you are using OTF fonts, try TTF ones.
