# Borgmatic

borgmatic is a Python-based wrapper script for Borg backup, designed to simplify and automate backups. It aims to provide an easy-to-use and flexible solution for creating backups using borgbackup.

## Installation
Install the  package.

## Configuration
By default no configuration file is installed. To create one you can use the command  to generate one:

The configuration file for borgmatic is located at one of the following

*  (or drop-ins in )
*  (or drop-ins in )

The configuration file allows you to define backup repositories, backup sources, retention policies, and other parameters.

## Usage
Once you have configured borgmatic to your liking, you can run it using the following command:

 # borgmatic --verbosity 2

This will start the backup process using the settings specified in your configuration file. borgmatic provides various options and flags that you can use to customize your backup behavior.

Borgmatic also provides systemd system and user units and timers.
