# Out-of-the-Box Experience

Out-of-the-Box Experience is a setup process before a login manager where a new computer can be configured instead of doing it during install.

## Installation
Install the  package for GDM or  for .

## Configuration
## GDM
First enable GDM. Initial Setup uses GDM to run. Ensure that the system has no user accounts. GDM will detect the absence of users on boot and launch
.

## Plasma Login Manager
Enable . Next time the computer is booted it will run the setup to create a new user, set system locale and set the theme. After finishing it will create  to signify that the setup has run.
