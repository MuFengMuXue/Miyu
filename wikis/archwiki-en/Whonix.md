# Whonix

Whonix is a desktop operating system setup designed for advanced security and privacy. This page describes how an Arch user may use a Whonix Gateway to route all traffic through Tor and receive many other the security benefits from compartmentalization as described below.

## Background on Whonix and Tor
The Whonix setup works by compartmentalizing two separate operating systems running inside of two separate virtual machines for greater security, while simultaneously routing all traffic through Tor.  This greater security model provides several benefits:

* Only connections through Tor are permitted.
* Servers can be run, and applications used, anonymously over the internet.
* DNS leaks are impossible.
* Malware with root privileges cannot discover the user's real IP address.
* Threats posed by misbehaving applications and user error are minimized.

The Whonix wiki provides many specific examples of attacks and software flaws that would normally pose a security and/or privacy problem, but are thwarted by this compartmentalization model.  It also describes where this model may still fail so it is an important page to understand.

The first operating system is "The Workstation" and is the OS you perform your normal everyday tasks in. The second is "The Gateway" that forces all traffic from the Workstation through Tor while providing the additional security benefits listed above.

The main Whonix team provides both a Gateway and Workstation running on top of Debian, but Arch users may enjoy using Arch as their main Workstation OS. This page describes how that can to be done.

## Downloading and Installing Whonix Gateway
You will not use the Gateway for everyday tasks.  It only serves to compartmentalize your Workstation activity from the internet while routing all traffic through Tor.

## Download and install the Whonix Gateway
Go to the Whonix VirtualBox page, download the "Whonix-Gateway" using one of the download options available, then verify download using one of the methods described on that page.  Make sure you also have VirtualBox installed.

Next, import the Whonix-Gateway inside VirtualBox by going to, File > Import Appliance > Whonix-Gateway-.ova, to select the Gateway file just downloaded, then agree to the conditions that describe system requirements and security considerations for using Whonix. It may be helpful to follow the instructions provided on the Whonix download page previously linked . There are also video tutorials available demonstrating this process.

After the appliance has been installed, start the Gateway using the start icon.

## Update the Whonix Gateway
Before we start Arch, we need to agree to the terms and ensure our Whonix Gateway has all up-to-date security patches. As with importing the appliance above, the terms you must agree to state that you understand the security considerations for running Whonix. After booting up the Gateway agree to these terms, state that you intend on using the stable repository and check "I am ready to enable TOR". After this, open a terminal. It will present you with information how to login as either root or a normal user.

Log in inside of this terminal as root and run:

 # apt-get update

 # apt-get dist-upgrade

Then reboot your Whonix Gateway.  After rebooting, open a terminal and this time log in as the normal user.  Run the whonix check:

 $ whonixcheck

You may also run nyx:

 $ nyx

To monitor traffic through the gateway.

## Installation of Arch as a Whonix Workstation
## Starting Arch inside VirtualBox
After you have installed the Whonix-Gateway, and while the Gateway is running, install an instance of Arch inside a separate VirtualBox instance. This is installation process is done as normal, save a few important steps described below, and so one should follow the Installation guide.

After creating the Arch instance, and before starting, three important settings need to be selected.  First, the network has to point to the running Whonix-Gateway. To do this, select Settings > Network > Attached to > Internal Network > Whonix to select networking through Whonix.

Also it is best if PAE is enabled so select Settings > System > Processor > Extended Features > Enable PAE/NX.

Lastly, select the Arch installation iso you downloaded as your boot storage by going to Settings > Storage > Empty > Optical Drive > Choose Virtual Optical Disk File > archlinux-.iso.

After these three settings have been selected, start your Arch VirtualBox instance.

## Connecting to internet during Arch install
When connecting a non-preset Workstation to the internet through a Whonix Gateway a few settings must be set manually as described here.  The address must be set to 10.152.152.50, the netmask to 255.255.192.0, the gateway to 10.152.152.10 and the nameserver to 10.152.152.10.  First, find your interface by running:

 # ip a

