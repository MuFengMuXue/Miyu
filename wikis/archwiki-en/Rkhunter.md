# Rkhunter

rkhunter (Rootkit Hunter) is a security monitoring tool for POSIX compliant systems. It scans for rootkits, and other possible vulnerabilities. It does so by searching for the default directories (of rootkits), misconfigured permissions, hidden files, kernel modules containing suspicious strings, and comparing hashes of important files with known good ones.

It is written in Bash, to allow for portability, and can run on most UNIX-based systems.

## Installation
Install the  package.

## Configuration
## Initial setup
Prior to running rkhunter for the first time, update the file properties database:

 # rkhunter --propupd

## Important files
The main configuration file is located at .

By default, a log of the last system check will be placed at .

## Usage
See  for full details.

## Basic commands
To update the file properties database:
 # rkhunter --propupd

It is necessary to ensure that the rkhunter data files are kept up-to-date by running:
 # rkhunter --update

To run a system check:
 # rkhunter --check --sk

To validate the configuration file(s):
 # rkhunter --config-check

## Troubleshooting
## False positives
Out of the box, Rootkit Hunter will throw up some false warnings during the file properties check. This occurs because a few of the core utilities have been replaced by scripts. These warnings can be muted through white-listing:

## External documentation
* Rootkit Hunter Homepage
* Rootkit Hunter README
* Rootkit Hunter FAQ

## Related Wikipedia pages
* rkhunter
* Host-based intrusion detection system (HIDS)
* Intrusion detection system (IDS)
