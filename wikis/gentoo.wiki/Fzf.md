[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Fzf&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][GitHub](https://github.com/junegunn/fzf)

[[]][Package information](https://packages.gentoo.org/packages/app-shells/fzf)

**fzf** is an interactive fuzzy finder for the command-line that can be used with any list of data.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
    -   [[1.2] [Integration with Bash]](#Integration_with_Bash)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Finding a string in a filename]](#Finding_a_string_in_a_filename)
    -   [[2.2] [Exact matching]](#Exact_matching)
-   [[3] [See also]](#See_also)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask app-shells/fzf`

### [Integration with Bash]

Append the this line to *\~/.bashrc* (for the current user) or */etc/bash/bashrc* (for all users):

    eval "$(fzf --bash)"

## [Usage]

### [Finding a string in a filename]

To find a string in a filename, run [fzf] and begin typing in the TUI to find the string:

`user `[`$`]`fzf`

### [Exact matching]

The `-e` or `--exact` arguments can tell [fzf] to only report exact matches:

`user `[`$`]`fzf --exact`

## [See also]

-   [find](https://wiki.gentoo.org/wiki/Find "Find") --- a utility to search for files in a directory hierarchy.