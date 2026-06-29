GNOME Configure the applications folders. **Applications folders** are the GNOME the containers for applications.

## Contents

-   [[1] [Introduction]](#Introduction)
    -   [[1.1] [Gsettings and desktop schemas]](#Gsettings_and_desktop_schemas)
    -   [[1.2] [Adding content to applications folders]](#Adding_content_to_applications_folders)
        -   [[1.2.1] [By categories]](#By_categories)
        -   [[1.2.2] [Individually]](#Individually)
        -   [[1.2.3] [Exclusions]](#Exclusions)
        -   [[1.2.4] [Inclusions]](#Inclusions)
        -   [[1.2.5] [Tile icon]](#Tile_icon)

## [Introduction]

By default in Gentoo there is no application folder and all applications are either showing in a single container without further organization than being presented in alphabetic order, either they are elected as favorites and are showing in the dash (left-side bar).

This is unsatisfactory for many users since as the number of applications is growing it becomes always harder and tedious to find out the application desired for launch. Hence, the solution is to organize the applications by subsets similar to the sub-menus in previous major version of GNOME or the Applications menu you can get using shell extensions.

The goal of this article is to present options for desktop customization for the purpose of better organization of applications. This will be done in such a way to avoid using GNOME shell extensions and menus.

### [Gsettings and desktop schemas]

The desktop is controlled by a set of XML files and schemas. The [dconf] application can be used to configure certain aspects of applications, however for full customization the [gsettings] command is recommended.

To add containers for applications, which are actually called folders, the `org.gnome.desktop.app-folders` key will need modified. You can access this key and update the value through [dconf] by following the specified schema, `org.gnome.desktop.app-folders` namely. The value is a list of strings between square brackets and separated by a comma. Here is how to add the folders Office, SysAdmin and Internet after checking the list is actually empty.

`user `[`$`]`gsettings get org.gnome.desktop.app-folders folder-children`

It should return and empty square brackets list. If not, you may wish to add the content of this list to your new list in the following commands instead of replacing it.

To add the folders, proceed as follow:

`user `[`$`]`gsettings set org.gnome.desktop.app-folders folder-children "['Office', 'SysAdmin', 'Internet']"`

This will create the three new applications folders empty and without a name to display. They will show as empty tiles when pressing the super key and clicking on the Applications tile in the dash (left side bar).

Now, you need to give the folders a name to display on the desktop. There is two ways to do it: you can set the name to the actual name you want to display or you can set the name to a file which contains the name and translations in supported languages you want to assign to the folder.

The first alternative is straight forward, for example, for the SysAdmin folder you can proceed as follow:

`user `[`$`]`gsettings set org.gnome.desktop.app-folders.folder:/org/gnome/desktop/app-folders/folders/SysAdmin/ name "System tools"`

However, if you have to support a system with multiple languages you may prefer to do it as follow:

`user `[`$`]`gsettings set org.gnome.desktop.app-folders.folder:/org/gnome/desktop/app-folders/folders/SysAdmin/ name "System-Tools.directory"`

Then,

`user `[`$`]`gsettings set org.gnome.desktop.app-folders.folder:/org/gnome/desktop/app-folders/folders/SysAdmin/ translate true`

The value in the first command (System-Tools.directory) must be an existing file which can be found either in the [/usr/share/desktop-directories] directory, either in [\$HOME/.local/share/desktop-directories] directory with the following format:

[FILE] **`/usr/share/desktop-directories/System-Tools.directory`Sample file content**

    [Desktop Entry]
    Name=System Tools
    Name[fr]=Outils système
    Comment=System configuration and monitoring
    Comment[fr]=Configuration et surveillance système
    Icon=applications-system
    Type=Directory

The format is the Free desktop XDG format as documented [here](https://specifications.freedesktop.org/autostart-spec/autostart-spec-latest.html).

The second command informs Gnome 3 the value is not a fixed string value and it is rather than a file with translations.

### [Adding content to applications folders]

To add content to your newly created folders you have two options:

1.  Select by categories which applications you want to add
2.  Select individually each application you want to add

#### [By categories]

To select by categories you simply change the value of the categories key to a list of applications. The categories\' names are those specified in the stanza Categories in the XDG desktop definition files. You can look at these as well as the list of available applications in directories: [/usr/share/applications and \$HOME/.local/share/applications].

Then, suppose we want to add all the applications in the identified category Office and those in the category Publishing in the Office folder you proceed as follow:

`user `[`$`]`gsettings set org.gnome.desktop.app-folders.folder:/org/gnome/desktop/app-folders/folders/Office/ categories "['Office', 'Publishing']"`

#### [Individually]

To select by the application name you use the XDG desktop definition file name. For example, suppose we want to add the applications Gnumeric, Evolution and Contacts to our folder [Office] we issue the following command given the files: [gnumeric.desktop], [evolution.desktop] and [gnome-contacts.desktop] exists in one of the valid directories:

`user `[`$`]`gsettings set org.gnome.desktop.app-folders.folder:/org/gnome/desktop/app-folders/folders/Office/ apps "['gnumeric.desktop', 'evolution.desktop', 'gnome-contacts.desktop']"`

#### [Exclusions]

What if you want almost all applications in one or more categories except few of them? You can simply specify an exclusion list using the key excluded-apps. For example, suppose we want to exclude Acrobat Reader from the Office folder:

`user `[`$`]`gsettings set org.gnome.desktop.app-folders.folder:/org/gnome/desktop/app-folders/folders/Office/ excluded-apps "['AdobeReader.desktop']"`

#### [Inclusions]

Using both the individual and by categories selection, you can add individually applications to a set of categories in a folder.

#### [Tile icon]

The tile icon will update itself using a smaller version of the icons for the applications in the given folder. There is nothing you need to do for that to happen. It may take a while however before the tile get updated.

-   ::::::
    ::::
    :::
    [![](/images/thumb/e/ec/NoAF.png/120px-NoAF.png)](https://wiki.gentoo.org/wiki/File:NoAF.png)
    :::
    ::::

    ::: gallerytext
    Original applications folder.
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/e/e6/EmptiesAF.png/120px-EmptiesAF.png)](https://wiki.gentoo.org/wiki/File:EmptiesAF.png)
    :::
    ::::

    ::: gallerytext
    Three applications folders newly created without any label assigned to them.
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/6/6a/EmptyAFwithName.png/120px-EmptyAFwithName.png)](https://wiki.gentoo.org/wiki/File:EmptyAFwithName.png)
    :::
    ::::

    ::: gallerytext
    The SysAdmin applications folder with the static label \"System tools\" assigned to it.
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/e/e5/EmptyAFwithTransName.png/120px-EmptyAFwithTransName.png)](https://wiki.gentoo.org/wiki/File:EmptyAFwithTransName.png)
    :::
    ::::

    ::: gallerytext
    The SysAdmin applications folder with a translated label assigned to it. Showing in french here.
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/8/8c/AFwithCategories.png/120px-AFwithCategories.png)](https://wiki.gentoo.org/wiki/File:AFwithCategories.png)
    :::
    ::::

    ::: gallerytext
    The Office applications folder with the two categories Office and Publishing assigned to it, showing the content.
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/3/35/AFwithList.png/120px-AFwithList.png)](https://wiki.gentoo.org/wiki/File:AFwithList.png)
    :::
    ::::

    ::: gallerytext
    The applications folder Office with a list of three applications assigned to it.
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/c/c6/AFwithExclusion.png/120px-AFwithExclusion.png)](https://wiki.gentoo.org/wiki/File:AFwithExclusion.png)
    :::
    ::::

    ::: gallerytext
    The applications folder Office with the Acrobat Reader application excluded.
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/d/d8/AFwithCategories%2BList.png/120px-AFwithCategories%2BList.png)](https://wiki.gentoo.org/wiki/File:AFwithCategories%2BList.png)
    :::
    ::::

    ::: gallerytext
    The application folder Office with categories Office and Publishing assigned to it in addition with the three previous applications.
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/0/04/AFwithIcons.png/120px-AFwithIcons.png)](https://wiki.gentoo.org/wiki/File:AFwithIcons.png)
    :::
    ::::

    ::: gallerytext
    The application folder Office, labeled in french \"Bureautique\", showing the icons on the tile.
    :::
    ::::::