Thread functions

D-Bus low-level public API

dbus_threads_init() and dbus_threads_init_default() More...

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
<td class="memItemRight" data-valign="bottom">DBusThreadFunctions</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Functions that must be implemented to make the D-Bus library thread-aware. More...<br />
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
<td colspan="2"><h2 id="typedefs" class="groupheader"> Typedefs</h2></td>
</tr>
<tr id="r_ga4eb021cd6cd0830423eac2738e0ddc40" class="memitem:ga4eb021cd6cd0830423eac2738e0ddc40">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusMutex </td>
<td class="memItemRight" data-valign="bottom">DBusMutex</td>
</tr>
<tr class="memdesc:ga4eb021cd6cd0830423eac2738e0ddc40">
<td class="mdescLeft"> </td>
<td class="mdescRight">An opaque mutex type provided by the DBusThreadFunctions implementation installed by dbus_threads_init().<br />
</td>
</tr>
<tr class="separator:ga4eb021cd6cd0830423eac2738e0ddc40">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa14cd16a336a85b5edbca3c237c3829e" class="memitem:gaa14cd16a336a85b5edbca3c237c3829e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusCondVar </td>
<td class="memItemRight" data-valign="bottom">DBusCondVar</td>
</tr>
<tr class="memdesc:gaa14cd16a336a85b5edbca3c237c3829e">
<td class="mdescLeft"> </td>
<td class="mdescRight">An opaque condition variable type provided by the DBusThreadFunctions implementation installed by dbus_threads_init().<br />
</td>
</tr>
<tr class="separator:gaa14cd16a336a85b5edbca3c237c3829e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga26a2a554e867cf0ebf0e532a8e87837c" class="memitem:ga26a2a554e867cf0ebf0e532a8e87837c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef DBusMutex *(* </td>
<td class="memItemRight" data-valign="bottom">DBusMutexNewFunction) (void)</td>
</tr>
<tr class="memdesc:ga26a2a554e867cf0ebf0e532a8e87837c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Deprecated, provide DBusRecursiveMutexNewFunction instead.<br />
</td>
</tr>
<tr class="separator:ga26a2a554e867cf0ebf0e532a8e87837c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gadcdd0312b9764349a8781f9ec50af3a5" class="memitem:gadcdd0312b9764349a8781f9ec50af3a5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusMutexFreeFunction) (DBusMutex *mutex)</td>
</tr>
<tr class="memdesc:gadcdd0312b9764349a8781f9ec50af3a5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Deprecated, provide DBusRecursiveMutexFreeFunction instead.<br />
</td>
</tr>
<tr class="separator:gadcdd0312b9764349a8781f9ec50af3a5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2beae753cc149b17d7da31764d180a2c" class="memitem:ga2beae753cc149b17d7da31764d180a2c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef dbus_bool_t(* </td>
<td class="memItemRight" data-valign="bottom">DBusMutexLockFunction) (DBusMutex *mutex)</td>
</tr>
<tr class="memdesc:ga2beae753cc149b17d7da31764d180a2c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Deprecated, provide DBusRecursiveMutexLockFunction instead.<br />
</td>
</tr>
<tr class="separator:ga2beae753cc149b17d7da31764d180a2c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga485db5209eed586c5d123b204abfaa5b" class="memitem:ga485db5209eed586c5d123b204abfaa5b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef dbus_bool_t(* </td>
<td class="memItemRight" data-valign="bottom">DBusMutexUnlockFunction) (DBusMutex *mutex)</td>
</tr>
<tr class="memdesc:ga485db5209eed586c5d123b204abfaa5b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Deprecated, provide DBusRecursiveMutexUnlockFunction instead.<br />
</td>
</tr>
<tr class="separator:ga485db5209eed586c5d123b204abfaa5b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2c8bcaaf40ae2b4f99a3990df883b851" class="memitem:ga2c8bcaaf40ae2b4f99a3990df883b851">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef DBusMutex *(* </td>
<td class="memItemRight" data-valign="bottom">DBusRecursiveMutexNewFunction) (void)</td>
</tr>
<tr class="memdesc:ga2c8bcaaf40ae2b4f99a3990df883b851">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new recursively-lockable mutex, or returns NULL if not enough memory.<br />
</td>
</tr>
<tr class="separator:ga2c8bcaaf40ae2b4f99a3990df883b851">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga54eec7640827bae19803054ee788055b" class="memitem:ga54eec7640827bae19803054ee788055b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusRecursiveMutexFreeFunction) (DBusMutex *mutex)</td>
</tr>
<tr class="memdesc:ga54eec7640827bae19803054ee788055b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Frees a recursively-lockable mutex.<br />
</td>
</tr>
<tr class="separator:ga54eec7640827bae19803054ee788055b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab9cc1e65419234941c0812db5b597c8b" class="memitem:gab9cc1e65419234941c0812db5b597c8b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusRecursiveMutexLockFunction) (DBusMutex *mutex)</td>
</tr>
<tr class="memdesc:gab9cc1e65419234941c0812db5b597c8b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Locks a recursively-lockable mutex.<br />
</td>
</tr>
<tr class="separator:gab9cc1e65419234941c0812db5b597c8b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga614e98f72541ae2a1df1aacbdcd63003" class="memitem:ga614e98f72541ae2a1df1aacbdcd63003">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusRecursiveMutexUnlockFunction) (DBusMutex *mutex)</td>
</tr>
<tr class="memdesc:ga614e98f72541ae2a1df1aacbdcd63003">
<td class="mdescLeft"> </td>
<td class="mdescRight">Unlocks a recursively-lockable mutex.<br />
</td>
</tr>
<tr class="separator:ga614e98f72541ae2a1df1aacbdcd63003">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9d52c81ac1a2b5ba187110dde030af51" class="memitem:ga9d52c81ac1a2b5ba187110dde030af51">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef DBusCondVar *(* </td>
<td class="memItemRight" data-valign="bottom">DBusCondVarNewFunction) (void)</td>
</tr>
<tr class="memdesc:ga9d52c81ac1a2b5ba187110dde030af51">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new condition variable.<br />
</td>
</tr>
<tr class="separator:ga9d52c81ac1a2b5ba187110dde030af51">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa09af8404e3e6d1b90240c518ce4882f" class="memitem:gaa09af8404e3e6d1b90240c518ce4882f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusCondVarFreeFunction) (DBusCondVar *cond)</td>
</tr>
<tr class="memdesc:gaa09af8404e3e6d1b90240c518ce4882f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Frees a condition variable.<br />
</td>
</tr>
<tr class="separator:gaa09af8404e3e6d1b90240c518ce4882f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga67533f7fdf29a1675454573551b9a55f" class="memitem:ga67533f7fdf29a1675454573551b9a55f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusCondVarWaitFunction) (DBusCondVar *cond, DBusMutex *mutex)</td>
</tr>
<tr class="memdesc:ga67533f7fdf29a1675454573551b9a55f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Waits on a condition variable.<br />
</td>
</tr>
<tr class="separator:ga67533f7fdf29a1675454573551b9a55f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga00bed7bcde662ef280739975b5671ea6" class="memitem:ga00bed7bcde662ef280739975b5671ea6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef dbus_bool_t(* </td>
<td class="memItemRight" data-valign="bottom">DBusCondVarWaitTimeoutFunction) (DBusCondVar *cond, DBusMutex *mutex, int timeout_milliseconds)</td>
</tr>
<tr class="memdesc:ga00bed7bcde662ef280739975b5671ea6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Waits on a condition variable with a timeout.<br />
</td>
</tr>
<tr class="separator:ga00bed7bcde662ef280739975b5671ea6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga06ebf9cfcc867e65fdb277c8a567a544" class="memitem:ga06ebf9cfcc867e65fdb277c8a567a544">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusCondVarWakeOneFunction) (DBusCondVar *cond)</td>
</tr>
<tr class="memdesc:ga06ebf9cfcc867e65fdb277c8a567a544">
<td class="mdescLeft"> </td>
<td class="mdescRight">Wakes one waiting thread on a condition variable.<br />
</td>
</tr>
<tr class="separator:ga06ebf9cfcc867e65fdb277c8a567a544">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga57021594625f0d0540469d4058e5b18a" class="memitem:ga57021594625f0d0540469d4058e5b18a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusCondVarWakeAllFunction) (DBusCondVar *cond)</td>
</tr>
<tr class="memdesc:ga57021594625f0d0540469d4058e5b18a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Wakes all waiting threads on a condition variable.<br />
</td>
</tr>
<tr class="separator:ga57021594625f0d0540469d4058e5b18a">
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
<tr id="r_gaf6212cb5e78b84cf5c6c6cb6e2b5aabe" class="memitem:gaf6212cb5e78b84cf5c6c6cb6e2b5aabe">
<td class="memItemLeft" style="text-align: right;" data-valign="top">enum  </td>
<td class="memItemRight" data-valign="bottom">DBusThreadFunctionsMask {<br />
  <strong>DBUS_THREAD_FUNCTIONS_MUTEX_NEW_MASK</strong> = 1 &lt;&lt; 0 , <strong>DBUS_THREAD_FUNCTIONS_MUTEX_FREE_MASK</strong> = 1 &lt;&lt; 1 , <strong>DBUS_THREAD_FUNCTIONS_MUTEX_LOCK_MASK</strong> = 1 &lt;&lt; 2 , <strong>DBUS_THREAD_FUNCTIONS_MUTEX_UNLOCK_MASK</strong> = 1 &lt;&lt; 3 ,<br />
  <strong>DBUS_THREAD_FUNCTIONS_CONDVAR_NEW_MASK</strong> = 1 &lt;&lt; 4 , <strong>DBUS_THREAD_FUNCTIONS_CONDVAR_FREE_MASK</strong> = 1 &lt;&lt; 5 , <strong>DBUS_THREAD_FUNCTIONS_CONDVAR_WAIT_MASK</strong> = 1 &lt;&lt; 6 , <strong>DBUS_THREAD_FUNCTIONS_CONDVAR_WAIT_TIMEOUT_MASK</strong> = 1 &lt;&lt; 7 ,<br />
  <strong>DBUS_THREAD_FUNCTIONS_CONDVAR_WAKE_ONE_MASK</strong> = 1 &lt;&lt; 8 , <strong>DBUS_THREAD_FUNCTIONS_CONDVAR_WAKE_ALL_MASK</strong> = 1 &lt;&lt; 9 , <strong>DBUS_THREAD_FUNCTIONS_RECURSIVE_MUTEX_NEW_MASK</strong> = 1 &lt;&lt; 10 , <strong>DBUS_THREAD_FUNCTIONS_RECURSIVE_MUTEX_FREE_MASK</strong> = 1 &lt;&lt; 11 ,<br />
  <strong>DBUS_THREAD_FUNCTIONS_RECURSIVE_MUTEX_LOCK_MASK</strong> = 1 &lt;&lt; 12 , <strong>DBUS_THREAD_FUNCTIONS_RECURSIVE_MUTEX_UNLOCK_MASK</strong> = 1 &lt;&lt; 13 , <strong>DBUS_THREAD_FUNCTIONS_ALL_MASK</strong> = (1 &lt;&lt; 14) - 1<br />
}</td>
</tr>
<tr class="memdesc:gaf6212cb5e78b84cf5c6c6cb6e2b5aabe">
<td class="mdescLeft"> </td>
<td class="mdescRight">Flags indicating which functions are present in DBusThreadFunctions. More...<br />
</td>
</tr>
<tr class="separator:gaf6212cb5e78b84cf5c6c6cb6e2b5aabe">
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
<td colspan="2"><h2 id="functions" class="groupheader"> Functions</h2></td>
</tr>
<tr id="r_gac7b8a7001befc3eaa8c6b043151008dc" class="memitem:gac7b8a7001befc3eaa8c6b043151008dc">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_threads_init (const DBusThreadFunctions *functions)</td>
</tr>
<tr class="memdesc:gac7b8a7001befc3eaa8c6b043151008dc">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initializes threads, like dbus_threads_init_default().<br />
</td>
</tr>
<tr class="separator:gac7b8a7001befc3eaa8c6b043151008dc">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga33b6cf3b8f1e41bad5508f84758818a7" class="memitem:ga33b6cf3b8f1e41bad5508f84758818a7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_threads_init_default (void)</td>
</tr>
<tr class="memdesc:ga33b6cf3b8f1e41bad5508f84758818a7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initializes threads.<br />
</td>
</tr>
<tr class="separator:ga33b6cf3b8f1e41bad5508f84758818a7">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

