## [chmod]

Adminstrators can change file permissions with:

`user `[`$`]`chmod [u][g][o] [file]`

-   \[u\] is the number for user permissions
-   \[g\] is the number for group permissions
-   \[o\] is the number for other users permissions

Numbers are obtained in the following way:

-   7 = 4 + 2 + 1 (read/write/execute)
-   6 = 4 + 2 (read/write)
-   5 = 4 + 1 (read/execute)
-   4 = 4 (read)
-   3 = 2 + 1 (write/execute)
-   2 = 2 (write)
-   1 = 1 (execute)

## [chown]

Administrators can change owner and group of a file with:

`root `[`#`]`chown [user]:[group] [file]`

Administrators can change owner of a folder and files inside recursively with:

`root `[`#`]`chown -R [user]:[group] [folder]`

## [gpasswd]

Administrators can add a user to a group with:

`root `[`#`]`gpasswd -a [user] [group]`

Administrators can remove a user from a group with:

`root `[`#`]`gpasswd -d [user] [group]`