dbus-internals.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-internals.c random utility stuff (internal to D-Bus implementation)

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

25

26\#include \<config.h\>

27\#include "dbus-internals.h"

28\#include "dbus-protocol.h"

29\#include "dbus-marshal-basic.h"

30\#include "dbus-test.h"

31\#include "dbus-test-tap.h"

32\#include "dbus-valgrind-internal.h"

33\#include \<stdio.h\>

34\#include \<stdarg.h\>

35\#include \<string.h\>

36\#include \<stdlib.h\>

37\#ifdef DBUS_USE_OUTPUT_DEBUG_STRING

38\#include \<windows.h\>

39\#include \<mbstring.h\>

40\#endif

41

182/\* The build system should have checked for DBUS_SIZEOF_VOID_P \*/

183\_DBUS_STATIC_ASSERT (sizeof (void \*) == DBUS_SIZEOF_VOID_P);

184

185/\* dbus currently assumes that function pointers are essentially

186 \* interchangeable with data pointers. There's nothing special about

187 \* DBusShutdownFunction, it's just an arbitrary function pointer type.

188 \* If this assertion fails on your platform, some porting will be required. \*/

189\_DBUS_STATIC_ASSERT (sizeof (void \*) == sizeof (DBusShutdownFunction));

190\_DBUS_STATIC_ASSERT (\_DBUS_ALIGNOF (void \*) == \_DBUS_ALIGNOF (DBusShutdownFunction));

191

192/\* This is meant to be true by definition. \*/

193\_DBUS_STATIC_ASSERT (sizeof (void \*) == sizeof (intptr_t));

194\_DBUS_STATIC_ASSERT (sizeof (void \*) == sizeof (uintptr_t));

195

196/\*

197 \* Some frequent assumptions that we should \*avoid\* making include these,

198 \* all of which are false on CHERI (which has 128-bit tagged pointers,

199 \* but a 64-bit address space and therefore 64-bit sizes):

200 \*

201 \* sizeof (void \*) \<= sizeof (size_t)

202 \* sizeof (void \*) \<= 8

203 \* \_DBUS_ALIGNOF (void \*) \<= 8

204 \*

205 \* We should also avoid making these assumptions, although we don't currently

206 \* know a concrete example of platforms where they're false:

207 \*

208 \* sizeof (ptrdiff_t) == sizeof (size_t)

209 \*/

210

216const char \*\_dbus_no_memory_message = "Not enough memory";

217

218/\* Not necessarily thread-safe, but if writes don't propagate between

219 \* threads, the worst that will happen is that we duplicate work in more than

220 \* one thread. \*/

221static dbus_bool_t warn_initted = FALSE;

222

223/\* Not necessarily thread-safe, but if writes don't propagate between

224 \* threads, the worst that will happen is that warnings get their default

225 \* fatal/non-fatal nature. \*/

226static dbus_bool_t fatal_warnings = FALSE;

227static dbus_bool_t fatal_warnings_on_check_failed = TRUE;

228

229static int check_failed_count = 0;

230

231int \_dbus_get_check_failed_count (void)

232{

233 return check_failed_count;

234}

235

236static void

237init_warnings(void)

238{

239 if (!warn_initted)

240 {

241 const char \*s;

242 s = \_dbus_getenv ("DBUS_FATAL_WARNINGS");

243 if (s && \*s)

244 {

245 if (\*s == '0')

246 {

247 fatal_warnings = FALSE;

248 fatal_warnings_on_check_failed = FALSE;

249 }

250 else if (\*s == '1')

251 {

252 fatal_warnings = TRUE;

253 fatal_warnings_on_check_failed = TRUE;

254 }

255 else

256 {

257 fprintf(stderr, "DBUS_FATAL_WARNINGS should be set to 0 or 1 if set, not '%s'",

258 s);

259 }

260 }

261

262 check_failed_count = 0;

263

264 warn_initted = TRUE;

265 }

266}

267

277void

278\_dbus_warn (const char \*format,

279 ...)

280{

281 DBusSystemLogSeverity severity = DBUS_SYSTEM_LOG_WARNING;

282 va_list args;

283

284 if (!warn_initted)

285 init_warnings ();

286

287 if (fatal_warnings)

288 severity = DBUS_SYSTEM_LOG_ERROR;

289

290 va_start (args, format);

291 \_dbus_logv (severity, format, args);

292 va_end (args);

293

294 if (fatal_warnings)

295 {

296 fflush (stderr);

297 \_dbus_abort ();

298 }

299}

300

309void

310\_dbus_warn_check_failed(const char \*format,

311 ...)

