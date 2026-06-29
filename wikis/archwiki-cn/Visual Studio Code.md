**翻译状态：**

  * 本文（或部分内容）译自 [Visual Studio Code](<https://wiki.archlinux.org/title/Visual_Studio_Code> "arch:Visual Studio Code")，最近一次同步于 2025-5-25，若英文版本有所[更改](<https://wiki.archlinux.org/title/Visual_Studio_Code?diff=0&oldid=831666>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Visual_Studio_Code_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Code](<https://code.visualstudio.com/>) 是由微软开发的跨平台[文本编辑器](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E6%96%87%E6%A1%A3.html#%E6%96%87%E6%9C%AC%E7%BC%96%E8%BE%91%E5%99%A8> "文本编辑器")，基于 Electron 框架构建，并且极具扩展性。可以在编辑器自带的应用商店，或者从 <https://marketplace.visualstudio.com/VSCode> 中安装扩展。“Visual Studio Code” 是 [Code - OSS](<https://github.com/microsoft/vscode/>)仓库的二进制分发版本，该仓库遵循 MIT 许可证，但包含了微软特定的定制，并在[专有许可证](<https://code.visualstudio.com/license>)下发布（有关混合授权的说明，请参阅此 GitHub [评论](<https://github.com/Microsoft/vscode/issues/60#issuecomment-161792005>)）。另外还有一个由社区驱动、遵循 MIT 许可证的二进制发行版本名为[VSCodium](<https://vscodium.com/>)，默认情况下禁用了[遥测](<https://code.visualstudio.com/docs/getstarted/telemetry>)功能。 

##  安装

下列安装包提供 VSCode: 

  * **Code - OSS** — Arch Linux 官方开源版本。配置有[Open VSX](<https://open-vsx.org/>)。

     <https://github.com/microsoft/vscode> || [code](<https://archlinux.org/packages/?name=code>)包

  * **Visual Studio Code** — 微软官方版本，专有软件。

     <https://code.visualstudio.com/> || [visual-studio-code-bin](<https://aur.archlinux.org/packages/visual-studio-code-bin/>)AUR

  * **VSCodium** — 社区驱动的完全开源的 VSCode 版本,不带微软附属和遥测功能[[1]](<https://github.com/VSCodium/vscodium/issues/267#issuecomment-542462446>), 同时启用了Open VSX。

     <https://vscodium.com/> || [vscodium](<https://aur.archlinux.org/packages/vscodium/>)AUR

其他可用版本： 

  * [code-git](<https://aur.archlinux.org/packages/code-git/>)AUR(开发中的最新开源版本)
  * [visual-studio-code-insiders-bin](<https://aur.archlinux.org/packages/visual-studio-code-insiders-bin/>)AUR(微软官方版本,每日更新)
  * [vscodium-bin](<https://aur.archlinux.org/packages/vscodium-bin/>)AUR(社区驱动的完全开源的 VSCode 版本,不带微软附属和遥测功能,二进制包)
  * [vscodium-git](<https://aur.archlinux.org/packages/vscodium-git/>)AUR (社区驱动的完全开源的 VSCode 版本,不带微软附属和遥测功能,最新的开发版)

这些不同的版本都是基于[Code - OSS](<https://github.com/VSCodium/vscodium/blob/master/README.md>)构建的, 但具有不同的许可证和默认配置。值得注意的是，只有专有版本被允许使用官方拓展市场并使用微软的专有扩展，例如[OmniSharp C# Debugger](<https://github.com/OmniSharp/omnisharp-vscode/blob/master/debugger.md>)。后者通过握手机制进行验证，并不能被绕过。有关开源和专有 "Visual Studio Code "构建之间差异的更多信息，请查阅[Code - OSS GitHub wiki](<https://github.com/microsoft/vscode/wiki/Differences-between-the-repository-and-Visual-Studio-Code>). 

###  扩展支持

Code 的一个主要特点是其灵活的API和丰富的扩展生态(托管在[Visual Studio Marketplace](<https://marketplace.visualstudio.com/vscode>)上)。但是，根据Code的扩展商场[使用条款](<https://aka.ms/vsmarketplace-ToU>)，拓展商场只能和微软官方版本配合使用。因此[code](<https://archlinux.org/packages/?name=code>)包并没有内置一个预配置的拓展商场，虽然它支持[Open VSX registry](<https://open-vsx.org/>)，但其并不能提供相同范围的扩展。 

**警告：** 由微软开发的某些语言扩展现强制要求使用专有的Visual Studio Code版本[[2]](<https://github.com/VSCodium/vscodium/issues/2300>)，且无法通过修改`product.json`文件来绕开限制。目前已知受影响扩展包括[C/C++](<https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools>)和[C# Dev Kit](<https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit>)。

已知的解决方法: 

  * 请求开发者将扩展上传至[Open VSX registry](<https://open-vsx.org/>);

  * 根据你使用的版本，安装对应的包来接入官方拓展市场：[code-marketplace](<https://aur.archlinux.org/packages/code-marketplace/>)AUR/[vscodium-bin-marketplace](<https://aur.archlinux.org/packages/vscodium-bin-marketplace/>)AUR/[vscodium-marketplace](<https://aur.archlinux.org/packages/vscodium-marketplace/>)AUR/[vscodium-electron-marketplace](<https://aur.archlinux.org/packages/vscodium-electron-marketplace/>)AUR。这些软件包包含一个 [pacman 钩子](<../zh-cn/Pacman.html#%E9%92%A9%E5%AD%90> "Pacman")，在每次更新后会根据[Github comment](<https://github.com/VSCodium/vscodium/issues/418#issuecomment-643664182>)来更新`product.json`文件。

**提示：** 当你尝试频繁修改 `product.json` 文件时，你可以[设置一个的快捷键](<https://stackoverflow.com/a/69985500>) 更为快捷地重新加载IDE

##  使用

对于以下版本，运行`code`或`code --no-sandbox`即可启动： 

  * [code](<https://archlinux.org/packages/?name=code>)包
  * [visual-studio-code-bin](<https://aur.archlinux.org/packages/visual-studio-code-bin/>)AUR

对于以下版本，运行`code-git`即可启动： 

  * [code-git](<https://aur.archlinux.org/packages/code-git/>)AUR

对于以下版本，运行`codium`即可启动： 

  * [vscodium-bin](<https://aur.archlinux.org/packages/vscodium-bin/>)AUR/[vscodium](<https://aur.archlinux.org/packages/vscodium/>)AUR/[vscodium-git](<https://aur.archlinux.org/packages/vscodium-git/>)AUR/[vscodium-electron](<https://aur.archlinux.org/packages/vscodium-electron/>)AUR

如果你想打开多个实例，可以使用`-n`选项。 

##  配置

**注意：** 像[code-features](<https://aur.archlinux.org/packages/code-features/>)AUR这样通过修改`product.json`来打补丁的软件包，可以覆盖变量 `nameShort` 和 `dataFolderName`，这可能会使下文部分的描述不准确。

  * [code](<https://archlinux.org/packages/?name=code>)包 将配置文件保存在 `~/.config/Code - OSS/User/settings.json`，拓展保存在`~/.vscode-oss`。

  * [visual-studio-code-bin](<https://aur.archlinux.org/packages/visual-studio-code-bin/>)AUR 将配置文件保存在 `~/.config/Code/User/settings.json`，拓展保存在`~/.vscode`。

  * [vscodium](<https://aur.archlinux.org/packages/vscodium/>)AUR 及其衍生版本的配置文件保存在 `~/.config/VSCodium/User/settings.json`，拓展保存在`~/.vscode-oss`。

当从Code迁移到Codium时(反之亦然), 可以直接复制或移动配置文件，因为两者共享大部分代码库，设置是兼容的。 

###  集成终端

点击 _查看 > 集成终端_或使用快捷键 `Ctrl + `` 打开集成终端。 [Bash](<../zh-cn/Bash.html> "Bash")作为默认终端不带任何附加选项的方式启动。 `terminal.integrated.shell.linux` 可以配置默认终端，`terminal.integrated.shellArgs.linux` 可以配置启动终端时的附加参数。 

例子： 
    
    ~/.config/Code/User/settings.json
    
    "terminal.integrated.shell.linux": "/usr/bin/fish",
    "terminal.integrated.shellArgs.linux": ["-l","-d 3"]
    
您可能会收到奇怪的提示，这是由于将集成终端参数设置成了外部终端。要解决此问题，请移除该句，或换用外部终端。 

###  外部终端

如果你使用[Terminator](</wzh/index.php?title=Terminator&action=edit&redlink=1> "Terminator（页面不存在）")作为Arch的默认终端，而且在Visual Studio Code中遇到一个错误`Unable to launch debugger worker process (vsdbg) through the terminal. spawn truecolor ENOENT`，可以换另一个终端（比如，[gnome-terminal](<https://archlinux.org/packages/?name=gnome-terminal>)包）供Visual Studio Code使用。 

`"terminal.external.linuxExec": "Yours alternative terminal"` 用于设置调试默认终端。 

例子： 
    
    ~/.config/Code/User/settings.json
    
    "terminal.external.linuxExec": "gnome-terminal"
    
###  在Wayland下原生运行

Code使用了Electron,你可以参照[Wayland#Electron](<../zh-cn/Wayland.html#Electron> "Wayland")设置来让其在Wayland下原生运行。请注意，某些版本的应用会使用自带的Electron(而不是系统的Electron)，这种情况下应用将不会读取全局配置文件，你需要对[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")进行修改(而不是全局配置文件)。 

使用用户配置文件时，[visual-studio-code-bin](<https://aur.archlinux.org/packages/visual-studio-code-bin/>)AUR和[code](<https://archlinux.org/packages/?name=code>)包都会读取`~/.config/code-flags.conf`处的配置文件。这仅针对这些包及其衍生版本,因为它们使用[修改过的加载脚本](<https://aur.archlinux.org/cgit/aur.git/tree/visual-studio-code-bin.sh?h=visual-studio-code-bin>)来读取。 

如果使用的是[vscodium-bin](<https://aur.archlinux.org/packages/vscodium-bin/>)AUR, 其会加载`~/.config/codium-flags.conf`处的配置文件。注意从终端运行时，使用`codium` (而不是`vscodium`), 否则它将不会在Wayland下原生启动。 

[vscodium](<https://aur.archlinux.org/packages/vscodium/>)AUR不会读取配置文件(因为它没有使用加载脚本)。其提供了一个[桌面项](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html> "桌面项")文件 `vscodium-wayland.desktop` 以在Wayland下原生运行，在菜单中显示为"VSCodium - Wayland"。 

###  原生文件对话框

如果你使用KDE/Plasma, 默认情况下VS Codium将会打开GTK文件对话框。请确保您已经安装了KDE[桌面门户](<../zh-cn/XDG_%E6%A1%8C%E9%9D%A2%E9%97%A8%E6%88%B7.html> "XDG桌面门户")([xdg-desktop-portal-kde](<https://archlinux.org/packages/?name=xdg-desktop-portal-kde>)包)，并将[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")设置为`GTK_USE_PORTAL=1`来解决这个问题。 

###  远程SSH连接

官方的"Remote - SSH"扩展无法与[code](<https://archlinux.org/packages/?name=code>)包（VSCode-OSS）兼容，有两种解决方案： 

  * 安装[code-features](<https://aur.archlinux.org/packages/code-features/>)AUR
  * 尝试安装[Open Remote-SSH 扩展](<https://github.com/jeanp413/open-remote-ssh>)（目前存在一个[PR 使其支持 VSCode-OSS](<https://github.com/jeanp413/open-remote-ssh/pull/189>)）。

##  疑难解答

###  KDE/Plasma 全局菜单失效

Visual Studio Code使用DBus传递菜单，尝试安装 [libdbusmenu-glib](<https://archlinux.org/packages/?name=libdbusmenu-glib>)包。[[3]](<https://github.com/microsoft/vscode/issues/34510#issuecomment-364896975>)

也可以直接: 
    
    $ cp /usr/share/applications/code.desktop ~/.local/share/applications/ 
    
然后注销或者重启KDE桌面。 

###  无法将内容移至回收站

默认状态下，[Electron](<https://electron.atom.io/>)使用`gio`删除文件。如果检测到[Plasma](<../zh-cn/KDE.html> "Plasma")将会自动设置为使用`kioclient5`删除文件。不同的回收站实现可以通过设置`ELECTRON_TRASH`[环境变量](<../zh-cn/Environment_variables.html> "Environment variables")来使用。 

例如，要使用[trash-cli](<https://archlinux.org/packages/?name=trash-cli>)包删除文件： 
    
    $ ELECTRON_TRASH=trash-cli code
    
这样一来，Electron就支持了`kioclient5`，`kioclient`，`trash-cli`，`gio`（默认）和`gvfs-trash`（不推荐）。详情可在此查看[documentation page](<https://github.com/electron/electron/blob/master/docs/api/environment-variables.md#electron_trash-linux>)。 

###  C#无法调试

您若想调试C#[.NET](<../zh-cn/.NET_Core.html> ".NET Core")（使用[OmniSharp扩展](<https://www.omnisharp.net>)），则需要通过AUR安装微软专版。原因是.NET Core调试器仅授权官方微软产品使用，参见[这个github上的讨论](<https://github.com/OmniSharp/omnisharp-vscode/issues/1431#issuecomment-297578930>)。 

若使用开源软件包，调试器失效时不会有太多信息。调试台仅会提示初始信息： 
    
    You may only use the Microsoft .NET Core Debugger (vsdbg) with
    Visual Studio Code, Visual Studio or Visual Studio for Mac software
    to help you develop and test your applications.

要使用开源软件包进行调试，可以选择[netcoredbg](<https://aur.archlinux.org/packages/netcoredbg/>)AUR。要在VS Code中运行，请在项目的.NET Core启动配置中添加这个配置： 
    
    ./.vscode/launch.json
    
    "configurations": [
        {
    ...
        "pipeTransport": {
            "pipeCwd": "${workspaceFolder}",
            "pipeProgram": "/usr/bin/bash",
            "pipeArgs": ["-c"],
            "debuggerPath": "/usr/bin/netcoredbg"
        }
    ...
    
###  无法使用OmniSharp server打开.csproj，Microsoft.Common.props位置无效

您必须从mono切换到合适SDK版本的props。 
    
    /opt/dotnet/sdk/{VERSION}/Sdks/Microsoft.NET.Sdk/Sdk/Sdk.props
    
    $(MSBuildExtensionsPath)\$(MSBuildToolsVersion)\Microsoft.Common.props
    
把导入修改成类似这样： 
    
    /opt/dotnet/sdk/{VERSION}/Sdks/Microsoft.NET.Sdk/Sdk/Sdk.props
    
    /opt/dotnet/sdk/{VERSION}/Current/Microsoft.Common.props
    
###  OmniSharp错误，MSBuild无法定位

[OmniSharp](<https://github.com/OmniSharp/omnisharp-roslyn#introduction>)中提到了Arch Linux用户应当安装[mono-msbuild](<https://archlinux.org/packages/?name=mono-msbuild>)包软件包。否则，您可能收到类似以下的错误： 
    
    OmniSharp Log
    
    [info]: OmniSharp.MSBuild.Discovery.MSBuildLocator
            Registered MSBuild instance: StandAlone 15.0 - "~/.vscode/extensions/ms-vscode.csharp-1.18.0/.omnisharp/1.32.11/omnisharp/msbuild/15.0/Bin"
                MSBuildExtensionsPath = /usr/lib/mono/xbuild
                BypassFrameworkInstallChecks = true
                CscToolPath = ~/.vscode/extensions/ms-vscode.csharp-1.18.0/.omnisharp/1.32.11/omnisharp/msbuild/15.0/Bin/Roslyn
                CscToolExe = csc.exe
                MSBuildToolsPath = ~/.vscode/extensions/ms-vscode.csharp-1.18.0/.omnisharp/1.32.11/omnisharp/msbuild/15.0/Bin
                TargetFrameworkRootPath = /usr/lib/mono/xbuild-frameworks
    System.TypeLoadException: Could not load type of field 'OmniSharp.MSBuild.ProjectManager:_queue' (13) due to: Could not load file or assembly 'System.Threading.Tasks.Dataflow, Version=4.5.24.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a' or one of its dependencies.
    ...

不过您依然有可能成功组建——则很可能取决于您是否也安装了[mono](<https://archlinux.org/packages/?name=mono>)包。 

Omnisharp自带一个mono版本,因此如果它没有找到已安装的版本, 但是您想让omnisharp去寻找安装在计算机上的全局mono版本,您可以尝试在settings.json添加: 
    
    settings.json
    
    "omnisharp.useGlobalMono:"always"

。 

###  使用“Retry as Sudo”保存无效

这个特性在[code](<https://archlinux.org/packages/?name=code>)包软件包中无效，因为微软不支持Arch软件包的打包方式（原生的而非捆绑的Electron）。详情参见[FS#61516](<https://bugs.archlinux.org/task/61516>)和[upstream bug report](<https://github.com/Microsoft/vscode/issues/70403>)。 

二进制发行版[visual-studio-code-bin](<https://aur.archlinux.org/packages/visual-studio-code-bin/>)AUR没有这个问题，该特性在此版本中有效。 

###  键盘变体与键位映射不相符

根据[GitHub上的wiki页面](<https://github.com/Microsoft/vscode/wiki/Keybinding-Issues#troubleshoot-linux-keybindings>)： 

    Switching keyboard layouts under some Linux window managers does not result in a change in the low level X window APIs VS Code uses to read the current keyboard layout. This means that VS Code ends up sometimes reading one of the other configured keyboard layouts and not the current active one. PR welcome...

根据wiki页面，有两种解决方案： 

  1. 确保`setxkbmap -query`返回的第一个键盘布局是你想在VS Code中使用的。
  2. 在设置中使用`"keyboard.dispatch": "keyCode"`，并重启VS Code。这将彻底阻止VS Code确定您的键盘布局。

###  指令“...”未找到

在VS Coded官方编译版本中，`product.json`文件列出了所有能够使用某些特定API的扩展。然而,`product.json`在Code - OSS与VSCodium中是缺失的，尽管这似乎不是由于许可问题。这可能导致一些插件无法正常工作(例如Live Share)。但和强制打开官方拓展商场不同的是，这个解决方案得到了微软的认可[[4]](<https://docs.microsoft.com/en-us/visualstudio/liveshare/reference/linux#vs-code-oss-issues>)。 

您可以尝试通过安装一个[pacman 钩子](<../zh-cn/Pacman.html#%E9%92%A9%E5%AD%90> "Pacman")来解决，它将会在每次包更新时修补文件： 

  * 对于 [code](<https://archlinux.org/packages/?name=code>)包, [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [code-features](<https://aur.archlinux.org/packages/code-features/>)AUR
  * 对于 [vscodium](<https://aur.archlinux.org/packages/vscodium/>)AUR, 安装 [vscodium-features](<https://aur.archlinux.org/packages/vscodium-features/>)AUR
  * 对于 [vscodium-bin](<https://aur.archlinux.org/packages/vscodium-bin/>)AUR, 安装 [vscodium-bin-features](<https://aur.archlinux.org/packages/vscodium-bin-features/>)AUR
  * 对于 [vscodium-electron](<https://aur.archlinux.org/packages/vscodium-electron/>)AUR, 安装 [vscodium-electron-features](<https://aur.archlinux.org/packages/vscodium-electron-features/>)AUR

您也可以手动将相关条目添加到`product.json`文件中的`extensionAllowedProposedApi`部分： 

  * 对于 [code](<https://archlinux.org/packages/?name=code>)包, 编辑 `/usr/lib/code/product.json`
  * 对于 [vscodium](<https://aur.archlinux.org/packages/vscodium/>)AUR, 编辑 `/usr/share/vscodium/resources/app/product.json`
  * 对于 [vscodium-bin](<https://aur.archlinux.org/packages/vscodium-bin/>)AUR, 编辑 `/opt/vscodium-bin/resources/app/product.json`
  * 对于 [vscodium-electron](<https://aur.archlinux.org/packages/vscodium-electron/>)AUR, 编辑 `/usr/lib/vscodium/product.json`

一个使Live Share工作的手动配置示例是[[5]](<https://docs.microsoft.com/en-us/visualstudio/liveshare/reference/linux#vs-code-oss-issues>): 
    
    product.json
    
    ...
      "extensionAllowedProposedApi": [
        "ms-vsliveshare.vsliveshare",
        "ms-vscode.node-debug",
        "ms-vscode.node-debug2"
      ]
    ...
    
再或者，您也可以考虑使用命令行标帜来启动，[就如同GitHub拉取请求中所说的](<https://github.com/Microsoft/vscode-pull-request-github/wiki#3-why-isnt-the-extension-starting>)。 

####  VS Live Share缺失API

要么使用上述解决方案编辑`product.json`，要么使用如下命令打开VS Code： 
    
    $ code --enable-proposed-api ms-vsliveshare.vsliveshare
    
另请注意，为了使此扩展程序正常工作，您需要安装在这里列出的依赖项[[6]](<https://docs.microsoft.com/en-us/visualstudio/liveshare/reference/linux#tips-for-community-supported-distros>)。 

####  指令'remote-containers.openFolder'未找到

如[FS#63374](<https://bugs.archlinux.org/task/63374>)所述，打开VS Code时启用remote-containers API： 
    
    $ code-oss --enable-proposed-api ms-vscode-remote.remote-containers
    
####  指令'GitHub Pull Requests: Configure Remotes...'导致错误（指令'pr.configureRemotes'未找到）

使用如下命令打开VS Code： 
    
    $ code --enable-proposed-api GitHub.vscode-pull-request-github
    
####  错误提示'Git: ssh_askpass: exec(/usr/lib/ssh/ssh-askpass): No such file or directory'

这个错误是由于SSH密匙加密且无法使用SSH agent造成的,参见[这个问题报告](<https://github.com/microsoft/vscode/issues/57488>)。您可以尝试安装一个配置解释器（dialogue provider），例如[SSH keys#x11-ssh-askpass](<../zh-cn/SSH_keys.html#x11-ssh-askpass> "SSH keys")或者其他的代替方案(例如，对于KDE用户您可以尝试使用[ksshaskpass](<https://archlinux.org/packages/?name=ksshaskpass>)包)。 

对于 _ksshaskpass_ ，为了让Code找到它，您需要将其链接到`/usr/lib/ssh/ssh-askpass`: 
    
    # ln /usr/bin/ksshaskpass /usr/lib/ssh/ssh-askpass
    
或者为您的shell设置以下[环境变量](<../zh-cn/Environment_variables.html> "Environment variables"),参见[[7]](<https://github.com/microsoft/vscode/issues/57488#issuecomment-1413903793>): 
    
    GIT_ASKPASS=ksshaskpass
    SSH_ASKPASS=ksshaskpass
    SSH_ASKPASS_REQUIRE=prefer
    
为了禁用Code内置的 _git-askpass_ , 请在以下文件中添加: 
    
    ~/.config/Code - OSS/User/settings.json
    
    {
        "git.useIntegratedAskPass": false
    }

###  终端中的截断字符

太宽的字符可能会被截断。例如Deno堆栈跟踪中使用的斜体粗体文本。 

你可以将"terminal.integrated.rendererType"设置为"experimentalWebgl"来解决这个问题。 

###  运行在Wayland下出现字体模糊

Code默认会在Xwayland下运行,如果你使用[HiDPI](<../zh-cn/HiDPI.html> "HiDPI")屏幕，可能会有字体模糊的问题。你可以尝试让Electron强制在Wayland下运行——参见[#在Wayland下原生运行](<#%E5%9C%A8Wayland%E4%B8%8B%E5%8E%9F%E7%94%9F%E8%BF%90%E8%A1%8C>)。 

或者如你的Wayland环境提供了运行未缩放的Xwayland应用程序的选项，你可以绕过这个问题。你可以附带参数`--force-device-scale-factor=`来运行Code,手动指定其缩放比例。 

例如，将缩放比例设置成2: 
    
    $ code --force-device-scale-factor=2
    
###  找不到接口“org.freedesktop.Secret.Collection”

参见Code官方文档[settings-sync#_troubleshooting-keychain-issues](<https://code.visualstudio.com/docs/editor/settings-sync#_troubleshooting-keychain-issues>)。 

###  使用VSCodium时无法进行Github身份验证

参照[这个Github评论](<https://github.com/VSCodium/vscodium/issues/401#issuecomment-631502370>),当要连接到Github时,将弹出的网址中的"vscodium"改为"vscode"，随后将识别令牌（identification token）拷贝到VSCodium中。如果还是不成功,你可以尝试安装一个密钥环，例如[gnome-keyring](<https://archlinux.org/packages/?name=gnome-keyring>)包，或者你也可以参照[Code官方文档](<https://code.visualstudio.com/docs/editor/settings-sync#_troubleshooting-keychain-issues>)与[这个Github链接](<https://github.com/microsoft/vscode/issues/92972#issuecomment-625751232>)来自己创建一个密钥环。 

如果遇到登录账户后会自动退出的情况，你也可以尝试安装密匙环[gnome-keyring](<https://archlinux.org/packages/?name=gnome-keyring>)包来解决这个问题，如果你使用的是KDE,可能还需要安装[qtkeychain-qt5](<https://archlinux.org/packages/?name=qtkeychain-qt5>)包[[8]](<https://github.com/microsoft/vscode/issues/92972#issuecomment-625751232>)。 

###  找不到密钥环“An OS keyring couldn't be identified”

在一些桌面环境上(例如i3),Code可能会找不到密钥环。你需要手动指定Code使用的密匙环,例如gnome-keyring,在以下文件中添加: 
    
    ~/.vscode-oss/argv.json
    
    {
        ...
        "password-store": "gnome-libsecret",
    }

这个文件地址仅适用于[code](<https://archlinux.org/packages/?name=code>)包包，如果你使用的是其他版本的Code,请相应调整`argv.json`的目录。例如，如果安装的是[visual-studio-code-bin](<https://aur.archlinux.org/packages/visual-studio-code-bin/>)AUR，其地址应调整为`~/.vscode/argv.json`。 
