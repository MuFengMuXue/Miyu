## 10 Registering MIME Types

The `MimeType` key is used to indicate the MIME Types that an application knows how to handle. It is expected that for some applications this list could become long. An application is expected to be able to reasonably open files of these types using the command listed in the `Exec` key.

There should be no priority for MIME Types in this field, or any form of priority in the desktop file. Priority for applications is handled external to the `.desktop` files.
