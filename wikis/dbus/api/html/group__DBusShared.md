Shared constants

D-Bus low-level public API

Shared header included by both libdbus and C/C++ bindings such as the GLib bindings. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="macros" class="groupheader"> Macros</h2></td>
</tr>
<tr id="r_ga9e017e829e575bdc5c554fd4d07d7355" class="memitem:ga9e017e829e575bdc5c554fd4d07d7355">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_SERVICE_DBUS   "org.freedesktop.DBus"</td>
</tr>
<tr class="memdesc:ga9e017e829e575bdc5c554fd4d07d7355">
<td class="mdescLeft"> </td>
<td class="mdescRight">The bus name used to talk to the bus itself.<br />
</td>
</tr>
<tr class="separator:ga9e017e829e575bdc5c554fd4d07d7355">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga840a593b8fa139c69ef679830f42d91f" class="memitem:ga840a593b8fa139c69ef679830f42d91f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_PATH_DBUS   "/org/freedesktop/DBus"</td>
</tr>
<tr class="memdesc:ga840a593b8fa139c69ef679830f42d91f">
<td class="mdescLeft"> </td>
<td class="mdescRight">The object path used to talk to the bus itself.<br />
</td>
</tr>
<tr class="separator:ga840a593b8fa139c69ef679830f42d91f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga850990a54a46142ee7c5f8174cc932c1" class="memitem:ga850990a54a46142ee7c5f8174cc932c1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_PATH_LOCAL   "/org/freedesktop/DBus/Local"</td>
</tr>
<tr class="memdesc:ga850990a54a46142ee7c5f8174cc932c1">
<td class="mdescLeft"> </td>
<td class="mdescRight">The object path used in local/in-process-generated messages.<br />
</td>
</tr>
<tr class="separator:ga850990a54a46142ee7c5f8174cc932c1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa34514374bb61b8222a670a3d0b3fdc4" class="memitem:gaa34514374bb61b8222a670a3d0b3fdc4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_INTERFACE_DBUS   "org.freedesktop.DBus"</td>
</tr>
<tr class="memdesc:gaa34514374bb61b8222a670a3d0b3fdc4">
<td class="mdescLeft"> </td>
<td class="mdescRight">The interface exported by the object with DBUS_SERVICE_DBUS and DBUS_PATH_DBUS.<br />
</td>
</tr>
<tr class="separator:gaa34514374bb61b8222a670a3d0b3fdc4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga77eb6e2c74e146f9d6b20b1ceaf4a472" class="memitem:ga77eb6e2c74e146f9d6b20b1ceaf4a472">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_INTERFACE_MONITORING   "org.freedesktop.DBus.Monitoring"</td>
</tr>
<tr class="memdesc:ga77eb6e2c74e146f9d6b20b1ceaf4a472">
<td class="mdescLeft"> </td>
<td class="mdescRight">The monitoring interface exported by the dbus-daemon.<br />
</td>
</tr>
<tr class="separator:ga77eb6e2c74e146f9d6b20b1ceaf4a472">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga70ede9ee1e2c5f6c15100f59cbbb19ef" class="memitem:ga70ede9ee1e2c5f6c15100f59cbbb19ef">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_INTERFACE_VERBOSE   "org.freedesktop.DBus.Verbose"</td>
</tr>
<tr class="memdesc:ga70ede9ee1e2c5f6c15100f59cbbb19ef">
<td class="mdescLeft"> </td>
<td class="mdescRight">The verbose interface exported by the dbus-daemon.<br />
</td>
</tr>
<tr class="separator:ga70ede9ee1e2c5f6c15100f59cbbb19ef">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gafe8861886c0b53c1000fb322fd84641b" class="memitem:gafe8861886c0b53c1000fb322fd84641b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_INTERFACE_INTROSPECTABLE   "org.freedesktop.DBus.Introspectable"</td>
</tr>
<tr class="memdesc:gafe8861886c0b53c1000fb322fd84641b">
<td class="mdescLeft"> </td>
<td class="mdescRight">The interface supported by introspectable objects.<br />
</td>
</tr>
<tr class="separator:gafe8861886c0b53c1000fb322fd84641b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae93739fa4bb948d87d61d6659938e325" class="memitem:gae93739fa4bb948d87d61d6659938e325">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_INTERFACE_PROPERTIES   "org.freedesktop.DBus.Properties"</td>
</tr>
<tr class="memdesc:gae93739fa4bb948d87d61d6659938e325">
<td class="mdescLeft"> </td>
<td class="mdescRight">The interface supported by objects with properties.<br />
</td>
</tr>
<tr class="separator:gae93739fa4bb948d87d61d6659938e325">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaacbd4e8ccdef18c75edd0785fbcc70ef" class="memitem:gaacbd4e8ccdef18c75edd0785fbcc70ef">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_INTERFACE_PEER   "org.freedesktop.DBus.Peer"</td>
</tr>
<tr class="memdesc:gaacbd4e8ccdef18c75edd0785fbcc70ef">
<td class="mdescLeft"> </td>
<td class="mdescRight">The interface supported by most dbus peers.<br />
</td>
</tr>
<tr class="separator:gaacbd4e8ccdef18c75edd0785fbcc70ef">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9ef6478aae637449ec0c5de1679f75ce" class="memitem:ga9ef6478aae637449ec0c5de1679f75ce">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_INTERFACE_LOCAL   "org.freedesktop.DBus.Local"</td>
</tr>
<tr class="memdesc:ga9ef6478aae637449ec0c5de1679f75ce">
<td class="mdescLeft"> </td>
<td class="mdescRight">This is a special interface whose methods can only be invoked by the local implementation (messages from remote apps aren't allowed to specify this interface).<br />
</td>
</tr>
<tr class="separator:ga9ef6478aae637449ec0c5de1679f75ce">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga40b7a263caf8d6e39b39a8c7350a084f" class="memitem:ga40b7a263caf8d6e39b39a8c7350a084f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_NAME_FLAG_ALLOW_REPLACEMENT   0x1</td>
</tr>
<tr class="memdesc:ga40b7a263caf8d6e39b39a8c7350a084f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Allow another service to become the primary owner if requested.<br />
</td>
</tr>
<tr class="separator:ga40b7a263caf8d6e39b39a8c7350a084f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0f16ed23be47eb22a37a227a6e39597b" class="memitem:ga0f16ed23be47eb22a37a227a6e39597b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_NAME_FLAG_REPLACE_EXISTING   0x2</td>
</tr>
<tr class="memdesc:ga0f16ed23be47eb22a37a227a6e39597b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Request to replace the current primary owner.<br />
</td>
</tr>
<tr class="separator:ga0f16ed23be47eb22a37a227a6e39597b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3c18c35e4c2dfbe9a0a5be47f4b4b6e9" class="memitem:ga3c18c35e4c2dfbe9a0a5be47f4b4b6e9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_NAME_FLAG_DO_NOT_QUEUE   0x4</td>
</tr>
<tr class="memdesc:ga3c18c35e4c2dfbe9a0a5be47f4b4b6e9">
<td class="mdescLeft"> </td>
<td class="mdescRight">If we can not become the primary owner do not place us in the queue.<br />
</td>
</tr>
<tr class="separator:ga3c18c35e4c2dfbe9a0a5be47f4b4b6e9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga37a9bc7c6eb11d212bf8d5e5ff3b50f9" class="memitem:ga37a9bc7c6eb11d212bf8d5e5ff3b50f9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_REQUEST_NAME_REPLY_PRIMARY_OWNER   1</td>
</tr>
<tr class="memdesc:ga37a9bc7c6eb11d212bf8d5e5ff3b50f9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Service has become the primary owner of the requested name.<br />
</td>
</tr>
<tr class="separator:ga37a9bc7c6eb11d212bf8d5e5ff3b50f9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaee62d7003ea4ed8c1957e9a072c7b16a" class="memitem:gaee62d7003ea4ed8c1957e9a072c7b16a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_REQUEST_NAME_REPLY_IN_QUEUE   2</td>
</tr>
<tr class="memdesc:gaee62d7003ea4ed8c1957e9a072c7b16a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Service could not become the primary owner and has been placed in the queue.<br />
</td>
</tr>
<tr class="separator:gaee62d7003ea4ed8c1957e9a072c7b16a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac5e749f4dfcc3adcdb714ece3c1be1c7" class="memitem:gac5e749f4dfcc3adcdb714ece3c1be1c7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_REQUEST_NAME_REPLY_EXISTS   3</td>
</tr>
<tr class="memdesc:gac5e749f4dfcc3adcdb714ece3c1be1c7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Service is already in the queue.<br />
</td>
</tr>
<tr class="separator:gac5e749f4dfcc3adcdb714ece3c1be1c7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaefd5513d0d448f6c106202ebde26f969" class="memitem:gaefd5513d0d448f6c106202ebde26f969">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_REQUEST_NAME_REPLY_ALREADY_OWNER   4</td>
</tr>
<tr class="memdesc:gaefd5513d0d448f6c106202ebde26f969">
<td class="mdescLeft"> </td>
<td class="mdescRight">Service is already the primary owner.<br />
</td>
</tr>
<tr class="separator:gaefd5513d0d448f6c106202ebde26f969">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf51666b3db57bfc94f0fef7604ba35e2" class="memitem:gaf51666b3db57bfc94f0fef7604ba35e2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_RELEASE_NAME_REPLY_RELEASED   1</td>
</tr>
<tr class="memdesc:gaf51666b3db57bfc94f0fef7604ba35e2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Service was released from the given name.<br />
</td>
</tr>
<tr class="separator:gaf51666b3db57bfc94f0fef7604ba35e2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2aebb664a3c1ea2c08740139f44c386a" class="memitem:ga2aebb664a3c1ea2c08740139f44c386a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_RELEASE_NAME_REPLY_NON_EXISTENT   2</td>
</tr>
<tr class="memdesc:ga2aebb664a3c1ea2c08740139f44c386a">
<td class="mdescLeft"> </td>
<td class="mdescRight">The given name does not exist on the bus.<br />
</td>
</tr>
<tr class="separator:ga2aebb664a3c1ea2c08740139f44c386a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga994df340fa233202857ea9358b935aac" class="memitem:ga994df340fa233202857ea9358b935aac">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_RELEASE_NAME_REPLY_NOT_OWNER   3</td>
</tr>
<tr class="memdesc:ga994df340fa233202857ea9358b935aac">
<td class="mdescLeft"> </td>
<td class="mdescRight">Service is not an owner of the given name.<br />
</td>
</tr>
<tr class="separator:ga994df340fa233202857ea9358b935aac">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga375114145e2eb43473fb778cc603f08b" class="memitem:ga375114145e2eb43473fb778cc603f08b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_START_REPLY_SUCCESS   1</td>
</tr>
<tr class="memdesc:ga375114145e2eb43473fb778cc603f08b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Service was auto started.<br />
</td>
</tr>
<tr class="separator:ga375114145e2eb43473fb778cc603f08b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad6de6047e398631e590cdae679f044c5" class="memitem:gad6de6047e398631e590cdae679f044c5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_START_REPLY_ALREADY_RUNNING   2</td>
</tr>
<tr class="memdesc:gad6de6047e398631e590cdae679f044c5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Service was already running.<br />
</td>
</tr>
<tr class="separator:gad6de6047e398631e590cdae679f044c5">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="enumerations" class="groupheader"> Enumerations</h2></td>
</tr>
<tr id="r_ga980320deb96476bee7555edcdebc3528" class="memitem:ga980320deb96476bee7555edcdebc3528">
<td class="memItemLeft" style="text-align: right;" data-valign="top">enum  </td>
<td class="memItemRight" data-valign="bottom">DBusBusType { DBUS_BUS_SESSION , DBUS_BUS_SYSTEM , DBUS_BUS_STARTER }</td>
</tr>
<tr class="memdesc:ga980320deb96476bee7555edcdebc3528">
<td class="mdescLeft"> </td>
<td class="mdescRight">Well-known bus types. More...<br />
</td>
</tr>
<tr class="separator:ga980320deb96476bee7555edcdebc3528">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8244b29230187624c24986c24edab1de" class="memitem:ga8244b29230187624c24986c24edab1de">
<td class="memItemLeft" style="text-align: right;" data-valign="top">enum  </td>
<td class="memItemRight" data-valign="bottom">DBusHandlerResult { DBUS_HANDLER_RESULT_HANDLED , DBUS_HANDLER_RESULT_NOT_YET_HANDLED , DBUS_HANDLER_RESULT_NEED_MEMORY }</td>
</tr>
<tr class="memdesc:ga8244b29230187624c24986c24edab1de">
<td class="mdescLeft"> </td>
<td class="mdescRight">Results that a message handler can return. More...<br />
</td>
</tr>
<tr class="separator:ga8244b29230187624c24986c24edab1de">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Shared header included by both libdbus and C/C++ bindings such as the GLib bindings.

Usually a C/C++ binding such as the GLib or Qt binding won't want to include dbus.h in its public headers. However, a few constants and macros may be useful to include; those are found here and in dbus-protocol.h

## Macro Definition Documentation

## ◆ DBUS_INTERFACE_DBUS

|                                                       |
|-------------------------------------------------------|
| \#define DBUS_INTERFACE_DBUS   "org.freedesktop.DBus" |

The interface exported by the object with DBUS_SERVICE_DBUS and DBUS_PATH_DBUS.

Definition at line 90 of file dbus-shared.h.

## ◆ DBUS_INTERFACE_INTROSPECTABLE

|  |
|----|
| \#define DBUS_INTERFACE_INTROSPECTABLE   "org.freedesktop.DBus.Introspectable" |

The interface supported by introspectable objects.

Definition at line 97 of file dbus-shared.h.

## ◆ DBUS_INTERFACE_LOCAL

|                                                              |
|--------------------------------------------------------------|
| \#define DBUS_INTERFACE_LOCAL   "org.freedesktop.DBus.Local" |

This is a special interface whose methods can only be invoked by the local implementation (messages from remote apps aren't allowed to specify this interface).

Definition at line 107 of file dbus-shared.h.

## ◆ DBUS_INTERFACE_MONITORING

|                                                                        |
|------------------------------------------------------------------------|
| \#define DBUS_INTERFACE_MONITORING   "org.freedesktop.DBus.Monitoring" |

The monitoring interface exported by the dbus-daemon.

Definition at line 92 of file dbus-shared.h.

## ◆ DBUS_INTERFACE_PEER

|                                                            |
|------------------------------------------------------------|
| \#define DBUS_INTERFACE_PEER   "org.freedesktop.DBus.Peer" |

The interface supported by most dbus peers.

Definition at line 101 of file dbus-shared.h.

## ◆ DBUS_INTERFACE_PROPERTIES

|                                                                        |
|------------------------------------------------------------------------|
| \#define DBUS_INTERFACE_PROPERTIES   "org.freedesktop.DBus.Properties" |

The interface supported by objects with properties.

Definition at line 99 of file dbus-shared.h.

## ◆ DBUS_INTERFACE_VERBOSE

|                                                                  |
|------------------------------------------------------------------|
| \#define DBUS_INTERFACE_VERBOSE   "org.freedesktop.DBus.Verbose" |

The verbose interface exported by the dbus-daemon.

Definition at line 95 of file dbus-shared.h.

## ◆ DBUS_NAME_FLAG_ALLOW_REPLACEMENT

|                                                 |
|-------------------------------------------------|
| \#define DBUS_NAME_FLAG_ALLOW_REPLACEMENT   0x1 |

Allow another service to become the primary owner if requested.

Definition at line 110 of file dbus-shared.h.

## ◆ DBUS_NAME_FLAG_DO_NOT_QUEUE

|                                            |
|--------------------------------------------|
| \#define DBUS_NAME_FLAG_DO_NOT_QUEUE   0x4 |

If we can not become the primary owner do not place us in the queue.

Definition at line 112 of file dbus-shared.h.

## ◆ DBUS_NAME_FLAG_REPLACE_EXISTING

|                                                |
|------------------------------------------------|
| \#define DBUS_NAME_FLAG_REPLACE_EXISTING   0x2 |

Request to replace the current primary owner.

Definition at line 111 of file dbus-shared.h.

## ◆ DBUS_PATH_DBUS

|                                                   |
|---------------------------------------------------|
| \#define DBUS_PATH_DBUS   "/org/freedesktop/DBus" |

The object path used to talk to the bus itself.

Definition at line 82 of file dbus-shared.h.

## ◆ DBUS_PATH_LOCAL

|                                                          |
|----------------------------------------------------------|
| \#define DBUS_PATH_LOCAL   "/org/freedesktop/DBus/Local" |

The object path used in local/in-process-generated messages.

Definition at line 84 of file dbus-shared.h.

## ◆ DBUS_RELEASE_NAME_REPLY_NON_EXISTENT

|                                                   |
|---------------------------------------------------|
| \#define DBUS_RELEASE_NAME_REPLY_NON_EXISTENT   2 |

The given name does not exist on the bus.

Definition at line 122 of file dbus-shared.h.

## ◆ DBUS_RELEASE_NAME_REPLY_NOT_OWNER

|                                                |
|------------------------------------------------|
| \#define DBUS_RELEASE_NAME_REPLY_NOT_OWNER   3 |

Service is not an owner of the given name.

Definition at line 123 of file dbus-shared.h.

## ◆ DBUS_RELEASE_NAME_REPLY_RELEASED

|                                               |
|-----------------------------------------------|
| \#define DBUS_RELEASE_NAME_REPLY_RELEASED   1 |

Service was released from the given name.

Definition at line 121 of file dbus-shared.h.

## ◆ DBUS_REQUEST_NAME_REPLY_ALREADY_OWNER

|                                                    |
|----------------------------------------------------|
| \#define DBUS_REQUEST_NAME_REPLY_ALREADY_OWNER   4 |

Service is already the primary owner.

Definition at line 118 of file dbus-shared.h.

## ◆ DBUS_REQUEST_NAME_REPLY_EXISTS

|                                             |
|---------------------------------------------|
| \#define DBUS_REQUEST_NAME_REPLY_EXISTS   3 |

Service is already in the queue.

Definition at line 117 of file dbus-shared.h.

## ◆ DBUS_REQUEST_NAME_REPLY_IN_QUEUE

|                                               |
|-----------------------------------------------|
| \#define DBUS_REQUEST_NAME_REPLY_IN_QUEUE   2 |

Service could not become the primary owner and has been placed in the queue.

Definition at line 116 of file dbus-shared.h.

## ◆ DBUS_REQUEST_NAME_REPLY_PRIMARY_OWNER

|                                                    |
|----------------------------------------------------|
| \#define DBUS_REQUEST_NAME_REPLY_PRIMARY_OWNER   1 |

Service has become the primary owner of the requested name.

Definition at line 115 of file dbus-shared.h.

## ◆ DBUS_SERVICE_DBUS

|                                                     |
|-----------------------------------------------------|
| \#define DBUS_SERVICE_DBUS   "org.freedesktop.DBus" |

The bus name used to talk to the bus itself.

Definition at line 78 of file dbus-shared.h.

## ◆ DBUS_START_REPLY_ALREADY_RUNNING

|                                               |
|-----------------------------------------------|
| \#define DBUS_START_REPLY_ALREADY_RUNNING   2 |

Service was already running.

Definition at line 127 of file dbus-shared.h.

## ◆ DBUS_START_REPLY_SUCCESS

|                                       |
|---------------------------------------|
| \#define DBUS_START_REPLY_SUCCESS   1 |

Service was auto started.

Definition at line 126 of file dbus-shared.h.

## Enumeration Type Documentation

## ◆ DBusBusType

|                  |
|------------------|
| enum DBusBusType |

Well-known bus types.

See dbus_bus_get().

| Enumerator        |                                  |
|-------------------|----------------------------------|
| DBUS_BUS_SESSION  | The login session bus.           |
| DBUS_BUS_SYSTEM   | The systemwide bus.              |
| DBUS_BUS_STARTER  | The bus that started us, if any. |

Definition at line 58 of file dbus-shared.h.

## ◆ DBusHandlerResult

|                        |
|------------------------|
| enum DBusHandlerResult |

Results that a message handler can return.

<table class="fieldtable">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Enumerator</th>
</tr>
</thead>
<tbody>
<tr>
<td class="fieldname">DBUS_HANDLER_RESULT_HANDLED </td>
<td class="fielddoc"><p>Message has had its effect - no need to run more handlers.</p></td>
</tr>
<tr>
<td class="fieldname">DBUS_HANDLER_RESULT_NOT_YET_HANDLED </td>
<td class="fielddoc"><p>Message has not had any effect - see if other handlers want it.</p></td>
</tr>
<tr>
<td class="fieldname">DBUS_HANDLER_RESULT_NEED_MEMORY </td>
<td class="fielddoc"><p>Need more memory in order to return DBUS_HANDLER_RESULT_HANDLED or DBUS_HANDLER_RESULT_NOT_YET_HANDLED.</p>
<p>Please try again later with more memory.</p></td>
</tr>
</tbody>
</table>

Definition at line 68 of file dbus-shared.h.
