dbus-types.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-types.h types such as dbus_bool_t

3 \*

4 \* Copyright (C) 2002 Red Hat Inc.

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

25\#if !defined (DBUS_INSIDE_DBUS_H) && !defined (DBUS_COMPILATION)

26\#error "Only \<dbus/dbus.h\> can be included directly, this file may disappear or change contents."

27\#endif

28

29\#ifndef DBUS_TYPES_H

30\#define DBUS_TYPES_H

31

32\#include \<stddef.h\>

33\#include \<dbus/dbus-arch-deps.h\>

34

35typedef dbus_uint32_t dbus_unichar_t;

36/\* boolean size must be fixed at 4 bytes due to wire protocol! \*/

37typedef dbus_uint32_t dbus_bool_t;

38

39/\* Normally docs are in .c files, but there isn't a .c file for this. \*/

144typedef struct

145{

146 dbus_uint32_t first32;

147 dbus_uint32_t second32;

148} DBus8ByteStruct;

149

160typedef union

161{

162 unsigned char bytes\[8\];

163 dbus_int16_t i16;

164 dbus_uint16_t u16;

165 dbus_int32_t i32;

166 dbus_uint32_t u32;

167 dbus_bool_t bool_val;

168 dbus_int64_t i64;

169 dbus_uint64_t u64;

170 DBus8ByteStruct eight;

171 double dbl;

172 unsigned char byt;

173 char \*str;

174 int fd;

175} DBusBasicValue;

176

179\#endif /\* DBUS_TYPES_H \*/

DBus8ByteStruct

An 8-byte struct you could use to access int64 without having int64 support.

**Definition** dbus-types.h:145

DBus8ByteStruct::second32

dbus_uint32_t second32

second 32 bits in the 8 bytes (beware endian issues)

**Definition** dbus-types.h:147

DBus8ByteStruct::first32

dbus_uint32_t first32

first 32 bits in the 8 bytes (beware endian issues)

**Definition** dbus-types.h:146

DBusBasicValue

A simple value union that lets you access bytes as if they were various types; useful when dealing wi...

**Definition** dbus-types.h:161

DBusBasicValue::i32

dbus_int32_t i32

as int32

**Definition** dbus-types.h:165

DBusBasicValue::i64

dbus_int64_t i64

as int64

**Definition** dbus-types.h:168

DBusBasicValue::u32

dbus_uint32_t u32

as int32

**Definition** dbus-types.h:166

DBusBasicValue::u64

dbus_uint64_t u64

as int64

**Definition** dbus-types.h:169

DBusBasicValue::dbl

double dbl

as double

**Definition** dbus-types.h:171

DBusBasicValue::fd

int fd

as Unix file descriptor

**Definition** dbus-types.h:174

DBusBasicValue::eight

DBus8ByteStruct eight

as 8-byte struct

**Definition** dbus-types.h:170

DBusBasicValue::u16

dbus_uint16_t u16

as int16

**Definition** dbus-types.h:164

DBusBasicValue::byt

unsigned char byt

as byte

**Definition** dbus-types.h:172

DBusBasicValue::i16

dbus_int16_t i16

as int16

**Definition** dbus-types.h:163

DBusBasicValue::str

char \* str

as char\* (string, object path or signature)

**Definition** dbus-types.h:173

DBusBasicValue::bool_val

dbus_bool_t bool_val

as boolean

**Definition** dbus-types.h:167
