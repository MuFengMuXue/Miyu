Internal system-dependent API

D-Bus secret internal implementation details

Internal system-dependent API available on UNIX and Windows. More...

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
<td class="memItemRight" data-valign="bottom">DBusSocket</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Socket interface. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusAtomic</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">An atomic integer safe to increment or decrement from multiple threads. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusPollFD</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusStat</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Portable struct with stat() results. More...<br />
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
<tr id="r_ga4eb5f05dd6ad89caa4b0340e1cf0b8d9" class="memitem:ga4eb5f05dd6ad89caa4b0340e1cf0b8d9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_PID_UNSET   ((dbus_pid_t) -1)</td>
</tr>
<tr class="memdesc:ga4eb5f05dd6ad89caa4b0340e1cf0b8d9">
<td class="mdescLeft"> </td>
<td class="mdescRight">an invalid PID used to represent an uninitialized dbus_pid_t field<br />
</td>
</tr>
<tr class="separator:ga4eb5f05dd6ad89caa4b0340e1cf0b8d9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3d2f3fb32bb759cabe362ca2de383f7d" class="memitem:ga3d2f3fb32bb759cabe362ca2de383f7d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_UID_UNSET   ((dbus_uid_t) -1)</td>
</tr>
<tr class="memdesc:ga3d2f3fb32bb759cabe362ca2de383f7d">
<td class="mdescLeft"> </td>
<td class="mdescRight">an invalid UID used to represent an uninitialized dbus_uid_t field<br />
</td>
</tr>
<tr class="separator:ga3d2f3fb32bb759cabe362ca2de383f7d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga768a080926a119a6131083facc0bd42b" class="memitem:ga768a080926a119a6131083facc0bd42b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_GID_UNSET   ((dbus_gid_t) -1)</td>
</tr>
<tr class="memdesc:ga768a080926a119a6131083facc0bd42b">
<td class="mdescLeft"> </td>
<td class="mdescRight">an invalid GID used to represent an uninitialized dbus_gid_t field<br />
</td>
</tr>
<tr class="separator:ga768a080926a119a6131083facc0bd42b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf4553a43e3b8c0e43d9148a00dcc3fa4" class="memitem:gaf4553a43e3b8c0e43d9148a00dcc3fa4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_PID_FORMAT   "%lu"</td>
</tr>
<tr class="memdesc:gaf4553a43e3b8c0e43d9148a00dcc3fa4">
<td class="mdescLeft"> </td>
<td class="mdescRight">an appropriate printf format for dbus_pid_t<br />
</td>
</tr>
<tr class="separator:gaf4553a43e3b8c0e43d9148a00dcc3fa4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab657f0434f01b463891942f373f7b4a1" class="memitem:gab657f0434f01b463891942f373f7b4a1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_UID_FORMAT   "%lu"</td>
</tr>
<tr class="memdesc:gab657f0434f01b463891942f373f7b4a1">
<td class="mdescLeft"> </td>
<td class="mdescRight">an appropriate printf format for dbus_uid_t<br />
</td>
</tr>
<tr class="separator:gab657f0434f01b463891942f373f7b4a1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaaab5918b2ae57886d9783df09bd61c7e" class="memitem:gaaab5918b2ae57886d9783df09bd61c7e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_GID_FORMAT   "%lu"</td>
</tr>
<tr class="memdesc:gaaab5918b2ae57886d9783df09bd61c7e">
<td class="mdescLeft"> </td>
<td class="mdescRight">an appropriate printf format for dbus_gid_t<br />
</td>
</tr>
<tr class="separator:gaaab5918b2ae57886d9783df09bd61c7e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2adcbf7dbbbf3c345a38086972cb21b2" class="memitem:ga2adcbf7dbbbf3c345a38086972cb21b2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_SOCKET_FORMAT   "d"</td>
</tr>
<tr class="separator:ga2adcbf7dbbbf3c345a38086972cb21b2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga54fb3a4a911769c0bc59180e74410e9c" class="memitem:ga54fb3a4a911769c0bc59180e74410e9c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_SOCKET_INIT   { -1 }</td>
</tr>
<tr class="separator:ga54fb3a4a911769c0bc59180e74410e9c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad448c8ded79d55a3ca694d6aa9fa24cb" class="memitem:gad448c8ded79d55a3ca694d6aa9fa24cb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_POLLABLE_FORMAT   "d"</td>
</tr>
<tr class="separator:gad448c8ded79d55a3ca694d6aa9fa24cb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga96b5ba58b9939d789bfece0d9bb82f41" class="memitem:ga96b5ba58b9939d789bfece0d9bb82f41">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_POLLIN   0x0001</td>
</tr>
<tr class="memdesc:ga96b5ba58b9939d789bfece0d9bb82f41">
<td class="mdescLeft"> </td>
<td class="mdescRight">There is data to read.<br />
</td>
</tr>
<tr class="separator:ga96b5ba58b9939d789bfece0d9bb82f41">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1db7d09a41912c10978c6a4955d9a9d2" class="memitem:ga1db7d09a41912c10978c6a4955d9a9d2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_POLLPRI   0x0002</td>
</tr>
<tr class="memdesc:ga1db7d09a41912c10978c6a4955d9a9d2">
<td class="mdescLeft"> </td>
<td class="mdescRight">There is urgent data to read.<br />
</td>
</tr>
<tr class="separator:ga1db7d09a41912c10978c6a4955d9a9d2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0cb1ace07be145e0b908687e99b5f161" class="memitem:ga0cb1ace07be145e0b908687e99b5f161">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_POLLOUT   0x0004</td>
</tr>
<tr class="memdesc:ga0cb1ace07be145e0b908687e99b5f161">
<td class="mdescLeft"> </td>
<td class="mdescRight">Writing now will not block.<br />
</td>
</tr>
<tr class="separator:ga0cb1ace07be145e0b908687e99b5f161">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga231164196ff407eccb732452a2d36468" class="memitem:ga231164196ff407eccb732452a2d36468">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_POLLERR   0x0008</td>
</tr>
<tr class="memdesc:ga231164196ff407eccb732452a2d36468">
<td class="mdescLeft"> </td>
<td class="mdescRight">Error condition.<br />
</td>
</tr>
<tr class="separator:ga231164196ff407eccb732452a2d36468">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6f08232c1f943313e3eefd7de8f3592f" class="memitem:ga6f08232c1f943313e3eefd7de8f3592f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_POLLHUP   0x0010</td>
</tr>
<tr class="memdesc:ga6f08232c1f943313e3eefd7de8f3592f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Hung up.<br />
</td>
</tr>
<tr class="separator:ga6f08232c1f943313e3eefd7de8f3592f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga83bf3d24f3a1a853dda794835c39fc6f" class="memitem:ga83bf3d24f3a1a853dda794835c39fc6f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_POLLNVAL   0x0020</td>
</tr>
<tr class="memdesc:ga83bf3d24f3a1a853dda794835c39fc6f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Invalid request: fd not open.<br />
</td>
</tr>
<tr class="separator:ga83bf3d24f3a1a853dda794835c39fc6f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac8269b795461ee42004b65734ce89e0b" class="memitem:gac8269b795461ee42004b65734ce89e0b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_DOUBLES_BITWISE_EQUAL(a, b)   (memcmp (&amp;(a), &amp;(b), sizeof (double)) == 0)</td>
</tr>
<tr class="memdesc:gac8269b795461ee42004b65734ce89e0b">
<td class="mdescLeft"> </td>
<td class="mdescRight">On x86 there is an 80-bit FPU, and if you do "a == b" it may have a or b in an 80-bit register, thus failing to compare the two 64-bit doubles for bitwise equality.<br />
</td>
</tr>
<tr class="separator:gac8269b795461ee42004b65734ce89e0b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad11b2d894fce7ae647a9cb2d9ba70f81" class="memitem:gad11b2d894fce7ae647a9cb2d9ba70f81">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_DEFAULT_MESSAGE_UNIX_FDS   16</td>
</tr>
<tr class="separator:gad11b2d894fce7ae647a9cb2d9ba70f81">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae0c49dcd1add7eb501c4de5d528eb33d" class="memitem:gae0c49dcd1add7eb501c4de5d528eb33d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_MAX_SUN_PATH_LENGTH   99</td>
</tr>
<tr class="memdesc:gae0c49dcd1add7eb501c4de5d528eb33d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Maximum length of the path to a UNIX domain socket, sockaddr_un::sun_path member.<br />
</td>
</tr>
<tr class="separator:gae0c49dcd1add7eb501c4de5d528eb33d">
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
<tr id="r_ga1eff6303266888ec466cddba6c03aa40" class="memitem:ga1eff6303266888ec466cddba6c03aa40">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef unsigned long </td>
<td class="memItemRight" data-valign="bottom">dbus_pid_t</td>
</tr>
<tr class="memdesc:ga1eff6303266888ec466cddba6c03aa40">
<td class="mdescLeft"> </td>
<td class="mdescRight">A process ID.<br />
</td>
</tr>
<tr class="separator:ga1eff6303266888ec466cddba6c03aa40">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga186e987b700f9ddc6cea8aa0db82b151" class="memitem:ga186e987b700f9ddc6cea8aa0db82b151">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef unsigned long </td>
<td class="memItemRight" data-valign="bottom">dbus_uid_t</td>
</tr>
<tr class="memdesc:ga186e987b700f9ddc6cea8aa0db82b151">
<td class="mdescLeft"> </td>
<td class="mdescRight">A user ID.<br />
</td>
</tr>
<tr class="separator:ga186e987b700f9ddc6cea8aa0db82b151">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2f5c2e418b81ec2a86594f56ec6d7627" class="memitem:ga2f5c2e418b81ec2a86594f56ec6d7627">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef unsigned long </td>
<td class="memItemRight" data-valign="bottom">dbus_gid_t</td>
</tr>
<tr class="memdesc:ga2f5c2e418b81ec2a86594f56ec6d7627">
<td class="mdescLeft"> </td>
<td class="mdescRight">A group ID.<br />
</td>
</tr>
<tr class="separator:ga2f5c2e418b81ec2a86594f56ec6d7627">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga208bb797a458b9cc721b317d9c95d233" class="memitem:ga208bb797a458b9cc721b317d9c95d233">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusAtomic </td>
<td class="memItemRight" data-valign="bottom">DBusAtomic</td>
</tr>
<tr class="memdesc:ga208bb797a458b9cc721b317d9c95d233">
<td class="mdescLeft"> </td>
<td class="mdescRight">Opaque type representing an atomically-modifiable integer that can be used from multiple threads.<br />
</td>
</tr>
<tr class="separator:ga208bb797a458b9cc721b317d9c95d233">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae217564e8ab50848f04003d982287661" class="memitem:gae217564e8ab50848f04003d982287661">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef int </td>
<td class="memItemRight" data-valign="bottom">DBusPollable</td>
</tr>
<tr class="separator:gae217564e8ab50848f04003d982287661">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga54409fb809f59d2b497592c49df04c52" class="memitem:ga54409fb809f59d2b497592c49df04c52">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusDirIter </td>
<td class="memItemRight" data-valign="bottom">DBusDirIter</td>
</tr>
<tr class="memdesc:ga54409fb809f59d2b497592c49df04c52">
<td class="mdescLeft"> </td>
<td class="mdescRight">Opaque type for reading a directory listing.<br />
</td>
</tr>
<tr class="separator:ga54409fb809f59d2b497592c49df04c52">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga24015a2f75b94c1307360755ce97f869" class="memitem:ga24015a2f75b94c1307360755ce97f869">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef union DBusGUID </td>
<td class="memItemRight" data-valign="bottom">DBusGUID</td>
</tr>
<tr class="memdesc:ga24015a2f75b94c1307360755ce97f869">
<td class="mdescLeft"> </td>
<td class="mdescRight">Type representing a universally unique ID.<br />
</td>
</tr>
<tr class="separator:ga24015a2f75b94c1307360755ce97f869">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga064d89fe6400aac228895eea96117769" class="memitem:ga064d89fe6400aac228895eea96117769">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusRLimit </td>
<td class="memItemRight" data-valign="bottom">DBusRLimit</td>
</tr>
<tr class="separator:ga064d89fe6400aac228895eea96117769">
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
<tr id="r_ga4b5c2486177405073218decdfe22a518" class="memitem:ga4b5c2486177405073218decdfe22a518">
<td class="memItemLeft" style="text-align: right;" data-valign="top">enum  </td>
<td class="memItemRight" data-valign="bottom"><strong>DBusCredentialsAddFlags</strong> { <strong>DBUS_CREDENTIALS_ADD_FLAGS_USER_DATABASE</strong> = (1 &lt;&lt; 0) , <strong>DBUS_CREDENTIALS_ADD_FLAGS_NONE</strong> = 0 }</td>
</tr>
<tr class="separator:ga4b5c2486177405073218decdfe22a518">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2c2312e94991e6dba67c725c18715ff4" class="memitem:ga2c2312e94991e6dba67c725c18715ff4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">enum  </td>
<td class="memItemRight" data-valign="bottom"><strong>DBusLogFlags</strong> { <strong>DBUS_LOG_FLAGS_STDERR</strong> = (1 &lt;&lt; 0) , <strong>DBUS_LOG_FLAGS_SYSTEM_LOG</strong> = (1 &lt;&lt; 1) }</td>
</tr>
<tr class="separator:ga2c2312e94991e6dba67c725c18715ff4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab77d7c590819f95d97f78c5544e714c4" class="memitem:gab77d7c590819f95d97f78c5544e714c4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">enum  </td>
<td class="memItemRight" data-valign="bottom"><strong>DBusSystemLogSeverity</strong> { <strong>DBUS_SYSTEM_LOG_INFO</strong> , <strong>DBUS_SYSTEM_LOG_WARNING</strong> , <strong>DBUS_SYSTEM_LOG_SECURITY</strong> , <strong>DBUS_SYSTEM_LOG_ERROR</strong> }</td>
</tr>
<tr class="separator:gab77d7c590819f95d97f78c5544e714c4">
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
<tr id="r_gab8b712cdd4f365c55263b0e2c4fabbfa" class="memitem:gab8b712cdd4f365c55263b0e2c4fabbfa">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_abort (void)</td>
</tr>
<tr class="memdesc:gab8b712cdd4f365c55263b0e2c4fabbfa">
<td class="mdescLeft"> </td>
<td class="mdescRight">Aborts the program with SIGABRT (dumping core).<br />
</td>
</tr>
<tr class="separator:gab8b712cdd4f365c55263b0e2c4fabbfa">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga50b17be5597d832a592ce8dc04098e7d" class="memitem:ga50b17be5597d832a592ce8dc04098e7d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">_dbus_getenv (const char *varname)</td>
</tr>
<tr class="memdesc:ga50b17be5597d832a592ce8dc04098e7d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Wrapper for getenv().<br />
</td>
</tr>
<tr class="separator:ga50b17be5597d832a592ce8dc04098e7d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1e41f8a9d87a5c78477fbbc318a4ab68" class="memitem:ga1e41f8a9d87a5c78477fbbc318a4ab68">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_clearenv (void)</td>
</tr>
<tr class="memdesc:ga1e41f8a9d87a5c78477fbbc318a4ab68">
<td class="mdescLeft"> </td>
<td class="mdescRight">Wrapper for clearenv().<br />
</td>
</tr>
<tr class="separator:ga1e41f8a9d87a5c78477fbbc318a4ab68">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad13a7c789c5cdcc3bcd0e80232efbd77" class="memitem:gad13a7c789c5cdcc3bcd0e80232efbd77">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_split_paths_and_append (DBusString *dirs, const char *suffix, DBusList **dir_list)</td>
</tr>
<tr class="memdesc:gad13a7c789c5cdcc3bcd0e80232efbd77">
<td class="mdescLeft"> </td>
<td class="mdescRight">Split paths into a list of char strings.<br />
</td>
</tr>
<tr class="separator:gad13a7c789c5cdcc3bcd0e80232efbd77">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6c14c6bf4dd98b3fe3a114e9f5630148" class="memitem:ga6c14c6bf4dd98b3fe3a114e9f5630148">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_check_setuid (void)</td>
</tr>
<tr class="memdesc:ga6c14c6bf4dd98b3fe3a114e9f5630148">
<td class="mdescLeft"> </td>
<td class="mdescRight"><strong>NOTE</strong>: If you modify this function, please also consider making the corresponding change in GLib.<br />
</td>
</tr>
<tr class="separator:ga6c14c6bf4dd98b3fe3a114e9f5630148">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga41a980c914021cdb1825316cccc4ee6c" class="memitem:ga41a980c914021cdb1825316cccc4ee6c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char ** </td>
<td class="memItemRight" data-valign="bottom">_dbus_get_environment (void)</td>
</tr>
<tr class="memdesc:ga41a980c914021cdb1825316cccc4ee6c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets a NULL-terminated list of key=value pairs from the environment.<br />
</td>
</tr>
<tr class="separator:ga41a980c914021cdb1825316cccc4ee6c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5553c656446d0fb6457fd8853d9ecda4" class="memitem:ga5553c656446d0fb6457fd8853d9ecda4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_set_socket_nonblocking (DBusSocket fd, DBusError *error)</td>
</tr>
<tr class="memdesc:ga5553c656446d0fb6457fd8853d9ecda4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets a file descriptor to be nonblocking.<br />
</td>
</tr>
<tr class="separator:ga5553c656446d0fb6457fd8853d9ecda4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa2c43bfbfbddd0873737170ff7814ec1" class="memitem:gaa2c43bfbfbddd0873737170ff7814ec1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_close_socket (DBusSocket *fd, DBusError *error)</td>
</tr>
<tr class="memdesc:gaa2c43bfbfbddd0873737170ff7814ec1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Closes a socket and invalidates it.<br />
</td>
</tr>
<tr class="separator:gaa2c43bfbfbddd0873737170ff7814ec1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga20c7b3383854d1cbe38f15e7859bb162" class="memitem:ga20c7b3383854d1cbe38f15e7859bb162">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT int </td>
<td class="memItemRight" data-valign="bottom">_dbus_read_socket (DBusSocket fd, DBusString *buffer, int count)</td>
</tr>
<tr class="memdesc:ga20c7b3383854d1cbe38f15e7859bb162">
<td class="mdescLeft"> </td>
<td class="mdescRight">Like _dbus_read(), but only works on sockets so is available on Windows.<br />
</td>
</tr>
<tr class="separator:ga20c7b3383854d1cbe38f15e7859bb162">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga24bc1f53563e4fa074ce856896ce40dc" class="memitem:ga24bc1f53563e4fa074ce856896ce40dc">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT int </td>
<td class="memItemRight" data-valign="bottom">_dbus_write_socket (DBusSocket fd, const DBusString *buffer, int start, int len)</td>
</tr>
<tr class="memdesc:ga24bc1f53563e4fa074ce856896ce40dc">
<td class="mdescLeft"> </td>
<td class="mdescRight">Like _dbus_write(), but only supports sockets and is thus available on Windows.<br />
</td>
</tr>
<tr class="separator:ga24bc1f53563e4fa074ce856896ce40dc">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabdab5405de96668921721a26e9a387b8" class="memitem:gabdab5405de96668921721a26e9a387b8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_write_socket_two (DBusSocket fd, const DBusString *buffer1, int start1, int len1, const DBusString *buffer2, int start2, int len2)</td>
</tr>
<tr class="memdesc:gabdab5405de96668921721a26e9a387b8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Like _dbus_write_two() but only works on sockets and is thus available on Windows.<br />
</td>
</tr>
<tr class="separator:gabdab5405de96668921721a26e9a387b8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga302dc35ae1e736fc56617a65555ab314" class="memitem:ga302dc35ae1e736fc56617a65555ab314">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_read_socket_with_unix_fds (DBusSocket fd, DBusString *buffer, int count, int *fds, unsigned int *n_fds)</td>
</tr>
<tr class="memdesc:ga302dc35ae1e736fc56617a65555ab314">
<td class="mdescLeft"> </td>
<td class="mdescRight">Like _dbus_read_socket() but also tries to read unix fds from the socket.<br />
</td>
</tr>
<tr class="separator:ga302dc35ae1e736fc56617a65555ab314">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad988ed5d7a172952fee4a5b267b94708" class="memitem:gad988ed5d7a172952fee4a5b267b94708">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT int </td>
<td class="memItemRight" data-valign="bottom">_dbus_write_socket_with_unix_fds (DBusSocket fd, const DBusString *buffer, int start, int len, const int *fds, int n_fds)</td>
</tr>
<tr class="separator:gad988ed5d7a172952fee4a5b267b94708">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gafb0eff5e6f29e727d77f249531281d26" class="memitem:gafb0eff5e6f29e727d77f249531281d26">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_write_socket_with_unix_fds_two (DBusSocket fd, const DBusString *buffer1, int start1, int len1, const DBusString *buffer2, int start2, int len2, const int *fds, int n_fds)</td>
</tr>
<tr class="separator:gafb0eff5e6f29e727d77f249531281d26">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5be199cbcaca9cec2f6680ae487dd91a" class="memitem:ga5be199cbcaca9cec2f6680ae487dd91a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusSocket </td>
<td class="memItemRight" data-valign="bottom">_dbus_connect_tcp_socket (const char *host, const char *port, const char *family, DBusError *error)</td>
</tr>
<tr class="memdesc:ga5be199cbcaca9cec2f6680ae487dd91a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a socket and connects to a socket at the given host and port.<br />
</td>
</tr>
<tr class="separator:ga5be199cbcaca9cec2f6680ae487dd91a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaec2e23cd930512ceec30f9c1bfcc5571" class="memitem:gaec2e23cd930512ceec30f9c1bfcc5571">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusSocket </td>
<td class="memItemRight" data-valign="bottom">_dbus_connect_tcp_socket_with_nonce (const char *host, const char *port, const char *family, const char *noncefile, DBusError *error)</td>
</tr>
<tr class="separator:gaec2e23cd930512ceec30f9c1bfcc5571">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga98387537c13817487010f0f4bcb198f8" class="memitem:ga98387537c13817487010f0f4bcb198f8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_listen_tcp_socket (const char *host, const char *port, const char *family, DBusString *retport, const char **retfamily, DBusSocket **fds_p, DBusError *error)</td>
</tr>
<tr class="memdesc:ga98387537c13817487010f0f4bcb198f8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a socket and binds it to the given path, then listens on the socket.<br />
</td>
</tr>
<tr class="separator:ga98387537c13817487010f0f4bcb198f8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gadeb52ef1d93e91abdc3661bf6db03926" class="memitem:gadeb52ef1d93e91abdc3661bf6db03926">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusSocket </td>
<td class="memItemRight" data-valign="bottom">_dbus_accept (DBusSocket listen_fd)</td>
</tr>
<tr class="memdesc:gadeb52ef1d93e91abdc3661bf6db03926">
<td class="mdescLeft"> </td>
<td class="mdescRight">Accepts a connection on a listening socket.<br />
</td>
</tr>
<tr class="separator:gadeb52ef1d93e91abdc3661bf6db03926">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4bf66f04742727fe68f620ad99590091" class="memitem:ga4bf66f04742727fe68f620ad99590091">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_read_credentials_socket (DBusSocket client_fd, DBusCredentials *credentials, DBusError *error)</td>
</tr>
<tr class="memdesc:ga4bf66f04742727fe68f620ad99590091">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reads a single byte which must be nul (an error occurs otherwise), and reads unix credentials if available.<br />
</td>
</tr>
<tr class="separator:ga4bf66f04742727fe68f620ad99590091">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9a059bb96163b948f41cf427f23a2c91" class="memitem:ga9a059bb96163b948f41cf427f23a2c91">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_send_credentials_socket (DBusSocket server_fd, DBusError *error)</td>
</tr>
<tr class="memdesc:ga9a059bb96163b948f41cf427f23a2c91">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sends a single nul byte with our UNIX credentials as ancillary data.<br />
</td>
</tr>
<tr class="separator:ga9a059bb96163b948f41cf427f23a2c91">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5b480c61a00094aad60d0c8bb9126c1e" class="memitem:ga5b480c61a00094aad60d0c8bb9126c1e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_add_from_user (DBusCredentials *credentials, const DBusString *username, DBusCredentialsAddFlags flags, DBusError *error)</td>
</tr>
<tr class="memdesc:ga5b480c61a00094aad60d0c8bb9126c1e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Adds the credentials corresponding to the given username.<br />
</td>
</tr>
<tr class="separator:ga5b480c61a00094aad60d0c8bb9126c1e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9d5493f8bd1c5577060c8c6dce44d09f" class="memitem:ga9d5493f8bd1c5577060c8c6dce44d09f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_add_from_current_process (DBusCredentials *credentials)</td>
</tr>
<tr class="memdesc:ga9d5493f8bd1c5577060c8c6dce44d09f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Adds the most important credentials of the current process (the uid and pid) to the passed-in credentials object.<br />
</td>
</tr>
<tr class="separator:ga9d5493f8bd1c5577060c8c6dce44d09f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae3f3a437c681c0855bbba80c162d29eb" class="memitem:gae3f3a437c681c0855bbba80c162d29eb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_append_user_from_current_process (DBusString *str)</td>
</tr>
<tr class="memdesc:gae3f3a437c681c0855bbba80c162d29eb">
<td class="mdescLeft"> </td>
<td class="mdescRight">Append to the string the identity we would like to have when we authenticate, on UNIX this is the current process UID and on Windows something else, probably a Windows SID string.<br />
</td>
</tr>
<tr class="separator:gae3f3a437c681c0855bbba80c162d29eb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga437470fc327b0169fc14a0b66a6e5278" class="memitem:ga437470fc327b0169fc14a0b66a6e5278">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_parse_unix_user_from_config (const DBusString *username, dbus_uid_t *uid_p)</td>
</tr>
<tr class="memdesc:ga437470fc327b0169fc14a0b66a6e5278">
<td class="mdescLeft"> </td>
<td class="mdescRight">Parse a UNIX user from the bus config file.<br />
</td>
</tr>
<tr class="separator:ga437470fc327b0169fc14a0b66a6e5278">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga96da816095ec7fec07136a6019745bcb" class="memitem:ga96da816095ec7fec07136a6019745bcb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_parse_unix_group_from_config (const DBusString *groupname, dbus_gid_t *gid_p)</td>
</tr>
<tr class="memdesc:ga96da816095ec7fec07136a6019745bcb">
<td class="mdescLeft"> </td>
<td class="mdescRight">Parse a UNIX group from the bus config file.<br />
</td>
</tr>
<tr class="separator:ga96da816095ec7fec07136a6019745bcb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9abae6dadad0773206dca0519c5b3c9c" class="memitem:ga9abae6dadad0773206dca0519c5b3c9c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_unix_groups_from_uid (dbus_uid_t uid, dbus_gid_t **group_ids, int *n_group_ids, DBusError *error)</td>
</tr>
<tr class="memdesc:ga9abae6dadad0773206dca0519c5b3c9c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets all groups corresponding to the given UNIX user ID.<br />
</td>
</tr>
<tr class="separator:ga9abae6dadad0773206dca0519c5b3c9c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaed2e025454364fbe31cd9b6538c9a936" class="memitem:gaed2e025454364fbe31cd9b6538c9a936">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_unix_user_is_at_console (dbus_uid_t uid, DBusError *error)</td>
</tr>
<tr class="memdesc:gaed2e025454364fbe31cd9b6538c9a936">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks to see if the UNIX user ID is at the console.<br />
</td>
</tr>
<tr class="separator:gaed2e025454364fbe31cd9b6538c9a936">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga849177164bc5e73435104f57c631ed7e" class="memitem:ga849177164bc5e73435104f57c631ed7e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_unix_user_is_process_owner (dbus_uid_t uid)</td>
</tr>
<tr class="memdesc:ga849177164bc5e73435104f57c631ed7e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks to see if the UNIX user ID matches the UID of the process.<br />
</td>
</tr>
<tr class="separator:ga849177164bc5e73435104f57c631ed7e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga912d34a7e40b3a57864972e6d6ab65ba" class="memitem:ga912d34a7e40b3a57864972e6d6ab65ba">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_windows_user_is_process_owner (const char *windows_sid)</td>
</tr>
<tr class="memdesc:ga912d34a7e40b3a57864972e6d6ab65ba">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks to see if the Windows user SID matches the owner of the process.<br />
</td>
</tr>
<tr class="separator:ga912d34a7e40b3a57864972e6d6ab65ba">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3cc5a5734416858fa58f3166ed181a64" class="memitem:ga3cc5a5734416858fa58f3166ed181a64">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_append_keyring_directory_for_credentials (DBusString *directory, DBusCredentials *credentials)</td>
</tr>
<tr class="memdesc:ga3cc5a5734416858fa58f3166ed181a64">
<td class="mdescLeft"> </td>
<td class="mdescRight">Appends the directory in which a keyring for the given credentials should be stored.<br />
</td>
</tr>
<tr class="separator:ga3cc5a5734416858fa58f3166ed181a64">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga958ec7123df36d431ddb07ba18e25cee" class="memitem:ga958ec7123df36d431ddb07ba18e25cee">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_daemon_unpublish_session_bus_address (void)</td>
</tr>
<tr class="memdesc:ga958ec7123df36d431ddb07ba18e25cee">
<td class="mdescLeft"> </td>
<td class="mdescRight">Clear the platform-specific centralized location where the session bus address is published.<br />
</td>
</tr>
<tr class="separator:ga958ec7123df36d431ddb07ba18e25cee">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2435088cc87a541290b6c8150bfb8afb" class="memitem:ga2435088cc87a541290b6c8150bfb8afb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_socket_can_pass_unix_fd (DBusSocket fd)</td>
</tr>
<tr class="memdesc:ga2435088cc87a541290b6c8150bfb8afb">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether file descriptors may be passed via the socket.<br />
</td>
</tr>
<tr class="separator:ga2435088cc87a541290b6c8150bfb8afb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7dbdeaecd3e6780e661566b03597feff" class="memitem:ga7dbdeaecd3e6780e661566b03597feff">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT dbus_pid_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_resolve_pid_fd (int pid_fd)</td>
</tr>
<tr class="memdesc:ga7dbdeaecd3e6780e661566b03597feff">
<td class="mdescLeft"> </td>
<td class="mdescRight">Resolve the PID from the PID FD, if any.<br />
</td>
</tr>
<tr class="separator:ga7dbdeaecd3e6780e661566b03597feff">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa479b9fc0d2bb007667654d07452344e" class="memitem:gaa479b9fc0d2bb007667654d07452344e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT dbus_int32_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_atomic_inc (DBusAtomic *atomic)</td>
</tr>
<tr class="memdesc:gaa479b9fc0d2bb007667654d07452344e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Atomically increments an integer.<br />
</td>
</tr>
<tr class="separator:gaa479b9fc0d2bb007667654d07452344e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga43a4376739482af393f8719b428f529b" class="memitem:ga43a4376739482af393f8719b428f529b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT dbus_int32_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_atomic_dec (DBusAtomic *atomic)</td>
</tr>
<tr class="memdesc:ga43a4376739482af393f8719b428f529b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Atomically decrement an integer.<br />
</td>
</tr>
<tr class="separator:ga43a4376739482af393f8719b428f529b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga54efe0662d88aa9fffb9b5d92dcfd7a1" class="memitem:ga54efe0662d88aa9fffb9b5d92dcfd7a1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT dbus_int32_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_atomic_get (DBusAtomic *atomic)</td>
</tr>
<tr class="memdesc:ga54efe0662d88aa9fffb9b5d92dcfd7a1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Atomically get the value of an integer.<br />
</td>
</tr>
<tr class="separator:ga54efe0662d88aa9fffb9b5d92dcfd7a1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa416b00e48307950b3fe0476bf353247" class="memitem:gaa416b00e48307950b3fe0476bf353247">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT void </td>
<td class="memItemRight" data-valign="bottom">_dbus_atomic_set_zero (DBusAtomic *atomic)</td>
</tr>
<tr class="memdesc:gaa416b00e48307950b3fe0476bf353247">
<td class="mdescLeft"> </td>
<td class="mdescRight">Atomically set the value of an integer to 0.<br />
</td>
</tr>
<tr class="separator:gaa416b00e48307950b3fe0476bf353247">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga26fb23709d57a52f03ac1fefa9f54bde" class="memitem:ga26fb23709d57a52f03ac1fefa9f54bde">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT void </td>
<td class="memItemRight" data-valign="bottom">_dbus_atomic_set_nonzero (DBusAtomic *atomic)</td>
</tr>
<tr class="memdesc:ga26fb23709d57a52f03ac1fefa9f54bde">
<td class="mdescLeft"> </td>
<td class="mdescRight">Atomically set the value of an integer to something nonzero.<br />
</td>
</tr>
<tr class="separator:ga26fb23709d57a52f03ac1fefa9f54bde">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab9cd554d4947888a79695e776b57e6b5" class="memitem:gab9cd554d4947888a79695e776b57e6b5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT int </td>
<td class="memItemRight" data-valign="bottom">_dbus_poll (DBusPollFD *fds, int n_fds, int timeout_milliseconds)</td>
</tr>
<tr class="memdesc:gab9cd554d4947888a79695e776b57e6b5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Wrapper for poll().<br />
</td>
</tr>
<tr class="separator:gab9cd554d4947888a79695e776b57e6b5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga71be9d447d11a9dbea6474467c563310" class="memitem:ga71be9d447d11a9dbea6474467c563310">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT void </td>
<td class="memItemRight" data-valign="bottom">_dbus_sleep_milliseconds (int milliseconds)</td>
</tr>
<tr class="memdesc:ga71be9d447d11a9dbea6474467c563310">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sleeps the given number of milliseconds.<br />
</td>
</tr>
<tr class="separator:ga71be9d447d11a9dbea6474467c563310">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga04ec07c3aa9c1ecf48fffc9d41231ccd" class="memitem:ga04ec07c3aa9c1ecf48fffc9d41231ccd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT void </td>
<td class="memItemRight" data-valign="bottom">_dbus_get_monotonic_time (dbus_int64_t *tv_sec, long *tv_usec)</td>
</tr>
<tr class="memdesc:ga04ec07c3aa9c1ecf48fffc9d41231ccd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Get current time, as in gettimeofday().<br />
</td>
</tr>
<tr class="separator:ga04ec07c3aa9c1ecf48fffc9d41231ccd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad6a33737e744fa4702c2a3ea7d2ecfbd" class="memitem:gad6a33737e744fa4702c2a3ea7d2ecfbd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT void </td>
<td class="memItemRight" data-valign="bottom">_dbus_get_real_time (dbus_int64_t *tv_sec, long *tv_usec)</td>
</tr>
<tr class="memdesc:gad6a33737e744fa4702c2a3ea7d2ecfbd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Get current time, as in gettimeofday().<br />
</td>
</tr>
<tr class="separator:gad6a33737e744fa4702c2a3ea7d2ecfbd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gafc2b9826e24bac893de24261343de158" class="memitem:gafc2b9826e24bac893de24261343de158">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_create_directory (const DBusString *filename, DBusError *error)</td>
</tr>
<tr class="memdesc:gafc2b9826e24bac893de24261343de158">
<td class="mdescLeft"> </td>
<td class="mdescRight">directory interface<br />
</td>
</tr>
<tr class="separator:gafc2b9826e24bac893de24261343de158">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf5e6ed5a1ba2cd57ebf4c3f1bd2ee503" class="memitem:gaf5e6ed5a1ba2cd57ebf4c3f1bd2ee503">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_ensure_directory (const DBusString *filename, DBusError *error)</td>
</tr>
<tr class="memdesc:gaf5e6ed5a1ba2cd57ebf4c3f1bd2ee503">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a directory; succeeds if the directory is created or already existed.<br />
</td>
</tr>
<tr class="separator:gaf5e6ed5a1ba2cd57ebf4c3f1bd2ee503">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab55075f15b5e4bd1005eae990bf03f09" class="memitem:gab55075f15b5e4bd1005eae990bf03f09">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_delete_directory (const DBusString *filename, DBusError *error)</td>
</tr>
<tr class="memdesc:gab55075f15b5e4bd1005eae990bf03f09">
<td class="mdescLeft"> </td>
<td class="mdescRight">Removes a directory; Directory must be empty.<br />
</td>
</tr>
<tr class="separator:gab55075f15b5e4bd1005eae990bf03f09">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac68145a202b8214fa08dff79df803a5b" class="memitem:gac68145a202b8214fa08dff79df803a5b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_concat_dir_and_file (DBusString *dir, const DBusString *next_component)</td>
</tr>
<tr class="memdesc:gac68145a202b8214fa08dff79df803a5b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Appends the given filename to the given directory.<br />
</td>
</tr>
<tr class="separator:gac68145a202b8214fa08dff79df803a5b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gafa79c1113fa75419dcc5ee4290e06608" class="memitem:gafa79c1113fa75419dcc5ee4290e06608">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_get_dirname (const DBusString *filename, DBusString *dirname)</td>
</tr>
<tr class="memdesc:gafa79c1113fa75419dcc5ee4290e06608">
<td class="mdescLeft"> </td>
<td class="mdescRight">Get the directory name from a complete filename.<br />
</td>
</tr>
<tr class="separator:gafa79c1113fa75419dcc5ee4290e06608">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gafb107a5c05ace8b35777eb2f0c5d680f" class="memitem:gafb107a5c05ace8b35777eb2f0c5d680f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_path_is_absolute (const DBusString *filename)</td>
</tr>
<tr class="memdesc:gafb107a5c05ace8b35777eb2f0c5d680f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether the filename is an absolute path.<br />
</td>
</tr>
<tr class="separator:gafb107a5c05ace8b35777eb2f0c5d680f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga079d34a9d90759e6b3ebebab424c696e" class="memitem:ga079d34a9d90759e6b3ebebab424c696e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_get_standard_session_servicedirs (DBusList **dirs)</td>
</tr>
<tr class="memdesc:ga079d34a9d90759e6b3ebebab424c696e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns the standard directories for a session bus to look for service activation files.<br />
</td>
</tr>
<tr class="separator:ga079d34a9d90759e6b3ebebab424c696e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5193160c3dc144af34b250cfb5b0a61e" class="memitem:ga5193160c3dc144af34b250cfb5b0a61e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_get_standard_system_servicedirs (DBusList **dirs)</td>
</tr>
<tr class="memdesc:ga5193160c3dc144af34b250cfb5b0a61e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns the standard directories for a system bus to look for service activation files.<br />
</td>
</tr>
<tr class="separator:ga5193160c3dc144af34b250cfb5b0a61e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5198615b5a0fdb19e779eb3ce76bd35f" class="memitem:ga5198615b5a0fdb19e779eb3ce76bd35f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_get_local_system_servicedirs (DBusList **dirs)</td>
</tr>
<tr class="memdesc:ga5198615b5a0fdb19e779eb3ce76bd35f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns the local admin directories for a system bus to look for service activation files.<br />
</td>
</tr>
<tr class="separator:ga5198615b5a0fdb19e779eb3ce76bd35f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3889d6db3fc21905018cbe9e99dd92ba" class="memitem:ga3889d6db3fc21905018cbe9e99dd92ba">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_set_up_transient_session_servicedirs (DBusList **dirs, DBusError *error)</td>
</tr>
<tr class="memdesc:ga3889d6db3fc21905018cbe9e99dd92ba">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns the standard directories for a session bus to look for transient service activation files.<br />
</td>
</tr>
<tr class="separator:ga3889d6db3fc21905018cbe9e99dd92ba">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga37277778e62ee8d3153a01e1b26e84b4" class="memitem:ga37277778e62ee8d3153a01e1b26e84b4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_get_system_config_file (DBusString *str)</td>
</tr>
<tr class="memdesc:ga37277778e62ee8d3153a01e1b26e84b4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Get the absolute path of the system.conf file (there is no system bus on Windows so this can just return FALSE and print a warning or something)<br />
</td>
</tr>
<tr class="separator:ga37277778e62ee8d3153a01e1b26e84b4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1e2f599317b9a5cbf802f4472db1de55" class="memitem:ga1e2f599317b9a5cbf802f4472db1de55">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_get_session_config_file (DBusString *str)</td>
</tr>
<tr class="memdesc:ga1e2f599317b9a5cbf802f4472db1de55">
<td class="mdescLeft"> </td>
<td class="mdescRight">Get the absolute path of the session.conf file.<br />
</td>
</tr>
<tr class="separator:ga1e2f599317b9a5cbf802f4472db1de55">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga387d7e6643322c9813b62edf441bf13e" class="memitem:ga387d7e6643322c9813b62edf441bf13e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusDirIter * </td>
<td class="memItemRight" data-valign="bottom">_dbus_directory_open (const DBusString *filename, DBusError *error)</td>
</tr>
<tr class="memdesc:ga387d7e6643322c9813b62edf441bf13e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Open a directory to iterate over.<br />
</td>
</tr>
<tr class="separator:ga387d7e6643322c9813b62edf441bf13e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab9a2ddb130da035d6186f2d96bf37cb4" class="memitem:gab9a2ddb130da035d6186f2d96bf37cb4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_directory_get_next_file (DBusDirIter *iter, DBusString *filename, DBusError *error)</td>
</tr>
<tr class="memdesc:gab9a2ddb130da035d6186f2d96bf37cb4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Get next file in the directory.<br />
</td>
</tr>
<tr class="separator:gab9a2ddb130da035d6186f2d96bf37cb4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1821b64302fe8e12278fa227eb11d393" class="memitem:ga1821b64302fe8e12278fa227eb11d393">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_directory_close (DBusDirIter *iter)</td>
</tr>
<tr class="memdesc:ga1821b64302fe8e12278fa227eb11d393">
<td class="mdescLeft"> </td>
<td class="mdescRight">Closes a directory iteration.<br />
</td>
</tr>
<tr class="separator:ga1821b64302fe8e12278fa227eb11d393">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8e16f75e361d9fed43223f69baf0e2a5" class="memitem:ga8e16f75e361d9fed43223f69baf0e2a5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_check_dir_is_private_to_user (DBusString *dir, DBusError *error)</td>
</tr>
<tr class="memdesc:ga8e16f75e361d9fed43223f69baf0e2a5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks to make sure the given directory is private to the user.<br />
</td>
</tr>
<tr class="separator:ga8e16f75e361d9fed43223f69baf0e2a5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf24436b3d08b2ed74c5f49500a95cb7c" class="memitem:gaf24436b3d08b2ed74c5f49500a95cb7c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT const char * </td>
<td class="memItemRight" data-valign="bottom">_dbus_get_tmpdir (void)</td>
</tr>
<tr class="memdesc:gaf24436b3d08b2ed74c5f49500a95cb7c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the temporary files directory by inspecting the environment variables TMPDIR, TMP, and TEMP in that order.<br />
</td>
</tr>
<tr class="separator:gaf24436b3d08b2ed74c5f49500a95cb7c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1a0a518569d7fcb9e07d80f273c07aba" class="memitem:ga1a0a518569d7fcb9e07d80f273c07aba">
<td class="memItemLeft" style="text-align: right;" data-valign="top">_DBUS_WARN_UNUSED_RESULT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_generate_random_bytes_buffer (char *buffer, int n_bytes, DBusError *error)</td>
</tr>
<tr class="memdesc:ga1a0a518569d7fcb9e07d80f273c07aba">
<td class="mdescLeft"> </td>
<td class="mdescRight">Random numbers.<br />
</td>
</tr>
<tr class="separator:ga1a0a518569d7fcb9e07d80f273c07aba">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa6d0c743bc5998a90106868c898f989c" class="memitem:gaa6d0c743bc5998a90106868c898f989c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_generate_random_bytes (DBusString *str, int n_bytes, DBusError *error)</td>
</tr>
<tr class="memdesc:gaa6d0c743bc5998a90106868c898f989c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Generates the given number of securely random bytes, using the best mechanism we can come up with.<br />
</td>
</tr>
<tr class="separator:gaa6d0c743bc5998a90106868c898f989c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabc0605d3ac09cc58158994791e950f37" class="memitem:gabc0605d3ac09cc58158994791e950f37">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_generate_random_ascii (DBusString *str, int n_bytes, DBusError *error)</td>
</tr>
<tr class="memdesc:gabc0605d3ac09cc58158994791e950f37">
<td class="mdescLeft"> </td>
<td class="mdescRight">Generates the given number of random bytes, where the bytes are chosen from the alphanumeric ASCII subset.<br />
</td>
</tr>
<tr class="separator:gabc0605d3ac09cc58158994791e950f37">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab74adea5e6ceede8e539273fe51387bb" class="memitem:gab74adea5e6ceede8e539273fe51387bb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT const char * </td>
<td class="memItemRight" data-valign="bottom">_dbus_error_from_errno (int error_number)</td>
</tr>
<tr class="memdesc:gab74adea5e6ceede8e539273fe51387bb">
<td class="mdescLeft"> </td>
<td class="mdescRight">Converts a UNIX errno, or Windows errno or WinSock error value into a DBusError name.<br />
</td>
</tr>
<tr class="separator:gab74adea5e6ceede8e539273fe51387bb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5a7e28bf9dea864c09e5fd23e1e8636e" class="memitem:ga5a7e28bf9dea864c09e5fd23e1e8636e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT const char * </td>
<td class="memItemRight" data-valign="bottom">_dbus_error_from_system_errno (void)</td>
</tr>
<tr class="memdesc:ga5a7e28bf9dea864c09e5fd23e1e8636e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Converts the current system errno value into a DBusError name.<br />
</td>
</tr>
<tr class="separator:ga5a7e28bf9dea864c09e5fd23e1e8636e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8c0af1705d7417873cee0e23ecc51b14" class="memitem:ga8c0af1705d7417873cee0e23ecc51b14">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_get_low_level_socket_errno (void)</td>
</tr>
<tr class="separator:ga8c0af1705d7417873cee0e23ecc51b14">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf80b18a5eff6d59c15f66029be352c8a" class="memitem:gaf80b18a5eff6d59c15f66029be352c8a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_save_socket_errno (void)</td>
</tr>
<tr class="separator:gaf80b18a5eff6d59c15f66029be352c8a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga618db839cc75653ba05d6b5871049007" class="memitem:ga618db839cc75653ba05d6b5871049007">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_restore_socket_errno (int saved_errno)</td>
</tr>
<tr class="separator:ga618db839cc75653ba05d6b5871049007">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf0f4cb7f145fe1f48f5302277560407a" class="memitem:gaf0f4cb7f145fe1f48f5302277560407a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_set_errno_to_zero (void)</td>
</tr>
<tr class="memdesc:gaf0f4cb7f145fe1f48f5302277560407a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Assign 0 to the global errno variable.<br />
</td>
</tr>
<tr class="separator:gaf0f4cb7f145fe1f48f5302277560407a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1895e860a4a9993cea584ec7e30dd71d" class="memitem:ga1895e860a4a9993cea584ec7e30dd71d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_get_is_errno_eagain_or_ewouldblock (int e)</td>
</tr>
<tr class="memdesc:ga1895e860a4a9993cea584ec7e30dd71d">
<td class="mdescLeft"> </td>
<td class="mdescRight">See if errno is EAGAIN or EWOULDBLOCK (this has to be done differently for Winsock so is abstracted)<br />
</td>
</tr>
<tr class="separator:ga1895e860a4a9993cea584ec7e30dd71d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf8962f4044a2a8689eb95a0ffd08b837" class="memitem:gaf8962f4044a2a8689eb95a0ffd08b837">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_get_is_errno_enomem (int e)</td>
</tr>
<tr class="memdesc:gaf8962f4044a2a8689eb95a0ffd08b837">
<td class="mdescLeft"> </td>
<td class="mdescRight">See if errno is ENOMEM.<br />
</td>
</tr>
<tr class="separator:gaf8962f4044a2a8689eb95a0ffd08b837">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae638e92d9bbeef287421a0f2d5837b9a" class="memitem:gae638e92d9bbeef287421a0f2d5837b9a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_get_is_errno_eintr (int e)</td>
</tr>
<tr class="memdesc:gae638e92d9bbeef287421a0f2d5837b9a">
<td class="mdescLeft"> </td>
<td class="mdescRight">See if errno is EINTR.<br />
</td>
</tr>
<tr class="separator:gae638e92d9bbeef287421a0f2d5837b9a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga07d3d26556b75d728fd1755baddb0792" class="memitem:ga07d3d26556b75d728fd1755baddb0792">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_get_is_errno_epipe (int e)</td>
</tr>
<tr class="memdesc:ga07d3d26556b75d728fd1755baddb0792">
<td class="mdescLeft"> </td>
<td class="mdescRight">See if errno is EPIPE.<br />
</td>
</tr>
<tr class="separator:ga07d3d26556b75d728fd1755baddb0792">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0e84d22f6cc293eef3c4f4f465ef1d9f" class="memitem:ga0e84d22f6cc293eef3c4f4f465ef1d9f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_get_is_errno_etoomanyrefs (int e)</td>
</tr>
<tr class="memdesc:ga0e84d22f6cc293eef3c4f4f465ef1d9f">
<td class="mdescLeft"> </td>
<td class="mdescRight">See if errno is ETOOMANYREFS.<br />
</td>
</tr>
<tr class="separator:ga0e84d22f6cc293eef3c4f4f465ef1d9f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8a219ee7a8a8c929cfd393f50930335d" class="memitem:ga8a219ee7a8a8c929cfd393f50930335d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT const char * </td>
<td class="memItemRight" data-valign="bottom">_dbus_strerror_from_errno (void)</td>
</tr>
<tr class="memdesc:ga8a219ee7a8a8c929cfd393f50930335d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Get error message from errno.<br />
</td>
</tr>
<tr class="separator:ga8a219ee7a8a8c929cfd393f50930335d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6890d4cde3afec0bf274ca2af8c9e204" class="memitem:ga6890d4cde3afec0bf274ca2af8c9e204">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_disable_sigpipe (void)</td>
</tr>
<tr class="memdesc:ga6890d4cde3afec0bf274ca2af8c9e204">
<td class="mdescLeft"> </td>
<td class="mdescRight">signal (SIGPIPE, SIG_IGN);<br />
</td>
</tr>
<tr class="separator:ga6890d4cde3afec0bf274ca2af8c9e204">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga22caa89bafef37be114d5d4762a82cbc" class="memitem:ga22caa89bafef37be114d5d4762a82cbc">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT void </td>
<td class="memItemRight" data-valign="bottom">_dbus_exit (int code) _DBUS_GNUC_NORETURN</td>
</tr>
<tr class="memdesc:ga22caa89bafef37be114d5d4762a82cbc">
<td class="mdescLeft"> </td>
<td class="mdescRight">Exit the process, returning the given value.<br />
</td>
</tr>
<tr class="separator:ga22caa89bafef37be114d5d4762a82cbc">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaab04975b7eadfe5744f11b4682bb46b4" class="memitem:gaab04975b7eadfe5744f11b4682bb46b4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT int </td>
<td class="memItemRight" data-valign="bottom">_dbus_printf_string_upper_bound (const char *format, va_list args)</td>
</tr>
<tr class="memdesc:gaab04975b7eadfe5744f11b4682bb46b4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Measure the length of the given format string and arguments, not including the terminating nul.<br />
</td>
</tr>
<tr class="separator:gaab04975b7eadfe5744f11b4682bb46b4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga04e98ad0e3a181f0a5921a4cbc49cf08" class="memitem:ga04e98ad0e3a181f0a5921a4cbc49cf08">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_stat (const DBusString *filename, DBusStat *statbuf, DBusError *error)</td>
</tr>
<tr class="memdesc:ga04e98ad0e3a181f0a5921a4cbc49cf08">
<td class="mdescLeft"> </td>
<td class="mdescRight">stat() wrapper.<br />
</td>
</tr>
<tr class="separator:ga04e98ad0e3a181f0a5921a4cbc49cf08">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa2d99d36c96caaee2084d8c11cb97a55" class="memitem:gaa2d99d36c96caaee2084d8c11cb97a55">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusSocket </td>
<td class="memItemRight" data-valign="bottom">_dbus_connect_unix_socket (const char *path, dbus_bool_t abstract, DBusError *error)</td>
</tr>
<tr class="memdesc:gaa2d99d36c96caaee2084d8c11cb97a55">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a socket and connects it to the UNIX domain socket at the given path.<br />
</td>
</tr>
<tr class="separator:gaa2d99d36c96caaee2084d8c11cb97a55">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga50da823288d41a2ca3944a25247f7aad" class="memitem:ga50da823288d41a2ca3944a25247f7aad">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusSocket </td>
<td class="memItemRight" data-valign="bottom">_dbus_listen_unix_socket (const char *path, dbus_bool_t abstract, DBusError *error)</td>
</tr>
<tr class="memdesc:ga50da823288d41a2ca3944a25247f7aad">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a socket and binds it to the given path, then listens on the socket.<br />
</td>
</tr>
<tr class="separator:ga50da823288d41a2ca3944a25247f7aad">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gacaea998a9735beca9218c369b9ed1436" class="memitem:gacaea998a9735beca9218c369b9ed1436">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusSocket </td>
<td class="memItemRight" data-valign="bottom">_dbus_connect_exec (const char *path, char *const argv[], DBusError *error)</td>
</tr>
<tr class="memdesc:gacaea998a9735beca9218c369b9ed1436">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a UNIX domain socket and connects it to the specified process to execute.<br />
</td>
</tr>
<tr class="separator:gacaea998a9735beca9218c369b9ed1436">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2941154fe6dce846bf4e5c4ce1c4e085" class="memitem:ga2941154fe6dce846bf4e5c4ce1c4e085">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_socketpair (DBusSocket *fd1, DBusSocket *fd2, dbus_bool_t blocking, DBusError *error)</td>
</tr>
<tr class="memdesc:ga2941154fe6dce846bf4e5c4ce1c4e085">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates pair of connect sockets (as in socketpair()).<br />
</td>
</tr>
<tr class="separator:ga2941154fe6dce846bf4e5c4ce1c4e085">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad56615fd263913cf88042782598d383e" class="memitem:gad56615fd263913cf88042782598d383e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT void </td>
<td class="memItemRight" data-valign="bottom">_dbus_print_backtrace (void)</td>
</tr>
<tr class="memdesc:gad56615fd263913cf88042782598d383e">
<td class="mdescLeft"> </td>
<td class="mdescRight">On GNU libc systems, print a crude backtrace to stderr.<br />
</td>
</tr>
<tr class="separator:gad56615fd263913cf88042782598d383e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaca61af8681a48862835ea8cfd263f5ab" class="memitem:gaca61af8681a48862835ea8cfd263f5ab">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_become_daemon (const DBusString *pidfile, DBusPipe *print_pid_pipe, DBusError *error, dbus_bool_t keep_umask)</td>
</tr>
<tr class="memdesc:gaca61af8681a48862835ea8cfd263f5ab">
<td class="mdescLeft"> </td>
<td class="mdescRight">Does the chdir, fork, setsid, etc.<br />
</td>
</tr>
<tr class="separator:gaca61af8681a48862835ea8cfd263f5ab">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga45f661c5a089ed45233a1acabaf31964" class="memitem:ga45f661c5a089ed45233a1acabaf31964">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_verify_daemon_user (const char *user)</td>
</tr>
<tr class="memdesc:ga45f661c5a089ed45233a1acabaf31964">
<td class="mdescLeft"> </td>
<td class="mdescRight">Verify that after the fork we can successfully change to this user.<br />
</td>
</tr>
<tr class="separator:ga45f661c5a089ed45233a1acabaf31964">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga82c920a8c3b5958ba1ecf8e5f5d6373b" class="memitem:ga82c920a8c3b5958ba1ecf8e5f5d6373b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_change_to_daemon_user (const char *user, DBusError *error)</td>
</tr>
<tr class="memdesc:ga82c920a8c3b5958ba1ecf8e5f5d6373b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Changes the user and group the bus is running as.<br />
</td>
</tr>
<tr class="separator:ga82c920a8c3b5958ba1ecf8e5f5d6373b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga123620ec5ce2b881786588121d6a03fd" class="memitem:ga123620ec5ce2b881786588121d6a03fd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_write_pid_to_file_and_pipe (const DBusString *pidfile, DBusPipe *print_pid_pipe, dbus_pid_t pid_to_write, DBusError *error)</td>
</tr>
<tr class="memdesc:ga123620ec5ce2b881786588121d6a03fd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Writes the given pid_to_write to a pidfile (if non-NULL) and/or to a pipe (if non-NULL).<br />
</td>
</tr>
<tr class="separator:ga123620ec5ce2b881786588121d6a03fd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3551d425aba3d92e652b8809fdfe9339" class="memitem:ga3551d425aba3d92e652b8809fdfe9339">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_command_for_pid (unsigned long pid, DBusString *str, int max_len, DBusError *error)</td>
</tr>
<tr class="memdesc:ga3551d425aba3d92e652b8809fdfe9339">
<td class="mdescLeft"> </td>
<td class="mdescRight">Get a printable string describing the command used to execute the process with pid.<br />
</td>
</tr>
<tr class="separator:ga3551d425aba3d92e652b8809fdfe9339">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gadafb0b04c0b9b00f4c327cafe64bf733" class="memitem:gadafb0b04c0b9b00f4c327cafe64bf733">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT void </td>
<td class="memItemRight" data-valign="bottom">_dbus_init_system_log (const char *tag, DBusLogFlags flags)</td>
</tr>
<tr class="memdesc:gadafb0b04c0b9b00f4c327cafe64bf733">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initialize the system log.<br />
</td>
</tr>
<tr class="separator:gadafb0b04c0b9b00f4c327cafe64bf733">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8f91d051ad57f13d3e2adef79976787d" class="memitem:ga8f91d051ad57f13d3e2adef79976787d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT void </td>
<td class="memItemRight" data-valign="bottom">_dbus_log (DBusSystemLogSeverity severity, const char *msg,...)</td>
</tr>
<tr class="memdesc:ga8f91d051ad57f13d3e2adef79976787d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Log a message to the system log file (e.g.<br />
</td>
</tr>
<tr class="separator:ga8f91d051ad57f13d3e2adef79976787d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga00edf5980729f7086df1d301909dd5d7" class="memitem:ga00edf5980729f7086df1d301909dd5d7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT void </td>
<td class="memItemRight" data-valign="bottom">_dbus_logv (DBusSystemLogSeverity severity, const char *msg, va_list args)</td>
</tr>
<tr class="memdesc:ga00edf5980729f7086df1d301909dd5d7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Log a message to the system log file (e.g.<br />
</td>
</tr>
<tr class="separator:ga00edf5980729f7086df1d301909dd5d7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabc4712c0db91f11854cdd933027355af" class="memitem:gabc4712c0db91f11854cdd933027355af">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_get_autolaunch_address (const char *scope, DBusString *address, DBusError *error)</td>
</tr>
<tr class="memdesc:gabc4712c0db91f11854cdd933027355af">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns the address of a new session bus.<br />
</td>
</tr>
<tr class="separator:gabc4712c0db91f11854cdd933027355af">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga588dbd2f1ff522eaed675606a3c35e15" class="memitem:ga588dbd2f1ff522eaed675606a3c35e15">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_lookup_session_address (dbus_bool_t *supported, DBusString *address, DBusError *error)</td>
</tr>
<tr class="memdesc:ga588dbd2f1ff522eaed675606a3c35e15">
<td class="mdescLeft"> </td>
<td class="mdescRight">Determines the address of the session bus by querying a platform-specific method.<br />
</td>
</tr>
<tr class="separator:ga588dbd2f1ff522eaed675606a3c35e15">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga06115afaa25711728597c48de5b67115" class="memitem:ga06115afaa25711728597c48de5b67115">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_read_local_machine_uuid (DBusGUID *machine_id, dbus_bool_t create_if_not_found, DBusError *error)</td>
</tr>
<tr class="memdesc:ga06115afaa25711728597c48de5b67115">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reads the uuid of the machine we're running on from the dbus configuration.<br />
</td>
</tr>
<tr class="separator:ga06115afaa25711728597c48de5b67115">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae7be34dbffb6458578e86c59a26d4fad" class="memitem:gae7be34dbffb6458578e86c59a26d4fad">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_threads_init_platform_specific (void)</td>
</tr>
<tr class="memdesc:gae7be34dbffb6458578e86c59a26d4fad">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initialize threads as in dbus_threads_init_default(), appropriately for the platform.<br />
</td>
</tr>
<tr class="separator:gae7be34dbffb6458578e86c59a26d4fad">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga65d32daf6d876dd39b7410f3fa35b591" class="memitem:ga65d32daf6d876dd39b7410f3fa35b591">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_threads_lock_platform_specific (void)</td>
</tr>
<tr class="memdesc:ga65d32daf6d876dd39b7410f3fa35b591">
<td class="mdescLeft"> </td>
<td class="mdescRight">Lock a static mutex used to protect _dbus_threads_init_platform_specific().<br />
</td>
</tr>
<tr class="separator:ga65d32daf6d876dd39b7410f3fa35b591">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga99c22b80d17ef18fa0a11f3a2a415403" class="memitem:ga99c22b80d17ef18fa0a11f3a2a415403">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_threads_unlock_platform_specific (void)</td>
</tr>
<tr class="memdesc:ga99c22b80d17ef18fa0a11f3a2a415403">
<td class="mdescLeft"> </td>
<td class="mdescRight">Undo _dbus_threads_lock_platform_specific().<br />
</td>
</tr>
<tr class="separator:ga99c22b80d17ef18fa0a11f3a2a415403">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1b30aa55e8758ed6e1b62e0f86866543" class="memitem:ga1b30aa55e8758ed6e1b62e0f86866543">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned long </td>
<td class="memItemRight" data-valign="bottom">_dbus_pid_for_log (void)</td>
</tr>
<tr class="memdesc:ga1b30aa55e8758ed6e1b62e0f86866543">
<td class="mdescLeft"> </td>
<td class="mdescRight">The only reason this is separate from _dbus_getpid() is to allow it on Windows for logging but not for other purposes.<br />
</td>
</tr>
<tr class="separator:ga1b30aa55e8758ed6e1b62e0f86866543">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga52af1dee1f5aa81e66ab6c1e66eacc73" class="memitem:ga52af1dee1f5aa81e66ab6c1e66eacc73">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT dbus_pid_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_getpid (void)</td>
</tr>
<tr class="memdesc:ga52af1dee1f5aa81e66ab6c1e66eacc73">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets our process ID.<br />
</td>
</tr>
<tr class="separator:ga52af1dee1f5aa81e66ab6c1e66eacc73">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9bc86fe20b84a4b686cbf4bdecd3bbf4" class="memitem:ga9bc86fe20b84a4b686cbf4bdecd3bbf4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT dbus_uid_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_getuid (void)</td>
</tr>
<tr class="memdesc:ga9bc86fe20b84a4b686cbf4bdecd3bbf4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets our UID.<br />
</td>
</tr>
<tr class="separator:ga9bc86fe20b84a4b686cbf4bdecd3bbf4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae5e7d55020906c4c29585765ae9656c8" class="memitem:gae5e7d55020906c4c29585765ae9656c8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT void </td>
<td class="memItemRight" data-valign="bottom">_dbus_flush_caches (void)</td>
</tr>
<tr class="memdesc:gae5e7d55020906c4c29585765ae9656c8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Called when the bus daemon is signaled to reload its configuration; any caches should be nuked.<br />
</td>
</tr>
<tr class="separator:gae5e7d55020906c4c29585765ae9656c8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gadcbd0c5622d28bb94075a43d7d8d51ec" class="memitem:gadcbd0c5622d28bb94075a43d7d8d51ec">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_replace_install_prefix (DBusString *path)</td>
</tr>
<tr class="memdesc:gadcbd0c5622d28bb94075a43d7d8d51ec">
<td class="mdescLeft"> </td>
<td class="mdescRight">Replace the DBUS_PREFIX in the given path, in-place, by the current D-Bus installation directory.<br />
</td>
</tr>
<tr class="separator:gadcbd0c5622d28bb94075a43d7d8d51ec">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5573a7a21c60fcd86c43ae51c10ee4d4" class="memitem:ga5573a7a21c60fcd86c43ae51c10ee4d4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusRLimit * </td>
<td class="memItemRight" data-valign="bottom">_dbus_rlimit_save_fd_limit (DBusError *error)</td>
</tr>
<tr class="separator:ga5573a7a21c60fcd86c43ae51c10ee4d4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad231dff4b9a9f3912a6e1774ceaddb0f" class="memitem:gad231dff4b9a9f3912a6e1774ceaddb0f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_rlimit_raise_fd_limit (DBusError *error)</td>
</tr>
<tr class="separator:gad231dff4b9a9f3912a6e1774ceaddb0f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab87dbd966b0051b7ff916e06e43fcf2e" class="memitem:gab87dbd966b0051b7ff916e06e43fcf2e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_rlimit_restore_fd_limit (DBusRLimit *saved, DBusError *error)</td>
</tr>
<tr class="separator:gab87dbd966b0051b7ff916e06e43fcf2e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga53db90ef9ed40073f1b0821d1589a024" class="memitem:ga53db90ef9ed40073f1b0821d1589a024">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_rlimit_free (DBusRLimit *lim)</td>
</tr>
<tr class="separator:ga53db90ef9ed40073f1b0821d1589a024">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0d03632014dc02a9fe0557e5cf64ed41" class="memitem:ga0d03632014dc02a9fe0557e5cf64ed41">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_daemon_report_ready (void)</td>
</tr>
<tr class="memdesc:ga0d03632014dc02a9fe0557e5cf64ed41">
<td class="mdescLeft"> </td>
<td class="mdescRight">Report to a service manager that the daemon calling this function is ready for use.<br />
</td>
</tr>
<tr class="separator:ga0d03632014dc02a9fe0557e5cf64ed41">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga219320568548166dd419f2d5524cf808" class="memitem:ga219320568548166dd419f2d5524cf808">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_daemon_report_reloading (void)</td>
</tr>
<tr class="memdesc:ga219320568548166dd419f2d5524cf808">
<td class="mdescLeft"> </td>
<td class="mdescRight">Report to a service manager that the daemon calling this function is reloading configuration.<br />
</td>
</tr>
<tr class="separator:ga219320568548166dd419f2d5524cf808">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6f9a6c2146687bdf10e2e77843729de2" class="memitem:ga6f9a6c2146687bdf10e2e77843729de2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_daemon_report_reloaded (void)</td>
</tr>
<tr class="memdesc:ga6f9a6c2146687bdf10e2e77843729de2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Report to a service manager that the daemon calling this function is reloading configuration.<br />
</td>
</tr>
<tr class="separator:ga6f9a6c2146687bdf10e2e77843729de2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9eecdc3dd66afdb4255e74cb904dc43f" class="memitem:ga9eecdc3dd66afdb4255e74cb904dc43f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_daemon_report_stopping (void)</td>
</tr>
<tr class="memdesc:ga9eecdc3dd66afdb4255e74cb904dc43f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Report to a service manager that the daemon calling this function is shutting down.<br />
</td>
</tr>
<tr class="separator:ga9eecdc3dd66afdb4255e74cb904dc43f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga052a2867cb74911e28b3055397d73526" class="memitem:ga052a2867cb74911e28b3055397d73526">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_inet_sockaddr_to_string (const void *sockaddr_pointer, size_t len, char *string, size_t string_len, const char **family_name, dbus_uint16_t *port, DBusError *error)</td>
</tr>
<tr class="separator:ga052a2867cb74911e28b3055397d73526">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga176d8ed4425894cf6ebe315b2fa9ce24" class="memitem:ga176d8ed4425894cf6ebe315b2fa9ce24">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_set_error_with_inet_sockaddr (DBusError *error, const void *sockaddr_pointer, size_t len, const char *description, int saved_errno)</td>
</tr>
<tr class="separator:ga176d8ed4425894cf6ebe315b2fa9ce24">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaebe1c886a34697762ca8b213fda28c95" class="memitem:gaebe1c886a34697762ca8b213fda28c95">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_combine_tcp_errors (DBusList **sources, const char *summary, const char *host, const char *port, DBusError *dest)</td>
</tr>
<tr class="separator:gaebe1c886a34697762ca8b213fda28c95">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Internal system-dependent API available on UNIX and Windows.

