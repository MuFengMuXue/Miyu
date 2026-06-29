dbus-transport-unix.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-transport-unix.c UNIX socket subclasses of DBusTransport

3 \*

4 \* Copyright (C) 2002, 2003, 2004 Red Hat Inc.

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

27

28\#include \<stdio.h\>

29

30\#include "dbus-internals.h"

31\#include "dbus-connection-internal.h"

32\#include "dbus-transport-unix.h"

33\#include "dbus-transport-socket.h"

34\#include "dbus-transport-protected.h"

35\#include "dbus-watch.h"

36\#include "dbus-sysdeps-unix.h"

37\#include "dbus-test.h"

38

58static DBusTransport\*

59\_dbus_transport_new_for_exec (const char \*path,

60 char \*const argv\[\],

61 DBusError \*error)

62{

63 DBusSocket fd = DBUS_SOCKET_INIT;

64 DBusTransport \*transport;

65 DBusString address;

66 unsigned i;

67 char \*escaped;

68

69 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

70

71 if (!\_dbus_string_init (&address))

72 {

73 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

74 return NULL;

75 }

76

77 escaped = dbus_address_escape_value (path);

78 if (!escaped)

79 {

80 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

81 goto failed;

82 }

83

84 if (!\_dbus_string_append (&address, "unixexec:path=") \|\|

85 !\_dbus_string_append (&address, escaped))

86 {

87 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

88 dbus_free (escaped);

89 goto failed;

90 }

91

92 dbus_free (escaped);

93

94 if (argv)

95 {

96 for (i = 0; argv\[i\]; i++)

97 {

98 dbus_bool_t success;

99

100 escaped = dbus_address_escape_value (argv\[i\]);

101 if (!escaped)

102 {

103 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

104 goto failed;

105 }

106

107 success = \_dbus_string_append_printf (&address, ",argv%u=%s", i, escaped);

108 dbus_free (escaped);

109

110 if (!success)

111 {

112 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

113 goto failed;

114 }

115 }

116 }

117

118 fd = \_dbus_connect_exec (path, argv, error);

119 if (!\_dbus_socket_is_valid (fd))

120 {

121 \_DBUS_ASSERT_ERROR_IS_SET (error);

122 goto failed;

123 }

124

125 \_dbus_verbose ("Successfully connected to process %s\n",

126 path);

127

128 transport = \_dbus_transport_new_for_socket (fd, NULL, &address);

129 if (transport == NULL)

130 {

131 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

132 goto failed;

133 }

134

135 \_dbus_string_free (&address);

136

137 return transport;

138

139 failed:

140 if (\_dbus_socket_is_valid (fd))

141 \_dbus_close_socket (&fd, NULL);

142

143 \_dbus_string_free (&address);

144 return NULL;

145}

146

147

148DBusTransportOpenResult

149\_dbus_transport_open_unixexec (DBusAddressEntry \*entry,

150 DBusTransport \*\*transport_p,

151 DBusError \*error)

152{

153 const char \*method;

154

155 method = dbus_address_entry_get_method (entry);

156 \_dbus_assert (method != NULL);

157

158 if (strcmp (method, "unixexec") == 0)

159 {

160 const char \*path;

161 unsigned i;

162 char \*\*argv;

163

164 path = dbus_address_entry_get_value (entry, "path");

165 if (path == NULL)

166 {

167 \_dbus_set_bad_address (error, NULL, NULL,

168 "No process path specified");

169 return DBUS_TRANSPORT_OPEN_BAD_ADDRESS;

170 }

171

172 /\* First count argv arguments \*/

173 for (i = 1; ; i++)

174 {

175 char t\[4+20+1\]; /\* "argv" plus space for a formatted base 10 64bit integer, plus NUL \*/

176

177 snprintf (t, sizeof(t), "argv%u", i);

178

179 if (!dbus_address_entry_get_value (entry, t))

180 break;

181 }

182

183 /\* Allocate string array \*/

184 argv = dbus_new0 (char\*, i+1);

185 if (!argv)

186 {

187 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

188 return DBUS_TRANSPORT_OPEN_DID_NOT_CONNECT;

189 }

190

191 /\* Fill in string array \*/

192 for (i = 0; ; i++)

193 {

194 char t\[4+20+1\];

195 const char \*p;

196

197 snprintf (t, sizeof(t), "argv%u", i);

198

199 p = dbus_address_entry_get_value (entry, t);

200 if (!p)

201 {

202 if (i == 0)

203 /\* If argv0 isn't specified, fill in the path instead \*/

204 p = path;

205 else

206 break;

207 }

208

209 argv\[i\] = \_dbus_strdup (p);

210 if (!argv\[i\])

211 {

212 dbus_free_string_array (argv);

213 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

214 return DBUS_TRANSPORT_OPEN_DID_NOT_CONNECT;

215 }

216 }

217

218 \*transport_p = \_dbus_transport_new_for_exec (path, argv, error);

219 dbus_free_string_array (argv);

220

221 if (\*transport_p == NULL)

222 {

223 \_DBUS_ASSERT_ERROR_IS_SET (error);

224 return DBUS_TRANSPORT_OPEN_DID_NOT_CONNECT;

225 }

226 else

227 {

228 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

229 return DBUS_TRANSPORT_OPEN_OK;

230 }

231 }

232 else

233 {

234 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

235 return DBUS_TRANSPORT_OPEN_NOT_HANDLED;

236 }

237}

