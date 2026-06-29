dbus-server-protected.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-server-protected.h Used by subclasses of DBusServer object (internal to D-Bus implementation)

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

25\#ifndef DBUS_SERVER_PROTECTED_H

26\#define DBUS_SERVER_PROTECTED_H

27

28\#include \<dbus/dbus-internals.h\>

29\#include \<dbus/dbus-threads-internal.h\>

30\#include \<dbus/dbus-server.h\>

31\#include \<dbus/dbus-address.h\>

32\#include \<dbus/dbus-timeout.h\>

33\#include \<dbus/dbus-watch.h\>

34\#include \<dbus/dbus-resources.h\>

35\#include \<dbus/dbus-dataslot.h\>

36\#include \<dbus/dbus-string.h\>

37

38DBUS_BEGIN_DECLS

39

40typedef struct DBusServerVTable DBusServerVTable;

41

45struct DBusServerVTable

46{

47 void (\* finalize) (DBusServer \*server);

50 void (\* disconnect) (DBusServer \*server);

52};

53

58struct DBusServer

59{

60 DBusAtomic refcount;

61 const DBusServerVTable \*vtable;

62 DBusRMutex \*mutex;

64 DBusGUID guid;

66 DBusString guid_hex;

68 DBusWatchList \*watches;

69 DBusTimeoutList \*timeouts;

71 char \*address;

72 dbus_bool_t published_address;

74 int max_connections;

76 DBusDataSlotList slot_list;

78 DBusNewConnectionFunction new_connection_function;

80 void \*new_connection_data;

82 DBusFreeFunction new_connection_free_data_function;

87 char \*\*auth_mechanisms;

89 unsigned int disconnected : 1;

91\#ifndef DBUS_DISABLE_CHECKS

92 unsigned int have_server_lock : 1;

93\#endif

94};

95

96dbus_bool_t \_dbus_server_init_base (DBusServer \*server,

97 const DBusServerVTable \*vtable,

98 const DBusString \*address,

99 DBusError \*error);

100void \_dbus_server_finalize_base (DBusServer \*server);

101void \_dbus_server_disconnect_unlocked (DBusServer \*server);

102dbus_bool_t \_dbus_server_add_watch (DBusServer \*server,

103 DBusWatch \*watch);

104void \_dbus_server_remove_watch (DBusServer \*server,

105 DBusWatch \*watch);

106DBUS_PRIVATE_EXPORT

107void \_dbus_server_toggle_all_watches (DBusServer \*server,

108 dbus_bool_t enabled);

109dbus_bool_t \_dbus_server_add_timeout (DBusServer \*server,

110 DBusTimeout \*timeout);

111void \_dbus_server_remove_timeout (DBusServer \*server,

112 DBusTimeout \*timeout);

113void \_dbus_server_toggle_timeout (DBusServer \*server,

114 DBusTimeout \*timeout,

115 dbus_bool_t enabled);

116

117DBUS_PRIVATE_EXPORT

118void \_dbus_server_ref_unlocked (DBusServer \*server);

119DBUS_PRIVATE_EXPORT

120void \_dbus_server_unref_unlocked (DBusServer \*server);

121

122typedef enum

123{

124 DBUS_SERVER_LISTEN_NOT_HANDLED,

125 DBUS_SERVER_LISTEN_OK,

126 DBUS_SERVER_LISTEN_BAD_ADDRESS,

127 DBUS_SERVER_LISTEN_DID_NOT_CONNECT,

128 DBUS_SERVER_LISTEN_ADDRESS_ALREADY_USED

129} DBusServerListenResult;

130

131DBusServerListenResult \_dbus_server_listen_unix_socket (DBusAddressEntry \*entry,

132 DBusServer \*\*server_p,

133 DBusError \*error);

134

135DBusServerListenResult \_dbus_server_listen_platform_specific (DBusAddressEntry \*entry,

136 DBusServer \*\*server_p,

137 DBusError \*error);

138

139\#ifdef DBUS_ENABLE_VERBOSE_MODE

140void \_dbus_server_trace_ref (DBusServer \*server,

141 int old_refcount,

142 int new_refcount,

143 const char \*why);

144\#else

145\#define \_dbus_server_trace_ref(s,o,n,w) \\

146 do \\

147 {\\

148 (void) (o); \\

149 (void) (n); \\

150 } while (0)

151\#endif

152

153\#ifdef DBUS_DISABLE_CHECKS

