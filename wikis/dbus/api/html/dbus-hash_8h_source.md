dbus-hash.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-hash.h Generic hash table utility (internal to D-Bus implementation)

3 \*

4 \* Copyright (C) 2002 Red Hat, Inc.

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

26\#ifndef DBUS_HASH_H

27\#define DBUS_HASH_H

28

29\#include \<stdint.h\>

30

31\#ifdef HAVE_INTTYPES_H

32\#include \<inttypes.h\>

33\#endif

34

35\#include \<dbus/dbus-memory.h\>

36\#include \<dbus/dbus-types.h\>

37\#include \<dbus/dbus-sysdeps.h\>

38

39DBUS_BEGIN_DECLS

40

49struct DBusHashIter

50{

51 void \*dummy1;

52 void \*dummy2;

53 void \*dummy3;

54 void \*dummy4;

55 int dummy5;

56 int dummy6;

57};

58

59typedef struct DBusHashTable DBusHashTable;

60typedef struct DBusHashIter DBusHashIter;

61

62/\* Allowing an arbitrary function as with GLib

63 \* would be nicer for a public API, but for

64 \* an internal API this saves typing, we can add

65 \* more whenever we feel like it.

66 \*/

67typedef enum

68{

69 DBUS_HASH_STRING,

70 DBUS_HASH_INT,

71 DBUS_HASH_UINTPTR

72} DBusHashType;

73

74DBUS_PRIVATE_EXPORT

75DBusHashTable\* \_dbus_hash_table_new (DBusHashType type,

76 DBusFreeFunction key_free_function,

77 DBusFreeFunction value_free_function);

78DBUS_PRIVATE_EXPORT

79DBusHashTable\* \_dbus_hash_table_ref (DBusHashTable \*table);

80DBUS_PRIVATE_EXPORT

81void \_dbus_hash_table_unref (DBusHashTable \*table);

82void \_dbus_hash_table_remove_all (DBusHashTable \*table);

83DBUS_PRIVATE_EXPORT

84void \_dbus_hash_iter_init (DBusHashTable \*table,

85 DBusHashIter \*iter);

86DBUS_PRIVATE_EXPORT

87dbus_bool_t \_dbus_hash_iter_next (DBusHashIter \*iter);

88DBUS_PRIVATE_EXPORT

89void \_dbus_hash_iter_remove_entry (DBusHashIter \*iter);

90DBUS_PRIVATE_EXPORT

91void\* \_dbus_hash_iter_get_value (DBusHashIter \*iter);

92DBUS_PRIVATE_EXPORT

93void \_dbus_hash_iter_set_value (DBusHashIter \*iter,

94 void \*value);

95DBUS_PRIVATE_EXPORT

96int \_dbus_hash_iter_get_int_key (DBusHashIter \*iter);

97DBUS_PRIVATE_EXPORT

98const char\* \_dbus_hash_iter_get_string_key (DBusHashIter \*iter);

99DBUS_PRIVATE_EXPORT

100uintptr_t \_dbus_hash_iter_get_uintptr_key (DBusHashIter \*iter);

101DBUS_PRIVATE_EXPORT

102dbus_bool_t \_dbus_hash_iter_lookup (DBusHashTable \*table,

103 void \*key,

104 dbus_bool_t create_if_not_found,

105 DBusHashIter \*iter);

106DBUS_PRIVATE_EXPORT

107void\* \_dbus_hash_table_lookup_string (DBusHashTable \*table,

108 const char \*key);

109DBUS_PRIVATE_EXPORT

110void\* \_dbus_hash_table_lookup_int (DBusHashTable \*table,

111 int key);

112DBUS_PRIVATE_EXPORT

113void\* \_dbus_hash_table_lookup_uintptr (DBusHashTable \*table,

114 uintptr_t key);

115DBUS_PRIVATE_EXPORT

116dbus_bool_t \_dbus_hash_table_remove_string (DBusHashTable \*table,

117 const char \*key);

118DBUS_PRIVATE_EXPORT

119dbus_bool_t \_dbus_hash_table_remove_int (DBusHashTable \*table,

120 int key);

121DBUS_PRIVATE_EXPORT

