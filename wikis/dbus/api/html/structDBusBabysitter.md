DBusBabysitter Struct Reference

D-Bus secret internal implementation details » Utilities and portability

Babysitter implementation details. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_abd6c2c867f005bea3932fc9f754dd14e" class="memitem:abd6c2c867f005bea3932fc9f754dd14e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">refcount</td>
</tr>
<tr class="memdesc:abd6c2c867f005bea3932fc9f754dd14e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reference count.<br />
</td>
</tr>
<tr class="separator:abd6c2c867f005bea3932fc9f754dd14e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aa5f57474dbc3603fd888430496769778" class="memitem:aa5f57474dbc3603fd888430496769778">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">log_name</td>
</tr>
<tr class="memdesc:aa5f57474dbc3603fd888430496769778">
<td class="mdescLeft"> </td>
<td class="mdescRight">the name under which to log messages about this process being spawned<br />
</td>
</tr>
<tr class="separator:aa5f57474dbc3603fd888430496769778">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a287e96e0153eb170bd60ec6d0825ab78" class="memitem:a287e96e0153eb170bd60ec6d0825ab78">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusSocket </td>
<td class="memItemRight" data-valign="bottom">socket_to_babysitter</td>
</tr>
<tr class="memdesc:a287e96e0153eb170bd60ec6d0825ab78">
<td class="mdescLeft"> </td>
<td class="mdescRight">Connection to the babysitter process.<br />
</td>
</tr>
<tr class="separator:a287e96e0153eb170bd60ec6d0825ab78">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_abc42ea27fa4ee1e4f04819364e0a9bde" class="memitem:abc42ea27fa4ee1e4f04819364e0a9bde">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">error_pipe_from_child</td>
</tr>
<tr class="memdesc:abc42ea27fa4ee1e4f04819364e0a9bde">
<td class="mdescLeft"> </td>
<td class="mdescRight">Connection to the process that does the exec()<br />
</td>
</tr>
<tr class="separator:abc42ea27fa4ee1e4f04819364e0a9bde">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aa783f733db30b4587f08ee906612fa6c" class="memitem:aa783f733db30b4587f08ee906612fa6c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">pid_t </td>
<td class="memItemRight" data-valign="bottom">sitter_pid</td>
</tr>
<tr class="memdesc:aa783f733db30b4587f08ee906612fa6c">
<td class="mdescLeft"> </td>
<td class="mdescRight">PID Of the babysitter.<br />
</td>
</tr>
<tr class="separator:aa783f733db30b4587f08ee906612fa6c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_af0f5b85d39a7d2957ae83b3c594b88af" class="memitem:af0f5b85d39a7d2957ae83b3c594b88af">
<td class="memItemLeft" style="text-align: right;" data-valign="top">pid_t </td>
<td class="memItemRight" data-valign="bottom">grandchild_pid</td>
</tr>
<tr class="memdesc:af0f5b85d39a7d2957ae83b3c594b88af">
<td class="mdescLeft"> </td>
<td class="mdescRight">PID of the grandchild.<br />
</td>
</tr>
<tr class="separator:af0f5b85d39a7d2957ae83b3c594b88af">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ae0219a288aa52775dee075b80ab8c170" class="memitem:ae0219a288aa52775dee075b80ab8c170">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusWatchList * </td>
<td class="memItemRight" data-valign="bottom">watches</td>
</tr>
<tr class="memdesc:ae0219a288aa52775dee075b80ab8c170">
<td class="mdescLeft"> </td>
<td class="mdescRight">Watches.<br />
</td>
</tr>
<tr class="separator:ae0219a288aa52775dee075b80ab8c170">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ae89fdf7339b921a19728a2c8abfad251" class="memitem:ae89fdf7339b921a19728a2c8abfad251">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusWatch * </td>
<td class="memItemRight" data-valign="bottom">error_watch</td>
</tr>
<tr class="memdesc:ae89fdf7339b921a19728a2c8abfad251">
<td class="mdescLeft"> </td>
<td class="mdescRight">Error pipe watch.<br />
</td>
</tr>
<tr class="separator:ae89fdf7339b921a19728a2c8abfad251">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a1f01b1d3775f4b3437a01117cf8ddfcb" class="memitem:a1f01b1d3775f4b3437a01117cf8ddfcb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusWatch * </td>
<td class="memItemRight" data-valign="bottom">sitter_watch</td>
</tr>
<tr class="memdesc:a1f01b1d3775f4b3437a01117cf8ddfcb">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sitter pipe watch.<br />
</td>
</tr>
<tr class="separator:a1f01b1d3775f4b3437a01117cf8ddfcb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ab04435571fee6493f933842b68f800be" class="memitem:ab04435571fee6493f933842b68f800be">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusBabysitterFinishedFunc </td>
<td class="memItemRight" data-valign="bottom">finished_cb</td>
</tr>
<tr class="separator:ab04435571fee6493f933842b68f800be">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_acef97789a7db6f7219ddb200fd6d0c12" class="memitem:acef97789a7db6f7219ddb200fd6d0c12">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">finished_data</td>
</tr>
<tr class="separator:acef97789a7db6f7219ddb200fd6d0c12">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aaca14d66f484b0a3b06b395aa8485c70" class="memitem:aaca14d66f484b0a3b06b395aa8485c70">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">errnum</td>
</tr>
<tr class="memdesc:aaca14d66f484b0a3b06b395aa8485c70">
<td class="mdescLeft"> </td>
<td class="mdescRight">Error number.<br />
</td>
</tr>
<tr class="separator:aaca14d66f484b0a3b06b395aa8485c70">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a6b3aa53fa01507b290bf575f5cc088e3" class="memitem:a6b3aa53fa01507b290bf575f5cc088e3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">status</td>
</tr>
<tr class="memdesc:a6b3aa53fa01507b290bf575f5cc088e3">
<td class="mdescLeft"> </td>
<td class="mdescRight">Exit status code.<br />
</td>
</tr>
<tr class="separator:a6b3aa53fa01507b290bf575f5cc088e3">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a8d6c87e5e04e3f6e2e11dc4547e238c7" class="memitem:a8d6c87e5e04e3f6e2e11dc4547e238c7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">have_child_status: 1</td>
</tr>
<tr class="memdesc:a8d6c87e5e04e3f6e2e11dc4547e238c7">
<td class="mdescLeft"> </td>
<td class="mdescRight">True if child status has been reaped.<br />
</td>
</tr>
<tr class="separator:a8d6c87e5e04e3f6e2e11dc4547e238c7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_afc7d26bf84459ec406ddd615101018f9" class="memitem:afc7d26bf84459ec406ddd615101018f9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">have_fork_errnum: 1</td>
</tr>
<tr class="memdesc:afc7d26bf84459ec406ddd615101018f9">
<td class="mdescLeft"> </td>
<td class="mdescRight">True if we have an error code from fork()<br />
</td>
</tr>
<tr class="separator:afc7d26bf84459ec406ddd615101018f9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a2275e6071accc74280cd354debb5f801" class="memitem:a2275e6071accc74280cd354debb5f801">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">have_exec_errnum: 1</td>
</tr>
<tr class="memdesc:a2275e6071accc74280cd354debb5f801">
<td class="mdescLeft"> </td>
<td class="mdescRight">True if we have an error code from exec()<br />
</td>
</tr>
<tr class="separator:a2275e6071accc74280cd354debb5f801">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a8a19c137b938b85c844d12e26387b097" class="memitem:a8a19c137b938b85c844d12e26387b097">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAtomic </td>
<td class="memItemRight" data-valign="bottom">refcount</td>
</tr>
<tr class="separator:a8a19c137b938b85c844d12e26387b097">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a458794614c39490bc5411898e4a42033" class="memitem:a458794614c39490bc5411898e4a42033">
<td class="memItemLeft" style="text-align: right;" data-valign="top">HANDLE </td>
<td class="memItemRight" data-valign="bottom">thread_handle</td>
</tr>
<tr class="separator:a458794614c39490bc5411898e4a42033">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ac1ed8e4274f909befe35fee5143c40a0" class="memitem:ac1ed8e4274f909befe35fee5143c40a0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">HANDLE </td>
<td class="memItemRight" data-valign="bottom">child_handle</td>
</tr>
<tr class="separator:ac1ed8e4274f909befe35fee5143c40a0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a5e6a562ea0a76509fc5d19edef08e8ee" class="memitem:a5e6a562ea0a76509fc5d19edef08e8ee">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusSocket </td>
<td class="memItemRight" data-valign="bottom">socket_to_main</td>
</tr>
<tr class="separator:a5e6a562ea0a76509fc5d19edef08e8ee">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aa5932b647ec8ece2fe27f998e1a71d56" class="memitem:aa5932b647ec8ece2fe27f998e1a71d56">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">have_spawn_errno</td>
</tr>
<tr class="separator:aa5932b647ec8ece2fe27f998e1a71d56">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a256f84a0bccdc33553f595e26e0037ac" class="memitem:a256f84a0bccdc33553f595e26e0037ac">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">spawn_errno</td>
</tr>
<tr class="separator:a256f84a0bccdc33553f595e26e0037ac">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aef16c6321917a1f593ba3cdd6057451a" class="memitem:aef16c6321917a1f593ba3cdd6057451a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">have_child_status</td>
</tr>
<tr class="separator:aef16c6321917a1f593ba3cdd6057451a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a636fa0239712e02c60ef0e167f0e54fd" class="memitem:a636fa0239712e02c60ef0e167f0e54fd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">child_status</td>
</tr>
<tr class="separator:a636fa0239712e02c60ef0e167f0e54fd">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Babysitter implementation details.

