dbus-internals.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-internals.h random utility stuff (internal to D-Bus implementation)

3 \*

4 \* Copyright (C) 2002, 2003 Red Hat, Inc.

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

25\#ifdef DBUS_INSIDE_DBUS_H

26\#error "You can't include dbus-internals.h in the public header dbus.h"

27\#endif

28

29\#ifndef DBUS_INTERNALS_H

30\#define DBUS_INTERNALS_H

31

32\#include \<dbus/dbus-memory.h\>

33\#include \<dbus/dbus-types.h\>

34\#include \<dbus/dbus-errors.h\>

35\#include \<dbus/dbus-sysdeps.h\>

36\#include \<dbus/dbus-macros-internal.h\>

37\#include \<dbus/dbus-threads-internal.h\>

38

39DBUS_BEGIN_DECLS

40

41DBUS_PRIVATE_EXPORT

42void \_dbus_warn (const char \*format,

43 ...) \_DBUS_GNUC_PRINTF (1, 2);

44

45DBUS_PRIVATE_EXPORT

46void \_dbus_warn_check_failed (const char \*format,

47 ...) \_DBUS_GNUC_PRINTF (1, 2);

48DBUS_PRIVATE_EXPORT

49void \_dbus_warn_return_if_fail (const char \*function,

50 const char \*assertion,

51 const char \*file,

52 int line);

53

54DBUS_EMBEDDED_TESTS_EXPORT

55int \_dbus_get_check_failed_count (void);

56

57\#if defined (\_\_STDC_VERSION\_\_) && (\_\_STDC_VERSION\_\_ \>= 199901L)

58\#define \_DBUS_FUNCTION_NAME \_\_func\_\_

59\#elif defined(\_\_GNUC\_\_) \|\| defined(\_MSC_VER)

60\#define \_DBUS_FUNCTION_NAME \_\_FUNCTION\_\_

61\#else

62\#define \_DBUS_FUNCTION_NAME "unknown function"

63\#endif

64

65/\*

66 \* (code from GLib)

67 \*

68 \* The \_DBUS_LIKELY and \_DBUS_UNLIKELY macros let the programmer give hints to

69 \* the compiler about the expected result of an expression. Some compilers

70 \* can use this information for optimizations.

71 \*

72 \* The \_DBUS_BOOLEAN_EXPR macro is intended to trigger a gcc warning when

73 \* putting assignments in the macro arg

74 \*/

75\#if defined(\_\_GNUC\_\_) && (\_\_GNUC\_\_ \> 2) && defined(\_\_OPTIMIZE\_\_)

76\#define \_DBUS_BOOLEAN_EXPR(expr) \\

77 \_\_extension\_\_ ({ \\

78 int \_dbus_boolean_var\_; \\

79 if (expr) \\

80 \_dbus_boolean_var\_ = 1; \\

81 else \\

82 \_dbus_boolean_var\_ = 0; \\

83 \_dbus_boolean_var\_; \\

84})

85\#define \_DBUS_LIKELY(expr) (\_\_builtin_expect (\_DBUS_BOOLEAN_EXPR(expr), 1))

86\#define \_DBUS_UNLIKELY(expr) (\_\_builtin_expect (\_DBUS_BOOLEAN_EXPR(expr), 0))

87\#else

88\#define \_DBUS_LIKELY(expr) (expr)

89\#define \_DBUS_UNLIKELY(expr) (expr)

90\#endif

91

92\#ifdef DBUS_ENABLE_VERBOSE_MODE

93

94/\*

95 at least gnu cc and msvc compiler are known to

96 have support for variable macro argument lists

97 add other compilers is required

98\*/

99\#if defined(\_\_GNUC\_\_) \|\| defined(\_MSC_VER)

100\#define DBUS_CPP_SUPPORTS_VARIABLE_MACRO_ARGUMENTS

101\#endif

102

103\#ifdef DBUS_CPP_SUPPORTS_VARIABLE_MACRO_ARGUMENTS

104DBUS_PRIVATE_EXPORT

105void \_dbus_verbose_real (const char \*file, const int line, const char \*function,

106 const char \*format,...) \_DBUS_GNUC_PRINTF (4, 5);

107\# define \_dbus_verbose(fmt,...) \_dbus_verbose_real( \_\_FILE\_\_,\_\_LINE\_\_,\_DBUS_FUNCTION_NAME,fmt, \## \_\_VA_ARGS\_\_)

