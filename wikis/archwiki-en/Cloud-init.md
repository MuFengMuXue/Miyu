# Cloud-init

Cloud-init is a package that contains utilities for early initialization of cloud instances. It is needed in Arch Linux images that are built with the intention of being launched in cloud environments like OpenStack, AWS etc.

## Installation
Install the  package.

If you intend to use the growpart module you will also need the  package.

## Configuration
This section only discusses the most basic settings. For a full list of available configuration options, please see the cloud-init documentation.

The main configuration file is . Optionally, additional  files to be loaded can be placed in . All of their contents will be merged.

The default configuration shipped with cloud-init 19.3 and later should work out of the box with most major cloud environments. In rough terms, it does the following:

* Disable the root user, create a user  for logging in
* Rely on cloud-init's built-in detection for data sources
* Run all modules known to work on Arch Linux

Depending on the use case, the default configuration might need to be adapted.

## Default user configuration
The default configuration includes the following contents (comments omitted for brevity):

 users:
    - default

The users to be added to the system. The special name  is just a reference to the  in the  section (see below), but the syntax supports configuring arbitrary users with many options. The first user in this list will be considered the "default" user by other modules, for example the one that sets up SSH keys passed in from the cloud environment.

 disable_root: true

Disable root SSH access. You may also delete the root user password on the cloud image:

 # passwd -d root

 system_info:
    default_user:
      name: arch
      lock_passwd: true
      gecos: arch Cloud User
      groups: adm
      sudo: NOPASSWD:ALL"
      shell: /bin/bash

This is the specification of the distribution's default user:

* the default user's name will be
* the default user is password locked, which means you can only log into the instance with the SSH keys configured during boot
* the default user will be added to the groups  and
* the default user is allowed passwordless  usage
* the default user's shell is

Note that the user specified here will only be created if the special user "default" is included in the  section above (or the section is omitted entirely).

## Configuring data sources
Data Sources define how the instance metadata is pulled during boot. This depends on the cloud environment (OpenStack, AWS, OpenNebula etc.) you are running your instance in. Under the hood, this translates to a corresponding module which implements a few methods defined in a common interface.

The default configuration specifies no data sources, which means that cloud-init will attempt to auto-detect the cloud environment. However, some environments cannot be detected or may require special configuration to work. In this case, the data sources to be used can be explictly specified and configured. Refer to the list of known data sources in the documentation.

To specify a list of data sources to be used in your  add something like this:

 datasource_list: [ NoCloud, ConfigDrive, OpenNebula, Azure, AltCloud, OVF, MAAS, GCE, OpenStack, CloudSigma, Ec2, CloudStack, None ]

This instructs cloud-init what modules to load while trying to download instance metadata. Optionally further configuration parameters may be passed specific to each datasource as follows:

 datasource:
   OpenStack:
     metadata_urls: [ 'http://169.254.169.254:80' ]
     dsmode: net

The above configuration tells OpenStack datasource to use the url  to download metadata and to run after network initialization, both of which are the default behaviour and may be omitted.

## Modules
Cloud-init comes with a set of modules that can be enabled or disabled in the configuration. The default configuration enables all modules that are known to work on Arch Linux. Omitted modules include e.g. those specific to other distributions or operating systems.

The fact that a module is enabled usually does not mean that it will actually do anything. It will however check if any configuration relevant to it was passed in, e.g. from the cloud environment via the data source. Only then it will attempt to act. As such, enabling all modules usually helps to maximize compatibility with cloud environments. Nevertheless, modules known to be not needed can be removed from configuration, e.g. to improve start-up times. You can use  on a booted instance to see how much time was spent on individual modules.

Some modules declare to cloud-init which distributions they have been verified for. Even if you specify that you want to run them, they will refuse to run unless the distribution specified in  is one of the verified distributions for that module. If you need to override this behavior to run a module on Arch anyway, add the module to the  section in the cloud config, e.g.:

 unverified_modules: == systemd integration ==

Package cloud-init provides four , two , and a , whose dependencies are constructed in a way that they are activated in the sequence listed:

* . Determines availability of any data source and enables or disables
* . Only requires the filesystems to be up. Executes
* . Requires the network to be up. Executes
* . Corresponds to the cloud-config upstart event "to inform third parties that cloud-config is available"
* . Executes
* . Executes
* . Reached when all services have been started

The Uplink Labs EC2 images have all of them enabled, although that appears to be overkill due to the dependencies. When preparing an image, enabling  and  should be sufficient. Note that this does not mean that the cloud-init services will actually be run - that still depends on the generator enabling the  on early boot.

See also the [https://cloudinit.readthedocs.io/en/latest/explanation/boot.html cloud-init boot stages documentation for more information.

## Using
## Archiso
Here is how to test an Archiso with cloud-init (see ) using QEMU:

Create a  file in YAML format for cloud-init containing username(s) and public SSH key(s).  You can either use the convenient  script proposed in archiso Merge Request #117, or just hand write as below, as-is or adding any additional options shown on the cloud-init documentation. Beware that the  is NOT a YAML comment, but is required to be present by cloud-init.

 #cloud-config
 users:
   - name: vorburger
     ssh_authorized_keys:
       - ssh-rsa (...)

We can use  as well, but do not have to, so we can just make that an empty file (but it has to exist):

 $ touch meta-data

Then build a  containing (only) the  and  using xorriso from :

 $ xorriso -as genisoimage -output cloud-init.iso -volid CIDATA -joliet -rock user-data meta-data

Now add this  as an additional second drive to the VM, using e.g. , or if using archiso then with the .

You should then be able to SSH into the machine using as the chosen user and public key supplied in . Note that it may take a moment to be available, due to a delay at the boot menu; e.g. the standard releng  will wait there for 30s at start-up. For frequent re-testing of new instances with changing hostkeys,  may be handy.

## Troubleshooting
## FAQ
The cloud-init FAQ has useful information about how to debug cloud-init, including where its log files are, and how to re-run datasource detection and cloud-init during development.

## Unmounted image
The first thing to check is often if the cloud-init image (ISO) is seen, with  and .

## "device /dev/sr0 with label cidata not a valid seed"
 appears when the nocloud datasource sees an ISO that e.g. only contains  but no  - both are required, even if one is empty.

## "unhandled non-multipart ssh_authorized_keys"
 appears when  YAML does not start with  (no space, apparently; even though  will tell you that it is ).