dbus_threads_init() and dbus_threads_init_default()

Functions and macros related to threads and thread locks.

If threads are initialized, the D-Bus library has locks on all global data structures. In addition, each DBusConnection has a lock, so only one thread at a time can touch the connection. (See DBusConnection for more on connection locking.)

Most other objects, however, do not have locks - they can only be used from a single thread at a time, unless you lock them yourself. For example, a DBusMessage can't be modified from two threads at once.

## Typedef Documentation

## ◆ DBusCondVar

|                                        |
|----------------------------------------|
| typedef struct DBusCondVar DBusCondVar |

An opaque condition variable type provided by the DBusThreadFunctions implementation installed by dbus_threads_init().

Definition at line 45 of file dbus-threads.h.

## ◆ DBusCondVarFreeFunction

|                                                               |
|---------------------------------------------------------------|
| typedef void(\* DBusCondVarFreeFunction) (DBusCondVar \*cond) |

Frees a condition variable.

Found in DBusThreadFunctions.

Definition at line 82 of file dbus-threads.h.

## ◆ DBusCondVarNewFunction

|                                                          |
|----------------------------------------------------------|
| typedef DBusCondVar \*(\* DBusCondVarNewFunction) (void) |

Creates a new condition variable.

Found in DBusThreadFunctions. Can only fail (returning NULL) due to lack of memory.