122dbus_bool_t \_dbus_hash_table_remove_uintptr (DBusHashTable \*table,

123 uintptr_t key);

124DBUS_PRIVATE_EXPORT

125dbus_bool_t \_dbus_hash_table_insert_string (DBusHashTable \*table,

126 char \*key,

127 void \*value);

128DBUS_PRIVATE_EXPORT

129dbus_bool_t \_dbus_hash_table_insert_int (DBusHashTable \*table,

130 int key,

131 void \*value);

132DBUS_PRIVATE_EXPORT

133dbus_bool_t \_dbus_hash_table_insert_uintptr (DBusHashTable \*table,

134 uintptr_t key,

135 void \*value);

136DBUS_PRIVATE_EXPORT

137int \_dbus_hash_table_get_n_entries (DBusHashTable \*table);

138

139DBUS_PRIVATE_EXPORT

140char \*\* \_dbus_hash_table_to_array (DBusHashTable \*table,

141 char delimiter);

142DBUS_PRIVATE_EXPORT

143dbus_bool_t \_dbus_hash_table_from_array (DBusHashTable \*table,

144 char \*\*array,

145 char delimiter);

146

147/\* Preallocation \*/

148

150typedef struct DBusPreallocatedHash DBusPreallocatedHash;

151

152DBUS_PRIVATE_EXPORT

153DBusPreallocatedHash \*\_dbus_hash_table_preallocate_entry (DBusHashTable \*table);

154DBUS_PRIVATE_EXPORT

155void \_dbus_hash_table_free_preallocated_entry (DBusHashTable \*table,

156 DBusPreallocatedHash \*preallocated);

157DBUS_PRIVATE_EXPORT

158void \_dbus_hash_table_insert_string_preallocated (DBusHashTable \*table,

159 DBusPreallocatedHash \*preallocated,

160 char \*key,

161 void \*value);

162

163\#ifdef DBUS_WIN

164\# define DBUS_HASH_POLLABLE DBUS_HASH_UINTPTR

165\#else

166\# define DBUS_HASH_POLLABLE DBUS_HASH_INT

167\#endif

168

169static inline DBusPollable

170\_dbus_hash_iter_get_pollable_key (DBusHashIter \*iter)

171{

172\#ifdef DBUS_WIN

173 DBusSocket s;

174

175 s.sock = \_dbus_hash_iter_get_uintptr_key (iter);

176 return s;

177\#else

178 return \_dbus_hash_iter_get_int_key (iter);

179\#endif

180}

181

182static inline void \*

183\_dbus_hash_table_lookup_pollable (DBusHashTable \*table,

184 DBusPollable key)

185{

186\#ifdef DBUS_WIN

187 return \_dbus_hash_table_lookup_uintptr (table, key.sock);

188\#else

189 return \_dbus_hash_table_lookup_int (table, key);

190\#endif

191}

192

193static inline dbus_bool_t

194\_dbus_hash_table_remove_pollable (DBusHashTable \*table,

195 DBusPollable key)

196{

197\#ifdef DBUS_WIN

198 return \_dbus_hash_table_remove_uintptr (table, key.sock);

199\#else

200 return \_dbus_hash_table_remove_int (table, key);

201\#endif

202}

203

204static inline dbus_bool_t

205\_dbus_hash_table_insert_pollable (DBusHashTable \*table,

206 DBusPollable key,

207 void \*value)

208{

209\#ifdef DBUS_WIN

210 return \_dbus_hash_table_insert_uintptr (table, key.sock, value);

211\#else

212 return \_dbus_hash_table_insert_int (table, key, value);

213\#endif

214}

215

216static inline void

217\_dbus_clear_hash_table (DBusHashTable \*\*table_p)

218{

219 \_dbus_clear_pointer_impl (DBusHashTable, table_p, \_dbus_hash_table_unref);

220}

221

224DBUS_END_DECLS

225

226\#endif /\* DBUS_HASH_H \*/

\_dbus_hash_table_get_n_entries

int \_dbus_hash_table_get_n_entries(DBusHashTable \*table)

Gets the number of hash entries in a hash table.

