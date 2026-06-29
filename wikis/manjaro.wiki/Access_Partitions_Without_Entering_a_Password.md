+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![Tango-dialog-warning.png](/images/d/d8/Tango-dialog-warning.png)](//wiki.manjaro.org/index.php?title=File:Tango-dialog-warning.png) | **This article or section is out of date.**                                                                                                                                                                                                                                                                                                                                                                                                                                             | [![Tango-dialog-warning.png](/images/d/d8/Tango-dialog-warning.png)](//wiki.manjaro.org/index.php?title=File:Tango-dialog-warning.png) |
|                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                          | :::                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                          | **Reason:** This information is now obsolete but kept for historical reasons! [Fhdk](//wiki.manjaro.org/index.php?title=User:Fhdk "User:Fhdk") ([talk](//wiki.manjaro.org/index.php?title=User_talk:Fhdk&action=edit&redlink=1 "User talk:Fhdk (page does not exist)")) ([Discuss](//wiki.manjaro.org/index.php?title=Talk:Access_Partitions_Without_Entering_a_Password&action=edit&redlink=1 "Talk:Access Partitions Without Entering a Password (page does not exist)")) |                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                          | :::                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## [Overview]

A particular nuisance for many users is the need to enter a password in order to access other partitions present on their hard disk. In addition, those who installed Openbox 0.8.3 have also encountered the additional issue of having to enter a their passwords in order to eject removable media such as USB sticks and CD/DVDs.

This is due to the default policy/permissions settings implemented by a program called *UDisks2*, which itself is responsible for mounting partitions and removable media. In essence, permissions for mounting are set by default to Root / Administrator level only, rather than the user. Fortunately, this issue can be easily \--and permanently\-- resolved by creating a special file called **99-manjaro.rules** to override the default permissions, consequently resulting in no further need to enter a password.

## [Create 99-manjaro.rules file]

You will need to first open your terminal in order to create the *99-manjaro.rules* file. The syntax of the command to edit the rules file:

[user \$ ][ sudo \[text editor\] /etc/polkit-1/rules.d/99-manjaro.rules [COPY TO CLIPBOARD]]

\

For example, if you wish to edit the file within the terminal using nano (a standard terminal-based text editor) then enter:

[user \$ ][ sudo nano /etc/polkit-1/rules.d/99-manjaro.rules [COPY TO CLIPBOARD]]

\

Otherwise, if you have installed the full version of Manjaro (i.e. not the NET-Edition), you may find it easier to use a text editor like *Gedit* or *Leafpad* instead. This will create and open the *99-manjaro.rules* file up as a document, making it easier to read and edit. To use *Gedit* instead, the command is:

[user \$ ][ gksu gedit /etc/polkit-1/rules.d/99-manjaro.rules [COPY TO CLIPBOARD]]

\

## [Edit *99-manjaro.rules*]

**Warning**

------------------------------------------------------------------------

If you decide to manually type in the necessary command yourself, ensure that it is entered [exactly] as illustrated below.

Once the blank file has been opened, copy and paste in the following command to override the default permissions used by *UDisks2*:

/etc/polkit-1/rules.d/99-manjaro.rules

    polkit.addRule(function(action, subject)
    });

Once you have completed the new file, save the changes and close it by:

-   **nano**: Press [CTRL] and [x] to exit, [y] to save, and [enter] to finish
-   **Gedit or Leafpad**: Select the \'save\' option and then close the window.

**Now reboot your system for the changes to take effect.**