# PowerShell

PowerShell is a cross-platform task automation framework and scripting language developed by Microsoft. Designed for system administrators and power users, it facilitates the automation of administrative tasks through a command-line shell and a scripting language, enabling efficient management of Microsoft Windows and other operating systems.

## Installation
Install  or .

PowerShell Core can also be installed via the .NET SDK, if this is already configured. Alternatively, PowerShell can also be installed with the Snap package manager. It's packaged as powershell in Snapcraft.

After installation, PowerShell can be started with  command. It's highly recommended to fetch the PowerShell help files from Internet. It can be done with  cmdlet.

## Telemetry
By default PowerShell collects telemetry. It can be disabled by setting the following environment variable
 POWERSHELL_TELEMETRY_OPTOUT=1

## PowerShell remoting over SSH
PowerShell has a built-in remote management system via the  cmdlets. This system can run over SSH. In order to configure a Linux SSH host for this, the OpenSSH server configuration file  needs the following line:

It is then possible to use the ,  and  cmdlets to control the host. This can also be done from Linux to Windows or vice versa. For an usage example, see the Microsoft documentation.