**Definition** dbus-hash.c:1461

\_dbus_hash_table_ref

DBusHashTable \* \_dbus_hash_table_ref(DBusHashTable \*table)

Increments the reference count for a hash table.

**Definition** dbus-hash.c:354

\_dbus_hash_table_remove_uintptr

dbus_bool_t \_dbus_hash_table_remove_uintptr(DBusHashTable \*table, uintptr_t key)

Removes the hash entry for the given key.

**Definition** dbus-hash.c:1243

\_dbus_hash_iter_get_value

void \* \_dbus_hash_iter_get_value(DBusHashIter \*iter)

Gets the value of the current entry.

**Definition** dbus-hash.c:620

DBusPreallocatedHash

struct DBusPreallocatedHash DBusPreallocatedHash

A preallocated hash entry.

**Definition** dbus-hash.h:150

\_dbus_hash_table_insert_int

dbus_bool_t \_dbus_hash_table_insert_int(DBusHashTable \*table, int key, void \*value)

Creates a hash entry with the given key and value.

**Definition** dbus-hash.c:1312

\_dbus_hash_table_insert_string

dbus_bool_t \_dbus_hash_table_insert_string(DBusHashTable \*table, char \*key, void \*value)

Creates a hash entry with the given key and value.

**Definition** dbus-hash.c:1278

\_dbus_hash_table_from_array

dbus_bool_t \_dbus_hash_table_from_array(DBusHashTable \*table, char \*\*array, char delimiter)

Imports a string array into a hash table The hash table needs to be initialized with string keys,...

**Definition** dbus-hash.c:1479

\_dbus_hash_iter_get_uintptr_key

uintptr_t \_dbus_hash_iter_get_uintptr_key(DBusHashIter \*iter)

Gets the key for the current entry.

**Definition** dbus-hash.c:685

\_dbus_hash_table_lookup_uintptr

void \* \_dbus_hash_table_lookup_uintptr(DBusHashTable \*table, uintptr_t key)

Looks up the value for a given integer in a hash table of type DBUS_HASH_UINTPTR.

**Definition** dbus-hash.c:1163

\_dbus_hash_table_unref

void \_dbus_hash_table_unref(DBusHashTable \*table)

Decrements the reference count for a hash table, freeing the hash table if the count reaches zero.

**Definition** dbus-hash.c:368

\_dbus_hash_iter_next

dbus_bool_t \_dbus_hash_iter_next(DBusHashIter \*iter)

Move the hash iterator forward one step, to the next hash entry.

**Definition** dbus-hash.c:550

\_dbus_hash_iter_get_int_key

int \_dbus_hash_iter_get_int_key(DBusHashIter \*iter)

Gets the key for the current entry.

**Definition** dbus-hash.c:666

\_dbus_hash_iter_init

void \_dbus_hash_iter_init(DBusHashTable \*table, DBusHashIter \*iter)

Initializes a hash table iterator.

**Definition** dbus-hash.c:524

\_dbus_hash_table_free_preallocated_entry

void \_dbus_hash_table_free_preallocated_entry(DBusHashTable \*table, DBusPreallocatedHash \*preallocated)

Frees an opaque DBusPreallocatedHash that was not used in order to insert into the hash table.

**Definition** dbus-hash.c:1403

\_dbus_hash_table_new

DBusHashTable \* \_dbus_hash_table_new(DBusHashType type, DBusFreeFunction key_free_function, DBusFreeFunction value_free_function)

Constructs a new hash table.

**Definition** dbus-hash.c:292

\_dbus_hash_table_remove_int

dbus_bool_t \_dbus_hash_table_remove_int(DBusHashTable \*table, int key)

Removes the hash entry for the given key.

**Definition** dbus-hash.c:1215

\_dbus_hash_table_preallocate_entry

DBusPreallocatedHash \* \_dbus_hash_table_preallocate_entry(DBusHashTable \*table)

Preallocate an opaque data blob that allows us to insert into the hash table at a later time without ...

**Definition** dbus-hash.c:1386

\_dbus_hash_table_remove_string

dbus_bool_t \_dbus_hash_table_remove_string(DBusHashTable \*table, const char \*key)

