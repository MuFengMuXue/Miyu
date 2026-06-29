Protocol constants

D-Bus low-level public API

Defines constants which are part of the D-Bus protocol. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="macros" class="groupheader"> Macros</h2></td>
</tr>
<tr id="r_gaae5e00bf9091a457e5bb3f9a75d982ca" class="memitem:gaae5e00bf9091a457e5bb3f9a75d982ca">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_LITTLE_ENDIAN   ('l')</td>
</tr>
<tr class="memdesc:gaae5e00bf9091a457e5bb3f9a75d982ca">
<td class="mdescLeft"> </td>
<td class="mdescRight">Code marking LSB-first byte order in the wire protocol.<br />
</td>
</tr>
<tr class="separator:gaae5e00bf9091a457e5bb3f9a75d982ca">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaed8596f854e755344dfbc811a73b0757" class="memitem:gaed8596f854e755344dfbc811a73b0757">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_BIG_ENDIAN   ('B')</td>
</tr>
<tr class="memdesc:gaed8596f854e755344dfbc811a73b0757">
<td class="mdescLeft"> </td>
<td class="mdescRight">Code marking MSB-first byte order in the wire protocol.<br />
</td>
</tr>
<tr class="separator:gaed8596f854e755344dfbc811a73b0757">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae1ab70067a616d852e5fc264abb66608" class="memitem:gae1ab70067a616d852e5fc264abb66608">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_MAJOR_PROTOCOL_VERSION   1</td>
</tr>
<tr class="memdesc:gae1ab70067a616d852e5fc264abb66608">
<td class="mdescLeft"> </td>
<td class="mdescRight">Protocol version.<br />
</td>
</tr>
<tr class="separator:gae1ab70067a616d852e5fc264abb66608">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa9588da889743b2119dc6664712ae51e" class="memitem:gaa9588da889743b2119dc6664712ae51e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_INVALID   ((int) '\0')</td>
</tr>
<tr class="memdesc:gaa9588da889743b2119dc6664712ae51e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Type code that is never equal to a legitimate type code.<br />
</td>
</tr>
<tr class="separator:gaa9588da889743b2119dc6664712ae51e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0ce68c19b9039f3db5a1d6f60dd14930" class="memitem:ga0ce68c19b9039f3db5a1d6f60dd14930">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_INVALID_AS_STRING   "\0"</td>
</tr>
<tr class="memdesc:ga0ce68c19b9039f3db5a1d6f60dd14930">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBUS_TYPE_INVALID as a string literal instead of a int literal<br />
</td>
</tr>
<tr class="separator:ga0ce68c19b9039f3db5a1d6f60dd14930">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga355d6d0998164a5eb915a26fb67fce5f" class="memitem:ga355d6d0998164a5eb915a26fb67fce5f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_BYTE   ((int) 'y')</td>
</tr>
<tr class="memdesc:ga355d6d0998164a5eb915a26fb67fce5f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Type code marking an 8-bit unsigned integer.<br />
</td>
</tr>
<tr class="separator:ga355d6d0998164a5eb915a26fb67fce5f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga309cc856f9b903032b55fe346268104b" class="memitem:ga309cc856f9b903032b55fe346268104b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_BYTE_AS_STRING   "y"</td>
</tr>
<tr class="memdesc:ga309cc856f9b903032b55fe346268104b">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBUS_TYPE_BYTE as a string literal instead of a int literal<br />
</td>
</tr>
<tr class="separator:ga309cc856f9b903032b55fe346268104b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga624ecee83984330ad89cbf064a2b28e6" class="memitem:ga624ecee83984330ad89cbf064a2b28e6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_BOOLEAN   ((int) 'b')</td>
</tr>
<tr class="memdesc:ga624ecee83984330ad89cbf064a2b28e6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Type code marking a boolean.<br />
</td>
</tr>
<tr class="separator:ga624ecee83984330ad89cbf064a2b28e6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2183265114080428cbfda3cffe8ac73d" class="memitem:ga2183265114080428cbfda3cffe8ac73d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_BOOLEAN_AS_STRING   "b"</td>
</tr>
<tr class="memdesc:ga2183265114080428cbfda3cffe8ac73d">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBUS_TYPE_BOOLEAN as a string literal instead of a int literal<br />
</td>
</tr>
<tr class="separator:ga2183265114080428cbfda3cffe8ac73d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga49cdd4169af84ed7937f34b31f43e331" class="memitem:ga49cdd4169af84ed7937f34b31f43e331">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_INT16   ((int) 'n')</td>
</tr>
<tr class="memdesc:ga49cdd4169af84ed7937f34b31f43e331">
<td class="mdescLeft"> </td>
<td class="mdescRight">Type code marking a 16-bit signed integer.<br />
</td>
</tr>
<tr class="separator:ga49cdd4169af84ed7937f34b31f43e331">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga21c2efd8ed6b83302f3ef2a1f759359f" class="memitem:ga21c2efd8ed6b83302f3ef2a1f759359f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_INT16_AS_STRING   "n"</td>
</tr>
<tr class="memdesc:ga21c2efd8ed6b83302f3ef2a1f759359f">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBUS_TYPE_INT16 as a string literal instead of a int literal<br />
</td>
</tr>
<tr class="separator:ga21c2efd8ed6b83302f3ef2a1f759359f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad74b8d93a1464182ac1af7e0e2435f46" class="memitem:gad74b8d93a1464182ac1af7e0e2435f46">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_UINT16   ((int) 'q')</td>
</tr>
<tr class="memdesc:gad74b8d93a1464182ac1af7e0e2435f46">
<td class="mdescLeft"> </td>
<td class="mdescRight">Type code marking a 16-bit unsigned integer.<br />
</td>
</tr>
<tr class="separator:gad74b8d93a1464182ac1af7e0e2435f46">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaee963e8da6d318a6b4fd8a73f9538c70" class="memitem:gaee963e8da6d318a6b4fd8a73f9538c70">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_UINT16_AS_STRING   "q"</td>
</tr>
<tr class="memdesc:gaee963e8da6d318a6b4fd8a73f9538c70">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBUS_TYPE_UINT16 as a string literal instead of a int literal<br />
</td>
</tr>
<tr class="separator:gaee963e8da6d318a6b4fd8a73f9538c70">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5943b497db2e1dec04fae60584a294bb" class="memitem:ga5943b497db2e1dec04fae60584a294bb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_INT32   ((int) 'i')</td>
</tr>
<tr class="memdesc:ga5943b497db2e1dec04fae60584a294bb">
<td class="mdescLeft"> </td>
<td class="mdescRight">Type code marking a 32-bit signed integer.<br />
</td>
</tr>
<tr class="separator:ga5943b497db2e1dec04fae60584a294bb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5a7e049ba73ac54c2ffed02c28625b9e" class="memitem:ga5a7e049ba73ac54c2ffed02c28625b9e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_INT32_AS_STRING   "i"</td>
</tr>
<tr class="memdesc:ga5a7e049ba73ac54c2ffed02c28625b9e">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBUS_TYPE_INT32 as a string literal instead of a int literal<br />
</td>
</tr>
<tr class="separator:ga5a7e049ba73ac54c2ffed02c28625b9e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaedb1740bd8a9174b98ac593eded25d49" class="memitem:gaedb1740bd8a9174b98ac593eded25d49">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_UINT32   ((int) 'u')</td>
</tr>
<tr class="memdesc:gaedb1740bd8a9174b98ac593eded25d49">
<td class="mdescLeft"> </td>
<td class="mdescRight">Type code marking a 32-bit unsigned integer.<br />
</td>
</tr>
<tr class="separator:gaedb1740bd8a9174b98ac593eded25d49">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gadd89012acfc88aef2b084ed265242e5e" class="memitem:gadd89012acfc88aef2b084ed265242e5e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_UINT32_AS_STRING   "u"</td>
</tr>
<tr class="memdesc:gadd89012acfc88aef2b084ed265242e5e">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBUS_TYPE_UINT32 as a string literal instead of a int literal<br />
</td>
</tr>
<tr class="separator:gadd89012acfc88aef2b084ed265242e5e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabda4301c14b367f151f86769a1c27c5b" class="memitem:gabda4301c14b367f151f86769a1c27c5b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_INT64   ((int) 'x')</td>
</tr>
<tr class="memdesc:gabda4301c14b367f151f86769a1c27c5b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Type code marking a 64-bit signed integer.<br />
</td>
</tr>
<tr class="separator:gabda4301c14b367f151f86769a1c27c5b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4082f867803555e1278e7c4b6f5a2ab4" class="memitem:ga4082f867803555e1278e7c4b6f5a2ab4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_INT64_AS_STRING   "x"</td>
</tr>
<tr class="memdesc:ga4082f867803555e1278e7c4b6f5a2ab4">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBUS_TYPE_INT64 as a string literal instead of a int literal<br />
</td>
</tr>
<tr class="separator:ga4082f867803555e1278e7c4b6f5a2ab4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac59cc8f824813444cc9585effd4770d7" class="memitem:gac59cc8f824813444cc9585effd4770d7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_UINT64   ((int) 't')</td>
</tr>
<tr class="memdesc:gac59cc8f824813444cc9585effd4770d7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Type code marking a 64-bit unsigned integer.<br />
</td>
</tr>
<tr class="separator:gac59cc8f824813444cc9585effd4770d7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0321d37da6c2b15eac8d4b19da2014be" class="memitem:ga0321d37da6c2b15eac8d4b19da2014be">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_UINT64_AS_STRING   "t"</td>
</tr>
<tr class="memdesc:ga0321d37da6c2b15eac8d4b19da2014be">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBUS_TYPE_UINT64 as a string literal instead of a int literal<br />
</td>
</tr>
<tr class="separator:ga0321d37da6c2b15eac8d4b19da2014be">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac30c00bb6de04d0886cfbace276ec353" class="memitem:gac30c00bb6de04d0886cfbace276ec353">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_DOUBLE   ((int) 'd')</td>
</tr>
<tr class="memdesc:gac30c00bb6de04d0886cfbace276ec353">
<td class="mdescLeft"> </td>
<td class="mdescRight">Type code marking an 8-byte double in IEEE 754 format.<br />
</td>
</tr>
<tr class="separator:gac30c00bb6de04d0886cfbace276ec353">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga456972f2328504450ab5eec13730278c" class="memitem:ga456972f2328504450ab5eec13730278c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_DOUBLE_AS_STRING   "d"</td>
</tr>
<tr class="memdesc:ga456972f2328504450ab5eec13730278c">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBUS_TYPE_DOUBLE as a string literal instead of a int literal<br />
</td>
</tr>
<tr class="separator:ga456972f2328504450ab5eec13730278c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7eb77066dadf5415896b44c56d93acce" class="memitem:ga7eb77066dadf5415896b44c56d93acce">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_STRING   ((int) 's')</td>
</tr>
<tr class="memdesc:ga7eb77066dadf5415896b44c56d93acce">
<td class="mdescLeft"> </td>
<td class="mdescRight">Type code marking a UTF-8 encoded, nul-terminated Unicode string.<br />
</td>
</tr>
<tr class="separator:ga7eb77066dadf5415896b44c56d93acce">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabca06d9d52c249619f52c903c06800aa" class="memitem:gabca06d9d52c249619f52c903c06800aa">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_STRING_AS_STRING   "s"</td>
</tr>
<tr class="memdesc:gabca06d9d52c249619f52c903c06800aa">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBUS_TYPE_STRING as a string literal instead of a int literal<br />
</td>
</tr>
<tr class="separator:gabca06d9d52c249619f52c903c06800aa">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga31cc59c99a6cbbfcef71756e1390dc4c" class="memitem:ga31cc59c99a6cbbfcef71756e1390dc4c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_OBJECT_PATH   ((int) 'o')</td>
</tr>
<tr class="memdesc:ga31cc59c99a6cbbfcef71756e1390dc4c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Type code marking a D-Bus object path.<br />
</td>
</tr>
<tr class="separator:ga31cc59c99a6cbbfcef71756e1390dc4c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga82487e68b4a6a031405c70a20653b821" class="memitem:ga82487e68b4a6a031405c70a20653b821">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_OBJECT_PATH_AS_STRING   "o"</td>
</tr>
<tr class="memdesc:ga82487e68b4a6a031405c70a20653b821">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBUS_TYPE_OBJECT_PATH as a string literal instead of a int literal<br />
</td>
</tr>
<tr class="separator:ga82487e68b4a6a031405c70a20653b821">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga26ed6c20c3d9f0b50ea0a1cf80be3279" class="memitem:ga26ed6c20c3d9f0b50ea0a1cf80be3279">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_SIGNATURE   ((int) 'g')</td>
</tr>
<tr class="memdesc:ga26ed6c20c3d9f0b50ea0a1cf80be3279">
<td class="mdescLeft"> </td>
<td class="mdescRight">Type code marking a D-Bus type signature.<br />
</td>
</tr>
<tr class="separator:ga26ed6c20c3d9f0b50ea0a1cf80be3279">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga65f6317a9f41ca3854992a03058e7639" class="memitem:ga65f6317a9f41ca3854992a03058e7639">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_SIGNATURE_AS_STRING   "g"</td>
</tr>
<tr class="memdesc:ga65f6317a9f41ca3854992a03058e7639">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBUS_TYPE_SIGNATURE as a string literal instead of a int literal<br />
</td>
</tr>
<tr class="separator:ga65f6317a9f41ca3854992a03058e7639">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga59f8acaeb207b182982dfb97174b7f16" class="memitem:ga59f8acaeb207b182982dfb97174b7f16">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_UNIX_FD   ((int) 'h')</td>
</tr>
<tr class="memdesc:ga59f8acaeb207b182982dfb97174b7f16">
<td class="mdescLeft"> </td>
<td class="mdescRight">Type code marking a unix file descriptor.<br />
</td>
</tr>
<tr class="separator:ga59f8acaeb207b182982dfb97174b7f16">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga053d2d4cf3cd7a9eb45d709f774c2c57" class="memitem:ga053d2d4cf3cd7a9eb45d709f774c2c57">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_UNIX_FD_AS_STRING   "h"</td>
</tr>
<tr class="memdesc:ga053d2d4cf3cd7a9eb45d709f774c2c57">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBUS_TYPE_UNIX_FD as a string literal instead of a int literal<br />
</td>
</tr>
<tr class="separator:ga053d2d4cf3cd7a9eb45d709f774c2c57">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8912f600f81a773066ca03d9163613a9" class="memitem:ga8912f600f81a773066ca03d9163613a9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_ARRAY   ((int) 'a')</td>
</tr>
<tr class="memdesc:ga8912f600f81a773066ca03d9163613a9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Type code marking a D-Bus array type.<br />
</td>
</tr>
<tr class="separator:ga8912f600f81a773066ca03d9163613a9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga94236ec2eb0778dc636d061c48eeef23" class="memitem:ga94236ec2eb0778dc636d061c48eeef23">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_ARRAY_AS_STRING   "a"</td>
</tr>
<tr class="memdesc:ga94236ec2eb0778dc636d061c48eeef23">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBUS_TYPE_ARRAY as a string literal instead of a int literal<br />
</td>
</tr>
<tr class="separator:ga94236ec2eb0778dc636d061c48eeef23">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4aa7a463ad2bce4e9aa95e3e397ddcf1" class="memitem:ga4aa7a463ad2bce4e9aa95e3e397ddcf1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_VARIANT   ((int) 'v')</td>
</tr>
<tr class="memdesc:ga4aa7a463ad2bce4e9aa95e3e397ddcf1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Type code marking a D-Bus variant type.<br />
</td>
</tr>
<tr class="separator:ga4aa7a463ad2bce4e9aa95e3e397ddcf1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac5d9893972a0fdcd77eab6534cada8be" class="memitem:gac5d9893972a0fdcd77eab6534cada8be">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_VARIANT_AS_STRING   "v"</td>
</tr>
<tr class="memdesc:gac5d9893972a0fdcd77eab6534cada8be">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBUS_TYPE_VARIANT as a string literal instead of a int literal<br />
</td>
</tr>
<tr class="separator:gac5d9893972a0fdcd77eab6534cada8be">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae4b22a74b9edb0ec0ff6e0294794d3f9" class="memitem:gae4b22a74b9edb0ec0ff6e0294794d3f9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_STRUCT   ((int) 'r')</td>
</tr>
<tr class="memdesc:gae4b22a74b9edb0ec0ff6e0294794d3f9">
<td class="mdescLeft"> </td>
<td class="mdescRight">STRUCT and DICT_ENTRY are sort of special since their codes can't appear in a type string, instead DBUS_STRUCT_BEGIN_CHAR/DBUS_DICT_ENTRY_BEGIN_CHAR have to appear.<br />
</td>
</tr>
<tr class="separator:gae4b22a74b9edb0ec0ff6e0294794d3f9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga04d49c7b72b09b14f3815c6e39bf6d17" class="memitem:ga04d49c7b72b09b14f3815c6e39bf6d17">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_STRUCT_AS_STRING   "r"</td>
</tr>
<tr class="memdesc:ga04d49c7b72b09b14f3815c6e39bf6d17">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBUS_TYPE_STRUCT as a string literal instead of a int literal<br />
</td>
</tr>
<tr class="separator:ga04d49c7b72b09b14f3815c6e39bf6d17">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad2fc8e6c50e0ad927f4249fb9e53ca97" class="memitem:gad2fc8e6c50e0ad927f4249fb9e53ca97">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_DICT_ENTRY   ((int) 'e')</td>
</tr>
<tr class="memdesc:gad2fc8e6c50e0ad927f4249fb9e53ca97">
<td class="mdescLeft"> </td>
<td class="mdescRight">Type code used to represent a dict entry; however, this type code does not appear in type signatures, instead DBUS_DICT_ENTRY_BEGIN_CHAR and DBUS_DICT_ENTRY_END_CHAR will appear in a signature.<br />
</td>
</tr>
<tr class="separator:gad2fc8e6c50e0ad927f4249fb9e53ca97">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9a39a1547bc0325ec3287defc3ccb95d" class="memitem:ga9a39a1547bc0325ec3287defc3ccb95d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_TYPE_DICT_ENTRY_AS_STRING   "e"</td>
</tr>
<tr class="memdesc:ga9a39a1547bc0325ec3287defc3ccb95d">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBUS_TYPE_DICT_ENTRY as a string literal instead of a int literal<br />
</td>
</tr>
<tr class="separator:ga9a39a1547bc0325ec3287defc3ccb95d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga31efabc439ed5f2601b9686be4229cbe" class="memitem:ga31efabc439ed5f2601b9686be4229cbe">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_NUMBER_OF_TYPES   (16)</td>
</tr>
<tr class="memdesc:ga31efabc439ed5f2601b9686be4229cbe">
<td class="mdescLeft"> </td>
<td class="mdescRight">Does not include DBUS_TYPE_INVALID, DBUS_STRUCT_BEGIN_CHAR, DBUS_STRUCT_END_CHAR, DBUS_DICT_ENTRY_BEGIN_CHAR, or DBUS_DICT_ENTRY_END_CHAR - i.e.<br />
</td>
</tr>
<tr class="separator:ga31efabc439ed5f2601b9686be4229cbe">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga725657eca93175475e0694b858f51fd6" class="memitem:ga725657eca93175475e0694b858f51fd6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_STRUCT_BEGIN_CHAR   ((int) '(')</td>
</tr>
<tr class="memdesc:ga725657eca93175475e0694b858f51fd6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Code marking the start of a struct type in a type signature.<br />
</td>
</tr>
<tr class="separator:ga725657eca93175475e0694b858f51fd6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab6f2a0c823bd291bcb68948ce8181b8d" class="memitem:gab6f2a0c823bd291bcb68948ce8181b8d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_STRUCT_BEGIN_CHAR_AS_STRING   "("</td>
</tr>
<tr class="memdesc:gab6f2a0c823bd291bcb68948ce8181b8d">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBUS_STRUCT_BEGIN_CHAR as a string literal instead of a int literal<br />
</td>
</tr>
<tr class="separator:gab6f2a0c823bd291bcb68948ce8181b8d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaeab5ea0def3f587a0ed548b77d5c5cea" class="memitem:gaeab5ea0def3f587a0ed548b77d5c5cea">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_STRUCT_END_CHAR   ((int) ')')</td>
</tr>
<tr class="memdesc:gaeab5ea0def3f587a0ed548b77d5c5cea">
<td class="mdescLeft"> </td>
<td class="mdescRight">Code marking the end of a struct type in a type signature.<br />
</td>
</tr>
<tr class="separator:gaeab5ea0def3f587a0ed548b77d5c5cea">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga97075c0573afa424216716f86e3693ad" class="memitem:ga97075c0573afa424216716f86e3693ad">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_STRUCT_END_CHAR_AS_STRING   ")"</td>
</tr>
<tr class="memdesc:ga97075c0573afa424216716f86e3693ad">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBUS_STRUCT_END_CHAR a string literal instead of a int literal<br />
</td>
</tr>
<tr class="separator:ga97075c0573afa424216716f86e3693ad">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad51b5f7a2e6d927295479dd371f6b353" class="memitem:gad51b5f7a2e6d927295479dd371f6b353">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_DICT_ENTRY_BEGIN_CHAR   ((int) '{')</td>
</tr>
<tr class="memdesc:gad51b5f7a2e6d927295479dd371f6b353">
<td class="mdescLeft"> </td>
<td class="mdescRight">Code marking the start of a dict entry type in a type signature.<br />
</td>
</tr>
<tr class="separator:gad51b5f7a2e6d927295479dd371f6b353">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga590dc911798c8cdb47196871e12e68ec" class="memitem:ga590dc911798c8cdb47196871e12e68ec">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_DICT_ENTRY_BEGIN_CHAR_AS_STRING   "{"</td>
</tr>
<tr class="memdesc:ga590dc911798c8cdb47196871e12e68ec">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBUS_DICT_ENTRY_BEGIN_CHAR as a string literal instead of a int literal<br />
</td>
</tr>
<tr class="separator:ga590dc911798c8cdb47196871e12e68ec">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga29ad22c7342ead042ae9e55ae20b49f1" class="memitem:ga29ad22c7342ead042ae9e55ae20b49f1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_DICT_ENTRY_END_CHAR   ((int) '}')</td>
</tr>
<tr class="memdesc:ga29ad22c7342ead042ae9e55ae20b49f1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Code marking the end of a dict entry type in a type signature.<br />
</td>
</tr>
<tr class="separator:ga29ad22c7342ead042ae9e55ae20b49f1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae0db9510e56f2d33fd999ca67ebe964e" class="memitem:gae0db9510e56f2d33fd999ca67ebe964e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_DICT_ENTRY_END_CHAR_AS_STRING   "}"</td>
</tr>
<tr class="memdesc:gae0db9510e56f2d33fd999ca67ebe964e">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBUS_DICT_ENTRY_END_CHAR as a string literal instead of a int literal<br />
</td>
</tr>
<tr class="separator:gae0db9510e56f2d33fd999ca67ebe964e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga80186ac58d031d83127d1ad6644b0011" class="memitem:ga80186ac58d031d83127d1ad6644b0011">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_MAXIMUM_NAME_LENGTH   255</td>
</tr>
<tr class="memdesc:ga80186ac58d031d83127d1ad6644b0011">
<td class="mdescLeft"> </td>
<td class="mdescRight">Max length in bytes of a bus name, interface, or member (not object path, paths are unlimited).<br />
</td>
</tr>
<tr class="separator:ga80186ac58d031d83127d1ad6644b0011">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga28f099674760229e6de85a0e3c3e3e46" class="memitem:ga28f099674760229e6de85a0e3c3e3e46">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_MAXIMUM_SIGNATURE_LENGTH   255</td>
</tr>
<tr class="memdesc:ga28f099674760229e6de85a0e3c3e3e46">
<td class="mdescLeft"> </td>
<td class="mdescRight">This one is 255 so it fits in a byte.<br />
</td>
</tr>
<tr class="separator:ga28f099674760229e6de85a0e3c3e3e46">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaca161f9a67ce5adf617476c1956d4ee1" class="memitem:gaca161f9a67ce5adf617476c1956d4ee1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_MAXIMUM_MATCH_RULE_LENGTH   1024</td>
</tr>
<tr class="memdesc:gaca161f9a67ce5adf617476c1956d4ee1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Max length of a match rule string; to keep people from hosing the daemon with some huge rule.<br />
</td>
</tr>
<tr class="separator:gaca161f9a67ce5adf617476c1956d4ee1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaefeb44421a66e8184d70aae52918b101" class="memitem:gaefeb44421a66e8184d70aae52918b101">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_MAXIMUM_MATCH_RULE_ARG_NUMBER   63</td>
</tr>
<tr class="memdesc:gaefeb44421a66e8184d70aae52918b101">
<td class="mdescLeft"> </td>
<td class="mdescRight">Max arg number you can match on in a match rule, e.g.<br />
</td>
</tr>
<tr class="separator:gaefeb44421a66e8184d70aae52918b101">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5265afa08a4c8d9f31b287a57e8cb217" class="memitem:ga5265afa08a4c8d9f31b287a57e8cb217">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_MAXIMUM_ARRAY_LENGTH   (67108864)</td>
</tr>
<tr class="memdesc:ga5265afa08a4c8d9f31b287a57e8cb217">
<td class="mdescLeft"> </td>
<td class="mdescRight">Max length of a marshaled array in bytes (64M, 2^26) We use signed int for lengths so must be INT_MAX or less.<br />
</td>
</tr>
<tr class="separator:ga5265afa08a4c8d9f31b287a57e8cb217">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae1432f932131f0dcec0ac95f0fa1cb26" class="memitem:gae1432f932131f0dcec0ac95f0fa1cb26">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_MAXIMUM_ARRAY_LENGTH_BITS   26</td>
</tr>
<tr class="memdesc:gae1432f932131f0dcec0ac95f0fa1cb26">
<td class="mdescLeft"> </td>
<td class="mdescRight">Number of bits you need in an unsigned to store the max array size.<br />
</td>
</tr>
<tr class="separator:gae1432f932131f0dcec0ac95f0fa1cb26">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2874c299e1c87fe745ef09bf231264e9" class="memitem:ga2874c299e1c87fe745ef09bf231264e9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_MAXIMUM_MESSAGE_LENGTH   (DBUS_MAXIMUM_ARRAY_LENGTH * 2)</td>
</tr>
<tr class="memdesc:ga2874c299e1c87fe745ef09bf231264e9">
<td class="mdescLeft"> </td>
<td class="mdescRight">The maximum total message size including header and body; similar rationale to max array size.<br />
</td>
</tr>
<tr class="separator:ga2874c299e1c87fe745ef09bf231264e9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga36124260a66ce87ce18468644387aa84" class="memitem:ga36124260a66ce87ce18468644387aa84">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_MAXIMUM_MESSAGE_LENGTH_BITS   27</td>
</tr>
<tr class="memdesc:ga36124260a66ce87ce18468644387aa84">
<td class="mdescLeft"> </td>
<td class="mdescRight">Number of bits you need in an unsigned to store the max message size.<br />
</td>
</tr>
<tr class="separator:ga36124260a66ce87ce18468644387aa84">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2735432928240c083c72a5f5d23ec6a1" class="memitem:ga2735432928240c083c72a5f5d23ec6a1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_MAXIMUM_MESSAGE_UNIX_FDS   (DBUS_MAXIMUM_MESSAGE_LENGTH/4)</td>
</tr>
<tr class="memdesc:ga2735432928240c083c72a5f5d23ec6a1">
<td class="mdescLeft"> </td>
<td class="mdescRight">The maximum total number of unix fds in a message.<br />
</td>
</tr>
<tr class="separator:ga2735432928240c083c72a5f5d23ec6a1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga11d6c64b30c18e631dcf5af640fe67a4" class="memitem:ga11d6c64b30c18e631dcf5af640fe67a4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_MAXIMUM_MESSAGE_UNIX_FDS_BITS   (DBUS_MAXIMUM_MESSAGE_LENGTH_BITS-2)</td>
</tr>
<tr class="memdesc:ga11d6c64b30c18e631dcf5af640fe67a4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Number of bits you need in an unsigned to store the max message unix fds.<br />
</td>
</tr>
<tr class="separator:ga11d6c64b30c18e631dcf5af640fe67a4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaab86b8c110c95911e1c83ae4422b4018" class="memitem:gaab86b8c110c95911e1c83ae4422b4018">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_MAXIMUM_TYPE_RECURSION_DEPTH   32</td>
</tr>
<tr class="memdesc:gaab86b8c110c95911e1c83ae4422b4018">
<td class="mdescLeft"> </td>
<td class="mdescRight">Depth of recursion in the type tree.<br />
</td>
</tr>
<tr class="separator:gaab86b8c110c95911e1c83ae4422b4018">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac975525a6ce258a7a70c583c9741b516" class="memitem:gac975525a6ce258a7a70c583c9741b516">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_MESSAGE_TYPE_INVALID   0</td>
</tr>
<tr class="memdesc:gac975525a6ce258a7a70c583c9741b516">
<td class="mdescLeft"> </td>
<td class="mdescRight">This value is never a valid message type, see dbus_message_get_type()<br />
</td>
</tr>
<tr class="separator:gac975525a6ce258a7a70c583c9741b516">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga09416afd76b65139eddd31e1085d9ebf" class="memitem:ga09416afd76b65139eddd31e1085d9ebf">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_MESSAGE_TYPE_METHOD_CALL   1</td>
</tr>
<tr class="memdesc:ga09416afd76b65139eddd31e1085d9ebf">
<td class="mdescLeft"> </td>
<td class="mdescRight">Message type of a method call message, see dbus_message_get_type()<br />
</td>
</tr>
<tr class="separator:ga09416afd76b65139eddd31e1085d9ebf">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4a9012edd7f22342f845e98150aeb858" class="memitem:ga4a9012edd7f22342f845e98150aeb858">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_MESSAGE_TYPE_METHOD_RETURN   2</td>
</tr>
<tr class="memdesc:ga4a9012edd7f22342f845e98150aeb858">
<td class="mdescLeft"> </td>
<td class="mdescRight">Message type of a method return message, see dbus_message_get_type()<br />
</td>
</tr>
<tr class="separator:ga4a9012edd7f22342f845e98150aeb858">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2b9423d95066313d73eeea8eeaf86812" class="memitem:ga2b9423d95066313d73eeea8eeaf86812">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_MESSAGE_TYPE_ERROR   3</td>
</tr>
<tr class="memdesc:ga2b9423d95066313d73eeea8eeaf86812">
<td class="mdescLeft"> </td>
<td class="mdescRight">Message type of an error reply message, see dbus_message_get_type()<br />
</td>
</tr>
<tr class="separator:ga2b9423d95066313d73eeea8eeaf86812">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga728d893ff0c00e126517ba39835220a5" class="memitem:ga728d893ff0c00e126517ba39835220a5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_MESSAGE_TYPE_SIGNAL   4</td>
</tr>
<tr class="memdesc:ga728d893ff0c00e126517ba39835220a5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Message type of a signal message, see dbus_message_get_type()<br />
</td>
</tr>
<tr class="separator:ga728d893ff0c00e126517ba39835220a5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga224e49e00ad532c7c8788f6141fad644" class="memitem:ga224e49e00ad532c7c8788f6141fad644">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_NUM_MESSAGE_TYPES   5</td>
</tr>
<tr class="separator:ga224e49e00ad532c7c8788f6141fad644">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0dcac038284250b3b0bff49cb4990626" class="memitem:ga0dcac038284250b3b0bff49cb4990626">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_HEADER_FLAG_NO_REPLY_EXPECTED   0x1</td>
</tr>
<tr class="memdesc:ga0dcac038284250b3b0bff49cb4990626">
<td class="mdescLeft"> </td>
<td class="mdescRight">If set, this flag means that the sender of a message does not care about getting a reply, so the recipient need not send one.<br />
</td>
</tr>
<tr class="separator:ga0dcac038284250b3b0bff49cb4990626">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8699fad5ce9ff93fe3f3471ba463dd40" class="memitem:ga8699fad5ce9ff93fe3f3471ba463dd40">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_HEADER_FLAG_NO_AUTO_START   0x2</td>
</tr>
<tr class="memdesc:ga8699fad5ce9ff93fe3f3471ba463dd40">
<td class="mdescLeft"> </td>
<td class="mdescRight">If set, this flag means that even if the message bus knows how to start an owner for the destination bus name (see dbus_message_set_destination()), it should not do so.<br />
</td>
</tr>
<tr class="separator:ga8699fad5ce9ff93fe3f3471ba463dd40">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9e3539506c57a085ce40ca4dc919015b" class="memitem:ga9e3539506c57a085ce40ca4dc919015b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_HEADER_FLAG_ALLOW_INTERACTIVE_AUTHORIZATION   0x4</td>
</tr>
<tr class="memdesc:ga9e3539506c57a085ce40ca4dc919015b">
<td class="mdescLeft"> </td>
<td class="mdescRight">If set on a method call, this flag means that the caller is prepared to wait for interactive authorization.<br />
</td>
</tr>
<tr class="separator:ga9e3539506c57a085ce40ca4dc919015b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga075b0efc570129393d3fb653ce4bbd76" class="memitem:ga075b0efc570129393d3fb653ce4bbd76">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_HEADER_FIELD_INVALID   0</td>
</tr>
<tr class="memdesc:ga075b0efc570129393d3fb653ce4bbd76">
<td class="mdescLeft"> </td>
<td class="mdescRight">Not equal to any valid header field code.<br />
</td>
</tr>
<tr class="separator:ga075b0efc570129393d3fb653ce4bbd76">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0cd885e6e808b28ff082a7f8a2c9f579" class="memitem:ga0cd885e6e808b28ff082a7f8a2c9f579">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_HEADER_FIELD_PATH   1</td>
</tr>
<tr class="memdesc:ga0cd885e6e808b28ff082a7f8a2c9f579">
<td class="mdescLeft"> </td>
<td class="mdescRight">Header field code for the path - the path is the object emitting a signal or the object receiving a method call.<br />
</td>
</tr>
<tr class="separator:ga0cd885e6e808b28ff082a7f8a2c9f579">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga296b5f099b6c347f65d53ef0a6fa2b0d" class="memitem:ga296b5f099b6c347f65d53ef0a6fa2b0d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_HEADER_FIELD_INTERFACE   2</td>
</tr>
<tr class="memdesc:ga296b5f099b6c347f65d53ef0a6fa2b0d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Header field code for the interface containing a member (method or signal).<br />
</td>
</tr>
<tr class="separator:ga296b5f099b6c347f65d53ef0a6fa2b0d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2aa9d65ef983ac9c08c1d4cb31366818" class="memitem:ga2aa9d65ef983ac9c08c1d4cb31366818">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_HEADER_FIELD_MEMBER   3</td>
</tr>
<tr class="memdesc:ga2aa9d65ef983ac9c08c1d4cb31366818">
<td class="mdescLeft"> </td>
<td class="mdescRight">Header field code for a member (method or signal).<br />
</td>
</tr>
<tr class="separator:ga2aa9d65ef983ac9c08c1d4cb31366818">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac551be0f921390d01104cce30a814a5e" class="memitem:gac551be0f921390d01104cce30a814a5e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_HEADER_FIELD_ERROR_NAME   4</td>
</tr>
<tr class="memdesc:gac551be0f921390d01104cce30a814a5e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Header field code for an error name (found in DBUS_MESSAGE_TYPE_ERROR messages).<br />
</td>
</tr>
<tr class="separator:gac551be0f921390d01104cce30a814a5e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1067e28a7151a161e5fd601a3b017584" class="memitem:ga1067e28a7151a161e5fd601a3b017584">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_HEADER_FIELD_REPLY_SERIAL   5</td>
</tr>
<tr class="memdesc:ga1067e28a7151a161e5fd601a3b017584">
<td class="mdescLeft"> </td>
<td class="mdescRight">Header field code for a reply serial, used to match a DBUS_MESSAGE_TYPE_METHOD_RETURN message with the message that it's a reply to.<br />
</td>
</tr>
<tr class="separator:ga1067e28a7151a161e5fd601a3b017584">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gade98f71a08a1e0198d095fdb6d46cab9" class="memitem:gade98f71a08a1e0198d095fdb6d46cab9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_HEADER_FIELD_DESTINATION   6</td>
</tr>
<tr class="memdesc:gade98f71a08a1e0198d095fdb6d46cab9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Header field code for the destination bus name of a message.<br />
</td>
</tr>
<tr class="separator:gade98f71a08a1e0198d095fdb6d46cab9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3ba84ae623951832bd73e2796bb13e71" class="memitem:ga3ba84ae623951832bd73e2796bb13e71">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_HEADER_FIELD_SENDER   7</td>
</tr>
<tr class="memdesc:ga3ba84ae623951832bd73e2796bb13e71">
<td class="mdescLeft"> </td>
<td class="mdescRight">Header field code for the sender of a message; usually initialized by the message bus.<br />
</td>
</tr>
<tr class="separator:ga3ba84ae623951832bd73e2796bb13e71">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga450d63fa110d3cb891082e23291580b4" class="memitem:ga450d63fa110d3cb891082e23291580b4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_HEADER_FIELD_SIGNATURE   8</td>
</tr>
<tr class="memdesc:ga450d63fa110d3cb891082e23291580b4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Header field code for the type signature of a message.<br />
</td>
</tr>
<tr class="separator:ga450d63fa110d3cb891082e23291580b4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga03b9c24acbfd1e3da19804c739612885" class="memitem:ga03b9c24acbfd1e3da19804c739612885">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_HEADER_FIELD_UNIX_FDS   9</td>
</tr>
<tr class="memdesc:ga03b9c24acbfd1e3da19804c739612885">
<td class="mdescLeft"> </td>
<td class="mdescRight">Header field code for the number of unix file descriptors associated with this message.<br />
</td>
</tr>
<tr class="separator:ga03b9c24acbfd1e3da19804c739612885">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1caf2b9169a8ef7163cb279667799b75" class="memitem:ga1caf2b9169a8ef7163cb279667799b75">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_HEADER_FIELD_CONTAINER_INSTANCE   10</td>
</tr>
<tr class="memdesc:ga1caf2b9169a8ef7163cb279667799b75">
<td class="mdescLeft"> </td>
<td class="mdescRight">Header field code for the container instance that sent this message.<br />
</td>
</tr>
<tr class="separator:ga1caf2b9169a8ef7163cb279667799b75">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga94f09d2b35473c8ffa6d3190b5f97c5c" class="memitem:ga94f09d2b35473c8ffa6d3190b5f97c5c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_HEADER_FIELD_LAST   DBUS_HEADER_FIELD_CONTAINER_INSTANCE</td>
</tr>
<tr class="memdesc:ga94f09d2b35473c8ffa6d3190b5f97c5c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Value of the highest-numbered header field code, can be used to determine the size of an array indexed by header field code.<br />
</td>
</tr>
<tr class="separator:ga94f09d2b35473c8ffa6d3190b5f97c5c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga82e39a6508e551fb14c7bdbb17590cc6" class="memitem:ga82e39a6508e551fb14c7bdbb17590cc6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_HEADER_SIGNATURE</td>
</tr>
<tr class="memdesc:ga82e39a6508e551fb14c7bdbb17590cc6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Header format is defined as a signature: byte byte order byte message type ID byte flags byte protocol version uint32 body length uint32 serial array of struct (byte,variant) (field name, value)<br />
</td>
</tr>
<tr class="separator:ga82e39a6508e551fb14c7bdbb17590cc6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf8c13dd883c21b5dea179d77d8ac12e3" class="memitem:gaf8c13dd883c21b5dea179d77d8ac12e3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_MINIMUM_HEADER_SIZE   16</td>
</tr>
<tr class="memdesc:gaf8c13dd883c21b5dea179d77d8ac12e3">
<td class="mdescLeft"> </td>
<td class="mdescRight">The smallest header size that can occur.<br />
</td>
</tr>
<tr class="separator:gaf8c13dd883c21b5dea179d77d8ac12e3">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabb62fd6340d0787fbd56ff8dd2f326c7" class="memitem:gabb62fd6340d0787fbd56ff8dd2f326c7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_FAILED   "org.freedesktop.DBus.Error.Failed"</td>
</tr>
<tr class="memdesc:gabb62fd6340d0787fbd56ff8dd2f326c7">
<td class="mdescLeft"> </td>
<td class="mdescRight">A generic error; "something went wrong" - see the error message for more.<br />
</td>
</tr>
<tr class="separator:gabb62fd6340d0787fbd56ff8dd2f326c7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac32eaf0b92f798307853cd4fe0cf11c2" class="memitem:gac32eaf0b92f798307853cd4fe0cf11c2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_NO_MEMORY   "org.freedesktop.DBus.Error.NoMemory"</td>
</tr>
<tr class="memdesc:gac32eaf0b92f798307853cd4fe0cf11c2">
<td class="mdescLeft"> </td>
<td class="mdescRight">There was not enough memory to complete an operation.<br />
</td>
</tr>
<tr class="separator:gac32eaf0b92f798307853cd4fe0cf11c2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gacc32eb0c0d9a30f68d774601df01e1f5" class="memitem:gacc32eb0c0d9a30f68d774601df01e1f5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_SERVICE_UNKNOWN   "org.freedesktop.DBus.Error.ServiceUnknown"</td>
</tr>
<tr class="memdesc:gacc32eb0c0d9a30f68d774601df01e1f5">
<td class="mdescLeft"> </td>
<td class="mdescRight">The bus doesn't know how to launch a service to supply the bus name you wanted.<br />
</td>
</tr>
<tr class="separator:gacc32eb0c0d9a30f68d774601df01e1f5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7be7c443404400d5b3c3417138f27cb3" class="memitem:ga7be7c443404400d5b3c3417138f27cb3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_NAME_HAS_NO_OWNER   "org.freedesktop.DBus.Error.NameHasNoOwner"</td>
</tr>
<tr class="memdesc:ga7be7c443404400d5b3c3417138f27cb3">
<td class="mdescLeft"> </td>
<td class="mdescRight">The bus name you referenced doesn't exist (i.e.<br />
</td>
</tr>
<tr class="separator:ga7be7c443404400d5b3c3417138f27cb3">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gade2cb1c5a6adf47af18672865f233b6d" class="memitem:gade2cb1c5a6adf47af18672865f233b6d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_NO_REPLY   "org.freedesktop.DBus.Error.NoReply"</td>
</tr>
<tr class="memdesc:gade2cb1c5a6adf47af18672865f233b6d">
<td class="mdescLeft"> </td>
<td class="mdescRight">No reply to a message expecting one, usually means a timeout occurred.<br />
</td>
</tr>
<tr class="separator:gade2cb1c5a6adf47af18672865f233b6d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga445d7ad73da94c796ef441df2dcc3cc8" class="memitem:ga445d7ad73da94c796ef441df2dcc3cc8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_IO_ERROR   "org.freedesktop.DBus.Error.IOError"</td>
</tr>
<tr class="memdesc:ga445d7ad73da94c796ef441df2dcc3cc8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Something went wrong reading or writing to a socket, for example.<br />
</td>
</tr>
<tr class="separator:ga445d7ad73da94c796ef441df2dcc3cc8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3fa04eb600edda4afc2dd9fe2e0f8b02" class="memitem:ga3fa04eb600edda4afc2dd9fe2e0f8b02">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_BAD_ADDRESS   "org.freedesktop.DBus.Error.BadAddress"</td>
</tr>
<tr class="memdesc:ga3fa04eb600edda4afc2dd9fe2e0f8b02">
<td class="mdescLeft"> </td>
<td class="mdescRight">A D-Bus bus address was malformed.<br />
</td>
</tr>
<tr class="separator:ga3fa04eb600edda4afc2dd9fe2e0f8b02">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga33122bcaf8f5896ec222c755b6effb40" class="memitem:ga33122bcaf8f5896ec222c755b6effb40">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_NOT_SUPPORTED   "org.freedesktop.DBus.Error.NotSupported"</td>
</tr>
<tr class="memdesc:ga33122bcaf8f5896ec222c755b6effb40">
<td class="mdescLeft"> </td>
<td class="mdescRight">Requested operation isn't supported (like ENOSYS on UNIX).<br />
</td>
</tr>
<tr class="separator:ga33122bcaf8f5896ec222c755b6effb40">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7c96d165c4ebee51e939969934d18027" class="memitem:ga7c96d165c4ebee51e939969934d18027">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_LIMITS_EXCEEDED   "org.freedesktop.DBus.Error.LimitsExceeded"</td>
</tr>
<tr class="memdesc:ga7c96d165c4ebee51e939969934d18027">
<td class="mdescLeft"> </td>
<td class="mdescRight">Some limited resource is exhausted.<br />
</td>
</tr>
<tr class="separator:ga7c96d165c4ebee51e939969934d18027">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6d3940075c1fbd1bfe06626b59723a16" class="memitem:ga6d3940075c1fbd1bfe06626b59723a16">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_ACCESS_DENIED   "org.freedesktop.DBus.Error.AccessDenied"</td>
</tr>
<tr class="memdesc:ga6d3940075c1fbd1bfe06626b59723a16">
<td class="mdescLeft"> </td>
<td class="mdescRight">Security restrictions don't allow doing what you're trying to do.<br />
</td>
</tr>
<tr class="separator:ga6d3940075c1fbd1bfe06626b59723a16">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5a03c8e0e98131ee2a03d46d72c6ab49" class="memitem:ga5a03c8e0e98131ee2a03d46d72c6ab49">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_AUTH_FAILED   "org.freedesktop.DBus.Error.AuthFailed"</td>
</tr>
<tr class="memdesc:ga5a03c8e0e98131ee2a03d46d72c6ab49">
<td class="mdescLeft"> </td>
<td class="mdescRight">Authentication didn't work.<br />
</td>
</tr>
<tr class="separator:ga5a03c8e0e98131ee2a03d46d72c6ab49">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga72b375fab2486ee165e1cca2bd145695" class="memitem:ga72b375fab2486ee165e1cca2bd145695">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_NO_SERVER   "org.freedesktop.DBus.Error.NoServer"</td>
</tr>
<tr class="memdesc:ga72b375fab2486ee165e1cca2bd145695">
<td class="mdescLeft"> </td>
<td class="mdescRight">Unable to connect to server (probably caused by ECONNREFUSED on a socket).<br />
</td>
</tr>
<tr class="separator:ga72b375fab2486ee165e1cca2bd145695">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0e4674c42373ee449ddf08aab8bce9ce" class="memitem:ga0e4674c42373ee449ddf08aab8bce9ce">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_TIMEOUT   "org.freedesktop.DBus.Error.Timeout"</td>
</tr>
<tr class="memdesc:ga0e4674c42373ee449ddf08aab8bce9ce">
<td class="mdescLeft"> </td>
<td class="mdescRight">Certain timeout errors, possibly ETIMEDOUT on a socket.<br />
</td>
</tr>
<tr class="separator:ga0e4674c42373ee449ddf08aab8bce9ce">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab18c0e4eee0936dc042319803730b62e" class="memitem:gab18c0e4eee0936dc042319803730b62e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_NO_NETWORK   "org.freedesktop.DBus.Error.NoNetwork"</td>
</tr>
<tr class="memdesc:gab18c0e4eee0936dc042319803730b62e">
<td class="mdescLeft"> </td>
<td class="mdescRight">No network access (probably ENETUNREACH on a socket).<br />
</td>
</tr>
<tr class="separator:gab18c0e4eee0936dc042319803730b62e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3d13424a19bb774cf3481216bf4ba366" class="memitem:ga3d13424a19bb774cf3481216bf4ba366">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_ADDRESS_IN_USE   "org.freedesktop.DBus.Error.AddressInUse"</td>
</tr>
<tr class="memdesc:ga3d13424a19bb774cf3481216bf4ba366">
<td class="mdescLeft"> </td>
<td class="mdescRight">Can't bind a socket since its address is in use (i.e.<br />
</td>
</tr>
<tr class="separator:ga3d13424a19bb774cf3481216bf4ba366">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaef6443e0bd8cdcc1606d985a775d07a7" class="memitem:gaef6443e0bd8cdcc1606d985a775d07a7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_DISCONNECTED   "org.freedesktop.DBus.Error.Disconnected"</td>
</tr>
<tr class="memdesc:gaef6443e0bd8cdcc1606d985a775d07a7">
<td class="mdescLeft"> </td>
<td class="mdescRight">The connection is disconnected and you're trying to use it.<br />
</td>
</tr>
<tr class="separator:gaef6443e0bd8cdcc1606d985a775d07a7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gacf5321b161193ad66d5bdf5c910a9792" class="memitem:gacf5321b161193ad66d5bdf5c910a9792">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_INVALID_ARGS   "org.freedesktop.DBus.Error.InvalidArgs"</td>
</tr>
<tr class="memdesc:gacf5321b161193ad66d5bdf5c910a9792">
<td class="mdescLeft"> </td>
<td class="mdescRight">Invalid arguments passed to a method call.<br />
</td>
</tr>
<tr class="separator:gacf5321b161193ad66d5bdf5c910a9792">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf5ad9572cc5935d4655635003073c21a" class="memitem:gaf5ad9572cc5935d4655635003073c21a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_FILE_NOT_FOUND   "org.freedesktop.DBus.Error.FileNotFound"</td>
</tr>
<tr class="memdesc:gaf5ad9572cc5935d4655635003073c21a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Missing file.<br />
</td>
</tr>
<tr class="separator:gaf5ad9572cc5935d4655635003073c21a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7c65e9730331eb19b7d6b128a79361ef" class="memitem:ga7c65e9730331eb19b7d6b128a79361ef">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_FILE_EXISTS   "org.freedesktop.DBus.Error.FileExists"</td>
</tr>
<tr class="memdesc:ga7c65e9730331eb19b7d6b128a79361ef">
<td class="mdescLeft"> </td>
<td class="mdescRight">Existing file and the operation you're using does not silently overwrite.<br />
</td>
</tr>
<tr class="separator:ga7c65e9730331eb19b7d6b128a79361ef">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga46c7cbfa1806b0cccb56e9a7ca92f02b" class="memitem:ga46c7cbfa1806b0cccb56e9a7ca92f02b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_UNKNOWN_METHOD   "org.freedesktop.DBus.Error.UnknownMethod"</td>
</tr>
<tr class="memdesc:ga46c7cbfa1806b0cccb56e9a7ca92f02b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Method name you invoked isn't known by the object you invoked it on.<br />
</td>
</tr>
<tr class="separator:ga46c7cbfa1806b0cccb56e9a7ca92f02b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa31b8b1f9226530bb41ff1b01a836f6a" class="memitem:gaa31b8b1f9226530bb41ff1b01a836f6a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_UNKNOWN_OBJECT   "org.freedesktop.DBus.Error.UnknownObject"</td>
</tr>
<tr class="memdesc:gaa31b8b1f9226530bb41ff1b01a836f6a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Object you invoked a method on isn't known.<br />
</td>
</tr>
<tr class="separator:gaa31b8b1f9226530bb41ff1b01a836f6a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gafb812b2dbfbc04a8be56a516fb5070a5" class="memitem:gafb812b2dbfbc04a8be56a516fb5070a5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_UNKNOWN_INTERFACE   "org.freedesktop.DBus.Error.UnknownInterface"</td>
</tr>
<tr class="memdesc:gafb812b2dbfbc04a8be56a516fb5070a5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Interface you invoked a method on isn't known by the object.<br />
</td>
</tr>
<tr class="separator:gafb812b2dbfbc04a8be56a516fb5070a5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2a36fe0c35940b29f8ea9082f9e6e22a" class="memitem:ga2a36fe0c35940b29f8ea9082f9e6e22a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_UNKNOWN_PROPERTY   "org.freedesktop.DBus.Error.UnknownProperty"</td>
</tr>
<tr class="memdesc:ga2a36fe0c35940b29f8ea9082f9e6e22a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Property you tried to access isn't known by the object.<br />
</td>
</tr>
<tr class="separator:ga2a36fe0c35940b29f8ea9082f9e6e22a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabbcfbff98af28340921001dbf01fad52" class="memitem:gabbcfbff98af28340921001dbf01fad52">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_PROPERTY_READ_ONLY   "org.freedesktop.DBus.Error.PropertyReadOnly"</td>
</tr>
<tr class="memdesc:gabbcfbff98af28340921001dbf01fad52">
<td class="mdescLeft"> </td>
<td class="mdescRight">Property you tried to set is read-only.<br />
</td>
</tr>
<tr class="separator:gabbcfbff98af28340921001dbf01fad52">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga78ed308c8e1a52ef04da3ccc9ede37c8" class="memitem:ga78ed308c8e1a52ef04da3ccc9ede37c8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_TIMED_OUT   "org.freedesktop.DBus.Error.TimedOut"</td>
</tr>
<tr class="memdesc:ga78ed308c8e1a52ef04da3ccc9ede37c8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Certain timeout errors, e.g.<br />
</td>
</tr>
<tr class="separator:ga78ed308c8e1a52ef04da3ccc9ede37c8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gadbb070d61d10c2235eae26b065116eb9" class="memitem:gadbb070d61d10c2235eae26b065116eb9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_MATCH_RULE_NOT_FOUND   "org.freedesktop.DBus.Error.MatchRuleNotFound"</td>
</tr>
<tr class="memdesc:gadbb070d61d10c2235eae26b065116eb9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Tried to remove or modify a match rule that didn't exist.<br />
</td>
</tr>
<tr class="separator:gadbb070d61d10c2235eae26b065116eb9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga317e54b1dec8420dc22792be58138c77" class="memitem:ga317e54b1dec8420dc22792be58138c77">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_MATCH_RULE_INVALID   "org.freedesktop.DBus.Error.MatchRuleInvalid"</td>
</tr>
<tr class="memdesc:ga317e54b1dec8420dc22792be58138c77">
<td class="mdescLeft"> </td>
<td class="mdescRight">The match rule isn't syntactically valid.<br />
</td>
</tr>
<tr class="separator:ga317e54b1dec8420dc22792be58138c77">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac04bc3bebee1674e93ef96aaa2b34b40" class="memitem:gac04bc3bebee1674e93ef96aaa2b34b40">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_SPAWN_EXEC_FAILED   "org.freedesktop.DBus.Error.Spawn.ExecFailed"</td>
</tr>
<tr class="memdesc:gac04bc3bebee1674e93ef96aaa2b34b40">
<td class="mdescLeft"> </td>
<td class="mdescRight">While starting a new process, the exec() call failed.<br />
</td>
</tr>
<tr class="separator:gac04bc3bebee1674e93ef96aaa2b34b40">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gafe69e1ac207a66cc86d2880fd3ca62af" class="memitem:gafe69e1ac207a66cc86d2880fd3ca62af">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_SPAWN_FORK_FAILED   "org.freedesktop.DBus.Error.Spawn.ForkFailed"</td>
</tr>
<tr class="memdesc:gafe69e1ac207a66cc86d2880fd3ca62af">
<td class="mdescLeft"> </td>
<td class="mdescRight">While starting a new process, the fork() call failed.<br />
</td>
</tr>
<tr class="separator:gafe69e1ac207a66cc86d2880fd3ca62af">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6cd00ac22b189360a7f0ce2f2b97975b" class="memitem:ga6cd00ac22b189360a7f0ce2f2b97975b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_SPAWN_CHILD_EXITED   "org.freedesktop.DBus.Error.Spawn.ChildExited"</td>
</tr>
<tr class="memdesc:ga6cd00ac22b189360a7f0ce2f2b97975b">
<td class="mdescLeft"> </td>
<td class="mdescRight">While starting a new process, the child exited with a status code.<br />
</td>
</tr>
<tr class="separator:ga6cd00ac22b189360a7f0ce2f2b97975b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8404cd7fd5f0d62a63e26783bdf572ae" class="memitem:ga8404cd7fd5f0d62a63e26783bdf572ae">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_SPAWN_CHILD_SIGNALED   "org.freedesktop.DBus.Error.Spawn.ChildSignaled"</td>
</tr>
<tr class="memdesc:ga8404cd7fd5f0d62a63e26783bdf572ae">
<td class="mdescLeft"> </td>
<td class="mdescRight">While starting a new process, the child exited on a signal.<br />
</td>
</tr>
<tr class="separator:ga8404cd7fd5f0d62a63e26783bdf572ae">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac52e7ce94426443ff385994b539c6c38" class="memitem:gac52e7ce94426443ff385994b539c6c38">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_SPAWN_FAILED   "org.freedesktop.DBus.Error.Spawn.Failed"</td>
</tr>
<tr class="memdesc:gac52e7ce94426443ff385994b539c6c38">
<td class="mdescLeft"> </td>
<td class="mdescRight">While starting a new process, something went wrong.<br />
</td>
</tr>
<tr class="separator:gac52e7ce94426443ff385994b539c6c38">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa688518d769f96532c416cbb3641d70b" class="memitem:gaa688518d769f96532c416cbb3641d70b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_SPAWN_SETUP_FAILED   "org.freedesktop.DBus.Error.Spawn.FailedToSetup"</td>
</tr>
<tr class="memdesc:gaa688518d769f96532c416cbb3641d70b">
<td class="mdescLeft"> </td>
<td class="mdescRight">We failed to setup the environment correctly.<br />
</td>
</tr>
<tr class="separator:gaa688518d769f96532c416cbb3641d70b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1f3d7d0b407c89e8789f4831879fe070" class="memitem:ga1f3d7d0b407c89e8789f4831879fe070">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_SPAWN_CONFIG_INVALID   "org.freedesktop.DBus.Error.Spawn.ConfigInvalid"</td>
</tr>
<tr class="memdesc:ga1f3d7d0b407c89e8789f4831879fe070">
<td class="mdescLeft"> </td>
<td class="mdescRight">We failed to setup the config parser correctly.<br />
</td>
</tr>
<tr class="separator:ga1f3d7d0b407c89e8789f4831879fe070">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa6ff6e4ec30531fbdfe072713b12666c" class="memitem:gaa6ff6e4ec30531fbdfe072713b12666c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_SPAWN_SERVICE_INVALID   "org.freedesktop.DBus.Error.Spawn.ServiceNotValid"</td>
</tr>
<tr class="memdesc:gaa6ff6e4ec30531fbdfe072713b12666c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Bus name was not valid.<br />
</td>
</tr>
<tr class="separator:gaa6ff6e4ec30531fbdfe072713b12666c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac9ca901693db51c46be33705742f2f99" class="memitem:gac9ca901693db51c46be33705742f2f99">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_SPAWN_SERVICE_NOT_FOUND   "org.freedesktop.DBus.Error.Spawn.ServiceNotFound"</td>
</tr>
<tr class="memdesc:gac9ca901693db51c46be33705742f2f99">
<td class="mdescLeft"> </td>
<td class="mdescRight">Service file not found in system-services directory.<br />
</td>
</tr>
<tr class="separator:gac9ca901693db51c46be33705742f2f99">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga99a394feef7f3596fec477113d06f297" class="memitem:ga99a394feef7f3596fec477113d06f297">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_SPAWN_PERMISSIONS_INVALID   "org.freedesktop.DBus.Error.Spawn.PermissionsInvalid"</td>
</tr>
<tr class="memdesc:ga99a394feef7f3596fec477113d06f297">
<td class="mdescLeft"> </td>
<td class="mdescRight">Permissions are incorrect on the setuid helper.<br />
</td>
</tr>
<tr class="separator:ga99a394feef7f3596fec477113d06f297">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaca18a6762e361431066538588c827e05" class="memitem:gaca18a6762e361431066538588c827e05">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_SPAWN_FILE_INVALID   "org.freedesktop.DBus.Error.Spawn.FileInvalid"</td>
</tr>
<tr class="memdesc:gaca18a6762e361431066538588c827e05">
<td class="mdescLeft"> </td>
<td class="mdescRight">Service file invalid (Name, User or Exec missing).<br />
</td>
</tr>
<tr class="separator:gaca18a6762e361431066538588c827e05">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf20e1cdcb7e8a0445fba1aeb5e9618ce" class="memitem:gaf20e1cdcb7e8a0445fba1aeb5e9618ce">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_SPAWN_NO_MEMORY   "org.freedesktop.DBus.Error.Spawn.NoMemory"</td>
</tr>
<tr class="memdesc:gaf20e1cdcb7e8a0445fba1aeb5e9618ce">
<td class="mdescLeft"> </td>
<td class="mdescRight">There was not enough memory to complete the operation.<br />
</td>
</tr>
<tr class="separator:gaf20e1cdcb7e8a0445fba1aeb5e9618ce">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga79164703124135d658dc182dac53e6bb" class="memitem:ga79164703124135d658dc182dac53e6bb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_UNIX_PROCESS_ID_UNKNOWN   "org.freedesktop.DBus.Error.UnixProcessIdUnknown"</td>
</tr>
<tr class="memdesc:ga79164703124135d658dc182dac53e6bb">
<td class="mdescLeft"> </td>
<td class="mdescRight">Tried to get a UNIX process ID and it wasn't available.<br />
</td>
</tr>
<tr class="separator:ga79164703124135d658dc182dac53e6bb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac4fd50196d0b801a2204ccad4465c74e" class="memitem:gac4fd50196d0b801a2204ccad4465c74e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_INVALID_SIGNATURE   "org.freedesktop.DBus.Error.InvalidSignature"</td>
</tr>
<tr class="memdesc:gac4fd50196d0b801a2204ccad4465c74e">
<td class="mdescLeft"> </td>
<td class="mdescRight">A type signature is not valid.<br />
</td>
</tr>
<tr class="separator:gac4fd50196d0b801a2204ccad4465c74e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6a4e92aa48ed4486eaf48c40c72490c4" class="memitem:ga6a4e92aa48ed4486eaf48c40c72490c4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_INVALID_FILE_CONTENT   "org.freedesktop.DBus.Error.InvalidFileContent"</td>
</tr>
<tr class="memdesc:ga6a4e92aa48ed4486eaf48c40c72490c4">
<td class="mdescLeft"> </td>
<td class="mdescRight">A file contains invalid syntax or is otherwise broken.<br />
</td>
</tr>
<tr class="separator:ga6a4e92aa48ed4486eaf48c40c72490c4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaac816ecfc2f982d3d70322ba38be04ea" class="memitem:gaac816ecfc2f982d3d70322ba38be04ea">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_SELINUX_SECURITY_CONTEXT_UNKNOWN   "org.freedesktop.DBus.Error.SELinuxSecurityContextUnknown"</td>
</tr>
<tr class="memdesc:gaac816ecfc2f982d3d70322ba38be04ea">
<td class="mdescLeft"> </td>
<td class="mdescRight">Asked for SELinux security context and it wasn't available.<br />
</td>
</tr>
<tr class="separator:gaac816ecfc2f982d3d70322ba38be04ea">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab2f5567bd869d3552addf23d25bb883b" class="memitem:gab2f5567bd869d3552addf23d25bb883b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_ADT_AUDIT_DATA_UNKNOWN   "org.freedesktop.DBus.Error.AdtAuditDataUnknown"</td>
</tr>
<tr class="memdesc:gab2f5567bd869d3552addf23d25bb883b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Asked for ADT audit data and it wasn't available.<br />
</td>
</tr>
<tr class="separator:gab2f5567bd869d3552addf23d25bb883b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6a4358a62f0cd68d637532772475e576" class="memitem:ga6a4358a62f0cd68d637532772475e576">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_OBJECT_PATH_IN_USE   "org.freedesktop.DBus.Error.ObjectPathInUse"</td>
</tr>
<tr class="memdesc:ga6a4358a62f0cd68d637532772475e576">
<td class="mdescLeft"> </td>
<td class="mdescRight">There's already an object with the requested object path.<br />
</td>
</tr>
<tr class="separator:ga6a4358a62f0cd68d637532772475e576">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2a23b986cd4cef832b8823b6b0d1bcb1" class="memitem:ga2a23b986cd4cef832b8823b6b0d1bcb1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_INCONSISTENT_MESSAGE   "org.freedesktop.DBus.Error.InconsistentMessage"</td>
</tr>
<tr class="memdesc:ga2a23b986cd4cef832b8823b6b0d1bcb1">
<td class="mdescLeft"> </td>
<td class="mdescRight">The message meta data does not match the payload.<br />
</td>
</tr>
<tr class="separator:ga2a23b986cd4cef832b8823b6b0d1bcb1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf5ed34ef6339d3903d0c30c4a8221877" class="memitem:gaf5ed34ef6339d3903d0c30c4a8221877">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_INTERACTIVE_AUTHORIZATION_REQUIRED   "org.freedesktop.DBus.Error.InteractiveAuthorizationRequired"</td>
</tr>
<tr class="memdesc:gaf5ed34ef6339d3903d0c30c4a8221877">
<td class="mdescLeft"> </td>
<td class="mdescRight">The message is not allowed without performing interactive authorization, but could have succeeded if an interactive authorization step was allowed.<br />
</td>
</tr>
<tr class="separator:gaf5ed34ef6339d3903d0c30c4a8221877">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2c4f622e4179ceb10b5653e20a4ad89f" class="memitem:ga2c4f622e4179ceb10b5653e20a4ad89f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_NOT_CONTAINER   "org.freedesktop.DBus.Error.NotContainer"</td>
</tr>
<tr class="memdesc:ga2c4f622e4179ceb10b5653e20a4ad89f">
<td class="mdescLeft"> </td>
<td class="mdescRight">The connection is not from a container, or the specified container instance does not exist.<br />
</td>
</tr>
<tr class="separator:ga2c4f622e4179ceb10b5653e20a4ad89f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad15af90a0f0a382ae02d44cba71f2fb7" class="memitem:gad15af90a0f0a382ae02d44cba71f2fb7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_INTROSPECT_1_0_XML_NAMESPACE   "http://www.freedesktop.org/standards/dbus"</td>
</tr>
<tr class="memdesc:gad15af90a0f0a382ae02d44cba71f2fb7">
<td class="mdescLeft"> </td>
<td class="mdescRight">XML namespace of the introspection format version 1.0.<br />
</td>
</tr>
<tr class="separator:gad15af90a0f0a382ae02d44cba71f2fb7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga057290c3dbed7754c1c96e5a45e76b78" class="memitem:ga057290c3dbed7754c1c96e5a45e76b78">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_INTROSPECT_1_0_XML_PUBLIC_IDENTIFIER   "-//freedesktop//DTD D-BUS Object Introspection 1.0//EN"</td>
</tr>
<tr class="memdesc:ga057290c3dbed7754c1c96e5a45e76b78">
<td class="mdescLeft"> </td>
<td class="mdescRight">XML public identifier of the introspection format version 1.0.<br />
</td>
</tr>
<tr class="separator:ga057290c3dbed7754c1c96e5a45e76b78">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga411e41609d73806e0b7c0ad215c22390" class="memitem:ga411e41609d73806e0b7c0ad215c22390">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_INTROSPECT_1_0_XML_SYSTEM_IDENTIFIER   "http://www.freedesktop.org/standards/dbus/1.0/introspect.dtd"</td>
</tr>
<tr class="memdesc:ga411e41609d73806e0b7c0ad215c22390">
<td class="mdescLeft"> </td>
<td class="mdescRight">XML system identifier of the introspection format version 1.0.<br />
</td>
</tr>
<tr class="separator:ga411e41609d73806e0b7c0ad215c22390">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5e7de0ccf222f5fa69241e517824b712" class="memitem:ga5e7de0ccf222f5fa69241e517824b712">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_INTROSPECT_1_0_XML_DOCTYPE_DECL_NODE   "&lt;!DOCTYPE node PUBLIC \"" DBUS_INTROSPECT_1_0_XML_PUBLIC_IDENTIFIER "\"\n\"" DBUS_INTROSPECT_1_0_XML_SYSTEM_IDENTIFIER "\"&gt;\n"</td>
</tr>
<tr class="memdesc:ga5e7de0ccf222f5fa69241e517824b712">
<td class="mdescLeft"> </td>
<td class="mdescRight">XML document type declaration of the introspection format version 1.0.<br />
</td>
</tr>
<tr class="separator:ga5e7de0ccf222f5fa69241e517824b712">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Defines constants which are part of the D-Bus protocol.