238

247DBusTransportOpenResult

248\_dbus_transport_open_platform_specific (DBusAddressEntry \*entry,

249 DBusTransport \*\*transport_p,

250 DBusError \*error)

251{

252\#ifdef DBUS_ENABLE_LAUNCHD

253 const char \*method;

254

255 method = dbus_address_entry_get_method (entry);

256 \_dbus_assert (method != NULL);

257

258 if (strcmp (method, "launchd") == 0)

259 {

260 DBusError tmp_error = DBUS_ERROR_INIT;

261 const char \*launchd_env_var = dbus_address_entry_get_value (entry, "env");

262 const char \*launchd_socket;

263 DBusString socket_path;

264 dbus_bool_t valid_socket;

265

266 if (!\_dbus_string_init (&socket_path))

267 {

268 \_DBUS_SET_OOM (error);

269 return FALSE;

270 }

271

272 if (launchd_env_var == NULL)

273 {

274 \_dbus_set_bad_address (error, "launchd", "env", NULL);

275 return DBUS_TRANSPORT_OPEN_BAD_ADDRESS;

276 }

277

278 valid_socket = \_dbus_lookup_launchd_socket (&socket_path, launchd_env_var, error);

279

280 if (dbus_error_is_set(error))

281 {

282 \_dbus_string_free(&socket_path);

283 return DBUS_TRANSPORT_OPEN_DID_NOT_CONNECT;

284 }

285

286 if (!valid_socket)

287 {

288 dbus_set_error(&tmp_error, DBUS_ERROR_BAD_ADDRESS,

289 "launchd's env var %s does not exist", launchd_env_var);

290 dbus_error_free(error);

291 dbus_move_error(&tmp_error, error);

292 return DBUS_TRANSPORT_OPEN_DID_NOT_CONNECT;

293 }

294

295 launchd_socket = \_dbus_string_get_const_data(&socket_path);

296 \*transport_p = \_dbus_transport_new_for_domain_socket (launchd_socket, FALSE, error);

297

298 if (\*transport_p == NULL)

299 {

300 \_DBUS_ASSERT_ERROR_IS_SET (error);

301 return DBUS_TRANSPORT_OPEN_DID_NOT_CONNECT;

302 }

303 else

304 {

305 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

306 return DBUS_TRANSPORT_OPEN_OK;

307 }

308 }

309 else

310\#endif /\* DBUS_ENABLE_LAUNCHD \*/

311 {

312 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

313 return DBUS_TRANSPORT_OPEN_NOT_HANDLED;

314 }

315}

316

\_dbus_set_bad_address

void \_dbus_set_bad_address(DBusError \*error, const char \*address_problem_type, const char \*address_problem_field, const char \*address_problem_other)

Sets DBUS_ERROR_BAD_ADDRESS.

**Definition** dbus-address.c:70

dbus_address_entry_get_method

const char \* dbus_address_entry_get_method(DBusAddressEntry \*entry)

Returns the method string of an address entry.

**Definition** dbus-address.c:232

dbus_address_escape_value

char \* dbus_address_escape_value(const char \*value)

Escapes the given string as a value in a key=value pair for a D-Bus address.

**Definition** dbus-address.c:588

