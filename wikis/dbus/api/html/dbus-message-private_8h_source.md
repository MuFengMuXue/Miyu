dbus-message-private.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-message-private.h header shared between dbus-message.c and dbus-message-util.c

3 \*

4 \* Copyright (C) 2005 Red Hat Inc.

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

25\#ifndef DBUS_MESSAGE_PRIVATE_H

26\#define DBUS_MESSAGE_PRIVATE_H

27

28\#include \<dbus/dbus-message.h\>

29\#include \<dbus/dbus-message-internal.h\>

30\#include \<dbus/dbus-string.h\>

31\#include \<dbus/dbus-dataslot.h\>

32\#include \<dbus/dbus-marshal-header.h\>

33

34DBUS_BEGIN_DECLS

35

62struct DBusMessageLoader

63{

64 int refcount;

66 DBusString data;

68 DBusList \*messages;

70 long max_message_size;

71 long max_message_unix_fds;

73 DBusValidity corruption_reason;

75 unsigned int corrupted : 1;

77 unsigned int buffer_outstanding : 1;

79\#ifdef HAVE_UNIX_FD_PASSING

80 unsigned int unix_fds_outstanding : 1;

82 int \*unix_fds;

83 unsigned n_unix_fds_allocated;

84 unsigned n_unix_fds;

85 void (\* unix_fds_change) (void \*);

86 void \*unix_fds_change_data;

87\#endif

88};

89

90

92\#define CHANGED_STAMP_BITS 21

93

101struct DBusMessage

102{

103 DBusAtomic refcount;

105 DBusHeader header;

107 DBusString body;

109 unsigned int locked : 1;

111\#ifndef DBUS_DISABLE_CHECKS

112 unsigned int in_cache : 1;

113\#endif

114

115 DBusList \*counters;

116 long size_counter_delta;

118 dbus_uint32_t changed_stamp : CHANGED_STAMP_BITS;

120 DBusDataSlotList slot_list;

122\#ifndef DBUS_DISABLE_CHECKS

123 int generation;

124\#endif

125

126\#ifdef HAVE_UNIX_FD_PASSING

127 int \*unix_fds;

131 unsigned n_unix_fds;

132 unsigned n_unix_fds_allocated;

134 long unix_fd_counter_delta;

135\#endif

136};

137

138DBUS_PRIVATE_EXPORT

139dbus_bool_t \_dbus_message_iter_get_args_valist (DBusMessageIter \*iter,

140 DBusError \*error,

141 int first_arg_type,

142 va_list var_args);

143

146DBUS_END_DECLS

147

148\#endif /\* DBUS_MESSAGE_H \*/

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

DBusValidity

DBusValidity

This is primarily used in unit testing, so we can verify that each invalid message is invalid for the...

**Definition** dbus-marshal-validate.h:54

\_dbus_message_iter_get_args_valist

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_message_iter_get_args_valist(DBusMessageIter \*iter, DBusError \*error, int first_arg_type, va_list var_args)

Implementation of the varargs arg-getting functions.

**Definition** dbus-message.c:838

CHANGED_STAMP_BITS

\#define CHANGED_STAMP_BITS

How many bits are in the changed_stamp used to validate iterators.

**Definition** dbus-message-private.h:92

DBusAtomic

An atomic integer safe to increment or decrement from multiple threads.

**Definition** dbus-sysdeps.h:340

DBusDataSlotList

Data structure that stores the actual user data set at a given slot.

**Definition** dbus-dataslot.h:72

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusHeader

Message header data and some cached details of it.

**Definition** dbus-marshal-header.h:90

DBusList

A node in a linked list.

**Definition** dbus-list.h:37

DBusMessageIter

DBusMessageIter struct; contains no public fields.

**Definition** dbus-message.h:64

DBusMessageLoader

Implementation details of DBusMessageLoader.

**Definition** dbus-message-private.h:63

DBusMessageLoader::max_message_size

long max_message_size

Maximum size of a message.

**Definition** dbus-message-private.h:70

DBusMessageLoader::max_message_unix_fds

long max_message_unix_fds

Maximum unix fds in a message.

**Definition** dbus-message-private.h:71

DBusMessageLoader::data

DBusString data

Buffered data.

**Definition** dbus-message-private.h:66

DBusMessageLoader::messages

DBusList \* messages

Complete messages.

**Definition** dbus-message-private.h:68

DBusMessageLoader::corrupted

unsigned int corrupted

We got broken data, and are no longer working.

**Definition** dbus-message-private.h:75

DBusMessageLoader::buffer_outstanding

unsigned int buffer_outstanding

Someone is using the buffer to read.

**Definition** dbus-message-private.h:77

DBusMessageLoader::corruption_reason

DBusValidity corruption_reason

why we were corrupted

**Definition** dbus-message-private.h:73

DBusMessageLoader::refcount

int refcount

Reference count.

**Definition** dbus-message-private.h:64

DBusMessage

Internals of DBusMessage.

**Definition** dbus-message-private.h:102

DBusMessage::header

DBusHeader header

Header network data and associated cache.

**Definition** dbus-message-private.h:105

DBusMessage::body

DBusString body

Body network data.

**Definition** dbus-message-private.h:107

DBusMessage::slot_list

DBusDataSlotList slot_list

Data stored by allocated integer ID.

**Definition** dbus-message-private.h:120

DBusMessage::refcount

DBusAtomic refcount

Reference count.

**Definition** dbus-message-private.h:103

DBusMessage::changed_stamp

dbus_uint32_t changed_stamp

Incremented when iterators are invalidated.

**Definition** dbus-message-private.h:118

DBusMessage::generation

int generation

\_dbus_current_generation when message was created

**Definition** dbus-message-private.h:123

DBusMessage::size_counter_delta

long size_counter_delta

Size we incremented the size counters by.

**Definition** dbus-message-private.h:116

DBusMessage::counters

DBusList \* counters

0-N DBusCounter used to track message size/unix fds.

**Definition** dbus-message-private.h:115

DBusMessage::in_cache

unsigned int in_cache

Has been "freed" since it's in the cache (this is a debug feature)

**Definition** dbus-message-private.h:112

DBusMessage::locked

unsigned int locked

Message being sent, no modifications allowed.

**Definition** dbus-message-private.h:109

DBusString

**Definition** dbus-string.h:47
