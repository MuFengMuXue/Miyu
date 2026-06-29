# Jujutsu

Jujutsu (commonly referred to as jj) is a modern, Git-compatible version control system written in Rust that aims to be both simpler and more powerful than Git.

## Installation
Install the  package.

## Graphical front-ends
See also Community-built tools around Jujutsu.

*
*
*
*

## Useful tools
Jujutsu can be configured to use alternative tools for tasks such as diff viewing, diff editing, merging. Many tools built for Git also support Jujutsu. The following tools directly or indirectly support Jujutsu and thus can either be used out-of-the-box or after simple adjustment to the Jujutsu configuration file.

## Conflict resolution
*
*
*
*

## Diff viewing
*
*

## Configuration
Just like with most other VCSes, you need to at least configure a name and email that will be attached to your commits.

 $ jj config set --user user.name  "John Doe"
 $ jj config set --user user.email "johndoe@example.com"

The  option tells Jujutsu to set these options in the global configuration file, stored in .

Alternatively,  opens the configuration file in your default text editor (defined in the / environment variable or can be set with the  configuration option).

See #Tips and tricks for more settings.

## Usage
All Jujutsu commands are initiated with the '''' prefix. To see a list of some of the common commands, run

 $ jj help

Each command has a help page that can be read using either of:

 $ jj help subcommand
 $ jj subcommand --help

You can get brief help with the  option.

## Initializing repository
Jujutsu uses Git as a storage backend, so it is compatible with existing Git repositories. Since version 0.34.0, Jujutsu creates colocated repositories by default, so no additional configuration is required to use it with Git.
The following command initializes a repository in the current directory:

 $ jj git init

Similarly to Git, it optionally takes a repository destination path as an argument.

As a result, it will create  and  folders to store its data. As of version 0.38.0, there is no  yet.

To clone a remote Git repository, use

 $ jj git clone

Just as with , the local copy of the cloned repository will be colocated.

The  family of commands can be used to view the current status of colocation and optionally enable/disable it. You can find more info in the relevant Jujutsu documentation page.

## Authenticating with remote hosts
Jujutsu uses Git under the hood for all remote operations, such as pushing and fetching, and thus all authentication tasks are also handled by Git. Starting from version 0.6.0,  subcommands support Git's credential helpers, and since v0.30.0, Jujutsu fully supports SSH authentication.

With that said, to use a credential helper with Jujutsu, you need to configure Git. See Git#Using git-credential-libsecret as credential-helper for instructions.

For SSH authentication, create an SSH key and then add it to your account on the hosting service. Relevant instructions can be found in your host's documentation.

## Tips and tricks
## Use Neovim as a vimdiff backend
Jujutsu has the  option to use Vim as a diff editor, but it doesn't detect Neovim. Add this to your configuration file to use  instead:

Alternatively, you can add your own merge-tools as described in Jujutsu documentation here.