108\#else

109DBUS_PRIVATE_EXPORT

110void \_dbus_verbose_real (const char \*format,

111 ...) \_DBUS_GNUC_PRINTF (1, 2);

112\# define \_dbus_verbose \_dbus_verbose_real

113\#endif

114DBUS_PRIVATE_EXPORT

115void \_dbus_verbose_reset_real (void);

116DBUS_PRIVATE_EXPORT

117dbus_bool_t \_dbus_is_verbose_real (void);

118DBUS_PRIVATE_EXPORT

119dbus_bool_t \_dbus_get_verbose (void);

120DBUS_PRIVATE_EXPORT

121void \_dbus_set_verbose (dbus_bool_t state);

122void \_dbus_verbose_raw (const char \*s);

123

124\# define \_dbus_verbose_reset \_dbus_verbose_reset_real

125\# define \_dbus_is_verbose \_dbus_is_verbose_real

126\#else

127\# define \_dbus_verbose(...) do { } while (0)

128\# define \_dbus_verbose_reset() do { } while (0)

129\# define \_dbus_is_verbose() FALSE

130\#endif /\* !DBUS_ENABLE_VERBOSE_MODE \*/

131

132DBUS_PRIVATE_EXPORT

133void \_dbus_trace_ref (const char \*obj_name,

134 void \*obj,

135 int old_refcount,

136 int new_refcount,

137 const char \*why,

138 const char \*env_var,

139 int \*enabled);

140

141DBUS_PRIVATE_EXPORT

142const char\* \_dbus_strerror (int error_number);

143

144\#ifdef DBUS_DISABLE_ASSERT

145\#define \_dbus_assert(condition) do { } while (0)

146\#else

147DBUS_PRIVATE_EXPORT

148void \_dbus_real_assert (dbus_bool_t condition,

149 const char \*condition_text,

150 const char \*file,

151 int line,

152 const char \*func);

153\#define \_dbus_assert(condition) \\

