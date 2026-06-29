dbus-marshal-validate.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-marshal-validate.h Validation routines for marshaled data

3 \*

4 \* Copyright (C) 2005 Red Hat, Inc.

5 \*

6 \* SPDX-License-Identifier: AFL-2.1 OR GPL-2.0-or-later

7 \*

8 \* Licensed under the Academic Free License version 2.1

9 \*

10 \* This program is free software; you can redistribute it and/or modify

11 \* it under the terms of the GNU General Public License as published by

12 \* the Free Software Foundation; either version 2 of the License, or

13 \* (at your option) any later version.

14 \*

15 \* This program is distributed in the hope that it will be useful,

16 \* but WITHOUT ANY WARRANTY; without even the implied warranty of

17 \* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

18 \* GNU General Public License for more details.

19 \*

20 \* You should have received a copy of the GNU General Public License

21 \* along with this program; if not, write to the Free Software

22 \* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

23 \*

24 \*/

25

26\#ifndef DBUS_MARSHAL_VALIDATE_H

27\#define DBUS_MARSHAL_VALIDATE_H

28

29\#include \<dbus/dbus-string.h\>

30

40typedef enum

41{

42 DBUS_VALIDATION_MODE_WE_TRUST_THIS_DATA_ABSOLUTELY,

43 DBUS_VALIDATION_MODE_DATA_IS_UNTRUSTED

44} DBusValidationMode;

45

53typedef enum

54{

55\#define \_DBUS_NEGATIVE_VALIDITY_COUNT 4

56 DBUS_VALIDITY_UNKNOWN_OOM_ERROR = -4,

57 DBUS_INVALID_FOR_UNKNOWN_REASON = -3,

58 DBUS_VALID_BUT_INCOMPLETE = -2,

59 DBUS_VALIDITY_UNKNOWN = -1,

60 DBUS_VALID = 0,

61 DBUS_INVALID_UNKNOWN_TYPECODE = 1,

62 DBUS_INVALID_MISSING_ARRAY_ELEMENT_TYPE = 2,

63 DBUS_INVALID_SIGNATURE_TOO_LONG = 3, /\* this one is impossible right now since

64 \* you can't put a too-long value in a byte

65 \*/

66 DBUS_INVALID_EXCEEDED_MAXIMUM_ARRAY_RECURSION = 4,

67 DBUS_INVALID_EXCEEDED_MAXIMUM_STRUCT_RECURSION = 5,

68 DBUS_INVALID_STRUCT_ENDED_BUT_NOT_STARTED = 6,

69 DBUS_INVALID_STRUCT_STARTED_BUT_NOT_ENDED = 7,

70 DBUS_INVALID_STRUCT_HAS_NO_FIELDS = 8,

71 DBUS_INVALID_ALIGNMENT_PADDING_NOT_NUL = 9,

72 DBUS_INVALID_BOOLEAN_NOT_ZERO_OR_ONE = 10,

73 DBUS_INVALID_NOT_ENOUGH_DATA = 11,

74 DBUS_INVALID_TOO_MUCH_DATA = 12,

75 DBUS_INVALID_BAD_BYTE_ORDER = 13,

76 DBUS_INVALID_BAD_PROTOCOL_VERSION = 14,

77 DBUS_INVALID_BAD_MESSAGE_TYPE = 15,

78 DBUS_INVALID_BAD_SERIAL = 16,

79 DBUS_INVALID_INSANE_FIELDS_ARRAY_LENGTH = 17,

80 DBUS_INVALID_INSANE_BODY_LENGTH = 18,

81 DBUS_INVALID_MESSAGE_TOO_LONG = 19,

82 DBUS_INVALID_HEADER_FIELD_CODE = 20,

83 DBUS_INVALID_HEADER_FIELD_HAS_WRONG_TYPE = 21,

84 DBUS_INVALID_USES_LOCAL_INTERFACE = 22,

85 DBUS_INVALID_USES_LOCAL_PATH = 23,

86 DBUS_INVALID_HEADER_FIELD_APPEARS_TWICE = 24,

87 DBUS_INVALID_BAD_DESTINATION = 25,

88 DBUS_INVALID_BAD_INTERFACE = 26,

89 DBUS_INVALID_BAD_MEMBER = 27,

90 DBUS_INVALID_BAD_ERROR_NAME = 28,

91 DBUS_INVALID_BAD_SENDER = 29,

92 DBUS_INVALID_MISSING_PATH = 30,

93 DBUS_INVALID_MISSING_INTERFACE = 31,

94 DBUS_INVALID_MISSING_MEMBER = 32,

95 DBUS_INVALID_MISSING_ERROR_NAME = 33,

96 DBUS_INVALID_MISSING_REPLY_SERIAL = 34,

97 DBUS_INVALID_LENGTH_OUT_OF_BOUNDS = 35,

98 DBUS_INVALID_ARRAY_LENGTH_EXCEEDS_MAXIMUM = 36,

99 DBUS_INVALID_BAD_PATH = 37,

100 DBUS_INVALID_SIGNATURE_LENGTH_OUT_OF_BOUNDS = 38,

101 DBUS_INVALID_BAD_UTF8_IN_STRING = 39,

102 DBUS_INVALID_ARRAY_LENGTH_INCORRECT = 40,

103 DBUS_INVALID_VARIANT_SIGNATURE_LENGTH_OUT_OF_BOUNDS = 41,

104 DBUS_INVALID_VARIANT_SIGNATURE_BAD = 42,

105 DBUS_INVALID_VARIANT_SIGNATURE_EMPTY = 43,

106 DBUS_INVALID_VARIANT_SIGNATURE_SPECIFIES_MULTIPLE_VALUES = 44,

107 DBUS_INVALID_VARIANT_SIGNATURE_MISSING_NUL = 45,

108 DBUS_INVALID_STRING_MISSING_NUL = 46,

109 DBUS_INVALID_SIGNATURE_MISSING_NUL = 47,

110 DBUS_INVALID_EXCEEDED_MAXIMUM_DICT_ENTRY_RECURSION = 48,

111 DBUS_INVALID_DICT_ENTRY_ENDED_BUT_NOT_STARTED = 49,

112 DBUS_INVALID_DICT_ENTRY_STARTED_BUT_NOT_ENDED = 50,

113 DBUS_INVALID_DICT_ENTRY_HAS_NO_FIELDS = 51,

114 DBUS_INVALID_DICT_ENTRY_HAS_ONLY_ONE_FIELD = 52,

115 DBUS_INVALID_DICT_ENTRY_HAS_TOO_MANY_FIELDS = 53,

116 DBUS_INVALID_DICT_ENTRY_NOT_INSIDE_ARRAY = 54,

117 DBUS_INVALID_DICT_KEY_MUST_BE_BASIC_TYPE = 55,

118 DBUS_INVALID_MISSING_UNIX_FDS = 56,

119 DBUS_INVALID_NESTED_TOO_DEEPLY = 57,

120 DBUS_VALIDITY_LAST

121} DBusValidity;

