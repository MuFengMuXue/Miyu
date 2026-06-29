**Resources**

[[]][Home](https://haskell.org/haskellwiki/Haskell)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Haskell_(programming_language) "wikipedia:Haskell (programming language)")

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Haskell "Project:Haskell")][Project](https://wiki.gentoo.org/wiki/Project:Haskell "Project:Haskell")

[[]][Ebuild repository](https://github.com/gentoo-haskell/gentoo-haskell/blob/master/README.rst)

[[]][[#haskell](ircs://irc.libera.chat/#haskell)] ([[webchat](https://web.libera.chat/#haskell)])

[[]][[#gentoo-haskell](ircs://irc.libera.chat/#gentoo-haskell)] ([[webchat](https://web.libera.chat/#gentoo-haskell)])

**Haskell** is a purely-functional programming language.

## Contents

-   [[1] [Getting started]](#Getting_started)
-   [[2] [Compiler and interpreter]](#Compiler_and_interpreter)
-   [[3] [cabal tool]](#cabal_tool)
-   [[4] [Updating Haskell packages]](#Updating_Haskell_packages)
-   [[5] [Hoogle with local installation]](#Hoogle_with_local_installation)
    -   [[5.1] [Integration with GHCi]](#Integration_with_GHCi)
-   [[6] [HLint]](#HLint)
-   [[7] [Editor plugins]](#Editor_plugins)
    -   [[7.1] [Emacs]](#Emacs)
        -   [[7.1.1] [Haskell Mode]](#Haskell_Mode)
        -   [[7.1.2] [ghc-mod]](#ghc-mod)
    -   [[7.2] [Haskell-Mode for Vim]](#Haskell-Mode_for_Vim)
-   [[8] [Troubleshooting]](#Troubleshooting)
    -   [[8.1] [Haskell ebuilds failing with out of memory error]](#Haskell_ebuilds_failing_with_out_of_memory_error)
-   [[9] [External resources]](#External_resources)

## [Getting started]

First, put the following entries into [/etc/portage/package.accept_keywords]:

[FILE] **`/etc/portage/package.accept_keywords`**

    # Haskell has no stable keywords in Gentoo
    dev-haskell/*
    dev-lang/ghc

    # Only needed if using ::haskell, but harmless if not.
    # May as well put it in, just in case for future use.
    */*::haskell

If interested in doing Haskell development, or if the needed packages required are not in the main [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository"), please enable and configure the [haskell](https://repos.gentoo.org/#haskell) repository. The Haskell repository (::haskell) has its own [instructions](https://github.com/gentoo-haskell/gentoo-haskell/blob/master/README.rst) too. The most important part is that this repository requires a specific unmasking procedure to prevent blockers.

Install git to fetch the overlay and eselect-repository to setup the overlay:

`root `[`#`]`emerge --ask app-eselect/eselect-repository dev-vcs/git`

Add the overlay:

`root `[`#`]`eselect repository enable haskell `

Update system:

`root `[`#`]`emerge --sync `

`root `[`#`]`emerge -uvDU @world `

## [Compiler and interpreter]

The most important and up-to-date Haskell-implementation is the [**Glasgow Haskell Compiler**](https://www.haskell.org/ghc/) (GHC). Install it with:

`root `[`#`]`emerge --ask dev-lang/ghc`

The package also includes an interpreter called GHCI (except on the ARM architecture).

Furthermore, there\'s [**Hugs**](https://www.haskell.org/hugs/), an (now outdated) interpreter for Haskell98. The ecosystem has moved on with both a newer Haskell specification being published (Haskell 2010) and packages often relying on GHC extensions to Haskell. However, Hugs can still be fun to play with. Install it with:

`root `[`#`]`emerge --ask dev-lang/hugs98`

## [cabal tool]

With [**cabal**](https://www.haskell.org/cabal/) tool, it is possible to package and build libraries and programs. Install it with:

`root `[`#`]`emerge --ask dev-haskell/cabal-install`

** Warning**\
Despite the package name, [[[dev-haskell/cabal-install]](https://packages.gentoo.org/packages/dev-haskell/cabal-install)[]] **should not** be used to install Haskell packages, especially system-wide. (If you are running `cabal install`, you are most likely making a mistake.)\

\
Instead, `emerge` should be used to install Haskell packages, assuming the package is available as an [ebuild](https://wiki.gentoo.org/wiki/Ebuild "Ebuild"). If a package is needed that isn\'t in the main Gentoo tree, it may be present in the [Haskell ebuild repository](https://github.com/gentoo-haskell/gentoo-haskell/). If not, please file a bug/issue, or ask us in [#gentoo-haskell](irc://irc.gentoo.org/gentoo-haskell) on IRC!\
\

It is safe to use [[[dev-haskell/cabal-install]](https://packages.gentoo.org/packages/dev-haskell/cabal-install)[]] for building packages and running executables at the project level. A Haskell project can be developed without needing system-wide libraries by using the now-standard [\"Nix-style Local Builds\"](https://cabal.readthedocs.io/en/3.10/nix-local-build-overview.html).

## [Updating Haskell packages]

Sometimes:

`root `[`#`]`emerge -auvDN --keep-going @world`

has trouble figuring out how to update Haskell packages. Providing emerge with the full list of dev-haskell packages that have upgrades available can sometimes help:

`root `[`#`]`eix-update`

`root `[`#`]`` emerge -av --oneshot --keep-going `eix --only-names --upgrade -C dev-haskell` ``

`root `[`#`]`haskell-updater`

Sometimes, if there are sub-slot blockers (when updating ghc or some specific package there are a list of blockers), this issue could be solved via running:

`root `[`#`]`haskell-updater --all -- =dev-lang/ghc-`*`<latest.version>`*

## [Hoogle with local installation]

The Hoogle ebuild is currently only available in the official *gentoo-haskell* [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository"). So add that first.

** Important**\
Remember to unmask the each package as described in the [repository README](https://github.com/gentoo-haskell/gentoo-haskell/blob/master/README.rst)

`root `[`#`]`eselect repository enable haskell `

`root `[`#`]`emerge --sync haskell`

In order to get the an offline installation of all hoogle data, enable the `doc`, `hscolour`, and `hoogle` USE flag values.

`root `[`#`]`echo "dev-haskell/* doc hoogle hscolour" >> /etc/portage/package.use`

Enable the relevant USE flags for hoogle to store all data local, and emerge hoogle:

`root `[`#`]`echo "dev-haskell/hoogle fetchdb fetchdb-ghc localdb" >> /etc/portage/package.use`

`root `[`#`]`emerge --ask dev-util/hoogle`

After emerging haskell packages, the hoogle database of the locally installed packages is updated by running:

`root `[`#`]`hoogle-build-localdb`

(It\'s normal for `hoogle-build-localdb` to output a bunch of junk. Redirect [stdout] to [/dev/null] if it has been added to e.g. [/etc/cron.daily].)

At this point, Hoogle should work from the command-line. For example, the following will search for the `splitOn` function:

`user `[`$`]`$ hoogle splitOn`

    Data.Text.Lazy splitOn :: Text -> Text -> [Text]
    Data.Text splitOn :: Text -> Text -> [Text]
    Data.List.Extra splitOn :: Eq a => [a] -> [a] -> [[a]]
    Extra splitOn :: Eq a => [a] -> [a] -> [[a]]
    Data.List.Split.Internals splitOn :: Eq a => [a] -> [a] -> [[a]]
    Data.List.Split splitOn :: Eq a => [a] -> [a] -> [[a]]
    Data.List.Split.Internals splitOneOf :: Eq a => [a] -> [a] -> [[a]]
    Data.List.Split splitOneOf :: Eq a => [a] -> [a] -> [[a]]

### [Integration with GHCi]

To use Hoogle within GHCi, make a little modification to local [\~/.ghci] file. Add the following:

[FILE] **`~/.ghci`**

    -- Surround a string in single quotes.
    let single_quote s = concat ["'", s, "'"]

    -- Escape a single quote in the shell. (This mess actually works.)
    let escape_single_quote c = if c == '\'' then "'\"'\"'" else [c]

    -- Simple heuristic to escape shell command arguments.
    let simple_shell_escape = single_quote . (concatMap escape_single_quote)

    :def hoogle \x -> return $ ":!hoogle --color " ++ (simple_shell_escape x)
    :def doc \x -> return $ ":!hoogle --info --color " ++ (simple_shell_escape x)

Now, within GHCi, there should be access to two new commands, `:hoogle` and `:doc`. The first will perform a normal Hoogle search and print the output:

`user `[`$`]`ghci`

    ghci> :hoogle splitOn
    Searching for: splitOn
    Data.Text.Lazy splitOn :: Text -> Text -> [Text]
    Data.Text splitOn :: Text -> Text -> [Text]
    Data.List.Extra splitOn :: Eq a => [a] -> [a] -> [[a]]
    Extra splitOn :: Eq a => [a] -> [a] -> [[a]]
    Data.List.Split.Internals splitOn :: Eq a => [a] -> [a] -> [[a]]
    Data.List.Split splitOn :: Eq a => [a] -> [a] -> [[a]]
    Data.List.Split.Internals splitOneOf :: Eq a => [a] -> [a] -> [[a]]
    Data.List.Split splitOneOf :: Eq a => [a] -> [a] -> [[a]]

The second will display the Haddock documentation for the method:

`user `[`$`]`ghci`

    ghci> :doc splitOn
    Searching for: splitOn
    Data.Text.Lazy splitOn :: Text -> Text -> [Text]

    O(m+n) Break a Text into pieces separated by the first Text argument (which cannot be an empty string), consuming the delimiter. An empty delimiter is invalid, and will cause an error to be raised.

    Examples:

    > splitOn "\r\n" "a\r\nb\r\nd\r\ne" == ["a","b","d","e"]
    > splitOn "aaa"  "aaaXaaaXaaaXaaa"  == ["","X","X","X",""]
    > splitOn "x"    "x"                == ["",""]

    and

    > intercalate s . splitOn s         == id
    > splitOn (singleton c)             == split (==c)

    (Note: the string s to split on above cannot be empty.)

    This function is strict in its first argument, and lazy in its second.

    In (unlikely) bad cases, this function's time complexity degrades towards O(n*m).

    From package text
    splitOn :: Text -> Text -> [Text]

## [HLint]

[**HLint**](http://community.haskell.org/~ndm/hlint/) checks and simplifies the Haskell source code! Install it with:

`root `[`#`]`eselect repository enable haskell `

`root `[`#`]`emerge --sync haskell`

`root `[`#`]`emerge --ask dev-haskell/hlint`

## [Editor plugins]

### [Emacs]

#### [Haskell Mode]

The [Haskell Mode for Emacs](https://haskell.github.io/haskell-mode/) improves the experience of developing and debugging Haskell programs in Emacs. It can be installed with:

`root `[`#`]`emerge --ask app-emacs/haskell-mode`

Now it can be configured with `M-x customize-group RET haskell RET`.

#### [ghc-mod]

The official Gentoo Haskell ebuild repository provides an ebuild for ghc-mod, an extension of Haskell Mode. Add the repository with:

`root `[`#`]`eselect repository enable haskell `

`root `[`#`]`emerge --sync haskell`

Then, install the ebuild:

`root `[`#`]`emerge --ask app-emacs/ghc-mod`

### [Haskell-Mode for Vim]

[There](http://projects.haskell.org/haskellmode-vim/)\'s also a Haskell-Mode for [Vim](https://wiki.gentoo.org/wiki/Vim "Vim").

## [Troubleshooting]

### [Haskell ebuilds failing with out of memory error]

When [MAKEOPTS](https://wiki.gentoo.org/wiki//etc/portage/make.conf#MAKEOPTS "/etc/portage/make.conf") is set to allow parallel jobs, ghc may fail in Haskell ebuilds with `ghc: failed to create OS thread: Cannot allocate memory`. To fix this, lower the amount of jobs set in `MAKEOPTS`, or do not allow parallel jobs at all. `MAKEOPTS` can be overridden for failing ebuilds as described in [Overriding environment variables per package](https://wiki.gentoo.org/wiki/Knowledge_Base:Overriding_environment_variables_per_package "Knowledge Base:Overriding environment variables per package").

## [External resources]

-   The [[#haskell](ircs://irc.libera.chat/#haskell)] ([[webchat](https://web.libera.chat/#haskell)]) and [[#gentoo-haskell](ircs://irc.libera.chat/#gentoo-haskell)] ([[webchat](https://web.libera.chat/#gentoo-haskell)]) channels on code.freenode.net.