**翻译状态：**

  * 本文（或部分内容）译自 [Ruby](<https://wiki.archlinux.org/title/Ruby> "arch:Ruby")，最近一次同步于 2025-05-02，若英文版本有所[更改](<https://wiki.archlinux.org/title/Ruby?diff=0&oldid=829226>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Ruby_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

Ruby 是一门专注于简洁和生产力的动态解释型开源编程语言。 

##  安装

要使用 Ruby，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [ruby](<https://archlinux.org/packages/?name=ruby>)包。 

要安装 IRB，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [ruby-irb](<https://archlinux.org/packages/?name=ruby-irb>)包。 

###  多版本

如果你要在同一系统中运行多个版本 (比如 2.0.0-p0 和 1.9.3-p392），最简单的办法就是使用 [RVM](</wzh/index.php?title=RVM&action=edit&redlink=1> "RVM（页面不存在）")（英语：[RVM](<https://wiki.archlinux.org/title/RVM> "en:RVM")）、[chruby](<https://aur.archlinux.org/packages/chruby/>)AUR、[rbenv](<../zh-cn/Rbenv.html> "Rbenv") 或者 [asdf-vm](<https://aur.archlinux.org/packages/asdf-vm/>)AUR。 

###  文档

要通过 `ri` 命令行工具访问文档，安装 [ruby-rdoc](<https://archlinux.org/packages/?name=ruby-rdoc>)包（工具）和 [ruby-docs](<https://archlinux.org/packages/?name=ruby-docs>)包（文档），随后便可以使用 `ri Array`、`ri Array.pop` 等命令查询文档（类似于手册页）。 

### JRuby

Ruby 的 [Java](<../zh-cn/Java.html> "Java") 实现 [JRuby](<https://zh.wikipedia.org/wiki/JRuby> "zhwp:JRuby") 可通过 [jruby](<https://archlinux.org/packages/?name=jruby>)包 安装。 

###  标准库

Ruby 的标准库包含一系列 Ruby 模块（关于模块的更多信息请参见 [#RubyGems](<#RubyGems>)）。[ruby](<https://archlinux.org/packages/?name=ruby>)包 并未包含所有 Ruby 用户预期在标准 Ruby 系统中存在的标准模块，因此某些 Ruby 代码可能无法直接运行。关于标准库模块集的详细信息可参考： 

<https://stdgems.org/>

在 [#RubyGems](<#RubyGems>) 章节中讨论了多种安装模块的方法。若要通过 [pacman](<../zh-cn/Pacman.html> "Pacman") 系统级安装标准模块，可以安装 [ruby-stdlib](<https://archlinux.org/packages/?name=ruby-stdlib>)包。注意 JRuby 无需此操作，因为 [jruby](<https://archlinux.org/packages/?name=jruby>)包 软件包已包含标准模块。 

## RubyGems

RubyGems 是 Ruby 模块（称为 gem）的包管理器，和 [pacman](<../zh-cn/Pacman.html> "Pacman") 与 Arch Linux 的关系大致相当，可通过 [rubygems](<https://archlinux.org/packages/?name=rubygems>)包 安装（[ruby](<https://archlinux.org/packages/?name=ruby>)包 依赖）。 

###  配置

在 Arch Linux 中，默认情况下运行 `gem` 时，gem 会按用户安装到 `~/.local/share/gem/ruby/` 目录下，而非安装到系统级的 `/usr/lib/ruby/gems/` 目录。这被视为 Arch 上管理 gem 的最佳实践，因为若采用系统级安装可能会与 Pacman 安装的 gem 产生冲突。 

推荐的手动配置方法是设定 `$GEM_HOME` 环境变量，并将其[添加](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "添加")到 `$PATH` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")中，以便执行 RubyGems 的二进制文件： 
    
    ~/.profile
    
    export GEM_HOME="$(gem env user_gemhome)"
    export PATH="$PATH:$GEM_HOME/bin"

此配置使得无需输入完整路径即可运行可执行 gem，而库 gem 无需修改路径即可正常使用。 

**注意：** 保存修改后，请重启终端以使配置生效。

###  用法

查看已安装的 gem 列表: 
    
    $ gem list
    
获取某个 gem 的详细信息： 
    
    $ gem spec "gem_name"
    
默认情况下，`gem list` 和 `gem spec` 开启了 `--local` 选项，导致 gem 只会在本地系统里进行搜索。这可以用 `--remote` 参数来覆盖。因此，可以这样搜索 mysql2 gem： 
    
    $ gem list --remote mysql2
    
安装某个 gem： 
    
    $ gem install mysql2
    
可以通过不安装本地文档加快一点安装速度： 
    
    $ gem install mysql2 --no-document
    
**注意：** 这可以通过配置以下 `~/.gemrc` 文件成为默认选项： 
    
    ~/.gemrc
    
    gem: --no-document
    
更新所有已安装的 gem： 
    
    $ gem update
    
###  按用户或以系统级安装 gem

在 Arch Linux 下运行 `gem` 时，gem 默认按用户安装（即安装到 `~/.gem/ruby/`），而非以系统级安装（即安装到 `/usr/lib/ruby/gems/`）。这被认为是 Arch 上管理 gem 的最好方式，因为系统级安装可能会和 pacman 安装的 gem 冲突。 

可以通过以 root 身份运行 `gem` 命令并附加 `--no-user-install` 标志以系统级安装 gem。若要将此标志设为默认行为，可在 `/etc/gemrc`（系统级配置）或 `~/.gemrc`（用户级配置，优先级更高）中将原有的 `--user-install` 参数替换为 `--no-user-install`。 

[Bundler](<#Bundler>) 通过将 gem 打包到应用程序中，在一定程度上解决了这些问题。请参阅下面关于使用 Bundler 的部分。 

### Bundler

[Bundler](<https://bundler.io>) 用于指定应用程序所依赖的 gem，并可以同时指定所需版本。完成依赖声明后，Bundler 将安装所有必需的 gem（包含完整的依赖树）并记录安装结果以便后续检查。默认情况下，Bundler 将 gem 安装到统一位置，但也支持直接安装到应用程序目录中。当运行应用程序时，Bundler 可确保使用正确的 gem 版本（即使系统中存在同一 gem 的多个版本），这需要以下配置： 

  * 应用程序必须通过 `bundle exec` 命令启动
  * 需在应用程序的主执行文件中添加所需样板代码

安装 Bundler： 
    
    $ gem install bundler
    
新建一个 bundle： 
    
    $ bundle init
    
然后编辑当前目录下的 `Gemfile`（由 `bundle init` 创建）以添加所需的 gem： 
    
    Gemfile
    
    gem "rails", "3.2.9"
    gem "mysql2"
    
运行下面的命令安装所有必需的 gem 到 `GEM_HOME`： 
    
    $ bundle install
    
或者，运行下面的命令把 gem 安装到工作路径的 `.bundle`： 
    
    $ bundle config set --local path '.bundle'
    
**注意：** 命令 `bundle install --path .bundle` 已过时。但如果你的 Bundler 或 Ruby 版本较低导致上条命令无效，可以选择尝试使用这条命令。

别忘了编辑主执行文件： 
    
    #!/usr/bin/env ruby
    
    # "This will automatically discover your Gemfile, and make all of the gems in
    # your Gemfile available to Ruby." <https://bundler.io/rationale.html>
    require 'bundler/setup'
    
    ...
    
最后运行你的程序: 
    
    $ bundle exec _主执行文件.rb_
    
###  使用 pacman 管理 gem

除了使用 `gem` 管理 gem，也可以通过 [pacman](<../zh-cn/Pacman.html> "Pacman") 或 [AUR 助手](<../zh-cn/AUR_%E5%8A%A9%E6%89%8B.html> "AUR 助手")进行管理。Ruby 软件包遵循命名约定：`ruby-_gem名称_`。 

此方法具有以下优势： 

  * gem 会随系统其他软件一同更新
  * 安装的 gem 可在系统范围内使用，而非仅限于安装它们的用户

**注意：** 另有工具可通过自动生成指定 gem 的 PKGBUILD 文件，实现 gem 与 pacman 的集成，参见[创建软件包#PKGBUILD 生成器](<../zh-cn/%E5%88%9B%E5%BB%BA%E8%BD%AF%E4%BB%B6%E5%8C%85.html#PKGBUILD_%E7%94%9F%E6%88%90%E5%99%A8> "创建软件包")。

#### Quarry

Quarry 工具用于通过 [RubyGems](<https://rubygems.org>) 生成二进制 Arch Linux 仓库，可作为手动从 AUR 构建软件包的简化替代方案。其源代码托管于 [Github](<https://github.com/anatol/quarry>)。 

Quarry 仓库由 Arch 开发者 anatolik 维护，地址为 <https://pkgbuild.com/~anatolik/quarry/> ，包含了许多流行的 gem，并可根据请求添加新 gem。 

启用方法请参阅[非官方用户仓库#quarry](<../zh-cn/%E9%9D%9E%E5%AE%98%E6%96%B9%E7%94%A8%E6%88%B7%E4%BB%93%E5%BA%93.html#quarry> "非官方用户仓库")。 

随后可[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")所需的 gem 包，软件包名为 `ruby-_gem名称_`（如 [ruby-rails](<https://archlinux.org/packages/?name=ruby-rails>)包）。 

一般性问题可至 <https://bbs.archlinux.org/viewtopic.php?id=182729> 询问。 

##  交互式 Shell

### Pry

Pry 是 Ruby 标准 IRB Shell 的强大替代品，具备语法高亮、灵活的插件架构、运行时代码调用及源代码与文档浏览功能。 

安装与启动方法： 
    
    $ gem install pry
    $ pry
    
##  另见

  * [Ruby on Rails](<../zh-cn/Ruby_on_Rails.html> "Ruby on Rails")
  * Ruby - <https://www.ruby-lang.org/>
  * Bundler - <https://bundler.io/>
  * [why's (poignant) Guide to Ruby](<https://en.wikipedia.org/wiki/Why%27s_\(poignant\)_Guide_to_Ruby> "wikipedia:Why's \(poignant\) Guide to Ruby")
  * [Learn Ruby The Hard Way](<http://learnrubythehardway.org/book/>)
