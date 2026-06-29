Other languages:

[English] • ‎[русский](//wiki.manjaro.org/index.php?title=Manjaro_IRC/ru "Manjaro IRC (100% translated)")

## Contents

-   [[1] [What is IRC?]](#What_is_IRC.3F)
-   [[2] [How do I use Manjaro IRC?]](#How_do_I_use_Manjaro_IRC.3F)
-   [[3] [Asking questions on IRC]](#Asking_questions_on_IRC)
    -   [[3.1] [How to Register a User Name]](#How_to_Register_a_User_Name)
    -   [[3.2] [Secure your nick name]](#Secure_your_nick_name)
    -   [[3.3] [Trolling]](#Trolling)
-   [[4] [Configuring an IRC client]](#Configuring_an_IRC_client)
-   [[5] [Manjaro IRC is multilingual]](#Manjaro_IRC_is_multilingual)
-   [[6] [Logging]](#Logging)
-   [[7] [See also]](#See_also)

# [][What is IRC?]

**#manjaro IRC** is a place to provide additional direct support to Manjaro users.

You can connect to the **#manjaro** channel on **irc.libera.chat**.

-   Frequent users will probably prefer an *IRC client* like *Weechat*, *Hexchat*, or *Konversation*
-   One-time users will probably prefer a web-based chat, such as [https://web.libera.chat/#manjaro](https://web.libera.chat/#manjaro)

It\'s not a replacement for the forum, but supplements it with direct community support. Sometimes it is quiet and sometimes busy, but we will try to help.

Also, sometimes the reason it is busy is that the conversation has gone off-topic!

For further issues that can\'t be solved on IRC there is always the Forum.\

# [][How do I use Manjaro IRC?]

Connect to #manjaro on irc.libera.chat using one of methods noted above.

When you are logged in, into the standard IRC client you have an name like Manjarouser. The #manjaro channel now requires you to use a [registered user name](#How_to_Register_a_User_Name). If you do not, you will be re-directed to #manjaro-unregistered.

You can change temporarily your nick with:

    /nick [your nickname]

For example, to set your nick as \"John\", you would enter the following:

    /nick John

The only rule of the IRC Channel is to be friendly. Just be your friendly self, and you\'ll find a lot of other friendly people to socialize with and receive support from.

# [Asking questions on IRC]

1.  Ask the question. You don\'t need to ask for permission to ask, or to find out if anyone is willing to answer the question.
2.  Make sure you have time to wait for an answer (10 minutes is a bare minimum). If you don\'t get an answer, it\'s likely people don\'t know, are in the middle of writing one or didn\'t notice your question.
3.  Try to be concise with your question.
4.  Even if you see a lot of people listed on the channel, this doesn\'t mean that they are actually present.
5.  When sending reports (especially multi-line reports) please use an Pastebin service like pastebin.com\

\

## [How to Register a User Name]

0\. **Choose a user name or nick**.

The user name should consist only of the letters from A-Z, the numbers from 0-9 and certain symbols such as \"\_\" and \"-\". It may have a maximum of 16 characters. To do so, enter the following command into the text field, where you would normally enter comments:

    /nick [your nickname]

1\. **Register your nick / user name**.

Type the following command and replace \"your_password\" with a password that will be easy to remember, and replace \"your_email_address\" with your email address.

    /msg nickserv register your_password your_email_address

2\. **Check your e-mail and verify your account**.

After you register, you will not be able to identify to NickServ until you have verified your registration. To do this, check your email for an account verification code.

3\. **Type the command that Libera.Chat asks you to type**.

Press the Enter key to fully confirm.

## [Secure your nick name]

Its possible someone using your nick.

please set :

     /msg NickServ SET ENFORCE ON

Then no one can abuse your nick directly Make sure your client got configure right

you can always do manually with :

     /msg NickServ IDENTIFY account password

For further info see [Libera.Chat user registration](https://libera.chat/guides/registration)

## [Trolling]

IRC is a well-known chat protocol frequently used by trolls, if you encounter a troll please notify a moderator. In case the troll is sending you private messages, you can set +Rg on your nick, so only registered users can chat with you privately. If you wish to set this mode, it can be done with:

       /mode (yournick) +Rg

stops messages from troll that is unregistered. so, no users that is unregistered can harm you.

If the troll is registered, you can ignore the troll with the command:

do also : */ns info (troll-nick)* to get information over the registered name.

     /ignore (troll-nick-registered name)

# [Configuring an IRC client]

With pidgin hexchat and konversation you can a good go to irc.

Please see the following on how to configure for your client for Sasl: [\[1\]](https://libera.chat/guides/sasl)

\

# [Manjaro IRC is multilingual]

It is always a good idea to look for IRC channels in your region too.

-   #manjaro = Main IRC Channel
-   #manjaro-br = Brasil IRC Channel
-   #manjaro-de = German IRC Channel
-   #manjaro-es = Spanish IRC Channel
-   #manjaro-fi = Finnish IRC Channel
-   #manjaro-fr = French IRC Channel
-   #manjaro-it = Italian IRC Channel
-   #manjaro-jp = Japanese IRC Channel
-   #manjaro-nl = Dutch / Belgian IRC channel
-   #manjaro-ru = Russian IRC Channel
-   #linuxpark = Turkish IRC Channel
-   #manjaro-talk = Manjaro off-topic channel, is optional in use.
-   #manjaro-openrc = OpenRC support Manjaro
-   ##manjaro-ops = channel admin is there and leave a message about issues on channel

Please support those channels !\

# [Logging]

If there is some issues and you could catch a operator. There is some logging you can find some logs back !

check this :

-   Link removed.

# [See also]

[IRC Support Guidelines](//wiki.manjaro.org/index.php?title=Manjaro-irc-support-guidelines&action=edit&redlink=1 "Manjaro-irc-support-guidelines (page does not exist)")