marshaling and unmarshaling

D-Bus secret internal implementation details

functions to marshal/unmarshal data from the wire More...

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
<td class="memItemRight" data-valign="bottom">HeaderFieldType</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusTypeReaderClass</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Virtual table for a type reader. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">ReplacementBlock</td>
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
<tr id="r_ga935ea6d7c6bb72a10c670f5ef3e34d49" class="memitem:ga935ea6d7c6bb72a10c670f5ef3e34d49">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">FIELDS_ARRAY_SIGNATURE_OFFSET   6</td>
</tr>
<tr class="memdesc:ga935ea6d7c6bb72a10c670f5ef3e34d49">
<td class="mdescLeft"> </td>
<td class="mdescRight">Offset from start of _dbus_header_signature_str to the signature of the fields array.<br />
</td>
</tr>
<tr class="separator:ga935ea6d7c6bb72a10c670f5ef3e34d49">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaca36ac2e9b37067279d1bc967793e071" class="memitem:gaca36ac2e9b37067279d1bc967793e071">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">FIELDS_ARRAY_ELEMENT_SIGNATURE_OFFSET   7</td>
</tr>
<tr class="memdesc:gaca36ac2e9b37067279d1bc967793e071">
<td class="mdescLeft"> </td>
<td class="mdescRight">Offset from start of _dbus_header_signature_str to the signature of an element of the fields array.<br />
</td>
</tr>
<tr class="separator:gaca36ac2e9b37067279d1bc967793e071">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa5b7e77f37761139698892e4b8aad029" class="memitem:gaa5b7e77f37761139698892e4b8aad029">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">BYTE_ORDER_OFFSET   0</td>
</tr>
<tr class="memdesc:gaa5b7e77f37761139698892e4b8aad029">
<td class="mdescLeft"> </td>
<td class="mdescRight">Offset to byte order from start of header.<br />
</td>
</tr>
<tr class="separator:gaa5b7e77f37761139698892e4b8aad029">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf4fe78df75f4afa2ec63304462614b03" class="memitem:gaf4fe78df75f4afa2ec63304462614b03">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">TYPE_OFFSET   1</td>
</tr>
<tr class="memdesc:gaf4fe78df75f4afa2ec63304462614b03">
<td class="mdescLeft"> </td>
<td class="mdescRight">Offset to type from start of header.<br />
</td>
</tr>
<tr class="separator:gaf4fe78df75f4afa2ec63304462614b03">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7fe1bac4010cdc7e27de1e19702c071e" class="memitem:ga7fe1bac4010cdc7e27de1e19702c071e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">FLAGS_OFFSET   2</td>
</tr>
<tr class="memdesc:ga7fe1bac4010cdc7e27de1e19702c071e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Offset to flags from start of header.<br />
</td>
</tr>
<tr class="separator:ga7fe1bac4010cdc7e27de1e19702c071e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4f04ecce1223b00d263c0accdea144ad" class="memitem:ga4f04ecce1223b00d263c0accdea144ad">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">VERSION_OFFSET   3</td>
</tr>
<tr class="memdesc:ga4f04ecce1223b00d263c0accdea144ad">
<td class="mdescLeft"> </td>
<td class="mdescRight">Offset to version from start of header.<br />
</td>
</tr>
<tr class="separator:ga4f04ecce1223b00d263c0accdea144ad">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga190a2d89e79c9d76fcba4f06ec8b5b5c" class="memitem:ga190a2d89e79c9d76fcba4f06ec8b5b5c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">BODY_LENGTH_OFFSET   4</td>
</tr>
<tr class="memdesc:ga190a2d89e79c9d76fcba4f06ec8b5b5c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Offset to body length from start of header.<br />
</td>
</tr>
<tr class="separator:ga190a2d89e79c9d76fcba4f06ec8b5b5c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4a9c0639714b478a4905cdd6e999b6b3" class="memitem:ga4a9c0639714b478a4905cdd6e999b6b3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">SERIAL_OFFSET   8</td>
</tr>
<tr class="memdesc:ga4a9c0639714b478a4905cdd6e999b6b3">
<td class="mdescLeft"> </td>
<td class="mdescRight">Offset to client serial from start of header.<br />
</td>
</tr>
<tr class="separator:ga4a9c0639714b478a4905cdd6e999b6b3">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae9759e0de1d8a650f37632c3dc22427e" class="memitem:gae9759e0de1d8a650f37632c3dc22427e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">FIELDS_ARRAY_LENGTH_OFFSET   12</td>
</tr>
<tr class="memdesc:gae9759e0de1d8a650f37632c3dc22427e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Offset to fields array length from start of header.<br />
</td>
</tr>
<tr class="separator:gae9759e0de1d8a650f37632c3dc22427e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaaa085e57f49f527ef210e842be999929" class="memitem:gaaa085e57f49f527ef210e842be999929">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">FIRST_FIELD_OFFSET   16</td>
</tr>
<tr class="memdesc:gaaa085e57f49f527ef210e842be999929">
<td class="mdescLeft"> </td>
<td class="mdescRight">Offset to first field in header.<br />
</td>
</tr>
<tr class="separator:gaaa085e57f49f527ef210e842be999929">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga37be3d294f5be31c95bc7620e451b0b2" class="memitem:ga37be3d294f5be31c95bc7620e451b0b2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">EXPECTED_TYPE_OF_FIELD(field)   (_dbus_header_field_types[field].type)</td>
</tr>
<tr class="memdesc:ga37be3d294f5be31c95bc7620e451b0b2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Macro to look up the correct type for a field.<br />
</td>
</tr>
<tr class="separator:ga37be3d294f5be31c95bc7620e451b0b2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa10402f90ea6e004e3b9f04eea34f73c" class="memitem:gaa10402f90ea6e004e3b9f04eea34f73c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">MAX_POSSIBLE_HEADER_PADDING   7</td>
</tr>
<tr class="memdesc:gaa10402f90ea6e004e3b9f04eea34f73c">
<td class="mdescLeft"> </td>
<td class="mdescRight">The most padding we could ever need for a header.<br />
</td>
</tr>
<tr class="separator:gaa10402f90ea6e004e3b9f04eea34f73c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaef7e86e442aeb887c8bfe5559cd4eabb" class="memitem:gaef7e86e442aeb887c8bfe5559cd4eabb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">HEADER_END_BEFORE_PADDING(header)    (_dbus_string_get_length (&amp;(header)-&gt;data) - (header)-&gt;padding)</td>
</tr>
<tr class="memdesc:gaef7e86e442aeb887c8bfe5559cd4eabb">
<td class="mdescLeft"> </td>
<td class="mdescRight">Compute the end of the header, ignoring padding.<br />
</td>
</tr>
<tr class="separator:gaef7e86e442aeb887c8bfe5559cd4eabb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2055dc20f1e0c13064cebf1fb65b8ce8" class="memitem:ga2055dc20f1e0c13064cebf1fb65b8ce8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">RECURSIVE_MARSHAL_READ_TRACE   0</td>
</tr>
<tr class="memdesc:ga2055dc20f1e0c13064cebf1fb65b8ce8">
<td class="mdescLeft"> </td>
<td class="mdescRight">turn this on to get deluged in TypeReader verbose spam<br />
</td>
</tr>
<tr class="separator:ga2055dc20f1e0c13064cebf1fb65b8ce8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga428a18f23d9a4c59560f03fd2088fe7f" class="memitem:ga428a18f23d9a4c59560f03fd2088fe7f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">RECURSIVE_MARSHAL_WRITE_TRACE   0</td>
</tr>
<tr class="memdesc:ga428a18f23d9a4c59560f03fd2088fe7f">
<td class="mdescLeft"> </td>
<td class="mdescRight">turn this on to get deluged in TypeWriter verbose spam<br />
</td>
</tr>
<tr class="separator:ga428a18f23d9a4c59560f03fd2088fe7f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gacca774d24b7d7e790b169f23d3362497" class="memitem:gacca774d24b7d7e790b169f23d3362497">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">ARRAY_READER_LEN_POS(reader)    ((reader)-&gt;u.array.start_pos - ((int)(reader)-&gt;array_len_offset) - 4)</td>
</tr>
<tr class="memdesc:gacca774d24b7d7e790b169f23d3362497">
<td class="mdescLeft"> </td>
<td class="mdescRight">compute position of array length given array_len_offset, which is the offset back from start_pos to end of the len<br />
</td>
</tr>
<tr class="separator:gacca774d24b7d7e790b169f23d3362497">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8eb3b26eec8ebfeef410caa4acc9570d" class="memitem:ga8eb3b26eec8ebfeef410caa4acc9570d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">VALID_INITIAL_NAME_CHARACTER(c)</td>
</tr>
<tr class="memdesc:ga8eb3b26eec8ebfeef410caa4acc9570d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Determine wether the given character is valid as the first character in a name.<br />
</td>
</tr>
<tr class="separator:ga8eb3b26eec8ebfeef410caa4acc9570d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga11d63128bf5c1b7e0164be7072c6c6c7" class="memitem:ga11d63128bf5c1b7e0164be7072c6c6c7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">VALID_NAME_CHARACTER(c)</td>
</tr>
<tr class="memdesc:ga11d63128bf5c1b7e0164be7072c6c6c7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Determine wether the given character is valid as a second or later character in a name.<br />
</td>
</tr>
<tr class="separator:ga11d63128bf5c1b7e0164be7072c6c6c7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1ec58a1d7a35131dd81c6eb99b9a2950" class="memitem:ga1ec58a1d7a35131dd81c6eb99b9a2950">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">VALID_INITIAL_BUS_NAME_CHARACTER(c)</td>
</tr>
<tr class="memdesc:ga1ec58a1d7a35131dd81c6eb99b9a2950">
<td class="mdescLeft"> </td>
<td class="mdescRight">Determine wether the given character is valid as the first character in a bus name.<br />
</td>
</tr>
<tr class="separator:ga1ec58a1d7a35131dd81c6eb99b9a2950">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga225bd010fa638c822271047157a880f2" class="memitem:ga225bd010fa638c822271047157a880f2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">VALID_BUS_NAME_CHARACTER(c)</td>
</tr>
<tr class="memdesc:ga225bd010fa638c822271047157a880f2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Determine wether the given character is valid as a second or later character in a bus name.<br />
</td>
</tr>
<tr class="separator:ga225bd010fa638c822271047157a880f2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6751169d8d53eb2d4b3002ebd9bd021a" class="memitem:ga6751169d8d53eb2d4b3002ebd9bd021a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_dbus_validate_utf8(s, b, e)   _dbus_string_validate_utf8 (s, b, e)</td>
</tr>
<tr class="separator:ga6751169d8d53eb2d4b3002ebd9bd021a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab17853bba6b5508dc2d1eddad7e40946" class="memitem:gab17853bba6b5508dc2d1eddad7e40946">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DECLARE_DBUS_NAME_CHECK(what)   dbus_bool_t _dbus_check_is_valid_##what (const char *name)</td>
</tr>
<tr class="memdesc:gab17853bba6b5508dc2d1eddad7e40946">
<td class="mdescLeft"> </td>
<td class="mdescRight">A name check is used in _dbus_return_if_fail(), it's not suitable for validating untrusted data.<br />
</td>
</tr>
<tr class="separator:gab17853bba6b5508dc2d1eddad7e40946">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2d30023893c9483413f63d2b8d4e1fb9" class="memitem:ga2d30023893c9483413f63d2b8d4e1fb9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DEFINE_DBUS_NAME_CHECK(what)</td>
</tr>
<tr class="memdesc:ga2d30023893c9483413f63d2b8d4e1fb9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Define a name check to be used in _dbus_return_if_fail() statements.<br />
</td>
</tr>
<tr class="separator:ga2d30023893c9483413f63d2b8d4e1fb9">
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
<tr id="r_ga06fc87d81c62e9abb8790b6e5713c55b" class="memitem:ga06fc87d81c62e9abb8790b6e5713c55b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">enum  </td>
<td class="memItemRight" data-valign="bottom">{ <strong>MARSHAL_AS_STRING</strong> , <strong>MARSHAL_AS_SIGNATURE</strong> , <strong>MARSHAL_AS_BYTE_ARRAY</strong> }</td>
</tr>
<tr class="separator:ga06fc87d81c62e9abb8790b6e5713c55b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf9dce059725fa793c44b219460cbbe6d" class="memitem:gaf9dce059725fa793c44b219460cbbe6d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">enum  </td>
<td class="memItemRight" data-valign="bottom">DBusValidationMode { <strong>DBUS_VALIDATION_MODE_WE_TRUST_THIS_DATA_ABSOLUTELY</strong> , <strong>DBUS_VALIDATION_MODE_DATA_IS_UNTRUSTED</strong> }</td>
</tr>
<tr class="memdesc:gaf9dce059725fa793c44b219460cbbe6d">
<td class="mdescLeft"> </td>
<td class="mdescRight">This is used rather than a bool for high visibility. More...<br />
</td>
</tr>
<tr class="separator:gaf9dce059725fa793c44b219460cbbe6d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0c4521d30d6650a33673a4d7f9cc007c" class="memitem:ga0c4521d30d6650a33673a4d7f9cc007c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">enum  </td>
<td class="memItemRight" data-valign="bottom">DBusValidity {<br />
  DBUS_VALIDITY_UNKNOWN_OOM_ERROR = -4 , <strong>DBUS_INVALID_FOR_UNKNOWN_REASON</strong> = -3 , <strong>DBUS_VALID_BUT_INCOMPLETE</strong> = -2 , <strong>DBUS_VALIDITY_UNKNOWN</strong> = -1 ,<br />
  DBUS_VALID = 0 , <strong>DBUS_INVALID_UNKNOWN_TYPECODE</strong> = 1 , <strong>DBUS_INVALID_MISSING_ARRAY_ELEMENT_TYPE</strong> = 2 , <strong>DBUS_INVALID_SIGNATURE_TOO_LONG</strong> = 3 ,<br />
  <strong>DBUS_INVALID_EXCEEDED_MAXIMUM_ARRAY_RECURSION</strong> = 4 , <strong>DBUS_INVALID_EXCEEDED_MAXIMUM_STRUCT_RECURSION</strong> = 5 , <strong>DBUS_INVALID_STRUCT_ENDED_BUT_NOT_STARTED</strong> = 6 , <strong>DBUS_INVALID_STRUCT_STARTED_BUT_NOT_ENDED</strong> = 7 ,<br />
  <strong>DBUS_INVALID_STRUCT_HAS_NO_FIELDS</strong> = 8 , <strong>DBUS_INVALID_ALIGNMENT_PADDING_NOT_NUL</strong> = 9 , <strong>DBUS_INVALID_BOOLEAN_NOT_ZERO_OR_ONE</strong> = 10 , <strong>DBUS_INVALID_NOT_ENOUGH_DATA</strong> = 11 ,<br />
  DBUS_INVALID_TOO_MUCH_DATA = 12 , <strong>DBUS_INVALID_BAD_BYTE_ORDER</strong> = 13 , <strong>DBUS_INVALID_BAD_PROTOCOL_VERSION</strong> = 14 , <strong>DBUS_INVALID_BAD_MESSAGE_TYPE</strong> = 15 ,<br />
  <strong>DBUS_INVALID_BAD_SERIAL</strong> = 16 , <strong>DBUS_INVALID_INSANE_FIELDS_ARRAY_LENGTH</strong> = 17 , <strong>DBUS_INVALID_INSANE_BODY_LENGTH</strong> = 18 , <strong>DBUS_INVALID_MESSAGE_TOO_LONG</strong> = 19 ,<br />
  <strong>DBUS_INVALID_HEADER_FIELD_CODE</strong> = 20 , <strong>DBUS_INVALID_HEADER_FIELD_HAS_WRONG_TYPE</strong> = 21 , <strong>DBUS_INVALID_USES_LOCAL_INTERFACE</strong> = 22 , <strong>DBUS_INVALID_USES_LOCAL_PATH</strong> = 23 ,<br />
  <strong>DBUS_INVALID_HEADER_FIELD_APPEARS_TWICE</strong> = 24 , <strong>DBUS_INVALID_BAD_DESTINATION</strong> = 25 , <strong>DBUS_INVALID_BAD_INTERFACE</strong> = 26 , <strong>DBUS_INVALID_BAD_MEMBER</strong> = 27 ,<br />
  <strong>DBUS_INVALID_BAD_ERROR_NAME</strong> = 28 , <strong>DBUS_INVALID_BAD_SENDER</strong> = 29 , <strong>DBUS_INVALID_MISSING_PATH</strong> = 30 , <strong>DBUS_INVALID_MISSING_INTERFACE</strong> = 31 ,<br />
  <strong>DBUS_INVALID_MISSING_MEMBER</strong> = 32 , <strong>DBUS_INVALID_MISSING_ERROR_NAME</strong> = 33 , <strong>DBUS_INVALID_MISSING_REPLY_SERIAL</strong> = 34 , <strong>DBUS_INVALID_LENGTH_OUT_OF_BOUNDS</strong> = 35 ,<br />
  <strong>DBUS_INVALID_ARRAY_LENGTH_EXCEEDS_MAXIMUM</strong> = 36 , <strong>DBUS_INVALID_BAD_PATH</strong> = 37 , <strong>DBUS_INVALID_SIGNATURE_LENGTH_OUT_OF_BOUNDS</strong> = 38 , <strong>DBUS_INVALID_BAD_UTF8_IN_STRING</strong> = 39 ,<br />
  <strong>DBUS_INVALID_ARRAY_LENGTH_INCORRECT</strong> = 40 , <strong>DBUS_INVALID_VARIANT_SIGNATURE_LENGTH_OUT_OF_BOUNDS</strong> = 41 , <strong>DBUS_INVALID_VARIANT_SIGNATURE_BAD</strong> = 42 , <strong>DBUS_INVALID_VARIANT_SIGNATURE_EMPTY</strong> = 43 ,<br />
  <strong>DBUS_INVALID_VARIANT_SIGNATURE_SPECIFIES_MULTIPLE_VALUES</strong> = 44 , <strong>DBUS_INVALID_VARIANT_SIGNATURE_MISSING_NUL</strong> = 45 , <strong>DBUS_INVALID_STRING_MISSING_NUL</strong> = 46 , <strong>DBUS_INVALID_SIGNATURE_MISSING_NUL</strong> = 47 ,<br />
  <strong>DBUS_INVALID_EXCEEDED_MAXIMUM_DICT_ENTRY_RECURSION</strong> = 48 , <strong>DBUS_INVALID_DICT_ENTRY_ENDED_BUT_NOT_STARTED</strong> = 49 , <strong>DBUS_INVALID_DICT_ENTRY_STARTED_BUT_NOT_ENDED</strong> = 50 , <strong>DBUS_INVALID_DICT_ENTRY_HAS_NO_FIELDS</strong> = 51 ,<br />
  <strong>DBUS_INVALID_DICT_ENTRY_HAS_ONLY_ONE_FIELD</strong> = 52 , <strong>DBUS_INVALID_DICT_ENTRY_HAS_TOO_MANY_FIELDS</strong> = 53 , <strong>DBUS_INVALID_DICT_ENTRY_NOT_INSIDE_ARRAY</strong> = 54 , <strong>DBUS_INVALID_DICT_KEY_MUST_BE_BASIC_TYPE</strong> = 55 ,<br />
  <strong>DBUS_INVALID_MISSING_UNIX_FDS</strong> = 56 , <strong>DBUS_INVALID_NESTED_TOO_DEEPLY</strong> = 57 , <strong>DBUS_VALIDITY_LAST</strong><br />
}</td>
</tr>
<tr class="memdesc:ga0c4521d30d6650a33673a4d7f9cc007c">
<td class="mdescLeft"> </td>
<td class="mdescRight">This is primarily used in unit testing, so we can verify that each invalid message is invalid for the expected reasons. More...<br />
</td>
</tr>
<tr class="separator:ga0c4521d30d6650a33673a4d7f9cc007c">
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
<tr id="r_ga44e670d715bb678045f3d79b35920b0b" class="memitem:ga44e670d715bb678045f3d79b35920b0b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_pack_uint32 (dbus_uint32_t value, int byte_order, unsigned char *data)</td>
</tr>
<tr class="memdesc:ga44e670d715bb678045f3d79b35920b0b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Packs a 32 bit unsigned integer into a data pointer.<br />
</td>
</tr>
<tr class="separator:ga44e670d715bb678045f3d79b35920b0b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga09651b41b9a5aca37b0e2ff269880d6a" class="memitem:ga09651b41b9a5aca37b0e2ff269880d6a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint16_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_unpack_uint16 (int byte_order, const unsigned char *data)</td>
</tr>
<tr class="memdesc:ga09651b41b9a5aca37b0e2ff269880d6a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Unpacks a 16 bit unsigned integer from a data pointer.<br />
</td>
</tr>
<tr class="separator:ga09651b41b9a5aca37b0e2ff269880d6a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga50a9187b315cfcd6b311ed1b36488c05" class="memitem:ga50a9187b315cfcd6b311ed1b36488c05">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_unpack_uint32 (int byte_order, const unsigned char *data)</td>
</tr>
<tr class="memdesc:ga50a9187b315cfcd6b311ed1b36488c05">
<td class="mdescLeft"> </td>
<td class="mdescRight">Unpacks a 32 bit unsigned integer from a data pointer.<br />
</td>
</tr>
<tr class="separator:ga50a9187b315cfcd6b311ed1b36488c05">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4bcfb6a664c7e46c7ffc31f96d532a02" class="memitem:ga4bcfb6a664c7e46c7ffc31f96d532a02">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_marshal_set_uint32 (DBusString *str, int pos, dbus_uint32_t value, int byte_order)</td>
</tr>
<tr class="memdesc:ga4bcfb6a664c7e46c7ffc31f96d532a02">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the 4 bytes at the given offset to a marshaled unsigned integer, replacing anything found there previously.<br />
</td>
</tr>
<tr class="separator:ga4bcfb6a664c7e46c7ffc31f96d532a02">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga854526bdf221a5e82b2e14581ac17d8f" class="memitem:ga854526bdf221a5e82b2e14581ac17d8f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_marshal_set_basic (DBusString *str, int pos, int type, const void *value, int byte_order, int *old_end_pos, int *new_end_pos)</td>
</tr>
<tr class="memdesc:ga854526bdf221a5e82b2e14581ac17d8f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets an existing basic type value to a new value.<br />
</td>
</tr>
<tr class="separator:ga854526bdf221a5e82b2e14581ac17d8f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6dd82a202c19758cbf76dbed2946615d" class="memitem:ga6dd82a202c19758cbf76dbed2946615d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_marshal_read_uint32 (const DBusString *str, int pos, int byte_order, int *new_pos)</td>
</tr>
<tr class="memdesc:ga6dd82a202c19758cbf76dbed2946615d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Convenience function to demarshal a 32 bit unsigned integer.<br />
</td>
</tr>
<tr class="separator:ga6dd82a202c19758cbf76dbed2946615d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab331e099fa8cf3d94cf33ad7b20c81ae" class="memitem:gab331e099fa8cf3d94cf33ad7b20c81ae">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_marshal_read_basic (const DBusString *str, int pos, int type, void *value, int byte_order, int *new_pos)</td>
</tr>
<tr class="memdesc:gab331e099fa8cf3d94cf33ad7b20c81ae">
<td class="mdescLeft"> </td>
<td class="mdescRight">Demarshals a basic-typed value.<br />
</td>
</tr>
<tr class="separator:gab331e099fa8cf3d94cf33ad7b20c81ae">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga54323d48921de8c5bd04ae01548312bb" class="memitem:ga54323d48921de8c5bd04ae01548312bb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_marshal_write_basic (DBusString *str, int insert_at, int type, const void *value, int byte_order, int *pos_after)</td>
</tr>
<tr class="memdesc:ga54323d48921de8c5bd04ae01548312bb">
<td class="mdescLeft"> </td>
<td class="mdescRight">Marshals a basic-typed value.<br />
</td>
</tr>
<tr class="separator:ga54323d48921de8c5bd04ae01548312bb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaec86e8e1ae2f25b673ae6d900ab323c7" class="memitem:gaec86e8e1ae2f25b673ae6d900ab323c7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_swap_array (unsigned char *data, int n_elements, int alignment)</td>
</tr>
<tr class="memdesc:gaec86e8e1ae2f25b673ae6d900ab323c7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Swaps the elements of an array to the opposite byte order.<br />
</td>
</tr>
<tr class="separator:gaec86e8e1ae2f25b673ae6d900ab323c7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga990da87b984d8917da26b89a6470fdf5" class="memitem:ga990da87b984d8917da26b89a6470fdf5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_marshal_write_fixed_multi (DBusString *str, int insert_at, int element_type, const void *value, int n_elements, int byte_order, int *pos_after)</td>
</tr>
<tr class="memdesc:ga990da87b984d8917da26b89a6470fdf5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Marshals a block of values of fixed-length type all at once, as an optimization.<br />
</td>
</tr>
<tr class="separator:ga990da87b984d8917da26b89a6470fdf5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gafd1ab7e9bd8e74cc41f03c76f4dce2dd" class="memitem:gafd1ab7e9bd8e74cc41f03c76f4dce2dd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_marshal_skip_basic (const DBusString *str, int type, int byte_order, int *pos)</td>
</tr>
<tr class="memdesc:gafd1ab7e9bd8e74cc41f03c76f4dce2dd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Skips over a basic-typed value, reporting the following position.<br />
</td>
</tr>
<tr class="separator:gafd1ab7e9bd8e74cc41f03c76f4dce2dd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8d9c5bcc039d9099df197a125a7259b8" class="memitem:ga8d9c5bcc039d9099df197a125a7259b8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_marshal_skip_array (const DBusString *str, int element_type, int byte_order, int *pos)</td>
</tr>
<tr class="memdesc:ga8d9c5bcc039d9099df197a125a7259b8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Skips an array, returning the next position.<br />
</td>
</tr>
<tr class="separator:ga8d9c5bcc039d9099df197a125a7259b8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2ba80f227880e442c140bc67653b0abd" class="memitem:ga2ba80f227880e442c140bc67653b0abd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_get_alignment (int typecode)</td>
</tr>
<tr class="memdesc:ga2ba80f227880e442c140bc67653b0abd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the alignment requirement for the given type; will be 1, 2, 4, or 8.<br />
</td>
</tr>
<tr class="separator:ga2ba80f227880e442c140bc67653b0abd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaaddd76c0af2175dd80c99c052a12e724" class="memitem:gaaddd76c0af2175dd80c99c052a12e724">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_to_string (int typecode)</td>
</tr>
<tr class="memdesc:gaaddd76c0af2175dd80c99c052a12e724">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns a string describing the given type.<br />
</td>
</tr>
<tr class="separator:gaaddd76c0af2175dd80c99c052a12e724">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7f3320a0b0f7633cdf5c149588ae9bd9" class="memitem:ga7f3320a0b0f7633cdf5c149588ae9bd9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_verbose_bytes (const unsigned char *data, int len, int offset)</td>
</tr>
<tr class="memdesc:ga7f3320a0b0f7633cdf5c149588ae9bd9">
<td class="mdescLeft"> </td>
<td class="mdescRight">If in verbose mode, print a block of binary data.<br />
</td>
</tr>
<tr class="separator:ga7f3320a0b0f7633cdf5c149588ae9bd9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3926bb35edf78d114cf0c341fe3258e0" class="memitem:ga3926bb35edf78d114cf0c341fe3258e0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_verbose_bytes_of_string (const DBusString *str, int start, int len)</td>
</tr>
<tr class="memdesc:ga3926bb35edf78d114cf0c341fe3258e0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Dump the given part of the string to verbose log.<br />
</td>
</tr>
<tr class="separator:ga3926bb35edf78d114cf0c341fe3258e0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5866a0fd058aed3396402d0456144fd2" class="memitem:ga5866a0fd058aed3396402d0456144fd2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_first_type_in_signature (const DBusString *str, int pos)</td>
</tr>
<tr class="memdesc:ga5866a0fd058aed3396402d0456144fd2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Get the first type in the signature.<br />
</td>
</tr>
<tr class="separator:ga5866a0fd058aed3396402d0456144fd2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga61cc8d9c4e4217be654455d8eb45544c" class="memitem:ga61cc8d9c4e4217be654455d8eb45544c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_first_type_in_signature_c_str (const char *str, int pos)</td>
</tr>
<tr class="memdesc:ga61cc8d9c4e4217be654455d8eb45544c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Similar to _dbus_first_type_in_signature, but operates on a C string buffer.<br />
</td>
</tr>
<tr class="separator:ga61cc8d9c4e4217be654455d8eb45544c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga609a4b8c0b65096890766fda73a4c40f" class="memitem:ga609a4b8c0b65096890766fda73a4c40f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_marshal_byteswap (const DBusString *signature, int signature_start, int old_byte_order, int new_byte_order, DBusString *value_str, int value_pos)</td>
</tr>
<tr class="memdesc:ga609a4b8c0b65096890766fda73a4c40f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Byteswaps the marshaled data in the given value_str.<br />
</td>
</tr>
<tr class="separator:ga609a4b8c0b65096890766fda73a4c40f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab49ca4819ef45b26463427bb09060844" class="memitem:gab49ca4819ef45b26463427bb09060844">
<td class="memItemLeft" style="text-align: right;" data-valign="top">  </td>
<td class="memItemRight" data-valign="bottom"><strong>_DBUS_STRING_DEFINE_STATIC</strong> (_dbus_header_signature_str, DBUS_HEADER_SIGNATURE)</td>
</tr>
<tr class="memdesc:gab49ca4819ef45b26463427bb09060844">
<td class="mdescLeft"> </td>
<td class="mdescRight">Static DBusString containing the signature of a message header.<br />
</td>
</tr>
<tr class="separator:gab49ca4819ef45b26463427bb09060844">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4d454446fbca28c07187eb8bb627f70b" class="memitem:ga4d454446fbca28c07187eb8bb627f70b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">  </td>
<td class="memItemRight" data-valign="bottom"><strong>_DBUS_STRING_DEFINE_STATIC</strong> (_dbus_local_interface_str, DBUS_INTERFACE_LOCAL)</td>
</tr>
<tr class="memdesc:ga4d454446fbca28c07187eb8bb627f70b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Static DBusString containing the local interface.<br />
</td>
</tr>
<tr class="separator:ga4d454446fbca28c07187eb8bb627f70b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga991dd170f3d84b4bf195caf3a1046d28" class="memitem:ga991dd170f3d84b4bf195caf3a1046d28">
<td class="memItemLeft" style="text-align: right;" data-valign="top">  </td>
<td class="memItemRight" data-valign="bottom"><strong>_DBUS_STRING_DEFINE_STATIC</strong> (_dbus_local_path_str, DBUS_PATH_LOCAL)</td>
</tr>
<tr class="memdesc:ga991dd170f3d84b4bf195caf3a1046d28">
<td class="mdescLeft"> </td>
<td class="mdescRight">Static DBusString containing the local path.<br />
</td>
</tr>
<tr class="separator:ga991dd170f3d84b4bf195caf3a1046d28">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga65c023673b837c27e8ccda5c2528d806" class="memitem:ga65c023673b837c27e8ccda5c2528d806">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char </td>
<td class="memItemRight" data-valign="bottom">_dbus_header_get_byte_order (const DBusHeader *header)</td>
</tr>
<tr class="memdesc:ga65c023673b837c27e8ccda5c2528d806">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns the header's byte order.<br />
</td>
</tr>
<tr class="separator:ga65c023673b837c27e8ccda5c2528d806">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4427247494fc5c988498c5a87d42092d" class="memitem:ga4427247494fc5c988498c5a87d42092d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_header_get_message_type (DBusHeader *header)</td>
</tr>
<tr class="memdesc:ga4427247494fc5c988498c5a87d42092d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the type of the message.<br />
</td>
</tr>
<tr class="separator:ga4427247494fc5c988498c5a87d42092d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad92e0b1992cf96a4da642a4a54a5d26d" class="memitem:gad92e0b1992cf96a4da642a4a54a5d26d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_header_set_serial (DBusHeader *header, dbus_uint32_t serial)</td>
</tr>
<tr class="memdesc:gad92e0b1992cf96a4da642a4a54a5d26d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the serial number of a header.<br />
</td>
</tr>
<tr class="separator:gad92e0b1992cf96a4da642a4a54a5d26d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7ec7222423db42935aae4a24499ee0fb" class="memitem:ga7ec7222423db42935aae4a24499ee0fb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_header_get_serial (DBusHeader *header)</td>
</tr>
<tr class="memdesc:ga7ec7222423db42935aae4a24499ee0fb">
<td class="mdescLeft"> </td>
<td class="mdescRight">See dbus_message_get_serial()<br />
</td>
</tr>
<tr class="separator:ga7ec7222423db42935aae4a24499ee0fb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6d41ad4de211c87f4b8a43340b6893e2" class="memitem:ga6d41ad4de211c87f4b8a43340b6893e2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_header_reinit (DBusHeader *header)</td>
</tr>
<tr class="memdesc:ga6d41ad4de211c87f4b8a43340b6893e2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Re-initializes a header that was previously initialized and never freed.<br />
</td>
</tr>
<tr class="separator:ga6d41ad4de211c87f4b8a43340b6893e2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabe1b78193d712976734a39d35842f033" class="memitem:gabe1b78193d712976734a39d35842f033">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_header_init (DBusHeader *header)</td>
</tr>
<tr class="memdesc:gabe1b78193d712976734a39d35842f033">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initializes a header, but doesn't prepare it for use; to make the header valid, you have to call _dbus_header_create().<br />
</td>
</tr>
<tr class="separator:gabe1b78193d712976734a39d35842f033">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab90a814a27aeeace7e02c4ed130539cf" class="memitem:gab90a814a27aeeace7e02c4ed130539cf">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_header_free (DBusHeader *header)</td>
</tr>
<tr class="memdesc:gab90a814a27aeeace7e02c4ed130539cf">
<td class="mdescLeft"> </td>
<td class="mdescRight">Frees a header.<br />
</td>
</tr>
<tr class="separator:gab90a814a27aeeace7e02c4ed130539cf">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0d5aad82f8bf5a314dcf3f70930e254b" class="memitem:ga0d5aad82f8bf5a314dcf3f70930e254b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_header_copy (const DBusHeader *header, DBusHeader *dest)</td>
</tr>
<tr class="memdesc:ga0d5aad82f8bf5a314dcf3f70930e254b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initializes dest with a copy of the given header.<br />
</td>
</tr>
<tr class="separator:ga0d5aad82f8bf5a314dcf3f70930e254b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac7901e4196f10d4763df89b42d5db03e" class="memitem:gac7901e4196f10d4763df89b42d5db03e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_header_create (DBusHeader *header, int byte_order, int message_type, const char *destination, const char *path, const char *interface, const char *member, const char *error_name)</td>
</tr>
<tr class="memdesc:gac7901e4196f10d4763df89b42d5db03e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Fills in the primary fields of the header, so the header is ready for use.<br />
</td>
</tr>
<tr class="separator:gac7901e4196f10d4763df89b42d5db03e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga674d74081baf6e7531e0d4a286724210" class="memitem:ga674d74081baf6e7531e0d4a286724210">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_header_have_message_untrusted (int max_message_length, DBusValidity *validity, int *byte_order, int *fields_array_len, int *header_len, int *body_len, const DBusString *str, int start, int len)</td>
</tr>
<tr class="memdesc:ga674d74081baf6e7531e0d4a286724210">
<td class="mdescLeft"> </td>
<td class="mdescRight">Given data long enough to contain the length of the message body and the fields array, check whether the data is long enough to contain the entire message (assuming the claimed lengths are accurate).<br />
</td>
</tr>
<tr class="separator:ga674d74081baf6e7531e0d4a286724210">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gada7fb80ccb799c63a1cfe8d111ac4d30" class="memitem:gada7fb80ccb799c63a1cfe8d111ac4d30">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_header_load (DBusHeader *header, DBusValidationMode mode, DBusValidity *validity, int byte_order, int fields_array_len, int header_len, int body_len, const DBusString *str)</td>
</tr>
<tr class="memdesc:gada7fb80ccb799c63a1cfe8d111ac4d30">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a message header from potentially-untrusted data.<br />
</td>
</tr>
<tr class="separator:gada7fb80ccb799c63a1cfe8d111ac4d30">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0cff04252f97f6a25552c368199897f5" class="memitem:ga0cff04252f97f6a25552c368199897f5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_header_update_lengths (DBusHeader *header, int body_len)</td>
</tr>
<tr class="memdesc:ga0cff04252f97f6a25552c368199897f5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Fills in the correct body length.<br />
</td>
</tr>
<tr class="separator:ga0cff04252f97f6a25552c368199897f5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4349de00b7754a337526e36fda133464" class="memitem:ga4349de00b7754a337526e36fda133464">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_header_set_field_basic (DBusHeader *header, int field, int type, const void *value)</td>
</tr>
<tr class="memdesc:ga4349de00b7754a337526e36fda133464">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the value of a field with basic type.<br />
</td>
</tr>
<tr class="separator:ga4349de00b7754a337526e36fda133464">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga499973a18dcb17d854eaf14101a66736" class="memitem:ga499973a18dcb17d854eaf14101a66736">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_header_get_field_basic (DBusHeader *header, int field, int type, void *value)</td>
</tr>
<tr class="memdesc:ga499973a18dcb17d854eaf14101a66736">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the value of a field with basic type.<br />
</td>
</tr>
<tr class="separator:ga499973a18dcb17d854eaf14101a66736">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf4661ba8e7067f349ba03c9f5776bbb0" class="memitem:gaf4661ba8e7067f349ba03c9f5776bbb0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_header_get_field_raw (DBusHeader *header, int field, const DBusString **str, int *pos)</td>
</tr>
<tr class="memdesc:gaf4661ba8e7067f349ba03c9f5776bbb0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the raw marshaled data for a field.<br />
</td>
</tr>
<tr class="separator:gaf4661ba8e7067f349ba03c9f5776bbb0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7814248f4d74d109d29dc00487cd9b0c" class="memitem:ga7814248f4d74d109d29dc00487cd9b0c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_header_delete_field (DBusHeader *header, int field)</td>
</tr>
<tr class="memdesc:ga7814248f4d74d109d29dc00487cd9b0c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Deletes a field, if it exists.<br />
</td>
</tr>
<tr class="separator:ga7814248f4d74d109d29dc00487cd9b0c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad2073f8f2f2ba3b710aa929dced34cc3" class="memitem:gad2073f8f2f2ba3b710aa929dced34cc3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_header_toggle_flag (DBusHeader *header, dbus_uint32_t flag, dbus_bool_t value)</td>
</tr>
<tr class="memdesc:gad2073f8f2f2ba3b710aa929dced34cc3">
<td class="mdescLeft"> </td>
<td class="mdescRight">Toggles a message flag bit, turning on the bit if value = TRUE and flipping it off if value = FALSE.<br />
</td>
</tr>
<tr class="separator:gad2073f8f2f2ba3b710aa929dced34cc3">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga56619efed3088554b8760edd246b4157" class="memitem:ga56619efed3088554b8760edd246b4157">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_header_get_flag (DBusHeader *header, dbus_uint32_t flag)</td>
</tr>
<tr class="memdesc:ga56619efed3088554b8760edd246b4157">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets a message flag bit, returning TRUE if the bit is set.<br />
</td>
</tr>
<tr class="separator:ga56619efed3088554b8760edd246b4157">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae5277c7b7bfb7b85e421baceac0398c8" class="memitem:gae5277c7b7bfb7b85e421baceac0398c8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_header_byteswap (DBusHeader *header, int new_order)</td>
</tr>
<tr class="memdesc:gae5277c7b7bfb7b85e421baceac0398c8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Swaps the header into the given order if required.<br />
</td>
</tr>
<tr class="separator:gae5277c7b7bfb7b85e421baceac0398c8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7e273d0673d55e0124d7f074979d3dea" class="memitem:ga7e273d0673d55e0124d7f074979d3dea">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_header_remove_unknown_fields (DBusHeader *header)</td>
</tr>
<tr class="memdesc:ga7e273d0673d55e0124d7f074979d3dea">
<td class="mdescLeft"> </td>
<td class="mdescRight">Remove every header field not known to this version of dbus.<br />
</td>
</tr>
<tr class="separator:ga7e273d0673d55e0124d7f074979d3dea">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf2f5b2f027fa7d24f6179c6dbdf71a83" class="memitem:gaf2f5b2f027fa7d24f6179c6dbdf71a83">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_signature_next (const char *type_str, int *type_pos)</td>
</tr>
<tr class="memdesc:gaf2f5b2f027fa7d24f6179c6dbdf71a83">
<td class="mdescLeft"> </td>
<td class="mdescRight">Skips to the next "complete" type inside a type signature.<br />
</td>
</tr>
<tr class="separator:gaf2f5b2f027fa7d24f6179c6dbdf71a83">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga35d70cf69b1196518367e3e68e9b2dd2" class="memitem:ga35d70cf69b1196518367e3e68e9b2dd2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_reader_init (DBusTypeReader *reader, int byte_order, const DBusString *type_str, int type_pos, const DBusString *value_str, int value_pos)</td>
</tr>
<tr class="memdesc:ga35d70cf69b1196518367e3e68e9b2dd2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initializes a type reader.<br />
</td>
</tr>
<tr class="separator:ga35d70cf69b1196518367e3e68e9b2dd2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3a5845f555f11c33ebaa71a75abff661" class="memitem:ga3a5845f555f11c33ebaa71a75abff661">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_reader_init_types_only (DBusTypeReader *reader, const DBusString *type_str, int type_pos)</td>
</tr>
<tr class="memdesc:ga3a5845f555f11c33ebaa71a75abff661">
<td class="mdescLeft"> </td>
<td class="mdescRight">Like _dbus_type_reader_init() but the iteration is over the signature, not over values.<br />
</td>
</tr>
<tr class="separator:ga3a5845f555f11c33ebaa71a75abff661">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab8e39cb8084247d54d7f272c51622a73" class="memitem:gab8e39cb8084247d54d7f272c51622a73">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_reader_get_current_type (const DBusTypeReader *reader)</td>
</tr>
<tr class="memdesc:gab8e39cb8084247d54d7f272c51622a73">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the type of the value the reader is currently pointing to; or for a types-only reader gets the type it's currently pointing to.<br />
</td>
</tr>
<tr class="separator:gab8e39cb8084247d54d7f272c51622a73">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6e5439f7ca5ee8a1ce943ddab7611d0d" class="memitem:ga6e5439f7ca5ee8a1ce943ddab7611d0d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_reader_get_element_type (const DBusTypeReader *reader)</td>
</tr>
<tr class="memdesc:ga6e5439f7ca5ee8a1ce943ddab7611d0d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the type of an element of the array the reader is currently pointing to.<br />
</td>
</tr>
<tr class="separator:ga6e5439f7ca5ee8a1ce943ddab7611d0d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2a8ab1152821950b1fe29e000954981c" class="memitem:ga2a8ab1152821950b1fe29e000954981c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_reader_get_value_pos (const DBusTypeReader *reader)</td>
</tr>
<tr class="memdesc:ga2a8ab1152821950b1fe29e000954981c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the current position in the value block.<br />
</td>
</tr>
<tr class="separator:ga2a8ab1152821950b1fe29e000954981c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac87315d74386314ec3b148ef737626d2" class="memitem:gac87315d74386314ec3b148ef737626d2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_reader_read_raw (const DBusTypeReader *reader, const unsigned char **value_location)</td>
</tr>
<tr class="memdesc:gac87315d74386314ec3b148ef737626d2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Get the address of the marshaled value in the data being read.<br />
</td>
</tr>
<tr class="separator:gac87315d74386314ec3b148ef737626d2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa54355ee98d6721d7a29b5ae7d92eb9a" class="memitem:gaa54355ee98d6721d7a29b5ae7d92eb9a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_reader_read_basic (const DBusTypeReader *reader, void *value)</td>
</tr>
<tr class="memdesc:gaa54355ee98d6721d7a29b5ae7d92eb9a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reads a basic-typed value, as with _dbus_marshal_read_basic().<br />
</td>
</tr>
<tr class="separator:gaa54355ee98d6721d7a29b5ae7d92eb9a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7def93d676d528c261aa274cea41c29d" class="memitem:ga7def93d676d528c261aa274cea41c29d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_reader_get_array_length (const DBusTypeReader *reader)</td>
</tr>
<tr class="memdesc:ga7def93d676d528c261aa274cea41c29d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns the number of bytes in the array.<br />
</td>
</tr>
<tr class="separator:ga7def93d676d528c261aa274cea41c29d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga638f98cc5dc5855c583541fba67ad5b6" class="memitem:ga638f98cc5dc5855c583541fba67ad5b6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_reader_read_fixed_multi (const DBusTypeReader *reader, const void **value, int *n_elements)</td>
</tr>
<tr class="memdesc:ga638f98cc5dc5855c583541fba67ad5b6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reads a block of fixed-length basic values, from the current point in an array to the end of the array.<br />
</td>
</tr>
<tr class="separator:ga638f98cc5dc5855c583541fba67ad5b6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga082b410820c74b2a6ca816a8e0c91803" class="memitem:ga082b410820c74b2a6ca816a8e0c91803">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_reader_recurse (DBusTypeReader *reader, DBusTypeReader *sub)</td>
</tr>
<tr class="memdesc:ga082b410820c74b2a6ca816a8e0c91803">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initialize a new reader pointing to the first type and corresponding value that's a child of the current container.<br />
</td>
</tr>
<tr class="separator:ga082b410820c74b2a6ca816a8e0c91803">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga746c09512d4905f2d2fac7ed4c3c63c2" class="memitem:ga746c09512d4905f2d2fac7ed4c3c63c2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_reader_next (DBusTypeReader *reader)</td>
</tr>
<tr class="memdesc:ga746c09512d4905f2d2fac7ed4c3c63c2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Skip to the next value on this "level".<br />
</td>
</tr>
<tr class="separator:ga746c09512d4905f2d2fac7ed4c3c63c2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga97a59dbd1597ef1b267457e809f095de" class="memitem:ga97a59dbd1597ef1b267457e809f095de">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_reader_has_next (const DBusTypeReader *reader)</td>
</tr>
<tr class="memdesc:ga97a59dbd1597ef1b267457e809f095de">
<td class="mdescLeft"> </td>
<td class="mdescRight">Check whether there's another value on this "level".<br />
</td>
</tr>
<tr class="separator:ga97a59dbd1597ef1b267457e809f095de">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4578cc623c8b0978ca780ce0ab950fdb" class="memitem:ga4578cc623c8b0978ca780ce0ab950fdb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_reader_get_signature (const DBusTypeReader *reader, const DBusString **str_p, int *start_p, int *len_p)</td>
</tr>
<tr class="memdesc:ga4578cc623c8b0978ca780ce0ab950fdb">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the string and range of said string containing the signature of the current value.<br />
</td>
</tr>
<tr class="separator:ga4578cc623c8b0978ca780ce0ab950fdb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaaf11ca429434c2c280f5fad34ed95204" class="memitem:gaaf11ca429434c2c280f5fad34ed95204">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_reader_set_basic (DBusTypeReader *reader, const void *value, const DBusTypeReader *realign_root)</td>
</tr>
<tr class="memdesc:gaaf11ca429434c2c280f5fad34ed95204">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets a new value for the basic type value pointed to by the reader, leaving the reader valid to continue reading.<br />
</td>
</tr>
<tr class="separator:gaaf11ca429434c2c280f5fad34ed95204">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa4057610b3d9e81fed212c17f6599516" class="memitem:gaa4057610b3d9e81fed212c17f6599516">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_reader_delete (DBusTypeReader *reader, const DBusTypeReader *realign_root)</td>
</tr>
<tr class="memdesc:gaa4057610b3d9e81fed212c17f6599516">
<td class="mdescLeft"> </td>
<td class="mdescRight">Recursively deletes any value pointed to by the reader, leaving the reader valid to continue reading.<br />
</td>
</tr>
<tr class="separator:gaa4057610b3d9e81fed212c17f6599516">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gadeb83962df31e074874e957d17a0d4d1" class="memitem:gadeb83962df31e074874e957d17a0d4d1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_writer_init (DBusTypeWriter *writer, int byte_order, DBusString *type_str, int type_pos, DBusString *value_str, int value_pos)</td>
</tr>
<tr class="memdesc:gadeb83962df31e074874e957d17a0d4d1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initialize a write iterator, which is used to write out values in serialized D-Bus format.<br />
</td>
</tr>
<tr class="separator:gadeb83962df31e074874e957d17a0d4d1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa9ecf7e96d5323bc1da9cdf0c3f2c1e7" class="memitem:gaa9ecf7e96d5323bc1da9cdf0c3f2c1e7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_writer_init_types_delayed (DBusTypeWriter *writer, int byte_order, DBusString *value_str, int value_pos)</td>
</tr>
<tr class="memdesc:gaa9ecf7e96d5323bc1da9cdf0c3f2c1e7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initialize a write iterator, with the signature to be provided later.<br />
</td>
</tr>
<tr class="separator:gaa9ecf7e96d5323bc1da9cdf0c3f2c1e7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga863b2f232a21582f9e6fe1951b09da91" class="memitem:ga863b2f232a21582f9e6fe1951b09da91">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_writer_add_types (DBusTypeWriter *writer, DBusString *type_str, int type_pos)</td>
</tr>
<tr class="memdesc:ga863b2f232a21582f9e6fe1951b09da91">
<td class="mdescLeft"> </td>
<td class="mdescRight">Adds type string to the writer, if it had none.<br />
</td>
</tr>
<tr class="separator:ga863b2f232a21582f9e6fe1951b09da91">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga34d675b57c7e6569707d22ba76ae010c" class="memitem:ga34d675b57c7e6569707d22ba76ae010c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_writer_remove_types (DBusTypeWriter *writer)</td>
</tr>
<tr class="memdesc:ga34d675b57c7e6569707d22ba76ae010c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Removes type string from the writer.<br />
</td>
</tr>
<tr class="separator:ga34d675b57c7e6569707d22ba76ae010c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1f101175ce6f33221fcb59f0b46349bd" class="memitem:ga1f101175ce6f33221fcb59f0b46349bd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_writer_init_values_only (DBusTypeWriter *writer, int byte_order, const DBusString *type_str, int type_pos, DBusString *value_str, int value_pos)</td>
</tr>
<tr class="memdesc:ga1f101175ce6f33221fcb59f0b46349bd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Like _dbus_type_writer_init(), except the type string passed in should correspond to an existing signature that matches what you're going to write out.<br />
</td>
</tr>
<tr class="separator:ga1f101175ce6f33221fcb59f0b46349bd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4c0a1036e59dac270141052d951baff2" class="memitem:ga4c0a1036e59dac270141052d951baff2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_writer_recurse (DBusTypeWriter *writer, int container_type, const DBusString *contained_type, int contained_type_start, DBusTypeWriter *sub)</td>
</tr>
<tr class="memdesc:ga4c0a1036e59dac270141052d951baff2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Opens a new container and writes out the initial information for that container.<br />
</td>
</tr>
<tr class="separator:ga4c0a1036e59dac270141052d951baff2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gacc2b4c348f93898f6269feb0bf055617" class="memitem:gacc2b4c348f93898f6269feb0bf055617">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_writer_append_array (DBusTypeWriter *writer, const DBusString *contained_type, int contained_type_start, DBusTypeWriter *sub)</td>
</tr>
<tr class="memdesc:gacc2b4c348f93898f6269feb0bf055617">
<td class="mdescLeft"> </td>
<td class="mdescRight">Append to an existing array.<br />
</td>
</tr>
<tr class="separator:gacc2b4c348f93898f6269feb0bf055617">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gacbe7eddf4f9c19da91b742087fcc111a" class="memitem:gacbe7eddf4f9c19da91b742087fcc111a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_writer_unrecurse (DBusTypeWriter *writer, DBusTypeWriter *sub)</td>
</tr>
<tr class="memdesc:gacbe7eddf4f9c19da91b742087fcc111a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Closes a container created by _dbus_type_writer_recurse() and writes any additional information to the values block.<br />
</td>
</tr>
<tr class="separator:gacbe7eddf4f9c19da91b742087fcc111a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0103b0214766b0ff1ca05bcc7f1e631b" class="memitem:ga0103b0214766b0ff1ca05bcc7f1e631b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_writer_write_basic (DBusTypeWriter *writer, int type, const void *value)</td>
</tr>
<tr class="memdesc:ga0103b0214766b0ff1ca05bcc7f1e631b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Writes out a basic type.<br />
</td>
</tr>
<tr class="separator:ga0103b0214766b0ff1ca05bcc7f1e631b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gacf99495cbed7462992b6a231563b4528" class="memitem:gacf99495cbed7462992b6a231563b4528">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_writer_write_fixed_multi (DBusTypeWriter *writer, int element_type, const void *value, int n_elements)</td>
</tr>
<tr class="memdesc:gacf99495cbed7462992b6a231563b4528">
<td class="mdescLeft"> </td>
<td class="mdescRight">Writes a block of fixed-length basic values, i.e.<br />
</td>
</tr>
<tr class="separator:gacf99495cbed7462992b6a231563b4528">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4905750705d220efe9dfc71f49bedc11" class="memitem:ga4905750705d220efe9dfc71f49bedc11">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_type_writer_write_reader (DBusTypeWriter *writer, DBusTypeReader *reader)</td>
</tr>
<tr class="memdesc:ga4905750705d220efe9dfc71f49bedc11">
<td class="mdescLeft"> </td>
<td class="mdescRight">Iterate through all values in the given reader, writing a copy of each value to the writer.<br />
</td>
</tr>
<tr class="separator:ga4905750705d220efe9dfc71f49bedc11">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga11a11f05c4f57415f9725a2cb9af30ea" class="memitem:ga11a11f05c4f57415f9725a2cb9af30ea">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusValidity </td>
<td class="memItemRight" data-valign="bottom">_dbus_validate_signature_with_reason (const DBusString *type_str, int type_pos, int len)</td>
</tr>
<tr class="memdesc:ga11a11f05c4f57415f9725a2cb9af30ea">
<td class="mdescLeft"> </td>
<td class="mdescRight">Verifies that the range of type_str from type_pos to type_end is a valid signature.<br />
</td>
</tr>
<tr class="separator:ga11a11f05c4f57415f9725a2cb9af30ea">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab184d3630bab4e32cb02d969ef216b9d" class="memitem:gab184d3630bab4e32cb02d969ef216b9d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusValidity </td>
<td class="memItemRight" data-valign="bottom">_dbus_validate_body_with_reason (const DBusString *expected_signature, int expected_signature_start, int byte_order, int *bytes_remaining, const DBusString *value_str, int value_pos, int len)</td>
</tr>
<tr class="memdesc:gab184d3630bab4e32cb02d969ef216b9d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Verifies that the range of value_str from value_pos to value_end is a legitimate value of type expected_signature.<br />
</td>
</tr>
<tr class="separator:gab184d3630bab4e32cb02d969ef216b9d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9835918b2484496d59542a9c36623413" class="memitem:ga9835918b2484496d59542a9c36623413">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_validate_path (const DBusString *str, int start, int len)</td>
</tr>
<tr class="memdesc:ga9835918b2484496d59542a9c36623413">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks that the given range of the string is a valid object path name in the D-Bus protocol.<br />
</td>
</tr>
<tr class="separator:ga9835918b2484496d59542a9c36623413">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf556cf614f291d931deb07fdeb74369f" class="memitem:gaf556cf614f291d931deb07fdeb74369f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">_dbus_validity_to_error_message (DBusValidity validity)</td>
</tr>
<tr class="separator:gaf556cf614f291d931deb07fdeb74369f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaaae1848bb806d1e5281af4ddb56990be" class="memitem:gaaae1848bb806d1e5281af4ddb56990be">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_validate_interface (const DBusString *str, int start, int len)</td>
</tr>
<tr class="memdesc:gaaae1848bb806d1e5281af4ddb56990be">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks that the given range of the string is a valid interface name in the D-Bus protocol.<br />
</td>
</tr>
<tr class="separator:gaaae1848bb806d1e5281af4ddb56990be">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga73c4f75424f78c6a9bc5122b301d8964" class="memitem:ga73c4f75424f78c6a9bc5122b301d8964">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_validate_member (const DBusString *str, int start, int len)</td>
</tr>
<tr class="memdesc:ga73c4f75424f78c6a9bc5122b301d8964">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks that the given range of the string is a valid member name in the D-Bus protocol.<br />
</td>
</tr>
<tr class="separator:ga73c4f75424f78c6a9bc5122b301d8964">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4305e3ccdbeca4cb2c1b3e922d36142f" class="memitem:ga4305e3ccdbeca4cb2c1b3e922d36142f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_validate_error_name (const DBusString *str, int start, int len)</td>
</tr>
<tr class="memdesc:ga4305e3ccdbeca4cb2c1b3e922d36142f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks that the given range of the string is a valid error name in the D-Bus protocol.<br />
</td>
</tr>
<tr class="separator:ga4305e3ccdbeca4cb2c1b3e922d36142f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab9dc933ebab3e6b0c9d52af308cae87f" class="memitem:gab9dc933ebab3e6b0c9d52af308cae87f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_validate_bus_name (const DBusString *str, int start, int len)</td>
</tr>
<tr class="memdesc:gab9dc933ebab3e6b0c9d52af308cae87f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks that the given range of the string is a valid bus name in the D-Bus protocol.<br />
</td>
</tr>
<tr class="separator:gab9dc933ebab3e6b0c9d52af308cae87f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga820b8a607c6a931bb0163bba7c4e8014" class="memitem:ga820b8a607c6a931bb0163bba7c4e8014">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_validate_bus_namespace (const DBusString *str, int start, int len)</td>
</tr>
<tr class="memdesc:ga820b8a607c6a931bb0163bba7c4e8014">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks that the given range of the string is a prefix of a valid bus name in the D-Bus protocol.<br />
</td>
</tr>
<tr class="separator:ga820b8a607c6a931bb0163bba7c4e8014">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gafc52be1357121d1ba57d2b381ce3bd33" class="memitem:gafc52be1357121d1ba57d2b381ce3bd33">
<td class="memItemLeft" style="text-align: right;" data-valign="top">  </td>
<td class="memItemRight" data-valign="bottom"><strong>DECLARE_DBUS_NAME_CHECK</strong> (path)</td>
</tr>
<tr class="memdesc:gafc52be1357121d1ba57d2b381ce3bd33">
<td class="mdescLeft"> </td>
<td class="mdescRight">defines _dbus_check_is_valid_path()<br />
</td>
</tr>
<tr class="separator:gafc52be1357121d1ba57d2b381ce3bd33">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga540ccb97245861b105db0066245957be" class="memitem:ga540ccb97245861b105db0066245957be">
<td class="memItemLeft" style="text-align: right;" data-valign="top">  </td>
<td class="memItemRight" data-valign="bottom"><strong>DECLARE_DBUS_NAME_CHECK</strong> (interface)</td>
</tr>
<tr class="memdesc:ga540ccb97245861b105db0066245957be">
<td class="mdescLeft"> </td>
<td class="mdescRight">defines _dbus_check_is_valid_interface()<br />
</td>
</tr>
<tr class="separator:ga540ccb97245861b105db0066245957be">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabc341dacc35d8243ed6350646bf8e685" class="memitem:gabc341dacc35d8243ed6350646bf8e685">
<td class="memItemLeft" style="text-align: right;" data-valign="top">  </td>
<td class="memItemRight" data-valign="bottom"><strong>DECLARE_DBUS_NAME_CHECK</strong> (member)</td>
</tr>
<tr class="memdesc:gabc341dacc35d8243ed6350646bf8e685">
<td class="mdescLeft"> </td>
<td class="mdescRight">defines _dbus_check_is_valid_member()<br />
</td>
</tr>
<tr class="separator:gabc341dacc35d8243ed6350646bf8e685">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac396456d8607c59950426c253f7f2b06" class="memitem:gac396456d8607c59950426c253f7f2b06">
<td class="memItemLeft" style="text-align: right;" data-valign="top">  </td>
<td class="memItemRight" data-valign="bottom"><strong>DECLARE_DBUS_NAME_CHECK</strong> (error_name)</td>
</tr>
<tr class="memdesc:gac396456d8607c59950426c253f7f2b06">
<td class="mdescLeft"> </td>
<td class="mdescRight">defines _dbus_check_is_valid_error_name()<br />
</td>
</tr>
<tr class="separator:gac396456d8607c59950426c253f7f2b06">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1389b299c4eeeb226d819c0c97d51e5b" class="memitem:ga1389b299c4eeeb226d819c0c97d51e5b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">  </td>
<td class="memItemRight" data-valign="bottom"><strong>DECLARE_DBUS_NAME_CHECK</strong> (bus_name)</td>
</tr>
<tr class="memdesc:ga1389b299c4eeeb226d819c0c97d51e5b">
<td class="mdescLeft"> </td>
<td class="mdescRight">defines _dbus_check_is_valid_bus_name()<br />
</td>
</tr>
<tr class="separator:ga1389b299c4eeeb226d819c0c97d51e5b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaef0b21f97857a0333d84b84f4d98a7da" class="memitem:gaef0b21f97857a0333d84b84f4d98a7da">
<td class="memItemLeft" style="text-align: right;" data-valign="top">  </td>
<td class="memItemRight" data-valign="bottom"><strong>DECLARE_DBUS_NAME_CHECK</strong> (utf8)</td>
</tr>
<tr class="memdesc:gaef0b21f97857a0333d84b84f4d98a7da">
<td class="mdescLeft"> </td>
<td class="mdescRight">defines _dbus_check_is_valid_utf8()<br />
</td>
</tr>
<tr class="separator:gaef0b21f97857a0333d84b84f4d98a7da">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

