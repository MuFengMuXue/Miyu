** Tip**\
wgetpaste can be very useful for providing information to people helping with troubleshooting - for posting to [IRC](https://wiki.gentoo.org/wiki/IRC "IRC") or to the [forums](https://forums.gentoo.org/), for example. It is often requested to be used when asking for [support from the Gentoo community](https://wiki.gentoo.org/wiki/Support "Support").

**Resources**

[[]][Home](https://wgetpaste.zlin.dk/)

[[]][Package information](https://packages.gentoo.org/packages/app-text/wgetpaste)

[[]][GitHub](https://github.com/zlin/wgetpaste)

[[]][Bugs (upstream)](https://github.com/zlin/wgetpaste/issues)

**wgetpaste** is a [command-line](https://wiki.gentoo.org/wiki/Shell "Shell") tool for posting snippets of text to various online [pastebin](https://en.wikipedia.org/wiki/pastebin "wikipedia:pastebin") services.

wgetpaste allows posting text directly to a pastebin from the command line or from a script, returning a link to allow the post to be shared.

See the [service selection](https://wiki.gentoo.org/wiki/Wgetpaste#Service_selection "Wgetpaste") section for a list of available pastebin services. Visit a service\'s website for usage-information specific to that service.

The default service, [bpaste](//bpa.st), is well suited for posting to Gentoo IRC or requesting support. Services that require *javascript* to view the posts can be impractical.

wgetpaste is written in [bash](https://wiki.gentoo.org/wiki/Bash "Bash") and only requires [sed](https://wiki.gentoo.org/wiki/Sed "Sed") and [wget](https://wiki.gentoo.org/wiki/Wget "Wget"), so it is very [portable](https://en.wikipedia.org/wiki/Software_portability "wikipedia:Software portability").

** Important**\
Remember that paste services are often public, **avoid posting sensitive information**. It may not be possible to delete posted information.

** See also**\
See the [support](https://wiki.gentoo.org/wiki/Support "Support") article about how to ask for help with Gentoo.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Example configurations]](#Example_configurations)
    -   [[2.3] [Github gists]](#Github_gists)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
    -   [[3.2] [Service selection]](#Service_selection)
    -   [[3.3] [Posting a file]](#Posting_a_file)
        -   [[3.3.1] [Binary files]](#Binary_files)
    -   [[3.4] [Post command output]](#Post_command_output)
    -   [[3.5] [Advanced options]](#Advanced_options)
    -   [[3.6] [Removing ANSI sequences with ansifilter]](#Removing_ANSI_sequences_with_ansifilter)
    -   [[3.7] [Interacting with the clipboard]](#Interacting_with_the_clipboard)
-   [[4] [External resources]](#External_resources)
-   [[5] [See also]](#See_also)

## [Installation]

### [USE flags]

[wgetpaste] currently has just one use flag, for using SSL/TLS or not:

### [USE flags for] [app-text/wgetpaste](https://packages.gentoo.org/packages/app-text/wgetpaste) [[]] [Command-line interface to various pastebins]

  ----------------------------------------------------- --------------------------------------------------------------------------------------
  [`+ssl`](https://packages.gentoo.org/useflags/+ssl)   Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  ----------------------------------------------------- --------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[app-text/wgetpaste]](https://packages.gentoo.org/packages/app-text/wgetpaste)[]]:

`root `[`#`]`emerge --ask app-text/wgetpaste`

## [Configuration]

### [Files]

-   [/etc/wgetpaste.conf] - Global (system wide) configuration file.
-   [/etc/wgetpaste.d/] - Global configuration directory, for [\*.conf] files.
-   [\~/.wgetpaste.conf] - Local (per user) configuration file.
-   [\~/.wgetpaste.d/] - Local configuration directory, for [\*.conf] files.

### [Example configurations]

[FILE] **`~/.wgetpaste.d/main.conf`**

    # Always pass pastes through app-text/ansifilter
    NOANSI=1

    # Give raw links which can immediately be used for patches, etc
    RAW=1

    # Optionally default to gists
    #DEFAULT_SERVICE=gists
    # Default gists to secret
    PUBLIC_gists='false'
    # Provide github gist authorization token
    HEADER_gists="Authorization: token XXXX"

There is also an [example configuration file](//wgetpaste.zlin.dk/wgetpaste.example) available from upstream, and an [advanced configuration example](https://wgetpaste.zlin.dk/zlin.conf) showing how to add a new service.

### [Github gists]

** Warning**\
`PUBLIC_gists` **must** be explicitly set to `true` or `false` only or it *will* report an error!

The gists service requires a valid API token. Generate it on the [Github website](https://github.com/settings/tokens) and paste it into a config snippet:

[FILE] **`~/.wgetpaste.d/gists.conf`**

    HEADER_gists="Authorization: token abcdef..."

A gist **must** be set to public or private by setting the `PUBLIC_gists` variable either in the config file, or on the command-line, thus (for Bash):

`user `[`$`]`PUBLIC_gists=false wgetpaste -s gists `

## [Usage]

### [Invocation]

Invoke [wgetpaste] with the `--help` option for useful information on usage:

`user `[`$`]`wgetpaste --help`

    Usage: /usr/bin/wgetpaste [options] [file[s]]

    Options:
        -l, --language LANG           set language (defaults to "Plain Text")
        -d, --description DESCRIPTION set description (defaults to "stdin" or filename)
        -n, --nick NICK               set nick (defaults to your username)
        -s, --service SERVICE         set service to use (defaults to "dpaste")
        -e, --expiration EXPIRATION   set when it should expire (defaults to "1")

        -S, --list-services           list supported pastebin services
        -L, --list-languages          list languages supported by the specified service
        -E, --list-expiration         list expiration setting supported by the specified service

        -u, --tinyurl URL             convert input url to tinyurl

        -c, --command COMMAND         paste COMMAND and the output of COMMAND
        -i, --info                    append the output of `emerge --info`
        -I, --info-only               paste the output of `emerge --info` only
        -x, --xcut                    read input from clipboard (requires x11-misc/xclip)
        -X, --xpaste                  write resulting url to the X primary selection buffer (requires x11-misc/xclip)
        -C, --xclippaste              write resulting url to the X clipboard selection buffer (requires x11-misc/xclip)

        -r, --raw                     show url for the raw paste (no syntax highlighting or html)
        -t, --tee                     use tee to show what is being pasted
        -v, --verbose                 show wget stderr output if no url is received
            --completions             emit output suitable for shell completions (only affects --list-*)
            --debug                   be *very* verbose (implies -v)

        -h, --help                    show this help
        -g, --ignore-configs          ignore ""/etc/wgetpaste.conf, ~/.wgetpaste.conf etc.
            --version                 show version information

    Defaults (DEFAULT_[_$] and DEFAULT_SERVICE)
    can be overridden globally in ""/etc/wgetpaste.conf or ""/etc/wgetpaste.d/*.conf or
    per user in any of ~/.wgetpaste.conf or ~/.wgetpaste.d/*.conf.

    An additional http header can be passed by setting HEADER_$ in any of the
    configuration files mentioned above. For example, authenticating with github gist:
    HEADER_gists="Authorization: token 1234abc56789...", or with gitlab snippets:
    HEADER_snippets="PRIVATE-TOKEN: 1234abc56789..."

    You can also set PUBLIC_gists='false' if you want to default to secret instead of
    public github gists. In the case of gitlab, you can set VISIBILITY_snippets= to
    'public', 'private' or 'internal'"

    To change your gitlab server, you can override the default API URL setting
    URL_snippets='https://gitlab.[server].com/api/v4/snippets'

### [Service selection]

Before posting a snippet, care should be taken to select the desired service to post to.

To show which is the current default service, and list available services, use the `--list-services` (`-S` for short) option:

`user `[`$`]`wgetpaste --list-services`

    Services supported: (case sensitive):
       Name:     | Url:
       ==========|=================
        0x0      | http://0x0.st
        bpaste   | https://bpa.st/api/v1/paste
        codepad  | http://codepad.org/
        dpaste   | http://dpaste.com/api/v2/
        gists    | https://api.github.com/gists
        ix_io    | http://ix.io
        snippets | https://gitlab.com/api/v4/snippets
       *pgz      | https://paste.gentoo.zip

The default service is marked with an asterisk, this service will be used unless a different service is selected with the `--service` (`-s` for short) option, when pasting. For example:

`user `[`$`]`wgetpaste --service codepad file.txt`

Different paste services have different constraints, such as allowable size, retention period etc. Go to the service website for full information. For larger posts, 0x0 may be useful.

** Note**\
It may be preferable to **simply set a sensible default service** before use, or just leave it as \"dpaste\" - see the [configuration](https://wiki.gentoo.org/wiki/Wgetpaste#Configuration "Wgetpaste") section.

### [Posting a file]

To post a file, simply run [wgetpaste] followed by the filename, not forgetting to specify a paste service if somthing other than the default is required.

For example, run the following command to create a paste of the system\'s Xorg configuration:

`user `[`$`]`wgetpaste /etc/X11/xorg.conf`

To create a paste of [xorg.conf] using the tiny URL service use the `--tinyurl` option (`-u` for short):

`user `[`$`]`wgetpaste --tinyurl /etc/X11/xorg.conf`

#### [Binary files]

Most paste services cannot handle binary files, e.g. gzip archives. However, there is a simple core utility to help with that [base64].

If a binary file needs to be posted, run this command first to prepare the file and post the result instead:

`user `[`$`]`base64 hugefile.log.gz > hugefile.log.gz.base64`

After someone receives the paste, the file can be decoded like:

`user `[`$`]`base64 -d hugefile.log.gz.base64 > hugefile.log.gz`

This encoding will inflate the original size so files on the brink of maximum size may be rejected.

### [Post command output]

A command\'s output may be directly posted to a snippet service, though it is recommended to write output to a file and check the contents before pasting, to avoid any possible security issues.

To paste the entire output of a command, use the `--command` (`-c` for short) option. Remember to quote the command:

`user `[`$`]`wgetpaste --command 'emerge -vp musique'`

Output can also be piped to [wgetpaste], but this will only include [stdout] by default. Use `|&` to include [stderr] as well:

`user `[`$`]` |& wgetpaste`

** Tip**\
If you seek help in the Gentoo IRC channel, it is a good habit to use the `-i` parameter(it will append the output of `emerge --info`). For example, `wgetpaste -ic "emerge -pvuDU @world"`.

### [Advanced options]

To set a language for syntax highlighting use the `--language` (`-l` for short) option:

`user `[`$`]`wgetpaste --language Bash /etc/bash/bashrc`

Use the `--list-languages` (`-L` for short) option to list all available languages, these depend on the selected paste service:

`user `[`$`]`wgetpaste --list-languages`

** Note**\
See the [invocation](https://wiki.gentoo.org/wiki/Wgetpaste#Invocation "Wgetpaste") section for other advanced options, such as automatically adding system diagnostic information, or pasting to or from clipboards.

### [Removing ANSI sequences with ansifilter]

** Tip**\
wgetpaste 2.33 and newer supports `--no-ansi` (`-N`) to automatically filter via [ansifilter]. It also supports `NOANSI=1` in [.wgetpaste.conf].

For getting color on terminals, ANSI sequences are used. When uploading a logfile these can be annoying (in particular it makes it hard to search for error messages), e.g.:

    �[32m * �[39;49;00mPackage:    x11-wm/dwm-6.2
    �[32m * �[39;49;00mRepository: gentoo
    �[32m * �[39;49;00mMaintainer: gyakovlev@gentoo.org
    �[32m * �[39;49;00mUSE:        abi_x86_64 amd64 elibc_glibc kernel_linux savedconfig userland_GNU xinerama
    �[32m * �[39;49;00mFEATURES:   network-sandbox preserve-libs sandbox userpriv usersandbox

[[[app-text/ansifilter]](https://packages.gentoo.org/packages/app-text/ansifilter)[]] removes these control characters. To install:

`root `[`#`]`emerge --ask app-text/ansifilter`

Filter the build.log and upload with wgetpaste:

`user `[`$`]`ansifilter /var/tmp/portage/cat/package-1.23/temp/build.log | wgetpaste`

You can also use ansifilter in the middle of pipes. For example:

`user `[`$`]`ls --color / | ansifilter | wgetpaste`

** Note**\
Note the use of `--color`. Many software disables ansi output by default when outputting to a pipe --- this is just an example to show ansifilter being used in this manner.

### [Interacting with the clipboard]

wgetpaste can read from the system clipboard as content input or write the resulting url to the system clipboard. You need to install [[[x11-misc/xclip]](https://packages.gentoo.org/packages/x11-misc/xclip)[]] as an optional dependency.

`root `[`#`]`emerge --ask x11-misc/xclip`

Read input from clipboard:

`user `[`$`]`wgetpaste --xcut`

    Your paste can be seen here: https://paste.gentoo.zip/85vuQg0X

Write resulting url to the X clipboard selection buffer:

`user `[`$`]`wgetpaste -c "emerge --info" --xclippaste`

    Your paste can be seen here: https://paste.gentoo.zip/4HnpeZvu

You can also use `--xpaste` to write resulting url to the X primary selection buffer.

** Tip**\
wgetpaste also supports `SOURCE=xcut`, `XPASTE=1` and `XCLIPPASTE=1` in [.wgetpaste.conf].

## [External resources]

-   [[[app-text/pastebinit]](https://packages.gentoo.org/packages/app-text/pastebinit)[]] - Another similar tool available through Portage.
-   [Pastebin](https://en.wikipedia.org/wiki/Pastebin "wikipedia:Pastebin") - Wikipedia article about pastebin services.

## [See also]

-   [Support](https://wiki.gentoo.org/wiki/Support "Support") --- provide **support** for technical issues encountered when installing or using Gentoo Linux
-   [Troubleshooting](https://wiki.gentoo.org/wiki/Troubleshooting "Troubleshooting") --- provide users with a set of techniques and tools to troubleshoot and fix problems with their Gentoo setups.