Definition at line 79 of file dbus-threads.h.

## ◆ DBusCondVarWaitFunction

|  |
|----|
| typedef void(\* DBusCondVarWaitFunction) (DBusCondVar \*cond, DBusMutex \*mutex) |

Waits on a condition variable.

Found in DBusThreadFunctions. Must work with either a recursive or nonrecursive mutex, whichever the thread implementation provides. Note that PTHREAD_MUTEX_RECURSIVE does not work with condition variables (does not save/restore the recursion count) so don't try using simply pthread_cond_wait() and a PTHREAD_MUTEX_RECURSIVE to implement this, it won't work right.

Has no error conditions. Must succeed if it returns.

Definition at line 94 of file dbus-threads.h.

## ◆ DBusCondVarWaitTimeoutFunction

|  |
|----|
| typedef dbus_bool_t(\* DBusCondVarWaitTimeoutFunction) (DBusCondVar \*cond, DBusMutex \*mutex, int timeout_milliseconds) |

Waits on a condition variable with a timeout.

Found in DBusThreadFunctions. Returns TRUE if the wait did not time out, and FALSE if it did.

Has no error conditions. Must succeed if it returns.

Definition at line 103 of file dbus-threads.h.

## ◆ DBusCondVarWakeAllFunction

|                                                                  |
|------------------------------------------------------------------|
| typedef void(\* DBusCondVarWakeAllFunction) (DBusCondVar \*cond) |