122

123DBUS_PRIVATE_EXPORT

124DBusValidity \_dbus_validate_signature_with_reason (const DBusString \*type_str,

125 int type_pos,

126 int len);

127DBUS_PRIVATE_EXPORT

128DBusValidity \_dbus_validate_body_with_reason (const DBusString \*expected_signature,

129 int expected_signature_start,

130 int byte_order,

131 int \*bytes_remaining,

132 const DBusString \*value_str,

133 int value_pos,

134 int len);

135

136const char \*\_dbus_validity_to_error_message (DBusValidity validity);

137

138DBUS_PRIVATE_EXPORT

139dbus_bool_t \_dbus_validate_path (const DBusString \*str,

140 int start,

141 int len);

142DBUS_PRIVATE_EXPORT

143dbus_bool_t \_dbus_validate_interface (const DBusString \*str,

144 int start,

145 int len);

146DBUS_PRIVATE_EXPORT

147dbus_bool_t \_dbus_validate_member (const DBusString \*str,

148 int start,

149 int len);

150DBUS_PRIVATE_EXPORT

151dbus_bool_t \_dbus_validate_error_name (const DBusString \*str,

152 int start,

153 int len);

154DBUS_PRIVATE_EXPORT

155dbus_bool_t \_dbus_validate_bus_name (const DBusString \*str,

156 int start,

157 int len);

158DBUS_PRIVATE_EXPORT

159dbus_bool_t \_dbus_validate_bus_namespace (const DBusString \*str,

160 int start,

161 int len);

162/\* just to have a name consistent with the above: \*/

163\#define \_dbus_validate_utf8(s,b,e) \_dbus_string_validate_utf8 (s, b, e)

164

165\#ifdef DBUS_DISABLE_CHECKS

166

167/\* Be sure they don't exist, since we don't want to use them outside of checks

168 \* and so we want the compile failure.

169 \*/

170\#define DECLARE_DBUS_NAME_CHECK(what)

171\#define DEFINE_DBUS_NAME_CHECK(what)

172

