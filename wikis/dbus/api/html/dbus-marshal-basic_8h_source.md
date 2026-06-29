dbus-marshal-basic.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-marshal-basic.h Marshalling routines for basic (primitive) types

3 \*

4 \* Copyright (C) 2002 CodeFactory AB

5 \* Copyright (C) 2004, 2005 Red Hat, Inc.

6 \*

7 \* SPDX-License-Identifier: AFL-2.1 OR GPL-2.0-or-later

8 \*

9 \* Licensed under the Academic Free License version 2.1

10 \*

11 \* This program is free software; you can redistribute it and/or modify

12 \* it under the terms of the GNU General Public License as published by

13 \* the Free Software Foundation; either version 2 of the License, or

14 \* (at your option) any later version.

15 \*

16 \* This program is distributed in the hope that it will be useful,

17 \* but WITHOUT ANY WARRANTY; without even the implied warranty of

18 \* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

19 \* GNU General Public License for more details.

20 \*

21 \* You should have received a copy of the GNU General Public License

22 \* along with this program; if not, write to the Free Software

23 \* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

24 \*

25 \*/

26

27\#ifndef DBUS_MARSHAL_BASIC_H

28\#define DBUS_MARSHAL_BASIC_H

29

30\#ifdef HAVE_BYTESWAP_H

31\#include \<byteswap.h\>

32\#endif

33

34\#include \<dbus/dbus-protocol.h\>

35\#include \<dbus/dbus-types.h\>

36\#include \<dbus/dbus-arch-deps.h\>

37\#include \<dbus/dbus-string.h\>

38

39\#ifdef WORDS_BIGENDIAN

40\#define DBUS_COMPILER_BYTE_ORDER DBUS_BIG_ENDIAN

41\#else

42\#define DBUS_COMPILER_BYTE_ORDER DBUS_LITTLE_ENDIAN

43\#endif

44

45\#ifdef HAVE_BYTESWAP_H

46\#define DBUS_UINT16_SWAP_LE_BE_CONSTANT(val) bswap_16(val)

47\#define DBUS_UINT32_SWAP_LE_BE_CONSTANT(val) bswap_32(val)

48\#else /\* HAVE_BYTESWAP_H \*/

49

50\#define DBUS_UINT16_SWAP_LE_BE_CONSTANT(val) ((dbus_uint16_t) ( \\

51 (dbus_uint16_t) ((dbus_uint16_t) (val) \>\> 8) \| \\

52 (dbus_uint16_t) ((dbus_uint16_t) (val) \<\< 8)))

53

54\#define DBUS_UINT32_SWAP_LE_BE_CONSTANT(val) ((dbus_uint32_t) ( \\

55 (((dbus_uint32_t) (val) & (dbus_uint32_t) 0x000000ffU) \<\< 24) \| \\

56 (((dbus_uint32_t) (val) & (dbus_uint32_t) 0x0000ff00U) \<\< 8) \| \\

57 (((dbus_uint32_t) (val) & (dbus_uint32_t) 0x00ff0000U) \>\> 8) \| \\

58 (((dbus_uint32_t) (val) & (dbus_uint32_t) 0xff000000U) \>\> 24)))

59

60\#endif /\* HAVE_BYTESWAP_H \*/

61

62\#ifdef HAVE_BYTESWAP_H

63\#define DBUS_UINT64_SWAP_LE_BE_CONSTANT(val) bswap_64(val)

64\#else /\* HAVE_BYTESWAP_H \*/

65

66\#define DBUS_UINT64_SWAP_LE_BE_CONSTANT(val) ((dbus_uint64_t) ( \\

67 (((dbus_uint64_t) (val) & \\

68 (dbus_uint64_t) DBUS_UINT64_CONSTANT (0x00000000000000ff)) \<\< 56) \| \\

69 (((dbus_uint64_t) (val) & \\

70 (dbus_uint64_t) DBUS_UINT64_CONSTANT (0x000000000000ff00)) \<\< 40) \| \\

71 (((dbus_uint64_t) (val) & \\

72 (dbus_uint64_t) DBUS_UINT64_CONSTANT (0x0000000000ff0000)) \<\< 24) \| \\

73 (((dbus_uint64_t) (val) & \\

74 (dbus_uint64_t) DBUS_UINT64_CONSTANT (0x00000000ff000000)) \<\< 8) \| \\

75 (((dbus_uint64_t) (val) & \\

76 (dbus_uint64_t) DBUS_UINT64_CONSTANT (0x000000ff00000000)) \>\> 8) \| \\

