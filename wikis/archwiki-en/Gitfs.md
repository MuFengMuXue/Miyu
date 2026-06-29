# Gitfs

From gitfs:
:gitfs is a FUSE file system that fully integrates with git. You can mount a remote repository’s branch locally, and any subsequent changes made to the files will be automatically committed to the remote.
:You can mount any repository, and all the changes you make will be automatically converted into commits. gitfs will also expose the history of the branch you’re currently working on by simulating snapshots of every commit.
:gitfs is useful in places where you want to keep track of all your files, but at the same time you don’t have the possibility of organizing everything into commits yourself. A FUSE file system for git repositories, with local cache.

## Installation
Install .

## Usage
gitfs enables a user to mount a remote git repository as a FUSE filesystem, for example:
 $ gitfs https://example.com/repository.git /mount/directory

See its documentation for options.

## Troubleshooting
## Write access to /var/lib/gitfs
 needs to exist and is not automatically created. Also, if you want to mount gitfs as a regular user, make sure to make it writable for that user:
 # mkdir /var/lib/gitfs
 # chown username:users /var/lib/gitfs

## Write access to pygit2
On first run gitfs tries to do some self-introspection which fails, if you run it as a regular user. To remedy this, run it once as root. You do not need to actually mount anything. It is enough to show the help message as root:

 # gitfs -h

## Options for use with ssh key
Gitfs (and pygit2 on which it relies) seems to be under heavy development and options change.
Although the official docs state that the option  can be used to change the key, it turns out that version 0.4.1-1 from AUR requires the use of .
Note that gitfs will not ask for a passphrase, if the key is passphrase protected. It simply returns with the error:
 _pygit2.GitError: Failed to authenticate SSH session: Callback returned error
It is recommended to create a separate key for this by issuing:
 ssh-keygen
 /home/user/.ssh/gitfs_rsa
