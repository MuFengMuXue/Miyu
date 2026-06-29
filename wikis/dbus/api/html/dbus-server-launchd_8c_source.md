dbus-server-launchd.c

1/\* dbus-server-launchd.c Server methods for interacting with launchd.

2 \* Copyright (C) 2007, Tanner Lovelace \<lovelace@wayfarer.org\>

3 \* Copyright (C) 2008, Colin Walters \<walters@verbum.org\>

4 \* Copyright (C) 2008-2009, Benjamin Reed \<rangerrick@befunk.com\>

5 \* Copyright (C) 2009, Jonas Bähr \<jonas.baehr@web.de\>

6 \* SPDX-License-Identifier: MIT

7 \*

8 \* Permission is hereby granted, free of charge, to any person

9 \* obtaining a copy of this software and associated documentation

10 \* files (the "Software"), to deal in the Software without

11 \* restriction, including without limitation the rights to use, copy,

12 \* modify, merge, publish, distribute, sublicense, and/or sell copies

13 \* of the Software, and to permit persons to whom the Software is

14 \* furnished to do so, subject to the following conditions:

15 \*

16 \* The above copyright notice and this permission notice shall be

17 \* included in all copies or substantial portions of the Software.

18 \*

19 \* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,

20 \* EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF

21 \* MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND

22 \* NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT

23 \* HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,

24 \* WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,

25 \* OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER

26 \* DEALINGS IN THE SOFTWARE.

27 \*/

28

29\#include \<config.h\>

30\#include "dbus-server-launchd.h"

31

40\#ifdef DBUS_ENABLE_LAUNCHD

41\#include \<launch.h\>

42\#include \<errno.h\>

43\#include \<unistd.h\>

44

45\#include "dbus-misc.h"

46\#include "dbus-server-socket.h"

47\#include "dbus-sysdeps-unix.h"

48

49/\* put other private launchd functions here \*/

50

51\#endif /\* DBUS_ENABLE_LAUNCHD \*/

52

67DBusServer \*

68\_dbus_server_new_for_launchd (const char \*launchd_env_var, DBusError \* error)

69 {

70\#ifdef DBUS_ENABLE_LAUNCHD

71 DBusServer \*server;

72 DBusString address;

73 int launchd_fd = -1;

74 launch_data_t sockets_dict, checkin_response;

75 launch_data_t checkin_request;

76 launch_data_t listening_fd_array, listening_fd;

77 launch_data_t environment_dict, environment_param;

78 const char \*launchd_socket_path, \*display;

79

80 launchd_socket_path = \_dbus_getenv (launchd_env_var);

81 display = \_dbus_getenv ("DISPLAY");

82

83 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

84

85 if (launchd_socket_path == NULL \|\| \*launchd_socket_path == '\0')

86 {

87 dbus_set_error (error, DBUS_ERROR_BAD_ADDRESS,

88 "launchd's environment variable %s is empty, but should contain a socket path.\n", launchd_env_var);

89 return NULL;

90 }

91

92 if (!\_dbus_string_init (&address))

93 {

94 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

95 return NULL;

96 }

97 if (!\_dbus_string_append (&address, "unix:path="))

98 {

99 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

100 goto l_failed_0;

101 }

102 if (!\_dbus_string_append (&address, launchd_socket_path))

103 {

104 dbus_set_error (error, DBUS_ERROR_NO_MEMORY, NULL);

105 goto l_failed_0;

106 }

107

108 if ((checkin_request = launch_data_new_string (LAUNCH_KEY_CHECKIN)) == NULL)

109 {

110 dbus_set_error (error, DBUS_ERROR_NO_MEMORY,

111 "launch_data_new_string(\\%s\\) Unable to create string.\n",

112 LAUNCH_KEY_CHECKIN);

113 goto l_failed_0;

114 }

115

116 if ((checkin_response = launch_msg (checkin_request)) == NULL)

117 {

118 dbus_set_error (error, DBUS_ERROR_IO_ERROR,

119 "launch_msg(\\%s\\) IPC failure: %s\n",

120 LAUNCH_KEY_CHECKIN, strerror (errno));

121 goto l_failed_0;

122 }

123

124 if (LAUNCH_DATA_ERRNO == launch_data_get_type (checkin_response))

125 {

126 dbus_set_error (error, DBUS_ERROR_FAILED, "Check-in failed: %s\n",

127 strerror (launch_data_get_errno (checkin_response)));

128 goto l_failed_0;

129 }

130

131 sockets_dict =

132 launch_data_dict_lookup (checkin_response, LAUNCH_JOBKEY_SOCKETS);

133 if (NULL == sockets_dict)

134 {

135 dbus_set_error (error, DBUS_ERROR_IO_ERROR,

136 "No sockets found to answer requests on!\n");

137 goto l_failed_0;

138 }

139

140 listening_fd_array =

141 launch_data_dict_lookup (sockets_dict, "unix_domain_listener");

142 if (NULL == listening_fd_array)

143 {

144 dbus_set_error (error, DBUS_ERROR_IO_ERROR,

145 "No known sockets found to answer requests on!\n");

146 goto l_failed_0;

147 }

148

149 if (launch_data_array_get_count (listening_fd_array) != 1)

150 {

151 dbus_set_error (error, DBUS_ERROR_LIMITS_EXCEEDED,

152 "Expected 1 socket from launchd, got %d.\n",

153 launch_data_array_get_count (listening_fd_array));

154 goto l_failed_0;

155 }

156

157 listening_fd = launch_data_array_get_index (listening_fd_array, 0);

158 launchd_fd = launch_data_get_fd (listening_fd);

159

160 \_dbus_fd_set_close_on_exec (launchd_fd);

161

162 if (launchd_fd \< 0)

163 {

164 \_DBUS_ASSERT_ERROR_IS_SET (error);

165 goto l_failed_0;

166 if (display == NULL \|\| \*display == '\0')

167 {

168 environment_dict = launch_data_dict_lookup (checkin_response, LAUNCH_JOBKEY_USERENVIRONMENTVARIABLES);

169 if (NULL == environment_dict)

170 {

171 \_dbus_warn ("Unable to retrieve user environment from launchd.");

172 }

173 else

174 {

175 environment_param = launch_data_dict_lookup (environment_dict, "DISPLAY");

176 if (NULL == environment_param)

177 {

178 \_dbus_warn ("Unable to retrieve DISPLAY from launchd.");

179 }

180 else

181 {

182 display = launch_data_get_string(environment_param);

183 dbus_setenv ("DISPLAY", display);

184 }

185 }

186 }

187

188 }

189

190 server = \_dbus_server_new_for_socket (&launchd_fd, 1, &address, 0, error);

191 if (server == NULL)

192 {

193 goto l_failed_0;

194 }

195

196 \_dbus_string_free (&address);

197

198 return server;

199

200 l_failed_0:

201 if (launchd_fd \>= 0)

202 close (launchd_fd);

203

204 \_dbus_string_free (&address);

205

206 return NULL;

207\#else /\* DBUS_ENABLE_LAUNCHD \*/

208 dbus_set_error (error, DBUS_ERROR_BAD_ADDRESS,

209 "address type 'launchd' requested, but launchd support not compiled in");

210 return NULL;

211\#endif

212 }