The system-dependent API has a dual purpose. First, it encapsulates all usage of operating system APIs for ease of auditing and to avoid cluttering the rest of the code with bizarre OS quirks and headers. Second, it abstracts different operating system APIs for portability.

## Macro Definition Documentation

## ◆ \_DBUS_DOUBLES_BITWISE_EQUAL

|  |  |  |  |
|----|----|----|----|
| \#define \_DBUS_DOUBLES_BITWISE_EQUAL | ( |   | a, |
|  |  |   | b  |
|  | ) |  |    (memcmp (&(a), &(b), sizeof (double)) == 0) |

On x86 there is an 80-bit FPU, and if you do "a == b" it may have a or b in an 80-bit register, thus failing to compare the two 64-bit doubles for bitwise equality.

So this macro compares the two doubles bitwise.

Definition at line 654 of file dbus-sysdeps.h.

## ◆ \_DBUS_MAX_SUN_PATH_LENGTH

|                                          |
|------------------------------------------|
| \#define \_DBUS_MAX_SUN_PATH_LENGTH   99 |

Maximum length of the path to a UNIX domain socket, sockaddr_un::sun_path member.

POSIX requires that all systems support at least 100 bytes here, including the nul termination. We use 99 for the max value to allow for the nul.

We could probably also do sizeof (addr.sun_path) but this way we are the same on all platforms which is probably a good idea.

