# NAME

ipptool - perform internet printing protocol requests

# SYNOPSIS

**ipptool** \[ **--help** \] \[ **--bearer-token** *BEARER-TOKEN* \] \[ **--client-name** *CLIENT-NAME* \] \[ **--ippfile** *FILENAME* \] \[ **--stop-after-include-error** \] \[ **--user-agent** *USER-AGENT* \] \[ **--version** \] \[ **-4** \] \[ **-6** \] \[ **-c** \] \[ **-C** \] \[ **-d** *NAME=VALUE* \] \[ **-E** \] \[ **-f** *FILENAME* \] \[ **-h** \] \[ **-i** *SECONDS* \] \[ **-I** \] \[ **-j** \] \[ **-L** \] \[ **-n** *REPEAT-COUNT* \] \[ **-P** *FILENAME.plist* \] \[ **-q** \] \[ **-R** \] \[ **-S** \] \[ **-t** \] \[ **-T** *SECONDS* \] \[ **-v** \] \[ **-V** *VERSION* \] \[ **-X** \] *PRINTER-URI* *TESTFILE* \[ ... *TESTFILE* \]

# DESCRIPTION

**ipptool** sends IPP requests to the specified *printer-uri* and tests and/or displays the results. Each named *testfile* defines one or more requests, including the expected response status, attributes, and values. Output is either a plain text, formatted text, CSV, JSON, or XML report on the standard output, with a non-zero exit status indicating that one or more tests have failed. The *testfile* format is described in **ipptoolfile**(5).

# OPTIONS

The following options are recognized by **ipptool:**

**--bearer-token** *BEARER-TOKEN*
Specifies the OAuth 2.0 token to use for HTTP Bearer authentication (RFC 6750).

**--client-name** *CLIENT-NAME*
Specifies the client name to use for the TLS client certificate. If not specified, no client certificate is used during negotiation.

**--help**
Shows program help.

**--ippfile** *FILENAME*
Specifies that the test results should be written to the named IPP file. These files can be used with programs like **ippeveprinter**(1).

**--stop-after-include-error**
Tells **ipptool** to stop if an error occurs in an included file. Normally **ipptool** will continue with subsequent tests after the INCLUDE directive.

**--user-agent** *USER-AGENT*
Specifies the HTTP User-Agent string to use. The default is based on the **UserAgentTokens** value in the **client.conf**(5) file.

**--version**
Shows the version of **ipptool** being used.

**-4**
Specifies that **ipptool** must connect to the printer or server using IPv4.

**-6**
Specifies that **ipptool** must connect to the printer or server using IPv6.

**-c**
Specifies that CSV (comma-separated values) output is desired instead of the plain text output.

**-C**
Specifies that requests should be sent using the HTTP/1.1 "Transfer-Encoding: chunked" header, which is required for conformance by all versions of IPP. The default is to use "Transfer-Encoding: chunked" for requests with attached files and "Content-Length:" for requests without attached files.

**-d*** NAME=VALUE*
Defines the named variable.

**-E**
Forces TLS encryption when connecting to the server using the HTTP "Upgrade" header.

**-f*** FILENAME*
Defines the default request filename for tests.

**-h**
Validate HTTP response headers.

**-i*** SECONDS*
Specifies that the (last) *testfile* should be repeated at the specified interval. This option is incompatible with the **--ippfile** (IPP file output) and *-P* or **-X** (XML plist output) options.

**-I**
Specifies that **ipptool** will continue past errors.

**-j**
Specifies that **ipptool** will produce JSON output.

**-l**
Specifies that plain text output is desired.

**-L**
Specifies that requests should be sent using the HTTP/1.0 "Content-Length:" header, which is required for conformance by all versions of IPP. The default is to use "Transfer-Encoding: chunked" for requests with attached files and "Content-Length:" for requests without attached files.

**-n*** REPEAT-COUNT*
Specifies that the (last) *testfile* should be repeated the specified number of times. This option is incompatible with the *--ippfile* (IPP file output) and *-P* or *-X* (XML plist output) options.

**-P*** FILENAME.plist*
Specifies that the test results should be written to the named XML (Apple plist) file in addition to the regular test report (**-t**). This option is incompatible with the **-i** (interval) and **-n** (repeat-count) options.

**-q**
Be quiet and produce no output.

**-S**
Forces (dedicated) TLS encryption when connecting to the server.

**-t**
Specifies that CUPS test report output is desired instead of the plain text output.

**-T*** SECONDS*
Specifies a timeout for IPP requests in SECONDS.