77 (((dbus_uint64_t) (val) & \\

78 (dbus_uint64_t) DBUS_UINT64_CONSTANT (0x0000ff0000000000)) \>\> 24) \| \\

79 (((dbus_uint64_t) (val) & \\

80 (dbus_uint64_t) DBUS_UINT64_CONSTANT (0x00ff000000000000)) \>\> 40) \| \\

81 (((dbus_uint64_t) (val) & \\

82 (dbus_uint64_t) DBUS_UINT64_CONSTANT (0xff00000000000000)) \>\> 56)))

83

84\#endif /\* HAVE_BYTESWAP_H \*/

85

86\#define DBUS_UINT16_SWAP_LE_BE(val) (DBUS_UINT16_SWAP_LE_BE_CONSTANT (val))

87\#define DBUS_INT16_SWAP_LE_BE(val) ((dbus_int16_t)DBUS_UINT16_SWAP_LE_BE_CONSTANT (val))

88

89\#define DBUS_UINT32_SWAP_LE_BE(val) (DBUS_UINT32_SWAP_LE_BE_CONSTANT (val))

90\#define DBUS_INT32_SWAP_LE_BE(val) ((dbus_int32_t)DBUS_UINT32_SWAP_LE_BE_CONSTANT (val))

91

92\#define DBUS_UINT64_SWAP_LE_BE(val) (DBUS_UINT64_SWAP_LE_BE_CONSTANT (val))

93\#define DBUS_INT64_SWAP_LE_BE(val) ((dbus_int64_t)DBUS_UINT64_SWAP_LE_BE_CONSTANT (val))

94

95\#ifdef WORDS_BIGENDIAN

96

97\# define DBUS_INT16_TO_BE(val) ((dbus_int16_t) (val))

98\# define DBUS_UINT16_TO_BE(val) ((dbus_uint16_t) (val))

99\# define DBUS_INT16_TO_LE(val) (DBUS_INT16_SWAP_LE_BE (val))

100\# define DBUS_UINT16_TO_LE(val) (DBUS_UINT16_SWAP_LE_BE (val))

101\# define DBUS_INT32_TO_BE(val) ((dbus_int32_t) (val))

102\# define DBUS_UINT32_TO_BE(val) ((dbus_uint32_t) (val))

103\# define DBUS_INT32_TO_LE(val) (DBUS_INT32_SWAP_LE_BE (val))

104\# define DBUS_UINT32_TO_LE(val) (DBUS_UINT32_SWAP_LE_BE (val))

105\# define DBUS_INT64_TO_BE(val) ((dbus_int64_t) (val))

106\# define DBUS_UINT64_TO_BE(val) ((dbus_uint64_t) (val))

107\# define DBUS_INT64_TO_LE(val) (DBUS_INT64_SWAP_LE_BE (val))

108\# define DBUS_UINT64_TO_LE(val) (DBUS_UINT64_SWAP_LE_BE (val))

109

110\#else /\* WORDS_BIGENDIAN \*/

111

112\# define DBUS_INT16_TO_LE(val) ((dbus_int16_t) (val))

113\# define DBUS_UINT16_TO_LE(val) ((dbus_uint16_t) (val))

114\# define DBUS_INT16_TO_BE(val) ((dbus_int16_t) DBUS_UINT16_SWAP_LE_BE (val))

115\# define DBUS_UINT16_TO_BE(val) (DBUS_UINT16_SWAP_LE_BE (val))

116\# define DBUS_INT32_TO_LE(val) ((dbus_int32_t) (val))

117\# define DBUS_UINT32_TO_LE(val) ((dbus_uint32_t) (val))

118\# define DBUS_INT32_TO_BE(val) ((dbus_int32_t) DBUS_UINT32_SWAP_LE_BE (val))

119\# define DBUS_UINT32_TO_BE(val) (DBUS_UINT32_SWAP_LE_BE (val))

120\# define DBUS_INT64_TO_LE(val) ((dbus_int64_t) (val))

121\# define DBUS_UINT64_TO_LE(val) ((dbus_uint64_t) (val))

122\# define DBUS_INT64_TO_BE(val) ((dbus_int64_t) DBUS_UINT64_SWAP_LE_BE (val))

123\# define DBUS_UINT64_TO_BE(val) (DBUS_UINT64_SWAP_LE_BE (val))

124\#endif

125

126/\* The transformation is symmetric, so the FROM just maps to the TO. \*/

127\#define DBUS_INT16_FROM_LE(val) (DBUS_INT16_TO_LE (val))

128\#define DBUS_UINT16_FROM_LE(val) (DBUS_UINT16_TO_LE (val))