dbus_address_entry_get_value

const char \* dbus_address_entry_get_value(DBusAddressEntry \*entry, const char \*key)

Returns a value from a key of an entry.

**Definition** dbus-address.c:249

DBUS_ERROR_INIT

\#define DBUS_ERROR_INIT

Expands to a suitable initializer for a DBusError on the stack.

**Definition** dbus-errors.h:64

dbus_move_error

void dbus_move_error(DBusError \*src, DBusError \*dest)

Moves an error src into dest, freeing src and overwriting dest.

**Definition** dbus-errors.c:281

dbus_set_error

void dbus_set_error(DBusError \*error, const char \*name, const char \*format,...)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:356

dbus_error_free

void dbus_error_free(DBusError \*error)

Frees an error that's been set (or just initialized), then reinitializes the error as in dbus_error_i...

**Definition** dbus-errors.c:213

dbus_error_is_set

dbus_bool_t dbus_error_is_set(const DBusError \*error)

Checks whether an error occurred (the error is set).

**Definition** dbus-errors.c:331

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

dbus_free_string_array

void dbus_free_string_array(char \*\*str_array)

Frees a NULL-terminated array of strings.

**Definition** dbus-memory.c:758

DBUS_ERROR_BAD_ADDRESS

\#define DBUS_ERROR_BAD_ADDRESS

A D-Bus bus address was malformed.

**Definition** dbus-protocol.h:373

DBUS_ERROR_NO_MEMORY

\#define DBUS_ERROR_NO_MEMORY

There was not enough memory to complete an operation.

**Definition** dbus-protocol.h:363

\_dbus_string_append

dbus_bool_t \_dbus_string_append(DBusString \*str, const char \*buffer)

Appends a nul-terminated C-style string to a DBusString.

**Definition** dbus-string.c:980

\_dbus_string_init

dbus_bool_t \_dbus_string_init(DBusString \*str)

Initializes a string.

**Definition** dbus-string.c:182

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_string_append_printf

dbus_bool_t \_dbus_string_append_printf(DBusString \*str, const char \*format,...)

Appends a printf-style formatted string to the DBusString.

**Definition** dbus-string.c:1147

\_dbus_string_get_const_data

const char \* \_dbus_string_get_const_data(const DBusString \*str)

Gets the raw character buffer from a const string.

**Definition** dbus-string.c:513

\_dbus_lookup_launchd_socket

dbus_bool_t \_dbus_lookup_launchd_socket(DBusString \*socket_path, const char \*launchd_env_var, DBusError \*error)

quries launchd for a specific env var which holds the socket path.

**Definition** dbus-sysdeps-unix.c:4486

\_dbus_close_socket

dbus_bool_t \_dbus_close_socket(DBusSocket \*fd, DBusError \*error)

Closes a socket and invalidates it.

**Definition** dbus-sysdeps-unix.c:314

\_dbus_connect_exec

DBusSocket \_dbus_connect_exec(const char \*path, char \*const argv\[\], DBusError \*error)

Creates a UNIX domain socket and connects it to the specified process to execute.

**Definition** dbus-sysdeps-unix.c:1054

\_dbus_transport_new_for_socket

DBusTransport \* \_dbus_transport_new_for_socket(DBusSocket fd, const DBusString \*server_guid, const DBusString \*address)

Creates a new transport for the given socket file descriptor.

**Definition** dbus-transport-socket.c:1295

\_dbus_transport_new_for_domain_socket

DBusTransport \* \_dbus_transport_new_for_domain_socket(const char \*path, dbus_bool_t abstract, DBusError \*error)

Creates a new transport for the given Unix domain socket path.

**Definition** dbus-transport-socket.c:1518

\_dbus_transport_open_platform_specific

DBusTransportOpenResult \_dbus_transport_open_platform_specific(DBusAddressEntry \*entry, DBusTransport \*\*transport_p, DBusError \*error)

Opens platform specific transport types.

**Definition** dbus-transport-unix.c:248

DBusAddressEntry

Internals of DBusAddressEntry.

**Definition** dbus-address.c:49

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusSocket

Socket interface.

**Definition** dbus-sysdeps.h:185

DBusString

**Definition** dbus-string.h:47

DBusTransport

Object representing a transport such as a socket.

**Definition** dbus-transport-protected.h:83
