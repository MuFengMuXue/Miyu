**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Fingerprint_recognition "wikipedia:Fingerprint recognition")

[[]]This article has some todo items:\

-   how to enroll a fingerprint for a specific user
-   GNOME/KDE integration and development status of this features
-   Configure PAM to use fprintd

the three things above should be finished but they may need to be checked and expanded upon

Some laptops (especially those of the [ThinkPad](https://en.wikipedia.org/wiki/ThinkPad "wikipedia:ThinkPad") persuasion) come with an integrated fingerprint reader which can be used for authentication.

** Warning**\
Many guides expect the fingerprint reader to be used in the place of a password. It is highly imperative to note: fingerprint reader technology is *not* considered to be secure by security experts.^[\[1\]](#cite_note-1)^ Fingerprints should ***not*** be substituted for passwords for any device. Passwords can be easily changed; fingers cannot.^[\[2\]](#cite_note-2)^ There are many known techniques to extract fingerprints from the device casing in order to gain access to the system through the fingerprint reader.

With the warning being understood, it is perfectly acceptable to use a fingerprint to identify the user account before signing with key-based or another form of authentication.

## Contents

-   [[1] [Available software]](#Available_software)
-   [[2] [Enrolling a fingerprint]](#Enrolling_a_fingerprint)
-   [[3] [Graphical Integration]](#Graphical_Integration)
-   [[4] [Configuring fprintd for use with PAM]](#Configuring_fprintd_for_use_with_PAM)
-   [[5] [References]](#References)

## [Available software]

** Note**\
The [fprint project](https://www.freedesktop.org/wiki/Software/fprint) is probably the most advanced approach to provide a solution for integrating fingerprint readers in Linux - other solutions such as [thinkfinger](http://thinkfinger.sourceforge.net/download.php) are mostly outdated and do not provide such a general approach as well as [fprint].

  ------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name          Package                                                                                                                                                                                                                                                                                                                                                                              Homepage                                                                                                                             Description
  fprint        [[[sys-auth/fprintd]](https://packages.gentoo.org/packages/sys-auth/fprintd)[]]               [https://cgit.freedesktop.org/libfprint/fprintd/](https://cgit.freedesktop.org/libfprint/fprintd/)   [fprint] consists of several components. The primary being a daemon which provides access to [fprint] functionality through [D-Bus](https://wiki.gentoo.org/wiki/D-Bus "D-Bus") to applications, such as login managers (GDM, KDM, \...), screen locking mechanisms etc.
  thinkfinger   [[[sys-auth/thinkfinger]](https://packages.gentoo.org/packages/sys-auth/thinkfinger)[]]   [http://thinkfinger.sourceforge.net/](http://thinkfinger.sourceforge.net/)                           Support for the UPEK/SGS Thomson Microelectronics fingerprint reader, often seen in ThinkPad laptops.
  ------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [Enrolling a fingerprint]

Enroll a fingerprint as a user:

`user `[`$`]`fprintd-enroll`

To enroll a fingerprint to a specific user^[\[3\]](#cite_note-3)^, use the [fprintd-enroll] utility:

`root `[`#`]`fprintd-enroll <user>`

To enroll a certain finger:

`root `[`#`]`fprintd-enroll -f right-index-finger <user>`

To test if the finger is enrolled, use the [fprintd-verify] command:

`user `[`$`]`fprintd-verify -f right-index-finger`

## [Graphical Integration]

[] This section has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

KDE supports the adding/removing of fingerprints via their system settings app under the users tab by clicking configure fingerprint authentication.^[\[4\]](#cite_note-4)^

As for the enabling of it for graphical authentication, the system is able to login, wake up from sleep, and sudo in the terminal, however, it is unknown at this time whether you can replace the authentication popups.

## [Configuring fprintd for use with PAM]

[PAM](https://wiki.gentoo.org/wiki/PAM "PAM") is the authentication service used by Linux. To use a fingerprint reader with PAM, insert the following command in to the configuration file to make eligible for fingerprint.

[FILE] **`/etc/pam.d/(pam.d service)`**

    auth            sufficient      pam_fprintd.so

## [References]

1.  [[[↑](#cite_ref-1)] [[https://www.schneier.com/blog/archives/2013/09/iphone_fingerpr.html](https://www.schneier.com/blog/archives/2013/09/iphone_fingerpr.html)]]
2.  [[[↑](#cite_ref-2)] [[https://www.vice.com/en/article/stealing-fingerprints/](https://www.vice.com/en/article/stealing-fingerprints/)]]
3.  [[[↑](#cite_ref-3)] [[https://www.makeuseof.com/set-up-fingerprint-scanner-with-pam-on-linux/](https://www.makeuseof.com/set-up-fingerprint-scanner-with-pam-on-linux/)]]
4.  [[[↑](#cite_ref-4)] [[https://9to5linux.com/kde-plasma-5-24-desktop-environment-to-introduce-support-for-fingerprint-readers](https://9to5linux.com/kde-plasma-5-24-desktop-environment-to-introduce-support-for-fingerprint-readers)]]