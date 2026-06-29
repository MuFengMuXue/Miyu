This directory is optional and can be used for patches - call them \"user patches\" - to be applied without changing the ebuild. User patches provide a way to apply patches to package source code when sources are extracted before installation. This can be useful for applying upstream patches to unresolved bugs and for the rare cases of site-specific patches.

The basic method is to just drop patches into the appropriate subdirectory of **/etc/portage/patches**, and they will be applied during [package installation](https://wiki.gentoo.org/wiki/Emerge "Emerge").

[Ebuilds](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") themselves cannot be patched by this method, just the package\'s source code, as fetched by an ebuild.

## Contents

-   [[1] [Precondition]](#Precondition)
-   [[2] [Adding user patches]](#Adding_user_patches)
    -   [[2.1] [Example patch file]](#Example_patch_file)
-   [[3] [Using a git directory as a source of patches]](#Using_a_git_directory_as_a_source_of_patches)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Precondition]

Prior to EAPI 6, user patching support was optional, so some poorly maintained ebuilds in third-party ebuild repositories still may not support it.

## [Adding user patches]

A patch can be set to be applied to all versions of a package, or to a single specific version. Additionally, it can be constrained to apply only to a particular slot. All this is done by naming the directory containing the patch file. This directory name must be the name of the package, optionally followed by a hyphen and the version number, optionally followed by a colon and the slot number.

Examples:

  ---------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------
  Syntax                                                                                                                                   with [[[dev-lang/python]](https://packages.gentoo.org/packages/dev-lang/python)[]]   Explanation
  [/etc/portage/patches/\$/\$]            [/etc/portage/patches/dev-lang/python]                                                                                                                                                                                                                                                  Applies to any version of the python package.
  [/etc/portage/patches/\$/\$:\$]   [/etc/portage/patches/dev-lang/python:3.4]                                                                                                                                                                                                                                              Applies to any version in slot 3.4.
  [/etc/portage/patches/\$/\$]             [/etc/portage/patches/dev-lang/python-3.4.2]                                                                                                                                                                                                                                            Applies to version 3.4.2 only.
  [/etc/portage/patches/\$/\$-\$]      [/etc/portage/patches/dev-lang/python-3.3.5-r0]                                                                                                                                                                                                                                         The version number may contain modifiers like \"-r0\".
  ---------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------

### [Example patch file]

An example shows how to easily apply an upstream patch for [[[CVE-2017-8934]](https://bugs.gentoo.org/show_bug.cgi?id=618622)[]] of [[[x11-misc/pcmanfm]](https://packages.gentoo.org/packages/x11-misc/pcmanfm)[]].

The affected version of that package is 1.2.5 and upstream provides the patch for it but has not yet released a new version.

For applying the patch from upstream, the appropriate directory needs to be created:

`root `[`#`]`mkdir -p /etc/portage/patches/x11-misc/pcmanfm-1.2.5`

Next, an arbitrarily named file with suffix [.patch] or [.diff] has to be dropped here with the content provided from upstream:

[FILE] **[[`/etc/portage/patches/x11-misc/pcmanfm-1.2.5/CVE-2017-8934.patch`]](https://github.com/lxde/pcmanfm/commit/bc8c3d871e9ecc67c47ff002b68cf049793faf08.diff)**

    # index 8c2049a..876f7f3 100644 (file)
    # --- a/NEWS
    # +++ b/NEWS
    # @@ -1,3 +1,7 @@
    # +* Fixed potential access violation, use runtime user dir instead of tmp dir
    # +    for single instance socket.
    # +
    # +
    #  Changes on 1.2.5 since 1.2.4:

     * Removed options to Cut, Remove and Rename from context menu on mounted
    diff --git a/src/single-inst.c b/src/single-inst.c
    index 62c37b3..aaf84ab 100644 (file)
    --- a/src/single-inst.c
    +++ b/src/single-inst.c
    @@ -2,7 +2,7 @@
      *      single-inst.c: simple IPC mechanism for single instance app
      *
      *      Copyright 2010 Hong Jen Yee (PCMan)
    - *      Copyright 2012 Andriy Grytsenko (LStranger) <andrej@rep.kiev.ua>
    + *      Copyright 2012-2017 Andriy Grytsenko (LStranger) <andrej@rep.kiev.ua>
      *
      *      This program is free software; you can redistribute it and/or modify
      *      it under the terms of the GNU General Public License as published by
    @@ -404,11 +404,16 @@ static void get_socket_name(SingleInstData* data, char* buf, int len)
         }
         else
             dpynum = 0;
    +#if GLIB_CHECK_VERSION(2, 28, 0)
    +    g_snprintf(buf, len, "%s/%s-socket-%s-%d", g_get_user_runtime_dir(),
    +               data->prog_name, host ? host : "", dpynum);
    +#else
         g_snprintf(buf, len, "%s/.%s-socket-%s-%d-%s",
                     g_get_tmp_dir(),
                     data->prog_name,
                     host ? host : "",
                     dpynum,
                     g_get_user_name());
    +#endif
     }

For testing, step into the package\'s ebuild directory and run the [ebuild pcmanfm-1.2.5.ebuild clean prepare]:

`root `[`#`]`cd $(portageq get_repo_path / gentoo)/x11-misc/pcmanfm `

`root `[`#`]`ebuild pcmanfm-1.2.5.ebuild clean prepare`

     * pcmanfm-1.2.5.tar.xz SHA256 SHA512 WHIRLPOOL size ;-) ...             [ ok ]
     * checking ebuild checksums ;-) ...                                     [ ok ]
     * checking auxfile checksums ;-) ...                                    [ ok ]
     * checking miscfile checksums ;-) ...                                   [ ok ]
    >>> Unpacking source...
    >>> Unpacking pcmanfm-1.2.5.tar.xz to /var/tmp/portage/x11-misc/pcmanfm-1.2.5/work
    >>> Source unpacked in /var/tmp/portage/x11-misc/pcmanfm-1.2.5/work
    >>> Preparing source in /var/tmp/portage/x11-misc/pcmanfm-1.2.5/work/pcmanfm-1.2.5 ...
     * Applying patches from /etc/portage/patches/x11-misc/pcmanfm-1.2.5 ...
     *   CVE-2017-8934.patch ...                               [ ok ]
     * User patches applied.
    >>> Source prepared.

With the message *\"User patches applied.\"* all is good and the package needs to be re-emerged as normally.

Once the patch gets merged to the [ebuild repository](https://gitweb.gentoo.org/repo/gentoo.git/log), do not forget to remove it from the [/etc/portage/patches] directory. Otherwise next time compiling the ebuild might fail.

## [Using a git directory as a source of patches]

Instead of creating the directory, a symlink can be created to a git directory on the system.

`root `[`#`]`mkdir -p /etc/portage/patches/sys-libs && ln -s /home/user/projects/glibc /etc/portage/patches/sys-libs/glibc`

** Note**\
When using `userpriv` as a [`FEATURES`](https://wiki.gentoo.org/wiki/FEATURES "FEATURES") value in Portage (eg. in [/etc/portage/make.conf]), Portage drops root privileges to `portage:portage` which means that the folder that the symlink points to must be accessible by the user or group *portage* otherwise the patches will be silently ignored and not applied (file [epatch_user.log] contains the string *none*); ie. in this case, all the folders of [/home/user/projects/glibc] are already accessible due to `o+rx` permissions but in the case of root and using this path [/root/projects/glibc] then [/root], unlike [/home], is inaccessible due to `u+rx` permissions\...

Now, in the git directory, perform the usual work. After finishing remove all patches from the previous run and use `git format-patch` to create a patchset from the branch based on another known branch.

`user `[`$`]`rm -f *.patch && git format-patch origin/master`

This solution relies on the fact that only files ending with [.patch] are processed in the patch directory.

## [See also]

-   [/etc/portage/bashrc](https://wiki.gentoo.org/wiki//etc/portage/bashrc "/etc/portage/bashrc") --- a global [bashrc] file referenced by Portage.
-   [/etc/portage/package.env](https://wiki.gentoo.org/wiki//etc/portage/package.env "/etc/portage/package.env") --- can contain files to be called during the installation of specific packages, or files used to set Portage\'s environment variables on a per-package basis.
-   [Creating a patch](https://wiki.gentoo.org/wiki/Creating_a_patch "Creating a patch") --- describes how to create a patch for source code.
-   [Using eapply_user (AMD64 Handbook)](https://wiki.gentoo.org/wiki/Handbook:AMD64/Portage/Advanced#Using_eapply_user "Handbook:AMD64/Portage/Advanced")

## [External resources]

-   [GLEP 25](https://www.gentoo.org/glep/glep-0025.html)
-   [eutils.eclass: Disable epatch_user in EAPI 6.](https://gitweb.gentoo.org/repo/gentoo.git/commit/eclass/eutils.eclass?id=324c60a90afb8c34ba05b5b4f5814ce72e835c48) - EAPI 6 has eapply_user which should be used instead.
-   [The Ultimate Guide to EAPI 6](https://blogs.gentoo.org/mgorny/2015/11/13/the-ultimate-guide-to-eapi-6/)
-   [Patching with eapply](https://devmanual.gentoo.org/ebuild-writing/functions/src_prepare/eapply/) - Patching within ebuilds, from devmanual.gentoo.org
-   How to write [clean patches](https://devmanual.gentoo.org/ebuild-writing/misc-files/patches/#clean-patch-howto) when not using *git-format-patch*.
-   [A Patchy System -- Applying Patches with Portage to Fix Upstream Bugs](https://leo3418.github.io/2021/03/01/portage-user-patches.html)