312{

313 DBusSystemLogSeverity severity = DBUS_SYSTEM_LOG_WARNING;

314 va_list args;

315

316 if (!warn_initted)

317 init_warnings ();

318

319 if (fatal_warnings_on_check_failed)

320 severity = DBUS_SYSTEM_LOG_ERROR;

321

322 va_start (args, format);

323 \_dbus_logv (severity, format, args);

324 va_end (args);

325

326 if (fatal_warnings_on_check_failed)

327 {

328 fflush (stderr);

329 \_dbus_abort ();

330 }

331 else

332 check_failed_count++;

333}

334

335\#ifdef DBUS_ENABLE_VERBOSE_MODE

336

337static dbus_bool_t verbose_initted = FALSE;

338static dbus_bool_t verbose = TRUE;

339

340\#ifdef DBUS_USE_OUTPUT_DEBUG_STRING

341static char module_name\[1024\];

342\#endif

343

344static inline void

345\_dbus_verbose_init (void)

346{

347 if (!verbose_initted)

348 {

349 const char \*p = \_dbus_getenv ("DBUS_VERBOSE");

350 verbose = p != NULL && \*p == '1';

351 verbose_initted = TRUE;

352\#ifdef DBUS_USE_OUTPUT_DEBUG_STRING

353 {

354 char \*last_period, \*last_slash;

355 GetModuleFileName(0,module_name,sizeof(module_name)-1);

356 last_period = \_mbsrchr(module_name,'.');

357 if (last_period)

358 \*last_period ='\0';

359 last_slash = \_mbsrchr(module_name,'\\');

360 if (last_slash)

361 strcpy(module_name,last_slash+1);

362 strcat(module_name,": ");

363 }

364\#endif

365 }

366}

367

372static char \*\_dbus_file_path_extract_elements_from_tail(const char \*file,int level)

373{

374 int prefix = 0;

375 char \*p = (char \*)file + strlen(file);

376 int i = 0;

377

378 for (;p \>= file;p--)

379 {

380 if (DBUS_IS_DIR_SEPARATOR(\*p))

381 {

382 if (++i \>= level)

383 {

384 prefix = p-file+1;

385 break;

386 }

387 }

388 }

389

390 return (char \*)file+prefix;

391}

392

398dbus_bool_t

399\_dbus_is_verbose_real (void)

400{

401 \_dbus_verbose_init ();

402 return verbose;

403}

404

405void \_dbus_set_verbose (dbus_bool_t state)

406{

407 verbose = state;

408}

409

410dbus_bool_t \_dbus_get_verbose (void)

411{

412 return verbose;

413}

414

426void

427\_dbus_verbose_raw (const char \*s)

428{

429 if (!\_dbus_is_verbose_real ())

430 return;

431\#ifdef DBUS_USE_OUTPUT_DEBUG_STRING

432 OutputDebugStringA (s);

433\#else

434 fputs (s, stderr);

435 fflush (stderr);

436\#endif

437}

438

447void

448\_dbus_verbose_real (

449\#ifdef DBUS_CPP_SUPPORTS_VARIABLE_MACRO_ARGUMENTS

450 const char \*file,

451 const int line,

452 const char \*function,

453\#endif

454 const char \*format,

455 ...)

456{

457 va_list args;

458 static dbus_bool_t need_pid = TRUE;

459 int len;

460 dbus_int64_t sec;

461 long usec;

462

463 /\* things are written a bit oddly here so that

464 \* in the non-verbose case we just have the one

465 \* conditional and return immediately.

466 \*/

467 if (!\_dbus_is_verbose_real())

468 return;

469

470\#ifndef DBUS_USE_OUTPUT_DEBUG_STRING

471 /\* Print out pid before the line \*/

472 if (need_pid)

473 {

474 \_dbus_print_thread ();

475 }

476 \_dbus_get_real_time (&sec, &usec);

477 fprintf (stderr, "%" DBUS_INT64_MODIFIER "d.%06ld ", sec, usec);

478\#endif

479

480 /\* Only print pid again if the next line is a new line \*/

481 len = strlen (format);

482 if (format\[len-1\] == '\n')

483 need_pid = TRUE;

484 else

485 need_pid = FALSE;

486

487 va_start (args, format);

488

489\#ifdef DBUS_USE_OUTPUT_DEBUG_STRING

490 {

491 DBusString out = \_DBUS_STRING_INIT_INVALID;

492 const char \*message = NULL;

493

494 if (!\_dbus_string_init (&out))

495 goto out;

496

497 if (!\_dbus_string_append (&out, module_name))

498 goto out;

499

500\#ifdef DBUS_CPP_SUPPORTS_VARIABLE_MACRO_ARGUMENTS

501 if (!\_dbus_string_append_printf (&out, "\[%s(%d):%s\] ", \_dbus_file_path_extract_elements_from_tail (file, 2), line, function))

502 goto out;

503\#endif

504 if (!\_dbus_string_append_printf_valist (&out, format, args))

505 goto out;

506 message = \_dbus_string_get_const_data (&out);

507out:

508 if (message == NULL)

509 {

510 OutputDebugStringA ("Out of memory while formatting verbose message: '''");

511 OutputDebugStringA (format);

512 OutputDebugStringA ("'''");

513 }

514 else

515 {

516 OutputDebugStringA (message);

517 }

518 \_dbus_string_free (&out);

519 }

520\#else

521\#ifdef DBUS_CPP_SUPPORTS_VARIABLE_MACRO_ARGUMENTS

522 fprintf (stderr, "\[%s(%d):%s\] ",\_dbus_file_path_extract_elements_from_tail(file,2),line,function);

523\#endif

524

525 vfprintf (stderr, format, args);

526 fflush (stderr);

527\#endif

528

529 va_end (args);

530}

