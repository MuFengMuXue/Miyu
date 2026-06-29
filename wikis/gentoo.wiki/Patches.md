**Resources**

[[]][Home](https://devmanual.gentoo.org/ebuild-writing/misc-files/patches/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Patch_(computing) "wikipedia:Patch (computing)")

This page amends the Devmanual\'s [patches article](https://devmanual.gentoo.org/ebuild-writing/misc-files/patches/) and describes how to create a patch for source code.

## Contents

-   [[1] [Creating a patch]](#Creating_a_patch)
    -   [[1.1] [Using diff]](#Using_diff)
    -   [[1.2] [Using git]](#Using_git)
        -   [[1.2.1] [Initialize a git repository]](#Initialize_a_git_repository)
        -   [[1.2.2] [Make changes]](#Make_changes)
        -   [[1.2.3] [Create diff using git]](#Create_diff_using_git)
    -   [[1.3] [Using quilt]](#Using_quilt)
-   [[2] [Unrelated]](#Unrelated)
    -   [[2.1] [Cleanup]](#Cleanup)
    -   [[2.2] [Adjusting a malformed patch from TortoiseGit or Git for Windows]](#Adjusting_a_malformed_patch_from_TortoiseGit_or_Git_for_Windows)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Creating a patch]

### [Using diff]

Unpack the package to a directory name \"a\".

`root `[`#`]`tar -x -v -f /var/cache/distfiles/package.tar.xz`

`root `[`#`]`mv package a`

Copy to a directory named \"b\".

`root `[`#`]`cp -r a b`

Make your changes to b.

`root `[`#`]`emacs b/file.c`

Run diff.

`root `[`#`]`diff -Naur a b > /etc/portage/patches/example-category/example-packagename/my-patch.patch`

### [Using git]

A source code patch for an existing package can easily be created using [[git diff]](https://wiki.gentoo.org/wiki/Git "Git").

Unpack the package to be patched using the [[ebuild](https://wiki.gentoo.org/wiki/Ebuild "Ebuild")] command:

`user `[`$`]`ebuild $(portageq get_repo_path / gentoo)/sys-fs/lvm2/lvm2-2.02.145-r2.ebuild clean unpack`

```
...
>>> Unpacking source...
>>> Unpacking LVM2.2.02.145.tgz to /var/tmp/portage/sys-fs/lvm2-2.02.145-r2/work
>>> Source unpacked in /var/tmp/portage/sys-fs/lvm2-2.02.145-r2/work
```

Step into the [\$] directory as defined in the ebuild:

`user `[`$`]`cd /var/tmp/portage/sys-fs/lvm2-2.02.145-r2/work/LVM2.2.02.145/`

#### [Initialize a git repository]

If the unpacked directory is a git repository, skip the following initialization of the git repository.

Initialize the unpacked package sources as a git repository:

`user `[`$`]`git init`

    Initialized empty Git repository in /var/tmp/portage/sys-fs/lvm2-2.02.145-r2/work/LVM2.2.02.145/.git/

Add all the existing files to git and do a commit. Remember to write a commit message!

`user `[`$`]`git add .`

`user `[`$`]`git commit -m "Initial commit"`

#### [Make changes]

Now make the necessary changes to the unpacked source code, one or more files may be changed. Of course, the required changes should probably be known in advance.

Here is an example of a command making changes to the source code:

`user `[`$`]`sed -e 's/MAKEDEV:-"debian"/MAKEDEV:-"gentoo"/' -i scripts/lvm2create_initrd/lvm2create_initrd`

#### [Create diff using git]

When changes are done, have [git] output the diff, and [tee] it into the patch file:

`user `[`$`]`git diff | tee /tmp/foobar.patch`

```
diff --git a/scripts/lvm2create_initrd/lvm2create_initrd b/scripts/lvm2create_initrd/lvm2create_initrd
index 6e70c55..1e46b5e 100644
--- a/scripts/lvm2create_initrd/lvm2create_initrd
+++ b/scripts/lvm2create_initrd/lvm2create_initrd
@@ -57,7 +57,7 @@ DEVRAM=/tmp/initrd.$$
 BINFILES=$
 BASICDEVICES=$
 BLOCKDEVICES=$
-MAKEDEV=$
+MAKEDEV=$

 # Uncomment this if you want to disable automatic size detection
 #INITRDSIZE=4096
```

### [Using quilt]

[[[dev-util/quilt]](https://packages.gentoo.org/packages/dev-util/quilt)[]] is a patch manager used extensively by the Debian project, that can be used to create and maintain simple patchsets. It fills a niche where the diff method is too inconvenient for multiple patches, and git is too involved. The workflow is similar to both:

Unpack the package and enter the directory:

`root `[`#`]`tar -x -v -f /var/cache/distfiles/package.tar.xz`

`root `[`#`]`cd package`

Create a new patch:

`root `[`#`]`quilt new package-fix.patch`

Add a file to the patch and make your changes:

`root `[`#`]`quilt add file.c`

`root `[`#`]`vi file.c`

Or as a shortcut (change the \$EDITOR variable for your prefered editor):

`root `[`#`]`quilt edit file.c`

Refresh the patch. This generates the actual patch file:

`root `[`#`]`quilt refresh -p ab`

Other useful commands include:

-   [quilt series]: Show patch stack
-   [quilt pop -a]: Unapply all patches
-   [quilt push -a]: Apply all patches
-   [quilt header -e]: Modify the patch\'s header (Using \$EDITOR)
-   [quilt diff]: Show changes of current patch in the stack, without refreshing the file
-   [quilt rename package-fix-more.patch]: Rename the current patch in the stack
-   [quilt fork package-v2-fix.patch]: Copy and rename the current patch in the stack
-   [quilt delete]: Delete the current patch in the stack
-   [quilt remove]: Remove file from current patch

## [Unrelated]

### [Cleanup]

If the patch isn\'t in a standard format already (like [git format-patch]), it\'s a good idea to clean it up a bit before using it in an ebuild. The devmanual has a [guide](https://devmanual.gentoo.org/ebuild-writing/misc-files/patches/index.html#clean-patch-howto), and the [scrub-patch] command from [[[app-portage/iwdevtools]](https://packages.gentoo.org/packages/app-portage/iwdevtools)[]] may used to automate some changes.

### [Adjusting a malformed patch from TortoiseGit or Git for Windows]

Patches generated by [Tortoise Git](//tortoisegit.org/docs/tortoisegit/tgit-dug-patch.html) and Git for Windows are padded with additional information that `patch` does not understand.

[FILE] **`PATCH.patch`Typical Tortoise Git/Git for Windows Patch**

    From HASH Day Mon DD hh:mm:ss YYYY
    From: AUTHOR <AUTHOR@E-MAIL.TLD>
    Date: Day, DD MMM YYYY hh:mm:ss +hhmm
    Subject: [PATCH] COMMIT MESSAGE

    ---
     PATH/TO/FILE.EXT  1 +
     1 file changed, 1 insertion(+)

    diff --git a/PATH/TO/FILE.EXT b/PATH/TO/FILE.EXT
    index HA..SH CODE
    --- a/PATH/TO/FILE.EXT
    +++ b/PATH/TO/FILE.EXT
    @@ -56,6 +56,7 @@
    +  some new code
    -  some old code
    --
    VERSION.windows.REVISION

The individual generating the patch has to strip these additional lines to make a viable patch file.

[FILE] **`PATCH.patch`Acceptable Tortoise Git/Git for Windows Patch**

    --- a/PATH/TO/FILE.EXT
    +++ b/PATH/TO/FILE.EXT
    @@ -56,6 +56,7 @@
    +  some new code
    -  some old code

## [See also]

-   [/etc/portage/patches](https://wiki.gentoo.org/wiki//etc/portage/patches "/etc/portage/patches") --- provide a way to apply patches to package source code when sources are extracted before installation
-   [User:Veremit/Patch_format](https://wiki.gentoo.org/wiki/User:Veremit/Patch_format "User:Veremit/Patch format")
-   [GLEP 25](https://www.gentoo.org/glep/glep-0025.html) - Technical information about the formal inclusion and usage of patches within portage.

## [External resources]

-   How to write [clean patches](https://devmanual.gentoo.org/ebuild-writing/misc-files/patches/#clean-patch-howto) when not using *git-format-patch*.
-   [Patching with eapply](https://devmanual.gentoo.org/ebuild-writing/functions/src_prepare/eapply/index.html) - Describes how ebuilds should use PATCHES=( \"\$/mypatch.patch\" \"\$/patches_folder/\" )