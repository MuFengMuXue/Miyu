dbus-marshal-byteswap.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-marshal-byteswap.c Swap a block of marshaled data

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

26\#include \<config.h\>

27\#include "dbus-marshal-byteswap.h"

28\#include "dbus-marshal-basic.h"

29\#include "dbus-signature.h"

30

36static void

37byteswap_body_helper (DBusTypeReader \*reader,

38 dbus_bool_t walk_reader_to_end,

39 int old_byte_order,

40 int new_byte_order,

41 unsigned char \*p,

42 unsigned char \*\*new_p)

43{

44 int current_type;

45

46 while ((current_type = \_dbus_type_reader_get_current_type (reader)) != DBUS_TYPE_INVALID)

47 {

48 switch (current_type)

49 {

50 case DBUS_TYPE_BYTE:

51 ++p;

52 break;

53

54 case DBUS_TYPE_INT16:

55 case DBUS_TYPE_UINT16:

56 {

57 p = \_DBUS_ALIGN_ADDRESS (p, 2);

58 \*((dbus_uint16_t \*) (void \*) p) =

59 DBUS_UINT16_SWAP_LE_BE (\*((dbus_uint16_t \*) (void \*) p));

60 p += 2;

61 }

62 break;

63

64 case DBUS_TYPE_BOOLEAN:

65 case DBUS_TYPE_INT32:

66 case DBUS_TYPE_UINT32:

67 case DBUS_TYPE_UNIX_FD:

68 {

69 p = \_DBUS_ALIGN_ADDRESS (p, 4);

70 \*((dbus_uint32_t \*) (void \*) p) =

71 DBUS_UINT32_SWAP_LE_BE (\*((dbus_uint32_t \*) (void \*) p));

72 p += 4;

73 }

74 break;

75

76 case DBUS_TYPE_INT64:

77 case DBUS_TYPE_UINT64:

78 case DBUS_TYPE_DOUBLE:

79 {

80 p = \_DBUS_ALIGN_ADDRESS (p, 8);

81 \*((dbus_uint64_t \*) (void \*) p) =

82 DBUS_UINT64_SWAP_LE_BE (\*((dbus_uint64_t \*) (void \*) p));

83 p += 8;

84 }

85 break;

86

87 case DBUS_TYPE_ARRAY:

88 case DBUS_TYPE_STRING:

89 case DBUS_TYPE_OBJECT_PATH:

90 {

91 dbus_uint32_t array_len;

92

93 p = \_DBUS_ALIGN_ADDRESS (p, 4);

94

95 array_len = \_dbus_unpack_uint32 (old_byte_order, p);

96

97 \*((dbus_uint32_t \*) (void \*) p) =

98 DBUS_UINT32_SWAP_LE_BE (\*((dbus_uint32_t \*) (void \*) p));

99 p += 4;

100

101 if (current_type == DBUS_TYPE_ARRAY)

102 {

103 int elem_type;

104 int alignment;

105

106 elem_type = \_dbus_type_reader_get_element_type (reader);

107 alignment = \_dbus_type_get_alignment (elem_type);

108

109 \_dbus_assert ((array_len / alignment) \< DBUS_MAXIMUM_ARRAY_LENGTH);

110

111 p = \_DBUS_ALIGN_ADDRESS (p, alignment);

112

113 if (dbus_type_is_fixed (elem_type))

114 {

115 if (alignment \> 1)

116 \_dbus_swap_array (p, array_len / alignment, alignment);

117 p += array_len;

118 }

119 else

120 {

121 DBusTypeReader sub;

122 const unsigned char \*array_end;

123

124 array_end = p + array_len;

125

126 \_dbus_type_reader_recurse (reader, &sub);

127

128 while (p \< array_end)

129 {

130 byteswap_body_helper (&sub,

131 FALSE,

132 old_byte_order,

133 new_byte_order,

134 p, &p);

135 }

136 }

137 }

138 else

139 {

140 \_dbus_assert (current_type == DBUS_TYPE_STRING \|\|

141 current_type == DBUS_TYPE_OBJECT_PATH);

142

143 p += (array_len + 1); /\* + 1 for nul \*/

144 }

145 }

146 break;

147

148 case DBUS_TYPE_SIGNATURE:

149 {

150 dbus_uint32_t sig_len;

151

152 sig_len = \*p;

153

154 p += (sig_len + 2); /\* +2 for len and nul \*/

155 }

156 break;

157

158 case DBUS_TYPE_VARIANT:

159 {

160 /\* 1 byte sig len, sig typecodes, align to

161 \* contained-type-boundary, values.

162 \*/

163 dbus_uint32_t sig_len;

164 DBusString sig;

165 DBusTypeReader sub;

166 int contained_alignment;

167

168 sig_len = \*p;

169 ++p;

170

171 \_dbus_string_init_const_len (&sig, (const char \*) p, sig_len);

172

173 p += (sig_len + 1); /\* 1 for nul \*/

174

175 contained_alignment = \_dbus_type_get_alignment (\_dbus_first_type_in_signature (&sig, 0));

176

177 p = \_DBUS_ALIGN_ADDRESS (p, contained_alignment);

178

179 \_dbus_type_reader_init_types_only (&sub, &sig, 0);

180

181 byteswap_body_helper (&sub, FALSE, old_byte_order, new_byte_order, p, &p);

182 }

183 break;

184

185 case DBUS_TYPE_STRUCT:

186 case DBUS_TYPE_DICT_ENTRY:

187 {

188 DBusTypeReader sub;

189

190 p = \_DBUS_ALIGN_ADDRESS (p, 8);

191

192 \_dbus_type_reader_recurse (reader, &sub);

193

194 byteswap_body_helper (&sub, TRUE, old_byte_order, new_byte_order, p, &p);

195 }

196 break;

197

198 default:

199 \_dbus_assert_not_reached ("invalid typecode in supposedly-validated signature");

200 break;

201 }

202

203 if (walk_reader_to_end)

204 \_dbus_type_reader_next (reader);

205 else

206 break;

207 }

208

209 if (new_p)

210 \*new_p = p;

211}

