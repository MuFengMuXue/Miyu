DBusKeyring implementation details

D-Bus secret internal implementation details

DBusKeyring implementation details. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-structures" class="groupheader"> Data Structures</h2></td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusKey</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">A single key from the cookie file. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusKeyring</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Internals of DBusKeyring. More...<br />
</td>
</tr>
<tr class="separator:">
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
<td colspan="2"><h2 id="macros" class="groupheader"> Macros</h2></td>
</tr>
<tr id="r_ga73544ee0e71ac5224d339bcc87b4b559" class="memitem:ga73544ee0e71ac5224d339bcc87b4b559">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">NEW_KEY_TIMEOUT_SECONDS   (60*5)</td>
</tr>
<tr class="memdesc:ga73544ee0e71ac5224d339bcc87b4b559">
<td class="mdescLeft"> </td>
<td class="mdescRight">The maximum age of a key before we create a new key to use in challenges.<br />
</td>
</tr>
<tr class="separator:ga73544ee0e71ac5224d339bcc87b4b559">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gada47ab381d8e794bd9563f362ea1e09e" class="memitem:gada47ab381d8e794bd9563f362ea1e09e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">EXPIRE_KEYS_TIMEOUT_SECONDS   (NEW_KEY_TIMEOUT_SECONDS + (60*2))</td>
</tr>
<tr class="memdesc:gada47ab381d8e794bd9563f362ea1e09e">
<td class="mdescLeft"> </td>
<td class="mdescRight">The time after which we drop a key from the secrets file.<br />
</td>
</tr>
<tr class="separator:gada47ab381d8e794bd9563f362ea1e09e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5b0fdbdfffac1aebfc00716cec02afcd" class="memitem:ga5b0fdbdfffac1aebfc00716cec02afcd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">MAX_TIME_TRAVEL_SECONDS   (60*5)</td>
</tr>
<tr class="memdesc:ga5b0fdbdfffac1aebfc00716cec02afcd">
<td class="mdescLeft"> </td>
<td class="mdescRight">The maximum amount of time a key can be in the future.<br />
</td>
</tr>
<tr class="separator:ga5b0fdbdfffac1aebfc00716cec02afcd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gacf841625731864fd6c3fab95bd0e878a" class="memitem:gacf841625731864fd6c3fab95bd0e878a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">MAX_KEYS_IN_FILE   256</td>
</tr>
<tr class="memdesc:gacf841625731864fd6c3fab95bd0e878a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Maximum number of keys in the keyring before we just ignore the rest.<br />
</td>
</tr>
<tr class="separator:gacf841625731864fd6c3fab95bd0e878a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad11bde7ec18fb393d9f6e552dc89e6c2" class="memitem:gad11bde7ec18fb393d9f6e552dc89e6c2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">MAX_LOCK_TIMEOUTS   32</td>
</tr>
<tr class="memdesc:gad11bde7ec18fb393d9f6e552dc89e6c2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Maximum number of timeouts waiting for lock before we decide it's stale.<br />
</td>
</tr>
<tr class="separator:gad11bde7ec18fb393d9f6e552dc89e6c2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga046e055537cce7bc45caf9d6e51e19dd" class="memitem:ga046e055537cce7bc45caf9d6e51e19dd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">LOCK_TIMEOUT_MILLISECONDS   250</td>
</tr>
<tr class="memdesc:ga046e055537cce7bc45caf9d6e51e19dd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Length of each timeout while waiting for a lock.<br />
</td>
</tr>
<tr class="separator:ga046e055537cce7bc45caf9d6e51e19dd">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

DBusKeyring implementation details.

The guts of DBusKeyring.

## Macro Definition Documentation

## ◆ EXPIRE_KEYS_TIMEOUT_SECONDS

|  |
|----|
| \#define EXPIRE_KEYS_TIMEOUT_SECONDS   (NEW_KEY_TIMEOUT_SECONDS + (60\*2)) |

The time after which we drop a key from the secrets file.

The EXPIRE_KEYS_TIMEOUT_SECONDS - NEW_KEY_TIMEOUT_SECONDS is the minimum time window a client has to complete authentication.

Definition at line 76 of file dbus-keyring.c.

## ◆ LOCK_TIMEOUT_MILLISECONDS

|                                          |
|------------------------------------------|
| \#define LOCK_TIMEOUT_MILLISECONDS   250 |

Length of each timeout while waiting for a lock.

Definition at line 193 of file dbus-keyring.c.

## ◆ MAX_KEYS_IN_FILE

|                                 |
|---------------------------------|
| \#define MAX_KEYS_IN_FILE   256 |

Maximum number of keys in the keyring before we just ignore the rest.

Definition at line 89 of file dbus-keyring.c.

## ◆ MAX_LOCK_TIMEOUTS

|                                 |
|---------------------------------|
| \#define MAX_LOCK_TIMEOUTS   32 |

Maximum number of timeouts waiting for lock before we decide it's stale.

Definition at line 191 of file dbus-keyring.c.

## ◆ MAX_TIME_TRAVEL_SECONDS

|                                            |
|--------------------------------------------|
| \#define MAX_TIME_TRAVEL_SECONDS   (60\*5) |

The maximum amount of time a key can be in the future.

Definition at line 80 of file dbus-keyring.c.

## ◆ NEW_KEY_TIMEOUT_SECONDS

|                                            |
|--------------------------------------------|
| \#define NEW_KEY_TIMEOUT_SECONDS   (60\*5) |

The maximum age of a key before we create a new key to use in challenges.

This isn't super-reliably enforced, since system clocks can change or be wrong, but we make a best effort to only use keys for a short time.

Definition at line 70 of file dbus-keyring.c.
