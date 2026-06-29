# OpenClaw

OpenClaw is an open-source AI agent developed by Peter Steinberger, an Austrian programmer. Users can connect with it through instant messaging tools and remotely control their computers to automate tasks such as email processing, document reading, coding, and posting social media content.

## Installation
Install . For a development build install .

## Official installation method
First, install , , .  can be replaced by its LTS version  or . Then, run in terminal:

 # curl -fsSL https://openclaw.ai/install.sh | bash

One command could finish the whole installation. As of now, the AUR packages are all buggy and unstable, using the official installation method could avoid the bugs introduced by AUR packaging. If you need your OpenClaw to work continuously for a long time, and you don't care whether OpenClaw is manageable by , it is recommended to use the official installation method.

## Installing via nix
Install ，switch to unstable channel，then run:

 # nix-env -iA nixpkgs.openclaw

Note that unless you are using nix to manage other software packages, it is not recommended to use this installation method separately for OpenClaw, as it will result in nix downloading a large number of dependencies that are duplicated with Arch Linux's existing software packages, occupying a lot of disk space.

## Configuration
After installing OpenClaw, run the beginner's guide using the following command:

 # openclaw onboard --install-daemon

For detailed configuration methods, please refer to the official document.

In order to use OpenClaw, you need to prepare a large model API Key, an AI search engine API Key, and an instant messaging software in advance, and you may need to make appropriate deposits for the large model provider. OpenClaw compatible large models, AI search engines, and instant messaging software will all be listed in the beginner's guide. If you haven't prepared in advance, you can also choose and register one during the beginner's guide process.

After the configuration, run

 # openclaw dashboard

to open the control UI in your browser. You can also bookmark the page in your browser and access it directly through the browser.

## Migration
If you reinstall Arch Linux, migrate from other distributions to Arch Linux, migrate from Arch Linux to other distributions, change installation methods, or change computers, then you will need to perform migration work.

First, before the migration, run in the terminal of the old system:

 # openclaw gateway stop

Stop the OpenClaw gateway from running to prevent data changes during the migration process. Then, backup the .openclaw directory in the home directory. Afterwards, install OpenClaw on the new system. If it is the same system, only changing the installation method requires deleting old software packages to avoid conflicts. Afterwards, copy the .openclaw directory to the home directory of the new system. There is no need to run a beginner's guide, but simply run:

 # openclaw doctor

The program will automatically repair the configuration file, and the original data will be retained without the need for reconfiguration. Then, run in the terminal of the new system:

 # openclaw gateway restart

Then you can use OpenClaw on the new system.

## Note
## Data Safety
OpenClaw requires system level permissions to perform tasks, and improper use can lead to various risks such as data leakage, accidental deletion of important data, and virus infection. Some methods to reduce security risks include:

* If you have two or more computers, use one specifically to run OpenClaw while the other computer stores important data. (Physical isolation, safest)
* Run OpenClaw in a sandbox. If you installed OpenClaw via  or , then bubblewrap sandbox is installed as a dependency.
* Install OpenClaw in a Virtual Machine.
* Using Arch and Windows dual system, placing important data in Windows, and not to directly mount the partition where Windows is located. You can even use BitLocker to encrypt the partition where Windows is located to prevent Arch Linux from mounting the partition.

## Updating Notice
OpenClaw is under frequent development, with new versions released almost daily. Some updates may modify certain files, causing existing configurations to malfunction. It is recommended to manually run the command after each update:

 # openclaw doctor

Thus, it can automatically resolve some configuration issues.

## FAQ
## Bash could not find command
Commonly seen in OpenClaw installed using nix, or OpenClaw migrated from nix to other installation methods. Restarting the system will solve the problem.

## An error occurs in prepare while installing
The logic of some files in  has been changed by upstream, but the packager has not yet updated PKGBUILD and openclaw-patch.sh. By now, install  instead.

## No reply in instant messaging software
Ask OpenClaw to self-diagnose.

## Reference
* Official document