Wakes all waiting threads on a condition variable.

Found in DBusThreadFunctions.

Has no error conditions. Must succeed if it returns.

Definition at line 116 of file dbus-threads.h.

## ◆ DBusCondVarWakeOneFunction

|                                                                  |
|------------------------------------------------------------------|
| typedef void(\* DBusCondVarWakeOneFunction) (DBusCondVar \*cond) |

Wakes one waiting thread on a condition variable.

Found in DBusThreadFunctions.

Has no error conditions. Must succeed if it returns.

Definition at line 110 of file dbus-threads.h.

## ◆ DBusMutex

|                                    |
|------------------------------------|
| typedef struct DBusMutex DBusMutex |

An opaque mutex type provided by the DBusThreadFunctions implementation installed by dbus_threads_init().

Definition at line 43 of file dbus-threads.h.

## ◆ DBusMutexFreeFunction

|                                                            |
|------------------------------------------------------------|
| typedef void(\* DBusMutexFreeFunction) (DBusMutex \*mutex) |

Deprecated, provide DBusRecursiveMutexFreeFunction instead.

Definition at line 50 of file dbus-threads.h.

## ◆ DBusMutexLockFunction

|                                                                   |
|-------------------------------------------------------------------|
| typedef dbus_bool_t(\* DBusMutexLockFunction) (DBusMutex \*mutex) |

Deprecated, provide DBusRecursiveMutexLockFunction instead.

Return value is lock success, but gets ignored in practice.

Definition at line 52 of file dbus-threads.h.

## ◆ DBusMutexNewFunction

|                                                      |
|------------------------------------------------------|
| typedef DBusMutex \*(\* DBusMutexNewFunction) (void) |

Deprecated, provide DBusRecursiveMutexNewFunction instead.

Definition at line 48 of file dbus-threads.h.

## ◆ DBusMutexUnlockFunction

