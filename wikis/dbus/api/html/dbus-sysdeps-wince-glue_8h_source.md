dbus-sysdeps-wince-glue.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-sysdeps-wince-glue.h Emulation of system/libc features for Windows CE (internal to D-Bus implementation)

3 \*

4 \* Copyright (C) 2002, 2003 Red Hat, Inc.

5 \* Copyright (C) 2003 CodeFactory AB

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

27\#ifndef DBUS_SYSDEPS_WINCE_GLUE_H

28\#define DBUS_SYSDEPS_WINCE_GLUE_H

29

30\#include \<time.h\>

31\#include \<stdarg.h\>

32

33/\* For getaddrinfo, configure/cmake defined \_WIN32_WCE to something \>= 0x0401. \*/

34\#include \<windows.h\>

35\#undef interface

36

37DBUS_BEGIN_DECLS

38

39/\* shlobj.h declares these only for \_WIN32_IE that we don't want to define.

40 In any case, with mingw32ce we only get a SHGetSpecialFolderPath. \*/

41\#define SHGetSpecialFolderPathW SHGetSpecialFolderPath

42BOOL WINAPI SHGetSpecialFolderPathA(HWND,LPSTR,int,BOOL);

43BOOL WINAPI SHGetSpecialFolderPathW(HWND,LPWSTR,int,BOOL);

44

45\#ifndef TLS_OUT_OF_INDEXES

46\#define TLS_OUT_OF_INDEXES 0xffffffff

47\#endif

48

49

50/\* Seriously. Windows CE does not have errno. Don't you hate it when

51 that happens? \*/

52\#define errno ((int)GetLastError ())

53

54\#define ENOENT ERROR_FILE_NOT_FOUND

55\#define EMFILE ERROR_TOO_MANY_OPEN_FILES

56\#define EACCES ERROR_ACCESS_DENIED

57\#define EBADF ERROR_INVALID_HANDLE

58\#define ENOMEM ERROR_NOT_ENOUGH_MEMORY

59\#define EXDEV ERROR_NOT_SAME_DEVICE

60\#define ENFILE ERROR_NO_MORE_FILES

61\#define EROFS ERROR_WRITE_PROTECT

62\#define ENOLCK ERROR_SHARING_BUFFER_EXCEEDED

63\#define ENOSYS ERROR_NOT_SUPPORTED

64\#define EEXIST ERROR_FILE_EXISTS

65\#define EPERM ERROR_CANNOT_MAKE

66\#define EINVAL ERROR_INVALID_PARAMETER

67\#define EINTR ERROR_INVALID_AT_INTERRUPT_TIME

68\#define EPIPE ERROR_BROKEN_PIPE

69\#define ENOSPC ERROR_DISK_FULL

70\#define ENOTEMPTY ERROR_DIR_NOT_EMPTY

71\#define EBUSY ERROR_BUSY

72\#define ENAMETOOLONG ERROR_FILENAME_EXCED_RANGE

73\#define EAGAIN ERROR_MORE_DATA

74\#define ENOTDIR ERROR_DIRECTORY

75\#define ERANGE ERROR_ARITHMETIC_OVERFLOW

76\#define ENXIO ERROR_FILE_INVALID

77\#define EFAULT ERROR_PROCESS_ABORTED

78\#define EIO ERROR_IO_DEVICE

79\#define EDEADLOCK ERROR_POSSIBLE_DEADLOCK

80\#define ENODEV ERROR_BAD_DEVICE

81

82/\* Windows CE is missing more stuff that is pretty standard. \*/

83

84\#define strdup \_strdup

85\#define stricmp \_stricmp

86\#define strnicmp \_strnicmp

87

88\#define environ \_dbus_wince_environ

89extern char \*environ\[\];

90

91\#define getenv \_dbus_wince_getenv

92char \*getenv (const char \*name);

93

94\#define putenv \_dbus_wince_putenv

95int putenv (char \*str);

96

97\#define clock \_dbus_wince_clock

98clock_t clock (void);

99

100\#define abort \_dbus_wince_abort

101void abort (void);

102

103\#define \_S_IFMT 0170000 /\* file type mask \*/

104\#define \_S_IFDIR 0040000 /\* directory \*/

105\#define \_S_IFCHR 0020000 /\* character special \*/

106\#define \_S_IFIFO 0010000 /\* pipe \*/

107\#define \_S_IFREG 0100000 /\* regular \*/

108\#define \_S_IREAD 0000400 /\* read permission, owner \*/

109\#define \_S_IWRITE 0000200 /\* write permission, owner \*/

110\#define \_S_IEXEC 0000100 /\* execute/search permission, owner \*/

111

112\#ifndef \_\_OFF_T_DEFINED

113typedef long off_t;

114\#define \_\_OFF_T_DEFINED

115\#endif

116\#ifndef \_INTPTR_T_DEFINED

117typedef int intptr_t;

118\#define \_INTPTR_T_DEFINED

119\#endif

120\#ifndef \_UINTPTR_T_DEFINED

121typedef unsigned int uintptr_t;

122\#define \_UINTPTR_T_DEFINED

123\#endif

124

125\#ifndef \_MAX_FNAME

126\#define \_MAX_FNAME 256

127\#endif

128

129\#ifndef \_IOFBF

130\#define \_IOFBF 0

131\#endif

132\#ifndef \_IOLBF

133\#define \_IOLBF 1

134\#endif

135\#ifndef \_IONBF

136\#define \_IONBF 2

137\#endif

138

139

140/\* Windows CE is missing some Windows functions that we want. \*/

141

142\#define GetSystemTimeAsFileTime \_dbus_wince_GetSystemTimeAsFileTime

143void GetSystemTimeAsFileTime (LPFILETIME ftp);

144

