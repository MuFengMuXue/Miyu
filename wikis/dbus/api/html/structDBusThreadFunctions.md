DBusThreadFunctions Struct Reference

D-Bus low-level public API » Thread functions

Functions that must be implemented to make the D-Bus library thread-aware. More...

`#include <``dbus-threads.h``>`

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a8f1c2a3b3805e2c4034d7a341f7f82f1" class="memitem:a8f1c2a3b3805e2c4034d7a341f7f82f1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">mask</td>
</tr>
<tr class="memdesc:a8f1c2a3b3805e2c4034d7a341f7f82f1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Mask indicating which functions are present.<br />
</td>
</tr>
<tr class="separator:a8f1c2a3b3805e2c4034d7a341f7f82f1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a342ba12a619162a5b228903076b46a44" class="memitem:a342ba12a619162a5b228903076b46a44">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMutexNewFunction </td>
<td class="memItemRight" data-valign="bottom">mutex_new</td>
</tr>
<tr class="memdesc:a342ba12a619162a5b228903076b46a44">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to create a mutex; optional and deprecated.<br />
</td>
</tr>
<tr class="separator:a342ba12a619162a5b228903076b46a44">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a01107266a74895f13af9962af6ad07dd" class="memitem:a01107266a74895f13af9962af6ad07dd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMutexFreeFunction </td>
<td class="memItemRight" data-valign="bottom">mutex_free</td>
</tr>
<tr class="memdesc:a01107266a74895f13af9962af6ad07dd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to free a mutex; optional and deprecated.<br />
</td>
</tr>
<tr class="separator:a01107266a74895f13af9962af6ad07dd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a1cc9d20f2ad0296e932951470063f8d0" class="memitem:a1cc9d20f2ad0296e932951470063f8d0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMutexLockFunction </td>
<td class="memItemRight" data-valign="bottom">mutex_lock</td>
</tr>
<tr class="memdesc:a1cc9d20f2ad0296e932951470063f8d0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to lock a mutex; optional and deprecated.<br />
</td>
</tr>
<tr class="separator:a1cc9d20f2ad0296e932951470063f8d0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a334d478ec305b04f526537c131cd8e8a" class="memitem:a334d478ec305b04f526537c131cd8e8a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMutexUnlockFunction </td>
<td class="memItemRight" data-valign="bottom">mutex_unlock</td>
</tr>
<tr class="memdesc:a334d478ec305b04f526537c131cd8e8a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to unlock a mutex; optional and deprecated.<br />
</td>
</tr>
<tr class="separator:a334d478ec305b04f526537c131cd8e8a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a1796b617165734984bc40d38f9600d78" class="memitem:a1796b617165734984bc40d38f9600d78">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCondVarNewFunction </td>
<td class="memItemRight" data-valign="bottom">condvar_new</td>
</tr>
<tr class="memdesc:a1796b617165734984bc40d38f9600d78">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to create a condition variable.<br />
</td>
</tr>
<tr class="separator:a1796b617165734984bc40d38f9600d78">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ad302412c382190eddc05736f24d8855c" class="memitem:ad302412c382190eddc05736f24d8855c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCondVarFreeFunction </td>
<td class="memItemRight" data-valign="bottom">condvar_free</td>
</tr>
<tr class="memdesc:ad302412c382190eddc05736f24d8855c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to free a condition variable.<br />
</td>
</tr>
<tr class="separator:ad302412c382190eddc05736f24d8855c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ae4cb6e9fe7c0813213561150721f349c" class="memitem:ae4cb6e9fe7c0813213561150721f349c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCondVarWaitFunction </td>
<td class="memItemRight" data-valign="bottom">condvar_wait</td>
</tr>
<tr class="memdesc:ae4cb6e9fe7c0813213561150721f349c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to wait on a condition.<br />
</td>
</tr>
<tr class="separator:ae4cb6e9fe7c0813213561150721f349c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a5e049c7bdf4d83a85ebce31d838d4218" class="memitem:a5e049c7bdf4d83a85ebce31d838d4218">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCondVarWaitTimeoutFunction </td>
<td class="memItemRight" data-valign="bottom">condvar_wait_timeout</td>
</tr>
<tr class="memdesc:a5e049c7bdf4d83a85ebce31d838d4218">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to wait on a condition with a timeout.<br />
</td>
</tr>
<tr class="separator:a5e049c7bdf4d83a85ebce31d838d4218">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a3f1301eacf666381ec6c39100e6787e1" class="memitem:a3f1301eacf666381ec6c39100e6787e1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCondVarWakeOneFunction </td>
<td class="memItemRight" data-valign="bottom">condvar_wake_one</td>
</tr>
<tr class="memdesc:a3f1301eacf666381ec6c39100e6787e1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to wake one thread waiting on the condition.<br />
</td>
</tr>
<tr class="separator:a3f1301eacf666381ec6c39100e6787e1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a128295c0019a401163d04ea0e291b36c" class="memitem:a128295c0019a401163d04ea0e291b36c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCondVarWakeAllFunction </td>
<td class="memItemRight" data-valign="bottom">condvar_wake_all</td>
</tr>
<tr class="memdesc:a128295c0019a401163d04ea0e291b36c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to wake all threads waiting on the condition.<br />
</td>
</tr>
<tr class="separator:a128295c0019a401163d04ea0e291b36c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_afd30fb78a3ca1064bc8c074a6a61361e" class="memitem:afd30fb78a3ca1064bc8c074a6a61361e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusRecursiveMutexNewFunction </td>
<td class="memItemRight" data-valign="bottom">recursive_mutex_new</td>
</tr>
<tr class="memdesc:afd30fb78a3ca1064bc8c074a6a61361e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to create a recursive mutex.<br />
</td>
</tr>
<tr class="separator:afd30fb78a3ca1064bc8c074a6a61361e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a8be6d85b7f162352efa5bb4a5663f44f" class="memitem:a8be6d85b7f162352efa5bb4a5663f44f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusRecursiveMutexFreeFunction </td>
<td class="memItemRight" data-valign="bottom">recursive_mutex_free</td>
</tr>
<tr class="memdesc:a8be6d85b7f162352efa5bb4a5663f44f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to free a recursive mutex.<br />
</td>
</tr>
<tr class="separator:a8be6d85b7f162352efa5bb4a5663f44f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ae99179276be65fe4f701de307882dac5" class="memitem:ae99179276be65fe4f701de307882dac5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusRecursiveMutexLockFunction </td>
<td class="memItemRight" data-valign="bottom">recursive_mutex_lock</td>
</tr>
<tr class="memdesc:ae99179276be65fe4f701de307882dac5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to lock a recursive mutex.<br />
</td>
</tr>
<tr class="separator:ae99179276be65fe4f701de307882dac5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a0bdb8cd9b263bcde5a0548b16ccd0702" class="memitem:a0bdb8cd9b263bcde5a0548b16ccd0702">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusRecursiveMutexUnlockFunction </td>
<td class="memItemRight" data-valign="bottom">recursive_mutex_unlock</td>
</tr>
<tr class="memdesc:a0bdb8cd9b263bcde5a0548b16ccd0702">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to unlock a recursive mutex.<br />
</td>
</tr>
<tr class="separator:a0bdb8cd9b263bcde5a0548b16ccd0702">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ad257488b556bbc2f7d7c0d8fd1ee7bfb" class="memitem:ad257488b556bbc2f7d7c0d8fd1ee7bfb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void(* </td>
<td class="memItemRight" data-valign="bottom">padding1 )(void)</td>
</tr>
<tr class="memdesc:ad257488b556bbc2f7d7c0d8fd1ee7bfb">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reserved for future expansion.<br />
</td>
</tr>
<tr class="separator:ad257488b556bbc2f7d7c0d8fd1ee7bfb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ac685ad4919b74777c22cdb488719f4ca" class="memitem:ac685ad4919b74777c22cdb488719f4ca">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void(* </td>
<td class="memItemRight" data-valign="bottom">padding2 )(void)</td>
</tr>
<tr class="memdesc:ac685ad4919b74777c22cdb488719f4ca">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reserved for future expansion.<br />
</td>
</tr>
<tr class="separator:ac685ad4919b74777c22cdb488719f4ca">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ad0a49486e130ba93b1b36627d80ae516" class="memitem:ad0a49486e130ba93b1b36627d80ae516">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void(* </td>
<td class="memItemRight" data-valign="bottom">padding3 )(void)</td>
</tr>
<tr class="memdesc:ad0a49486e130ba93b1b36627d80ae516">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reserved for future expansion.<br />
</td>
</tr>
<tr class="separator:ad0a49486e130ba93b1b36627d80ae516">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a210150901e12926e8ed01f5d4e084963" class="memitem:a210150901e12926e8ed01f5d4e084963">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void(* </td>
<td class="memItemRight" data-valign="bottom">padding4 )(void)</td>
</tr>
<tr class="memdesc:a210150901e12926e8ed01f5d4e084963">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reserved for future expansion.<br />
</td>
</tr>
<tr class="separator:a210150901e12926e8ed01f5d4e084963">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Functions that must be implemented to make the D-Bus library thread-aware.

