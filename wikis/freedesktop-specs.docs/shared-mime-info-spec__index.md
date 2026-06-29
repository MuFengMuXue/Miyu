## Shared MIME-info Database

Authors:

`<>`

Thomas Leonard `<tal197 at users.sf.net>`

  

Publication Date: 2 October 2018

[1 Introduction](index.md#id-1.2)

[2 Unified system](ar01s02.md)

[3 Contributors](ar01s03.md)

[References](bi01.md)

## 1 Introduction

### 1.1 Version

This is version 0.21 of the Shared MIME-info Database specification, last updated 2 October 2018.

### 1.2 What is this spec?

Many programs and desktops use the MIME system\[MIME\] to represent the types of files. Frequently, it is necessary to work out the correct MIME type for a file. This is generally done by examining the file's name or contents, and looking up the correct MIME type in a database.

It is also useful to store information about each type, such as a textual description of it, or a list of applications that can be used to view or edit files of that type.

For interoperability, it is useful for different programs to use the same database so that different programs agree on the type of a file and information is not duplicated. It is also helpful for application authors to only have to install new information in one place.

This specification attempts to unify the MIME database systems currently in use by GNOME\[[GNOME](bi01.md#id-1.5.2)\], KDE\[[KDE](bi01.md#id-1.5.3)\] and ROX\[[ROX](bi01.md#id-1.5.4)\], and provide room for future extensibility.

The MIME database does NOT store user preferences (such as a user's preferred application for handling files of a particular type). It may be used to store static information, such as that files of a certain type may be viewed with a particular application.

### 1.3 Language used in this specification

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119\[[RFC-2119](bi01.md#id-1.5.7)\].