145\#define \_mbsrchr \_dbus_wince_mbsrchr

146unsigned char\* \_mbsrchr (const unsigned char\*, unsigned int);

147

148\#define OpenFileMappingA \_dbus_wince_OpenFileMappingA

149HANDLE OpenFileMappingA(DWORD,BOOL,LPCSTR);

150

151\#define MoveFileExA \_dbus_wince_MoveFileExA

152BOOL MoveFileExA(LPCSTR,LPCSTR,DWORD);

153\#ifndef MOVEFILE_REPLACE_EXISTING

154\#define MOVEFILE_REPLACE_EXISTING 0x00000001

155\#endif

156

157\#define SetHandleInformation \_dbus_wince_SetHandleInformation

158BOOL SetHandleInformation(HANDLE,DWORD,DWORD);

159\#ifndef HANDLE_FLAG_INHERIT

160\#define HANDLE_FLAG_INHERIT 0x01

161\#endif

162\#ifndef HANDLE_FLAG_PROTECT

163\#define HANDLE_FLAG_PROTECT_FROM_CLOSE 0x02

164\#endif

165

166\#define SearchPathA \_dbus_wince_SearchPathA

167DWORD SearchPathA(LPCSTR,LPCSTR,LPCSTR,DWORD,LPSTR,LPSTR\*);

168

169/\* Instead of emulating all functions needed for this, we replace the

170 whole thing. \*/

171dbus_bool_t \_dbus_getsid(char \*\*sid);

172

173

174\#define LookupAccountNameW \_dbus_wince_LookupAccountNameW

175BOOL LookupAccountNameW(LPCWSTR,LPCWSTR,PSID,PDWORD,LPWSTR,PDWORD,PSID_NAME_USE);

176

177\#define IsValidSid \_dbus_wince_IsValidSid

178BOOL IsValidSid(PSID);

179

180

181/\* Windows CE does only have the UNICODE interfaces (FooW), but we

182 want to use the ASCII interfaces (FooA). We implement them

183 here. \*/

184

185\#define CreateFileA \_dbus_wince_CreateFileA

186HANDLE CreateFileA(LPCSTR,DWORD,DWORD,LPSECURITY_ATTRIBUTES,DWORD,DWORD,HANDLE);

187

188\#define DeleteFileA \_dbus_wince_DeleteFileA

189BOOL DeleteFileA(LPCSTR);

190

191\#define GetFileAttributesA \_dbus_wince_GetFileAttributesA

192DWORD GetFileAttributesA(LPCSTR);

193

194\#define GetFileAttributesExA \_dbus_wince_GetFileAttributesExA

195BOOL GetFileAttributesExA(LPCSTR,GET_FILEEX_INFO_LEVELS,PVOID);

196

197\#define CreateFileMappingA \_dbus_wince_CreateFileMappingA

198HANDLE CreateFileMappingA(HANDLE,LPSECURITY_ATTRIBUTES,DWORD,DWORD,DWORD,LPCSTR);

199

200\#define CreateDirectoryA \_dbus_wince_CreateDirectoryA

201BOOL CreateDirectoryA(LPCSTR,LPSECURITY_ATTRIBUTES);

202

203\#define RemoveDirectoryA \_dbus_wince_RemoveDirectoryA

204BOOL RemoveDirectoryA(LPCSTR);

205

206\#define FindFirstFileA \_dbus_wince_FindFirstFileA

207HANDLE FindFirstFileA(LPCSTR,LPWIN32_FIND_DATAA);

208

209\#define FindNextFileA \_dbus_wince_FindNextFileA

210BOOL FindNextFileA(HANDLE,LPWIN32_FIND_DATAA);

211

212\#define CreateMutexA \_dbus_wince_CreateMutexA

213HANDLE CreateMutexA(LPSECURITY_ATTRIBUTES,BOOL,LPCSTR);

214

215\#define CreateProcessA \_dbus_wince_CreateProcessA

216BOOL CreateProcessA(LPCSTR,LPSTR,LPSECURITY_ATTRIBUTES,LPSECURITY_ATTRIBUTES,BOOL,DWORD,PVOID,LPCSTR,LPSTARTUPINFOA,LPPROCESS_INFORMATION);

217\#ifndef CREATE_NO_WINDOW

218\#define CREATE_NO_WINDOW 0x08000000

219\#endif

220

221

222\#define RegOpenKeyExA \_dbus_wince_RegOpenKeyExA

223LONG RegOpenKeyExA(HKEY,LPCSTR,DWORD,REGSAM,PHKEY);

224

225\#define RegQueryValueExA \_dbus_wince_RegQueryValueExA

226LONG WINAPI RegQueryValueExA(HKEY,LPCSTR,LPDWORD,LPDWORD,LPBYTE,LPDWORD);

227

228

229\#define FormatMessageA \_dbus_wince_FormatMessageA

230DWORD FormatMessageA(DWORD,PCVOID,DWORD,DWORD,LPSTR,DWORD,va_list\*);

231

232\#define GetModuleFileNameA \_dbus_wince_GetModuleFileNameA

233DWORD GetModuleFileNameA(HINSTANCE,LPSTR,DWORD);

234

235\#define GetTempPathA \_dbus_wince_GetTempPathA

236DWORD GetTempPathA(DWORD,LPSTR);

237

238\#define SHGetSpecialFolderPathA \_dbus_wince_SHGetSpecialFolderPathA

239BOOL SHGetSpecialFolderPathA(HWND,LPSTR,int,BOOL);

240

241

242\#define OutputDebugStringA \_dbus_wince_OutputDebugStringA

243void OutputDebugStringA(LPCSTR);

244

245

246DBUS_END_DECLS

247

248\#endif /\* DBUS_SYSDEPS_WINCE_GLUE_H \*/

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37
