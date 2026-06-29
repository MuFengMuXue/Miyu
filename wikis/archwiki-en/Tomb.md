# Tomb

From the official website:
:Tomb is 100% free and open source software to make strong encryption easy to use.
:A tomb is like a locked folder that can be safely transported and hidden in a filesystem.
:Keys can be kept separate: for instance the tomb on your computer and the key on a USB stick.

Tomb aims to be a really simple to use software to manage "encrypted directories", called tombs. A tomb can only be opened if you both have a keyfile and you know the password.

## Installation
Install  or .

## Usage
Tomb is meant to be used from the console as a single, non-interactive script. it also provides tomb-open, which is a simple interactive script to help you create a tomb, open it, retrieve keys from USB.

Tombs are operated from a terminal command line and require root access to the machine (or just sudo access to the script).

To create a 100 MiB tomb called "secret" do:

 # tomb dig -s 100 secret.tomb
 # tomb forge secret.tomb.key
 # tomb lock secret.tomb -k secret.tomb.key

To open it, do:

 # tomb open secret.tomb -k secret.tomb.key

And after you are done:

 # tomb close

For more information see  and .

## Advanced features
The advanced features are:

* steganography to hide the key inside a jpeg/wav file.
** This feature can be used on its own using .
** If an attacker assumes you are using this feature (i.e., searching for ) they can scan your system using .
* bind hooks: can automatically apply a  to a subdirectory inside a tomb with the  operation to one outside. Suppose, for example, you would like to encrypt your  directory. Then you can create a tomb which contains it (and others too, if you want) and create a simple configuration file inside the tomb itself. When you run  it will automatically bind the directories into the right places. This way you will easily get an encrypted documents folder, browser profile, or maildir.
* post hooks: commands that are run when the tomb is opened, or closed. You can imagine lot of things for this: open files inside the tomb, put your computer in a "paranoid" status (for example, disabling swap), etc.
