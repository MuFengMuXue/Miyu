dbus-backtrace-win.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-backtrace-win.c Backtrace Generator

3 \*

4 \* Copyright 2004 Eric Poech

5 \* Copyright 2004 Robert Shearman

6 \* Copyright 2010 Patrick von Reth \<patrick.vonreth@gmail.com\>

7 \* Copyright 2015 Ralf Habacker \<ralf.habacker@freenet.de\>

8 \*

9 \* SPDX-License-Identifier: LGPL-2.1-or-later

10 \*

11 \* This library is free software; you can redistribute it and/or

12 \* modify it under the terms of the GNU Lesser General Public

13 \* License as published by the Free Software Foundation; either

14 \* version 2.1 of the License, or (at your option) any later version.

15 \*

16 \* This library is distributed in the hope that it will be useful,

17 \* but WITHOUT ANY WARRANTY; without even the implied warranty of

18 \* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU

19 \* Lesser General Public License for more details.

20 \*

21 \* You should have received a copy of the GNU Lesser General Public

22 \* License along with this library; if not, write to the Free Software

23 \* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

24 \*/

25

26\#include \<config.h\>

27

28\#include "dbus-internals.h"

29\#include "dbus-sysdeps.h"

30

31\#if !defined (DBUS_DISABLE_ASSERT) \|\| defined(DBUS_ENABLE_EMBEDDED_TESTS)

32

33\#if defined(\_MSC_VER) \|\| defined(DBUS_WINCE)

34\# ifdef BACKTRACES

35\# undef BACKTRACES

36\# endif

37\#else

38\# define BACKTRACES

39\#endif

40

41\#ifdef BACKTRACES

42\#include "dbus-sysdeps-win.h"

43

44\#include \<stdio.h\>

45\#include \<windows.h\>

46\#include \<imagehlp.h\>

47

48\#define DPRINTF(fmt, ...) fprintf (stderr, fmt, \##\_\_VA_ARGS\_\_)

49

50\#ifdef \_MSC_VER

51\#define BOOL int

52

53\#define \_\_i386\_\_

54\#endif

55

56static void dump_backtrace_for_thread (HANDLE hThread)