This header is intended for use by any library, not only libdbus.

## Macro Definition Documentation

## ◆ DBUS_BIG_ENDIAN

|                                  |
|----------------------------------|
| \#define DBUS_BIG_ENDIAN   ('B') |

Code marking MSB-first byte order in the wire protocol.

Definition at line 56 of file dbus-protocol.h.

## ◆ DBUS_DICT_ENTRY_BEGIN_CHAR

|                                                   |
|---------------------------------------------------|
| \#define DBUS_DICT_ENTRY_BEGIN_CHAR   ((int) '{') |

Code marking the start of a dict entry type in a type signature.

Definition at line 166 of file dbus-protocol.h.

## ◆ DBUS_DICT_ENTRY_BEGIN_CHAR_AS_STRING

|                                                     |
|-----------------------------------------------------|
| \#define DBUS_DICT_ENTRY_BEGIN_CHAR_AS_STRING   "{" |

DBUS_DICT_ENTRY_BEGIN_CHAR as a string literal instead of a int literal

Definition at line 168 of file dbus-protocol.h.

## ◆ DBUS_DICT_ENTRY_END_CHAR

|                                                 |
|-------------------------------------------------|
| \#define DBUS_DICT_ENTRY_END_CHAR   ((int) '}') |

Code marking the end of a dict entry type in a type signature.

