**[Wiki Help pages](https://wiki.gentoo.org/wiki/Help:Contents "Help:Contents")**\
[Contributor\'s guide](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide") --- [Fixing errors](https://wiki.gentoo.org/wiki/What_to_do_when_noticing_an_error_on_the_wiki "What to do when noticing an error on the wiki") --- [Guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines") --- [Blueprints](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Article_blueprints "Gentoo Wiki:Article blueprints")\
[Wiki FAQ](https://wiki.gentoo.org/wiki/Gentoo_Wiki:FAQ "Gentoo Wiki:FAQ") --- [About Gentoo wiki](https://wiki.gentoo.org/wiki/Gentoo_Wiki:About "Gentoo Wiki:About") --- [Wiki project page](https://wiki.gentoo.org/wiki/Project:Wiki "Project:Wiki")\
[Talk pages](https://wiki.gentoo.org/wiki/Help:Talk_pages "Help:Talk pages") --- [Contributing to Gentoo](https://wiki.gentoo.org/wiki/Contributing_to_Gentoo "Contributing to Gentoo") --- [Code of conduct](https://wiki.gentoo.org/wiki/Project:Council/Code_of_conduct "Project:Council/Code of conduct")\
[Help improve the documentation!](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation! "Help improve Gentoo by getting involved with documentation!")

\

[Editing pages](https://wiki.gentoo.org/wiki/Help:Editing_pages "Help:Editing pages") --- [Formatting](https://wiki.gentoo.org/wiki/Help:Formatting "Help:Formatting") --- [Translating articles](https://wiki.gentoo.org/wiki/Help:Translating "Help:Translating")\
[Links](https://wiki.gentoo.org/wiki/Help:Links "Help:Links") --- [Images](https://wiki.gentoo.org/wiki/Help:Images "Help:Images") --- [Categories](https://wiki.gentoo.org/wiki/Help:Categories "Help:Categories") --- [Templates](https://wiki.gentoo.org/wiki/Help:Templates "Help:Templates")\
[Moving (renaming) a page](https://wiki.gentoo.org/wiki/Help:Moving_a_page "Help:Moving a page") --- [Redirects] --- [Deleting a page](https://wiki.gentoo.org/wiki/Help:Deleting_a_page "Help:Deleting a page")\
[Starting a new page](https://wiki.gentoo.org/wiki/Help:Starting_a_new_page "Help:Starting a new page") --- *[more](https://wiki.gentoo.org/wiki/Help:Contents "Help:Contents")*

**Redirects** are used to *forward* users from one *page name* to another.

Redirection is useful if a particular article can be referred to by multiple names (e.g. [KVM](https://wiki.gentoo.org/wiki/KVM "KVM") →‎ [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU")), or has alternative punctuation (e.g. [X.org](https://wiki.gentoo.org/wiki/X.org "X.org") →‎ [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg")), capitalization (e.g. [Qemu](https://wiki.gentoo.org/wiki/Qemu "Qemu") →‎ [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU")) or spellings. Redirects are also used when [moving a page](https://wiki.gentoo.org/wiki/Help:Moving_a_page "Help:Moving a page").

## Contents

-   [[1] [Creating a redirect]](#Creating_a_redirect)
-   [[2] [Viewing and editing a redirect]](#Viewing_and_editing_a_redirect)
-   [[3] [Deleting a redirect]](#Deleting_a_redirect)
-   [[4] [Double redirects]](#Double_redirects)
-   [[5] [A redirect to a page in the \"category\" namespace]](#A_redirect_to_a_page_in_the_.22category.22_namespace)

## [Creating a redirect]

To start a new redirect, create a page with the name that should be redirected from (see [Help:Starting a new page](https://wiki.gentoo.org/wiki/Help:Starting_a_new_page "Help:Starting a new page")). It is also possible to use an existing page, that will then become inactive, by going to that page and using the \"edit\" tab at the top, and replacing the page contents with the redirect.

A redirect consists of the following code, at the very first text position of the *Edit window* for the page:

    #REDIRECT [[pagename]]

*pagename* is the name of the destination page. The word \"redirect\" is not case-sensitive, but there must be no space before the \"#\" symbol. Any text before the code will invalidate the redirect. Any text or regular content code after the redirect code will be ignored (and should be deleted from an existing page).

To put or keep the current page name listed in a Category, the usual tag for that category is entered (or kept) on a line after the redirect code entry.

Please use the \'preview\' button below the *Edit window* (or [Alt]+[P]) to check that the destination page name is correct, i.e. it leads to the intended page. The preview page will not look or act like the resulting redirect page, it will show a list, with the destination page in blue:

    <Name of "redirect page" as title>

    Redirect page

    ↳

If the *pagename* it is not a valid page, it will show in red. Until there is a valid destination page, the redirect should not be saved.

## [Viewing and editing a redirect]

After making a redirect for a page, the redirect page will no longer be accessible directly through its name (or by any link using that name). After following a redirect, a notice will be shown near the top of the destination page to indicate that a redirection has occurred. This notice includes an active link which will lead to the actual redirect page.

By accessing the actual redirect page through this link, the redirect may be edited just like any wiki page, like when the redirect was first created (see previous section). The history of the redirect page will be accessible, and the discussion page may be used to talk about the redirect itself with other editors.

Use this link if the redirect must be corrected, removed, or have an edit reverted.

** Tip**\
To resume: to view or modify a redirect page, first follow the redirect, then at the top of the destination page that will appear, use the link back to the actual redirect page.

## [Deleting a redirect]

There\'s generally no need to delete redirects. They do not occupy a significant amount of database space. If a page name is vaguely meaningful, there\'s no harm (and some benefit) in having it as a redirect to the more relevant or current page.

If a redirect must really be removed - e.g. if the page name is offensive, or to discourage people from referring to a concept by an erroneous or obsolete name - then go to the redirect page as mentioned above, and follow the procedures at [Help:Deleting a page](https://wiki.gentoo.org/wiki/Help:Deleting_a_page "Help:Deleting a page").

## [Double redirects]

A double redirect is a page redirecting to a page which is itself a redirect, and it will not work. Instead, people will be presented with a view of the next redirect page. This is a deliberate restriction, partly to prevent infinite loops, and partly to keep things simple and show up when a redirect is not pointing to an actual destination page.

Look out for double redirects, and eliminate them by changing them to be one-step redirects instead. This will often be needed after a significant [page move](https://wiki.gentoo.org/wiki/Help:Moving_a_page "Help:Moving a page"). Use the \"what links here\" toolbox link to find double redirects to a particular page, or use [Special:DoubleRedirects](https://wiki.gentoo.org/wiki/Special:DoubleRedirects "Special:DoubleRedirects") to find them throughout the whole wiki.

## [][A redirect to a page in the \"category\" namespace]

To prevent a page that redirects to a category from appearing in the category, precede the word \"Category\" with a colon:

    #REDIRECT [[:Category:Glossary]]