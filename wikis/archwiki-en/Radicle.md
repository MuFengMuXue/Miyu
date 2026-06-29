# Radicle

:"Radicle is an open source, peer-to-peer code collaboration stack built on Git. Unlike centralized code hosting platforms, there is no single entity controlling the network. Repositories are replicated across peers in a decentralized manner, and users are in full control of their data and workflow." - from radicle.xyz.

See upstream documentation for any missing parts.

Radicle, though great, has some notable missing features compared to Forgejo:
* The web frontend is purely read-only, interaction is done only via the CLI or the desktop application.
* No "releases". Unless you count git tags.
* No built-in "project management", e.g kanban. See #Planning board/kanban.
* Relatively simple issue management with assigning, commenting, reacting & tagging.
** No "milestones", "due date" or "dependencies".
* No bundled package registries, you will have to use a separate programs.

If you're alright without those features, or find the minimalism itself a feature, then continue on.

## Installation
Install the  package which includes  and .

## Configuration
First we need to generate our Radicle DID (Decentralized Identifier):

 $ rad auth

We can also query the DID with:

 $ rad self

To be able to have any peer-to-peer communications, we need to have our node up and running. If you did NOT set a key passphrase, then you can start/enable  user unit, otherwise you will need to start it manually to provide the passphrase.

 $ rad node start

We can query the node's status with:

 $ rad node status

## Usage
Radicle manages issues and content distribution, but the core is still git, so make sure you're familiar with it.

In an already initialized git repository, create a globally unique Repository ID (RID).
 $ rad init

This creates a new remote "rad".
 $ git remote show rad

We can now locally or remotely clone the repository with the shown "Fetch URL". We can also emit the "//" from the command.
 $ rad clone rad:z3gqcJUoA1n9HaHKufZs5FCSGazv5

The example RID is for heartwood, the backbone for radicle.

We can also just seed the repository without checking  it out.
 $ rad seed rad:z3gqcJUoA1n9HaHKufZs5FCSGazv5
And to stop seeding:
 $ rad unseed rad:z3gqcJUoA1n9HaHKufZs5FCSGazv5

The seeded repositories storage directory is mentioned in  as "Home" => "Storage".
We can list all, including seeded, repositories with:
 $ rad ls --all

## Managing Issues
Radicle bundles issues with the repository.
 $ rad issue

## Seed node Setup
Node uptime isn't guaranteed for regular users, so having a dedicated server to seed your repository is a good idea.

Also see upstream guide.

Instead of running  for every new repository you might create. It's simpler to "follow" your node to automatically seed every published repository.
 $ rad follow

## Frontend Web Server Setup
Since radicle is decentralized, there is no real need for a server, but for users not using radicle, it can be used to introduce them and to clone with regular git.

Note that the frontend is purely read-only. You can not "log in" nor create issues with it.

Frontend maintained by the core team: https://app.radicle.xyz/

Install the

## Tips and tricks
## CI/CD
See radicle-ci-broker.

## Migrating from github/gitlab
See radicle-migration-tool.

## Planning board/kanban
See radicle-planning-boards.
