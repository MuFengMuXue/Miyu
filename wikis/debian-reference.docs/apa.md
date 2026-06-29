> **原文链接：** [https://www.debian.org/doc/manuals/debian-reference/apa.zh-cn.html](https://www.debian.org/doc/manuals/debian-reference/apa.zh-cn.html)

---

::: navheader
  附录 A. 附录                                                        
  --------------------------------------------------------------- --- ---
  [![上一页](images/prev.png)](ch12.zh-cn.html){accesskey="p"}           

------------------------------------------------------------------------
:::

:::::::::::::::::::::::::::::: appendix
::::: titlepage
<div>

<div>

# []{#_appendix}附录 A. 附录 {#附录-a.-附录 .title}

</div>

</div>
:::::

::: toc
**目录**

[ [A.1. Debian 迷宫](apa.zh-cn.html#_the_debian_maze) ]{.section}

[ [A.2. 版权历史](apa.zh-cn.html#_copyright_history) ]{.section}

[ [A.3. 简体中文翻译](apa.zh-cn.html#_zh-CN_translate) ]{.section}

[ [A.4. 文档格式](apa.zh-cn.html#_document_format) ]{.section}
:::

下列为本文档背景。

:::::: section
::::: titlepage
<div>

<div>

## []{#_the_debian_maze}A.1. Debian 迷宫 {#a.1.-debian-迷宫 .title}

</div>

</div>
:::::

Linux 系统是一个面向网络计算机的功能强大的计算平台。然而，学习使用它的全部功能并非易事。使用非 PostScript 的打印机配置 LPR 打印机队列，就是个好例子。（自从使用新 CUPS 系统的新的安装系统出现后，就不再会有问题。）

有一张完整而详尽的地图叫做"SOURCE CODE"，它非常准确但极难理解。还有一些参考书叫 HOWTO 和 mini-HOWTO，它们易于理解，但给出了太多细节反而让人忘记了大方向。为了使用某个命令，我有时得在长长的 HOWTO 中找上半天。

我希望这个"Debian 参考手册（版本 2.139）"（2026-04-22 04:01:24 UTC）能帮助在 Debian 迷宫里面徘徊的人们，为他们提供一个好的出发方向。
::::::

:::::::::: section
::::: titlepage
<div>

<div>

## []{#_copyright_history}A.2. 版权历史 {#a.2.-版权历史 .title}

</div>

</div>
:::::

Debian 参考手册由我（Osamu Aoki\<osamu at debian dot org\>）发起，将其作为一个个人系统管理笔记。其中的许多内容都是我从 [Debian 用户邮件列表](https://lists.debian.org/debian-user/){.ulink}和其他 Debian 相关资源获得的积累。

在采纳了来自 Josip Rodin 的建议之后（Josip Rodin 在 [Debian 文档项目（DDP）](https://www.debian.org/doc/ddp){.ulink}中非常活跃）,"Debian 参考手册（第一版，2001-2007）"成为了 DDP 文档的一员。

6 年后，我意识到原来的"Debian 参考手册（第一版）"内容陈旧，便开始重新很多内容。新的"Debian 参考手册（第二版）"在 2008 年发布。

我已经更新了 \"Debian 参考手册 (版本 2)\" 来处理新的话题 (Systemd, Wayland, IMAP, PipeWire, Linux 内核 5.10)，移除过期话题 (SysV init, CVS, Subversion, SSH 1 协议, 2.5 版本之前的 Linux 内核 ). Jessie 8 (2015-2020) 版本的情况，或者更老的内容也被大部分移除。

这个 \"Debian 参考手册 (version 2.139)\" (2026-04-22 04:01:24 UTC) 覆盖了大部分 Trixie (=`stable`{.literal}) 和 Forky (=`testing`{.literal}) Debian 版本。

教程的起源和灵感，可以通过下面的内容来追溯。

::: itemizedlist
-   \"[Linux 用户手册](https://tldp.org/pub/Linux/docs/ldp-archived/users-guide/){.ulink}\" Larry Greenfield (1996年12月)

    ::: itemizedlist
    -   该文档被后来的《Debian 教程》取代
    :::

-   \"Debian 教程\" Havoc Pennington (1998年12月11日)

    ::: itemizedlist
    -   部分由 Oliver Elphick, Ole Tetlie, James Treacy, Craig Sawyer 和 Ivan E. Moore II 书写

    -   该文档被后来的 《Debian GNU/Linux: 安装和使用手册》取代
    :::

-   \"[Debian GNU/Linux: 安装和使用手册](https://www.gutenberg.org/files/6527/6527-h/6527-h.htm){.ulink}\" John Goerzen 和 Ossama Othman (1999)

    ::: itemizedlist
    -   该文档被《Debian 参考手册（第一版）》取代
    :::
:::

软件包和文档描述的一些起源和灵感，能够通过下面的内容来追溯。

::: itemizedlist
-   \"[Debian FAQ](https://www.debian.org/doc/manuals/debian-faq/){.ulink}\" (2002 年 3 月版本，当时是由 Josip Rodin 维护)
:::

其它内容的一些起源和灵感，能够通过下面的内容来追溯。

::: itemizedlist
-   \"Debian 参考手册 (第一版)\" Osamu Aoki (2001--2007)

    ::: itemizedlist
    -   于 2008 年被这个新的 \"Debian 参考手册 (第二版)\" 取代。
    :::
:::

先前的"Debian 参考手册 (第一版)"由许多贡献者创建。

::: itemizedlist
-   Thomas Hood 是网络配置主题的主要内容贡献者

-   Brian Nelson 突出贡献了关于 X 和 VCS 的相关主题

-   Jens Seidel 对构建脚本和许多内容的更正提供了帮助

-   David Sewell 进行了大量的校对

-   来自翻译者、贡献者和 bug 报告者的许多贡献
:::

Debian 系统中许多的手册页面和 info 信息页面，和上游 网站页面，[Wikipedia](https://www.wikipedia.org/){.ulink} 维基百科文档，被用来作为这个文档的主要参考。在一定范围内，青木修（Osamu Aoki）也考虑了[公平使用](https://zh.wikipedia.org/wiki/Fair_use){.ulink}，它们中的许多地方，尤其是命令的定义，在细心的编辑以适应样式和本文档的目标后，作为了本文档的短语部分。

gdb 调试器的描述使用了扩展 [Debian 维基内容的回溯系统](https://wiki.debian.org/HowToGetABacktrace){.ulink}, 这是被 Ari Pollak, Loïc Minier, 和 Dafydd Harries 同意的.

除了上面提到的部分之外，"Debian 参考手册（版本 2.139）（2026-04-22 04:01:24 UTC）"的大部分内容是我自己的工作。一些贡献者也会对内容进行更新。

作者 Osamu Aoki 在此感谢所有在文档写作过程中曾给予帮助的人。
::::::::::

::::::::: section
::::: titlepage
<div>

<div>

## []{#_zh-CN_translate}A.3. 简体中文翻译 {#a.3.-简体中文翻译 .title}

</div>

</div>
:::::

该文档的简体中文翻译，通过 Debian 简体中文邮件列表召集讨论，具体翻译工作通过 weblate 翻译平台进行。欢迎大家继续通过 weblate 参加翻译工作:

[` https://hosted.weblate.org/projects/debian-reference/translations/zh_Hans/ `{.literal}](https://hosted.weblate.org/projects/debian-reference/translations/zh_Hans/){.ulink}

该项目继续征集校对人员,欢迎大家在 weblate 参与,有翻译得不好的地方,可以直接修改。

Debian 官方网站也及时同步了我们的最新翻译成果:

::: itemizedlist
-   [https://www.debian.org/doc/manuals/debian-reference/index.zh-cn.html](https://www.debian.org/doc/manuals/debian-reference/index.zh-cn.html){.ulink}
-   [https://www.debian.org/doc/manuals/debian-reference/debian-reference.zh-cn.pdf](https://www.debian.org/doc/manuals/debian-reference/debian-reference.zh-cn.pdf){.ulink}
:::

该手册中文版本软件包名字为：debian-reference-zh-cn

官方网页为： [` https://packages.debian.org/testing/doc/debian-reference-zh-cn `{.literal}](https://packages.debian.org/testing/doc/debian-reference-zh-cn){.ulink}

::: {.tip style="margin-left: 0.5in; margin-right: 0.5in;"}
+:---------------------------------:+:---------------------------------------------------------------------------------------------------------------------------------------+
| ![\[提示\]](images/tip.png)       | 提示                                                                                                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
|                                   | 在 `testing`{.literal} 版里面，软件包更新比较及时，大家如果在 apt 源里面设置了 `testing`{.literal} 源,则可以直接用                     |
|                                   |                                                                                                                                        |
|                                   | ``` screen                                                                                                                             |
|                                   | #apt-get install debian-reference-zh-cn                                                                                                |
|                                   | ```                                                                                                                                    |
|                                   |                                                                                                                                        |
|                                   | 命令安装该软件包。 安装软件包后，就可以在本机看 pdf 格式（`/usr/share/debian-reference/debian-reference.zh-cn.pdf`{.literal}）的文档。 |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
:::

对该手册翻译的任何问题或建议,欢迎大家在 Debian 简体中文邮件列表讨论:

::: itemizedlist
-   debian-chinese-gb dot lists.debian.org
-   debian-l10n-chinese dot lists.debian.org
:::

《Debian 参考手册》（第二版）翻译相关数据统计如下:

统计信息截止到:2017-09-19

（一）英文原版情况

手册英文有 7638 个字符串，82658 个词。英文版 pdf 文件，有 271 页。

（二）翻译耗时

zh-cn.po 文件 git 初始提交日期为：

``` screen
commit 20948e15ffa005b6b4b6c6dd36f2833f01368f09
Author: Faris Xiao
Date:   Wed Jun 29 18:59:03 2016 +0800

    Chines init version po copy from templates.pot
```

我们在近 15 个月的时间内，完成了全部翻译。

（三）git 提交数量

weblate 和手工，总共有 688 次 git 提交。

``` screen
git log zh-cn.po|grep commit|wc -l
688
```

（四）参与情况

从 weblate 和 git 日志统计，先后有 26 位翻译贡献者。

贡献者的名字是：

chimez Dongliang Mu John Zhang Liang Guo zlffcn Zunway 孤月蓝风 李ZQ Anthony Fok mao CGH Jiagang Xu rainysia Xie Yanbo Zhang Rui zhangmiao wenqin chen Zongren Zhang scmarxx Boyuan Yang zlf chiachen Philip Ye 吴昊昱 Lou Letian 肖盛文
:::::::::

:::::: section
::::: titlepage
<div>

<div>

## []{#_document_format}A.4. 文档格式 {#a.4.-文档格式 .title}

</div>

</div>
:::::

目前，英文原始文档使用 [DocBook](https://zh.wikipedia.org/wiki/DocBook){.ulink} XML 文件写作。 此源文件可被转换成 HTML、纯文本、PostScript 和 PDF。(发布时会省略部分格式。)
::::::
::::::::::::::::::::::::::::::

::: navfooter

------------------------------------------------------------------------

  --------------------------------------------------------------- --------------------------------------------------------------- ---
  [![上一页](images/prev.png)](ch12.zh-cn.html){accesskey="p"}                                                                       
  第 12 章 编程                                                    [![起始页](images/home.png)](index.zh-cn.html){accesskey="h"}     
  --------------------------------------------------------------- --------------------------------------------------------------- ---
:::