57{

58 ADDRESS old_address;

59 STACKFRAME sf;

60 CONTEXT context;

61 DWORD dwImageType;

62 int i = 0;

63

64 SymSetOptions (SYMOPT_UNDNAME \| SYMOPT_LOAD_LINES);

65 SymInitialize (GetCurrentProcess (), NULL, TRUE);

66

67

68 /\* can't use this function for current thread as GetThreadContext

69 \* doesn't support getting context from current thread \*/

70 if (hThread == GetCurrentThread())

71 return;

72

73 DPRINTF ("Backtrace:\n");

74

75 \_DBUS_ZERO (old_address);

76 \_DBUS_ZERO (context);

77 context.ContextFlags = CONTEXT_FULL;

78

79 SuspendThread (hThread);

80

81 if (!GetThreadContext (hThread, &context))

82 {

83 DPRINTF ("Couldn't get thread context (error %ld)\n", GetLastError ());

84 ResumeThread (hThread);

85 return;

86 }

87

88 \_DBUS_ZERO (sf);

89

90\#ifdef \_\_i386\_\_

91 dwImageType = IMAGE_FILE_MACHINE_I386;

92 sf.AddrFrame.Offset = context.Ebp;

93 sf.AddrFrame.Mode = AddrModeFlat;

94 sf.AddrPC.Offset = context.Eip;

95 sf.AddrPC.Mode = AddrModeFlat;

96\#elif defined(\_M_X64)

97 dwImageType = IMAGE_FILE_MACHINE_AMD64;

98 sf.AddrPC.Offset = context.Rip;

99 sf.AddrPC.Mode = AddrModeFlat;

100 sf.AddrFrame.Offset = context.Rsp;

101 sf.AddrFrame.Mode = AddrModeFlat;

102 sf.AddrStack.Offset = context.Rsp;

103 sf.AddrStack.Mode = AddrModeFlat;

104\#elif defined(\_M_IA64)

105 dwImageType = IMAGE_FILE_MACHINE_IA64;

106 sf.AddrPC.Offset = context.StIIP;

107 sf.AddrPC.Mode = AddrModeFlat;

108 sf.AddrFrame.Offset = context.IntSp;

109 sf.AddrFrame.Mode = AddrModeFlat;

110 sf.AddrBStore.Offset= context.RsBSP;

111 sf.AddrBStore.Mode = AddrModeFlat;

112 sf.AddrStack.Offset = context.IntSp;

113 sf.AddrStack.Mode = AddrModeFlat;

114\#else

115\# error You need to fill in the STACKFRAME structure for your architecture

116\#endif

117

118 /\*

119 backtrace format

120 \<level\> \<address\> \<symbol\>\[+offset\] \[ '\[' \<file\> ':' \<line\> '\]' \] \[ 'in' \<module\> \]

121 example:

122 6 0xf75ade6b wine_switch_to_stack+0x2a \[/usr/src/debug/wine-snapshot/libs/wine/port.c:59\] in libwine.so.1

123 \*/

124 while (StackWalk (dwImageType, GetCurrentProcess (),

125 hThread, &sf, &context, NULL, SymFunctionTableAccess,

126 SymGetModuleBase, NULL))

127 {

128 char buffer\[sizeof(SYMBOL_INFO) + MAX_SYM_NAME \* sizeof(char)\];

129 PSYMBOL_INFO pSymbol = (PSYMBOL_INFO)buffer;

130 DWORD64 displacement;

131 IMAGEHLP_LINE line;

132 DWORD dwDisplacement;

133 IMAGEHLP_MODULE moduleInfo;

134

135 /\*

136 on Wine64 version 1.7.54, we get an infinite number of stack entries

137 pointing to the same stack frame (\_start+0x29 in \<wine-loader\>)

138 see bug https://bugs.winehq.org/show_bug.cgi?id=39606

139 \*/

140\#ifndef \_\_i386\_\_

141 if (old_address.Offset == sf.AddrPC.Offset)

142 {

143 break;

144 }

145\#endif

146

147 pSymbol-\>SizeOfStruct = sizeof(SYMBOL_INFO);

148 pSymbol-\>MaxNameLen = MAX_SYM_NAME;

149

150 if (SymFromAddr (GetCurrentProcess (), sf.AddrPC.Offset, &displacement, pSymbol))

151 {

152 if (displacement)

153 DPRINTF ("%3d %s+0x%I64x", i++, pSymbol-\>Name, displacement);

154 else

155 DPRINTF ("%3d %s", i++, pSymbol-\>Name);

156 }

157 else

158 DPRINTF ("%3d 0x%Ix", i++, sf.AddrPC.Offset);

159

160 line.SizeOfStruct = sizeof(IMAGEHLP_LINE);

161 if (SymGetLineFromAddr (GetCurrentProcess (), sf.AddrPC.Offset, &dwDisplacement, &line))

162 {

163 DPRINTF (" \[%s:%ld\]", line.FileName, line.LineNumber);

164 }

165

166 moduleInfo.SizeOfStruct = sizeof(moduleInfo);

167 if (SymGetModuleInfo (GetCurrentProcess (), sf.AddrPC.Offset, &moduleInfo))

168 {

169 DPRINTF (" in %s", moduleInfo.ModuleName);

170 }

171 DPRINTF ("\n");

172 old_address = sf.AddrPC;

173 }

174 ResumeThread (hThread);

175}

176

177static DWORD WINAPI dump_thread_proc (LPVOID lpParameter)

178{

179 dump_backtrace_for_thread ((HANDLE) lpParameter);

180 return 0;

181}

182

183/\* cannot get valid context from current thread, so we have to execute

184 \* backtrace from another thread \*/

185static void

186dump_backtrace (void)

187{

188 HANDLE hCurrentThread;

189 HANDLE hThread;

190 DWORD dwThreadId;

191 DuplicateHandle (GetCurrentProcess (), GetCurrentThread (),

192 GetCurrentProcess (), &hCurrentThread,

193 0, FALSE, DUPLICATE_SAME_ACCESS);

194 hThread = CreateThread (NULL, 0, dump_thread_proc, (LPVOID)hCurrentThread,

195 0, &dwThreadId);

196 WaitForSingleObject (hThread, INFINITE);

197 CloseHandle (hThread);

198 CloseHandle (hCurrentThread);

199}

200\#endif

201\#endif /\* asserts or tests enabled \*/

202

203\#ifdef BACKTRACES

204void \_dbus_print_backtrace (void)

205{

206 dump_backtrace ();

207}

208\#else

209void \_dbus_print_backtrace (void)

210{

211 \_dbus_verbose (" D-Bus not compiled with backtrace support\n");

212}

213\#endif

\_DBUS_ZERO

\#define \_DBUS_ZERO(object)

Sets all bits in an object to zero.

**Definition** dbus-internals.h:194

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
