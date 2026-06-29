# Back In Time

From upstream:

:Back In Time is an easy-to-use tool to backup files and folders. It runs on GNU/Linux (not on Windows or OS X/macOS) and provides a command line tool backintime and a GUI backintime-qt both written in Python3. It uses rsync to take manual or scheduled snapshots and stores them locally or remotely through SSH. Each snapshot is in its own folder with copies of the original files, but unchanged files are hard-linked between snapshots to save storage space. It was inspired by FlyBack.

## Installation
Install  for the GUI version or  for a CLI-only version.

## Usage
For the graphical interface (GUI) run backintime-qt. For the command line interface (CLI), run backintime.

For the GUI version two starters are installed in your desktop environment: Back In Time and Back In Time (root). The latter will start the GUI with root privileges (using ) and can be used to backup files other than the current user's own files in .

## Enable scheduling
The scheduling of backup jobs is realized using cron.

By default, no service are automatically enabled: you will need to enable the cron service relevant to the cron provider you have installed.
