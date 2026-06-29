[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-How+to+mount+Windows+%28NTFS%29+filesystem+due+to+hibernation&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=How_to_mount_Windows_(NTFS)_filesystem_due_to_hibernation "How to mount Windows (NTFS) filesystem due to hibernation (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=How_to_mount_Windows_(NTFS)_filesystem_due_to_hibernation/tr "Hazırda bekletme nedeniyle Windows (NTFS) dosya sistemi nasıl bağlanır (3% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=How_to_mount_Windows_(NTFS)_filesystem_due_to_hibernation/ru "Как смонтировать файловую систему Windows (NTFS) из-за спящего режима (100% translated)")

## Contents

-   [[1] [A bug \[1\]]](#A_bug_.5B1.5D)
    -   [[1.1] [Explanation: Why Linux can\'t open hibernated Windows partitions]](#Explanation:_Why_Linux_can.27t_open_hibernated_Windows_partitions)
-   [[2] [Workaround for all versions of Windows]](#Workaround_for_all_versions_of_Windows)
    -   [[2.1] [Manually mount the filesystem in read only mode]](#Manually_mount_the_filesystem_in_read_only_mode)
    -   [[2.2] [The Third Option]](#The_Third_Option)
-   [[3] [Solution (only for Windows 8 and 10)]](#Solution_.28only_for_Windows_8_and_10.29)

# [][A bug [\[1\]](https://bugs.launchpad.net/ubuntu/+source/ntfs-3g/+bug/1008117)]

has been filed about the Nautilus dialog you are seeing as it recommends a potentially dangerous option that could result in data loss. Please do not run the command in this dialog unless you want to delete your saved Windows session and potentially lose unsaved work.

## [][Explanation: Why Linux can\'t open hibernated Windows partitions]

You are seeing this error because you hibernated Windows instead of turning it off the normal way (in newer versions of Windows, hibernate might be the default option).

Hibernating saves the current state information to the hard disk and then powers down the computer. Shutting down the computer closes all programs and ends all running processes before powering down the computer.

When you turn off Windows by hibernating it, you are essentially pausing the system and saving all of that information (into a big file called **hiberfil.sys**). This way when you resume from hibernation all of your applications and files will be exactly how you left them. It also sets a flag in hiberfil.sys to let other Operating Systems know that Windows is hibernated.

Making changes to your Windows (ntfs) partition while it is hibernated could be dangerous\--it could cause Windows to not resume from hibernation or to crash after resuming. Because of this, the tool (ntfs-3g) that mounts (opens) the partition will not mount it in read-write mode if it sees a hibernation flag. As such, Nautilus, the default file browser, will not be able to automatically open this partition\--hence the error message that you see\--because it is trying to open it in read-write mode.

# [Workaround for all versions of Windows]

There are three ways to mount a hibernated Windows partition:

Boot into Windows and power down the system by shutting it down completely. You may then boot back into Manjaro and the partition will mount in read-write mode automatically when you open it in Nautilus.

\

**Note**

------------------------------------------------------------------------

that the \"Shut Down\" option may not be the one displayed in your start menu by default. You may need to click the button next to it to see further options.

### [Manually mount the filesystem in read only mode]

Check to see if you have a mount point (folder for mounting your partition in) for your Windows partition in the folder **/media** using this command:

[user \$ ][ ls /media [COPY TO CLIPBOARD]]

\

If you don\'t see a folder for your Windows partition, you should create one with the following command:

[user \$ ][ sudo mkdir /media/windows [COPY TO CLIPBOARD]]

\

Next, mount the partition in read-only mode onto this folder with this command:

[user \$ ][ mount -t ntfs-3g -o ro /dev/sda3 /media/windows [COPY TO CLIPBOARD]]

\

**Note:** that you should change **/media/windows** if your mountpoint is called something else.

\
Now you will be able to view/open files on your Windows partition using any program in Manjaro. However you will not be able to write to the partition or modify any files as it is in read only mode.

## [The Third Option]

If you need to mount the partition in read-write mode and are not able to or willing to boot into Windows and shut it down completely there is a third option. However, it is not included here because it completely deletes hiberfil.sys and will cause you to lose all unsaved information in the hibernated Windows programs. The following is a quotation from man ntfs-3g about the option that would be used to do this.

    remove_hiberfile

    Unlike in case of  read-only  mount,  the  read-write  mount  is
    denied  if  the  NTFS  volume is hibernated. One needs either to
    resume Windows and shutdown it  properly,  or  use  this  option
    which  will  remove  the  Windows hibernation file. Please note,
    this means that the saved Windows  session  will  be  completely
    lost. Use this option under your own responsibility.

# [][Solution (only for Windows 8 and 10)]

There is a new feature in **Windows 8** called **Fast Startup** [\[2\]](http://www.typicaltips.com/2013/02/disable-fast-startup-in-windows-8.html). If this feature is enabled (which it is by default), Windows 8 does not actually completely shutdown when you choose shutdown. Instead, it does a \"hybrid shutdown\". This is something like hibernating; it makes booting Windows 8 back up faster. So, you need to disable this feature to be able to shut it down properly, and be able to mount the Windows partitions. To do this, boot into your Windows 8 and:

\

**Note**

------------------------------------------------------------------------

disabling Fast Startup will most likely make your Windows 8 take a longer time to boot. There are no \"exact\" numbers, but let\'s say that if it took you 10 seconds to boot into Windows 8, it will now take you 50 seconds after disabling this feature.

    1. Open Control Panel in the small icons view and click on Power Options.
    2. Click on Choose what the power buttons do (look in the left hand column).
    3. Click on Change settings that are currently unavailable.
    4. Uncheck Turn on fast startup (recommended).

Click on **Save changes**. Now, shutdown Windows 8 and boot back into Manjaro.

If you still aren\'t able to mount without getting errors, you may need to turn off hibernation completely. Open an elevated Command Prompt (right click on the shortcut, click on **Run as Administrator**), and input:

[user \$ ][ powercfg /h off [COPY TO CLIPBOARD]]

\

Source: Fast Startup - Turn On or Off in Windows. [\[3\]](http://www.eightforums.com/tutorials/6320-fast-startup-turn-off-windows-8-a.html)