## Name

ostree-admin-set-origin — Change the "origin" (location for upgrades)

## Synopsis

`ostree admin set-origin ` {REMOTENAME} {URL} \[BRANCH\]

## Description

Add a new remote named *`REMOTENAME`* (if it does not already exist). Then change the origin file for the current deployment. This is the ref that will be "tracked" and upgraded with **ostree admin upgrade**.

## Options

`--set`=KEY=VALUE  
Set an option for the remote.

`--index`=INDEX  
Change the origin of the deployment numbered *`INDEX`* (starting from 0).

## Example

**\$ ostree admin set-origin exampleos http://os.example.com/repo exampleos/10.0/main/router**
