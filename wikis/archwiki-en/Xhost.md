# Xhost

From Xhost man page (boldface added):

: The xhost program is used to add and delete host names or user names to the list allowed to make connections to the X server. In the case of hosts, this provides a rudimentary form of privacy control and security. It is only sufficient for a workstation (single user) environment, although it does limit the worst abuses. Environments which require more sophisticated measures should implement the user-based mechanism or use the hooks in the protocol for passing other authentication data to the server.

See  for the full info.

## Installation
Install the  package.

## Usage
To provide access to an application running with sudo or su to the graphical server (aka your X session aka your computer screen), open a terminal and type as your normal user:

 $ xhost +SI:localuser:username

To get things back to normal, with controlled access to the X screen:

 $ xhost -

 will disable X authentication entirely. Do not do that unless you really know what are you doing.

## The 'cannot connect to X server :0.0' output
The above command  will get you rid of that output, albeit momentarily; one way of getting permanently rid of this issue, among many, is to add

 xhost + > /dev/null

to your  file. This way, each time you fire up the terminal, the command gets executed. If you do not yet have a  file in your home directory, it is OK to create one with just this line in it. If you do not add  then each time you fire a terminal, you will see a non-disruptive message saying: access control disabled, clients can connect from any host, which is your confirmation that you can now run your_software as root without issue.
