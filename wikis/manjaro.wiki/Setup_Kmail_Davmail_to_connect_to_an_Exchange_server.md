Other languages:

[English] • ‎[русский](//wiki.manjaro.org/index.php?title=Setup_Kmail_%26_Davmail_to_connect_to_an_Exchange_server/ru "Настройка Kmail и Davmail для подключения к серверу Exchange (100% translated)")

## Contents

-   [[1] [Preamble]](#Preamble)
-   [[2] [Davmail]](#Davmail)
    -   [[2.1] [Main Tab]](#Main_Tab)
    -   [[2.2] [Advanced Tab]](#Advanced_Tab)
-   [[3] [Kmail]](#Kmail)
    -   [[3.1] [General TAB]](#General_TAB)
    -   [[3.2] [Advanced TAB]](#Advanced_TAB_2)
        -   [[3.2.1] [Add your company\'s e-mail account in Kmail]](#Add_your_company.27s_e-mail_account_in_Kmail)
        -   [[3.2.2] [General TAB]](#General_TAB_2)
        -   [[3.2.3] [Advanced TAB]](#Advanced_TAB_3)
    -   [[3.3] [Now we handle the Sending mail]](#Now_we_handle_the_Sending_mail)
        -   [[3.3.1] [General Tab]](#General_Tab_3)
        -   [[3.3.2] [Advanced TAB]](#Advanced_TAB_4)
-   [[4] [Summation]](#Summation)
-   [[5] [Support]](#Support)

# [Preamble]

It is best to start by asking your company's IT-manager for details cause they can and will be different from mine.

    Note: The contents of any angle brackets (including the angle brackets
    themselves) must be replaced with your appropriate details.

In Davmail you need to change just a few settings, all but one on the Main TAB of the settings window.

# [Davmail]

## [Main Tab]

**Exchange Protocol**: I needed to set it to EWS but that can be different for you, so ask your IT-manager.

**OWA or EWS (Exchange) URL**: http(s)://\<mail.company URL\>/owa

**Port numbers**: are setup the way they should be so don't change those. As you can see they are the normal port numbers for the different services added with 1000: POP is normally 110, now it is 1110, etc.

**Delays**: no need to change those cause the default settings work just fine

## [Advanced Tab]

**SMTP save in sent**: UNCHECK

If it is checked Davmail stores a copy of your sent mail in your sent mail folder, just as your mail program does. You end up with 2 copies of every sent mail. Just uncheck this item. That's all for Davmail.

\

# [Kmail]

For Kmail you need to setup an Identity and an e-mail account. The new identity gets only a few filled out details.

## [General TAB]

I filled out my name and my e-mail address.

## [Advanced TAB]

On the **Advanced TAB** I chose the **Sent** and **Drafts** folders on the company's server so I can also reach them when I am at the company. The default domain is your company's domain, the IT manager knows it if you are unsure.

All other TABs are left as is.

### [][Add your company\'s e-mail account in Kmail]

First we look at the Receiving mail

### [General TAB]

**General TAB**: you fill out a name for the account. This can be anything but I chose the name of the company so I can easily see which account it is.

**IMAP server**: localhost   Davmail is your server and it is local so your server address is localhost.

**Username**: \<company-domain name\>\\\<login name\> does it for me. Ask IT for details.

**Password**: is your normal password for this mail account.

### [Advanced TAB]

Choose the new identity as the one you use for this account.

**Connection Settings**:

I had to choose

**Encryption**: None

**Port**: 1993 for IMAP and

**Authentication**: *Clear text* but these are details which can and probably will be different for your situation so ask IT.

\

## [Now we handle the Sending mail]

### [General Tab]

**Outgoing mail server**: localhost

**Server requires authentication**: on

**Login**: \<company-domain name\>\\\<login name\>

**Password**: \*\*\*\*\*\*\*\*

If you like you can check the Store SMTP password checkbox.

### [Advanced TAB]

**Encryption**: None **Port**: 1025 for SMTP **Authentication**: LOGIN

# [Summation]

And that's it. This works for me but as said several times before: it can and will be different for your company so ask for the details.

# [Support]

Following is a link to this page\'s forum counterpart where you can post any related feedback: [\[1\]](https://forum.manjaro.org/t/wiki-setup-kmail-davmail-to-connect-to-an-exchange-server/19644)\