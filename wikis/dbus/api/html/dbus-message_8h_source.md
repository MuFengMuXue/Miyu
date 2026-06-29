dbus-message.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-message.h DBusMessage object

3 \*

4 \* Copyright (C) 2002, 2003, 2005 Red Hat Inc.

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

29\#ifndef DBUS_MESSAGE_H

30\#define DBUS_MESSAGE_H

31

32\#include \<dbus/dbus-macros.h\>

33\#include \<dbus/dbus-types.h\>

34\#include \<dbus/dbus-arch-deps.h\>

35\#include \<dbus/dbus-memory.h\>

36\#include \<dbus/dbus-errors.h\>

37\#include \<stdarg.h\>

38

39DBUS_BEGIN_DECLS

40

46typedef struct DBusMessage DBusMessage;

58typedef struct DBusMessageIter DBusMessageIter;

59

63struct DBusMessageIter

64{

65\#if DBUS_SIZEOF_VOID_P \> 8

66 void \*dummy\[16\];

67\#else

68 void \*dummy1;

69 void \*dummy2;

70 dbus_uint32_t dummy3;

71 int dummy4;

72 int dummy5;

73 int dummy6;

74 int dummy7;

75 int dummy8;

76 int dummy9;

77 int dummy10;

78 int dummy11;

79 int pad1;

80 void \*pad2;

81 void \*pad3;

82\#endif

83};

84

89\#if DBUS_SIZEOF_VOID_P \> 8

90\#define DBUS_MESSAGE_ITER_INIT_CLOSED \\

91{ \\

92 { \\

93 NULL, NULL, NULL, NULL, \\

94 NULL, NULL, NULL, NULL, \\

95 NULL, NULL, NULL, NULL, \\

96 NULL, NULL, NULL, NULL \\

97 } \\

98}

99\#else

100\#define DBUS_MESSAGE_ITER_INIT_CLOSED \\

101{ \\

102 NULL, /\* dummy1 \*/ \\

103 NULL, /\* dummy2 \*/ \\

104 0, /\* dummy3 \*/ \\

105 0, /\* dummy4 \*/ \\

106 0, /\* dummy5 \*/ \\

107 0, /\* dummy6 \*/ \\

108 0, /\* dummy7 \*/ \\

109 0, /\* dummy8 \*/ \\

110 0, /\* dummy9 \*/ \\

111 0, /\* dummy10 \*/ \\

112 0, /\* dummy11 \*/ \\

113 0, /\* pad1 \*/ \\

114 NULL, /\* pad2 \*/ \\

115 NULL /\* pad3 \*/ \\

116}

117\#endif

118

119DBUS_EXPORT

120DBusMessage\* dbus_message_new (int message_type);

121DBUS_EXPORT

122DBusMessage\* dbus_message_new_method_call (const char \*bus_name,

123 const char \*path,

124 const char \*iface,

125 const char \*method);

126DBUS_EXPORT

127DBusMessage\* dbus_message_new_method_return (DBusMessage \*method_call);

128DBUS_EXPORT

129DBusMessage\* dbus_message_new_signal (const char \*path,

130 const char \*iface,

131 const char \*name);

132DBUS_EXPORT

133DBusMessage\* dbus_message_new_error (DBusMessage \*reply_to,

134 const char \*error_name,

135 const char \*error_message);

136DBUS_EXPORT

137DBusMessage\* dbus_message_new_error_printf (DBusMessage \*reply_to,

138 const char \*error_name,

139 const char \*error_format,

140 ...) \_DBUS_GNUC_PRINTF (3, 4);

141

142DBUS_EXPORT

143DBusMessage\* dbus_message_copy (const DBusMessage \*message);

144

145DBUS_EXPORT

146DBusMessage\* dbus_message_ref (DBusMessage \*message);

147DBUS_EXPORT

148void dbus_message_unref (DBusMessage \*message);

149DBUS_EXPORT

150int dbus_message_get_type (DBusMessage \*message);

151DBUS_EXPORT

152dbus_bool_t dbus_message_set_path (DBusMessage \*message,

153 const char \*object_path);

154DBUS_EXPORT

155const char\* dbus_message_get_path (DBusMessage \*message);

156DBUS_EXPORT

157dbus_bool_t dbus_message_has_path (DBusMessage \*message,

158 const char \*object_path);

