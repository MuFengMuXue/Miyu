dbus-syntax.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-syntax.c - utility functions for strings with special syntax

3 \*

4 \* Author: Simon McVittie \<simon.mcvittie@collabora.co.uk\>

5 \* Copyright © 2011 Nokia Corporation

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

28\#include "dbus-syntax.h"

29

30\#include "dbus-internals.h"

31\#include "dbus-marshal-validate.h"

32\#include "dbus-shared.h"

33

55dbus_bool_t

56dbus_validate_path (const char \*path,

57 DBusError \*error)

58{

59 DBusString str;

60 int len;

61

62 \_dbus_return_val_if_fail (path != NULL, FALSE);

63

64 \_dbus_string_init_const (&str, path);

65 len = \_dbus_string_get_length (&str);

66

67 /\* In general, it ought to be valid... \*/

68 if (\_DBUS_LIKELY (\_dbus_validate_path (&str, 0, len)))

69 return TRUE;

70

71 /\* slow path: string is invalid, find out why \*/

72

73 if (!\_dbus_string_validate_utf8 (&str, 0, len))

74 {

75 /\* don't quote the actual string here, since a DBusError also needs to

76 \* be valid UTF-8 \*/

77 dbus_set_error (error, DBUS_ERROR_INVALID_ARGS,

78 "Object path was not valid UTF-8");

79 return FALSE;

80 }

81

82 /\* FIXME: later, diagnose exactly how it was invalid \*/

83 dbus_set_error (error, DBUS_ERROR_INVALID_ARGS,

84 "Object path was not valid: '%s'", path);

85 return FALSE;

86}

87

102dbus_bool_t

103dbus_validate_interface (const char \*name,

104 DBusError \*error)

105{

106 DBusString str;

107 int len;

108

109 \_dbus_return_val_if_fail (name != NULL, FALSE);

110

111 \_dbus_string_init_const (&str, name);

112 len = \_dbus_string_get_length (&str);

113

114 /\* In general, it ought to be valid... \*/

115 if (\_DBUS_LIKELY (\_dbus_validate_interface (&str, 0, len)))

116 return TRUE;

117

118 /\* slow path: string is invalid, find out why \*/

119

120 if (!\_dbus_string_validate_utf8 (&str, 0, len))

121 {

122 /\* don't quote the actual string here, since a DBusError also needs to

123 \* be valid UTF-8 \*/

124 dbus_set_error (error, DBUS_ERROR_INVALID_ARGS,

125 "Interface name was not valid UTF-8");

126 return FALSE;

127 }

128

129 /\* FIXME: later, diagnose exactly how it was invalid \*/

130 dbus_set_error (error, DBUS_ERROR_INVALID_ARGS,

131 "Interface name was not valid: '%s'", name);

132 return FALSE;

133}

134

149dbus_bool_t

150dbus_validate_member (const char \*name,

151 DBusError \*error)

152{

153 DBusString str;

154 int len;

155

156 \_dbus_return_val_if_fail (name != NULL, FALSE);

157

158 \_dbus_string_init_const (&str, name);

159 len = \_dbus_string_get_length (&str);

160

161 /\* In general, it ought to be valid... \*/

162 if (\_DBUS_LIKELY (\_dbus_validate_member (&str, 0, len)))

163 return TRUE;

164

165 /\* slow path: string is invalid, find out why \*/

166

167 if (!\_dbus_string_validate_utf8 (&str, 0, len))

168 {

169 /\* don't quote the actual string here, since a DBusError also needs to

170 \* be valid UTF-8 \*/

171 dbus_set_error (error, DBUS_ERROR_INVALID_ARGS,

172 "Member name was not valid UTF-8");

173 return FALSE;

174 }

175

176 /\* FIXME: later, diagnose exactly how it was invalid \*/

177 dbus_set_error (error, DBUS_ERROR_INVALID_ARGS,

178 "Member name was not valid: '%s'", name);

179 return FALSE;

180}

181

196dbus_bool_t

197dbus_validate_error_name (const char \*name,

198 DBusError \*error)

199{

200 DBusString str;

201 int len;

202

203 \_dbus_return_val_if_fail (name != NULL, FALSE);

204

205 \_dbus_string_init_const (&str, name);

206 len = \_dbus_string_get_length (&str);

207

208 /\* In general, it ought to be valid... \*/

209 if (\_DBUS_LIKELY (\_dbus_validate_error_name (&str, 0, len)))

210 return TRUE;

211

212 /\* slow path: string is invalid, find out why \*/

213

214 if (!\_dbus_string_validate_utf8 (&str, 0, len))

215 {

216 /\* don't quote the actual string here, since a DBusError also needs to

217 \* be valid UTF-8 \*/

218 dbus_set_error (error, DBUS_ERROR_INVALID_ARGS,

219 "Error name was not valid UTF-8");

220 return FALSE;

221 }

222

223 /\* FIXME: later, diagnose exactly how it was invalid \*/

224 dbus_set_error (error, DBUS_ERROR_INVALID_ARGS,

225 "Error name was not valid: '%s'", name);

226 return FALSE;

227}

228

243dbus_bool_t

