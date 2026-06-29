### [Problem Description]

Some packages open many files at the same time during build time. The Gentoo default setting on 2024-02-09 is 1024.

`user `[`$`]`ulimit -n`

### [Tracking problematic packages]

Reports about packages which exceeded the limit of max open files are tracked in [[[bug #924186]](https://bugs.gentoo.org/show_bug.cgi?id=924186)[]]

### [Solutions]

-   As user one can increase the max number of open files

`root `[`#`]`ulimit -n 4096`