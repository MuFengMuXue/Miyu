dbus-marshal-recursive.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-marshal-recursive.h Marshalling routines for recursive types

3 \*

4 \* Copyright (C) 2004, 2005 Red Hat, Inc.

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

26\#ifndef DBUS_MARSHAL_RECURSIVE_H

27\#define DBUS_MARSHAL_RECURSIVE_H

28

29\#include \<dbus/dbus-protocol.h\>

30\#include \<dbus/dbus-list.h\>

31

32typedef struct DBusTypeReader DBusTypeReader;

33typedef struct DBusTypeWriter DBusTypeWriter;

34typedef struct DBusTypeReaderClass DBusTypeReaderClass;

35typedef struct DBusArrayLenFixup DBusArrayLenFixup;

36

41struct DBusTypeReader

42{

43 const DBusTypeReaderClass \*klass;

44 const DBusString \*type_str;

45 const DBusString \*value_str;

47 dbus_uint32_t byte_order : 8;

49 dbus_uint32_t finished : 1;

52 dbus_uint32_t array_len_offset : 3;

53 int type_pos;

54 int value_pos;

56 union

57 {

58 struct {

59 int start_pos;

60 } array;

61 } u;

62};

63

67struct DBusTypeWriter

68{

69 DBusString \*type_str;

70 DBusString \*value_str;

71 dbus_uint32_t byte_order : 8;

73 dbus_uint32_t container_type : 8;

75 dbus_uint32_t type_pos_is_expectation : 1;

77 dbus_uint32_t enabled : 1;

79 int type_pos;

80 int value_pos;

82 union

83 {

84 struct {

85 int start_pos;

86 int len_pos;

87 int element_type_pos;

88 } array;

89 } u;

90};

91

96struct DBusArrayLenFixup

97{

98 int len_pos_in_reader;

99 int new_len;

100};

101

102DBUS_PRIVATE_EXPORT

103void \_dbus_type_reader_init (DBusTypeReader \*reader,

104 int byte_order,

105 const DBusString \*type_str,

106 int type_pos,

107 const DBusString \*value_str,

108 int value_pos);

109DBUS_PRIVATE_EXPORT

110void \_dbus_type_reader_init_types_only (DBusTypeReader \*reader,

111 const DBusString \*type_str,

112 int type_pos);

113DBUS_PRIVATE_EXPORT

114int \_dbus_type_reader_get_current_type (const DBusTypeReader \*reader);

115DBUS_PRIVATE_EXPORT

116int \_dbus_type_reader_get_element_type (const DBusTypeReader \*reader);

117DBUS_PRIVATE_EXPORT

118int \_dbus_type_reader_get_value_pos (const DBusTypeReader \*reader);

119DBUS_PRIVATE_EXPORT

120void \_dbus_type_reader_read_basic (const DBusTypeReader \*reader,

121 void \*value);

122int \_dbus_type_reader_get_array_length (const DBusTypeReader \*reader);

123DBUS_PRIVATE_EXPORT

124void \_dbus_type_reader_read_fixed_multi (const DBusTypeReader \*reader,

125 const void \*\*value,

126 int \*n_elements);

127void \_dbus_type_reader_read_raw (const DBusTypeReader \*reader,

128 const unsigned char \*\*value_location);

129DBUS_PRIVATE_EXPORT

130void \_dbus_type_reader_recurse (DBusTypeReader \*reader,

131 DBusTypeReader \*subreader);

132DBUS_PRIVATE_EXPORT

133dbus_bool_t \_dbus_type_reader_next (DBusTypeReader \*reader);

134dbus_bool_t \_dbus_type_reader_has_next (const DBusTypeReader \*reader);

135DBUS_PRIVATE_EXPORT

136void \_dbus_type_reader_get_signature (const DBusTypeReader \*reader,

137 const DBusString \*\*str_p,

138 int \*start_p,

139 int \*len_p);

140DBUS_PRIVATE_EXPORT

141dbus_bool_t \_dbus_type_reader_set_basic (DBusTypeReader \*reader,

142 const void \*value,

143 const DBusTypeReader \*realign_root);

144DBUS_PRIVATE_EXPORT

145dbus_bool_t \_dbus_type_reader_delete (DBusTypeReader \*reader,

146 const DBusTypeReader \*realign_root);

147

148dbus_bool_t \_dbus_type_reader_equal_values (const DBusTypeReader \*lhs,

149 const DBusTypeReader \*rhs);

150

151void \_dbus_type_signature_next (const char \*signature,

152 int \*type_pos);

153

154DBUS_PRIVATE_EXPORT

