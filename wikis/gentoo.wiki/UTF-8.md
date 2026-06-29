Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/UTF-8/es "UTF-8 (76% translated)")
-   [français](https://wiki.gentoo.org/wiki/UTF-8/fr "UTF-8 (79% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/UTF-8/it "UTF-8 (1% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/UTF-8/hu "UTF-8 (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/UTF-8/ru "UTF-8 (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/UTF-8/zh-cn "UTF-8 (17% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/UTF-8/ja "UTF-8 (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/UTF-8/ko "UTF-8 (69% translated)")

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/UTF-8 "wikipedia:UTF-8")

**UTF-8** is a variable-length character encoding, which in this instance means that it uses 1 to 4 bytes per symbol. So, the first UTF-8 byte is used for encoding ASCII, giving the character set full backwards compatibility with ASCII. UTF-8 means that ASCII and Latin characters are interchangeable with little increase in the size of the data, because only the first byte is used. Users of Eastern alphabets such as Japanese, who have been assigned a higher byte range are unhappy, as this results in as much as a 50% redundancy in their data.

## Contents

-   [[1] [Character encodings]](#Character_encodings)
    -   [[1.1] [What is a character encoding?]](#What_is_a_character_encoding.3F)
    -   [[1.2] [The history of character encodings]](#The_history_of_character_encodings)
    -   [[1.3] [What is Unicode?]](#What_is_Unicode.3F)
    -   [[1.4] [What UTF-8 can do]](#What_UTF-8_can_do)
-   [[2] [Setting up UTF-8 in Gentoo]](#Setting_up_UTF-8_in_Gentoo)
    -   [[2.1] [Finding or creating UTF-8 locales]](#Finding_or_creating_UTF-8_locales)
    -   [[2.2] [Setting the locale]](#Setting_the_locale)
    -   [[2.3] [Alternative: Using eselect to set locales]](#Alternative:_Using_eselect_to_set_locales)
-   [[3] [Application support]](#Application_support)
    -   [[3.1] [(V)FAT]](#.28V.29FAT)
    -   [[3.2] [Filenames]](#Filenames)
    -   [[3.3] [The system console]](#The_system_console)
    -   [[3.4] [Ncurses and Slang]](#Ncurses_and_Slang)
    -   [[3.5] [KDE, GNOME, and Xfce]](#KDE.2C_GNOME.2C_and_Xfce)
    -   [[3.6] [X11 and fonts]](#X11_and_fonts)
    -   [[3.7] [Window managers and terminal emulators]](#Window_managers_and_terminal_emulators)
    -   [[3.8] [Vim, emacs, xemacs, and nano]](#Vim.2C_emacs.2C_xemacs.2C_and_nano)
    -   [[3.9] [Shells]](#Shells)
    -   [[3.10] [Irssi]](#Irssi)
    -   [[3.11] [Mutt]](#Mutt)
    -   [[3.12] [links and elinks]](#links_and_elinks)
    -   [[3.13] [Samba]](#Samba)
    -   [[3.14] [Testing it all out]](#Testing_it_all_out)
-   [[4] [Reported issues and problems]](#Reported_issues_and_problems)
    -   [[4.1] [System configuration files (in /etc)]](#System_configuration_files_.28in_.2Fetc.29)
-   [[5] [External resources]](#External_resources)

## [Character encodings]

### [][What is a character encoding?]

Computers themselves do not understand printed text as a human would. For computers, every character of text is represented by a number. Traditionally, each set of numbers used to represent alphabets and characters (known as a coding system, encoding, or character set) was limited in size due to limitations in computer hardware.

### [The history of character encodings]

The most common (or at least the most widely accepted) character set is **ASCII** (American Standard Code for Information Interchange). It is widely held that ASCII is the most successful software standard ever created. Modern ASCII was standardized in 1986 (ANSI X3.4, RFC 20, ISO/IEC 646:1991, ECMA-6) by the American National Standards Institute.

ASCII is strictly seven-bit, meaning that it uses bit patterns representable with seven binary digits, which provides a range of 0 to 127 in decimal. These include 33 non-visible control characters, most between 0 and 31, with the final control character, DEL or delete at 127. Characters 32 to 126 are visible characters: a space, punctuation marks, Latin letters and numbers.

The eighth bit in ASCII was originally used as a parity bit for error checking. If error checking is not desired, it is left as 0. This means that, with ASCII, each character is represented by a single byte.

Although ASCII was enough for communication in modern English, in other European languages that include accented characters, things were not so easy. The ISO 8859 standards were developed to meet these needs. They were backwards compatible with ASCII, but instead of leaving the eighth bit blank, they used it to allow another 128 characters (32 controls plus 96 visible characters) in each encoding. ISO 8859\'s limitations soon came to light, and there are currently 15 variants of the ISO 8859 standard (8859-1 through to 8859-15). Outside of the ASCII-compatible byte range of these character sets, there is often conflict between the letters represented by each byte. To complicate interoperability between character encodings further, Windows-1252 is used in some versions of Microsoft Windows instead for Western European languages. Its visible characters are a super-set of ISO 8859-1, however it is different in several ways; these sets do all retain ASCII compatibility.

The necessary development of completely different single-byte encodings for non-Latin alphabets, such as EUC (Extended Unix Coding) which is used for Japanese and Korean (and to a lesser extent Chinese) created more confusion. Other operating systems still used different character sets for the same languages, for example, Shift-JIS and ISO-2022-JP. Users wishing to view Cyrillic glyphs had to choose between KOI8-R for Russian and Bulgarian or KOI8-U for Ukrainian, as well as all the other Cyrillic encodings such as the unsuccessful ISO 8859-5, and the common Windows-1251 set. All of these character sets broke most compatibility with ASCII. Although it should be mentioned KOI8 encodings place Cyrillic characters in Latin order, so in case the eighth bit is stripped, text is still decipherable on an ASCII terminal through case-reversed transliteration.

All of this has led to mass confusion, and to an almost total inability for multilingual communication; especially across different alphabets. Enter Unicode.

### [][What is Unicode?]

Unicode throws away the traditional single-byte limit of character sets. It uses 17 \"[planes](https://en.wikipedia.org/wiki/Plane_(Unicode) "wikipedia:Plane (Unicode)")\" of 65,536 code points to describe a maximum of 1,114,112 characters. As the first plane, aka. \"Basic Multilingual Plane\" or BMP, contains almost every character a user will ever need. Many have made the wrong assumption that Unicode was a 16-bit character set.

Unicode has been mapped in many different ways, but the two most common are **UTF** (Unicode Transformation Format) and **UCS** (Universal Character Set). A number after UTF indicates the number of bits in one unit, while the number after UCS indicates the number of bytes. UTF-8 has become the most widespread means for the interchange of Unicode text as a result of its eight-bit clean nature; it is therefore the subject of this document.

### [What UTF-8 can do]

UTF-8 allows users to work in a standards-compliant and internationally accepted multilingual environment, with a comparatively low data redundancy. It is the preferred way for transmitting non-ASCII characters over the Internet, through Email, IRC, or almost any other medium. Despite this, many people regard UTF-8 in online communication as abusive. It is always best to be aware of the attitude towards UTF-8 in a specific channel, mailing list, or Usenet group before using *non-ASCII* UTF-8.

## [Setting up UTF-8 in Gentoo]

### [Finding or creating UTF-8 locales]

Now that the principles behind Unicode have been laid out, get ready to start using UTF-8 locally!

For users interested in more knowledge further explanation can be found in the [Gentoo Localization Guide](https://wiki.gentoo.org/wiki/Localization/Guide "Localization/Guide").

Next, the user needs to decide whether a UTF-8 locale is available for the language of choice, or whether one needs to be generated.

`user `[`$`]`locale -a | grep 'en_GB'`

    en_GB
    en_GB.utf8

From the output of the above command, look for a result with a suffix similar to `.UTF-8`. If there is no result with a similar suffix a UTF-8 compatible locale must be created.

The command lists the suffix in lower case without any hyphens, glibc understands both forms of the suffix, many other programs don\'t. The most common example of which is [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg"). So it is best to always use UTF-8 in preference to utf8.

** Note**\
Only execute the following code if the system does not have a UTF-8 locale available for the language of choice.

Replace \"en_GB\" with the desired locale setting:

`root `[`#`]`localedef -i en_GB -f UTF-8 en_GB.UTF-8`

Another way to include a UTF-8 locale is to add it to the [/etc/locale.gen] file and generate necessary locales using the [locale-gen] command. Locales will be written to the locale-archive [/usr/lib/locale/locale-archive].

[CODE] **Line in /etc/locale.gen**

    en_GB.UTF-8 UTF-8

`root `[`#`]`locale-gen`

     * Generating 1 locales (this might take a while) with 1 jobs
     *  (1/1) Generating en_GB.UTF-8 ...                            [ ok ]
     * Generation complete

### [[] Setting the locale]

There is one environment variable that needs to be set in order to use the new UTF-8 locales: `LC_CTYPE` (optionally modify the `LANG` variable to change the system language as well). There are also many different ways to set it; some system administrators prefer to only have a UTF-8 environment for a specific user, in which case they set them in their [\~/.profile] ([/bin/sh] for Bourne shell users), [\~/.bash_profile] or [\~/.bashrc] ([/bin/bash] for Bourne again shell users). More details and best practices can be found in the [Localization Guide](https://wiki.gentoo.org/wiki/Localization/Guide "Localization/Guide").

Still others prefer to set the locale globally. One specific circumstance where the author particularly recommends doing this is when [/etc/init.d/xdm] is in use, because this init script starts the display manager and desktop before any of the aforementioned shell startup files are sourced. In other words, this is performed before any of the variables are loaded in the environment.

Setting the locale globally should be done using [/etc/env.d/02locale] file. This file should look something like the following:

[FILE] **`/etc/env.d/02locale`Demonstration of en_GB.UTF-8**

    ## (As always, change "en_GB.UTF-8" to the appropriate locale value; each language has a different value!)
    LANG="en_GB.UTF-8"

** Note**\
It is possible to substitute the `LC_CTYPE` variable for the `LANG` variable. For more information on the categories affected by using `LC_CTYPE` read the [GNU locale page](http://www.gnu.org/software/libc/manual/html_node/Locale-Categories.html#Locale-Categories).

Next, the environment must be updated by running the following command:

`root `[`#`]`env-update`

    >>> Regenerating /etc/ld.so.cache...

`root `[`#`]`source /etc/profile`

Now, run [locale] with no arguments to see if the correct variables have been loaded in the environment:

`root `[`#`]`locale`

    LANG=en_GB.utf8
    LC_CTYPE="en_GB.utf8"
    LC_NUMERIC="en_GB.utf8"
    LC_TIME="en_GB.utf8"
    LC_COLLATE="en_GB.utf8"
    LC_MONETARY="en_GB.utf8"
    LC_MESSAGES="en_GB.utf8"
    LC_PAPER="en_GB.utf8"
    LC_NAME="en_GB.utf8"
    LC_ADDRESS="en_GB.utf8"
    LC_TELEPHONE="en_GB.utf8"
    LC_MEASUREMENT="en_GB.utf8"
    LC_IDENTIFICATION="en_GB.utf8"
    LC_ALL=

The values of locale environment variables that have been explicitly set e.g. in an export statement (if using bash) are listed without double quotes. Those whose value has been inherited from other locale environment variables have their values in double quotes.

### [Alternative: Using eselect to set locales]

Although it is good to maintain the system as described above, it is possible to verify the correct locale configured using the [[eselect](https://wiki.gentoo.org/wiki/Eselect "Eselect")] utility.

Use [eselect] to list the available locales on the system:

`root `[`#`]`eselect locale list `

      [1] C
      [2] POSIX *
      [3] en_GB.utf8
      [ ] (free form)

Using [eselect] setting the locale is as simple as listing them. Once the correct locale has been determined invoke:

`root `[`#`]`eselect locale set 3 `

    Setting LANG to en_GB.utf8 ...

Check the result:

`root `[`#`]`eselect locale list `

      [1] C
      [2] POSIX
      [3] en_GB.utf8 *
      [ ] (free form)

In case it is preferred to have [/etc/env.d/02locale] with `.UTF-8` instead of `.utf8`, run the appropriate [eselect] command:

`root `[`#`]`eselect locale set en_GB.UTF-8 `

    Setting LANG to en_GB.UTF-8 ...

`root `[`#`]`eselect locale list `

      [1] C
      [2] POSIX
      [3] en_GB.utf8
      [4] en_GB.UTF-8 *
      [ ] (free form)

Running the following command will update the variables in the shell:

`root `[`#`]`env-update && source /etc/profile `

    >>> Regenerating /etc/ld.so.cache...

That is everything. The system is now using UTF-8 locales. The next hurdle is the configuration of the applications used from day to day.

## [Application support]

When Unicode first started gaining momentum in the software world, multibyte character sets were not well suited to languages like C, which is the base language of most commonly used programs. Even today, some programs are not able to handle UTF-8 properly. Fortunately the majority of programs, especially the common ones, are supported.

### [][(V)FAT]

For UTF-8 support in FAT [filesystems](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") see the [FAT](https://wiki.gentoo.org/wiki/FAT "FAT") article.

### [Filenames]

For changing the encoding of filenames, [[[app-text/convmv]](https://packages.gentoo.org/packages/app-text/convmv)[]] can be used.

`root `[`#`]`emerge --ask app-text/convmv`

The format of the [convmv] command is as follows:

`root `[`#`]`convmv -f <current-encoding> -t utf-8 <filename>`

Substitute `iso-8859-1` with the charset being converted from:

`root `[`#`]`convmv -f iso-8859-1 -t utf-8 filename`

For changing the *contents* of files, use the [iconv] utility, it comes bundled with [[[sys-libs/glibc]](https://packages.gentoo.org/packages/sys-libs/glibc)[]] and should be installed on all Gentoo systems. Substitute `iso-8859-1` with the charset being converted from. After running the command be sure to check for sane output:

`root `[`#`]`iconv -f iso-8859-1 -t utf-8 filename`

To convert a file, another file must be created:

`root `[`#`]`iconv -f iso-8859-1 -t utf-8 filename > newfile`

The recode ([[[app-text/recode]](https://packages.gentoo.org/packages/app-text/recode)[]]) package can also be used for this purpose.

### [The system console]

To enable UTF-8 on the console edit [/etc/rc.conf]. Set `unicode="yes"` and read the comments \-- it is important to have a font that has a good range of characters to make the most of Unicode. For this to work make sure the Unicode locale has been properly created.

The `keymap` variable, set in [/etc/conf.d/keymaps], should have a Unicode keymap specified.

[CODE] **Example /etc/conf.d/keymaps snippet**

    ## (Change "uk" to the right local layout)
    keymap="uk"

### [Ncurses and Slang]

** Note**\
Ignore any mention of Slang in this section if it is not installed or unneeded.

It is wise to add [`unicode`](https://packages.gentoo.org/useflags/unicode) to the global [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") in [[/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf#USE "/etc/portage/make.conf")], and then to re-emerge [[[sys-libs/ncurses]](https://packages.gentoo.org/packages/sys-libs/ncurses)[]] and [[[sys-libs/slang]](https://packages.gentoo.org/packages/sys-libs/slang)[]]. Portage will do this automatically if the `--changed-use` or `--newuse` options are used. Run the following command to pull in the packages:

`root `[`#`]`emerge --update --deep --newuse @world`

We also need to rebuild packages that link to these, now the USE changes have been applied. The tool we use ([revdep-rebuild]) is part of the [[[app-portage/gentoolkit]](https://packages.gentoo.org/packages/app-portage/gentoolkit)[]] package.

`root `[`#`]`revdep-rebuild --library libncurses.so.5 `

`root `[`#`]`revdep-rebuild --library libslang.so.1`

### [][KDE, GNOME, and Xfce]

All of the major desktop environments have full Unicode support, and will require no further setup than what has already been covered in this guide. This is because the underlying graphical toolkits (Qt or GTK 2) are UTF-8 aware. Subsequently, all applications running on top of these toolkits should be UTF-8-aware out of the box.

On [GTK](https://wiki.gentoo.org/wiki/GTK "GTK") based applications, the key sequence for hexadecimal Unicode input is [Ctrl]+[Shift]+[u]+`<hex digit>`. As an example, the unicode character ✔ which has unicode number [U+2714](http://unicode-table.com/en/2714/) can be written as [Ctrl]+[Shift]+[u]+`2714`+`ENTER`, being rendered as `✔`. [IBus](https://wiki.gentoo.org/wiki/IBus "IBus") is needed for support in other applications.

### [X11 and fonts]

TrueType fonts have support for Unicode, and most of the fonts that ship with Xorg have extensive character support, although, obviously, not every single glyph available in Unicode has been created for that font.

Also, many font packages in Portage are Unicode aware. See the [Fontconfig](https://wiki.gentoo.org/wiki/Fontconfig "Fontconfig") page for more information on recommended fonts and configuration.

### [Window managers and terminal emulators]

Window managers not built on GTK or Qt generally have very good Unicode support, as they often use the Xft library for handling fonts. If the window manager does not use Xft for fonts, then it is still possible to use the FontSpec mentioned in the previous section as a Unicode font.

Terminal emulators that use Xft and support Unicode are harder to come by. Aside from Konsole and GNOME Terminal, the best options in Portage are [[[x11-terms/rxvt-unicode]](https://packages.gentoo.org/packages/x11-terms/rxvt-unicode)[]], [[[x11-terms/xfce4-terminal]](https://packages.gentoo.org/packages/x11-terms/xfce4-terminal)[]], [[[gnustep-apps/terminal]](https://packages.gentoo.org/packages/gnustep-apps/terminal)[]], [[[x11-terms/mlterm]](https://packages.gentoo.org/packages/x11-terms/mlterm)[]], or plain [[[x11-terms/xterm]](https://packages.gentoo.org/packages/x11-terms/xterm)[]] when built with the `unicode` USE flag and invoked as `uxterm`. [[[app-misc/screen]](https://packages.gentoo.org/packages/app-misc/screen)[]] supports UTF-8 too, when invoked as [screen -U] or the following is put into the [\~/.screenrc]:

[CODE] **\~/.screenrc for UTF-8**

    defutf8 on

### [][Vim, emacs, xemacs, and nano]

[Vim](https://wiki.gentoo.org/wiki/Vim "Vim") provides full UTF-8 support, and also has builtin detection of UTF-8 files. For further information in [Vim](https://wiki.gentoo.org/wiki/Vim#Change_file_encoding "Vim"), use `:help mbyte.txt`.

[GNU Emacs](https://wiki.gentoo.org/wiki/GNU_Emacs "GNU Emacs") since version 23 and XEmacs version 21.5 have full UTF-8 support. GNU Emacs 24 also supports editing bidirectional text.

Nano has provided full UTF-8 support since version 1.3.6.

### [Shells]

Currently, [Bash](https://wiki.gentoo.org/wiki/Bash "Bash") provides full Unicode support through the GNU readline library. [Z Shell](https://wiki.gentoo.org/wiki/Zsh "Zsh") offers Unicode support with the `unicode` USE flag.

The C shell, [tcsh] and [ksh] do not provide UTF-8 support at all.

### [Irssi]

Irssi has complete UTF-8 support, although it does require a user to set an option.

`[irssi]``set term_charset UTF-8`

For channels where non-ASCII characters are often exchanged in non-UTF-8 charsets, the [/recode] command may be used to convert the characters. Type [/help recode] for more information.

### [Mutt]

The Mutt mail user agent has very good Unicode support. To use UTF-8 with Mutt, nothing needs to be put in the configuration files. Mutt will work under Unicode environment without modification if all the configuration files (signature included) are UTF-8 encoded.

** Note**\
It is still possible to see \'?\' in mails read with Mutt. This is a result of people using a mail client which does not indicate the used charset. There is little one can do about this than to ask them to configure their client correctly.

Further information is available from the [Mutt Wiki](https://dev.mutt.org/trac/wiki/MuttFaq/Charset).

### [links and elinks]

These are commonly used text-based browsers, and we shall see how we can enable UTF-8 support on them. On [elinks] and [links], there are two ways to go about this, one using the Setup option from within the browser or editing the config file. To set the option through the browser, open a site with [elinks] or [links] and then [Alt]+[S] to enter the Setup Menu then select Terminal options, or press [T]. Scroll down and select the last option `UTF-8 I/O` by pressing [Enter]. Then Save and exit the menu. On [links] one may have to do a repeat [Alt]+[S] and then press [S] to save. The config file option, is shown below.

[CODE] **Enabling UTF-8 for elinks/links**

    ## (For elinks, edit /etc/elinks/elinks.conf or ~/.elinks/elinks.conf and add the following line)
    set terminal.linux.utf_8_io = 1
    ## (For links, edit ~/.links/links.cfg and add the following line)
    terminal "xterm" 0 1 0 us-ascii utf-8

### [Samba]

[Samba](https://wiki.gentoo.org/wiki/Samba "Samba") is a software suite which implements the SMB (Server Message Block) protocol for UNIX systems such as Macs, Linux and FreeBSD. The protocol is also sometimes referred to as the Common Internet File System (CIFS). Samba also includes the NetBIOS system - used for file sharing over windows networks.

Add the following lines under the `[global]` section:

`root `[`#`]`nano -w /etc/samba/smb.conf`

    dos charset = 1255
    unix charset = UTF-8
    display charset = UTF-8

### [Testing it all out]

There are numerous UTF-8 test websites around and most of the popular [browsers in Gentoo](https://packages.gentoo.org/categories/www-client) have full UTF-8 support.

When using one of the text-only web browsers, make absolutely sure a Unicode-aware terminal is used.

If certain characters are displayed as boxes with letters or numbers inside, then the current [font](https://wiki.gentoo.org/wiki/Fonts "Fonts") does not have glyphs for those characters. Instead, it displays a box with the hex code of the UTF-8 symbol.

-   [unicode-table.com](https://unicode-table.com/en/)
-   [A W3C UTF-8 Test Page](https://www.w3.org/2001/06/utf-8-test/UTF-8-demo.html)
-   [A UTF-8 test page provided by the University of Frankfurt](http://titus.uni-frankfurt.de/indexe.htm?/unicode/unitest.htm)

## [Reported issues and problems]

### [][System configuration files (in /etc)]

Most system configuration files (such as [/etc/fstab]) do not support UTF-8. It is recommended to stick with the ASCII character set for these files.

## [External resources]

-   [The Wikipedia entry for Unicode](https://en.wikipedia.org/wiki/Unicode)
-   [The Wikipedia entry for UTF-8](https://en.wikipedia.org/wiki/UTF-8)
-   [Unicode.org](http://www.unicode.org)
-   [UTF-8.com](http://www.utf-8.com)
-   [RFC 3629](https://www.ietf.org/rfc/rfc3629.txt)
-   [RFC 2277](https://www.ietf.org/rfc/rfc2277.txt)
-   [Characters vs. Bytes](https://www.tbray.org/ongoing/When/200x/2003/04/26/UTF)
-   [The GNU C Library: Locales and Internationalization](https://www.gnu.org/software/libc/manual/html_node/Locales.html)
-   [Unifoundry.com - Unicode Tutorial](http://unifoundry.com/unicode-tutorial)
-   [unicode USE flag description](https://packages.gentoo.org/useflags/unicode)

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Thomas Martin, Alexander Simonov, Shyam Mani, **\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*