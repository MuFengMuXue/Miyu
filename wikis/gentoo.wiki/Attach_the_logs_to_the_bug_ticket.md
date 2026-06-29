This article explains how to **attach log files to a bug ticket**.

Bugs may be reported using the online form at [https://bugs.gentoo.org/](https://bugs.gentoo.org/) with log files uploaded via this form, or with [[[www-client/pybugz]](https://packages.gentoo.org/packages/www-client/pybugz)[]] which allows [attaching log files](https://wiki.gentoo.org/wiki/Pybugz "Pybugz") using the [bugz] utility on the command line.

## Contents

-   [[1] [Including system information and emerge logs]](#Including_system_information_and_emerge_logs)
    -   [[1.1] [Compressing log files]](#Compressing_log_files)
-   [[2] [FAQ]](#FAQ)
-   [[3] [See also]](#See_also)

## [Including system information and emerge logs]

[![](/images/thumb/2/21/Bugzilla_screenshot_summary-keyword.png/300px-Bugzilla_screenshot_summary-keyword.png)](https://wiki.gentoo.org/wiki/File:Bugzilla_screenshot_summary-keyword.png)

[](https://wiki.gentoo.org/wiki/File:Bugzilla_screenshot_summary-keyword.png "Enlarge")

Use the **Add an attachment** button below the description text box in order to attach files in Bugzilla.

[![](/images/thumb/c/c6/Bugzilla_attachments_buildlog.png/300px-Bugzilla_attachments_buildlog.png)](https://wiki.gentoo.org/wiki/File:Bugzilla_attachments_buildlog.png)

[](https://wiki.gentoo.org/wiki/File:Bugzilla_attachments_buildlog.png "Enlarge")

Developpers can see immediately that the required log is provided. The attachments are easy to access and do not clutter the comment fields.

Please include information that can be helpful to developers when filing bugs:

-   **Paste** *into the comment box* the output of:

    :::: cmd-box


    `user `[`$`]`emerge --info <category/packagename>`


    ::::
-   **Attach** the log file from [/var/tmp/portage/\<category\>/\/temp/build.log] (adjust path if `PORTAGE_TMPDIR` is set in [make.conf](https://wiki.gentoo.org/wiki/Make.conf "Make.conf")).

\
There may be no log file in [/var/tmp/portage/\<category\>/\/temp/] after the emerge, as by default this is deleted upon successful completion. If no log file persists after the emerge, force [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") to [conserve the logs](https://wiki.gentoo.org/wiki/Portage_log#Build_logs "Portage log") before running the previous command, and include the file from [/var/log/portage/] instead (adjust path if personalized configuration is used).

Remember to change the configuration back if it is not desirable to always retain build logs, or at least turn on `clean-logs` in the `FEATURES` variable, or regularly clean them out: these logs can take up some space, over time.

If [build.log] is large, [compress it](#Compressing_log_files) before uploading.

When submitting a bug report, please:

-   Do **not paste files into comments**, because the ticket gets difficult to read. Developers often use tools to handle attachments.
-   Do **not upload files to pastebins**. It is often important to read about a bug some years later. Links to external pages are not archived by Gentoo and the information is lost. Some developers use tools to work on bugs and cannot open external websites easily.

### [Compressing log files]

**Compress** large log files before uploading:

`user `[`$`]`xz -9 `[`/var/tmp/portage/<category>//temp/build.log`]

Attachments are limited to 1 MB per file. Ask developers how to proceed if the compressed file is larger.

## [FAQ]

**Q:** I think the [build.log] file or the [emerge \--info] output for my bug will not be needed. It takes me additional 30 seconds to add it! *Why should I add this information?*

**A:** It may *seem* that the requested information might not be relevant to some situations, but it really is almost always invaluable. Developers have limited resources and need to work efficiently; providing all context when first reporting a bug often saves quite some unnecessary effort.

Between 2018-01-01 and 2018-12-31 Gentoo received and assigned **15,640 bugs**. Just to triage this number of bugs is quite some work: each ticket has to be read by at least one person who tries to figure out exactly what the ticket is about and which developers can help to resolve it. These developers then read the ticket themselves, and start trying to determine what the issue is exactly. If information is missing they won\'t even be able to start towards a solution, and will have to send a message to the person who reported the bug, then wait for an answer. Sometimes the wait is long, all too often several weeks or more! Many submitters never even reply, in which case all the time spent triaging, and trying to understand the bug without all the relevant information, is wasted! ***If*** required information gets added later, the developers have to go through the whole process a second time. Multiply this waste for hundreds of incomplete bugs, and it should be clear that it can be quite a drain.

The person checking and assigning a ticket to developers probably does not know the specific package, but nevertheless has to ensure that the report is complete - so as not waste developer\'s time. If logs are not included, bugs can lay in limbo, not being assigned to developers - and this even if, in fine, the logs actually weren\'t totally necessary.

***Please take the time to write a well prepared report***, this really does help developers not waste their limited resources on process and on chasing down the information needed to understand bugs properly. It will also ensure the fastest possible response and eventual solution to bugs.

\
**Q:** But I am 100% sure, that [build.log] file and the [emerge \--info] is not needed.

**A:** I know your feeling. Even the author of these lines hit the trap recently. I was so sure and during debugging we found out that the bug was not obvious but hidden and could only be found with the log files. Note to me and you: \"mind the logs\" ;-)

\
**Q:** Why shouldn\'t I just copy and paste the snippets of my log which I found important?

**A:** Because the people who assign tickets don\'t know if it is sufficient for the maintainer, and it takes much longer to check. It is more productive if all tickets have the same structure.

**Q:** Why should I attach the [build.log] file, if there is an error at runtime, but no error during compilation?

**A:** Because there is often additional information in the log. Some warnings during compile time are precursors for problems at runtime.

## [See also]

-   [Bugzilla/Guide](https://wiki.gentoo.org/wiki/Bugzilla/Guide "Bugzilla/Guide") --- covers the recommended method of forensically reporting *specific details* of bugs within Gentoo.
-   [Bugzilla/Bug report guide](https://wiki.gentoo.org/wiki/Bugzilla/Bug_report_guide "Bugzilla/Bug report guide") --- explains how to report bugs using Gentoo\'s Bugzilla instance, which may be lightly customized to collect specific details for each Gentoo project area
-   [Support](https://wiki.gentoo.org/wiki/Support "Support") --- provide **support** for technical issues encountered when installing or using Gentoo Linux
-   [Troubleshooting](https://wiki.gentoo.org/wiki/Troubleshooting "Troubleshooting") --- provide users with a set of techniques and tools to troubleshoot and fix problems with their Gentoo setups.