531

538void

539\_dbus_verbose_reset_real (void)

540{

541 verbose_initted = FALSE;

542}

543

544void

545\_dbus_trace_ref (const char \*obj_name,

546 void \*obj,

547 int old_refcount,

548 int new_refcount,

549 const char \*why,

550 const char \*env_var,

551 int \*enabled)

552{

553 \_dbus_assert (obj_name != NULL);

554 \_dbus_assert (obj != NULL);

555 \_dbus_assert (old_refcount \>= -1);

556 \_dbus_assert (new_refcount \>= -1);

557

558 if (old_refcount == -1)

559 {

560 \_dbus_assert (new_refcount == -1);

561 }

562 else

563 {

564 \_dbus_assert (new_refcount \>= 0);

565 \_dbus_assert (old_refcount \>= 0);

566 \_dbus_assert (old_refcount \> 0 \|\| new_refcount \> 0);

567 }

568

569 \_dbus_assert (why != NULL);

570 \_dbus_assert (env_var != NULL);

571 \_dbus_assert (enabled != NULL);

572

573 if (\*enabled \< 0)

574 {

575 const char \*s = \_dbus_getenv (env_var);

576

577 \*enabled = FALSE;

578

579 if (s && \*s)

580 {

581 if (\*s == '0')

582 \*enabled = FALSE;

583 else if (\*s == '1')

584 \*enabled = TRUE;

585 else

586 \_dbus_warn ("%s should be 0 or 1 if set, not '%s'", env_var, s);

587 }

588 }

589

590 if (\*enabled)

591 {

592 if (old_refcount == -1)

593 {

594 VALGRIND_PRINTF_BACKTRACE ("%s %p ref stolen (%s)",

595 obj_name, obj, why);

596 \_dbus_verbose ("%s %p ref stolen (%s)\n",

597 obj_name, obj, why);

598 }

599 else

600 {

601 VALGRIND_PRINTF_BACKTRACE ("%s %p %d -\> %d refs (%s)",

602 obj_name, obj,

603 old_refcount, new_refcount, why);

604 \_dbus_verbose ("%s %p %d -\> %d refs (%s)\n",

605 obj_name, obj, old_refcount, new_refcount, why);

606 }

607 }

608}

609

610\#endif /\* DBUS_ENABLE_VERBOSE_MODE \*/

611

620char\*

621\_dbus_strdup (const char \*str)

622{

623 size_t len;

624 char \*copy;

625

626 if (str == NULL)

627 return NULL;

628

629 len = strlen (str);

630

631 copy = dbus_malloc (len + 1);

632 if (copy == NULL)

633 return NULL;

634

635 memcpy (copy, str, len + 1);

636

637 return copy;

638}

639

648void\*

649\_dbus_memdup (const void \*mem,

650 size_t n_bytes)

651{

652 void \*copy;

653

654 copy = dbus_malloc (n_bytes);

655 if (copy == NULL)

656 return NULL;

657

658 memcpy (copy, mem, n_bytes);

659

660 return copy;

661}

662

671char\*\*

672\_dbus_dup_string_array (const char \*\*array)

673{

674 int len;

675 int i;

676 char \*\*copy;

677

678 if (array == NULL)

679 return NULL;

680

681 for (len = 0; array\[len\] != NULL; ++len)

682 ;

683

684 copy = dbus_new0 (char\*, len + 1);

685 if (copy == NULL)

686 return NULL;

687

688 i = 0;

689 while (i \< len)

690 {

691 copy\[i\] = \_dbus_strdup (array\[i\]);

692 if (copy\[i\] == NULL)

693 {

694 dbus_free_string_array (copy);

695 return NULL;

696 }

697

698 ++i;

699 }

700

701 return copy;

702}

703

711dbus_bool_t

712\_dbus_string_array_contains (const char \*\*array,

713 const char \*str)

