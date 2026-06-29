# DNSSEC

From the DNSSEC Wikipedia article:
:The Domain Name System Security Extensions (DNSSEC) is a suite of Internet Engineering Task Force (IETF) specifications for securing certain kinds of information provided by the Domain Name System (DNS) as used on Internet Protocol (IP) networks. It is a set of extensions to DNS which provide to DNS clients (resolvers) origin authentication of DNS data, authenticated denial of existence, and data integrity, but not availability or confidentiality.

## Install a DNSSEC-validating resolver
To ensure DNSSEC is validated system-wide, setup a local DNS server that validates DNSSEC records and configure  to use it so that all DNS lookups go through it. See Domain name resolution#DNS servers for available validating resolvers. Note that some DNS servers require specific options to enable DNSSEC validation.

If you attempt to visit a site with a bogus (spoofed) IP address, the validating resolver will prevent you from receiving the invalid DNS data and your browser (or other application) will be told there is no such host. Since all DNS lookups go through the validating resolver, you do not need software that has DNSSEC support built-in when using this option.

## Test the local validating resolver
## From a terminal
To test if your local resolver properly validates DNSSEC, use a DNS lookup utility that supports setting the  ("DNSSEC OK") bit, such as .

Test if the resolver does not return an answer for a domain with an invalid signature such as badsig.test.dnscheck.tools, rhybar.cz or dnssec-failed.org:

The query should return successfully and contain the  (authenticated data) flag.

## From a web browser
Multiple websites provide tests that check if your DNS resolver validates DNSSEC:

* http://www.dnssec-or-not.com/
* https://dnscheck.tools/
* https://wander.science/projects/dns/dnssec-resolver-test/
* https://internet.nl/connection/

## Recursive query with DNSSEC validation
To validate DNSSEC for a domain without involving a recursive resolver, use a DNS lookup utility that can trace a domain starting from a the DNS root. E.g.  (from ) or  (from ).

With drill, use the  option to set the  (DNSSEC OK) bit and the  option to trace from the root name servers down to the domain being resolved:

 $ drill -DT example.com

Replace  with a domain name for which you want to preform DNSSEC validation.

For a domain with an invalid DNSSEC signature, the result should end with the following lines:

For a domain with a trusted signature, the result should end with the following lines:
