# VMWare vCLI

The vCLI utilities make it possible to manage VMWare ESX servers (with the possibility of using vCenter). Even though Arch Linux is not one of the "supported platforms"; the installation process is relatively straightforward. We have a two method's of VMWare vCLI installation. It is a build package from AUR, or manually installation.

## Installation
Install .

Alternatively, the utilities can be installed manually.

## Manually
## Download location
The utilities can be downloaded from http://www.vmware.com/support/developer/vcli. Registration is mandatory.
It seems that registration is not enough to download latest release from this link. It gives "Download is not available."

5.1 can be downloaded from here: https://my.vmware.com/group/vmware/details?downloadGroup=VSP510-VCLI-510&productId=285

## Dependencies
vCLI has quite a few dependencies which can easily be managed via pacman:               .

## Installation
Unpack the archive:

 tar xzvf VMware-vSphere-CLI-5*.tar.gz

Change to the newly created directory:

 cd vmware-vsphere-cli-distrib/

Open the file  with your favorite editor. Change the following rules:

 my $installed_ssl_version = '1.0.0';   # rule 5248
 my $ssleay_installed = 1;              # rule 5250
 my $OpenSSL_installed = 1;             # rule 5256
 my $LibXML2_installed = 1;             # rule 5257
 my $OpenSSL_dev_installed = 1;         # rule 5258
 my $e2fsprogs_installed = 1;           # rule 5261
 my $e2fsprogs_version = '1.42';        # rule 5262
 my $install_rhel55_local = 1;          # rule 5266

The next step is to configure a ftp and http proxy. These values are mandatory, even when you are not using a proxy (in which case you leave the values in a blank state):

 export ftp_proxy=""
 export http_proxy=""

Fire up the installation:
 ./vmware-install.pl

Potential warnings about rpm and versions can be safely ignored.
