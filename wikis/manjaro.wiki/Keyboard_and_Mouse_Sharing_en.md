[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Keyboard+and+Mouse+Sharing&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Keyboard_and_Mouse_Sharing "Keyboard and Mouse Sharing (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Keyboard_and_Mouse_Sharing/ru "Совместное использование клавиатуры и мыши (100% translated)")

## Contents

-   [[1] [Overview]](#Overview)
    -   [[1.1] [So What Does Synergy Do?]](#So_What_Does_Synergy_Do.3F)
    -   [[1.2] [Bug Awareness]](#Bug_Awareness)
    -   [[1.3] [The Synergy Server:]](#The_Synergy_Server:)
        -   [[1.3.1] [Installation:]](#Installation:)
        -   [[1.3.2] [Configuration:]](#Configuration:)
        -   [[1.3.3] [Synergy.conf]](#Synergy.conf)
    -   [[1.4] [The Synergy Client(s):]](#The_Synergy_Client.28s.29:)
        -   [[1.4.1] [Client /etc/hosts:]](#Client_.2Fetc.2Fhosts:)
        -   [[1.4.2] [\~/.xinitrc]](#.7E.2F.xinitrc)
    -   [[1.5] [Conclusion:]](#Conclusion:)

**Note**

------------------------------------------------------------------------

This page it out of date. It should be updated to include barrier as well

# [Overview]

[Synergy](http://synergy-foss.org/) is a brilliant piece of software that doesn\'t require much effort to get going, Though faultless autostart did require some configuration.\

## [][So What Does Synergy Do?]

I can now use my favourite keyboard & mouse to operate two computers (synergy will do plenty more computers if you have them) one at a time of course\...

With two machines set to load synergy when they boot it doesn\'t matter what order the server or the client is booted in.

Synergy uses next to no system resources and even shares the clipboard as well!\

## [Bug Awareness]

Running Openbox, I can\'t make use of synergy until OB has loaded. But some Linux display managers you can use it before hand.

While it should already be fixed, there is an old bug that can produce 1-2 second black screens. For most this is fixed by issuing the command

    xset -dpms

If necessary, the command can be placed in *\~/.xinitrc* so the problem never appears.\

## [The Synergy Server:]

### [Installation:]

Rather than me duplicating it, the Archwiki has a great page on [Synergy installation](https://wiki.archlinux.org/index.php/Synergy).

\

### [Configuration:]

My **/etc/hosts** file follows which should speak for itself:

    192.168.1.3             rightpc.localdomain  rightpc         ## the HP server
    192.168.1.6             leftpc.localdomain      leftpc          ## the iMac client

\

### [Synergy.conf]

Here is a great start (a complete solution in my case) for a very smoothly running pair of machines (easily edited for more though), via one mouse & keyboard being connected to the synergys server - this **synergy.conf** is the server configuration file which does the job faultlessly for me:

    #synergy.conf

    section: screens
        leftpc:
            halfDuplexCapsLock = false
            halfDuplexNumLock = false
            halfDuplexScrollLock = false
            xtestIsXineramaUnaware = false
            switchCorners = none +top-left +top-right  +bottom-left +bottom-right
            switchCornerSize = 0
        rightpc:
            halfDuplexCapsLock = false
            halfDuplexNumLock = false
            halfDuplexScrollLock = false
            xtestIsXineramaUnaware = false
            switchCorners = none +top-left +top-right +bottom-left +bottom-right
            switchCornerSize = 0
    end

    section: aliases
    leftpc:
    192.168.1.6
    rightpc:
    192.168.1.3
    end

    section: links
        leftpc:
            right = rightpc
        rightpc:
            left = leftpc
    end

    section: options
        heartbeat = 1000
        relativeMouseMoves = false
        screenSaverSync = false
        win32KeepForeground = false
        switchCorners = none +top-left +top-right  +bottom-left +bottom-right
        switchCornerSize = 4
    end

\
This **synergyc.conf** file suits my uses perfectly, I found it on the Arch wiki, & it needed no functional modification. I put it in /home/handy as a \<.dot\> file i.e. \~/.synergy.conf .

\

## [][The Synergy Client(s):]

Install synergy

    sudo pacman -S synergy

\

### [][Client /etc/hosts:]

Edit the **/etc/hosts** file, mine is below for those that do need to reference, & if you do make sure you compare it with the server side one posted earlier on this page:

    192.168.1.6     leftpc.localdomain               leftpc          ## the iMac client
    192.168.1.3     rightpc.localdomain             rightpc         ## the HP server [/code]

\

### [][\~/.xinitrc]

Add the following to the **\~/.xinitrc** file (guess how I copied it?):

    synergyc -d ERROR rightpc

\

## [Conclusion:]

The server is where the hardest work is, beyond that it comes down to getting your auto-start sorted so that it just works no matter which machine(s) come on in what order. For me the above works in that regard perfectly once Openbox has loaded.