Definition at line 170 of file dbus-protocol.h.

## ◆ DBUS_DICT_ENTRY_END_CHAR_AS_STRING

|                                                   |
|---------------------------------------------------|
| \#define DBUS_DICT_ENTRY_END_CHAR_AS_STRING   "}" |

DBUS_DICT_ENTRY_END_CHAR as a string literal instead of a int literal

Definition at line 172 of file dbus-protocol.h.

## ◆ DBUS_ERROR_ACCESS_DENIED

|  |
|----|
| \#define DBUS_ERROR_ACCESS_DENIED   "org.freedesktop.DBus.Error.AccessDenied" |

Security restrictions don't allow doing what you're trying to do.

Definition at line 379 of file dbus-protocol.h.

## ◆ DBUS_ERROR_ADDRESS_IN_USE

|  |
|----|
| \#define DBUS_ERROR_ADDRESS_IN_USE   "org.freedesktop.DBus.Error.AddressInUse" |

Can't bind a socket since its address is in use (i.e.

EADDRINUSE).

Definition at line 393 of file dbus-protocol.h.

## ◆ DBUS_ERROR_ADT_AUDIT_DATA_UNKNOWN

|  |
|----|
| \#define DBUS_ERROR_ADT_AUDIT_DATA_UNKNOWN   "org.freedesktop.DBus.Error.AdtAuditDataUnknown" |

