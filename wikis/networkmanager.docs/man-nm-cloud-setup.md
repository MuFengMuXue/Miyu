# Man / Nm Cloud Setup

nm-cloud-setup

     Automatic Network Configuration in Cloud with NetworkManager


     nm-cloud-setup
     8
     NetworkManager
     Automatic Network Configuration in Cloud with NetworkManager


nm-cloud-setup


Overview of Automatic Network Configuration in Cloud


Overview


When running a virtual machine in a public cloud environment, it is
    desirable to automatically configure the network of that VM.
    In simple setups, the VM only has one network interface and the public
    cloud supports automatic configuration via DHCP, DHCP6 or IPv6 autoconf.
    However, the virtual machine might have multiple network
    interfaces, or multiple IP addresses and IP subnets
    on one interface which cannot be configured via DHCP. Also, the administrator
    may reconfigure the network while the machine is running. NetworkManager's
    nm-cloud-setup is a tool
    that automatically picks up such configuration in cloud environments and updates the network
    configuration of the host.


Multiple cloud providers are supported. See  .


Use


The goal of nm-cloud-setup is to be configuration-less and work automatically.
    All you need is to opt-in to the desired cloud providers (see  )
    and run  /usr/libexec/nm-cloud-setup .


Usually this is done by enabling the nm-cloud-setup.service systemd service
    and let it run periodically. For that there is both a nm-cloud-setup.timer systemd timer
    and a NetworkManager dispatcher script.


Details


    nm-cloud-setup configures the network by fetching the configuration from
    the well-known meta data server of the cloud provider. That means, it already
    needs the network configured to the point where it can reach the meta data
    server. Commonly that means, that a simple connection profile is activated
    that possibly uses DHCP to get the primary IP address. NetworkManager will
    create such a profile for ethernet devices automatically if it is not configured
    otherwise via  "no-auto-default"  setting in NetworkManager.conf.
    One possible alternative may be to create such an initial profile with
     nmcli device connect "$DEVICE"  or
     nmcli connection add type ethernet ... .


    By setting the user-data  org.freedesktop.nm-cloud-setup.skip=yes
    on the profile, nm-cloud-setup will skip the device.


nm-cloud-setup modifies the run time configuration akin to  nmcli device modify .
    With this approach, the configuration is not persisted
    and only preserved until the device disconnects.


/usr/libexec/nm-cloud-setup


The binary  /usr/libexec/nm-cloud-setup  does most of the
      work. It supports no command line arguments but can be configured via environment
      variables.
      See   for the supported environment variables.


By default, all cloud providers are disabled unless you opt-in by enabling one
      or several providers. If cloud providers are enabled, the program
      tries to fetch the host's configuration from a meta data server of the cloud via HTTP.
      If configuration could be not fetched, no cloud provider are detected and the
      program quits.
      If host configuration is obtained, the corresponding cloud provider is
      successfully detected. Then the network of the host will be configured.


It is intended to re-run nm-cloud-setup every time when the configuration
      (maybe) changes. The tool is idempotent, so it should be OK to also run it
      more often than necessary. You could run  /usr/libexec/nm-cloud-setup
      directly. However it may be preferable to restart the nm-cloud-setup systemd
      service instead or use the timer or dispatcher script to run it periodically (see below).


nm-cloud-setup.service systemd unit


Usually  /usr/libexec/nm-cloud-setup  is not run directly,
      but only by  systemctl restart nm-cloud-setup.service . This
      ensures that the tool only runs once at any time.
      The unit is also used by the nm-cloud-setup systemd timer and allows
      enabling/disabling the service via systemd.


As you need to set environment variable to configure nm-cloud-setup binary,
      you can do so via systemd override files. Try  systemctl edit nm-cloud-setup.service .


nm-cloud-setup.timer systemd timer


 /usr/libexec/nm-cloud-setup  is intended to run
      whenever an update is necessary. For example, during boot when when
      changing the network configuration of the virtual machine via the cloud
      provider.


One way to do this, is by enabling the nm-cloud-setup.timer systemd timer
      with  systemctl enable --now nm-cloud-setup.timer .


/usr/lib/NetworkManager/dispatcher.d/90-nm-cloud-setup.sh


There is also a NetworkManager dispatcher script that will
      run for example when an interface is activated by NetworkManager.
      Together with the nm-cloud-setup.timer systemd timer this
      script is to automatically pick up changes to the network.


