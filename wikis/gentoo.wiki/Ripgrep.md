[[]][Package information](https://packages.gentoo.org/packages/sys-apps/ripgrep)

[[]][GitHub](https://github.com/BurntSushi/ripgrep)

**ripgrep** is search tool that can recursively search directories for regex search patterns. ripgrep can replicate much of the functionality of the [grep](https://wiki.gentoo.org/wiki/Grep "Grep") command, but has a generally wider scope.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Search for a string in current directory]](#Search_for_a_string_in_current_directory)
    -   [[2.3] [Find a string in a file]](#Find_a_string_in_a_file)
    -   [[2.4] [Prettified Output for JSON Results]](#Prettified_Output_for_JSON_Results)
    -   [[2.5] [Suppress Error Messages]](#Suppress_Error_Messages)
    -   [[2.6] [Set Maximum Filesize for Search]](#Set_Maximum_Filesize_for_Search)
    -   [[2.7] [Replace Each Match]](#Replace_Each_Match)
    -   [[2.8] [Disable Searching Inside Compressed Files]](#Disable_Searching_Inside_Compressed_Files)
    -   [[2.9] [Enable Searching Inside Compressed Files]](#Enable_Searching_Inside_Compressed_Files)
    -   [[2.10] [Display Statistics After Search]](#Display_Statistics_After_Search)
    -   [[2.11] [Search Both Binary and Text Files]](#Search_Both_Binary_and_Text_Files)
    -   [[2.12] [List Available File Types]](#List_Available_File_Types)
    -   [[2.13] [Output Results in Vim-Compatible Format]](#Output_Results_in_Vim-Compatible_Format)
    -   [[2.14] [Read Ignore Patterns from a File]](#Read_Ignore_Patterns_from_a_File)
    -   [[2.15] [Disable Memory-Mapped I/O]](#Disable_Memory-Mapped_I.2FO)
-   [[3] [File Listing]](#File_Listing)
    -   [[3.1] [Listing Files]](#Listing_Files)
    -   [[3.2] [Searching for Specific Filenames]](#Searching_for_Specific_Filenames)
-   [[4] [Sorting Results]](#Sorting_Results)
    -   [[4.1] [Sorting in Ascending Order]](#Sorting_in_Ascending_Order)
    -   [[4.2] [Sorting in Descending Order]](#Sorting_in_Descending_Order)
-   [[5] [Configuration]](#Configuration)
-   [[6] [Integration with Other Tools]](#Integration_with_Other_Tools)
-   [[7] [Removal]](#Removal)
    -   [[7.1] [Unmerge]](#Unmerge)
-   [[8] [Debug]](#Debug)
-   [[9] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [sys-apps/ripgrep](https://packages.gentoo.org/packages/sys-apps/ripgrep) [[]] [Search tool that combines the usability of ag with the raw speed of grep]

  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+pcre`](https://packages.gentoo.org/useflags/+pcre)   Add support for Perl Compatible Regular Expressions
  [`debug`](https://packages.gentoo.org/useflags/debug)   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-05 06:55] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[sys-apps/ripgrep]](https://packages.gentoo.org/packages/sys-apps/ripgrep)[]]:

`root `[`#`]`emerge --ask sys-apps/ripgrep`

## [Usage]

### [Invocation]

To view ripgrep usage and options:

`user `[`$`]`rg --help`

### [Search for a string in current directory]

To recursively search files in the current directory for a string:

`user `[`$`]`rg <string>`

### [Find a string in a file]

Use ripgrep to find a string in a file:

`user `[`$`]`rg <string> <file>`

### [Prettified Output for JSON Results]

Use this option to provide a more readable format for JSON search results:

`user `[`$`]`rg --pretty`

### [Suppress Error Messages]

Suppress all error messages:

`user `[`$`]`rg --quiet`

### [Set Maximum Filesize for Search]

Limit the search to files of a specific size:

`user `[`$`]`rg --max-filesize N`

Example: Limit search to files smaller than 1MB

`user `[`$`]`rg --max-filesize 1M "pattern"`

### [Replace Each Match]

Replace each matched instance with a specified string:

`user `[`$`]`rg --replace REPLACEMENT "pattern"`

Example: Replace \"foo\" with \"bar\" in the search results

`user `[`$`]`rg --replace bar foo`

### [Disable Searching Inside Compressed Files]

Avoid searching within compressed files:

`user `[`$`]`rg --no-search-zip`

### [Enable Searching Inside Compressed Files]

Search within compressed files such as .zip and .gzip:

`user `[`$`]`rg --search-zip`

### [Display Statistics After Search]

Show detailed statistics after completing the search:

`user `[`$`]`rg --stats`

### [Search Both Binary and Text Files]

Include both binary and text files in the search:

`user `[`$`]`rg --binary "pattern"`

### [List Available File Types]

Display a list of all file types recognized by ripgrep:

`user `[`$`]`rg --type-list`

### [Output Results in Vim-Compatible Format]

Format the search results in a manner compatible with Vim:

`user `[`$`]`rg --vimgrep "pattern"`

### [Read Ignore Patterns from a File]

Exclude patterns specified in a particular file:

`user `[`$`]`rg --ignore-file FILE_PATH`

Example: Ignore patterns listed in \".rgignore\"

`user `[`$`]`rg --ignore-file .rgignore "pattern"`

### [][Disable Memory-Mapped I/O]

Turn off memory-mapped I/O during file search:

`user `[`$`]`rg --no-mmap "pattern"`

## [File Listing]

While **ripgrep** is primarily a text-searching tool, it also offers the capability to list files, similar to the [[find]](https://wiki.gentoo.org/wiki/Find "Find") command, though with its unique set of advantages.

** Note**\
Although ripgrep provides file listing functionalities, this tool shouldn\'t be viewed as a direct substitute for the [find] command.

### [Listing Files]

Print the files that ripgrep would search, but don\'t actually search them.

`user `[`$`]`rg --files /path/to/directory`

### [Searching for Specific Filenames]

Combining the file listing feature with another ripgrep command allows for matching specific filenames. For instance, to find all filenames with a certain match:

`user `[`$`]`rg --files /path/to/directory | rg -i <filename_pattern>`

This command first lists all files ripgrep would search in the specified path and then filters them based on the provided filename match.

## [Sorting Results]

**ripgrep** offers the flexibility to sort search results based on different criteria. The sorting modes available are:

** Note**\
Note that sorting results currently always forces ripgrep to abandon parallelism and run in a single thread.

### [Sorting in Ascending Order]

-   Do not sort results. This is the default behavior, offering the fastest performance and the potential for multi-threading.

`user `[`$`]`rg --sort none`

-   Sort results by file path.

`user `[`$`]`rg --sort path`

-   Sort results based on the last modified time of files.

`user `[`$`]`rg --sort modified`

-   Sort results based on the last accessed time of files.

`user `[`$`]`rg --sort accessed`

-   Sort results based on the file creation time.

`user `[`$`]`rg --sort created`

### [Sorting in Descending Order]

-   Do not sort results (same as the default behavior). Offers the fastest performance with potential multi-threading.

`user `[`$`]`rg --sortr none`

-   Sort results in reverse order by file path.

`user `[`$`]`rg --sortr path`

-   Sort results in reverse order based on the last modified time of files.

`user `[`$`]`rg --sortr modified`

-   Sort results in reverse order based on the last accessed time of files.

`user `[`$`]`rg --sortr accessed`

-   Sort results in reverse order based on the file creation time. This mode is single-threaded.

`user `[`$`]`rg --sortr created`

## [Configuration]

**ripgrep** offers customization capabilities through a configuration file named [.ripgreprc]. This file, when placed in a user\'s home directory, enables the setting of default flags that the software reads every time it\'s invoked.

[FILE] **`~/.ripgreprc`**

    # Search hidden files and directories.
    --hidden

    # Follow symbolic links.
    --follow

    # Don't respect ignore files (.gitignore, .ignore, etc.).
    --no-ignore

    # Exclude directories.
    --glob=!

    # Configure color settings and styles.
    --colors=path:bg:0x3b,0x3b,0x3b
    --colors=path:fg:white
    --colors=line:fg:0xf2,0xc2,0x60
    --colors=match:bg:0x2b,0x83,0xa6
    --colors=match:fg:0xff,0xff,0xff
    --colors=match:style:nobold

** Note**\
Flags provided at the command line will override those set in the [.ripgreprc] file.

## [Integration with Other Tools]

**ripgrep** integrates seamlessly with various tools to enhance workflow:

-   **Vim**: Integration of ripgrep with [Vim](https://wiki.gentoo.org/wiki/Vim "Vim") allows for searching patterns across projects. Plugins such as [vim-ripgrep](https://github.com/jremmen/vim-ripgrep) and [fzf.vim](https://github.com/junegunn/fzf.vim) provide this capability.

<!-- -->

-   **Less**: Combining ripgrep\'s output with [[[sys-apps/less]](https://packages.gentoo.org/packages/sys-apps/less)[]] offers paginated viewing.

`user `[`$`]`rg 'pattern' | less`

## [Removal]

### [Unmerge]

Remove [[[sys-apps/ripgrep]](https://packages.gentoo.org/packages/sys-apps/ripgrep)[]]:

`root `[`#`]`emerge --ask --depclean --verbose sys-apps/ripgrep`

## [Debug]

Shows ripgrep\'s debug output. This is useful for understanding why a particular file might be ignored from search, or what kinds of configuration ripgrep is loading from the environment.

`user `[`$`]`rg --debug "pattern"`

## [See also]

-   [grep](https://wiki.gentoo.org/wiki/Grep "Grep") --- a tool for searching text files with regular expressions