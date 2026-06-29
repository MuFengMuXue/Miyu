Other languages:

[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=VirtualBox/tr "VirtualBox (5% translated)") • ‎[português do Brasil](//wiki.manjaro.org/index.php?title=VirtualBox/pt-br "VirtualBox (97% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=VirtualBox/ru "VirtualBox (100% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Installing Virtualbox on Manjaro]](#Installing_Virtualbox_on_Manjaro)
    -   [[2.1] [Enabling Virtualisation]](#Enabling_Virtualisation)
    -   [[2.2] [Install VirtualBox]](#Install_VirtualBox)
    -   [[2.3] [Install the Extension Pack(Optional)]](#Install_the_Extension_Pack.28Optional.29)
        -   [[2.3.1] [Install extensionpack using AUR]](#Install_extensionpack_using_AUR)
        -   [[2.3.2] [Get extensionpack from VirtualBox]](#Get_extensionpack_from_VirtualBox)
-   [[3] [Configuring the host]](#Configuring_the_host)
    -   [[3.1] [Adding Your Account to the **vboxusers** User Group]](#Adding_Your_Account_to_the_vboxusers_User_Group)
-   [[4] [Manjaro VBox guest]](#Manjaro_VBox_guest)
    -   [[4.1] [Selecting a Display Controller]](#Selecting_a_Display_Controller)
    -   [[4.2] [Troubleshooting Manjaro guest]](#Troubleshooting_Manjaro_guest)
    -   [[4.3] [Guest Configuration]](#Guest_Configuration)
-   [[5] [Advise, Tips, and Tricks]](#Advise.2C_Tips.2C_and_Tricks)
    -   [[5.1] [Guest Installation]](#Guest_Installation)
    -   [[5.2] [Guest Additions]](#Guest_Additions)
    -   [[5.3] [Guest Display]](#Guest_Display)
    -   [[5.4] [Guest Internet Connection]](#Guest_Internet_Connection)
-   [[6] [General Troubleshooting]](#General_Troubleshooting)
-   [[7] [See Also]](#See_Also)

## [Overview]

[![Vbox.png](/images/f/ff/Vbox.png)](//wiki.manjaro.org/index.php?title=File:Vbox.png)

Developed by Sun Microsystems, now Oracle Corporation, **[VirtualBox](https://www.virtualbox.org/)** is a popular application that allows for other operating systems (known as *Guests*) to be installed and run within an existing operating system (known as the *Host*). This is undertaken through the process of *virtualisation*, whereby virtual versions of your computer (also referred to as *virtual machines* or *VMs*) are created within and draw resources directly from the host system. As such, how fast or powerful a virtual machine may be will depend entirely on the resources available - and allocated - for it to use. The benefits of virtualisation include:\

-   The fast and easy installation of other operating systems without affecting your existing system (e.g. no need for dual booting and/or preparation in the form of hard disk partitioning or re-sizing)
-   Completely safe learning and experimentation with operating systems, as nothing that occurs within a Guest will affect the Host (e.g. the Host operating system can also be installed as a Guest in a virtual machine as a risk-free means of trying out new things), and
-   An almost unlimited capacity to install as many additional operating systems as desired\...provided space is available on your hard drive to store them!

## [Installing Virtualbox on Manjaro]

### [Enabling Virtualisation]

Before installing VirtualBox, it is important to first ensure that **virtualization** has been enabled in your BIOS. The exact instructions for doing this vary based on your hardware. Please review the manual provided by your computer or motherboard manufacturer for specific instructions.

### [Install VirtualBox]

**List the installed and currently running kernel on your system and make sure it\'s supported:**

[user \$ ][ mhwd-kernel -li [COPY TO CLIPBOARD]]

\

To install VirtualBox, you need to install the packages `virtualbox` and `linux*-virtualbox-host-modules`. The latter must match the version of the kernel you are running. To list what kernels is installed use mhwd (example)

\

[\$] [mhwd-kernel -li]\

    Currently running: 6.6.17-1-MANJARO (linux66)
    The following kernels are installed in your system:
       * linux66

\
To install VirtualBox and the kernel modules for your installed kernel enter the following command in the terminal - continuing the above example:

[user \$ ][ sudo pacman -Syu virtualbox linux66-virtualbox-host-modules [COPY TO CLIPBOARD]]

\

Once the installation has completed, it will then be necessary to add the *VirtualBox Module* to your kernel. **The easy way is to simply reboot your system**. Otherwise, to start using VirtualBox immediately, enter the following command:

[user \$ ][ sudo vboxreload [COPY TO CLIPBOARD]]

\

### [][Install the Extension Pack(Optional)]

The extension pack is a proprietary set of extensions providing extra functionality to VirtualBox like USB2 and USB3 passthrough. You only need this if you are going to use the functionality provided and it is **not required** for VirtualBox to function.

-   Oracle Cloud Infrastructure integration
-   USB 2.0 and USB 3.0 Host Controller
-   Host Webcam
-   VirtualBox RDP
-   PXE ROM
-   Disk Encryption
-   NVMe

\

**Info**

------------------------------------------------------------------------

As noted by VirtualBox - it is important you are using the extension pack matching your installed version of VirtualBox.\
**Please install the same version extension pack as your installed version of VirtualBox.** -- [VirtualBox Download page](https://www.virtualbox.org/wiki/Downloads)

\
Check your VirtualBox version (example)

\

[\$] [vboxmanage \--version]\

    7.0.14r161095

\

#### [Install extensionpack using AUR]

Locate the correct AUR PKGBUILD using pamac (or the AUR helper of choice) - example is using **pamac**

**Info**

------------------------------------------------------------------------

AUR PKGBUILDs labelled manjaro is **not** maintained by Manjaro!

\

\

[\$] [pamac search \--aur virtualbox-ext-oracle]\

    virtualbox6-ext-oracle  6.1.x-5                               AUR
        Oracle VM VirtualBox Extension Pack 6.1.48 (stable)
    virtualbox6.1-ext-oracle  6.1.50-1                            AUR
        Oracle VM VirtualBox Extension Pack (version 6.1)
    virtualbox-ext-oracle-dev  7.0.97.161344-1                    AUR
        Oracle VM VirtualBox Extension Pack for virtualbox dev
        version
    virtualbox-ext-oracle  7.0.14-1                               AUR
        Oracle VM VirtualBox Extension Pack

\
When you have found the match you can install using the helper - example is using pamac

[user \$ ][ pamac build virtualbox-ext-\<your-decision\> [COPY TO CLIPBOARD]]

\

#### [Get extensionpack from VirtualBox]

Same rule apply - match your VirtualBox version - usually the latest version applies.

> [Downloads -- Oracle VM VirtualBox](https://www.virtualbox.org/wiki/Downloads)

If the latest version do not match yours - you can find earlier versions using this page

> [Download Old Builds - Oracle VM Virtualbox](https://www.virtualbox.org/wiki/Download_Old_Builds)

The extension **.vbox-extpack** is a registered mime extension so just open the file and VirtualBox will install the extension pack. Provide your password when asked.

## [Configuring the host]

### [Adding Your Account to the **vboxusers** User Group]

The final step is to now add your personal user account to the `vboxusers` group. This is necessary in order to fully access the features provided by VirtualBox. The **\$USER** variable translates to the currently logged in user and you must logout or restart for the change to take effect.

[user \$ ][ sudo gpasswd -a \$USER vboxusers [COPY TO CLIPBOARD]]

\

## [Manjaro VBox guest]

For those intending to use Manjaro under VirtualBox, you can install Manjaro as usual. Please observe below point of setting the correct display type.

### [Selecting a Display Controller]

Before installation of Manjaro Guest set display controller to VMSVGA

The VirtualBox guideline is

-   select VMSVGA for a Linux guest
-   select VBoxSVGA for a Windows guest

If you are using a Desktop utilizing wayland, enable 3D for best experience.

### [Troubleshooting Manjaro guest]

If you deem it necessary to ensure the packages are installed please follow this recipe

\

[\$] [mhwd-kernel -li]\

     Currently running: 6.6.17-1-MANJARO (linux66)
     The following kernels are installed in your system:
        * linux66

[user \$ ][ sudo pacman -Syu virtualbox-guest-utils [COPY TO CLIPBOARD]]

\

### [Guest Configuration]

You will need to load the modules if you don\'t want to reboot:

[user \$ ][ sudo modprobe vboxguest vboxvideo vboxsf [COPY TO CLIPBOARD]]

\

The guest utils than need to be started and enabled:

[user \$ ][ sudo systemctl enable \--now vboxservice.service [COPY TO CLIPBOARD]]

\

Add you VM user to the vboxsf group (this requires you to logout to apply the new group)

[user \$ ][ sudo usermod -aG vboxsf \$ [COPY TO CLIPBOARD]"}]

\

Create media folder in root directory if it does not already exist

[user \$ ][ sudo mkdir /media [COPY TO CLIPBOARD]]

\

Assign the correct permissions to the media folder to be able to access shared folders

[user \$ ][ sudo chmod 755 /media [COPY TO CLIPBOARD]]

\

## [][Advise, Tips, and Tricks]

Advice on using Virtualbox effectively, as well as some tips and tricks learned along the way, have been provided for the benefit of new users.

### [Guest Installation]

-   Virtualbox can run installation files (ISOs) directly as virtual discs, so there is no need to burn them to an installation medium such as a disc or USB data stick.
-   The process to install any Guest operating system, [including Manjaro](//wiki.manjaro.org/index.php?title=Installation_Guides "Installation Guides"), is exactly the same as if actually installing for real on your computer.

### [Guest Additions]

Guest Additions are special software packages designed to improve the performance and usability of guest operating systems.

They are installed within the Guest operating system itself, and most notably result in enhancing the display resolution, as well as enabling much better control over the mouse. As such, two tell-tale signs that Guest Additions have not been installed in a Guest are that the display will not scale to the size of the display window (i.e. it will be necessary to scroll around to see the whole screen), and the mouse may be quite hard to control.

Instructions for installing the guest additions in Manjaro are provided above. For other operating systems please review the VirtualBox instructions [linked below](#See_Also)

### [Guest Display]

If you are using other guests e.g. Ubuntu, Linux Mint and others be sure to use the default VMSVGA display driver.

It will be necessary to activate the **Enable 3D acceleration** box in order to allow for some desktop effects (such as transparency) to be shown. This can be undertaken by going into the settings menu, and then selecting the **Display** section.

If you are getting screen distortion or transparent dialogs using Windows guest - shutdown the VM and change the graphics settings of the VM. Remove the checkbox for **Enable 3D acceleration**.

### [Guest Internet Connection]

Some users have encountered problems when attempting to connect their virtual machine to the internet using the default VirtualBox settings. Where this is the case, try the following solution

-   Click the **Settings Button** and then select the **Network** tab
-   Next to the **Attached to** heading is a button that states **NAT**. Click it to reveal a drop down menu and select **Bridged Adapter** instead.
-   Next to the **Name** heading is a button whereby you may select how you are currently connected to the internet (e.g. *Wlan* means Wireless, and *Eth0* means Ethernet). Select the appropriate connection type you are currently using.
-   Click the **OK** button to confirm.

## [General Troubleshooting]

-   A VirtualBox installation will not automatically detect when USB device has been connected. As such, it is therefore necessary to click the USB icon located at the bottom of the VirtualBox window in order to select and activate it.
-   It is possible to enable the (very useful) ability to copy and paste text between the Guest and Host systems. This is undertaken by clicking **Settings** button and then going to the **General** Section.
-   Don\'t be afraid to take risks, to experiment, and to have fun with Guest operating systems. The worst that can happen is that they will have to be re-installed!

## [See Also]

-   [VirtualBox Installation, USB and Shared Folders Forum Wiki HowTo](https://https://forum.manjaro.org/t/howto-virtualbox-installation-usb-shared-folder/1178)
-   The official [VirtualBox Manual](http://www.virtualbox.org/manual/)