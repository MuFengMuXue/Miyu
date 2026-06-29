This guide explains how to submit ebuilds for inclusion in the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository").

## Contents

-   [[1] [Submitting an ebuild]](#Submitting_an_ebuild)
    -   [[1.1] [Pull requests]](#Pull_requests)
    -   [[1.2] [Do not submit CPAN ebuilds]](#Do_not_submit_CPAN_ebuilds)
-   [[2] [Alternate Submission Methods]](#Alternate_Submission_Methods)
    -   [[2.1] [Bugzilla]](#Bugzilla)
        -   [[2.1.1] [Create a Bugzilla account]](#Create_a_Bugzilla_account)
        -   [[2.1.2] [Create a new bug]](#Create_a_new_bug)
        -   [[2.1.3] [Completing the bug form]](#Completing_the_bug_form)
        -   [[2.1.4] [Attaching the ebuild script]](#Attaching_the_ebuild_script)
        -   [[2.1.5] [Multiple ebuilds]](#Multiple_ebuilds)
            -   [[2.1.5.1] [Dependencies]](#Dependencies)
    -   [[2.2] [Mailing list patches]](#Mailing_list_patches)
    -   [[2.3] [GURU Overlay]](#GURU_Overlay)
-   [[3] [See also]](#See_also)

## [Submitting an ebuild]

The review for new packages can take a while because of the need to test the ebuild and go through upstream files and issues.

### [Pull requests]

The preferred way of submitting ebuilds is via Pull Requests on the [Gentoo Mirror on GitHub](https://github.com/gentoo/gentoo/pulls). From there they can be picked up by [package maintainers](https://wiki.gentoo.org/wiki/Package_maintainer%27s_responsibilities "Package maintainer's responsibilities") and merged into the main repository.

** See also**\
[GitHub Pull Requests](https://wiki.gentoo.org/wiki/GitHub_Pull_Requests "GitHub Pull Requests").

### [Do not submit CPAN ebuilds]

The [[[app-portage/g-cpan]](https://packages.gentoo.org/packages/app-portage/g-cpan)[]] package provides a tool called [g-cpan.pl] which installs a given CPAN module on your Gentoo system using Portage, storing the necessary information (such as dependencies, provided files, etc.) in the Portage database, just like it would when you install an ebuild. It is therefore not needed (nor recommended) to submit CPAN ebuilds.

For more information on [g-cpan.pl], please consult its man page: [man g-cpan.pl]

## [Alternate Submission Methods]

### [Bugzilla]

#### [Create a Bugzilla account]

Point your web browser to [https://bugs.gentoo.org/](https://bugs.gentoo.org/). This is the URL for the Bugzilla bug tracking database. In the list of links, one of the items reads \"Open a new Bugzilla account\". If you have not done so already (e.g. for submitting a bug), click on this link and create a new account.

#### [Create a new bug]

At the bottom of the main page or login page, there is a yellow box. Choose the [New - Expert] link. Or, you can just go to the URL [https://bugs.gentoo.org/enter_bug.cgi](https://bugs.gentoo.org/enter_bug.cgi). Either will bring you to the `Enter Bug` page.

** Note**\
In the Bugzilla system, all entries are bugs. That includes newly submitted ebuilds. Each bug is assigned a tracking id. Take note of the ID, especially if you have other ebuilds that depend on this package.

Bugzilla can track multiple products. For example, in Gentoo, other products may include documentation or tools used to administrate the website. From the list of products, Ebuilds should always be submitted to [Gentoo Linux].

Clicking on the [Gentoo Linux] product should bring up a new bug entry form.

#### [Completing the bug form]

The first field on the form is `version`. If you know which version the package belongs in, set it here. Otherwise, select `unspecified`. Next, set the component. All ebuild scripts are of the component type `New packages` or `Current packages`.

** Important**\
Ebuilds should *always* be of component type `New packages` or `Current packages`. Categories such as `GNOME`, `Libraries`, and `Server` may look like they apply to your ebuild, but they are used for filing bugs against packages, not submitting ebuilds.

The categories `Platform`, `OS`, and `Priority` do not need to be set for ebuilds.

The `Severity` field should be set to `enhancement`.

Leave the `Assigned To` field blank. If you haven\'t changed Bugzilla\'s mail settings, you, as a reporter, will automatically receive email on bug updates.

Fill in the `Summary` field with a brief note of what package you are submitting and whether it\'s an update or a new submission. Something like the following is great: `foo-bar-x.y.z.ebuild (New Package)` or `foo-x.y.z.ebuild (Update)`.

The `Description` field should be filled in as completely as possible. Here\'s an example from [bug #7](https://bugs.gentoo.org/show_bug.cgi?id=7):

    Hi!

    Please find attached gramps-4.2.0.ebuild and a patch so that it will
    compile against python-3.2

    Gramps is the Genealogical Research and Analysis Management Programming
    System.  It is a very cool gnome/python app.  If you are in the US, you
    can head over to http://www.familysearch.com/ and you can probably find a
    GEDCOM file for your family tree to import into Gramps. (Mormons sure do like
    genealogy)

    I suggest app-misc/gramps Also, this ebuild depend on Imaging and Graphviz
    previously submitted

    tod

Once the summary is complete, click `Commit`.

#### [Attaching the ebuild script]

After clicking `submit` on the [Enter Bug] page, you will go to the `Posting Bug` page. Take note of the bug number.

Toward the bottom of this page, there is a link to [Create a new attachment]. Click on this link.

Select the file using the text entry box or the `Browse` dialog. In the `Description` field, type the name of the ebuild file, much the same as you did in the `Summary` section of the last page.

Make sure that the content type is set to `text/plain`, and that the radio button for `select from list` is marked.

There are no other required fields on this form. Click `Submit` and you are done!

#### [Multiple ebuilds]

##### [Dependencies]

In cases where you might submit multiple ebuilds, and some of them depend on others, it is very helpful if these dependencies are noted. Viewing the bug again should allow you to enter another note. Please add dependency information here.

### [Mailing list patches]

See [Project:Proxy_Maintainers/User_Guide#Mailing_list_patches](https://wiki.gentoo.org/wiki/Project:Proxy_Maintainers/User_Guide#Mailing_list_patches "Project:Proxy Maintainers/User Guide")

### [GURU Overlay]

[GURU](https://wiki.gentoo.org/wiki/Project:GURU "Project:GURU") is an official Gentoo overlay that is maintained by Gentoo users. Ebuilds submitted here have a less stringent review process.

## [See also]

-   [Basic guide to write Gentoo Ebuilds](https://wiki.gentoo.org/wiki/Basic_guide_to_write_Gentoo_Ebuilds "Basic guide to write Gentoo Ebuilds") --- getting started writing **[ebuilds](https://wiki.gentoo.org/wiki/Ebuild "Ebuild")**, to harness the power of [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), to install and manage even more software.
-   [Ebuild](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") --- a text file, usually stored in a [repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository"), which identifies a specific software package and tells the Gentoo package manager how to handle it.
-   [Github Pull Requests](https://wiki.gentoo.org/wiki/Github_Pull_Requests "Github Pull Requests") --- how to contribute to Gentoo by creating [pull requests on GitHub](https://github.com/gentoo/gentoo/pulls).
-   [Project:GURU](https://wiki.gentoo.org/wiki/Project:GURU "Project:GURU") --- an official repository of new Gentoo packages that are maintained collaboratively by Gentoo users

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Matt Butcher**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*