Asked for ADT audit data and it wasn't available.

Definition at line 454 of file dbus-protocol.h.

## ◆ DBUS_ERROR_AUTH_FAILED

|  |
|----|
| \#define DBUS_ERROR_AUTH_FAILED   "org.freedesktop.DBus.Error.AuthFailed" |

Authentication didn't work.

Definition at line 381 of file dbus-protocol.h.

## ◆ DBUS_ERROR_BAD_ADDRESS

|  |
|----|
| \#define DBUS_ERROR_BAD_ADDRESS   "org.freedesktop.DBus.Error.BadAddress" |

A D-Bus bus address was malformed.

Definition at line 373 of file dbus-protocol.h.

## ◆ DBUS_ERROR_DISCONNECTED

|  |
|----|
| \#define DBUS_ERROR_DISCONNECTED   "org.freedesktop.DBus.Error.Disconnected" |

The connection is disconnected and you're trying to use it.

Definition at line 395 of file dbus-protocol.h.

## ◆ DBUS_ERROR_FAILED

|                                                                  |
|------------------------------------------------------------------|
| \#define DBUS_ERROR_FAILED   "org.freedesktop.DBus.Error.Failed" |

A generic error; "something went wrong" - see the error message for more.

Definition at line 361 of file dbus-protocol.h.

