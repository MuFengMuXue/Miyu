**Revision bumping**, also known as *revbumping*, is the act of updating an [ebuild](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") to a new revision. This article describes the procedure to be followed.

## Contents

-   [[1] [When is a revbump needed?]](#When_is_a_revbump_needed.3F)
-   [[2] [Procedure]](#Procedure)
    -   [[2.1] [Bumping files]](#Bumping_files)
    -   [[2.2] [Bumping ebuilds]](#Bumping_ebuilds)
        -   [[2.2.1] [Copying the ebuilds]](#Copying_the_ebuilds)
        -   [[2.2.2] [Incrementing the ebuild revisions]](#Incrementing_the_ebuild_revisions)
        -   [[2.2.3] [Destabilizing the new ebuilds]](#Destabilizing_the_new_ebuilds)
        -   [[2.2.4] [Using the bumped files]](#Using_the_bumped_files)

## [][[] When is a revbump needed?]

Revbumping may be required upon request from a package maintainer. Additional reasons to perform revbumps are outlined at the [Ebuild revisions](https://devmanual.gentoo.org/general-concepts/ebuild-revisions/index.html) page in the development guide.

## [[] Procedure]

Revbumps usually accompany changes to other files in the tree, such as files under [files/].

### [[] Bumping files]

When making changes that require a revbump, those changes should not be made in place. Instead, the following steps should be followed:

1.  Copy the latest revisions of the files.
2.  Increment their revision numbers.
3.  Add any modifications to these copies.

[DIFF] [app-editors/vim-core/files/]

Before revbump

    app-editors/vim-core/files/
    ├── vimrc-r5
    └── vimrc-r6

After revbump

    app-editors/vim-core/files/
    ├── vimrc-r5
    ├── vimrc-r6
    └── vimrc-r7

For files that do not have revision numbers, append `-r1`:

[DIFF] [app-editors/neovim/files/]

Before revbump

    app-editors/neovim/files/
    └── sysinit.vim

After revbump

    app-editors/neovim/files/
    ├── sysinit.vim
    └── sysinit.vim-r1

These files are not used in any ebuilds yet. The next section explains how to create new ebuilds that use these files.

### [[] Bumping ebuilds]

Similarly to files, ebuild changes that require a revbump should be applied to *copies* of those ebuilds, not the original ebuilds. The following steps should be followed:

1.  For each package, copy the latest stable and unstable ebuild.
2.  Increment the copies\' revision numbers.
3.  [Destabilize](https://wiki.gentoo.org/wiki/Stable_request "Stable request") these copies.
4.  Modify the copied ebuilds to use the bumped files from before.

These steps are explained in detail in the following sections.

#### [[]Copying the ebuilds]

Ideally, only the latest stable and unstable version of each package should be revbumped, in order not to clutter the [Portage tree](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository").

The ebuild files themselves need to be inspected to determine their stability. Unstable versions have `~` in front of each architecture in the [`KEYWORDS`](https://wiki.gentoo.org/wiki/KEYWORDS "KEYWORDS") variable:

[FILE] **`app-editors/vim-core/vim-core-9.1.0366.ebuild`**

    KEYWORDS="~alpha ~amd64 ~arm ~arm64 ~hppa ~ia64 ~loong ~m68k ~mips ~ppc ~ppc64 ~riscv ~s390 ~sparc ~x86 ~amd64-linux ~x86-linux ~arm64-macos ~ppc-macos ~x64-macos ~x64-solaris"

Stable versions lack `~` in front of some architectures:

[FILE] **`app-editors/vim-core/vim-core-9.0.2167.ebuild`**

    KEYWORDS="~alpha amd64 arm arm64 hppa ~ia64 ~loong ~m68k ~mips ppc ppc64 ~riscv ~s390 sparc x86 ~amd64-linux ~x86-linux ~arm64-macos ~ppc-macos ~x64-macos ~x64-solaris"

[Live ebuilds](https://wiki.gentoo.org/wiki/Live_ebuilds "Live ebuilds") should be modified in place; not copied.

#### [[] Incrementing the ebuild revisions]

The same rules apply as in section [Bumping files](#Bumping_files), except that the revision numbers belong *before* the file extensions.

[DIFF] [app-editors/vim-core/]

Before copying

    app-editors/vim-core/
    ├── files
    │   ├── vimrc-r6
    │   └── vimrc-r7
    ├── metadata.xml
    ├── vim-core-9.0.2092.ebuild

    ├── vim-core-9.0.2167.ebuild

    ├── vim-core-9.1.0366.ebuild
    └── vim-core-9999.ebuild

After copying

    app-editors/vim-core/
    ├── files
    │   ├── vimrc-r6
    │   └── vimrc-r7
    ├── metadata.xml
    ├── vim-core-9.0.2092.ebuild
    ├── vim-core-9.0.2167-r1.ebuild
    ├── vim-core-9.0.2167.ebuild
    ├── vim-core-9.1.0366-r1.ebuild
    ├── vim-core-9.1.0366.ebuild
    └── vim-core-9999.ebuild

The modifications to these new ebuilds and the live ebuilds are explained in the following two sections.

#### [[] Destabilizing the new ebuilds]

`~` should be present in front of each arch that does not already have some prefix in `KEYWORDS`.

[DIFF] [app-editors/vim-core/vim-core-9.0.2167-r1.ebuild]

Before modifying

    KEYWORDS="~alpha amd64 arm arm64 hppa ~ia64 ~loong ~m68k ~mips ppc ppc64 ~riscv ~s390 sparc x86 ~amd64-linux ~x86-linux ~arm64-macos ~ppc-macos ~x64-macos ~x64-solaris"

After modifying

    KEYWORDS="~alpha ~amd64 ~arm ~arm64 ~hppa ~ia64 ~loong ~m68k ~mips ~ppc ~ppc64 ~riscv ~s390 ~sparc ~x86 ~amd64-linux ~x86-linux ~arm64-macos ~ppc-macos ~x64-macos ~x64-solaris"

#### [[] Using the bumped files]

Find lines that reference the files that were bumped. Modify these to reference the new files. For example:

[DIFF] [app-editors/vim-core/vim-core-9.0.2167-r1.ebuild]

Before modifying

    newins "$"/vimrc-r6 vimrc

After modifying

    newins "$"/vimrc-r7 vimrc

Another example:

[DIFF] [app-editors/neovim/neovim-0.9.5-r1.ebuild]

Before modifying

    doins "$"/sysinit.vim

After modifying

    newins "$"/sysinit.vim-r1 sysinit.vim