and look for your ethernet interface.  Something like eth0 or enp0s3 is common. Next, deactivate the interface with:

 # ip link set interface down

Where  is replaced with the name of the interface found above.  Next we must configure the static network connection to use the values shown above.  Perhaps the easiest way is to copy the static example file:

 # cp /etc/netctl/examples/ethernet-static /etc/netctl/whonix

Then replace the contents of that file with:

Where you should use replace enp0s3 with your  found above. The /18 is CIDR notation for the above netmask. Then edit :

Then edit  to prevent potential Tor over Tor problems:

Now enable the Whonix network connection:

 # netctl start whonix

And bring your interface back up:

 # ip link set interface up

Where once again  should be replaced with your interface. Next, confirm that the address 10.152.152.50/18 now shows up under your interface using:

 # ip a

If that checks out, try loading your favorite website such as:

 # lynx www.google.com

If lynx successfully loads a website, then the internet is working through Whonix.  Running "nyx" inside the Gateway as described above will further confirm that the packets are being sent across the Gateway.

## Mapping files over to your arch-chroot installation environment
Once these files have been edited and your internet is working, proceed with the normal Arch installation process. Preparing drives, formatting, etc. Then after you run pacstrap, but before you arch-chroot into your installation chroot, you need to copy the files you created above over.

 # cp /etc/netctl/whonix /mnt/etc/netctl/whonix

 # cp /etc/resolv.conf /mnt/etc/resolv.conf

 # cp /etc/environment /mnt/etc/environment

Then perform the standard arch-chroot and enable your network settings there:

 # arch-chroot /mnt

 # netctl enable whonix

Make sure you are still connected to the internet, and complete your Arch installation as you would normally. Set up root password, boot loader, etc. It is important that you set your timezone to UTC to match the Gateway.  Once the installation is done, reboot.

## Tor Check
Once your installation is completed, you have rebooted into Arch, and verified the Whonix Gateway is running, you should be able to access the internet routed through Tor.  You can verify traffic is being routed through Tor by installing your favorite web browser and performing the Tor Check.  This Tor Check should explicitly say you are using Tor.

## (Optional) Post-Installation considerations
## Installing Tor Browser
The standard web-browsers one would install in Arch will be forced to route all traffic through Tor and will receive all the benefits of Whonix compartmentalization.  This can easily easily be checked by performing the Tor Check as well as other DNS tests described below.

However, some might like to use the official Tor browser that comes with extra add-ons and security audits for use with Tor.  To install the Tor browser, download the browser from here and extract it into ~/.tb as follows.

 $ mkdir -p ~/.tb

 $ tar -xf tor-browser-version.tar.xz

 $ mv tor-browser_version ~/.tb/tor-browser

After the Tor Browser is installed we need to set the configuration to access Tor properly through the Whonix Gateway which is done by editing the following file:

Now start the Tor Browser.

 $ cd ~/.tb/tor-browser

 $ ./start-tor-browser.desktop

The Tor Check should verify both that you are using Tor and the Tor Browser.

## DNS Leak Tests
There are several Leak Tests one can preform to verify no traffic is leaking outside of tor:

* DNS Leak Test
* dnsleak.com

These are also helpful for verifying that no location or other identifying information is being leaked.

The Whonix DNS Leak Test Wiki has other helpful leak tests that can be performed in addition to checking websites.

## Familiarize yourself with the strengths and weaknesses of both the Whonix model and Tor
As suggested above, familiarize yourself with how the Whonix model works, the specific cases it provides extra security and privacy benefits in comparison with other approaches, how Tor works along with the benefits it provides, and the Tor project suggestions for making Tor work more reliably.

There is no silver bullet to security and privacy, but understanding these concepts may bring many additional benefits when used properly.