## ◆ DBUS_ERROR_FILE_EXISTS

|  |
|----|
| \#define DBUS_ERROR_FILE_EXISTS   "org.freedesktop.DBus.Error.FileExists" |

Existing file and the operation you're using does not silently overwrite.

Definition at line 401 of file dbus-protocol.h.

## ◆ DBUS_ERROR_FILE_NOT_FOUND

|  |
|----|
| \#define DBUS_ERROR_FILE_NOT_FOUND   "org.freedesktop.DBus.Error.FileNotFound" |

Missing file.

Definition at line 399 of file dbus-protocol.h.

## ◆ DBUS_ERROR_INCONSISTENT_MESSAGE

|  |
|----|
| \#define DBUS_ERROR_INCONSISTENT_MESSAGE   "org.freedesktop.DBus.Error.InconsistentMessage" |

The message meta data does not match the payload.

e.g. expected number of file descriptors were not sent over the socket this message was received on.

Definition at line 459 of file dbus-protocol.h.

## ◆ DBUS_ERROR_INTERACTIVE_AUTHORIZATION_REQUIRED

|  |
|----|
| \#define DBUS_ERROR_INTERACTIVE_AUTHORIZATION_REQUIRED   "org.freedesktop.DBus.Error.InteractiveAuthorizationRequired" |