129\#define DBUS_INT16_FROM_BE(val) (DBUS_INT16_TO_BE (val))

130\#define DBUS_UINT16_FROM_BE(val) (DBUS_UINT16_TO_BE (val))

131\#define DBUS_INT32_FROM_LE(val) (DBUS_INT32_TO_LE (val))

132\#define DBUS_UINT32_FROM_LE(val) (DBUS_UINT32_TO_LE (val))

133\#define DBUS_INT32_FROM_BE(val) (DBUS_INT32_TO_BE (val))

134\#define DBUS_UINT32_FROM_BE(val) (DBUS_UINT32_TO_BE (val))

135\#define DBUS_INT64_FROM_LE(val) (DBUS_INT64_TO_LE (val))

136\#define DBUS_UINT64_FROM_LE(val) (DBUS_UINT64_TO_LE (val))

137\#define DBUS_INT64_FROM_BE(val) (DBUS_INT64_TO_BE (val))

138\#define DBUS_UINT64_FROM_BE(val) (DBUS_UINT64_TO_BE (val))

139

140\#ifdef DBUS_DISABLE_ASSERT

141\#define \_dbus_unpack_uint16(byte_order, data) \\

142 (((byte_order) == DBUS_LITTLE_ENDIAN) ? \\

143 DBUS_UINT16_FROM_LE (\*(dbus_uint16_t\*)(data)) : \\

144 DBUS_UINT16_FROM_BE (\*(dbus_uint16_t\*)(data)))

145

146\#define \_dbus_unpack_uint32(byte_order, data) \\

147 (((byte_order) == DBUS_LITTLE_ENDIAN) ? \\

148 DBUS_UINT32_FROM_LE (\*(dbus_uint32_t\*)(data)) : \\

149 DBUS_UINT32_FROM_BE (\*(dbus_uint32_t\*)(data)))

150\#endif

151

152\#ifndef \_dbus_unpack_uint16

153DBUS_PRIVATE_EXPORT

154dbus_uint16_t \_dbus_unpack_uint16 (int byte_order,

155 const unsigned char \*data);

156\#endif

157

158void \_dbus_pack_uint32 (dbus_uint32_t value,

159 int byte_order,

160 unsigned char \*data);

161\#ifndef \_dbus_unpack_uint32

162DBUS_PRIVATE_EXPORT

163dbus_uint32_t \_dbus_unpack_uint32 (int byte_order,

164 const unsigned char \*data);

165\#endif

166

167dbus_bool_t \_dbus_marshal_set_basic (DBusString \*str,

168 int pos,

169 int type,

170 const void \*value,

171 int byte_order,

172 int \*old_end_pos,

173 int \*new_end_pos);

174dbus_bool_t \_dbus_marshal_write_basic (DBusString \*str,

175 int insert_at,

176 int type,

177 const void \*value,

178 int byte_order,

179 int \*pos_after);

180dbus_bool_t \_dbus_marshal_write_fixed_multi (DBusString \*str,

181 int insert_at,

182 int element_type,

183 const void \*value,

184 int n_elements,

185 int byte_order,

186 int \*pos_after);

187void \_dbus_marshal_read_basic (const DBusString \*str,

188 int pos,

189 int type,

190 void \*value,

191 int byte_order,

192 int \*new_pos);

193void \_dbus_marshal_read_fixed_multi (const DBusString \*str,

194 int pos,

195 int element_type,

196 const void \*\*value,

197 int n_elements,

198 int byte_order,

199 int \*new_pos);

200void \_dbus_marshal_skip_basic (const DBusString \*str,

201 int type,

202 int byte_order,

203 int \*pos);

204void \_dbus_marshal_skip_array (const DBusString \*str,

205 int element_type,

206 int byte_order,

207 int \*pos);

208DBUS_PRIVATE_EXPORT

209void \_dbus_marshal_set_uint32 (DBusString \*str,

210 int pos,

211 dbus_uint32_t value,

212 int byte_order);

213DBUS_PRIVATE_EXPORT

214dbus_uint32_t \_dbus_marshal_read_uint32 (const DBusString \*str,

215 int pos,

216 int byte_order,

217 int \*new_pos);

218int \_dbus_type_get_alignment (int typecode);

219DBUS_PRIVATE_EXPORT

220const char\* \_dbus_type_to_string (int typecode);

221

222DBUS_PRIVATE_EXPORT

223int \_dbus_first_type_in_signature (const DBusString \*str,

224 int pos);

225

226int \_dbus_first_type_in_signature_c_str (const char \*str,

227 int pos);

