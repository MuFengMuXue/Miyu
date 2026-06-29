# Eureka

From Eureka's README:

:Eureka is a CLI tool that allows you to quickly write down an idea using your preferred editor, and then have the idea committed and pushed to your idea git repository.

## Installation
Install the  package.

## Configuration
Eureka does not currently support any sort of complex configuration. However generates its own configuration when you first execute eureka.

When you first execute eureka, it will ask you to enter the full path to the repository you would like to use, this is a git repository containing a README.md file. For this setup we will store the eureka data within the home directory of the user you are logged in as.

Firstly, ensure you are in your home directory.

 $ cd

Then create the eureka directory, and enter it.

 $ mkdir eureka && cd eureka

Then initialise a new git repository within the eureka directory.

 $ git init

Then create the  file in which the notes will be stored.

 $ touch README.md

Congratulations, you have created the eureka storage directory, now in order to keep these notes safe from loss of data, such as you dropping your laptop and losing all the data, eureka automatically pushes to the "origin" remote ever change you make to your notes, so we must add this remote.

Any git provider can be used, such as Github or Gitlab as long as you have read/write permissions to the repository you would like to use, once you have created the repository, copy the ssh link and copy it into the following command:

 - With your ssh url of the repository you would like to use

Finally, you are ready to start eureka, once executed eureka will ask for the full path to your repository, enter .

Eureka will automatically generated the configuration for you in json format, you can find the configuration file at .

## Troubleshooting
## Cannot find binary path error
If you get the following error , Eureka defaults to the vi editor when no EDITOR environment variable is set.

If you do not want to define the environment variable globally, you can always define it inline when executing eureka, below is an example with using eureka with neovim without any environment variable set:

 $ EDITOR=nvim eureka

## No such file or directory error
If you get the following error  Eureka has attempted to look for the directory you defined on first startup, and could not find it, or the directory does not contain the  file which must be present for eureka to function.