159DBUS_EXPORT

160dbus_bool_t dbus_message_set_interface (DBusMessage \*message,

161 const char \*iface);

162DBUS_EXPORT

163const char\* dbus_message_get_interface (DBusMessage \*message);

164DBUS_EXPORT

165dbus_bool_t dbus_message_has_interface (DBusMessage \*message,

166 const char \*iface);

167DBUS_EXPORT

168dbus_bool_t dbus_message_set_member (DBusMessage \*message,

169 const char \*member);

170DBUS_EXPORT

171const char\* dbus_message_get_member (DBusMessage \*message);

172DBUS_EXPORT

173dbus_bool_t dbus_message_has_member (DBusMessage \*message,

174 const char \*member);

175DBUS_EXPORT

176dbus_bool_t dbus_message_set_error_name (DBusMessage \*message,

177 const char \*name);

178DBUS_EXPORT

179const char\* dbus_message_get_error_name (DBusMessage \*message);

180DBUS_EXPORT

181dbus_bool_t dbus_message_set_destination (DBusMessage \*message,

182 const char \*destination);

183DBUS_EXPORT

184const char\* dbus_message_get_destination (DBusMessage \*message);

185DBUS_EXPORT

186dbus_bool_t dbus_message_set_sender (DBusMessage \*message,

187 const char \*sender);

188DBUS_EXPORT

189const char\* dbus_message_get_sender (DBusMessage \*message);

190DBUS_EXPORT

191const char\* dbus_message_get_signature (DBusMessage \*message);

192DBUS_EXPORT

193void dbus_message_set_no_reply (DBusMessage \*message,

194 dbus_bool_t no_reply);

195DBUS_EXPORT

196dbus_bool_t dbus_message_get_no_reply (DBusMessage \*message);

197DBUS_EXPORT

198dbus_bool_t dbus_message_is_method_call (DBusMessage \*message,

199 const char \*iface,

200 const char \*method);

201DBUS_EXPORT

202dbus_bool_t dbus_message_is_signal (DBusMessage \*message,

203 const char \*iface,

204 const char \*signal_name);

205DBUS_EXPORT

206dbus_bool_t dbus_message_is_error (DBusMessage \*message,

207 const char \*error_name);

208DBUS_EXPORT

209dbus_bool_t dbus_message_has_destination (DBusMessage \*message,

210 const char \*bus_name);

211DBUS_EXPORT

212dbus_bool_t dbus_message_has_sender (DBusMessage \*message,

213 const char \*unique_bus_name);

214DBUS_EXPORT

215dbus_bool_t dbus_message_has_signature (DBusMessage \*message,

216 const char \*signature);

217DBUS_EXPORT

218dbus_uint32_t dbus_message_get_serial (DBusMessage \*message);

219DBUS_EXPORT

220void dbus_message_set_serial (DBusMessage \*message,

221 dbus_uint32_t serial);

222DBUS_EXPORT

223dbus_bool_t dbus_message_set_reply_serial (DBusMessage \*message,

224 dbus_uint32_t reply_serial);

225DBUS_EXPORT

226dbus_uint32_t dbus_message_get_reply_serial (DBusMessage \*message);

227

228DBUS_EXPORT

229void dbus_message_set_auto_start (DBusMessage \*message,

230 dbus_bool_t auto_start);

231DBUS_EXPORT

232dbus_bool_t dbus_message_get_auto_start (DBusMessage \*message);

233

234DBUS_EXPORT

235dbus_bool_t dbus_message_get_path_decomposed (DBusMessage \*message,

236 char \*\*\*path);

237

238DBUS_EXPORT

239const char \*dbus_message_get_container_instance (DBusMessage \*message);

240DBUS_EXPORT

241dbus_bool_t dbus_message_set_container_instance (DBusMessage \*message,

242 const char \*object_path);

243

244DBUS_EXPORT

245dbus_bool_t dbus_message_append_args (DBusMessage \*message,

246 int first_arg_type,

247 ...);

248DBUS_EXPORT

249dbus_bool_t dbus_message_append_args_valist (DBusMessage \*message,

250 int first_arg_type,

251 va_list var_args);

252DBUS_EXPORT

