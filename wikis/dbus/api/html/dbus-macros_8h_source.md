dbus-macros.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-macros.h generic macros

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

25\#if !defined (DBUS_INSIDE_DBUS_H) && !defined (DBUS_COMPILATION)

26\#error "Only \<dbus/dbus.h\> can be included directly, this file may disappear or change contents."

27\#endif

28

29\#ifndef DBUS_MACROS_H

30\#define DBUS_MACROS_H

31

32\#ifdef \_\_cplusplus

33\# define DBUS_BEGIN_DECLS extern "C" {

34\# define DBUS_END_DECLS }

35\#else

36\# define DBUS_BEGIN_DECLS

37\# define DBUS_END_DECLS

38\#endif

39

40\#ifndef TRUE

41\# define TRUE 1

42\#endif

43\#ifndef FALSE

44\# define FALSE 0

45\#endif

46

47\#ifndef NULL

48\# ifdef \_\_cplusplus

49\# define NULL (0L)

50\# else /\* !\_\_cplusplus \*/

51\# define NULL ((void\*) 0)

52\# endif /\* !\_\_cplusplus \*/

53\#endif

54

55\#if \_\_GNUC\_\_ \> 3 \|\| (\_\_GNUC\_\_ == 3 && \_\_GNUC_MINOR\_\_ \>= 1)

56\# define DBUS_DEPRECATED \_\_attribute\_\_ ((\_\_deprecated\_\_))

57\#elif defined(\_MSC_VER) && (\_MSC_VER \>= 1300)

58\# define DBUS_DEPRECATED \_\_declspec(deprecated)

59\#else

60\# define DBUS_DEPRECATED

61\#endif

62

63\#if \_\_GNUC\_\_ \> 2 \|\| (\_\_GNUC\_\_ == 2 && \_\_GNUC_MINOR\_\_ \>= 8)

64\# define \_DBUS_GNUC_EXTENSION \_\_extension\_\_

65\#else

66\# define \_DBUS_GNUC_EXTENSION

67\#endif

68

69\#if (\_\_GNUC\_\_ \> 2 \|\| (\_\_GNUC\_\_ == 2 && \_\_GNUC_MINOR\_\_ \> 4)) \|\| \\

70 defined(\_\_clang\_\_)

71\#define \_DBUS_GNUC_PRINTF( format_idx, arg_idx ) \\

72 \_\_attribute\_\_((\_\_format\_\_ (\_\_printf\_\_, format_idx, arg_idx)))

73\#define \_DBUS_GNUC_NORETURN \\

74 \_\_attribute\_\_((\_\_noreturn\_\_))

75\#define \_DBUS_GNUC_UNUSED \\

76 \_\_attribute\_\_((\_\_unused\_\_))

77\#else /\* !\_\_GNUC\_\_ \*/

78\#define \_DBUS_GNUC_PRINTF( format_idx, arg_idx )

79\#define \_DBUS_GNUC_NORETURN

80\#define \_DBUS_GNUC_UNUSED

81\#endif /\* !\_\_GNUC\_\_ \*/

82

83\#if \_\_GNUC\_\_ \> 2 \|\| (\_\_GNUC\_\_ == 2 && \_\_GNUC_MINOR\_\_ \>= 96)

84\#define DBUS_MALLOC \_\_attribute\_\_((\_\_malloc\_\_))

85\#else

86\#define DBUS_MALLOC

87\#endif

88

89\#if (\_\_GNUC\_\_ \> 4) \|\| (\_\_GNUC\_\_ == 4 && \_\_GNUC_MINOR\_\_ \>= 3)

90\#define DBUS_ALLOC_SIZE(x) \_\_attribute\_\_((\_\_alloc_size\_\_(x)))

91\#define DBUS_ALLOC_SIZE2(x,y) \_\_attribute\_\_((\_\_alloc_size\_\_(x,y)))

92\#else

93\#define DBUS_ALLOC_SIZE(x)

94\#define DBUS_ALLOC_SIZE2(x,y)

95\#endif

96

109\#if defined(\_MSC_VER) && (\_MSC_VER \>= 1700)

110\#define \_DBUS_WARN_UNUSED_RESULT \_Must_inspect_result\_

111\#elif (\_\_GNUC\_\_ \> 3) \|\| (\_\_GNUC\_\_ == 3 && \_\_GNUC_MINOR\_\_ \>= 4)

112\#define \_DBUS_WARN_UNUSED_RESULT \_\_attribute\_\_((warn_unused_result))

113\#else

114\#define \_DBUS_WARN_UNUSED_RESULT

115\#endif

116

124/\* Normally docs are in .c files, but there isn't a .c file for this. \*/

192/\*

193 \* @def DBUS_EXPORT

194 \*

195 \* Declare the following symbol as public. This is currently a noop on

196 \* platforms other than Windows.

197 \*/

198

199\#if defined(DBUS_EXPORT)

200 /\* value forced by compiler command line, don't redefine \*/

201\#elif defined(\_WIN32)

202\# if defined(DBUS_STATIC_BUILD)

203\# define DBUS_EXPORT

204\# elif defined(dbus_1_EXPORTS)

205\# define DBUS_EXPORT \_\_declspec(dllexport)

206\# else

207\# define DBUS_EXPORT \_\_declspec(dllimport)

208\# endif

209\#elif defined(\_\_GNUC\_\_) && \_\_GNUC\_\_ \>= 4

210\# define DBUS_EXPORT \_\_attribute\_\_ ((\_\_visibility\_\_ ("default")))

211\#else

212\#define DBUS_EXPORT

213\#endif

214

215/\* Implementation for dbus_clear_message() etc. This is not API,

216 \* do not use it directly.

217 \*

218 \* We're using a specific type (T \*\* and T \*) instead of void \*\* and

219 \* void \* partly for type-safety, partly to be strict-aliasing-compliant,

220 \* and partly to keep C++ compilers happy. This code is inlined into

221 \* users of libdbus, so we can't rely on it having dbus' own compiler

222 \* settings. \*/

223\#define \_dbus_clear_pointer_impl(T, pointer_to_pointer, destroy) \\

224 do { \\

225 T \*\*\_pp = (pointer_to_pointer); \\

226 T \*\_value = \*\_pp; \\

227 \\

228 \*\_pp = NULL; \\

229 \\

230 if (\_value != NULL) \\

231 destroy (\_value); \\

232 } while (0)

233/\* Not (destroy) (\_value) in case destroy() is a function-like macro \*/

234

237\#endif /\* DBUS_MACROS_H \*/