Definition at line 251 of file dbus-spawn-unix.c.

## Field Documentation

## ◆ child_handle

|                                     |
|-------------------------------------|
| HANDLE DBusBabysitter::child_handle |

Definition at line 69 of file dbus-spawn-win.c.

## ◆ child_status

|                                  |
|----------------------------------|
| int DBusBabysitter::child_status |

Definition at line 81 of file dbus-spawn-win.c.

## ◆ errnum

|                            |
|----------------------------|
| int DBusBabysitter::errnum |

Error number.

Definition at line 272 of file dbus-spawn-unix.c.

Referenced by \_dbus_babysitter_set_child_exit_error().

## ◆ error_pipe_from_child

|                                           |
|-------------------------------------------|
| int DBusBabysitter::error_pipe_from_child |

Connection to the process that does the exec()

Definition at line 259 of file dbus-spawn-unix.c.

Referenced by \_dbus_spawn_async_with_babysitter().

## ◆ error_watch

|                                         |
|-----------------------------------------|
| DBusWatch\* DBusBabysitter::error_watch |

Error pipe watch.

Definition at line 266 of file dbus-spawn-unix.c.

Referenced by \_dbus_spawn_async_with_babysitter().

## ◆ finished_cb

|                                                        |
|--------------------------------------------------------|
| DBusBabysitterFinishedFunc DBusBabysitter::finished_cb |