154 \_dbus_real_assert ((condition) != 0, \#condition, \_\_FILE\_\_, \_\_LINE\_\_, \_DBUS_FUNCTION_NAME)

155\#endif /\* !DBUS_DISABLE_ASSERT \*/

156

157\#ifdef DBUS_DISABLE_ASSERT

158\#define \_dbus_assert_not_reached(explanation) do { } while (0)

159\#else

160DBUS_PRIVATE_EXPORT

161void \_dbus_real_assert_not_reached (const char \*explanation,

162 const char \*file,

163 int line) \_DBUS_GNUC_NORETURN;

164\#define \_dbus_assert_not_reached(explanation) \\

165 \_dbus_real_assert_not_reached (explanation, \_\_FILE\_\_, \_\_LINE\_\_)

166\#endif /\* !DBUS_DISABLE_ASSERT \*/

167

168\#ifdef DBUS_DISABLE_CHECKS

169\#define \_dbus_return_if_fail(condition)

170\#define \_dbus_return_val_if_fail(condition, val)

171\#else

172

173\#define \_dbus_return_if_fail(condition) do { \\

174 \_dbus_assert ((\*(const char\*)\_DBUS_FUNCTION_NAME) != '\_'); \\

175 if (!(condition)) { \\

176 \_dbus_warn_return_if_fail (\_DBUS_FUNCTION_NAME, \#condition, \_\_FILE\_\_, \_\_LINE\_\_); \\

177 return; \\

178 } } while (0)

179

180\#define \_dbus_return_val_if_fail(condition, val) do { \\

181 \_dbus_assert ((\*(const char\*)\_DBUS_FUNCTION_NAME) != '\_'); \\

182 if (!(condition)) { \\

183 \_dbus_warn_return_if_fail (\_DBUS_FUNCTION_NAME, \#condition, \_\_FILE\_\_, \_\_LINE\_\_); \\

184 return (val); \\

185 } } while (0)

186

187\#endif /\* !DBUS_DISABLE_ASSERT \*/

188

189\#define \_DBUS_N_ELEMENTS(array) ((int) (sizeof ((array)) / sizeof ((array)\[0\])))

190

191\#define \_DBUS_POINTER_TO_INT(pointer) ((intptr_t)(pointer))

192\#define \_DBUS_INT_TO_POINTER(integer) ((void\*)((intptr_t)(integer)))

193

194\#define \_DBUS_ZERO(object) (memset (&(object), '\0', sizeof ((object))))

195

196\#ifdef offsetof

197\#define \_DBUS_STRUCT_OFFSET(struct_type, member) \\

198 (offsetof (struct_type, member))

199\#else

200\#define \_DBUS_STRUCT_OFFSET(struct_type, member) \\

201 ((intptr_t) ((unsigned char\*) &((struct_type\*) 0)-\>member))

202\#endif

203

204\#if defined(\_\_STDC_VERSION\_\_) && \_\_STDC_VERSION\_\_ \>= 201112L && !defined(\_\_cplusplus)

205\#define \_DBUS_ALIGNOF(type) \_Alignof(type)

206\#else

207\#define \_DBUS_ALIGNOF(type) \\

208 (\_DBUS_STRUCT_OFFSET (struct { char \_1; type \_2; }, \_2))

209\#endif

210

211\#if defined(DBUS_DISABLE_CHECKS) \|\| defined(DBUS_DISABLE_ASSERT)

212/\* this is an assert and not an error, but in the typical --disable-checks case (you're trying

213 \* to really minimize code size), disabling these assertions makes sense.

214 \*/

215\#define \_DBUS_ASSERT_ERROR_IS_SET(error) do { } while (0)

216\#define \_DBUS_ASSERT_ERROR_IS_CLEAR(error) do { } while (0)

217\#define \_DBUS_ASSERT_ERROR_XOR_BOOL(error, retval) do { } while (0)

218\#else

219static inline void

220\_dbus_assert_error_is_set (const DBusError \*error,

221 const char \*file,

222 int line,

223 const char \*func)

224{

225 \_dbus_real_assert (error == NULL \|\| dbus_error_is_set (error),

226 "error is set", file, line, func);

227}

228

229static inline void

230\_dbus_assert_error_is_clear (const DBusError \*error,

231 const char \*file,

232 int line,

233 const char \*func)

234{

235 \_dbus_real_assert (error == NULL \|\| !dbus_error_is_set (error),

236 "error is clear", file, line, func);

237}

238

239static inline void

240\_dbus_assert_error_xor_bool (const DBusError \*error,

241 dbus_bool_t retval,

242 const char \*file,

243 int line,

244 const char \*func)

245{

246 \_dbus_real_assert (error == NULL \|\| dbus_error_is_set (error) == !retval,

247 "error is consistent with boolean result", file, line, func);

248}

249

254\#define \_DBUS_ASSERT_ERROR_IS_SET(error) \_dbus_assert_error_is_set (error, \_\_FILE\_\_, \_\_LINE\_\_, \_DBUS_FUNCTION_NAME)

255

260\#define \_DBUS_ASSERT_ERROR_IS_CLEAR(error) \_dbus_assert_error_is_clear (error, \_\_FILE\_\_, \_\_LINE\_\_, \_DBUS_FUNCTION_NAME)

261

268\#define \_DBUS_ASSERT_ERROR_XOR_BOOL(error, retval) \_dbus_assert_error_xor_bool (error, retval, \_\_FILE\_\_, \_\_LINE\_\_, \_DBUS_FUNCTION_NAME)

269\#endif

270

271\#define \_dbus_return_if_error_is_set(error) \_dbus_return_if_fail ((error) == NULL \|\| !dbus_error_is_set ((error)))

272\#define \_dbus_return_val_if_error_is_set(error, val) \_dbus_return_val_if_fail ((error) == NULL \|\| !dbus_error_is_set ((error)), (val))

273

274/\* This alignment thing is from ORBit2 \*/

275/\* Align a value upward to a boundary, expressed as a number of bytes.

276 \* E.g. align to an 8-byte boundary with argument of 8.

277 \*/

278

279/\*

280 \* (this + boundary - 1)

281 \* &

282 \* ~(boundary - 1)

283 \*/

284

285\#define \_DBUS_ALIGN_VALUE(this, boundary) \\

286 ((((uintptr_t) (this)) + (((size_t) (boundary)) - 1)) & \\

287 (~(((size_t) (boundary)) - 1)))

288

289\#define \_DBUS_ALIGN_ADDRESS(this, boundary) \\

290 ((void\*)\_DBUS_ALIGN_VALUE(this, boundary))

291

292\#define \_DBUS_IS_ALIGNED(this, boundary) \\

293 ((((size_t) (uintptr_t) (this)) & ((size_t) (boundary) - 1)) == 0)

294

302\#if defined(\_\_STDC_VERSION\_\_) && (\_\_STDC_VERSION\_\_ \>= 201112L)

303typedef max_align_t dbus_max_align_t;

304\#else

305typedef DBusBasicValue dbus_max_align_t;

306\#endif

307

308DBUS_PRIVATE_EXPORT

309char\* \_dbus_strdup (const char \*str);

310void\* \_dbus_memdup (const void \*mem,

311 size_t n_bytes);

312DBUS_PRIVATE_EXPORT

313dbus_bool_t \_dbus_string_array_contains (const char \*\*array,

314 const char \*str);

315DBUS_PRIVATE_EXPORT

316size_t \_dbus_string_array_length (const char \*\*array);

317char\*\* \_dbus_dup_string_array (const char \*\*array);

318

319\#define \_DBUS_INT16_MIN ((dbus_int16_t) 0x8000)

320\#define \_DBUS_INT16_MAX ((dbus_int16_t) 0x7fff)

321\#define \_DBUS_UINT16_MAX ((dbus_uint16_t)0xffff)

322\#define \_DBUS_INT32_MIN ((dbus_int32_t) 0x80000000)

323\#define \_DBUS_INT32_MAX ((dbus_int32_t) 0x7fffffff)

324\#define \_DBUS_UINT32_MAX ((dbus_uint32_t)0xffffffff)

325/\* using 32-bit here is sort of bogus \*/

326\#define \_DBUS_INT_MIN \_DBUS_INT32_MIN

327\#define \_DBUS_INT_MAX \_DBUS_INT32_MAX

328\#define \_DBUS_UINT_MAX \_DBUS_UINT32_MAX

329\#define \_DBUS_INT64_MAX DBUS_INT64_CONSTANT (0x7fffffffffffffff)

330\#define \_DBUS_UINT64_MAX DBUS_UINT64_CONSTANT (0xffffffffffffffff)

331\#define \_DBUS_ONE_KILOBYTE 1024

332\#define \_DBUS_ONE_MEGABYTE 1024 \* \_DBUS_ONE_KILOBYTE

333\#define \_DBUS_ONE_HOUR_IN_MILLISECONDS (1000 \* 60 \* 60)

334\#define \_DBUS_USEC_PER_SECOND (1000000)

335

336\#undef MAX

337\#define MAX(a, b) (((a) \> (b)) ? (a) : (b))

338

339\#undef MIN

340\#define MIN(a, b) (((a) \< (b)) ? (a) : (b))

341

342\#undef ABS

343\#define ABS(a) (((a) \< 0) ? -(a) : (a))

344

345\#define \_DBUS_ISASCII(c) ((c) != '\0' && (((c) & ~0x7f) == 0))

346

347typedef void (\* DBusForeachFunction) (void \*element,

348 void \*data);

349

350void \_dbus_verbose_bytes (const unsigned char \*data,

351 int len,

352 int offset);

353DBUS_PRIVATE_EXPORT

354void \_dbus_verbose_bytes_of_string (const DBusString \*str,

355 int start,

356 int len);

357

358DBUS_PRIVATE_EXPORT

359extern const char \*\_dbus_no_memory_message;

360\#define \_DBUS_SET_OOM(error) dbus_set_error_const ((error), DBUS_ERROR_NO_MEMORY, \_dbus_no_memory_message)

361DBUS_PRIVATE_EXPORT

362void \_dbus_set_error_valist (DBusError \*error,

363 const char \*name,

364 const char \*format,

365 va_list args) \_DBUS_GNUC_PRINTF (3, 0);

366

367typedef dbus_bool_t (\* DBusTestMemoryFunction) (void \*data,

368 dbus_bool_t have_memory);

369

370\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

371/\* Memory debugging \*/

372void \_dbus_set_fail_alloc_counter (int until_next_fail);

373int \_dbus_get_fail_alloc_counter (void);

374void \_dbus_set_fail_alloc_failures (int failures_per_failure);

375int \_dbus_get_fail_alloc_failures (void);

376dbus_bool_t \_dbus_decrement_fail_alloc_counter (void);

377dbus_bool_t \_dbus_disable_mem_pools (void);

378DBUS_PRIVATE_EXPORT

379int \_dbus_get_malloc_blocks_outstanding (void);

380

381DBUS_PRIVATE_EXPORT

382dbus_bool_t \_dbus_test_oom_handling (const char \*description,

383 DBusTestMemoryFunction func,

384 void \*data);

385\#else

386\#define \_dbus_set_fail_alloc_counter(n)

387\#define \_dbus_get_fail_alloc_counter (-1)

388

389/\* These are constant expressions so that blocks

390 \* they protect should be optimized away

391 \*/

392\#define \_dbus_decrement_fail_alloc_counter() (FALSE)

393\#define \_dbus_disable_mem_pools() (FALSE)

394\#define \_dbus_get_malloc_blocks_outstanding() (0)

395

396\#define \_dbus_test_oom_handling(description, func, data) ((\*func) (data, TRUE))

397\#endif /\* !DBUS_ENABLE_EMBEDDED_TESTS \*/

398

399typedef void (\* DBusShutdownFunction) (void \*data);

400DBUS_PRIVATE_EXPORT

401dbus_bool_t \_dbus_register_shutdown_func (DBusShutdownFunction function,

402 void \*data);

403dbus_bool_t \_dbus_register_shutdown_func_unlocked (DBusShutdownFunction function,

404 void \*data);

405

406extern int \_dbus_current_generation;

407

408/\* The weird case convention is to avoid having to change all the callers,

409 \* which would be quite a mega-patch. \*/

410typedef enum

411{

412 /\* index 0-4 \*/

413 \_DBUS_LOCK_list,

414 \_DBUS_LOCK_connection_slots,

415 \_DBUS_LOCK_pending_call_slots,

416 \_DBUS_LOCK_server_slots,

417 \_DBUS_LOCK_message_slots,

418 /\* index 5-9 \*/

419 \_DBUS_LOCK_bus,

420 \_DBUS_LOCK_bus_datas,

421 \_DBUS_LOCK_shutdown_funcs,

422 \_DBUS_LOCK_system_users,

423 \_DBUS_LOCK_message_cache,

424 /\* index 10-12 \*/

425 \_DBUS_LOCK_shared_connections,

426 \_DBUS_LOCK_machine_uuid,

427 \_DBUS_LOCK_sysdeps,

428

429 \_DBUS_N_GLOBAL_LOCKS

430} DBusGlobalLock;

431

432\_DBUS_WARN_UNUSED_RESULT

433dbus_bool_t \_dbus_lock (DBusGlobalLock lock);

434void \_dbus_unlock (DBusGlobalLock lock);

435

436\#define \_DBUS_LOCK_NAME(name) \_DBUS_LOCK\_##name

437\#define \_DBUS_LOCK(name) \_dbus_lock (\_DBUS_LOCK\_##name)

438\#define \_DBUS_UNLOCK(name) \_dbus_unlock (\_DBUS_LOCK\_##name)

439

440DBUS_PRIVATE_EXPORT

441dbus_bool_t \_dbus_address_append_escaped (DBusString \*escaped,

442 const DBusString \*unescaped);

443

444void \_dbus_set_bad_address (DBusError \*error,

445 const char \*address_problem_type,

446 const char \*address_problem_field,

447 const char \*address_problem_other);

448

449\#define DBUS_UUID_LENGTH_BYTES 16

450\#define DBUS_UUID_LENGTH_WORDS (DBUS_UUID_LENGTH_BYTES / 4)

451\#define DBUS_UUID_LENGTH_HEX (DBUS_UUID_LENGTH_BYTES \* 2)

452

457union DBusGUID

458{

459 dbus_uint32_t as_uint32s\[DBUS_UUID_LENGTH_WORDS\];

460 char as_bytes\[DBUS_UUID_LENGTH_BYTES\];

461};

462

463DBUS_PRIVATE_EXPORT \_DBUS_WARN_UNUSED_RESULT

464dbus_bool_t \_dbus_generate_uuid (DBusGUID \*uuid,

465 DBusError \*error);

466DBUS_PRIVATE_EXPORT

467dbus_bool_t \_dbus_uuid_encode (const DBusGUID \*uuid,

468 DBusString \*encoded);

469dbus_bool_t \_dbus_read_uuid_file (const DBusString \*filename,

470 DBusGUID \*uuid,

471 dbus_bool_t create_if_not_found,

472 DBusError \*error);

473

474dbus_bool_t \_dbus_write_uuid_file (const DBusString \*filename,

475 const DBusGUID \*uuid,

476 DBusError \*error);

477

478DBUS_PRIVATE_EXPORT

479dbus_bool_t \_dbus_get_local_machine_uuid_encoded (DBusString \*uuid_str,

480 DBusError \*error);

481

482\#define \_DBUS_PASTE2(a, b) a \## b

483\#define \_DBUS_PASTE(a, b) \_DBUS_PASTE2 (a, b)

484\#define \_DBUS_STATIC_ASSERT(expr) \\

485 typedef struct { char \_assertion\[(expr) ? 1 : -1\]; } \\

486 \_DBUS_PASTE (\_DBUS_STATIC_ASSERT\_, \_\_LINE\_\_) \_DBUS_GNUC_UNUSED

487

488\#define \_DBUS_STRINGIFY(x) \#x

489\#define \_DBUS_FILE_LINE \_\_FILE\_\_ ":" \_DBUS_STRINGIFY(\_\_LINE\_\_)

490

491\#ifndef \_\_has_feature

492\# define \_\_has_feature(x) 0

493\#endif

494

495/\* MSVC defines \_\_SANITIZE_ADDRESS\_\_, but does not provide the special

496 \* builtins associated with it. \*/

497\#if ((defined(\_\_SANITIZE_ADDRESS\_\_) \|\| \_\_has_feature(address_sanitizer)) && \\

498 !defined(\_MSC_VER))

