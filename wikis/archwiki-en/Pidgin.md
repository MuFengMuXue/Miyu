# Pidgin

Pidgin is a chat program which lets you log into accounts on multiple chat networks simultaneously. It is compatible with Jabber/XMPP, Bonjour, Gadu-Gadu, IRC, Novell GroupWise Messenger, Lotus Sametime, SILC, SIMPLE, and Zephyr, and many more chat networks with plugins.

## Installation
Install the  package. A notable variant is .

You may also want to install additional plugins from the  and .

## Spellcheck
The  package will be installed as a dependency, but to prevent all of your text from showing up as incorrect you will need to install an aspell dictionary. See the aspell article.

## Services
## AIM plugin
Pidgin no longer has out-of-the-box support for AOL Instant Messenger (AIM) as of version 2.14.3. However, there is a plugin available on GitHub that may be compiled and installed for use with unofficial AIM-based servers like AIM Phoenix.

## Windows Live Messenger/MSN Messenger plugin
Pidgin no longer has out-of-the-box support for Windows Live Messenger (WLM) as of version 2.12.0. However, there are multiple plugins available that may be compiled and installed for use with unofficial WLM-based servers like CrossTalk and Escargot. A few notable plugins are HIDEN's fork of msn-pecan and Animadoria's fork of msn-pecan.

## Discord plugin
Install the  package.

Then add a new account, select Discord as the protocol, enter your Discord login e-mail address and its password.

## IRC
This is a small tutorial for connecting to the Libera Chat network. It works for other IRC networks as long as you substitute the port numbers and other specific settings.

Go to Accounts > Manage Accounts > Add. Fill/select the following options:
 Protocol: IRC
 Username: your nick

Now go to Buddies > New instant message (or hit ), fill 'libera.chat' in the textbox and username@irc.libera.chat, then click 'Ok'. Type:

 /join #archlinux

The channel can be substituted with any other channel.

This final step will add your channel to 'Buddies': go to Buddies > Add chat, fill the correct channel in the textbox named channel (#archlinux).

## Sametime protocol
Install the  package. The 'Sametime' protocol will be available when creating an account.

## Slack plugin
Install the  package.

## Rocket.Chat plugin
Install the  package.

## Telegram plugin
Install the  or  package.

Enter your Telegram phone number when creating the account, after which you will receive an SMS text message with a confirmation code, which you will have to enter to authorize your Telegram protocol account on Pidgin.

## XMPP
Pidgin has out-of-the-box support for the XMPP/Jabber chat protocol. Some additional plugins exist for support of XMPP extensions such as OMEMO () or Message Carbons ().

## WhatsApp plugin
The  package provides support for WhatsAppWeb.

## Security
Pidgin uses Libpurple 2 which stores passwords unencrypted (in plaintext) in $HOME/.purple/account.xml, see You can store them in a keyring by using a plugin like:

*
*

## Privacy
Pidgin has some privacy rules set by default. Namely, the whole world cannot send you messages;
only your contacts or people selected from a list. Adjust this, and other settings in Tools > Privacy.

## Pidgin-OTR
This is a plugin that brings Off-The-Record (OTR) messaging to Pidgin. OTR is a cryptographic protocol that will encrypt your instant messages.

First you need to install . Once this has been done, OTR has been added to Pidgin.

# To enable OTR, start Pidgin and go to Tools > Plugins or press . Scroll down to the entry entitled "Off-The-Record Messaging". If the checkbox beside it is not checked, check it.
# Next, click on the plugin entry and select "Configure plugin" at the bottom. Select which account you wish to generate a key for, then click "Generate". You will have now generated a private key. If you are not sure what the other options do, leave them, the default options will work fine.
# The next step is to contact a buddy who also has OTR installed. In the chat window, a new icon should appear to the top right of your text input box. Click on it, and select "Start private conversation". This will start an 'Unverified' session. Unverified sessions are encrypted, but not verified - that is, you have started a private conversation with someone using your buddy's account who has OTR, but who might not be your buddy. The steps for verification of a buddy are beyond the scope of this section; however, they might be added in the future.

## Pidgin-Encryption
 transparently encrypts your instant messages with RSA encryption. Easy-to-use, but very secure.

You can enable it the same way as Pidgin-OTR.

Now you can open conversation window and new icon should appear beside menu. Press it to enable or disable encryption.
Also if you want to make encryption enabled by default right-click on a buddy's name (in your buddy list), and select Turn Auto-Encrypt On. Now, whenever a new conversation window for that buddy is opened, encryption will start out as enabled.

## Pidgin-GPG
Pidgin-GPG transparently encrypt conversations using GPG, and taking advantage of all the features of a pre-existing WoT.

The plugin is available on AUR as . It can be enabled the same way as the previously mentioned ones.

## Other packages
Arch has other Pidgin-related packages. Here are the most popular (for a thorough list, search the AUR):
* - Libnotify support, for theme-consistent notifications
* - A small latex plugin for pidgin. Put math between $$ and have it rendered (recepient also needs to have this installed)

## Auto logout on suspend
If you suspend your computer pidgin seems to stay connected for about 15 minutes. To prevent message loss, it is needed to set your status offline before suspending or hibernating. The status message will not be changed.

Therefore create a new systemd unit  in
Take the following snippet and replace myuser with your user.

 [Unit
 Description=Suspend Pidgin
 Before=sleep.target
 StopWhenUnneeded=yes

 Type=oneshot
 User=myuser
 RemainAfterExit=yes
 Environment=DISPLAY=:0
 ExecStart=-/usr/bin/purple-remote setstatus?status=offline
 ExecStop=-/usr/bin/purple-remote setstatus?status=available

 [Install
 WantedBy=sleep.target

## Minimize to tray
To make use of the Xfce system tray go to preferences and enable the system tray in the section "Interface".
You can now close the main window and run pidgin minimized. You will also be able to see message notifications in the tray.

## Backup
Save  to backup all message logs, accounts and other application data.

## Troubleshooting
## Version Match for Sametime
There was an issue if you would connect to the Sametime via Pidgin, it prompt "Version Match". A potential solution on the client side is to fake the version in accounts.xml. Insert/change the lines:

in the  section of Sametime account in accounts.xml which is located in $HOME/.purple/ folder.

## Browser error
If clicking a link within Pidgin creates an error message about trying to use 'sensible-browser' to open a link, try editing . Find the line referencing 'sensible-browser' and change it to this:

This example assumes you use Firefox.

As an alternative if the method above does not work you can set the desired browser in the pidgin preferences in the section "Browser".