If you supply both recursive and non-recursive mutexes, libdbus will use the non-recursive version for condition variables, and the recursive version in other contexts.

The condition variable functions have to work with nonrecursive mutexes if you provide those, or with recursive mutexes if you don't.

Definition at line 154 of file dbus-threads.h.

## Field Documentation

## ◆ condvar_free

|                                                           |
|-----------------------------------------------------------|
| DBusCondVarFreeFunction DBusThreadFunctions::condvar_free |

Function to free a condition variable.

Definition at line 164 of file dbus-threads.h.

## ◆ condvar_new

|                                                         |
|---------------------------------------------------------|
| DBusCondVarNewFunction DBusThreadFunctions::condvar_new |

Function to create a condition variable.

Definition at line 163 of file dbus-threads.h.

## ◆ condvar_wait

|                                                           |
|-----------------------------------------------------------|
| DBusCondVarWaitFunction DBusThreadFunctions::condvar_wait |

Function to wait on a condition.

Definition at line 165 of file dbus-threads.h.

## ◆ condvar_wait_timeout

|                                                                          |
|--------------------------------------------------------------------------|
| DBusCondVarWaitTimeoutFunction DBusThreadFunctions::condvar_wait_timeout |

Function to wait on a condition with a timeout.

Definition at line 166 of file dbus-threads.h.

