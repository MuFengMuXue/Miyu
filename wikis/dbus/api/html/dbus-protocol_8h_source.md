dbus-protocol.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-protocol.h D-Bus protocol constants

3 \*

4 \* Copyright (C) 2002, 2003 CodeFactory AB

5 \* Copyright (C) 2004, 2005 Red Hat, Inc.

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

27\#ifndef DBUS_PROTOCOL_H

28\#define DBUS_PROTOCOL_H

29

30/\* Don't include anything in here from anywhere else. It's

31 \* intended for use by any random library.

32 \*/

33

34\#ifdef \_\_cplusplus

35extern "C" {

36\#if 0

37} /\* avoids confusing emacs indentation \*/

38\#endif

39\#endif

40

41/\* Normally docs are in .c files, but there isn't a .c file for this. \*/

54/\* Message byte order \*/

55\#define DBUS_LITTLE_ENDIAN ('l')

56\#define DBUS_BIG_ENDIAN ('B')

59\#define DBUS_MAJOR_PROTOCOL_VERSION 1

60

62\#define DBUS_TYPE_INVALID ((int) '\0')

64\#define DBUS_TYPE_INVALID_AS_STRING "\0"

65

66/\* Primitive types \*/

68\#define DBUS_TYPE_BYTE ((int) 'y')

70\#define DBUS_TYPE_BYTE_AS_STRING "y"

72\#define DBUS_TYPE_BOOLEAN ((int) 'b')

74\#define DBUS_TYPE_BOOLEAN_AS_STRING "b"

76\#define DBUS_TYPE_INT16 ((int) 'n')

78\#define DBUS_TYPE_INT16_AS_STRING "n"

80\#define DBUS_TYPE_UINT16 ((int) 'q')

82\#define DBUS_TYPE_UINT16_AS_STRING "q"

84\#define DBUS_TYPE_INT32 ((int) 'i')

86\#define DBUS_TYPE_INT32_AS_STRING "i"

88\#define DBUS_TYPE_UINT32 ((int) 'u')

90\#define DBUS_TYPE_UINT32_AS_STRING "u"

92\#define DBUS_TYPE_INT64 ((int) 'x')

94\#define DBUS_TYPE_INT64_AS_STRING "x"

96\#define DBUS_TYPE_UINT64 ((int) 't')

98\#define DBUS_TYPE_UINT64_AS_STRING "t"

100\#define DBUS_TYPE_DOUBLE ((int) 'd')

102\#define DBUS_TYPE_DOUBLE_AS_STRING "d"

104\#define DBUS_TYPE_STRING ((int) 's')

106\#define DBUS_TYPE_STRING_AS_STRING "s"

108\#define DBUS_TYPE_OBJECT_PATH ((int) 'o')

110\#define DBUS_TYPE_OBJECT_PATH_AS_STRING "o"

112\#define DBUS_TYPE_SIGNATURE ((int) 'g')

114\#define DBUS_TYPE_SIGNATURE_AS_STRING "g"

116\#define DBUS_TYPE_UNIX_FD ((int) 'h')

118\#define DBUS_TYPE_UNIX_FD_AS_STRING "h"

119

120/\* Compound types \*/

122\#define DBUS_TYPE_ARRAY ((int) 'a')

124\#define DBUS_TYPE_ARRAY_AS_STRING "a"

126\#define DBUS_TYPE_VARIANT ((int) 'v')

128\#define DBUS_TYPE_VARIANT_AS_STRING "v"

129

138\#define DBUS_TYPE_STRUCT ((int) 'r')

140\#define DBUS_TYPE_STRUCT_AS_STRING "r"

145\#define DBUS_TYPE_DICT_ENTRY ((int) 'e')

147\#define DBUS_TYPE_DICT_ENTRY_AS_STRING "e"

148

153\#define DBUS_NUMBER_OF_TYPES (16)

154

155/\* characters other than typecodes that appear in type signatures \*/

156

158\#define DBUS_STRUCT_BEGIN_CHAR ((int) '(')

160\#define DBUS_STRUCT_BEGIN_CHAR_AS_STRING "("