The dispatcher script will do nothing, unless the systemd service is
      enabled. To use the dispatcher script you should therefore run
       systemctl enable nm-cloud-setup.service  once.


Environment Variables


The following environment variables are used to configure  /usr/libexec/nm-cloud-setup .
    You may want to configure them with a drop-in for the systemd service.
    For example by calling  systemctl edit nm-cloud-setup.service
    and configuring  [Service] Environment= , as described in
       systemd.exec  5
    manual.


 NM_CLOUD_SETUP_LOG : control the logging verbosity. Set it
          to one of  TRACE ,  DEBUG ,  INFO ,
           WARN ,  ERR  or  OFF . The program
          will print message on stdout and the default level is  WARN . When
          run as systemd service, the log will be collected by journald can can be seen with
           journalctl .


 NM_CLOUD_SETUP_AZURE : boolean, whether Microsoft Azure support is enabled. Defaults
          to  no .


 NM_CLOUD_SETUP_EC2 : boolean, whether Amazon EC2 (AWS) support is enabled. Defaults
          to  no .


 NM_CLOUD_SETUP_GCP : boolean, whether Google GCP support is enabled. Defaults
          to  no .


 NM_CLOUD_SETUP_ALIYUN : boolean, whether Alibaba Cloud (Aliyun) support is enabled. Defaults
          to  no .


 NM_CLOUD_SETUP_OCI : boolean, whether Oracle Cloud (OCI) support is enabled. Defaults
          to  no .


Debugging


Enable debug logging by setting  NM_CLOUD_SETUP_LOG  environment variable to  TRACE .


In the common case where nm-cloud-setup is running as systemd service, this can be done via  systemctl edit nm-cloud-setup.service
    and add  Environment=NM_CLOUD_SETUP_LOG=TRACE  to the  [Service]  section. Afterwards, the log can
    be found in syslog via  journalctl . You may also want to enable debug logging in NetworkManager as described
    in the DEBUGGING section in    NetworkManager  5
    manual. When sharing logs, it's best to share complete logs and not preemptively filter for NetworkManager or nm-cloud-setup logs.


Example Setup for Configuring and Predeploying nm-cloud-setup


As detailed before, nm-cloud-setup needs to be explicitly enabled. As it
      runs as a systemd service and timer, that basically means to enable and configure
      those. This can be done by dropping the correct files and symlinks to disk.


      The following example enables nm-cloud-setup for Amazon EC2 cloud:


dnf install -y NetworkManager-cloud-setup

mkdir -p /etc/systemd/system/nm-cloud-setup.service.d
cat > /etc/systemd/system/nm-cloud-setup.service.d/10-enable-ec2.conf


Supported Cloud Providers


Amazon EC2 (AWS)


For AWS, the tools tries to fetch configuration from  http://169.254.169.254/ . Currently, it only
      configures IPv4 and does nothing about IPv6. It will do the following.


First fetch  http://169.254.169.254/latest/meta-data/  to determine whether the
          expected API is present. This determines whether EC2 environment is detected and whether to proceed
          to configure the host using EC2 meta data.


Fetch  http://169.254.169.254/2018-09-24/meta-data/network/interfaces/macs/  to get the list
          of available interface. Interfaces are identified by their MAC address.


Then for each interface fetch  http://169.254.169.254/2018-09-24/meta-data/network/interfaces/macs/$MAC/subnet-ipv4-cidr-block
          and  http://169.254.169.254/2018-09-24/meta-data/network/interfaces/macs/$MAC/local-ipv4s .
          Thereby we get a list of local IPv4 addresses and one CIDR subnet block.


Then nm-cloud-setup iterates over all interfaces for which it could fetch IP configuration.
          If no ethernet device for the respective MAC address is found, it is skipped.
          Also, if the device is currently not activated in NetworkManager or if the currently
          activated profile has a user-data  org.freedesktop.nm-cloud-setup.skip=yes ,
          it is skipped.


If only one interface and one address is configured, then the tool does nothing
          and leaves the automatic configuration that was obtained via DHCP.


Otherwise, the tool will change the runtime configuration of the device.


Add static IPv4 addresses for all the configured addresses from  local-ipv4s  with
                prefix length according to  subnet-ipv4-cidr-block . For example,
                we might have here 2 IP addresses like  "172.16.5.3/24,172.16.5.4/24" .