functions to marshal/unmarshal data from the wire

Types and functions related to converting primitive data types from wire format to native machine format, and vice versa.

A signature is just a string with multiple types one after the other. for example a type is "i" or "(ii)", a signature is "i(ii)" where i is int and (ii) is struct { int; int; }

## Macro Definition Documentation

## ◆ \_dbus_validate_utf8

|  |  |  |  |
|----|----|----|----|
| \#define \_dbus_validate_utf8 | ( |   | s, |
|  |  |   | b, |
|  |  |   | e  |
|  | ) |  |    \_dbus_string_validate_utf8 (s, b, e) |

Definition at line 163 of file dbus-marshal-validate.h.

## ◆ ARRAY_READER_LEN_POS

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| \#define ARRAY_READER_LEN_POS | ( |   | reader | ) |     ((reader)-\>u.array.start_pos - ((int)(reader)-\>array_len_offset) - 4) |

compute position of array length given array_len_offset, which is the offset back from start_pos to end of the len

Definition at line 216 of file dbus-marshal-recursive.c.

## ◆ BODY_LENGTH_OFFSET

|                                 |
|---------------------------------|
| \#define BODY_LENGTH_OFFSET   4 |

Offset to body length from start of header.

Definition at line 63 of file dbus-marshal-header.c.