155void \_dbus_type_writer_init (DBusTypeWriter \*writer,

156 int byte_order,

157 DBusString \*type_str,

158 int type_pos,

159 DBusString \*value_str,

160 int value_pos);

161void \_dbus_type_writer_init_types_delayed (DBusTypeWriter \*writer,

162 int byte_order,

163 DBusString \*value_str,

164 int value_pos);

165void \_dbus_type_writer_add_types (DBusTypeWriter \*writer,

166 DBusString \*type_str,

167 int type_pos);

168void \_dbus_type_writer_remove_types (DBusTypeWriter \*writer);

169DBUS_PRIVATE_EXPORT

170void \_dbus_type_writer_init_values_only (DBusTypeWriter \*writer,

171 int byte_order,

172 const DBusString \*type_str,

173 int type_pos,

174 DBusString \*value_str,

175 int value_pos);

176DBUS_PRIVATE_EXPORT

177dbus_bool_t \_dbus_type_writer_write_basic (DBusTypeWriter \*writer,

178 int type,

179 const void \*value);

180DBUS_PRIVATE_EXPORT

181dbus_bool_t \_dbus_type_writer_write_fixed_multi (DBusTypeWriter \*writer,

182 int element_type,

183 const void \*value,

184 int n_elements);

185DBUS_PRIVATE_EXPORT

186dbus_bool_t \_dbus_type_writer_recurse (DBusTypeWriter \*writer,

187 int container_type,

188 const DBusString \*contained_type,

189 int contained_type_start,

190 DBusTypeWriter \*sub);

191DBUS_PRIVATE_EXPORT

192dbus_bool_t \_dbus_type_writer_unrecurse (DBusTypeWriter \*writer,

193 DBusTypeWriter \*sub);

194dbus_bool_t \_dbus_type_writer_append_array (DBusTypeWriter \*writer,

195 const DBusString \*contained_type,

196 int contained_type_start,

197 DBusTypeWriter \*sub);

198DBUS_PRIVATE_EXPORT

199dbus_bool_t \_dbus_type_writer_write_reader (DBusTypeWriter \*writer,

200 DBusTypeReader \*reader);

201

202

203\#endif /\* DBUS_MARSHAL_RECURSIVE_H \*/

\_dbus_type_writer_write_basic

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_type_writer_write_basic(DBusTypeWriter \*writer, int type, const void \*value)

Writes out a basic type.

**Definition** dbus-marshal-recursive.c:2310

\_dbus_type_reader_recurse

DBUS_PRIVATE_EXPORT void \_dbus_type_reader_recurse(DBusTypeReader \*reader, DBusTypeReader \*subreader)

Initialize a new reader pointing to the first type and corresponding value that's a child of the curr...

**Definition** dbus-marshal-recursive.c:987

\_dbus_type_writer_init_values_only

DBUS_PRIVATE_EXPORT void \_dbus_type_writer_init_values_only(DBusTypeWriter \*writer, int byte_order, const DBusString \*type_str, int type_pos, DBusString \*value_str, int value_pos)

Like \_dbus_type_writer_init(), except the type string passed in should correspond to an existing sign...

**Definition** dbus-marshal-recursive.c:1583

\_dbus_type_reader_get_value_pos

DBUS_PRIVATE_EXPORT int \_dbus_type_reader_get_value_pos(const DBusTypeReader \*reader)

Gets the current position in the value block.

**Definition** dbus-marshal-recursive.c:837

\_dbus_type_writer_remove_types

void \_dbus_type_writer_remove_types(DBusTypeWriter \*writer)

Removes type string from the writer.

**Definition** dbus-marshal-recursive.c:1562

\_dbus_type_reader_init

DBUS_PRIVATE_EXPORT void \_dbus_type_reader_init(DBusTypeReader \*reader, int byte_order, const DBusString \*type_str, int type_pos, const DBusString \*value_str, int value_pos)

Initializes a type reader.

**Definition** dbus-marshal-recursive.c:732

\_dbus_type_reader_init_types_only

DBUS_PRIVATE_EXPORT void \_dbus_type_reader_init_types_only(DBusTypeReader \*reader, const DBusString \*type_str, int type_pos)

Like \_dbus_type_reader_init() but the iteration is over the signature, not over values.

**Definition** dbus-marshal-recursive.c:760

\_dbus_type_reader_get_signature

DBUS_PRIVATE_EXPORT void \_dbus_type_reader_get_signature(const DBusTypeReader \*reader, const DBusString \*\*str_p, int \*start_p, int \*len_p)

Gets the string and range of said string containing the signature of the current value.

