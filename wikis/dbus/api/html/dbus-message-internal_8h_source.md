dbus-message-internal.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-message-internal.h DBusMessage object internal interfaces

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

25\#ifndef DBUS_MESSAGE_INTERNAL_H

26\#define DBUS_MESSAGE_INTERNAL_H

27

28\#include \<dbus/dbus-marshal-validate.h\>

29\#include \<dbus/dbus-message.h\>

30\#include \<dbus/dbus-resources.h\>

31\#include \<dbus/dbus-list.h\>

32

33DBUS_BEGIN_DECLS

34

35\#ifdef DBUS_ENABLE_VERBOSE_MODE

36void \_dbus_message_trace_ref (DBusMessage \*message,

37 int old_refcount,

38 int new_refcount,

39 const char \*why);

40\#else

41/\* this bypasses any "unused" warnings for the old and new refcount \*/

42\#define \_dbus_message_trace_ref(m, o, n, w) \\

43 do \\

44 {\\

45 (void) (o); \\

46 (void) (n); \\

47 } while (0)

48\#endif

49

50typedef struct DBusMessageLoader DBusMessageLoader;

51

52void \_dbus_message_get_network_data (DBusMessage \*message,

53 const DBusString \*\*header,

54 const DBusString \*\*body);

55DBUS_PRIVATE_EXPORT

56void \_dbus_message_get_unix_fds (DBusMessage \*message,

57 const int \*\*fds,

58 unsigned \*n_fds);

59

60unsigned int \_dbus_message_get_n_unix_fds (DBusMessage \*message);

61void \_dbus_message_lock (DBusMessage \*message);

62void \_dbus_message_unlock (DBusMessage \*message);

63dbus_bool_t \_dbus_message_add_counter (DBusMessage \*message,

64 DBusCounter \*counter);

65void \_dbus_message_add_counter_link (DBusMessage \*message,

66 DBusList \*link);

67void \_dbus_message_remove_counter (DBusMessage \*message,

68 DBusCounter \*counter);

69DBUS_PRIVATE_EXPORT

70dbus_bool_t \_dbus_message_remove_unknown_fields (DBusMessage \*message);

71

72DBUS_PRIVATE_EXPORT

73DBusMessageLoader\* \_dbus_message_loader_new (void);

74DBUS_PRIVATE_EXPORT

75DBusMessageLoader\* \_dbus_message_loader_ref (DBusMessageLoader \*loader);

76DBUS_PRIVATE_EXPORT

77void \_dbus_message_loader_unref (DBusMessageLoader \*loader);

78

79DBUS_PRIVATE_EXPORT

80void \_dbus_message_loader_get_buffer (DBusMessageLoader \*loader,

81 DBusString \*\*buffer,

82 int \*max_to_read,

83 dbus_bool_t \*may_read_unix_fds);

84DBUS_PRIVATE_EXPORT

85void \_dbus_message_loader_return_buffer (DBusMessageLoader \*loader,

86 DBusString \*buffer);

87

88

89\#ifdef HAVE_UNIX_FD_PASSING

90DBUS_PRIVATE_EXPORT

91dbus_bool_t \_dbus_message_loader_get_unix_fds (DBusMessageLoader \*loader,

92 int \*\*fds,

93 unsigned \*max_n_fds);

94

95DBUS_PRIVATE_EXPORT

96void \_dbus_message_loader_return_unix_fds (DBusMessageLoader \*loader,

97 int \*fds,

98 unsigned n_fds);

99\#endif

100

101DBUS_PRIVATE_EXPORT

102dbus_bool_t \_dbus_message_loader_queue_messages (DBusMessageLoader \*loader);

103DBusMessage\* \_dbus_message_loader_peek_message (DBusMessageLoader \*loader);

104DBUS_PRIVATE_EXPORT

105DBusMessage\* \_dbus_message_loader_pop_message (DBusMessageLoader \*loader);

106DBusList\* \_dbus_message_loader_pop_message_link (DBusMessageLoader \*loader);

107void \_dbus_message_loader_putback_message_link (DBusMessageLoader \*loader,

108 DBusList \*link);

109

110DBUS_PRIVATE_EXPORT

111dbus_bool_t \_dbus_message_loader_get_is_corrupted (DBusMessageLoader \*loader);

112DBusValidity \_dbus_message_loader_get_corruption_reason (DBusMessageLoader \*loader);

113

114void \_dbus_message_loader_set_max_message_size (DBusMessageLoader \*loader,

115 long size);

116DBUS_PRIVATE_EXPORT

117long \_dbus_message_loader_get_max_message_size (DBusMessageLoader \*loader);

118

