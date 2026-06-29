# Rebuilderd

rebuilderd is an independent verification system for binary packages. It allows verification of pre-compiled packages by repeating the build step in an identical environment and then verifies that the package is identical. Right now only Arch Linux packages can be verified.

If you run a rebuilder or consider running a rebuilder feel free to join the #archlinux-reproducible IRC channel.

## Installation
Install the  package.

## Configuration
## Single machine
On a single machine you just enable  and the worker service(s): .

Afterwards you can verify rebuilderd is correctly running with a single worker by running:

 # rebuildctl status

If you get an error that no authentication cookie could be found, you might need to add yourself to the  user group.

Continue with the next section to sync packages that our worker can rebuild.

## Multi-node rebuilder
To run a multi-node rebuilder network we need at least two servers:

; rebuilderd daemon
: This one only needs very few resources (a CX11 instance is fine), it keeps track of all packages, coordinates the workers and serves results to clients.
:
; rebuilderd worker
: This server runs the actual builds. This server should have at least 16 GiB RAM, if you want to build all packages this should be closer to 32 GiB.

The worker needs to authenticate itself to the daemon with a secret signup key (). This key can be generated with .

You can also generate a second secret to use rebuildctl remotely (). This is optional, you can also run rebuildctl on the server after adding yourself to the  group.

Start and enable .

Next we head over to our worker machines to set them up. Install  as well and edit :

We can start the worker unit multiple times for concurrent rebuilds (if the machine has enough resources). We are going to start with just one worker (and call it ) by starting/enabling

## Syncing packages to rebuild
The rebuilder setup will not do anything by default until you explicitly configure where to sync packages from. The sync profiles are configured in . The profile names are supposed to be unique. You configure it to only build packages of a specific maintainer with the  option. By default it is importing packages of all maintainers.

Afterwards you can enable  to automatically sync the profile.

## Ansible playbook
An Ansible playbook with a rebuilderd role can be found in Arch Linux's infastructure repository. Use this as inspiration as the Ansible repository is heavily dependent on how the Arch Linux infrastructure is set up.

## Tips and tricks
## Requeueing failed builds
Starting with rebuilderd 0.5.0 failed builds are retried automatically with increasing delays. You can retry packages immediately with:

 # rebuildctl pkgs requeue --suite core --status BAD

In older versions you had to use this command to add all failed builds to the queue again:

 # rebuildctl pkgs ls --distro archlinux --suite core --status BAD --json | jq -r '.| xargs -L1 rebuildctl queue push archlinux core

## Removing suites after being synced
Currently, using rebuildctl is not possible to remove whole suites after they have been synced once. However, this can be achieved by setting a filter that does not match on any packages before removing the sync profile. For example, adding the following maintainers filter will effectively remove the core suite from rebuilderd.

## Package rebuilders
Rebuilders using rebuilderd:

{| class="wikitable"
! URL!! Contact !! Comment
|-
| https://reproducible.archlinux.org/
| jelle
|
|-
| https://wolfpit.net/rebuild/
| wahrwolf
|
|-
| https://r-b.engineering.nyu.edu/
| [https://ssl.engineering.nyu.edu/ NYU Secure Systems Lab
|-
| https://rebuilder.pitastrudl.me/
| pitastrudl
| Contact on IRC Libera or pitastrudl@chaos.social
|-
| https://reproducible.crypto-lab.ch/
| Applied Cyber Security Research Lab (HSLU)
| Contact iyanmv on #archlinux-reproducible
|}