714{

715 int i;

716

717 i = 0;

718 while (array\[i\] != NULL)

719 {

720 if (strcmp (array\[i\], str) == 0)

721 return TRUE;

722 ++i;

723 }

724

725 return FALSE;

726}

727

734size_t

735\_dbus_string_array_length (const char \*\*array)

736{

737 size_t i;

738 for (i = 0; array\[i\]; i++) {}

739 return i;

740}

741

742

751dbus_bool_t

752\_dbus_generate_uuid (DBusGUID \*uuid,

753 DBusError \*error)

754{

755 DBusError rand_error;

756 dbus_int64_t now;

757

758 dbus_error_init (&rand_error);

759

760 /\* don't use monotonic time because the UUID may be saved to disk, e.g.

761 \* it may persist across reboots

762 \*/

763 \_dbus_get_real_time (&now, NULL);

764

765 uuid-\>as_uint32s\[DBUS_UUID_LENGTH_WORDS - 1\] = DBUS_UINT32_TO_BE (now);

766

767 if (!\_dbus_generate_random_bytes_buffer (uuid-\>as_bytes,

768 DBUS_UUID_LENGTH_BYTES - 4,

769 &rand_error))

770 {

771 dbus_set_error (error, rand_error.name,

772 "Failed to generate UUID: %s", rand_error.message);

773 dbus_error_free (&rand_error);

774 return FALSE;

775 }

776

777 return TRUE;

778}

779

787dbus_bool_t

788\_dbus_uuid_encode (const DBusGUID \*uuid,

789 DBusString \*encoded)

790{

791 DBusString binary;

792 \_dbus_string_init_const_len (&binary, uuid-\>as_bytes, DBUS_UUID_LENGTH_BYTES);

793 return \_dbus_string_hex_encode (&binary, 0, encoded, \_dbus_string_get_length (encoded));

794}

795

796static dbus_bool_t

797\_dbus_read_uuid_file_without_creating (const DBusString \*filename,

798 DBusGUID \*uuid,

799 DBusError \*error)

800{

801 DBusString contents;

802 DBusString decoded;

803 int end;

804

805 if (!\_dbus_string_init (&contents))

806 {

807 \_DBUS_SET_OOM (error);

808 return FALSE;

809 }

810

811 if (!\_dbus_string_init (&decoded))

812 {

813 \_dbus_string_free (&contents);

814 \_DBUS_SET_OOM (error);

815 return FALSE;

816 }

817

818 if (!\_dbus_file_get_contents (&contents, filename, error))

819 goto error;

820

821 \_dbus_string_chop_white (&contents);

822

823 if (\_dbus_string_get_length (&contents) != DBUS_UUID_LENGTH_HEX)

824 {

825 dbus_set_error (error, DBUS_ERROR_INVALID_FILE_CONTENT,

826 "UUID file '%s' should contain a hex string of length %d, not length %d, with no other text",

827 \_dbus_string_get_const_data (filename),

828 DBUS_UUID_LENGTH_HEX,

829 \_dbus_string_get_length (&contents));

830 goto error;

831 }

832

833 if (!\_dbus_string_hex_decode (&contents, 0, &end, &decoded, 0))

834 {

835 \_DBUS_SET_OOM (error);

836 goto error;

837 }

838

839 if (end == 0)

840 {

841 dbus_set_error (error, DBUS_ERROR_INVALID_FILE_CONTENT,

842 "UUID file '%s' contains invalid hex data",

843 \_dbus_string_get_const_data (filename));

844 goto error;

845 }

846

847 if (\_dbus_string_get_length (&decoded) != DBUS_UUID_LENGTH_BYTES)

848 {

849 dbus_set_error (error, DBUS_ERROR_INVALID_FILE_CONTENT,

850 "UUID file '%s' contains %d bytes of hex-encoded data instead of %d",

851 \_dbus_string_get_const_data (filename),

852 \_dbus_string_get_length (&decoded),

853 DBUS_UUID_LENGTH_BYTES);

854 goto error;

855 }

856

857 \_dbus_string_copy_to_buffer (&decoded, uuid-\>as_bytes, DBUS_UUID_LENGTH_BYTES);

858

859 \_dbus_string_free (&decoded);

860 \_dbus_string_free (&contents);

861

862 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

863

864 return TRUE;

865

866 error:

867 \_DBUS_ASSERT_ERROR_IS_SET (error);

868 \_dbus_string_free (&contents);

869 \_dbus_string_free (&decoded);

870 return FALSE;

871}

872

881dbus_bool_t

882\_dbus_write_uuid_file (const DBusString \*filename,

883 const DBusGUID \*uuid,

884 DBusError \*error)

