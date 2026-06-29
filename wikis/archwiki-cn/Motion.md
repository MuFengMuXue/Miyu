**翻译状态：**

  * 本文（或部分内容）译自 [Motion](<https://wiki.archlinux.org/title/Motion> "arch:Motion")，最近一次同步于 2020-07-25，若英文版本有所[更改](<https://wiki.archlinux.org/title/Motion?diff=0&oldid=626771>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Motion_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [网络摄像机配置](<../zh-cn/%E7%BD%91%E7%BB%9C%E6%91%84%E5%83%8F%E6%9C%BA%E9%85%8D%E7%BD%AE.html> "网络摄像机配置")

[Motion](<https://motion-project.github.io/>) 是监视来自摄像机的视频信号的程序。它能够检测图像的重要部分是否已更改；换句话说，它可以检测运动。 

##  安装

安装 [motion](<https://archlinux.org/packages/?name=motion>)包 软件包。 

##  配置

可以使用 `-c` 选项调用 Motion 来定义特定的配置文件（与 [motionEye](<https://github.com/ccrisan/motioneye/wiki>) 一样）。 

如果不指定 `-c` 或给 Motion 的文件名不存在，Motion 将按以下顺序搜索名为 `motion.conf` 的配置文件： 

  1. 调用 motion 的当前目录
  2. 当前用户主目录（shell 环境变量 `$HOME`）中的目录 `.motion`。例如 `~/.motion/motion.conf`
  3. `/etc/motion/`

默认配置文件（`/etc/motion/motion.conf`）带有注释，因此很容易找到所需的选项以及如何设置（例如 `rotate 90`）。 

默认情况下，Motion 将使用端口 `8080`（每个连接的摄像机则 +1），对 Web 配置服务器（端口 `8080`）和摄像机视频流的访问仅限于本地连接。 