228

229void \_dbus_swap_array (unsigned char \*data,

230 int n_elements,

231 int alignment);

232

233\#endif /\* DBUS_MARSHAL_BASIC_H \*/

\_dbus_unpack_uint16

DBUS_PRIVATE_EXPORT dbus_uint16_t \_dbus_unpack_uint16(int byte_order, const unsigned char \*data)

Unpacks a 16 bit unsigned integer from a data pointer.

**Definition** dbus-marshal-basic.c:168

\_dbus_type_get_alignment

int \_dbus_type_get_alignment(int typecode)

Gets the alignment requirement for the given type; will be 1, 2, 4, or 8.

**Definition** dbus-marshal-basic.c:1244

\_dbus_pack_uint32

void \_dbus_pack_uint32(dbus_uint32_t value, int byte_order, unsigned char \*data)

Packs a 32 bit unsigned integer into a data pointer.

**Definition** dbus-marshal-basic.c:142

\_dbus_marshal_set_uint32

DBUS_PRIVATE_EXPORT void \_dbus_marshal_set_uint32(DBusString \*str, int pos, dbus_uint32_t value, int byte_order)

Sets the 4 bytes at the given offset to a marshaled unsigned integer, replacing anything found there ...

**Definition** dbus-marshal-basic.c:260

\_dbus_unpack_uint32

DBUS_PRIVATE_EXPORT dbus_uint32_t \_dbus_unpack_uint32(int byte_order, const unsigned char \*data)

Unpacks a 32 bit unsigned integer from a data pointer.

**Definition** dbus-marshal-basic.c:189

\_dbus_marshal_write_basic

dbus_bool_t \_dbus_marshal_write_basic(DBusString \*str, int insert_at, int type, const void \*value, int byte_order, int \*pos_after)

Marshals a basic-typed value.

**Definition** dbus-marshal-basic.c:817

\_dbus_first_type_in_signature

DBUS_PRIVATE_EXPORT int \_dbus_first_type_in_signature(const DBusString \*str, int pos)

Get the first type in the signature.

**Definition** dbus-marshal-basic.c:1484

\_dbus_first_type_in_signature_c_str

int \_dbus_first_type_in_signature_c_str(const char \*str, int pos)

Similar to \_dbus_first_type_in_signature, but operates on a C string buffer.

**Definition** dbus-marshal-basic.c:1499

\_dbus_marshal_read_uint32

DBUS_PRIVATE_EXPORT dbus_uint32_t \_dbus_marshal_read_uint32(const DBusString \*str, int pos, int byte_order, int \*new_pos)

Convenience function to demarshal a 32 bit unsigned integer.

**Definition** dbus-marshal-basic.c:476

\_dbus_marshal_set_basic

dbus_bool_t \_dbus_marshal_set_basic(DBusString \*str, int pos, int type, const void \*value, int byte_order, int \*old_end_pos, int \*new_end_pos)

Sets an existing basic type value to a new value.

**Definition** dbus-marshal-basic.c:377

\_dbus_marshal_skip_array

void \_dbus_marshal_skip_array(const DBusString \*str, int element_type, int byte_order, int \*pos)

Skips an array, returning the next position.

**Definition** dbus-marshal-basic.c:1205

\_dbus_marshal_write_fixed_multi

dbus_bool_t \_dbus_marshal_write_fixed_multi(DBusString \*str, int insert_at, int element_type, const void \*value, int n_elements, int byte_order, int \*pos_after)

Marshals a block of values of fixed-length type all at once, as an optimization.

**Definition** dbus-marshal-basic.c:1059

\_dbus_type_to_string

DBUS_PRIVATE_EXPORT const char \* \_dbus_type_to_string(int typecode)

Returns a string describing the given type.

**Definition** dbus-marshal-basic.c:1290

\_dbus_marshal_read_basic

void \_dbus_marshal_read_basic(const DBusString \*str, int pos, int type, void \*value, int byte_order, int \*new_pos)

Demarshals a basic-typed value.

**Definition** dbus-marshal-basic.c:514

\_dbus_swap_array

void \_dbus_swap_array(unsigned char \*data, int n_elements, int alignment)

Swaps the elements of an array to the opposite byte order.

**Definition** dbus-marshal-basic.c:927

\_dbus_marshal_skip_basic

void \_dbus_marshal_skip_basic(const DBusString \*str, int type, int byte_order, int \*pos)

Skips over a basic-typed value, reporting the following position.

**Definition** dbus-marshal-basic.c:1130

DBusString

**Definition** dbus-string.h:47