154\#define TOOK_LOCK_CHECK(server)

155\#define RELEASING_LOCK_CHECK(server)

156\#define HAVE_LOCK_CHECK(server)

157\#else

158\#define TOOK_LOCK_CHECK(server) do { \\

159 \_dbus_assert (!(server)-\>have_server_lock); \\

160 (server)-\>have_server_lock = TRUE; \\

161 } while (0)

162\#define RELEASING_LOCK_CHECK(server) do { \\

163 \_dbus_assert ((server)-\>have_server_lock); \\

164 (server)-\>have_server_lock = FALSE; \\

165 } while (0)

166\#define HAVE_LOCK_CHECK(server) \_dbus_assert ((server)-\>have_server_lock)

167/\* A "DO_NOT_HAVE_LOCK_CHECK" is impossible since we need the lock to check the flag \*/

168\#endif

169

170\#define TRACE_LOCKS 0

171

172\#define SERVER_LOCK(server) do { \\

173 if (TRACE_LOCKS) { \_dbus_verbose ("LOCK\n"); } \\

174 \_dbus_rmutex_lock ((server)-\>mutex); \\

175 TOOK_LOCK_CHECK (server); \\

176 } while (0)

177

178\#define SERVER_UNLOCK(server) do { \\

179 if (TRACE_LOCKS) { \_dbus_verbose ("UNLOCK\n"); } \\

180 RELEASING_LOCK_CHECK (server); \\

181 \_dbus_rmutex_unlock ((server)-\>mutex); \\

182 } while (0)

183

184DBUS_END_DECLS

185

186\#endif /\* DBUS_SERVER_PROTECTED_H \*/

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

\_dbus_server_add_watch

dbus_bool_t \_dbus_server_add_watch(DBusServer \*server, DBusWatch \*watch)

Adds a watch for this server, chaining out to application-provided watch handlers.

**Definition** dbus-server.c:297

\_dbus_server_remove_watch

void \_dbus_server_remove_watch(DBusServer \*server, DBusWatch \*watch)

Removes a watch previously added with \_dbus_server_remove_watch().

**Definition** dbus-server.c:313

\_dbus_server_remove_timeout

void \_dbus_server_remove_timeout(DBusServer \*server, DBusTimeout \*timeout)

Removes a timeout previously added with \_dbus_server_add_timeout().

**Definition** dbus-server.c:421

\_dbus_server_unref_unlocked

DBUS_PRIVATE_EXPORT void \_dbus_server_unref_unlocked(DBusServer \*server)

Like dbus_server_unref() but does not acquire the lock (must already be held)

**Definition** dbus-server.c:476

\_dbus_server_toggle_timeout

void \_dbus_server_toggle_timeout(DBusServer \*server, DBusTimeout \*timeout, dbus_bool_t enabled)

Toggles a timeout and notifies app via server's DBusTimeoutToggledFunction if available.

**Definition** dbus-server.c:440

\_dbus_server_add_timeout

dbus_bool_t \_dbus_server_add_timeout(DBusServer \*server, DBusTimeout \*timeout)

Adds a timeout for this server, chaining out to application-provided timeout handlers.

**Definition** dbus-server.c:406

\_dbus_server_init_base

dbus_bool_t \_dbus_server_init_base(DBusServer \*server, const DBusServerVTable \*vtable, const DBusString \*address, DBusError \*error)

Initializes the members of the DBusServer base class.

**Definition** dbus-server.c:113

\_dbus_server_finalize_base

void \_dbus_server_finalize_base(DBusServer \*server)

Finalizes the members of the DBusServer base class.

**Definition** dbus-server.c:202

\_dbus_server_ref_unlocked

DBUS_PRIVATE_EXPORT void \_dbus_server_ref_unlocked(DBusServer \*server)

Like dbus_server_ref() but does not acquire the lock (must already be held)

**Definition** dbus-server.c:457

\_dbus_server_toggle_all_watches

DBUS_PRIVATE_EXPORT void \_dbus_server_toggle_all_watches(DBusServer \*server, dbus_bool_t enabled)

Toggles all watch and notifies app via server's DBusWatchToggledFunction if available.

**Definition** dbus-server.c:331

\_dbus_server_listen_unix_socket

DBusServerListenResult \_dbus_server_listen_unix_socket(DBusAddressEntry \*entry, DBusServer \*\*server_p, DBusError \*error)

Tries to interpret the address entry for UNIX socket addresses.

