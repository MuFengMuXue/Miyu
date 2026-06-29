# Su

The su core utility (substitute user) is used to assume the identity of another user on the system, root by default.

See PAM for ways to configure sus behavior.

## Installation
su is part of the  package.

## Usage
To assume the login of another user, pass the username that you want to become to su, as in:

 $ su username

By default, when running as a regular user, you will be prompted for the password of the user you are attempting to become. When running su as root, no password is required.

If no username is passed, su assumes the root user, and the password for which you are prompted will be that of root.

For more information, see .

## Tips and tricks
## Login shell
The default behavior of su is to remain within the current directory and to maintain the environment variables of the original user (rather than switch to those of the new user).

Note the following important contrasting considerations:

* It sometimes can be advantageous for a system administrator to use the shell account of an ordinary user rather than its own. In particular, occasionally the most efficient way to solve a user's problem is to log into that user's account in order to reproduce or debug the problem.
* However, in many situations it is not desirable, or it can even be dangerous, for the root user to be operating from an ordinary user's shell account and with that account's environment variables rather than from its own. While inadvertently using an ordinary user's shell account, root could install a program or make other changes to the system that would not have the same result as if they were made while using the root account. For instance, a program could be installed that could give the ordinary user power to accidentally damage the system or gain unauthorized access to certain data.

Thus, it is advisable that administrative users, as well as any other users that are authorized to use su (and it is suggested that there be very few, if any) acquire the habit of always running the su command with the / option. It has two effects:

# Switches from the current directory to the home directory of the new user (e.g., to  in the case of the root user) by logging in as that user.
# Changes the environment variables to those of the new user, as dictated by their shell runtime configuration file. That is, the current directory and environment will be changed to what would be expected if the new user had actually logged on to a new session (rather than just taking over an existing session).

Thus, administrators should generally use su as follows:

 $ su -l

An identical result is produced by adding the username root:

 $ su -l root

Likewise, the same can be done for any other user (e.g. for a user named archie):

 # su -l archie

To log into a passwordless user, first log in as root and then log into the passwordless user account from the root shell:

 $ su -l
 # runuser -l archie

## su and wheel
BSD su allows only members of the  user group to assume root's identity by default. This is not the default behavior of GNU su, but this behavior can be mimicked using PAM. Uncomment the appropriate line in  and :

 auth required pam_wheel.so use_uid

## Nologin users
You cannot run commands as an other user by simply using  if they are not allowed to login (i.e. they have  or  set as their shell).

You can work around this by specifying the shell to use:

 # su -s /usr/bin/bash nologin_user