## ◆ BYTE_ORDER_OFFSET

|                                |
|--------------------------------|
| \#define BYTE_ORDER_OFFSET   0 |

Offset to byte order from start of header.

Definition at line 55 of file dbus-marshal-header.c.

## ◆ DECLARE_DBUS_NAME_CHECK

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| \#define DECLARE_DBUS_NAME_CHECK | ( |   | what | ) |    dbus_bool_t \_dbus_check_is_valid\_##what (const char \*name) |

A name check is used in \_dbus_return_if_fail(), it's not suitable for validating untrusted data.

use \_dbus_validate_whatever for that.

Definition at line 178 of file dbus-marshal-validate.h.

## ◆ DEFINE_DBUS_NAME_CHECK

|                                 |     |     |      |     |     |
|---------------------------------|-----|-----|------|-----|-----|
| \#define DEFINE_DBUS_NAME_CHECK | (   |     | what | )   |     |

**Value:**

dbus_bool_t \\

\_dbus_check_is_valid\_##what (const char \*name) \\

{ \\

DBusString str; \\

\\

if (name == NULL) \\

return FALSE; \\

\\

\_dbus_string_init_const (&str, name); \\

return \_dbus_validate\_##what (&str, 0, \\

\_dbus_string_get_length (&str)); \\

}