885{

886 DBusString encoded;

887

888 if (!\_dbus_string_init (&encoded))

889 {

890 \_DBUS_SET_OOM (error);

891 return FALSE;

892 }

893

894 if (!\_dbus_uuid_encode (uuid, &encoded))

895 {

896 \_DBUS_SET_OOM (error);

897 goto error;

898 }

899

900 if (!\_dbus_string_append_byte (&encoded, '\n'))

901 {

902 \_DBUS_SET_OOM (error);

903 goto error;

904 }

905

906 if (!\_dbus_string_save_to_file (&encoded, filename, TRUE, error))

907 goto error;

908

909 \_dbus_string_free (&encoded);

910

911 \_DBUS_ASSERT_ERROR_IS_CLEAR (error);

912 return TRUE;

913

914 error:

915 \_DBUS_ASSERT_ERROR_IS_SET (error);

916 \_dbus_string_free (&encoded);

917 return FALSE;

918}

919

930dbus_bool_t

931\_dbus_read_uuid_file (const DBusString \*filename,

932 DBusGUID \*uuid,

933 dbus_bool_t create_if_not_found,

934 DBusError \*error)

935{

936 DBusError read_error = DBUS_ERROR_INIT;

937

938 if (\_dbus_read_uuid_file_without_creating (filename, uuid, &read_error))

939 return TRUE;

940

941 if (!create_if_not_found)

942 {

943 dbus_move_error (&read_error, error);

944 return FALSE;

945 }

946

947 /\* If the file exists and contains junk, we want to keep that error

948 \* message instead of overwriting it with a "file exists" error

949 \* message when we try to write

950 \*/

951 if (dbus_error_has_name (&read_error, DBUS_ERROR_INVALID_FILE_CONTENT))

952 {

953 dbus_move_error (&read_error, error);

954 return FALSE;

955 }

956 else

957 {

958 dbus_error_free (&read_error);

959

960 if (!\_dbus_generate_uuid (uuid, error))

961 return FALSE;

962

963 return \_dbus_write_uuid_file (filename, uuid, error);

964 }

965}

966

967/\* Protected by \_DBUS_LOCK (machine_uuid) \*/

968static int machine_uuid_initialized_generation = 0;

969static DBusGUID machine_uuid;

970

982dbus_bool_t

983\_dbus_get_local_machine_uuid_encoded (DBusString \*uuid_str,

984 DBusError \*error)

985{

986 dbus_bool_t ok = TRUE;

987

988 if (!\_DBUS_LOCK (machine_uuid))

989 {

990 \_DBUS_SET_OOM (error);

991 return FALSE;

992 }

993

994 if (machine_uuid_initialized_generation != \_dbus_current_generation)

995 {

996 if (!\_dbus_read_local_machine_uuid (&machine_uuid, FALSE, error))

997 ok = FALSE;

998 }

999

1000 if (ok)

1001 {

1002 if (!\_dbus_uuid_encode (&machine_uuid, uuid_str))

1003 {

1004 ok = FALSE;

1005 \_DBUS_SET_OOM (error);

1006 }

1007 }

1008

1009 \_DBUS_UNLOCK (machine_uuid);

1010

1011 return ok;

1012}

1013

1014\#ifndef DBUS_DISABLE_CHECKS

1015void

1016\_dbus_warn_return_if_fail (const char \*function,

1017 const char \*assertion,

1018 const char \*file,

1019 int line)

1020{

1021 \_dbus_warn_check_failed (

1022 "arguments to %s() were incorrect, assertion \\%s\\ failed in file %s line %d.\n"

1023 "This is normally a bug in some application using the D-Bus library.\n",

1024 function, assertion, file, line);

1025}

1026\#endif

1027

1028\#ifndef DBUS_DISABLE_ASSERT

1041void

1042\_dbus_real_assert (dbus_bool_t condition,

1043 const char \*condition_text,

1044 const char \*file,

1045 int line,

1046 const char \*func)

1047{

1048 if (\_DBUS_UNLIKELY (!condition))

1049 {

1050 \_dbus_warn ("assertion failed \\%s\\ file \\%s\\ line %d function %s",

1051 condition_text, file, line, func);

1052 \_dbus_abort ();

1053 }

1054}

1055

1066void

1067\_dbus_real_assert_not_reached (const char \*explanation,

1068 const char \*file,

1069 int line)

1070{

1071 \_dbus_warn ("File \\%s\\ line %d should not have been reached: %s",

1072 file, line, explanation);

1073 \_dbus_abort ();

1074}

1075\#endif /\* DBUS_DISABLE_ASSERT \*/

1076

1077\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

1078static dbus_bool_t

1079run_failing_each_malloc (int n_mallocs,

1080 const char \*description,

1081 DBusTestMemoryFunction func,

1082 void \*data)