119void \_dbus_message_loader_set_max_message_unix_fds(DBusMessageLoader \*loader,

120 long n);

121long \_dbus_message_loader_get_max_message_unix_fds(DBusMessageLoader \*loader);

122int \_dbus_message_loader_get_pending_fds_count (DBusMessageLoader \*loader);

123void \_dbus_message_loader_set_pending_fds_function (DBusMessageLoader \*loader,

124 void (\* callback) (void \*),

125 void \*data);

126

127typedef struct DBusVariant DBusVariant;

128DBUS_PRIVATE_EXPORT

129DBusVariant \*\_dbus_variant_read (DBusMessageIter \*reader);

130DBUS_PRIVATE_EXPORT

131dbus_bool_t \_dbus_variant_write (DBusVariant \*self,

132 DBusMessageIter \*writer);

133DBUS_PRIVATE_EXPORT

134void \_dbus_variant_free (DBusVariant \*self);

135DBUS_PRIVATE_EXPORT

136int \_dbus_variant_get_length (DBusVariant \*self);

137DBUS_PRIVATE_EXPORT

138const DBusString \*\_dbus_variant_peek (DBusVariant \*self);

139DBUS_PRIVATE_EXPORT

140const char \*\_dbus_variant_get_signature (DBusVariant \*self);

141

142static inline void

143\_dbus_clear_variant (DBusVariant \*\*variant_p)

144{

145 \_dbus_clear_pointer_impl (DBusVariant, variant_p, \_dbus_variant_free);

146}

147

148DBUS_END_DECLS

149

150\#endif /\* DBUS_MESSAGE_INTERNAL_H \*/

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

\_dbus_message_loader_set_max_message_size

void \_dbus_message_loader_set_max_message_size(DBusMessageLoader \*loader, long size)

Sets the maximum size message we allow.

**Definition** dbus-message.c:4843

\_dbus_message_remove_unknown_fields

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_message_remove_unknown_fields(DBusMessage \*message)

Remove every header field not known to this version of dbus.

**Definition** dbus-message.c:284

\_dbus_variant_read

DBUS_PRIVATE_EXPORT DBusVariant \* \_dbus_variant_read(DBusMessageIter \*reader)

Copy a single D-Bus message item from reader into a newly-allocated DBusVariant.

**Definition** dbus-message.c:5349

\_dbus_variant_write

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_variant_write(DBusVariant \*self, DBusMessageIter \*writer)

Copy the single D-Bus message item from self into writer.

**Definition** dbus-message.c:5516

\_dbus_message_loader_get_is_corrupted

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_message_loader_get_is_corrupted(DBusMessageLoader \*loader)

Checks whether the loader is confused due to bad data.

**Definition** dbus-message.c:4814

\_dbus_message_get_n_unix_fds

unsigned int \_dbus_message_get_n_unix_fds(DBusMessage \*message)

Gets the number of unix fds attached to this message.

**Definition** dbus-message-util.c:42

\_dbus_message_loader_unref

DBUS_PRIVATE_EXPORT void \_dbus_message_loader_unref(DBusMessageLoader \*loader)

Decrements the reference count of the loader and finalizes the loader when the count reaches zero.

**Definition** dbus-message.c:4239

\_dbus_message_get_unix_fds

DBUS_PRIVATE_EXPORT void \_dbus_message_get_unix_fds(DBusMessage \*message, const int \*\*fds, unsigned \*n_fds)

Gets the unix fds to be sent over the network for this message.

**Definition** dbus-message.c:262

\_dbus_message_loader_pop_message

DBUS_PRIVATE_EXPORT DBusMessage \* \_dbus_message_loader_pop_message(DBusMessageLoader \*loader)

Pops a loaded message (passing ownership of the message to the caller).

**Definition** dbus-message.c:4772

\_dbus_message_get_network_data

void \_dbus_message_get_network_data(DBusMessage \*message, const DBusString \*\*header, const DBusString \*\*body)

Gets the data to be sent over the network for this message.

**Definition** dbus-message.c:243

\_dbus_message_loader_set_pending_fds_function

void \_dbus_message_loader_set_pending_fds_function(DBusMessageLoader \*loader, void(\*callback)(void \*), void \*data)

Register a function to be called whenever the number of pending file descriptors in the loader change...

**Definition** dbus-message.c:4922

\_dbus_message_loader_putback_message_link

void \_dbus_message_loader_putback_message_link(DBusMessageLoader \*loader, DBusList \*link)

Returns a popped message link, used to undo a pop.

**Definition** dbus-message.c:4798

\_dbus_message_loader_get_pending_fds_count

int \_dbus_message_loader_get_pending_fds_count(DBusMessageLoader \*loader)

