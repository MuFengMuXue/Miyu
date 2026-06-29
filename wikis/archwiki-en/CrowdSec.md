# CrowdSec

CrowdSec is an open-source and lightweight software that allows you to detect peers with malevolent behaviors and block them from accessing your systems at various levels (infrastructural, system, applicative).
CrowdSec bouncers are standalone software pieces in charge of acting upon a decision taken by crowdsec : block an IP, present a captcha, enforce MFA on a given user, etc.

## Installation
Install the  packages, and CrowdSec firewall bouncer .

Enable/start

## Usage
Enroll your CrowdSec instance to Crowdsec console:

 # cscli  console enroll your_enroll_key

You can get your key from upstream.

## Hub management
Lists installed parsers, scenarios and collections:

 # cscli hub list

Parsers parse string from logs or previous parsers. To install  parser:

 # cscli parsers install crowdsecurity/sshd-logs

Scenarios receive events and can detect attacks and produce alerts. Install  scenario:

 # cscli scenarios install crowdsecurity/ssh-slow-bf

Collections are bundle of parsers, scenarios, postoverflows. Install  collection:

 # cscli collections install crowdsecurity/whitelist-good-actors

Update installed parsers, scenarios and collections:

 # cscli hub update
 # cscli hub upgrade

## Decisions management
List active decisions:

 # cscli decisions list

Manually add a decision (ban):

 # cscli decisions add --ip 1.2.3.4 --duration 24h --reason "web bruteforce"

Remove a decision:

 # cscli decisions delete --ip 1.2.3.4

List past alerts:

 # cscli alerts list --since 1h

Alerts will include expired or deleted decisions.