1083{

1084 n_mallocs += 10; /\* fudge factor to ensure reallocs etc. are covered \*/

1085

1086 while (n_mallocs \>= 0)

1087 {

1088 \_dbus_set_fail_alloc_counter (n_mallocs);

1089

1090 \_dbus_test_diag ("%s: will fail malloc %d and %d that follow",

1091 description, n_mallocs,

1092 \_dbus_get_fail_alloc_failures () - 1);

1093

1094 if (!(\* func) (data, FALSE))

1095 return FALSE;

1096

1097 n_mallocs -= 1;

1098 }

1099

1100 \_dbus_set_fail_alloc_counter (-1);

1101

1102 return TRUE;

1103}

1104

1118dbus_bool_t

1119\_dbus_test_oom_handling (const char \*description,

1120 DBusTestMemoryFunction func,

1121 void \*data)

1122{

1123 int approx_mallocs;

1124 const char \*setting;

1125 int max_failures_to_try;

1126 int i;

1127

1128 /\* Run once to see about how many mallocs are involved \*/

1129

1130 \_dbus_set_fail_alloc_counter (-1);

1131

1132 \_dbus_test_diag ("Running \\%s\\ once to count mallocs", description);

1133

1134 if (!(\* func) (data, TRUE))

1135 return FALSE;

1136

1137 /\* We have decremented the counter once per allocation, so for example

1138 \* if there were 10 allocations, it will have changed from -1 to -11.

1139 \* Subtract from -1 to get the positive number of allocations that took

1140 \* place. \*/

1141 approx_mallocs = -1 - \_dbus_get_fail_alloc_counter ();

1142

1143 \_dbus_test_diag ("\\%s\\ has about %d mallocs in total",

1144 description, approx_mallocs);

1145

1146 setting = \_dbus_getenv ("DBUS_TEST_MALLOC_FAILURES");

1147

1148 if (setting != NULL)

1149 {

1150 DBusString str;

1151 long v;

1152 \_dbus_string_init_const (&str, setting);

1153 v = 4;

1154 if (!\_dbus_string_parse_int (&str, 0, &v, NULL))

1155 \_dbus_warn ("couldn't parse '%s' as integer\n", setting);

1156 max_failures_to_try = v;

1157 }

1158 else

1159 {

1160 max_failures_to_try = 4;

1161 }

1162

1163 if (RUNNING_ON_VALGRIND && \_dbus_getenv ("DBUS_TEST_SLOW") == NULL)

1164 {

1165 /\* The full OOM testing is slow, valgrind is slow, so the

1166 \* combination is just horrible. Only do this if the user

1167 \* asked for extra-slow tests. \*/

1168 max_failures_to_try = 0;

1169 }

1170

1171 if (max_failures_to_try \< 1)

1172 {

1173 \_dbus_test_diag ("not testing OOM handling");

1174 return TRUE;

1175 }

1176

1177 \_dbus_test_diag ("testing \\%s\\ with up to %d consecutive malloc failures",

1178 description, max_failures_to_try);

1179

1180 i = setting ? max_failures_to_try - 1 : 1;

1181 while (i \< max_failures_to_try)

1182 {

1183 \_dbus_test_diag ("testing \\%s\\ with %d consecutive malloc failures",

1184 description, i + 1);

1185

1186 \_dbus_set_fail_alloc_failures (i);

1187 if (!run_failing_each_malloc (approx_mallocs, description, func, data))

1188 return FALSE;

1189 ++i;

1190 }

1191

1192 \_dbus_verbose ("\\%s\\ coped OK with malloc failures\n", description);

1193

1194 return TRUE;

1195}

1196\#endif /\* DBUS_ENABLE_EMBEDDED_TESTS \*/

1197

DBUS_ERROR_INIT

\#define DBUS_ERROR_INIT

Expands to a suitable initializer for a DBusError on the stack.

**Definition** dbus-errors.h:64

dbus_move_error

void dbus_move_error(DBusError \*src, DBusError \*dest)

Moves an error src into dest, freeing src and overwriting dest.

**Definition** dbus-errors.c:281

dbus_error_has_name

dbus_bool_t dbus_error_has_name(const DBusError \*error, const char \*name)

Checks whether the error is set and has the given name.

**Definition** dbus-errors.c:304

dbus_error_init

void dbus_error_init(DBusError \*error)

Initializes a DBusError structure.

**Definition** dbus-errors.c:190

dbus_set_error

void dbus_set_error(DBusError \*error, const char \*name, const char \*format,...)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:356

dbus_error_free

void dbus_error_free(DBusError \*error)

Frees an error that's been set (or just initialized), then reinitializes the error as in dbus_error_i...

**Definition** dbus-errors.c:213

\_dbus_string_save_to_file

