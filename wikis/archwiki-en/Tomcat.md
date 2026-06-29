# Tomcat

Tomcat is an open source Java Servlet container developed by the Apache Software Foundation.

## Installation
Install one of , , or .

If deploying Tomcat onto a production environment, consider installing . The native library for Tomcat configures the server to use the Apache Portable Runtime (APR) library's network connection (socket) and RNG implementations. It uses native 32- or 64-bit code to enhance performance and is sometimes used in production environments where speed is crucial. No configuration is necessary for default Tomcat installations. More information is available in the official Tomcat docs.

Using tomcat-native will remove the following warning in :

 INFO: The APR based Apache Tomcat Native library which allows optimal performance in production environments was not found on the java.library.path === Filesystem hierarchy ===

Replace the  with your installed version (8, 9, 10).

{| class="wikitable"
! Pathname !! Use
|-
|             || Configuration files. Among some:  (defines users allowed to use administration tools and their roles),  (Main Tomcat configuration file),  (security policies configuration file)
|-
|       || Main Tomcat folder containing scripts and links to other directories
|-
|  || Tomcat Java libraries (jars)
|-
|        || Log files not handled by  (see #Logging)
|-
| || Where Tomcat deploys your web applications
|-
|         || Where Tomcat store your webapps' data
|}

## Initial configuration
In order to be able to use the manager webapp and the admin webapp, you need to edit .

Uncomment the "role and user" XML declaration and modify it to enable roles , ,  and/or , , , , depending on your needs (see [https://tomcat.apache.org/tomcat-7.0-doc/manager-howto.html#Configuring_Manager_Application_Access Configuring Manager Application Access).
To keep it short,  is the mandatory role used to run,  are roles able to administer web applications and  are full right administrator roles on the Tomcat server.

Here is a bare configuration file that declares some of these roles along with usernames and passwords (be sure to change the following passwords to something secure):

Keep in mind that Tomcat must be restarted each time a modification is made to this file.

This [https://blog.techstacks.com/2010/07/new-manager-roles-in-tomcat-7-are-wonderful.html blog post gives a good description of these roles.

To have read permissions on the configuration files and work well with some IDEs, you must add your user to the  user group.

## Start/stop Tomcat
Start the .

Once Tomcat is started, you can visit this page to see the result: http://localhost:8080. If a nice Tomcat local home page is displayed, this means your Servlet container is up and running and ready to host you web apps. If the startup script failed or you can only see a Java error displayed in you browser, have a look at startup logs using systemd's journalctl. Google is full of answers on recurrent issues found in Tomcat logs.

{{Out of date| does not exist at least on tomcat{9,10}. Check where the new  exists.}}

## Alternate "manual" way
Tomcat can also be controlled directly using upstream scripts:

 /usr/share/tomcat/bin/{startup.sh,shutdown.sh,..}

This can be useful to debug applications or even debug Tomcat, but do not use it to start Tomcat for the first time as doing so can set some permissions wrongly and stop web apps from working. In order to be able to use these scripts, some further configuration may be needed. Be aware that using these scripts prevents the jsvc security advantage described above.

## Deploy and handle web applications
Tomcat is bundled with 5 already deployed web applications (change localhost with your server's FQDN if needed):

* The default home page: http://localhost:8080/
* Tomcat's local documentation: http://localhost:8080/docs/
* Examples of Servlets and JSP: http://localhost:8080/examples/
* The host-manager to handle virtual hosts: http://localhost:8080/host-manager/
* The manager to administer web applications: http://localhost:8080/manager/html/

## The GUI way
Probably the easiest way is to use the manager webapp http://localhost:8080/manager/html. Use the username/password you defined as  in . Once logged in, you can see five already deployed web applications. Add yours through the "Deploy" area and then stop/start/undeploy it with the "Applications" area.

## The CLI way
One can also just copy the WAR file of the application to directory . For that later, be sure that the  option is still set for the right host as shown here:

Otherwise simply restart the tomcat service.

## Hosting files outside the webapps folder
If you want to keep your project outside the webapps folder, this is possible by creating a .
Go to  and create your context. A context is a simple xml file which specifies where tomcat should look for the project. The basic format of the file is:

A working example is as follows. This assumes that the project is hosted somewhere in the users /home-folder.

The files can now be hosted in . To see the project in your webbrowser, go to http://localhost:8080/myProject.
If tomcat is unable to load the files, it might be an issue with permissions. Making  executable should fix the issue.

## Logging
Tomcat when used with official Arch Linux packages uses systemd's journalctl for startup log. This means that files  and  are not used. Other logs such as access logs and business logs defined in  as  will still by default end up in .

To restore upstream style logging, use a drop-in file to change both  for the absolute paths of log files.

## Further setup
Basic configuration can be made through the virtual host manager web application: http://localhost:8080/host-manager/html. Provide the username/password you set in . Other options are tweaked in configuration files in , the most important being . Using these files is out of the scope of this 101 wiki page. Please have a look at the latest official Tomcat documentation for more details.

## Migrating from previous versions of Tomcat
As said in the introduction, Tomcat 10 does not deprecate Tomcat 9, Tomcat 9 does not deprecate Tomcat 8 and so on. They all are implementations of Servlet/JSP standards. Hence you must first determine which version of Tomcat you need depending on the versions of Servlet/JSP your application uses. If you need to migrate, the official website gives instructions on how to handle such a process.

## Using Tomcat with a different JRE/JDK
Apart from installing the desired JRE/JDK, the only requirement is to set the  variable with a drop-in file:

## Security configuration
This page gives the bare minimum to get your first web application to run on Tomcat. It is not intended to be the definitive guide to administering Tomcat (it is a job of its own). The official Tomcat website will provide all necessary official matter. One could also refer to this O'Reilly page and this unidata one.
Still, here are some security tips to get you started:

* Keep your Tomcat installation up to date to get the latest fixes to security issues
* Remove unwanted default applications such as , , default home page  ("_" in the  webapp). This prevents potential security holes to be exploited. Use the  for that.

For more security, you could even remove the host-manager and manager web applications. Keep in mind that the later is useful to deploy web applications.

* Disable the WAR auto-deploy option. This would prevent someone who gained restricted access to the server to copy a WAR into the  directory to get it running. Edit  and set the  to :

* Anonymize Tomcat's default error page to prevent potential attackers to retrieve Tomcat's version. To see what Tomcat says by default, just visit an nonexistent page such as http://localhost:8080/I_dont_exist. You get a 404 error page with Tomcat's version at the bottom.

To anonymize this, edit/open the following JAR (Editors like  can edit zips directly)

 /usr/share/tomcatn/lib/catalina.jar

And edit the following file:

* Disable unused  in
* Keep restricted access to . Only  user and/or  should be able to read and write this.
* Keep  usage. Do not use upstream startup scripts unless particular reason as explained in the security note above.
* Use strong different passwords for each user in , give roles to users who really need them and even disable usernames/roles you do not use/need.

One can even crypt  passwords using the following upstream script:

 /usr/share/tomcatn/bin/digest.sh -a sha-512 -h org.apache.catalina.realm.MessageDigestCredentialHandler NEW_PASSWORD

This will output something like:

 NEW_PASSWORD:58adca01951a24aebce28f4d7a759aa30ef2f38bc54e41e51071c257ed4a1a9b$1$b4ccaafa86c26dea13825d35da73f9d11ce63f5deae15a13aafb835bdaf710d38922843c8065f35f245a20b1d2df9b20ddf2c005990512c598a62514f78cf3d2

Paste the hashed part in place of the clear password in  and add the following to :

Note that this may not be relevant because only root and/or tomcat is supposed to have read/write access to that file. If an intruder manages to gain root access, they would not need such passwords to mess with your applications/data anyway. Be sure to keep restricted read and write access to that file, and always know what you are deploying!

## Troubleshooting
## Tomcat service is started, but page is not loaded
First, check  for any syntax error. If everything is fine and  is correctly running, run  as root to check the logs for any exception thrown (see #Logging). If you read anything like , this is due to some other service listening on the same port. For instance, it is possible that Apache HTTP Server and Tomcat are listening on the same port (if for example you have Apache running on port 8080 with Nginx serving it as a proxy on port 80). If this is the case, edit the  file and change the Connector port to something else under :

Finally, restart  and  services.

If you have no solution and you are in a VM, it can help to delete  and create it again (cf. Solution: FUTEX_WAIT hangs Java on Linux / Ubuntu in vmware or virtual box):

 # rm /dev/random
 # mknod -m 644 /dev/random c 1 9

Or another solution to keep it even after a reboot is to modify  (for example) to point to /
