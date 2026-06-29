# Himitsu

Himitsu is a secure secret storage system for Unix-like systems.
It is extensible and suitable for storing passwords, private keys, logins, etc.

Himitsu secrets are stored in a arbitrary key/value store, accessible via a daemon.
Himitsu also provides a command-line interface and query language for the store.
Himitsu is designed for various integrations and frontends, including the graphical himitsu-keyring application.

## Installation
Install the  package.

You will also need a Himitsu prompter: .

## Configuration
The  man page is worth reading.
The following is a guide specific to an Arch Linux installation of .

Firstly, you will need a himitsu secstore (secrets store) and some basic configuration.
Initialize these with .

 $ himitsu-store -i

You will then need to configure Himitsu to use your prompter of choice.
Edit the  config file. For example, for
:

The Himitsu daemon  can now be run.
The Himitsu package comes with a systemd user unit, .
Starting/enabling it runs  in the background.

## Usage
Use the  command to query and manage the keystore.

You can manage the keystore graphically using .

## Integrations
Himitsu has integrations for various software.

## SSH
The  package provides an SSH agent and utilities for using and storing SSH keys in the Himitsu keystore.

For ssh to use the Himitsu SSH agent, it is required that:

* The agent is running (enable/start the included  user unit).
* The  environment variable is set to the Himitsu SSH agent's socket (i.e. ).

See .

With that, ssh will consult the Himitsu keystore for SSH key data.

## Firefox
The  package provides the backend (a native messaging component) for the official Firefox Himitsu Add-on.
Once both installed, Firefox can consult the Himitsu keystore for logins/passwords, from keystore entries with the  key-value pair.
The add-on implements the "web" protocol.