dbus_bool_t \_dbus_string_save_to_file(const DBusString \*str, const DBusString \*filename, dbus_bool_t world_readable, DBusError \*error)

Writes a string out to a file.

**Definition** dbus-file-unix.c:208

\_dbus_file_get_contents

dbus_bool_t \_dbus_file_get_contents(DBusString \*str, const DBusString \*filename, DBusError \*error)

Appends the contents of the given file to the string, returning error code.

**Definition** dbus-file-unix.c:63

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_DBUS_UNLOCK

\#define \_DBUS_UNLOCK(name)

Unlocks a global lock.

**Definition** dbus-internals.h:438

\_DBUS_LOCK

\#define \_DBUS_LOCK(name)

Locks a global lock, initializing it first if necessary.

**Definition** dbus-internals.h:437

\_dbus_real_assert_not_reached

void \_dbus_real_assert_not_reached(const char \*explanation, const char \*file, int line)

Internals of \_dbus_assert_not_reached(); it's a function rather than a macro with the inline code so ...

**Definition** dbus-internals.c:1067

\_dbus_generate_uuid

dbus_bool_t \_dbus_generate_uuid(DBusGUID \*uuid, DBusError \*error)

Generates a new UUID.

**Definition** dbus-internals.c:752

\_dbus_warn_check_failed

void \_dbus_warn_check_failed(const char \*format,...)

Prints a "critical" warning to stderr when an assertion fails; differs from \_dbus_warn primarily in t...

**Definition** dbus-internals.c:310

\_dbus_strdup

char \* \_dbus_strdup(const char \*str)

Duplicates a string.

**Definition** dbus-internals.c:621

\_dbus_read_uuid_file

dbus_bool_t \_dbus_read_uuid_file(const DBusString \*filename, DBusGUID \*uuid, dbus_bool_t create_if_not_found, DBusError \*error)

Reads (and optionally writes) a uuid to a file.

**Definition** dbus-internals.c:931

\_dbus_string_array_contains

dbus_bool_t \_dbus_string_array_contains(const char \*\*array, const char \*str)

Checks whether a string array contains the given string.

**Definition** dbus-internals.c:712

\_dbus_get_local_machine_uuid_encoded

dbus_bool_t \_dbus_get_local_machine_uuid_encoded(DBusString \*uuid_str, DBusError \*error)

Gets the hex-encoded UUID of the machine this function is executed on.

**Definition** dbus-internals.c:983

\_dbus_real_assert

void \_dbus_real_assert(dbus_bool_t condition, const char \*condition_text, const char \*file, int line, const char \*func)

Internals of \_dbus_assert(); it's a function rather than a macro with the inline code so that the ass...

**Definition** dbus-internals.c:1042

\_dbus_write_uuid_file

dbus_bool_t \_dbus_write_uuid_file(const DBusString \*filename, const DBusGUID \*uuid, DBusError \*error)

Write the give UUID to a file.

**Definition** dbus-internals.c:882

\_dbus_warn

void \_dbus_warn(const char \*format,...)

Prints a warning message to stderr.

**Definition** dbus-internals.c:278

\_dbus_string_array_length

size_t \_dbus_string_array_length(const char \*\*array)

Returns the size of a string array.

**Definition** dbus-internals.c:735

\_dbus_no_memory_message

const char \* \_dbus_no_memory_message

Fixed "out of memory" error message, just to avoid making up a different string every time and wastin...

**Definition** dbus-internals.c:216

\_dbus_memdup

void \* \_dbus_memdup(const void \*mem, size_t n_bytes)

Duplicates a block of memory.

**Definition** dbus-internals.c:649

\_dbus_uuid_encode

dbus_bool_t \_dbus_uuid_encode(const DBusGUID \*uuid, DBusString \*encoded)

Hex-encode a UUID.

**Definition** dbus-internals.c:788

\_dbus_dup_string_array

char \*\* \_dbus_dup_string_array(const char \*\*array)

Duplicates a string array.

**Definition** dbus-internals.c:672

\_dbus_generate_random_bytes_buffer

dbus_bool_t \_dbus_generate_random_bytes_buffer(char \*buffer, int n_bytes, DBusError \*error)

Fills n_bytes of the given buffer with random bytes.

**Definition** dbus-sysdeps.c:491

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

\_dbus_current_generation

int \_dbus_current_generation

\_dbus_current_generation is used to track each time that dbus_shutdown() is called,...

**Definition** dbus-memory.c:790

dbus_new0

\#define dbus_new0(type, count)

Safe macro for using dbus_malloc0().

**Definition** dbus-memory.h:60

dbus_free_string_array

void dbus_free_string_array(char \*\*str_array)

Frees a NULL-terminated array of strings.

**Definition** dbus-memory.c:758

dbus_malloc

void \* dbus_malloc(size_t bytes)

