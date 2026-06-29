**翻译状态：**

  * 本文（或部分内容）译自 [Node.js](<https://wiki.archlinux.org/title/Node.js> "arch:Node.js")，最近一次同步于 2026-04-30，若英文版本有所[更改](<https://wiki.archlinux.org/title/Node.js?diff=0&oldid=868498>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Node.js_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Node.js](<https://nodejs.org/>) 是一个 javascript 运行环境，并附带有功能丰富的库.使用 [Google's V8 引擎](<https://code.google.com/p/v8/>)在浏览器外执行代码。 由于 Node.js 是事件驱动、非阻塞 I/O，非常适合于实时 web 应用。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [nodejs](<https://archlinux.org/packages/?name=nodejs>)包。还可以安装长期支持版本： 

  * [nodejs-lts-krypton](<https://archlinux.org/packages/?name=nodejs-lts-krypton>)包 \- 24.X
  * [nodejs-lts-jod](<https://archlinux.org/packages/?name=nodejs-lts-jod>)包 \- 22.X
  * [nodejs-lts-iron](<https://archlinux.org/packages/?name=nodejs-lts-iron>)包 \- 20.X

###  多版本需求

如果需要使用多个 [nodejs](<https://archlinux.org/packages/?name=nodejs>)包 版本，可以使用 [NVM](<https://github.com/creationix/nvm>) (Node Version Manager)。[nvm](<https://archlinux.org/packages/?name=nvm>)包 可以很方便的安装多个版本，并在版本间快速切换。命令很简单： 

将下面命令加入 shell 的启动文件： 
    
    # Set up Node Version Manager
    source /usr/share/nvm/init-nvm.sh
    
项目的 GitHub 页面包含使用文档，命令很简单： 
    
    $ nvm install 8.0
    Downloading and installing node v8.0.0...
    [..]
    
    $ nvm use 8.0
    Now using node v8.0.0 (npm v5.0.0)
    
使用 [nvm](<https://archlinux.org/packages/?name=nvm>)包 时，可以用 [pacman](<https://archlinux.org/pacman/pacman.8.html#_transaction_options_apply_to_em_s_em_em_r_em_and_em_u_em>) 的 `--assume-installed nodejs=<version>` 参数避免安装系统提供的版本。 

如果希望在目录存在 `.nvmrc` 时自动执行 `nvm use`，将[此配置](<https://stackoverflow.com/a/50378304>)添加到 [shell 初始化文件](<../zh-cn/Environment_variables.html#Using_shell_initialization_files> "Environment variables")。 

## Node Packaged Modules

[npm](<https://www.npmjs.org/>) 是官方的 node.js 包管理器，通过 [npm](<https://archlinux.org/packages/?name=npm>)包 进行安装。 

###  使用 npm 管理包

####  安装软件包

任何包可以用以下命令安装： 
    
    $ npm install packageName
    
这个命令会将包安装在当前目录下 `node_modules` 目录内，可执行命令（如果有）安装在 `node_modules/.bin` 目录下. 

作为系统级的全局安装使用 `-g` 选项: 
    
    # npm -g install packageName
    
默认情形下这个命令会将包安装至 `/usr/lib/node_modules/npm`，需要管理员权限. 

###  用户级别安装

作为个人用户级的安装您可以使用一个本地目录来配置 `npm` 。请配置 `npm_config_prefix` [用户环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html#%E6%8C%89%E7%94%A8%E6%88%B7> "环境变量")。npm 和 [yarn](<https://yarnpkg.com/en/>) 都会使用此环境变量。 
    
    ~/.profile
    
    PATH="$HOME/.node_modules/bin:$PATH"
    export npm_config_prefix=~/.node_modules

不要忘记重新登录或读取新配置。 

也可以在 `npm install` 时指定 `--prefix` 参数，但是不建议使用这个方式，因为需要每次安装全局软件包时都记得使用此参数。 
    
    $ npm -g install packageName --prefix ~/.node_modules
    
还有一个方式是设置 `$HOME/.npmrc` 中的 `prefix`。这和设置 `.profile` 中的 `npm_config_prefix="$HOME/.local"` 具有同样的效果，但是仅应用于 _npm_ 。 
    
    $ npm set prefix="$HOME/.local"
    
####  更新包

更新包只需要执行 
    
     $ npm update packageName
    
对于全局环境安装的包 ( ` -g` ) 
    
     # npm update -g packageName
    
**注意：** 请记住全局安装的包需要管理员权限，除非使用 `prefix` 设置到用户可写目录。

#####  更新所有包

有时您只希望更新所有包，去掉包名将试图更新所有包。 
    
     $ npm update
    
或者添加 ` -g` 标记更新全局环境安装的包 
    
     # npm update -g
    
####  删除包

删除使用 ` -g ` 标记安装的包只须： 
    
    # npm -g uninstall packageName
    
**注意：** 请记住全局安装的包需要管理员权限

若删除个人用户目录下的包去掉标记执行： 
    
     $ npm uninstall packageName
    
####  列出所有包

若要显示已安装的包的树形视图执行： 
    
    $ npm -g list
    
仅显示顶层树： 
    
    $ npm list --depth=0
    
要显示需要更新的过期软件包： 
    
    $ npm outdated
    
###  使用 pacman 管理包

一些 node.js 包可以在 [Arch User Repository](<../zh-cn/Arch_User_Repository.html> "Arch User Repository") 找到，命名为 ` nodejs-packageName ` 格式。要向 AUR 中添加 node.js 软件包，请参考 [Node.js 打包准则](<../zh-cn/Node.js_package_guidelines.html> "Node.js package guidelines")。 

##  问题处理

###  npm help 不显示文档

如果 `npm help _topic_` 没有显示 _topic_ 的文档，请使用 `man npm-_topic_`。例如: 
    
    $ npm help install
    Top hits for "install"
    ...
    $ man npm-install
    ... shows the documentation for the npm install subcommand
    
这是 Arch npm 软件包的一个 [bug](<https://bugs.archlinux.org/task/69969>)。 

###  node-gyp python 错误

如果出现 **gyp WARN EACCES user "root" does not have permission to access the ... dir** ，可以使用 _\--unsafe-perm_ 选项: 
    
    # npm install --unsafe-perm -g node-inspector
    
###  无法找到模块错误

从 npm 5.x.x. 开始，package-lock.json 会和 package.json 文件一起创建，如果两个文件引用了不同的版本，会出现冲突。临时解决方案是： 
    
    $ rm package-lock.json
    $ npm install
    
nmp 5.1.0 或以上版本已经解决了此问题，请参考: [missing dependencies](<https://github.com/npm/npm/pull/17508>)

##  其他资源

更多关于 [nodejs](<https://archlinux.org/packages/?name=nodejs>)包 和官方包管理器 [npm](<https://www.npmjs.org/>) 的使用信息您也许需要查询下列额外资源。 

  * [NodeJs Documentation](<https://nodejs.org/documentation/>) Node 文档和教程。
  * [NodeJS Community](<https://nodejs.org/community/>)
  * [API Documentation](<https://www.npmjs.org/doc/>) 官方 ` npm ` API 文档
  * IRC channel #node.js on irc.libera.chat

中文社区 

  * [v2ex NodeJS 节点](<https://www.v2ex.com/go/nodejs>)开发者作品发布与开发探讨
  * [cnodejs.org](<https://cnodejs.org/>) Node.js 专业中文社区
