[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=PyCharm_Community_Edition&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.jetbrains.com/pycharm/)

[[]][Package information](https://packages.gentoo.org/packages/dev-util/pycharm-community)

[[]][Wikipedia](https://en.wikipedia.org/wiki/PyCharm "wikipedia:PyCharm")

[[]][GitHub](https://github.com/JetBrains/intellij-community/tree/master/python)

**PyCharm Community Edition** is an open source, single-language integrated developer environment (IDE) for [Python](https://wiki.gentoo.org/wiki/Python "Python") projects created by JetBrains. PyCharm features syntax and error highlighting, auto-indentation, code completion, spell check, and a built-in Python debugger.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Troubleshooting]](#Troubleshooting)
    -   [[2.1] [Partition is mounted with no exec]](#Partition_is_mounted_with_no_exec)
    -   [[2.2] [No JDK found]](#No_JDK_found)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [dev-util/pycharm-community](https://packages.gentoo.org/packages/dev-util/pycharm-community) [[]] [Intelligent Python IDE with unique code assistance and analysis]

  --------------------------------------------------------------------- -----------------
  [`+bundled-jdk`](https://packages.gentoo.org/useflags/+bundled-jdk)   Use bundled jdk
  --------------------------------------------------------------------- -----------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-11 07:46] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install PyCharm:

`root `[`#`]`emerge --ask dev-util/pycharm-community`

## [Troubleshooting]

### [Partition is mounted with no exec]

The IDE cannot execute a test script in the directory. Possible reason: the partition is mounted with \'no exec\' option.

`user `[`$`]`ln -s /tmp /home/pych/.cache/JetBrains/PyCharmCE2023.1/tmp`

### [No JDK found]

If getting the following error message:

[CODE] **ERROR: Cannot start PyCharm Community Edition:**

    No JDK found. Please validate either PYCHARM_JDK, JDK_HOME or JAVA_HOME environment variable points to valid JDK installation.

That means the `JDK` environment variables are not set properly.

If using `bash`:

[FILE] **`~/.bashrc`**

    export PYCHARM_JDK=`java-config -O`

If using `fish`:

[FILE] **`~/.config/fish/conf.d/pycharm.fish`**

    set -x PYCHARM_JDK (java-config -O)

## [See also]

-   [Vim](https://wiki.gentoo.org/wiki/Vim "Vim") --- a [vi](https://wiki.gentoo.org/wiki/Vi "Vi")-like [text editor](https://wiki.gentoo.org/wiki/Text_editor "Text editor"), originally descended from the [Stevie](https://en.wikipedia.org/wiki/Stevie_(text_editor) "wikipedia:Stevie (text editor)") vi clone.
-   [Emacs](https://wiki.gentoo.org/wiki/Emacs "Emacs") --- a class of powerful, extensible, self-documenting text editors.

\

## [External resources]

-   [The official PyCharm blog](https://blog.jetbrains.com/pycharm/)