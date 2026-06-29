# BOINC

From the BOINC website:

:Use the idle time on your computer (Windows, Mac, or Linux) to cure diseases, study global warming, discover pulsars, and do many other types of scientific research. It's safe, secure, and easy.

From Wikipedia:BOINC:
:The Berkeley Open Infrastructure for Network Computing (BOINC) is a non-commercial middleware system for volunteer and grid computing. It was originally developed to support the SETI@home project before it became useful as a platform for other distributed applications in areas as diverse as mathematics, medicine, molecular biology, climatology, and astrophysics. The intent of BOINC is to make it possible for researchers to tap into the enormous processing power of personal computers around the world.

## Installation
Install either the  or the  package. The latter omits Xorg dependencies, and is therefore suited for use on headless servers.

Both packages install a unit file named .

You will also need to add yourself to the  user group in order for the manager to connect.

To generate the necessary files referenced in the next section, make sure to start .

## Known issues
## Log spam
On Wayland, and possibly also on X, you may notice frequent (one per second) of messages in the journal like:

 boincAuthorization required, but no authorization protocol specified

See [https://boinc.berkeley.edu/dev/forum_thread.php?id=14249 and Until this is fixed, one workaround is to filter this message by editing  :

which will filter that message from  since the [https://github.com/systemd/systemd/blob/b9dac418372401742609bd600f05267ae3a724de/NEWS#L147-L152 release 253 of .

## Using BOINC
## BOINC via the GUI
By default, a password is created in  for connecting to the daemon. To simplify connection of the GUI to the daemon, create a link to this file in your home directory.

 $ ln -s /var/lib/boinc/gui_rpc_auth.cfg ~/gui_rpc_auth.cfg

Do not forget to add your user to the  group as described above and then relogin or reboot.

If you prefer a different password, or none at all, you can edit . Then restart BOINC daemon.

If you do not like the idea of having this file in your home directory, there is an alternative approach.  BOINC Manager will also look for a readable gui_rpc_auth.cfg file in the current working directory.  If you make the file readable by the boinc group and ensure that the manager is run with  as the working directory, you should find that the client connects to the daemon automatically, as desired.  This can usually be achieved via the menu editor in your desktop environment of choice.

To start the GUI, use the boincmgr command
 $ boincmgr

BOINC should now take you through the process of attaching to a project. NB, some projects will let you create an account remotely via the GUI while some may require you to first create an account via their website. You can attach to multiple projects if you have the resources (disk space, time, CPU power). Do this via menu option Tools / Attach to project.

If BOINC did not ask you to connect to a project, then make sure you are connected to the daemon. Go to menu option Advanced / Select computer, choose your machine's name and enter the password. (To avoid this, make sure the above steps regarding gui_rpc_auth.cfg have been done.)

## Projects using GPU
If you want to use your GPU, you may need the proprietary nvidia or amd drivers.
For newer AMD systems such as the Ryzen 5 2400G you can simply install  on top of the open source AMDGPU to provide OpenCL capability for GPU work.
For Nvidia, you also need the package  located in extra. To prevent computation errors, you most likely need the 32-bit version of your OpenGL graphics driver. Certain tasks (such as Genefer on PrimeGrid) need the package  to work properly.

In addition, the boinc user should be in the  user group.

In order to suspend GPU computing when the computer is in use, the boinc user should have access to your X session so that mouse/keyboard input can be communicated to the client. This can be accomplished by installing the package  (Extra) and executing the following command:

 $ xhost si:localuser:boinc

You may want to autostart that on Xorg startup.

## BOINC via the CLI
Install  to use BOINC on a headless system. Two command-line management tools are available:  and .  is recommended. To use , you must:

# Start the BOINC service.
# Provide  with a password for communicating with the service's RPC API.

To start the BOINC service, use the provided  unit file. (For more information, see systemd#Using units.) The first time BOINC starts, it will generate a password and save it to . To provide  with this password, consider one of the following:

* Provide the password as a command-line flag, e.g. .
* Ensure a file named  is present in the current directory.

That done, you can register with a project and attach BOINC to the project.

To register with a project, you may be able to use the command-line client, or you may need to register with a separate website. To register with a project from the command-line, pick a project from BOINC Project List, and execute a command like {{ic|boinccmd --passwd abc123 --create_account ${project_url} ${my_email} ${project_password} ${project_username} }}. Regardless of how you register, you must obtain a key for each project you would like BOINC to attach to. To attach BOINC to a project, execute a command like {{ic|boinccmd --passwd abc123 --project_attach ${project_url} ${project_key} }}.

By default, BOINC uses at most 60% of available CPU time. If you wish to let boinc do more work, edit the CPU-related options in its configuration file:

You can see other available XML configuration options in the BOINC project's documentation.

## Controlling BOINC remotely
A "remote" RPC is one that comes from a different computer.

All remote RPCs (both status and control) are authenticated using the GUI RPC password.

By default, remote RPCs are not accepted from any host. To specify a set of hosts from which RPCs are allowed, create a file  in your BOINC data directory containing a list of allowed DNS host names or IP addresses (one per line). Only these hosts will be able to connect. The  file can also have comment lines that start with either a # or a ; character.

You can also set remote-allowed option  in the options section of a  file

You can see other available Client configuration in the BOINC project's documentation.

Alternatively, if you run the client with the  command line option, it will accept connections from any host (subject to password authentication). If you have a  file but also start the client with , the file will be ignored, and any host will be allowed to connect.

Note that the "Read config file" on the BOINC Manager, Advanced menu will also read in the  file i.e. a restart of the client is not required to enable changes to the remote host list.

## Log files
BOINC places log files in

 /var/lib/boinc/stderrdae.txt
 /var/lib/boinc/stdoutdae.txt

## Considerations when choosing a project
Projects have different minimum hardware requirements (CPU, disk space), and different times to taken to run each work unit. If you do not finish a work unit before the deadline it will sent out to someone else, but it is better to look around to see what projects suit your machine and your uptime patterns to avoid this happening.

Also, if it is important to you, check if the project makes the data and results publicly available.

## Running 32bit projects
Some projects provide only 32bit applications which may require 32bit libraries to run work units or show graphics.  You will find most of these libraries in the multilib repository.

To run WUs (e.g. Climateprediction), install , .

To show graphics (e.g. Several projects of WCG, Climateprediction, Quake-Catcher Network), install , , , , ,  and .

## Troubleshooting
## GPU missing
If you get this error :

and the Work Unit does not start, you should restart the  daemon.

This will happen if the BOINC daemon starts before the an X session is fully initialized.

## Laptop overheating and battery duration reduction
If you run BOINC on a laptop with the  scaling governor (the default), it will keep the CPUs at their maximum frequencies, (over)heating them, and decreasing battery duration. The best way to fix this is to set  to not rise the CPU frequencies for BOINC:

 # echo 1 >/sys/devices/system/cpu/cpufreq/ondemand/ignore_nice_load

To do this on boot, create the following tmpfile config:

## GPU work units insufficient memory
When attempting OpenCL based work units you may get the error:

 Sorry, at the moment your system doesn't have enough free CPU/GPU memory to run this task!

Edit the  and modify the line:

 ProtectSystem=strict

To:

 ProtectSystem=full

To apply the changes, do a systemd daemon-reload and restart the .