253dbus_bool_t dbus_message_get_args (DBusMessage \*message,

254 DBusError \*error,

255 int first_arg_type,

256 ...);

257DBUS_EXPORT

258dbus_bool_t dbus_message_get_args_valist (DBusMessage \*message,

259 DBusError \*error,

260 int first_arg_type,

261 va_list var_args);

262

263DBUS_EXPORT

264dbus_bool_t dbus_message_contains_unix_fds (DBusMessage \*message);

265

266DBUS_EXPORT

267void dbus_message_iter_init_closed (DBusMessageIter \*iter);

268DBUS_EXPORT

269dbus_bool_t dbus_message_iter_init (DBusMessage \*message,

270 DBusMessageIter \*iter);

271DBUS_EXPORT

272dbus_bool_t dbus_message_iter_has_next (DBusMessageIter \*iter);

273DBUS_EXPORT

274dbus_bool_t dbus_message_iter_next (DBusMessageIter \*iter);

275DBUS_EXPORT

276char\* dbus_message_iter_get_signature (DBusMessageIter \*iter);

277DBUS_EXPORT

278int dbus_message_iter_get_arg_type (DBusMessageIter \*iter);

279DBUS_EXPORT

280int dbus_message_iter_get_element_type (DBusMessageIter \*iter);

281DBUS_EXPORT

282void dbus_message_iter_recurse (DBusMessageIter \*iter,

283 DBusMessageIter \*sub);

284DBUS_EXPORT

285void dbus_message_iter_get_basic (DBusMessageIter \*iter,

286 void \*value);

287DBUS_EXPORT

288int dbus_message_iter_get_element_count(DBusMessageIter \*iter);

289

290\#ifndef DBUS_DISABLE_DEPRECATED

291/\* This function returns the wire protocol size of the array in bytes,

292 \* you do not want to know that probably

293 \*/

294DBUS_EXPORT

295DBUS_DEPRECATED int dbus_message_iter_get_array_len (DBusMessageIter \*iter);

296\#endif

297DBUS_EXPORT

298void dbus_message_iter_get_fixed_array (DBusMessageIter \*iter,

299 void \*value,

300 int \*n_elements);

301

302

303DBUS_EXPORT

304void dbus_message_iter_init_append (DBusMessage \*message,

305 DBusMessageIter \*iter);

306DBUS_EXPORT

307dbus_bool_t dbus_message_iter_append_basic (DBusMessageIter \*iter,

308 int type,

309 const void \*value);

310DBUS_EXPORT

311dbus_bool_t dbus_message_iter_append_fixed_array (DBusMessageIter \*iter,

312 int element_type,

313 const void \*value,

314 int n_elements);

315DBUS_EXPORT

316dbus_bool_t dbus_message_iter_open_container (DBusMessageIter \*iter,

317 int type,

318 const char \*contained_signature,

319 DBusMessageIter \*sub);

320DBUS_EXPORT

321dbus_bool_t dbus_message_iter_close_container (DBusMessageIter \*iter,

322 DBusMessageIter \*sub);

323DBUS_EXPORT

324void dbus_message_iter_abandon_container (DBusMessageIter \*iter,

325 DBusMessageIter \*sub);

326

327DBUS_EXPORT

328void dbus_message_iter_abandon_container_if_open (DBusMessageIter \*iter,

329 DBusMessageIter \*sub);

330

331DBUS_EXPORT

332void dbus_message_lock (DBusMessage \*message);

333

334DBUS_EXPORT

335dbus_bool_t dbus_set_error_from_message (DBusError \*error,

336 DBusMessage \*message);

337

338

339DBUS_EXPORT

340dbus_bool_t dbus_message_allocate_data_slot (dbus_int32_t \*slot_p);

341DBUS_EXPORT

342void dbus_message_free_data_slot (dbus_int32_t \*slot_p);

343DBUS_EXPORT

344dbus_bool_t dbus_message_set_data (DBusMessage \*message,

345 dbus_int32_t slot,

346 void \*data,

347 DBusFreeFunction free_data_func);

348DBUS_EXPORT

349void\* dbus_message_get_data (DBusMessage \*message,

350 dbus_int32_t slot);

351

352DBUS_EXPORT

353int dbus_message_type_from_string (const char \*type_str);

354DBUS_EXPORT

355const char\* dbus_message_type_to_string (int type);

