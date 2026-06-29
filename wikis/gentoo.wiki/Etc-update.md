** Warning**\
[etc-update] is **no longer recommended** to users not already using it, as it can clobber protected configuration files without making any backups.

\

[dispatch-conf](https://wiki.gentoo.org/wiki/Dispatch-conf "Dispatch-conf") is preferred, as it stores history and supports reverting changes to protected configuration files. [etc-update] is also not as fully featured as [dispatch-conf].

[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines") (This was mostly just copied from [Special:Diff/1272597/1309269](https://wiki.gentoo.org/wiki/Special:Diff/1272597/1309269 "Special:Diff/1272597/1309269"). This may not be worth fixing - see talk page.). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**etc-update** is a tool to merge configuration files with an interactive merging setup and can also auto-merge trivial changes.

`root `[`#`]`etc-update --help`

    etc-update: Handle configuration file updates

    Usage: etc-update [options] [paths to scan]

    If no paths are specified, then $ will be used.

    Options:
      -d, --debug    Enable shell debugging
      -h, --help     Show help and run away
      -p, --preen    Automerge trivial changes only and quit
      -q, --quiet    Show only essential output
      -v, --verbose  Show settings and such along the way
      -V, --version  Show version and trundle away

      --automode <mode>
                 -3 to auto merge all files
                 -5 to auto-merge AND not use 'mv -i'
                 -7 to discard all updates
                 -9 to discard all updates AND not use 'rm -i'

After merging the straightforward changes, a list of protected files will be provided that have an update waiting. At the bottom the possible options are shown:

[CODE] **Options presented by etc-update**

    Please select a file to edit by entering the corresponding number.
                  (-1 to exit) (-3 to auto merge all remaining files)
                               (-5 to auto-merge AND not use 'mv -i'):

When entering `-1`, [etc-update] will exit and discontinue any other changes. With `-3` or `-5`, all listed configuration files will be overwritten with the newer versions. It is therefore very important to first select the configuration files that should not be automatically updated. This is simply a matter of entering the number listed to the left of that configuration file.

As an example, we select the configuration file [/etc/pear.conf]:

[CODE] **Updating a specific configuration file**

    Beginning of differences between /etc/pear.conf and /etc/._cfg0000_pear.conf
    [...]
    End of differences between /etc/pear.conf and /etc/._cfg0000_pear.conf
    1) Replace original with update
    2) Delete update, keeping original as is
    3) Interactively merge original with update
    4) Show differences again

The differences between the two files are shown. If the updated configuration file can be used without problems, enter [1]. If the updated configuration file isn\'t necessary, or doesn\'t provide any new or useful information, enter [2]. If the current configuration file has to be interactively updated, enter [3].

There is no point in further elaborating the interactive merging here. For completeness sake, we will list the possible commands that can be used while interactively merging the two files. Users are greeted with two lines (the original one, and the proposed new one) and a prompt at which the user can enter one of the following commands:

[CODE] **Commands available for the interactive merging**

    ed:     Edit then use both versions, each decorated with a header.
    eb:     Edit then use both versions.
    el:     Edit then use the left version.
    er:     Edit then use the right version.
    e:      Edit a new version.
    l:      Use the left version.
    r:      Use the right version.
    s:      Silently include common lines.
    v:      Verbosely include common lines.
    q:      Quit.

After having finished updating the important configuration files, users can then automatically update all the other configuration files. [etc-update] will exit if it doesn\'t find any more updateable configuration files.

## [See also]

-   [cfg-update](https://wiki.gentoo.org/wiki/Cfg-update "Cfg-update") --- a utility used on Gentoo to manage configuration file updates.
-   [dispatch-conf](https://wiki.gentoo.org/wiki/Dispatch-conf "Dispatch-conf") --- a utility included with [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), used to safely and conveniently manage configuration files after package updates.