Definition at line 765 of file dbus-sysdeps.h.

## ◆ \_DBUS_POLLERR

|                                  |
|----------------------------------|
| \#define \_DBUS_POLLERR   0x0008 |

Error condition.

Definition at line 450 of file dbus-sysdeps.h.

## ◆ \_DBUS_POLLHUP

|                                  |
|----------------------------------|
| \#define \_DBUS_POLLHUP   0x0010 |

Hung up.

Definition at line 452 of file dbus-sysdeps.h.

## ◆ \_DBUS_POLLIN

|                                 |
|---------------------------------|
| \#define \_DBUS_POLLIN   0x0001 |

There is data to read.

Definition at line 444 of file dbus-sysdeps.h.

## ◆ \_DBUS_POLLNVAL

|                                   |
|-----------------------------------|
| \#define \_DBUS_POLLNVAL   0x0020 |

Invalid request: fd not open.

Definition at line 454 of file dbus-sysdeps.h.

## ◆ \_DBUS_POLLOUT

|                                  |
|----------------------------------|
| \#define \_DBUS_POLLOUT   0x0004 |

Writing now will not block.

Definition at line 448 of file dbus-sysdeps.h.

## ◆ \_DBUS_POLLPRI

|                                  |
|----------------------------------|
| \#define \_DBUS_POLLPRI   0x0002 |