356

357DBUS_EXPORT

358dbus_bool_t dbus_message_marshal (DBusMessage \*msg,

359 char \*\*marshalled_data_p,

360 int \*len_p);

361DBUS_EXPORT

362DBusMessage\* dbus_message_demarshal (const char \*str,

363 int len,

364 DBusError \*error);

365

366DBUS_EXPORT

367int dbus_message_demarshal_bytes_needed (const char \*str,

368 int len);

369

370DBUS_EXPORT

371void dbus_message_set_allow_interactive_authorization (DBusMessage \*message,

372 dbus_bool_t allow);

373

374DBUS_EXPORT

375dbus_bool_t dbus_message_get_allow_interactive_authorization (

376 DBusMessage \*message);

377

390static inline void

391dbus_clear_message (DBusMessage \*\*pointer_to_message)

392{

393 \_dbus_clear_pointer_impl (DBusMessage, pointer_to_message,

394 dbus_message_unref);

395}

396

399DBUS_END_DECLS

400

401\#endif /\* DBUS_MESSAGE_H \*/

DBUS_DEPRECATED

\#define DBUS_DEPRECATED

Tells the compiler to warn about a function or type if it's used.

**Definition** dbus-macros.h:60

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

dbus_message_has_destination

dbus_bool_t dbus_message_has_destination(DBusMessage \*message, const char \*name)

Checks whether the message was sent to the given name.

**Definition** dbus-message.c:3953

dbus_message_set_interface

dbus_bool_t dbus_message_set_interface(DBusMessage \*message, const char \*iface)

Sets the interface this message is being sent to (for DBUS_MESSAGE_TYPE_METHOD_CALL) or the interface...

**Definition** dbus-message.c:3461

dbus_message_has_interface

dbus_bool_t dbus_message_has_interface(DBusMessage \*message, const char \*iface)

Checks if the message has an interface.

**Definition** dbus-message.c:3512

dbus_message_set_no_reply

void dbus_message_set_no_reply(DBusMessage \*message, dbus_bool_t no_reply)

Sets a flag indicating that the message does not want a reply; if this flag is set,...

**Definition** dbus-message.c:3247

dbus_message_append_args_valist

dbus_bool_t dbus_message_append_args_valist(DBusMessage \*message, int first_arg_type, va_list var_args)

Like dbus_message_append_args() but takes a va_list for use by language bindings.

**Definition** dbus-message.c:1875

dbus_message_get_sender

const char \* dbus_message_get_sender(DBusMessage \*message)

Gets the unique name of the connection which originated this message, or NULL if unknown or inapplica...

**Definition** dbus-message.c:3773

dbus_message_set_auto_start

void dbus_message_set_auto_start(DBusMessage \*message, dbus_bool_t auto_start)

Sets a flag indicating that an owner for the destination name will be automatically started before th...

**Definition** dbus-message.c:3289

dbus_message_iter_append_basic

dbus_bool_t dbus_message_iter_append_basic(DBusMessageIter \*iter, int type, const void \*value)

Appends a basic-typed value to the message.

**Definition** dbus-message.c:2771

dbus_message_get_path

const char \* dbus_message_get_path(DBusMessage \*message)

Gets the object path this message is being sent to (for DBUS_MESSAGE_TYPE_METHOD_CALL) or being emitt...

**Definition** dbus-message.c:3359

dbus_message_get_interface

const char \* dbus_message_get_interface(DBusMessage \*message)

Gets the interface this message is being sent to (for DBUS_MESSAGE_TYPE_METHOD_CALL) or being emitted...

**Definition** dbus-message.c:3490

dbus_message_free_data_slot

DBUS_EXPORT void dbus_message_free_data_slot(dbus_int32_t \*slot_p)

Deallocates a global ID for message data slots.

**Definition** dbus-message.c:4968

dbus_message_set_data

DBUS_EXPORT dbus_bool_t dbus_message_set_data(DBusMessage \*message, dbus_int32_t slot, void \*data, DBusFreeFunction free_data_func)

Stores a pointer on a DBusMessage, along with an optional function to be used for freeing the data wh...

**Definition** dbus-message.c:4989

dbus_message_new_error

DBusMessage \* dbus_message_new_error(DBusMessage \*reply_to, const char \*error_name, const char \*error_message)

