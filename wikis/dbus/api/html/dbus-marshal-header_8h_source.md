dbus-marshal-header.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-marshal-header.h Managing marshaling/demarshaling of message headers

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

26\#ifndef DBUS_MARSHAL_HEADER_H

27\#define DBUS_MARSHAL_HEADER_H

28

29\#include \<dbus/dbus-marshal-basic.h\>

30\#include \<dbus/dbus-marshal-validate.h\>

31

32typedef struct DBusHeader DBusHeader;

33typedef struct DBusHeaderField DBusHeaderField;

34

35\#define \_DBUS_HEADER_FIELD_VALUE_UNKNOWN -1

36\#define \_DBUS_HEADER_FIELD_VALUE_NONEXISTENT -2

37

41struct DBusHeaderField

42{

43 int value_pos;

44};

45

89struct DBusHeader

90{

91 DBusString data;

102 DBusHeaderField fields\[DBUS_HEADER_FIELD_LAST + 1\];

106 dbus_uint32_t padding : 3;

108 dbus_uint32_t byte_order : 8;

110};

111

112dbus_bool_t \_dbus_header_init (DBusHeader \*header);

113void \_dbus_header_free (DBusHeader \*header);

114void \_dbus_header_reinit (DBusHeader \*header);

115dbus_bool_t \_dbus_header_create (DBusHeader \*header,

116 int byte_order,

117 int type,

118 const char \*destination,

119 const char \*path,

120 const char \*interface,

121 const char \*member,

122 const char \*error_name);

123dbus_bool_t \_dbus_header_copy (const DBusHeader \*header,

124 DBusHeader \*dest);

125int \_dbus_header_get_message_type (DBusHeader \*header);

126void \_dbus_header_set_serial (DBusHeader \*header,

127 dbus_uint32_t serial);

128dbus_uint32_t \_dbus_header_get_serial (DBusHeader \*header);

129void \_dbus_header_update_lengths (DBusHeader \*header,

130 int body_len);

131DBUS_PRIVATE_EXPORT

132dbus_bool_t \_dbus_header_set_field_basic (DBusHeader \*header,

133 int field,

134 int type,

135 const void \*value);

136dbus_bool_t \_dbus_header_get_field_basic (DBusHeader \*header,

137 int field,

138 int type,

139 void \*value);

140DBUS_PRIVATE_EXPORT

141dbus_bool_t \_dbus_header_get_field_raw (DBusHeader \*header,

142 int field,

143 const DBusString \*\*str,

144 int \*pos);

145DBUS_PRIVATE_EXPORT

146dbus_bool_t \_dbus_header_delete_field (DBusHeader \*header,

147 int field);

148void \_dbus_header_toggle_flag (DBusHeader \*header,

149 dbus_uint32_t flag,

150 dbus_bool_t value);

151dbus_bool_t \_dbus_header_get_flag (DBusHeader \*header,

152 dbus_uint32_t flag);

153dbus_bool_t \_dbus_header_ensure_signature (DBusHeader \*header,

154 DBusString \*\*type_str,

155 int \*type_pos);

156dbus_bool_t \_dbus_header_have_message_untrusted (int max_message_length,

157 DBusValidity \*validity,

158 int \*byte_order,

159 int \*fields_array_len,

160 int \*header_len,

161 int \*body_len,

162 const DBusString \*str,

163 int start,

164 int len);

165dbus_bool_t \_dbus_header_load (DBusHeader \*header,

166 DBusValidationMode mode,

167 DBusValidity \*validity,

168 int byte_order,

169 int fields_array_len,

170 int header_len,

171 int body_len,

172 const DBusString \*str);

173void \_dbus_header_byteswap (DBusHeader \*header,

174 int new_order);

175DBUS_PRIVATE_EXPORT

176char \_dbus_header_get_byte_order (const DBusHeader \*header);

177dbus_bool_t \_dbus_header_remove_unknown_fields (DBusHeader \*header);

178

179\#endif /\* DBUS_MARSHAL_HEADER_H \*/

DBusValidity

DBusValidity

This is primarily used in unit testing, so we can verify that each invalid message is invalid for the...

**Definition** dbus-marshal-validate.h:54

\_dbus_header_update_lengths

void \_dbus_header_update_lengths(DBusHeader \*header, int body_len)

Fills in the correct body length.

**Definition** dbus-marshal-header.c:1207

\_dbus_header_copy

dbus_bool_t \_dbus_header_copy(const DBusHeader \*header, DBusHeader \*dest)

Initializes dest with a copy of the given header.

**Definition** dbus-marshal-header.c:495

\_dbus_header_set_field_basic

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_header_set_field_basic(DBusHeader \*header, int field, int type, const void \*value)

Sets the value of a field with basic type.

**Definition** dbus-marshal-header.c:1284

\_dbus_header_get_message_type

int \_dbus_header_get_message_type(DBusHeader \*header)

Gets the type of the message.

**Definition** dbus-marshal-header.c:391

\_dbus_header_get_field_basic

dbus_bool_t \_dbus_header_get_field_basic(DBusHeader \*header, int field, int type, void \*value)