There is urgent data to read.

Definition at line 446 of file dbus-sysdeps.h.

## ◆ DBUS_DEFAULT_MESSAGE_UNIX_FDS

|                                             |
|---------------------------------------------|
| \#define DBUS_DEFAULT_MESSAGE_UNIX_FDS   16 |

Definition at line 720 of file dbus-sysdeps.h.

## ◆ DBUS_GID_FORMAT

|                                  |
|----------------------------------|
| \#define DBUS_GID_FORMAT   "%lu" |

an appropriate printf format for dbus_gid_t

Definition at line 157 of file dbus-sysdeps.h.

## ◆ DBUS_GID_UNSET

|                                             |
|---------------------------------------------|
| \#define DBUS_GID_UNSET   ((dbus_gid_t) -1) |

an invalid GID used to represent an uninitialized dbus_gid_t field

Definition at line 150 of file dbus-sysdeps.h.

## ◆ DBUS_PID_FORMAT

|                                  |
|----------------------------------|
| \#define DBUS_PID_FORMAT   "%lu" |

an appropriate printf format for dbus_pid_t

Definition at line 153 of file dbus-sysdeps.h.

## ◆ DBUS_PID_UNSET

|                                             |
|---------------------------------------------|
| \#define DBUS_PID_UNSET   ((dbus_pid_t) -1) |

an invalid PID used to represent an uninitialized dbus_pid_t field

Definition at line 146 of file dbus-sysdeps.h.

## ◆ DBUS_POLLABLE_FORMAT

|                                     |
|-------------------------------------|
| \#define DBUS_POLLABLE_FORMAT   "d" |

Definition at line 393 of file dbus-sysdeps.h.

## ◆ DBUS_SOCKET_FORMAT

|                                   |
|-----------------------------------|
| \#define DBUS_SOCKET_FORMAT   "d" |

Definition at line 186 of file dbus-sysdeps.h.

## ◆ DBUS_SOCKET_INIT

|                                    |
|------------------------------------|
| \#define DBUS_SOCKET_INIT   { -1 } |

Definition at line 187 of file dbus-sysdeps.h.

## ◆ DBUS_UID_FORMAT

|                                  |
|----------------------------------|
| \#define DBUS_UID_FORMAT   "%lu" |

an appropriate printf format for dbus_uid_t

Definition at line 155 of file dbus-sysdeps.h.

## ◆ DBUS_UID_UNSET

|                                             |
|---------------------------------------------|
| \#define DBUS_UID_UNSET   ((dbus_uid_t) -1) |

an invalid UID used to represent an uninitialized dbus_uid_t field

Definition at line 148 of file dbus-sysdeps.h.

## Typedef Documentation

## ◆ dbus_gid_t

|                                  |
|----------------------------------|
| typedef unsigned long dbus_gid_t |

A group ID.

Definition at line 143 of file dbus-sysdeps.h.

## ◆ dbus_pid_t

|                                  |
|----------------------------------|
| typedef unsigned long dbus_pid_t |

A process ID.

Definition at line 139 of file dbus-sysdeps.h.

## ◆ dbus_uid_t

|                                  |
|----------------------------------|
| typedef unsigned long dbus_uid_t |

A user ID.

Definition at line 141 of file dbus-sysdeps.h.

## ◆ DBusAtomic

|                                      |
|--------------------------------------|
| typedef struct DBusAtomic DBusAtomic |

Opaque type representing an atomically-modifiable integer that can be used from multiple threads.

Definition at line 334 of file dbus-sysdeps.h.

## ◆ DBusDirIter

|                                        |
|----------------------------------------|
| typedef struct DBusDirIter DBusDirIter |

Opaque type for reading a directory listing.

Definition at line 504 of file dbus-sysdeps.h.

## ◆ DBusGUID

|                                 |
|---------------------------------|
| typedef union DBusGUID DBusGUID |

Type representing a universally unique ID.

Definition at line 668 of file dbus-sysdeps.h.

## ◆ DBusPollable

|                          |
|--------------------------|
| typedef int DBusPollable |

Definition at line 392 of file dbus-sysdeps.h.

## ◆ DBusRLimit

|                                      |
|--------------------------------------|
| typedef struct DBusRLimit DBusRLimit |

Definition at line 722 of file dbus-sysdeps.h.

## Enumeration Type Documentation

## ◆ DBusCredentialsAddFlags

|                              |
|------------------------------|
| enum DBusCredentialsAddFlags |

Definition at line 284 of file dbus-sysdeps.h.

## ◆ DBusLogFlags

|                   |
|-------------------|
| enum DBusLogFlags |

Definition at line 624 of file dbus-sysdeps.h.

## ◆ DBusSystemLogSeverity

|                            |
|----------------------------|
| enum DBusSystemLogSeverity |

Definition at line 633 of file dbus-sysdeps.h.

## Function Documentation

## ◆ \_dbus_abort()

|                                       |     |       |     |     |     |
|---------------------------------------|-----|-------|-----|-----|-----|
| DBUS_PRIVATE_EXPORT void \_dbus_abort | (   | void  |     | )   |     |

Aborts the program with SIGABRT (dumping core).

Definition at line 89 of file dbus-sysdeps.c.

References \_dbus_exit(), \_dbus_getenv(), \_dbus_pid_for_log(), and \_dbus_sleep_milliseconds().

Referenced by \_dbus_get_tmpdir(), \_dbus_real_assert(), \_dbus_real_assert_not_reached(), \_dbus_warn(), \_dbus_warn_check_failed(), dbus_malloc(), dbus_malloc0(), and dbus_realloc().

## ◆ \_dbus_accept()

|                          |     |             |             |     |     |
|--------------------------|-----|-------------|-------------|-----|-----|
| DBusSocket \_dbus_accept | (   | DBusSocket  | *listen_fd* | )   |     |

Accepts a connection on a listening socket.

Handles EINTR for you.

This will enable FD_CLOEXEC for the returned socket.

Parameters  
|           |                            |
|-----------|----------------------------|
| listen_fd | the listen file descriptor |

<!-- -->

Returns  
the connection fd of the client, or -1 on error

Handles EINTR for you.

Parameters  
|           |                            |
|-----------|----------------------------|
| listen_fd | the listen file descriptor |

<!-- -->

Returns  
the connection fd of the client, or -1 on error

Definition at line 2589 of file dbus-sysdeps-unix.c.

References \_dbus_fd_set_close_on_exec(), and NULL.

## ◆ \_dbus_append_keyring_directory_for_credentials()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_append_keyring_directory_for_credentials | ( | DBusString \*  | *directory*, |
|  |  | DBusCredentials \*  | *credentials*  |
|  | ) |  |  |

Appends the directory in which a keyring for the given credentials should be stored.

The credentials should have either a Windows or UNIX user in them. The directory should be an absolute path.

On UNIX the directory is ~/.dbus-keyrings while on Windows it should probably be something else, since the dotfile convention is not normal on Windows.

Parameters  
|             |                                         |
|-------------|-----------------------------------------|
| directory   | string to append directory to           |
| credentials | credentials the directory should be for |

<!-- -->

Returns  
FALSE on no memory

Definition at line 4721 of file dbus-sysdeps-unix.c.

References \_dbus_assert, \_dbus_concat_dir_and_file(), \_dbus_credentials_are_anonymous(), \_dbus_credentials_get_unix_uid(), \_dbus_getenv(), \_dbus_homedir_from_uid(), \_dbus_string_append(), \_dbus_string_copy(), \_dbus_string_free(), \_dbus_string_get_const_data(), \_dbus_string_get_length(), \_dbus_string_init(), \_dbus_string_init_const(), \_dbus_string_set_length(), \_dbus_warn(), DBUS_UID_UNSET, FALSE, NULL, and TRUE.

Referenced by \_dbus_keyring_new_for_credentials().

## ◆ \_dbus_append_user_from_current_process()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_append_user_from_current_process | ( | DBusString \*  | *str* | ) |  |

Append to the string the identity we would like to have when we authenticate, on UNIX this is the current process UID and on Windows something else, probably a Windows SID string.

No escaping is required, that is done in dbus-auth.c. The username here need not be anything human-readable, it can be the machine-readable form i.e. a user id.

Parameters  
|     |                         |
|-----|-------------------------|
| str | the string to append to |

<!-- -->

Returns  
FALSE on no memory

No escaping is required, that is done in dbus-auth.c. The username here need not be anything human-readable, it can be the machine-readable form i.e. a user id.

Parameters  
|     |                         |
|-----|-------------------------|
| str | the string to append to |

<!-- -->

Returns  
FALSE on no memory

Definition at line 3117 of file dbus-sysdeps-unix.c.

References \_dbus_geteuid(), \_dbus_getpid(), \_dbus_string_append(), \_dbus_string_append_printf(), DBUS_UID_FORMAT, FALSE, and NULL.

## ◆ \_dbus_atomic_dec()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_int32_t \_dbus_atomic_dec | ( | DBusAtomic \*  | *atomic* | ) |  |

Atomically decrement an integer.

Parameters  
|        |                                     |
|--------|-------------------------------------|
| atomic | pointer to the integer to decrement |

<!-- -->

Returns  
the value before decrementing

Definition at line 3205 of file dbus-sysdeps-unix.c.

References DBusAtomic::value.

Referenced by \_dbus_babysitter_unref(), \_dbus_connection_unref_unlocked(), \_dbus_pending_call_unref_and_unlock(), \_dbus_server_unref_unlocked(), dbus_connection_unref(), dbus_free(), dbus_message_unref(), dbus_pending_call_unref(), dbus_server_ref(), and dbus_server_unref().

## ◆ \_dbus_atomic_get()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_int32_t \_dbus_atomic_get | ( | DBusAtomic \*  | *atomic* | ) |  |

Atomically get the value of an integer.

It may change at any time thereafter, so this is mostly only useful for assertions.

Parameters  
|        |                               |
|--------|-------------------------------|
| atomic | pointer to the integer to get |

<!-- -->

Returns  
the value at this moment

Definition at line 3233 of file dbus-sysdeps-unix.c.

References DBusAtomic::value.

Referenced by \_dbus_connection_close_if_only_one_ref(), and \_dbus_connection_new_for_transport().

## ◆ \_dbus_atomic_inc()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_int32_t \_dbus_atomic_inc | ( | DBusAtomic \*  | *atomic* | ) |  |

Atomically increments an integer.

Parameters  
|        |                                     |
|--------|-------------------------------------|
| atomic | pointer to the integer to increment |

<!-- -->

Returns  
the value before incrementing

Definition at line 3178 of file dbus-sysdeps-unix.c.

References DBusAtomic::value.

Referenced by \_dbus_babysitter_ref(), \_dbus_connection_new_for_transport(), \_dbus_connection_ref_unlocked(), \_dbus_pending_call_new_unlocked(), \_dbus_pending_call_ref_unlocked(), \_dbus_server_init_base(), \_dbus_server_ref_unlocked(), dbus_connection_add_filter(), dbus_connection_ref(), dbus_malloc(), dbus_malloc0(), dbus_message_copy(), dbus_message_ref(), dbus_pending_call_ref(), dbus_realloc(), dbus_server_ref(), and dbus_server_unref().

## ◆ \_dbus_atomic_set_nonzero()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT void \_dbus_atomic_set_nonzero | ( | DBusAtomic \*  | *atomic* | ) |  |

Atomically set the value of an integer to something nonzero.

Parameters  
|        |                               |
|--------|-------------------------------|
| atomic | pointer to the integer to set |

Definition at line 3279 of file dbus-sysdeps-unix.c.

References DBusAtomic::value.

Referenced by dbus_connection_set_change_sigpipe().

## ◆ \_dbus_atomic_set_zero()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT void \_dbus_atomic_set_zero | ( | DBusAtomic \*  | *atomic* | ) |  |

Atomically set the value of an integer to 0.

Parameters  
|        |                               |
|--------|-------------------------------|
| atomic | pointer to the integer to set |

Definition at line 3258 of file dbus-sysdeps-unix.c.

References DBusAtomic::value.

Referenced by dbus_connection_set_change_sigpipe().

## ◆ \_dbus_become_daemon()

|                                  |     |                      |                   |
|----------------------------------|-----|----------------------|-------------------|
| dbus_bool_t \_dbus_become_daemon | (   | const DBusString \*  | *pidfile*,        |
|                                  |     | DBusPipe \*          | *print_pid_pipe*, |
|                                  |     | DBusError \*         | *error*,          |
|                                  |     | dbus_bool_t          | *keep_umask*      |
|                                  | )   |                      |                   |

Does the chdir, fork, setsid, etc.

to become a daemon process.

Parameters  
|                |                                               |
|----------------|-----------------------------------------------|
| pidfile        | NULL, or pidfile to create                    |
| print_pid_pipe | pipe to print daemon's pid to, or -1 for none |
| error          | return location for errors                    |
| keep_umask     | TRUE to keep the original umask               |

<!-- -->

Returns  
FALSE on failure

to become a daemon process.

Parameters  
|                |                                                          |
|----------------|----------------------------------------------------------|
| pidfile        | NULL, or pidfile to create                               |
| print_pid_pipe | file descriptor to print daemon's pid to, or -1 for none |
| error          | return location for errors                               |
| keep_umask     | TRUE to keep the original umask                          |

<!-- -->

Returns  
FALSE on failure

Definition at line 86 of file dbus-sysdeps-util-unix.c.

References \_dbus_assert_not_reached, \_dbus_ensure_standard_fds(), \_dbus_error_from_errno(), \_dbus_getenv(), \_dbus_warn(), \_dbus_write_pid_to_file_and_pipe(), DBUS_ERROR_FAILED, DBUS_ERROR_NOT_SUPPORTED, dbus_set_error(), FALSE, DBusError::message, NULL, and TRUE.

## ◆ \_dbus_change_to_daemon_user()

|                                          |     |                |          |
|------------------------------------------|-----|----------------|----------|
| dbus_bool_t \_dbus_change_to_daemon_user | (   | const char \*  | *user*,  |
|                                          |     | DBusError \*   | *error*  |
|                                          | )   |                |          |

