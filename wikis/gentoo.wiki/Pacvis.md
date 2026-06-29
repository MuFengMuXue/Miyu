[[]][GitHub](https://github.com/bgloyer/pacvis)

[pacvis] is a tool to interactively display dependency graphs of the portage tree using a web interface. It can show graphs of the installed packages as well previews of emerges.

## Contents

-   [[1] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
-   [[3] [See also]](#See_also)

### [Emerge]

[pacvis] is available in the [GURU](https://wiki.gentoo.org/wiki/Project:GURU "Project:GURU") overlay which can be added through either [Eselect/Repository](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository"). GURU is an official Gentoo overlay that is maintained by Gentoo users. Assuming [eselect repository] is set up, the GURU overlay can be added by:

`root `[`#`]`eselect repository enable guru`

Then [pacvis] can be emerged:

`root `[`#`]`emerge --ask app-portage/pacvis`

## [Usage]

[pacvis] uses [tornado] and vis.js to display portage depedency graphs. The graphs are based on the portage depclean tree or the tree resulting from an emerge -p \<arguments\> command.

### [Invocation]

To show a dependency graph of all installed packages run the command below and open a web browser to the indicated address.

`user `[`$`]`pacvis`

    Start PacVis at http://localhost:8888/
    use --browser to open a browser automatically.

[pacvis] can take [emerge] command line arguments to show a preview of what an emerge command would do. The command below will show a graph of all the packages that would be added or updated as a result of the equivalent emerge. In addition, it will show all packages that depend on the updated package.

`user `[`$`]`pacvis --browser --update --changed-use --deep @world`

To see what a complete system reinstall would look like, run:

`user `[`$`]`pacvis --browser -e @world`

## [See also]

-   [Project:GURU](https://wiki.gentoo.org/wiki/Project:GURU "Project:GURU") --- an official repository of new Gentoo packages that are maintained collaboratively by Gentoo users
-   [Q applets](https://wiki.gentoo.org/wiki/Q_applets "Q applets") --- a collection of small, fast [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") **q**uery utilities written in C.
-   [Gentoolkit](https://wiki.gentoo.org/wiki/Gentoolkit "Gentoolkit") --- a suite of tools to ease the administration of a Gentoo system, and [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") in particular.
-   [Useful_Portage_tools](https://wiki.gentoo.org/wiki/Useful_Portage_tools "Useful Portage tools") --- provides a list of Gentoo-specific system management tools, notably for [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), available in the [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository").