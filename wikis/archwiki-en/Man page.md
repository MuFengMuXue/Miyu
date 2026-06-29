# Man page

man pages—abbreviation for "manual pages"—are the form of documentation that is available on almost all UNIX-like operating systems, including Arch Linux. The command used to display them is .

In spite of their scope, manual pages are designed to be self-contained documents, consequently limiting themselves to referring to other manual pages when discussing related subjects. This is in sharp contrast with the hyperlink-aware Info documents—GNU attempt at replacing the traditional manual page format.

## Installation
 implements man on Arch Linux, and less is the default pager used with man.  can also be used.

 provides both the Linux and the POSIX.1 man pages Some localized man pages are also available:

*  for Czech
*  for Danish
*  for German
*  for Greek
*  for Spanish
*  for Finnish
*  for French
*  for Hungarian
*  for Indonesian
*  for Italian
*  for Japanese
*  for Macedonian
*  for Dutch
*  for Polish
*  for Brazilian Portuguese
*  for Romanian
*  for Russian
*  for Serbian
*  for Swedish
*  for Turkish
*  for Ukrainian
*  for Vietnamese
*  for Simplified Chinese
*  for Traditional Chinese

You can also search for all of the available localized man pages [https://archlinux.org/packages/?sort=&q=man-pages- on the official repositories and on the AUR.

## Accessing man pages
To read a man page, simply enter:

 $ man page_name

Manuals are sorted into several sections. Each section has an intro, such as ,  and so on. For a full listing see .

Man pages are usually referred to by their name, followed by their section number in parentheses. Often there are multiple man pages of the same name, such as  and . In this case, give man the section number followed by the name of the man page, for example:

 $ man 5 passwd

to read the man page on , rather than the  utility.

Or equivalently, the man page followed by the section number, separated by a period:

 $ man passwd.5

## Searching manuals
Man pages can be searched when the exact name of a page is not known using any of the following equivalent commands:

 $ man -k expression
 $ man --apropos expression
 $ apropos expression

 is interpreted as a regular expression by default.

To search for keywords in whole page texts, use the  option instead.

One-line descriptions of man pages can be displayed using the  command. For example, for a brief description of the man page sections about , type:

## Page width
The man page width is controlled by the  environment variable.

If the number of columns in the terminal is too small (e.g. the window width is narrow), the line breaks will be wrong. This can be very disturbing for reading. You can fix this by setting the  on  invocation. With Bash, that would be:

{{hc|~/.bashrc|
man() {
    local width=$(tput cols)
    [ $width -gt $MANWIDTH ] && width=$MANWIDTH
    env MANWIDTH=$width \
    man "$@"
}
}}

## Reading local man pages
You can use some applications to view man pages:

*
*
*
*
*
*

Using browsers such as  and Firefox to view man pages allows users to reap info pages' main benefit of hyperlinked text. Alternatives include the following:

## Conversion to HTML
## mandoc
Install the  package. To convert a page, for example :

 $ mandoc -Thtml -Ostyle=style.css /usr/share/man/man1/free.1.gz > free.html

Now open the file called  in your favourite browser.

## man2html
First, install  from the official repositories.

Now, convert a man page:

 $ man free | man2html -compress -cgiurl man$section/$title.$section$subsection.html > ~/man/free.html

Another use for  is exporting to raw, printer-friendly text:

 $ man free | man2html -bare > ~/free.txt

## man -H
The  implementation also has the ability to do this on its own:

 $ man -H free

This will read your  environment variable to determine the browser. You can override this by passing the binary to the  option.

## roffit
First install .

To convert a man page:

 $ gunzip -c /usr/share/man/man1/free.1.gz | roffit > free.html

## Conversion to PDF
man pages have always been printable: they are written in , which is fundamentally a typesetting language. Therefore, you can easily convert man pages to any of the formats supported as output devices by groff, which is used by . For a list of output devices, see the  option in  (or  if you use the  package).

This will produce a PDF file:

 $ man -Tpdf manpage > filename

Caveats: Fonts are generally limited to Times at hardcoded sizes. Some man pages were specifically designed for terminal viewing, and will not look right in PS or PDF form.

## Qman
For an alternative interface for reading manual pages, one that supports modern features such as hyperlinks and history, install . You can now use  in the place of :

 $ qman ls    # Display the manual page for ls
 $ qman -k ls # Perform apropos on 'ls'

For more information and troubleshooting, see the project's GitHub page.

## Online man pages
* Arch Linux manual pages – Contains man pages from Arch Linux packages. Used for man page links from the wiki. You can also use the  bang with search engines like DuckDuckGo or Brave to search through the Arch manual pages directly.
* man7.org – The Linux man-pages project. Upstream of the  package. The online pages currently show an outdated version of man-pages (5.13, released in 2021).
* manned.org – Collection from various Linux distributions, BSD, etc., with multiple package versions.
* linux.die.net
* man.cx – Man pages extracted from Debian testing.
* Debian man pages
* Ubuntu man pages
* DragonFlyBSD man pages
* FreeBSD man pages
* NetBSD man pages
* OpenBSD man pages
* Plan 9 Manual – Volume 1
* Inferno Manual – Volume 1
* The UNIX and Linux forums man page repository

Note that while  provides man pages for POSIX.1-2017 (see an official online reference also exists:

* [https://pubs.opengroup.org/onlinepubs/9799919799/ POSIX.1-2024
* POSIX.1-2017

There is also a comparison table of the online databases.

## Noteworthy man pages
Here follows a non-exhaustive list of noteworthy pages that might help you understand a lot of things more in-depth. Some of them might serve as a good reference (like the ASCII table).

*
*
*
*
*
*
*
*
* , ,
*
*
*
*
* ,
*
*
*

More generally, have a look at category 7 (miscellaneous) pages:

 $ man -s 7 -k ".*"

Arch Linux specific pages:

*
*
*
*
*
*
*
*
*
*
