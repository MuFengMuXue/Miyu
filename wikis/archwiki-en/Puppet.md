# Puppet

From Puppet web site:

:Puppet is IT automation software that helps system administrators manage infrastructure throughout its lifecycle, from provisioning and configuration to patch management and compliance. Using Puppet, you can easily automate repetitive tasks, quickly deploy critical applications, and proactively manage change, scaling from 10s of servers to 1000s, on-premise or in the cloud.

## Installation
Install the  package.

If you want to install a puppet master you can install the  package, the documentation for which is in Puppet server.

## Configuration
Puppet's main configuration file is  which is located at .

There are 3 sections to place settings depending if it is a master/agent: ,  and .

Bare minimum of settings are:

* server: The hostname of the puppet server. Default:
* report: Most users should set this to true.
* pluginsync: Most users should set this to true.
* certname: The certified name of the machine (unique identifier). Default:

Puppet will look for node configuration in .

After starting puppet by daemon/cron/standalone, it will generate certificates in  directory. You need to accept this certificate in the puppet master:

 # puppet cert sign name

Notes on bindaddress for puppet master.

The default value for bindaddress is , which makes puppet listen on IPv4 only:

To make puppet master listen on IPv6, set the bindaddress value to:

To make puppet listen on both interface, set the value to:

## Facter
Facter is a companion program of puppet that gathers facts about the system it runs on.

Commands:

 # puppet facts find facter
 # facter -p

## Puppet Resources
## Packages
Pacman is supported by puppet. Installing packages works out of the box since puppet 3.1.0.

## Services
Since puppet 3.2.1, systemd on Arch Linux is fully supported.

See systemctl for details on how to use the provided units.

## Puppet Bolt
Puppet Bolt is standalone piece of software that was introduced by puppet to allow applying tasks without the need for puppet agent and puppet server (like Ansible/Salt). Of course many advantages of the master/agent-design are then lost, but if you need to send one-time commands, puppet bolt is the right tool for you.

For example restarting a webserver or deleting the mailqueue is done better with puppet bolt whereas keeping a package to the most current version should be done with standard puppet configuration management.

## Installing Bolt on Arch
To use Bolt on Arch to run tasks (that may target the local system or remote targets), the only needed package is . More information can be found in its Documentation and official hands-on lab.

## Targeting Arch with Bolt
When Bolt is run against an Arch target (regardless of whether Bolt itself is invoked on Arch), some functionality does not work out of the box. In general, when diagnosing mysterious Bolt failures on Arch targets, information about the cause of the failure is available via the debug log level, for example:

 $ bolt apply --target arch --log-level debug ...

Execute  for the command nomenclature.

## Using Bolt to install Puppet
The  Bolt task (which is invoked automatically as part of  and several other pieces of Bolt functionality) does not support installing the Puppet agent on Arch Linux. Attempts to do this may encounter errors like  in the Bolt debug logs.

Fortunately, Bolt can use a pre-installed version of Puppet. To set this up, install Puppet manually using the instructions in the "Installation" section above, then ensure that  is installed.  is required due to this Bolt issue; if it is not present the  error may continue to occur in Bolt even after Puppet is correctly installed on the target.

## Bolt Binary-location Expectations
A lot of Bolt functionality, including , expects several Puppet-related binaries to be installed in , which is not done by the default  package. Until this is resolved, errors like this may occur in the Bolt debug logs:

 /tmp/7b7dae3f-c3d9-4482-af14-a7e94a98b6cd/custom_facts.rb: bad interpreter: /opt/puppetlabs/puppet/bin/ruby: no such file or directory

To work around this issue, symlink the installed Ruby into the expected location:

 $ mkdir -p /opt/puppetlabs/puppet/bin
 $ ln -s $(type -p ruby) /opt/puppetlabs/puppet/bin/ruby

If additional Bolt failures occur due to other binaries not being installed in that folder, you can symlink  to it:

 $ rm /opt/puppetlabs/puppet/bin/ruby
 $ rm -r /opt/puppetlabs/puppet/bin
 $ ln -s /usr/bin /opt/puppetlabs/puppet/bin