**Definition** dbus-server-socket.c:761

\_dbus_server_listen_platform_specific

DBusServerListenResult \_dbus_server_listen_platform_specific(DBusAddressEntry \*entry, DBusServer \*\*server_p, DBusError \*error)

Tries to interpret the address entry in a platform-specific way, creating a platform-specific server ...

**Definition** dbus-server-unix.c:55

DBusNewConnectionFunction

void(\* DBusNewConnectionFunction)(DBusServer \*server, DBusConnection \*new_connection, void \*data)

Called when a new connection to the server is available.

**Definition** dbus-server.h:50

DBusAddressEntry

Internals of DBusAddressEntry.

**Definition** dbus-address.c:49

DBusAtomic

An atomic integer safe to increment or decrement from multiple threads.

**Definition** dbus-sysdeps.h:340

DBusDataSlotList

Data structure that stores the actual user data set at a given slot.

**Definition** dbus-dataslot.h:72

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusRMutex

**Definition** dbus-sysdeps-pthread.c:51

DBusServerVTable

Virtual table to be implemented by all server "subclasses".

**Definition** dbus-server-protected.h:46

DBusServerVTable::disconnect

void(\* disconnect)(DBusServer \*server)

Disconnect this server.

**Definition** dbus-server-protected.h:50

DBusServerVTable::finalize

void(\* finalize)(DBusServer \*server)

The finalize method must free the server.

**Definition** dbus-server-protected.h:47

DBusServer

Internals of DBusServer object.

**Definition** dbus-server-protected.h:59

DBusServer::published_address

dbus_bool_t published_address

flag which indicates that server has published its bus address.

**Definition** dbus-server-protected.h:72

DBusServer::slot_list

DBusDataSlotList slot_list

Data stored by allocated integer ID.

**Definition** dbus-server-protected.h:76

DBusServer::address

char \* address

Address this server is listening on.

**Definition** dbus-server-protected.h:71

DBusServer::new_connection_free_data_function

DBusFreeFunction new_connection_free_data_function

Callback to invoke to free new_connection_data when server is finalized or data is replaced.

**Definition** dbus-server-protected.h:82

DBusServer::refcount

DBusAtomic refcount

Reference count.

**Definition** dbus-server-protected.h:60

DBusServer::watches

DBusWatchList \* watches

Our watches.

**Definition** dbus-server-protected.h:68

DBusServer::guid

DBusGUID guid

Globally unique ID of server.

**Definition** dbus-server-protected.h:64

DBusServer::guid_hex

DBusString guid_hex

Hex-encoded version of GUID.

**Definition** dbus-server-protected.h:66

DBusServer::disconnected

unsigned int disconnected

TRUE if we are disconnected.

**Definition** dbus-server-protected.h:89

DBusServer::mutex

DBusRMutex \* mutex

Lock on the server object.

**Definition** dbus-server-protected.h:62

DBusServer::max_connections

int max_connections

Max number of connections allowed at once.

**Definition** dbus-server-protected.h:74

DBusServer::new_connection_function

DBusNewConnectionFunction new_connection_function

Callback to invoke when a new connection is created.

**Definition** dbus-server-protected.h:78

DBusServer::vtable

const DBusServerVTable \* vtable

Virtual methods for this instance.

**Definition** dbus-server-protected.h:61

DBusServer::new_connection_data

void \* new_connection_data

Data for new connection callback.

**Definition** dbus-server-protected.h:80

DBusServer::have_server_lock

unsigned int have_server_lock

Does someone have the server mutex locked.

**Definition** dbus-server-protected.h:92

DBusServer::auth_mechanisms

char \*\* auth_mechanisms

Array of allowed authentication mechanisms.

**Definition** dbus-server-protected.h:87

DBusServer::timeouts

DBusTimeoutList \* timeouts

Our timeouts.

**Definition** dbus-server-protected.h:69

DBusString

**Definition** dbus-string.h:47

DBusTimeoutList

DBusTimeoutList implementation details.

**Definition** dbus-timeout.c:183

DBusTimeout

Internals of DBusTimeout.

**Definition** dbus-timeout.c:43

DBusWatchList

DBusWatchList implementation details.

**Definition** dbus-watch.c:217

DBusWatch

Implementation of DBusWatch.

**Definition** dbus-watch.c:43

DBusGUID

A globally unique ID ; we have one for each DBusServer, and also one for each machine with libdbus in...

**Definition** dbus-internals.h:458
