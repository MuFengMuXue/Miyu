# Chef

Chef is a configuration management tool primarily written in Ruby, with an Erlang & Java server. It uses a pure-Ruby, domain-specific language (DSL) for writing system configuration "recipes". Chef is used to streamline the task of configuring and maintaining a company's servers, and can integrate with cloud-based platforms such as Amazon EC2, Google Cloud Platform, OpenStack, SoftLayer, and Microsoft Azure to automatically provision and configure new machines. Chef contains solutions for both small and large scale systems, with features and pricing for the respective ranges.

## Chef Workstation
 contains the development and deployment tools for working with the Chef platform. It includes:

* Chef Infra Client
* Test Kitchen
* Cookstyle
* Chef InSpec

## Chef Infra Client
For the systems being managed, install the  package. This is the recommend installation method to get , , or  tools.

## CINC client
Chef Software changed their licensing for using their packages to require accepting their license, much like Red Hat requires license acceptance to use Red Hat Enterprise Linux. There is a community distribution called CINC that is working towards providing community-supported packages for Chef Software's products (similar to CentOS as an alternative). The  package provides the alternate , , or  tools.

## Omnibus Chef installer
The packages provided by Chef Software are built with their dependencies included. This allows them to ship Chef without worrying about the underlying operating systems' support for Ruby, OpenSSL, etc. The , , and  packages are built by re-using these packages.

## Installing from source
If you wish to build your own Omnibus packages:

  $ git clone https://github.com/chef/chef.git
  $ cd chef/omnibus

Wipe out any previous installations and the omnibus cache:

 # rm -Rf /opt/chef/* /var/cache/omnibus/*

Set up the directories and change the ownership to yourself so building as root is not required:

 # mkdir -p /opt/chef /var/cache/omnibus
 # chown -R "$USER:users" /opt/chef
 # chown -R "$USER:users" /var/cache/omnibus

Run the following to build:

 $ bundle install --binstubs
 $ bundle exec omnibus clean chef
 $ bundle exec omnibus build chef

After that, you may like to change the ownership of directories back to the system:

 # chown -R root:root /opt/chef
 # chown -R root:root /var/cache/omnibus

A Makeself portable installer will be created, e.g. chef-11.8.2_0.arch.3.12.6-1-ARCH.sh.
Run this executable to install chef.

## Removal
Remove all installation files manually:

 # rm -Rf /opt/chef

You can also ensure the omnibus cache is removed:

 # rm -Rf /var/cache/omnibus
