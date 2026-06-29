**翻译状态：**

  * 本文（或部分内容）译自 [Faction](<https://wiki.archlinux.org/title/Faction> "arch:Faction")，最近一次同步于 2024-09-02，若英文版本有所[更改](<https://wiki.archlinux.org/title/Faction?diff=0&oldid=815766>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Faction_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**Faction** 是一个用于测试驱动软件开发的 C 语言库。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [libfaction](<https://aur.archlinux.org/packages/libfaction/>)AUR 软件包。 

##  用法

该库提供了几个 C 宏，使编写测试变得更快。 

  * FI 表示 Faction Initialization
  * FT 表示 Faction Test
  * FC 表示 Faction Close

使用 FT 宏时，需要填写三个字段。 

  * AUTHORS() takes a comma-separated list of double-quotation surrounded author names
  * SPEC() takes a single double-quotation surrounded test specification description
  * A C boolean expression (just like when using C assert macros)

按照惯例，Faction Test 应写在包含测试代码的源文件的底部。Test 应由 FACTION 宏保护（见下面的示例）包围，以便在编译时启用或禁用。C 编译器（如 GNU C 编译器 (GCC)）m提供了一种在命令行上启用宏的方法（即 `-D` 标志）。 

##  示例
    
    /* 这就是要测试的函数 */
    int
    increment(int input)
    {
       return (input + 1);
    }
    
    #ifdef FACTION
    #include <faction.h>
    #include <limits.h>
    FI
    
      FT(
        AUTHORS( "timetoplatypus" ),
        SPEC( "increment() returns 1 when given 0" ),
        increment(0) == 1
      );
    
      FT(
        AUTHORS( "timetoplatypus" ),
        SPEC( "increment() returns 0 when given the largest integer value" ),
        increment(INT_MAX) == 0
      );
    
    FC
    #endif
    
可以使用 `gcc _filename.c_ -D FACTION` 对其进行编译。 

##  模式

Faction 有两种编译模式： _最小_ 模式和 _扩展_ 模式。 

上述示例以最小模式编译 Faction。最小化编译只依赖三个库：stdlib、stdio 和 getopt。扩展编译则需要额外的依赖库，包括一些只能通过 GNU 功能测试宏使用的函数。 

因此，要在扩展模式下编译，只需在文件顶部定义 GNU 功能测试宏即可。例如，将前面的示例修改为在扩展模式下编译，就会变成这样： 
    
    #ifdef FACTION
    #define _GNU_SOURCE
    #endif
    
    /* 这就是要测试的函数 */
    increment(int input)
    {
      return (input + 1);
    }
    
    #ifdef FACTION
    #include <faction.h>
    #include <limits.h>
    FI
    
      FT(
        AUTHORS( "timetoplatypus" ),
        SPEC( "increment() returns 1 when given 0" ),
        increment(0) == 1
      );
    
      FT(
        AUTHORS( "timetoplatypus" ),
        SPEC( "increment() returns 0 when given the largest integer value" ),
        increment(INT_MAX) == 0
      );
    
    FC
    #endif

###  扩展模式功能

在扩展模式下， 

  * 可以在运行时使用 `-l` 标记将输出镜像到用户指定的日志文件。
  * 结果表将根据所使用终端的宽度动态调整大小。否则，默认宽度为 78 个字符。

##  参见

  * [Faction 主页](<https://timetoplatypus.com/static/faction/index.html>)
