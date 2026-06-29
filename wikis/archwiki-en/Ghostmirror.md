# Ghostmirror

GhostMirror can generate a mirror list from the most recent mirrors, compare them with the local mirror, and indicate whether they are outdated, identical, or more up-to-date than the current local mirror in use.

It can:

* perform speed tests using ping and download methods.
* analyze a non-working mirror to identify potential issues, a feature particularly useful for mirror maintainers.
* function as a systemd service, automatically determining when mirrors need to be rechecked.

The main difference with Reflector is that Ghostmirror does not consider lastsync reliable, so it downloads the mirror databases and compares them, showing the actual state of a mirror. For speed, in addition to ping, Ghostmirror downloads packages to detect the actual speed of the mirror; the result is therefore more accurate.

## Installation
Install the  package.

## Usage
To see all of the available options, run the following command:

 $ ghostmirror --help

## Best mirror
If your mirror list already contains a good number of mirrors that you consider valid, you can skip this step. From the developer's experience, a good number is more than 20, but anywhere from 1 to more than 100 is possible.

Search for reliable mirrors to include in your list:

*  show a progress and show a colorful table.
*  select country, to find good mirrors, it is common to search within your own country and neighboring ones.
: The more mirrors you add, the slower the search might become, but this operation does not need to be done periodically—it's just an initial sift through the countless mirrors available.
*  the path where you want to save the new mirror list.
*  max numbers of output mirror in list.
*  sort mode, to remove erroneous mirrors, add  as the first sort mode, then  displays first the mirror sync, adding  ensures you never go out of sync, and at the end  to try to prioritize the closest ones.

 $ ghostmirror -Po -c Italy,Germany,France -l ./mirrorlist.new -L 30 -S state,outofdate,morerecent,ping

The estimated field will not provide an optimal value without a speed test, but for finding a stable mirror, it is not necessary. If the operation is particularly slow, you can try increasing the number of simultaneous downloads with .

## Sort mirrors
Once you have a good mirror list, you can perform periodic checks to reorganize it and continue using the best mirrors based on your usage patterns.

Keeping the options  of the previous command:

*  sets the path to the mirror list and use only un-commented mirror.
*  apply test for mirror speed.

We need to change the sorting method. While we were previously looking for the closest mirrors, now we will focus on finding the most stable and fastest ones.

 $ ghostmirror -Po -mu ./mirrorlist.new -l ./mirrorlist.new -s light -S state,outofdate,morerecent,estimated,speed

Now you can copy the file so that pacman makes use of it:

 # cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak
 # cp ./mirrorlist.new /etc/pacman.d/mirrorlist

## Directly replace the mirror list
Instead of running the command as a user, you can execute it as root to work directly on the .

## Automation
Sorting mirrors can be automated using systemd timers, specifically, use the  functionality for automation. Linger will be automatically activated along with its configuration files—you just need to run the appropriate command.

## Preparation
You need to manual create a directory for the mirror list, where your user can edit it without root privilege:

 $ mkdir ~/.config/ghostmirror

It can then be added to your pacman configuration file:

## Activate
Create a mirror list in  (see #Best mirror) or simple copy from .

The following command with  enables linger if it is not already enabled, creates a new mirror list, starts the timer, and will be reused for subsequent automatic mirror checks.

 $ ghostmirror -DPo -mul ~/.config/ghostmirror/mirrorlist ~/.config/ghostmirror/mirrorlist -s light -S state,outofdate,morerecent,estimated,speed

By default, it uses the first element of the estimated time to determine when the service should run again.
You can choose to add a time in the format  (which defaults to ).
If you do not want to use the estimated time but a fixed period to refresh the mirrors, you can use a fixed date with .

Before using these parameters, check if the values are correct with:

 $ systemd-analyze calendar date_to_check

## systemd
See Systemd/Timers#Management for details on viewing started timers.

To force a refresh of the mirror list, start the  user unit instead of waiting for the timer to run it.

## Analyzer
To analyze mirrors, simply add the  option to check if the mirror redirects to another server, verify if the URLs are correct, the errors reported by the mirror, and optionally the package names that have not been synchronized.

For example to investigate only in specific mirror list:

 $ ghostmirror -Pomui ./mirrorlist.maintainer all