Removes the hash entry for the given key.

**Definition** dbus-hash.c:1187

\_dbus_hash_table_to_array

char \*\* \_dbus_hash_table_to_array(DBusHashTable \*table, char delimiter)

Creates a string array from a hash table.

**Definition** dbus-hash.c:1544

\_dbus_hash_iter_set_value

void \_dbus_hash_iter_set_value(DBusHashIter \*iter, void \*value)

Sets the value of the current entry.

**Definition** dbus-hash.c:643

DBusHashType

DBusHashType

Indicates the type of a key in the hash table.

**Definition** dbus-hash.h:68

\_dbus_hash_table_lookup_string

void \* \_dbus_hash_table_lookup_string(DBusHashTable \*table, const char \*key)

Looks up the value for a given string in a hash table of type DBUS_HASH_STRING.

**Definition** dbus-hash.c:1113

\_dbus_hash_iter_lookup

dbus_bool_t \_dbus_hash_iter_lookup(DBusHashTable \*table, void \*key, dbus_bool_t create_if_not_found, DBusHashIter \*iter)

A low-level but efficient interface for manipulating the hash table.

**Definition** dbus-hash.c:748

\_dbus_hash_table_remove_all

void \_dbus_hash_table_remove_all(DBusHashTable \*table)

Removed all entries from a hash table.

**Definition** dbus-hash.c:425

\_dbus_hash_iter_get_string_key

const char \* \_dbus_hash_iter_get_string_key(DBusHashIter \*iter)

Gets the key for the current entry.

**Definition** dbus-hash.c:703

\_dbus_hash_table_insert_uintptr

dbus_bool_t \_dbus_hash_table_insert_uintptr(DBusHashTable \*table, uintptr_t key, void \*value)

Creates a hash entry with the given key and value.

**Definition** dbus-hash.c:1353

\_dbus_hash_iter_remove_entry

void \_dbus_hash_iter_remove_entry(DBusHashIter \*iter)

Removes the current entry from the hash table.

**Definition** dbus-hash.c:599

\_dbus_hash_table_insert_string_preallocated

void \_dbus_hash_table_insert_string_preallocated(DBusHashTable \*table, DBusPreallocatedHash \*preallocated, char \*key, void \*value)

Inserts a string-keyed entry into the hash table, using a preallocated data block from \_dbus_hash_tab...

**Definition** dbus-hash.c:1430

\_dbus_hash_table_lookup_int

void \* \_dbus_hash_table_lookup_int(DBusHashTable \*table, int key)

Looks up the value for a given integer in a hash table of type DBUS_HASH_INT.

**Definition** dbus-hash.c:1138

DBUS_HASH_INT

@ DBUS_HASH_INT

Hash keys are integers.

**Definition** dbus-hash.h:70

DBUS_HASH_UINTPTR

@ DBUS_HASH_UINTPTR

Hash keys are integer capable to hold a pointer.

**Definition** dbus-hash.h:71

DBUS_HASH_STRING

@ DBUS_HASH_STRING

Hash keys are strings.

**Definition** dbus-hash.h:69

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

DBusFreeFunction

void(\* DBusFreeFunction)(void \*memory)

The type of a function which frees a block of memory.

**Definition** dbus-memory.h:65

DBusHashIter

Hash iterator object.

**Definition** dbus-hash.h:50

DBusHashIter::dummy1

void \* dummy1

Do not use.

**Definition** dbus-hash.h:51

DBusHashIter::dummy4

void \* dummy4

Do not use.

**Definition** dbus-hash.h:54

DBusHashIter::dummy5

int dummy5

Do not use.

**Definition** dbus-hash.h:55

DBusHashIter::dummy6

int dummy6

Do not use.

**Definition** dbus-hash.h:56

DBusHashIter::dummy3

void \* dummy3

Do not use.

**Definition** dbus-hash.h:53

DBusHashIter::dummy2

void \* dummy2

Do not use.

**Definition** dbus-hash.h:52

DBusHashTable

Internals of DBusHashTable.

**Definition** dbus-hash.c:175

DBusSocket

Socket interface.

**Definition** dbus-sysdeps.h:185
