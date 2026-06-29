# Git server

This article gives an overview on how to host a Git server. For more information, refer to the Git on the Server chapter of the Pro Git book.

## Protocols
Refer to Git on the Server - The Protocols for a detailed description along with pros and cons.

## SSH
You only need to set up an SSH server.

## Normal existing user account
This is the easiest approach, if your ssh login works:
* Create a bare repository on the Server, wherever you have write permission.
 $ git init --bare ~/foo
* Clone the repo on a different Machine.
 $ git clone ssh://sshserver:foo

## Restricted login shell for Git-only SSH access
If you want to limit the amount of available commands for a user account then  is one way. Multiple user could share one ssh account, just add all keys in .

To create a interactive login shell with few limited commands, other than git repo management, you need something like this:

 $ mkdir ~/git-shell-commands
 $ cd ~/git-shell-commands
 $ ln -s /usr/share/git/git-shell/commands/help
 $ ln -s /usr/share/git/git-shell/commands/list

Finally change the shell:

 # chsh -s /usr/bin/git-shell username

An example shell script to create new bare repos could be:

{{hc|1=~/git-shell-commands/new_repo|2=#!/bin/sh

new_repo() {
        local repo_name
        repo_name="${1}"
        if  -e "${repo_name}" ;then
                printf 'Please provide a different repo name.\n'
                exit 1
        fi
        if  "x${repo_name}" = "x" ;then
                printf 'Please providea a repo name.\n'
                exit 2
        fi
        git init --bare "${repo_name}"
}

new_repo "${1}"
}}

 $ chmod u+rx ~/git-shell-commands/new_repo

Also it could be beneficial in some scenarios to restrict things like port forwarding.

Prepend all keys in authorized_keys with:

## Restricted user account
You are able to secure the SSH user account even more allowing only push and pull commands on this user account. This is done by replacing the default login shell by git-shell. Described in Setting Up the Server.

When securing the git server created with the instructions of this clause (#SSH), the following additional steps are needed on Arch:

#Change the home directory: In order for ssh to be able to read , the home directory for git in  needs to be changed from  to .
#Change the base path when home directory is corrected: In order for git to serve the repositories, the  in  need to be changed to  if the repositories are served from git's home directory.

## Git daemon service (git://)
The Git daemon () can be started with .

The service uses the  and  parameters to serve all repositories placed in .

## Modify git services (per-repository) / Write anonymous push to repo
 uses the  service and is per default disabled. In the repo/config file enable .

All repos can be cloned/pulled by default, because the service is enabled with  by default, but you can be disabled it. Read more .

## Enable error messages for clients
Instead of getting the default Error Message  and get more specific error. Create a drop-in file for the  and append  in the ExecStart like:

## Error Messages server
 # journalctl -t git-daemon

## Dumb HTTP
"Dumb" in this context means that only WebDAV is involved in pulls and pushes.

## nginx
Follow the basic WebDAV instructions for nginx. Pushing via WebDAV also requires Locking. Here is an example location block:

{{hc|1=/etc/nginx/nginx.conf|2=
location /repos/ {
        auth_basic "Authorized Personnel Only!";
        auth_basic_user_file /etc/nginx/htpasswd;
        dav_methods PUT DELETE MKCOL COPY MOVE;
        dav_ext_methods PROPFIND OPTIONS LOCK UNLOCK;
        dav_access user:rw group:rw all:r;
        dav_ext_lock zone=general;
        create_full_put_path on;
        client_body_temp_path /tmp;
    }
}}

Note the . Add the specified locking zone to the http section of your config:

Now do the usual steps when preparing a git repo for the server:

*
* copy the bare repo to the server
* run  in the bare repo
* chown the repo to be owned by http:http

You might have noticed that I added HTTP Basic Authentication to have at lease some means of access control. Everyone who has an password entry in the htaccess file can push.

Now you can clone as usual:

 $ git clone https://www.example.com/repos/myrepo.git
 Cloning into 'myrepo'...
 $

Make some changes, add, commit, and push:

 $ git push origin main
 error: Cannot access URL https://www.example.com/repos/myrepo.git/, return code 22
 fatal: git-http-push failed
 error: failed to push some refs to 'https://www.example.com/repos/myrepo.git'

Oh noes! For some reason PROPFIND reports 401 Unauthorized and that's all. Nothing in the nginx error logs. Appearently the git client has a problem passing the username and password for all subsequent requests. Running a git credential cache does not help. The only solution that works so far is editing the ~/.netrc (obviously git uses curl for http):

 $  > git push origin main
 Fetching remote heads...
  refs/
  refs/heads/
  refs/tags/
 updating 'refs/heads/main'
  from 03f8860418facfbecedd5e0a81b480131b31bcba
  to   ec5536091e31ebf172a34c6d1ebddfc36e3bd3a6
    sending 3 objects
    done
 Updating remote server info
 To https://www.example.com/repos/myrepo.git
   0318860..ec55560  main -> main

Don't even think to specify the clone URL as . This works for the initial clone but for a subsequent push you get an error message in your error log stating that the destination URL is handled by a different repository.

## Smart HTTP
The  is a CGI program, allowing efficient cloning, pulling and pushing over HTTP(S).

## Apache
The setup for this is rather simple as all you need to have installed is the Apache HTTP Server (with , , and  enabled) and of course, .

Once you have your basic setup running, add the following to your Apache configuration file, which is usually located at:

This assumes your Git repositories are located at  and that you want to access them via something like: .

For more detailed documentation, visit the following links:
* https://git-scm.com/book/en/v2/Git-on-the-Server-Smart-HTTP
* https://git-scm.com/docs/git-http-backend

## Access control
For fine-grained access control, the following solutions are available:

*
*

Note that if you are willing to create user accounts for all of the people that should have access to the repositories and do not need access control at the level of git objects (like branches), you can also use standard file permissions for access control.https://github.com/sitaramc/gitolite/blob/d74e58b5de8c78bddd29b009ba2d606f7fcb4f2d/doc/overkill.mkd

## Web interfaces
* Gitweb — the default web interface that comes with Git
*

Refer to code forges for a list of web interfaces with more advanced capabilities.