162\#define DBUS_STRUCT_END_CHAR ((int) ')')

164\#define DBUS_STRUCT_END_CHAR_AS_STRING ")"

166\#define DBUS_DICT_ENTRY_BEGIN_CHAR ((int) '{')

168\#define DBUS_DICT_ENTRY_BEGIN_CHAR_AS_STRING "{"

170\#define DBUS_DICT_ENTRY_END_CHAR ((int) '}')

172\#define DBUS_DICT_ENTRY_END_CHAR_AS_STRING "}"

173

180\#define DBUS_MAXIMUM_NAME_LENGTH 255

181

183\#define DBUS_MAXIMUM_SIGNATURE_LENGTH 255

184

188\#define DBUS_MAXIMUM_MATCH_RULE_LENGTH 1024

189

193\#define DBUS_MAXIMUM_MATCH_RULE_ARG_NUMBER 63

194

205\#define DBUS_MAXIMUM_ARRAY_LENGTH (67108864)

207\#define DBUS_MAXIMUM_ARRAY_LENGTH_BITS 26

208

212\#define DBUS_MAXIMUM_MESSAGE_LENGTH (DBUS_MAXIMUM_ARRAY_LENGTH \* 2)

214\#define DBUS_MAXIMUM_MESSAGE_LENGTH_BITS 27

215

220\#define DBUS_MAXIMUM_MESSAGE_UNIX_FDS (DBUS_MAXIMUM_MESSAGE_LENGTH/4)

222\#define DBUS_MAXIMUM_MESSAGE_UNIX_FDS_BITS (DBUS_MAXIMUM_MESSAGE_LENGTH_BITS-2)

223

229\#define DBUS_MAXIMUM_TYPE_RECURSION_DEPTH 32

230

231/\* Types of message \*/

232

234\#define DBUS_MESSAGE_TYPE_INVALID 0

236\#define DBUS_MESSAGE_TYPE_METHOD_CALL 1

238\#define DBUS_MESSAGE_TYPE_METHOD_RETURN 2

240\#define DBUS_MESSAGE_TYPE_ERROR 3

242\#define DBUS_MESSAGE_TYPE_SIGNAL 4

243

244\#define DBUS_NUM_MESSAGE_TYPES 5

245

246/\* Header flags \*/

247

251\#define DBUS_HEADER_FLAG_NO_REPLY_EXPECTED 0x1

258\#define DBUS_HEADER_FLAG_NO_AUTO_START 0x2

263\#define DBUS_HEADER_FLAG_ALLOW_INTERACTIVE_AUTHORIZATION 0x4

264

265/\* Header fields \*/

266

268\#define DBUS_HEADER_FIELD_INVALID 0

272\#define DBUS_HEADER_FIELD_PATH 1

276\#define DBUS_HEADER_FIELD_INTERFACE 2

278\#define DBUS_HEADER_FIELD_MEMBER 3

282\#define DBUS_HEADER_FIELD_ERROR_NAME 4

286\#define DBUS_HEADER_FIELD_REPLY_SERIAL 5

290\#define DBUS_HEADER_FIELD_DESTINATION 6

295\#define DBUS_HEADER_FIELD_SENDER 7

299\#define DBUS_HEADER_FIELD_SIGNATURE 8

304\#define DBUS_HEADER_FIELD_UNIX_FDS 9

308\#define DBUS_HEADER_FIELD_CONTAINER_INSTANCE 10

309

310

317\#define DBUS_HEADER_FIELD_LAST DBUS_HEADER_FIELD_CONTAINER_INSTANCE

318

332\#define DBUS_HEADER_SIGNATURE \\

333 DBUS_TYPE_BYTE_AS_STRING \\

334 DBUS_TYPE_BYTE_AS_STRING \\

335 DBUS_TYPE_BYTE_AS_STRING \\

336 DBUS_TYPE_BYTE_AS_STRING \\

337 DBUS_TYPE_UINT32_AS_STRING \\

338 DBUS_TYPE_UINT32_AS_STRING \\

339 DBUS_TYPE_ARRAY_AS_STRING \\

