**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Base "Project:Base")][Project](https://wiki.gentoo.org/wiki/Project:Base "Project:Base")

[[]][Home](https://www.gnu.org/software/coreutils/)

[[]][Official documentation](https://www.gnu.org/software/coreutils/manual/coreutils.html)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/coreutils)

[[]][Wikipedia](https://en.wikipedia.org/wiki/GNU_Coreutils "wikipedia:GNU Coreutils")

[[]][GitWeb](https://git.sv.gnu.org/cgit/coreutils.git)

[[]][GitHub (mirror)](https://github.com/coreutils/coreutils)

[[]][Bugs (upstream)](mailto:bug-coreutils@gnu.org)

The **coreutils** package contains the GNU coreutils, the basic file, shell and text manipulation utilities of the GNU operating system; a superset of the utilities specified by the [POSIX \"Shell and Utilities\" volume](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/contents.html).

These commands are provided for quick reference only, with some Gentoo specific notes. For up to date and in depth documentation, see the local `--help` options and [man pages](https://wiki.gentoo.org/wiki/Man_page "Man page") for each command.

These commands are powerful, but beware that this means that data loss may be incurred in case of misuse. Always [backup](https://wiki.gentoo.org/wiki/Backup "Backup") important data. Pay particular attention when working with [escalated privileges](https://wiki.gentoo.org/wiki/Sudo "Sudo").

Gentoo includes the [[[sys-apps/coreutils]](https://packages.gentoo.org/packages/sys-apps/coreutils)[]] package in the [system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [arch]](#arch)
    -   [[2.2] [b2sum]](#b2sum)
    -   [[2.3] [base32]](#base32)
    -   [[2.4] [base64]](#base64)
    -   [[2.5] [basename]](#basename)
    -   [[2.6] [basenc]](#basenc)
    -   [[2.7] [cat]](#cat)
    -   [[2.8] [chcon]](#chcon)
    -   [[2.9] [chgrp]](#chgrp)
    -   [[2.10] [chmod]](#chmod)
    -   [[2.11] [chown]](#chown)
    -   [[2.12] [chroot]](#chroot)
    -   [[2.13] [cksum]](#cksum)
    -   [[2.14] [comm]](#comm)
    -   [[2.15] [cp]](#cp)
    -   [[2.16] [csplit]](#csplit)
    -   [[2.17] [cut]](#cut)
    -   [[2.18] [date]](#date)
    -   [[2.19] [dd]](#dd)
    -   [[2.20] [df]](#df)
    -   [[2.21] [dir]](#dir)
    -   [[2.22] [dircolors]](#dircolors)
    -   [[2.23] [dirname]](#dirname)
    -   [[2.24] [du]](#du)
    -   [[2.25] [echo]](#echo)
    -   [[2.26] [env]](#env)
    -   [[2.27] [expand]](#expand)
    -   [[2.28] [expr]](#expr)
    -   [[2.29] [factor]](#factor)
    -   [[2.30] [false]](#false)
    -   [[2.31] [fmt]](#fmt)
    -   [[2.32] [fold]](#fold)
    -   [[2.33] [head]](#head)
    -   [[2.34] [hostid]](#hostid)
    -   [[2.35] [id]](#id)
    -   [[2.36] [install]](#install)
    -   [[2.37] [join]](#join)
    -   [[2.38] [link]](#link)
    -   [[2.39] [ln]](#ln)
    -   [[2.40] [logname]](#logname)
    -   [[2.41] [ls]](#ls)
    -   [[2.42] [md5sum]](#md5sum)
    -   [[2.43] [mkdir]](#mkdir)
    -   [[2.44] [mkfifo]](#mkfifo)
    -   [[2.45] [mknod]](#mknod)
    -   [[2.46] [mktemp]](#mktemp)
    -   [[2.47] [mv]](#mv)
    -   [[2.48] [nice]](#nice)
    -   [[2.49] [nl]](#nl)
    -   [[2.50] [nohup]](#nohup)
    -   [[2.51] [nproc]](#nproc)
    -   [[2.52] [numfmt]](#numfmt)
    -   [[2.53] [od]](#od)
    -   [[2.54] [paste]](#paste)
    -   [[2.55] [pathchk]](#pathchk)
    -   [[2.56] [pinky]](#pinky)
    -   [[2.57] [pr]](#pr)
    -   [[2.58] [printenv]](#printenv)
    -   [[2.59] [printf]](#printf)
    -   [[2.60] [ptx]](#ptx)
    -   [[2.61] [pwd]](#pwd)
    -   [[2.62] [readlink]](#readlink)
    -   [[2.63] [realpath]](#realpath)
    -   [[2.64] [rm]](#rm)
    -   [[2.65] [rmdir]](#rmdir)
    -   [[2.66] [runcon]](#runcon)
    -   [[2.67] [seq]](#seq)
    -   [[2.68] [sha1sum]](#sha1sum)
    -   [[2.69] [sha224sum]](#sha224sum)
    -   [[2.70] [sha256sum]](#sha256sum)
    -   [[2.71] [sha384sum]](#sha384sum)
    -   [[2.72] [sha512sum]](#sha512sum)
    -   [[2.73] [shred]](#shred)
    -   [[2.74] [shuf]](#shuf)
    -   [[2.75] [sleep]](#sleep)
    -   [[2.76] [sort]](#sort)
    -   [[2.77] [split]](#split)
    -   [[2.78] [stat]](#stat)
    -   [[2.79] [stdbuf]](#stdbuf)
    -   [[2.80] [stty]](#stty)
    -   [[2.81] [sum]](#sum)
    -   [[2.82] [sync]](#sync)
    -   [[2.83] [tac]](#tac)
    -   [[2.84] [tail]](#tail)
    -   [[2.85] [tee]](#tee)
    -   [[2.86] [test]](#test)
    -   [[2.87] [timeout]](#timeout)
    -   [[2.88] [touch]](#touch)
    -   [[2.89] [tr]](#tr)
    -   [[2.90] [true]](#true)
    -   [[2.91] [truncate]](#truncate)
    -   [[2.92] [tsort]](#tsort)
    -   [[2.93] [tty]](#tty)
    -   [[2.94] [uname]](#uname)
    -   [[2.95] [unexpand]](#unexpand)
    -   [[2.96] [uniq]](#uniq)
    -   [[2.97] [unlink]](#unlink)
    -   [[2.98] [users]](#users)
    -   [[2.99] [vdir]](#vdir)
    -   [[2.100] [wc]](#wc)
    -   [[2.101] [who]](#who)
    -   [[2.102] [whoami]](#whoami)
    -   [[2.103] [yes]](#yes)
-   [[3] [See also]](#See_also)

## [Installation]

The [[[sys-apps/coreutils]](https://packages.gentoo.org/packages/sys-apps/coreutils)[]] package is part of the [system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)") so it should not need installing.

### [USE flags]

The package offers a couple of [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag").

### [USE flags for] [sys-apps/coreutils](https://packages.gentoo.org/packages/sys-apps/coreutils) [[]] [Standard GNU utilities (chmod, cp, dd, ls, sort, tr, head, wc, who,\...)]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------
  [`+openssl`](https://packages.gentoo.org/useflags/+openssl)       Use openssl libcrypto hash routines for hash functions
  [`+split-usr`](https://packages.gentoo.org/useflags/+split-usr)   Enable this if /bin and /usr/bin are separate directories
  [`acl`](https://packages.gentoo.org/useflags/acl)                 Add support for Access Control Lists
  [`caps`](https://packages.gentoo.org/useflags/caps)               Add Linux capabilities support in output of file utilities (ls, dir, \...) via sys-libs/libcap
  [`gmp`](https://packages.gentoo.org/useflags/gmp)                 Add support for dev-libs/gmp (GNU MP library)
  [`hostname`](https://packages.gentoo.org/useflags/hostname)       Build the hostname program
  [`kill`](https://packages.gentoo.org/useflags/kill)               Build the kill program
  [`multicall`](https://packages.gentoo.org/useflags/multicall)     Build all tools into a single \`coreutils\` program akin to busybox to save space
  [`nls`](https://packages.gentoo.org/useflags/nls)                 Add Native Language Support (using gettext - GNU locale utilities)
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`static`](https://packages.gentoo.org/useflags/static)           !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`test-full`](https://packages.gentoo.org/useflags/test-full)     Run expensive tests (mostly CPU intensive).
  [`vanilla`](https://packages.gentoo.org/useflags/vanilla)         Do not add extra patches which change default behaviour; DO NOT USE THIS ON A GLOBAL SCALE as the severity of the meaning changes drastically
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  [`xattr`](https://packages.gentoo.org/useflags/xattr)             Add support for extended attributes (filesystem-stored metadata)
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-24 04:38] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

If [USE flags](#USE_flags) are changed or the package needs rebuilding, the following command should be issued.

`root `[`#`]`emerge --ask --oneshot sys-apps/coreutils`

** Note**\
`--oneshot` is used in the above command because [[[sys-apps/coreutils]](https://packages.gentoo.org/packages/sys-apps/coreutils)[]] is included in the [system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)"), so it should not be added to the [selected set](https://wiki.gentoo.org/wiki/Selected_set_(Portage) "Selected set (Portage)").

## [Usage]

Depending on the [shell](https://wiki.gentoo.org/wiki/Shell "Shell") used, some of these commands may be pre-empted by shell builtins.

### [arch]

Print machine hardware name (same as uname -m).

`user `[`$`]`arch --help`

    Usage: arch [OPTION]...
    Print machine architecture.

          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/arch>
    or available locally via: info '(coreutils) arch invocation'

### [b2sum]

Compute and check BLAKE2 message digest.

`user `[`$`]`b2sum --help`

    Usage: b2sum [OPTION]... [FILE]...
    Print or check BLAKE2 (512-bit) checksums.

    With no FILE, or when FILE is -, read standard input.

      -b, --binary         read in binary mode
      -c, --check          read BLAKE2 sums from the FILEs and check them
      -l, --length         digest length in bits; must not exceed the maximum for
                           the blake2 algorithm and must be a multiple of 8
          --tag            create a BSD-style checksum
      -t, --text           read in text mode (default)
      -z, --zero           end each output line with NUL, not newline,
                           and disable file name escaping

    The following five options are useful only when verifying checksums:
          --ignore-missing  don't fail or report status for missing files
          --quiet          don't print OK for each successfully verified file
          --status         don't output anything, status code shows success
          --strict         exit non-zero for improperly formatted checksum lines
      -w, --warn           warn about improperly formatted checksum lines

          --help     display this help and exit
          --version  output version information and exit

    The sums are computed as described in RFC 7693.  When checking, the input
    should be a former output of this program.  The default mode is to print a
    line with checksum, a space, a character indicating input mode ('*' for binary,
    ' ' for text or where binary is insignificant), and name for each FILE.

    Note: There is no difference between binary mode and text mode on GNU systems.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/b2sum>
    or available locally via: info '(coreutils) b2sum invocation'

### [base32]

Base32 encode/decode data and print to standard output.

`user `[`$`]`base32 --help`

    Usage: base32 [OPTION]... [FILE]
    Base32 encode or decode FILE, or standard input, to standard output.

    With no FILE, or when FILE is -, read standard input.

    Mandatory arguments to long options are mandatory for short options too.
      -d, --decode          decode data
      -i, --ignore-garbage  when decoding, ignore non-alphabet characters
      -w, --wrap=COLS       wrap encoded lines after COLS character (default 76).
                              Use 0 to disable line wrapping

          --help     display this help and exit
          --version  output version information and exit

    The data are encoded as described for the base32 alphabet in RFC 4648.
    When decoding, the input may contain newlines in addition to the bytes of
    the formal base32 alphabet.  Use --ignore-garbage to attempt to recover
    from any other non-alphabet bytes in the encoded stream.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/base32>
    or available locally via: info '(coreutils) base32 invocation'

### [base64]

Base64 encode/decode data and print to standard output.

`user `[`$`]`base64 --help`

    Usage: base64 [OPTION]... [FILE]
    Base64 encode or decode FILE, or standard input, to standard output.

    With no FILE, or when FILE is -, read standard input.

    Mandatory arguments to long options are mandatory for short options too.
      -d, --decode          decode data
      -i, --ignore-garbage  when decoding, ignore non-alphabet characters
      -w, --wrap=COLS       wrap encoded lines after COLS character (default 76).
                              Use 0 to disable line wrapping

          --help     display this help and exit
          --version  output version information and exit

    The data are encoded as described for the base64 alphabet in RFC 4648.
    When decoding, the input may contain newlines in addition to the bytes of
    the formal base64 alphabet.  Use --ignore-garbage to attempt to recover
    from any other non-alphabet bytes in the encoded stream.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/base64>
    or available locally via: info '(coreutils) base64 invocation'

### [basename]

Strip directory and suffix from filenames.

`user `[`$`]`basename --help`

    Usage: basename NAME [SUFFIX]
      or:  basename OPTION... NAME...
    Print NAME with any leading directory components removed.
    If specified, also remove a trailing SUFFIX.

    Mandatory arguments to long options are mandatory for short options too.
      -a, --multiple       support multiple arguments and treat each as a NAME
      -s, --suffix=SUFFIX  remove a trailing SUFFIX; implies -a
      -z, --zero           end each output line with NUL, not newline
          --help     display this help and exit
          --version  output version information and exit

    Examples:
      basename /usr/bin/sort          -> "sort"
      basename include/stdio.h .h     -> "stdio"
      basename -s .h include/stdio.h  -> "stdio"
      basename -a any/str1 any/str2   -> "str1" followed by "str2"

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/basename>
    or available locally via: info '(coreutils) basename invocation'

### [basenc]

Encode/decode data and print to standard output.

`user `[`$`]`basenc --help`

    Usage: basenc [OPTION]... [FILE]
    basenc encode or decode FILE, or standard input, to standard output.

    With no FILE, or when FILE is -, read standard input.

    Mandatory arguments to long options are mandatory for short options too.
          --base64          same as 'base64' program (RFC4648 section 4)
          --base64url       file- and url-safe base64 (RFC4648 section 5)
          --base32          same as 'base32' program (RFC4648 section 6)
          --base32hex       extended hex alphabet base32 (RFC4648 section 7)
          --base16          hex encoding (RFC4648 section 8)
          --base2msbf       bit string with most significant bit (msb) first
          --base2lsbf       bit string with least significant bit (lsb) first
      -d, --decode          decode data
      -i, --ignore-garbage  when decoding, ignore non-alphabet characters
      -w, --wrap=COLS       wrap encoded lines after COLS character (default 76).
                              Use 0 to disable line wrapping

          --z85             ascii85-like encoding (ZeroMQ spec:32/Z85);
                            when encoding, input length must be a multiple of 4;
                            when decoding, input length must be a multiple of 5
          --help     display this help and exit
          --version  output version information and exit

    When decoding, the input may contain newlines in addition to the bytes of
    the formal alphabet.  Use --ignore-garbage to attempt to recover
    from any other non-alphabet bytes in the encoded stream.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/basenc>
    or available locally via: info '(coreutils) basenc invocation'

### [cat]

Concatenate files and print on the standard output.

`user `[`$`]`cat --help`

    Usage: cat [OPTION]... [FILE]...
    Concatenate FILE(s) to standard output.

    With no FILE, or when FILE is -, read standard input.

      -A, --show-all           equivalent to -vET
      -b, --number-nonblank    number nonempty output lines, overrides -n
      -e                       equivalent to -vE
      -E, --show-ends          display $ at end of each line
      -n, --number             number all output lines
      -s, --squeeze-blank      suppress repeated empty output lines
      -t                       equivalent to -vT
      -T, --show-tabs          display TAB characters as ^I
      -u                       (ignored)
      -v, --show-nonprinting   use ^ and M- notation, except for LFD and TAB
          --help     display this help and exit
          --version  output version information and exit

    Examples:
      cat f - g  Output f's contents, then standard input, then g's contents.
      cat        Copy standard input to standard output.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/cat>
    or available locally via: info '(coreutils) cat invocation'

### [chcon]

Change file security context.

`user `[`$`]`chcon --help`

    Usage: chcon [OPTION]... CONTEXT FILE...
      or:  chcon [OPTION]... [-u USER] [-r ROLE] [-l RANGE] [-t TYPE] FILE...
      or:  chcon [OPTION]... --reference=RFILE FILE...
    Change the SELinux security context of each FILE to CONTEXT.
    With --reference, change the security context of each FILE to that of RFILE.

    Mandatory arguments to long options are mandatory for short options too.
          --dereference      affect the referent of each symbolic link (this is
                             the default), rather than the symbolic link itself
      -h, --no-dereference   affect symbolic links instead of any referenced file
      -u, --user=USER        set user USER in the target security context
      -r, --role=ROLE        set role ROLE in the target security context
      -t, --type=TYPE        set type TYPE in the target security context
      -l, --range=RANGE      set range RANGE in the target security context
          --no-preserve-root  do not treat '/' specially (the default)
          --preserve-root    fail to operate recursively on '/'
          --reference=RFILE  use RFILE's security context rather than specifying
                             a CONTEXT value
      -R, --recursive        operate on files and directories recursively
      -v, --verbose          output a diagnostic for every file processed

    The following options modify how a hierarchy is traversed when the -R
    option is also specified.  If more than one is specified, only the final
    one takes effect.

      -H                     if a command line argument is a symbolic link
                             to a directory, traverse it
      -L                     traverse every symbolic link to a directory
                             encountered
      -P                     do not traverse any symbolic links (default)

          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/chcon>
    or available locally via: info '(coreutils) chcon invocation'

### [chgrp]

Change group ownership.

`user `[`$`]`chgrp --help`

    Usage: chgrp [OPTION]... GROUP FILE...
      or:  chgrp [OPTION]... --reference=RFILE FILE...
    Change the group of each FILE to GROUP.
    With --reference, change the group of each FILE to that of RFILE.

      -c, --changes          like verbose but report only when a change is made
      -f, --silent, --quiet  suppress most error messages
      -v, --verbose          output a diagnostic for every file processed
          --dereference      affect the referent of each symbolic link (this is
                             the default), rather than the symbolic link itself
      -h, --no-dereference   affect symbolic links instead of any referenced file
                             (useful only on systems that can change the
                             ownership of a symlink)
          --no-preserve-root  do not treat '/' specially (the default)
          --preserve-root    fail to operate recursively on '/'
          --reference=RFILE  use RFILE's group rather than specifying a
                             GROUP value
      -R, --recursive        operate on files and directories recursively

    The following options modify how a hierarchy is traversed when the -R
    option is also specified.  If more than one is specified, only the final
    one takes effect.

      -H                     if a command line argument is a symbolic link
                             to a directory, traverse it
      -L                     traverse every symbolic link to a directory
                             encountered
      -P                     do not traverse any symbolic links (default)

          --help     display this help and exit
          --version  output version information and exit

    Examples:
      chgrp staff /u      Change the group of /u to "staff".
      chgrp -hR staff /u  Change the group of /u and subfiles to "staff".

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/chgrp>
    or available locally via: info '(coreutils) chgrp invocation'

### [chmod]

Change file mode bits.

`user `[`$`]`chmod --help`

    Usage: chmod [OPTION]... MODE[,MODE]... FILE...
      or:  chmod [OPTION]... OCTAL-MODE FILE...
      or:  chmod [OPTION]... --reference=RFILE FILE...
    Change the mode of each FILE to MODE.
    With --reference, change the mode of each FILE to that of RFILE.

      -c, --changes          like verbose but report only when a change is made
      -f, --silent, --quiet  suppress most error messages
      -v, --verbose          output a diagnostic for every file processed
          --no-preserve-root  do not treat '/' specially (the default)
          --preserve-root    fail to operate recursively on '/'
          --reference=RFILE  use RFILE's mode instead of MODE values
      -R, --recursive        change files and directories recursively
          --help     display this help and exit
          --version  output version information and exit

    Each MODE is of the form '[ugoa]*([-+=]([rwxXst]*|[ugo]))+|[-+=][0-7]+'.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/chmod>
    or available locally via: info '(coreutils) chmod invocation'

### [chown]

Change file owner and group.

`user `[`$`]`chown --help`

    Usage: chown [OPTION]... [OWNER][:[GROUP]] FILE...
      or:  chown [OPTION]... --reference=RFILE FILE...
    Change the owner and/or group of each FILE to OWNER and/or GROUP.
    With --reference, change the owner and group of each FILE to those of RFILE.

      -c, --changes          like verbose but report only when a change is made
      -f, --silent, --quiet  suppress most error messages
      -v, --verbose          output a diagnostic for every file processed
          --dereference      affect the referent of each symbolic link (this is
                             the default), rather than the symbolic link itself
      -h, --no-dereference   affect symbolic links instead of any referenced file
                             (useful only on systems that can change the
                             ownership of a symlink)
          --from=CURRENT_OWNER:CURRENT_GROUP
                             change the owner and/or group of each file only if
                             its current owner and/or group match those specified
                             here.  Either may be omitted, in which case a match
                             is not required for the omitted attribute
          --no-preserve-root  do not treat '/' specially (the default)
          --preserve-root    fail to operate recursively on '/'
          --reference=RFILE  use RFILE's owner and group rather than
                             specifying OWNER:GROUP values
      -R, --recursive        operate on files and directories recursively

    The following options modify how a hierarchy is traversed when the -R
    option is also specified.  If more than one is specified, only the final
    one takes effect.

      -H                     if a command line argument is a symbolic link
                             to a directory, traverse it
      -L                     traverse every symbolic link to a directory
                             encountered
      -P                     do not traverse any symbolic links (default)

          --help     display this help and exit
          --version  output version information and exit

    Owner is unchanged if missing.  Group is unchanged if missing, but changed
    to login group if implied by a ':' following a symbolic OWNER.
    OWNER and GROUP may be numeric as well as symbolic.

    Examples:
      chown root /u        Change the owner of /u to "root".
      chown root:staff /u  Likewise, but also change its group to "staff".
      chown -hR root /u    Change the owner of /u and subfiles to "root".

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/chown>
    or available locally via: info '(coreutils) chown invocation'

### [chroot]

Run command or interactive shell with special root directory.

`user `[`$`]`chroot --help`

    Usage: chroot [OPTION] NEWROOT [COMMAND [ARG]...]
      or:  chroot OPTION
    Run COMMAND with root directory set to NEWROOT.

      --groups=G_LIST        specify supplementary groups as g1,g2,..,gN
      --userspec=USER:GROUP  specify user and group (ID or name) to use
      --skip-chdir           do not change working directory to '/'
          --help     display this help and exit
          --version  output version information and exit

    If no command is given, run '"$SHELL" -i' (default: '/bin/sh -i').

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/chroot>
    or available locally via: info '(coreutils) chroot invocation'

### [cksum]

Checksum and count the bytes in a file.

`user `[`$`]`cksum --help`

    Usage: cksum [FILE]...
      or:  cksum [OPTION]
    Print CRC checksum and byte counts of each FILE.

          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/cksum>
    or available locally via: info '(coreutils) cksum invocation'

### [comm]

Compare two sorted files line by line.

`user `[`$`]`comm --help`

    Usage: comm [OPTION]... FILE1 FILE2
    Compare sorted files FILE1 and FILE2 line by line.

    When FILE1 or FILE2 (not both) is -, read standard input.

    With no options, produce three-column output.  Column one contains
    lines unique to FILE1, column two contains lines unique to FILE2,
    and column three contains lines common to both files.

      -1              suppress column 1 (lines unique to FILE1)
      -2              suppress column 2 (lines unique to FILE2)
      -3              suppress column 3 (lines that appear in both files)

      --check-order     check that the input is correctly sorted, even
                          if all input lines are pairable
      --nocheck-order   do not check that the input is correctly sorted
      --output-delimiter=STR  separate columns with STR
      --total           output a summary
      -z, --zero-terminated    line delimiter is NUL, not newline
          --help     display this help and exit
          --version  output version information and exit

    Note, comparisons honor the rules specified by 'LC_COLLATE'.

    Examples:
      comm -12 file1 file2  Print only lines present in both file1 and file2.
      comm -3 file1 file2  Print lines in file1 not in file2, and vice versa.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/comm>
    or available locally via: info '(coreutils) comm invocation'

### [cp]

Copy files and directories.

`user `[`$`]`cp --help`

    Usage: cp [OPTION]... [-T] SOURCE DEST
      or:  cp [OPTION]... SOURCE... DIRECTORY
      or:  cp [OPTION]... -t DIRECTORY SOURCE...
    Copy SOURCE to DEST, or multiple SOURCE(s) to DIRECTORY.

    Mandatory arguments to long options are mandatory for short options too.
      -a, --archive                same as -dR --preserve=all
          --attributes-only        don't copy the file data, just the attributes
          --backup[=CONTROL]       make a backup of each existing destination file
      -b                           like --backup but does not accept an argument
          --copy-contents          copy contents of special files when recursive
      -d                           same as --no-dereference --preserve=links
      -f, --force                  if an existing destination file cannot be
                                     opened, remove it and try again (this option
                                     is ignored when the -n option is also used)
      -i, --interactive            prompt before overwrite (overrides a previous -n
                                      option)
      -H                           follow command-line symbolic links in SOURCE
      -l, --link                   hard link files instead of copying
      -L, --dereference            always follow symbolic links in SOURCE
      -n, --no-clobber             do not overwrite an existing file (overrides
                                     a previous -i option)
      -P, --no-dereference         never follow symbolic links in SOURCE
      -p                           same as --preserve=mode,ownership,timestamps
          --preserve[=ATTR_LIST]   preserve the specified attributes (default:
                                     mode,ownership,timestamps), if possible
                                     additional attributes: context, links, xattr,
                                     all
          --no-preserve=ATTR_LIST  don't preserve the specified attributes
          --parents                use full source file name under DIRECTORY
      -R, -r, --recursive          copy directories recursively
          --reflink[=WHEN]         control clone/CoW copies. See below
          --remove-destination     remove each existing destination file before
                                     attempting to open it (contrast with --force)
          --sparse=WHEN            control creation of sparse files. See below
          --strip-trailing-slashes  remove any trailing slashes from each SOURCE
                                     argument
      -s, --symbolic-link          make symbolic links instead of copying
      -S, --suffix=SUFFIX          override the usual backup suffix
      -t, --target-directory=DIRECTORY  copy all SOURCE arguments into DIRECTORY
      -T, --no-target-directory    treat DEST as a normal file
      -u, --update                 copy only when the SOURCE file is newer
                                     than the destination file or when the
                                     destination file is missing
      -v, --verbose                explain what is being done
      -x, --one-file-system        stay on this file system
      -Z                           set SELinux security context of destination
                                     file to default type
          --context[=CTX]          like -Z, or if CTX is specified then set the
                                     SELinux or SMACK security context to CTX
          --help     display this help and exit
          --version  output version information and exit

    By default, sparse SOURCE files are detected by a crude heuristic and the
    corresponding DEST file is made sparse as well.  That is the behavior
    selected by --sparse=auto.  Specify --sparse=always to create a sparse DEST
    file whenever the SOURCE file contains a long enough sequence of zero bytes.
    Use --sparse=never to inhibit creation of sparse files.

    When --reflink[=always] is specified, perform a lightweight copy, where the
    data blocks are copied only when modified.  If this is not possible the copy
    fails, or if --reflink=auto is specified, fall back to a standard copy.
    Use --reflink=never to ensure a standard copy is performed.

    The backup suffix is '~', unless set with --suffix or SIMPLE_BACKUP_SUFFIX.
    The version control method may be selected via the --backup option or through
    the VERSION_CONTROL environment variable.  Here are the values:

      none, off       never make backups (even if --backup is given)
      numbered, t     make numbered backups
      existing, nil   numbered if numbered backups exist, simple otherwise
      simple, never   always make simple backups

    As a special case, cp makes a backup of SOURCE when the force and backup
    options are given and SOURCE and DEST are the same name for an existing,
    regular file.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/cp>
    or available locally via: info '(coreutils) cp invocation'

### [csplit]

Split a file into sections determined by context lines.

`user `[`$`]`csplit --help`

    Usage: csplit [OPTION]... FILE PATTERN...
    Output pieces of FILE separated by PATTERN(s) to files 'xx00', 'xx01', ...,
    and output byte counts of each piece to standard output.

    Read standard input if FILE is -

    Mandatory arguments to long options are mandatory for short options too.
      -b, --suffix-format=FORMAT  use sprintf FORMAT instead of %02d
      -f, --prefix=PREFIX        use PREFIX instead of 'xx'
      -k, --keep-files           do not remove output files on errors
          --suppress-matched     suppress the lines matching PATTERN
      -n, --digits=DIGITS        use specified number of digits instead of 2
      -s, --quiet, --silent      do not print counts of output file sizes
      -z, --elide-empty-files    remove empty output files
          --help     display this help and exit
          --version  output version information and exit

    Each PATTERN may be:
      INTEGER            copy up to but not including specified line number
      /REGEXP/[OFFSET]   copy up to but not including a matching line
      %REGEXP%[OFFSET]   skip to, but not including a matching line
                repeat the previous pattern specified number of times
                      repeat the previous pattern as many times as possible

    A line OFFSET is a required '+' or '-' followed by a positive integer.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/csplit>
    or available locally via: info '(coreutils) csplit invocation'

### [cut]

Remove sections from each line of files.

`user `[`$`]`cut --help`

    Usage: cut OPTION... [FILE]...
    Print selected parts of lines from each FILE to standard output.

    With no FILE, or when FILE is -, read standard input.

    Mandatory arguments to long options are mandatory for short options too.
      -b, --bytes=LIST        select only these bytes
      -c, --characters=LIST   select only these characters
      -d, --delimiter=DELIM   use DELIM instead of TAB for field delimiter
      -f, --fields=LIST       select only these fields;  also print any line
                                that contains no delimiter character, unless
                                the -s option is specified
      -n                      (ignored)
          --complement        complement the set of selected bytes, characters
                                or fields
      -s, --only-delimited    do not print lines not containing delimiters
          --output-delimiter=STRING  use STRING as the output delimiter
                                the default is to use the input delimiter
      -z, --zero-terminated    line delimiter is NUL, not newline
          --help     display this help and exit
          --version  output version information and exit

    Use one, and only one of -b, -c or -f.  Each LIST is made up of one
    range, or many ranges separated by commas.  Selected input is written
    in the same order that it is read, and is written exactly once.
    Each range is one of:

      N     N'th byte, character or field, counted from 1
      N-    from N'th byte, character or field, to end of line
      N-M   from N'th to M'th (included) byte, character or field
      -M    from first to M'th (included) byte, character or field

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/cut>
    or available locally via: info '(coreutils) cut invocation'

### [date]

Print or set the system date and time.

`user `[`$`]`date --help`

    Usage: date [OPTION]... [+FORMAT]
      or:  date [-u|--utc|--universal] [MMDDhhmm[[CC]YY][.ss]]
    Display the current time in the given FORMAT, or set the system date.

    Mandatory arguments to long options are mandatory for short options too.
      -d, --date=STRING          display time described by STRING, not 'now'
          --debug                annotate the parsed date,
                                  and warn about questionable usage to stderr
      -f, --file=DATEFILE        like --date; once for each line of DATEFILE
      -I[FMT], --iso-8601[=FMT]  output date/time in ISO 8601 format.
                                   FMT='date' for date only (the default),
                                   'hours', 'minutes', 'seconds', or 'ns'
                                   for date and time to the indicated precision.
                                   Example: 2006-08-14T02:34:56-06:00
      -R, --rfc-email            output date and time in RFC 5322 format.
                                   Example: Mon, 14 Aug 2006 02:34:56 -0600
          --rfc-3339=FMT         output date/time in RFC 3339 format.
                                   FMT='date', 'seconds', or 'ns'
                                   for date and time to the indicated precision.
                                   Example: 2006-08-14 02:34:56-06:00
      -r, --reference=FILE       display the last modification time of FILE
      -s, --set=STRING           set time described by STRING
      -u, --utc, --universal     print or set Coordinated Universal Time (UTC)
          --help     display this help and exit
          --version  output version information and exit

    FORMAT controls the output.  Interpreted sequences are:

      %%   a literal %
      %a   locale's abbreviated weekday name (e.g., Sun)
      %A   locale's full weekday name (e.g., Sunday)
      %b   locale's abbreviated month name (e.g., Jan)
      %B   locale's full month name (e.g., January)
      %c   locale's date and time (e.g., Thu Mar  3 23:05:25 2005)
      %C   century; like %Y, except omit last two digits (e.g., 20)
      %d   day of month (e.g., 01)
      %D   date; same as %m/%d/%y
      %e   day of month, space padded; same as %_d
      %F   full date; like %+4Y-%m-%d
      %g   last two digits of year of ISO week number (see %G)
      %G   year of ISO week number (see %V); normally useful only with %V
      %h   same as %b
      %H   hour (00..23)
      %I   hour (01..12)
      %j   day of year (001..366)
      %k   hour, space padded ( 0..23); same as %_H
      %l   hour, space padded ( 1..12); same as %_I
      %m   month (01..12)
      %M   minute (00..59)
      %n   a newline
      %N   nanoseconds (000000000..999999999)
      %p   locale's equivalent of either AM or PM; blank if not known
      %P   like %p, but lower case
      %q   quarter of year (1..4)
      %r   locale's 12-hour clock time (e.g., 11:11:04 PM)
      %R   24-hour hour and minute; same as %H:%M
      %s   seconds since 1970-01-01 00:00:00 UTC
      %S   second (00..60)
      %t   a tab
      %T   time; same as %H:%M:%S
      %u   day of week (1..7); 1 is Monday
      %U   week number of year, with Sunday as first day of week (00..53)
      %V   ISO week number, with Monday as first day of week (01..53)
      %w   day of week (0..6); 0 is Sunday
      %W   week number of year, with Monday as first day of week (00..53)
      %x   locale's date representation (e.g., 12/31/99)
      %X   locale's time representation (e.g., 23:13:48)
      %y   last two digits of year (00..99)
      %Y   year
      %z   +hhmm numeric time zone (e.g., -0400)
      %:z  +hh:mm numeric time zone (e.g., -04:00)
      %::z  +hh:mm:ss numeric time zone (e.g., -04:00:00)
      %:::z  numeric time zone with : to necessary precision (e.g., -04, +05:30)
      %Z   alphabetic time zone abbreviation (e.g., EDT)

    By default, date pads numeric fields with zeroes.
    The following optional flags may follow '%':

      -  (hyphen) do not pad the field
      _  (underscore) pad with spaces
      0  (zero) pad with zeros
      +  pad with zeros, and put '+' before future years with >4 digits
      ^  use upper case if possible
      #  use opposite case if possible

    After any flags comes an optional field width, as a decimal number;
    then an optional modifier, which is either
    E to use the locale's alternate representations if available, or
    O to use the locale's alternate numeric symbols if available.

    Examples:
    Convert seconds since the epoch (1970-01-01 UTC) to a date
      $ date --date='@2147483647'

    Show the time on the west coast of the US (use tzselect(1) to find TZ)
      $ TZ='America/Los_Angeles' date

    Show the local time for 9AM next Friday on the west coast of the US
      $ date --date='TZ="America/Los_Angeles" 09:00 next Fri'

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/date>
    or available locally via: info '(coreutils) date invocation'

### [dd]

Convert and copy a file. See the [dd](https://wiki.gentoo.org/wiki/Dd "Dd") article.

`user `[`$`]`dd --help`

    Usage: dd [OPERAND]...
      or:  dd OPTION
    Copy a file, converting and formatting according to the operands.

      bs=BYTES        read and write up to BYTES bytes at a time (default: 512);
                      overrides ibs and obs
      cbs=BYTES       convert BYTES bytes at a time
      conv=CONVS      convert the file as per the comma separated symbol list
      count=N         copy only N input blocks
      ibs=BYTES       read up to BYTES bytes at a time (default: 512)
      if=FILE         read from FILE instead of stdin
      iflag=FLAGS     read as per the comma separated symbol list
      obs=BYTES       write BYTES bytes at a time (default: 512)
      of=FILE         write to FILE instead of stdout
      oflag=FLAGS     write as per the comma separated symbol list
      seek=N          skip N obs-sized blocks at start of output
      skip=N          skip N ibs-sized blocks at start of input
      status=LEVEL    The LEVEL of information to print to stderr;
                      'none' suppresses everything but error messages,
                      'noxfer' suppresses the final transfer statistics,
                      'progress' shows periodic transfer statistics

    N and BYTES may be followed by the following multiplicative suffixes:
    c=1, w=2, b=512, kB=1000, K=1024, MB=1000*1000, M=1024*1024, xM=M,
    GB=1000*1000*1000, G=1024*1024*1024, and so on for T, P, E, Z, Y.
    Binary prefixes can be used, too: KiB=K, MiB=M, and so on.

    Each CONV symbol may be:

      ascii     from EBCDIC to ASCII
      ebcdic    from ASCII to EBCDIC
      ibm       from ASCII to alternate EBCDIC
      block     pad newline-terminated records with spaces to cbs-size
      unblock   replace trailing spaces in cbs-size records with newline
      lcase     change upper case to lower case
      ucase     change lower case to upper case
      sparse    try to seek rather than write all-NUL output blocks
      swab      swap every pair of input bytes
      sync      pad every input block with NULs to ibs-size; when used
                with block or unblock, pad with spaces rather than NULs
      excl      fail if the output file already exists
      nocreat   do not create the output file
      notrunc   do not truncate the output file
      noerror   continue after read errors
      fdatasync  physically write output file data before finishing
      fsync     likewise, but also write metadata

    Each FLAG symbol may be:

      append    append mode (makes sense only for output; conv=notrunc suggested)
      direct    use direct I/O for data
      directory  fail unless a directory
      dsync     use synchronized I/O for data
      sync      likewise, but also for metadata
      fullblock  accumulate full blocks of input (iflag only)
      nonblock  use non-blocking I/O
      noatime   do not update access time
      nocache   Request to drop cache.  See also oflag=sync
      noctty    do not assign controlling terminal from file
      nofollow  do not follow symlinks
      count_bytes  treat 'count=N' as a byte count (iflag only)
      skip_bytes  treat 'skip=N' as a byte count (iflag only)
      seek_bytes  treat 'seek=N' as a byte count (oflag only)

    Sending a USR1 signal to a running 'dd' process makes it
    print I/O statistics to standard error and then resume copying.

    Options are:

          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/dd>
    or available locally via: info '(coreutils) dd invocation'

** Warning**\
Misuse of the dd command can easily result in severe data loss.

### [df]

Report file system disk space usage.

`user `[`$`]`df --help`

    Usage: /bin/df [OPTION]... [FILE]...
    Show information about the file system on which each FILE resides,
    or all file systems by default.

    Mandatory arguments to long options are mandatory for short options too.
      -a, --all             include pseudo, duplicate, inaccessible file systems
      -B, --block-size=SIZE  scale sizes by SIZE before printing them; e.g.,
                               '-BM' prints sizes in units of 1,048,576 bytes;
                               see SIZE format below
      -h, --human-readable  print sizes in powers of 1024 (e.g., 1023M)
      -H, --si              print sizes in powers of 1000 (e.g., 1.1G)
      -i, --inodes          list inode information instead of block usage
      -k                    like --block-size=1K
      -l, --local           limit listing to local file systems
          --no-sync         do not invoke sync before getting usage info (default)
          --output[=FIELD_LIST]  use the output format defined by FIELD_LIST,
                                   or print all fields if FIELD_LIST is omitted.
      -P, --portability     use the POSIX output format
          --sync            invoke sync before getting usage info
          --total           elide all entries insignificant to available space,
                              and produce a grand total
      -t, --type=TYPE       limit listing to file systems of type TYPE
      -T, --print-type      print file system type
      -x, --exclude-type=TYPE   limit listing to file systems not of type TYPE
      -v                    (ignored)
          --help     display this help and exit
          --version  output version information and exit

### [dir]

List directory contents.

`user `[`$`]`dir --help`

    Usage: dir [OPTION]... [FILE]...
    List information about the FILEs (the current directory by default).
    Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

    Mandatory arguments to long options are mandatory for short options too.
      -a, --all                  do not ignore entries starting with .
      -A, --almost-all           do not list implied . and ..
          --author               with -l, print the author of each file
      -b, --escape               print C-style escapes for nongraphic characters
          --block-size=SIZE      with -l, scale sizes by SIZE when printing them;
                                   e.g., '--block-size=M'; see SIZE format below
      -B, --ignore-backups       do not list implied entries ending with ~
      -c                         with -lt: sort by, and show, ctime (time of last
                                   modification of file status information);
                                   with -l: show ctime and sort by name;
                                   otherwise: sort by ctime, newest first
      -C                         list entries by columns
          --color[=WHEN]         colorize the output; WHEN can be 'always' (default
                                   if omitted), 'auto', or 'never'; more info below
      -d, --directory            list directories themselves, not their contents
      -D, --dired                generate output designed for Emacs' dired mode
      -f                         do not sort, enable -aU, disable -ls --color
      -F, --classify             append indicator (one of */=>@|) to entries
          --file-type            likewise, except do not append '*'
          --format=WORD          across -x, commas -m, horizontal -x, long -l,
                                   single-column -1, verbose -l, vertical -C
          --full-time            like -l --time-style=full-iso
      -g                         like -l, but do not list owner
          --group-directories-first
                                 group directories before files;
                                   can be augmented with a --sort option, but any
                                   use of --sort=none (-U) disables grouping
      -G, --no-group             in a long listing, don't print group names
      -h, --human-readable       with -l and -s, print sizes like 1K 234M 2G etc.
          --si                   likewise, but use powers of 1000 not 1024
      -H, --dereference-command-line
                                 follow symbolic links listed on the command line
          --dereference-command-line-symlink-to-dir
                                 follow each command line symbolic link
                                   that points to a directory
          --hide=PATTERN         do not list implied entries matching shell PATTERN
                                   (overridden by -a or -A)
          --hyperlink[=WHEN]     hyperlink file names; WHEN can be 'always'
                                   (default if omitted), 'auto', or 'never'
          --indicator-style=WORD  append indicator with style WORD to entry names:
                                   none (default), slash (-p),
                                   file-type (--file-type), classify (-F)
      -i, --inode                print the index number of each file
      -I, --ignore=PATTERN       do not list implied entries matching shell PATTERN
      -k, --kibibytes            default to 1024-byte blocks for disk usage;
                                   used only with -s and per directory totals
      -l                         use a long listing format
      -L, --dereference          when showing file information for a symbolic
                                   link, show information for the file the link
                                   references rather than for the link itself
      -m                         fill width with a comma separated list of entries
      -n, --numeric-uid-gid      like -l, but list numeric user and group IDs
      -N, --literal              print entry names without quoting
      -o                         like -l, but do not list group information
      -p, --indicator-style=slash
                                 append / indicator to directories
      -q, --hide-control-chars   print ? instead of nongraphic characters
          --show-control-chars   show nongraphic characters as-is (the default,
                                   unless program is 'ls' and output is a terminal)
      -Q, --quote-name           enclose entry names in double quotes
          --quoting-style=WORD   use quoting style WORD for entry names:
                                   literal, locale, shell, shell-always,
                                   shell-escape, shell-escape-always, c, escape
                                   (overrides QUOTING_STYLE environment variable)
      -r, --reverse              reverse order while sorting
      -R, --recursive            list subdirectories recursively
      -s, --size                 print the allocated size of each file, in blocks
      -S                         sort by file size, largest first
          --sort=WORD            sort by WORD instead of name: none (-U), size (-S),
                                   time (-t), version (-v), extension (-X)
          --time=WORD            change the default of using modification times;
                                   access time (-u): atime, access, use;
                                   change time (-c): ctime, status;
                                   birth time: birth, creation;
                                 with -l, WORD determines which time to show;
                                 with --sort=time, sort by WORD (newest first)
          --time-style=TIME_STYLE  time/date format with -l; see TIME_STYLE below
      -t                         sort by time, newest first; see --time
      -T, --tabsize=COLS         assume tab stops at each COLS instead of 8
      -u                         with -lt: sort by, and show, access time;
                                   with -l: show access time and sort by name;
                                   otherwise: sort by access time, newest first
      -U                         do not sort; list entries in directory order
      -v                         natural sort of (version) numbers within text
      -w, --width=COLS           set output width to COLS.  0 means no limit
      -x                         list entries by lines instead of by columns
      -X                         sort alphabetically by entry extension
      -Z, --context              print any security context of each file
      -1                         list one file per line.  Avoid '\n' with -q or -b
          --help     display this help and exit
          --version  output version information and exit

    The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
    Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).
    Binary prefixes can be used, too: KiB=K, MiB=M, and so on.

    The TIME_STYLE argument can be full-iso, long-iso, iso, locale, or +FORMAT.
    FORMAT is interpreted like in date(1).  If FORMAT is FORMAT1<newline>FORMAT2,
    then FORMAT1 applies to non-recent files and FORMAT2 to recent files.
    TIME_STYLE prefixed with 'posix-' takes effect only outside the POSIX locale.
    Also the TIME_STYLE environment variable sets the default style to use.

    Using color to distinguish file types is disabled both by default and
    with --color=never.  With --color=auto, ls emits color codes only when
    standard output is connected to a terminal.  The LS_COLORS environment
    variable can change the settings.  Use the dircolors command to set it.

    Exit status:
     0  if OK,
     1  if minor problems (e.g., cannot access subdirectory),
     2  if serious trouble (e.g., cannot access command-line argument).

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/dir>
    or available locally via: info '(coreutils) dir invocation'

### [dircolors]

Color setup for ls.

`user `[`$`]`dircolors --help`

    Usage: dircolors [OPTION]... [FILE]
    Output commands to set the LS_COLORS environment variable.

    Determine format of output:
      -b, --sh, --bourne-shell    output Bourne shell code to set LS_COLORS
      -c, --csh, --c-shell        output C shell code to set LS_COLORS
      -p, --print-database        output defaults
          --help     display this help and exit
          --version  output version information and exit

    If FILE is specified, read it to determine which colors to use for which
    file types and extensions.  Otherwise, a precompiled database is used.
    For details on the format of these files, run 'dircolors --print-database'.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/dircolors>
    or available locally via: info '(coreutils) dircolors invocation'

### [dirname]

Strip last component from file name.

`user `[`$`]`dirname --help`

    Usage: dirname [OPTION] NAME...
    Output each NAME with its last non-slash component and trailing slashes
    removed; if NAME contains no /'s, output '.' (meaning the current directory).

      -z, --zero     end each output line with NUL, not newline
          --help     display this help and exit
          --version  output version information and exit

    Examples:
      dirname /usr/bin/          -> "/usr"
      dirname dir1/str dir2/str  -> "dir1" followed by "dir2"
      dirname stdio.h            -> "."

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/dirname>
    or available locally via: info '(coreutils) dirname invocation'

### [du]

Estimate file space usage.

`user `[`$`]`du --help`

    Usage: du [OPTION]... [FILE]...
      or:  du [OPTION]... --files0-from=F
    Summarize disk usage of the set of FILEs, recursively for directories.

    Mandatory arguments to long options are mandatory for short options too.
      -0, --null            end each output line with NUL, not newline
      -a, --all             write counts for all files, not just directories
          --apparent-size   print apparent sizes, rather than disk usage; although
                              the apparent size is usually smaller, it may be
                              larger due to holes in ('sparse') files, internal
                              fragmentation, indirect blocks, and the like
      -B, --block-size=SIZE  scale sizes by SIZE before printing them; e.g.,
                               '-BM' prints sizes in units of 1,048,576 bytes;
                               see SIZE format below
      -b, --bytes           equivalent to '--apparent-size --block-size=1'
      -c, --total           produce a grand total
      -D, --dereference-args  dereference only symlinks that are listed on the
                              command line
      -d, --max-depth=N     print the total for a directory (or file, with --all)
                              only if it is N or fewer levels below the command
                              line argument;  --max-depth=0 is the same as
                              --summarize
          --files0-from=F   summarize disk usage of the
                              NUL-terminated file names specified in file F;
                              if F is -, then read names from standard input
      -H                    equivalent to --dereference-args (-D)
      -h, --human-readable  print sizes in human readable format (e.g., 1K 234M 2G)
          --inodes          list inode usage information instead of block usage
      -k                    like --block-size=1K
      -L, --dereference     dereference all symbolic links
      -l, --count-links     count sizes many times if hard linked
      -m                    like --block-size=1M
      -P, --no-dereference  don't follow any symbolic links (this is the default)
      -S, --separate-dirs   for directories do not include size of subdirectories
          --si              like -h, but use powers of 1000 not 1024
      -s, --summarize       display only a total for each argument
      -t, --threshold=SIZE  exclude entries smaller than SIZE if positive,
                              or entries greater than SIZE if negative
          --time            show time of the last modification of any file in the
                              directory, or any of its subdirectories
          --time=WORD       show time as WORD instead of modification time:
                              atime, access, use, ctime or status
          --time-style=STYLE  show times using STYLE, which can be:
                                full-iso, long-iso, iso, or +FORMAT;
                                FORMAT is interpreted like in 'date'
      -X, --exclude-from=FILE  exclude files that match any pattern in FILE
          --exclude=PATTERN    exclude files that match PATTERN
      -x, --one-file-system    skip directories on different file systems
          --help     display this help and exit
          --version  output version information and exit

    Display values are in units of the first available SIZE from --block-size,
    and the DU_BLOCK_SIZE, BLOCK_SIZE and BLOCKSIZE environment variables.
    Otherwise, units default to 1024 bytes (or 512 if POSIXLY_CORRECT is set).

    The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
    Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).
    Binary prefixes can be used, too: KiB=K, MiB=M, and so on.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/du>
    or available locally via: info '(coreutils) du invocation'

### [echo]

Display a line of text.

`user `[`$`]`/bin/echo --help`

    Usage: /bin/echo [SHORT-OPTION]... [STRING]...
      or:  /bin/echo LONG-OPTION
    Echo the STRING(s) to standard output.

      -n             do not output the trailing newline
      -e             enable interpretation of backslash escapes
      -E             disable interpretation of backslash escapes (default)
          --help     display this help and exit
          --version  output version information and exit

    If -e is in effect, the following sequences are recognized:

      \\      backslash
      \a      alert (BEL)
      \b      backspace
      \c      produce no further output
      \e      escape
      \f      form feed
      \n      new line
      \r      carriage return
      \t      horizontal tab
      \v      vertical tab
      \0NNN   byte with octal value NNN (1 to 3 digits)
      \xHH    byte with hexadecimal value HH (1 to 2 digits)

    NOTE: your shell may have its own version of echo, which usually supersedes
    the version described here.  Please refer to your shell's documentation
    for details about the options it supports.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/echo>
    or available locally via: info '(coreutils) echo invocation'

n.b. Some shells have an [echo] command built in, which is why this needs the [/bin] prefix to return the help text.

### [env]

Run a program in a modified environment.

`user `[`$`]`env --help`

    Usage: env [OPTION]... [-] [NAME=VALUE]... [COMMAND [ARG]...]
    Set each NAME to VALUE in the environment and run COMMAND.

    Mandatory arguments to long options are mandatory for short options too.
      -i, --ignore-environment  start with an empty environment
      -0, --null           end each output line with NUL, not newline
      -u, --unset=NAME     remove variable from the environment
      -C, --chdir=DIR      change working directory to DIR
      -S, --split-string=S  process and split S into separate arguments;
                            used to pass multiple arguments on shebang lines
          --block-signal[=SIG]    block delivery of SIG signal(s) to COMMAND
          --default-signal[=SIG]  reset handling of SIG signal(s) to the default
          --ignore-signal[=SIG]   set handling of SIG signals(s) to do nothing
          --list-signal-handling  list non default signal handling to stderr
      -v, --debug          print verbose information for each processing step
          --help     display this help and exit
          --version  output version information and exit

    A mere - implies -i.  If no COMMAND, print the resulting environment.

    SIG may be a signal name like 'PIPE', or a signal number like '13'.
    Without SIG, all known signals are included.  Multiple signals can be
    comma-separated.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/env>
    or available locally via: info '(coreutils) env invocation'

### [expand]

Convert tabs to spaces.

`user `[`$`]`expand --help`

    Usage: expand [OPTION]... [FILE]...
    Convert tabs in each FILE to spaces, writing to standard output.

    With no FILE, or when FILE is -, read standard input.

    Mandatory arguments to long options are mandatory for short options too.
      -i, --initial    do not convert tabs after non blanks
      -t, --tabs=N     have tabs N characters apart, not 8
      -t, --tabs=LIST  use comma separated list of tab positions
                         The last specified position can be prefixed with '/'
                         to specify a tab size to use after the last
                         explicitly specified tab stop.  Also a prefix of '+'
                         can be used to align remaining tab stops relative to
                         the last specified tab stop instead of the first column
          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/expand>
    or available locally via: info '(coreutils) expand invocation'

### [expr]

Evaluate expressions.

`user `[`$`]`expr --help`

    Usage: expr EXPRESSION
      or:  expr OPTION

          --help     display this help and exit
          --version  output version information and exit

    Print the value of EXPRESSION to standard output.  A blank line below
    separates increasing precedence groups.  EXPRESSION may be:

      ARG1 | ARG2       ARG1 if it is neither null nor 0, otherwise ARG2

      ARG1 & ARG2       ARG1 if neither argument is null or 0, otherwise 0

      ARG1 < ARG2       ARG1 is less than ARG2
      ARG1 <= ARG2      ARG1 is less than or equal to ARG2
      ARG1 = ARG2       ARG1 is equal to ARG2
      ARG1 != ARG2      ARG1 is unequal to ARG2
      ARG1 >= ARG2      ARG1 is greater than or equal to ARG2
      ARG1 > ARG2       ARG1 is greater than ARG2

      ARG1 + ARG2       arithmetic sum of ARG1 and ARG2
      ARG1 - ARG2       arithmetic difference of ARG1 and ARG2

      ARG1 * ARG2       arithmetic product of ARG1 and ARG2
      ARG1 / ARG2       arithmetic quotient of ARG1 divided by ARG2
      ARG1 % ARG2       arithmetic remainder of ARG1 divided by ARG2

      STRING : REGEXP   anchored pattern match of REGEXP in STRING

      match STRING REGEXP        same as STRING : REGEXP
      substr STRING POS LENGTH   substring of STRING, POS counted from 1
      index STRING CHARS         index in STRING where any CHARS is found, or 0
      length STRING              length of STRING
      + TOKEN                    interpret TOKEN as a string, even if it is a
                                   keyword like 'match' or an operator like '/'

      ( EXPRESSION )             value of EXPRESSION

    Beware that many operators need to be escaped or quoted for shells.
    Comparisons are arithmetic if both ARGs are numbers, else lexicographical.
    Pattern matches return the string matched between \( and \) or null; if
    \( and \) are not used, they return the number of characters matched or 0.

    Exit status is 0 if EXPRESSION is neither null nor 0, 1 if EXPRESSION is null
    or 0, 2 if EXPRESSION is syntactically invalid, and 3 if an error occurred.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/expr>
    or available locally via: info '(coreutils) expr invocation'

### [factor]

Factor numbers.

`user `[`$`]`factor --help`

    Usage: factor [NUMBER]...
      or:  factor OPTION
    Print the prime factors of each specified integer NUMBER.  If none
    are specified on the command line, read them from standard input.

          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/factor>
    or available locally via: info '(coreutils) factor invocation'

### [false]

Do nothing, unsuccessfully.

`user `[`$`]`/bin/false --help`

    Usage: /bin/false [ignored command line arguments]
      or:  /bin/false OPTION
    Exit with a status code indicating failure.

          --help     display this help and exit
          --version  output version information and exit

    NOTE: your shell may have its own version of false, which usually supersedes
    the version described here.  Please refer to your shell's documentation
    for details about the options it supports.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/false>
    or available locally via: info '(coreutils) false invocation'

n.b. Some shells have a [false] command built in, which is why this needs the [/bin] prefix to return the help text.

### [fmt]

Simple optimal text formatter.

`user `[`$`]`fmt --help`

    Usage: fmt [-WIDTH] [OPTION]... [FILE]...
    Reformat each paragraph in the FILE(s), writing to standard output.
    The option -WIDTH is an abbreviated form of --width=DIGITS.

    With no FILE, or when FILE is -, read standard input.

    Mandatory arguments to long options are mandatory for short options too.
      -c, --crown-margin        preserve indentation of first two lines
      -p, --prefix=STRING       reformat only lines beginning with STRING,
                                  reattaching the prefix to reformatted lines
      -s, --split-only          split long lines, but do not refill
      -t, --tagged-paragraph    indentation of first line different from second
      -u, --uniform-spacing     one space between words, two after sentences
      -w, --width=WIDTH         maximum line width (default of 75 columns)
      -g, --goal=WIDTH          goal width (default of 93% of width)
          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/fmt>
    or available locally via: info '(coreutils) fmt invocation'

### [fold]

Wrap each input line to fit in specified width.

`user `[`$`]`fold --help`

    Usage: fold [OPTION]... [FILE]...
    Wrap input lines in each FILE, writing to standard output.

    With no FILE, or when FILE is -, read standard input.

    Mandatory arguments to long options are mandatory for short options too.
      -b, --bytes         count bytes rather than columns
      -s, --spaces        break at spaces
      -w, --width=WIDTH   use WIDTH columns instead of 80
          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/fold>
    or available locally via: info '(coreutils) fold invocation'

### [head]

Output the first part of files.

`user `[`$`]`head --help`

    Usage: head [OPTION]... [FILE]...
    Print the first 10 lines of each FILE to standard output.
    With more than one FILE, precede each with a header giving the file name.

    With no FILE, or when FILE is -, read standard input.

    Mandatory arguments to long options are mandatory for short options too.
      -c, --bytes=[-]NUM       print the first NUM bytes of each file;
                                 with the leading '-', print all but the last
                                 NUM bytes of each file
      -n, --lines=[-]NUM       print the first NUM lines instead of the first 10;
                                 with the leading '-', print all but the last
                                 NUM lines of each file
      -q, --quiet, --silent    never print headers giving file names
      -v, --verbose            always print headers giving file names
      -z, --zero-terminated    line delimiter is NUL, not newline
          --help     display this help and exit
          --version  output version information and exit

    NUM may have a multiplier suffix:
    b 512, kB 1000, K 1024, MB 1000*1000, M 1024*1024,
    GB 1000*1000*1000, G 1024*1024*1024, and so on for T, P, E, Z, Y.
    Binary prefixes can be used, too: KiB=K, MiB=M, and so on.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/head>
    or available locally via: info '(coreutils) head invocation'

### [hostid]

Print the numeric identifier for the current host.

`user `[`$`]`hostid --help`

    Usage: hostid [OPTION]
    Print the numeric identifier (in hexadecimal) for the current host.

          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/hostid>
    or available locally via: info '(coreutils) hostid invocation'

### [id]

Print real and effective user and group IDs.

`user `[`$`]`id --help`

    Usage: id [OPTION]... [USER]...
    Print user and group information for each specified USER,
    or (when USER omitted) for the current user.

      -a             ignore, for compatibility with other versions
      -Z, --context  print only the security context of the process
      -g, --group    print only the effective group ID
      -G, --groups   print all group IDs
      -n, --name     print a name instead of a number, for -ugG
      -r, --real     print the real ID instead of the effective ID, with -ugG
      -u, --user     print only the effective user ID
      -z, --zero     delimit entries with NUL characters, not whitespace;
                       not permitted in default format
          --help     display this help and exit
          --version  output version information and exit

    Without any OPTION, print some useful set of identified information.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/id>
    or available locally via: info '(coreutils) id invocation'

### [install]

Copy files and set attributes.

`user `[`$`]`install --help`

    Usage: install [OPTION]... [-T] SOURCE DEST
      or:  install [OPTION]... SOURCE... DIRECTORY
      or:  install [OPTION]... -t DIRECTORY SOURCE...
      or:  install [OPTION]... -d DIRECTORY...

    This install program copies files (often just compiled) into destination
    locations you choose.  If you want to download and install a ready-to-use
    package on a GNU/Linux system, you should instead be using a package manager
    like yum(1) or apt-get(1).

    In the first three forms, copy SOURCE to DEST or multiple SOURCE(s) to
    the existing DIRECTORY, while setting permission modes and owner/group.
    In the 4th form, create all components of the given DIRECTORY(ies).

    Mandatory arguments to long options are mandatory for short options too.
          --backup[=CONTROL]  make a backup of each existing destination file
      -b                  like --backup but does not accept an argument
      -c                  (ignored)
      -C, --compare       compare each pair of source and destination files, and
                            in some cases, do not modify the destination at all
      -d, --directory     treat all arguments as directory names; create all
                            components of the specified directories
      -D                  create all leading components of DEST except the last,
                            or all components of --target-directory,
                            then copy SOURCE to DEST
      -g, --group=GROUP   set group ownership, instead of process' current group
      -m, --mode=MODE     set permission mode (as in chmod), instead of rwxr-xr-x
      -o, --owner=OWNER   set ownership (super-user only)
      -p, --preserve-timestamps   apply access/modification times of SOURCE files
                            to corresponding destination files
      -s, --strip         strip symbol tables
          --strip-program=PROGRAM  program used to strip binaries
      -S, --suffix=SUFFIX  override the usual backup suffix
      -t, --target-directory=DIRECTORY  copy all SOURCE arguments into DIRECTORY
      -T, --no-target-directory  treat DEST as a normal file
      -v, --verbose       print the name of each directory as it is created
          --preserve-context  preserve SELinux security context
      -Z                      set SELinux security context of destination
                                file and each created directory to default type
          --context[=CTX]     like -Z, or if CTX is specified then set the
                                SELinux or SMACK security context to CTX
          --help     display this help and exit
          --version  output version information and exit

    The backup suffix is '~', unless set with --suffix or SIMPLE_BACKUP_SUFFIX.
    The version control method may be selected via the --backup option or through
    the VERSION_CONTROL environment variable.  Here are the values:

      none, off       never make backups (even if --backup is given)
      numbered, t     make numbered backups
      existing, nil   numbered if numbered backups exist, simple otherwise
      simple, never   always make simple backups

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/install>
    or available locally via: info '(coreutils) install invocation'

### [join]

Join lines of two files on a common field.

`user `[`$`]`join --help`

    Usage: join [OPTION]... FILE1 FILE2
    For each pair of input lines with identical join fields, write a line to
    standard output.  The default join field is the first, delimited by blanks.

    When FILE1 or FILE2 (not both) is -, read standard input.

      -a FILENUM        also print unpairable lines from file FILENUM, where
                          FILENUM is 1 or 2, corresponding to FILE1 or FILE2
      -e EMPTY          replace missing input fields with EMPTY
      -i, --ignore-case  ignore differences in case when comparing fields
      -j FIELD          equivalent to '-1 FIELD -2 FIELD'
      -o FORMAT         obey FORMAT while constructing output line
      -t CHAR           use CHAR as input and output field separator
      -v FILENUM        like -a FILENUM, but suppress joined output lines
      -1 FIELD          join on this FIELD of file 1
      -2 FIELD          join on this FIELD of file 2
      --check-order     check that the input is correctly sorted, even
                          if all input lines are pairable
      --nocheck-order   do not check that the input is correctly sorted
      --header          treat the first line in each file as field headers,
                          print them without trying to pair them
      -z, --zero-terminated     line delimiter is NUL, not newline
          --help     display this help and exit
          --version  output version information and exit

    Unless -t CHAR is given, leading blanks separate fields and are ignored,
    else fields are separated by CHAR.  Any FIELD is a field number counted
    from 1.  FORMAT is one or more comma or blank separated specifications,
    each being 'FILENUM.FIELD' or '0'.  Default FORMAT outputs the join field,
    the remaining fields from FILE1, the remaining fields from FILE2, all
    separated by CHAR.  If FORMAT is the keyword 'auto', then the first
    line of each file determines the number of fields output for each line.

    Important: FILE1 and FILE2 must be sorted on the join fields.
    E.g., use "sort -k 1b,1" if 'join' has no options,
    or use "join -t ''" if 'sort' has no options.
    Note, comparisons honor the rules specified by 'LC_COLLATE'.
    If the input is not sorted and some lines cannot be joined, a
    warning message will be given.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/join>
    or available locally via: info '(coreutils) join invocation'

### [link]

Call the link function to create a link to a file.

`user `[`$`]`link --help`

    Usage: link FILE1 FILE2
      or:  link OPTION
    Call the link function to create a link named FILE2 to an existing FILE1.

          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/link>
    or available locally via: info '(coreutils) link invocation'

### [ln]

Make links between files.

`user `[`$`]`ln --help`

    Usage: ln [OPTION]... [-T] TARGET LINK_NAME
      or:  ln [OPTION]... TARGET
      or:  ln [OPTION]... TARGET... DIRECTORY
      or:  ln [OPTION]... -t DIRECTORY TARGET...
    In the 1st form, create a link to TARGET with the name LINK_NAME.
    In the 2nd form, create a link to TARGET in the current directory.
    In the 3rd and 4th forms, create links to each TARGET in DIRECTORY.
    Create hard links by default, symbolic links with --symbolic.
    By default, each destination (name of new link) should not already exist.
    When creating hard links, each TARGET must exist.  Symbolic links
    can hold arbitrary text; if later resolved, a relative link is
    interpreted in relation to its parent directory.

    Mandatory arguments to long options are mandatory for short options too.
          --backup[=CONTROL]      make a backup of each existing destination file
      -b                          like --backup but does not accept an argument
      -d, -F, --directory         allow the superuser to attempt to hard link
                                    directories (note: will probably fail due to
                                    system restrictions, even for the superuser)
      -f, --force                 remove existing destination files
      -i, --interactive           prompt whether to remove destinations
      -L, --logical               dereference TARGETs that are symbolic links
      -n, --no-dereference        treat LINK_NAME as a normal file if
                                    it is a symbolic link to a directory
      -P, --physical              make hard links directly to symbolic links
      -r, --relative              create symbolic links relative to link location
      -s, --symbolic              make symbolic links instead of hard links
      -S, --suffix=SUFFIX         override the usual backup suffix
      -t, --target-directory=DIRECTORY  specify the DIRECTORY in which to create
                                    the links
      -T, --no-target-directory   treat LINK_NAME as a normal file always
      -v, --verbose               print name of each linked file
          --help     display this help and exit
          --version  output version information and exit

    The backup suffix is '~', unless set with --suffix or SIMPLE_BACKUP_SUFFIX.
    The version control method may be selected via the --backup option or through
    the VERSION_CONTROL environment variable.  Here are the values:

      none, off       never make backups (even if --backup is given)
      numbered, t     make numbered backups
      existing, nil   numbered if numbered backups exist, simple otherwise
      simple, never   always make simple backups

    Using -s ignores -L and -P.  Otherwise, the last option specified controls
    behavior when a TARGET is a symbolic link, defaulting to -P.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/ln>
    or available locally via: info '(coreutils) ln invocation'

### [logname]

Print user\'s login name.

`user `[`$`]`logname --help`

    Usage: logname [OPTION]
    Print the name of the current user.

          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/logname>
    or available locally via: info '(coreutils) logname invocation'

### [ls]

List directory contents.

`user `[`$`]`ls --help`

    Usage: ls [OPTION]... [FILE]...
    List information about the FILEs (the current directory by default).
    Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

    Mandatory arguments to long options are mandatory for short options too.
      -a, --all                  do not ignore entries starting with .
      -A, --almost-all           do not list implied . and ..
          --author               with -l, print the author of each file
      -b, --escape               print C-style escapes for nongraphic characters
          --block-size=SIZE      with -l, scale sizes by SIZE when printing them;
                                   e.g., '--block-size=M'; see SIZE format below
      -B, --ignore-backups       do not list implied entries ending with ~
      -c                         with -lt: sort by, and show, ctime (time of last
                                   modification of file status information);
                                   with -l: show ctime and sort by name;
                                   otherwise: sort by ctime, newest first
      -C                         list entries by columns
          --color[=WHEN]         colorize the output; WHEN can be 'always' (default
                                   if omitted), 'auto', or 'never'; more info below
      -d, --directory            list directories themselves, not their contents
      -D, --dired                generate output designed for Emacs' dired mode
      -f                         do not sort, enable -aU, disable -ls --color
      -F, --classify             append indicator (one of */=>@|) to entries
          --file-type            likewise, except do not append '*'
          --format=WORD          across -x, commas -m, horizontal -x, long -l,
                                   single-column -1, verbose -l, vertical -C
          --full-time            like -l --time-style=full-iso
      -g                         like -l, but do not list owner
          --group-directories-first
                                 group directories before files;
                                   can be augmented with a --sort option, but any
                                   use of --sort=none (-U) disables grouping
      -G, --no-group             in a long listing, don't print group names
      -h, --human-readable       with -l and -s, print sizes like 1K 234M 2G etc.
          --si                   likewise, but use powers of 1000 not 1024
      -H, --dereference-command-line
                                 follow symbolic links listed on the command line
          --dereference-command-line-symlink-to-dir
                                 follow each command line symbolic link
                                   that points to a directory
          --hide=PATTERN         do not list implied entries matching shell PATTERN
                                   (overridden by -a or -A)
          --hyperlink[=WHEN]     hyperlink file names; WHEN can be 'always'
                                   (default if omitted), 'auto', or 'never'
          --indicator-style=WORD  append indicator with style WORD to entry names:
                                   none (default), slash (-p),
                                   file-type (--file-type), classify (-F)
      -i, --inode                print the index number of each file
      -I, --ignore=PATTERN       do not list implied entries matching shell PATTERN
      -k, --kibibytes            default to 1024-byte blocks for disk usage;
                                   used only with -s and per directory totals
      -l                         use a long listing format
      -L, --dereference          when showing file information for a symbolic
                                   link, show information for the file the link
                                   references rather than for the link itself
      -m                         fill width with a comma separated list of entries
      -n, --numeric-uid-gid      like -l, but list numeric user and group IDs
      -N, --literal              print entry names without quoting
      -o                         like -l, but do not list group information
      -p, --indicator-style=slash
                                 append / indicator to directories
      -q, --hide-control-chars   print ? instead of nongraphic characters
          --show-control-chars   show nongraphic characters as-is (the default,
                                   unless program is 'ls' and output is a terminal)
      -Q, --quote-name           enclose entry names in double quotes
          --quoting-style=WORD   use quoting style WORD for entry names:
                                   literal, locale, shell, shell-always,
                                   shell-escape, shell-escape-always, c, escape
                                   (overrides QUOTING_STYLE environment variable)
      -r, --reverse              reverse order while sorting
      -R, --recursive            list subdirectories recursively
      -s, --size                 print the allocated size of each file, in blocks
      -S                         sort by file size, largest first
          --sort=WORD            sort by WORD instead of name: none (-U), size (-S),
                                   time (-t), version (-v), extension (-X)
          --time=WORD            change the default of using modification times;
                                   access time (-u): atime, access, use;
                                   change time (-c): ctime, status;
                                   birth time: birth, creation;
                                 with -l, WORD determines which time to show;
                                 with --sort=time, sort by WORD (newest first)
          --time-style=TIME_STYLE  time/date format with -l; see TIME_STYLE below
      -t                         sort by time, newest first; see --time
      -T, --tabsize=COLS         assume tab stops at each COLS instead of 8
      -u                         with -lt: sort by, and show, access time;
                                   with -l: show access time and sort by name;
                                   otherwise: sort by access time, newest first
      -U                         do not sort; list entries in directory order
      -v                         natural sort of (version) numbers within text
      -w, --width=COLS           set output width to COLS.  0 means no limit
      -x                         list entries by lines instead of by columns
      -X                         sort alphabetically by entry extension
      -Z, --context              print any security context of each file
      -1                         list one file per line.  Avoid '\n' with -q or -b
          --help     display this help and exit
          --version  output version information and exit

    The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
    Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).
    Binary prefixes can be used, too: KiB=K, MiB=M, and so on.

    The TIME_STYLE argument can be full-iso, long-iso, iso, locale, or +FORMAT.
    FORMAT is interpreted like in date(1).  If FORMAT is FORMAT1<newline>FORMAT2,
    then FORMAT1 applies to non-recent files and FORMAT2 to recent files.
    TIME_STYLE prefixed with 'posix-' takes effect only outside the POSIX locale.
    Also the TIME_STYLE environment variable sets the default style to use.

    Using color to distinguish file types is disabled both by default and
    with --color=never.  With --color=auto, ls emits color codes only when
    standard output is connected to a terminal.  The LS_COLORS environment
    variable can change the settings.  Use the dircolors command to set it.

    Exit status:
     0  if OK,
     1  if minor problems (e.g., cannot access subdirectory),
     2  if serious trouble (e.g., cannot access command-line argument).

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/ls>
    or available locally via: info '(coreutils) ls invocation'

### [md5sum]

Compute and check MD5 message digest.

`user `[`$`]`md5sum --help`

    Usage: md5sum [OPTION]... [FILE]...
    Print or check MD5 (128-bit) checksums.

    With no FILE, or when FILE is -, read standard input.

      -b, --binary         read in binary mode
      -c, --check          read MD5 sums from the FILEs and check them
          --tag            create a BSD-style checksum
      -t, --text           read in text mode (default)
      -z, --zero           end each output line with NUL, not newline,
                           and disable file name escaping

    The following five options are useful only when verifying checksums:
          --ignore-missing  don't fail or report status for missing files
          --quiet          don't print OK for each successfully verified file
          --status         don't output anything, status code shows success
          --strict         exit non-zero for improperly formatted checksum lines
      -w, --warn           warn about improperly formatted checksum lines

          --help     display this help and exit
          --version  output version information and exit

    The sums are computed as described in RFC 1321.  When checking, the input
    should be a former output of this program.  The default mode is to print a
    line with checksum, a space, a character indicating input mode ('*' for binary,
    ' ' for text or where binary is insignificant), and name for each FILE.

    Note: There is no difference between binary mode and text mode on GNU systems.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/md5sum>
    or available locally via: info '(coreutils) md5sum invocation'

### [mkdir]

Make directories.

`user `[`$`]`mkdir --help`

    Usage: mkdir [OPTION]... DIRECTORY...
    Create the DIRECTORY(ies), if they do not already exist.

    Mandatory arguments to long options are mandatory for short options too.
      -m, --mode=MODE   set file mode (as in chmod), not a=rwx - umask
      -p, --parents     no error if existing, make parent directories as needed
      -v, --verbose     print a message for each created directory
      -Z                   set SELinux security context of each created directory
                             to the default type
          --context[=CTX]  like -Z, or if CTX is specified then set the SELinux
                             or SMACK security context to CTX
          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/mkdir>
    or available locally via: info '(coreutils) mkdir invocation'

### [mkfifo]

Make FIFOs (named pipes).

`user `[`$`]`mkfifo --help`

    Usage: mkfifo [OPTION]... NAME...
    Create named pipes (FIFOs) with the given NAMEs.

    Mandatory arguments to long options are mandatory for short options too.
      -m, --mode=MODE    set file permission bits to MODE, not a=rw - umask
      -Z                   set the SELinux security context to default type
          --context[=CTX]  like -Z, or if CTX is specified then set the SELinux
                             or SMACK security context to CTX
          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/mkfifo>
    or available locally via: info '(coreutils) mkfifo invocation'

### [mknod]

Make block or character special files.

`user `[`$`]`mknod --help`

    Usage: mknod [OPTION]... NAME TYPE [MAJOR MINOR]
    Create the special file NAME of the given TYPE.

    Mandatory arguments to long options are mandatory for short options too.
      -m, --mode=MODE    set file permission bits to MODE, not a=rw - umask
      -Z                   set the SELinux security context to default type
          --context[=CTX]  like -Z, or if CTX is specified then set the SELinux
                             or SMACK security context to CTX
          --help     display this help and exit
          --version  output version information and exit

    Both MAJOR and MINOR must be specified when TYPE is b, c, or u, and they
    must be omitted when TYPE is p.  If MAJOR or MINOR begins with 0x or 0X,
    it is interpreted as hexadecimal; otherwise, if it begins with 0, as octal;
    otherwise, as decimal.  TYPE may be:

      b      create a block (buffered) special file
      c, u   create a character (unbuffered) special file
      p      create a FIFO

    NOTE: your shell may have its own version of mknod, which usually supersedes
    the version described here.  Please refer to your shell's documentation
    for details about the options it supports.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/mknod>
    or available locally via: info '(coreutils) mknod invocation'

### [mktemp]

Create a temporary file or directory.

`user `[`$`]`mktemp --help`

    Usage: mktemp [OPTION]... [TEMPLATE]
    Create a temporary file or directory, safely, and print its name.
    TEMPLATE must contain at least 3 consecutive 'X's in last component.
    If TEMPLATE is not specified, use tmp.XXXXXXXXXX, and --tmpdir is implied.
    Files are created u+rw, and directories u+rwx, minus umask restrictions.

      -d, --directory     create a directory, not a file
      -u, --dry-run       do not create anything; merely print a name (unsafe)
      -q, --quiet         suppress diagnostics about file/dir-creation failure
          --suffix=SUFF   append SUFF to TEMPLATE; SUFF must not contain a slash.
                            This option is implied if TEMPLATE does not end in X
      -p DIR, --tmpdir[=DIR]  interpret TEMPLATE relative to DIR; if DIR is not
                            specified, use $TMPDIR if set, else /tmp.  With
                            this option, TEMPLATE must not be an absolute name;
                            unlike with -t, TEMPLATE may contain slashes, but
                            mktemp creates only the final component
      -t                  interpret TEMPLATE as a single file name component,
                            relative to a directory: $TMPDIR, if set; else the
                            directory specified via -p; else /tmp [deprecated]
          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/mktemp>
    or available locally via: info '(coreutils) mktemp invocation'

### [mv]

Move (rename) files.

`user `[`$`]`mv --help`

    Usage: mv [OPTION]... [-T] SOURCE DEST
      or:  mv [OPTION]... SOURCE... DIRECTORY
      or:  mv [OPTION]... -t DIRECTORY SOURCE...
    Rename SOURCE to DEST, or move SOURCE(s) to DIRECTORY.

    Mandatory arguments to long options are mandatory for short options too.
          --backup[=CONTROL]       make a backup of each existing destination file
      -b                           like --backup but does not accept an argument
      -f, --force                  do not prompt before overwriting
      -i, --interactive            prompt before overwrite
      -n, --no-clobber             do not overwrite an existing file
    If you specify more than one of -i, -f, -n, only the final one takes effect.
          --strip-trailing-slashes  remove any trailing slashes from each SOURCE
                                     argument
      -S, --suffix=SUFFIX          override the usual backup suffix
      -t, --target-directory=DIRECTORY  move all SOURCE arguments into DIRECTORY
      -T, --no-target-directory    treat DEST as a normal file
      -u, --update                 move only when the SOURCE file is newer
                                     than the destination file or when the
                                     destination file is missing
      -v, --verbose                explain what is being done
      -Z, --context                set SELinux security context of destination
                                     file to default type
          --help     display this help and exit
          --version  output version information and exit

    The backup suffix is '~', unless set with --suffix or SIMPLE_BACKUP_SUFFIX.
    The version control method may be selected via the --backup option or through
    the VERSION_CONTROL environment variable.  Here are the values:

      none, off       never make backups (even if --backup is given)
      numbered, t     make numbered backups
      existing, nil   numbered if numbered backups exist, simple otherwise
      simple, never   always make simple backups

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/mv>
    or available locally via: info '(coreutils) mv invocation'

### [nice]

Run a program with modified scheduling priority.

`user `[`$`]`nice --help`

    Usage: nice [OPTION] [COMMAND [ARG]...]
    Run COMMAND with an adjusted niceness, which affects process scheduling.
    With no COMMAND, print the current niceness.  Niceness values range from
    -20 (most favorable to the process) to 19 (least favorable to the process).

    Mandatory arguments to long options are mandatory for short options too.
      -n, --adjustment=N   add integer N to the niceness (default 10)
          --help     display this help and exit
          --version  output version information and exit

    NOTE: your shell may have its own version of nice, which usually supersedes
    the version described here.  Please refer to your shell's documentation
    for details about the options it supports.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/nice>
    or available locally via: info '(coreutils) nice invocation'

### [nl]

Number lines of files.

`user `[`$`]`nl --help`

    Usage: nl [OPTION]... [FILE]...
    Write each FILE to standard output, with line numbers added.

    With no FILE, or when FILE is -, read standard input.

    Mandatory arguments to long options are mandatory for short options too.
      -b, --body-numbering=STYLE      use STYLE for numbering body lines
      -d, --section-delimiter=CC      use CC for logical page delimiters
      -f, --footer-numbering=STYLE    use STYLE for numbering footer lines
      -h, --header-numbering=STYLE    use STYLE for numbering header lines
      -i, --line-increment=NUMBER     line number increment at each line
      -l, --join-blank-lines=NUMBER   group of NUMBER empty lines counted as one
      -n, --number-format=FORMAT      insert line numbers according to FORMAT
      -p, --no-renumber               do not reset line numbers for each section
      -s, --number-separator=STRING   add STRING after (possible) line number
      -v, --starting-line-number=NUMBER  first line number for each section
      -w, --number-width=NUMBER       use NUMBER columns for line numbers
          --help     display this help and exit
          --version  output version information and exit

    Default options are: -bt -d'\:' -fn -hn -i1 -l1 -n'rn' -s<TAB> -v1 -w6

    CC are two delimiter characters used to construct logical page delimiters;
    a missing second character implies ':'.

    STYLE is one of:

      a      number all lines
      t      number only nonempty lines
      n      number no lines
      pBRE   number only lines that contain a match for the basic regular
             expression, BRE

    FORMAT is one of:

      ln     left justified, no leading zeros
      rn     right justified, no leading zeros
      rz     right justified, leading zeros

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/nl>
    or available locally via: info '(coreutils) nl invocation'

### [nohup]

Run a command immune to hangups, with output to a non-tty.

`user `[`$`]`nohup --help`

    Usage: nohup COMMAND [ARG]...
      or:  nohup OPTION
    Run COMMAND, ignoring hangup signals.

          --help     display this help and exit
          --version  output version information and exit

    If standard input is a terminal, redirect it from an unreadable file.
    If standard output is a terminal, append output to 'nohup.out' if possible,
    '$HOME/nohup.out' otherwise.
    If standard error is a terminal, redirect it to standard output.
    To save output to FILE, use 'nohup COMMAND > FILE'.

    NOTE: your shell may have its own version of nohup, which usually supersedes
    the version described here.  Please refer to your shell's documentation
    for details about the options it supports.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/nohup>
    or available locally via: info '(coreutils) nohup invocation'

### [nproc]

Print the number of processing units available.

`user `[`$`]`nproc --help`

    Usage: nproc [OPTION]...
    Print the number of processing units available to the current process,
    which may be less than the number of online processors

          --all      print the number of installed processors
          --ignore=N  if possible, exclude N processing units
          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/nproc>
    or available locally via: info '(coreutils) nproc invocation'

### [numfmt]

Convert numbers from/to human-readable strings.

`user `[`$`]`numfmt --help`

    Usage: numfmt [OPTION]... [NUMBER]...
    Reformat NUMBER(s), or the numbers from standard input if none are specified.

    Mandatory arguments to long options are mandatory for short options too.
          --debug          print warnings about invalid input
      -d, --delimiter=X    use X instead of whitespace for field delimiter
          --field=FIELDS   replace the numbers in these input fields (default=1)
                             see FIELDS below
          --format=FORMAT  use printf style floating-point FORMAT;
                             see FORMAT below for details
          --from=UNIT      auto-scale input numbers to UNITs; default is 'none';
                             see UNIT below
          --from-unit=N    specify the input unit size (instead of the default 1)
          --grouping       use locale-defined grouping of digits, e.g. 1,000,000
                             (which means it has no effect in the C/POSIX locale)
          --header[=N]     print (without converting) the first N header lines;
                             N defaults to 1 if not specified
          --invalid=MODE   failure mode for invalid numbers: MODE can be:
                             abort (default), fail, warn, ignore
          --padding=N      pad the output to N characters; positive N will
                             right-align; negative N will left-align;
                             padding is ignored if the output is wider than N;
                             the default is to automatically pad if a whitespace
                             is found
          --round=METHOD   use METHOD for rounding when scaling; METHOD can be:
                             up, down, from-zero (default), towards-zero, nearest
          --suffix=SUFFIX  add SUFFIX to output numbers, and accept optional
                             SUFFIX in input numbers
          --to=UNIT        auto-scale output numbers to UNITs; see UNIT below
          --to-unit=N      the output unit size (instead of the default 1)
      -z, --zero-terminated    line delimiter is NUL, not newline
          --help     display this help and exit
          --version  output version information and exit

    UNIT options:
      none       no auto-scaling is done; suffixes will trigger an error
      auto       accept optional single/two letter suffix:
                   1K = 1000,
                   1Ki = 1024,
                   1M = 1000000,
                   1Mi = 1048576,
      si         accept optional single letter suffix:
                   1K = 1000,
                   1M = 1000000,
                   ...
      iec        accept optional single letter suffix:
                   1K = 1024,
                   1M = 1048576,
                   ...
      iec-i      accept optional two-letter suffix:
                   1Ki = 1024,
                   1Mi = 1048576,
                   ...

    FIELDS supports cut(1) style field ranges:
      N    N'th field, counted from 1
      N-   from N'th field, to end of line
      N-M  from N'th to M'th field (inclusive)
      -M   from first to M'th field (inclusive)
      -    all fields
    Multiple fields/ranges can be separated with commas

    FORMAT must be suitable for printing one floating-point argument '%f'.
    Optional quote (%'f) will enable --grouping (if supported by current locale).
    Optional width value (%10f) will pad output. Optional zero (%010f) width
    will zero pad the number. Optional negative values (%-10f) will left align.
    Optional precision (%.1f) will override the input determined precision.

    Exit status is 0 if all input numbers were successfully converted.
    By default, numfmt will stop at the first conversion error with exit status 2.
    With --invalid='fail' a warning is printed for each conversion error
    and the exit status is 2.  With --invalid='warn' each conversion error is
    diagnosed, but the exit status is 0.  With --invalid='ignore' conversion
    errors are not diagnosed and the exit status is 0.

    Examples:
      $ numfmt --to=si 1000
                -> "1.0K"
      $ numfmt --to=iec 2048
               -> "2.0K"
      $ numfmt --to=iec-i 4096
               -> "4.0Ki"
      $ echo 1K | numfmt --from=si
               -> "1000"
      $ echo 1K | numfmt --from=iec
               -> "1024"
      $ df -B1 | numfmt --header --field 2-4 --to=si
      $ ls -l  | numfmt --header --field 5 --to=iec
      $ ls -lh | numfmt --header --field 5 --from=iec --padding=10
      $ ls -lh | numfmt --header --field 5 --from=iec --format %10f

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/numfmt>
    or available locally via: info '(coreutils) numfmt invocation'

### [od]

Dump files in octal and other formats.

`user `[`$`]`od --help`

    Usage: od [OPTION]... [FILE]...
      or:  od [-abcdfilosx]... [FILE] [[+]OFFSET[.][b]]
      or:  od --traditional [OPTION]... [FILE] [[+]OFFSET[.][b] [+][LABEL][.][b]]

    Write an unambiguous representation, octal bytes by default,
    of FILE to standard output.  With more than one FILE argument,
    concatenate them in the listed order to form the input.

    With no FILE, or when FILE is -, read standard input.

    If first and second call formats both apply, the second format is assumed
    if the last operand begins with + or (if there are 2 operands) a digit.
    An OFFSET operand means -j OFFSET.  LABEL is the pseudo-address
    at first byte printed, incremented when dump is progressing.
    For OFFSET and LABEL, a 0x or 0X prefix indicates hexadecimal;
    suffixes may be . for octal and b for multiply by 512.

    Mandatory arguments to long options are mandatory for short options too.
      -A, --address-radix=RADIX   output format for file offsets; RADIX is one
                                    of [doxn], for Decimal, Octal, Hex or None
          --endian=   swap input bytes according the specified order
      -j, --skip-bytes=BYTES      skip BYTES input bytes first
      -N, --read-bytes=BYTES      limit dump to BYTES input bytes
      -S BYTES, --strings[=BYTES]  output strings of at least BYTES graphic chars;
                                    3 is implied when BYTES is not specified
      -t, --format=TYPE           select output format or formats
      -v, --output-duplicates     do not use * to mark line suppression
      -w[BYTES], --width[=BYTES]  output BYTES bytes per output line;
                                    32 is implied when BYTES is not specified
          --traditional           accept arguments in third form above
          --help     display this help and exit
          --version  output version information and exit

    Traditional format specifications may be intermixed; they accumulate:
      -a   same as -t a,  select named characters, ignoring high-order bit
      -b   same as -t o1, select octal bytes
      -c   same as -t c,  select printable characters or backslash escapes
      -d   same as -t u2, select unsigned decimal 2-byte units
      -f   same as -t fF, select floats
      -i   same as -t dI, select decimal ints
      -l   same as -t dL, select decimal longs
      -o   same as -t o2, select octal 2-byte units
      -s   same as -t d2, select decimal 2-byte units
      -x   same as -t x2, select hexadecimal 2-byte units

    TYPE is made up of one or more of these specifications:
      a          named character, ignoring high-order bit
      c          printable character or backslash escape
      d[SIZE]    signed decimal, SIZE bytes per integer
      f[SIZE]    floating point, SIZE bytes per float
      o[SIZE]    octal, SIZE bytes per integer
      u[SIZE]    unsigned decimal, SIZE bytes per integer
      x[SIZE]    hexadecimal, SIZE bytes per integer

    SIZE is a number.  For TYPE in [doux], SIZE may also be C for
    sizeof(char), S for sizeof(short), I for sizeof(int) or L for
    sizeof(long).  If TYPE is f, SIZE may also be F for sizeof(float), D
    for sizeof(double) or L for sizeof(long double).

    Adding a z suffix to any type displays printable characters at the end of
    each output line.

    BYTES is hex with 0x or 0X prefix, and may have a multiplier suffix:
      b    512
      KB   1000
      K    1024
      MB   1000*1000
      M    1024*1024
    and so on for G, T, P, E, Z, Y.
    Binary prefixes can be used, too: KiB=K, MiB=M, and so on.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/od>
    or available locally via: info '(coreutils) od invocation'

### [paste]

Merge lines of files.

`user `[`$`]`paste --help`

    Usage: paste [OPTION]... [FILE]...
    Write lines consisting of the sequentially corresponding lines from
    each FILE, separated by TABs, to standard output.

    With no FILE, or when FILE is -, read standard input.

    Mandatory arguments to long options are mandatory for short options too.
      -d, --delimiters=LIST   reuse characters from LIST instead of TABs
      -s, --serial            paste one file at a time instead of in parallel
      -z, --zero-terminated    line delimiter is NUL, not newline
          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/paste>
    or available locally via: info '(coreutils) paste invocation'

### [pathchk]

Check whether file names are valid or portable.

`user `[`$`]`pathchk --help`

    Usage: pathchk [OPTION]... NAME...
    Diagnose invalid or unportable file names.

      -p                  check for most POSIX systems
      -P                  check for empty names and leading "-"
          --portability   check for all POSIX systems (equivalent to -p -P)
          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/pathchk>
    or available locally via: info '(coreutils) pathchk invocation'

### [pinky]

Lightweight finger. Print user informtion.

`user `[`$`]`pinky --help`

    Usage: pinky [OPTION]... [USER]...

      -l              produce long format output for the specified USERs
      -b              omit the user's home directory and shell in long format
      -h              omit the user's project file in long format
      -p              omit the user's plan file in long format
      -s              do short format output, this is the default
      -f              omit the line of column headings in short format
      -w              omit the user's full name in short format
      -i              omit the user's full name and remote host in short format
      -q              omit the user's full name, remote host and idle time
                      in short format
          --help     display this help and exit
          --version  output version information and exit

    A lightweight 'finger' program;  print user information.
    The utmp file will be /var/run/utmp.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/pinky>
    or available locally via: info '(coreutils) pinky invocation'

### [pr]

Convert text files for printing.

`user `[`$`]`pr --help`

    Usage: pr [OPTION]... [FILE]...
    Paginate or columnate FILE(s) for printing.

    With no FILE, or when FILE is -, read standard input.

    Mandatory arguments to long options are mandatory for short options too.
      +FIRST_PAGE[:LAST_PAGE], --pages=FIRST_PAGE[:LAST_PAGE]
                        begin [stop] printing with page FIRST_[LAST_]PAGE
      -COLUMN, --columns=COLUMN
                        output COLUMN columns and print columns down,
                        unless -a is used. Balance number of lines in the
                        columns on each page
      -a, --across      print columns across rather than down, used together
                        with -COLUMN
      -c, --show-control-chars
                        use hat notation (^G) and octal backslash notation
      -d, --double-space
                        double space the output
      -D, --date-format=FORMAT
                        use FORMAT for the header date
      -e[CHAR[WIDTH]], --expand-tabs[=CHAR[WIDTH]]
                        expand input CHARs (TABs) to tab WIDTH (8)
      -F, -f, --form-feed
                        use form feeds instead of newlines to separate pages
                        (by a 3-line page header with -F or a 5-line header
                        and trailer without -F)
      -h, --header=HEADER
                        use a centered HEADER instead of filename in page header,
                        -h "" prints a blank line, don't use -h""
      -i[CHAR[WIDTH]], --output-tabs[=CHAR[WIDTH]]
                        replace spaces with CHARs (TABs) to tab WIDTH (8)
      -J, --join-lines  merge full lines, turns off -W line truncation, no column
                        alignment, --sep-string[=STRING] sets separators
      -l, --length=PAGE_LENGTH
                        set the page length to PAGE_LENGTH (66) lines
                        (default number of lines of text 56, and with -F 63).
                        implies -t if PAGE_LENGTH <= 10
      -m, --merge       print all files in parallel, one in each column,
                        truncate lines, but join lines of full length with -J
      -n[SEP[DIGITS]], --number-lines[=SEP[DIGITS]]
                        number lines, use DIGITS (5) digits, then SEP (TAB),
                        default counting starts with 1st line of input file
      -N, --first-line-number=NUMBER
                        start counting with NUMBER at 1st line of first
                        page printed (see +FIRST_PAGE)
      -o, --indent=MARGIN
                        offset each line with MARGIN (zero) spaces, do not
                        affect -w or -W, MARGIN will be added to PAGE_WIDTH
      -r, --no-file-warnings
                        omit warning when a file cannot be opened
      -s[CHAR], --separator[=CHAR]
                        separate columns by a single character, default for CHAR
                        is the <TAB> character without -w and 'no char' with -w.
                        -s[CHAR] turns off line truncation of all 3 column
                        options (-COLUMN|-a -COLUMN|-m) except -w is set
      -S[STRING], --sep-string[=STRING]
                        separate columns by STRING,
                        without -S: Default separator <TAB> with -J and <space>
                        otherwise (same as -S" "), no effect on column options
      -t, --omit-header  omit page headers and trailers;
                         implied if PAGE_LENGTH <= 10
      -T, --omit-pagination
                        omit page headers and trailers, eliminate any pagination
                        by form feeds set in input files
      -v, --show-nonprinting
                        use octal backslash notation
      -w, --width=PAGE_WIDTH
                        set page width to PAGE_WIDTH (72) characters for
                        multiple text-column output only, -s[char] turns off (72)
      -W, --page-width=PAGE_WIDTH
                        set page width to PAGE_WIDTH (72) characters always,
                        truncate lines, except -J option is set, no interference
                        with -S or -s
          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/pr>
    or available locally via: info '(coreutils) pr invocation'

### [printenv]

Print all or part of environment.

`user `[`$`]`printenv --help`

    Usage: printenv [OPTION]... [VARIABLE]...
    Print the values of the specified environment VARIABLE(s).
    If no VARIABLE is specified, print name and value pairs for them all.

      -0, --null     end each output line with NUL, not newline
          --help     display this help and exit
          --version  output version information and exit

    NOTE: your shell may have its own version of printenv, which usually supersedes
    the version described here.  Please refer to your shell's documentation
    for details about the options it supports.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/printenv>
    or available locally via: info '(coreutils) printenv invocation'

### [printf]

Display text according to a format string.

`user `[`$`]`/usr/bin/printf --help`

    Usage: /usr/bin/printf FORMAT [ARGUMENT]...
      or:  /usr/bin/printf OPTION
    Print ARGUMENT(s) according to FORMAT, or execute according to OPTION:

          --help     display this help and exit
          --version  output version information and exit

    FORMAT controls the output as in C printf.  Interpreted sequences are:

      \"      double quote
      \\      backslash
      \a      alert (BEL)
      \b      backspace
      \c      produce no further output
      \e      escape
      \f      form feed
      \n      new line
      \r      carriage return
      \t      horizontal tab
      \v      vertical tab
      \NNN    byte with octal value NNN (1 to 3 digits)
      \xHH    byte with hexadecimal value HH (1 to 2 digits)
      \uHHHH  Unicode (ISO/IEC 10646) character with hex value HHHH (4 digits)
      \UHHHHHHHH  Unicode character with hex value HHHHHHHH (8 digits)
      %%      a single %
      %b      ARGUMENT as a string with '\' escapes interpreted,
              except that octal escapes are of the form \0 or \0NNN
      %q      ARGUMENT is printed in a format that can be reused as shell input,
              escaping non-printable characters with the proposed POSIX $'' syntax.

    and all C format specifications ending with one of diouxXfeEgGcs, with
    ARGUMENTs converted to proper type first.  Variable widths are handled.

    NOTE: your shell may have its own version of printf, which usually supersedes
    the version described here.  Please refer to your shell's documentation
    for details about the options it supports.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/printf>
    or available locally via: info '(coreutils) printf invocation'

n.b. Some shells have a [printf] command built in, which is why this needs the [/usr/bin] prefix to return the help text.

### [ptx]

Produce a permuted index of file contents.

`user `[`$`]`ptx --help`

    Usage: ptx [OPTION]... [INPUT]...   (without -G)
      or:  ptx -G [OPTION]... [INPUT [OUTPUT]]
    Output a permuted index, including context, of the words in the input files.

    With no FILE, or when FILE is -, read standard input.

    Mandatory arguments to long options are mandatory for short options too.
      -A, --auto-reference           output automatically generated references
      -G, --traditional              behave more like System V 'ptx'
      -F, --flag-truncation=STRING   use STRING for flagging line truncations.
                                     The default is '/'
      -M, --macro-name=STRING        macro name to use instead of 'xx'
      -O, --format=roff              generate output as roff directives
      -R, --right-side-refs          put references at right, not counted in -w
      -S, --sentence-regexp=REGEXP   for end of lines or end of sentences
      -T, --format=tex               generate output as TeX directives
      -W, --word-regexp=REGEXP       use REGEXP to match each keyword
      -b, --break-file=FILE          word break characters in this FILE
      -f, --ignore-case              fold lower case to upper case for sorting
      -g, --gap-size=NUMBER          gap size in columns between output fields
      -i, --ignore-file=FILE         read ignore word list from FILE
      -o, --only-file=FILE           read only word list from this FILE
      -r, --references               first field of each line is a reference
      -t, --typeset-mode               - not implemented -
      -w, --width=NUMBER             output width in columns, reference excluded
          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/ptx>
    or available locally via: info '(coreutils) ptx invocation'

### [pwd]

Output the current working directory.

`user `[`$`]`pwd --help`

    Usage: /bin/pwd [OPTION]...
    Print the full filename of the current working directory.

      -L, --logical   use PWD from environment, even if it contains symlinks
      -P, --physical  avoid all symlinks
          --help     display this help and exit
          --version  output version information and exit

    If no option is specified, -P is assumed.

    NOTE: your shell may have its own version of pwd, which usually supersedes
    the version described here.  Please refer to your shell's documentation
    for details about the options it supports.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/pwd>
    or available locally via: info '(coreutils) pwd invocation'

n.b. Some shells have a [pwd] builtin, which is why this needs the [/bin] prefix to return the help text.

### [readlink]

Print resolved symbolic links or canonical file names.

`user `[`$`]`readlink --help`

    Usage: readlink [OPTION]... FILE...
    Print value of a symbolic link or canonical file name

      -f, --canonicalize            canonicalize by following every symlink in
                                    every component of the given name recursively;
                                    all but the last component must exist
      -e, --canonicalize-existing   canonicalize by following every symlink in
                                    every component of the given name recursively,
                                    all components must exist
      -m, --canonicalize-missing    canonicalize by following every symlink in
                                    every component of the given name recursively,
                                    without requirements on components existence
      -n, --no-newline              do not output the trailing delimiter
      -q, --quiet
      -s, --silent                  suppress most error messages (on by default)
      -v, --verbose                 report error messages
      -z, --zero                    end each output line with NUL, not newline
          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/readlink>
    or available locally via: info '(coreutils) readlink invocation'

### [realpath]

Print the resolved path.

`user `[`$`]`realpath --help`

    Usage: realpath [OPTION]... FILE...
    Print the resolved absolute file name;
    all but the last component must exist

      -e, --canonicalize-existing  all components of the path must exist
      -m, --canonicalize-missing   no path components need exist or be a directory
      -L, --logical                resolve '..' components before symlinks
      -P, --physical               resolve symlinks as encountered (default)
      -q, --quiet                  suppress most error messages
          --relative-to=DIR        print the resolved path relative to DIR
          --relative-base=DIR      print absolute paths unless paths below DIR
      -s, --strip, --no-symlinks   don't expand symlinks
      -z, --zero                   end each output line with NUL, not newline

          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/realpath>
    or available locally via: info '(coreutils) realpath invocation'

### [rm]

Remove files or directories.

`user `[`$`]`rm --help`

    Usage: /bin/rm [OPTION]... [FILE]...
    Remove (unlink) the FILE(s).

      -f, --force           ignore nonexistent files and arguments, never prompt
      -i                    prompt before every removal
      -I                    prompt once before removing more than three files, or
                              when removing recursively; less intrusive than -i,
                              while still giving protection against most mistakes
          --interactive[=WHEN]  prompt according to WHEN: never, once (-I), or
                              always (-i); without WHEN, prompt always
          --one-file-system  when removing a hierarchy recursively, skip any
                              directory that is on a file system different from
                              that of the corresponding command line argument
          --no-preserve-root  do not treat '/' specially
          --preserve-root[=all]  do not remove '/' (default);
                                  with 'all', reject any command line argument
                                  on a separate device from its parent
      -r, -R, --recursive   remove directories and their contents recursively
      -d, --dir             remove empty directories
      -v, --verbose         explain what is being done
          --help     display this help and exit
          --version  output version information and exit

    By default, rm does not remove directories.  Use the --recursive (-r or -R)
    option to remove each listed directory, too, along with all of its contents.

    To remove a file whose name starts with a '-', for example '-foo',
    use one of these commands:
      /bin/rm -- -foo

      /bin/rm ./-foo

    Note that if you use rm to remove a file, it might be possible to recover
    some of its contents, given sufficient expertise and/or time.  For greater
    assurance that the contents are truly unrecoverable, consider using shred.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/rm>
    or available locally via: info '(coreutils) rm invocation'

** Warning**\
The [rm] command is irrevocable. The \--recursive option can induce massive data loss if used carelessly.

### [rmdir]

Remove empty directories.

`user `[`$`]`rmdir --help`

    Usage: rmdir [OPTION]... DIRECTORY...
    Remove the DIRECTORY(ies), if they are empty.

          --ignore-fail-on-non-empty
                      ignore each failure that is solely because a directory
                        is non-empty
      -p, --parents   remove DIRECTORY and its ancestors; e.g., 'rmdir -p a/b/c' is
                        similar to 'rmdir a/b/c a/b a'
      -v, --verbose   output a diagnostic for every directory processed
          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/rmdir>
    or available locally via: info '(coreutils) rmdir invocation'

### [runcon]

Run command with specified security context.

`user `[`$`]`runcon --help`

    Usage: runcon CONTEXT COMMAND [args]
      or:  runcon [ -c ] [-u USER] [-r ROLE] [-t TYPE] [-l RANGE] COMMAND [args]
    Run a program in a different SELinux security context.
    With neither CONTEXT nor COMMAND, print the current security context.

    Mandatory arguments to long options are mandatory for short options too.
      CONTEXT            Complete security context
      -c, --compute      compute process transition context before modifying
      -t, --type=TYPE    type (for same role as parent)
      -u, --user=USER    user identity
      -r, --role=ROLE    role
      -l, --range=RANGE  levelrange

          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/runcon>
    or available locally via: info '(coreutils) runcon invocation'

### [seq]

Print a sequence of numbers.

`user `[`$`]`seq --help`

    Usage: seq [OPTION]... LAST
      or:  seq [OPTION]... FIRST LAST
      or:  seq [OPTION]... FIRST INCREMENT LAST
    Print numbers from FIRST to LAST, in steps of INCREMENT.

    Mandatory arguments to long options are mandatory for short options too.
      -f, --format=FORMAT      use printf style floating-point FORMAT
      -s, --separator=STRING   use STRING to separate numbers (default: \n)
      -w, --equal-width        equalize width by padding with leading zeroes
          --help     display this help and exit
          --version  output version information and exit

    If FIRST or INCREMENT is omitted, it defaults to 1.  That is, an
    omitted INCREMENT defaults to 1 even when LAST is smaller than FIRST.
    The sequence of numbers ends when the sum of the current number and
    INCREMENT would become greater than LAST.
    FIRST, INCREMENT, and LAST are interpreted as floating point values.
    INCREMENT is usually positive if FIRST is smaller than LAST, and
    INCREMENT is usually negative if FIRST is greater than LAST.
    INCREMENT must not be 0; none of FIRST, INCREMENT and LAST may be NaN.
    FORMAT must be suitable for printing one argument of type 'double';
    it defaults to %.PRECf if FIRST, INCREMENT, and LAST are all fixed point
    decimal numbers with maximum precision PREC, and to %g otherwise.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/seq>
    or available locally via: info '(coreutils) seq invocation'

### [sha1sum]

Compute and check SHA1 message digest.

`user `[`$`]`sha1sum --help`

    Usage: sha1sum [OPTION]... [FILE]...
    Print or check SHA1 (160-bit) checksums.

    With no FILE, or when FILE is -, read standard input.

      -b, --binary         read in binary mode
      -c, --check          read SHA1 sums from the FILEs and check them
          --tag            create a BSD-style checksum
      -t, --text           read in text mode (default)
      -z, --zero           end each output line with NUL, not newline,
                           and disable file name escaping

    The following five options are useful only when verifying checksums:
          --ignore-missing  don't fail or report status for missing files
          --quiet          don't print OK for each successfully verified file
          --status         don't output anything, status code shows success
          --strict         exit non-zero for improperly formatted checksum lines
      -w, --warn           warn about improperly formatted checksum lines

          --help     display this help and exit
          --version  output version information and exit

    The sums are computed as described in FIPS-180-1.  When checking, the input
    should be a former output of this program.  The default mode is to print a
    line with checksum, a space, a character indicating input mode ('*' for binary,
    ' ' for text or where binary is insignificant), and name for each FILE.

    Note: There is no difference between binary mode and text mode on GNU systems.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/sha1sum>
    or available locally via: info '(coreutils) sha1sum invocation'

### [sha224sum]

Compute and check SHA224 message digest.

`user `[`$`]`sha224sum --help`

    Usage: sha224sum [OPTION]... [FILE]...
    Print or check SHA224 (224-bit) checksums.

    With no FILE, or when FILE is -, read standard input.

      -b, --binary         read in binary mode
      -c, --check          read SHA224 sums from the FILEs and check them
          --tag            create a BSD-style checksum
      -t, --text           read in text mode (default)
      -z, --zero           end each output line with NUL, not newline,
                           and disable file name escaping

    The following five options are useful only when verifying checksums:
          --ignore-missing  don't fail or report status for missing files
          --quiet          don't print OK for each successfully verified file
          --status         don't output anything, status code shows success
          --strict         exit non-zero for improperly formatted checksum lines
      -w, --warn           warn about improperly formatted checksum lines

          --help     display this help and exit
          --version  output version information and exit

    The sums are computed as described in RFC 3874.  When checking, the input
    should be a former output of this program.  The default mode is to print a
    line with checksum, a space, a character indicating input mode ('*' for binary,
    ' ' for text or where binary is insignificant), and name for each FILE.

    Note: There is no difference between binary mode and text mode on GNU systems.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/sha224sum>
    or available locally via: info '(coreutils) sha2 utilities'

### [sha256sum]

Compute and check SHA256 message digest.

`user `[`$`]`sha256sum --help`

    Usage: sha256sum [OPTION]... [FILE]...
    Print or check SHA256 (256-bit) checksums.

    With no FILE, or when FILE is -, read standard input.

      -b, --binary         read in binary mode
      -c, --check          read SHA256 sums from the FILEs and check them
          --tag            create a BSD-style checksum
      -t, --text           read in text mode (default)
      -z, --zero           end each output line with NUL, not newline,
                           and disable file name escaping

    The following five options are useful only when verifying checksums:
          --ignore-missing  don't fail or report status for missing files
          --quiet          don't print OK for each successfully verified file
          --status         don't output anything, status code shows success
          --strict         exit non-zero for improperly formatted checksum lines
      -w, --warn           warn about improperly formatted checksum lines

          --help     display this help and exit
          --version  output version information and exit

    The sums are computed as described in FIPS-180-2.  When checking, the input
    should be a former output of this program.  The default mode is to print a
    line with checksum, a space, a character indicating input mode ('*' for binary,
    ' ' for text or where binary is insignificant), and name for each FILE.

    Note: There is no difference between binary mode and text mode on GNU systems.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/sha256sum>
    or available locally via: info '(coreutils) sha2 utilities'

### [sha384sum]

Compute and check SHA384 message digest.

`user `[`$`]`sha384sum --help`

    Usage: sha384sum [OPTION]... [FILE]...
    Print or check SHA384 (384-bit) checksums.

    With no FILE, or when FILE is -, read standard input.

      -b, --binary         read in binary mode
      -c, --check          read SHA384 sums from the FILEs and check them
          --tag            create a BSD-style checksum
      -t, --text           read in text mode (default)
      -z, --zero           end each output line with NUL, not newline,
                           and disable file name escaping

    The following five options are useful only when verifying checksums:
          --ignore-missing  don't fail or report status for missing files
          --quiet          don't print OK for each successfully verified file
          --status         don't output anything, status code shows success
          --strict         exit non-zero for improperly formatted checksum lines
      -w, --warn           warn about improperly formatted checksum lines

          --help     display this help and exit
          --version  output version information and exit

    The sums are computed as described in FIPS-180-2.  When checking, the input
    should be a former output of this program.  The default mode is to print a
    line with checksum, a space, a character indicating input mode ('*' for binary,
    ' ' for text or where binary is insignificant), and name for each FILE.

    Note: There is no difference between binary mode and text mode on GNU systems.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/sha384sum>
    or available locally via: info '(coreutils) sha2 utilities'

### [sha512sum]

Compute and check SHA512 message digest.

`user `[`$`]`sha512sum --help`

    Usage: sha512sum [OPTION]... [FILE]...
    Print or check SHA512 (512-bit) checksums.

    With no FILE, or when FILE is -, read standard input.

      -b, --binary         read in binary mode
      -c, --check          read SHA512 sums from the FILEs and check them
          --tag            create a BSD-style checksum
      -t, --text           read in text mode (default)
      -z, --zero           end each output line with NUL, not newline,
                           and disable file name escaping

    The following five options are useful only when verifying checksums:
          --ignore-missing  don't fail or report status for missing files
          --quiet          don't print OK for each successfully verified file
          --status         don't output anything, status code shows success
          --strict         exit non-zero for improperly formatted checksum lines
      -w, --warn           warn about improperly formatted checksum lines

          --help     display this help and exit
          --version  output version information and exit

    The sums are computed as described in FIPS-180-2.  When checking, the input
    should be a former output of this program.  The default mode is to print a
    line with checksum, a space, a character indicating input mode ('*' for binary,
    ' ' for text or where binary is insignificant), and name for each FILE.

    Note: There is no difference between binary mode and text mode on GNU systems.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/sha512sum>
    or available locally via: info '(coreutils) sha2 utilities'

### [shred]

Overwrite a file to hide its contents, and optionally delete it.

`user `[`$`]`shred --help`

    Usage: shred [OPTION]... FILE...
    Overwrite the specified FILE(s) repeatedly, in order to make it harder
    for even very expensive hardware probing to recover the data.

    If FILE is -, shred standard output.

    Mandatory arguments to long options are mandatory for short options too.
      -f, --force    change permissions to allow writing if necessary
      -n, --iterations=N  overwrite N times instead of the default (3)
          --random-source=FILE  get random bytes from FILE
      -s, --size=N   shred this many bytes (suffixes like K, M, G accepted)
      -u             deallocate and remove file after overwriting
          --remove[=HOW]  like -u but give control on HOW to delete;  See below
      -v, --verbose  show progress
      -x, --exact    do not round file sizes up to the next full block;
                       this is the default for non-regular files
      -z, --zero     add a final overwrite with zeros to hide shredding
          --help     display this help and exit
          --version  output version information and exit

    Delete FILE(s) if --remove (-u) is specified.  The default is not to remove
    the files because it is common to operate on device files like /dev/hda,
    and those files usually should not be removed.
    The optional HOW parameter indicates how to remove a directory entry:
    'unlink' => use a standard unlink call.
    'wipe' => also first obfuscate bytes in the name.
    'wipesync' => also sync each obfuscated byte to disk.
    The default mode is 'wipesync', but note it can be expensive.

    CAUTION: shred assumes the file system and hardware overwrite data in place.
    Although this is common, many platforms operate otherwise.  Also, backups
    and mirrors may contain unremovable copies that will let a shredded file
    be recovered later.  See the GNU coreutils manual for details.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/shred>
    or available locally via: info '(coreutils) shred invocation'

** Warning**\
Of course the [shred] command will result in permanent data loss - by design.

### [shuf]

Generate random permutations.

`user `[`$`]`shuf --help`

    Usage: shuf [OPTION]... [FILE]
      or:  shuf -e [OPTION]... [ARG]...
      or:  shuf -i LO-HI [OPTION]...
    Write a random permutation of the input lines to standard output.

    With no FILE, or when FILE is -, read standard input.

    Mandatory arguments to long options are mandatory for short options too.
      -e, --echo                treat each ARG as an input line
      -i, --input-range=LO-HI   treat each number LO through HI as an input line
      -n, --head-count=COUNT    output at most COUNT lines
      -o, --output=FILE         write result to FILE instead of standard output
          --random-source=FILE  get random bytes from FILE
      -r, --repeat              output lines can be repeated
      -z, --zero-terminated     line delimiter is NUL, not newline
          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/shuf>
    or available locally via: info '(coreutils) shuf invocation'

### [sleep]

Delay for a specified amount of time.

`user `[`$`]`sleep --help`

    Usage: sleep NUMBER[SUFFIX]...
      or:  sleep OPTION
    Pause for NUMBER seconds.  SUFFIX may be 's' for seconds (the default),
    'm' for minutes, 'h' for hours or 'd' for days.  NUMBER need not be an
    integer.  Given two or more arguments, pause for the amount of time
    specified by the sum of their values.

          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/sleep>
    or available locally via: info '(coreutils) sleep invocation'

### [sort]

Sort lines of text files.

`user `[`$`]`sort --help`

    Usage: sort [OPTION]... [FILE]...
      or:  sort [OPTION]... --files0-from=F
    Write sorted concatenation of all FILE(s) to standard output.

    With no FILE, or when FILE is -, read standard input.

    Mandatory arguments to long options are mandatory for short options too.
    Ordering options:

      -b, --ignore-leading-blanks  ignore leading blanks
      -d, --dictionary-order      consider only blanks and alphanumeric characters
      -f, --ignore-case           fold lower case to upper case characters
      -g, --general-numeric-sort  compare according to general numerical value
      -i, --ignore-nonprinting    consider only printable characters
      -M, --month-sort            compare (unknown) < 'JAN' < ... < 'DEC'
      -h, --human-numeric-sort    compare human readable numbers (e.g., 2K 1G)
      -n, --numeric-sort          compare according to string numerical value
      -R, --random-sort           shuffle, but group identical keys.  See shuf(1)
          --random-source=FILE    get random bytes from FILE
      -r, --reverse               reverse the result of comparisons
          --sort=WORD             sort according to WORD:
                                    general-numeric -g, human-numeric -h, month -M,
                                    numeric -n, random -R, version -V
      -V, --version-sort          natural sort of (version) numbers within text

    Other options:

          --batch-size=NMERGE   merge at most NMERGE inputs at once;
                                for more use temp files
      -c, --check, --check=diagnose-first  check for sorted input; do not sort
      -C, --check=quiet, --check=silent  like -c, but do not report first bad line
          --compress-program=PROG  compress temporaries with PROG;
                                  decompress them with PROG -d
          --debug               annotate the part of the line used to sort,
                                  and warn about questionable usage to stderr
          --files0-from=F       read input from the files specified by
                                NUL-terminated names in file F;
                                If F is - then read names from standard input
      -k, --key=KEYDEF          sort via a key; KEYDEF gives location and type
      -m, --merge               merge already sorted files; do not sort
      -o, --output=FILE         write result to FILE instead of standard output
      -s, --stable              stabilize sort by disabling last-resort comparison
      -S, --buffer-size=SIZE    use SIZE for main memory buffer
      -t, --field-separator=SEP  use SEP instead of non-blank to blank transition
      -T, --temporary-directory=DIR  use DIR for temporaries, not $TMPDIR or /tmp;
                                  multiple options specify multiple directories
          --parallel=N          change the number of sorts run concurrently to N
      -u, --unique              with -c, check for strict ordering;
                                  without -c, output only the first of an equal run
      -z, --zero-terminated     line delimiter is NUL, not newline
          --help     display this help and exit
          --version  output version information and exit

    KEYDEF is F[.C][OPTS][,F[.C][OPTS]] for start and stop position, where F is a
    field number and C a character position in the field; both are origin 1, and
    the stop position defaults to the line's end.  If neither -t nor -b is in
    effect, characters in a field are counted from the beginning of the preceding
    whitespace.  OPTS is one or more single-letter ordering options [bdfgiMhnRrV],
    which override global ordering options for that key.  If no key is given, use
    the entire line as the key.  Use --debug to diagnose incorrect key usage.

    SIZE may be followed by the following multiplicative suffixes:
    % 1% of memory, b 1, K 1024 (default), and so on for M, G, T, P, E, Z, Y.

    *** WARNING ***
    The locale specified by the environment affects sort order.
    Set LC_ALL=C to get the traditional sort order that uses
    native byte values.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/sort>
    or available locally via: info '(coreutils) sort invocation'

### [split]

Split a file into pieces.

`user `[`$`]`split --help`

    Usage: split [OPTION]... [FILE [PREFIX]]
    Output pieces of FILE to PREFIXaa, PREFIXab, ...;
    default size is 1000 lines, and default PREFIX is 'x'.

    With no FILE, or when FILE is -, read standard input.

    Mandatory arguments to long options are mandatory for short options too.
      -a, --suffix-length=N   generate suffixes of length N (default 2)
          --additional-suffix=SUFFIX  append an additional SUFFIX to file names
      -b, --bytes=SIZE        put SIZE bytes per output file
      -C, --line-bytes=SIZE   put at most SIZE bytes of records per output file
      -d                      use numeric suffixes starting at 0, not alphabetic
          --numeric-suffixes[=FROM]  same as -d, but allow setting the start value
      -x                      use hex suffixes starting at 0, not alphabetic
          --hex-suffixes[=FROM]  same as -x, but allow setting the start value
      -e, --elide-empty-files  do not generate empty output files with '-n'
          --filter=COMMAND    write to shell COMMAND; file name is $FILE
      -l, --lines=NUMBER      put NUMBER lines/records per output file
      -n, --number=CHUNKS     generate CHUNKS output files; see explanation below
      -t, --separator=SEP     use SEP instead of newline as the record separator;
                                '\0' (zero) specifies the NUL character
      -u, --unbuffered        immediately copy input to output with '-n r/...'
          --verbose           print a diagnostic just before each
                                output file is opened
          --help     display this help and exit
          --version  output version information and exit

    The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
    Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).
    Binary prefixes can be used, too: KiB=K, MiB=M, and so on.

    CHUNKS may be:
      N       split into N files based on size of input
      K/N     output Kth of N to stdout
      l/N     split into N files without splitting lines/records
      l/K/N   output Kth of N to stdout without splitting lines/records
      r/N     like 'l' but use round robin distribution
      r/K/N   likewise but only output Kth of N to stdout

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/split>
    or available locally via: info '(coreutils) split invocation'

### [stat]

Display file or file system status.

`user `[`$`]`stat --help`

    Usage: stat [OPTION]... FILE...
    Display file or file system status.

    Mandatory arguments to long options are mandatory for short options too.
      -L, --dereference     follow links
      -f, --file-system     display file system status instead of file status
          --cached=MODE     specify how to use cached attributes;
                              useful on remote file systems. See MODE below
      -c  --format=FORMAT   use the specified FORMAT instead of the default;
                              output a newline after each use of FORMAT
          --printf=FORMAT   like --format, but interpret backslash escapes,
                              and do not output a mandatory trailing newline;
                              if you want a newline, include \n in FORMAT
      -t, --terse           print the information in terse form
          --help     display this help and exit
          --version  output version information and exit

    The --cached MODE argument can be; always, never, or default.
    `always` will use cached attributes if available, while
    `never` will try to synchronize with the latest attributes, and
    `default` will leave it up to the underlying file system.

    The valid format sequences for files (without --file-system):

      %a   permission bits in octal (note '#' and '0' printf flags)
      %A   permission bits and file type in human readable form
      %b   number of blocks allocated (see %B)
      %B   the size in bytes of each block reported by %b
      %C   SELinux security context string
      %d   device number in decimal
      %D   device number in hex
      %f   raw mode in hex
      %F   file type
      %g   group ID of owner
      %G   group name of owner
      %h   number of hard links
      %i   inode number
      %m   mount point
      %n   file name
      %N   quoted file name with dereference if symbolic link
      %o   optimal I/O transfer size hint
      %s   total size, in bytes
      %t   major device type in hex, for character/block device special files
      %T   minor device type in hex, for character/block device special files
      %u   user ID of owner
      %U   user name of owner
      %w   time of file birth, human-readable; - if unknown
      %W   time of file birth, seconds since Epoch; 0 if unknown
      %x   time of last access, human-readable
      %X   time of last access, seconds since Epoch
      %y   time of last data modification, human-readable
      %Y   time of last data modification, seconds since Epoch
      %z   time of last status change, human-readable
      %Z   time of last status change, seconds since Epoch

    Valid format sequences for file systems:

      %a   free blocks available to non-superuser
      %b   total data blocks in file system
      %c   total file nodes in file system
      %d   free file nodes in file system
      %f   free blocks in file system
      %i   file system ID in hex
      %l   maximum length of filenames
      %n   file name
      %s   block size (for faster transfers)
      %S   fundamental block size (for block counts)
      %t   file system type in hex
      %T   file system type in human readable form

    --terse is equivalent to the following FORMAT:
        %n %s %b %f %u %g %D %i %h %t %T %X %Y %Z %W %o
    --terse --file-system is equivalent to the following FORMAT:
        %n %i %l %t %s %S %b %f %a %c %d

    NOTE: your shell may have its own version of stat, which usually supersedes
    the version described here.  Please refer to your shell's documentation
    for details about the options it supports.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/stat>
    or available locally via: info '(coreutils) stat invocation'

### [stdbuf]

Run COMMAND, with modified buffering operations for its standard streams.

`user `[`$`]`stdbuf --help`

    Usage: stdbuf OPTION... COMMAND
    Run COMMAND, with modified buffering operations for its standard streams.

    Mandatory arguments to long options are mandatory for short options too.
      -i, --input=MODE   adjust standard input stream buffering
      -o, --output=MODE  adjust standard output stream buffering
      -e, --error=MODE   adjust standard error stream buffering
          --help     display this help and exit
          --version  output version information and exit

    If MODE is 'L' the corresponding stream will be line buffered.
    This option is invalid with standard input.

    If MODE is '0' the corresponding stream will be unbuffered.

    Otherwise MODE is a number which may be followed by one of the following:
    KB 1000, K 1024, MB 1000*1000, M 1024*1024, and so on for G, T, P, E, Z, Y.
    Binary prefixes can be used, too: KiB=K, MiB=M, and so on.
    In this case the corresponding stream will be fully buffered with the buffer
    size set to MODE bytes.

    NOTE: If COMMAND adjusts the buffering of its standard streams ('tee' does
    for example) then that will override corresponding changes by 'stdbuf'.
    Also some filters (like 'dd' and 'cat' etc.) don't use streams for I/O,
    and are thus unaffected by 'stdbuf' settings.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/stdbuf>
    or available locally via: info '(coreutils) stdbuf invocation'

### [stty]

Change and print terminal line settings.

`user `[`$`]`stty --help`

    Usage: stty [-F DEVICE | --file=DEVICE] [SETTING]...
      or:  stty [-F DEVICE | --file=DEVICE] [-a|--all]
      or:  stty [-F DEVICE | --file=DEVICE] [-g|--save]
    Print or change terminal characteristics.

    Mandatory arguments to long options are mandatory for short options too.
      -a, --all          print all current settings in human-readable form
      -g, --save         print all current settings in a stty-readable form
      -F, --file=DEVICE  open and use the specified DEVICE instead of stdin
          --help     display this help and exit
          --version  output version information and exit

    Optional - before SETTING indicates negation.  An * marks non-POSIX
    settings.  The underlying system defines which settings are available.

    Special characters:
     * discard CHAR  CHAR will toggle discarding of output
       eof CHAR      CHAR will send an end of file (terminate the input)
       eol CHAR      CHAR will end the line
     * eol2 CHAR     alternate CHAR for ending the line
       erase CHAR    CHAR will erase the last character typed
       intr CHAR     CHAR will send an interrupt signal
       kill CHAR     CHAR will erase the current line
     * lnext CHAR    CHAR will enter the next character quoted
       quit CHAR     CHAR will send a quit signal
     * rprnt CHAR    CHAR will redraw the current line
       start CHAR    CHAR will restart the output after stopping it
       stop CHAR     CHAR will stop the output
       susp CHAR     CHAR will send a terminal stop signal
     * swtch CHAR    CHAR will switch to a different shell layer
     * werase CHAR   CHAR will erase the last word typed

    Special settings:
       N             set the input and output speeds to N bauds
     * cols N        tell the kernel that the terminal has N columns
     * columns N     same as cols N
     * [-]drain      wait for transmission before applying settings (on by default)
       ispeed N      set the input speed to N
     * line N        use line discipline N
       min N         with -icanon, set N characters minimum for a completed read
       ospeed N      set the output speed to N
     * rows N        tell the kernel that the terminal has N rows
     * size          print the number of rows and columns according to the kernel
       speed         print the terminal speed
       time N        with -icanon, set read timeout of N tenths of a second

    Control settings:
       [-]clocal     disable modem control signals
       [-]cread      allow input to be received
     * [-]crtscts    enable RTS/CTS handshaking
       csN           set character size to N bits, N in [5..8]
       [-]cstopb     use two stop bits per character (one with '-')
       [-]hup        send a hangup signal when the last process closes the tty
       [-]hupcl      same as [-]hup
       [-]parenb     generate parity bit in output and expect parity bit in input
       [-]parodd     set odd parity (or even parity with '-')
     * [-]cmspar     use "stick" (mark/space) parity

    Input settings:
       [-]brkint     breaks cause an interrupt signal
       [-]icrnl      translate carriage return to newline
       [-]ignbrk     ignore break characters
       [-]igncr      ignore carriage return
       [-]ignpar     ignore characters with parity errors
     * [-]imaxbel    beep and do not flush a full input buffer on a character
       [-]inlcr      translate newline to carriage return
       [-]inpck      enable input parity checking
       [-]istrip     clear high (8th) bit of input characters
     * [-]iutf8      assume input characters are UTF-8 encoded
     * [-]iuclc      translate uppercase characters to lowercase
     * [-]ixany      let any character restart output, not only start character
       [-]ixoff      enable sending of start/stop characters
       [-]ixon       enable XON/XOFF flow control
       [-]parmrk     mark parity errors (with a 255-0-character sequence)
       [-]tandem     same as [-]ixoff

    Output settings:
     * bsN           backspace delay style, N in [0..1]
     * crN           carriage return delay style, N in [0..3]
     * ffN           form feed delay style, N in [0..1]
     * nlN           newline delay style, N in [0..1]
     * [-]ocrnl      translate carriage return to newline
     * [-]ofdel      use delete characters for fill instead of NUL characters
     * [-]ofill      use fill (padding) characters instead of timing for delays
     * [-]olcuc      translate lowercase characters to uppercase
     * [-]onlcr      translate newline to carriage return-newline
     * [-]onlret     newline performs a carriage return
     * [-]onocr      do not print carriage returns in the first column
       [-]opost      postprocess output
     * tabN          horizontal tab delay style, N in [0..3]
     * tabs          same as tab0
     * -tabs         same as tab3
     * vtN           vertical tab delay style, N in [0..1]

    Local settings:
       [-]crterase   echo erase characters as backspace-space-backspace
     * crtkill       kill all line by obeying the echoprt and echoe settings
     * -crtkill      kill all line by obeying the echoctl and echok settings
     * [-]ctlecho    echo control characters in hat notation ('^c')
       [-]echo       echo input characters
     * [-]echoctl    same as [-]ctlecho
       [-]echoe      same as [-]crterase
       [-]echok      echo a newline after a kill character
     * [-]echoke     same as [-]crtkill
       [-]echonl     echo newline even if not echoing other characters
     * [-]echoprt    echo erased characters backward, between '\' and '/'
     * [-]extproc    enable "LINEMODE"; useful with high latency links
     * [-]flusho     discard output
       [-]icanon     enable special characters: erase, kill, werase, rprnt
       [-]iexten     enable non-POSIX special characters
       [-]isig       enable interrupt, quit, and suspend special characters
       [-]noflsh     disable flushing after interrupt and quit special characters
     * [-]prterase   same as [-]echoprt
     * [-]tostop     stop background jobs that try to write to the terminal
     * [-]xcase      with icanon, escape with '\' for uppercase characters

    Combination settings:
     * [-]LCASE      same as [-]lcase
       cbreak        same as -icanon
       -cbreak       same as icanon
       cooked        same as brkint ignpar istrip icrnl ixon opost isig
                     icanon, eof and eol characters to their default values
       -cooked       same as raw
       crt           same as echoe echoctl echoke
       dec           same as echoe echoctl echoke -ixany intr ^c erase 0177
                     kill ^u
     * [-]decctlq    same as [-]ixany
       ek            erase and kill characters to their default values
       evenp         same as parenb -parodd cs7
       -evenp        same as -parenb cs8
     * [-]lcase      same as xcase iuclc olcuc
       litout        same as -parenb -istrip -opost cs8
       -litout       same as parenb istrip opost cs7
       nl            same as -icrnl -onlcr
       -nl           same as icrnl -inlcr -igncr onlcr -ocrnl -onlret
       oddp          same as parenb parodd cs7
       -oddp         same as -parenb cs8
       [-]parity     same as [-]evenp
       pass8         same as -parenb -istrip cs8
       -pass8        same as parenb istrip cs7
       raw           same as -ignbrk -brkint -ignpar -parmrk -inpck -istrip
                     -inlcr -igncr -icrnl -ixon -ixoff -icanon -opost
                     -isig -iuclc -ixany -imaxbel -xcase min 1 time 0
       -raw          same as cooked
       sane          same as cread -ignbrk brkint -inlcr -igncr icrnl
                     icanon iexten echo echoe echok -echonl -noflsh
                     -ixoff -iutf8 -iuclc -ixany imaxbel -xcase -olcuc -ocrnl
                     opost -ofill onlcr -onocr -onlret nl0 cr0 tab0 bs0 vt0 ff0
                     isig -tostop -ofdel -echoprt echoctl echoke -extproc -flusho,
                     all special characters to their default values

    Handle the tty line connected to standard input.  Without arguments,
    prints baud rate, line discipline, and deviations from stty sane.  In
    settings, CHAR is taken literally, or coded as in ^c, 0x37, 0177 or
    127; special values ^- or undef used to disable special characters.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/stty>
    or available locally via: info '(coreutils) stty invocation'

### [sum]

Checksum and count the blocks in a file.

`user `[`$`]`sum --help`

    Usage: sum [OPTION]... [FILE]...
    Print checksum and block counts for each FILE.

    With no FILE, or when FILE is -, read standard input.

      -r              use BSD sum algorithm, use 1K blocks
      -s, --sysv      use System V sum algorithm, use 512 bytes blocks
          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/sum>
    or available locally via: info '(coreutils) sum invocation'

### [sync]

Synchronize cached writes to persistent storage.

`user `[`$`]`sync --help`

    Usage: sync [OPTION] [FILE]...
    Synchronize cached writes to persistent storage

    If one or more files are specified, sync only them,
    or their containing file systems.

      -d, --data             sync only file data, no unneeded metadata
      -f, --file-system      sync the file systems that contain the files
          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/sync>
    or available locally via: info '(coreutils) sync invocation'

### [tac]

Concatenate and print files in reverse.

`user `[`$`]`tac --help`

    Usage: tac [OPTION]... [FILE]...
    Write each FILE to standard output, last line first.

    With no FILE, or when FILE is -, read standard input.

    Mandatory arguments to long options are mandatory for short options too.
      -b, --before             attach the separator before instead of after
      -r, --regex              interpret the separator as a regular expression
      -s, --separator=STRING   use STRING as the separator instead of newline
          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/tac>
    or available locally via: info '(coreutils) tac invocation'

### [tail]

Output the last part of files.

`user `[`$`]`tail --help`

    Usage: tail [OPTION]... [FILE]...
    Print the last 10 lines of each FILE to standard output.
    With more than one FILE, precede each with a header giving the file name.

    With no FILE, or when FILE is -, read standard input.

    Mandatory arguments to long options are mandatory for short options too.
      -c, --bytes=[+]NUM       output the last NUM bytes; or use -c +NUM to
                                 output starting with byte NUM of each file
      -f, --follow[=]
                               output appended data as the file grows;
                                 an absent option argument means 'descriptor'
      -F                       same as --follow=name --retry
      -n, --lines=[+]NUM       output the last NUM lines, instead of the last 10;
                                 or use -n +NUM to output starting with line NUM
          --max-unchanged-stats=N
                               with --follow=name, reopen a FILE which has not
                                 changed size after N (default 5) iterations
                                 to see if it has been unlinked or renamed
                                 (this is the usual case of rotated log files);
                                 with inotify, this option is rarely useful
          --pid=PID            with -f, terminate after process ID, PID dies
      -q, --quiet, --silent    never output headers giving file names
          --retry              keep trying to open a file if it is inaccessible
      -s, --sleep-interval=N   with -f, sleep for approximately N seconds
                                 (default 1.0) between iterations;
                                 with inotify and --pid=P, check process P at
                                 least once every N seconds
      -v, --verbose            always output headers giving file names
      -z, --zero-terminated    line delimiter is NUL, not newline
          --help     display this help and exit
          --version  output version information and exit

    NUM may have a multiplier suffix:
    b 512, kB 1000, K 1024, MB 1000*1000, M 1024*1024,
    GB 1000*1000*1000, G 1024*1024*1024, and so on for T, P, E, Z, Y.
    Binary prefixes can be used, too: KiB=K, MiB=M, and so on.

    With --follow (-f), tail defaults to following the file descriptor, which
    means that even if a tail'ed file is renamed, tail will continue to track
    its end.  This default behavior is not desirable when you really want to
    track the actual name of the file, not the file descriptor (e.g., log
    rotation).  Use --follow=name in that case.  That causes tail to track the
    named file in a way that accommodates renaming, removal and creation.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/tail>
    or available locally via: info '(coreutils) tail invocation'

### [tee]

Read from standard input and write to standard output and files.

`user `[`$`]`tee --help`

    Usage: tee [OPTION]... [FILE]...
    Copy standard input to each FILE, and also to standard output.

      -a, --append              append to the given FILEs, do not overwrite
      -i, --ignore-interrupts   ignore interrupt signals
      -p                        diagnose errors writing to non pipes
          --output-error[=MODE]   set behavior on write error.  See MODE below
          --help     display this help and exit
          --version  output version information and exit

    MODE determines behavior with write errors on the outputs:
      'warn'         diagnose errors writing to any output
      'warn-nopipe'  diagnose errors writing to any output not a pipe
      'exit'         exit on error writing to any output
      'exit-nopipe'  exit on error writing to any output not a pipe
    The default MODE for the -p option is 'warn-nopipe'.
    The default operation when --output-error is not specified, is to
    exit immediately on error writing to a pipe, and diagnose errors
    writing to non pipe outputs.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/tee>
    or available locally via: info '(coreutils) tee invocation'

### [test]

Perform tests on files and text.

[/usr/bin/test] command does not seem to have \--help option.

### [timeout]

Run a command with a time limit.

`user `[`$`]`timeout --help`

    Usage: timeout [OPTION] DURATION COMMAND [ARG]...
      or:  timeout [OPTION]
    Start COMMAND, and kill it if still running after DURATION.

    Mandatory arguments to long options are mandatory for short options too.
          --preserve-status
                     exit with the same status as COMMAND, even when the
                       command times out
          --foreground
                     when not running timeout directly from a shell prompt,
                       allow COMMAND to read from the TTY and get TTY signals;
                       in this mode, children of COMMAND will not be timed out
      -k, --kill-after=DURATION
                     also send a KILL signal if COMMAND is still running
                       this long after the initial signal was sent
      -s, --signal=SIGNAL
                     specify the signal to be sent on timeout;
                       SIGNAL may be a name like 'HUP' or a number;
                       see 'kill -l' for a list of signals
      -v, --verbose  diagnose to stderr any signal sent upon timeout
          --help     display this help and exit
          --version  output version information and exit

    DURATION is a floating point number with an optional suffix:
    's' for seconds (the default), 'm' for minutes, 'h' for hours or 'd' for days.
    A duration of 0 disables the associated timeout.

    If the command times out, and --preserve-status is not set, then exit with
    status 124.  Otherwise, exit with the status of COMMAND.  If no signal
    is specified, send the TERM signal upon timeout.  The TERM signal kills
    any process that does not block or catch that signal.  It may be necessary
    to use the KILL (9) signal, since this signal cannot be caught, in which
    case the exit status is 128+9 rather than 124.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/timeout>
    or available locally via: info '(coreutils) timeout invocation'

### [touch]

Change file timestamps.

`user `[`$`]`touch --help`

    Usage: touch [OPTION]... FILE...
    Update the access and modification times of each FILE to the current time.

    A FILE argument that does not exist is created empty, unless -c or -h
    is supplied.

    A FILE argument string of - is handled specially and causes touch to
    change the times of the file associated with standard output.

    Mandatory arguments to long options are mandatory for short options too.
      -a                     change only the access time
      -c, --no-create        do not create any files
      -d, --date=STRING      parse STRING and use it instead of current time
      -f                     (ignored)
      -h, --no-dereference   affect each symbolic link instead of any referenced
                             file (useful only on systems that can change the
                             timestamps of a symlink)
      -m                     change only the modification time
      -r, --reference=FILE   use this file's times instead of current time
      -t STAMP               use [[CC]YY]MMDDhhmm[.ss] instead of current time
          --time=WORD        change the specified time:
                               WORD is access, atime, or use: equivalent to -a
                               WORD is modify or mtime: equivalent to -m
          --help     display this help and exit
          --version  output version information and exit

    Note that the -d and -t options accept different time-date formats.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/touch>
    or available locally via: info '(coreutils) touch invocation'

### [tr]

Translate or delete characters.

`user `[`$`]`tr --help`

    Usage: tr [OPTION]... SET1 [SET2]
    Translate, squeeze, and/or delete characters from standard input,
    writing to standard output.

      -c, -C, --complement    use the complement of SET1
      -d, --delete            delete characters in SET1, do not translate
      -s, --squeeze-repeats   replace each sequence of a repeated character
                                that is listed in the last specified SET,
                                with a single occurrence of that character
      -t, --truncate-set1     first truncate SET1 to length of SET2
          --help     display this help and exit
          --version  output version information and exit

    SETs are specified as strings of characters.  Most represent themselves.
    Interpreted sequences are:

      \NNN            character with octal value NNN (1 to 3 octal digits)
      \\              backslash
      \a              audible BEL
      \b              backspace
      \f              form feed
      \n              new line
      \r              return
      \t              horizontal tab
      \v              vertical tab
      CHAR1-CHAR2     all characters from CHAR1 to CHAR2 in ascending order
      [CHAR*]         in SET2, copies of CHAR until length of SET1
      [CHAR*REPEAT]   REPEAT copies of CHAR, REPEAT octal if starting with 0
      [:alnum:]       all letters and digits
      [:alpha:]       all letters
      [:blank:]       all horizontal whitespace
      [:cntrl:]       all control characters
      [:digit:]       all digits
      [:graph:]       all printable characters, not including space
      [:lower:]       all lower case letters
      [:print:]       all printable characters, including space
      [:punct:]       all punctuation characters
      [:space:]       all horizontal or vertical whitespace
      [:upper:]       all upper case letters
      [:xdigit:]      all hexadecimal digits
      [=CHAR=]        all characters which are equivalent to CHAR

    Translation occurs if -d is not given and both SET1 and SET2 appear.
    -t may be used only when translating.  SET2 is extended to length of
    SET1 by repeating its last character as necessary.  Excess characters
    of SET2 are ignored.  Only [:lower:] and [:upper:] are guaranteed to
    expand in ascending order; used in SET2 while translating, they may
    only be used in pairs to specify case conversion.  -s uses the last
    specified SET, and occurs after translation or deletion.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/tr>
    or available locally via: info '(coreutils) tr invocation'

### [true]

Return a successful result.

`user `[`$`]`/bin/true --help`

    Usage: /bin/true [ignored command line arguments]
      or:  /bin/true OPTION
    Exit with a status code indicating success.

          --help     display this help and exit
          --version  output version information and exit

    NOTE: your shell may have its own version of true, which usually supersedes
    the version described here.  Please refer to your shell's documentation
    for details about the options it supports.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/true>
    or available locally via: info '(coreutils) true invocation'

n.b. Some shells have a [true] command built in, which is why this needs the [/bin] prefix to return the help text.

### [truncate]

Shrink or extend the size of a file to the specified size.

`user `[`$`]`truncate --help`

    Usage: truncate OPTION... FILE...
    Shrink or extend the size of each FILE to the specified size

    A FILE argument that does not exist is created.

    If a FILE is larger than the specified size, the extra data is lost.
    If a FILE is shorter, it is extended and the sparse extended part (hole)
    reads as zero bytes.

    Mandatory arguments to long options are mandatory for short options too.
      -c, --no-create        do not create any files
      -o, --io-blocks        treat SIZE as number of IO blocks instead of bytes
      -r, --reference=RFILE  base size on RFILE
      -s, --size=SIZE        set or adjust the file size by SIZE bytes
          --help     display this help and exit
          --version  output version information and exit

    The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
    Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).
    Binary prefixes can be used, too: KiB=K, MiB=M, and so on.

    SIZE may also be prefixed by one of the following modifying characters:
    '+' extend by, '-' reduce by, '<' at most, '>' at least,
    '/' round down to multiple of, '%' round up to multiple of.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/truncate>
    or available locally via: info '(coreutils) truncate invocation'

### [tsort]

Perform topological sort.

`user `[`$`]`tsort --help`

    Usage: tsort [OPTION] [FILE]
    Write totally ordered list consistent with the partial ordering in FILE.

    With no FILE, or when FILE is -, read standard input.

          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/tsort>
    or available locally via: info '(coreutils) tsort invocation'

### [tty]

Print the file name of the terminal connected to standard input.

`user `[`$`]`tty --help`

    Usage: tty [OPTION]...
    Print the file name of the terminal connected to standard input.

      -s, --silent, --quiet   print nothing, only return an exit status
          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/tty>
    or available locally via: info '(coreutils) tty invocation'

### [uname]

Print system information.

`user `[`$`]`uname --help`

    Usage: uname [OPTION]...
    Print certain system information.  With no OPTION, same as -s.

      -a, --all                print all information, in the following order,
                                 except omit -p and -i if unknown:
      -s, --kernel-name        print the kernel name
      -n, --nodename           print the network node hostname
      -r, --kernel-release     print the kernel release
      -v, --kernel-version     print the kernel version
      -m, --machine            print the machine hardware name
      -p, --processor          print the processor type (non-portable)
      -i, --hardware-platform  print the hardware platform (non-portable)
      -o, --operating-system   print the operating system
          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/uname>
    or available locally via: info '(coreutils) uname invocation'

### [unexpand]

Convert spaces to tabs.

`user `[`$`]`unexpand --help`

    Usage: unexpand [OPTION]... [FILE]...
    Convert blanks in each FILE to tabs, writing to standard output.

    With no FILE, or when FILE is -, read standard input.

    Mandatory arguments to long options are mandatory for short options too.
      -a, --all        convert all blanks, instead of just initial blanks
          --first-only  convert only leading sequences of blanks (overrides -a)
      -t, --tabs=N     have tabs N characters apart instead of 8 (enables -a)
      -t, --tabs=LIST  use comma separated list of tab positions
                         The last specified position can be prefixed with '/'
                         to specify a tab size to use after the last
                         explicitly specified tab stop.  Also a prefix of '+'
                         can be used to align remaining tab stops relative to
                         the last specified tab stop instead of the first column
          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/unexpand>
    or available locally via: info '(coreutils) unexpand invocation'

### [uniq]

Report or omit repeated lines.

`user `[`$`]`uniq --help`

    Usage: uniq [OPTION]... [INPUT [OUTPUT]]
    Filter adjacent matching lines from INPUT (or standard input),
    writing to OUTPUT (or standard output).

    With no options, matching lines are merged to the first occurrence.

    Mandatory arguments to long options are mandatory for short options too.
      -c, --count           prefix lines by the number of occurrences
      -d, --repeated        only print duplicate lines, one for each group
      -D                    print all duplicate lines
          --all-repeated[=METHOD]  like -D, but allow separating groups
                                     with an empty line;
                                     METHOD=
      -f, --skip-fields=N   avoid comparing the first N fields
          --group[=METHOD]  show all items, separating groups with an empty line;
                              METHOD=
      -i, --ignore-case     ignore differences in case when comparing
      -s, --skip-chars=N    avoid comparing the first N characters
      -u, --unique          only print unique lines
      -z, --zero-terminated     line delimiter is NUL, not newline
      -w, --check-chars=N   compare no more than N characters in lines
          --help     display this help and exit
          --version  output version information and exit

    A field is a run of blanks (usually spaces and/or TABs), then non-blank
    characters.  Fields are skipped before chars.

    Note: 'uniq' does not detect repeated lines unless they are adjacent.
    You may want to sort the input first, or use 'sort -u' without 'uniq'.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/uniq>
    or available locally via: info '(coreutils) uniq invocation'

### [unlink]

Call the unlink function to remove the specified file.

`user `[`$`]`unlink --help`

    Usage: unlink FILE
      or:  unlink OPTION
    Call the unlink function to remove the specified FILE.

          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/unlink>
    or available locally via: info '(coreutils) unlink invocation'

### [users]

Print the user names of users currently logged in to the current host.

`user `[`$`]`users --help`

    Usage: users [OPTION]... [FILE]
    Output who is currently logged in according to FILE.
    If FILE is not specified, use /var/run/utmp.  /var/log/wtmp as FILE is common.

          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/users>
    or available locally via: info '(coreutils) users invocation'

### [vdir]

List directory contents.

`user `[`$`]`vdir --help`

    Usage: vdir [OPTION]... [FILE]...
    List information about the FILEs (the current directory by default).
    Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

    Mandatory arguments to long options are mandatory for short options too.
      -a, --all                  do not ignore entries starting with .
      -A, --almost-all           do not list implied . and ..
          --author               with -l, print the author of each file
      -b, --escape               print C-style escapes for nongraphic characters
          --block-size=SIZE      with -l, scale sizes by SIZE when printing them;
                                   e.g., '--block-size=M'; see SIZE format below
      -B, --ignore-backups       do not list implied entries ending with ~
      -c                         with -lt: sort by, and show, ctime (time of last
                                   modification of file status information);
                                   with -l: show ctime and sort by name;
                                   otherwise: sort by ctime, newest first
      -C                         list entries by columns
          --color[=WHEN]         colorize the output; WHEN can be 'always' (default
                                   if omitted), 'auto', or 'never'; more info below
      -d, --directory            list directories themselves, not their contents
      -D, --dired                generate output designed for Emacs' dired mode
      -f                         do not sort, enable -aU, disable -ls --color
      -F, --classify             append indicator (one of */=>@|) to entries
          --file-type            likewise, except do not append '*'
          --format=WORD          across -x, commas -m, horizontal -x, long -l,
                                   single-column -1, verbose -l, vertical -C
          --full-time            like -l --time-style=full-iso
      -g                         like -l, but do not list owner
          --group-directories-first
                                 group directories before files;
                                   can be augmented with a --sort option, but any
                                   use of --sort=none (-U) disables grouping
      -G, --no-group             in a long listing, don't print group names
      -h, --human-readable       with -l and -s, print sizes like 1K 234M 2G etc.
          --si                   likewise, but use powers of 1000 not 1024
      -H, --dereference-command-line
                                 follow symbolic links listed on the command line
          --dereference-command-line-symlink-to-dir
                                 follow each command line symbolic link
                                   that points to a directory
          --hide=PATTERN         do not list implied entries matching shell PATTERN
                                   (overridden by -a or -A)
          --hyperlink[=WHEN]     hyperlink file names; WHEN can be 'always'
                                   (default if omitted), 'auto', or 'never'
          --indicator-style=WORD  append indicator with style WORD to entry names:
                                   none (default), slash (-p),
                                   file-type (--file-type), classify (-F)
      -i, --inode                print the index number of each file
      -I, --ignore=PATTERN       do not list implied entries matching shell PATTERN
      -k, --kibibytes            default to 1024-byte blocks for disk usage;
                                   used only with -s and per directory totals
      -l                         use a long listing format
      -L, --dereference          when showing file information for a symbolic
                                   link, show information for the file the link
                                   references rather than for the link itself
      -m                         fill width with a comma separated list of entries
      -n, --numeric-uid-gid      like -l, but list numeric user and group IDs
      -N, --literal              print entry names without quoting
      -o                         like -l, but do not list group information
      -p, --indicator-style=slash
                                 append / indicator to directories
      -q, --hide-control-chars   print ? instead of nongraphic characters
          --show-control-chars   show nongraphic characters as-is (the default,
                                   unless program is 'ls' and output is a terminal)
      -Q, --quote-name           enclose entry names in double quotes
          --quoting-style=WORD   use quoting style WORD for entry names:
                                   literal, locale, shell, shell-always,
                                   shell-escape, shell-escape-always, c, escape
                                   (overrides QUOTING_STYLE environment variable)
      -r, --reverse              reverse order while sorting
      -R, --recursive            list subdirectories recursively
      -s, --size                 print the allocated size of each file, in blocks
      -S                         sort by file size, largest first
          --sort=WORD            sort by WORD instead of name: none (-U), size (-S),
                                   time (-t), version (-v), extension (-X)
          --time=WORD            change the default of using modification times;
                                   access time (-u): atime, access, use;
                                   change time (-c): ctime, status;
                                   birth time: birth, creation;
                                 with -l, WORD determines which time to show;
                                 with --sort=time, sort by WORD (newest first)
          --time-style=TIME_STYLE  time/date format with -l; see TIME_STYLE below
      -t                         sort by time, newest first; see --time
      -T, --tabsize=COLS         assume tab stops at each COLS instead of 8
      -u                         with -lt: sort by, and show, access time;
                                   with -l: show access time and sort by name;
                                   otherwise: sort by access time, newest first
      -U                         do not sort; list entries in directory order
      -v                         natural sort of (version) numbers within text
      -w, --width=COLS           set output width to COLS.  0 means no limit
      -x                         list entries by lines instead of by columns
      -X                         sort alphabetically by entry extension
      -Z, --context              print any security context of each file
      -1                         list one file per line.  Avoid '\n' with -q or -b
          --help     display this help and exit
          --version  output version information and exit

    The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
    Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).
    Binary prefixes can be used, too: KiB=K, MiB=M, and so on.

    The TIME_STYLE argument can be full-iso, long-iso, iso, locale, or +FORMAT.
    FORMAT is interpreted like in date(1).  If FORMAT is FORMAT1<newline>FORMAT2,
    then FORMAT1 applies to non-recent files and FORMAT2 to recent files.
    TIME_STYLE prefixed with 'posix-' takes effect only outside the POSIX locale.
    Also the TIME_STYLE environment variable sets the default style to use.

    Using color to distinguish file types is disabled both by default and
    with --color=never.  With --color=auto, ls emits color codes only when
    standard output is connected to a terminal.  The LS_COLORS environment
    variable can change the settings.  Use the dircolors command to set it.

    Exit status:
     0  if OK,
     1  if minor problems (e.g., cannot access subdirectory),
     2  if serious trouble (e.g., cannot access command-line argument).

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/vdir>
    or available locally via: info '(coreutils) vdir invocation'

### [wc]

Print newline, word, and byte counts for each file.

`user `[`$`]`wc --help`

    Usage: wc [OPTION]... [FILE]...
      or:  wc [OPTION]... --files0-from=F
    Print newline, word, and byte counts for each FILE, and a total line if
    more than one FILE is specified.  A word is a non-zero-length sequence of
    characters delimited by white space.

    With no FILE, or when FILE is -, read standard input.

    The options below may be used to select which counts are printed, always in
    the following order: newline, word, character, byte, maximum line length.
      -c, --bytes            print the byte counts
      -m, --chars            print the character counts
      -l, --lines            print the newline counts
          --files0-from=F    read input from the files specified by
                               NUL-terminated names in file F;
                               If F is - then read names from standard input
      -L, --max-line-length  print the maximum display width
      -w, --words            print the word counts
          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/wc>
    or available locally via: info '(coreutils) wc invocation'

### [who]

Show who is logged on.

`user `[`$`]`who --help`

    Usage: who [OPTION]... [ FILE | ARG1 ARG2 ]
    Print information about users who are currently logged in.

      -a, --all         same as -b -d --login -p -r -t -T -u
      -b, --boot        time of last system boot
      -d, --dead        print dead processes
      -H, --heading     print line of column headings
      -l, --login       print system login processes
          --lookup      attempt to canonicalize hostnames via DNS
      -m                only hostname and user associated with stdin
      -p, --process     print active processes spawned by init
      -q, --count       all login names and number of users logged on
      -r, --runlevel    print current runlevel
      -s, --short       print only name, line, and time (default)
      -t, --time        print last system clock change
      -T, -w, --mesg    add user's message status as +, - or ?
      -u, --users       list users logged in
          --message     same as -T
          --writable    same as -T
          --help     display this help and exit
          --version  output version information and exit

    If FILE is not specified, use /var/run/utmp.  /var/log/wtmp as FILE is common.
    If ARG1 ARG2 given, -m presumed: 'am i' or 'mom likes' are usual.

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/who>
    or available locally via: info '(coreutils) who invocation'

### [whoami]

Print effective userid.

`user `[`$`]`whoami --help`

    Usage: whoami [OPTION]...
    Print the user name associated with the current effective user ID.
    Same as id -un.

          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/whoami>
    or available locally via: info '(coreutils) whoami invocation'

### [yes]

Output a string repeatedly until killed.

`user `[`$`]`yes --help`

    Usage: yes [STRING]...
      or:  yes OPTION
    Repeatedly output a line with all specified STRING(s), or 'y'.

          --help     display this help and exit
          --version  output version information and exit

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/yes>
    or available locally via: info '(coreutils) yes invocation'

## [See also]

-   [util-linux](https://wiki.gentoo.org/wiki/Util-linux "Util-linux") --- userspace utilities for Linux-specific system management, including device control, terminal logins, process management, and tty messaging.