244dbus_validate_bus_name (const char \*name,

245 DBusError \*error)

246{

247 DBusString str;

248 int len;

249

250 \_dbus_return_val_if_fail (name != NULL, FALSE);

251

252 \_dbus_string_init_const (&str, name);

253 len = \_dbus_string_get_length (&str);

254

255 /\* In general, it ought to be valid... \*/

256 if (\_DBUS_LIKELY (\_dbus_validate_bus_name (&str, 0, len)))

257 return TRUE;

258

259 /\* slow path: string is invalid, find out why \*/

260

261 if (!\_dbus_string_validate_utf8 (&str, 0, len))

262 {

263 /\* don't quote the actual string here, since a DBusError also needs to

264 \* be valid UTF-8 \*/

265 dbus_set_error (error, DBUS_ERROR_INVALID_ARGS,

266 "Bus name was not valid UTF-8");

267 return FALSE;

268 }

269

270 /\* FIXME: later, diagnose exactly how it was invalid \*/

271 dbus_set_error (error, DBUS_ERROR_INVALID_ARGS,

272 "Bus name was not valid: '%s'", name);

273 return FALSE;

274}

275

290dbus_bool_t

291dbus_validate_utf8 (const char \*alleged_utf8,

292 DBusError \*error)

293{

294 DBusString str;

295

296 \_dbus_return_val_if_fail (alleged_utf8 != NULL, FALSE);

297

298 \_dbus_string_init_const (&str, alleged_utf8);

299

300 if (\_DBUS_LIKELY (\_dbus_string_validate_utf8 (&str, 0,

301 \_dbus_string_get_length (&str))))

302 return TRUE;

303

304 /\* don't quote the actual string here, since a DBusError also needs to

305 \* be valid UTF-8 \*/

306 dbus_set_error (error, DBUS_ERROR_INVALID_ARGS,

307 "String was not valid UTF-8");

308 return FALSE;

309}

310

/\* end of group \*/

dbus_set_error

void dbus_set_error(DBusError \*error, const char \*name, const char \*format,...)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:356

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

\_dbus_validate_error_name

dbus_bool_t \_dbus_validate_error_name(const DBusString \*str, int start, int len)

Checks that the given range of the string is a valid error name in the D-Bus protocol.

**Definition** dbus-marshal-validate.c:1124

\_dbus_validate_member

dbus_bool_t \_dbus_validate_member(const DBusString \*str, int start, int len)

Checks that the given range of the string is a valid member name in the D-Bus protocol.

**Definition** dbus-marshal-validate.c:1063

\_dbus_validate_path

dbus_bool_t \_dbus_validate_path(const DBusString \*str, int start, int len)

Checks that the given range of the string is a valid object path name in the D-Bus protocol.

**Definition** dbus-marshal-validate.c:849

\_dbus_validate_interface

dbus_bool_t \_dbus_validate_interface(const DBusString \*str, int start, int len)

Checks that the given range of the string is a valid interface name in the D-Bus protocol.

**Definition** dbus-marshal-validate.c:987

\_dbus_validate_bus_name

dbus_bool_t \_dbus_validate_bus_name(const DBusString \*str, int start, int len)

Checks that the given range of the string is a valid bus name in the D-Bus protocol.

**Definition** dbus-marshal-validate.c:1253

DBUS_ERROR_INVALID_ARGS

\#define DBUS_ERROR_INVALID_ARGS

Invalid arguments passed to a method call.

**Definition** dbus-protocol.h:397

\_dbus_string_init_const

void \_dbus_string_init_const(DBusString \*str, const char \*value)

Initializes a constant string.

**Definition** dbus-string.c:197

\_dbus_string_validate_utf8

dbus_bool_t \_dbus_string_validate_utf8(const DBusString \*str, int start, int len)

Checks that the given range of the string is valid UTF-8.

**Definition** dbus-string.c:2678

\_dbus_string_get_length

int \_dbus_string_get_length(const DBusString \*str)

Gets the length of a string (not including nul termination).

**Definition** dbus-string.c:784

dbus_validate_interface

dbus_bool_t dbus_validate_interface(const char \*name, DBusError \*error)

Check an interface name for validity.

**Definition** dbus-syntax.c:103

dbus_validate_path

dbus_bool_t dbus_validate_path(const char \*path, DBusError \*error)

Check an object path for validity.

**Definition** dbus-syntax.c:56

dbus_validate_utf8

dbus_bool_t dbus_validate_utf8(const char \*alleged_utf8, DBusError \*error)

Check a string for validity.

**Definition** dbus-syntax.c:291

dbus_validate_member

dbus_bool_t dbus_validate_member(const char \*name, DBusError \*error)

Check a member (method/signal) name for validity.

**Definition** dbus-syntax.c:150

dbus_validate_bus_name

dbus_bool_t dbus_validate_bus_name(const char \*name, DBusError \*error)

Check a bus name for validity.

**Definition** dbus-syntax.c:244

dbus_validate_error_name

dbus_bool_t dbus_validate_error_name(const char \*name, DBusError \*error)

Check an error name for validity.

**Definition** dbus-syntax.c:197

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusString

**Definition** dbus-string.h:47