212

223void

224\_dbus_marshal_byteswap (const DBusString \*signature,

225 int signature_start,

226 int old_byte_order,

227 int new_byte_order,

228 DBusString \*value_str,

229 int value_pos)

230{

231 DBusTypeReader reader;

232

233 \_dbus_assert (value_pos \>= 0);

234 \_dbus_assert (value_pos \<= \_dbus_string_get_length (value_str));

235

236 if (old_byte_order == new_byte_order)

237 return;

238

239 \_dbus_type_reader_init_types_only (&reader,

240 signature, signature_start);

241

242 byteswap_body_helper (&reader, TRUE,

243 old_byte_order, new_byte_order,

244 \_dbus_string_get_udata_len (value_str, value_pos, 0),

245 NULL);

246}

247

250/\* Tests in dbus-marshal-byteswap-util.c \*/

\_dbus_assert_not_reached

\#define \_dbus_assert_not_reached(explanation)

Aborts with an error message if called.

**Definition** dbus-internals.h:164

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

NULL

\#define NULL

A null pointer, defined appropriately for C or C++.

**Definition** dbus-macros.h:51

TRUE

\#define TRUE

Expands to "1".

**Definition** dbus-macros.h:41

FALSE

\#define FALSE

Expands to "0".

**Definition** dbus-macros.h:44

\_dbus_type_reader_recurse

void \_dbus_type_reader_recurse(DBusTypeReader \*reader, DBusTypeReader \*sub)

Initialize a new reader pointing to the first type and corresponding value that's a child of the curr...

**Definition** dbus-marshal-recursive.c:987

\_dbus_type_get_alignment

int \_dbus_type_get_alignment(int typecode)

Gets the alignment requirement for the given type; will be 1, 2, 4, or 8.

**Definition** dbus-marshal-basic.c:1244

\_dbus_type_reader_init_types_only

void \_dbus_type_reader_init_types_only(DBusTypeReader \*reader, const DBusString \*type_str, int type_pos)

Like \_dbus_type_reader_init() but the iteration is over the signature, not over values.

**Definition** dbus-marshal-recursive.c:760

\_dbus_unpack_uint32

dbus_uint32_t \_dbus_unpack_uint32(int byte_order, const unsigned char \*data)

Unpacks a 32 bit unsigned integer from a data pointer.

**Definition** dbus-marshal-basic.c:189

\_dbus_first_type_in_signature

int \_dbus_first_type_in_signature(const DBusString \*str, int pos)

Get the first type in the signature.

**Definition** dbus-marshal-basic.c:1484

\_dbus_marshal_byteswap

void \_dbus_marshal_byteswap(const DBusString \*signature, int signature_start, int old_byte_order, int new_byte_order, DBusString \*value_str, int value_pos)

Byteswaps the marshaled data in the given value_str.

**Definition** dbus-marshal-byteswap.c:224

\_dbus_type_reader_get_element_type

int \_dbus_type_reader_get_element_type(const DBusTypeReader \*reader)

Gets the type of an element of the array the reader is currently pointing to.

**Definition** dbus-marshal-recursive.c:820

\_dbus_type_reader_next

dbus_bool_t \_dbus_type_reader_next(DBusTypeReader \*reader)

Skip to the next value on this "level".

**Definition** dbus-marshal-recursive.c:1053