Definition at line 269 of file dbus-spawn-unix.c.

## ◆ finished_data

|                                       |
|---------------------------------------|
| void \* DBusBabysitter::finished_data |

Definition at line 270 of file dbus-spawn-unix.c.

## ◆ grandchild_pid

|                                      |
|--------------------------------------|
| pid_t DBusBabysitter::grandchild_pid |

PID of the grandchild.

Definition at line 262 of file dbus-spawn-unix.c.

Referenced by \_dbus_babysitter_kill_child().

## ◆ have_child_status \[1/2\]

|                                                |
|------------------------------------------------|
| unsigned int DBusBabysitter::have_child_status |

True if child status has been reaped.

Definition at line 274 of file dbus-spawn-unix.c.

Referenced by \_dbus_babysitter_get_child_exit_status(), and \_dbus_babysitter_set_child_exit_error().

## ◆ have_child_status \[2/2\]

|                                               |
|-----------------------------------------------|
| dbus_bool_t DBusBabysitter::have_child_status |

Definition at line 80 of file dbus-spawn-win.c.

## ◆ have_exec_errnum

|                                               |
|-----------------------------------------------|
| unsigned int DBusBabysitter::have_exec_errnum |

True if we have an error code from exec()

Definition at line 276 of file dbus-spawn-unix.c.

