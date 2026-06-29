[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Dokuwiki&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.dokuwiki.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Dokuwiki "wikipedia:Dokuwiki")

[[]][Package information](https://packages.gentoo.org/packages/www-apps/dokuwiki)

[DokuWiki] is a wiki system based on files instead of a database. The file-based approach makes it easier to use with file hosting and sychronization services. Access controls are provided by default, more than 50 languages are supported, and a range of plugins and themes (\'templates\') are available.

## [Installation]

### [USE flags]

### [USE flags for] [www-apps/dokuwiki](https://packages.gentoo.org/packages/www-apps/dokuwiki) [[]] [DokuWiki is a simple to use Wiki aimed at a small company\'s documentation needs]

  --------------------------------------------------------- --------------------------------------------------------------------------------------
  [`gd`](https://packages.gentoo.org/useflags/gd)           Add support for media-libs/gd (to generate graphics on the fly)
  [`vhosts`](https://packages.gentoo.org/useflags/vhosts)   Add support for installing web-based applications into a virtual-hosting environment
  --------------------------------------------------------- --------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-09-19 15:07] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask www-apps/dokuwiki`

Unmasking the package (if necessary):

`root `[`#`]`echo "www-apps/dokuwiki" > /etc/portage/package.accept_keywords/dokuwiki`

** Note**\
The command have to be edited accordingly to the system settings.

And now the emerge command should install [[[www-apps/mediawiki]](https://packages.gentoo.org/packages/www-apps/mediawiki)[]].