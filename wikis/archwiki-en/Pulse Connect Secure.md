# Pulse Connect Secure

Pulse Connect Secure (PCS), previously known as Juniper SSL VPN, is a commercial VPN solution targeted at businesses.

## Installation
## AUR
Install the  package and start/enable .

To connect via the command line, run the command:

 $ /opt/pulsesecure/bin/pulselauncher signinUrl realm role cert username password

Note that the login URL is different from the URL used in browsers. Check "Note regarding Server/URL" section below.

To use the  GUI client you need to additionally install  and . In the GUI client, the URL should be same as that used in browsers.

## OpenConnect
The OpenConnect VPN client also supports Pulse Connect Secure, however Host Checker support (required by some Pulse servers) is not yet implemented at the time of this writing (Spring 2022). See the initial announcement for more details.

To use, install . If your Juniper VPN setup does not require any input after connecting you can use this command in order to connect
 # openconnect --protocol=pulse https://vpn.example.com/

If you want NetworkManager support, install , or try the latest git version. The VPN connection can be created through the GUI or by using this command:
 $ nmcli con add type vpn con-name "Connection Name" ifname "*" vpn-type openconnect -- vpn.data "gateway=vpn.example.com,protocol=nc"

## Third-party scripts
## MSJNC
The Mad Scientist's "msjnc" script requires multilib, then install , , ,  and .

Access the Juniper VPN website you need to use. Log in and allow the installation to attempt and fail (due to non-32 bit Java). You should get an error similar to the following:

You should now have the file  present.

However, if  is not downloaded, fetch it manually - see the following example URL:  (note: you need to log in first).

Then download the msjnc script, make it executable, and put it in your .

## Automatic installation of ncsvc using msjnc
The first time you launch msjnc (before ncsvc is installed), it will extract  and prompt for your password in order to install the service. This requires sudo to be configured to allow all commands to your user.

After the service is installed to  with suid, create a profile and connect.

## Manual installation of msjnc
Create these directories:
 $ mkdir -p ~/.juniper_networks/network_connect
 $ mkdir -p ~/.juniper_networks/tmp

Extract the software:
 $ unzip ~/.juniper_networks/ncLinuxApp.jar -d ~/.juniper_networks/tmp

Copy  to the  directory:
 $ cp ~/.juniper_networks/tmp/NC.jar ~/.juniper_networks/network_connect

Install the service:
 $ sh ~/.juniper_networks/tmp/installNC.sh ~/.juniper_networks/network_connect

Launch msjnc, create a profile, and connect.

## Note regarding Server/URL
For the Server/URL, you may have to provide the URL that processes the login form rather than the login page itself. As an example, one company's login form is on  but the form is actually processed by . You may have to inspect the html of the login page to find the form's action attribute.

## JVPN
The JVPN Perl script establishes a Juniper VPN connection and supports the following features:
* Connection using Host Checker.
* Automatic download of the required Juniper java and daemon files (ncsvc) when run as root.

## Installation
Install the perl dependencies  and . Once you have done so, you must choose whether to run jvpn as root (easiest method) or as a regular user and run the steps below accordingly.

## Running as root
Run the command:
 # curl -L https://github.com/samm-git/jvpn/archive/v0.7.0.tar.gz | tar xz
The command creates a file  in current directory.

Finally, start the script with:
 # ./jvpn.pl
On first run, the script will download all the necessary files

## Running as a regular user
Use your web browser (no need for 32-bit Java) to connect to the VPN website and download the appropriate software. The files downloaded will be located in  (even if the VPN connection actually fails).

This step is considered more complex because you have to have a functional Java plugin in your browser (configured with appropriate security settings). During installation of Network Connect, the browser will request a root password to set the setuid flag on ncsvc (Juniper daemon).

Then install jvpn into the folder by executing the following:
 $ cd ~/.juniper_networks/network_connect
 $ curl -L https://github.com/samm-git/jvpn/archive/v0.7.0.tar.gz | tar xz --strip-components=1

Next, edit  (directions are included in the file).

Finally, start the script with the following:
 $ cd ~/.juniper_networks/network_connect
 $ ./jvpn.pl

## Workarounds
## 64-bit Java (workaround 1)
1) Install . Make sure the PKGBUILD installs it to , rather than , where it will conflict with the 64-bit JRE.

2) Install .

3) Move the java binary to :
 # mv /opt/java/jre/bin/java /opt/java/jre/bin/java.orig

4) Create a bash script  and make it executable:
 # touch /opt/java/jre/bin/java
 # chmod 755 /opt/java/jre/bin/java

5) Finally, edit the bash script as per the below:

## 64-bit Java (workaround 2)
Another approach is to install an alternative version of Java and link the Java plugin for Firefox manually - this avoids the necessity of using a chroot environment. Follow the instructions below:

#install .
#Install a custom 64-bit Java environment from java.com. Select the Linux x64 version. Once you have decided upon a location for the installation, extract the binary into that location and then mark it executable. Finally, run the binary to install Java.
#Install a custom 32-bit Java environment, also from java.com but this time, select the Linux (self-extracting) option. Extract the new binary to the same location created above, mark it executable, and run the binary. It will ask you whether you want to replace the files to 32 bit: Type "A" to overwrite all the 64-bit files with the 32-bit ones.
#Finally, link the library into the required location. The relevant library for Firefox is . To link it, use the following command .

For more information, see the following guide from Southern Illinois University.

## Troubleshooting
## Login succeeds but Network Connect will not launch
#Firstly, verify your Java installation.
#Then navigate to .
#Check that  is setuid root. Fix it if not.
#Run  and see if there are any missing libraries.
#Follow the instructions from the Juniper forum to run it from command line. Use the  switch to log everything and use strace as root. Also try consulting  for any possible errors.

## Network Connect launched but the VPN does not work
Run  to to check if the route is present. Network connect has a diagnosis tool in the GUI. You can also checks the logs (also available in the GUI).

Other cause for VPN not working can lie in DNS settings. Check whether they really are set (usually in /etc/resolv.conf) and that DNS cache does not intervene (stop systemd-resolved service if running).

## Network Connect launched and a configuration error message is displayed
Check that you have  installed.

## ncapp.error Failed to connect/authenticate with IVE.
See this post on the Ubuntu forums. Note that in some cases, the policy will not permit a connection initiated from the command line. Instead, you have to install both  and  and authenticate through the browser.

## Unauthorized new route has been added, disconnecting
When using the  client, VPN may not work with  due to conflicting routing table strategies. Check  for such messages:

 rmon.error Unauthorized new route to x.x.x.x/y.y.y.y has been added (conflicts with our route to z.z.z.z), disconnecting (routemon.cpp:598)

If this is the case, using NetworkManager instead can fix the issue.

## After login, pulseUi displays 'Compliance: Security policies not met'
It seems that  uses NetworkManager internally while verifying connection in some cases. If this is the case, install NetworkManager and start .

## pulseUi does not remember connections
If pulseUI keeps forgetting your connections, make sure the directory  exists. If it does not:
 # mkdir -p /var/lib/pulsesecure/pulse/
