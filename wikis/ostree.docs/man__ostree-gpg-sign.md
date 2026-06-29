## Name

ostree-gpg-sign — Sign a commit

## Synopsis

`ostree gpg-sign` \[OPTIONS...\] {COMMIT} {KEY-ID...}

## Description

Add a new signature to a commit for each specified GPG key. Note that currently, this will append a new signature even if the commit is already signed with a given key.

## Options

`--delete`  
Delete signatures having any of the GPG KEY-IDs.

`--gpg-homedir`="HOMEDIR"  
GPG Homedir to use when looking for keyrings.