Allocates the given number of bytes, as with standard malloc().

**Definition** dbus-memory.c:470

DBUS_ERROR_INVALID_FILE_CONTENT

\#define DBUS_ERROR_INVALID_FILE_CONTENT

A file contains invalid syntax or is otherwise broken.

**Definition** dbus-protocol.h:450

\_dbus_string_hex_decode

dbus_bool_t \_dbus_string_hex_decode(const DBusString \*source, int start, int \*end_return, DBusString \*dest, int insert_at)

Decodes a string from hex encoding.

**Definition** dbus-string.c:2432

\_dbus_string_append

dbus_bool_t \_dbus_string_append(DBusString \*str, const char \*buffer)

Appends a nul-terminated C-style string to a DBusString.

**Definition** dbus-string.c:980

\_dbus_string_init

dbus_bool_t \_dbus_string_init(DBusString \*str)

Initializes a string.

**Definition** dbus-string.c:182

\_dbus_string_init_const

void \_dbus_string_init_const(DBusString \*str, const char \*value)

Initializes a constant string.

**Definition** dbus-string.c:197

\_dbus_string_init_const_len

void \_dbus_string_init_const_len(DBusString \*str, const char \*value, int len)

Initializes a constant string with a length.

**Definition** dbus-string.c:217

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_string_append_printf_valist

dbus_bool_t \_dbus_string_append_printf_valist(DBusString \*str, const char \*format, va_list args)

Appends a printf-style formatted string to the DBusString.

**Definition** dbus-string.c:1105

\_dbus_string_parse_int

DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_string_parse_int(const DBusString \*str, int start, long \*value_return, int \*end_return)

Parses an integer contained in a DBusString.

**Definition** dbus-sysdeps.c:371

\_dbus_string_get_length

int \_dbus_string_get_length(const DBusString \*str)

Gets the length of a string (not including nul termination).

**Definition** dbus-string.c:784

\_dbus_string_append_byte

dbus_bool_t \_dbus_string_append_byte(DBusString \*str, unsigned char byte)

Appends a single byte to the string, returning FALSE if not enough memory.

**Definition** dbus-string.c:1190

\_dbus_string_chop_white

void \_dbus_string_chop_white(DBusString \*str)

Deletes leading and trailing whitespace.

**Definition** dbus-string.c:2051

\_dbus_string_hex_encode

dbus_bool_t \_dbus_string_hex_encode(const DBusString \*source, int start, DBusString \*dest, int insert_at)

Encodes a string in hex, the way MD5 and SHA-1 are usually encoded.

**Definition** dbus-string.c:2382

\_dbus_string_append_printf

dbus_bool_t \_dbus_string_append_printf(DBusString \*str, const char \*format,...)

Appends a printf-style formatted string to the DBusString.

**Definition** dbus-string.c:1147

\_dbus_string_get_const_data

const char \* \_dbus_string_get_const_data(const DBusString \*str)

Gets the raw character buffer from a const string.

**Definition** dbus-string.c:513

\_dbus_string_copy_to_buffer

void \_dbus_string_copy_to_buffer(const DBusString \*str, char \*buffer, int avail_len)

Copies the contents of a DBusString into a different buffer.

**Definition** dbus-string.c:742

\_dbus_logv

void \_dbus_logv(DBusSystemLogSeverity severity, const char \*msg, va_list args)

Log a message to the system log file (e.g.

**Definition** dbus-sysdeps-unix.c:5208

\_dbus_read_local_machine_uuid

dbus_bool_t \_dbus_read_local_machine_uuid(DBusGUID \*machine_id, dbus_bool_t create_if_not_found, DBusError \*error)

Reads the uuid of the machine we're running on from the dbus configuration.

**Definition** dbus-sysdeps-unix.c:4421

\_dbus_getenv

const char \* \_dbus_getenv(const char \*varname)

Wrapper for getenv().

**Definition** dbus-sysdeps.c:197

\_dbus_abort

void \_dbus_abort(void)

Aborts the program with SIGABRT (dumping core).

**Definition** dbus-sysdeps.c:89

\_dbus_get_real_time

void \_dbus_get_real_time(dbus_int64_t \*tv_sec, long \*tv_usec)

Get current time, as in gettimeofday().

**Definition** dbus-sysdeps-unix.c:3412

DBUS_INT64_MODIFIER

\#define DBUS_INT64_MODIFIER

A string literal for a length modifier that is appropriate to print the dbus_int64_t and dbus_uint64\_...

**Definition** dbus-arch-deps.h:39

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusError::name

const char \* name

public error name field

**Definition** dbus-errors.h:52

DBusError::message

const char \* message

public error message field

**Definition** dbus-errors.h:53

DBusString

**Definition** dbus-string.h:47

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
