# Sheepit

SheepIt is a free, distributed renderfarm for Blender. Blender files are submitted to the renderfarm where they are distributed to the participants for rendering. A scheduler takes into account factors relating to both the project and the machines participating, when distributing the frames.

## Launcher
The  package is the method preferred by the SheepIt developers. This package provides a launcher which checks for, and downloads, the latest client release on launch.

## Client
## Installation
Install either  or  which provide the SheepIt client. These packages do not conflict and can be installed at the same time.

## Launching the client
Launch the client using either  (when using ) or  (when using ).

## Running as a service
 provides systemd and configuration files for running the SheepIt client as a service.

## sheepit-client-git
Use of this package is dissuaded by the SheepIt developers as it compiles a bleeding edge version of the client, intended for use with the development sandbox. Please consider using the other packages described instead (e.g.  provides equivalent functionality).

## Troubleshooting
## Client spends most of its time downloading projects
As the scheduler finds the optimal project for your client to work on for each job request it makes, this can cause it to switch to a different project each time. If your internet connection is slow, this leads to a lot of 'project download' overhead. Launching the client with the  argument hints to the scheduler to keep your client on the same project as much as possible, reducing the amount of projects downloaded.

## Client shows 503 errors or 'leaked connection'
Due to the load on the servers, they can temporarily become overloaded. The client will recover without interference once the servers become available again.

## No jobs available
As the scheduler takes into account a lot of factors while determining which frames to provide a client to render, sometimes no suitable work can be found. Viewing the clients session on the SheepIt website can indicate why this is the case (e.g. not enough memory) but  does not mean your client will be asked to do it, due to other reasons, only that it could be.
