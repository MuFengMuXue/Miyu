[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Warning_about_insecure_obsolete_network_hardware&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

** Important**\
This article is a work in progress and is still incomplete, these are not the only known systems to avoid.

Most network hardware requires regular updates to patch security issues, just as operating systems do. Sadly, some network hardware is under-supported by manufacturers, or supported for a limited amount of time. If such outdated network hardware is used without appropriate updates, security issues arise.

Because hardware often sees continued use even without the required security updates, users should be aware of potential security issues, and be mindful of using potentially obsolete and insecure network hardware.

Over the years, whole security protocols have been found to be insecure and have been deprecated, however these insecure implementations can sometimes remain in operation on old hardware. Users should be aware of what to avoid.

## Contents

-   [[1] [Insecure protocols]](#Insecure_protocols)
    -   [[1.1] [WEP]](#WEP)
    -   [[1.2] [TKIP (WPA or \"WPA+WPA2\")]](#TKIP_.28WPA_or_.22WPA.2BWPA2.22.29)
        -   [[1.2.1] [Insecure workaround]](#Insecure_workaround)
-   [[2] [Updated open firmware]](#Updated_open_firmware)
-   [[3] [See also]](#See_also)

## [Insecure protocols]

### [WEP]

A major design flaw was discovered in WEP in 2001, it should no longer be used. Devices from this era often do not have updates available, and sadly have to be be discarded.

[[[net-wireless/wpa_supplicant]](https://packages.gentoo.org/packages/net-wireless/wpa_supplicant)[]] has a [[[wep]](https://packages.gentoo.org/useflags/wep)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] flag, though this should be avoided if possible.

### [][TKIP (WPA or \"WPA+WPA2\")]

WPA was a temporary measure to avoid WEP\'s security issues, flaws have since been discovered in WPA (TKIP), and it was deprecated in 2012.

Routers should deactivate the insecure \"TKIP\" or \"WPA/WPA2 mixed mode\" methods, and prefer for example \"WPA2-AES\" or \"WPA3\". Devices which do not allow this, and only support the insecure method, should be replaced, if they cannot be updated.

#### [Insecure workaround]

** Warning**\
Using insecure network infrastructure is high risk. Only attempt to do so if fully cognizant of the risks, for activities that do not require security, such as testing.\
\
**It is important to understand these USE flags are disabled because of how insecure they are!** An overview as to why the following instructions should only be followed when there is no possible way to access the router and change to something that will keep the system and network safe, is available [here](https://engineerfix.com/why-tkip-is-no-longer-a-secure-wi-fi-protocol/).

Those using [wpa_supplicant](https://wiki.gentoo.org/wiki/Wpa_supplicant "Wpa supplicant") can activate the following use flags, if they are fully aware of the risks outlined in the rest of this article:

[FILE] **`/etc/portage/package.use/wpa_supplicant`**

    net-wireless/wpa_supplicant tkip

Re-emerge wpa_supplicant:

`root `[`#`]`emerge --ask net-wireless/wpa_supplicant`

Portage keeps source tarballs for all currently installed packages in [/var/cache/distfiles], which will include wpa_suppilcant. Thus these flags can be enabled even without a working network connection, and there should be no need to use live media to fix this from a chroot, on a correctly maintained system.

See the previous section for information about the [[[wep]](https://packages.gentoo.org/useflags/wep)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] flag, though this should be avoided if possible.

## [Updated open firmware]

If the manufacturer does not provide updated, secure firmware, for some devices, alternative firmware such as [OpenWrt](https://openwrt.org/) or [OPNsense](https://opnsense.org) may be available. Be aware that installing these solutions can be technically demanding (sometimes extremely so for some devices).

## [See also]

-   [Wi-Fi](https://wiki.gentoo.org/wiki/Wi-Fi "Wi-Fi") --- describes the setup of a [Wi-Fi](https://en.wikipedia.org/wiki/Wi-Fi "wikipedia:Wi-Fi") (wireless) network device.
-   [wpa_supplicant](https://wiki.gentoo.org/wiki/Wpa_supplicant "Wpa supplicant") --- an app for [Wi-Fi](https://wiki.gentoo.org/wiki/Wi-Fi "Wi-Fi") authentication