dbus-server-debug-pipe.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-server-debug-pipe.c In-proc debug server implementation

3 \*

4 \* Copyright (C) 2003 CodeFactory AB

5 \* Copyright (C) 2003, 2004 Red Hat, Inc.

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

27\#include \<config.h\>

28\#include "dbus-internals.h"

29\#include "dbus-server-debug-pipe.h"

30\#include "dbus-transport-socket.h"

31\#include "dbus-connection-internal.h"

32\#include "dbus-hash.h"

33\#include "dbus-string.h"

34\#include "dbus-protocol.h"

35

36\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

37

52typedef struct DBusServerDebugPipe DBusServerDebugPipe;

53

58struct DBusServerDebugPipe

59{

60 DBusServer base;

62 char \*name;

64 dbus_bool_t disconnected;

65};

66

67/\* FIXME not threadsafe (right now the test suite doesn't use threads anyhow ) \*/

68static DBusHashTable \*server_pipe_hash;

69static int server_pipe_hash_refcount = 0;

70

71static dbus_bool_t

72pipe_hash_ref (void)

73{

74 if (!server_pipe_hash)

75 {

76 \_dbus_assert (server_pipe_hash_refcount == 0);

77

78 server_pipe_hash = \_dbus_hash_table_new (DBUS_HASH_STRING, NULL, NULL);

79

80 if (!server_pipe_hash)

81 return FALSE;

82 }

83

84 server_pipe_hash_refcount = 1;

85

86 return TRUE;

87}

88

89static void

90pipe_hash_unref (void)

91{

92 \_dbus_assert (server_pipe_hash != NULL);

93 \_dbus_assert (server_pipe_hash_refcount \> 0);

94

95 server_pipe_hash_refcount -= 1;

96 if (server_pipe_hash_refcount == 0)

97 {

98 \_dbus_hash_table_unref (server_pipe_hash);

99 server_pipe_hash = NULL;

100 }

101}

102

103static void

104debug_finalize (DBusServer \*server)

105{

106 DBusServerDebugPipe \*debug_server = (DBusServerDebugPipe\*) server;

107

108 pipe_hash_unref ();

109

110 \_dbus_server_finalize_base (server);

111

112 dbus_free (debug_server-\>name);

113 dbus_free (server);

114}

115

116static void

117debug_disconnect (DBusServer \*server)

118{

119 ((DBusServerDebugPipe\*)server)-\>disconnected = TRUE;

120}

121

122static DBusServerVTable debug_vtable = {

123 debug_finalize,

124 debug_disconnect

125};

126

134DBusServer\*

135\_dbus_server_debug_pipe_new (const char \*server_name,

136 DBusError \*error)

137{

138 DBusServerDebugPipe \*debug_server;

139 DBusString address;

140 DBusString name_str;

141

142 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

143

144 if (!pipe_hash_ref ())

145 return NULL;

146

147 if (\_dbus_hash_table_lookup_string (server_pipe_hash, server_name) != NULL)

148 {

149 dbus_set_error (error, DBUS_ERROR_ADDRESS_IN_USE, NULL);

150 pipe_hash_unref ();

151 return NULL;

152 }

153

154 debug_server = dbus_new0 (DBusServerDebugPipe, 1);

155 if (debug_server == NULL)

156 goto nomem_0;

157

158 if (!\_dbus_string_init (&address))

159 goto nomem_1;

160

161 \_dbus_string_init_const (&name_str, server_name);

162 if (!\_dbus_string_append (&address, "debug-pipe:name=") \|\|

163 !\_dbus_address_append_escaped (&address, &name_str))

164 goto nomem_2;

165

166 debug_server-\>name = \_dbus_strdup (server_name);

167 if (debug_server-\>name == NULL)

168 goto nomem_2;

169

170 if (!\_dbus_server_init_base (&debug_server-\>base,

171 &debug_vtable, &address,

172 error))

173 goto fail_3;

174

175 if (!\_dbus_hash_table_insert_string (server_pipe_hash,

176 debug_server-\>name,

177 debug_server))

178 goto nomem_4;

179

180 \_dbus_string_free (&address);

181

182 /\* server keeps the pipe hash ref \*/

183

184 \_dbus_server_trace_ref (&debug_server-\>base, 0, 1, "debug_pipe_new");

185 return (DBusServer \*)debug_server;

186

187 nomem_4:

188 \_dbus_server_finalize_base (&debug_server-\>base);

189 fail_3:

190 dbus_free (debug_server-\>name);

191 nomem_2:

192 \_dbus_string_free (&address);

193 nomem_1:

194 dbus_free (debug_server);

195 nomem_0:

196 pipe_hash_unref ();

197 if (error != NULL && !dbus_error_is_set (error))

198 \_DBUS_SET_OOM (error);

199 return NULL;

200}

201

211DBusTransport\*

212\_dbus_transport_debug_pipe_new (const char \*server_name,

213 DBusError \*error)

214{

215 DBusTransport \*client_transport;

216 DBusTransport \*server_transport;

217 DBusConnection \*connection;

218 DBusSocket client_fd, server_fd;

219 DBusServer \*server;

220 DBusString address;

221

222 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

223

224 if (server_pipe_hash == NULL)

225 {

226 dbus_set_error (error, DBUS_ERROR_NO_SERVER, NULL);

227 return NULL;

228 }

229

230 server = \_dbus_hash_table_lookup_string (server_pipe_hash,

231 server_name);

232 if (server == NULL \|\|

233 ((DBusServerDebugPipe\*)server)-\>disconnected)

234 {

235 dbus_set_error (error, DBUS_ERROR_NO_SERVER, NULL);

236 return NULL;

237 }

238

239 if (!\_dbus_string_init (&address))

240 {

241 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

242 return NULL;

243 }

244

245 if (!\_dbus_string_append (&address, "debug-pipe:name=") \|\|

246 !\_dbus_string_append (&address, server_name))

247 {

248 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

249 \_dbus_string_free (&address);

250 return NULL;

251 }

252

253 if (!\_dbus_socketpair (&client_fd, &server_fd, FALSE, NULL))

254 {

255 \_dbus_verbose ("failed to create full duplex pipe\n");

256 dbus_set_error (error, DBUS_ERROR_FAILED, "Could not create full-duplex pipe");

257 \_dbus_string_free (&address);

258 return NULL;

259 }

260

261 client_transport = \_dbus_transport_new_for_socket (client_fd,

262 NULL, &address);

263 if (client_transport == NULL)

264 {

265 \_dbus_close_socket (&client_fd, NULL);

266 \_dbus_close_socket (&server_fd, NULL);

267 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

268 \_dbus_string_free (&address);

269 return NULL;

270 }

271

272 \_dbus_string_free (&address);

273

274 \_dbus_socket_invalidate (&client_fd);

275

276 server_transport = \_dbus_transport_new_for_socket (server_fd,

277 &server-\>guid_hex, NULL);

278 if (server_transport == NULL)

279 {

280 \_dbus_transport_unref (client_transport);

281 \_dbus_close_socket (&server_fd, NULL);

282 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

283 return NULL;

284 }

285

286 \_dbus_socket_invalidate (&server_fd);

287

288 if (!\_dbus_transport_set_auth_mechanisms (server_transport,

289 (const char\*\*) server-\>auth_mechanisms))

290 {

291 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

292 \_dbus_transport_unref (server_transport);

293 \_dbus_transport_unref (client_transport);

294 return NULL;

295 }

296

297 connection = \_dbus_connection_new_for_transport (server_transport);

298 \_dbus_transport_unref (server_transport);

299 server_transport = NULL;

300

301 if (connection == NULL)

302 {

303 \_dbus_transport_unref (client_transport);

304 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

305 return NULL;

306 }

307

308 /\* See if someone wants to handle this new connection,

309 \* self-referencing for paranoia

310 \*/

311 if (server-\>new_connection_function)

312 {

313 dbus_server_ref (server);

314 (\* server-\>new_connection_function) (server, connection,

315 server-\>new_connection_data);

316 dbus_server_unref (server);

317 }

318

319 /\* If no one grabbed a reference, the connection will die,

320 \* and the client transport will get an immediate disconnect

321 \*/

322 \_dbus_connection_close_if_only_one_ref (connection);

323 dbus_connection_unref (connection);

324

325 return client_transport;

326}

327

339DBusServerListenResult

340\_dbus_server_listen_debug_pipe (DBusAddressEntry \*entry,

341 DBusServer \*\*server_p,

342 DBusError \*error)

343{

344 const char \*method;

345

346 \*server_p = NULL;

347

348 method = dbus_address_entry_get_method (entry);

349

350 if (strcmp (method, "debug-pipe") == 0)

351 {

352 const char \*name = dbus_address_entry_get_value (entry, "name");

353

354 if (name == NULL)

355 {

356 \_dbus_set_bad_address(error, "debug-pipe", "name",

357 NULL);

358 return DBUS_SERVER_LISTEN_BAD_ADDRESS;

359 }

360

361 \*server_p = \_dbus_server_debug_pipe_new (name, error);

362

363 if (\*server_p)

364 {

365 \_DBUS_ASSERT_ERROR_IS_CLEAR(error);

366 return DBUS_SERVER_LISTEN_OK;

367 }

368 else

369 {

370 \_DBUS_ASSERT_ERROR_IS_SET(error);

371 return DBUS_SERVER_LISTEN_DID_NOT_CONNECT;

372 }

373 }

374 else

375 {

376 \_DBUS_ASSERT_ERROR_IS_CLEAR(error);

377 return DBUS_SERVER_LISTEN_NOT_HANDLED;

378 }

379}

380

389DBusTransportOpenResult

390\_dbus_transport_open_debug_pipe (DBusAddressEntry \*entry,

391 DBusTransport \*\*transport_p,

392 DBusError \*error)

393{

394 const char \*method;

395

396 method = dbus_address_entry_get_method (entry);

397 \_dbus_assert (method != NULL);

398

399 if (strcmp (method, "debug-pipe") == 0)

400 {

401 const char \*name = dbus_address_entry_get_value (entry, "name");

402

403 if (name == NULL)

404 {

405 \_dbus_set_bad_address (error, "debug-pipe", "name",

406 NULL);

407 return DBUS_TRANSPORT_OPEN_BAD_ADDRESS;

408 }

409

410 \*transport_p = \_dbus_transport_debug_pipe_new (name, error);

411

412 if (\*transport_p == NULL)

413 {

414 \_DBUS_ASSERT_ERROR_IS_SET (error);

415 return DBUS_TRANSPORT_OPEN_DID_NOT_CONNECT;

416 }

417 else

418 {

419 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

420 return DBUS_TRANSPORT_OPEN_OK;

421 }

422 }

423 else

424 {

425 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

426 return DBUS_TRANSPORT_OPEN_NOT_HANDLED;

427 }

428}

429

430

433\#endif /\* DBUS_ENABLE_EMBEDDED_TESTS \*/

\_dbus_address_append_escaped

dbus_bool_t \_dbus_address_append_escaped(DBusString \*escaped, const DBusString \*unescaped)

Appends an escaped version of one string to another string, using the D-Bus address escaping mechanis...

**Definition** dbus-address.c:109

\_dbus_set_bad_address

void \_dbus_set_bad_address(DBusError \*error, const char \*address_problem_type, const char \*address_problem_field, const char \*address_problem_other)

Sets DBUS_ERROR_BAD_ADDRESS.

**Definition** dbus-address.c:70

dbus_address_entry_get_method

const char \* dbus_address_entry_get_method(DBusAddressEntry \*entry)

Returns the method string of an address entry.

**Definition** dbus-address.c:232

dbus_address_entry_get_value

const char \* dbus_address_entry_get_value(DBusAddressEntry \*entry, const char \*key)

Returns a value from a key of an entry.

**Definition** dbus-address.c:249

\_dbus_connection_new_for_transport

DBusConnection \* \_dbus_connection_new_for_transport(DBusTransport \*transport)

Creates a new connection for the given transport.

**Definition** dbus-connection.c:1253

\_dbus_connection_close_if_only_one_ref

void \_dbus_connection_close_if_only_one_ref(DBusConnection \*connection)

Used internally to handle the semantics of dbus_server_set_new_connection_function().

**Definition** dbus-connection.c:2160

dbus_connection_unref

void dbus_connection_unref(DBusConnection \*connection)

Decrements the reference count of a DBusConnection, and finalizes it if the count reaches zero.

**Definition** dbus-connection.c:2832

dbus_set_error

void dbus_set_error(DBusError \*error, const char \*name, const char \*format,...)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:356

dbus_error_is_set

dbus_bool_t dbus_error_is_set(const DBusError \*error)

Checks whether an error occurred (the error is set).

**Definition** dbus-errors.c:331

\_dbus_hash_table_insert_string

dbus_bool_t \_dbus_hash_table_insert_string(DBusHashTable \*table, char \*key, void \*value)

Creates a hash entry with the given key and value.

**Definition** dbus-hash.c:1278

\_dbus_hash_table_unref

void \_dbus_hash_table_unref(DBusHashTable \*table)

Decrements the reference count for a hash table, freeing the hash table if the count reaches zero.

**Definition** dbus-hash.c:368

\_dbus_hash_table_new

DBusHashTable \* \_dbus_hash_table_new(DBusHashType type, DBusFreeFunction key_free_function, DBusFreeFunction value_free_function)

Constructs a new hash table.

**Definition** dbus-hash.c:292

\_dbus_hash_table_lookup_string

void \* \_dbus_hash_table_lookup_string(DBusHashTable \*table, const char \*key)

Looks up the value for a given string in a hash table of type DBUS_HASH_STRING.

**Definition** dbus-hash.c:1113

DBUS_HASH_STRING

@ DBUS_HASH_STRING

Hash keys are strings.

**Definition** dbus-hash.h:69

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_dbus_strdup

char \* \_dbus_strdup(const char \*str)

Duplicates a string.

**Definition** dbus-internals.c:621

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

dbus_free

void dbus_free(void \*memory)

Frees a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:710

dbus_new0

\#define dbus_new0(type, count)

Safe macro for using dbus_malloc0().

**Definition** dbus-memory.h:60

DBUS_ERROR_ADDRESS_IN_USE

\#define DBUS_ERROR_ADDRESS_IN_USE

Can't bind a socket since its address is in use (i.e.

**Definition** dbus-protocol.h:393

DBUS_ERROR_NO_SERVER

\#define DBUS_ERROR_NO_SERVER

Unable to connect to server (probably caused by ECONNREFUSED on a socket).

**Definition** dbus-protocol.h:383

DBUS_ERROR_FAILED

\#define DBUS_ERROR_FAILED

A generic error; "something went wrong" - see the error message for more.

**Definition** dbus-protocol.h:361

DBUS_ERROR_NO_MEMORY

\#define DBUS_ERROR_NO_MEMORY

There was not enough memory to complete an operation.

**Definition** dbus-protocol.h:363

\_dbus_server_init_base

dbus_bool_t \_dbus_server_init_base(DBusServer \*server, const DBusServerVTable \*vtable, const DBusString \*address, DBusError \*error)

Initializes the members of the DBusServer base class.

**Definition** dbus-server.c:113

\_dbus_server_finalize_base

void \_dbus_server_finalize_base(DBusServer \*server)

Finalizes the members of the DBusServer base class.

**Definition** dbus-server.c:202

dbus_server_unref

void dbus_server_unref(DBusServer \*server)

Decrements the reference count of a DBusServer.

**Definition** dbus-server.c:735

dbus_server_ref

DBusServer \* dbus_server_ref(DBusServer \*server)

Increments the reference count of a DBusServer.

**Definition** dbus-server.c:703

\_dbus_string_append

dbus_bool_t \_dbus_string_append(DBusString \*str, const char \*buffer)

Appends a nul-terminated C-style string to a DBusString.

**Definition** dbus-string.c:980

\_dbus_string_init

dbus_bool_t \_dbus_string_init(DBusString \*str)

Initializes a string.

**Definition** dbus-string.c:182

\_dbus_string_init_const

void \_dbus_string_init_const(DBusString \*str, const char \*value)

Initializes a constant string.

**Definition** dbus-string.c:197

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_socketpair

dbus_bool_t \_dbus_socketpair(DBusSocket \*fd1, DBusSocket \*fd2, dbus_bool_t blocking, DBusError \*error)

Creates pair of connect sockets (as in socketpair()).

**Definition** dbus-sysdeps-unix.c:3884

\_dbus_close_socket

dbus_bool_t \_dbus_close_socket(DBusSocket \*fd, DBusError \*error)

Closes a socket and invalidates it.

**Definition** dbus-sysdeps-unix.c:314

\_dbus_transport_new_for_socket

DBusTransport \* \_dbus_transport_new_for_socket(DBusSocket fd, const DBusString \*server_guid, const DBusString \*address)

Creates a new transport for the given socket file descriptor.

**Definition** dbus-transport-socket.c:1295

\_dbus_transport_set_auth_mechanisms

dbus_bool_t \_dbus_transport_set_auth_mechanisms(DBusTransport \*transport, const char \*\*mechanisms)

Sets the SASL authentication mechanisms supported by this transport.

**Definition** dbus-transport.c:1565

\_dbus_transport_unref

void \_dbus_transport_unref(DBusTransport \*transport)

Decrements the reference count for the transport.

**Definition** dbus-transport.c:486

DBusAddressEntry

Internals of DBusAddressEntry.

**Definition** dbus-address.c:49

DBusConnection

Implementation details of DBusConnection.

**Definition** dbus-connection.c:259

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusHashTable

Internals of DBusHashTable.

**Definition** dbus-hash.c:175

DBusServerVTable

Virtual table to be implemented by all server "subclasses".

**Definition** dbus-server-protected.h:46

DBusServer

Internals of DBusServer object.

**Definition** dbus-server-protected.h:59

DBusSocket

Socket interface.

**Definition** dbus-sysdeps.h:185

DBusString

**Definition** dbus-string.h:47

DBusTransport

Object representing a transport such as a socket.

**Definition** dbus-transport-protected.h:83