499\# include \<sanitizer/lsan_interface.h\>

500/\* Defined if we are building with AddressSanitizer \*/

501\# define \_DBUS_ADDRESS_SANITIZER

502/\* Ignore memory allocations until the next \_DBUS_END_IGNORE_LEAKS when

503 \* checking for memory leaks \*/

504\# define \_DBUS_BEGIN_IGNORE_LEAKS \_\_lsan_disable ()

505/\* End the scope of a previous \_DBUS_BEGIN_IGNORE_LEAKS \*/

506\# define \_DBUS_END_IGNORE_LEAKS \_\_lsan_enable ()

507\#else

508\# undef \_DBUS_ADDRESS_SANITIZER

509\# define \_DBUS_BEGIN_IGNORE_LEAKS do { } while (0)

510\# define \_DBUS_END_IGNORE_LEAKS do { } while (0)

511\#endif

512

516\#ifdef DBUS_WIN

517\#define DBUS_IS_DIR_SEPARATOR(c) (c == '\\' \|\| c == '/')

518\#define DBUS_DIR_SEPARATOR '\\'

519\#define DBUS_DIR_SEPARATOR_S "\\"

520\#else

521\#define DBUS_IS_DIR_SEPARATOR(c) (c == '/')

522\#define DBUS_DIR_SEPARATOR '/'

