[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Hugo&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://gohugo.io/)

[[]][Official documentation](https://gohugo.io/documentation/)

[[]][Package information](https://packages.gentoo.org/packages/www-apps/hugo)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Hugo_(software) "wikipedia:Hugo (software)")

[[]][GitHub](https://github.com/gohugoio/hugo)

[[]][Bugs (upstream)](https://github.com/gohugoio/hugo/issues)

**Hugo** is a static website generator written in [Go](https://wiki.gentoo.org/wiki/Go "Go"). Hugo is well known for its speed and claims to be the \"worlds fastest\" static website generator. It competes successfully against other \"heavyweight\" content management systems such as [WordPress](https://wiki.gentoo.org/wiki/WordPress "WordPress") when dynamic content isn\'t needed.

Hugo website content is written lightweight human readable document description languages such as Markdown or ASCIIDoc. Configuration can be specified in YAML, TOML, or JSON.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Environment variables]](#Environment_variables)
    -   [[1.4] [Invocation]](#Invocation)
-   [[2] [Create site]](#Create_site)
-   [[3] [Removal]](#Removal)
-   [[4] [See Also]](#See_Also)

## [Installation]

### [USE flags]

### [USE flags for] [www-apps/hugo](https://packages.gentoo.org/packages/www-apps/hugo) [[]] [Fast static HTML and CSS website generator]

  --------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+deploy`](https://packages.gentoo.org/useflags/+deploy)       Enable support for deployment support (hugo deploy)
  [`+extended`](https://packages.gentoo.org/useflags/+extended)   Enable SASS/SCSS support
  [`doc`](https://packages.gentoo.org/useflags/doc)               Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`test`](https://packages.gentoo.org/useflags/test)             Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  --------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-19 20:36] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask www-apps/hugo`

### [Environment variables]

-   `HUGO_NUMWORKERMULTIPLIER` --- By default the number of logical CPUs will be used to set the number of hugo worker processes. This variable overrides that behavior.

### [Invocation]

`user `[`$`]`hugo --help`

      -b, --baseURL string             hostname (and path) to the root, e.g. https://spf13.com/
      -D, --buildDrafts                include content marked as draft
      -E, --buildExpired               include expired content
      -F, --buildFuture                include content with publishdate in the future
          --cacheDir string            filesystem path to cache directory. Defaults: $TMPDIR/hugo_cache/
          --cleanDestinationDir        remove files from destination not found in static directories
          --clock string               set the clock used by Hugo, e.g. --clock 2021-11-06T22:30:00.00+09:00
          --config string              config file (default is path/config.yaml|json|toml)
          --configDir string           config dir (default "config")
      -c, --contentDir string          filesystem path to content directory
          --debug                      debug output
      -d, --destination string         filesystem path to write files to
          --disableKinds strings       disable different kind of pages (home, RSS etc.)
          --enableGitInfo              add Git revision, date, author, and CODEOWNERS info to the pages
      -e, --environment string         build environment
          --forceSyncStatic            copy all files when static is changed.
          --gc                         enable to run some cleanup tasks (remove unused cache files) after the build
      -h, --help                       help for hugo
          --ignoreCache                ignores the cache directory
          --ignoreVendorPaths string   ignores any _vendor for module paths matching the given Glob pattern
      -l, --layoutDir string           filesystem path to layout directory
          --log                        enable Logging
          --logFile string             log File path (if set, logging enabled automatically)
          --minify                     minify any supported output format (HTML, XML etc.)
          --noBuildLock                don't create .hugo_build.lock file
          --noChmod                    don't sync permission mode of files
          --noTimes                    don't sync modification time of files
          --panicOnWarning             panic on first WARNING log
          --poll string                set this to a poll interval, e.g --poll 700ms, to use a poll based approach to watch for file system changes
          --printI18nWarnings          print missing translations
          --printMemoryUsage           print memory usage to screen at intervals
          --printPathWarnings          print warnings on duplicate target paths etc.
          --printUnusedTemplates       print warnings on unused templates.
          --quiet                      build in quiet mode
          --renderToMemory             render to memory (only useful for benchmark testing)
      -s, --source string              filesystem path to read files relative from
          --templateMetrics            display metrics about template executions
          --templateMetricsHints       calculate some improvement hints when combined with --templateMetrics
      -t, --theme strings              themes to use (located in /themes/THEMENAME/)
          --themesDir string           filesystem path to themes directory
          --trace file                 write trace to file (not useful in general)
      -v, --verbose                    verbose output
          --verboseLog                 verbose logging
      -w, --watch                      watch filesystem for changes and recreate as needed

## [Create site]

1\. Run the following command to create a new site named *quickstart*

`user `[`$`]`hugo new site quickstart`

2\. Change into the newly created site directory:

`user `[`$`]`cd quickstart`

3\. Initialize a new Git repository for version control:

`user `[`$`]`git init`

4\. Append the following line to the [config.toml] file to disable any theme:

`user `[`$`]`echo "theme = `*`" >> config.toml`*

5\. Finally, start the Hugo server to preview your site locally:

`user `[`$`]`hugo server`

You can now open your web browser and visit [http://localhost:1313](http://localhost:1313) to view your Hugo site without any theme applied.

## [Removal]

`root `[`#`]`emerge --ask --depclean --verbose www-apps/hugo`

## [See Also]

-   [WordPress](https://wiki.gentoo.org/wiki/WordPress "WordPress")