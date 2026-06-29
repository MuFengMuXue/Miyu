# Bioperl

BioPerl is a set of scripts in the Perl programming language to aid researchers in computational biology and bioinformatics.

## Installation
Install the  package.

## Configuration
If you installed from the AUR to the  path (default), the path to bioperl should be added to the @INC array of perl: add  as an environment variable.

It is adviced to install extra modules from CPAN, to avoid having dependencies errors.
* Upgrade CPAN
 # perl -MCPAN -e shell
 install Bundle::CPAN
 q
* Install/upgrade , and make it your preferred installer
 # cpan
 install Module::Build
 o conf prefer_installer MB
 o conf commit
 q

## Extras
The package Bioperl-run, which provides wrapper modules around many common bioinformatics applications and tools, is not installed by default.
 # cpan
 d /bioperl/
Which would return something like this:
 Distribution    BIRNEY/bioperl-1.2.2.tar.gz
 Distribution    BIRNEY/bioperl-1.2.3.tar.gz
 Distribution    BIRNEY/bioperl-1.2.tar.gz
 Distribution    BIRNEY/bioperl-1.4.tar.gz
 Distribution    BIRNEY/bioperl-db-0.1.tar.gz
 Distribution    BIRNEY/bioperl-ext-1.4.tar.gz
 Distribution    BIRNEY/bioperl-gui-0.7.tar.gz
 Distribution    BIRNEY/bioperl-run-1.4.tar.gz
 Distribution    BOZO/Fry-Lib-BioPerl-0.15.tar.gz
 Distribution    CJFIELDS/BioPerl-1.6.0.tar.gz
 Distribution    CJFIELDS/BioPerl-1.6.1.tar.gz
 Distribution    CJFIELDS/BioPerl-db-1.6.0.tar.gz
 Distribution    CJFIELDS/BioPerl-network-1.6.0.tar.gz
 Distribution    CJFIELDS/BioPerl-run-1.6.1.tar.gz
 Distribution    CRAFFI/Bundle-BioPerl-2.1.8.tar.gz
 15 items found
Then simply do (check the version compatibility):
 install CJFIELDS/BioPerl-run-1.6.1.tar.gz
 q

## Troubleshooting
If you run into trouble while compiling your perl scripts, with an error like , install the missing modules like this:

 # cpan
 install Module::Name
 q