Choose a route table 30400 + the index of the interface and
                  add a default route  0.0.0.0/0 . The gateway
                  is the first IP address in the CIDR subnet block. For
                  example, we might get a route  "0.0.0.0/0 172.16.5.1 10 table=30400" .


Also choose a route table 30200 + the interface index. This
                  contains a direct routes to the subnets of this interface.


Finally, add a policy routing rule for each address. For example
                   "priority 30200 from 172.16.5.3/32 table 30200, priority 30200 from 172.16.5.4/32 table 30200" .
                  and
                   "priority 30400 from 172.16.5.3/32 table 30400, priority 30400 from 172.16.5.4/32 table 30400"
                  The 30200+ rules select the table to reach the subnet directly, while the 30400+ rules use the
                  default route. Also add a rule
                   "priority 30350 table main suppress_prefixlength 0" . This has a priority between
                  the two previous rules and causes a lookup of routes in the main table while ignoring the default
                  route. The purpose of this is so that other specific routes in the main table are honored over
                  the default route in table 30400+.


            With above example, this roughly corresponds for interface  eth0  to
             nmcli device modify "eth0" ipv4.addresses "172.16.5.3/24,172.16.5.4/24" ipv4.routes "172.16.5.0/24 0.0.0.0 10 table=30200, 0.0.0.0/0 172.16.5.1 10 table=30400" ipv4.routing-rules "priority 30200 from 172.16.5.3/32 table 30200, priority 30200 from 172.16.5.4/32 table 30200, priority 20350 table main suppress_prefixlength 0, priority 30400 from 172.16.5.3/32 table 30400, priority 30400 from 172.16.5.4/32 table 30400" .
            Note that this replaces the previous addresses, routes and rules with the new information.
            But also note that this only changes the run time configuration of the device. The
            connection profile on disk is not affected.


Google Cloud Platform (GCP)


        For GCP, the meta data is fetched from URIs starting with  http://metadata.google.internal/computeMetadata/v1/  with a
        HTTP header  "Metadata-Flavor: Google" .
        Currently, the tool only configures IPv4 and does nothing about IPv6. It will do the following.


First fetch  http://metadata.google.internal/computeMetadata/v1/instance/id  to detect whether the tool
          runs on Google Cloud Platform. Only if the platform is detected, it will continue fetching the configuration.


Fetch  http://metadata.google.internal/computeMetadata/v1/instance/network-interfaces/  to get the list
          of available interface indexes. These indexes can be used for further lookups.


Then, for each interface fetch  http://metadata.google.internal/computeMetadata/v1/instance/network-interfaces/$IFACE_INDEX/mac  to get
          the corresponding MAC address of the found interfaces. The MAC address is used to identify the device later on.


Then, for each interface with a MAC address fetch  http://metadata.google.internal/computeMetadata/v1/instance/network-interfaces/$IFACE_INDEX/forwarded-ips/
          and then all the found IP addresses at  http://metadata.google.internal/computeMetadata/v1/instance/network-interfaces/$IFACE_INDEX/forwarded-ips/$FIPS_INDEX .


At this point, we have a list of all interfaces (by MAC address) and their configured IPv4 addresses.


For each device, we lookup the currently applied connection in NetworkManager. That implies, that the device is currently activated
          in NetworkManager. If no such device was in NetworkManager, or if the profile has user-data  org.freedesktop.nm-cloud-setup.skip=yes ,
          we skip the device. Now for each found IP address we add a static route "$FIPS_ADDR/32 0.0.0.0 100 type=local" and reapply the change.


The effect is not unlike calling  nmcli device modify "$DEVICE" ipv4.routes "$FIPS_ADDR/32 0.0.0.0 100 type=local [,...]"  for all relevant
          devices and all found addresses.


Microsoft Azure


        For Azure, the meta data is fetched from URIs starting with  http://169.254.169.254/metadata/instance  with a
        URL parameter  "?format=text&api-version=2017-04-02"  and a HTTP header  "Metadata:true" .
        Currently, the tool only configures IPv4 and does nothing about IPv6. It will do the following.


First fetch  http://169.254.169.254/metadata/instance?format=text&api-version=2017-04-02  to detect whether the tool
          runs on Azure Cloud. Only if the platform is detected, it will continue fetching the configuration.