|                                                                     |
|---------------------------------------------------------------------|
| typedef dbus_bool_t(\* DBusMutexUnlockFunction) (DBusMutex \*mutex) |

Deprecated, provide DBusRecursiveMutexUnlockFunction instead.

Return value is unlock success, but gets ignored in practice.

Definition at line 54 of file dbus-threads.h.

## ◆ DBusRecursiveMutexFreeFunction

|                                                                     |
|---------------------------------------------------------------------|
| typedef void(\* DBusRecursiveMutexFreeFunction) (DBusMutex \*mutex) |

Frees a recursively-lockable mutex.

Found in DBusThreadFunctions.

Definition at line 66 of file dbus-threads.h.

## ◆ DBusRecursiveMutexLockFunction

|                                                                     |
|---------------------------------------------------------------------|
| typedef void(\* DBusRecursiveMutexLockFunction) (DBusMutex \*mutex) |

Locks a recursively-lockable mutex.

Found in DBusThreadFunctions. Can only fail due to lack of memory.

Definition at line 70 of file dbus-threads.h.

## ◆ DBusRecursiveMutexNewFunction

|                                                               |
|---------------------------------------------------------------|
| typedef DBusMutex \*(\* DBusRecursiveMutexNewFunction) (void) |

Creates a new recursively-lockable mutex, or returns NULL if not enough memory.

Can only fail due to lack of memory. Found in DBusThreadFunctions. Do not just use PTHREAD_MUTEX_RECURSIVE for this, because it does not save/restore the recursion count when waiting on a condition. libdbus requires the Java-style behavior where the mutex is fully unlocked to wait on a condition.

Definition at line 63 of file dbus-threads.h.

## ◆ DBusRecursiveMutexUnlockFunction

|                                                                       |
|-----------------------------------------------------------------------|
| typedef void(\* DBusRecursiveMutexUnlockFunction) (DBusMutex \*mutex) |

Unlocks a recursively-lockable mutex.

Found in DBusThreadFunctions. Can only fail due to lack of memory.

Definition at line 74 of file dbus-threads.h.

## Enumeration Type Documentation

## ◆ DBusThreadFunctionsMask

|                              |
|------------------------------|
| enum DBusThreadFunctionsMask |

Flags indicating which functions are present in DBusThreadFunctions.

Used to allow the library to detect older callers of dbus_threads_init() if new possible functions are added to DBusThreadFunctions.

Definition at line 123 of file dbus-threads.h.

## Function Documentation

## ◆ dbus_threads_init()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_threads_init | ( | const DBusThreadFunctions \*  | *functions* | ) |  |

Initializes threads, like dbus_threads_init_default().

This version previously allowed user-specified threading primitives, but since D-Bus 1.6 it ignores them and behaves exactly like dbus_threads_init_default().

Parameters  
|           |                                               |
|-----------|-----------------------------------------------|
| functions | ignored, formerly functions for using threads |

<!-- -->

Returns  
TRUE on success, FALSE if no memory

Definition at line 395 of file dbus-threads.c.

References \_dbus_current_generation, \_dbus_threads_init_platform_specific(), \_dbus_threads_lock_platform_specific(), \_dbus_threads_unlock_platform_specific(), FALSE, and TRUE.

Referenced by dbus_threads_init_default().

## ◆ dbus_threads_init_default()

|                                                   |     |       |     |     |     |
|---------------------------------------------------|-----|-------|-----|-----|-----|
| DBUS_EXPORT dbus_bool_t dbus_threads_init_default | (   | void  |     | )   |     |

Initializes threads.

If this function is not called, the D-Bus library will not lock any data structures. If it is called, D-Bus will do locking, at some cost in efficiency.

Since D-Bus 1.7 it is safe to call this function from any thread, any number of times (but it must be called before any other libdbus API is used).

In D-Bus 1.6 or older, this function must be called in the main thread before any other thread starts. As a result, it is not sufficient to call this function in a library or plugin, unless the library or plugin imposes a similar requirement on its callers.

dbus_shutdown() reverses the effects of this function when it resets all global state in libdbus.

Returns  
TRUE on success, FALSE if not enough memory

Definition at line 442 of file dbus-threads.c.

References dbus_threads_init(), and NULL.

Referenced by \_dbus_cmutex_new_at_location(), \_dbus_condvar_new(), and \_dbus_rmutex_new_at_location().
