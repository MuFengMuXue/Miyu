# Burp Suite

From the official website:

:Burp Suite is an integrated platform for performing security testing of web applications. Its various tools work seamlessly together to support the entire testing process, from initial mapping and analysis of an application's attack surface, to finding and exploiting security vulnerabilities.

## Installation
Install  or .

This will install Burp Suite Community (free edition) or the commercial edition (license needed).

## Configuration
Burp Proxy will work out of the box with HTTP connections. For HTTPS, PortSwigger's certificate must be installed first.

## Install HTTPS certificate in Firefox
Start up Burp:

 $ burpsuite

Open the Proxy > Options. In the Proxy Listeners section add a new interface. Set Interface to  and make sure the Running checkbox is enabled.

Navigate to http://127.0.0.1:8080/ in Firefox, click the CA Certificate link at top right and save the certificate file somewhere.

In Firefox open the Options tab and go to Privacy & Security > Certificates > View Certificates... > Authorities. Click Import and select the file. Check the Trust this CA to identify websites checkbox and click OK.

## Troubleshooting
## Fix segfault during startup
The  package update to 4.0.0 causes Burp to segfault during startup when used with the JRE that ships with Burp.

Use Java 18 instead of the 16 JRE that ships with Burp:

 $ app_java_home=/usr/lib/jvm/java-18-openjdk ~/BurpSuitePro/BurpSuitePro

For the desktop entry change the Exec line to:

## Fix small fonts on screens with HiDPI
Screens with high resolutions will show Burp's GUI with very small fonts when opened. To solve this, run the burp suite from the command line providing VMOptions to scale it up.

 $ java -Dsun.java2d.dpiaware=true -Dsun.java2d.uiScale=2.0 -jar /usr/share/burpsuite/burpsuite.jar

## Wayland support
Java has experimental support for Wayland through project Wakefield. This is beneficial when using HiDPI monitor with scaling.

Install  or , set  as the default Java environment then launch Burp Suite Pro using the following command, or include the Java options in the script that executes the JAR (by default ):

 $ _JAVA_OPTIONS="-Dawt.toolkit.name=WLToolkit -Dsun.java2d.vulkan=True" burpsuite-pro

Alternatively, install Xwayland and restart your compositor. HiDPI monitors with scaling enabled will lead to blurriness.
