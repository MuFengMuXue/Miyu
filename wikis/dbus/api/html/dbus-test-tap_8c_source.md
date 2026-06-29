dbus-test-tap.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-test-tap — TAP helpers for "embedded tests"

3 \*

4 \* Copyright © 2017 Collabora Ltd.

5 \* SPDX-License-Identifier: MIT

6 \*

7 \* Permission is hereby granted, free of charge, to any person

8 \* obtaining a copy of this software and associated documentation files

9 \* (the "Software"), to deal in the Software without restriction,

10 \* including without limitation the rights to use, copy, modify, merge,

11 \* publish, distribute, sublicense, and/or sell copies of the Software,

12 \* and to permit persons to whom the Software is furnished to do so,

13 \* subject to the following conditions:

14 \*

15 \* The above copyright notice and this permission notice shall be

16 \* included in all copies or substantial portions of the Software.

17 \*

18 \* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,

19 \* EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF

20 \* MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND

21 \* NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS

22 \* BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN

23 \* ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN

24 \* CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE

25 \* SOFTWARE.

26 \*/

27

28\#include \<config.h\>

29\#include "dbus/dbus-test-tap.h"

30

31/\*

32 \* TAP, the Test Anything Protocol, is a text-based syntax for test-cases

33 \* to report results to test harnesses.

34 \*

35 \* See \<http://testanything.org/\> for details of the syntax, which

36 \* will not be explained here.

37 \*/

38

39\#include \<stdio.h\>

40\#include \<stdlib.h\>

41

42static unsigned int failures = 0;

43static unsigned int skipped = 0;

44static unsigned int tap_test_counter = 0;

45

46/\*

47 \* Output TAP indicating a fatal error, and exit unsuccessfully.

48 \*/

49void

50\_dbus_test_fatal (const char \*format,

51 ...)

52{

53 va_list ap;

54

55 printf ("Bail out! ");

56 va_start (ap, format);

57 vprintf (format, ap);

58 va_end (ap);

59 printf ("\n");

60 fflush (stdout);

61 exit (1);

62}

63

64/\*

65 \* Output TAP indicating a diagnostic (informational message).

66 \*/

67void

68\_dbus_test_diag (const char \*format,

69 ...)

70{

71 va_list ap;

72

73 printf ("# ");

74 va_start (ap, format);

75 vprintf (format, ap);

76 va_end (ap);

77 printf ("\n");

78 fflush (stdout);

79}

80

81/\*

82 \* Output TAP indicating that all tests have been skipped, and exit

83 \* successfully.

84 \*

85 \* This is only valid if \_dbus_test_ok(), \_dbus_test_not_ok(),

86 \* etc. have not yet been called.

87 \*/

88void

89\_dbus_test_skip_all (const char \*format,

90 ...)

91{

92 va_list ap;

93

94 \_dbus_assert (tap_test_counter == 0);

95

96 printf ("1..0 \# SKIP - ");

97 va_start (ap, format);

98 vprintf (format, ap);

99 va_end (ap);

100 printf ("\n");

101 fflush (stdout);

102 exit (0);

103}

104

105/\*

106 \* Output TAP indicating that a test has passed, and increment the

107 \* test counter.

108 \*/

109void

110\_dbus_test_ok (const char \*format,

111 ...)

112{

113 va_list ap;

114

115 printf ("ok %u - ", ++tap_test_counter);

116 va_start (ap, format);

117 vprintf (format, ap);

118 va_end (ap);

119 printf ("\n");

120 fflush (stdout);

121}

122

123/\*

124 \* Output TAP indicating that a test has failed (in a way that is not

125 \* fatal to the test executable), and increment the test counter.

126 \*/

127void

128\_dbus_test_not_ok (const char \*format,

129 ...)

130{

131 va_list ap;

132

133 printf ("not ok %u - ", ++tap_test_counter);

134 va_start (ap, format);

135 vprintf (format, ap);

136 va_end (ap);

137 printf ("\n");

138 failures++;

139 fflush (stdout);

140}

141

142/\*

143 \* Output TAP indicating that a test has been skipped (in a way that is

144 \* not fatal to the test executable), and increment the test counter.

145 \*/

146void

147\_dbus_test_skip (const char \*format,

148 ...)

149{

150 va_list ap;

151

152 printf ("ok %u \# SKIP ", ++tap_test_counter);

153 ++skipped;

154 va_start (ap, format);

155 vprintf (format, ap);

156 va_end (ap);

157 printf ("\n");

158 fflush (stdout);

159}

160

161/\*

162 \* Shut down libdbus, check that exactly previously_allocated memory

163 \* blocks are allocated, and output TAP indicating a test pass or failure.

164 \*

165 \* Return TRUE if no leaks were detected.

166 \*/

167void

168\_dbus_test_check_memleaks (const char \*test_name)

169{

170\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

171 dbus_shutdown ();

172

173 if (\_dbus_get_malloc_blocks_outstanding () == 0)

174 {

175 printf ("ok %u - %s did not leak memory\n", ++tap_test_counter,

176 test_name);

177 }

178 else

179 {

180 printf ("not ok %u - %s leaked %d blocks\n",

181 ++tap_test_counter, test_name,

182 \_dbus_get_malloc_blocks_outstanding ());

183 failures++;

184 }

185\#else

186 \_dbus_test_skip (

187 "unable to determine whether %s leaked memory (not compiled "

188 "with memory instrumentation)",

189 test_name);

190\#endif

191}

192

193/\*

194 \* Output TAP indicating that testing has finished and no more tests

195 \* are going to be run. Return the Unix-style exit code.

196 \*/

197int

198\_dbus_test_done_testing (void)

199{

200 \_dbus_assert (skipped \<= tap_test_counter);

201

202 if (failures == 0)

203 \_dbus_test_diag ("%u tests passed (%d skipped)",

204 tap_test_counter - skipped, skipped);

205 else

206 \_dbus_test_diag ("%u/%u tests failed (%d skipped)",

207 failures, tap_test_counter - skipped, skipped);

208

209 printf ("1..%u\n", tap_test_counter);

210 fflush (stdout);

211

212 if (failures == 0)

213 return 0;

214

215 return 1;

216}

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

dbus_shutdown

void dbus_shutdown(void)

Frees all memory allocated internally by libdbus and reverses the effects of dbus_threads_init().

**Definition** dbus-memory.c:906