**-v**
Specifies that all request and response attributes should be output in CUPS test mode (**-t**). This is the default for CSV, JSON, and XML output.

**-V*** VERSION*
Specifies the default IPP version to use: 1.0, 1.1, 2.0, 2.1, or 2.2. If not specified, version 1.1 is used.

**-X**
Specifies that XML (Apple plist) output is desired instead of the plain text report. This option is incompatible with the **-i** (interval) and **-n** (repeat-count) options.

# EXIT STATUS

The **ipptool** program returns 0 if all tests were successful and 1 otherwise.

# FILES

The following standard test files are available:


        cancel-current-job.test           - Cancel the current job
        create-job.test                   - Create a job and send a document
        create-job-sheets.test            - "" with banner
        create-job-timeout.test           - "" with timeout
        create-printer-subscription.test  - Create a printer subscription
        cups-create-local-printer.test    - Create a local print queue
        fax-job.test                      - Fax a file (for fax queues)
        get-completed-jobs.test           - Get a list of completed jobs
        get-job-attributes.test           - Get attributes for a job
        get-job-template-attributes.test  - Get job ticket attributes for a printer
        get-jobs.test                     - Get a list of not-completed jobs
        get-notifications.test            - Get notifications for a subscription
        get-printer-attributes.test       - Get attributes for a printer
        get-printer-attributes-suite.test - Test Get-Printer-Attributes conformance
        get-printers.test                 - Get a list of printers
        get-subscriptions.test            - Get a list of subscriptions
        identify-printer.test             - Identify a printer
        identify-printer-display.test     - Identify a printer via the display
        ipp-1.1.test                      - Run IPP/1.1 conformance tests
        ipp-2.0.test                      - Run IPP/2.0 conformance tests
        ipp-2.1.test                      - Run IPP/2.1 conformance tests
        ipp-2.2.test                      - Run IPP/2.2 conformance tests
        print-job.test                    - Print a file
        print-job-and-wait.test           - Print a file and wait for completion
        print-job-deflate.test            - Print a file with deflate compression
        print-job-gzip.test               - Print a file with gzip compression
        print-job-hold.test               - Print a file and hold
        print-job-letter.test             - Print a file on US Letter media
        print-job-manual.test             - Print a file with manual feed
        print-job-media-col.test          - Print a file using "media-col"
        print-job-media-needed.test       - Print a file and test for "media-needed"
        print-job-password.test           - Print a file with a password/PIN
        print-job-raster.test             - Print a generated raster file
        print-uri.test                    - Print a URI/URL
        set-attrs-hold.test               - Test setting job-hold-until to hold a job
        validate-job.test                 - Validate a job ticket

The following standard document files are available:


        color.jpg                         - A color photo of a flower
        document-a4.pdf                   - A 4-page A4 PDF document
        document-a4.ps                    - A 4-page A4 PostScript document
        document-letter.pdf               - A 4-page US Letter PDF document
        document-letter.ps                - A 4-page US Letter PostScript document
        gray.jpg                          - A grayscale photo of an Alcatraz doorway
        onepage-a4-300-black-1.pwg        - A one page A4 PWG Raster document
        onepage-a4.pdf                    - A one page A4 PDF document
        onepage-a4.ps                     - A one page A4 PostScript document
        onepage-letter-300-black-1.pwg    - A one page US Letter PWG Raster document
        onepage-letter.pdf                - A one page US Letter PDF document
        onepage-letter.ps                 - A one page US Letter PostScript document
        testfile.jpg                      - A color photo collage
        testfile.pcl                      - A HP-PCL homage to "The Shining"
        testfile.pdf                      - A historical CUPS PDF document
        testfile.ps                       - A historical CUPS PostScript document
        testfile.txt                      - A plain text homage to "The Shining"

# CONFORMING TO

The **ipptool** program is unique to CUPS and conforms to the Internet Printing Protocol up to version 2.2.

# EXAMPLES

Get a list of completed jobs for "myprinter":


        ipptool ipp://localhost/printers/myprinter get-completed-jobs.test

Send email notifications to "user@example.com" when "myprinter" changes:


        ipptool -d recipient=mailto:user@example.com \
            ipp://localhost/printers/myprinter create-printer-subscription.test

# SEE ALSO

**client.conf**(5), **ipptoolfile**(5), IANA IPP Registry (https://www.iana.org/assignments/ipp-registrations), PWG Internet Printing Protocol Workgroup (https://www.pwg.org/ipp), RFC 8011 (https://datatracker.ietf.org/doc/html/rfc8011)

# COPYRIGHT

Copyright © 2021-2025 by OpenPrinting.