NULL

\#define NULL

A null pointer, defined appropriately for C or C++.

**Definition** dbus-macros.h:51

FALSE

\#define FALSE

Expands to "0".

**Definition** dbus-macros.h:44

\_dbus_string_get_length

int \_dbus_string_get_length(const DBusString \*str)

Gets the length of a string (not including nul termination).

**Definition** dbus-string.c:784

DBusString

**Definition** dbus-string.h:47

Define a name check to be used in \_dbus_return_if_fail() statements.

Definition at line 183 of file dbus-marshal-validate.h.

## ◆ EXPECTED_TYPE_OF_FIELD

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| \#define EXPECTED_TYPE_OF_FIELD | ( |   | field | ) |    (\_dbus_header_field_types\[field\].type) |

Macro to look up the correct type for a field.

Definition at line 93 of file dbus-marshal-header.c.

## ◆ FIELDS_ARRAY_ELEMENT_SIGNATURE_OFFSET

|                                                    |
|----------------------------------------------------|
| \#define FIELDS_ARRAY_ELEMENT_SIGNATURE_OFFSET   7 |

Offset from start of \_dbus_header_signature_str to the signature of an element of the fields array.

Definition at line 51 of file dbus-marshal-header.c.

## ◆ FIELDS_ARRAY_LENGTH_OFFSET

|                                          |
|------------------------------------------|
| \#define FIELDS_ARRAY_LENGTH_OFFSET   12 |

Offset to fields array length from start of header.

Definition at line 67 of file dbus-marshal-header.c.

## ◆ FIELDS_ARRAY_SIGNATURE_OFFSET

|                                            |
|--------------------------------------------|
| \#define FIELDS_ARRAY_SIGNATURE_OFFSET   6 |

Offset from start of \_dbus_header_signature_str to the signature of the fields array.

Definition at line 49 of file dbus-marshal-header.c.

## ◆ FIRST_FIELD_OFFSET

|                                  |
|----------------------------------|
| \#define FIRST_FIELD_OFFSET   16 |

Offset to first field in header.

Definition at line 69 of file dbus-marshal-header.c.

## ◆ FLAGS_OFFSET

|                           |
|---------------------------|
| \#define FLAGS_OFFSET   2 |

Offset to flags from start of header.

Definition at line 59 of file dbus-marshal-header.c.

## ◆ HEADER_END_BEFORE_PADDING

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| \#define HEADER_END_BEFORE_PADDING | ( |   | header | ) |     (\_dbus_string_get_length (&(header)-\>data) - (header)-\>padding) |

Compute the end of the header, ignoring padding.

In the DBusHeader diagram, this is the distance from 0 to \[B\].

Definition at line 128 of file dbus-marshal-header.c.

## ◆ MAX_POSSIBLE_HEADER_PADDING

|                                          |
|------------------------------------------|
| \#define MAX_POSSIBLE_HEADER_PADDING   7 |

The most padding we could ever need for a header.

Definition at line 96 of file dbus-marshal-header.c.

## ◆ RECURSIVE_MARSHAL_READ_TRACE

|                                           |
|-------------------------------------------|
| \#define RECURSIVE_MARSHAL_READ_TRACE   0 |

turn this on to get deluged in TypeReader verbose spam

Definition at line 50 of file dbus-marshal-recursive.c.

## ◆ RECURSIVE_MARSHAL_WRITE_TRACE

|                                            |
|--------------------------------------------|
| \#define RECURSIVE_MARSHAL_WRITE_TRACE   0 |

turn this on to get deluged in TypeWriter verbose spam

Definition at line 53 of file dbus-marshal-recursive.c.

## ◆ SERIAL_OFFSET

|                            |
|----------------------------|
| \#define SERIAL_OFFSET   8 |

Offset to client serial from start of header.

Definition at line 65 of file dbus-marshal-header.c.

## ◆ TYPE_OFFSET

|                          |
|--------------------------|
| \#define TYPE_OFFSET   1 |

Offset to type from start of header.

Definition at line 57 of file dbus-marshal-header.c.

## ◆ VALID_BUS_NAME_CHARACTER

|                                   |     |     |     |     |     |
|-----------------------------------|-----|-----|-----|-----|-----|
| \#define VALID_BUS_NAME_CHARACTER | (   |     | c   | )   |     |

**Value:**

( ((c) \>= '0' && (c) \<= '9') \|\| \\

((c) \>= 'A' && (c) \<= 'Z') \|\| \\

((c) \>= 'a' && (c) \<= 'z') \|\| \\

((c) == '\_') \|\| ((c) == '-'))

Determine wether the given character is valid as a second or later character in a bus name.

Definition at line 1145 of file dbus-marshal-validate.c.

## ◆ VALID_INITIAL_BUS_NAME_CHARACTER

|                                           |     |     |     |     |     |
|-------------------------------------------|-----|-----|-----|-----|-----|
| \#define VALID_INITIAL_BUS_NAME_CHARACTER | (   |     | c   | )   |     |

**Value:**

( ((c) \>= 'A' && (c) \<= 'Z') \|\| \\

((c) \>= 'a' && (c) \<= 'z') \|\| \\

((c) == '\_') \|\| ((c) == '-'))

Determine wether the given character is valid as the first character in a bus name.

Definition at line 1136 of file dbus-marshal-validate.c.

## ◆ VALID_INITIAL_NAME_CHARACTER

|                                       |     |     |     |     |     |
|---------------------------------------|-----|-----|-----|-----|-----|
| \#define VALID_INITIAL_NAME_CHARACTER | (   |     | c   | )   |     |

**Value:**

( ((c) \>= 'A' && (c) \<= 'Z') \|\| \\

((c) \>= 'a' && (c) \<= 'z') \|\| \\

((c) == '\_') )

Determine wether the given character is valid as the first character in a name.

Definition at line 817 of file dbus-marshal-validate.c.

## ◆ VALID_NAME_CHARACTER

|                               |     |     |     |     |     |
|-------------------------------|-----|-----|-----|-----|-----|
| \#define VALID_NAME_CHARACTER | (   |     | c   | )   |     |

**Value:**

( ((c) \>= '0' && (c) \<= '9') \|\| \\

((c) \>= 'A' && (c) \<= 'Z') \|\| \\

((c) \>= 'a' && (c) \<= 'z') \|\| \\

((c) == '\_') )

Determine wether the given character is valid as a second or later character in a name.

Definition at line 826 of file dbus-marshal-validate.c.

## ◆ VERSION_OFFSET

|                             |
|-----------------------------|
| \#define VERSION_OFFSET   3 |

Offset to version from start of header.

Definition at line 61 of file dbus-marshal-header.c.

## Enumeration Type Documentation

## ◆ anonymous enum

|                |
|----------------|
| anonymous enum |

Definition at line 698 of file dbus-marshal-basic.c.

## ◆ DBusValidationMode

|                         |
|-------------------------|
| enum DBusValidationMode |

This is used rather than a bool for high visibility.

Definition at line 40 of file dbus-marshal-validate.h.

## ◆ DBusValidity

|                   |
|-------------------|
| enum DBusValidity |

This is primarily used in unit testing, so we can verify that each invalid message is invalid for the expected reasons.

Thus we really want a distinct enum value for every codepath leaving the validator functions. Enum values are specified manually for ease of debugging (so you can see the enum value given a printf)

| Enumerator                       |                                     |
|----------------------------------|-------------------------------------|
| DBUS_VALIDITY_UNKNOWN_OOM_ERROR  | can't determine validity due to OOM |
| DBUS_VALID                       | the data is valid                   |
| DBUS_INVALID_TOO_MUCH_DATA       | trailing junk makes it invalid      |

Definition at line 53 of file dbus-marshal-validate.h.

## Function Documentation

## ◆ \_dbus_first_type_in_signature()

|                                    |     |                      |        |
|------------------------------------|-----|----------------------|--------|
| int \_dbus_first_type_in_signature | (   | const DBusString \*  | *str*, |
|                                    |     | int                  | *pos*  |
|                                    | )   |                      |        |

Get the first type in the signature.

The difference between this and just getting the first byte of the signature is that you won't get DBUS_STRUCT_BEGIN_CHAR, you'll get DBUS_TYPE_STRUCT instead.

Parameters  
|     |                             |
|-----|-----------------------------|
| str | string containing signature |
| pos | where the signature starts  |

<!-- -->

Returns  
the first type in the signature

Definition at line 1484 of file dbus-marshal-basic.c.

References \_dbus_string_get_byte().

Referenced by \_dbus_type_reader_get_current_type(), \_dbus_type_reader_get_element_type(), \_dbus_type_reader_read_fixed_multi(), and \_dbus_type_reader_recurse().

## ◆ \_dbus_first_type_in_signature_c_str()

|                                          |     |                |        |
|------------------------------------------|-----|----------------|--------|
| int \_dbus_first_type_in_signature_c_str | (   | const char \*  | *str*, |
|                                          |     | int            | *pos*  |
|                                          | )   |                |        |

Similar to \_dbus_first_type_in_signature, but operates on a C string buffer.

Parameters  
|     |                            |
|-----|----------------------------|
| str | a C string buffer          |
| pos | where the signature starts |

<!-- -->

Returns  
the first type in the signature

Definition at line 1499 of file dbus-marshal-basic.c.

Referenced by dbus_signature_iter_get_current_type(), and dbus_signature_iter_get_element_type().

## ◆ \_dbus_header_byteswap()

|                             |     |                |              |
|-----------------------------|-----|----------------|--------------|
| void \_dbus_header_byteswap | (   | DBusHeader \*  | *header*,    |
|                             |     | int            | *new_order*  |
|                             | )   |                |              |

Swaps the header into the given order if required.

Parameters  
|           |                    |
|-----------|--------------------|
| header    | the header         |
| new_order | the new byte order |

Definition at line 1507 of file dbus-marshal-header.c.

References \_dbus_header_get_byte_order(), \_dbus_marshal_byteswap(), \_dbus_string_set_byte(), BYTE_ORDER_OFFSET, and DBusHeader::data.

## ◆ \_dbus_header_copy()

|                                |     |                      |           |
|--------------------------------|-----|----------------------|-----------|
| dbus_bool_t \_dbus_header_copy | (   | const DBusHeader \*  | *header*, |
|                                |     | DBusHeader \*        | *dest*    |
|                                | )   |                      |           |

Initializes dest with a copy of the given header.

Resets the message serial to 0 on the copy.

Parameters  
|        |                      |
|--------|----------------------|
| header | header to copy       |
| dest   | destination for copy |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 495 of file dbus-marshal-header.c.

References \_dbus_header_set_serial(), \_dbus_string_copy(), \_dbus_string_free(), \_dbus_string_get_length(), \_dbus_string_init_preallocated(), DBusHeader::data, FALSE, and TRUE.

Referenced by dbus_message_copy().

## ◆ \_dbus_header_create()

|                                  |     |                |                 |
|----------------------------------|-----|----------------|-----------------|
| dbus_bool_t \_dbus_header_create | (   | DBusHeader \*  | *header*,       |
|                                  |     | int            | *byte_order*,   |
|                                  |     | int            | *message_type*, |
|                                  |     | const char \*  | *destination*,  |
|                                  |     | const char \*  | *path*,         |
|                                  |     | const char \*  | *interface*,    |
|                                  |     | const char \*  | *member*,       |
|                                  |     | const char \*  | *error_name*    |
|                                  | )   |                |                 |

Fills in the primary fields of the header, so the header is ready for use.

NULL may be specified for some or all of the fields to avoid adding those fields. Some combinations of fields don't make sense, and passing them in will trigger an assertion failure.

Parameters  
|              |                           |
|--------------|---------------------------|
| header       | the header                |
| byte_order   | byte order of the header  |
| message_type | the message type          |
| destination  | destination field or NULL |
| path         | path field or NULL        |
| interface    | interface field or NULL   |
| member       | member field or NULL      |
| error_name   | error name or NULL        |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 533 of file dbus-marshal-header.c.