Fetch  http://169.254.169.254/metadata/instance/network/interface/?format=text&api-version=2017-04-02  to get the list
          of available interface indexes. These indexes can be used for further lookups.


Then, for each interface fetch  http://169.254.169.254/metadata/instance/network/interface/$IFACE_INDEX/macAddress?format=text&api-version=2017-04-02
          to get the corresponding MAC address of the found interfaces. The MAC address is used to identify the device later on.


Then, for each interface with a MAC address fetch  http://169.254.169.254/metadata/instance/network/interface/$IFACE_INDEX/ipv4/ipAddress/?format=text&api-version=2017-04-02
          to get the list of (indexes of) IP addresses on that interface.


Then, for each IP address index fetch the address at
           http://169.254.169.254/metadata/instance/network/interface/$IFACE_INDEX/ipv4/ipAddress/$ADDR_INDEX/privateIpAddress?format=text&api-version=2017-04-02 .
          Also fetch the size of the subnet and prefix for the interface from
           http://169.254.169.254/metadata/instance/network/interface/$IFACE_INDEX/ipv4/subnet/0/address/?format=text&api-version=2017-04-02 .
          and
           http://169.254.169.254/metadata/instance/network/interface/$IFACE_INDEX/ipv4/subnet/0/prefix/?format=text&api-version=2017-04-02 .


At this point, we have a list of all interfaces (by MAC address) and their configured IPv4 addresses.


Then the tool configures the system like doing for AWS environment. That is, using source based policy routing
          with the tables/rules 30200/30400.


Alibaba Cloud (Aliyun)


For Aliyun, the tools tries to fetch configuration from  http://100.100.100.200/ . Currently, it only
      configures IPv4 and does nothing about IPv6. It will do the following.


First fetch  http://100.100.100.200/2016-01-01/meta-data/  to determine whether the
          expected API is present. This determines whether Aliyun environment is detected and whether to proceed
          to configure the host using Aliyun meta data.


Fetch  http://100.100.100.200/2016-01-01/meta-data/network/interfaces/macs/  to get the list
          of available interface. Interfaces are identified by their MAC address.


Then for each interface fetch  http://100.100.100.200/2016-01-01/meta-data/network/interfaces/macs/$MAC/vpc-cidr-block ,
           http://100.100.100.200/2016-01-01/meta-data/network/interfaces/macs/$MAC/private-ipv4s ,
           http://100.100.100.200/2016-01-01/meta-data/network/interfaces/macs/$MAC/netmask  and
           http://100.100.100.200/2016-01-01/meta-data/network/interfaces/macs/$MAC/gateway .
          Thereby we get a list of private IPv4 addresses, one CIDR subnet block and private IPv4 addresses prefix.


Then nm-cloud-setup iterates over all interfaces for which it could fetch IP configuration.
          If no ethernet device for the respective MAC address is found, it is skipped.
          Also, if the device is currently not activated in NetworkManager or if the currently
          activated profile has a user-data  org.freedesktop.nm-cloud-setup.skip=yes ,
          it is skipped. Also, there is only one interface and one IP address, the tool does nothing.


Then the tool configures the system like doing for AWS environment. That is, using source based policy routing
          with the tables/rules 30200/30400. One difference to AWS is that the gateway is also fetched via metadata instead
          of using the first IP address in the subnet.


Oracle Cloud (OCI)


For OCI, the tools tries to fetch configuration from  http://169.254.169.254/ . Currently, it only
      configures IPv4 and does nothing about IPv6. It will do the following.


First fetch  http://169.254.169.254/opc/v2/instance  to determine whether the
          expected API is present. This determines whether OCI environment is detected and whether to proceed
          to configure the host using OCI meta data.


Fetch  http://169.254.169.254/opc/v2/vnics  to get the configuration
          for all the VNICs, getting their MAC address, private IP address, gateway and subnet block.


Then nm-cloud-setup iterates over all interfaces for which it could fetch a configuration.
          If no ethernet device for the respective MAC address is found, it is skipped.
          Also, if the device is currently not activated in NetworkManager or if the currently
          activated profile has a user-data  org.freedesktop.nm-cloud-setup.skip=yes ,
          it is skipped. Also, there is only one interface and one IP address, the tool does nothing.


Then the tool configures the system like doing for AWS environment. That is, using source based policy routing
          with the tables/rules 30200/30400.


See Also


         NetworkManager  8
         nmcli  1