The message is not allowed without performing interactive authorization, but could have succeeded if an interactive authorization step was allowed.

Definition at line 463 of file dbus-protocol.h.

## ◆ DBUS_ERROR_INVALID_ARGS

|  |
|----|
| \#define DBUS_ERROR_INVALID_ARGS   "org.freedesktop.DBus.Error.InvalidArgs" |

Invalid arguments passed to a method call.

Definition at line 397 of file dbus-protocol.h.

## ◆ DBUS_ERROR_INVALID_FILE_CONTENT

|  |
|----|
| \#define DBUS_ERROR_INVALID_FILE_CONTENT   "org.freedesktop.DBus.Error.InvalidFileContent" |

A file contains invalid syntax or is otherwise broken.

Definition at line 450 of file dbus-protocol.h.

## ◆ DBUS_ERROR_INVALID_SIGNATURE

|  |
|----|
| \#define DBUS_ERROR_INVALID_SIGNATURE   "org.freedesktop.DBus.Error.InvalidSignature" |

A type signature is not valid.

Definition at line 448 of file dbus-protocol.h.

## ◆ DBUS_ERROR_IO_ERROR

|                                                                     |
|---------------------------------------------------------------------|
| \#define DBUS_ERROR_IO_ERROR   "org.freedesktop.DBus.Error.IOError" |

Something went wrong reading or writing to a socket, for example.

Definition at line 371 of file dbus-protocol.h.

## ◆ DBUS_ERROR_LIMITS_EXCEEDED

|  |
|----|
| \#define DBUS_ERROR_LIMITS_EXCEEDED   "org.freedesktop.DBus.Error.LimitsExceeded" |

Some limited resource is exhausted.

Definition at line 377 of file dbus-protocol.h.

## ◆ DBUS_ERROR_MATCH_RULE_INVALID

|  |
|----|
| \#define DBUS_ERROR_MATCH_RULE_INVALID   "org.freedesktop.DBus.Error.MatchRuleInvalid" |

The match rule isn't syntactically valid.

Definition at line 420 of file dbus-protocol.h.

## ◆ DBUS_ERROR_MATCH_RULE_NOT_FOUND

|  |
|----|
| \#define DBUS_ERROR_MATCH_RULE_NOT_FOUND   "org.freedesktop.DBus.Error.MatchRuleNotFound" |

Tried to remove or modify a match rule that didn't exist.

Definition at line 418 of file dbus-protocol.h.

## ◆ DBUS_ERROR_NAME_HAS_NO_OWNER

|  |
|----|
| \#define DBUS_ERROR_NAME_HAS_NO_OWNER   "org.freedesktop.DBus.Error.NameHasNoOwner" |

The bus name you referenced doesn't exist (i.e.

no application owns it).

Definition at line 367 of file dbus-protocol.h.

## ◆ DBUS_ERROR_NO_MEMORY

|                                                                       |
|-----------------------------------------------------------------------|
| \#define DBUS_ERROR_NO_MEMORY   "org.freedesktop.DBus.Error.NoMemory" |

There was not enough memory to complete an operation.

Definition at line 363 of file dbus-protocol.h.

## ◆ DBUS_ERROR_NO_NETWORK

|                                                                         |
|-------------------------------------------------------------------------|
| \#define DBUS_ERROR_NO_NETWORK   "org.freedesktop.DBus.Error.NoNetwork" |

No network access (probably ENETUNREACH on a socket).

Definition at line 391 of file dbus-protocol.h.

## ◆ DBUS_ERROR_NO_REPLY

|                                                                     |
|---------------------------------------------------------------------|
| \#define DBUS_ERROR_NO_REPLY   "org.freedesktop.DBus.Error.NoReply" |

No reply to a message expecting one, usually means a timeout occurred.

Definition at line 369 of file dbus-protocol.h.

## ◆ DBUS_ERROR_NO_SERVER

|                                                                       |
|-----------------------------------------------------------------------|
| \#define DBUS_ERROR_NO_SERVER   "org.freedesktop.DBus.Error.NoServer" |

Unable to connect to server (probably caused by ECONNREFUSED on a socket).

Definition at line 383 of file dbus-protocol.h.

## ◆ DBUS_ERROR_NOT_CONTAINER

|  |
|----|
| \#define DBUS_ERROR_NOT_CONTAINER   "org.freedesktop.DBus.Error.NotContainer" |

The connection is not from a container, or the specified container instance does not exist.

Definition at line 466 of file dbus-protocol.h.

## ◆ DBUS_ERROR_NOT_SUPPORTED

|  |
|----|
| \#define DBUS_ERROR_NOT_SUPPORTED   "org.freedesktop.DBus.Error.NotSupported" |

Requested operation isn't supported (like ENOSYS on UNIX).

Definition at line 375 of file dbus-protocol.h.

## ◆ DBUS_ERROR_OBJECT_PATH_IN_USE

|  |
|----|
| \#define DBUS_ERROR_OBJECT_PATH_IN_USE   "org.freedesktop.DBus.Error.ObjectPathInUse" |

There's already an object with the requested object path.

Definition at line 456 of file dbus-protocol.h.

## ◆ DBUS_ERROR_PROPERTY_READ_ONLY

|  |
|----|
| \#define DBUS_ERROR_PROPERTY_READ_ONLY   "org.freedesktop.DBus.Error.PropertyReadOnly" |

Property you tried to set is read-only.

Definition at line 411 of file dbus-protocol.h.

## ◆ DBUS_ERROR_SELINUX_SECURITY_CONTEXT_UNKNOWN

|  |
|----|
| \#define DBUS_ERROR_SELINUX_SECURITY_CONTEXT_UNKNOWN   "org.freedesktop.DBus.Error.SELinuxSecurityContextUnknown" |

Asked for SELinux security context and it wasn't available.

Definition at line 452 of file dbus-protocol.h.

## ◆ DBUS_ERROR_SERVICE_UNKNOWN

|  |
|----|
| \#define DBUS_ERROR_SERVICE_UNKNOWN   "org.freedesktop.DBus.Error.ServiceUnknown" |

The bus doesn't know how to launch a service to supply the bus name you wanted.

Definition at line 365 of file dbus-protocol.h.

## ◆ DBUS_ERROR_SPAWN_CHILD_EXITED

|  |
|----|
| \#define DBUS_ERROR_SPAWN_CHILD_EXITED   "org.freedesktop.DBus.Error.Spawn.ChildExited" |

While starting a new process, the child exited with a status code.

Definition at line 426 of file dbus-protocol.h.

## ◆ DBUS_ERROR_SPAWN_CHILD_SIGNALED

|  |
|----|
| \#define DBUS_ERROR_SPAWN_CHILD_SIGNALED   "org.freedesktop.DBus.Error.Spawn.ChildSignaled" |

While starting a new process, the child exited on a signal.

Definition at line 428 of file dbus-protocol.h.

## ◆ DBUS_ERROR_SPAWN_CONFIG_INVALID

|  |
|----|
| \#define DBUS_ERROR_SPAWN_CONFIG_INVALID   "org.freedesktop.DBus.Error.Spawn.ConfigInvalid" |

We failed to setup the config parser correctly.

Definition at line 434 of file dbus-protocol.h.

## ◆ DBUS_ERROR_SPAWN_EXEC_FAILED

|  |
|----|
| \#define DBUS_ERROR_SPAWN_EXEC_FAILED   "org.freedesktop.DBus.Error.Spawn.ExecFailed" |

While starting a new process, the exec() call failed.

Definition at line 422 of file dbus-protocol.h.

## ◆ DBUS_ERROR_SPAWN_FAILED

|  |
|----|
| \#define DBUS_ERROR_SPAWN_FAILED   "org.freedesktop.DBus.Error.Spawn.Failed" |

While starting a new process, something went wrong.

Definition at line 430 of file dbus-protocol.h.

## ◆ DBUS_ERROR_SPAWN_FILE_INVALID

|  |
|----|
| \#define DBUS_ERROR_SPAWN_FILE_INVALID   "org.freedesktop.DBus.Error.Spawn.FileInvalid" |

Service file invalid (Name, User or Exec missing).

Definition at line 442 of file dbus-protocol.h.

## ◆ DBUS_ERROR_SPAWN_FORK_FAILED

|  |
|----|
| \#define DBUS_ERROR_SPAWN_FORK_FAILED   "org.freedesktop.DBus.Error.Spawn.ForkFailed" |

While starting a new process, the fork() call failed.

Definition at line 424 of file dbus-protocol.h.

## ◆ DBUS_ERROR_SPAWN_NO_MEMORY

|  |
|----|
| \#define DBUS_ERROR_SPAWN_NO_MEMORY   "org.freedesktop.DBus.Error.Spawn.NoMemory" |

There was not enough memory to complete the operation.

Definition at line 444 of file dbus-protocol.h.

## ◆ DBUS_ERROR_SPAWN_PERMISSIONS_INVALID

|  |
|----|
| \#define DBUS_ERROR_SPAWN_PERMISSIONS_INVALID   "org.freedesktop.DBus.Error.Spawn.PermissionsInvalid" |

Permissions are incorrect on the setuid helper.

Definition at line 440 of file dbus-protocol.h.

## ◆ DBUS_ERROR_SPAWN_SERVICE_INVALID

|  |
|----|
| \#define DBUS_ERROR_SPAWN_SERVICE_INVALID   "org.freedesktop.DBus.Error.Spawn.ServiceNotValid" |

Bus name was not valid.

Definition at line 436 of file dbus-protocol.h.

## ◆ DBUS_ERROR_SPAWN_SERVICE_NOT_FOUND

|  |
|----|
| \#define DBUS_ERROR_SPAWN_SERVICE_NOT_FOUND   "org.freedesktop.DBus.Error.Spawn.ServiceNotFound" |

Service file not found in system-services directory.

Definition at line 438 of file dbus-protocol.h.

## ◆ DBUS_ERROR_SPAWN_SETUP_FAILED

|  |
|----|
| \#define DBUS_ERROR_SPAWN_SETUP_FAILED   "org.freedesktop.DBus.Error.Spawn.FailedToSetup" |

We failed to setup the environment correctly.

Definition at line 432 of file dbus-protocol.h.

## ◆ DBUS_ERROR_TIMED_OUT

|                                                                       |
|-----------------------------------------------------------------------|
| \#define DBUS_ERROR_TIMED_OUT   "org.freedesktop.DBus.Error.TimedOut" |

Certain timeout errors, e.g.

while starting a service.

Warning  
this is confusingly-named given that DBUS_ERROR_TIMEOUT also exists. We can't fix it for compatibility reasons so just be careful.

Definition at line 416 of file dbus-protocol.h.

## ◆ DBUS_ERROR_TIMEOUT

|                                                                    |
|--------------------------------------------------------------------|
| \#define DBUS_ERROR_TIMEOUT   "org.freedesktop.DBus.Error.Timeout" |

Certain timeout errors, possibly ETIMEDOUT on a socket.

Note that DBUS_ERROR_NO_REPLY is used for message reply timeouts.

Warning  
this is confusingly-named given that DBUS_ERROR_TIMED_OUT also exists. We can't fix it for compatibility reasons so just be careful.

Definition at line 389 of file dbus-protocol.h.

## ◆ DBUS_ERROR_UNIX_PROCESS_ID_UNKNOWN

|  |
|----|
| \#define DBUS_ERROR_UNIX_PROCESS_ID_UNKNOWN   "org.freedesktop.DBus.Error.UnixProcessIdUnknown" |

Tried to get a UNIX process ID and it wasn't available.

Definition at line 446 of file dbus-protocol.h.

## ◆ DBUS_ERROR_UNKNOWN_INTERFACE

|  |
|----|
| \#define DBUS_ERROR_UNKNOWN_INTERFACE   "org.freedesktop.DBus.Error.UnknownInterface" |

Interface you invoked a method on isn't known by the object.

Definition at line 407 of file dbus-protocol.h.

## ◆ DBUS_ERROR_UNKNOWN_METHOD

|  |
|----|
| \#define DBUS_ERROR_UNKNOWN_METHOD   "org.freedesktop.DBus.Error.UnknownMethod" |