**Definition** dbus-marshal-recursive.c:1124

\_dbus_type_writer_write_reader

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_type_writer_write_reader(DBusTypeWriter \*writer, DBusTypeReader \*reader)

Iterate through all values in the given reader, writing a copy of each value to the writer.

**Definition** dbus-marshal-recursive.c:2730

\_dbus_type_writer_recurse

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_type_writer_recurse(DBusTypeWriter \*writer, int container_type, const DBusString \*contained_type, int contained_type_start, DBusTypeWriter \*sub)

Opens a new container and writes out the initial information for that container.

**Definition** dbus-marshal-recursive.c:2108

\_dbus_type_reader_read_fixed_multi

DBUS_PRIVATE_EXPORT void \_dbus_type_reader_read_fixed_multi(const DBusTypeReader \*reader, const void \*\*value, int \*n_elements)

Reads a block of fixed-length basic values, from the current point in an array to the end of the arra...

**Definition** dbus-marshal-recursive.c:923

\_dbus_type_reader_get_element_type

DBUS_PRIVATE_EXPORT int \_dbus_type_reader_get_element_type(const DBusTypeReader \*reader)

Gets the type of an element of the array the reader is currently pointing to.

**Definition** dbus-marshal-recursive.c:820

\_dbus_type_reader_next

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_type_reader_next(DBusTypeReader \*reader)

Skip to the next value on this "level".

**Definition** dbus-marshal-recursive.c:1053

\_dbus_type_reader_get_array_length

int \_dbus_type_reader_get_array_length(const DBusTypeReader \*reader)

Returns the number of bytes in the array.

**Definition** dbus-marshal-recursive.c:899

\_dbus_type_writer_add_types

void \_dbus_type_writer_add_types(DBusTypeWriter \*writer, DBusString \*type_str, int type_pos)

Adds type string to the writer, if it had none.

**Definition** dbus-marshal-recursive.c:1545

\_dbus_type_reader_has_next

dbus_bool_t \_dbus_type_reader_has_next(const DBusTypeReader \*reader)

Check whether there's another value on this "level".

**Definition** dbus-marshal-recursive.c:1093

\_dbus_type_reader_delete

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_type_reader_delete(DBusTypeReader \*reader, const DBusTypeReader \*realign_root)

Recursively deletes any value pointed to by the reader, leaving the reader valid to continue reading.

**Definition** dbus-marshal-recursive.c:1419

\_dbus_type_reader_read_basic

DBUS_PRIVATE_EXPORT void \_dbus_type_reader_read_basic(const DBusTypeReader \*reader, void \*value)

Reads a basic-typed value, as with \_dbus_marshal_read_basic().

**Definition** dbus-marshal-recursive.c:869

\_dbus_type_writer_init_types_delayed

void \_dbus_type_writer_init_types_delayed(DBusTypeWriter \*writer, int byte_order, DBusString \*value_str, int value_pos)

Initialize a write iterator, with the signature to be provided later.

**Definition** dbus-marshal-recursive.c:1527

\_dbus_type_reader_set_basic

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_type_reader_set_basic(DBusTypeReader \*reader, const void \*value, const DBusTypeReader \*realign_root)

Sets a new value for the basic type value pointed to by the reader, leaving the reader valid to conti...

**Definition** dbus-marshal-recursive.c:1362

\_dbus_type_reader_get_current_type

DBUS_PRIVATE_EXPORT int \_dbus_type_reader_get_current_type(const DBusTypeReader \*reader)

Gets the type of the value the reader is currently pointing to; or for a types-only reader gets the t...

**Definition** dbus-marshal-recursive.c:785

\_dbus_type_reader_read_raw

void \_dbus_type_reader_read_raw(const DBusTypeReader \*reader, const unsigned char \*\*value_location)

Get the address of the marshaled value in the data being read.

**Definition** dbus-marshal-recursive.c:852

\_dbus_type_writer_unrecurse

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_type_writer_unrecurse(DBusTypeWriter \*writer, DBusTypeWriter \*sub)

Closes a container created by \_dbus_type_writer_recurse() and writes any additional information to th...

**Definition** dbus-marshal-recursive.c:2178

\_dbus_type_writer_append_array

dbus_bool_t \_dbus_type_writer_append_array(DBusTypeWriter \*writer, const DBusString \*contained_type, int contained_type_start, DBusTypeWriter \*sub)

Append to an existing array.

**Definition** dbus-marshal-recursive.c:2142

\_dbus_type_writer_write_fixed_multi

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_type_writer_write_fixed_multi(DBusTypeWriter \*writer, int element_type, const void \*value, int n_elements)

