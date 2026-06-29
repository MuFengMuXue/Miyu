[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Virtual_packages&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Virtual packages** allow alternative packages to fulfill a dependency, when two or more packages are functionally equivalent for this use.

For example, if a package needs an editor installed, but doesn\'t need functionality only provided by a specific editor, that package can specify that it depends on [[[virtual/editor]](https://packages.gentoo.org/packages/virtual/editor)[]]. Then, that dependency will be satisfied as long as one or more specific packages are installed, including (amongst others) [[[app-editors/emacs]](https://packages.gentoo.org/packages/app-editors/emacs)[]], [[[app-editors/joe]](https://packages.gentoo.org/packages/app-editors/joe)[]], [[[app-editors/nano]](https://packages.gentoo.org/packages/app-editors/nano)[]], [[[app-editors/neovim]](https://packages.gentoo.org/packages/app-editors/neovim)[]], [`$`]`portageq expand_virtual / virtual/editor`

If no package is currently satisfying the virtual, the virtual itself will be returned as the result, as described in the `--help` output for [portageq]:

> expand_virtual \<eroot\> \<atom\>\
> Returns a \\n separated list of atoms expanded from a given virtual atom (GLEP 37 virtuals only), excluding blocker atoms. Satisfied virtual atoms are not included in the output, since they are expanded to real atoms which are displayed. Unsatisfied virtual atoms are displayed without any expansion. The \"match\" command can be used to resolve the returned atoms to specific installed packages.

To show which packages are available to satisfy a particular virtual:

`user `[`$`]`qdepends -r virtual/editor | tr ' ' '\n' | sed '1d' | sort`

Alternatively, the following function should work in any POSIX-compliant shell, and outputs one package per line:

     packages_satisfying_virtual ()  |
             tr ' ' '\n' |
             sed '1d' |
             sort
     }

The function can be used like so:

`user `[`$`]`packages_satisfying_virtual editor`

    app-editors/dav
    app-editors/e3
    app-editors/ee
    app-editors/emacs:*
    app-editors/emact
    app-editors/ersatz-emacs
    app-editors/fe
    app-editors/gvim
    app-editors/helix
    app-editors/jasspa-microemacs
    app-editors/jed
    app-editors/joe
    app-editors/jove
    app-editors/kakoune
    app-editors/levee
    app-editors/lpe
    app-editors/mg
    app-editors/micro
    app-editors/moe
    app-editors/nano
    app-editors/ne
    app-editors/neovim
    app-editors/ng
    app-editors/qemacs
    app-editors/teco
    app-editors/uemacs-pk
    app-editors/vile
    app-editors/vim
    app-editors/vis
    app-editors/xemacs
    app-editors/zile
    app-misc/mc[edit]
    dev-lisp/cmucl
    mail-client/alpine[-onlyalpine]

The full list of virtual packages is available online: [virtual](https://packages.gentoo.org/categories/virtual). It is also available locally by using a tool such as [eix](https://wiki.gentoo.org/wiki/Eix "Eix"), e.g.:

`user `[`$`]`eix -C virtual`

To list which packages depend on a virtual, e.g. [[[virtual/jdk]](https://packages.gentoo.org/packages/virtual/jdk)[]]:

`user `[`$`]`qdepends -qQF'%/%' virtual/jdk`

    dev-util/apktool: virtual/jdk
    virtual/jre: virtual/jdk:21
    virtual/jre: virtual/jdk:25

## [Substitute one virtual package for another]

It is possible to substitute one virtual package for another by installing the desired package with the `--oneshot` option, then [removing](https://wiki.gentoo.org/wiki/Emerge#Remove_.28uninstall.29_packages "Emerge") the undesired package.

See this section on [substituting a source based dependency for \"-bin\" version](https://wiki.gentoo.org/wiki/Minimizing_compilation_and_installation_time#Substituting_a_source_based_dependency_for_.22-bin.22_version "Minimizing compilation and installation time") for an example.