References \_dbus_assert, \_dbus_string_delete(), \_dbus_string_get_length(), \_dbus_type_writer_init_values_only(), \_dbus_type_writer_recurse(), \_dbus_type_writer_unrecurse(), \_dbus_type_writer_write_basic(), DBusHeader::data, DBUS_BIG_ENDIAN, DBUS_HEADER_FIELD_DESTINATION, DBUS_HEADER_FIELD_ERROR_NAME, DBUS_HEADER_FIELD_INTERFACE, DBUS_HEADER_FIELD_MEMBER, DBUS_HEADER_FIELD_PATH, DBUS_LITTLE_ENDIAN, DBUS_MAJOR_PROTOCOL_VERSION, DBUS_MESSAGE_TYPE_SIGNAL, DBUS_TYPE_ARRAY, DBUS_TYPE_BYTE, DBUS_TYPE_OBJECT_PATH, DBUS_TYPE_STRING, DBUS_TYPE_UINT32, FALSE, FIELDS_ARRAY_SIGNATURE_OFFSET, HEADER_END_BEFORE_PADDING, NULL, DBusHeader::padding, and TRUE.

Referenced by dbus_message_new(), dbus_message_new_error(), dbus_message_new_method_call(), dbus_message_new_method_return(), and dbus_message_new_signal().

## ◆ \_dbus_header_delete_field()

|                                        |     |                |           |
|----------------------------------------|-----|----------------|-----------|
| dbus_bool_t \_dbus_header_delete_field | (   | DBusHeader \*  | *header*, |
|                                        |     | int            | *field*   |
|                                        | )   |                |           |

Deletes a field, if it exists.

Parameters  
|        |                     |
|--------|---------------------|
| header | the header          |
| field  | the field to delete |

<!-- -->

Returns  
FALSE if no memory

Definition at line 1427 of file dbus-marshal-header.c.

References \_dbus_assert, \_dbus_type_reader_delete(), FALSE, and TRUE.

## ◆ \_dbus_header_free()

|                         |     |                |          |     |     |
|-------------------------|-----|----------------|----------|-----|-----|
| void \_dbus_header_free | (   | DBusHeader \*  | *header* | )   |     |

Frees a header.

Parameters  
|        |            |
|--------|------------|
| header | the header |

Definition at line 481 of file dbus-marshal-header.c.

References \_dbus_string_free(), and DBusHeader::data.

Referenced by dbus_message_copy().

## ◆ \_dbus_header_get_byte_order()

|                                   |     |                      |          |     |     |
|-----------------------------------|-----|----------------------|----------|-----|-----|
| char \_dbus_header_get_byte_order | (   | const DBusHeader \*  | *header* | )   |     |

Returns the header's byte order.

Parameters  
|        |            |
|--------|------------|
| header | the header |

<!-- -->

Returns  
the byte order

Definition at line 179 of file dbus-marshal-header.c.

References \_dbus_assert, \_dbus_string_get_byte(), \_dbus_string_get_length(), BYTE_ORDER_OFFSET, and DBusHeader::data.

Referenced by \_dbus_header_byteswap(), \_dbus_header_get_field_basic(), \_dbus_header_get_serial(), \_dbus_header_remove_unknown_fields(), \_dbus_header_set_field_basic(), \_dbus_header_set_serial(), \_dbus_header_update_lengths(), dbus_message_iter_init(), and dbus_message_iter_init_append().

## ◆ \_dbus_header_get_field_basic()

|                                           |     |                |           |
|-------------------------------------------|-----|----------------|-----------|
| dbus_bool_t \_dbus_header_get_field_basic | (   | DBusHeader \*  | *header*, |
|                                           |     | int            | *field*,  |
|                                           |     | int            | *type*,   |
|                                           |     | void \*        | *value*   |
|                                           | )   |                |           |

Gets the value of a field with basic type.

If the field doesn't exist, returns FALSE, otherwise returns TRUE.

Parameters  
|        |                                              |
|--------|----------------------------------------------|
| header | the header                                   |
| field  | the field to get                             |
| type   | the type of the value                        |
| value  | the value as for \_dbus_marshal_read_basic() |

<!-- -->

Returns  
FALSE if the field doesn't exist

Definition at line 1362 of file dbus-marshal-header.c.

References \_dbus_assert, \_dbus_header_get_byte_order(), \_dbus_marshal_read_basic(), DBusHeader::data, DBUS_HEADER_FIELD_INVALID, DBUS_HEADER_FIELD_LAST, EXPECTED_TYPE_OF_FIELD, FALSE, DBusHeader::fields, NULL, TRUE, and DBusHeaderField::value_pos.

Referenced by dbus_message_get_container_instance(), dbus_message_get_destination(), dbus_message_get_error_name(), dbus_message_get_interface(), dbus_message_get_member(), dbus_message_get_path(), dbus_message_get_reply_serial(), and dbus_message_get_sender().

## ◆ \_dbus_header_get_field_raw()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_header_get_field_raw | ( | DBusHeader \*  | *header*, |
|  |  | int  | *field*, |
|  |  | const DBusString \*\*  | *str*, |
|  |  | int \*  | *pos*  |
|  | ) |  |  |

Gets the raw marshaled data for a field.

If the field doesn't exist, returns FALSE, otherwise returns TRUE. Returns the start of the marshaled data, i.e. usually the byte where the length starts (for strings and arrays) or for basic types just the value itself.

Parameters  
|        |                                          |
|--------|------------------------------------------|
| header | the header                               |
| field  | the field to get                         |
| str    | return location for the data string      |
| pos    | return location for start of field value |

<!-- -->

Returns  
FALSE if the field doesn't exist

Definition at line 1403 of file dbus-marshal-header.c.

References DBusHeader::data, FALSE, DBusHeader::fields, TRUE, and DBusHeaderField::value_pos.

## ◆ \_dbus_header_get_flag()

|                                    |     |                |           |
|------------------------------------|-----|----------------|-----------|
| dbus_bool_t \_dbus_header_get_flag | (   | DBusHeader \*  | *header*, |
|                                    |     | dbus_uint32_t  | *flag*    |
|                                    | )   |                |           |

Gets a message flag bit, returning TRUE if the bit is set.

Parameters  
|        |                         |
|--------|-------------------------|
| header | the header              |
| flag   | the message flag to get |

<!-- -->

Returns  
TRUE if the flag is set

Definition at line 1490 of file dbus-marshal-header.c.

References DBusHeader::data, and FLAGS_OFFSET.

Referenced by dbus_message_get_allow_interactive_authorization(), dbus_message_get_auto_start(), and dbus_message_get_no_reply().

## ◆ \_dbus_header_get_message_type()

|                                    |     |                |          |     |     |
|------------------------------------|-----|----------------|----------|-----|-----|
| int \_dbus_header_get_message_type | (   | DBusHeader \*  | *header* | )   |     |

Gets the type of the message.

Parameters  
|        |            |
|--------|------------|
| header | the header |

<!-- -->

Returns  
the type

Definition at line 391 of file dbus-marshal-header.c.

References \_dbus_assert, \_dbus_string_get_byte(), DBusHeader::data, DBUS_MESSAGE_TYPE_INVALID, and TYPE_OFFSET.

Referenced by dbus_message_get_type().

## ◆ \_dbus_header_get_serial()

|                                        |     |                |          |     |     |
|----------------------------------------|-----|----------------|----------|-----|-----|
| dbus_uint32_t \_dbus_header_get_serial | (   | DBusHeader \*  | *header* | )   |     |

See dbus_message_get_serial()

Parameters  
|        |            |
|--------|------------|
| header | the header |

<!-- -->

Returns  
the client serial

Definition at line 432 of file dbus-marshal-header.c.

References \_dbus_header_get_byte_order(), \_dbus_marshal_read_uint32(), DBusHeader::data, NULL, and SERIAL_OFFSET.

Referenced by \_dbus_header_set_serial(), and dbus_message_get_serial().

## ◆ \_dbus_header_have_message_untrusted()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_header_have_message_untrusted | ( | int  | *max_message_length*, |
|  |  | DBusValidity \*  | *validity*, |
|  |  | int \*  | *byte_order*, |
|  |  | int \*  | *fields_array_len*, |
|  |  | int \*  | *header_len*, |
|  |  | int \*  | *body_len*, |
|  |  | const DBusString \*  | *str*, |
|  |  | int  | *start*, |
|  |  | int  | *len*  |
|  | ) |  |  |

Given data long enough to contain the length of the message body and the fields array, check whether the data is long enough to contain the entire message (assuming the claimed lengths are accurate).

Also checks that the lengths are in sanity parameters.

Parameters  
|                    |                                                      |
|--------------------|------------------------------------------------------|
| max_message_length | maximum length of a valid message                    |
| validity           | return location for why the data is invalid if it is |
| byte_order         | return location for byte order                       |
| fields_array_len   | return location for claimed fields array length      |
| header_len         | return location for claimed header length            |
| body_len           | return location for claimed body length              |
| str                | the data                                             |
| start              | start of data, 8-aligned                             |
| len                | length of data                                       |

<!-- -->

Returns  
TRUE if the data is long enough for the claimed length, and the lengths were valid

Definition at line 681 of file dbus-marshal-header.c.

References \_dbus_assert, \_DBUS_INT32_MAX, \_dbus_marshal_read_uint32(), \_dbus_string_get_byte(), BODY_LENGTH_OFFSET, BYTE_ORDER_OFFSET, DBUS_BIG_ENDIAN, DBUS_LITTLE_ENDIAN, DBUS_VALID, FALSE, FIELDS_ARRAY_LENGTH_OFFSET, FIRST_FIELD_OFFSET, and NULL.

Referenced by \_dbus_message_loader_get_buffer(), \_dbus_message_loader_queue_messages(), and dbus_message_demarshal_bytes_needed().

## ◆ \_dbus_header_init()

|                                |     |                |          |     |     |
|--------------------------------|-----|----------------|----------|-----|-----|
| dbus_bool_t \_dbus_header_init | (   | DBusHeader \*  | *header* | )   |     |

Initializes a header, but doesn't prepare it for use; to make the header valid, you have to call \_dbus_header_create().

Parameters  
|        |                      |
|--------|----------------------|
| header | header to initialize |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 465 of file dbus-marshal-header.c.

References \_dbus_header_reinit(), \_dbus_string_init_preallocated(), DBusHeader::data, FALSE, and TRUE.

## ◆ \_dbus_header_load()

|                                |     |                      |                     |
|--------------------------------|-----|----------------------|---------------------|
| dbus_bool_t \_dbus_header_load | (   | DBusHeader \*        | *header*,           |
|                                |     | DBusValidationMode   | *mode*,             |
|                                |     | DBusValidity \*      | *validity*,         |
|                                |     | int                  | *byte_order*,       |
|                                |     | int                  | *fields_array_len*, |
|                                |     | int                  | *header_len*,       |
|                                |     | int                  | *body_len*,         |
|                                |     | const DBusString \*  | *str*               |
|                                | )   |                      |                     |

Creates a message header from potentially-untrusted data.

The return value is TRUE if there was enough memory and the data was valid. If it returns TRUE, the header will be created. If it returns FALSE and \*validity == DBUS_VALIDITY_UNKNOWN_OOM_ERROR, then there wasn't enough memory. If it returns FALSE and \*validity != DBUS_VALIDITY_UNKNOWN_OOM_ERROR then the data was invalid.

The byte_order, fields_array_len, and body_len args should be from \_dbus_header_have_message_untrusted(). Validation performed in \_dbus_header_have_message_untrusted() is assumed to have been already done.

Parameters  
|                  |                                       |
|------------------|---------------------------------------|
| header           | the header (must be initialized)      |
| mode             | whether to do validation              |
| validity         | return location for invalidity reason |
| byte_order       | byte order from header                |
| fields_array_len | claimed length of fields array        |
| body_len         | claimed length of body                |
| header_len       | claimed length of header              |
| str              | a string starting with the header     |

<!-- -->

Returns  
FALSE if no memory or data was invalid, TRUE otherwise

Definition at line 981 of file dbus-marshal-header.c.

References \_dbus_assert, \_dbus_string_copy_len(), \_dbus_string_get_length(), \_dbus_string_set_length(), \_dbus_string_validate_nul(), \_dbus_type_reader_get_current_type(), \_dbus_type_reader_get_value_pos(), \_dbus_type_reader_init(), \_dbus_type_reader_next(), \_dbus_type_reader_read_basic(), \_dbus_type_reader_recurse(), \_dbus_validate_body_with_reason(), BODY_LENGTH_OFFSET, BYTE_ORDER_OFFSET, DBusHeader::data, DBUS_HEADER_FIELD_INVALID, DBUS_HEADER_FIELD_LAST, DBUS_MAJOR_PROTOCOL_VERSION, DBUS_MESSAGE_TYPE_INVALID, DBUS_TYPE_ARRAY, DBUS_TYPE_BYTE, DBUS_TYPE_INVALID, DBUS_TYPE_STRUCT, DBUS_TYPE_UINT32, DBUS_TYPE_VARIANT, DBUS_VALID, DBUS_VALIDITY_UNKNOWN_OOM_ERROR, FALSE, DBusHeader::fields, FIELDS_ARRAY_LENGTH_OFFSET, FIRST_FIELD_OFFSET, FLAGS_OFFSET, DBusHeader::padding, SERIAL_OFFSET, TRUE, TYPE_OFFSET, DBusHeaderField::value_pos, and VERSION_OFFSET.

## ◆ \_dbus_header_reinit()

|                           |     |                |          |     |     |
|---------------------------|-----|----------------|----------|-----|-----|
| void \_dbus_header_reinit | (   | DBusHeader \*  | *header* | )   |     |

Re-initializes a header that was previously initialized and never freed.

After this, to make the header valid you have to call \_dbus_header_create().

Parameters  
|        |                         |
|--------|-------------------------|
| header | header to re-initialize |

Definition at line 448 of file dbus-marshal-header.c.

References \_dbus_string_set_length(), DBusHeader::data, and DBusHeader::padding.

Referenced by \_dbus_header_init().

## ◆ \_dbus_header_remove_unknown_fields()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_header_remove_unknown_fields | ( | DBusHeader \*  | *header* | ) |  |

Remove every header field not known to this version of dbus.

Parameters  
|        |            |
|--------|------------|
| header | the header |

<!-- -->

Returns  
FALSE if no memory

Definition at line 1532 of file dbus-marshal-header.c.

References \_dbus_assert, \_dbus_header_get_byte_order(), \_dbus_type_reader_delete(), \_dbus_type_reader_get_current_type(), \_dbus_type_reader_init(), \_dbus_type_reader_next(), \_dbus_type_reader_read_basic(), \_dbus_type_reader_recurse(), DBusHeader::data, DBUS_HEADER_FIELD_LAST, DBUS_TYPE_BYTE, DBUS_TYPE_INVALID, FALSE, FIELDS_ARRAY_LENGTH_OFFSET, FIELDS_ARRAY_SIGNATURE_OFFSET, and TRUE.

Referenced by \_dbus_message_remove_unknown_fields().

## ◆ \_dbus_header_set_field_basic()

|                                           |     |                |           |
|-------------------------------------------|-----|----------------|-----------|
| dbus_bool_t \_dbus_header_set_field_basic | (   | DBusHeader \*  | *header*, |
|                                           |     | int            | *field*,  |
|                                           |     | int            | *type*,   |
|                                           |     | const void \*  | *value*   |
|                                           | )   |                |           |

Sets the value of a field with basic type.

If the value is a string value, it isn't allowed to be NULL. If the field doesn't exist, it will be created.

Parameters  
|        |                                             |
|--------|---------------------------------------------|
| header | the header                                  |
| field  | the field to set                            |
| type   | the type of the value                       |
| value  | the value as for \_dbus_marshal_set_basic() |

<!-- -->

Returns  
FALSE if no memory

Definition at line 1284 of file dbus-marshal-header.c.

References \_dbus_assert, \_dbus_assert_not_reached, \_dbus_header_get_byte_order(), \_dbus_type_writer_append_array(), \_dbus_type_writer_init_values_only(), \_dbus_type_writer_unrecurse(), DBusHeader::data, DBUS_HEADER_FIELD_LAST, FALSE, FIELDS_ARRAY_ELEMENT_SIGNATURE_OFFSET, FIELDS_ARRAY_LENGTH_OFFSET, FIELDS_ARRAY_SIGNATURE_OFFSET, FIRST_FIELD_OFFSET, HEADER_END_BEFORE_PADDING, DBusTypeWriter::len_pos, DBusTypeWriter::start_pos, TRUE, DBusTypeWriter::u, and DBusTypeWriter::value_pos.

Referenced by dbus_message_iter_append_basic(), and dbus_message_set_reply_serial().

## ◆ \_dbus_header_set_serial()

|                               |     |                |           |
|-------------------------------|-----|----------------|-----------|
| void \_dbus_header_set_serial | (   | DBusHeader \*  | *header*, |
|                               |     | dbus_uint32_t  | *serial*  |
|                               | )   |                |           |

Sets the serial number of a header.

This can only be done once on a header.

Parameters  
|        |            |
|--------|------------|
| header | the header |
| serial | the serial |

Definition at line 409 of file dbus-marshal-header.c.

References \_dbus_assert, \_dbus_header_get_byte_order(), \_dbus_header_get_serial(), \_dbus_marshal_set_uint32(), DBusHeader::data, and SERIAL_OFFSET.

Referenced by \_dbus_header_copy(), and dbus_message_set_serial().

## ◆ \_dbus_header_toggle_flag()

|                                |     |                |           |
|--------------------------------|-----|----------------|-----------|
| void \_dbus_header_toggle_flag | (   | DBusHeader \*  | *header*, |
|                                |     | dbus_uint32_t  | *flag*,   |
|                                |     | dbus_bool_t    | *value*   |
|                                | )   |                |           |

Toggles a message flag bit, turning on the bit if value = TRUE and flipping it off if value = FALSE.

Parameters  
|        |                            |
|--------|----------------------------|
| header | the header                 |
| flag   | the message flag to toggle |
| value  | toggle on or off           |

Definition at line 1468 of file dbus-marshal-header.c.

References DBusHeader::data, and FLAGS_OFFSET.

Referenced by dbus_message_set_allow_interactive_authorization(), dbus_message_set_auto_start(), and dbus_message_set_no_reply().

## ◆ \_dbus_header_update_lengths()

|                                   |     |                |             |
|-----------------------------------|-----|----------------|-------------|
| void \_dbus_header_update_lengths | (   | DBusHeader \*  | *header*,   |
|                                   |     | int            | *body_len*  |
|                                   | )   |                |             |

Fills in the correct body length.

Parameters  
|          |                        |
|----------|------------------------|
| header   | the header             |
| body_len | the length of the body |

Definition at line 1207 of file dbus-marshal-header.c.

References \_dbus_header_get_byte_order(), \_dbus_marshal_set_uint32(), BODY_LENGTH_OFFSET, and DBusHeader::data.

Referenced by dbus_message_lock().

## ◆ \_dbus_marshal_byteswap()