Gets the value of a field with basic type.

**Definition** dbus-marshal-header.c:1362

\_dbus_header_get_flag

dbus_bool_t \_dbus_header_get_flag(DBusHeader \*header, dbus_uint32_t flag)

Gets a message flag bit, returning TRUE if the bit is set.

**Definition** dbus-marshal-header.c:1490

\_dbus_header_get_byte_order

DBUS_PRIVATE_EXPORT char \_dbus_header_get_byte_order(const DBusHeader \*header)

Returns the header's byte order.

**Definition** dbus-marshal-header.c:179

\_dbus_header_have_message_untrusted

dbus_bool_t \_dbus_header_have_message_untrusted(int max_message_length, DBusValidity \*validity, int \*byte_order, int \*fields_array_len, int \*header_len, int \*body_len, const DBusString \*str, int start, int len)

Given data long enough to contain the length of the message body and the fields array,...

**Definition** dbus-marshal-header.c:681

\_dbus_header_reinit

void \_dbus_header_reinit(DBusHeader \*header)

Re-initializes a header that was previously initialized and never freed.

**Definition** dbus-marshal-header.c:448

\_dbus_header_delete_field

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_header_delete_field(DBusHeader \*header, int field)

Deletes a field, if it exists.

**Definition** dbus-marshal-header.c:1427

\_dbus_header_remove_unknown_fields

dbus_bool_t \_dbus_header_remove_unknown_fields(DBusHeader \*header)

Remove every header field not known to this version of dbus.

**Definition** dbus-marshal-header.c:1532

\_dbus_header_get_serial

dbus_uint32_t \_dbus_header_get_serial(DBusHeader \*header)

See dbus_message_get_serial()

**Definition** dbus-marshal-header.c:432

\_dbus_header_free

void \_dbus_header_free(DBusHeader \*header)

Frees a header.

**Definition** dbus-marshal-header.c:481

\_dbus_header_init

dbus_bool_t \_dbus_header_init(DBusHeader \*header)

Initializes a header, but doesn't prepare it for use; to make the header valid, you have to call \_dbu...

**Definition** dbus-marshal-header.c:465

\_dbus_header_create

dbus_bool_t \_dbus_header_create(DBusHeader \*header, int byte_order, int type, const char \*destination, const char \*path, const char \*interface, const char \*member, const char \*error_name)

Fills in the primary fields of the header, so the header is ready for use.

**Definition** dbus-marshal-header.c:533

\_dbus_header_toggle_flag

void \_dbus_header_toggle_flag(DBusHeader \*header, dbus_uint32_t flag, dbus_bool_t value)

Toggles a message flag bit, turning on the bit if value = TRUE and flipping it off if value = FALSE.

**Definition** dbus-marshal-header.c:1468

\_dbus_header_set_serial

void \_dbus_header_set_serial(DBusHeader \*header, dbus_uint32_t serial)

Sets the serial number of a header.

**Definition** dbus-marshal-header.c:409

\_dbus_header_load

dbus_bool_t \_dbus_header_load(DBusHeader \*header, DBusValidationMode mode, DBusValidity \*validity, int byte_order, int fields_array_len, int header_len, int body_len, const DBusString \*str)

Creates a message header from potentially-untrusted data.

**Definition** dbus-marshal-header.c:981

\_dbus_header_byteswap

void \_dbus_header_byteswap(DBusHeader \*header, int new_order)

Swaps the header into the given order if required.

**Definition** dbus-marshal-header.c:1507

\_dbus_header_get_field_raw

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_header_get_field_raw(DBusHeader \*header, int field, const DBusString \*\*str, int \*pos)

Gets the raw marshaled data for a field.

**Definition** dbus-marshal-header.c:1403

DBusValidationMode

DBusValidationMode

This is used rather than a bool for high visibility.

**Definition** dbus-marshal-validate.h:41

DBUS_HEADER_FIELD_LAST

\#define DBUS_HEADER_FIELD_LAST

Value of the highest-numbered header field code, can be used to determine the size of an array indexe...

**Definition** dbus-protocol.h:317

DBusHeaderField

Cached information about a header field in the message.

**Definition** dbus-marshal-header.h:42

DBusHeaderField::value_pos

int value_pos

Position of field value, or -1/-2.

**Definition** dbus-marshal-header.h:43

DBusHeader

Message header data and some cached details of it.

**Definition** dbus-marshal-header.h:90

DBusHeader::data

DBusString data

Header network data, stored separately from body so we can independently realloc it.

**Definition** dbus-marshal-header.h:91

DBusHeader::padding

dbus_uint32_t padding

0-7 bytes of alignment in header, the distance from \[B\] to \[C\]

**Definition** dbus-marshal-header.h:106

DBusHeader::byte_order

dbus_uint32_t byte_order

byte order of header (must always match the content of byte 0)

**Definition** dbus-marshal-header.h:108

DBusHeader::fields

DBusHeaderField fields\[DBUS_HEADER_FIELD_LAST+1\]

Track the location of each field in header.

**Definition** dbus-marshal-header.h:102

DBusString

**Definition** dbus-string.h:47
