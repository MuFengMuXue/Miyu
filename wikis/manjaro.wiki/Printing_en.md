[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Printing&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Printing "Printing (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Printing/ru "Печать (100% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Installing the Printer Software]](#Installing_the_Printer_Software)
-   [[3] [Enabling Printing Capabilities]](#Enabling_Printing_Capabilities)
-   [[4] [Managing Printers]](#Managing_Printers)
    -   [[4.1] [Managing Printers with HP Device Manager]](#Managing_Printers_with_HP_Device_Manager)
    -   [[4.2] [Managing Printers with CUPS]](#Managing_Printers_with_CUPS)
        -   [[4.2.1] [CUPS Webpage Interface]](#CUPS_Webpage_Interface)
        -   [[4.2.2] [CUPS Desktop Interface Part 1: The Automatic Method]](#CUPS_Desktop_Interface_Part_1:_The_Automatic_Method)
        -   [[4.2.3] [CUPS Desktop Interface Part 2: The Manual Method]](#CUPS_Desktop_Interface_Part_2:_The_Manual_Method)
        -   [[4.2.4] [Modifying an Installed Printer]](#Modifying_an_Installed_Printer)
        -   [[4.2.5] [Removing an Installed Printer]](#Removing_an_Installed_Printer)
-   [[5] [Disabling Printing Capabilities]](#Disabling_Printing_Capabilities)
-   [[6] [Specific printers/scanners that are known to work]](#Specific_printers.2Fscanners_that_are_known_to_work)

# [Overview]

Printing is undertaken through the use of [CUPS](http://en.wikipedia.org/wiki/CUPS) (previously an acronym for **C**ommon **U**nix **P**rinting **S**ystem). This is a popular open source printing system used in most Linux distributions due to its ease of use.

\

# [Installing the Printer Software]

First, install the `manjaro-printer` package using your favorite package manager or by using the command:

[user \$ ][ pamac install manjaro-printer [COPY TO CLIPBOARD]]

\

Note that you may need to add yourself to the `sys` group. To do this, use the command:

[user \$ ][ sudo gpasswd -a your_username sys [COPY TO CLIPBOARD]]

\

Some HP printers require proprietary software technologies to allow full access to printer features and performance. Unfortunately, these technologies cannot be open sourced by HP. To resolve this, HP uses a binary plugin for these printers. This does not come preinstalled with Manjaro as the license prohibits redistributing it. However an [AUR](//wiki.manjaro.org/index.php?title=Arch_User_Repository "Arch User Repository") package is available.

[user \$ ][ pamac build hplip-plugin [COPY TO CLIPBOARD]]

\

For a list of affected HP printers, please see the [HP developers page](https://developers.hp.com/hp-linux-imaging-and-printing/binary_plugin.html).

# [Enabling Printing Capabilities]

Once the necessary software has been installed, to start and enable printing capabilities, enter the following commands:

[user \$ ][ sudo systemctl enable \--now cups.service [COPY TO CLIPBOARD]]

\

[user \$ ][ sudo systemctl enable \--now cups.socket [COPY TO CLIPBOARD]]

\

[user \$ ][ sudo systemctl enable \--now cups.path [COPY TO CLIPBOARD]]

\

If easy detection of network printers is needed (not all editions have avahi installed and running) the following service can be installed & started:

[user \$ ][ pamac install avahi [COPY TO CLIPBOARD]]

\

[user \$ ][ sudo systemctl enable \--now avahi-daemon.service [COPY TO CLIPBOARD]]

\

\
At this point you should be ready to configure a printer

# [Managing Printers]

## [Managing Printers with HP Device Manager]

[![Hplip.png](/images/thumb/2/21/Hplip.png/375px-Hplip.png)](//wiki.manjaro.org/index.php?title=File:Hplip.png)

\
If have a printer made by HP, the easiest way to manage it is with the HP Device Manager(`hp-toolbox`). It is wizard based and handles automatic detection and setup of your printer locally or across a network.

You can run it by selecting **HP Device Manager** from the menu or with the command `hp-toolbox`.

\

## [Managing Printers with CUPS]

Another way to add a printer is to use CUPS directly. Assuming CUPS has been enabled (and started), upon connecting a printer, it should be automatically detected and configured for you to use. The process itself should take only about a minute. However, if the automatic detection and configuration doesn\'t seem to work, then your printer can be manually set up with relative ease. There are two methods to do so:

\

-   **Webpage Interface**: CUPS provides an webpage interface that will open in your default web browser to configure your printer. This interface also provides access to further information about CUPS, as well as on-line help.

<!-- -->

-   **Desktop Interface**: A standard desktop wizard is also available, which should be instantly familiar to those who have configured a printer before, whether using Linux or another operating system such as windows. Note that you may need to install your DE\'s printer config package using your favorite package manager or by using one of the following commands.

GNOME:

[user \$ ][ pamac install system-config-printer [COPY TO CLIPBOARD]]

\

KDE:

[user \$ ][ pamac install print-manager [COPY TO CLIPBOARD]]

\

### [CUPS Webpage Interface]

[![CUPSweb.png](/images/thumb/0/01/CUPSweb.png/375px-CUPSweb.png)](//wiki.manjaro.org/index.php?title=File:CUPSweb.png)

[](//wiki.manjaro.org/index.php?title=File:CUPSweb.png "Enlarge")

\
To access the webpage interface, select **Manage Printing** from your desktop menu. The interface will automatically open in your default web browser. Alternatively, you can also open your choice of web browser, and enter the following into the address bar:

    http://localhost:631/

\

**Tip**

------------------------------------------------------------------------

You can also just click the address provided above to access the CUPS web interface!

\

\

### [CUPS Desktop Interface Part 1: The Automatic Method]

[![CUPS1.png](/images/thumb/f/ff/CUPS1.png/375px-CUPS1.png)](//wiki.manjaro.org/index.php?title=File:CUPS1.png)

[](//wiki.manjaro.org/index.php?title=File:CUPS1.png "Enlarge")

\
**1. Add your printer**. Ensuring that your printer is properly connected and switched on, select **Print Settings** from your desktop menu. Once the *Print Settings* window has opened, click **+ add** to add a new printer.\

\

[![CUPS2.png](/images/thumb/8/83/CUPS2.png/375px-CUPS2.png)](//wiki.manjaro.org/index.php?title=File:CUPS2.png)

[](//wiki.manjaro.org/index.php?title=File:CUPS2.png "Enlarge")

\
**2. Select your printer name**. Once the *New Printer* window has opened, under the **Select Device** heading, find the name of your printer and click to highlight it. If your printer is listed more than once, check the description on the right to ensure your selection is not for another function, such as scanning or faxing.

\
**3. Select your printer connection**. Under the **Connection** heading, click to highlight your printer\'s connection method. As illustrated, this will usually always be \'USB\'.\

\

[![CUPS3.png](/images/thumb/6/63/CUPS3.png/375px-CUPS3.png)](//wiki.manjaro.org/index.php?title=File:CUPS3.png)

[](//wiki.manjaro.org/index.php?title=File:CUPS3.png "Enlarge")

\
**4. Install your printer driver**. Once your printer name and connection have been highlighted, click the **Forward** button and CUPS will automatically search for the available drivers for it. In most instances, once the appropriate driver has been found it will be automatically installed, and the set-up process will have completed.

Otherwise, if the process did not succeed, it will be necessary to click the forward button again in order chose the appropriate driver yourself.\

\

### [CUPS Desktop Interface Part 2: The Manual Method]

[![CUPS4.png](/images/thumb/0/0f/CUPS4.png/375px-CUPS4.png)](//wiki.manjaro.org/index.php?title=File:CUPS4.png)

[](//wiki.manjaro.org/index.php?title=File:CUPS4.png "Enlarge")

\

**Tip**

------------------------------------------------------------------------

CUPS will usually help you out by showing recommended choices for each step.

**1. Select your printer make**. If the Automatic method did not automatically find and install an appropriate driver for your printer, then clicking the forward button again will present the *Chose Driver* window. The first step is to select the make of your printer. As illustrated, as an HP printer is to be installed, the recommended choice of *HP* has been highlighted by clicking on it.

Once your make of printer has been highlighted, click the forward button to proceed to the next step.\

\

[![CUPS5.png](/images/thumb/6/6a/CUPS5.png/375px-CUPS5.png)](//wiki.manjaro.org/index.php?title=File:CUPS5.png)

[](//wiki.manjaro.org/index.php?title=File:CUPS5.png "Enlarge")

\
**2. Select your printer model**. Under the left-heading **models**, select the specific model of your printer. As illustrated, as the printer model to be installed in this instance is a Model 2210, the recommended choice of *PSC 2210* has been highlighted by clicking on it.

\
**3. Select your printer driver**. At last! Under the right-heading **Drivers**, select the appropriate driver for your printer. As illustrated, the recommended printer driver has been clicked to highlight it. **It is advised that you also select whatever driver is recommended for you**.

Once your printer model and driver have been highlighted, click the forward button to proceed to the next step.\

\

[![CUPS6.png](/images/thumb/0/0d/CUPS6.png/375px-CUPS6.png)](//wiki.manjaro.org/index.php?title=File:CUPS6.png)

[](//wiki.manjaro.org/index.php?title=File:CUPS6.png "Enlarge")

\
**4. Choose your printer name, description (optional), and location (optional)**. Unless you want to change something, it will not be necessary to make any amendments here.

If you are happy with the information provided - or have made the desired changes - click the **Apply** button to complete the process.\

\

[![CUPS7.png](/images/thumb/4/4e/CUPS7.png/375px-CUPS7.png)](//wiki.manjaro.org/index.php?title=File:CUPS7.png)

[](//wiki.manjaro.org/index.php?title=File:CUPS7.png "Enlarge")

\
**5. Configure your printer**. Having clicked the Apply button in the previous step, your printer\'s properties will be displayed. By selecting the categories on the right-hand side, you can view information and amend your printer\'s settings if you wish. **The standard settings will be fine for most people, so unless you have something specific in mind, there will be nothing you need to do**.

\
**6. Test your printer**. Although optional, this step is highly recommended! Click the **Print Test Page** button to ensure that your printer is set up and working properly.

\

**Tip**

------------------------------------------------------------------------

Your printer properties can be accessed - and changed - at any time by selecting the **Print Settings** option from your menu, and then double-clicking your printer\'s icon.

That\'s it! Now click the **OK** button to close the window and start using your printer.\

### [Modifying an Installed Printer]

To configure an installed printer at any time:

**1.** select the **Print Settings** option from your desktop menu, and

**2.** double-click the printer\'s icon.

The configuration window will appear. Select any of the categories on the left-hand side of the window to view the appropriate information and make any desired changes. Once complete, click the **Apply** and then **OK** buttons to confirm and save your changes, or click the **Cancel** button to close the window without making any changes.

\

### [Removing an Installed Printer]

If for any reason you wish to remove a printer (e.g. to reinstall it), select the **Print Settings** option from your menu, right-click your printer\'s icon, and then select **delete**. You will need to confirm your decision to delete the printer, as well as enter your password to complete the task.

\

# [Disabling Printing Capabilities]

If for any reason you wish to disable CUPS (e.g. in order to use an alternative printing system), open your terminal and enter the following command:

[user \$ ][ sudo systemctl disable \--now cups.service [COPY TO CLIPBOARD]]

\

[user \$ ][ sudo systemctl disable \--now cups.socket [COPY TO CLIPBOARD]]

\

[user \$ ][ sudo systemctl disable \--now cups.path [COPY TO CLIPBOARD]]

\

\

# [][Specific printers/scanners that are known to work]

  ------- ---------------- ---------------------------- ------------------ -------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------- --
  Brand   Type             Print                        Scan               Description how to set up                                                                                                              Issues & Solutions                                                                                                                                                                      More info
  Canon   mp 280           Yes, via network             Yes, only local    CUPS and manjaro-printer                                                                                                               Remote scanning
  Canon   Pixma MX535      Yes, via network             Yes, via network   Manjaro printer detects remote printer as mx530. scanner needs scangearmp2-sane-git to function properly                               Needs avahi and in my case ipv6 for some reason to be able to \'see\' the printer (@hanzel on the forum)
  Canon   PIXMA TR4522                                                     Needs: cnijfilter2 or cnijfilter2-bin from the [AUR](//wiki.manjaro.org/index.php?title=Arch_User_Repository "Arch User Repository")                                                                                                                                                                                           [forum post](https://forum.manjaro.org/t/installing-a-canon-pixma-tr4522/78221)
  Canon   PIXMA TS5120     Yes                          Yes                Scanner seems to work after CUPS and manjaro-printer, printing requires cnijfilter and selecting Canon TS5100 series drivers           Needs: cnijfilter2 or cnijfilter2-bin from the [AUR](//wiki.manjaro.org/index.php?title=Arch_User_Repository "Arch User Repository")
  Canon   Pixma Pro-100    Yes, via network and local   Not a feature      manjaro-printer                                                                                                                        Takes a moment to start printing, just be patient
  Canon   ISensys          LBP223dw                     Yes                                                                                                                                                                                                                                                                                                                                               [forum post](https://forum.manjaro.org/t/installation-canon-i-sensys-lbp223dw/80306)
  Canon   Pixma E4270      Yes via Network              not tested         Needs: cnijfilter2 or cnijfilter2-bin from the [AUR](//wiki.manjaro.org/index.php?title=Arch_User_Repository "Arch User Repository")                                                                                                                                                                                           [forum post](https://forum.manjaro.org/t/canon-pixma-e4270/86212)
  Canon   Pixma G2100      Yes                          Yes                Plug& play                                                                                                                                                                                                                                                                                                                     [forum post](https://forum.manjaro.org/t/does-canon-printers-well-supported/87040/5)
  Canon   PIXMA MG3650                                  Yes                                                                                                                                                                                                                                                                                                                                               [forum post](https://forum.manjaro.org/t/troubles-with-printing-on-canon-pixma-mg3650/136112/1)
  Epson   ET-M1120         Yes, via Network             Not a feature      manjaro-printer and system-config-printer                                                                                              Needs: epson-inkjet-printer-escpr and epson-inkjet-printer-escpr2 in [AUR](//wiki.manjaro.org/index.php?title=Arch_User_Repository "Arch User Repository") and then patch from pacman
  Epson   WF-3825 driver                                                   Needs: epson-inkjet-printer-escpr2 [AUR](//wiki.manjaro.org/index.php?title=Arch_User_Repository "Arch User Repository")                                                                                                                                                                                                       [Forum post](https://forum.manjaro.org/t/epson-wf-3825-driver/77910/5)
  ------- ---------------- ---------------------------- ------------------ -------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------- --

Table made from suggestion [here](https://forum.manjaro.org/t/printer-overview-and-functionality-on-manjaro/79794)