|                              |     |                      |                    |
|------------------------------|-----|----------------------|--------------------|
| void \_dbus_marshal_byteswap | (   | const DBusString \*  | *signature*,       |
|                              |     | int                  | *signature_start*, |
|                              |     | int                  | *old_byte_order*,  |
|                              |     | int                  | *new_byte_order*,  |
|                              |     | DBusString \*        | *value_str*,       |
|                              |     | int                  | *value_pos*        |
|                              | )   |                      |                    |

Byteswaps the marshaled data in the given value_str.

Parameters  
|                 |                                     |
|-----------------|-------------------------------------|
| signature       | the types in the value_str          |
| signature_start | where in signature is the signature |
| old_byte_order  | the old byte order                  |
| new_byte_order  | the new byte order                  |
| value_str       | the string containing the body      |
| value_pos       | where the values start              |

Definition at line 224 of file dbus-marshal-byteswap.c.

References \_dbus_assert, \_dbus_string_get_length(), \_dbus_type_reader_init_types_only(), NULL, and TRUE.

Referenced by \_dbus_header_byteswap().

## ◆ \_dbus_marshal_read_basic()

|                                |     |                      |               |
|--------------------------------|-----|----------------------|---------------|
| void \_dbus_marshal_read_basic | (   | const DBusString \*  | *str*,        |
|                                |     | int                  | *pos*,        |
|                                |     | int                  | *type*,       |
|                                |     | void \*              | *value*,      |
|                                |     | int                  | *byte_order*, |
|                                |     | int \*               | *new_pos*     |
|                                | )   |                      |               |

Demarshals a basic-typed value.

The "value" pointer is always the address of a variable of the basic type. So e.g. if the basic type is "double" then the pointer is a double\*, and if it's "char\*" then the pointer is a "char\*\*".

A value of type DBusBasicValue is guaranteed to be large enough to hold any of the types that may be returned, which is handy if you are trying to do things generically. For example you can pass a DBusBasicValue\* in to this function, and then pass the same DBusBasicValue\* in to \_dbus_marshal_basic_type() in order to move a value from one place to another.

Parameters  
|            |                                              |
|------------|----------------------------------------------|
| str        | the string containing the data               |
| pos        | position in the string                       |
| type       | type of value to demarshal                   |
| value      | pointer to return value data                 |
| byte_order | the byte order                               |
| new_pos    | pointer to update with new position, or NULL |

Definition at line 514 of file dbus-marshal-basic.c.

References \_dbus_assert, \_dbus_assert_not_reached, \_dbus_marshal_read_uint32(), \_dbus_string_get_byte(), \_dbus_string_get_const_data(), \_dbus_type_to_string(), \_dbus_warn_check_failed(), DBUS_TYPE_BOOLEAN, DBUS_TYPE_BYTE, DBUS_TYPE_DOUBLE, DBUS_TYPE_INT16, DBUS_TYPE_INT32, DBUS_TYPE_INT64, dbus_type_is_basic(), DBUS_TYPE_OBJECT_PATH, DBUS_TYPE_SIGNATURE, DBUS_TYPE_STRING, DBUS_TYPE_UINT16, DBUS_TYPE_UINT32, DBUS_TYPE_UINT64, and DBUS_TYPE_UNIX_FD.

Referenced by \_dbus_header_get_field_basic(), and \_dbus_type_reader_read_basic().

## ◆ \_dbus_marshal_read_uint32()

|  |  |  |  |
|----|----|----|----|
| dbus_uint32_t \_dbus_marshal_read_uint32 | ( | const DBusString \*  | *str*, |
|  |  | int  | *pos*, |
|  |  | int  | *byte_order*, |
|  |  | int \*  | *new_pos*  |
|  | ) |  |  |

Convenience function to demarshal a 32 bit unsigned integer.

Parameters  
|            |                                |
|------------|--------------------------------|
| str        | the string containing the data |
| byte_order | the byte order                 |
| pos        | the position in the string     |
| new_pos    | the new position of the string |

<!-- -->

Returns  
the demarshaled integer.

Definition at line 476 of file dbus-marshal-basic.c.

References \_dbus_assert, \_dbus_string_get_length(), and \_dbus_unpack_uint32().

Referenced by \_dbus_header_get_serial(), \_dbus_header_have_message_untrusted(), \_dbus_marshal_read_basic(), \_dbus_marshal_skip_array(), and \_dbus_marshal_skip_basic().

## ◆ \_dbus_marshal_set_basic()

|                                      |     |                |                |
|--------------------------------------|-----|----------------|----------------|
| dbus_bool_t \_dbus_marshal_set_basic | (   | DBusString \*  | *str*,         |
|                                      |     | int            | *pos*,         |
|                                      |     | int            | *type*,        |
|                                      |     | const void \*  | *value*,       |
|                                      |     | int            | *byte_order*,  |
|                                      |     | int \*         | *old_end_pos*, |
|                                      |     | int \*         | *new_end_pos*  |
|                                      | )   |                |                |

Sets an existing basic type value to a new value.

Arguments work the same way as \_dbus_marshal_basic_type().

Parameters  
|             |                                                          |
|-------------|----------------------------------------------------------|
| str         | the string                                               |
| pos         | location of the current value                            |
| type        | the type of the current and new values                   |
| value       | the address of the new value                             |
| byte_order  | byte order for marshaling                                |
| old_end_pos | location to store end position of the old value, or NULL |
| new_end_pos | location to store end position of the new value, or NULL |

<!-- -->

Returns  
FALSE if no memory

Definition at line 377 of file dbus-marshal-basic.c.

References \_dbus_assert, \_dbus_assert_not_reached, \_dbus_string_set_byte(), DBUS_TYPE_BOOLEAN, DBUS_TYPE_BYTE, DBUS_TYPE_DOUBLE, DBUS_TYPE_INT16, DBUS_TYPE_INT32, DBUS_TYPE_INT64, DBUS_TYPE_OBJECT_PATH, DBUS_TYPE_SIGNATURE, DBUS_TYPE_STRING, DBUS_TYPE_UINT16, DBUS_TYPE_UINT32, DBUS_TYPE_UINT64, DBUS_TYPE_UNIX_FD, FALSE, NULL, and TRUE.

## ◆ \_dbus_marshal_set_uint32()

|                                |     |                |               |
|--------------------------------|-----|----------------|---------------|
| void \_dbus_marshal_set_uint32 | (   | DBusString \*  | *str*,        |
|                                |     | int            | *pos*,        |
|                                |     | dbus_uint32_t  | *value*,      |
|                                |     | int            | *byte_order*  |
|                                | )   |                |               |

Sets the 4 bytes at the given offset to a marshaled unsigned integer, replacing anything found there previously.

Parameters  
|            |                                             |
|------------|---------------------------------------------|
| str        | the string to write the marshalled int to   |
| pos        | the byte offset where int should be written |
| value      | the value                                   |
| byte_order | the byte order to use                       |

Definition at line 260 of file dbus-marshal-basic.c.

Referenced by \_dbus_header_set_serial(), \_dbus_header_update_lengths(), and \_dbus_type_writer_unrecurse().

## ◆ \_dbus_marshal_skip_array()

|                                |     |                      |                 |
|--------------------------------|-----|----------------------|-----------------|
| void \_dbus_marshal_skip_array | (   | const DBusString \*  | *str*,          |
|                                |     | int                  | *element_type*, |
|                                |     | int                  | *byte_order*,   |
|                                |     | int \*               | *pos*           |
|                                | )   |                      |                 |

Skips an array, returning the next position.

Parameters  
|  |  |
|----|----|
| str | the string containing the data |
| element_type | the type of array elements |
| byte_order | the byte order |
| pos | pointer to position in the string, updated on return to new position |

Definition at line 1205 of file dbus-marshal-basic.c.

References \_dbus_assert, \_dbus_marshal_read_uint32(), \_dbus_string_get_length(), and \_dbus_type_get_alignment().

## ◆ \_dbus_marshal_skip_basic()

|                                |     |                      |               |
|--------------------------------|-----|----------------------|---------------|
| void \_dbus_marshal_skip_basic | (   | const DBusString \*  | *str*,        |
|                                |     | int                  | *type*,       |
|                                |     | int                  | *byte_order*, |
|                                |     | int \*               | *pos*         |
|                                | )   |                      |               |

Skips over a basic-typed value, reporting the following position.

Parameters  
|  |  |
|----|----|
| str | the string containing the data |
| type | type of value to read |
| byte_order | the byte order |
| pos | pointer to position in the string, updated on return to new position |

Definition at line 1130 of file dbus-marshal-basic.c.

References \_dbus_assert, \_dbus_assert_not_reached, \_dbus_marshal_read_uint32(), \_dbus_string_get_byte(), \_dbus_string_get_length(), \_dbus_type_to_string(), \_dbus_warn(), DBUS_BIG_ENDIAN, DBUS_LITTLE_ENDIAN, DBUS_TYPE_BOOLEAN, DBUS_TYPE_BYTE, DBUS_TYPE_DOUBLE, DBUS_TYPE_INT16, DBUS_TYPE_INT32, DBUS_TYPE_INT64, DBUS_TYPE_OBJECT_PATH, DBUS_TYPE_SIGNATURE, DBUS_TYPE_STRING, DBUS_TYPE_UINT16, DBUS_TYPE_UINT32, DBUS_TYPE_UINT64, and DBUS_TYPE_UNIX_FD.

## ◆ \_dbus_marshal_write_basic()

|                                        |     |                |               |
|----------------------------------------|-----|----------------|---------------|
| dbus_bool_t \_dbus_marshal_write_basic | (   | DBusString \*  | *str*,        |
|                                        |     | int            | *insert_at*,  |
|                                        |     | int            | *type*,       |
|                                        |     | const void \*  | *value*,      |
|                                        |     | int            | *byte_order*, |
|                                        |     | int \*         | *pos_after*   |
|                                        | )   |                |               |

Marshals a basic-typed value.

The "value" pointer is always the address of a variable containing the basic type value. So for example for int32 it will be dbus_int32_t\*, and for string it will be const char\*\*. This is for symmetry with \_dbus_marshal_read_basic() and to have a simple consistent rule.

Parameters  
|            |                                            |
|------------|--------------------------------------------|
| str        | string to marshal to                       |
| insert_at  | where to insert the value                  |
| type       | type of value                              |
| value      | pointer to a variable containing the value |
| byte_order | byte order                                 |
| pos_after  | NULL or the position after the type        |

<!-- -->

Returns  
TRUE on success

Definition at line 817 of file dbus-marshal-basic.c.

References \_dbus_assert, \_dbus_assert_not_reached, \_dbus_string_insert_byte(), DBUS_TYPE_BOOLEAN, DBUS_TYPE_BYTE, DBUS_TYPE_DOUBLE, DBUS_TYPE_INT16, DBUS_TYPE_INT32, DBUS_TYPE_INT64, dbus_type_is_basic(), DBUS_TYPE_OBJECT_PATH, DBUS_TYPE_SIGNATURE, DBUS_TYPE_STRING, DBUS_TYPE_UINT16, DBUS_TYPE_UINT32, DBUS_TYPE_UINT64, DBUS_TYPE_UNIX_FD, FALSE, NULL, and TRUE.

## ◆ \_dbus_marshal_write_fixed_multi()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_marshal_write_fixed_multi | ( | DBusString \*  | *str*, |
|  |  | int  | *insert_at*, |
|  |  | int  | *element_type*, |
|  |  | const void \*  | *value*, |
|  |  | int  | *n_elements*, |
|  |  | int  | *byte_order*, |
|  |  | int \*  | *pos_after*  |
|  | ) |  |  |

Marshals a block of values of fixed-length type all at once, as an optimization.

dbus_type_is_fixed() returns TRUE for fixed-length types, which are the basic types minus the string-like types.

The value argument should be the adddress of an array, so e.g. "const dbus_uint32_t\*\*"

Parameters  
|              |                                     |
|--------------|-------------------------------------|
| str          | string to marshal to                |
| insert_at    | where to insert the value           |
| element_type | type of array elements              |
| value        | address of an array to marshal      |
| n_elements   | number of elements in the array     |
| byte_order   | byte order                          |
| pos_after    | NULL or the position after the type |

<!-- -->

Returns  
TRUE on success

Definition at line 1059 of file dbus-marshal-basic.c.

References \_dbus_assert, \_dbus_assert_not_reached, \_dbus_type_to_string(), DBUS_TYPE_BOOLEAN, DBUS_TYPE_BYTE, DBUS_TYPE_DOUBLE, DBUS_TYPE_INT16, DBUS_TYPE_INT32, DBUS_TYPE_INT64, dbus_type_is_fixed(), DBUS_TYPE_UINT16, DBUS_TYPE_UINT32, DBUS_TYPE_UINT64, DBUS_TYPE_UNIX_FD, and FALSE.

Referenced by \_dbus_type_writer_write_fixed_multi().

## ◆ \_dbus_pack_uint32()

|                         |     |                   |               |
|-------------------------|-----|-------------------|---------------|
| void \_dbus_pack_uint32 | (   | dbus_uint32_t     | *value*,      |
|                         |     | int               | *byte_order*, |
|                         |     | unsigned char \*  | *data*        |
|                         | )   |                   |               |

Packs a 32 bit unsigned integer into a data pointer.

Parameters  
|            |                       |
|------------|-----------------------|
| value      | the value             |
| byte_order | the byte order to use |
| data       | the data pointer      |

Definition at line 142 of file dbus-marshal-basic.c.

## ◆ \_dbus_swap_array()

|                        |     |                   |               |
|------------------------|-----|-------------------|---------------|
| void \_dbus_swap_array | (   | unsigned char \*  | *data*,       |
|                        |     | int               | *n_elements*, |
|                        |     | int               | *alignment*   |
|                        | )   |                   |               |

Swaps the elements of an array to the opposite byte order.

Parameters  
|            |                      |
|------------|----------------------|
| data       | start of array       |
| n_elements | number of elements   |
| alignment  | size of each element |

Definition at line 927 of file dbus-marshal-basic.c.

References \_dbus_assert.

## ◆ \_dbus_type_get_alignment()

|                               |     |      |            |     |     |
|-------------------------------|-----|------|------------|-----|-----|
| int \_dbus_type_get_alignment | (   | int  | *typecode* | )   |     |

Gets the alignment requirement for the given type; will be 1, 2, 4, or 8.

Parameters  
|          |          |
|----------|----------|
| typecode | the type |

<!-- -->

Returns  
alignment of 1, 2, 4, or 8

Definition at line 1244 of file dbus-marshal-basic.c.

References \_dbus_assert_not_reached, DBUS_TYPE_ARRAY, DBUS_TYPE_BOOLEAN, DBUS_TYPE_BYTE, DBUS_TYPE_DICT_ENTRY, DBUS_TYPE_DOUBLE, DBUS_TYPE_INT16, DBUS_TYPE_INT32, DBUS_TYPE_INT64, DBUS_TYPE_OBJECT_PATH, DBUS_TYPE_SIGNATURE, DBUS_TYPE_STRING, DBUS_TYPE_STRUCT, DBUS_TYPE_UINT16, DBUS_TYPE_UINT32, DBUS_TYPE_UINT64, DBUS_TYPE_UNIX_FD, and DBUS_TYPE_VARIANT.

Referenced by \_dbus_marshal_skip_array(), \_dbus_type_reader_read_fixed_multi(), dbus_message_iter_append_fixed_array(), and dbus_message_iter_get_element_count().

## ◆ \_dbus_type_reader_delete()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_type_reader_delete | ( | DBusTypeReader \*  | *reader*, |
|  |  | const DBusTypeReader \*  | *realign_root*  |
|  | ) |  |  |

Recursively deletes any value pointed to by the reader, leaving the reader valid to continue reading.

Any other readers will be invalidated.

The provided realign_root is the reader to start from when realigning the data that follows the newly-set value. See \_dbus_type_reader_set_basic() for more details on the realign_root paramter.

Parameters  
|              |                                           |
|--------------|-------------------------------------------|
| reader       | reader indicating where to delete a value |
| realign_root | realign from here                         |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 1419 of file dbus-marshal-recursive.c.

References \_dbus_assert, FALSE, DBusTypeReader::klass, NULL, and TRUE.

Referenced by \_dbus_header_delete_field(), and \_dbus_header_remove_unknown_fields().

## ◆ \_dbus_type_reader_get_array_length()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| int \_dbus_type_reader_get_array_length | ( | const DBusTypeReader \*  | *reader* | ) |  |

Returns the number of bytes in the array.

Parameters  
|        |                         |
|--------|-------------------------|
| reader | the reader to read from |

<!-- -->

Returns  
the number of bytes in the array

Definition at line 899 of file dbus-marshal-recursive.c.

References \_dbus_assert, DBusTypeReader::klass, and DBusTypeReaderClass::types_only.

Referenced by dbus_message_iter_get_array_len(), and dbus_message_iter_get_element_count().

## ◆ \_dbus_type_reader_get_current_type()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| int \_dbus_type_reader_get_current_type | ( | const DBusTypeReader \*  | *reader* | ) |  |

Gets the type of the value the reader is currently pointing to; or for a types-only reader gets the type it's currently pointing to.

If the reader is at the end of a block or end of a container such as an array, returns DBUS_TYPE_INVALID.

Parameters  
|        |            |
|--------|------------|
| reader | the reader |

Definition at line 785 of file dbus-marshal-recursive.c.

References \_dbus_assert, \_dbus_first_type_in_signature(), \_dbus_type_to_string(), DBusTypeReaderClass::check_finished, DBUS_DICT_ENTRY_BEGIN_CHAR, DBUS_DICT_ENTRY_END_CHAR, DBUS_STRUCT_BEGIN_CHAR, DBUS_STRUCT_END_CHAR, DBUS_TYPE_INVALID, DBusTypeReader::finished, DBusTypeReader::klass, DBusTypeReader::type_pos, and DBusTypeReader::type_str.

Referenced by \_dbus_header_load(), \_dbus_header_remove_unknown_fields(), \_dbus_message_iter_get_args_valist(), \_dbus_type_reader_get_element_type(), \_dbus_type_reader_next(), \_dbus_type_reader_read_basic(), \_dbus_type_reader_set_basic(), dbus_message_iter_get_arg_type(), dbus_message_iter_get_element_count(), dbus_message_iter_get_fixed_array(), and dbus_message_iter_init().

## ◆ \_dbus_type_reader_get_element_type()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| int \_dbus_type_reader_get_element_type | ( | const DBusTypeReader \*  | *reader* | ) |  |

Gets the type of an element of the array the reader is currently pointing to.

It's an error to call this if \_dbus_type_reader_get_current_type() doesn't return DBUS_TYPE_ARRAY for this reader.

Parameters  
|        |            |
|--------|------------|
| reader | the reader |

Definition at line 820 of file dbus-marshal-recursive.c.

References \_dbus_assert, \_dbus_first_type_in_signature(), \_dbus_type_reader_get_current_type(), DBUS_TYPE_ARRAY, DBusTypeReader::type_pos, and DBusTypeReader::type_str.

Referenced by \_dbus_message_iter_get_args_valist(), dbus_message_iter_get_element_count(), and dbus_message_iter_get_element_type().

