The *way* a bug is reported helps to get it fixed sooner. This article covers the recommended method of forensically reporting *specific details* of bugs within Gentoo. These generally consist of broken upstream code causing compilation errors, run time problems, or packaging errors.

This article also details some common troubleshooting steps which may reveal the bug\'s solution, or clues for the solution, to report to the Gentoo developer or group responsible for the problem.

See [Bugzilla/Bug report guide](https://wiki.gentoo.org/wiki/Bugzilla/Bug_report_guide "Bugzilla/Bug report guide") for tips on how to prepare a bug report that is as helpful as possible for the developer to read.

## Contents

-   [[1] [Types of bugs]](#Types_of_bugs)
    -   [[1.1] [Broken code from upstream]](#Broken_code_from_upstream)
    -   [[1.2] [Run-time errors]](#Run-time_errors)
    -   [[1.3] [Emerge failures]](#Emerge_failures)
-   [[2] [Handling run-time errors]](#Handling_run-time_errors)
    -   [[2.1] [Finding file access errors using strace]](#Finding_file_access_errors_using_strace)
        -   [[2.1.1] [Introduction]](#Introduction)
        -   [[2.1.2] [Using strace to track the issue]](#Using_strace_to_track_the_issue)
-   [[3] [Handling emerge failures]](#Handling_emerge_failures)
    -   [[3.1] [Introduction]](#Introduction_2)
    -   [[3.2] [Evaluating emerge failures]](#Evaluating_emerge_failures)
    -   [[3.3] [Set locale to C or English]](#Set_locale_to_C_or_English)
    -   [[3.4] [Emerge and PORT_LOGDIR]](#Emerge_and_PORT_LOGDIR)
-   [[4] [Bugzilla search]](#Bugzilla_search)
-   [[5] [Reporting bugs]](#Reporting_bugs)
-   [[6] [Working with a bug]](#Working_with_a_bug)
-   [[7] [Testing ebuilds]](#Testing_ebuilds)
    -   [[7.1] [Repair and test ebuilds]](#Repair_and_test_ebuilds)
    -   [[7.2] [Testing the ebuild]](#Testing_the_ebuild)
-   [[8] [Account removal requests]](#Account_removal_requests)
-   [[9] [Acknowledgements]](#Acknowledgements)
-   [[10] [See also]](#See_also)
-   [[11] [External references]](#External_references)

## [Types of bugs]

Bugs come in many forms like emerge failures or segmentation faults. Whatever the cause, the fact still remains that such a bug must be fixed. Here are a few examples of such bugs.

### [Broken code from upstream]

A program installs without errors and the [.ebuild] file is fine. But during runtime the program has a malfunction that would appear on other distributions too. In this case you should report the bug upstream (to the developer of the program). Often you can find a link to the right place in the [metadata.xml](https://devmanual.gentoo.org/ebuild-writing/misc-files/metadata/) file which is stored in the same folder as the ebuild.

One should **not file a Gentoo bug** for upstream bugs.

### [Run-time errors]

`user `[`$`]`` ./bad_code `perl -e 'print "A"x100'` ``

    Segmentation fault

### [Emerge failures]

`root `[`#`]`emerge --ask xclass`

    /usr/lib/gcc-lib/i686-pc-linux-gnu/3.3.2/include/g++-v3/backward/backward_warning.h:32:2:
    warning: #warning This file includes at least one deprecated or antiquated
    header. Please consider using one of the 32 headers found in section 17.4.1.2 of
    the C++ standard. Examples include substituting the <X> header for the <X.h>
    header for C++ includes, or <sstream> instead of the deprecated header
    <strstream.h>. To disable this warning use -Wno-deprecated.
    In file included from main.cc:40:
    menudef.h:55: error: brace-enclosed initializer used to initialize `
    OXPopupMenu*'
    menudef.h:62: error: brace-enclosed initializer used to initialize `
    OXPopupMenu*'
    menudef.h:70: error: brace-enclosed initializer used to initialize `
    OXPopupMenu*'
    menudef.h:78: error: brace-enclosed initializer used to initialize `
    OXPopupMenu*'
    main.cc: In member function `void OXMain::DoOpen()':
    main.cc:323: warning: unused variable `FILE*fp'
    main.cc: In member function `void OXMain::DoSave(char*)':
    main.cc:337: warning: unused variable `FILE*fp'
    make[1]: *** [main.o] Error 1
    make[1]: Leaving directory
    `/var/tmp/portage/xclass-0.7.4/work/xclass-0.7.4/example-app'
    make: *** [shared] Error 2

    !!! ERROR: x11-libs/xclass-0.7.4 failed.
    !!! Function src_compile, Line 29, Exitcode 2
    !!! 'emake shared' failed

## [Handling run-time errors]

[Debugging with the **G**NU **D**e**b**ugger](https://wiki.gentoo.org/wiki/GDB "GDB").

### [Finding file access errors using strace]

#### [Introduction]

Programs often use files to fetch configuration information, access hardware or write logs. Sometimes, a program attempts to reach such files incorrectly. A tool called [strace] was created to help deal with this. [strace] traces system calls (hence the name) which include calls that use the memory and files. For our example, we\'re going to take a program foobar2. This is an updated version of foobar. However, during the change over to foobar2, you notice all your configurations are missing! In foobar version 1, you had it setup to say \"foo\", but now it\'s using the default \"bar\".

`user `[`$`]`./foobar2`

    Configuration says: bar

Our previous configuration specifically had it set to foo, so let\'s use [strace] to find out what is going on.

#### [Using strace to track the issue]

We make [strace] log the results of the system calls. To do this, we run [strace] with the -o\[file\] arguments. Let\'s use it on foobar2 as shown.

`root `[`#`]`strace -o strace.log ./foobar2`

This creates a file called [strace.log] in the current directory. We check the file, and shown below are the relevant parts from the file.

[CODE] **Viewing the strace log**

    open(".foobar2/config", O_RDONLY)       = 3
    read(3, "bar", 3)                       = 3

Aha! So there is the problem. Someone moved the configuration directory to [.foobar2] instead of [.foobar]. We also see the program reading in \"bar\" as it should. In this case, we can recommend the ebuild maintainer to put a warning about it. For now though, we can copy over the config file from [.foobar] and modify it to produce the correct results.

## [Handling emerge failures]

### [Introduction]

[emerge] errors, such as the one displayed earlier, can be a major cause of frustration for users. Reporting them is considered crucial for maintaining the health of Gentoo. Take a look at a sample ebuild, foobar2, which contains some build errors.

### [Evaluating emerge failures]

Here is a very simple [emerge] error:

`root `[`#`]`emerge --ask foobar2`

    gcc -D__TEST__ -D__GNU__ -D__LINUX__ -L/usr/lib -I/usr/include -L/usr/lib/nspr/ -I/usr/include/fmod \
     -c -o foobar2-7.o foobar2-7.c
    gcc -D__TEST__ -D__GNU__ -D__LINUX__ -L/usr/lib -I/usr/include -L/usr/lib/nspr/ -I/usr/include/fmod \
     -c -o foobar2-8.o foobar2-8.c
    gcc -D__TEST__ -D__GNU__ -D__LINUX__ -L/usr/lib -I/usr/include -L/usr/lib/nspr/ -I/usr/include/fmod \
     -c -o foobar2-9.o foobar2-9.c
    gcc -D__TEST__ -D__GNU__ -D__LINUX__ -L/usr/lib -I/usr/include -L/usr/lib/nspr/ -I/usr/include/fmod \
     -c -o foobar2.o foobar2.c
    foobar2.c:1:17: ogg.h: No such file or directory
    make: *** [foobar2.o] Error 1

    !!! ERROR: sys-apps/foobar2-1.0 failed.
    !!! Function src_compile, Line 19, Exitcode 2
    !!! Make failed!
    !!! If you need support, post the topmost build error, NOT this status message

The program is compiling smoothly when it suddenly stops and presents an error message. This particular error can be split into three different sections, the compile messages, the build error, and the emerge error message as shown below.

[CODE] **Compilation messages**

    gcc -D__TEST__ -D__GNU__ -D__LINUX__ -L/usr/lib -I/usr/include -L/usr/lib/nspr/ -I/usr/include/fmod \
     -c -o foobar2-7.o foobar2-7.c
    gcc -D__TEST__ -D__GNU__ -D__LINUX__ -L/usr/lib -I/usr/include -L/usr/lib/nspr/ -I/usr/include/fmod \
     -c -o foobar2-8.o foobar2-8.c
    gcc -D__TEST__ -D__GNU__ -D__LINUX__ -L/usr/lib -I/usr/include -L/usr/lib/nspr/ -I/usr/include/fmod \
     -c -o foobar2-9.o foobar2-9.c
    gcc -D__TEST__ -D__GNU__ -D__LINUX__ -L/usr/lib -I/usr/include -L/usr/lib/nspr/ -I/usr/include/fmod \
     -c -o foobar2.o foobar2.c

[CODE] **Build failure**

    foobar2.c:1:17: ogg.h: No such file or directory
    make: *** [foobar2.o] Error 1

[CODE] **Emerge failure**

    !!! ERROR: sys-apps/foobar2-1.0 failed.
    !!! Function src_compile, Line 19, Exitcode 2
    !!! Make failed!
    !!! If you need support, post the topmost build error, NOT this status message

The compilation messages are what lead up to the error. Most often, it is good to at least include 10 lines of compile information so that the developer knows where the compilation was at when the error occurred.

### [Set locale to C or English]

Please make sure you always include error messages in English, even when your system language is set to something else. You can temporarily switch to English locale by prepending `LC_ALL=C` to the emerge command like this:

`root `[`#`]`LC_ALL=C emerge sys-apps/foobar2`

** Note**\
This is also about the only time the `LC_ALL` environmental variable should be used for specifying locale settings. When looking for a way to switch the system\'s language, please consult the [localization guide](https://wiki.gentoo.org/wiki/Localization/Guide "Localization/Guide") instead.

Make errors are the actual error and the information the developer needs. When you see \"make: \*\*\*\", this is often where the error has occurred.

The emerge error is what [emerge] throws out as an error. Sometimes, this might also contain some important information.

### [Emerge and PORT_LOGDIR]

`PORT_LOGDIR` is a Portage variable that sets up a log directory for separate emerge logs. Let\'s take a look and see what that entails. First, run the emerge with `PORT_LOGDIR` set to a favorite log location. Let\'s set the favorite log location to [/var/log/portage] for this example.

** Note**\
In the default setup, [/var/log/portage] does not exist, and you will most likely have to create it. If you do not, portage will fail to write the logs.

`root `[`#`]`PORT_LOGDIR=/var/log/portage emerge category/foobar2`

Now the emerge fails again. However, this time we have a log we can work with, and attach to the bug later on. Let\'s take a quick look at our log directory.

`user `[`$`]`ls -la /var/log/portage`

    total 16
    drwxrws---   2 root root 4096 Jun 30 10:08 .
    drwxr-xr-x  15 root root 4096 Jun 30 10:08 ..
    -rw-r--r--   1 root root 7390 Jun 30 10:09 category:foobar2-1.0:20090110-213217.log

The log files have the format `[category]:[package name]-[version]:[date].log`. A quick look at the log file will show the entire emerge process. This can be attached later on as we\'ll see in the bug reporting section. Now that we\'ve safely obtained our information needed to report the bug we can continue to do so. However, before we get started on that, we need to make sure no one else has reported the issue. Let\'s take a look at searching for bugs.

## [Bugzilla search]

[Bugzilla](https://www.bugzilla.org/) is what the Gentoo project uses to handle bugs. Head over to [Gentoo Bugzilla](https://bugs.gentoo.org/) to see how it looks.

One of the most frustrating things for developers and bug-wranglers is finding duplicate bug reports. These cost them valuable time that they could otherwise use to work on more important bugs. Often, this can be prevented by a few simple search methods. So we\'re going to see how to search for bugs and find out if you have one that\'s similar. For this example, we\'re going to use the xclass emerge error that was used earlier.

[CODE] **xclass emerge error**

    /usr/lib/gcc-lib/i686-pc-linux-gnu/3.3.2/include/g++-v3/backward/backward_warning.h:32:2:
    warning: #warning This file includes at least one deprecated or antiquated
    header. Please consider using one of the 32 headers found in section 17.4.1.2 of
    the C++ standard. Examples include substituting the <X> header for the <X.h>
    header for C++ includes, or <sstream> instead of the deprecated header
    <strstream.h>. To disable this warning use -Wno-deprecated.
    In file included from main.cc:40:
    menudef.h:55: error: brace-enclosed initializer used to initialize `
    OXPopupMenu*'
    menudef.h:62: error: brace-enclosed initializer used to initialize `
    OXPopupMenu*'
    menudef.h:70: error: brace-enclosed initializer used to initialize `
    OXPopupMenu*'
    menudef.h:78: error: brace-enclosed initializer used to initialize `
    OXPopupMenu*'
    main.cc: In member function `void OXMain::DoOpen()':
    main.cc:323: warning: unused variable `FILE*fp'
    main.cc: In member function `void OXMain::DoSave(char*)':
    main.cc:337: warning: unused variable `FILE*fp'
    make[1]: *** [main.o] Error 1
    make[1]: Leaving directory
    `/var/tmp/portage/xclass-0.7.4/work/xclass-0.7.4/example-app'
    make: *** [shared] Error 2

    !!! ERROR: x11-libs/xclass-0.7.4 failed.
    !!! Function src_compile, Line 29, Exitcode 2
    !!! 'emake shared' failed

To begin searching, visit [Gentoo\'s Bugzilla homepage](https://bugs.gentoo.org/) and log in.

** Note**\
Logging in has been made a requirement for search due to hammering by bots; searching Bugzilla is intense on database queries.

Click on [Query Existing bug reports]. The reason why we choose this over the basic bug search is because the basic bug search tends to give vague results and often hinders users from looking through the results and finding the duplicate bug. Once we click on the query screen, we reach the next page:

** Note**\
If you\'ve used the Advanced Search before, you\'ll most likely see that screen instead.

Proceed by clicking on the [Advanced Search] link to bring up the Advanced Search page. While it may seem overwhelming at first, we\'re going to look at a few simple areas to narrow down the rather vague searches Bugzilla returns.

-   The first field is the summary of the bug. Here we\'re simply going to put the name of the package that\'s crashing. If Bugzilla does not return results, try removing the package name, just in case someone didn\'t put that in the summary (highly unlikely, but we\'ve seen a fair share of strange bug reports).
-   Product, Component, and Version should all be set to the default. This prevents us from being too specific and missing all the bugs.
-   Comment is the important part. Use the comment field to list what appears to be a specific instance of the error. Basically, don\'t use anything like the beginning of the build error, find a line that\'s before it stating a true error. Also, you\'ll want to filter out any punctuation to prevent bugzilla from interpreting the results the comment the wrong way.\
    Let\'s look at our example from the xclass emerge error again, and notice that it is specific enough to where we\'ll find the bug without wading through other xclass compile failure candidates:

[CODE] **Comment line content**

    menudef.h:78: error: brace-enclosed initializer used to initialize `OXPopupMenu'
    ## (Remove the quotes ' ')
    menudef.h 78 error brace-enclosed initializer used to initialize OXPopupMenu

-   URI, Whiteboard, and Keywords can all be left alone. What we\'ve entered so far should be enough to find our bug. Let\'s take a look at what we have filled out.

Now we click on the Search button and look at the results. If our search criteria are specific enough, then that is a lot easier to deal with. Chances are that the issue we found on Bugzilla is exactly the problem we\'ve hit, and that it has also been resolved. By checking the last comment we see the solution and know what to do in order to resolve it.

## [Reporting bugs]

The [Bugzilla/Bug report guide](https://wiki.gentoo.org/wiki/Bugzilla/Bug_report_guide "Bugzilla/Bug report guide") explains how to prepare a good bug report.

## [Working with a bug]

Looking at the bug, we see the information we provided earlier. You will notice that the bug has been assigned to bug-wranglers@gentoo.org. This is the default location for application component bugs. The details we entered about the bug are available as well.

However, bug-wranglers (usually) will not fix these kind of bugs, so we\'ll reassign it to someone that can (you can let bug-wranglers re-assign it for you as well). For this we use the package\'s [metadata.xml]. You can normally find them in [/var/db/repos/gentoo/category/package/metadata.xml].

** Note**\
You have to be the reporter of the bug or a member of certain Gentoo Bugzilla groups (like Gentoo Developers) to be able to reassign bugs.

[FILE] **`/var/db/repos/gentoo/category/package/metadata.xml`**

    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE pkgmetadata SYSTEM "http://www.gentoo.org/dtd/metadata.dtd">

    <herd>chriswhite</herd>
    <maintainer>
    <email>chriswhite@gentoo.org</email>
    <name>Chris White</name>
    </maintainer>
    <longdescription lang="en">
    Foobar2 is a package that uses a configuration file to display a word.
    </longdescription>
    </pkgmetadata>

`user `[`$`]` equery meta -mH media-sound/audacity # will grep and print (proxy-)maintainer from metadata`

Notice the maintainer section. This lists the maintainer of the package, which in this case is Chris White. The email listed is chriswhite@gentoo.org. We will use this to re-assign the bug to the proper person. To do this, click the bubble next to Reassign bug to, then fill in the email.

** Note**\
A bug for a package without a [metadata.xml] file should be re-assigned to maintainer-needed@gentoo.org and a package that needs a Gentoo Developer to maintain should be assigned to maintainer-wanted@gentoo.org.

Then click the [Commit] button for the changes to take place. The bug has been reassigned to the correct developer. Shortly afterward, you notice (by email usually) that the developer responded to the bug. For instance, he might have asked to see an strace log to figure out how the program is trying to reach the configuration file. You follow the instructions on using strace and obtain an strace log. Now you need to attach it to the bug. In order to do this, click on \"Create A New Attachment\":

-   File - This is the location of the file on the local machine. In this example, it is the location of [strace.log]. The [Browse\...] button can be used to select the [strace.log] file, or the path can be entered directly in the text field.
-   Description - A short one liner, or a few words describing the attachment. \"strace.log\" will be entered here, since that is self-explanatory.
-   Content Type - This is the type of the file being attached to the bug.
-   Obsoletes - If there were attachments submitted to the bug before the current one, you have an option of declaring them obsoleted by the newest (current) attachment. Since we have no prior attachments to this bug this field can be ignored.
-   Comment - Enter comments that will be visible along with the attachments. You could elaborate on the attachment here, if needed.

With respect to Content Type, here are a few more details. Check the \"patch\" check box when submitting a patch. Otherwise, Bugzilla can be asked to \"auto-detect\" the file type (not advisable). The other options are \"select from list\" (which is most frequently used), use plain text (text/plain) for *most* attachments except binary files like images (which can use image/gif, image/jpeg or image/png depending on type), or compressed files like .tar.bz2 which would use application/octet-stream as content type.

Submit [strace.log] and it is reflected on the bug report.

It has been mentioned above that sometimes ebuilds will output instructions in the emerge error to attach a certain file. An example can be seen below:

[CODE] **File attachment request example**

    configure: error: PNG support requires ZLIB. Use --with-zlib-dir=<DIR>

    !!! Please attach the config.log to your bug report:
    !!! /var/tmp/portage/php-5.0.3-r1/work/php-5.0.3/config.log

    !!! ERROR: dev-php/php-5.0.3-r1 failed.
    !!! Function econf, Line 485, Exitcode 0
    !!! econf failed
    !!! If you need support, post the topmost build error, NOT this status message.

Please attach any files mentioned in error messages to bug reports.

Sometimes a developer might ask bug submitters to attach a diff or patch for a file. Standard diff files can be obtained by executing the following commands:

`user `[`$`]`cp file file.old `

`user `[`$`]`nano file `

`user `[`$`]`diff -u file.old file `

For C/C++ source files, the `-p` flag is added to show what function calls the diff applies to:

`user `[`$`]`cp file.c file.c.old `

`user `[`$`]`nano file.c `

`user `[`$`]`diff -up file.c.old file.c `

The documentation team will require the flag combination `-Nt` as well as `-u`. This mainly has to do with tab expansion. You can create such a diff with:

`user `[`$`]`cp file.xml file.xml.old `

`user `[`$`]`nano file.xml `

`user `[`$`]`diff -Nut file.xml.old file.xml `

And your diff is created. While we\'re doing all this, suppose another person finds the same bug by searching through Bugzilla and is curious to keep track of the bug, they may do so by putting their email in the [Add CC field] of the bug as shown below. You could also keep track of other bugs by following the same method.

** Note**\
Email addresses must be registered with Gentoo Bugzilla. In order to CC multiple addresses, simply separate them with commas or spaces.

After all this work, the bug can undergo various status markings. This is usually done by the Gentoo Developers and sometimes by the reporter. The following are the various possible states a bug may go through during its lifetime:

-   UNCONFIRMED - You\'re generally not going to see this too often. This means that a bug reporter has opened a bug using the advanced method and is uncertain their bug is an actual bug.
-   NEW - Bugs that are first opened are considered new.
-   ASSIGNED - When the person assigned the bug validates the bug, it will often receive ASSIGNED status while they figure out the issue. This lets bug reporter know a developer has accepted the bug as a real bug.
-   REOPENED - Someone has resolved a bug and you think the solution is not feasible or the problem still persists. At this point, you may re-open the bug. Please **do not abuse this**. If a developer closes the bug a second or third time, chances are that your bug is closed.
-   RESOLVED - A firm decision has been taken on the bug. Usually goes onto FIXED to indicate the bug is solved and the matter closed although various other resolutions are possible. We\'ll look into those a little later.
-   VERIFIED - The steps take to work the bug are correct. This is usually a QA thing.
-   CLOSED - Basically means RIP for the bug and it\'s buried under the never ending flow of new bugs.

Now shortly afterward, we find the error in the strace log and fix the bug and mark it as RESOLVED FIXED and mention that there was a change in the location of configuration files, and that I will update the ebuild with a warning about it. The bug now becomes resolved.

If you open the bug, you\'ll notice you can still change the bug status. For instance, there is a link to REOPEN. This gives you the option of Reopening the bug if you wish to (i.e. the developer thinks it\'s resolved but it\'s really not to your standards).

The following is an overview of possible resolutions:

-   FIXED - The bug is fixed, follow the instructions to resolve your issue.
-   INVALID - You did not do something specifically documented, causing the bug.
-   DUPLICATE - You didn\'t use this guide and reported a duplicate bug.
-   WORKSFORME - Developer/person assigned the bug cannot reproduce your error.
-   CANTFIX - Somehow the bug cannot be solved because of certain circumstances. These circumstances will be noted by the person taking the bug.
-   WONTFIX - This is usually applied to new ebuilds or feature requests. Basically the developer does not want to add a certain feature because it is not needed, a better alternative exists, or it\'s just plain broken. Sometimes you may be given a solution to get said issue resolved.
-   UPSTREAM - The bug cannot be fixed by the Gentoo development team, and have requested you take the problem upstream (the people that actually made the program) for review. Upstream has a few ways of handling bugs. These include mailing lists, IRC channels, and even bug reporting systems. If you\'re not sure how to contact them, ask in the bug and someone will point you to the right direction.

Sometimes, before the bug can be resolved, a developer may request that you test an updated ebuild. In the next chapter we\'ll take a look at testing ebuilds.

## [Testing ebuilds]

### [Repair and test ebuilds]

[Create an ebuild repository](https://wiki.gentoo.org/wiki/Creating_an_ebuild_repository "Creating an ebuild repository") or a [topic branch](https://wiki.gentoo.org/wiki/GitHub_Pull_Requests#Step_2:_User_changes_a_package "GitHub Pull Requests") to test fixed ebuilds in.

### [Testing the ebuild]

The process to create an ebuild that can be used by [emerge] is fairly simple. A Manifest file must be generated for the ebuild. This can be done with the ebuild command. Run it as shown:

`root `[`#`]`ebuild foobar2-1.0.ebuild manifest`

    >>> Creating Manifest for /var/db/repos/localrepo/sys-apps/foobar2

Now let\'s test to see if it works as it should.

`root `[`#`]`emerge --ask --pretend foobar2`

    These are the packages that I would merge, in order:

    Calculating dependencies ...done!
    [ebuild  N    ] sys-apps/foobar2-1.0  0 kB [1]

    Total size of downloads: 0 kB
    Portage overlays:
     [1] /var/db/repos/localrepo

It does seem to have worked! You\'ll notice the `[1]` next to the \[ebuild\] line. That points to [/var/db/repos/localrepo], which is the overlay created earlier. Now [emerge] the package.

`root `[`#`]`emerge --ask foobar2`

     Calculating dependencies ...done!
    ## (compile info snipped)
    >>> Unpacking foobar2-1.0.tar.bz2 to /var/tmp/portage/foobar2-1.0/work
     * Applying foobar2-1.0-Makefile.patch ...                                    [ ok ]
    ## (compile info snipped)
    >>> Merging sys-apps/foobar2-1.0 to /
    >>> chris +sandbox(preinst)
    --- /usr/
    --- /usr/bin/
    >>> /usr/bin/foobar2

In the first section we see that the emerge started off as it should. The second section shows our patch being applied successfully by the \"\[ ok \]\" status message to the right. The last section tells us the program compiled correctly. The patch works! Now we can go and let the developer know that their patch works fine, and that they can commit the fix to portage.

## [Account removal requests]

Due to the damage deleting an account does to the database, we do not delete accounts that have been used. Instead we offer account anonymization:

1.  The account email is changed to a defined string with a random component.
2.  The account user name is removed.
3.  The password is set to a long random string.
4.  The account is disabled.

We also email the original address on the account confirming that the above actions have been taken.

Upstream Bugzilla documentation strongly discourages deletion of users, because it can cause integrity problems in the underlying database (e.g. if the user in question has already reported a bug or added a comment): [https://bugzilla.readthedocs.io/en/5.0.4/administering/users.html#deleting-users](https://bugzilla.readthedocs.io/en/5.0.4/administering/users.html#deleting-users)

See also the discussion in the upstream bug: [https://bugzilla.mozilla.org/show_bug.cgi?id=392184](https://bugzilla.mozilla.org/show_bug.cgi?id=392184)

## [Acknowledgements]

Special thanks go to moreon for his notes on `-g` flags and compile errors, the people at #gentoo-bugs for helping out with bug-wrangling, Griffon26 for his notes on maintainer-needed, robbat2 for general suggestions and fox2mike for fixing up the doc and adding stuff as needed.

## [See also]

-   [Attach the logs to the bug ticket](https://wiki.gentoo.org/wiki/Attach_the_logs_to_the_bug_ticket "Attach the logs to the bug ticket") --- explains how to **attach log files to a bug ticket**
-   [Bugzilla/Bug report guide](https://wiki.gentoo.org/wiki/Bugzilla/Bug_report_guide "Bugzilla/Bug report guide") --- explains how to report bugs using Gentoo\'s Bugzilla instance, which may be lightly customized to collect specific details for each Gentoo project area
-   [Contributing to Gentoo](https://wiki.gentoo.org/wiki/Contributing_to_Gentoo "Contributing to Gentoo") --- explains how users can **contribute to the development of Gentoo**
-   [Support](https://wiki.gentoo.org/wiki/Support "Support") --- provide **support** for technical issues encountered when installing or using Gentoo Linux
-   [Troubleshooting](https://wiki.gentoo.org/wiki/Troubleshooting "Troubleshooting") --- provide users with a set of techniques and tools to troubleshoot and fix problems with their Gentoo setups.

## [External references]

-   [Gentoo\'s Bugzilla site](https://bugs.gentoo.org/)

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Chris White, Shyam Mani**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*