Changes the user and group the bus is running as.

Parameters  
|       |                            |
|-------|----------------------------|
| user  | the user to become         |
| error | return location for errors |

<!-- -->

Returns  
FALSE on failure

Definition at line 333 of file dbus-sysdeps-util-unix.c.

References \_dbus_error_from_errno(), \_dbus_get_user_id_and_primary_group(), \_dbus_string_init_const(), \_dbus_warn(), DBUS_ERROR_FAILED, dbus_set_error(), FALSE, NULL, and TRUE.

## ◆ \_dbus_check_dir_is_private_to_user()

|                                                 |     |                |          |
|-------------------------------------------------|-----|----------------|----------|
| dbus_bool_t \_dbus_check_dir_is_private_to_user | (   | DBusString \*  | *dir*,   |
|                                                 |     | DBusError \*   | *error*  |
|                                                 | )   |                |          |

Checks to make sure the given directory is private to the user.

Parameters  
|       |                           |
|-------|---------------------------|
| dir   | the name of the directory |
| error | error return              |

<!-- -->

Returns  
FALSE on failure

Definition at line 2644 of file dbus-sysdeps-unix.c.

References \_dbus_error_from_errno(), \_dbus_string_get_const_data(), DBUS_ERROR_FAILED, dbus_set_error(), FALSE, and TRUE.

## ◆ \_dbus_check_setuid()

|                                 |     |       |     |     |     |
|---------------------------------|-----|-------|-----|-----|-----|
| dbus_bool_t \_dbus_check_setuid | (   | void  |     | )   |     |

**NOTE**: If you modify this function, please also consider making the corresponding change in GLib.

See glib/gutils.c:g_check_setuid().

Returns TRUE if the current process was executed as setuid (or an equivalent \_\_libc_enable_secure is available). See: http://osdir.com/ml/linux.lfs.hardened/2007-04/msg00032.html

Definition at line 5002 of file dbus-sysdeps-unix.c.

References FALSE, and TRUE.

Referenced by \_dbus_get_autolaunch_address(), \_dbus_getenv(), \_dbus_keyring_new_for_credentials(), \_dbus_lookup_launchd_socket(), and \_dbus_threads_init_platform_specific().

## ◆ \_dbus_clearenv()

|                                                 |     |       |     |     |     |
|-------------------------------------------------|-----|-------|-----|-----|-----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_clearenv | (   | void  |     | )   |     |

Wrapper for clearenv().

Returns  
TRUE on success.

Definition at line 213 of file dbus-sysdeps.c.

References FALSE, NULL, and TRUE.

## ◆ \_dbus_close_socket()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_close_socket | ( | DBusSocket \*  | *fd*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Closes a socket and invalidates it.

Should not be used on non-socket file descriptors or handles.

If an error is detected, this function returns FALSE and sets the error, but the socket is still closed and invalidated. Callers can use the error in a diagnostic message, but should not retry closing the socket.

Parameters  
|       |                              |
|-------|------------------------------|
| fd    | the socket                   |
| error | return location for an error |

<!-- -->

Returns  
FALSE if error is set

<!-- -->

Parameters  
|       |                     |
|-------|---------------------|
| fd    | the file descriptor |
| error | error object        |

<!-- -->

Returns  
FALSE if error set

Definition at line 314 of file dbus-sysdeps-unix.c.

References \_dbus_assert, \_dbus_close(), \_dbus_error_from_errno(), \_dbus_strerror_from_errno(), dbus_set_error(), FALSE, NULL, and TRUE.

Referenced by \_dbus_babysitter_unref(), \_dbus_connect_unix_socket(), \_dbus_listen_unix_socket(), \_dbus_server_listen_platform_specific(), \_dbus_server_new_for_domain_socket(), \_dbus_server_new_for_tcp_socket(), \_dbus_transport_new_for_domain_socket(), and \_dbus_transport_new_for_tcp_socket().

## ◆ \_dbus_combine_tcp_errors()

|                                |     |                |            |
|--------------------------------|-----|----------------|------------|
| void \_dbus_combine_tcp_errors | (   | DBusList \*\*  | *sources*, |
|                                |     | const char \*  | *summary*, |
|                                |     | const char \*  | *host*,    |
|                                |     | const char \*  | *port*,    |
|                                |     | DBusError \*   | *dest*     |
|                                | )   |                |            |

Definition at line 877 of file dbus-sysdeps.c.

## ◆ \_dbus_command_for_pid()

|                                    |     |                |            |
|------------------------------------|-----|----------------|------------|
| dbus_bool_t \_dbus_command_for_pid | (   | unsigned long  | *pid*,     |
|                                    |     | DBusString \*  | *str*,     |
|                                    |     | int            | *max_len*, |
|                                    |     | DBusError \*   | *error*    |
|                                    | )   |                |            |

Get a printable string describing the command used to execute the process with pid.

This string should only be used for informative purposes such as logging; it may not be trusted.

The command is guaranteed to be printable ASCII and no longer than max_len.

Parameters  
|         |                                    |
|---------|------------------------------------|
| pid     | Process id                         |
| str     | Append command to this string      |
| max_len | Maximum length of returned command |
| error   | return location for errors         |

<!-- -->

Returns  
FALSE on error

Definition at line 1109 of file dbus-sysdeps-util-unix.c.

References \_dbus_close(), \_dbus_error_from_errno(), \_dbus_read(), \_dbus_string_append_printf(), \_dbus_string_copy(), \_dbus_string_free(), \_dbus_string_get_const_data(), \_dbus_string_get_length(), \_dbus_string_init(), DBUS_ERROR_NOT_SUPPORTED, dbus_set_error(), FALSE, NULL, and TRUE.

## ◆ \_dbus_concat_dir_and_file()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_concat_dir_and_file | ( | DBusString \*  | *dir*, |
|  |  | const DBusString \*  | *next_component*  |
|  | ) |  |  |

Appends the given filename to the given directory.

Parameters  
|                |                    |
|----------------|--------------------|
| dir            | the directory name |
| next_component | the filename       |

<!-- -->

Returns  
TRUE on success

<!-- -->

Parameters  
|                |                    |
|----------------|--------------------|
| dir            | the directory name |
| next_component | the filename       |

<!-- -->

Returns  
TRUE on success

Definition at line 3497 of file dbus-sysdeps-unix.c.

References \_dbus_string_append_byte(), \_dbus_string_copy(), \_dbus_string_get_byte(), \_dbus_string_get_length(), \_dbus_string_shorten(), FALSE, and TRUE.

Referenced by \_dbus_append_keyring_directory_for_credentials(), \_dbus_get_standard_session_servicedirs(), \_dbus_keyring_new_for_credentials(), \_dbus_server_listen_unix_socket(), and \_dbus_split_paths_and_append().

## ◆ \_dbus_connect_exec()

|                                |     |                |             |
|--------------------------------|-----|----------------|-------------|
| DBusSocket \_dbus_connect_exec | (   | const char \*  | *path*,     |
|                                |     | char \*const   | *argv*\[\], |
|                                |     | DBusError \*   | *error*     |
|                                | )   |                |             |

Creates a UNIX domain socket and connects it to the specified process to execute.

This will set FD_CLOEXEC for the socket returned.

Parameters  
|  |  |
|----|----|
| path | the path to the executable |
| argv | the argument list for the process to execute. argv\[0\] typically is identical to the path of the executable |
| error | return location for error code |

<!-- -->

Returns  
a valid socket on success or an invalid socket on error

Definition at line 1054 of file dbus-sysdeps-unix.c.

References \_dbus_assert, \_dbus_close_all(), \_dbus_error_from_errno(), \_dbus_fd_set_close_on_exec(), and dbus_set_error().

## ◆ \_dbus_connect_tcp_socket()

|                                      |     |                |           |
|--------------------------------------|-----|----------------|-----------|
| DBusSocket \_dbus_connect_tcp_socket | (   | const char \*  | *host*,   |
|                                      |     | const char \*  | *port*,   |
|                                      |     | const char \*  | *family*, |
|                                      |     | DBusError \*   | *error*   |
|                                      | )   |                |           |

Creates a socket and connects to a socket at the given host and port.

The connection fd is returned, and is set up as nonblocking.

This will set FD_CLOEXEC for the socket returned

Parameters  
|        |                                               |
|--------|-----------------------------------------------|
| host   | the host name to connect to                   |
| port   | the port to connect to                        |
| family | the address family to listen on, NULL for all |
| error  | return location for error code                |

<!-- -->

Returns  
connection file descriptor or -1 on error

The connection fd is returned, and is set up as nonblocking.

Parameters  
|        |                                               |
|--------|-----------------------------------------------|
| host   | the host name to connect to                   |
| port   | the port to connect to                        |
| family | the address family to listen on, NULL for all |
| error  | return location for error code                |

<!-- -->

Returns  
connection file descriptor or -1 on error

Definition at line 1449 of file dbus-sysdeps-unix.c.

References NULL.

## ◆ \_dbus_connect_tcp_socket_with_nonce()

