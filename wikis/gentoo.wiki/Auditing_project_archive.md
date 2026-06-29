**[] Archived article**\
\

This article is **archived (obsolete)**. Contents are surely incorrect for current usage, and are intended for historical reference only.

\
TLDR: **Do not use this article!**

\
The Gentoo security audit project was focused upon auditing packages for security issues. The aim of the project was to audit many of available the stable packages in the Gentoo ebuild repository for potential flaws.

## Contents

-   [[1] [Auditing methodology]](#Auditing_methodology)
    -   [[1.1] [Scope]](#Scope)
    -   [[1.2] [Tools]](#Tools)
    -   [[1.3] [Submitting found flaws]](#Submitting_found_flaws)

## [Auditing methodology]

### [Scope]

Due to the sheer size of ::gentoo, it is infeasible for this project to be able to audit all the packages. The system of prioritizing is based on the time, risk factor, motivation and skills necessary to audit a given package.

### [Tools]

There are several packages available which are designed to aid source code audits. Some of the these include:

-   [[[dev-util/flawfinder]](https://packages.gentoo.org/packages/dev-util/flawfinder)[]]
-   [[[dev-util/rats]](https://packages.gentoo.org/packages/dev-util/rats)[]]
-   [[[dev-util/pscan]](https://packages.gentoo.org/packages/dev-util/pscan)[]]
-   [[[app-forensics/examiner]](https://packages.gentoo.org/packages/app-forensics/examiner)[]]
-   [[[dev-util/splint]](https://packages.gentoo.org/packages/dev-util/splint)[]]

Each of the general scanning tools will include output describing the flaw detected, and possibly giving advice on how the code can be fixed. For example the following is taken from the output of RATS describing the dangers of getenv: *\"Environment variables are highly untrustable input. They may be of any length, and contain any data. Do not make any assumptions regarding content or length. If at all possible avoid using them, and if it is necessary, sanitize them and truncate them to a reasonable length.\"*

For further advice on how to correct a hole which has been reported you should study a book on programming securely, such as the [Secure Programming for Linux and Unix HOWTO](http://www.dwheeler.com/secure-programs/) by David A. Wheeler or the [C Secure Coding Standard](https://www.securecoding.cert.org/confluence/display/seccode/CERT+C+Coding+Standard) by CERT. Remember: when reporting security issues a patch closing the hole is greatly appreciated.

### [Submitting found flaws]

When you find a vulnerability, you should write a vulnerability description and submit it for peer-review as a new security bug (with \"Gentoo Security\" as product and \"Auditing\" as component, restricted to Gentoo Security). Other auditors (and security team members) will double-check what you found, ensure that it is indeed a bug with a security impact.

When it has been thoroughly peer-reviewed, it will be cleared to go upstream as a \"Gentoo Security Audit Subproject\" sighting. Depending on its severity and how the package is common amongst distributions, it might need to be coordinated with vendor-sec for coordinated release and CVE number attribution.

** Important**\
Please do not submit non-peer-reviewed vulnerabilities to any disclosure channel (including upstream) under the Gentoo name or a gentoo.org email address. Nothing hurts more our credibility than issuing Gentoo-branded bogus vulnerability reports.