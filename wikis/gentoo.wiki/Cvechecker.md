**Resources**

[[]][Home](https://github.com/sjvermeu/cvechecker)

[[]][Official documentation](https://github.com/sjvermeu/cvechecker/wiki)

** Note**\
This project has been abandoned since 2022 and may not be up-to-date.

**cvechecker** is a small utility that provides reports on potentially vulnerable software.

cvechecker is for Gentoo systems and written and is maintained by former Gentoo developer [Sven Vermeulen (SwifT) ](https://wiki.gentoo.org/wiki/User:SwifT "User:SwifT").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Manual installation]](#Manual_installation)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [User account]](#User_account)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Database initialization]](#Database_initialization)
    -   [[3.2] [Invocation]](#Invocation)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

### [Manual installation]

Installation is possible via swift\'s overlay. Use [eselect repository](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository") (or equivalent) to add the [unregistered repository](https://wiki.gentoo.org/wiki/Eselect/Repository#Add_unregistered_repositories "Eselect/Repository"):

`root `[`#`]`eselect repository add sjvermeu git https://github.com/sjvermeu/gentoo.overlay`

Perform the initial sync:

`root `[`#`]`emaint sync -r sjvermeu`

Emerge the package:

`root `[`#`]`emerge --ask app-admin/cvechecker`

## [Configuration]

### [User account]

Upstream instructions suggest creating a service account to run [cvechecker].^[\[1\]](#cite_note-1)^

## [Usage]

Quick start instructions can be [found upstream](https://github.com/sjvermeu/cvechecker).

### [Database initialization]

The initial pull of the database using the below command will take some time and is synced into the [/var/lib/cvechecker/cache/] directory:

`root `[`#`]`pullcves pull`

** Note**\
As of April 14th, 2021, the [cache/] (902.6 MiB) and [local/] (142.7 MiB) directories are just over 1 GiB.

### [Invocation]

`user `[`$`]`cvechecker --help`

    Usage: cvechecker [OPTION...]
    cvechecker -- Verify the state of the system against a CVE database

      -b, --binlist=binlist      List of binary files on the system
      -c, --cvedata=cvefile      CSV file with CVE information (cfr. nvd2simple)
      -C, --csvoutput            Use (parseable) CSV output
      -d, --deltaonly            Given binaries or lists should be added only (not
                                 a full replacement)
      -D, --deletedeltaonly      Given binaries or lists should be removed (not a
                                 full replacement)
      -f, --fileinfo=binfile     File to obtain detected CPE of
      -H, --reporthigher         Report also when CVEs have been detected for
                                 higher versions
      -i, --initdbs              Initialize all databases
      -l, --loaddata=datafile    Load version gathering data file
      -r, --runcheck             Execute the checks (match installed software with
                                 CVEs)
      -s, --showinstalled        Output detected software/versions
      -S, --showinstalledfiles   Output detected software/versions with file
                                 information
      -w, --watchlist=watchlist  List of CPEs to watch for (assume these are
                                 installed)
      -?, --help                 Give this help list
          --usage                Give a short usage message
      -V, --version              Print program version

    Mandatory or optional arguments to long options are also mandatory or optional
    for any corresponding short options.

    Report bugs to <sven.vermeulen@siphos.be>.

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-admin/cvechecker`

## [See also]

-   [Greenbone Vulnerability Management](https://wiki.gentoo.org/wiki/Greenbone_Vulnerability_Management "Greenbone Vulnerability Management") --- a network security scanner with associated tools like a graphical user front-end.

## [External resources]

-   Author\'s blog: [https://blog.siphos.be/](https://blog.siphos.be/)

1.  [[[↑](#cite_ref-1)] [[https://github.com/sjvermeu/cvechecker/wiki/Installation](https://github.com/sjvermeu/cvechecker/wiki/Installation)]]