523\#define DBUS_DIR_SEPARATOR_S "/"

524\#endif

525

526DBUS_END_DECLS

527

528\#endif /\* DBUS_INTERNALS_H \*/

\_dbus_address_append_escaped

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_address_append_escaped(DBusString \*escaped, const DBusString \*unescaped)

Appends an escaped version of one string to another string, using the D-Bus address escaping mechanis...

**Definition** dbus-address.c:109

\_dbus_set_bad_address

void \_dbus_set_bad_address(DBusError \*error, const char \*address_problem_type, const char \*address_problem_field, const char \*address_problem_other)

Sets DBUS_ERROR_BAD_ADDRESS.

**Definition** dbus-address.c:70

dbus_error_is_set

dbus_bool_t dbus_error_is_set(const DBusError \*error)

Checks whether an error occurred (the error is set).

**Definition** dbus-errors.c:331

\_dbus_real_assert_not_reached

DBUS_PRIVATE_EXPORT void \_dbus_real_assert_not_reached(const char \*explanation, const char \*file, int line) \_DBUS_GNUC_NORETURN

Internals of \_dbus_assert_not_reached(); it's a function rather than a macro with the inline code so ...

**Definition** dbus-internals.c:1067

\_dbus_generate_uuid

DBUS_PRIVATE_EXPORT \_DBUS_WARN_UNUSED_RESULT dbus_bool_t \_dbus_generate_uuid(DBusGUID \*uuid, DBusError \*error)