173\#else /\* !DBUS_DISABLE_CHECKS \*/

174

178\#define DECLARE_DBUS_NAME_CHECK(what) \\

179dbus_bool_t \_dbus_check_is_valid\_##what (const char \*name)

180

183\#define DEFINE_DBUS_NAME_CHECK(what) \\

184dbus_bool_t \\

185\_dbus_check_is_valid\_##what (const char \*name) \\

186{ \\

187 DBusString str; \\

188 \\

189 if (name == NULL) \\

190 return FALSE; \\

191 \\

192 \_dbus_string_init_const (&str, name); \\

193 return \_dbus_validate\_##what (&str, 0, \\

194 \_dbus_string_get_length (&str)); \\

195}

196\#endif /\* !DBUS_DISABLE_CHECKS \*/

197

199DECLARE_DBUS_NAME_CHECK(path);

201DECLARE_DBUS_NAME_CHECK(interface);

203DECLARE_DBUS_NAME_CHECK(member);

205DECLARE_DBUS_NAME_CHECK(error_name);

207DECLARE_DBUS_NAME_CHECK(bus_name);

209DECLARE_DBUS_NAME_CHECK(utf8);

210

213\#endif /\* DBUS_MARSHAL_VALIDATE_H \*/

DBusValidity

DBusValidity

This is primarily used in unit testing, so we can verify that each invalid message is invalid for the...

**Definition** dbus-marshal-validate.h:54

\_dbus_validate_signature_with_reason

DBusValidity \_dbus_validate_signature_with_reason(const DBusString \*type_str, int type_pos, int len)

Verifies that the range of type_str from type_pos to type_end is a valid signature.

**Definition** dbus-marshal-validate.c:53

\_dbus_validate_error_name

dbus_bool_t \_dbus_validate_error_name(const DBusString \*str, int start, int len)

Checks that the given range of the string is a valid error name in the D-Bus protocol.

**Definition** dbus-marshal-validate.c:1124

\_dbus_validate_member

dbus_bool_t \_dbus_validate_member(const DBusString \*str, int start, int len)

Checks that the given range of the string is a valid member name in the D-Bus protocol.

**Definition** dbus-marshal-validate.c:1063

\_dbus_validate_bus_namespace

dbus_bool_t \_dbus_validate_bus_namespace(const DBusString \*str, int start, int len)

Checks that the given range of the string is a prefix of a valid bus name in the D-Bus protocol.

**Definition** dbus-marshal-validate.c:1274

\_dbus_validate_path

dbus_bool_t \_dbus_validate_path(const DBusString \*str, int start, int len)

Checks that the given range of the string is a valid object path name in the D-Bus protocol.

**Definition** dbus-marshal-validate.c:849

\_dbus_validate_interface

dbus_bool_t \_dbus_validate_interface(const DBusString \*str, int start, int len)

Checks that the given range of the string is a valid interface name in the D-Bus protocol.

**Definition** dbus-marshal-validate.c:987

DECLARE_DBUS_NAME_CHECK

\#define DECLARE_DBUS_NAME_CHECK(what)

A name check is used in \_dbus_return_if_fail(), it's not suitable for validating untrusted data.

**Definition** dbus-marshal-validate.h:178

\_dbus_validate_body_with_reason

DBusValidity \_dbus_validate_body_with_reason(const DBusString \*expected_signature, int expected_signature_start, int byte_order, int \*bytes_remaining, const DBusString \*value_str, int value_pos, int len)

Verifies that the range of value_str from value_pos to value_end is a legitimate value of type expect...

**Definition** dbus-marshal-validate.c:767

\_dbus_validate_bus_name

dbus_bool_t \_dbus_validate_bus_name(const DBusString \*str, int start, int len)

Checks that the given range of the string is a valid bus name in the D-Bus protocol.

**Definition** dbus-marshal-validate.c:1253

DBusValidationMode

DBusValidationMode

This is used rather than a bool for high visibility.

**Definition** dbus-marshal-validate.h:41

DBUS_VALIDITY_UNKNOWN_OOM_ERROR

@ DBUS_VALIDITY_UNKNOWN_OOM_ERROR

can't determine validity due to OOM

**Definition** dbus-marshal-validate.h:56

DBUS_INVALID_TOO_MUCH_DATA

@ DBUS_INVALID_TOO_MUCH_DATA

trailing junk makes it invalid

**Definition** dbus-marshal-validate.h:74

DBUS_VALID

@ DBUS_VALID

the data is valid

**Definition** dbus-marshal-validate.h:60

DBusString

**Definition** dbus-string.h:47