340 DBUS_STRUCT_BEGIN_CHAR_AS_STRING \\

341 DBUS_TYPE_BYTE_AS_STRING \\

342 DBUS_TYPE_VARIANT_AS_STRING \\

343 DBUS_STRUCT_END_CHAR_AS_STRING

344

345

352\#define DBUS_MINIMUM_HEADER_SIZE 16

353

354/\* Errors \*/

355/\* WARNING these get autoconverted to an enum in dbus-glib.h. Thus,

356 \* if you change the order it breaks the ABI. Keep them in order.

357 \* Also, don't change the formatting since that will break the sed

358 \* script.

359 \*/

361\#define DBUS_ERROR_FAILED "org.freedesktop.DBus.Error.Failed"

363\#define DBUS_ERROR_NO_MEMORY "org.freedesktop.DBus.Error.NoMemory"

365\#define DBUS_ERROR_SERVICE_UNKNOWN "org.freedesktop.DBus.Error.ServiceUnknown"

367\#define DBUS_ERROR_NAME_HAS_NO_OWNER "org.freedesktop.DBus.Error.NameHasNoOwner"

369\#define DBUS_ERROR_NO_REPLY "org.freedesktop.DBus.Error.NoReply"

371\#define DBUS_ERROR_IO_ERROR "org.freedesktop.DBus.Error.IOError"

373\#define DBUS_ERROR_BAD_ADDRESS "org.freedesktop.DBus.Error.BadAddress"

375\#define DBUS_ERROR_NOT_SUPPORTED "org.freedesktop.DBus.Error.NotSupported"

377\#define DBUS_ERROR_LIMITS_EXCEEDED "org.freedesktop.DBus.Error.LimitsExceeded"

379\#define DBUS_ERROR_ACCESS_DENIED "org.freedesktop.DBus.Error.AccessDenied"

381\#define DBUS_ERROR_AUTH_FAILED "org.freedesktop.DBus.Error.AuthFailed"

383\#define DBUS_ERROR_NO_SERVER "org.freedesktop.DBus.Error.NoServer"

389\#define DBUS_ERROR_TIMEOUT "org.freedesktop.DBus.Error.Timeout"

391\#define DBUS_ERROR_NO_NETWORK "org.freedesktop.DBus.Error.NoNetwork"

393\#define DBUS_ERROR_ADDRESS_IN_USE "org.freedesktop.DBus.Error.AddressInUse"

395\#define DBUS_ERROR_DISCONNECTED "org.freedesktop.DBus.Error.Disconnected"

397\#define DBUS_ERROR_INVALID_ARGS "org.freedesktop.DBus.Error.InvalidArgs"

399\#define DBUS_ERROR_FILE_NOT_FOUND "org.freedesktop.DBus.Error.FileNotFound"

401\#define DBUS_ERROR_FILE_EXISTS "org.freedesktop.DBus.Error.FileExists"

403\#define DBUS_ERROR_UNKNOWN_METHOD "org.freedesktop.DBus.Error.UnknownMethod"

405\#define DBUS_ERROR_UNKNOWN_OBJECT "org.freedesktop.DBus.Error.UnknownObject"

407\#define DBUS_ERROR_UNKNOWN_INTERFACE "org.freedesktop.DBus.Error.UnknownInterface"

409\#define DBUS_ERROR_UNKNOWN_PROPERTY "org.freedesktop.DBus.Error.UnknownProperty"

411\#define DBUS_ERROR_PROPERTY_READ_ONLY "org.freedesktop.DBus.Error.PropertyReadOnly"

416\#define DBUS_ERROR_TIMED_OUT "org.freedesktop.DBus.Error.TimedOut"

418\#define DBUS_ERROR_MATCH_RULE_NOT_FOUND "org.freedesktop.DBus.Error.MatchRuleNotFound"

420\#define DBUS_ERROR_MATCH_RULE_INVALID "org.freedesktop.DBus.Error.MatchRuleInvalid"

422\#define DBUS_ERROR_SPAWN_EXEC_FAILED "org.freedesktop.DBus.Error.Spawn.ExecFailed"