Method name you invoked isn't known by the object you invoked it on.

Definition at line 403 of file dbus-protocol.h.

## ◆ DBUS_ERROR_UNKNOWN_OBJECT

|  |
|----|
| \#define DBUS_ERROR_UNKNOWN_OBJECT   "org.freedesktop.DBus.Error.UnknownObject" |

Object you invoked a method on isn't known.

Definition at line 405 of file dbus-protocol.h.

## ◆ DBUS_ERROR_UNKNOWN_PROPERTY

|  |
|----|
| \#define DBUS_ERROR_UNKNOWN_PROPERTY   "org.freedesktop.DBus.Error.UnknownProperty" |

Property you tried to access isn't known by the object.

Definition at line 409 of file dbus-protocol.h.

## ◆ DBUS_HEADER_FIELD_CONTAINER_INSTANCE

|                                                    |
|----------------------------------------------------|
| \#define DBUS_HEADER_FIELD_CONTAINER_INSTANCE   10 |

Header field code for the container instance that sent this message.

Definition at line 308 of file dbus-protocol.h.

## ◆ DBUS_HEADER_FIELD_DESTINATION

|                                            |
|--------------------------------------------|
| \#define DBUS_HEADER_FIELD_DESTINATION   6 |

Header field code for the destination bus name of a message.

See dbus_message_set_destination().

Definition at line 290 of file dbus-protocol.h.

## ◆ DBUS_HEADER_FIELD_ERROR_NAME

|                                           |
|-------------------------------------------|
| \#define DBUS_HEADER_FIELD_ERROR_NAME   4 |

Header field code for an error name (found in DBUS_MESSAGE_TYPE_ERROR messages).

See dbus_message_set_error_name().

Definition at line 282 of file dbus-protocol.h.

## ◆ DBUS_HEADER_FIELD_INTERFACE

|                                          |
|------------------------------------------|
| \#define DBUS_HEADER_FIELD_INTERFACE   2 |

Header field code for the interface containing a member (method or signal).

See dbus_message_set_interface().

Definition at line 276 of file dbus-protocol.h.

## ◆ DBUS_HEADER_FIELD_INVALID

|                                        |
|----------------------------------------|
| \#define DBUS_HEADER_FIELD_INVALID   0 |

Not equal to any valid header field code.

Definition at line 268 of file dbus-protocol.h.

## ◆ DBUS_HEADER_FIELD_LAST

|                                                                        |
|------------------------------------------------------------------------|
| \#define DBUS_HEADER_FIELD_LAST   DBUS_HEADER_FIELD_CONTAINER_INSTANCE |

Value of the highest-numbered header field code, can be used to determine the size of an array indexed by header field code.

Remember though that unknown codes must be ignored, so check for that before indexing the array.

Definition at line 317 of file dbus-protocol.h.

## ◆ DBUS_HEADER_FIELD_MEMBER

|                                       |
|---------------------------------------|
| \#define DBUS_HEADER_FIELD_MEMBER   3 |

Header field code for a member (method or signal).

See dbus_message_set_member().

Definition at line 278 of file dbus-protocol.h.

## ◆ DBUS_HEADER_FIELD_PATH

|                                     |
|-------------------------------------|
| \#define DBUS_HEADER_FIELD_PATH   1 |

Header field code for the path - the path is the object emitting a signal or the object receiving a method call.

See dbus_message_set_path().

Definition at line 272 of file dbus-protocol.h.

## ◆ DBUS_HEADER_FIELD_REPLY_SERIAL

|                                             |
|---------------------------------------------|
| \#define DBUS_HEADER_FIELD_REPLY_SERIAL   5 |

Header field code for a reply serial, used to match a DBUS_MESSAGE_TYPE_METHOD_RETURN message with the message that it's a reply to.

See dbus_message_set_reply_serial().

Definition at line 286 of file dbus-protocol.h.

## ◆ DBUS_HEADER_FIELD_SENDER

|                                       |
|---------------------------------------|
| \#define DBUS_HEADER_FIELD_SENDER   7 |

Header field code for the sender of a message; usually initialized by the message bus.

See dbus_message_set_sender().

Definition at line 295 of file dbus-protocol.h.

## ◆ DBUS_HEADER_FIELD_SIGNATURE

|                                          |
|------------------------------------------|
| \#define DBUS_HEADER_FIELD_SIGNATURE   8 |

Header field code for the type signature of a message.

Definition at line 299 of file dbus-protocol.h.

## ◆ DBUS_HEADER_FIELD_UNIX_FDS

|                                         |
|-----------------------------------------|
| \#define DBUS_HEADER_FIELD_UNIX_FDS   9 |

Header field code for the number of unix file descriptors associated with this message.

Definition at line 304 of file dbus-protocol.h.

## ◆ DBUS_HEADER_FLAG_ALLOW_INTERACTIVE_AUTHORIZATION

|                                                                 |
|-----------------------------------------------------------------|
| \#define DBUS_HEADER_FLAG_ALLOW_INTERACTIVE_AUTHORIZATION   0x4 |

If set on a method call, this flag means that the caller is prepared to wait for interactive authorization.

Definition at line 263 of file dbus-protocol.h.

## ◆ DBUS_HEADER_FLAG_NO_AUTO_START

|                                               |
|-----------------------------------------------|
| \#define DBUS_HEADER_FLAG_NO_AUTO_START   0x2 |

If set, this flag means that even if the message bus knows how to start an owner for the destination bus name (see dbus_message_set_destination()), it should not do so.

If this flag is not set, the bus may launch a program to process the message.

Definition at line 258 of file dbus-protocol.h.

## ◆ DBUS_HEADER_FLAG_NO_REPLY_EXPECTED

|                                                   |
|---------------------------------------------------|
| \#define DBUS_HEADER_FLAG_NO_REPLY_EXPECTED   0x1 |

If set, this flag means that the sender of a message does not care about getting a reply, so the recipient need not send one.

See dbus_message_set_no_reply().

Definition at line 251 of file dbus-protocol.h.

## ◆ DBUS_HEADER_SIGNATURE

|                                |
|--------------------------------|
| \#define DBUS_HEADER_SIGNATURE |

**Value:**

DBUS_TYPE_BYTE_AS_STRING \\

DBUS_TYPE_BYTE_AS_STRING \\

DBUS_TYPE_BYTE_AS_STRING \\

DBUS_TYPE_BYTE_AS_STRING \\

DBUS_TYPE_UINT32_AS_STRING \\

DBUS_TYPE_UINT32_AS_STRING \\

DBUS_TYPE_ARRAY_AS_STRING \\

DBUS_STRUCT_BEGIN_CHAR_AS_STRING \\

DBUS_TYPE_BYTE_AS_STRING \\

DBUS_TYPE_VARIANT_AS_STRING \\

DBUS_STRUCT_END_CHAR_AS_STRING

Header format is defined as a signature: byte byte order byte message type ID byte flags byte protocol version uint32 body length uint32 serial array of struct (byte,variant) (field name, value)

The length of the header can be computed as the fixed size of the initial data, plus the length of the array at the end, plus padding to an 8-boundary.

Definition at line 332 of file dbus-protocol.h.

## ◆ DBUS_INTROSPECT_1_0_XML_DOCTYPE_DECL_NODE

|  |
|----|
| \#define DBUS_INTROSPECT_1_0_XML_DOCTYPE_DECL_NODE   "\<!DOCTYPE node PUBLIC \\" DBUS_INTROSPECT_1_0_XML_PUBLIC_IDENTIFIER "\\\n\\" DBUS_INTROSPECT_1_0_XML_SYSTEM_IDENTIFIER "\\\>\n" |

XML document type declaration of the introspection format version 1.0.

Definition at line 477 of file dbus-protocol.h.

## ◆ DBUS_INTROSPECT_1_0_XML_NAMESPACE

|  |
|----|
| \#define DBUS_INTROSPECT_1_0_XML_NAMESPACE   "http://www.freedesktop.org/standards/dbus" |

XML namespace of the introspection format version 1.0.

Definition at line 471 of file dbus-protocol.h.

## ◆ DBUS_INTROSPECT_1_0_XML_PUBLIC_IDENTIFIER

|  |
|----|
| \#define DBUS_INTROSPECT_1_0_XML_PUBLIC_IDENTIFIER   "-//freedesktop//DTD D-BUS Object Introspection 1.0//EN" |

XML public identifier of the introspection format version 1.0.

Definition at line 473 of file dbus-protocol.h.

## ◆ DBUS_INTROSPECT_1_0_XML_SYSTEM_IDENTIFIER

|  |
|----|
| \#define DBUS_INTROSPECT_1_0_XML_SYSTEM_IDENTIFIER   "http://www.freedesktop.org/standards/dbus/1.0/introspect.dtd" |

XML system identifier of the introspection format version 1.0.

Definition at line 475 of file dbus-protocol.h.

## ◆ DBUS_LITTLE_ENDIAN

|                                     |
|-------------------------------------|
| \#define DBUS_LITTLE_ENDIAN   ('l') |

Code marking LSB-first byte order in the wire protocol.

Definition at line 55 of file dbus-protocol.h.

## ◆ DBUS_MAJOR_PROTOCOL_VERSION

|                                          |
|------------------------------------------|
| \#define DBUS_MAJOR_PROTOCOL_VERSION   1 |

Protocol version.

Definition at line 59 of file dbus-protocol.h.

## ◆ DBUS_MAXIMUM_ARRAY_LENGTH

|                                                 |
|-------------------------------------------------|
| \#define DBUS_MAXIMUM_ARRAY_LENGTH   (67108864) |

Max length of a marshaled array in bytes (64M, 2^26) We use signed int for lengths so must be INT_MAX or less.

We need something a bit smaller than INT_MAX because the array is inside a message with header info, etc. so an INT_MAX array wouldn't allow the message overhead. The 64M number is an attempt at a larger number than we'd reasonably ever use, but small enough that your bus would chew through it fairly quickly without locking up forever. If you have data that's likely to be larger than this, you should probably be sending it in multiple incremental messages anyhow.

Definition at line 205 of file dbus-protocol.h.

## ◆ DBUS_MAXIMUM_ARRAY_LENGTH_BITS

|                                              |
|----------------------------------------------|
| \#define DBUS_MAXIMUM_ARRAY_LENGTH_BITS   26 |

Number of bits you need in an unsigned to store the max array size.

Definition at line 207 of file dbus-protocol.h.

## ◆ DBUS_MAXIMUM_MATCH_RULE_ARG_NUMBER

|                                                  |
|--------------------------------------------------|
| \#define DBUS_MAXIMUM_MATCH_RULE_ARG_NUMBER   63 |

Max arg number you can match on in a match rule, e.g.

arg0='hello' is OK, arg3489720987='hello' is not

Definition at line 193 of file dbus-protocol.h.

## ◆ DBUS_MAXIMUM_MATCH_RULE_LENGTH

|                                                |
|------------------------------------------------|
| \#define DBUS_MAXIMUM_MATCH_RULE_LENGTH   1024 |

Max length of a match rule string; to keep people from hosing the daemon with some huge rule.

Definition at line 188 of file dbus-protocol.h.

## ◆ DBUS_MAXIMUM_MESSAGE_LENGTH

|                                                                         |
|-------------------------------------------------------------------------|
| \#define DBUS_MAXIMUM_MESSAGE_LENGTH   (DBUS_MAXIMUM_ARRAY_LENGTH \* 2) |

The maximum total message size including header and body; similar rationale to max array size.

Definition at line 212 of file dbus-protocol.h.

## ◆ DBUS_MAXIMUM_MESSAGE_LENGTH_BITS

|                                                |
|------------------------------------------------|
| \#define DBUS_MAXIMUM_MESSAGE_LENGTH_BITS   27 |

Number of bits you need in an unsigned to store the max message size.

Definition at line 214 of file dbus-protocol.h.

## ◆ DBUS_MAXIMUM_MESSAGE_UNIX_FDS

|                                                                          |
|--------------------------------------------------------------------------|
| \#define DBUS_MAXIMUM_MESSAGE_UNIX_FDS   (DBUS_MAXIMUM_MESSAGE_LENGTH/4) |

The maximum total number of unix fds in a message.

Similar rationale as DBUS_MAXIMUM_MESSAGE_LENGTH. However we divide by four given that one fd is an int and hence at least 32 bits.

Definition at line 220 of file dbus-protocol.h.

## ◆ DBUS_MAXIMUM_MESSAGE_UNIX_FDS_BITS

|  |
|----|
| \#define DBUS_MAXIMUM_MESSAGE_UNIX_FDS_BITS   (DBUS_MAXIMUM_MESSAGE_LENGTH_BITS-2) |

Number of bits you need in an unsigned to store the max message unix fds.

Definition at line 222 of file dbus-protocol.h.

## ◆ DBUS_MAXIMUM_NAME_LENGTH

|                                         |
|-----------------------------------------|
| \#define DBUS_MAXIMUM_NAME_LENGTH   255 |

Max length in bytes of a bus name, interface, or member (not object path, paths are unlimited).

This is limited because lots of stuff is O(n) in this number, plus it would be obnoxious to type in a paragraph-long method name so most likely something like that would be an exploit.

Definition at line 180 of file dbus-protocol.h.

## ◆ DBUS_MAXIMUM_SIGNATURE_LENGTH

|                                              |
|----------------------------------------------|
| \#define DBUS_MAXIMUM_SIGNATURE_LENGTH   255 |

This one is 255 so it fits in a byte.

Definition at line 183 of file dbus-protocol.h.

## ◆ DBUS_MAXIMUM_TYPE_RECURSION_DEPTH

|                                                 |
|-------------------------------------------------|
| \#define DBUS_MAXIMUM_TYPE_RECURSION_DEPTH   32 |

Depth of recursion in the type tree.

This is automatically limited to DBUS_MAXIMUM_SIGNATURE_LENGTH since you could only have an array of array of array of ... that fit in the max signature. But that's probably a bit too large.

Definition at line 229 of file dbus-protocol.h.

## ◆ DBUS_MESSAGE_TYPE_ERROR

|                                      |
|--------------------------------------|
| \#define DBUS_MESSAGE_TYPE_ERROR   3 |

Message type of an error reply message, see dbus_message_get_type()

Definition at line 240 of file dbus-protocol.h.

## ◆ DBUS_MESSAGE_TYPE_INVALID

