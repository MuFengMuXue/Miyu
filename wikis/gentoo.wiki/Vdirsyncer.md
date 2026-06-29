[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Vdirsyncer&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Vdirsyncer "Project:Vdirsyncer")][Project](https://wiki.gentoo.org/index.php?title=Project:Vdirsyncer&action=edit&redlink=1 "Project:Vdirsyncer (page does not exist)")

[[]][Home](https://vdirsyncer.pimutils.org/en/stable/)

[[]][Package information](https://packages.gentoo.org/packages/dev-python/vdirsyncer)

[[]][GitHub](https://github.com/pimutils/vdirsyncer)

**vdirsyncer** is a command-line tool for synchronizing calendars and address books between a variety of servers and the local filesystem.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Additional software]](#Additional_software)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Caveats]](#Caveats)
-   [[5] [Tips]](#Tips)
-   [[6] [Troubleshooting]](#Troubleshooting)
    -   [[6.1] [Google calendars and contacts]](#Google_calendars_and_contacts)
    -   [[6.2] [Unmerge]](#Unmerge)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)
-   [[9] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [dev-python/vdirsyncer](https://packages.gentoo.org/packages/dev-python/vdirsyncer) [[]] [Synchronize calendars and contacts]

  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`test`](https://packages.gentoo.org/useflags/test)   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-04 18:25] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask dev-python/vdirsyncer`

### [Additional software]

## [Configuration]

### [Files]

-   [\~/.config/vdirsyncer/config] - Local (per user) configuration file.

## [Usage]

### [Invocation]

`user `[`$`]`vdirsyncer --help`

[\ ]

(Paste command help output here.)

\</pre\>

## [Caveats]

## [Tips]

## [Troubleshooting]

### [Google calendars and contacts]

vdirsyncer supports synchronization with Google calendars, but requires some additional steps to get working.

You need to register vdirsyncer as an application yourself to obtain client_id and client_secret. It is against Google's Terms of Service to hardcode those into open source software. The steps are as follows:

-   Go to the [Google API manager](https://console.cloud.google.com/apis/dashboard).
-   Login in as yourself.
-   Create a new project with any name (e.g. vdirsyncer). You do this via the toolbar at top of page.
-   Click on \"Enable APIs and Services\".

<!-- -->

-   Enter CalDAV (for calendars) in the search box (repeat all follow steps for CardDAV if you wish to sync contacts as well) .
-   Click on CalDAV API, enable the API.
-   Maybe you need to Click Manage (depends if you are returning), a menu tree/sidebar should appear on left.

<!-- -->

-   Select Oauth Consent screen.
-   Fill out the Consent screen however you like.
-   There are 3 screens to fill out, on the last it\'s a good idea to add yourself as a test user. If you don\'t the authorisation may fail.

<!-- -->

-   Next select Credentials in the sidebar.
-   Click add Credentials.
-   Select OAuth Client ID.
-   Select Web application.
-   Under \"Authorised redirect URIs\" add [http://127.0.0.1:8088](http://127.0.0.1:8088)
-   Press \"Create\".
-   Note down the client id and client secret.

<!-- -->

-   In your vdirsyncer config file; paste in the client ID and secret.

[FILE] **`~/.config/vdirsyncer/config`**

    ...
    [storage example_for_google_calendar]
    type = "google_calendar"
    client_id = "..."
    client_secret = "..."
    ...

\

-   Now you need to edit the port number used in the google.py file found at /usr/lib/python3.10/site-packages/vdirsyncer/storage. The redirect URL needs to use port 8088.

<!-- -->

-   Find the three lines

[FILE] **`/usr/lib/python3.10/site-packages/vdirsyncer/storage/google.py`**

    ...
    local_server = wsgiref.simple_server.make_server(
        host, 0, wsgi_app, handler_class=_WSGIRequestHandler
    )
    ...

-   Change \'0\' to \'8088\'.
-   Next run vdirsyncer discover (assuming you have a fully formed config file as per vdirsyncer documenation).

`user `[`$`]`vdirsyncer discover `

-   This should open a link in your browser to authorise vdirsyncer.
-   Proceed with Google authentication until fully complete and you can go no further.

<!-- -->

-   Switch back to command line where vdirsyncer was waiting, it should now have moved on to the next step in the discovery process.

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose dev-python/vdirsyncer`

## [See also]

-   [Article_name](https://wiki.gentoo.org/index.php?title=Article_name&action=edit&redlink=1 "Article name (page does not exist)")

## [External resources]

-   [Descriptive link name](https://_external_website_) --

## [References]