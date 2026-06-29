DBusCredentials Struct Reference

D-Bus secret internal implementation details » Credentials implementation details

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_af9b80fd01f235f0f9966bda009160f72" class="memitem:af9b80fd01f235f0f9966bda009160f72">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">refcount</td>
</tr>
<tr class="separator:af9b80fd01f235f0f9966bda009160f72">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ac80368624d1e5635078b5928ca3b5a4a" class="memitem:ac80368624d1e5635078b5928ca3b5a4a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uid_t </td>
<td class="memItemRight" data-valign="bottom">unix_uid</td>
</tr>
<tr class="separator:ac80368624d1e5635078b5928ca3b5a4a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a6353a98d6187003e3c0cd50f6940ac3c" class="memitem:a6353a98d6187003e3c0cd50f6940ac3c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_gid_t * </td>
<td class="memItemRight" data-valign="bottom">unix_gids</td>
</tr>
<tr class="separator:a6353a98d6187003e3c0cd50f6940ac3c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a2cfd68680aae9bdaf61e4ba4719d705c" class="memitem:a2cfd68680aae9bdaf61e4ba4719d705c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">size_t </td>
<td class="memItemRight" data-valign="bottom">n_unix_gids</td>
</tr>
<tr class="separator:a2cfd68680aae9bdaf61e4ba4719d705c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a7e7ef9c7976add83a1daec3d05670948" class="memitem:a7e7ef9c7976add83a1daec3d05670948">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_pid_t </td>
<td class="memItemRight" data-valign="bottom">pid</td>
</tr>
<tr class="separator:a7e7ef9c7976add83a1daec3d05670948">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a0a6dff147d858993940b8d01e43b2da6" class="memitem:a0a6dff147d858993940b8d01e43b2da6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">pid_fd</td>
</tr>
<tr class="separator:a0a6dff147d858993940b8d01e43b2da6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a4c744a3bdcee19cbf645c8ee137a8ae9" class="memitem:a4c744a3bdcee19cbf645c8ee137a8ae9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">windows_sid</td>
</tr>
<tr class="separator:a4c744a3bdcee19cbf645c8ee137a8ae9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a2b922578d012b340ad3996deb12ca47b" class="memitem:a2b922578d012b340ad3996deb12ca47b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">linux_security_label</td>
</tr>
<tr class="separator:a2b922578d012b340ad3996deb12ca47b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a10fb6f72f22ee0bc5cdf9b6780cf56a7" class="memitem:a10fb6f72f22ee0bc5cdf9b6780cf56a7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">adt_audit_data</td>
</tr>
<tr class="separator:a10fb6f72f22ee0bc5cdf9b6780cf56a7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ae261af0537d2aa3e6d926218e670c267" class="memitem:ae261af0537d2aa3e6d926218e670c267">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_int32_t </td>
<td class="memItemRight" data-valign="bottom">adt_audit_data_size</td>
</tr>
<tr class="separator:ae261af0537d2aa3e6d926218e670c267">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Definition at line 60 of file dbus-credentials.c.

## Field Documentation

## ◆ adt_audit_data

|                                        |
|----------------------------------------|
| void\* DBusCredentials::adt_audit_data |

Definition at line 69 of file dbus-credentials.c.

## ◆ adt_audit_data_size

|                                                   |
|---------------------------------------------------|
| dbus_int32_t DBusCredentials::adt_audit_data_size |

Definition at line 70 of file dbus-credentials.c.

## ◆ linux_security_label

|                                              |
|----------------------------------------------|
| char\* DBusCredentials::linux_security_label |

Definition at line 68 of file dbus-credentials.c.

## ◆ n_unix_gids

|                                     |
|-------------------------------------|
| size_t DBusCredentials::n_unix_gids |

Definition at line 64 of file dbus-credentials.c.

## ◆ pid

|                                 |
|---------------------------------|
| dbus_pid_t DBusCredentials::pid |

Definition at line 65 of file dbus-credentials.c.

## ◆ pid_fd

|                             |
|-----------------------------|
| int DBusCredentials::pid_fd |

Definition at line 66 of file dbus-credentials.c.

## ◆ refcount

|                               |
|-------------------------------|
| int DBusCredentials::refcount |

Definition at line 61 of file dbus-credentials.c.

## ◆ unix_gids

|                                         |
|-----------------------------------------|
| dbus_gid_t\* DBusCredentials::unix_gids |

Definition at line 63 of file dbus-credentials.c.

## ◆ unix_uid

|                                      |
|--------------------------------------|
| dbus_uid_t DBusCredentials::unix_uid |

Definition at line 62 of file dbus-credentials.c.

## ◆ windows_sid

|                                     |
|-------------------------------------|
| char\* DBusCredentials::windows_sid |

Definition at line 67 of file dbus-credentials.c.

The documentation for this struct was generated from the following file:

- dbus-credentials.c
