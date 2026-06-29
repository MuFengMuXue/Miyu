*Not to be confused with [SCP](https://wiki.gentoo.org/wiki/SCP "SCP").*

**Resources**

[[]][Home](http://scap.nist.gov/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Security_Content_Automation_Protocol "wikipedia:Security Content Automation Protocol")

The **Security Content Automation Protocol** is a set of standards and specifications that allow security-conscious actors to document and manage security-related settings (information, checks, vulnerabilities, \...) so that compatible tools can leverage this information.

A well known standard included in SCAP is CVE, the *Common Vulnerabilities and Exposures* system that identifies vulnerabilities in software, hardware and operating systems and is used by many vulnerability reports to link their information with the publicly available information (an example is [CVE-2011-1095](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2011-1095)). However, many other standards are included in SCAP, like XCCDF (to describe security benchmarks) and OVAL (to test security settings).

## Contents

-   [[1] [Standards]](#Standards)
    -   [[1.1] [XCCDF]](#XCCDF)
    -   [[1.2] [OVAL]](#OVAL)
    -   [[1.3] [OCIL]](#OCIL)
    -   [[1.4] [Asset Identification]](#Asset_Identification)
    -   [[1.5] [ARF]](#ARF)
    -   [[1.6] [CCE]](#CCE)
    -   [[1.7] [CPE]](#CPE)
    -   [[1.8] [CVE]](#CVE)
    -   [[1.9] [CVSS]](#CVSS)
    -   [[1.10] [CCSS]](#CCSS)
    -   [[1.11] [TMSAD]](#TMSAD)
-   [[2] [Supporting tools]](#Supporting_tools)
    -   [[2.1] [openscap]](#openscap)
    -   [[2.2] [cvechecker]](#cvechecker)
-   [[3] [External resources]](#External_resources)

## [Standards]

### [XCCDF]

The *Extensible Configuration Checklist Description Format* is an XML-driven language allowing authors to structurally describe (for instance) the setup and configuration of services, systems or tools, as well as connect the guide with OVAL content, supporting automated validation of these settings (does a system comply with the documented settings). Authors have a subset of XHTML available for formatting the content and can generate, from the XCCDF document, a plethora of formats (such as HTML pages, PDF documents, manual pages, \...) for further distribution.

### [OVAL]

The *Open Vulnerability and Assessment Language* is an XML-driven language allowing the description of specific settings. It uses a top-down approach, first describing a *definition* (what is being described), followed by the *tests* (one or more) that are involved with the given description. Each test refers to an *object* (such as a file, or a line within a file, or a kernel parameter, registry key, \...) and a *state* (regular expression, value of a key, permission, mount option, \...) and can optionally use variables to make the content somewhat more flexible.

OVAL documents are used for the automated validation of system states and are often referenced from the XCCDF documents (which describe the state in human-understandable texts).

### [OCIL]

The *Open Checklist Interactive Language* provides a conceptual framework for authors to ask users questions in a structured manner. Authors define questions (and their answer type, such as boolean, integer, string, (multiple)choice, etc.), the set of possible answers and potential actions to be taken depending on the users\' answer (fail the user, ask another (set of) question(s), pass the user).

### [Asset Identification]

In order to uniquely and properly identify / document assets within an organization, the *Asset Identification* standard in SCAP offers an XML-based identification scheme. It relies upon a hierarchical categorization (is the asset an IT asset, an organization or a person, and within the IT assets, is it a computing device, network, software or system) and provides fields for both uniquely identifiable values as well as additional properties related to the asset.

The use of a standardized asset identification scheme is important if you want full automation within the organization, as you will undoubtedly need to refer to particular assets within the tools or documents.

### [ARF]

The *Asset Reporting Format* is an XML-driven language allowing for tools to generate standardized reports about the assets, security state, etc. These standardized reports can then be parsed easily and formatted for further use.

### [CCE]

The *Common Configuration Enumeration* is a Mitre-managed database of settings or states. Combined, they describe which aspects of a system need to be guarded. The CCE entry often does not tell what the proper value is, but rather describes that it needs to be thought of.

For instance:

[CODE] **Example CCE setting**

    <cce cce_id='CCE-4072-5' platform='rhel5' modified='2011-10-07'>
      <description>The autofs service should be enabled or disabled as appropriate.</description>

        enabled / disabled</parameter>
      </parameters>
      <technical_mechanisms>
        <technical_mechanism>via chkconfig</technical_mechanism>
      </technical_mechanisms>
      <references>
        <reference resource_id='NSA "Guide to the Secure Configuration of Red Hat Enterprise Linux 5"'>Section: 2.2.2.3, Value: disabled</reference>
        <reference resource_id='Old "Unix-CCE-DRAFT-2" ID'>CCE-U-203</reference>
      </references>
    </cce>

### [CPE]

The *Common Platform Enumeration* is a string that represents the subject that is targeted by a definition. CPEs currently describe either hardware, software (application) or operation systems, and are used in CVEs to inform SCAP-capable tools when a vulnerability is potentially active. An example CPE entry is `cpe:/o:linux:linux_kernel:3.3.1` (Linux kernel 3.3.1) or `cpe:/a:microsoft:ie:6.00.3718` (Microsoft Internet Explorer version 6, build 3718.

### [CVE]

The *Common Vulnerabilities and Exposures* is a Mitre-managed database holding the description of discovered vulnerabilities. CVEs are then tied to the proper CPEs (identifying the subject that is vulnerable) and sometimes CCEs (identifying particular settings that influence if the vulnerability is exploitable or not).

A CVE number (like [CVE-2011-3170](https://nvd.nist.gov/vuln/detail/CVE-2011-3170)) is a unique identifier describing a particular vulnerability. Most security updates refer to the CVE or CVEs that they fix (including the [Gentoo Linux Security Advisories](https://security.gentoo.org/glsa/)).

### [CVSS]

The *Common Vulnerability Scoring System* tries to provide a way of measuring the severity (and influence) of vulnerabilities. The higher the score, the more severe a vulnerability is found.

### [CCSS]

The *Common Configuration Scoring System* tries to provide a way of measuring the severity (and influence) of configuration settings. The higher the score, the more severe the setting is. Unlike vulnerabilities, which are usually because of coding errors, configuration issues are not resolved by updating the software or platform, but by updating its configuration.

### [TMSAD]

The *Trust Model for Security Automation Data* recommends (and describes) the proper use of digital signatures within SCAP data streams.

## [Supporting tools]

### [openscap]

The **oscap** application (part of [[[app-forensics/openscap]](https://packages.gentoo.org/packages/app-forensics/openscap)[]] is able to read in XCCDF and OVAL file formats and both transform them into readable reports as well as execute OVAL-described tests against a system.

### [cvechecker]

The [cvechecker](https://github.com/sjvermeu/cvechecker) application pulls in CVE data from Mitre and matches this information (of vulnerable software) against a precompiled list of software found on the system, reporting on potential vulnerabilities.

## [External resources]

-   [User-provided benchmarks for Gentoo Linux](https://dev.gentoo.org/~swift/docs/security_benchmarks), usable with [[[app-forensics/openscap]](https://packages.gentoo.org/packages/app-forensics/openscap)[]]