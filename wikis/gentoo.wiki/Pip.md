This page contains [[changes](https://wiki.gentoo.org/index.php?title=Pip&diff=1412956)] which are not marked for translation.

**Resources**

[[]][Home](https://pip.pypa.io/en/stable/)

[[]][Package information](https://packages.gentoo.org/packages/dev-python/pip)

[[]][GitHub](https://github.com/pypa/pip)

**pip** is [Python](https://wiki.gentoo.org/wiki/Python "Python")\'s package management system. It references packages available in the official **Py**thon **P**ackage **I**ndex (PyPI).

** Warning**\
Running [pip] as root is not advised. It can render important system tools like [emerge] useless.^[\[1\]](#cite_note-1)^

## Contents

-   [[1] [Install]](#Install)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Package installation]](#Package_installation)
-   [[3] [Removal]](#Removal)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [Install]

### [Emerge]

Install [[[dev-python/pip]](https://packages.gentoo.org/packages/dev-python/pip)[]]:

`root `[`#`]`emerge --ask dev-python/pip`

## [Usage]

In order for [pip] to operate correctly when installing new packages an active internet connection is a requirement.

### [Invocation]

`user `[`$`]`pip --help`

    Usage:
      pip <command> [options]

    Commands:
      install                     Install packages.
      download                    Download packages.
      uninstall                   Uninstall packages.
      freeze                      Output installed packages in requirements format.
      list                        List installed packages.
      show                        Show information about installed packages.
      check                       Verify installed packages have compatible dependencies.
      config                      Manage local and global configuration.
      search                      Search PyPI for packages.
      cache                       Inspect and manage pip's wheel cache.
      wheel                       Build wheels from your requirements.
      hash                        Compute hashes of package archives.
      completion                  A helper command used for command completion.
      debug                       Show information useful for debugging.
      help                        Show help for commands.

    General Options:
      -h, --help                  Show help.
      --isolated                  Run pip in an isolated mode, ignoring environment variables and user configuration.
      -v, --verbose               Give more output. Option is additive, and can be used up to 3 times.
      -V, --version               Show version and exit.
      -q, --quiet                 Give less output. Option is additive, and can be used up to 3 times (corresponding to WARNING, ERROR, and CRITICAL logging levels).
      --log                 Path to a verbose appending log.
      --proxy              Specify a proxy in the form [user:passwd@]proxy.server:port.
      --retries <retries>         Maximum number of retries each connection should attempt (default 5 times).
      --timeout <sec>             Set the socket timeout (default 15 seconds).
      --exists-action <action>    Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort.
      --trusted-host <hostname>   Mark this host or host:port pair as trusted, even though it does not have valid or any HTTPS.
      --cert                Path to alternate CA bundle.
      --client-cert         Path to SSL client certificate, a single file containing the private key and the certificate in PEM format.
      --cache-dir <dir>           Store the cache data in <dir>.
      --no-cache-dir              Disable the cache.
      --disable-pip-version-check
                                  Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index.
      --no-color                  Suppress colored output
      --no-python-version-warning
                                  Silence deprecation warnings for upcoming unsupported Pythons.

### [Package installation]

** Warning**\
[pip] should not be used for package installation outside of a *virtual environment*. Doing so can break parts of the local Python installation. Even using [pip install] with the `--user` parameter can break things, as packages installed in this way will still be included in [sys.path]. Accordingly, pip will print an error message if called outside of a virtual environment. See [PEP 668](https://peps.python.org/pep-0668/) and [externally managed environments](https://packaging.python.org/en/latest/specifications/externally-managed-environments/) for details.

** Important**\
It is important to understand that packages installed using [pip] will not be tracked by Portage, which can lead to conflicts.

To install `package` using the [pip] command, first create and activate a virtual environment:

`user `[`$`]`python -m venv /path/to/venv `

`user `[`$`]`source /path/to/venv/bin/activate`

** Important**\
The `activate` script must be used with `source`. *It should not be run directly.*

Then install into the virtual environment:

`user `[`$`]`pip install `

To exit the virtual environment, run:

`user `[`$`]`deactivate`

The virtual environment is not deleted, and can be re-entered by re-sourcing the [activate] file (with the command beginning with the period).

To make a library installed in a virtual environment available to other software in that environment, add the relevant path to the `PYTHONPATH`:

`user `[`$`]`export PYTHONPATH="$:/path/to/venv/lib/python-<version>/site-packages/"`

To create a virtual environment with access to the system packages (i.e. the packages installed via Portage), use the `--system-site-packages` option when creating the environment:

`user `[`$`]`python -m venv --system-site-packages /path/to/venv`

Once the virtual environment has been activated, confirm that the system packages are available by running `pip list`.

## [Removal]

Again, this should probably only ever be used in a virtual environment.

To remove a package using [pip]:

`user `[`$`]`pip uninstall `

## [See also]

-   [Application level package management](https://wiki.gentoo.org/wiki/Application_level_package_management "Application level package management") --- provides best practice recommendations on managing the coexistence of operating system and **application level package managers** on Gentoo.
-   [Gem](https://wiki.gentoo.org/wiki/Gem "Gem") --- programs and libraries for the [Ruby](https://wiki.gentoo.org/wiki/Ruby "Ruby") programming language.
-   [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") --- the official [package manager](https://en.wikipedia.org/wiki/Package_manager "wikipedia:Package manager") and [distribution system](https://www.gentoo.org/get-started/about/) for Gentoo.
-   [Project:Python/Dependencies](https://wiki.gentoo.org/wiki/Project:Python/Dependencies "Project:Python/Dependencies") - How to turn PyPI dependencies to those of ebuild.

## [External resources]

-   [Externally managed environments](https://packaging.python.org/en/latest/specifications/externally-managed-environments/)
-   [PEP 668](https://peps.python.org/pep-0668/)
-   [Python/Virtual environment](https://wiki.archlinux.org/index.php/Python/Virtual_environment) (ArchWiki article) - Isolated Python\'s environment, enabling sandboxed installation of packages.
-   [pipx - Install and Run Python Applications in Isolated Environments](https://github.com/pypa/pipx)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://forums.gentoo.org/viewtopic-t-1006016.html](https://forums.gentoo.org/viewtopic-t-1006016.html)]]