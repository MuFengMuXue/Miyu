# Locate

locate is a common Unix tool for quickly finding files by name. It offers speed improvements over the find tool by searching a pre-constructed database file, rather than the filesystem directly. The downside of this approach is that changes made since the construction of the database file cannot be detected by . This problem can be minimised by scheduled database updates.

Over time, alternative implementations have replaced one another, from slocate (secure locate) that only showed files accessible to the user, to mlocate (merging locate) that merges databases at each update (which offers a performance speedup since it can skip previously examined files). The most recent iteration is plocate (posting locate), which is based on posting lists, consuming the database ahead of time, thus making a much faster (and smaller) index out of it.

## Installation
Install the  package.

While the GNU findutils also include a locate implementation, Arch's  package does not.

## Usage
Before  can be used, the database will need to be created, this is done with the  command, which (as the name suggests) updates the database.

 contains a  unit, which invokes a database update each day and is enabled upon installation. Start it manually if you want to use it before reboot. You can also manually run updatedb as root at any time.

To save time, updatedb can be (and by default is) configured to ignore certain filesystems and paths by editing .  describes the semantics of this file. It is worth noting that among the paths ignored in the default configuration () are  and , so locate may not discover files on external devices.

## Troubleshooting
## Btrfs
The default configuration prevents Btrfs filesystems from being included in the results. To allow including btrfs mountpoints, add:

Note of course that this also means other bind mountpoints also will be included. If you need to exclude these mountpoints, the  setting in the same configuration file can be used.
