# Vagrant

Vagrant is a tool for managing and configuring virtualised development environments.

Vagrant has a concept of 'providers', which map to the virtualisation engine and its API. The most popular and well-supported provider is Virtualbox; plugins exist for , ,  and more.

Vagrant uses a mostly declarative  to define virtualised machines. A single Vagrantfile can define multiple machines.

## Installation
Install the  package.

## Configuration
Vagrant is configured with environment variables. See the full list of options in the official documentation.

For example, to change the location where vagrant stores its "potentially large" files, set  to a suitable directory. (The default is ).

## Plugins
Vagrant has a middleware architecture providing support for powerful plugins.

Plugins can be installed with Vagrant's built-in plugin manager. You can specify multiple plugins to install:

 $ vagrant plugin install vagrant-vbguest vagrant-share

## vagrant-libvirt
This plugin adds a libvirt provider to Vagrant. libvirt and related packages (e.g. QEMU) must be installed and configured before using the provider.

To install the plugin, make sure  is installed and  has been started.
Then run

 $ vagrant plugin install vagrant-libvirt

Once the plugin is installed, the  provider will be available:

 $ vagrant up --provider=libvirt

If you have issues with dependency mismatch, the following environment variable can be set to ignore gem versions.

 export VAGRANT_DISABLE_STRICT_DEPENDENCY_ENFORCEMENT=1

If you have issues building ruby-libvirt, try the following (replace lib with lib64 as needed):

 $ CONFIGURE_ARGS='with-ldflags=-L/opt/vagrant/embedded/lib with-libvirt-include=/usr/include/libvirt with-libvirt-lib=/usr/lib' \
    GEM_HOME=~/.vagrant.d/gems \
    GEM_PATH=$GEM_HOME:/opt/vagrant/embedded/gems \
    PATH=/opt/vagrant/embedded/bin:$PATH \
        vagrant plugin install vagrant-libvirt

See for more troubleshooting.

## vagrant-lxc
First install  from the official repositories, then:

 $ vagrant plugin install vagrant-lxc

Next, configure lxc as directed in the [https://github.com/fgrehm/vagrant-lxc/wiki/Usage-on-Arch-Linux-hosts official repository. The plugin can now be used with a  like so:

The  file should be a shell script beside the . Do whatever setup is appropriate; for example, to remove puppet, which is packaged in the above box:

 rm /etc/apt/sources.list.d/puppetlabs.list
 apt-get purge -y puppet facter hiera puppet-common puppetlabs-release ruby-rgen

## Provisioning
Provisioners allow you to automatically install software, alter and automate configurations as part of the vagrant up process. The most common provisioner is .

## Base Boxes for Vagrant
Here is a list of places to get all sorts of vagrant base boxes for different purposes: development, testing, or even production.

* A well maintained up-to-date Arch Linux x86_64 base box for Vagrant.

* Vagrant Cloud is HashiCorp's official site for Vagrant boxes. You can browse user-submitted boxes or upload your own. A single Vagrant Cloud box can support multiple providers with versioning.

* vagrantbox.es—A List of vagrant base boxes. Initiated by Gareth Rushgrove @garethr hosted on Heroku using Nginx. See the story here: The Vagrantbox.es Story.

* Bento is a project that encapsulates Packer templates for building Vagrant base boxes. A subset of templates are built and published to the bento org on Vagrant Cloud.

* Puppet Labs Vagrant Boxes—Pre-rolled vagrant boxes, ready for use. Made by the folks at Puppet Labs.

* Vagrant Ubuntu Cloud Images—It has been there since Jan, 2013. For some reason Canonical has NOT officially promoted it yet, may be still in beta. Remember these are vanilla images, NOT very useful without Chef or Puppet.

* packer-arch project on Github provides configuration files to build light Arch Linux Vagrant images from the official iso image, using .

## Troubleshooting
## No ping between host and vagrant box (host-only networking)
Sometimes there are troubles with host-only networking not functioning. Host have no ip on vboxnet interface, host cannot ping vagrant boxes and cannot be pinged from them. This is solved by installing good old  as mentioned in this thread by kevin1024

## Virtual machine is not network accessible from the Arch host OS
As of version 1.8.4, Vagrant appears to use the deprecated  command to configure routing to the virtual network interface which bridges to the virtual machine(s).  If  is not installed, you will not be able to access the virtual machine from the host OS due to the lack of suitable route.  The solution, as mentioned above, is to install the  package, which includes the route command.

## 'vagrant up' hangs on NFS mounting (Mounting NFS shared folders...)
Installing  package may solve this problem.

Make sure the connection is not blocked by  or . If you are using libvirt along with firewalld, enable  (),  and  for the libvirt zone.

## Mounting NFS shared folders: mount.nfs: requested NFS version or transport protocol is not supported
Install the  package. Enable (v3 and) UDP support by editing  and uncommenting the following lines:
 vers3=y
 udp=y
Restart  to apply the changes immediately.

## Error starting network 'default': internal error: Failed to initialize a valid firewall backend
Most likely the firewall dependencies were not installed. Install the  and  packages and restart the  unit.

## Unable to ssh to vagrant guest
Check that virtualization is enabled in your BIOS. Because vagrant reports that the vm guest is booted, you would think that all was well with virtualization, but some vagrant boxes (e.g. tantegerda1/archlinux) allow you to get all the way to the ssh stage before the lack of cpu virtualization capabilities bites you.

## Could not get preferred machine for domain
 Error while creating domain: Error saving the server: Call to virDomainDefineXML failed: could not get preferred machine for domain

Check that virtualization is enabled in your BIOS.
