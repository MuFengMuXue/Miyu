# Docs / Kwallet Query / Man Kwallet Query.1

Valentin

Rusu

Original author

kde@rusu.info

2015-06-14

Frameworks 5.11

KDE Frameworks

kwallet-query

1

kwallet-query

Wallet command-line manipulation tool

**kwallet-query** *OPTIONS* *wallet*

# DESCRIPTION

`kwallet-query` comes in handy when shell scripts need to read or update the Wallet. It works by manipulating the entries displayed in the **Wallet Manager** utility. It’s only parameter is the *wallet*name the tool should read or update. The operation mode is specified by the options.

# OPTIONS

**-h,--help**
Display a short help message.

**-l,--list-entries**
List password entries. These are the folder names displayed in the **Wallet Manager** utility. If the **-f** option is given, this will only display the subfolders of the specified folder.

**-r,--read-password** *Entry*
Read the contents of the given *Entry* from the **Folder**section of the *wallet* and output it on the standard output. Maps are exported as object.

**-w,--write-password** *Entry*
Write secrets to the given *Entry* under the **Folder** section of the given *wallet*. The secrets are read from the standard input. Maps take in input a well-formed object. **IMPORTANT** previous wallet entry value will be overwritten by this option, so be careful when using it!

**-f,--folder** *Folder*
Set the *wallet* folder to *Folder* value. By default **Passwords** is used.

**-v,--verbose**
Output more information when performing the operation, to help debugging.

# EXIT STATUS

**0**
Success.

**1**
The wallet *wallet* was not found.

**2**
The wallet *wallet* could not be opened. For example, that would be an indication of a bad password entry or some other problem with the Wallet system.

**3**
The **Folder** section was not found inside the wallet *wallet*. Perhaps the wallet file is corrupt?

**4**
The read or write operation has failed for some reason.

# BUGS

Please report all bugs on the bug reporting website: bugs.kde.org. Be sure to select “kwallet-query” when submitting your bug-report.

# AUTHOR

`kwallet-query` was originally written by Valentin Rusu and is part of .

# COPYING

Copyright (C) 2015 Valentin Rusu. Free use of this software is granted under the terms of the General Public License (GPL).