Referenced by \_dbus_babysitter_set_child_exit_error().

## ◆ have_fork_errnum

|                                               |
|-----------------------------------------------|
| unsigned int DBusBabysitter::have_fork_errnum |

True if we have an error code from fork()

Definition at line 275 of file dbus-spawn-unix.c.

Referenced by \_dbus_babysitter_set_child_exit_error().

## ◆ have_spawn_errno

|                                              |
|----------------------------------------------|
| dbus_bool_t DBusBabysitter::have_spawn_errno |

Definition at line 78 of file dbus-spawn-win.c.

## ◆ log_name

|                                  |
|----------------------------------|
| char \* DBusBabysitter::log_name |

the name under which to log messages about this process being spawned

Definition at line 255 of file dbus-spawn-unix.c.

Referenced by \_dbus_babysitter_set_child_exit_error(), \_dbus_babysitter_unref(), and \_dbus_spawn_async_with_babysitter().

## ◆ refcount \[1/2\]

|                              |
|------------------------------|
| int DBusBabysitter::refcount |

Reference count.

Definition at line 253 of file dbus-spawn-unix.c.

Referenced by \_dbus_babysitter_ref(), and \_dbus_babysitter_unref().

## ◆ refcount \[2/2\]

|                                     |
|-------------------------------------|
| DBusAtomic DBusBabysitter::refcount |

Definition at line 65 of file dbus-spawn-win.c.

## ◆ sitter_pid

|                                  |
|----------------------------------|
| pid_t DBusBabysitter::sitter_pid |

PID Of the babysitter.

Definition at line 261 of file dbus-spawn-unix.c.

Referenced by \_dbus_babysitter_unref(), and \_dbus_spawn_async_with_babysitter().

## ◆ sitter_watch

|                                           |
|-------------------------------------------|
| DBusWatch \* DBusBabysitter::sitter_watch |

Sitter pipe watch.

Definition at line 267 of file dbus-spawn-unix.c.

Referenced by \_dbus_babysitter_unref(), and \_dbus_spawn_async_with_babysitter().

## ◆ socket_to_babysitter

|                                                 |
|-------------------------------------------------|
| DBusSocket DBusBabysitter::socket_to_babysitter |

Connection to the babysitter process.

Definition at line 258 of file dbus-spawn-unix.c.

Referenced by \_dbus_babysitter_get_child_exited(), and \_dbus_spawn_async_with_babysitter().

## ◆ socket_to_main

|                                           |
|-------------------------------------------|
| DBusSocket DBusBabysitter::socket_to_main |

Definition at line 71 of file dbus-spawn-win.c.

## ◆ spawn_errno

|                                 |
|---------------------------------|
| int DBusBabysitter::spawn_errno |

Definition at line 79 of file dbus-spawn-win.c.

## ◆ status

|                            |
|----------------------------|
| int DBusBabysitter::status |

Exit status code.

Definition at line 273 of file dbus-spawn-unix.c.

Referenced by \_dbus_babysitter_get_child_exit_status(), \_dbus_babysitter_set_child_exit_error(), and \_dbus_babysitter_unref().

## ◆ thread_handle

|                                      |
|--------------------------------------|
| HANDLE DBusBabysitter::thread_handle |

Definition at line 68 of file dbus-spawn-win.c.

## ◆ watches

|                                          |
|------------------------------------------|
| DBusWatchList \* DBusBabysitter::watches |

Watches.

Definition at line 264 of file dbus-spawn-unix.c.

Referenced by \_dbus_babysitter_set_watch_functions(), \_dbus_babysitter_unref(), and \_dbus_spawn_async_with_babysitter().

The documentation for this struct was generated from the following files:

- dbus-spawn-unix.c
- dbus-spawn-win.c