Generates a new UUID.

**Definition** dbus-internals.c:752

\_dbus_warn_check_failed

DBUS_PRIVATE_EXPORT void \_dbus_warn_check_failed(const char \*format,...)

Prints a "critical" warning to stderr when an assertion fails; differs from \_dbus_warn primarily in t...

**Definition** dbus-internals.c:310

\_dbus_strdup

DBUS_PRIVATE_EXPORT char \* \_dbus_strdup(const char \*str)

Duplicates a string.

**Definition** dbus-internals.c:621

\_dbus_read_uuid_file

dbus_bool_t \_dbus_read_uuid_file(const DBusString \*filename, DBusGUID \*uuid, dbus_bool_t create_if_not_found, DBusError \*error)

Reads (and optionally writes) a uuid to a file.

**Definition** dbus-internals.c:931

\_dbus_string_array_contains

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_array_contains(const char \*\*array, const char \*str)

Checks whether a string array contains the given string.

**Definition** dbus-internals.c:712

\_dbus_get_local_machine_uuid_encoded

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_get_local_machine_uuid_encoded(DBusString \*uuid_str, DBusError \*error)

Gets the hex-encoded UUID of the machine this function is executed on.

**Definition** dbus-internals.c:983

\_dbus_real_assert

DBUS_PRIVATE_EXPORT void \_dbus_real_assert(dbus_bool_t condition, const char \*condition_text, const char \*file, int line, const char \*func)