## ◆ \_dbus_type_reader_get_signature()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_type_reader_get_signature | ( | const DBusTypeReader \*  | *reader*, |
|  |  | const DBusString \*\*  | *str_p*, |
|  |  | int \*  | *start_p*, |
|  |  | int \*  | *len_p*  |
|  | ) |  |  |

Gets the string and range of said string containing the signature of the current value.

Essentially a more complete version of \_dbus_type_reader_get_current_type() (returns the full type rather than only the outside of the onion).

Note though that the first byte in a struct signature is DBUS_STRUCT_BEGIN_CHAR while the current type will be DBUS_TYPE_STRUCT so it isn't true that the first byte of the signature is always the same as the current type. Another difference is that this function will still return a signature when inside an empty array; say you recurse into empty array of int32, the signature is "i" but the current type will always be DBUS_TYPE_INVALID since there are no elements to be currently pointing to.

Parameters  
|         |                                                |
|---------|------------------------------------------------|
| reader  | the reader                                     |
| str_p   | place to return the string with the type in it |
| start_p | place to return start of the type              |
| len_p   | place to return the length of the type         |

Definition at line 1124 of file dbus-marshal-recursive.c.

References DBusTypeReader::type_pos, and DBusTypeReader::type_str.

Referenced by \_dbus_variant_read(), and dbus_message_iter_get_signature().

## ◆ \_dbus_type_reader_get_value_pos()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| int \_dbus_type_reader_get_value_pos | ( | const DBusTypeReader \*  | *reader* | ) |  |

Gets the current position in the value block.

Parameters  
|        |            |
|--------|------------|
| reader | the reader |

Definition at line 837 of file dbus-marshal-recursive.c.

References DBusTypeReader::value_pos.

Referenced by \_dbus_header_load().

## ◆ \_dbus_type_reader_has_next()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_type_reader_has_next | ( | const DBusTypeReader \*  | *reader* | ) |  |

Check whether there's another value on this "level".

e.g. the next field in a struct, the next value in an array. Returns FALSE at the end of the current container.

You probably don't want to use this; it makes for an awkward for/while loop. A nicer one is "while ((current_type = get_current_type()) != INVALID)"

Parameters  
|        |            |
|--------|------------|
| reader | the reader |

<!-- -->

Returns  
FALSE if nothing more to read at or below this level

Definition at line 1093 of file dbus-marshal-recursive.c.

References \_dbus_type_reader_next().

Referenced by dbus_message_iter_has_next().

## ◆ \_dbus_type_reader_init()

|                              |     |                      |               |
|------------------------------|-----|----------------------|---------------|
| void \_dbus_type_reader_init | (   | DBusTypeReader \*    | *reader*,     |
|                              |     | int                  | *byte_order*, |
|                              |     | const DBusString \*  | *type_str*,   |
|                              |     | int                  | *type_pos*,   |
|                              |     | const DBusString \*  | *value_str*,  |
|                              |     | int                  | *value_pos*   |
|                              | )   |                      |               |

Initializes a type reader.

Parameters  
|            |                                     |
|------------|-------------------------------------|
| reader     | the reader                          |
| byte_order | the byte order of the block to read |
| type_str   | the signature of the block to read  |
| type_pos   | location of signature               |
| value_str  | the string containing values block  |
| value_pos  | start of values block               |

Definition at line 732 of file dbus-marshal-recursive.c.

References \_dbus_string_get_const_data_len(), DBusTypeReader::klass, DBusTypeReader::type_pos, DBusTypeReader::type_str, and DBusTypeReader::value_pos.

Referenced by \_dbus_header_load(), \_dbus_header_remove_unknown_fields(), \_dbus_variant_write(), and dbus_message_iter_init().

## ◆ \_dbus_type_reader_init_types_only()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_type_reader_init_types_only | ( | DBusTypeReader \*  | *reader*, |
|  |  | const DBusString \*  | *type_str*, |
|  |  | int  | *type_pos*  |
|  | ) |  |  |

Like \_dbus_type_reader_init() but the iteration is over the signature, not over values.

Parameters  
|          |                                  |
|----------|----------------------------------|
| reader   | the reader                       |
| type_str | the signature string             |
| type_pos | location in the signature string |

Definition at line 760 of file dbus-marshal-recursive.c.

References \_DBUS_INT_MAX, \_dbus_string_get_const_data_len(), DBusTypeReader::klass, NULL, DBusTypeReader::type_pos, and DBusTypeReader::type_str.

Referenced by \_dbus_marshal_byteswap(), and \_dbus_validate_body_with_reason().

## ◆ \_dbus_type_reader_next()

|                                     |     |                    |          |     |     |
|-------------------------------------|-----|--------------------|----------|-----|-----|
| dbus_bool_t \_dbus_type_reader_next | (   | DBusTypeReader \*  | *reader* | )   |     |

Skip to the next value on this "level".

e.g. the next field in a struct, the next value in an array. Returns FALSE at the end of the current container.

Parameters  
|        |            |
|--------|------------|
| reader | the reader |

<!-- -->

Returns  
FALSE if nothing more to read at or below this level

Definition at line 1053 of file dbus-marshal-recursive.c.

References \_dbus_string_get_const_data_len(), \_dbus_type_reader_get_current_type(), \_dbus_type_to_string(), DBUS_TYPE_INVALID, FALSE, DBusTypeReader::klass, DBusTypeReaderClass::next, DBusTypeReader::type_pos, DBusTypeReader::type_str, and DBusTypeReader::value_pos.

Referenced by \_dbus_header_load(), \_dbus_header_remove_unknown_fields(), \_dbus_message_iter_get_args_valist(), \_dbus_type_reader_has_next(), dbus_message_iter_get_element_count(), and dbus_message_iter_next().

## ◆ \_dbus_type_reader_read_basic()

|                                    |     |                          |           |
|------------------------------------|-----|--------------------------|-----------|
| void \_dbus_type_reader_read_basic | (   | const DBusTypeReader \*  | *reader*, |
|                                    |     | void \*                  | *value*   |
|                                    | )   |                          |           |

Reads a basic-typed value, as with \_dbus_marshal_read_basic().

Parameters  
|        |                          |
|--------|--------------------------|
| reader | the reader               |
| value  | the address of the value |

Definition at line 869 of file dbus-marshal-recursive.c.

References \_dbus_assert, \_dbus_marshal_read_basic(), \_dbus_string_get_const_data_len(), \_dbus_type_reader_get_current_type(), DBusTypeReader::byte_order, DBusTypeReader::klass, NULL, DBusTypeReader::type_pos, DBusTypeReader::type_str, DBusTypeReaderClass::types_only, DBusTypeReader::value_pos, and DBusTypeReader::value_str.

Referenced by \_dbus_header_load(), \_dbus_header_remove_unknown_fields(), \_dbus_message_iter_get_args_valist(), and dbus_message_iter_get_basic().

## ◆ \_dbus_type_reader_read_fixed_multi()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_type_reader_read_fixed_multi | ( | const DBusTypeReader \*  | *reader*, |
|  |  | const void \*\*  | *value*, |
|  |  | int \*  | *n_elements*  |
|  | ) |  |  |

Reads a block of fixed-length basic values, from the current point in an array to the end of the array.

Does not work for arrays of string or container types.

This function returns the array in-place; it does not make a copy, and it does not swap the bytes.

If you ask for DBUS_TYPE_DOUBLE you will get a "const double\*" back and the "value" argument should be a "const double\*\*" and so on.

Parameters  
|            |                                          |
|------------|------------------------------------------|
| reader     | the reader to read from                  |
| value      | place to return the array values         |
| n_elements | place to return number of array elements |

Definition at line 923 of file dbus-marshal-recursive.c.

References \_dbus_assert, \_dbus_first_type_in_signature(), \_dbus_string_get_const_data_len(), \_dbus_type_get_alignment(), DBUS_TYPE_INVALID, dbus_type_is_fixed(), DBusTypeReader::klass, NULL, DBusTypeReader::start_pos, DBusTypeReader::type_pos, DBusTypeReader::type_str, DBusTypeReaderClass::types_only, DBusTypeReader::u, DBusTypeReader::value_pos, and DBusTypeReader::value_str.

Referenced by \_dbus_message_iter_get_args_valist(), and dbus_message_iter_get_fixed_array().

## ◆ \_dbus_type_reader_read_raw()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_type_reader_read_raw | ( | const DBusTypeReader \*  | *reader*, |
|  |  | const unsigned char \*\*  | *value_location*  |
|  | ) |  |  |

Get the address of the marshaled value in the data being read.

The address may not be aligned; you have to align it to the type of the value you want to read. Most of the demarshal routines do this for you.

Parameters  
|                |                                    |
|----------------|------------------------------------|
| reader         | the reader                         |
| value_location | the address of the marshaled value |

Definition at line 852 of file dbus-marshal-recursive.c.

References \_dbus_assert, DBusTypeReader::klass, DBusTypeReaderClass::types_only, DBusTypeReader::value_pos, and DBusTypeReader::value_str.

## ◆ \_dbus_type_reader_recurse()

|                                 |     |                    |           |
|---------------------------------|-----|--------------------|-----------|
| void \_dbus_type_reader_recurse | (   | DBusTypeReader \*  | *reader*, |
|                                 |     | DBusTypeReader \*  | *sub*     |
|                                 | )   |                    |           |

Initialize a new reader pointing to the first type and corresponding value that's a child of the current container.

It's an error to call this if the current type is a non-container.

Note that DBusTypeReader traverses values, not types. So if you have an empty array of array of int, you can't recurse into it. You can only recurse into each element.

Parameters  
|        |                                              |
|--------|----------------------------------------------|
| reader | the reader                                   |
| sub    | a reader to init pointing to the first child |

Definition at line 987 of file dbus-marshal-recursive.c.

References \_dbus_assert, \_dbus_assert_not_reached, \_dbus_first_type_in_signature(), \_dbus_string_get_const_data_len(), \_dbus_type_to_string(), \_dbus_warn_check_failed(), DBUS_TYPE_ARRAY, DBUS_TYPE_DICT_ENTRY, DBUS_TYPE_INVALID, DBUS_TYPE_STRUCT, DBUS_TYPE_VARIANT, DBusTypeReaderClass::id, DBusTypeReader::klass, NULL, DBusTypeReaderClass::recurse, DBusTypeReader::type_pos, DBusTypeReader::type_str, DBusTypeReaderClass::types_only, and DBusTypeReader::value_pos.

Referenced by \_dbus_header_load(), \_dbus_header_remove_unknown_fields(), \_dbus_message_iter_get_args_valist(), \_dbus_variant_write(), dbus_message_iter_get_element_count(), and dbus_message_iter_recurse().

## ◆ \_dbus_type_reader_set_basic()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_type_reader_set_basic | ( | DBusTypeReader \*  | *reader*, |
|  |  | const void \*  | *value*, |
|  |  | const DBusTypeReader \*  | *realign_root*  |
|  | ) |  |  |

Sets a new value for the basic type value pointed to by the reader, leaving the reader valid to continue reading.

Any other readers will be invalidated if you set a variable-length type such as a string.

The provided realign_root is the reader to start from when realigning the data that follows the newly-set value. The reader parameter must point to a value below the realign_root parameter. If the type being set is fixed-length, then realign_root may be NULL. Only values reachable from realign_root will be realigned, so if your string contains other values you will need to deal with those somehow yourself. It is OK if realign_root is the same reader as the reader parameter, though if you aren't setting the root it may not be such a good idea.

Parameters  
|              |                                            |
|--------------|--------------------------------------------|
| reader       | reader indicating where to set a new value |
| value        | address of the value to set                |
| realign_root | realign from here                          |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 1362 of file dbus-marshal-recursive.c.

References \_dbus_assert, \_dbus_string_get_const_data_len(), \_dbus_string_get_length(), \_dbus_type_reader_get_current_type(), \_dbus_type_to_string(), \_dbus_verbose_bytes_of_string(), dbus_type_is_basic(), dbus_type_is_fixed(), DBusTypeReader::klass, NULL, TRUE, DBusTypeReader::type_pos, DBusTypeReader::type_str, DBusTypeReaderClass::types_only, DBusTypeReader::value_pos, and DBusTypeReader::value_str.

## ◆ \_dbus_type_signature_next()

|                                 |     |                |             |
|---------------------------------|-----|----------------|-------------|
| void \_dbus_type_signature_next | (   | const char \*  | *type_str*, |
|                                 |     | int \*         | *type_pos*  |
|                                 | )   |                |             |

Skips to the next "complete" type inside a type signature.

The signature is read starting at type_pos, and the next type position is stored in the same variable.

Parameters  
|          |                                                        |
|----------|--------------------------------------------------------|
| type_str | a type signature (must be valid)                       |
| type_pos | an integer position in the type signature (in and out) |

Definition at line 340 of file dbus-marshal-recursive.c.

References \_dbus_assert, DBUS_DICT_ENTRY_BEGIN_CHAR, DBUS_DICT_ENTRY_END_CHAR, DBUS_STRUCT_BEGIN_CHAR, DBUS_STRUCT_END_CHAR, DBUS_TYPE_ARRAY, DBUS_TYPE_INVALID, NULL, and TRUE.

Referenced by dbus_signature_iter_get_signature(), and dbus_signature_iter_next().

## ◆ \_dbus_type_to_string()

|                                     |     |      |            |     |     |
|-------------------------------------|-----|------|------------|-----|-----|
| const char \* \_dbus_type_to_string | (   | int  | *typecode* | )   |     |

Returns a string describing the given type.

Parameters  
|          |                      |
|----------|----------------------|
| typecode | the type to describe |

<!-- -->

Returns  
a constant string describing the type

Definition at line 1290 of file dbus-marshal-basic.c.

References DBUS_DICT_ENTRY_BEGIN_CHAR, DBUS_DICT_ENTRY_END_CHAR, DBUS_STRUCT_BEGIN_CHAR, DBUS_STRUCT_END_CHAR, DBUS_TYPE_ARRAY, DBUS_TYPE_BOOLEAN, DBUS_TYPE_BYTE, DBUS_TYPE_DICT_ENTRY, DBUS_TYPE_DOUBLE, DBUS_TYPE_INT16, DBUS_TYPE_INT32, DBUS_TYPE_INT64, DBUS_TYPE_INVALID, DBUS_TYPE_OBJECT_PATH, DBUS_TYPE_SIGNATURE, DBUS_TYPE_STRING, DBUS_TYPE_STRUCT, DBUS_TYPE_UINT16, DBUS_TYPE_UINT32, DBUS_TYPE_UINT64, DBUS_TYPE_UNIX_FD, and DBUS_TYPE_VARIANT.

Referenced by \_dbus_marshal_read_basic(), \_dbus_marshal_skip_basic(), \_dbus_marshal_write_fixed_multi(), \_dbus_message_iter_get_args_valist(), \_dbus_type_reader_get_current_type(), \_dbus_type_reader_next(), \_dbus_type_reader_recurse(), \_dbus_type_reader_set_basic(), \_dbus_type_writer_unrecurse(), and dbus_message_append_args_valist().

## ◆ \_dbus_type_writer_add_types()

|                                   |     |                    |             |
|-----------------------------------|-----|--------------------|-------------|
| void \_dbus_type_writer_add_types | (   | DBusTypeWriter \*  | *writer*,   |
|                                   |     | DBusString \*      | *type_str*, |
|                                   |     | int                | *type_pos*  |
|                                   | )   |                    |             |

Adds type string to the writer, if it had none.

Parameters  
|          |                    |
|----------|--------------------|
| writer   | the writer to init |
| type_str | type string to add |
| type_pos | type position      |

Definition at line 1545 of file dbus-marshal-recursive.c.

References NULL, DBusTypeWriter::type_pos, and DBusTypeWriter::type_str.

## ◆ \_dbus_type_writer_append_array()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_type_writer_append_array | ( | DBusTypeWriter \*  | *writer*, |
|  |  | const DBusString \*  | *contained_type*, |
|  |  | int  | *contained_type_start*, |
|  |  | DBusTypeWriter \*  | *sub*  |
|  | ) |  |  |

Append to an existing array.

Essentially, the writer will read an existing length at the write location; jump over that length; and write new fields. On unrecurse(), the existing length will be updated.

Parameters  
|                      |                          |
|----------------------|--------------------------|
| writer               | the writer               |
| contained_type       | element type             |
| contained_type_start | position of element type |
| sub                  | the subwriter to init    |

<!-- -->

Returns  
FALSE if no memory

Definition at line 2142 of file dbus-marshal-recursive.c.

References DBUS_TYPE_ARRAY, and TRUE.

Referenced by \_dbus_header_set_field_basic().

## ◆ \_dbus_type_writer_init()

|                              |     |                    |               |
|------------------------------|-----|--------------------|---------------|
| void \_dbus_type_writer_init | (   | DBusTypeWriter \*  | *writer*,     |
|                              |     | int                | *byte_order*, |
|                              |     | DBusString \*      | *type_str*,   |
|                              |     | int                | *type_pos*,   |
|                              |     | DBusString \*      | *value_str*,  |
|                              |     | int                | *value_pos*   |
|                              | )   |                    |               |

Initialize a write iterator, which is used to write out values in serialized D-Bus format.

The type_pos passed in is expected to be inside an already-valid, though potentially empty, type signature. This means that the byte after type_pos must be either DBUS_TYPE_INVALID (aka nul) or some other valid type. DBusTypeWriter won't enforce that the signature is already valid (you can append the nul byte at the end if you like), but just be aware that you need the nul byte eventually and DBusTypeWriter isn't going to write it for you.

Parameters  
|            |                                    |
|------------|------------------------------------|
| writer     | the writer to init                 |
| byte_order | the byte order to marshal into     |
| type_str   | the string to write typecodes into |
| type_pos   | where to insert typecodes          |
| value_str  | the string to write values into    |
| value_pos  | where to insert values             |

Definition at line 1492 of file dbus-marshal-recursive.c.

References \_dbus_string_get_const_data_len(), DBusTypeWriter::byte_order, DBusTypeWriter::container_type, DBUS_TYPE_INVALID, DBusTypeWriter::enabled, FALSE, TRUE, DBusTypeWriter::type_pos, DBusTypeWriter::type_pos_is_expectation, DBusTypeWriter::type_str, DBusTypeWriter::value_pos, and DBusTypeWriter::value_str.

Referenced by \_dbus_type_writer_init_types_delayed(), and \_dbus_type_writer_init_values_only().

## ◆ \_dbus_type_writer_init_types_delayed()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_type_writer_init_types_delayed | ( | DBusTypeWriter \*  | *writer*, |
|  |  | int  | *byte_order*, |
|  |  | DBusString \*  | *value_str*, |
|  |  | int  | *value_pos*  |
|  | ) |  |  |

Initialize a write iterator, with the signature to be provided later.

Parameters  
|            |                                 |
|------------|---------------------------------|
| writer     | the writer to init              |
| byte_order | the byte order to marshal into  |
| value_str  | the string to write values into |
| value_pos  | where to insert values          |

Definition at line 1527 of file dbus-marshal-recursive.c.

References \_dbus_type_writer_init(), and NULL.

Referenced by dbus_message_iter_init_append().