213

dbus_set_error

void dbus_set_error(DBusError \*error, const char \*name, const char \*format,...)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:356

\_dbus_warn

void \_dbus_warn(const char \*format,...)

Prints a warning message to stderr.

**Definition** dbus-internals.c:278

NULL

\#define NULL

A null pointer, defined appropriately for C or C++.

**Definition** dbus-macros.h:51

dbus_setenv

DBUS_EXPORT dbus_bool_t dbus_setenv(const char \*variable, const char \*value)

Wrapper for setenv().

**Definition** dbus-sysdeps.c:126

DBUS_ERROR_BAD_ADDRESS

\#define DBUS_ERROR_BAD_ADDRESS

A D-Bus bus address was malformed.

**Definition** dbus-protocol.h:373

DBUS_ERROR_IO_ERROR

\#define DBUS_ERROR_IO_ERROR

Something went wrong reading or writing to a socket, for example.

**Definition** dbus-protocol.h:371

DBUS_ERROR_LIMITS_EXCEEDED

\#define DBUS_ERROR_LIMITS_EXCEEDED

Some limited resource is exhausted.

**Definition** dbus-protocol.h:377

DBUS_ERROR_FAILED

\#define DBUS_ERROR_FAILED

A generic error; "something went wrong" - see the error message for more.

**Definition** dbus-protocol.h:361

DBUS_ERROR_NO_MEMORY

\#define DBUS_ERROR_NO_MEMORY

There was not enough memory to complete an operation.

**Definition** dbus-protocol.h:363

\_dbus_server_new_for_launchd

DBusServer \* \_dbus_server_new_for_launchd(const char \*launchd_env_var, DBusError \*error)

Creates a new server from launchd.

**Definition** dbus-server-launchd.c:68

\_dbus_server_new_for_socket

DBusServer \* \_dbus_server_new_for_socket(DBusSocket \*fds, int n_fds, const DBusString \*address, DBusNonceFile \*noncefile, DBusError \*error)

Creates a new server listening on the given file descriptor.

**Definition** dbus-server-socket.c:288

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

\_dbus_fd_set_close_on_exec

void \_dbus_fd_set_close_on_exec(int fd)

Sets the file descriptor to be close on exec.

**Definition** dbus-sysdeps-unix.c:3683

\_dbus_getenv

const char \* \_dbus_getenv(const char \*varname)

Wrapper for getenv().

**Definition** dbus-sysdeps.c:197

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusServer

Internals of DBusServer object.

**Definition** dbus-server-protected.h:59

DBusString

**Definition** dbus-string.h:47
