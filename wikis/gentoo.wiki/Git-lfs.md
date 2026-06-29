**Resources**

[[]][Home](https://git-lfs.github.com/)

[[]][Package information](https://packages.gentoo.org/packages/dev-vcs/git-lfs)

[[]][Official documentation](https://github.com/github/git-lfs/wiki)

[[]][GitHub](https://github.com/github/git-lfs)

Git **L**arge **F**ile **S**torage (LFS) is an open source plugin created by GitHub that enables the [[git](https://wiki.gentoo.org/wiki/Git "Git")] version control system to better track binary blobs. It does so by creating a text-based reference to the blob, then tracking and storing the blob in a location external to the git repository itself; typically on a content server.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
    -   [[1.2] [Configuration]](#Configuration)
-   [[2] [Usage]](#Usage)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)
-   [[4] [See also]](#See_also)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask dev-vcs/git-lfs`

### [Configuration]

In order to use git-lfs, your \~/.gitconfig file must be setup with the appropriate filters. Run the following command to do this automatically.

`user `[`$`]`git lfs install --skip-repo`

## [Usage]

Binary files must be tracked by file extension. This enables git LFS to make proper distinctions between binary and non-binary files.

GitHub has released a video on YouTube explaining how to utilize git LFS: [https://www.youtube.com/watch?v=uLR1RNqJ1Mw](https://www.youtube.com/watch?v=uLR1RNqJ1Mw)

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose dev-vcs/git-lfs`

You will want to manually remove everything under \[filter \"lfs\"\] in \~/.gitconfig.

## [See also]

-   [Git](https://wiki.gentoo.org/wiki/Git "Git") --- widely used, open source, distributed [version control system](https://wiki.gentoo.org/wiki/Version_control_systems "Version control systems")