|  |  |  |  |
|----|----|----|----|
| DBusSocket \_dbus_connect_tcp_socket_with_nonce | ( | const char \*  | *host*, |
|  |  | const char \*  | *port*, |
|  |  | const char \*  | *family*, |
|  |  | const char \*  | *noncefile*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Definition at line 1458 of file dbus-sysdeps-unix.c.

## ◆ \_dbus_connect_unix_socket()

|                                       |     |                |             |
|---------------------------------------|-----|----------------|-------------|
| DBusSocket \_dbus_connect_unix_socket | (   | const char \*  | *path*,     |
|                                       |     | dbus_bool_t    | *abstract*, |
|                                       |     | DBusError \*   | *error*     |
|                                       | )   |                |             |

Creates a socket and connects it to the UNIX domain socket at the given path.

The connection fd is returned, and is set up as nonblocking.

Uses abstract sockets instead of filesystem-linked sockets if requested (it's possible only on Linux; see "man 7 unix" on Linux). On non-Linux abstract socket usage always fails.

This will set FD_CLOEXEC for the socket returned.

Parameters  
|          |                                |
|----------|--------------------------------|
| path     | the path to UNIX domain socket |
| abstract | TRUE to use abstract namespace |
| error    | return location for error code |

<!-- -->

Returns  
a valid socket on success or an invalid socket on error

The socket is returned, and is set up as nonblocking.

Abstract socket usage always fails.

This will set FD_CLOEXEC for the socket returned.

Parameters  
|          |                                |
|----------|--------------------------------|
| path     | the path to UNIX domain socket |
| abstract | TRUE to use abstract namespace |
| error    | return location for error code |

<!-- -->

Returns  
a valid socket on success or an invalid socket on error

Definition at line 957 of file dbus-sysdeps-unix.c.

References \_dbus_close_socket(), \_dbus_error_from_errno(), \_DBUS_MAX_SUN_PATH_LENGTH, \_dbus_set_socket_nonblocking(), \_DBUS_ZERO, DBUS_ERROR_BAD_ADDRESS, DBUS_ERROR_NOT_SUPPORTED, dbus_set_error(), and NULL.

Referenced by \_dbus_transport_new_for_domain_socket().

## ◆ \_dbus_create_directory()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_create_directory | ( | const DBusString \*  | *filename*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

directory interface

directory interface

Unlike \_dbus_ensure_directory(), this only succeeds if the directory is genuinely newly-created.

Parameters  
|          |                          |
|----------|--------------------------|
| filename | directory filename       |
| error    | initialized error object |

<!-- -->

Returns  
TRUE on success

Definition at line 3466 of file dbus-sysdeps-unix.c.

References \_dbus_strerror_from_errno(), \_dbus_string_get_const_data(), DBUS_ERROR_FAILED, dbus_set_error(), FALSE, NULL, and TRUE.

## ◆ \_dbus_credentials_add_from_current_process()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_credentials_add_from_current_process | ( | DBusCredentials \*  | *credentials* | ) |  |

Adds the most important credentials of the current process (the uid and pid) to the passed-in credentials object.

The group vector is not included because it is rarely needed. The Linux security label is not included because it is rarely needed, it requires reading /proc, and the LSM API doesn't actually guarantee that the string seen in /proc is comparable to the strings found in SO_PEERSEC results.

Parameters  
|             |                       |
|-------------|-----------------------|
| credentials | credentials to add to |

<!-- -->

Returns  
FALSE if no memory; does not properly roll back on failure, so only some credentials may have been added

Adds the most important credentials of the current process (the uid and pid) to the passed-in credentials object.

Parameters  
|             |                       |
|-------------|-----------------------|
| credentials | credentials to add to |

<!-- -->

Returns  
FALSE if no memory; does not properly roll back on failure, so only some credentials may have been added

Definition at line 3005 of file dbus-sysdeps-unix.c.

References \_dbus_credentials_add_pid(), \_dbus_credentials_add_unix_uid(), \_dbus_credentials_add_windows_sid(), \_dbus_credentials_take_pid_fd(), \_dbus_geteuid(), \_dbus_getpid(), FALSE, NULL, and TRUE.

Referenced by \_dbus_credentials_new_from_current_process(), and \_dbus_keyring_new_for_credentials().

## ◆ \_dbus_credentials_add_from_user()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_credentials_add_from_user | ( | DBusCredentials \*  | *credentials*, |
|  |  | const DBusString \*  | *username*, |
|  |  | DBusCredentialsAddFlags  | *flags*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Adds the credentials corresponding to the given username.

Parameters  
|             |                        |
|-------------|------------------------|
| credentials | credentials to fill in |
| username    | the username           |

<!-- -->

Returns  
TRUE if the username existed and we got some credentials

Used among other purposes to parses a desired identity provided from a client in the auth protocol. On UNIX this means parsing a UID, on Windows probably parsing an SID string.

Parameters  
|             |                        |
|-------------|------------------------|
| credentials | credentials to fill in |
| username    | the username           |

<!-- -->

Returns  
TRUE if the username existed and we got some credentials

Definition at line 2314 of file dbus-sysdeps-win.c.

References \_dbus_credentials_add_unix_uid(), \_dbus_credentials_add_windows_sid(), \_dbus_is_a_number(), \_dbus_string_get_const_data(), \_dbus_user_database_get_system(), \_dbus_user_database_get_username(), \_dbus_user_database_lock_system(), \_dbus_user_database_unlock_system(), DBUS_ERROR_INVALID_ARGS, dbus_set_error(), DBUS_UID_UNSET, FALSE, NULL, TRUE, and DBusUserInfo::uid.

## ◆ \_dbus_daemon_report_ready()

|                                 |     |       |     |     |     |
|---------------------------------|-----|-------|-----|-----|-----|
| void \_dbus_daemon_report_ready | (   | void  |     | )   |     |

Report to a service manager that the daemon calling this function is ready for use.

This is currently only implemented for systemd.

Definition at line 1544 of file dbus-sysdeps-util-unix.c.

Referenced by \_dbus_daemon_report_reloaded().

## ◆ \_dbus_daemon_report_reloaded()

|                                    |     |       |     |     |     |
|------------------------------------|-----|-------|-----|-----|-----|
| void \_dbus_daemon_report_reloaded | (   | void  |     | )   |     |

Report to a service manager that the daemon calling this function is reloading configuration.

This is currently only implemented for systemd.

Definition at line 1568 of file dbus-sysdeps-util-unix.c.

References \_dbus_daemon_report_ready().

## ◆ \_dbus_daemon_report_reloading()

|                                     |     |       |     |     |     |
|-------------------------------------|-----|-------|-----|-----|-----|
| void \_dbus_daemon_report_reloading | (   | void  |     | )   |     |

Report to a service manager that the daemon calling this function is reloading configuration.

This is currently only implemented for systemd.

Definition at line 1556 of file dbus-sysdeps-util-unix.c.

## ◆ \_dbus_daemon_report_stopping()

|                                    |     |       |     |     |     |
|------------------------------------|-----|-------|-----|-----|-----|
| void \_dbus_daemon_report_stopping | (   | void  |     | )   |     |

Report to a service manager that the daemon calling this function is shutting down.

This is currently only implemented for systemd.

Definition at line 1581 of file dbus-sysdeps-util-unix.c.

## ◆ \_dbus_daemon_unpublish_session_bus_address()

|                                                         |     |       |     |     |     |
|---------------------------------------------------------|-----|-------|-----|-----|-----|
| dbus_bool_t \_dbus_daemon_unpublish_session_bus_address | (   | void  |     | )   |     |

Clear the platform-specific centralized location where the session bus address is published.

This must only be called if DBusServer::published_address is TRUE, which is be the case if and only if platform-specific code has published the address centrally.

On Windows, this is implemented by closing a global shared memory segment.

On Unix, the session bus address is not published in a centralized location by libdbus, so this function does nothing. The closest equivalent on Unix is that the session bus address is published by the dbus-launch tool, and unpublished automatically when the dbus-launch tool exits.

Returns  
NULL in case of error

Definition at line 4789 of file dbus-sysdeps-unix.c.

References FALSE, NULL, and TRUE.

## ◆ \_dbus_delete_directory()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_delete_directory | ( | const DBusString \*  | *filename*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Removes a directory; Directory must be empty.

Parameters  
|          |                          |
|----------|--------------------------|
| filename | directory filename       |
| error    | initialized error object |

<!-- -->

Returns  
TRUE on success

Definition at line 4822 of file dbus-sysdeps-unix.c.

References \_dbus_string_get_const_data(), DBUS_ERROR_FAILED, dbus_set_error(), FALSE, and TRUE.

## ◆ \_dbus_directory_close()

|                             |     |                 |        |     |     |
|-----------------------------|-----|-----------------|--------|-----|-----|
| void \_dbus_directory_close | (   | DBusDirIter \*  | *iter* | )   |     |

Closes a directory iteration.

Definition at line 737 of file dbus-sysdeps-util-unix.c.

References DBusDirIter::d, and dbus_free().

## ◆ \_dbus_directory_get_next_file()

|                                            |     |                 |             |
|--------------------------------------------|-----|-----------------|-------------|
| dbus_bool_t \_dbus_directory_get_next_file | (   | DBusDirIter \*  | *iter*,     |
|                                            |     | DBusString \*   | *filename*, |
|                                            |     | DBusError \*    | *error*     |
|                                            | )   |                 |             |

Get next file in the directory.

Will not return "." or ".." on UNIX. If an error occurs, the contents of "filename" are undefined. The error is never set if the function succeeds.

This function is not re-entrant, and not necessarily thread-safe. Only use it for test code or single-threaded utilities.

Parameters  
|          |                                              |
|----------|----------------------------------------------|
| iter     | the iterator                                 |
| filename | string to be set to the next file in the dir |
| error    | return location for error                    |

<!-- -->

Returns  
TRUE if filename was filled in with a new filename

Will not return "." or ".." on UNIX. If an error occurs, the contents of "filename" are undefined. The error is never set if the function succeeds.

Parameters  
|          |                                              |
|----------|----------------------------------------------|
| iter     | the iterator                                 |
| filename | string to be set to the next file in the dir |
| error    | return location for error                    |

<!-- -->

Returns  
TRUE if filename was filled in with a new filename

Definition at line 689 of file dbus-sysdeps-util-unix.c.

References \_dbus_error_from_errno(), \_dbus_string_append(), \_dbus_string_set_length(), DBusDirIter::d, DBUS_ERROR_NO_MEMORY, dbus_set_error(), FALSE, and TRUE.

## ◆ \_dbus_directory_open()

|                                      |     |                      |             |
|--------------------------------------|-----|----------------------|-------------|
| DBusDirIter \* \_dbus_directory_open | (   | const DBusString \*  | *filename*, |
|                                      |     | DBusError \*         | *error*     |
|                                      | )   |                      |             |

Open a directory to iterate over.

Parameters  
|          |                                 |
|----------|---------------------------------|
| filename | the directory name              |
| error    | exception return object or NULL |

<!-- -->

Returns  
new iterator, or NULL on error

Definition at line 641 of file dbus-sysdeps-util-unix.c.

References \_dbus_error_from_errno(), \_dbus_string_append(), \_dbus_string_ends_with_c_str(), \_dbus_string_free(), \_dbus_string_get_const_data(), \_dbus_string_init_from_string(), DBusDirIter::d, DBUS_ERROR_NO_MEMORY, dbus_free(), dbus_new0, dbus_set_error(), FALSE, NULL, and TRUE.

## ◆ \_dbus_disable_sigpipe()

|                             |     |       |     |     |     |
|-----------------------------|-----|-------|-----|-----|-----|
| void \_dbus_disable_sigpipe | (   | void  |     | )   |     |

signal (SIGPIPE, SIG_IGN);

Definition at line 3670 of file dbus-sysdeps-unix.c.

Referenced by \_dbus_connection_new_for_transport().

## ◆ \_dbus_ensure_directory()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_ensure_directory | ( | const DBusString \*  | *filename*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Creates a directory; succeeds if the directory is created or already existed.

Parameters  
|          |                          |
|----------|--------------------------|
| filename | directory filename       |
| error    | initialized error object |

<!-- -->

Returns  
TRUE on success

Definition at line 3434 of file dbus-sysdeps-unix.c.

References \_dbus_strerror_from_errno(), \_dbus_string_get_const_data(), DBUS_ERROR_FAILED, dbus_set_error(), FALSE, NULL, and TRUE.

Referenced by \_dbus_keyring_new_for_credentials().

## ◆ \_dbus_error_from_errno()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT const char \* \_dbus_error_from_errno | ( | int  | *error_number* | ) |  |

Converts a UNIX errno, or Windows errno or WinSock error value into a DBusError name.

Parameters  
|              |            |
|--------------|------------|
| error_number | the errno. |

<!-- -->

Returns  
an error name

Definition at line 565 of file dbus-sysdeps.c.

References DBUS_ERROR_ACCESS_DENIED, DBUS_ERROR_ADDRESS_IN_USE, DBUS_ERROR_FAILED, DBUS_ERROR_FILE_EXISTS, DBUS_ERROR_FILE_NOT_FOUND, DBUS_ERROR_LIMITS_EXCEEDED, DBUS_ERROR_NO_MEMORY, DBUS_ERROR_NO_NETWORK, DBUS_ERROR_NO_SERVER, DBUS_ERROR_NOT_SUPPORTED, and DBUS_ERROR_TIMEOUT.

Referenced by \_dbus_append_address_from_socket(), \_dbus_become_daemon(), \_dbus_change_to_daemon_user(), \_dbus_check_dir_is_private_to_user(), \_dbus_close(), \_dbus_close_socket(), \_dbus_command_for_pid(), \_dbus_connect_exec(), \_dbus_connect_unix_socket(), \_dbus_directory_get_next_file(), \_dbus_directory_open(), \_dbus_dup(), \_dbus_error_from_system_errno(), \_dbus_file_get_contents(), \_dbus_generate_random_bytes(), \_dbus_is_console_user(), \_dbus_listen_systemd_sockets(), \_dbus_listen_tcp_socket(), \_dbus_listen_unix_socket(), \_dbus_read_credentials_socket(), \_dbus_send_credentials_socket(), \_dbus_set_socket_nonblocking(), \_dbus_socketpair(), \_dbus_spawn_async_with_babysitter(), \_dbus_stat(), and \_dbus_string_save_to_file().

## ◆ \_dbus_error_from_system_errno()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT const char \* \_dbus_error_from_system_errno | ( | void  |  | ) |  |

Converts the current system errno value into a DBusError name.

Returns  
an error name

Definition at line 657 of file dbus-sysdeps.c.

References \_dbus_error_from_errno().

## ◆ \_dbus_exit()

|                                      |     |      |        |     |     |
|--------------------------------------|-----|------|--------|-----|-----|
| DBUS_PRIVATE_EXPORT void \_dbus_exit | (   | int  | *code* | )   |     |

Exit the process, returning the given value.

Parameters  
|      |               |
|------|---------------|
| code | the exit code |

Definition at line 3641 of file dbus-sysdeps-unix.c.

Referenced by \_dbus_abort().

## ◆ \_dbus_flush_caches()

|                                              |     |       |     |     |     |
|----------------------------------------------|-----|-------|-----|-----|-----|
| DBUS_PRIVATE_EXPORT void \_dbus_flush_caches | (   | void  |     | )   |     |

Called when the bus daemon is signaled to reload its configuration; any caches should be nuked.

Of course any caches that need explicit reload are probably broken, but c'est la vie.

Definition at line 4702 of file dbus-sysdeps-unix.c.

References \_dbus_user_database_flush_system().

## ◆ \_dbus_generate_random_ascii()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_generate_random_ascii | ( | DBusString \*  | *str*, |
|  |  | int  | *n_bytes*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Generates the given number of random bytes, where the bytes are chosen from the alphanumeric ASCII subset.

Parameters  
|         |                                                      |
|---------|------------------------------------------------------|
| str     | the string                                           |
| n_bytes | the number of random ASCII bytes to append to string |
| error   | location to store reason for failure                 |

<!-- -->

Returns  
TRUE on success, FALSE if no memory or other failure

Definition at line 525 of file dbus-sysdeps.c.

References \_dbus_assert, \_dbus_generate_random_bytes(), \_dbus_string_get_byte(), \_dbus_string_get_length(), \_dbus_string_set_byte(), \_dbus_string_validate_ascii(), FALSE, and TRUE.

Referenced by \_dbus_string_save_to_file().

## ◆ \_dbus_generate_random_bytes()

|                                          |     |                |            |
|------------------------------------------|-----|----------------|------------|
| dbus_bool_t \_dbus_generate_random_bytes | (   | DBusString \*  | *str*,     |
|                                          |     | int            | *n_bytes*, |
|                                          |     | DBusError \*   | *error*    |
|                                          | )   |                |            |

Generates the given number of securely random bytes, using the best mechanism we can come up with.

Parameters  
|         |                                                |
|---------|------------------------------------------------|
| str     | the string                                     |
| n_bytes | the number of random bytes to append to string |
| error   | location to store reason for failure           |

<!-- -->

Returns  
TRUE on success, FALSE on error

Generates the given number of securely random bytes, using the best mechanism we can come up with.

Parameters  
|         |                                                |
|---------|------------------------------------------------|
| str     | the string                                     |
| n_bytes | the number of random bytes to append to string |
| error   | location to store reason for failure           |

<!-- -->

Returns  
TRUE on success

Definition at line 3572 of file dbus-sysdeps-unix.c.

References \_dbus_close(), \_dbus_error_from_errno(), \_dbus_read(), \_dbus_string_get_data_len(), \_dbus_string_get_length(), \_dbus_string_lengthen(), \_dbus_string_set_length(), DBUS_ERROR_IO_ERROR, dbus_set_error(), FALSE, NULL, and TRUE.

Referenced by \_dbus_generate_random_ascii(), and \_dbus_generate_random_bytes_buffer().

## ◆ \_dbus_generate_random_bytes_buffer()

|  |  |  |  |
|----|----|----|----|
| \_DBUS_WARN_UNUSED_RESULT dbus_bool_t \_dbus_generate_random_bytes_buffer | ( | char \*  | *buffer*, |
|  |  | int  | *n_bytes*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Random numbers.

Random numbers.

Parameters  
|         |                                           |
|---------|-------------------------------------------|
| buffer  | an allocated buffer                       |
| n_bytes | the number of bytes in buffer to write to |
| error   | location to store reason for failure      |

<!-- -->

Returns  
TRUE on success

Definition at line 491 of file dbus-sysdeps.c.

References \_dbus_generate_random_bytes(), \_dbus_string_copy_to_buffer(), \_dbus_string_free(), \_dbus_string_init(), FALSE, and TRUE.

Referenced by \_dbus_generate_uuid().

## ◆ \_dbus_get_autolaunch_address()

|                                           |     |                |            |
|-------------------------------------------|-----|----------------|------------|
| dbus_bool_t \_dbus_get_autolaunch_address | (   | const char \*  | *scope*,   |
|                                           |     | DBusString \*  | *address*, |
|                                           |     | DBusError \*   | *error*    |
|                                           | )   |                |            |

Returns the address of a new session bus.

If successful, returns TRUE and appends the address to `address`. If a failure happens, returns FALSE and sets an error in `error`.

Parameters  
|         |                                                   |
|---------|---------------------------------------------------|
| scope   | scope of autolaunch (Windows only)                |
| address | a DBusString where the address can be stored      |
| error   | a DBusError to store the error in case of failure |

<!-- -->

Returns  
TRUE on success, FALSE if an error happened

Definition at line 4299 of file dbus-sysdeps-unix.c.

References \_dbus_assert, \_dbus_check_setuid(), \_dbus_get_local_machine_uuid_encoded(), \_dbus_getenv(), \_DBUS_N_ELEMENTS, \_dbus_string_append_printf(), \_dbus_string_free(), \_dbus_string_get_const_data(), \_dbus_string_get_data(), \_dbus_string_get_length(), \_dbus_string_init(), DBUS_ERROR_FAILED, DBUS_ERROR_NO_MEMORY, DBUS_ERROR_NOT_SUPPORTED, DBUS_ERROR_SPAWN_CHILD_EXITED, DBUS_ERROR_TIMEOUT, dbus_set_error(), dbus_set_error_const(), FALSE, NULL, and TRUE.

## ◆ \_dbus_get_environment()

|                                  |     |       |     |     |     |
|----------------------------------|-----|-------|-----|-----|-----|
| char \*\* \_dbus_get_environment | (   | void  |     | )   |     |

Gets a NULL-terminated list of key=value pairs from the environment.

Use dbus_free_string_array to free it.

Returns  
the environment or NULL on OOM

Definition at line 55 of file dbus-sysdeps-util.c.

References \_dbus_assert, \_dbus_strdup(), dbus_free_string_array(), dbus_new0, and NULL.

## ◆ \_dbus_get_is_errno_eagain_or_ewouldblock()

|                                                       |     |      |     |     |     |
|-------------------------------------------------------|-----|------|-----|-----|-----|
| dbus_bool_t \_dbus_get_is_errno_eagain_or_ewouldblock | (   | int  | *e* | )   |     |

See if errno is EAGAIN or EWOULDBLOCK (this has to be done differently for Winsock so is abstracted)

Returns  
TRUE if e == EAGAIN or e == EWOULDBLOCK

Definition at line 4801 of file dbus-sysdeps-unix.c.

## ◆ \_dbus_get_is_errno_eintr()

|                                       |     |      |     |     |     |
|---------------------------------------|-----|------|-----|-----|-----|
| dbus_bool_t \_dbus_get_is_errno_eintr | (   | int  | *e* | )   |     |

See if errno is EINTR.

Returns  
TRUE if e == EINTR

Definition at line 690 of file dbus-sysdeps.c.

## ◆ \_dbus_get_is_errno_enomem()

|                                        |     |      |     |     |     |
|----------------------------------------|-----|------|-----|-----|-----|
| dbus_bool_t \_dbus_get_is_errno_enomem | (   | int  | *e* | )   |     |

See if errno is ENOMEM.

Returns  
TRUE if e == ENOMEM

Definition at line 680 of file dbus-sysdeps.c.

## ◆ \_dbus_get_is_errno_epipe()

|                                       |     |      |     |     |     |
|---------------------------------------|-----|------|-----|-----|-----|
| dbus_bool_t \_dbus_get_is_errno_epipe | (   | int  | *e* | )   |     |

See if errno is EPIPE.

Returns  
TRUE if errno == EPIPE

Definition at line 700 of file dbus-sysdeps.c.

## ◆ \_dbus_get_is_errno_etoomanyrefs()

|                                              |     |      |     |     |     |
|----------------------------------------------|-----|------|-----|-----|-----|
| dbus_bool_t \_dbus_get_is_errno_etoomanyrefs | (   | int  | *e* | )   |     |

See if errno is ETOOMANYREFS.

Returns  
TRUE if errno == ETOOMANYREFS

Definition at line 710 of file dbus-sysdeps.c.

References FALSE.

## ◆ \_dbus_get_local_system_servicedirs()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_get_local_system_servicedirs | ( | DBusList \*\*  | *dirs* | ) |  |

Returns the local admin directories for a system bus to look for service activation files.

On UNIX this should be the /etc/ and /run/ directories.

On Windows there is no system bus and this function can return nothing.

Parameters  
|      |                                     |
|------|-------------------------------------|
| dirs | the directory list we are returning |

<!-- -->

Returns  
FALSE on OOM

Definition at line 1495 of file dbus-sysdeps-util-unix.c.

References \_dbus_split_paths_and_append(), \_dbus_string_init_const(), NULL, and TRUE.

## ◆ \_dbus_get_low_level_socket_errno()

|                                       |     |       |     |     |     |
|---------------------------------------|-----|-------|-----|-----|-----|
| int \_dbus_get_low_level_socket_errno | (   | void  |     | )   |     |

Definition at line 5262 of file dbus-sysdeps-unix.c.

## ◆ \_dbus_get_monotonic_time()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT void \_dbus_get_monotonic_time | ( | dbus_int64_t \*  | *tv_sec*, |
|  |  | long \*  | *tv_usec*  |
|  | ) |  |  |

Get current time, as in gettimeofday().

Use the monotonic clock if available, to avoid problems when the system time changes.

Parameters  
|         |                                            |
|---------|--------------------------------------------|
| tv_sec  | return location for number of seconds      |
| tv_usec | return location for number of microseconds |

Definition at line 3381 of file dbus-sysdeps-unix.c.

References \_dbus_get_real_time(), and NULL.

Referenced by \_dbus_connection_block_pending_call().

## ◆ \_dbus_get_real_time()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT void \_dbus_get_real_time | ( | dbus_int64_t \*  | *tv_sec*, |
|  |  | long \*  | *tv_usec*  |
|  | ) |  |  |

Get current time, as in gettimeofday().

Never uses the monotonic clock.

Parameters  
|         |                                            |
|---------|--------------------------------------------|
| tv_sec  | return location for number of seconds      |
| tv_usec | return location for number of microseconds |

Definition at line 3412 of file dbus-sysdeps-unix.c.

References DBUS_INT64_CONSTANT, and NULL.

Referenced by \_dbus_generate_uuid(), and \_dbus_get_monotonic_time().

## ◆ \_dbus_get_session_config_file()

|                                            |     |                |       |     |     |
|--------------------------------------------|-----|----------------|-------|-----|-----|
| dbus_bool_t \_dbus_get_session_config_file | (   | DBusString \*  | *str* | )   |     |

Get the absolute path of the session.conf file.

Parameters  
|     |                                                       |
|-----|-------------------------------------------------------|
| str | the string to append to, which must be empty on entry |

<!-- -->

Returns  
FALSE if no memory

Definition at line 1532 of file dbus-sysdeps-util-unix.c.

References \_dbus_assert, \_dbus_string_append(), and \_dbus_string_get_length().

## ◆ \_dbus_get_standard_session_servicedirs()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_get_standard_session_servicedirs | ( | DBusList \*\*  | *dirs* | ) |  |

Returns the standard directories for a session bus to look for service activation files.

On UNIX this should be the standard xdg freedesktop.org data directories:

XDG_DATA_HOME=\${XDG_DATA_HOME-\$HOME/.local/share} XDG_DATA_DIRS=\${XDG_DATA_DIRS-/usr/local/share:/usr/share}

and

DBUS_DATADIR

Parameters  
|      |                                     |
|------|-------------------------------------|
| dirs | the directory list we are returning |

<!-- -->

Returns  
FALSE on OOM

On Windows this should be data directories:

CommonProgramFiles%/dbus

and

relocated DBUS_DATADIR

Parameters  
|      |                                     |
|------|-------------------------------------|
| dirs | the directory list we are returning |

<!-- -->

Returns  
FALSE on OOM

Definition at line 1364 of file dbus-sysdeps-util-unix.c.

References \_dbus_concat_dir_and_file(), \_dbus_getenv(), \_dbus_homedir_from_current_process(), \_dbus_replace_install_prefix(), \_dbus_split_paths_and_append(), \_dbus_string_append(), \_dbus_string_free(), \_dbus_string_get_const_data(), \_dbus_string_init(), \_dbus_string_init_const(), FALSE, NULL, and TRUE.

## ◆ \_dbus_get_standard_system_servicedirs()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_get_standard_system_servicedirs | ( | DBusList \*\*  | *dirs* | ) |  |

Returns the standard directories for a system bus to look for service activation files.

On UNIX this should be the standard xdg freedesktop.org data directories:

XDG_DATA_DIRS=\${XDG_DATA_DIRS-/usr/local/share:/usr/share}

and

DBUS_DATADIR

On Windows there is no system bus and this function can return nothing.

Parameters  
|      |                                     |
|------|-------------------------------------|
| dirs | the directory list we are returning |

<!-- -->

Returns  
FALSE on OOM

Definition at line 1456 of file dbus-sysdeps-util-unix.c.

References \_dbus_split_paths_and_append(), \_dbus_string_init_const(), NULL, and TRUE.

## ◆ \_dbus_get_system_config_file()

|                                           |     |                |       |     |     |
|-------------------------------------------|-----|----------------|-------|-----|-----|
| dbus_bool_t \_dbus_get_system_config_file | (   | DBusString \*  | *str* | )   |     |

Get the absolute path of the system.conf file (there is no system bus on Windows so this can just return FALSE and print a warning or something)

Parameters  
|     |                                                       |
|-----|-------------------------------------------------------|
| str | the string to append to, which must be empty on entry |

<!-- -->

Returns  
FALSE if no memory

Definition at line 1518 of file dbus-sysdeps-util-unix.c.

References \_dbus_assert, \_dbus_string_append(), and \_dbus_string_get_length().

## ◆ \_dbus_get_tmpdir()

|                                                     |     |       |     |     |     |
|-----------------------------------------------------|-----|-------|-----|-----|-----|
| DBUS_PRIVATE_EXPORT const char \* \_dbus_get_tmpdir | (   | void  |     | )   |     |

Gets the temporary files directory by inspecting the environment variables TMPDIR, TMP, and TEMP in that order.

If none of those are set "/tmp" is returned

Returns  
location of temp directory, or NULL if no memory for locking

Gets the temporary files directory by inspecting the environment variables TMPDIR, TMP, and TEMP in that order.

Returns  
location of temp directory, or NULL if no memory for locking

Definition at line 4029 of file dbus-sysdeps-unix.c.

References \_dbus_abort(), \_dbus_assert, \_DBUS_LOCK, \_DBUS_UNLOCK, \_dbus_warn(), and NULL.

## ◆ \_dbus_getenv()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT const char \* \_dbus_getenv | ( | const char \*  | *varname* | ) |  |

Wrapper for getenv().

Parameters  
|         |                              |
|---------|------------------------------|
| varname | name of environment variable |

<!-- -->

Returns  
value of environment variable or NULL if unset

Definition at line 197 of file dbus-sysdeps.c.

References \_dbus_check_setuid(), and NULL.

Referenced by \_dbus_abort(), \_dbus_append_keyring_directory_for_credentials(), \_dbus_become_daemon(), \_dbus_get_autolaunch_address(), \_dbus_get_standard_session_servicedirs(), \_dbus_homedir_from_uid(), \_dbus_server_listen_unix_socket(), \_dbus_server_new_for_launchd(), and \_dbus_set_up_transient_session_servicedirs().

## ◆ \_dbus_getpid()

|                                              |     |       |     |     |     |
|----------------------------------------------|-----|-------|-----|-----|-----|
| DBUS_PRIVATE_EXPORT dbus_pid_t \_dbus_getpid | (   | void  |     | )   |     |

Gets our process ID.

Returns  
process ID

Definition at line 3127 of file dbus-sysdeps-unix.c.

Referenced by \_dbus_append_user_from_current_process(), \_dbus_credentials_add_from_current_process(), \_dbus_logv(), and \_dbus_pid_for_log().

## ◆ \_dbus_getuid()

|                                              |     |       |     |     |     |
|----------------------------------------------|-----|-------|-----|-----|-----|
| DBUS_PRIVATE_EXPORT dbus_uid_t \_dbus_getuid | (   | void  |     | )   |     |

Gets our UID.

Returns  
process UID

Gets our UID.

Returns  
on Windows, just DBUS_UID_UNSET

Definition at line 3136 of file dbus-sysdeps-unix.c.

References DBUS_UID_UNSET.

Referenced by \_dbus_homedir_from_uid().

## ◆ \_dbus_inet_sockaddr_to_string()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_inet_sockaddr_to_string | ( | const void \*  | *sockaddr_pointer*, |
|  |  | size_t  | *len*, |
|  |  | char \*  | *string*, |
|  |  | size_t  | *string_len*, |
|  |  | const char \*\*  | *family_name*, |
|  |  | dbus_uint16_t \*  | *port*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Definition at line 762 of file dbus-sysdeps.c.

## ◆ \_dbus_init_system_log()

|                                                 |     |                |          |
|-------------------------------------------------|-----|----------------|----------|
| DBUS_PRIVATE_EXPORT void \_dbus_init_system_log | (   | const char \*  | *tag*,   |
|                                                 |     | DBusLogFlags   | *flags*  |
|                                                 | )   |                |          |

Initialize the system log.

The "tag" is not copied, and must remain valid for the entire lifetime of the process or until \_dbus_init_system_log() is called again. In practice it will normally be a constant.

On platforms that do not support a system log, the DBUS_LOG_FLAGS_SYSTEM_LOG flag is treated as equivalent to DBUS_LOG_FLAGS_STDERR.

Parameters  
|      |                                                  |
|------|--------------------------------------------------|
| tag  | the name of the executable (syslog tag)          |
| mode | whether to log to stderr, the system log or both |

The "tag" is not copied, and must remain valid for the entire lifetime of the process or until \_dbus_init_system_log() is called again. In practice it will normally be a constant.

Parameters  
|      |                                                  |
|------|--------------------------------------------------|
| tag  | the name of the executable (syslog tag)          |
| mode | whether to log to stderr, the system log or both |

Definition at line 5183 of file dbus-sysdeps-unix.c.

References \_dbus_assert.

## ◆ \_dbus_listen_tcp_socket()

|                              |     |                  |              |
|------------------------------|-----|------------------|--------------|
| int \_dbus_listen_tcp_socket | (   | const char \*    | *host*,      |
|                              |     | const char \*    | *port*,      |
|                              |     | const char \*    | *family*,    |
|                              |     | DBusString \*    | *retport*,   |
|                              |     | const char \*\*  | *retfamily*, |
|                              |     | DBusSocket \*\*  | *fds_p*,     |
|                              |     | DBusError \*     | *error*      |
|                              | )   |                  |              |

Creates a socket and binds it to the given path, then listens on the socket.

The socket is set to be nonblocking. In case of port=0 a random free port is used and returned in the port parameter. If inaddr_any is specified, the hostname is ignored.

This will set FD_CLOEXEC for the socket returned

Parameters  
|           |                                                         |
|-----------|---------------------------------------------------------|
| host      | the host name to listen on                              |
| port      | the port to listen on, if zero a free port will be used |
| family    | the address family to listen on, NULL for all           |
| retport   | string to return the actual port listened on            |
| retfamily | string to return the actual family listened on          |
| fds_p     | location to store returned file descriptors             |
| error     | return location for errors                              |

<!-- -->

Returns  
the number of listening file descriptors or -1 on error

The socket is set to be nonblocking. In case of port=0 a random free port is used and returned in the port parameter. If inaddr_any is specified, the hostname is ignored.

Parameters  
|           |                                                         |
|-----------|---------------------------------------------------------|
| host      | the host name to listen on                              |
| port      | the port to listen on, if zero a free port will be used |
| family    | the address family to listen on, NULL for all           |
| retport   | string to return the actual port listened on            |
| retfamily | string to return the actual family listened on          |
| fds_p     | location to store returned file descriptors             |
| error     | return location for errors                              |

<!-- -->

Returns  
the number of listening file descriptors or -1 on error

Definition at line 1606 of file dbus-sysdeps-unix.c.

References \_dbus_assert, \_dbus_close(), \_dbus_error_from_errno(), \_dbus_list_append(), \_dbus_list_pop_first(), \_dbus_set_socket_nonblocking(), \_dbus_string_append(), \_dbus_string_get_const_data(), \_dbus_string_get_length(), \_dbus_warn(), \_DBUS_ZERO, DBUS_ERROR_BAD_ADDRESS, dbus_error_free(), dbus_error_init(), DBUS_ERROR_INVALID_ARGS, DBUS_ERROR_NO_MEMORY, dbus_free(), dbus_new0, dbus_realloc(), dbus_set_error(), FALSE, NULL, and TRUE.

Referenced by \_dbus_server_new_for_tcp_socket().

## ◆ \_dbus_listen_unix_socket()

|                                      |     |                |             |
|--------------------------------------|-----|----------------|-------------|
| DBusSocket \_dbus_listen_unix_socket | (   | const char \*  | *path*,     |
|                                      |     | dbus_bool_t    | *abstract*, |
|                                      |     | DBusError \*   | *error*     |
|                                      | )   |                |             |

Creates a socket and binds it to the given path, then listens on the socket.

The socket is set to be nonblocking.

Uses abstract sockets instead of filesystem-linked sockets if requested (it's possible only on Linux; see "man 7 unix" on Linux). On non-Linux abstract socket usage always fails.

This will set FD_CLOEXEC for the socket returned

Parameters  
|          |                                |
|----------|--------------------------------|
| path     | the socket name                |
| abstract | TRUE to use abstract namespace |
| error    | return location for errors     |

<!-- -->

Returns  
a valid socket on success or an invalid socket on error

The socket is set to be nonblocking.

Abstract socket usage always fails.

This will set CLOEXEC for the socket returned

Parameters  
|          |                                |
|----------|--------------------------------|
| path     | the socket name                |
| abstract | TRUE to use abstract namespace |
| error    | return location for errors     |

<!-- -->

Returns  
a valid socket on success or an invalid socket on error

Definition at line 1170 of file dbus-sysdeps-unix.c.

References \_dbus_close(), \_dbus_close_socket(), \_dbus_error_from_errno(), \_DBUS_MAX_SUN_PATH_LENGTH, \_dbus_set_socket_nonblocking(), \_dbus_warn(), \_DBUS_ZERO, DBUS_ERROR_BAD_ADDRESS, DBUS_ERROR_NOT_SUPPORTED, dbus_set_error(), and NULL.

Referenced by \_dbus_server_new_for_domain_socket().

## ◆ \_dbus_log()

|                                     |     |                        |             |
|-------------------------------------|-----|------------------------|-------------|
| DBUS_PRIVATE_EXPORT void \_dbus_log | (   | DBusSystemLogSeverity  | *severity*, |
|                                     |     | const char \*          | *msg*,      |
|                                     |     |                        | *...*       |
|                                     | )   |                        |             |

Log a message to the system log file (e.g.

syslog on Unix) and/or stderr.

Parameters  
|          |                              |
|----------|------------------------------|
| severity | a severity value             |
| msg      | a printf-style format string |

Definition at line 736 of file dbus-sysdeps.c.

References \_dbus_logv().

## ◆ \_dbus_logv()

|                                      |     |                        |             |
|--------------------------------------|-----|------------------------|-------------|
| DBUS_PRIVATE_EXPORT void \_dbus_logv | (   | DBusSystemLogSeverity  | *severity*, |
|                                      |     | const char \*          | *msg*,      |
|                                      |     | va_list                | *args*      |
|                                      | )   |                        |             |

Log a message to the system log file (e.g.

syslog on Unix) and/or stderr.

Parameters  
|          |                                 |
|----------|---------------------------------|
| severity | a severity value                |
| msg      | a printf-style format string    |
| args     | arguments for the format string |

syslog on Unix).

Parameters  
|          |                                 |
|----------|---------------------------------|
| severity | a severity value                |
| msg      | a printf-style format string    |
| args     | arguments for the format string |

Definition at line 5208 of file dbus-sysdeps-unix.c.

References \_dbus_assert_not_reached, \_dbus_getpid(), \_dbus_pid_for_log(), \_dbus_string_append_printf(), \_dbus_string_append_printf_valist(), \_dbus_string_free(), \_dbus_string_get_const_data(), \_dbus_string_init(), DBUS_PID_FORMAT, and NULL.

Referenced by \_dbus_log(), \_dbus_warn(), and \_dbus_warn_check_failed().

## ◆ \_dbus_lookup_session_address()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_lookup_session_address | ( | dbus_bool_t \*  | *supported*, |
|  |  | DBusString \*  | *address*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Determines the address of the session bus by querying a platform-specific method.

The first parameter will be a boolean specifying whether or not a dynamic session lookup is supported on this platform.

If supported is TRUE and the return value is TRUE, the address will be appended to `address`. If a failure happens, returns FALSE and sets an error in `error`.

If supported is FALSE, ignore the return value.

Parameters  
|           |                                                   |
|-----------|---------------------------------------------------|
| supported | returns whether this method is supported          |
| address   | a DBusString where the address can be stored      |
| error     | a DBusError to store the error in case of failure |

<!-- -->

Returns  
TRUE on success, FALSE if an error happened

Definition at line 4670 of file dbus-sysdeps-unix.c.

References FALSE, and TRUE.

## ◆ \_dbus_parse_unix_group_from_config()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_parse_unix_group_from_config | ( | const DBusString \*  | *groupname*, |
|  |  | dbus_gid_t \*  | *gid_p*  |
|  | ) |  |  |