## ◆ condvar_wake_all

|                                                                  |
|------------------------------------------------------------------|
| DBusCondVarWakeAllFunction DBusThreadFunctions::condvar_wake_all |

Function to wake all threads waiting on the condition.

Definition at line 168 of file dbus-threads.h.

## ◆ condvar_wake_one

|                                                                  |
|------------------------------------------------------------------|
| DBusCondVarWakeOneFunction DBusThreadFunctions::condvar_wake_one |

Function to wake one thread waiting on the condition.

Definition at line 167 of file dbus-threads.h.

## ◆ mask

|                                        |
|----------------------------------------|
| unsigned int DBusThreadFunctions::mask |

Mask indicating which functions are present.

Definition at line 156 of file dbus-threads.h.

## ◆ mutex_free

|                                                       |
|-------------------------------------------------------|
| DBusMutexFreeFunction DBusThreadFunctions::mutex_free |

Function to free a mutex; optional and deprecated.

Definition at line 159 of file dbus-threads.h.

## ◆ mutex_lock

|                                                       |
|-------------------------------------------------------|
| DBusMutexLockFunction DBusThreadFunctions::mutex_lock |

Function to lock a mutex; optional and deprecated.

Definition at line 160 of file dbus-threads.h.

## ◆ mutex_new

|                                                     |
|-----------------------------------------------------|
| DBusMutexNewFunction DBusThreadFunctions::mutex_new |

Function to create a mutex; optional and deprecated.

Definition at line 158 of file dbus-threads.h.

## ◆ mutex_unlock

|                                                           |
|-----------------------------------------------------------|
| DBusMutexUnlockFunction DBusThreadFunctions::mutex_unlock |

Function to unlock a mutex; optional and deprecated.

Definition at line 161 of file dbus-threads.h.

## ◆ padding1

|                                               |
|-----------------------------------------------|
| void(\* DBusThreadFunctions::padding1) (void) |

Reserved for future expansion.

Definition at line 175 of file dbus-threads.h.

## ◆ padding2

|                                               |
|-----------------------------------------------|
| void(\* DBusThreadFunctions::padding2) (void) |

Reserved for future expansion.

Definition at line 176 of file dbus-threads.h.

## ◆ padding3

|                                               |
|-----------------------------------------------|
| void(\* DBusThreadFunctions::padding3) (void) |

Reserved for future expansion.

Definition at line 177 of file dbus-threads.h.

## ◆ padding4

|                                               |
|-----------------------------------------------|
| void(\* DBusThreadFunctions::padding4) (void) |

Reserved for future expansion.

Definition at line 178 of file dbus-threads.h.

## ◆ recursive_mutex_free

|                                                                          |
|--------------------------------------------------------------------------|
| DBusRecursiveMutexFreeFunction DBusThreadFunctions::recursive_mutex_free |

Function to free a recursive mutex.

Definition at line 171 of file dbus-threads.h.

## ◆ recursive_mutex_lock

|                                                                          |
|--------------------------------------------------------------------------|
| DBusRecursiveMutexLockFunction DBusThreadFunctions::recursive_mutex_lock |

Function to lock a recursive mutex.

Definition at line 172 of file dbus-threads.h.

## ◆ recursive_mutex_new

|                                                                        |
|------------------------------------------------------------------------|
| DBusRecursiveMutexNewFunction DBusThreadFunctions::recursive_mutex_new |

Function to create a recursive mutex.

Definition at line 170 of file dbus-threads.h.

## ◆ recursive_mutex_unlock

|  |
|----|
| DBusRecursiveMutexUnlockFunction DBusThreadFunctions::recursive_mutex_unlock |

Function to unlock a recursive mutex.

Definition at line 173 of file dbus-threads.h.

The documentation for this struct was generated from the following file:

- dbus-threads.h
