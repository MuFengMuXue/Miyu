# Nessus

Nessus is a proprietary vulnerability scanner available free of charge for personal use. There are over 40,000 plugins covering a large range of both local and remote flaws.

## Installation
Install the  package.

## Usage
Start/enable .

Access the web interface at https://localhost:8834 and/or use the commandline interface (). In most browsers, you will need to manually accept the SSL certificate you created for the server.

## License
Register your email at the tenable site and wait for your key to be emailed to you.

Stop  before doing anything with .

Activate the license:

 # nessuscli fetch --register Activation Code

View your current license activation code:

 # nessuscli fetch --code-in-use

## Plugins update
Stop  before doing anything with .

Update the plugins:

 # nessuscli update --plugins-only

## Removal
The package can be removed with pacman, but files created by Nessus, such as the plugin database it downloads, must be removed manually:

 # rm -r /opt/nessus
