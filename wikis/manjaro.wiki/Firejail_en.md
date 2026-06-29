[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Firejail&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Firejail "Firejail (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Firejail/tr "Firejail (SUID) (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Firejail/ru "Firejail (100% translated)")

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Install firejail]](#Install_firejail)
-   [[3] [Using Firejail]](#Using_Firejail)
-   [[4] [GUI]](#GUI)
-   [[5] [Block an application from accessing the internet]](#Block_an_application_from_accessing_the_internet)

## [Introduction]

[Firejail](https://github.com/netblue30/firejail) is a very easy to use piece of software, initially developed to make Firefox more secure by isolating it (putting it in a sandbox) from the rest of your system. Firejail has developed beyond that & can be used simultaneously on many parts of your system. It is worth reading about on Firejail site (linked to above).

From the Github page:

> Firejail is a SUID sandbox program that reduces the risk of security breaches by restricting the running environment of untrusted applications using Linux namespaces, seccomp-bpf and Linux capabilities. It allows a process and all its descendants to have their own private view of the globally shared kernel resources, such as the network stack, process table, mount table.

\

## [Install firejail]

Firejail is available in the repos. Install it using your graphical package manager or with pacman.

    sudo pacman -S firejail

\

## [Using Firejail]

Simply prefix your command or application with *firejail*. Example:

    firejail firefox

You can even integrate firejail into your whole desktop. Every application you launch will use the firejail sandbox if it is supported by default. To do this use the command

    sudo firecfg

For a list of all supported applications see [here](https://github.com/netblue30/firejail/blob/master/src/firecfg/firecfg.config)

\

## [GUI]

The firejail team also develops a graphical user interface for firejail called *firetools*. It is available in the [Arch User Repository](//wiki.manjaro.org/index.php?title=Arch_User_Repository "Arch User Repository").

\

## [Block an application from accessing the internet]

You can use the option *---net=none* to ensure firejail does not allow any network access like so:

    firejail –-net=none thunderbird

But that option will block local network access, such as access to shared folders. To still have local network access, but block the application from accessing the internet use option *\--protocol=unix*. Example:

    firejail --protocol=unix thunderbird