Writes a block of fixed-length basic values, i.e.

**Definition** dbus-marshal-recursive.c:2358

\_dbus_type_writer_init

DBUS_PRIVATE_EXPORT void \_dbus_type_writer_init(DBusTypeWriter \*writer, int byte_order, DBusString \*type_str, int type_pos, DBusString \*value_str, int value_pos)

Initialize a write iterator, which is used to write out values in serialized D-Bus format.

**Definition** dbus-marshal-recursive.c:1492

\_dbus_type_signature_next

void \_dbus_type_signature_next(const char \*signature, int \*type_pos)

Skips to the next "complete" type inside a type signature.

**Definition** dbus-marshal-recursive.c:340

DBusArrayLenFixup

When modifying an existing block of values, array lengths may need to be adjusted; those adjustments ...

**Definition** dbus-marshal-recursive.h:97

DBusArrayLenFixup::new_len

int new_len

the new value of the length in the written-out block

**Definition** dbus-marshal-recursive.h:99

DBusArrayLenFixup::len_pos_in_reader

int len_pos_in_reader

where the length was in the original block

**Definition** dbus-marshal-recursive.h:98

DBusString

**Definition** dbus-string.h:47

DBusTypeReaderClass

Virtual table for a type reader.

**Definition** dbus-marshal-recursive.c:128

DBusTypeReader

The type reader is an iterator for reading values from a block of values.

**Definition** dbus-marshal-recursive.h:42

DBusTypeReader::type_pos

int type_pos

current position in signature

**Definition** dbus-marshal-recursive.h:53

DBusTypeReader::klass

const DBusTypeReaderClass \* klass

the vtable for the reader

**Definition** dbus-marshal-recursive.h:43

DBusTypeReader::u

union DBusTypeReader::@1 u

class-specific data

DBusTypeReader::value_str

const DBusString \* value_str

string containing values of block

**Definition** dbus-marshal-recursive.h:45

DBusTypeReader::finished

dbus_uint32_t finished

marks we're at end iterator for cases where we don't have another way to tell

**Definition** dbus-marshal-recursive.h:49

DBusTypeReader::start_pos

int start_pos

for array readers, the start of the array values

**Definition** dbus-marshal-recursive.h:59

DBusTypeReader::array_len_offset

dbus_uint32_t array_len_offset

bytes back from start_pos that len ends

**Definition** dbus-marshal-recursive.h:52

DBusTypeReader::value_pos

int value_pos

current position in values

**Definition** dbus-marshal-recursive.h:54

DBusTypeReader::byte_order

dbus_uint32_t byte_order

byte order of the block

**Definition** dbus-marshal-recursive.h:47

DBusTypeReader::type_str

const DBusString \* type_str

string containing signature of block

**Definition** dbus-marshal-recursive.h:44

DBusTypeWriter

The type writer is an iterator for writing to a block of values.

**Definition** dbus-marshal-recursive.h:68

DBusTypeWriter::element_type_pos

int element_type_pos

position of array element type in type_str

**Definition** dbus-marshal-recursive.h:87

DBusTypeWriter::start_pos

int start_pos

position of first element in the array

**Definition** dbus-marshal-recursive.h:85

DBusTypeWriter::value_pos

int value_pos

next position to write

**Definition** dbus-marshal-recursive.h:80

DBusTypeWriter::enabled

dbus_uint32_t enabled

whether to write values

**Definition** dbus-marshal-recursive.h:77

DBusTypeWriter::u

union DBusTypeWriter::@3 u

class-specific data

DBusTypeWriter::byte_order

dbus_uint32_t byte_order

byte order to write values with

**Definition** dbus-marshal-recursive.h:71

DBusTypeWriter::type_pos

int type_pos

current pos in type_str

**Definition** dbus-marshal-recursive.h:79

DBusTypeWriter::type_str

DBusString \* type_str

where to write typecodes (or read type expectations)

**Definition** dbus-marshal-recursive.h:69

DBusTypeWriter::len_pos

int len_pos

position of length of the array

**Definition** dbus-marshal-recursive.h:86

DBusTypeWriter::value_str

DBusString \* value_str

where to write values

**Definition** dbus-marshal-recursive.h:70

DBusTypeWriter::container_type

dbus_uint32_t container_type

what are we inside? (e.g.

**Definition** dbus-marshal-recursive.h:73

DBusTypeWriter::type_pos_is_expectation

dbus_uint32_t type_pos_is_expectation

type_pos can be either an insertion point for or an expected next type

**Definition** dbus-marshal-recursive.h:75
