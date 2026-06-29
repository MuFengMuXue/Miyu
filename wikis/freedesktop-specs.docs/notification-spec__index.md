## Desktop Notifications Specification

Authors:

Mike Hearn `<mike@navi.cx>`

Christian Hammond `<chipx86@chipx86.com>`

William Jon McCann `<jmccann@redhat.com>`

  

Publication Date: 18 August 2024, Version: Version 1.3

[1 Introduction](index.md#introduction)

[2 Basic Design](basic-design.md)

[3 Backwards Compatibility](backwards-compat.md)

[4 Markup](markup.md)

[5 Icons and Images](icons-and-images.md)

[6 Categories](categories.md)

[7 Urgency Levels](urgency-levels.md)

[8 Hints](hints.md)

[9 D-BUS Protocol](protocol.md)

## 1 Introduction

This is a standard for a desktop notifications service, through which applications can generate passive popups to notify the user in an asynchronous manner of events.

This specification explicitly does not include other types of notification presentation such as modal message boxes, window manager decorations or window list annotations.

Example use cases include:

- Messages from chat programs

- Scheduled alarm

- Completed file transfer

- New mail notification

- Low disk space/battery warnings