Parse a UNIX group from the bus config file.

On Windows, this should simply always fail (just return FALSE).

Parameters  
|           |                         |
|-----------|-------------------------|
| groupname | the groupname text      |
| gid_p     | place to return the gid |

<!-- -->

Returns  
TRUE on success

Definition at line 935 of file dbus-sysdeps-util-unix.c.

References \_dbus_get_group_id(), and FALSE.

## ◆ \_dbus_parse_unix_user_from_config()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_parse_unix_user_from_config | ( | const DBusString \*  | *username*, |
|  |  | dbus_uid_t \*  | *uid_p*  |
|  | ) |  |  |

Parse a UNIX user from the bus config file.

On Windows, this should simply always fail (just return FALSE).

Parameters  
|          |                         |
|----------|-------------------------|
| username | the username text       |
| uid_p    | place to return the uid |

<!-- -->

Returns  
TRUE on success

Definition at line 919 of file dbus-sysdeps-util-unix.c.

References \_dbus_get_user_id(), and FALSE.

## ◆ \_dbus_path_is_absolute()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_path_is_absolute | ( | const DBusString \*  | *filename* | ) |  |

Checks whether the filename is an absolute path.

Parameters  
|          |              |
|----------|--------------|
| filename | the filename |

<!-- -->

Returns  
TRUE if an absolute path

Definition at line 576 of file dbus-sysdeps-util-unix.c.

References \_dbus_string_get_byte(), \_dbus_string_get_length(), and FALSE.

## ◆ \_dbus_pid_for_log()

|                                  |     |       |     |     |     |
|----------------------------------|-----|-------|-----|-----|-----|
| unsigned long \_dbus_pid_for_log | (   | void  |     | )   |     |

The only reason this is separate from \_dbus_getpid() is to allow it on Windows for logging but not for other purposes.

Returns  
process ID to put in log messages

Definition at line 3157 of file dbus-sysdeps-unix.c.

References \_dbus_getpid().

Referenced by \_dbus_abort(), and \_dbus_logv().

## ◆ \_dbus_poll()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT int \_dbus_poll | ( | DBusPollFD \*  | *fds*, |
|  |  | int  | *n_fds*, |
|  |  | int  | *timeout_milliseconds*  |
|  | ) |  |  |

Wrapper for poll().

Parameters  
|                      |                                    |
|----------------------|------------------------------------|
| fds                  | the file descriptors to poll       |
| n_fds                | number of descriptors in the array |
| timeout_milliseconds | timeout or -1 for infinite         |

<!-- -->

Returns  
numbers of fds with revents, or \<0 on error

Definition at line 3303 of file dbus-sysdeps-unix.c.

References \_DBUS_POLLERR, \_DBUS_POLLIN, \_DBUS_POLLOUT, DBusPollFD::events, DBusPollFD::fd, NULL, and DBusPollFD::revents.

## ◆ \_dbus_print_backtrace()

|                                                 |     |       |     |     |     |
|-------------------------------------------------|-----|-------|-----|-----|-----|
| DBUS_PRIVATE_EXPORT void \_dbus_print_backtrace | (   | void  |     | )   |     |

On GNU libc systems, print a crude backtrace to stderr.

On other systems, print "no backtrace support" and block for possible gdb attachment if an appropriate environment variable is set.

Definition at line 204 of file dbus-backtrace-win.c.

## ◆ \_dbus_printf_string_upper_bound()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT int \_dbus_printf_string_upper_bound | ( | const char \*  | *format*, |
|  |  | va_list  | *args*  |
|  | ) |  |  |

Measure the length of the given format string and arguments, not including the terminating nul.

Parameters  
|        |                                 |
|--------|---------------------------------|
| format | a printf-style format string    |
| args   | arguments for the format string |

<!-- -->

Returns  
length of the given format string and args, or -1 if no memory

Measure the length of the given format string and arguments, not including the terminating nul.

Definition at line 3959 of file dbus-sysdeps-unix.c.

References dbus_free(), dbus_malloc(), and NULL.

Referenced by \_dbus_string_append_printf_valist().

## ◆ \_dbus_read_credentials_socket()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_read_credentials_socket | ( | DBusSocket  | *handle*, |
|  |  | DBusCredentials \*  | *credentials*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Reads a single byte which must be nul (an error occurs otherwise), and reads unix credentials if available.

Clears the credentials object, then adds pid/uid if available, so any previous credentials stored in the object are lost.

DBusServer makes the security assumption that the credentials returned by this method are the credentials that were active at the time the socket was opened. Do not add APIs to this method that would break that assumption.

In particular, it is incorrect to use any API of the form "get the process ID at the other end of the connection, then determine its uid, gid, or other credentials from the pid" (e.g. looking in /proc on Linux). If we did that, we would be vulnerable to several attacks. A malicious process could queue up the rest of the authentication handshake and a malicious message that it should not be allowed to send, then race with the DBusServer to exec() a more privileged (e.g. setuid) binary that would have been allowed to send that message; or it could exit, and arrange for enough setuid processes to be started that its pid would be recycled for one of those processes with high probability; or it could fd-pass the connection to a more privileged process.

Return value indicates whether a byte was read, not whether we got valid credentials. On some systems, such as Linux, reading/writing the byte isn't actually required, but we do it anyway just to avoid multiple codepaths.

Fails if no byte is available, so you must select() first.

The point of the byte is that on some systems we have to use sendmsg()/recvmsg() to transmit credentials.

Parameters  
|             |                                     |
|-------------|-------------------------------------|
| client_fd   | the client file descriptor          |
| credentials | object to add client credentials to |
| error       | location to store error code        |

<!-- -->

Returns  
TRUE on success

Fills in pid/uid/gid with -1 if no credentials are available. Return value indicates whether a byte was read, not whether we got valid credentials. On some systems, such as Linux, reading/writing the byte isn't actually required, but we do it anyway just to avoid multiple codepaths.

Fails if no byte is available, so you must select() first.

The point of the byte is that on some systems we have to use sendmsg()/recvmsg() to transmit credentials.

Parameters  
|             |                                           |
|-------------|-------------------------------------------|
| handle      | the client file descriptor                |
| credentials | struct to fill with credentials of client |
| error       | location to store error code              |

<!-- -->

Returns  
TRUE on success

Definition at line 2209 of file dbus-sysdeps-unix.c.

References \_dbus_credentials_add_adt_audit_data(), \_dbus_credentials_add_pid(), \_dbus_credentials_add_unix_uid(), \_dbus_credentials_add_windows_sid(), \_dbus_credentials_clear(), \_dbus_credentials_take_pid_fd(), \_dbus_error_from_errno(), \_dbus_read_socket(), \_dbus_string_free(), \_dbus_string_init(), \_DBUS_ZERO, DBUS_ERROR_FAILED, dbus_error_is_set(), DBUS_GID_UNSET, DBUS_PID_FORMAT, DBUS_PID_UNSET, dbus_set_error(), DBUS_UID_FORMAT, DBUS_UID_UNSET, FALSE, NULL, and TRUE.

## ◆ \_dbus_read_local_machine_uuid()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_read_local_machine_uuid | ( | DBusGUID \*  | *machine_id*, |
|  |  | dbus_bool_t  | *create_if_not_found*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Reads the uuid of the machine we're running on from the dbus configuration.

Optionally try to create it (only root can do this usually).

On UNIX, reads a file that gets created by dbus-uuidgen in a post-install script. On Windows, if there's a standard machine uuid we could just use that, but I can't find one with the right properties (the hardware profile guid can change without rebooting I believe). If there's no standard one we might want to use the registry instead of a file for this, and I'm not sure how we'd ensure the uuid gets created.

Parameters  
|                     |                                            |
|---------------------|--------------------------------------------|
| machine_id          | guid to init with the machine's uuid       |
| create_if_not_found | try to create the uuid if it doesn't exist |
| error               | the error return                           |

<!-- -->

Returns  
FALSE if the error is set

Definition at line 4421 of file dbus-sysdeps-unix.c.

References \_dbus_generate_uuid(), \_dbus_read_uuid_file(), \_dbus_string_init_const(), \_dbus_write_uuid_file(), DBusGUID::as_uint32s, dbus_error_free(), DBUS_ERROR_INIT, DBUS_ERROR_NO_MEMORY, dbus_set_error(), FALSE, DBusError::message, DBusError::name, NULL, and TRUE.

Referenced by \_dbus_get_local_machine_uuid_encoded(), and \_dbus_get_uuid().

## ◆ \_dbus_read_socket()

|                                            |     |                |           |
|--------------------------------------------|-----|----------------|-----------|
| DBUS_PRIVATE_EXPORT int \_dbus_read_socket | (   | DBusSocket     | *fd*,     |
|                                            |     | DBusString \*  | *buffer*, |
|                                            |     | int            | *count*   |
|                                            | )   |                |           |

Like \_dbus_read(), but only works on sockets so is available on Windows.

Parameters  
|        |                            |
|--------|----------------------------|
| fd     | the socket                 |
| buffer | string to append data to   |
| count  | max amount of data to read |

<!-- -->

Returns  
number of bytes appended to the string

Like \_dbus_read(), but only works on sockets so is available on Windows.

Thin wrapper around the read() system call that appends the data it reads to the DBusString buffer. It appends up to the given count, and returns the same value and same errno as read(). The only exception is that \_dbus_read_socket() handles EINTR for you. \_dbus_read_socket() can return ENOMEM, even though regular UNIX read doesn't.

Parameters  
|        |                                  |
|--------|----------------------------------|
| fd     | the file descriptor to read from |
| buffer | the buffer to append data to     |
| count  | the amount of data to read       |

<!-- -->

Returns  
the number of bytes read or -1

Definition at line 338 of file dbus-sysdeps-unix.c.

References \_dbus_assert, \_dbus_read(), \_dbus_string_get_data_len(), \_dbus_string_get_length(), \_dbus_string_lengthen(), \_dbus_string_set_length(), and \_dbus_verbose_bytes_of_string().

Referenced by \_dbus_read_credentials_socket(), and \_dbus_read_socket_with_unix_fds().

## ◆ \_dbus_read_socket_with_unix_fds()

|                                      |     |                  |           |
|--------------------------------------|-----|------------------|-----------|
| int \_dbus_read_socket_with_unix_fds | (   | DBusSocket       | *fd*,     |
|                                      |     | DBusString \*    | *buffer*, |
|                                      |     | int              | *count*,  |
|                                      |     | int \*           | *fds*,    |
|                                      |     | unsigned int \*  | *n_fds*   |
|                                      | )   |                  |           |

Like \_dbus_read_socket() but also tries to read unix fds from the socket.

When there are more fds to read than space in the array passed this function will fail with ENOSPC.

Parameters  
|  |  |
|----|----|
| fd | the socket |
| buffer | string to append data to |
| count | max amount of data to read |
| fds | array to place read file descriptors in |
| n_fds | on input space in fds array, on output how many fds actually got read |

<!-- -->

Returns  
number of bytes appended to string

Definition at line 394 of file dbus-sysdeps-unix.c.

References \_dbus_assert, \_dbus_fd_set_close_on_exec(), \_dbus_read_socket(), \_dbus_string_get_data_len(), \_dbus_string_get_length(), \_dbus_string_lengthen(), \_dbus_string_set_length(), \_dbus_verbose_bytes_of_string(), \_DBUS_ZERO, DBUS_MAXIMUM_MESSAGE_UNIX_FDS, FALSE, NULL, and TRUE.

## ◆ \_dbus_replace_install_prefix()

|                                           |     |                |        |     |     |
|-------------------------------------------|-----|----------------|--------|-----|-----|
| dbus_bool_t \_dbus_replace_install_prefix | (   | DBusString \*  | *path* | )   |     |

Replace the DBUS_PREFIX in the given path, in-place, by the current D-Bus installation directory.

On Unix this function does nothing, successfully.

Parameters  
|      |              |
|------|--------------|
| path | path to edit |

<!-- -->

Returns  
FALSE on OOM

Definition at line 1185 of file dbus-sysdeps-util-unix.c.

References \_dbus_string_free(), \_dbus_string_get_byte(), \_dbus_string_get_length(), \_dbus_string_init(), \_dbus_string_replace_len(), \_dbus_string_set_byte(), \_dbus_string_starts_with_c_str(), FALSE, and TRUE.

Referenced by \_dbus_get_standard_session_servicedirs().

## ◆ \_dbus_resolve_pid_fd()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_pid_t \_dbus_resolve_pid_fd | ( | int  | *pid_fd* | ) |  |

Resolve the PID from the PID FD, if any.

This allows us to avoid PID reuse attacks. Returns DBUS_PID_UNSET if the PID could not be resolved. Note that this requires being able to read /proc/self/fdinfo/\<FD\>, which is created as 600 and owned by the original UID that the process started as. So it cannot work when the start as root and drop privileges mechanism is in use (the systemd unit no longer does this, but third-party init-scripts might).

Parameters  
|        |            |
|--------|------------|
| pid_fd | the PID FD |

<!-- -->

Returns  
the resolved PID if found, DBUS_PID_UNSET otherwise

Definition at line 3045 of file dbus-sysdeps-unix.c.

References \_dbus_file_get_contents(), \_dbus_string_append_printf(), \_dbus_string_find(), \_dbus_string_free(), \_dbus_string_get_byte(), \_dbus_string_init(), \_dbus_string_parse_uint(), dbus_error_free(), DBUS_ERROR_INIT, DBUS_PID_UNSET, DBusError::message, DBusError::name, and NULL.

Referenced by \_dbus_credentials_get_pid().

## ◆ \_dbus_restore_socket_errno()

|                                  |     |      |               |     |     |
|----------------------------------|-----|------|---------------|-----|-----|
| void \_dbus_restore_socket_errno | (   | int  | *saved_errno* | )   |     |

Definition at line 5158 of file dbus-sysdeps-unix.c.

## ◆ \_dbus_rlimit_free()

|                         |     |                |       |     |     |
|-------------------------|-----|----------------|-------|-----|-----|
| void \_dbus_rlimit_free | (   | DBusRLimit \*  | *lim* | )   |     |

Definition at line 534 of file dbus-sysdeps-util-unix.c.

## ◆ \_dbus_rlimit_raise_fd_limit()

|                                          |     |               |         |     |     |
|------------------------------------------|-----|---------------|---------|-----|-----|
| dbus_bool_t \_dbus_rlimit_raise_fd_limit | (   | DBusError \*  | *error* | )   |     |

Definition at line 517 of file dbus-sysdeps-util-unix.c.

## ◆ \_dbus_rlimit_restore_fd_limit()