## ◆ \_dbus_type_writer_init_values_only()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_type_writer_init_values_only | ( | DBusTypeWriter \*  | *writer*, |
|  |  | int  | *byte_order*, |
|  |  | const DBusString \*  | *type_str*, |
|  |  | int  | *type_pos*, |
|  |  | DBusString \*  | *value_str*, |
|  |  | int  | *value_pos*  |
|  | ) |  |  |

Like \_dbus_type_writer_init(), except the type string passed in should correspond to an existing signature that matches what you're going to write out.

The writer will check what you write vs. this existing signature.

Parameters  
|            |                                 |
|------------|---------------------------------|
| writer     | the writer to init              |
| byte_order | the byte order to marshal into  |
| type_str   | the string with signature       |
| type_pos   | start of signature              |
| value_str  | the string to write values into |
| value_pos  | where to insert values          |

Definition at line 1583 of file dbus-marshal-recursive.c.

References \_dbus_type_writer_init(), TRUE, and DBusTypeWriter::type_pos_is_expectation.

Referenced by \_dbus_header_create(), \_dbus_header_set_field_basic(), and \_dbus_variant_read().

## ◆ \_dbus_type_writer_recurse()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_type_writer_recurse | ( | DBusTypeWriter \*  | *writer*, |
|  |  | int  | *container_type*, |
|  |  | const DBusString \*  | *contained_type*, |
|  |  | int  | *contained_type_start*, |
|  |  | DBusTypeWriter \*  | *sub*  |
|  | ) |  |  |

Opens a new container and writes out the initial information for that container.

Parameters  
|                      |                                                |
|----------------------|------------------------------------------------|
| writer               | the writer                                     |
| container_type       | the type of the container to open              |
| contained_type       | the array element type or variant content type |
| contained_type_start | position to look for the type                  |
| sub                  | the new sub-writer to write container contents |

<!-- -->

Returns  
FALSE if no memory

Definition at line 2108 of file dbus-marshal-recursive.c.

References FALSE.

Referenced by \_dbus_header_create(), \_dbus_variant_read(), and dbus_message_iter_open_container().

## ◆ \_dbus_type_writer_remove_types()

|                                      |     |                    |          |     |     |
|--------------------------------------|-----|--------------------|----------|-----|-----|
| void \_dbus_type_writer_remove_types | (   | DBusTypeWriter \*  | *writer* | )   |     |

Removes type string from the writer.

Parameters  
|        |                           |
|--------|---------------------------|
| writer | the writer to remove from |

Definition at line 1562 of file dbus-marshal-recursive.c.

References NULL, DBusTypeWriter::type_pos, and DBusTypeWriter::type_str.

## ◆ \_dbus_type_writer_unrecurse()

|                                          |     |                    |           |
|------------------------------------------|-----|--------------------|-----------|
| dbus_bool_t \_dbus_type_writer_unrecurse | (   | DBusTypeWriter \*  | *writer*, |
|                                          |     | DBusTypeWriter \*  | *sub*     |
|                                          | )   |                    |           |

Closes a container created by \_dbus_type_writer_recurse() and writes any additional information to the values block.

Parameters  
|        |                                                        |
|--------|--------------------------------------------------------|
| writer | the writer                                             |
| sub    | the sub-writer created by \_dbus_type_writer_recurse() |

<!-- -->

Returns  
FALSE if no memory

Definition at line 2178 of file dbus-marshal-recursive.c.

References \_dbus_assert, \_dbus_marshal_set_uint32(), \_dbus_string_get_const_data_len(), \_dbus_type_to_string(), DBusTypeWriter::byte_order, DBusTypeWriter::container_type, DBUS_DICT_ENTRY_END_CHAR, DBUS_STRUCT_END_CHAR, DBUS_TYPE_ARRAY, DBUS_TYPE_DICT_ENTRY, DBUS_TYPE_INVALID, DBUS_TYPE_STRUCT, FALSE, DBusTypeWriter::len_pos, NULL, TRUE, DBusTypeWriter::type_pos, DBusTypeWriter::type_pos_is_expectation, DBusTypeWriter::type_str, DBusTypeWriter::u, DBusTypeWriter::value_pos, and DBusTypeWriter::value_str.

Referenced by \_dbus_header_create(), \_dbus_header_set_field_basic(), \_dbus_variant_read(), and dbus_message_iter_close_container().

## ◆ \_dbus_type_writer_write_basic()

|                                            |     |                    |           |
|--------------------------------------------|-----|--------------------|-----------|
| dbus_bool_t \_dbus_type_writer_write_basic | (   | DBusTypeWriter \*  | *writer*, |
|                                            |     | int                | *type*,   |
|                                            |     | const void \*      | *value*   |
|                                            | )   |                    |           |

Writes out a basic type.

Parameters  
|        |                                   |
|--------|-----------------------------------|
| writer | the writer                        |
| type   | the type to write                 |
| value  | the address of the value to write |

<!-- -->

Returns  
FALSE if no memory

Definition at line 2310 of file dbus-marshal-recursive.c.

References \_dbus_assert_not_reached, \_dbus_string_alloc_space(), DBusTypeWriter::enabled, FALSE, NULL, TRUE, DBusTypeWriter::type_pos, DBusTypeWriter::type_pos_is_expectation, DBusTypeWriter::type_str, and DBusTypeWriter::value_pos.

Referenced by \_dbus_header_create(), \_dbus_variant_read(), and dbus_message_iter_append_basic().

## ◆ \_dbus_type_writer_write_fixed_multi()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_type_writer_write_fixed_multi | ( | DBusTypeWriter \*  | *writer*, |
|  |  | int  | *element_type*, |
|  |  | const void \*  | *value*, |
|  |  | int  | *n_elements*  |
|  | ) |  |  |

Writes a block of fixed-length basic values, i.e.

those that are both dbus_type_is_fixed() and \_dbus_type_is_basic(). The block must be written inside an array.

The value parameter should be the address of said array of values, so e.g. if it's an array of double, pass in "const double\*\*"

Parameters  
|              |                                 |
|--------------|---------------------------------|
| writer       | the writer                      |
| element_type | type of stuff in the array      |
| value        | address of the array            |
| n_elements   | number of elements in the array |

<!-- -->

Returns  
FALSE if no memory

Definition at line 2358 of file dbus-marshal-recursive.c.

References \_dbus_assert, \_dbus_assert_not_reached, \_dbus_marshal_write_fixed_multi(), DBusTypeWriter::byte_order, DBusTypeWriter::container_type, DBUS_TYPE_ARRAY, dbus_type_is_fixed(), DBusTypeWriter::enabled, FALSE, TRUE, DBusTypeWriter::type_pos, DBusTypeWriter::type_pos_is_expectation, DBusTypeWriter::value_pos, and DBusTypeWriter::value_str.

Referenced by dbus_message_iter_append_fixed_array().

## ◆ \_dbus_type_writer_write_reader()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_type_writer_write_reader | ( | DBusTypeWriter \*  | *writer*, |
|  |  | DBusTypeReader \*  | *reader*  |
|  | ) |  |  |

Iterate through all values in the given reader, writing a copy of each value to the writer.

The reader will be moved forward to its end position.

Parameters  
|        |                         |
|--------|-------------------------|
| writer | the writer to copy to   |
| reader | the reader to copy from |

<!-- -->

Returns  
FALSE if no memory

Definition at line 2730 of file dbus-marshal-recursive.c.

References NULL.

Referenced by \_dbus_variant_read(), and \_dbus_variant_write().

## ◆ \_dbus_unpack_uint16()

|  |  |  |  |
|----|----|----|----|
| dbus_uint16_t \_dbus_unpack_uint16 | ( | int  | *byte_order*, |
|  |  | const unsigned char \*  | *data*  |
|  | ) |  |  |

Unpacks a 16 bit unsigned integer from a data pointer.

Parameters  
|            |                       |
|------------|-----------------------|
| byte_order | The byte order to use |
| data       | the data pointer      |

<!-- -->

Returns  
the integer

Definition at line 168 of file dbus-marshal-basic.c.

References \_dbus_assert, and DBUS_LITTLE_ENDIAN.

## ◆ \_dbus_unpack_uint32()

|  |  |  |  |
|----|----|----|----|
| dbus_uint32_t \_dbus_unpack_uint32 | ( | int  | *byte_order*, |
|  |  | const unsigned char \*  | *data*  |
|  | ) |  |  |

Unpacks a 32 bit unsigned integer from a data pointer.

Parameters  
|            |                       |
|------------|-----------------------|
| byte_order | The byte order to use |
| data       | the data pointer      |

<!-- -->

Returns  
the integer

Definition at line 189 of file dbus-marshal-basic.c.

References \_dbus_assert, and DBUS_LITTLE_ENDIAN.

Referenced by \_dbus_marshal_read_uint32(), and \_dbus_verbose_bytes().

## ◆ \_dbus_validate_body_with_reason()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT DBusValidity \_dbus_validate_body_with_reason | ( | const DBusString \*  | *expected_signature*, |
|  |  | int  | *expected_signature_start*, |
|  |  | int  | *byte_order*, |
|  |  | int \*  | *bytes_remaining*, |
|  |  | const DBusString \*  | *value_str*, |
|  |  | int  | *value_pos*, |
|  |  | int  | *len*  |
|  | ) |  |  |

Verifies that the range of value_str from value_pos to value_end is a legitimate value of type expected_signature.

If this function returns TRUE, it will be safe to iterate over the values with DBusTypeReader. The signature is assumed to be already valid.

If bytes_remaining is not NULL, then leftover bytes will be stored there and DBUS_VALID returned. If it is NULL, then DBUS_INVALID_TOO_MUCH_DATA will be returned if bytes are left over.

Parameters  
|                          |                                              |
|--------------------------|----------------------------------------------|
| expected_signature       | the expected types in the value_str          |
| expected_signature_start | where in expected_signature is the signature |
| byte_order               | the byte order                               |
| bytes_remaining          | place to store leftover bytes                |
| value_str                | the string containing the body               |
| value_pos                | where the values start                       |
| len                      | length of values after value_pos             |

<!-- -->

Returns  
DBUS_VALID if valid, reason why invalid otherwise

Definition at line 767 of file dbus-marshal-validate.c.

References \_dbus_assert, \_dbus_string_get_const_data_len(), \_dbus_string_get_length(), \_dbus_type_reader_init_types_only(), DBUS_INVALID_TOO_MUCH_DATA, DBUS_VALID, and TRUE.

Referenced by \_dbus_header_load().

## ◆ \_dbus_validate_bus_name()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_validate_bus_name | ( | const DBusString \*  | *str*, |
|  |  | int  | *start*, |
|  |  | int  | *len*  |
|  | ) |  |  |

Checks that the given range of the string is a valid bus name in the D-Bus protocol.

This includes a length restriction, etc., see the specification.

Parameters  
|       |                           |
|-------|---------------------------|
| str   | the string                |
| start | first byte index to check |
| len   | number of bytes to check  |

<!-- -->

Returns  
TRUE if the byte range exists and is a valid name

Definition at line 1253 of file dbus-marshal-validate.c.

References FALSE.

Referenced by dbus_validate_bus_name().

## ◆ \_dbus_validate_bus_namespace()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_validate_bus_namespace | ( | const DBusString \*  | *str*, |
|  |  | int  | *start*, |
|  |  | int  | *len*  |
|  | ) |  |  |

Checks that the given range of the string is a prefix of a valid bus name in the D-Bus protocol.

Unlike \_dbus_validate_bus_name(), this accepts strings with only one period-separated component.

Parameters  
|       |                           |
|-------|---------------------------|
| str   | the string                |
| start | first byte index to check |
| len   | number of bytes to check  |

<!-- -->

Returns  
TRUE if the byte range exists and is a valid name

Definition at line 1274 of file dbus-marshal-validate.c.

References TRUE.

## ◆ \_dbus_validate_error_name()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_validate_error_name | ( | const DBusString \*  | *str*, |
|  |  | int  | *start*, |
|  |  | int  | *len*  |
|  | ) |  |  |

Checks that the given range of the string is a valid error name in the D-Bus protocol.

This includes a length restriction, etc., see the specification.

Parameters  
|       |                           |
|-------|---------------------------|
| str   | the string                |
| start | first byte index to check |
| len   | number of bytes to check  |

<!-- -->

Returns  
TRUE if the byte range exists and is a valid name

Definition at line 1124 of file dbus-marshal-validate.c.

References \_dbus_validate_interface().

Referenced by dbus_validate_error_name().

## ◆ \_dbus_validate_interface()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_validate_interface | ( | const DBusString \*  | *str*, |
|  |  | int  | *start*, |
|  |  | int  | *len*  |
|  | ) |  |  |

Checks that the given range of the string is a valid interface name in the D-Bus protocol.

This includes a length restriction and an ASCII subset, see the specification.

Parameters  
|       |                           |
|-------|---------------------------|
| str   | the string                |
| start | first byte index to check |
| len   | number of bytes to check  |

<!-- -->

Returns  
TRUE if the byte range exists and is a valid name

Definition at line 987 of file dbus-marshal-validate.c.

References \_dbus_assert, \_dbus_string_get_length(), DBUS_MAXIMUM_NAME_LENGTH, FALSE, NULL, TRUE, VALID_INITIAL_NAME_CHARACTER, and VALID_NAME_CHARACTER.

Referenced by \_dbus_validate_error_name(), and dbus_validate_interface().

## ◆ \_dbus_validate_member()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_validate_member | ( | const DBusString \*  | *str*, |
|  |  | int  | *start*, |
|  |  | int  | *len*  |
|  | ) |  |  |

Checks that the given range of the string is a valid member name in the D-Bus protocol.

This includes a length restriction, etc., see the specification.

Parameters  
|       |                           |
|-------|---------------------------|
| str   | the string                |
| start | first byte index to check |
| len   | number of bytes to check  |

<!-- -->

Returns  
TRUE if the byte range exists and is a valid name

Definition at line 1063 of file dbus-marshal-validate.c.

References \_dbus_assert, \_dbus_string_get_length(), DBUS_MAXIMUM_NAME_LENGTH, FALSE, TRUE, VALID_INITIAL_NAME_CHARACTER, and VALID_NAME_CHARACTER.

Referenced by dbus_validate_member().

## ◆ \_dbus_validate_path()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_validate_path | ( | const DBusString \*  | *str*, |
|  |  | int  | *start*, |
|  |  | int  | *len*  |
|  | ) |  |  |

Checks that the given range of the string is a valid object path name in the D-Bus protocol.

Part of the validation ensures that the object path contains only ASCII.

Parameters  
|       |                           |
|-------|---------------------------|
| str   | the string                |
| start | first byte index to check |
| len   | number of bytes to check  |

<!-- -->

Returns  
TRUE if the byte range exists and is a valid name

Definition at line 849 of file dbus-marshal-validate.c.

References \_dbus_assert, \_dbus_string_get_length(), FALSE, TRUE, and VALID_NAME_CHARACTER.

Referenced by dbus_validate_path().

## ◆ \_dbus_validate_signature_with_reason()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT DBusValidity \_dbus_validate_signature_with_reason | ( | const DBusString \*  | *type_str*, |
|  |  | int  | *type_pos*, |
|  |  | int  | *len*  |
|  | ) |  |  |

Verifies that the range of type_str from type_pos to type_end is a valid signature.

If this function returns TRUE, it will be safe to iterate over the signature with a types-only DBusTypeReader. The range passed in should NOT include the terminating nul/DBUS_TYPE_INVALID.

Parameters  
|          |                           |
|----------|---------------------------|
| type_str | the string                |
| type_pos | where the typecodes start |
| len      | length of typecodes       |

<!-- -->

Returns  
DBUS_VALID if valid, reason why invalid otherwise

Definition at line 53 of file dbus-marshal-validate.c.

References \_dbus_assert, \_DBUS_INT32_MAX, \_DBUS_INT_TO_POINTER, \_dbus_list_append(), \_dbus_list_clear(), \_dbus_list_pop_last(), \_DBUS_N_ELEMENTS, \_DBUS_POINTER_TO_INT, DBUS_DICT_ENTRY_BEGIN_CHAR, DBUS_DICT_ENTRY_END_CHAR, DBUS_MAXIMUM_SIGNATURE_LENGTH, DBUS_MAXIMUM_TYPE_RECURSION_DEPTH, DBUS_STRUCT_BEGIN_CHAR, DBUS_STRUCT_END_CHAR, DBUS_TYPE_ARRAY, DBUS_TYPE_BOOLEAN, DBUS_TYPE_BYTE, DBUS_TYPE_DICT_ENTRY, DBUS_TYPE_DOUBLE, DBUS_TYPE_INT16, DBUS_TYPE_INT32, DBUS_TYPE_INT64, DBUS_TYPE_INVALID, dbus_type_is_basic(), dbus_type_is_valid(), DBUS_TYPE_OBJECT_PATH, DBUS_TYPE_SIGNATURE, DBUS_TYPE_STRING, DBUS_TYPE_STRUCT, DBUS_TYPE_UINT16, DBUS_TYPE_UINT32, DBUS_TYPE_UINT64, DBUS_TYPE_UNIX_FD, DBUS_TYPE_VARIANT, DBUS_VALID, DBUS_VALIDITY_UNKNOWN_OOM_ERROR, and NULL.

Referenced by dbus_message_iter_append_basic(), dbus_message_iter_open_container(), and dbus_signature_validate().

## ◆ \_dbus_validity_to_error_message()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| const char \* \_dbus_validity_to_error_message | ( | DBusValidity  | *validity* | ) |  |

Definition at line 901 of file dbus-marshal-validate.c.

## ◆ \_dbus_verbose_bytes()

|                           |     |                         |           |
|---------------------------|-----|-------------------------|-----------|
| void \_dbus_verbose_bytes | (   | const unsigned char \*  | *data*,   |
|                           |     | int                     | *len*,    |
|                           |     | int                     | *offset*  |
|                           | )   |                         |           |

If in verbose mode, print a block of binary data.

Parameters  
|        |                                          |
|--------|------------------------------------------|
| data   | the data                                 |
| len    | the length of the data                   |
| offset | where to start counting for byte indexes |

Definition at line 1351 of file dbus-marshal-basic.c.

References \_dbus_assert, \_dbus_unpack_uint32(), DBUS_BIG_ENDIAN, DBUS_INT64_MODIFIER, and DBUS_LITTLE_ENDIAN.

Referenced by \_dbus_verbose_bytes_of_string().

## ◆ \_dbus_verbose_bytes_of_string()

|                                     |     |                      |          |
|-------------------------------------|-----|----------------------|----------|
| void \_dbus_verbose_bytes_of_string | (   | const DBusString \*  | *str*,   |
|                                     |     | int                  | *start*, |
|                                     |     | int                  | *len*    |
|                                     | )   |                      |          |

Dump the given part of the string to verbose log.

Parameters  
|       |                            |
|-------|----------------------------|
| str   | the string                 |
| start | the start of range to dump |
| len   | length of range            |

Definition at line 1428 of file dbus-marshal-basic.c.

References \_dbus_assert, \_dbus_string_get_const_data_len(), \_dbus_string_get_length(), and \_dbus_verbose_bytes().

Referenced by \_dbus_read(), \_dbus_read_socket(), \_dbus_read_socket_with_unix_fds(), \_dbus_type_reader_set_basic(), \_dbus_write(), and \_dbus_write_socket().
