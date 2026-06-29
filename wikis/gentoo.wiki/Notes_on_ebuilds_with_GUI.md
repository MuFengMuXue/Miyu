When this wiki page was started (2017-11-13), there was a lot confusion about how to write clean ebuilds for desktop applications. As result, there are many ebuilds which use obsolete eclasses, or even worse do not install, update, or remove the icons and menus. The [eclasses](https://wiki.gentoo.org/wiki/Eclass "Eclass") are hardly documented and the documentation has mistakes. Many for loops for icons miss the definition of the local variable.

** Note**\
This page is still **work in progress**. It would be nice, if we could extract a howto wiki page from it afterwards and improve the documentation of the eclasses.

## Contents

-   [[1] [Eclasses]](#Eclasses)
    -   [[1.1] [xdg.eclass]](#xdg.eclass)
    -   [[1.2] [xdg-utils.eclass]](#xdg-utils.eclass)
    -   [[1.3] [gnome2.eclass]](#gnome2.eclass)
    -   [[1.4] [gnome2-utils.eclass]](#gnome2-utils.eclass)
-   [[2] [What repoman QA can detect]](#What_repoman_QA_can_detect)
-   [[3] [Code examples to create icons]](#Code_examples_to_create_icons)
-   [[4] [.desktop files]](#.desktop_files)
-   [[5] [brainstorming section (delete later, when merged in the text)]](#brainstorming_section_.28delete_later.2C_when_merged_in_the_text.29)
    -   [[5.1] [Working principle of a trigger in bash]](#Working_principle_of_a_trigger_in_bash)
-   [[6] [See also]](#See_also)

## [Eclasses]

### [xdg.eclass]

eclass reference: [[xdg.eclass](https://devmanual.gentoo.org/eclass-reference/xdg.eclass)]

-   xdg inherits xdg-utils

### [xdg-utils.eclass]

eclass reference: [[xdg-utils.eclass](https://devmanual.gentoo.org/eclass-reference/xdg-utils.eclass)]

### [gnome2.eclass]

eclass reference: [[gnome2.eclass](https://devmanual.gentoo.org/eclass-reference/gnome2.eclass)]

### [gnome2-utils.eclass]

eclass reference: [[gnome2-utils.eclass](https://devmanual.gentoo.org/eclass-reference/gnome2-utils.eclass)]

## [What repoman QA can detect]

[CODE]

    * QA Notice: .desktop files with MimeType= were found installed
     * but desktop mimeinfo cache has not been updated:
     *   /usr/share/applications/SciTE.desktop
     * Please make sure to call xdg_desktop_database_update()
     * in pkg_postinst() and pkg_postrm() phases of appropriate pkgs.

## [Code examples to create icons]

[CODE]

    src_install()  utilities/$$.png $.png
        done
    }

## [.desktop files]

-   [.desktop_files](https://wiki.gentoo.org/wiki/.desktop_files ".desktop files")

## [][brainstorming section (delete later, when merged in the text)]

This page provides a summary of various files whose installation should be accompanied by appropriate postinst/postrm trigger calls.

  ----------------------------------------------------- --------------------------- ------------------------------ ------- ------------------------------- -------------------------------
  Path                                                  Conditions                  preinst                        prerm   postrm                          postinst
  xdg-utils.eclass (or automatic in xdg.eclass)
  /usr/share/applications                               if MimeType= is specified   \-                             \-      xdg_desktop_database_update     xdg_desktop_database_update
  /usr/share/mime                                                                   \-                             \-      xdg_mimeinfo_database_update    xdg_mimeinfo_database_update
  /usr/share/icons                                                                  \-                             \-      xdg_icon_cache_update           xdg_icon_cache_update
  gnome2-utils.eclass (or automatic in gnome2.eclass)
  /etc/gconf/schemas/                                                               gnome2_gconf_savelist          \-      \-                              gnome2_gconf_install
  /usr/share/glib-2.0/schemas                                                       gnome2_schemas_savelist        \-      gnome2_schemas_update           gnome2_schemas_update
  /usr/share/omf                                                                    gnome2_scrollkeeper_savelist   \-      gnome2_scrollkeeper_update      gnome2_scrollkeeper_update
  /usr/lib\*/gdk-pixbuf-2.0                                                         gnome2_gdk_pixbuf_savelist     \-      \-                              gnome2_gdk_pixbuf_update
  /usr/lib\*/gio/modules                                                            \-                             \-      gnome2_giomodule_cache_update   gnome2_giomodule_cache_update
  ----------------------------------------------------- --------------------------- ------------------------------ ------- ------------------------------- -------------------------------

-   \*1) Not needed in general, but still useful to use in phase defining eclasses, like gnome2.eclass.

<!-- -->

-   Needs to be updated since some savelists are not needed
-   what about fonts?

### [Working principle of a trigger in bash]

[CODE]

    while read type file; do
        case "$" in
            /usr/share/ca-certificates/*.crt)
                update-ca-certificates
                break
            ;;
        esac
    done < "$/files"

\

-   portage generates the QA warnings here: [https://github.com/gentoo/portage/tree/master/bin/postinst-qa-check.d](https://github.com/gentoo/portage/tree/master/bin/postinst-qa-check.d)

## [See also]

-   [Future_EAPI/Triggers](https://wiki.gentoo.org/wiki/Future_EAPI/Triggers "Future EAPI/Triggers")