|                                        |
|----------------------------------------|
| \#define DBUS_MESSAGE_TYPE_INVALID   0 |

This value is never a valid message type, see dbus_message_get_type()

Definition at line 234 of file dbus-protocol.h.

## ◆ DBUS_MESSAGE_TYPE_METHOD_CALL

|                                            |
|--------------------------------------------|
| \#define DBUS_MESSAGE_TYPE_METHOD_CALL   1 |

Message type of a method call message, see dbus_message_get_type()

Definition at line 236 of file dbus-protocol.h.

## ◆ DBUS_MESSAGE_TYPE_METHOD_RETURN

|                                              |
|----------------------------------------------|
| \#define DBUS_MESSAGE_TYPE_METHOD_RETURN   2 |

Message type of a method return message, see dbus_message_get_type()

Definition at line 238 of file dbus-protocol.h.

## ◆ DBUS_MESSAGE_TYPE_SIGNAL

|                                       |
|---------------------------------------|
| \#define DBUS_MESSAGE_TYPE_SIGNAL   4 |

Message type of a signal message, see dbus_message_get_type()

Definition at line 242 of file dbus-protocol.h.

## ◆ DBUS_MINIMUM_HEADER_SIZE

|                                        |
|----------------------------------------|
| \#define DBUS_MINIMUM_HEADER_SIZE   16 |

The smallest header size that can occur.

(It won't be valid due to missing required header fields.) This is 4 bytes, two uint32, an array length. This isn't any kind of resource limit, just the necessary/logical outcome of the header signature.

Definition at line 352 of file dbus-protocol.h.

## ◆ DBUS_NUM_MESSAGE_TYPES

|                                     |
|-------------------------------------|
| \#define DBUS_NUM_MESSAGE_TYPES   5 |

Definition at line 244 of file dbus-protocol.h.

## ◆ DBUS_NUMBER_OF_TYPES

|                                      |
|--------------------------------------|
| \#define DBUS_NUMBER_OF_TYPES   (16) |

Does not include DBUS_TYPE_INVALID, DBUS_STRUCT_BEGIN_CHAR, DBUS_STRUCT_END_CHAR, DBUS_DICT_ENTRY_BEGIN_CHAR, or DBUS_DICT_ENTRY_END_CHAR - i.e.

it is the number of valid types, not the number of distinct characters that may appear in a type signature.

Definition at line 153 of file dbus-protocol.h.

## ◆ DBUS_STRUCT_BEGIN_CHAR

|                                               |
|-----------------------------------------------|
| \#define DBUS_STRUCT_BEGIN_CHAR   ((int) '(') |

Code marking the start of a struct type in a type signature.

Definition at line 158 of file dbus-protocol.h.

## ◆ DBUS_STRUCT_BEGIN_CHAR_AS_STRING

|                                                 |
|-------------------------------------------------|
| \#define DBUS_STRUCT_BEGIN_CHAR_AS_STRING   "(" |

DBUS_STRUCT_BEGIN_CHAR as a string literal instead of a int literal

Definition at line 160 of file dbus-protocol.h.

## ◆ DBUS_STRUCT_END_CHAR

|                                             |
|---------------------------------------------|
| \#define DBUS_STRUCT_END_CHAR   ((int) ')') |

Code marking the end of a struct type in a type signature.

Definition at line 162 of file dbus-protocol.h.

## ◆ DBUS_STRUCT_END_CHAR_AS_STRING

|                                               |
|-----------------------------------------------|
| \#define DBUS_STRUCT_END_CHAR_AS_STRING   ")" |

DBUS_STRUCT_END_CHAR a string literal instead of a int literal

Definition at line 164 of file dbus-protocol.h.

## ◆ DBUS_TYPE_ARRAY

|                                        |
|----------------------------------------|
| \#define DBUS_TYPE_ARRAY   ((int) 'a') |

Type code marking a D-Bus array type.

Definition at line 122 of file dbus-protocol.h.

## ◆ DBUS_TYPE_ARRAY_AS_STRING

|                                          |
|------------------------------------------|
| \#define DBUS_TYPE_ARRAY_AS_STRING   "a" |

DBUS_TYPE_ARRAY as a string literal instead of a int literal

Definition at line 124 of file dbus-protocol.h.

## ◆ DBUS_TYPE_BOOLEAN

|                                          |
|------------------------------------------|
| \#define DBUS_TYPE_BOOLEAN   ((int) 'b') |

Type code marking a boolean.

Definition at line 72 of file dbus-protocol.h.

## ◆ DBUS_TYPE_BOOLEAN_AS_STRING

|                                            |
|--------------------------------------------|
| \#define DBUS_TYPE_BOOLEAN_AS_STRING   "b" |

DBUS_TYPE_BOOLEAN as a string literal instead of a int literal

Definition at line 74 of file dbus-protocol.h.

## ◆ DBUS_TYPE_BYTE

|                                       |
|---------------------------------------|
| \#define DBUS_TYPE_BYTE   ((int) 'y') |

Type code marking an 8-bit unsigned integer.

Definition at line 68 of file dbus-protocol.h.

## ◆ DBUS_TYPE_BYTE_AS_STRING

|                                         |
|-----------------------------------------|
| \#define DBUS_TYPE_BYTE_AS_STRING   "y" |

DBUS_TYPE_BYTE as a string literal instead of a int literal

Definition at line 70 of file dbus-protocol.h.

## ◆ DBUS_TYPE_DICT_ENTRY

|                                             |
|---------------------------------------------|
| \#define DBUS_TYPE_DICT_ENTRY   ((int) 'e') |

Type code used to represent a dict entry; however, this type code does not appear in type signatures, instead DBUS_DICT_ENTRY_BEGIN_CHAR and DBUS_DICT_ENTRY_END_CHAR will appear in a signature.

Definition at line 145 of file dbus-protocol.h.

## ◆ DBUS_TYPE_DICT_ENTRY_AS_STRING

|                                               |
|-----------------------------------------------|
| \#define DBUS_TYPE_DICT_ENTRY_AS_STRING   "e" |

DBUS_TYPE_DICT_ENTRY as a string literal instead of a int literal

Definition at line 147 of file dbus-protocol.h.

## ◆ DBUS_TYPE_DOUBLE

|                                         |
|-----------------------------------------|
| \#define DBUS_TYPE_DOUBLE   ((int) 'd') |

Type code marking an 8-byte double in IEEE 754 format.

Definition at line 100 of file dbus-protocol.h.

## ◆ DBUS_TYPE_DOUBLE_AS_STRING

|                                           |
|-------------------------------------------|
| \#define DBUS_TYPE_DOUBLE_AS_STRING   "d" |

DBUS_TYPE_DOUBLE as a string literal instead of a int literal

Definition at line 102 of file dbus-protocol.h.

## ◆ DBUS_TYPE_INT16

|                                        |
|----------------------------------------|
| \#define DBUS_TYPE_INT16   ((int) 'n') |

Type code marking a 16-bit signed integer.

Definition at line 76 of file dbus-protocol.h.

## ◆ DBUS_TYPE_INT16_AS_STRING

|                                          |
|------------------------------------------|
| \#define DBUS_TYPE_INT16_AS_STRING   "n" |

DBUS_TYPE_INT16 as a string literal instead of a int literal

Definition at line 78 of file dbus-protocol.h.

## ◆ DBUS_TYPE_INT32

|                                        |
|----------------------------------------|
| \#define DBUS_TYPE_INT32   ((int) 'i') |

Type code marking a 32-bit signed integer.

Definition at line 84 of file dbus-protocol.h.

## ◆ DBUS_TYPE_INT32_AS_STRING

|                                          |
|------------------------------------------|
| \#define DBUS_TYPE_INT32_AS_STRING   "i" |

DBUS_TYPE_INT32 as a string literal instead of a int literal

Definition at line 86 of file dbus-protocol.h.

## ◆ DBUS_TYPE_INT64

|                                        |
|----------------------------------------|
| \#define DBUS_TYPE_INT64   ((int) 'x') |

Type code marking a 64-bit signed integer.

Definition at line 92 of file dbus-protocol.h.

## ◆ DBUS_TYPE_INT64_AS_STRING

|                                          |
|------------------------------------------|
| \#define DBUS_TYPE_INT64_AS_STRING   "x" |

DBUS_TYPE_INT64 as a string literal instead of a int literal

Definition at line 94 of file dbus-protocol.h.

## ◆ DBUS_TYPE_INVALID

|                                           |
|-------------------------------------------|
| \#define DBUS_TYPE_INVALID   ((int) '\0') |

Type code that is never equal to a legitimate type code.

Definition at line 62 of file dbus-protocol.h.

## ◆ DBUS_TYPE_INVALID_AS_STRING

|                                             |
|---------------------------------------------|
| \#define DBUS_TYPE_INVALID_AS_STRING   "\0" |

DBUS_TYPE_INVALID as a string literal instead of a int literal

Definition at line 64 of file dbus-protocol.h.

## ◆ DBUS_TYPE_OBJECT_PATH

|                                              |
|----------------------------------------------|
| \#define DBUS_TYPE_OBJECT_PATH   ((int) 'o') |

Type code marking a D-Bus object path.

Definition at line 108 of file dbus-protocol.h.

## ◆ DBUS_TYPE_OBJECT_PATH_AS_STRING

|                                                |
|------------------------------------------------|
| \#define DBUS_TYPE_OBJECT_PATH_AS_STRING   "o" |

DBUS_TYPE_OBJECT_PATH as a string literal instead of a int literal

Definition at line 110 of file dbus-protocol.h.

## ◆ DBUS_TYPE_SIGNATURE

|                                            |
|--------------------------------------------|
| \#define DBUS_TYPE_SIGNATURE   ((int) 'g') |

Type code marking a D-Bus type signature.

Definition at line 112 of file dbus-protocol.h.

## ◆ DBUS_TYPE_SIGNATURE_AS_STRING

|                                              |
|----------------------------------------------|
| \#define DBUS_TYPE_SIGNATURE_AS_STRING   "g" |

DBUS_TYPE_SIGNATURE as a string literal instead of a int literal

Definition at line 114 of file dbus-protocol.h.

## ◆ DBUS_TYPE_STRING

|                                         |
|-----------------------------------------|
| \#define DBUS_TYPE_STRING   ((int) 's') |

Type code marking a UTF-8 encoded, nul-terminated Unicode string.

Definition at line 104 of file dbus-protocol.h.

## ◆ DBUS_TYPE_STRING_AS_STRING

|                                           |
|-------------------------------------------|
| \#define DBUS_TYPE_STRING_AS_STRING   "s" |

DBUS_TYPE_STRING as a string literal instead of a int literal

Definition at line 106 of file dbus-protocol.h.

## ◆ DBUS_TYPE_STRUCT

|                                         |
|-----------------------------------------|
| \#define DBUS_TYPE_STRUCT   ((int) 'r') |

STRUCT and DICT_ENTRY are sort of special since their codes can't appear in a type string, instead DBUS_STRUCT_BEGIN_CHAR/DBUS_DICT_ENTRY_BEGIN_CHAR have to appear.

Type code used to represent a struct; however, this type code does not appear in type signatures, instead DBUS_STRUCT_BEGIN_CHAR and DBUS_STRUCT_END_CHAR will appear in a signature.

Definition at line 138 of file dbus-protocol.h.

## ◆ DBUS_TYPE_STRUCT_AS_STRING

|                                           |
|-------------------------------------------|
| \#define DBUS_TYPE_STRUCT_AS_STRING   "r" |

DBUS_TYPE_STRUCT as a string literal instead of a int literal

Definition at line 140 of file dbus-protocol.h.

## ◆ DBUS_TYPE_UINT16

|                                         |
|-----------------------------------------|
| \#define DBUS_TYPE_UINT16   ((int) 'q') |

Type code marking a 16-bit unsigned integer.

Definition at line 80 of file dbus-protocol.h.

## ◆ DBUS_TYPE_UINT16_AS_STRING

|                                           |
|-------------------------------------------|
| \#define DBUS_TYPE_UINT16_AS_STRING   "q" |

DBUS_TYPE_UINT16 as a string literal instead of a int literal

Definition at line 82 of file dbus-protocol.h.

## ◆ DBUS_TYPE_UINT32

|                                         |
|-----------------------------------------|
| \#define DBUS_TYPE_UINT32   ((int) 'u') |

Type code marking a 32-bit unsigned integer.

Definition at line 88 of file dbus-protocol.h.

## ◆ DBUS_TYPE_UINT32_AS_STRING

|                                           |
|-------------------------------------------|
| \#define DBUS_TYPE_UINT32_AS_STRING   "u" |

DBUS_TYPE_UINT32 as a string literal instead of a int literal

Definition at line 90 of file dbus-protocol.h.

## ◆ DBUS_TYPE_UINT64

|                                         |
|-----------------------------------------|
| \#define DBUS_TYPE_UINT64   ((int) 't') |

Type code marking a 64-bit unsigned integer.

Definition at line 96 of file dbus-protocol.h.

## ◆ DBUS_TYPE_UINT64_AS_STRING

|                                           |
|-------------------------------------------|
| \#define DBUS_TYPE_UINT64_AS_STRING   "t" |

DBUS_TYPE_UINT64 as a string literal instead of a int literal

Definition at line 98 of file dbus-protocol.h.

## ◆ DBUS_TYPE_UNIX_FD

|                                          |
|------------------------------------------|
| \#define DBUS_TYPE_UNIX_FD   ((int) 'h') |

Type code marking a unix file descriptor.

Definition at line 116 of file dbus-protocol.h.

## ◆ DBUS_TYPE_UNIX_FD_AS_STRING

|                                            |
|--------------------------------------------|
| \#define DBUS_TYPE_UNIX_FD_AS_STRING   "h" |

DBUS_TYPE_UNIX_FD as a string literal instead of a int literal

Definition at line 118 of file dbus-protocol.h.

## ◆ DBUS_TYPE_VARIANT

|                                          |
|------------------------------------------|
| \#define DBUS_TYPE_VARIANT   ((int) 'v') |

Type code marking a D-Bus variant type.

Definition at line 126 of file dbus-protocol.h.

## ◆ DBUS_TYPE_VARIANT_AS_STRING

|                                            |
|--------------------------------------------|
| \#define DBUS_TYPE_VARIANT_AS_STRING   "v" |

DBUS_TYPE_VARIANT as a string literal instead of a int literal

Definition at line 128 of file dbus-protocol.h.