Internals of \_dbus_assert(); it's a function rather than a macro with the inline code so that the ass...

**Definition** dbus-internals.c:1042

\_dbus_write_uuid_file

dbus_bool_t \_dbus_write_uuid_file(const DBusString \*filename, const DBusGUID \*uuid, DBusError \*error)

Write the give UUID to a file.

**Definition** dbus-internals.c:882

\_dbus_warn

DBUS_PRIVATE_EXPORT void \_dbus_warn(const char \*format,...)

Prints a warning message to stderr.

**Definition** dbus-internals.c:278

\_dbus_string_array_length

DBUS_PRIVATE_EXPORT size_t \_dbus_string_array_length(const char \*\*array)

Returns the size of a string array.

**Definition** dbus-internals.c:735

\_dbus_no_memory_message

DBUS_PRIVATE_EXPORT const char \* \_dbus_no_memory_message

Fixed "out of memory" error message, just to avoid making up a different string every time and wastin...

**Definition** dbus-internals.c:216

\_dbus_memdup

void \* \_dbus_memdup(const void \*mem, size_t n_bytes)

Duplicates a block of memory.

**Definition** dbus-internals.c:649

\_dbus_uuid_encode

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_uuid_encode(const DBusGUID \*uuid, DBusString \*encoded)

Hex-encode a UUID.

**Definition** dbus-internals.c:788

\_dbus_dup_string_array

char \*\* \_dbus_dup_string_array(const char \*\*array)

Duplicates a string array.

**Definition** dbus-internals.c:672

NULL

\#define NULL

A null pointer, defined appropriately for C or C++.

**Definition** dbus-macros.h:51

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

\_dbus_verbose_bytes_of_string

DBUS_PRIVATE_EXPORT void \_dbus_verbose_bytes_of_string(const DBusString \*str, int start, int len)

Dump the given part of the string to verbose log.

**Definition** dbus-marshal-basic.c:1428

\_dbus_verbose_bytes

void \_dbus_verbose_bytes(const unsigned char \*data, int len, int offset)

If in verbose mode, print a block of binary data.

**Definition** dbus-marshal-basic.c:1351

\_dbus_current_generation

int \_dbus_current_generation

\_dbus_current_generation is used to track each time that dbus_shutdown() is called,...

**Definition** dbus-memory.c:790

\_dbus_register_shutdown_func

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_register_shutdown_func(DBusShutdownFunction function, void \*data)

Register a cleanup function to be called exactly once the next time dbus_shutdown() is called.

**Definition** dbus-memory.c:819

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusString

**Definition** dbus-string.h:47

DBusBasicValue

A simple value union that lets you access bytes as if they were various types; useful when dealing wi...

**Definition** dbus-types.h:161

DBusGUID

A globally unique ID ; we have one for each DBusServer, and also one for each machine with libdbus in...

**Definition** dbus-internals.h:458

DBusGUID::as_uint32s

dbus_uint32_t as_uint32s\[DBUS_UUID_LENGTH_WORDS\]

guid as four uint32 values

**Definition** dbus-internals.h:459

DBusGUID::as_bytes

char as_bytes\[DBUS_UUID_LENGTH_BYTES\]

guid as 16 single-byte values

**Definition** dbus-internals.h:460
