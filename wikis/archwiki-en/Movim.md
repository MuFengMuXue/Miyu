# Movim

Movim is a browser based XMPP client. Movim is designed to be easy to use, quick to get started using their publically hosted instance. Movim aims to be a powerful replacement to social media by providing blogging features, as well as being an XMPP client.

Movim is Free and Open Source Software licensed under AGPL3.

## Installation
Install the  package.

## Public instances
Mov.im - Officially hosted instance of movim provided by the movim developers.

## Configuration
Since 0.20, all configuration is done through .

## Reverse proxy
Movim's development team has an amazing guide on setting up a reverse proxy for movim, please see The guide supports the following web servers:

*
*
*

## Known issues
## Images are not OMEMO encrypted
Movim does not currently support encryption of HTTP uploads, thus images and other media posted will not be encrypted using OMEMO. This is not to say that they are still not secure, as TLS encryption will still be in use. This feature is being worked on but has no tracking issue to follow its progression.

## Troubleshooting
## Messages are "gibberish"
If the message is red, and it seems to make no apparent sense, like a cat has been walking over your friends keyboard, this is due to them using OMEMO encryption (end to end encryption), the message was not encrypted for your client and thus you are unable to decrypt it. To fix this, movim does key exchange when OMEMO is enabled, so enabling OMEMO encryption and then sending your friend a message such as "could not decrypt your messages, please send them again" should solve this issue.

As a warning, movim does have issues with OMEMO encryption due to the complexity of the XEP, it is being constantly improved. If you find a bug, do not hesitate to report it on movim's [https://github.com/movim/movim/issues Issue Tracker.

## Cannot enable OMEMO encryption
In order to enable OMEMO encryption, you must have your friend added as a contact, and visa versa, once this has been achieved a lock icon at the end of the message input box should appear, click this to enable OMEMO encryption.