\_dbus_type_reader_get_current_type

int \_dbus_type_reader_get_current_type(const DBusTypeReader \*reader)

Gets the type of the value the reader is currently pointing to; or for a types-only reader gets the t...

**Definition** dbus-marshal-recursive.c:785

\_dbus_swap_array

void \_dbus_swap_array(unsigned char \*data, int n_elements, int alignment)

Swaps the elements of an array to the opposite byte order.

**Definition** dbus-marshal-basic.c:927

DBUS_TYPE_SIGNATURE

\#define DBUS_TYPE_SIGNATURE

Type code marking a D-Bus type signature.

**Definition** dbus-protocol.h:112

DBUS_TYPE_OBJECT_PATH

\#define DBUS_TYPE_OBJECT_PATH

Type code marking a D-Bus object path.

**Definition** dbus-protocol.h:108

DBUS_TYPE_BYTE

\#define DBUS_TYPE_BYTE

Type code marking an 8-bit unsigned integer.

**Definition** dbus-protocol.h:68

DBUS_TYPE_INT16

\#define DBUS_TYPE_INT16

Type code marking a 16-bit signed integer.

**Definition** dbus-protocol.h:76

DBUS_TYPE_VARIANT

\#define DBUS_TYPE_VARIANT

Type code marking a D-Bus variant type.

**Definition** dbus-protocol.h:126

DBUS_MAXIMUM_ARRAY_LENGTH

\#define DBUS_MAXIMUM_ARRAY_LENGTH

Max length of a marshaled array in bytes (64M, 2^26) We use signed int for lengths so must be INT_MAX...

**Definition** dbus-protocol.h:205

DBUS_TYPE_INT32

\#define DBUS_TYPE_INT32

Type code marking a 32-bit signed integer.

**Definition** dbus-protocol.h:84

DBUS_TYPE_UNIX_FD

\#define DBUS_TYPE_UNIX_FD

Type code marking a unix file descriptor.

**Definition** dbus-protocol.h:116

DBUS_TYPE_BOOLEAN

\#define DBUS_TYPE_BOOLEAN

Type code marking a boolean.

**Definition** dbus-protocol.h:72

DBUS_TYPE_STRING

\#define DBUS_TYPE_STRING

Type code marking a UTF-8 encoded, nul-terminated Unicode string.

**Definition** dbus-protocol.h:104

DBUS_TYPE_ARRAY

\#define DBUS_TYPE_ARRAY

Type code marking a D-Bus array type.

**Definition** dbus-protocol.h:122

DBUS_TYPE_INVALID

\#define DBUS_TYPE_INVALID

Type code that is never equal to a legitimate type code.

**Definition** dbus-protocol.h:62

DBUS_TYPE_INT64

\#define DBUS_TYPE_INT64

Type code marking a 64-bit signed integer.

**Definition** dbus-protocol.h:92

DBUS_TYPE_DOUBLE

\#define DBUS_TYPE_DOUBLE

Type code marking an 8-byte double in IEEE 754 format.

**Definition** dbus-protocol.h:100

DBUS_TYPE_UINT64

\#define DBUS_TYPE_UINT64

Type code marking a 64-bit unsigned integer.

**Definition** dbus-protocol.h:96

DBUS_TYPE_DICT_ENTRY

\#define DBUS_TYPE_DICT_ENTRY

Type code used to represent a dict entry; however, this type code does not appear in type signatures,...

**Definition** dbus-protocol.h:145

DBUS_TYPE_UINT16

\#define DBUS_TYPE_UINT16

Type code marking a 16-bit unsigned integer.

**Definition** dbus-protocol.h:80

DBUS_TYPE_STRUCT

\#define DBUS_TYPE_STRUCT

STRUCT and DICT_ENTRY are sort of special since their codes can't appear in a type string,...

**Definition** dbus-protocol.h:138

DBUS_TYPE_UINT32

\#define DBUS_TYPE_UINT32

Type code marking a 32-bit unsigned integer.

**Definition** dbus-protocol.h:88

dbus_type_is_fixed

dbus_bool_t dbus_type_is_fixed(int typecode)

Tells you whether values of this type can change length if you set them to some other value.

**Definition** dbus-signature.c:355

\_dbus_string_init_const_len

void \_dbus_string_init_const_len(DBusString \*str, const char \*value, int len)

Initializes a constant string with a length.

**Definition** dbus-string.c:217

\_dbus_string_get_length

int \_dbus_string_get_length(const DBusString \*str)

Gets the length of a string (not including nul termination).

**Definition** dbus-string.c:784

DBusString

**Definition** dbus-string.h:47

DBusTypeReader

The type reader is an iterator for reading values from a block of values.

**Definition** dbus-marshal-recursive.h:42