Creates a new message that is an error reply to another message.

**Definition** dbus-message.c:1515

dbus_message_type_to_string

DBUS_EXPORT const char \* dbus_message_type_to_string(int type)

Utility function to convert a D-Bus message type into a machine-readable string (not translated).

**Definition** dbus-message.c:5081

dbus_message_has_sender

dbus_bool_t dbus_message_has_sender(DBusMessage \*message, const char \*name)

Checks whether the message has the given unique name as its sender.

**Definition** dbus-message.c:3988

dbus_message_get_serial

dbus_uint32_t dbus_message_get_serial(DBusMessage \*message)

Returns the serial of a message or 0 if none has been specified.

**Definition** dbus-message.c:1168

dbus_message_set_member

dbus_bool_t dbus_message_set_member(DBusMessage \*message, const char \*member)

Sets the interface member being invoked (DBUS_MESSAGE_TYPE_METHOD_CALL) or emitted (DBUS_MESSAGE_TYPE...

**Definition** dbus-message.c:3549

dbus_message_marshal

DBUS_EXPORT dbus_bool_t dbus_message_marshal(DBusMessage \*msg, char \*\*marshalled_data_p, int \*len_p)

Turn a DBusMessage into the marshalled form as described in the D-Bus specification.

**Definition** dbus-message.c:5111

dbus_message_iter_get_basic

void dbus_message_iter_get_basic(DBusMessageIter \*iter, void \*value)

Reads a basic-typed value from the message iterator.

**Definition** dbus-message.c:2369

dbus_message_get_type

int dbus_message_get_type(DBusMessage \*message)

Gets the type of a message.

**Definition** dbus-message.c:1767

dbus_message_copy

DBusMessage \* dbus_message_copy(const DBusMessage \*message)

Creates a new message that is an exact replica of the message specified, except that its refcount is ...

**Definition** dbus-message.c:1632

dbus_message_get_error_name

const char \* dbus_message_get_error_name(DBusMessage \*message)

Gets the error name (DBUS_MESSAGE_TYPE_ERROR only) or NULL if none.

**Definition** dbus-message.c:3660

dbus_message_iter_next

dbus_bool_t dbus_message_iter_next(DBusMessageIter \*iter)

Moves the iterator to the next field, if any.

**Definition** dbus-message.c:2186

dbus_message_append_args

dbus_bool_t dbus_message_append_args(DBusMessage \*message, int first_arg_type,...)

Appends fields to a message given a variable argument list.

**Definition** dbus-message.c:1843

dbus_message_iter_get_arg_type

int dbus_message_iter_get_arg_type(DBusMessageIter \*iter)

Returns the argument type of the argument that the message iterator points to.

**Definition** dbus-message.c:2211

dbus_message_get_no_reply

dbus_bool_t dbus_message_get_no_reply(DBusMessage \*message)

Returns TRUE if the message does not expect a reply.

**Definition** dbus-message.c:3266

dbus_message_demarshal_bytes_needed

DBUS_EXPORT int dbus_message_demarshal_bytes_needed(const char \*str, int len)

Returns the number of bytes required to be in the buffer to demarshal a D-Bus message.

**Definition** dbus-message.c:5240

dbus_message_new_signal

DBusMessage \* dbus_message_new_signal(const char \*path, const char \*iface, const char \*name)

Constructs a new message representing a signal emission.

**Definition** dbus-message.c:1469

dbus_message_iter_append_fixed_array

dbus_bool_t dbus_message_iter_append_fixed_array(DBusMessageIter \*iter, int element_type, const void \*value, int n_elements)

Appends a block of fixed-length values to an array.

**Definition** dbus-message.c:2922

dbus_message_iter_abandon_container

void dbus_message_iter_abandon_container(DBusMessageIter \*iter, DBusMessageIter \*sub)

Abandons creation of a contained-typed value and frees resources created by dbus_message_iter_open_co...

**Definition** dbus-message.c:3123

dbus_message_new_error_printf

DBusMessage \* dbus_message_new_error_printf(DBusMessage \*reply_to, const char \*error_name, const char \*error_format,...)

Creates a new message that is an error reply to another message, allowing you to use printf formattin...

**Definition** dbus-message.c:1587

dbus_message_is_error

dbus_bool_t dbus_message_is_error(DBusMessage \*message, const char \*error_name)

Checks whether the message is an error reply with the given error name.

**Definition** dbus-message.c:3920

dbus_message_contains_unix_fds

dbus_bool_t dbus_message_contains_unix_fds(DBusMessage \*message)

Checks whether a message contains unix fds.

**Definition** dbus-message.c:4088

dbus_message_iter_recurse

void dbus_message_iter_recurse(DBusMessageIter \*iter, DBusMessageIter \*sub)

Recurses into a container value when reading values from a message, initializing a sub-iterator to us...

**Definition** dbus-message.c:2267

dbus_message_ref

DBusMessage \* dbus_message_ref(DBusMessage \*message)

Increments the reference count of a DBusMessage.

**Definition** dbus-message.c:1712

dbus_message_get_auto_start

dbus_bool_t dbus_message_get_auto_start(DBusMessage \*message)

Returns TRUE if the message will cause an owner for destination name to be auto-started.

**Definition** dbus-message.c:3308

dbus_message_iter_get_element_type

int dbus_message_iter_get_element_type(DBusMessageIter \*iter)

Returns the element type of the array that the message iterator points to.

**Definition** dbus-message.c:2230

dbus_message_set_error_name

dbus_bool_t dbus_message_set_error_name(DBusMessage \*message, const char \*error_name)

Sets the name of the error (DBUS_MESSAGE_TYPE_ERROR).

**Definition** dbus-message.c:3634

dbus_message_has_signature

dbus_bool_t dbus_message_has_signature(DBusMessage \*message, const char \*signature)

Checks whether the message has the given signature; see dbus_message_get_signature() for more details...

**Definition** dbus-message.c:4017

dbus_message_iter_open_container

dbus_bool_t dbus_message_iter_open_container(DBusMessageIter \*iter, int type, const char \*contained_signature, DBusMessageIter \*sub)

Appends a container-typed value to the message.

**Definition** dbus-message.c:2986

dbus_message_get_reply_serial

dbus_uint32_t dbus_message_get_reply_serial(DBusMessage \*message)

Returns the serial that the message is a reply to or 0 if none.

**Definition** dbus-message.c:1208

dbus_message_new_method_return

DBusMessage \* dbus_message_new_method_return(DBusMessage \*method_call)

Constructs a message that is a reply to a method call.

**Definition** dbus-message.c:1418

dbus_message_new_method_call

DBusMessage \* dbus_message_new_method_call(const char \*destination, const char \*path, const char \*iface, const char \*method)

Constructs a new message to invoke a method on a remote object.

**Definition** dbus-message.c:1378

dbus_message_iter_init

dbus_bool_t dbus_message_iter_init(DBusMessage \*message, DBusMessageIter \*iter)

Initializes a DBusMessageIter for reading the arguments of the message passed in.

**Definition** dbus-message.c:2136

dbus_message_set_sender

dbus_bool_t dbus_message_set_sender(DBusMessage \*message, const char \*sender)

Sets the message sender.

**Definition** dbus-message.c:3742

dbus_message_iter_abandon_container_if_open

void dbus_message_iter_abandon_container_if_open(DBusMessageIter \*iter, DBusMessageIter \*sub)

Abandons creation of a contained-typed value and frees resources created by dbus_message_iter_open_co...

**Definition** dbus-message.c:3182

dbus_message_set_serial

DBUS_EXPORT void dbus_message_set_serial(DBusMessage \*message, dbus_uint32_t serial)

Sets the serial number of a message.

**Definition** dbus-message.c:301

dbus_message_get_destination

const char \* dbus_message_get_destination(DBusMessage \*message)

Gets the destination of a message or NULL if there is none set.

**Definition** dbus-message.c:3713

dbus_message_set_path

dbus_bool_t dbus_message_set_path(DBusMessage \*message, const char \*object_path)

Sets the object path this message is being sent to (for DBUS_MESSAGE_TYPE_METHOD_CALL) or the one a s...

**Definition** dbus-message.c:3330

dbus_message_iter_has_next

dbus_bool_t dbus_message_iter_has_next(DBusMessageIter \*iter)

Checks if an iterator has any more fields.

**Definition** dbus-message.c:2167

dbus_message_get_args_valist

dbus_bool_t dbus_message_get_args_valist(DBusMessage \*message, DBusError \*error, int first_arg_type, va_list var_args)

Like dbus_message_get_args but takes a va_list for use by language bindings.

**Definition** dbus-message.c:2061

dbus_message_iter_get_signature

char \* dbus_message_iter_get_signature(DBusMessageIter \*iter)

Returns the current signature of a message iterator.

**Definition** dbus-message.c:2292

dbus_message_unref

void dbus_message_unref(DBusMessage \*message)

Decrements the reference count of a DBusMessage, freeing the message if the count reaches 0.

**Definition** dbus-message.c:1735

dbus_message_iter_get_array_len

int dbus_message_iter_get_array_len(DBusMessageIter \*iter)

Returns the number of bytes in the array as marshaled in the wire protocol.

**Definition** dbus-message.c:2458

dbus_message_new

DBusMessage \* dbus_message_new(int message_type)

Constructs a new message of the given message type.

**Definition** dbus-message.c:1334

dbus_set_error_from_message

dbus_bool_t dbus_set_error_from_message(DBusError \*error, DBusMessage \*message)

Sets a DBusError based on the contents of the given message.

**Definition** dbus-message.c:4059

dbus_message_type_from_string

DBUS_EXPORT int dbus_message_type_from_string(const char \*type_str)

Utility function to convert a machine-readable (not translated) string into a D-Bus message type.

**Definition** dbus-message.c:5053

dbus_message_iter_get_element_count

int dbus_message_iter_get_element_count(DBusMessageIter \*iter)

Returns the number of elements in the array-typed value pointed to by the iterator.

**Definition** dbus-message.c:2414

dbus_message_set_destination

dbus_bool_t dbus_message_set_destination(DBusMessage \*message, const char \*destination)

Sets the message's destination.

**Definition** dbus-message.c:3688

dbus_message_has_path

dbus_bool_t dbus_message_has_path(DBusMessage \*message, const char \*path)

Checks if the message has a particular object path.

**Definition** dbus-message.c:3383

dbus_message_lock

DBUS_EXPORT void dbus_message_lock(DBusMessage \*message)

Locks a message.

**Definition** dbus-message.c:431

dbus_message_has_member

dbus_bool_t dbus_message_has_member(DBusMessage \*message, const char \*member)

Checks if the message has an interface member.

**Definition** dbus-message.c:3598

dbus_message_get_args

dbus_bool_t dbus_message_get_args(DBusMessage \*message, DBusError \*error, int first_arg_type,...)

Gets arguments from a message given a variable argument list.

**Definition** dbus-message.c:2032

dbus_message_is_method_call

dbus_bool_t dbus_message_is_method_call(DBusMessage \*message, const char \*iface, const char \*method)

Checks whether the message is a method call with the given interface and member fields.

**Definition** dbus-message.c:3865

dbus_message_iter_get_fixed_array

void dbus_message_iter_get_fixed_array(DBusMessageIter \*iter, void \*value, int \*n_elements)

Reads a block of fixed-length values from the message iterator.

**Definition** dbus-message.c:2503

dbus_message_set_allow_interactive_authorization

DBUS_EXPORT void dbus_message_set_allow_interactive_authorization(DBusMessage \*message, dbus_bool_t allow)

Sets a flag indicating that the caller of the method is prepared to wait for interactive authorizatio...

**Definition** dbus-message.c:5300

dbus_message_get_allow_interactive_authorization

DBUS_EXPORT dbus_bool_t dbus_message_get_allow_interactive_authorization(DBusMessage \*message)

Returns whether the flag controlled by dbus_message_set_allow_interactive_authorization() has been se...

**Definition** dbus-message.c:5318

dbus_message_set_reply_serial

dbus_bool_t dbus_message_set_reply_serial(DBusMessage \*message, dbus_uint32_t reply_serial)

Sets the reply serial of a message (the serial of the message this is a reply to).

**Definition** dbus-message.c:1184

dbus_message_is_signal

dbus_bool_t dbus_message_is_signal(DBusMessage \*message, const char \*iface, const char \*signal_name)

Checks whether the message is a signal with the given interface and member fields.

**Definition** dbus-message.c:3893

dbus_message_get_signature

const char \* dbus_message_get_signature(DBusMessage \*message)

Gets the type signature of the message, i.e.

**Definition** dbus-message.c:3806

dbus_message_set_container_instance

dbus_bool_t dbus_message_set_container_instance(DBusMessage \*message, const char \*object_path)

Sets the container instance this message was sent from.

**Definition** dbus-message.c:4110

dbus_message_iter_close_container

dbus_bool_t dbus_message_iter_close_container(DBusMessageIter \*iter, DBusMessageIter \*sub)

Closes a container-typed value appended to the message; may write out more information to the message...

**Definition** dbus-message.c:3089

dbus_message_demarshal

DBUS_EXPORT DBusMessage \* dbus_message_demarshal(const char \*str, int len, DBusError \*error)

Demarshal a D-Bus message from the format described in the D-Bus specification.

**Definition** dbus-message.c:5173

dbus_message_get_path_decomposed

dbus_bool_t dbus_message_get_path_decomposed(DBusMessage \*message, char \*\*\*path)

Gets the object path this message is being sent to (for DBUS_MESSAGE_TYPE_METHOD_CALL) or being emitt...

**Definition** dbus-message.c:3427

dbus_message_iter_init_closed

DBUS_EXPORT void dbus_message_iter_init_closed(DBusMessageIter \*iter)

Initialize iter as if with DBUS_MESSAGE_ITER_INIT_CLOSED.

**Definition** dbus-message.c:755

dbus_message_get_member

const char \* dbus_message_get_member(DBusMessage \*message)

Gets the interface member being invoked (DBUS_MESSAGE_TYPE_METHOD_CALL) or emitted (DBUS_MESSAGE_TYPE...

**Definition** dbus-message.c:3576

dbus_message_iter_init_append

void dbus_message_iter_init_append(DBusMessage \*message, DBusMessageIter \*iter)

Initializes a DBusMessageIter for appending arguments to the end of a message.

**Definition** dbus-message.c:2533

dbus_message_get_data

DBUS_EXPORT void \* dbus_message_get_data(DBusMessage \*message, dbus_int32_t slot)

Retrieves data previously set with dbus_message_set_data().

**Definition** dbus-message.c:5025

dbus_message_allocate_data_slot

DBUS_EXPORT dbus_bool_t dbus_message_allocate_data_slot(dbus_int32_t \*slot_p)

Allocates an integer ID to be used for storing application-specific data on any DBusMessage.

**Definition** dbus-message.c:4950

dbus_message_get_container_instance

const char \* dbus_message_get_container_instance(DBusMessage \*message)

Gets the container instance this message was sent from, or NULL if none.

**Definition** dbus-message.c:4136

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusMessageIter

DBusMessageIter struct; contains no public fields.

**Definition** dbus-message.h:64

DBusMessageIter::dummy8

int dummy8

Don't use this.

**Definition** dbus-message.h:75

DBusMessageIter::dummy11

int dummy11

Don't use this.

**Definition** dbus-message.h:78

DBusMessageIter::dummy4

int dummy4

Don't use this.

**Definition** dbus-message.h:71

DBusMessageIter::pad1

int pad1

Don't use this.

**Definition** dbus-message.h:79

DBusMessageIter::dummy5

int dummy5

Don't use this.

**Definition** dbus-message.h:72

DBusMessageIter::pad2

void \* pad2

Don't use this.

**Definition** dbus-message.h:80

DBusMessageIter::dummy1

void \* dummy1

Don't use this.

**Definition** dbus-message.h:68

DBusMessageIter::dummy2

void \* dummy2

Don't use this.

**Definition** dbus-message.h:69

DBusMessageIter::dummy6

int dummy6

Don't use this.

**Definition** dbus-message.h:73

DBusMessageIter::dummy3

dbus_uint32_t dummy3

Don't use this.

**Definition** dbus-message.h:70

DBusMessageIter::dummy7

int dummy7

Don't use this.

**Definition** dbus-message.h:74

DBusMessageIter::dummy10

int dummy10

Don't use this.

**Definition** dbus-message.h:77

DBusMessageIter::dummy9

int dummy9

Don't use this.

**Definition** dbus-message.h:76

DBusMessageIter::pad3

void \* pad3

Don't use this.

**Definition** dbus-message.h:81

DBusMessage

Internals of DBusMessage.

**Definition** dbus-message-private.h:102