424\#define DBUS_ERROR_SPAWN_FORK_FAILED "org.freedesktop.DBus.Error.Spawn.ForkFailed"

426\#define DBUS_ERROR_SPAWN_CHILD_EXITED "org.freedesktop.DBus.Error.Spawn.ChildExited"

428\#define DBUS_ERROR_SPAWN_CHILD_SIGNALED "org.freedesktop.DBus.Error.Spawn.ChildSignaled"

430\#define DBUS_ERROR_SPAWN_FAILED "org.freedesktop.DBus.Error.Spawn.Failed"

432\#define DBUS_ERROR_SPAWN_SETUP_FAILED "org.freedesktop.DBus.Error.Spawn.FailedToSetup"

434\#define DBUS_ERROR_SPAWN_CONFIG_INVALID "org.freedesktop.DBus.Error.Spawn.ConfigInvalid"

436\#define DBUS_ERROR_SPAWN_SERVICE_INVALID "org.freedesktop.DBus.Error.Spawn.ServiceNotValid"

438\#define DBUS_ERROR_SPAWN_SERVICE_NOT_FOUND "org.freedesktop.DBus.Error.Spawn.ServiceNotFound"

440\#define DBUS_ERROR_SPAWN_PERMISSIONS_INVALID "org.freedesktop.DBus.Error.Spawn.PermissionsInvalid"

442\#define DBUS_ERROR_SPAWN_FILE_INVALID "org.freedesktop.DBus.Error.Spawn.FileInvalid"

444\#define DBUS_ERROR_SPAWN_NO_MEMORY "org.freedesktop.DBus.Error.Spawn.NoMemory"

446\#define DBUS_ERROR_UNIX_PROCESS_ID_UNKNOWN "org.freedesktop.DBus.Error.UnixProcessIdUnknown"

448\#define DBUS_ERROR_INVALID_SIGNATURE "org.freedesktop.DBus.Error.InvalidSignature"

450\#define DBUS_ERROR_INVALID_FILE_CONTENT "org.freedesktop.DBus.Error.InvalidFileContent"

452\#define DBUS_ERROR_SELINUX_SECURITY_CONTEXT_UNKNOWN "org.freedesktop.DBus.Error.SELinuxSecurityContextUnknown"

454\#define DBUS_ERROR_ADT_AUDIT_DATA_UNKNOWN "org.freedesktop.DBus.Error.AdtAuditDataUnknown"

456\#define DBUS_ERROR_OBJECT_PATH_IN_USE "org.freedesktop.DBus.Error.ObjectPathInUse"

459\#define DBUS_ERROR_INCONSISTENT_MESSAGE "org.freedesktop.DBus.Error.InconsistentMessage"

463\#define DBUS_ERROR_INTERACTIVE_AUTHORIZATION_REQUIRED "org.freedesktop.DBus.Error.InteractiveAuthorizationRequired"

466\#define DBUS_ERROR_NOT_CONTAINER "org.freedesktop.DBus.Error.NotContainer"

467

468/\* XML introspection format \*/

469

471\#define DBUS_INTROSPECT_1_0_XML_NAMESPACE "http://www.freedesktop.org/standards/dbus"

473\#define DBUS_INTROSPECT_1_0_XML_PUBLIC_IDENTIFIER "-//freedesktop//DTD D-BUS Object Introspection 1.0//EN"

475\#define DBUS_INTROSPECT_1_0_XML_SYSTEM_IDENTIFIER "http://www.freedesktop.org/standards/dbus/1.0/introspect.dtd"

477\#define DBUS_INTROSPECT_1_0_XML_DOCTYPE_DECL_NODE "\<!DOCTYPE node PUBLIC \\" DBUS_INTROSPECT_1_0_XML_PUBLIC_IDENTIFIER "\\\n\\" DBUS_INTROSPECT_1_0_XML_SYSTEM_IDENTIFIER "\\\>\n"

478

481\#ifdef \_\_cplusplus

482\#if 0

483{ /\* avoids confusing emacs indentation \*/

484\#endif

485}

486\#endif

487

488\#endif /\* DBUS_PROTOCOL_H \*/
