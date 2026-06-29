## [Example]

This is a list of remote-id types that can be used in the `<upstream>` element in package metadata.

[CODE] **Using remote-id in [metadata.xml]**


      <upstream>
        <remote-id type="github">karelzak/util-linux</remote-id>
      </upstream>
    </pkgmetadata>

## [Entries]

  -------------------- ------------------------------------------ --------------------------------------------------------------------------- -------------------------
  Remote-id type       Description                                Syntax                                                                      Notes
  bitbucket                                                       `https://bitbucket.org/``remote-id`
  codeberg                                                        `https://codeberg.org/``remote-id`
  cpan                 Comprehensive Perl Archive Network         `https://metacpan.org/dist/``remote-id`
  cpan-module                                                     `https://metacpan.org/pod/``remote-id`
  cpe                                                             `remote-id`
  cran                 Comprehensive R Archive Network            `https://cran.r-project.org/web/packages/``remote-id``/`
  ctan                 Comprehensive TeX Archive Network          `https://ctan.org/pkg/``remote-id`
  freedesktop-gitlab   FreeDesktop.org Gitlab repositories        `https://gitlab.freedesktop.org/``remote-id``.git/`
  gentoo               Gentoo Git repositories                    `https://gitweb.gentoo.org/``remote-id``.git/`
  github                                                          `https://github.com/``remote-id`
  gitlab                                                          `https://gitlab.com/``remote-id`
  gnome-gitlab         GNOME.org Gitlab repositories              `https://gitlab.gnome.org/``remote-id``.git/`
  google-code                                                     `https://code.google.com/archive/p/``remote-id``/`               archive
  hackage                                                         `https://hackage.haskell.org/package/``remote-id`
  heptapod                                                        `https://foss.heptapod.net/``remote-id`
  kde-invent                                                      `https://invent.kde.org/``remote-id`
  launchpad                                                       `https://launchpad.net/``remote-id`
  osdn                 Open Source Development Network            `https://osdn.net/projects/``remote-id``/`                       formerly SourceForge.JP
  pear                 PHP Extension and Application Repository   `https://pear.php.net/package/``remote-id`
  pecl                 PHP Extension Community Library            `https://pecl.php.net/package/``remote-id`
  pypi                 Python Package Index                       `https://pypi.org/project/``remote-id``/`
  rubygems                                                        `https://rubygems.org/gems/``remote-id``/`
  savannah                                                        `https://savannah.gnu.org/projects/``remote-id`
  savannah-nongnu                                                 `https://savannah.nongnu.org/projects/``remote-id`
  sourceforge                                                     `https://sourceforge.net/projects/``remote-id``/`
  sourcehut                                                       `https://sr.ht/``remote-id``/`
  vim                                                             `https://www.vim.org/scripts/script.php?script_id=``remote-id`   numerical identifier
  -------------------- ------------------------------------------ --------------------------------------------------------------------------- -------------------------

### [Adding a new remote-id]

The following locations must be updated:

-   [DTD](https://gitweb.gentoo.org/data/dtd.git/) (needs gentoo-dev ML review, do this before any other step)
-   [XML schema](https://gitweb.gentoo.org/data/xml-schema.git/)
-   this wiki page!
-   [pkgcore](https://gitweb.gentoo.org/proj/pkgcore/pkgcore.git/) (has a copy of the XML schema)
-   [pkgcheck](https://gitweb.gentoo.org/proj/pkgcore/pkgcheck.git/)
-   [soko](https://gitweb.gentoo.org/sites/soko.git/) (packages.gentoo.org)
-   [iwdevtools](https://github.com/ionenwks/iwdevtools)
-   [nxml-gentoo-schemas](https://gitweb.gentoo.org/proj/nxml-gentoo-schemas.git/) (for GNU Emacs)
-   [[[app-text/gentoo-dtd]](https://packages.gentoo.org/packages/app-text/gentoo-dtd)[]]