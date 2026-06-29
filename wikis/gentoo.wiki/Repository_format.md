A quick reference to Gentoo ebuild repository (overlay) format.

Tree

    <repository location>
    ├── <category>/
    │   └── <name>/
    │       ├── <name>-<version>.ebuild
    │       ├── ...
    │       ├── Manifest
    │       ├── metadata.xml
    │       └── files/
    ├── ...
    ├── eclass/
    ├── licenses/
    ├── metadata/
    │   └── layout.conf
    └── profiles/
        ├── ...
        ├── license_groups
        ├── package.mask
        └── repo_name

Each ebuild repository has its own `repository location``. It is set in `[`repos.conf`](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf")` and can be found with the `[[`portageq`](https://wiki.gentoo.org/wiki/Portageq "Portageq")]` utility: `

`user `[`$`]`portageq get_repo_path / gentoo`

    /var/db/repos/gentoo

## [See also]

-   [/etc/portage](https://wiki.gentoo.org/wiki//etc/portage "/etc/portage") --- the primary configuration directory for [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), Gentoo\'s package manager.
-   [/etc/portage/repos.conf](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf") --- specifies current [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") configured repositories\' location and settings