|                                            |     |                |          |
|--------------------------------------------|-----|----------------|----------|
| dbus_bool_t \_dbus_rlimit_restore_fd_limit | (   | DBusRLimit \*  | *saved*, |
|                                            |     | DBusError \*   | *error*  |
|                                            | )   |                |          |

Definition at line 524 of file dbus-sysdeps-util-unix.c.

## ◆ \_dbus_rlimit_save_fd_limit()

|                                           |     |               |         |     |     |
|-------------------------------------------|-----|---------------|---------|-----|-----|
| DBusRLimit \* \_dbus_rlimit_save_fd_limit | (   | DBusError \*  | *error* | )   |     |

Definition at line 510 of file dbus-sysdeps-util-unix.c.

## ◆ \_dbus_save_socket_errno()

|                              |     |       |     |     |     |
|------------------------------|-----|-------|-----|-----|-----|
| int \_dbus_save_socket_errno | (   | void  |     | )   |     |

Definition at line 5152 of file dbus-sysdeps-unix.c.

## ◆ \_dbus_send_credentials_socket()

|                                            |     |               |              |
|--------------------------------------------|-----|---------------|--------------|
| dbus_bool_t \_dbus_send_credentials_socket | (   | DBusSocket    | *server_fd*, |
|                                            |     | DBusError \*  | *error*      |
|                                            | )   |               |              |

Sends a single nul byte with our UNIX credentials as ancillary data.

Returns TRUE if the data was successfully written. On systems that don't support sending credentials, just writes a byte, doesn't send any credentials. On some systems, such as Linux, reading/writing the byte isn't actually required, but we do it anyway just to avoid multiple codepaths.

Fails if no byte can be written, so you must select() first.

The point of the byte is that on some systems we have to use sendmsg()/recvmsg() to transmit credentials.

Parameters  
|           |                                          |
|-----------|------------------------------------------|
| server_fd | file descriptor for connection to server |
| error     | return location for error code           |

<!-- -->

Returns  
TRUE if the byte was sent

Definition at line 2568 of file dbus-sysdeps-unix.c.

References \_dbus_assert, \_dbus_error_from_errno(), \_dbus_strerror_from_errno(), \_dbus_string_init_const_len(), \_dbus_write_socket(), DBUS_ERROR_IO_ERROR, dbus_set_error(), FALSE, and TRUE.

## ◆ \_dbus_set_errno_to_zero()

|                               |     |       |     |     |     |
|-------------------------------|-----|-------|-----|-----|-----|
| void \_dbus_set_errno_to_zero | (   | void  |     | )   |     |

Assign 0 to the global errno variable.

Definition at line 666 of file dbus-sysdeps.c.

Referenced by \_dbus_string_parse_int(), \_dbus_string_parse_int64(), and \_dbus_string_parse_uint().

## ◆ \_dbus_set_error_with_inet_sockaddr()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_set_error_with_inet_sockaddr | ( | DBusError \*  | *error*, |
|  |  | const void \*  | *sockaddr_pointer*, |
|  |  | size_t  | *len*, |
|  |  | const char \*  | *description*, |
|  |  | int  | *saved_errno*  |
|  | ) |  |  |

Definition at line 849 of file dbus-sysdeps.c.

## ◆ \_dbus_set_socket_nonblocking()

|                                           |     |               |           |
|-------------------------------------------|-----|---------------|-----------|
| dbus_bool_t \_dbus_set_socket_nonblocking | (   | DBusSocket    | *handle*, |
|                                           |     | DBusError \*  | *error*   |
|                                           | )   |               |           |

Sets a file descriptor to be nonblocking.

Parameters  
|       |                            |
|-------|----------------------------|
| fd    | the file descriptor.       |
| error | address of error location. |

<!-- -->

Returns  
TRUE on success.

<!-- -->

Parameters  
|        |                            |
|--------|----------------------------|
| handle | the file descriptor.       |
| error  | address of error location. |

<!-- -->

Returns  
TRUE on success.

Definition at line 3797 of file dbus-sysdeps-unix.c.

References \_dbus_error_from_errno(), \_dbus_strerror_from_errno(), dbus_set_error(), FALSE, and TRUE.

Referenced by \_dbus_connect_unix_socket(), \_dbus_listen_tcp_socket(), and \_dbus_listen_unix_socket().

## ◆ \_dbus_set_up_transient_session_servicedirs()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_set_up_transient_session_servicedirs | ( | DBusList \*\*  | *dirs*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Returns the standard directories for a session bus to look for transient service activation files.

Parameters  
|      |                                     |
|------|-------------------------------------|
| dirs | the directory list we are returning |

<!-- -->

Returns  
FALSE on error

On Windows, there are none.

Parameters  
|      |                                     |
|------|-------------------------------------|
| dirs | the directory list we are returning |

<!-- -->

Returns  
TRUE

Definition at line 1267 of file dbus-sysdeps-util-unix.c.

References \_dbus_getenv(), \_dbus_list_append(), \_dbus_string_append(), \_dbus_string_append_printf(), \_dbus_string_free(), \_dbus_string_init(), \_dbus_string_steal_data(), dbus_free(), FALSE, NULL, and TRUE.

## ◆ \_dbus_sleep_milliseconds()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT void \_dbus_sleep_milliseconds | ( | int  | *milliseconds* | ) |  |

Sleeps the given number of milliseconds.

Parameters  
|              |                        |
|--------------|------------------------|
| milliseconds | number of milliseconds |

Definition at line 3542 of file dbus-sysdeps-unix.c.

Referenced by \_dbus_abort().

## ◆ \_dbus_socket_can_pass_unix_fd()

|                                            |     |             |      |     |     |
|--------------------------------------------|-----|-------------|------|-----|-----|
| dbus_bool_t \_dbus_socket_can_pass_unix_fd | (   | DBusSocket  | *fd* | )   |     |

Checks whether file descriptors may be passed via the socket.

Parameters  
|     |            |
|-----|------------|
| fd  | the socket |

<!-- -->

Returns  
TRUE when fd passing over this socket is supported

Definition at line 4850 of file dbus-sysdeps-unix.c.

References \_DBUS_ZERO, and FALSE.

Referenced by \_dbus_transport_new_for_socket().

## ◆ \_dbus_socketpair()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_socketpair | ( | DBusSocket \*  | *fd1*, |
|  |  | DBusSocket \*  | *fd2*, |
|  |  | dbus_bool_t  | *blocking*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Creates pair of connect sockets (as in socketpair()).

Sets both ends of the pair nonblocking.

Marks both file descriptors as close-on-exec

Parameters  
|          |                                   |
|----------|-----------------------------------|
| fd1      | return location for one end       |
| fd2      | return location for the other end |
| blocking | TRUE if pair should be blocking   |
| error    | error return                      |

<!-- -->

Returns  
FALSE on failure (if error is set)

Definition at line 3884 of file dbus-sysdeps-unix.c.

References \_dbus_close(), \_dbus_error_from_errno(), \_dbus_fd_set_close_on_exec(), \_dbus_strerror_from_errno(), \_dbus_warn(), \_DBUS_ZERO, DBUS_ERROR_FAILED, dbus_set_error(), FALSE, NULL, and TRUE.

Referenced by \_dbus_spawn_async_with_babysitter().

## ◆ \_dbus_split_paths_and_append()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_split_paths_and_append | ( | DBusString \*  | *dirs*, |
|  |  | const char \*  | *suffix*, |
|  |  | DBusList \*\*  | *dir_list*  |
|  | ) |  |  |

Split paths into a list of char strings.

Parameters  
|  |  |
|----|----|
| dirs | string with pathes |
| suffix | string concated to each path in dirs |
| dir_list | contains a list of splitted pathes return TRUE is pathes could be splittes,FALSE in oom case |

Definition at line 238 of file dbus-sysdeps.c.

References \_dbus_concat_dir_and_file(), \_dbus_list_append(), \_dbus_list_clear_full(), \_dbus_string_chop_white(), \_dbus_string_copy_data(), \_dbus_string_copy_len(), \_dbus_string_find(), \_dbus_string_free(), \_dbus_string_get_length(), \_dbus_string_init(), \_dbus_string_init_const(), dbus_free(), FALSE, and TRUE.

Referenced by \_dbus_get_local_system_servicedirs(), \_dbus_get_standard_session_servicedirs(), and \_dbus_get_standard_system_servicedirs().

## ◆ \_dbus_stat()

|                         |     |                      |             |
|-------------------------|-----|----------------------|-------------|
| dbus_bool_t \_dbus_stat | (   | const DBusString \*  | *filename*, |
|                         |     | DBusStat \*          | *statbuf*,  |
|                         |     | DBusError \*         | *error*     |
|                         | )   |                      |             |

stat() wrapper.

Parameters  
|          |                           |
|----------|---------------------------|
| filename | the filename to stat      |
| statbuf  | the stat info to fill in  |
| error    | return location for error |

<!-- -->

Returns  
FALSE if error was set

Definition at line 593 of file dbus-sysdeps-util-unix.c.

References \_dbus_error_from_errno(), \_dbus_string_get_const_data(), DBusStat::atime, DBusStat::ctime, DBUS_GID_UNSET, DBUS_INT64_CONSTANT, dbus_set_error(), DBUS_UID_UNSET, FALSE, DBusStat::gid, DBusStat::mode, DBusStat::mtime, DBusStat::nlink, NULL, DBusStat::size, TRUE, and DBusStat::uid.

Referenced by \_dbus_is_console_user().

## ◆ \_dbus_strerror_from_errno()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT const char \* \_dbus_strerror_from_errno | ( | void  |  | ) |  |

Get error message from errno.

Returns  
\_dbus_strerror(errno)

Definition at line 724 of file dbus-sysdeps.c.

Referenced by \_dbus_close_socket(), \_dbus_create_directory(), \_dbus_delete_file(), \_dbus_ensure_directory(), \_dbus_send_credentials_socket(), \_dbus_set_socket_nonblocking(), \_dbus_socketpair(), \_dbus_write_socket(), and \_dbus_write_socket_two().

## ◆ \_dbus_string_get_dirname()

|                                       |     |                      |             |
|---------------------------------------|-----|----------------------|-------------|
| dbus_bool_t \_dbus_string_get_dirname | (   | const DBusString \*  | *filename*, |
|                                       |     | DBusString \*        | *dirname*   |
|                                       | )   |                      |             |

Get the directory name from a complete filename.

Parameters  
|          |                                    |
|----------|------------------------------------|
| filename | the filename                       |
| dirname  | string to append directory name to |

<!-- -->

Returns  
FALSE if no memory

Definition at line 1018 of file dbus-sysdeps-util-unix.c.

References \_dbus_assert, \_dbus_string_append(), \_dbus_string_copy_len(), \_dbus_string_find_byte_backward(), \_dbus_string_get_byte(), \_dbus_string_get_length(), and NULL.

## ◆ \_dbus_threads_init_platform_specific()

|                                                   |     |       |     |     |     |
|---------------------------------------------------|-----|-------|-----|-----|-----|
| dbus_bool_t \_dbus_threads_init_platform_specific | (   | void  |     | )   |     |

Initialize threads as in dbus_threads_init_default(), appropriately for the platform.

Returns  
FALSE if no memory

Definition at line 281 of file dbus-sysdeps-pthread.c.

References \_dbus_check_setuid(), FALSE, and TRUE.

Referenced by dbus_threads_init().

## ◆ \_dbus_threads_lock_platform_specific()

|                                            |     |       |     |     |     |
|--------------------------------------------|-----|-------|-----|-----|-----|
| void \_dbus_threads_lock_platform_specific | (   | void  |     | )   |     |

Lock a static mutex used to protect \_dbus_threads_init_platform_specific().

Definition at line 296 of file dbus-sysdeps-pthread.c.

References \_dbus_assert.

Referenced by dbus_shutdown(), and dbus_threads_init().

## ◆ \_dbus_threads_unlock_platform_specific()

|                                              |     |       |     |     |     |
|----------------------------------------------|-----|-------|-----|-----|-----|
| void \_dbus_threads_unlock_platform_specific | (   | void  |     | )   |     |

Undo \_dbus_threads_lock_platform_specific().

Definition at line 302 of file dbus-sysdeps-pthread.c.

References \_dbus_assert.

Referenced by dbus_shutdown(), and dbus_threads_init().

## ◆ \_dbus_unix_groups_from_uid()

|                                         |     |                  |                |
|-----------------------------------------|-----|------------------|----------------|
| dbus_bool_t \_dbus_unix_groups_from_uid | (   | dbus_uid_t       | *uid*,         |
|                                         |     | dbus_gid_t \*\*  | *group_ids*,   |
|                                         |     | int \*           | *n_group_ids*, |
|                                         |     | DBusError \*     | *error*        |
|                                         | )   |                  |                |

Gets all groups corresponding to the given UNIX user ID.

On UNIX, just calls \_dbus_groups_from_uid(). On Windows, should always fail since we don't know any UNIX groups.

Parameters  
|             |                                              |
|-------------|----------------------------------------------|
| uid         | the UID                                      |
| group_ids   | return location for array of group IDs       |
| n_group_ids | return location for length of returned array |
| error       | error location                               |

<!-- -->

Returns  
TRUE if the UID existed and we got some credentials

Definition at line 953 of file dbus-sysdeps-util-unix.c.

References \_dbus_groups_from_uid(), and FALSE.

## ◆ \_dbus_unix_user_is_at_console()

|                                            |     |               |          |
|--------------------------------------------|-----|---------------|----------|
| dbus_bool_t \_dbus_unix_user_is_at_console | (   | dbus_uid_t    | *uid*,   |
|                                            |     | DBusError \*  | *error*  |
|                                            | )   |               |          |

Checks to see if the UNIX user ID is at the console.

Should always fail on Windows (set the error to DBUS_ERROR_NOT_SUPPORTED).

Parameters  
|       |                            |
|-------|----------------------------|
| uid   | UID of person to check     |
| error | return location for errors |

<!-- -->

Returns  
TRUE if the UID is the same as the console user and there are no errors

Definition at line 971 of file dbus-sysdeps-util-unix.c.

References \_dbus_is_console_user(), and FALSE.

## ◆ \_dbus_unix_user_is_process_owner()

|                                               |     |             |       |     |     |
|-----------------------------------------------|-----|-------------|-------|-----|-----|
| dbus_bool_t \_dbus_unix_user_is_process_owner | (   | dbus_uid_t  | *uid* | )   |     |

Checks to see if the UNIX user ID matches the UID of the process.

Should always return FALSE on Windows.

Parameters  
|     |                  |
|-----|------------------|
| uid | the UNIX user ID |

<!-- -->

Returns  
TRUE if this uid owns the process.

Definition at line 986 of file dbus-sysdeps-util-unix.c.

References \_dbus_geteuid(), and FALSE.

## ◆ \_dbus_verify_daemon_user()

|                                       |     |                |        |     |     |
|---------------------------------------|-----|----------------|--------|-----|-----|
| dbus_bool_t \_dbus_verify_daemon_user | (   | const char \*  | *user* | )   |     |

Verify that after the fork we can successfully change to this user.

Parameters  
|      |                                                |
|------|------------------------------------------------|
| user | the username given in the daemon configuration |

<!-- -->

Returns  
TRUE if username is valid

Definition at line 313 of file dbus-sysdeps-util-unix.c.

References \_dbus_get_user_id_and_primary_group(), \_dbus_string_init_const(), NULL, and TRUE.

## ◆ \_dbus_windows_user_is_process_owner()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_windows_user_is_process_owner | ( | const char \*  | *windows_sid* | ) |  |

Checks to see if the Windows user SID matches the owner of the process.

Should always return FALSE on UNIX.

Parameters  
|             |                      |
|-------------|----------------------|
| windows_sid | the Windows user SID |

<!-- -->

Returns  
TRUE if this user owns the process.

Definition at line 999 of file dbus-sysdeps-util-unix.c.

References FALSE, and TRUE.

## ◆ \_dbus_write_pid_to_file_and_pipe()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_write_pid_to_file_and_pipe | ( | const DBusString \*  | *pidfile*, |
|  |  | DBusPipe \*  | *print_pid_pipe*, |
|  |  | dbus_pid_t  | *pid_to_write*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Writes the given pid_to_write to a pidfile (if non-NULL) and/or to a pipe (if non-NULL).

Does nothing if pidfile and print_pid_pipe are both NULL.

Parameters  
|                |                              |
|----------------|------------------------------|
| pidfile        | the file to write to or NULL |
| print_pid_pipe | the pipe to write to or NULL |
| pid_to_write   | the pid to write out         |
| error          | error on failure             |

<!-- -->

Returns  
FALSE if error is set

Definition at line 240 of file dbus-sysdeps-util-unix.c.

References \_dbus_string_append_printf(), \_dbus_string_free(), \_dbus_string_get_const_data(), \_dbus_string_get_length(), \_dbus_string_init(), DBUS_ERROR_FAILED, dbus_error_is_set(), DBUS_PID_FORMAT, dbus_set_error(), FALSE, NULL, and TRUE.

Referenced by \_dbus_become_daemon().

## ◆ \_dbus_write_socket()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT int \_dbus_write_socket | ( | DBusSocket  | *fd*, |
|  |  | const DBusString \*  | *buffer*, |
|  |  | int  | *start*, |
|  |  | int  | *len*  |
|  | ) |  |  |

Like \_dbus_write(), but only supports sockets and is thus available on Windows.

Parameters  
|        |                                       |
|--------|---------------------------------------|
| fd     | the file descriptor to write          |
| buffer | the buffer to write data from         |
| start  | the first byte in the buffer to write |
| len    | the number of bytes to try to write   |

<!-- -->

Returns  
the number of bytes written or -1 on error

Like \_dbus_write(), but only supports sockets and is thus available on Windows.

Parameters  
|        |                                       |
|--------|---------------------------------------|
| fd     | the file descriptor to write          |
| buffer | the buffer to write data from         |
| start  | the first byte in the buffer to write |
| len    | the number of bytes to try to write   |

<!-- -->

Returns  
the number of bytes written or -1 on error

Definition at line 356 of file dbus-sysdeps-unix.c.

References \_dbus_strerror_from_errno(), \_dbus_string_get_const_data_len(), \_dbus_verbose_bytes_of_string(), and \_dbus_write().

Referenced by \_dbus_send_credentials_socket().

## ◆ \_dbus_write_socket_two()

|                             |     |                      |            |
|-----------------------------|-----|----------------------|------------|
| int \_dbus_write_socket_two | (   | DBusSocket           | *fd*,      |
|                             |     | const DBusString \*  | *buffer1*, |
|                             |     | int                  | *start1*,  |
|                             |     | int                  | *len1*,    |
|                             |     | const DBusString \*  | *buffer2*, |
|                             |     | int                  | *start2*,  |
|                             |     | int                  | *len2*     |
|                             | )   |                      |            |

Like \_dbus_write_two() but only works on sockets and is thus available on Windows.

Parameters  
|         |                                            |
|---------|--------------------------------------------|
| fd      | the file descriptor                        |
| buffer1 | first buffer                               |
| start1  | first byte to write in first buffer        |
| len1    | number of bytes to write from first buffer |
| buffer2 | second buffer, or NULL                     |
| start2  | first byte to write in second buffer       |
| len2    | number of bytes to write in second buffer  |

<!-- -->

Returns  
total bytes written from both buffers, or -1 on error

Like \_dbus_write_two() but only works on sockets and is thus available on Windows.

The return value is the number of bytes written in the first buffer, plus the number written in the second. If the first buffer is written successfully and an error occurs writing the second, the number of bytes in the first is returned (i.e. the error is ignored), on systems that don't have writev. Handles EINTR for you. The second buffer may be NULL.

Parameters  
|         |                                            |
|---------|--------------------------------------------|
| fd      | the file descriptor                        |
| buffer1 | first buffer                               |
| start1  | first byte to write in first buffer        |
| len1    | number of bytes to write from first buffer |
| buffer2 | second buffer, or NULL                     |
| start2  | first byte to write in second buffer       |
| len2    | number of bytes to write in second buffer  |

<!-- -->

Returns  
total bytes written from both buffers, or -1 on error

Definition at line 694 of file dbus-sysdeps-unix.c.

References \_dbus_assert, \_dbus_strerror_from_errno(), \_dbus_string_get_const_data_len(), \_dbus_write_two(), \_DBUS_ZERO, and NULL.

## ◆ \_dbus_write_socket_with_unix_fds()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT int \_dbus_write_socket_with_unix_fds | ( | DBusSocket  | *fd*, |
|  |  | const DBusString \*  | *buffer*, |
|  |  | int  | *start*, |
|  |  | int  | *len*, |
|  |  | const int \*  | *fds*, |
|  |  | int  | *n_fds*  |
|  | ) |  |  |

Definition at line 581 of file dbus-sysdeps-unix.c.

## ◆ \_dbus_write_socket_with_unix_fds_two()

|  |  |  |  |
|----|----|----|----|
| int \_dbus_write_socket_with_unix_fds_two | ( | DBusSocket  | *fd*, |
|  |  | const DBusString \*  | *buffer1*, |
|  |  | int  | *start1*, |
|  |  | int  | *len1*, |
|  |  | const DBusString \*  | *buffer2*, |
|  |  | int  | *start2*, |
|  |  | int  | *len2*, |
|  |  | const int \*  | *fds*, |
|  |  | int  | *n_fds*  |
|  | ) |  |  |

Definition at line 602 of file dbus-sysdeps-unix.c.