Return how many file descriptors are pending in the loader.

**Definition** dbus-message.c:4904

\_dbus_variant_get_signature

DBUS_PRIVATE_EXPORT const char \* \_dbus_variant_get_signature(DBusVariant \*self)

Return the signature of the item stored in self.

**Definition** dbus-message.c:5485

\_dbus_message_loader_get_buffer

DBUS_PRIVATE_EXPORT void \_dbus_message_loader_get_buffer(DBusMessageLoader \*loader, DBusString \*\*buffer, int \*max_to_read, dbus_bool_t \*may_read_unix_fds)

Gets the buffer to use for reading data from the network.

**Definition** dbus-message.c:4274

\_dbus_message_remove_counter

void \_dbus_message_remove_counter(DBusMessage \*message, DBusCounter \*counter)

Removes a counter tracking the size/unix fds of this message, and decrements the counter by the size/...

**Definition** dbus-message.c:399

\_dbus_message_add_counter

dbus_bool_t \_dbus_message_add_counter(DBusMessage \*message, DBusCounter \*counter)

Adds a counter to be incremented immediately with the size/unix fds of this message,...

**Definition** dbus-message.c:376

\_dbus_message_loader_peek_message

DBusMessage \* \_dbus_message_loader_peek_message(DBusMessageLoader \*loader)

Peeks at first loaded message, returns NULL if no messages have been queued.

**Definition** dbus-message.c:4755

\_dbus_message_loader_set_max_message_unix_fds

void \_dbus_message_loader_set_max_message_unix_fds(DBusMessageLoader \*loader, long n)

Sets the maximum unix fds per message we allow.

**Definition** dbus-message.c:4874

\_dbus_message_loader_get_max_message_size

DBUS_PRIVATE_EXPORT long \_dbus_message_loader_get_max_message_size(DBusMessageLoader \*loader)

Gets the maximum allowed message size in bytes.

**Definition** dbus-message.c:4862

\_dbus_message_loader_new

DBUS_PRIVATE_EXPORT DBusMessageLoader \* \_dbus_message_loader_new(void)

Creates a new message loader.

**Definition** dbus-message.c:4177

\_dbus_message_loader_pop_message_link

DBusList \* \_dbus_message_loader_pop_message_link(DBusMessageLoader \*loader)

Pops a loaded message inside a list link (passing ownership of the message and link to the caller).

**Definition** dbus-message.c:4786

\_dbus_message_loader_queue_messages

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_message_loader_queue_messages(DBusMessageLoader \*loader)

Converts buffered data into messages, if we have enough data.

**Definition** dbus-message.c:4692

\_dbus_message_loader_return_buffer

DBUS_PRIVATE_EXPORT void \_dbus_message_loader_return_buffer(DBusMessageLoader \*loader, DBusString \*buffer)

Returns a buffer obtained from \_dbus_message_loader_get_buffer(), indicating to the loader how many b...

**Definition** dbus-message.c:4380

\_dbus_message_loader_ref

DBUS_PRIVATE_EXPORT DBusMessageLoader \* \_dbus_message_loader_ref(DBusMessageLoader \*loader)

Increments the reference count of the loader.

**Definition** dbus-message.c:4225

\_dbus_message_loader_get_max_message_unix_fds

long \_dbus_message_loader_get_max_message_unix_fds(DBusMessageLoader \*loader)

Gets the maximum allowed number of unix fds per message.

**Definition** dbus-message.c:4893

\_dbus_message_add_counter_link

void \_dbus_message_add_counter_link(DBusMessage \*message, DBusList \*link)

Adds a counter to be incremented immediately with the size/unix fds of this message,...

**Definition** dbus-message.c:327

\_dbus_message_loader_get_corruption_reason

DBusValidity \_dbus_message_loader_get_corruption_reason(DBusMessageLoader \*loader)

Checks what kind of bad data confused the loader.

**Definition** dbus-message.c:4828

DBusCounter

Internals of DBusCounter.

**Definition** dbus-resources.c:57

DBusList

A node in a linked list.

**Definition** dbus-list.h:37

DBusMessageIter

DBusMessageIter struct; contains no public fields.

**Definition** dbus-message.h:64

DBusMessageLoader

Implementation details of DBusMessageLoader.

**Definition** dbus-message-private.h:63

DBusMessageLoader::data

DBusString data

Buffered data.

**Definition** dbus-message-private.h:66

DBusMessage

Internals of DBusMessage.

**Definition** dbus-message-private.h:102

DBusString

**Definition** dbus-string.h:47

DBusVariant

An opaque data structure containing the serialized form of any single D-Bus message item,...

**Definition** dbus-message.c:5333
