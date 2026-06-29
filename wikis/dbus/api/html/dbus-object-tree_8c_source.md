dbus-object-tree.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-object-tree.c DBusObjectTree (internals of DBusConnection)

3 \*

4 \* Copyright (C) 2003, 2005 Red Hat Inc.

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

27\#include "dbus-object-tree.h"

28\#include "dbus-connection-internal.h"

29\#include "dbus-internals.h"

30\#include "dbus-hash.h"

31\#include "dbus-protocol.h"

32\#include "dbus-string.h"

33\#include \<dbus/dbus-test-tap.h\>

34\#include \<string.h\>

35\#include \<stdlib.h\>

36

49typedef struct DBusObjectSubtree DBusObjectSubtree;

50

51static DBusObjectSubtree\* \_dbus_object_subtree_new (const char \*name,

52 const DBusObjectPathVTable \*vtable,

53 void \*user_data);

54static DBusObjectSubtree\* \_dbus_object_subtree_ref (DBusObjectSubtree \*subtree);

55static void \_dbus_object_subtree_unref (DBusObjectSubtree \*subtree);

56

60struct DBusObjectTree

61{

62 int refcount;

63 DBusConnection \*connection;

65 DBusObjectSubtree \*root;

66};

67

73struct DBusObjectSubtree

74{

75 DBusAtomic refcount;

76 DBusObjectSubtree \*parent;

77 DBusObjectPathUnregisterFunction unregister_function;

78 DBusObjectPathMessageFunction message_function;

79 void \*user_data;

80 DBusObjectSubtree \*\*subtrees;

81 int n_subtrees;

82 int max_subtrees;

83 unsigned int invoke_as_fallback : 1;

84 char name\[1\];

85};

86

94DBusObjectTree\*

95\_dbus_object_tree_new (DBusConnection \*connection)

96{

97 DBusObjectTree \*tree;

98

99 /\* the connection passed in here isn't fully constructed,

100 \* so don't do anything more than store a pointer to

101 \* it

102 \*/

103

104 tree = dbus_new0 (DBusObjectTree, 1);

105 if (tree == NULL)

106 goto oom;

107

108 tree-\>refcount = 1;

109 tree-\>connection = connection;

110 tree-\>root = \_dbus_object_subtree_new ("/", NULL, NULL);

111 if (tree-\>root == NULL)

112 goto oom;

113 tree-\>root-\>invoke_as_fallback = TRUE;

114

115 return tree;

116

117 oom:

118 if (tree)

119 {

120 dbus_free (tree);

121 }

122

123 return NULL;

124}

125

131DBusObjectTree \*

132\_dbus_object_tree_ref (DBusObjectTree \*tree)

133{

134 \_dbus_assert (tree-\>refcount \> 0);

135

136 tree-\>refcount += 1;

137

138 return tree;

139}

140

145void

146\_dbus_object_tree_unref (DBusObjectTree \*tree)

147{

148 \_dbus_assert (tree-\>refcount \> 0);

149

150 tree-\>refcount -= 1;

151

152 if (tree-\>refcount == 0)

153 {

154 \_dbus_object_tree_free_all_unlocked (tree);

155

156 dbus_free (tree);

157 }

158}

159

163\#define VERBOSE_FIND 0

164

165static DBusObjectSubtree\*

166find_subtree_recurse (DBusObjectSubtree \*subtree,

167 const char \*\*path,

168 dbus_bool_t create_if_not_found,

169 int \*index_in_parent,

170 dbus_bool_t \*exact_match)

171{

172 int i, j;

173 dbus_bool_t return_deepest_match;

174

175 return_deepest_match = exact_match != NULL;

176

177 \_dbus_assert (!(return_deepest_match && create_if_not_found));

178

179 if (path\[0\] == NULL)

180 {

181\#if VERBOSE_FIND

182 \_dbus_verbose (" path exhausted, returning %s\n",

183 subtree-\>name);

184\#endif

185 if (exact_match != NULL)

186 \*exact_match = TRUE;

187 return subtree;

188 }

189

190\#if VERBOSE_FIND

191 \_dbus_verbose (" searching children of %s for %s\n",

192 subtree-\>name, path\[0\]);

193\#endif

194

195 i = 0;

196 j = subtree-\>n_subtrees;

197 while (i \< j)

198 {

199 int k, v;

200

201 k = (i + j) / 2;

202 v = strcmp (path\[0\], subtree-\>subtrees\[k\]-\>name);

203

204\#if VERBOSE_FIND

205 \_dbus_verbose (" %s cmp %s = %d\n",

206 path\[0\], subtree-\>subtrees\[k\]-\>name,

207 v);

208\#endif

209

210 if (v == 0)

211 {

212 if (index_in_parent)

213 {

214\#if VERBOSE_FIND

215 \_dbus_verbose (" storing parent index %d\n", k);

216\#endif

217 \*index_in_parent = k;

218 }

219

220 if (return_deepest_match)

221 {

222 DBusObjectSubtree \*next;

223

224 next = find_subtree_recurse (subtree-\>subtrees\[k\],

225 &path\[1\], create_if_not_found,

226 index_in_parent, exact_match);

227 if (next == NULL &&

228 subtree-\>invoke_as_fallback)

229 {

230\#if VERBOSE_FIND

231 \_dbus_verbose (" no deeper match found, returning %s\n",

232 subtree-\>name);

233\#endif

234 if (exact_match != NULL)

235 \*exact_match = FALSE;

236 return subtree;

237 }

238 else

239 return next;

240 }

241 else

242 return find_subtree_recurse (subtree-\>subtrees\[k\],

243 &path\[1\], create_if_not_found,

244 index_in_parent, exact_match);

245 }

246 else if (v \< 0)

247 {

248 j = k;

249 }

250 else

251 {

252 i = k + 1;

253 }

254 }

255

256\#if VERBOSE_FIND

257 \_dbus_verbose (" no match found, current tree %s, create_if_not_found = %d\n",

258 subtree-\>name, create_if_not_found);

259\#endif

260

261 if (create_if_not_found)

262 {

263 DBusObjectSubtree\* child;

264 int child_pos, new_n_subtrees;

265

266\#if VERBOSE_FIND

267 \_dbus_verbose (" creating subtree %s\n",

268 path\[0\]);

269\#endif

270

271 child = \_dbus_object_subtree_new (path\[0\],

272 NULL, NULL);

273 if (child == NULL)

274 return NULL;

275

276 new_n_subtrees = subtree-\>n_subtrees + 1;

277 if (new_n_subtrees \> subtree-\>max_subtrees)

278 {

279 int new_max_subtrees;

280 DBusObjectSubtree \*\*new_subtrees;

281

282 new_max_subtrees = subtree-\>max_subtrees == 0 ? 1 : 2 \* subtree-\>max_subtrees;

283 new_subtrees = dbus_realloc (subtree-\>subtrees,

284 new_max_subtrees \* sizeof (DBusObjectSubtree\*));

285 if (new_subtrees == NULL)

286 {

287 \_dbus_object_subtree_unref (child);

288 return NULL;

289 }

290 subtree-\>subtrees = new_subtrees;

291 subtree-\>max_subtrees = new_max_subtrees;

292 }

293

294 /\* The binary search failed, so i == j points to the

295 place the child should be inserted. \*/

296 child_pos = i;

297 \_dbus_assert (child_pos \< new_n_subtrees &&

298 new_n_subtrees \<= subtree-\>max_subtrees);

299 if (child_pos + 1 \< new_n_subtrees)

300 {

301 memmove (&subtree-\>subtrees\[child_pos+1\],

302 &subtree-\>subtrees\[child_pos\],

303 (new_n_subtrees - child_pos - 1) \*

304 sizeof subtree-\>subtrees\[0\]);

305 }

306 subtree-\>subtrees\[child_pos\] = child;

307

308 if (index_in_parent)

309 \*index_in_parent = child_pos;

310 subtree-\>n_subtrees = new_n_subtrees;

311 child-\>parent = subtree;

312

313 return find_subtree_recurse (child,

314 &path\[1\], create_if_not_found,

315 index_in_parent, exact_match);

316 }

317 else

318 {

319 if (exact_match != NULL)

320 \*exact_match = FALSE;

321 return (return_deepest_match && subtree-\>invoke_as_fallback) ? subtree : NULL;

322 }

323}

324

325\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

326static DBusObjectSubtree\*

327find_subtree (DBusObjectTree \*tree,

328 const char \*\*path,

329 int \*index_in_parent)

330{

331 DBusObjectSubtree \*subtree;

332

333\#if VERBOSE_FIND

334 \_dbus_verbose ("Looking for exact registered subtree\n");

335\#endif

336

337 subtree = find_subtree_recurse (tree-\>root, path, FALSE, index_in_parent, NULL);

338

339 if (subtree && subtree-\>message_function == NULL)

340 return NULL;

341 else

342 return subtree;

343}

344\#endif

345

346static DBusObjectSubtree\*

347lookup_subtree (DBusObjectTree \*tree,

348 const char \*\*path)

349{

350\#if VERBOSE_FIND

351 \_dbus_verbose ("Looking for subtree\n");

352\#endif

353 return find_subtree_recurse (tree-\>root, path, FALSE, NULL, NULL);

354}

355

356static DBusObjectSubtree\*

357find_handler (DBusObjectTree \*tree,

358 const char \*\*path,

359 dbus_bool_t \*exact_match)

360{

361\#if VERBOSE_FIND

362 \_dbus_verbose ("Looking for deepest handler\n");

363\#endif

364 \_dbus_assert (exact_match != NULL);

365

366 \*exact_match = FALSE; /\* ensure always initialized \*/

367

368 return find_subtree_recurse (tree-\>root, path, FALSE, NULL, exact_match);

369}

370

371static DBusObjectSubtree\*

372ensure_subtree (DBusObjectTree \*tree,

373 const char \*\*path)

374{

375\#if VERBOSE_FIND

376 \_dbus_verbose ("Ensuring subtree\n");

377\#endif

378 return find_subtree_recurse (tree-\>root, path, TRUE, NULL, NULL);

379}

380

381static char \*flatten_path (const char \*\*path);

382

395dbus_bool_t

396\_dbus_object_tree_register (DBusObjectTree \*tree,

397 dbus_bool_t fallback,

398 const char \*\*path,

399 const DBusObjectPathVTable \*vtable,

400 void \*user_data,

401 DBusError \*error)

402{

403 DBusObjectSubtree \*subtree;

404

405 \_dbus_assert (tree != NULL);

406 \_dbus_assert (vtable-\>message_function != NULL);

407 \_dbus_assert (path != NULL);

408

409 subtree = ensure_subtree (tree, path);

410 if (subtree == NULL)

411 {

412 \_DBUS_SET_OOM (error);

413 return FALSE;

414 }

415

416 if (subtree-\>message_function != NULL)

417 {

418 if (error != NULL)

419 {

420 char \*complete_path = flatten_path (path);

421

422 dbus_set_error (error, DBUS_ERROR_OBJECT_PATH_IN_USE,

423 "A handler is already registered for %s",

424 complete_path ? complete_path

425 : "(cannot represent path: out of memory!)");

426

427 dbus_free (complete_path);

428 }

429

430 return FALSE;

431 }

432

433 subtree-\>message_function = vtable-\>message_function;

434 subtree-\>unregister_function = vtable-\>unregister_function;

435 subtree-\>user_data = user_data;

436 subtree-\>invoke_as_fallback = fallback != FALSE;

437

438 return TRUE;

439}

440

452static dbus_bool_t

453unregister_subtree (DBusObjectSubtree \*subtree,

454 DBusObjectPathUnregisterFunction \*unregister_function_out,

455 void \*\*user_data_out)

456{

457 \_dbus_assert (subtree != NULL);

458 \_dbus_assert (unregister_function_out != NULL);

459 \_dbus_assert (user_data_out != NULL);

460

461 /\* Confirm subtree is registered \*/

462 if (subtree-\>message_function != NULL)

463 {

464 subtree-\>message_function = NULL;

465

466 \*unregister_function_out = subtree-\>unregister_function;

467 \*user_data_out = subtree-\>user_data;

468

469 subtree-\>unregister_function = NULL;

470 subtree-\>user_data = NULL;

471

472 return TRUE;

473 }

474 else

475 {

476 /\* Assert that this unregistered subtree is either the root node or has

477 children, otherwise we have a dangling path which should never

478 happen \*/

479 \_dbus_assert (subtree-\>parent == NULL \|\| subtree-\>n_subtrees \> 0);

480

481 /\* The subtree is not registered \*/

482 return FALSE;

483 }

484}

485

497static dbus_bool_t

498attempt_child_removal (DBusObjectSubtree \*parent,

499 int child_index)

500{

501 /\* Candidate for removal \*/

502 DBusObjectSubtree\* candidate;

503

504 \_dbus_assert (parent != NULL);

505 \_dbus_assert (child_index \>= 0 && child_index \< parent-\>n_subtrees);

506

507 candidate = parent-\>subtrees\[child_index\];

508 \_dbus_assert (candidate != NULL);

509

510 if (candidate-\>n_subtrees == 0 && candidate-\>message_function == NULL)

511 {

512 /\* The candidate node is childless and is not a registered

513 path, so... \*/

514

515 /\* ... remove it from its parent... \*/

516 /\* Assumes a 0-byte memmove is OK \*/

517 memmove (&parent-\>subtrees\[child_index\],

518 &parent-\>subtrees\[child_index + 1\],

519 (parent-\>n_subtrees - child_index - 1)

520 \* sizeof (parent-\>subtrees\[0\]));

521 parent-\>n_subtrees -= 1;

522

523 /\* ... and free it \*/

524 candidate-\>parent = NULL;

525 \_dbus_object_subtree_unref (candidate);

526

527 return TRUE;

528 }

529 return FALSE;

530}

531

569static dbus_bool_t

570unregister_and_free_path_recurse

571(DBusObjectSubtree \*subtree,

572 const char \*\*path,

573 dbus_bool_t \*continue_removal_attempts,

574 DBusObjectPathUnregisterFunction \*unregister_function_out,

575 void \*\*user_data_out)

576{

577 int i, j;

578

579 \_dbus_assert (continue_removal_attempts != NULL);

580 \_dbus_assert (\*continue_removal_attempts);

581 \_dbus_assert (unregister_function_out != NULL);

582 \_dbus_assert (user_data_out != NULL);

583

584 if (path\[0\] == NULL)

585 return unregister_subtree (subtree, unregister_function_out, user_data_out);

586

587 i = 0;

588 j = subtree-\>n_subtrees;

589 while (i \< j)

590 {

591 int k, v;

592

593 k = (i + j) / 2;

594 v = strcmp (path\[0\], subtree-\>subtrees\[k\]-\>name);

595

596 if (v == 0)

597 {

598 dbus_bool_t freed;

599 freed = unregister_and_free_path_recurse (subtree-\>subtrees\[k\],

600 &path\[1\],

601 continue_removal_attempts,

602 unregister_function_out,

603 user_data_out);

604 if (freed && \*continue_removal_attempts)

605 \*continue_removal_attempts = attempt_child_removal (subtree, k);

606 return freed;

607 }

608 else if (v \< 0)

609 {

610 j = k;

611 }

612 else

613 {

614 i = k + 1;

615 }

616 }

617 return FALSE;

618}

619

627void

628\_dbus_object_tree_unregister_and_unlock (DBusObjectTree \*tree,

629 const char \*\*path)

630{

631 dbus_bool_t found_subtree;

632 dbus_bool_t continue_removal_attempts;

633 DBusObjectPathUnregisterFunction unregister_function;

634 void \*user_data;

635 DBusConnection \*connection;

636

637 \_dbus_assert (tree != NULL);

638 \_dbus_assert (path != NULL);

639

640 continue_removal_attempts = TRUE;

641 unregister_function = NULL;

642 user_data = NULL;

643

644 found_subtree = unregister_and_free_path_recurse (tree-\>root,

645 path,

646 &continue_removal_attempts,

647 &unregister_function,

648 &user_data);

649

650\#ifndef DBUS_DISABLE_CHECKS

651 if (found_subtree == FALSE)

652 {

653 \_dbus_warn ("Attempted to unregister path (path\[0\] = %s path\[1\] = %s) which isn't registered",

654 path\[0\] ? path\[0\] : "null",

655 (path\[0\] && path\[1\]) ? path\[1\] : "null");

656 goto unlock;

657 }

658\#else

659 \_dbus_assert (found_subtree == TRUE);

660\#endif

661

662unlock:

663 connection = tree-\>connection;

664

665 /\* Unlock and call application code \*/

666\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

667 if (connection)

668\#endif

669 {

670 \_dbus_connection_ref_unlocked (connection);

671 \_dbus_verbose ("unlock\n");

672 \_dbus_connection_unlock (connection);

673 }

674

675 if (unregister_function)

676 (\* unregister_function) (connection, user_data);

677

678\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

679 if (connection)

680\#endif

681 dbus_connection_unref (connection);

682}

683

684static void

685free_subtree_recurse (DBusConnection \*connection,

686 DBusObjectSubtree \*subtree)

687{

688 /\* Delete them from the end, for slightly

689 \* more robustness against odd reentrancy.

690 \*/

691 while (subtree-\>n_subtrees \> 0)

692 {

693 DBusObjectSubtree \*child;

694

695 child = subtree-\>subtrees\[subtree-\>n_subtrees - 1\];

696 subtree-\>subtrees\[subtree-\>n_subtrees - 1\] = NULL;

697 subtree-\>n_subtrees -= 1;

698 child-\>parent = NULL;

699

700 free_subtree_recurse (connection, child);

701 }

702

703 /\* Call application code \*/

704 if (subtree-\>unregister_function)

705 (\* subtree-\>unregister_function) (connection,

706 subtree-\>user_data);

707

708 subtree-\>message_function = NULL;

709 subtree-\>unregister_function = NULL;

710 subtree-\>user_data = NULL;

711

712 /\* Now free ourselves \*/

713 \_dbus_object_subtree_unref (subtree);

714}

715

722void

723\_dbus_object_tree_free_all_unlocked (DBusObjectTree \*tree)

724{

725 if (tree-\>root)

726 free_subtree_recurse (tree-\>connection,

727 tree-\>root);

728 tree-\>root = NULL;

729}

730

731static dbus_bool_t

732\_dbus_object_tree_list_registered_unlocked (DBusObjectTree \*tree,

733 const char \*\*parent_path,

734 char \*\*\*child_entries)

735{

736 DBusObjectSubtree \*subtree;

737 char \*\*retval;

738

739 \_dbus_assert (parent_path != NULL);

740 \_dbus_assert (child_entries != NULL);

741

742 \*child_entries = NULL;

743

744 subtree = lookup_subtree (tree, parent_path);

745 if (subtree == NULL)

746 {

747 retval = dbus_new0 (char \*, 1);

748 }

749 else

750 {

751 int i;

752 retval = dbus_new0 (char\*, subtree-\>n_subtrees + 1);

753 if (retval == NULL)

754 goto out;

755 i = 0;

756 while (i \< subtree-\>n_subtrees)

757 {

758 retval\[i\] = \_dbus_strdup (subtree-\>subtrees\[i\]-\>name);

759 if (retval\[i\] == NULL)

760 {

761 dbus_free_string_array (retval);

762 retval = NULL;

763 goto out;

764 }

765 ++i;

766 }

767 }

768

769 out:

770

771 \*child_entries = retval;

772 return retval != NULL;

773}

774

775static DBusHandlerResult

776handle_default_introspect_and_unlock (DBusObjectTree \*tree,

777 DBusMessage \*message,

778 const char \*\*path)

779{

780 DBusString xml;

781 DBusHandlerResult result;

782 char \*\*children;

783 int i;

784 DBusMessage \*reply;

785 DBusMessageIter iter;

786 const char \*v_STRING;

787 dbus_bool_t already_unlocked;

788

789 /\* We have the connection lock here \*/

790

791 already_unlocked = FALSE;

792

793 \_dbus_verbose (" considering default Introspect() handler...\n");

794

795 reply = NULL;

796

797 if (!dbus_message_is_method_call (message,

798 DBUS_INTERFACE_INTROSPECTABLE,

799 "Introspect"))

800 {

801\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

802 if (tree-\>connection)

803\#endif

804 {

805 \_dbus_verbose ("unlock\n");

806 \_dbus_connection_unlock (tree-\>connection);

807 }

808

809 return DBUS_HANDLER_RESULT_NOT_YET_HANDLED;

810 }

811

812 \_dbus_verbose (" using default Introspect() handler!\n");

813

814 if (!\_dbus_string_init (&xml))

815 {

816\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

817 if (tree-\>connection)

818\#endif

819 {

820 \_dbus_verbose ("unlock\n");

821 \_dbus_connection_unlock (tree-\>connection);

822 }

823

824 return DBUS_HANDLER_RESULT_NEED_MEMORY;

825 }

826

827 result = DBUS_HANDLER_RESULT_NEED_MEMORY;

828

829 children = NULL;

830 if (!\_dbus_object_tree_list_registered_unlocked (tree, path, &children))

831 goto out;

832

833 if (!\_dbus_string_append (&xml, DBUS_INTROSPECT_1_0_XML_DOCTYPE_DECL_NODE))

834 goto out;

835

836 if (!\_dbus_string_append (&xml, "\<node\>\n"))

837 goto out;

838

839 i = 0;

840 while (children\[i\] != NULL)

841 {

842 if (!\_dbus_string_append_printf (&xml, " \<node name=\\%s\\/\>\n",

843 children\[i\]))

844 goto out;

845

846 ++i;

847 }

848

849 if (!\_dbus_string_append (&xml, "\</node\>\n"))

850 goto out;

851

852 reply = dbus_message_new_method_return (message);

853 if (reply == NULL)

854 goto out;

855

856 dbus_message_iter_init_append (reply, &iter);

857 v_STRING = \_dbus_string_get_const_data (&xml);

858 if (!dbus_message_iter_append_basic (&iter, DBUS_TYPE_STRING, &v_STRING))

859 goto out;

860

861\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

862 if (tree-\>connection)

863\#endif

864 {

865 already_unlocked = TRUE;

866

867 if (!\_dbus_connection_send_and_unlock (tree-\>connection, reply, NULL))

868 goto out;

869 }

870

871 result = DBUS_HANDLER_RESULT_HANDLED;

872

873 out:

874\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

875 if (tree-\>connection)

876\#endif

877 {

878 if (!already_unlocked)

879 {

880 \_dbus_verbose ("unlock\n");

881 \_dbus_connection_unlock (tree-\>connection);

882 }

883 }

884

885 \_dbus_string_free (&xml);

886 dbus_free_string_array (children);

887 if (reply)

888 dbus_message_unref (reply);

889

890 return result;

891}

892

907DBusHandlerResult

908\_dbus_object_tree_dispatch_and_unlock (DBusObjectTree \*tree,

909 DBusMessage \*message,

910 dbus_bool_t \*found_object)

911{

912 char \*\*path;

913 dbus_bool_t exact_match;

914 DBusList \*list;

915 DBusList \*link;

916 DBusHandlerResult result;

917 DBusObjectSubtree \*subtree;

918

919\#if 0

920 \_dbus_verbose ("Dispatch of message by object path\n");

921\#endif

922

923 path = NULL;

924 if (!dbus_message_get_path_decomposed (message, &path))

925 {

926\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

927 if (tree-\>connection)

928\#endif

929 {

930 \_dbus_verbose ("unlock\n");

931 \_dbus_connection_unlock (tree-\>connection);

932 }

933

934 \_dbus_verbose ("No memory to get decomposed path\n");

935

936 return DBUS_HANDLER_RESULT_NEED_MEMORY;

937 }

938

939 if (path == NULL)

940 {

941\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

942 if (tree-\>connection)

943\#endif

944 {

945 \_dbus_verbose ("unlock\n");

946 \_dbus_connection_unlock (tree-\>connection);

947 }

948

949 \_dbus_verbose ("No path field in message\n");

950 return DBUS_HANDLER_RESULT_NOT_YET_HANDLED;

951 }

952

953 /\* Find the deepest path that covers the path in the message \*/

954 subtree = find_handler (tree, (const char\*\*) path, &exact_match);

955

956 if (found_object)

957 \*found_object = !!subtree;

958

959 /\* Build a list of all paths that cover the path in the message \*/

960

961 list = NULL;

962

963 while (subtree != NULL)

964 {

965 if (subtree-\>message_function != NULL && (exact_match \|\| subtree-\>invoke_as_fallback))

966 {

967 \_dbus_object_subtree_ref (subtree);

968

969 /\* run deepest paths first \*/

970 if (!\_dbus_list_append (&list, subtree))

971 {

972 result = DBUS_HANDLER_RESULT_NEED_MEMORY;

973 \_dbus_object_subtree_unref (subtree);

974 goto free_and_return;

975 }

976 }

977

978 exact_match = FALSE;

979 subtree = subtree-\>parent;

980 }

981

982 \_dbus_verbose ("%d handlers in the path tree for this message\n",

983 \_dbus_list_get_length (&list));

984

985 /\* Invoke each handler in the list \*/

986

987 result = DBUS_HANDLER_RESULT_NOT_YET_HANDLED;

988

989 link = \_dbus_list_get_first_link (&list);

990 while (link != NULL)

991 {

992 DBusList \*next = \_dbus_list_get_next_link (&list, link);

993 subtree = link-\>data;

994

995 /\* message_function is NULL if we're unregistered

996 \* due to reentrancy

997 \*/

998 if (subtree-\>message_function)

999 {

1000 DBusObjectPathMessageFunction message_function;

1001 void \*user_data;

1002

1003 message_function = subtree-\>message_function;

1004 user_data = subtree-\>user_data;

1005

1006\#if 0

1007 \_dbus_verbose (" (invoking a handler)\n");

1008\#endif

1009

1010\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

1011 if (tree-\>connection)

1012\#endif

1013 {

1014 \_dbus_verbose ("unlock\n");

1015 \_dbus_connection_unlock (tree-\>connection);

1016 }

1017

1018 /\* FIXME you could unregister the subtree in another thread

1019 \* before we invoke the callback, and I can't figure out a

1020 \* good way to solve this.

1021 \*/

1022

1023 result = (\* message_function) (tree-\>connection,

1024 message,

1025 user_data);

1026

1027\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

1028 if (tree-\>connection)

1029\#endif

1030 \_dbus_connection_lock (tree-\>connection);

1031

1032 if (result != DBUS_HANDLER_RESULT_NOT_YET_HANDLED)

1033 goto free_and_return;

1034 }

1035

1036 link = next;

1037 }

1038

1039 free_and_return:

1040

1041 if (result == DBUS_HANDLER_RESULT_NOT_YET_HANDLED)

1042 {

1043 /\* This hardcoded default handler does a minimal Introspect()

1044 \*/

1045 result = handle_default_introspect_and_unlock (tree, message,

1046 (const char\*\*) path);

1047 }

1048 else

1049 {

1050\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

1051 if (tree-\>connection)

1052\#endif

1053 {

1054 \_dbus_verbose ("unlock\n");

1055 \_dbus_connection_unlock (tree-\>connection);

1056 }

1057 }

1058

1059 while (list != NULL)

1060 {

1061 link = \_dbus_list_get_first_link (&list);

1062 \_dbus_object_subtree_unref (link-\>data);

1063 \_dbus_list_remove_link (&list, link);

1064 }

1065

1066 dbus_free_string_array (path);

1067

1068 return result;

1069}

1070

1079void\*

1080\_dbus_object_tree_get_user_data_unlocked (DBusObjectTree \*tree,

1081 const char \*\*path)

1082{

1083 dbus_bool_t exact_match;

1084 DBusObjectSubtree \*subtree;

1085

1086 \_dbus_assert (tree != NULL);

1087 \_dbus_assert (path != NULL);

1088

1089 /\* Find the deepest path that covers the path in the message \*/

1090 subtree = find_handler (tree, (const char\*\*) path, &exact_match);

1091

1092 if ((subtree == NULL) \|\| !exact_match)

1093 {

1094 \_dbus_verbose ("No object at specified path found\n");

1095 return NULL;

1096 }

1097

1098 return subtree-\>user_data;

1099}

1100

1107static DBusObjectSubtree\*

1108allocate_subtree_object (const char \*name)

1109{

1110 int len;

1111 DBusObjectSubtree \*subtree;

1112 const size_t front_padding = \_DBUS_STRUCT_OFFSET (DBusObjectSubtree, name);

1113

1114 \_dbus_assert (name != NULL);

1115

1116 len = strlen (name);

1117

1118 subtree = dbus_malloc0 (MAX (front_padding + (len + 1), sizeof (DBusObjectSubtree)));

1119

1120 if (subtree == NULL)

1121 return NULL;

1122

1123 memcpy (subtree-\>name, name, len + 1);

1124

1125 return subtree;

1126}

1127

1128static DBusObjectSubtree\*

1129\_dbus_object_subtree_new (const char \*name,

1130 const DBusObjectPathVTable \*vtable,

1131 void \*user_data)

1132{

1133 DBusObjectSubtree \*subtree;

1134

1135 subtree = allocate_subtree_object (name);

1136 if (subtree == NULL)

1137 goto oom;

1138

1139 \_dbus_assert (name != NULL);

1140

1141 subtree-\>parent = NULL;

1142

1143 if (vtable)

1144 {

1145 subtree-\>message_function = vtable-\>message_function;

1146 subtree-\>unregister_function = vtable-\>unregister_function;

1147 }

1148 else

1149 {

1150 subtree-\>message_function = NULL;

1151 subtree-\>unregister_function = NULL;

1152 }

1153

1154 subtree-\>user_data = user_data;

1155 \_dbus_atomic_inc (&subtree-\>refcount);

1156 subtree-\>subtrees = NULL;

1157 subtree-\>n_subtrees = 0;

1158 subtree-\>max_subtrees = 0;

1159 subtree-\>invoke_as_fallback = FALSE;

1160

1161 return subtree;

1162

1163 oom:

1164 return NULL;

1165}

1166

1167static DBusObjectSubtree \*

1168\_dbus_object_subtree_ref (DBusObjectSubtree \*subtree)

1169{

1170\#ifdef DBUS_DISABLE_ASSERT

1171 \_dbus_atomic_inc (&subtree-\>refcount);

1172\#else

1173 dbus_int32_t old_value;

1174

1175 old_value = \_dbus_atomic_inc (&subtree-\>refcount);

1176 \_dbus_assert (old_value \> 0);

1177\#endif

1178

1179 return subtree;

1180}

1181

1182static void

1183\_dbus_object_subtree_unref (DBusObjectSubtree \*subtree)

1184{

1185 dbus_int32_t old_value;

1186

1187 old_value = \_dbus_atomic_dec (&subtree-\>refcount);

1188 \_dbus_assert (old_value \> 0);

1189

1190 if (old_value == 1)

1191 {

1192 \_dbus_assert (subtree-\>unregister_function == NULL);

1193 \_dbus_assert (subtree-\>message_function == NULL);

1194

1195 dbus_free (subtree-\>subtrees);

1196 dbus_free (subtree);

1197 }

1198}

1199

1210dbus_bool_t

1211\_dbus_object_tree_list_registered_and_unlock (DBusObjectTree \*tree,

1212 const char \*\*parent_path,

1213 char \*\*\*child_entries)

1214{

1215 dbus_bool_t result;

1216

1217 result = \_dbus_object_tree_list_registered_unlocked (tree,

1218 parent_path,

1219 child_entries);

1220

1221\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

1222 if (tree-\>connection)

1223\#endif

1224 {

1225 \_dbus_verbose ("unlock\n");

1226 \_dbus_connection_unlock (tree-\>connection);

1227 }

1228

1229 return result;

1230}

1231

1232

1234\#define VERBOSE_DECOMPOSE 0

1235

1246dbus_bool_t

1247\_dbus_decompose_path (const char\* data,

1248 int len,

1249 char \*\*\*path,

1250 int \*path_len)

1251{

1252 char \*\*retval;

1253 int n_components;

1254 int i, j, comp;

1255

1256 \_dbus_assert (data != NULL);

1257 \_dbus_assert (path != NULL);

1258

1259\#if VERBOSE_DECOMPOSE

1260 \_dbus_verbose ("Decomposing path \\%s\\\n",

1261 data);

1262\#endif

1263

1264 n_components = 0;

1265 if (len \> 1) /\* if path is not just "/" \*/

1266 {

1267 i = 0;

1268 while (i \< len)

1269 {

1270 \_dbus_assert (data\[i\] != '\0');

1271 if (data\[i\] == '/')

1272 n_components += 1;

1273 ++i;

1274 }

1275 }

1276

1277 retval = dbus_new0 (char\*, n_components + 1);

1278

1279 if (retval == NULL)

1280 return FALSE;

1281

1282 comp = 0;

1283 if (n_components == 0)

1284 i = 1;

1285 else

1286 i = 0;

1287 while (comp \< n_components)

1288 {

1289 \_dbus_assert (i \< len);

1290

1291 if (data\[i\] == '/')

1292 ++i;

1293 j = i;

1294

1295 while (j \< len && data\[j\] != '/')

1296 ++j;

1297

1298 /\* Now \[i, j) is the path component \*/

1299 \_dbus_assert (i \< j);

1300 \_dbus_assert (data\[i\] != '/');

1301 \_dbus_assert (j == len \|\| data\[j\] == '/');

1302

1303\#if VERBOSE_DECOMPOSE

1304 \_dbus_verbose (" (component in \[%d,%d))\n",

1305 i, j);

1306\#endif

1307

1308 retval\[comp\] = \_dbus_memdup (&data\[i\], j - i + 1);

1309 if (retval\[comp\] == NULL)

1310 {

1311 dbus_free_string_array (retval);

1312 return FALSE;

1313 }

1314 retval\[comp\]\[j-i\] = '\0';

1315\#if VERBOSE_DECOMPOSE

1316 \_dbus_verbose (" (component %d = \\%s\\)\n",

1317 comp, retval\[comp\]);

1318\#endif

1319

1320 ++comp;

1321 i = j;

1322 }

1323 \_dbus_assert (i == len);

1324

1325 \*path = retval;

1326 if (path_len)

1327 \*path_len = n_components;

1328

1329 return TRUE;

1330}

1331

1334static char\*

1335flatten_path (const char \*\*path)

1336{

1337 DBusString str;

1338 char \*s;

1339

1340 if (!\_dbus_string_init (&str))

1341 return NULL;

1342

1343 if (path\[0\] == NULL)

1344 {

1345 if (!\_dbus_string_append_byte (&str, '/'))

1346 goto nomem;

1347 }

1348 else

1349 {

1350 int i;

1351

1352 i = 0;

1353 while (path\[i\])

1354 {

1355 if (!\_dbus_string_append_byte (&str, '/'))

1356 goto nomem;

1357

1358 if (!\_dbus_string_append (&str, path\[i\]))

1359 goto nomem;

1360

1361 ++i;

1362 }

1363 }

1364

1365 if (!\_dbus_string_steal_data (&str, &s))

1366 goto nomem;

1367

1368 \_dbus_string_free (&str);

1369

1370 return s;

1371

1372 nomem:

1373 \_dbus_string_free (&str);

1374 return NULL;

1375}

1376

1377

1378\#ifdef DBUS_ENABLE_EMBEDDED_TESTS

1379

1380\#ifndef DOXYGEN_SHOULD_SKIP_THIS

1381

1382\#include "dbus-test.h"

1383\#include \<stdio.h\>

1384

1385typedef enum

1386{

1387 STR_EQUAL,

1388 STR_PREFIX,

1389 STR_DIFFERENT

1390} StrComparison;

1391

1392/\* Returns TRUE if container is a parent of child

1393 \*/

1394static StrComparison

1395path_contains (const char \*\*container,

1396 const char \*\*child)

1397{

1398 int i;

1399

1400 i = 0;

1401 while (child\[i\] != NULL)

1402 {

1403 int v;

1404

1405 if (container\[i\] == NULL)

1406 return STR_PREFIX; /\* container ran out, child continues;

1407 \* thus the container is a parent of the

1408 \* child.

1409 \*/

1410

1411 \_dbus_assert (container\[i\] != NULL);

1412 \_dbus_assert (child\[i\] != NULL);

1413

1414 v = strcmp (container\[i\], child\[i\]);

1415

1416 if (v != 0)

1417 return STR_DIFFERENT; /\* they overlap until here and then are different,

1418 \* not overlapping

1419 \*/

1420

1421 ++i;

1422 }

1423

1424 /\* Child ran out; if container also did, they are equal;

1425 \* otherwise, the child is a parent of the container.

1426 \*/

1427 if (container\[i\] == NULL)

1428 return STR_EQUAL;

1429 else

1430 return STR_DIFFERENT;

1431}

1432

1433\#if 0

1434static void

1435spew_subtree_recurse (DBusObjectSubtree \*subtree,

1436 int indent)

1437{

1438 int i;

1439

1440 i = 0;

1441 while (i \< indent)

1442 {

1443 \_dbus_verbose (" ");

1444 ++i;

1445 }

1446

1447 \_dbus_verbose ("%s (%d children)\n",

1448 subtree-\>name, subtree-\>n_subtrees);

1449

1450 i = 0;

1451 while (i \< subtree-\>n_subtrees)

1452 {

1453 spew_subtree_recurse (subtree-\>subtrees\[i\], indent + 2);

1454

1455 ++i;

1456 }

1457}

1458

1459static void

1460spew_tree (DBusObjectTree \*tree)

1461{

1462 spew_subtree_recurse (tree-\>root, 0);

1463}

1464\#endif

1465

1469typedef struct

1470{

1471 const char \*\*path;

1472 dbus_bool_t handler_fallback;

1473 dbus_bool_t message_handled;

1474 dbus_bool_t handler_unregistered;

1475} TreeTestData;

1476

1477

1478static void

1479test_unregister_function (DBusConnection \*connection,

1480 void \*user_data)

1481{

1482 TreeTestData \*ttd = user_data;

1483

1484 ttd-\>handler_unregistered = TRUE;

1485}

1486

1487static DBusHandlerResult

1488test_message_function (DBusConnection \*connection,

1489 DBusMessage \*message,

1490 void \*user_data)

1491{

1492 TreeTestData \*ttd = user_data;

1493

1494 ttd-\>message_handled = TRUE;

1495

1496 return DBUS_HANDLER_RESULT_NOT_YET_HANDLED;

1497}

1498

1499static dbus_bool_t

1500do_register (DBusObjectTree \*tree,

1501 const char \*\*path,

1502 dbus_bool_t fallback,

1503 int i,

1504 TreeTestData \*tree_test_data)

1505{

1506 DBusObjectPathVTable vtable = { test_unregister_function,

1507 test_message_function, NULL };

1508

1509 tree_test_data\[i\].message_handled = FALSE;

1510 tree_test_data\[i\].handler_unregistered = FALSE;

1511 tree_test_data\[i\].handler_fallback = fallback;

1512 tree_test_data\[i\].path = path;

1513

1514 if (!\_dbus_object_tree_register (tree, fallback, path,

1515 &vtable,

1516 &tree_test_data\[i\],

1517 NULL))

1518 return FALSE;

1519

1520 \_dbus_assert (\_dbus_object_tree_get_user_data_unlocked (tree, path) ==

1521 &tree_test_data\[i\]);

1522

1523 return TRUE;

1524}

1525

1526static dbus_bool_t

1527do_test_dispatch (DBusObjectTree \*tree,

1528 const char \*\*path,

1529 int i,

1530 TreeTestData \*tree_test_data,

1531 int n_test_data)

1532{

1533 DBusMessage \*message;

1534 int j;

1535 DBusHandlerResult result;

1536 char \*flat;

1537

1538 message = NULL;

1539

1540 flat = flatten_path (path);

1541 if (flat == NULL)

1542 goto oom;

1543

1544 message = dbus_message_new_method_call (NULL,

1545 flat,

1546 "org.freedesktop.TestInterface",

1547 "Foo");

1548 dbus_free (flat);

1549 if (message == NULL)

1550 goto oom;

1551

1552 j = 0;

1553 while (j \< n_test_data)

1554 {

1555 tree_test_data\[j\].message_handled = FALSE;

1556 ++j;

1557 }

1558

1559 result = \_dbus_object_tree_dispatch_and_unlock (tree, message, NULL);

1560 if (result == DBUS_HANDLER_RESULT_NEED_MEMORY)

1561 goto oom;

1562

1563 \_dbus_assert (tree_test_data\[i\].message_handled);

1564

1565 j = 0;

1566 while (j \< n_test_data)

1567 {

1568 if (tree_test_data\[j\].message_handled)

1569 {

1570 if (tree_test_data\[j\].handler_fallback)

1571 \_dbus_assert (path_contains (tree_test_data\[j\].path,

1572 path) != STR_DIFFERENT);

1573 else

1574 \_dbus_assert (path_contains (tree_test_data\[j\].path, path) == STR_EQUAL);

1575 }

1576 else

1577 {

1578 if (tree_test_data\[j\].handler_fallback)

1579 \_dbus_assert (path_contains (tree_test_data\[j\].path,

1580 path) == STR_DIFFERENT);

1581 else

1582 \_dbus_assert (path_contains (tree_test_data\[j\].path, path) != STR_EQUAL);

1583 }

1584

1585 ++j;

1586 }

1587

1588 dbus_message_unref (message);

1589

1590 return TRUE;

1591

1592 oom:

1593 if (message)

1594 dbus_message_unref (message);

1595 return FALSE;

1596}

1597

1598typedef struct

1599{

1600 const char \*path;

1601 const char \*result\[20\];

1602} DecomposePathTest;

1603

1604static DecomposePathTest decompose_tests\[\] = {

1605 { "/foo", { "foo", NULL } },

1606 { "/foo/bar", { "foo", "bar", NULL } },

1607 { "/", { NULL } },

1608 { "/a/b", { "a", "b", NULL } },

1609 { "/a/b/c", { "a", "b", "c", NULL } },

1610 { "/a/b/c/d", { "a", "b", "c", "d", NULL } },

1611 { "/foo/bar/q", { "foo", "bar", "q", NULL } },

1612 { "/foo/bar/this/is/longer", { "foo", "bar", "this", "is", "longer", NULL } }

1613};

1614

1615/\* Return TRUE on success, FALSE on OOM, die with an assertion failure

1616 \* on failure. \*/

1617static dbus_bool_t

1618run_decompose_tests (void)

1619{

1620 int i;

1621

1622 i = 0;

1623 while (i \< \_DBUS_N_ELEMENTS (decompose_tests))

1624 {

1625 char \*\*result;

1626 int result_len;

1627 int expected_len;

1628

1629 if (!\_dbus_decompose_path (decompose_tests\[i\].path,

1630 strlen (decompose_tests\[i\].path),

1631 &result, &result_len))

1632 return FALSE;

1633

1634 expected_len = \_dbus_string_array_length (decompose_tests\[i\].result);

1635

1636 if (result_len != (int) \_dbus_string_array_length ((const char\*\*)result) \|\|

1637 expected_len != result_len \|\|

1638 path_contains (decompose_tests\[i\].result,

1639 (const char\*\*) result) != STR_EQUAL)

1640 {

1641 int real_len = \_dbus_string_array_length ((const char\*\*)result);

1642 \_dbus_warn ("Expected decompose of %s to have len %d, returned %d, appears to have %d",

1643 decompose_tests\[i\].path, expected_len, result_len,

1644 real_len);

1645 \_dbus_warn ("Decompose resulted in elements: { ");

1646 i = 0;

1647 while (i \< real_len)

1648 {

1649 \_dbus_warn ("\\%s\\%s", result\[i\],

1650 (i + 1) == real_len ? "" : ", ");

1651 ++i;

1652 }

1653 \_dbus_warn ("}");

1654 \_dbus_test_fatal ("path decompose failed");

1655 }

1656

1657 dbus_free_string_array (result);

1658

1659 ++i;

1660 }

1661

1662 return TRUE;

1663}

1664

1665static DBusObjectSubtree\*

1666find_subtree_registered_or_unregistered (DBusObjectTree \*tree,

1667 const char \*\*path)

1668{

1669\#if VERBOSE_FIND

1670 \_dbus_verbose ("Looking for exact subtree, registered or unregistered\n");

1671\#endif

1672

1673 return find_subtree_recurse (tree-\>root, path, FALSE, NULL, NULL);

1674}

1675

1676/\* Returns TRUE if the right thing happens, but the right thing might

1677 \* be OOM. \*/

1678static dbus_bool_t

1679object_tree_test_iteration (void \*data,

1680 dbus_bool_t have_memory)

1681{

1682 const char \*path0\[\] = { NULL };

1683 const char \*path1\[\] = { "foo", NULL };

1684 const char \*path2\[\] = { "foo", "bar", NULL };

1685 const char \*path3\[\] = { "foo", "bar", "baz", NULL };

1686 const char \*path4\[\] = { "foo", "bar", "boo", NULL };

1687 const char \*path5\[\] = { "blah", NULL };

1688 const char \*path6\[\] = { "blah", "boof", NULL };

1689 const char \*path7\[\] = { "blah", "boof", "this", "is", "really", "long", NULL };

1690 const char \*path8\[\] = { "childless", NULL };

1691 const char \*path9\[\] = { "blah", "a", NULL };

1692 const char \*path10\[\] = { "blah", "b", NULL };

1693 const char \*path11\[\] = { "blah", "c", NULL };

1694 const char \*path12\[\] = { "blah", "a", "d", NULL };

1695 const char \*path13\[\] = { "blah", "b", "d", NULL };

1696 const char \*path14\[\] = { "blah", "c", "d", NULL };

1697 DBusObjectPathVTable test_vtable = { NULL, test_message_function, NULL };

1698 DBusObjectTree \*tree;

1699 TreeTestData tree_test_data\[9\];

1700 int i;

1701 dbus_bool_t exact_match;

1702

1703 if (!run_decompose_tests ())

1704 return TRUE; /\* OOM is OK \*/

1705

1706 tree = NULL;

1707

1708 tree = \_dbus_object_tree_new (NULL);

1709 if (tree == NULL)

1710 goto out;

1711

1712 if (!do_register (tree, path0, TRUE, 0, tree_test_data))

1713 goto out;

1714

1715 \_dbus_assert (find_subtree (tree, path0, NULL));

1716 \_dbus_assert (!find_subtree (tree, path1, NULL));

1717 \_dbus_assert (!find_subtree (tree, path2, NULL));

1718 \_dbus_assert (!find_subtree (tree, path3, NULL));

1719 \_dbus_assert (!find_subtree (tree, path4, NULL));

1720 \_dbus_assert (!find_subtree (tree, path5, NULL));

1721 \_dbus_assert (!find_subtree (tree, path6, NULL));

1722 \_dbus_assert (!find_subtree (tree, path7, NULL));

1723 \_dbus_assert (!find_subtree (tree, path8, NULL));

1724

1725 \_dbus_assert (find_handler (tree, path0, &exact_match) && exact_match);

1726 \_dbus_assert (find_handler (tree, path1, &exact_match) == tree-\>root && !exact_match);

1727 \_dbus_assert (find_handler (tree, path2, &exact_match) == tree-\>root && !exact_match);

1728 \_dbus_assert (find_handler (tree, path3, &exact_match) == tree-\>root && !exact_match);

1729 \_dbus_assert (find_handler (tree, path4, &exact_match) == tree-\>root && !exact_match);

1730 \_dbus_assert (find_handler (tree, path5, &exact_match) == tree-\>root && !exact_match);

1731 \_dbus_assert (find_handler (tree, path6, &exact_match) == tree-\>root && !exact_match);

1732 \_dbus_assert (find_handler (tree, path7, &exact_match) == tree-\>root && !exact_match);

1733 \_dbus_assert (find_handler (tree, path8, &exact_match) == tree-\>root && !exact_match);

1734

1735 if (!do_register (tree, path1, TRUE, 1, tree_test_data))

1736 goto out;

1737

1738 \_dbus_assert (find_subtree (tree, path0, NULL));

1739 \_dbus_assert (find_subtree (tree, path1, NULL));

1740 \_dbus_assert (!find_subtree (tree, path2, NULL));

1741 \_dbus_assert (!find_subtree (tree, path3, NULL));

1742 \_dbus_assert (!find_subtree (tree, path4, NULL));

1743 \_dbus_assert (!find_subtree (tree, path5, NULL));

1744 \_dbus_assert (!find_subtree (tree, path6, NULL));

1745 \_dbus_assert (!find_subtree (tree, path7, NULL));

1746 \_dbus_assert (!find_subtree (tree, path8, NULL));

1747

1748 \_dbus_assert (find_handler (tree, path0, &exact_match) && exact_match);

1749 \_dbus_assert (find_handler (tree, path1, &exact_match) && exact_match);

1750 \_dbus_assert (find_handler (tree, path2, &exact_match) && !exact_match);

1751 \_dbus_assert (find_handler (tree, path3, &exact_match) && !exact_match);

1752 \_dbus_assert (find_handler (tree, path4, &exact_match) && !exact_match);

1753 \_dbus_assert (find_handler (tree, path5, &exact_match) == tree-\>root && !exact_match);

1754 \_dbus_assert (find_handler (tree, path6, &exact_match) == tree-\>root && !exact_match);

1755 \_dbus_assert (find_handler (tree, path7, &exact_match) == tree-\>root && !exact_match);

1756 \_dbus_assert (find_handler (tree, path8, &exact_match) == tree-\>root && !exact_match);

1757

1758 if (!do_register (tree, path2, TRUE, 2, tree_test_data))

1759 goto out;

1760

1761 \_dbus_assert (find_subtree (tree, path1, NULL));

1762 \_dbus_assert (find_subtree (tree, path2, NULL));

1763 \_dbus_assert (!find_subtree (tree, path3, NULL));

1764 \_dbus_assert (!find_subtree (tree, path4, NULL));

1765 \_dbus_assert (!find_subtree (tree, path5, NULL));

1766 \_dbus_assert (!find_subtree (tree, path6, NULL));

1767 \_dbus_assert (!find_subtree (tree, path7, NULL));

1768 \_dbus_assert (!find_subtree (tree, path8, NULL));

1769

1770 if (!do_register (tree, path3, TRUE, 3, tree_test_data))

1771 goto out;

1772

1773 \_dbus_assert (find_subtree (tree, path0, NULL));

1774 \_dbus_assert (find_subtree (tree, path1, NULL));

1775 \_dbus_assert (find_subtree (tree, path2, NULL));

1776 \_dbus_assert (find_subtree (tree, path3, NULL));

1777 \_dbus_assert (!find_subtree (tree, path4, NULL));

1778 \_dbus_assert (!find_subtree (tree, path5, NULL));

1779 \_dbus_assert (!find_subtree (tree, path6, NULL));

1780 \_dbus_assert (!find_subtree (tree, path7, NULL));

1781 \_dbus_assert (!find_subtree (tree, path8, NULL));

1782

1783 if (!do_register (tree, path4, TRUE, 4, tree_test_data))

1784 goto out;

1785

1786 \_dbus_assert (find_subtree (tree, path0, NULL));

1787 \_dbus_assert (find_subtree (tree, path1, NULL));

1788 \_dbus_assert (find_subtree (tree, path2, NULL));

1789 \_dbus_assert (find_subtree (tree, path3, NULL));

1790 \_dbus_assert (find_subtree (tree, path4, NULL));

1791 \_dbus_assert (!find_subtree (tree, path5, NULL));

1792 \_dbus_assert (!find_subtree (tree, path6, NULL));

1793 \_dbus_assert (!find_subtree (tree, path7, NULL));

1794 \_dbus_assert (!find_subtree (tree, path8, NULL));

1795

1796 if (!do_register (tree, path5, TRUE, 5, tree_test_data))

1797 goto out;

1798

1799 \_dbus_assert (find_subtree (tree, path0, NULL));

1800 \_dbus_assert (find_subtree (tree, path1, NULL));

1801 \_dbus_assert (find_subtree (tree, path2, NULL));

1802 \_dbus_assert (find_subtree (tree, path3, NULL));

1803 \_dbus_assert (find_subtree (tree, path4, NULL));

1804 \_dbus_assert (find_subtree (tree, path5, NULL));

1805 \_dbus_assert (!find_subtree (tree, path6, NULL));

1806 \_dbus_assert (!find_subtree (tree, path7, NULL));

1807 \_dbus_assert (!find_subtree (tree, path8, NULL));

1808

1809 \_dbus_assert (find_handler (tree, path0, &exact_match) == tree-\>root && exact_match);

1810 \_dbus_assert (find_handler (tree, path1, &exact_match) != tree-\>root && exact_match);

1811 \_dbus_assert (find_handler (tree, path2, &exact_match) != tree-\>root && exact_match);

1812 \_dbus_assert (find_handler (tree, path3, &exact_match) != tree-\>root && exact_match);

1813 \_dbus_assert (find_handler (tree, path4, &exact_match) != tree-\>root && exact_match);

1814 \_dbus_assert (find_handler (tree, path5, &exact_match) != tree-\>root && exact_match);

1815 \_dbus_assert (find_handler (tree, path6, &exact_match) != tree-\>root && !exact_match);

1816 \_dbus_assert (find_handler (tree, path7, &exact_match) != tree-\>root && !exact_match);

1817 \_dbus_assert (find_handler (tree, path8, &exact_match) == tree-\>root && !exact_match);

1818

1819 if (!do_register (tree, path6, TRUE, 6, tree_test_data))

1820 goto out;

1821

1822 \_dbus_assert (find_subtree (tree, path0, NULL));

1823 \_dbus_assert (find_subtree (tree, path1, NULL));

1824 \_dbus_assert (find_subtree (tree, path2, NULL));

1825 \_dbus_assert (find_subtree (tree, path3, NULL));

1826 \_dbus_assert (find_subtree (tree, path4, NULL));

1827 \_dbus_assert (find_subtree (tree, path5, NULL));

1828 \_dbus_assert (find_subtree (tree, path6, NULL));

1829 \_dbus_assert (!find_subtree (tree, path7, NULL));

1830 \_dbus_assert (!find_subtree (tree, path8, NULL));

1831

1832 if (!do_register (tree, path7, TRUE, 7, tree_test_data))

1833 goto out;

1834

1835 \_dbus_assert (find_subtree (tree, path0, NULL));

1836 \_dbus_assert (find_subtree (tree, path1, NULL));

1837 \_dbus_assert (find_subtree (tree, path2, NULL));

1838 \_dbus_assert (find_subtree (tree, path3, NULL));

1839 \_dbus_assert (find_subtree (tree, path4, NULL));

1840 \_dbus_assert (find_subtree (tree, path5, NULL));

1841 \_dbus_assert (find_subtree (tree, path6, NULL));

1842 \_dbus_assert (find_subtree (tree, path7, NULL));

1843 \_dbus_assert (!find_subtree (tree, path8, NULL));

1844

1845 if (!do_register (tree, path8, TRUE, 8, tree_test_data))

1846 goto out;

1847

1848 \_dbus_assert (find_subtree (tree, path0, NULL));

1849 \_dbus_assert (find_subtree (tree, path1, NULL));

1850 \_dbus_assert (find_subtree (tree, path2, NULL));

1851 \_dbus_assert (find_subtree (tree, path3, NULL));

1852 \_dbus_assert (find_subtree (tree, path4, NULL));

1853 \_dbus_assert (find_subtree (tree, path5, NULL));

1854 \_dbus_assert (find_subtree (tree, path6, NULL));

1855 \_dbus_assert (find_subtree (tree, path7, NULL));

1856 \_dbus_assert (find_subtree (tree, path8, NULL));

1857

1858 \_dbus_assert (find_handler (tree, path0, &exact_match) == tree-\>root && exact_match);

1859 \_dbus_assert (find_handler (tree, path1, &exact_match) != tree-\>root && exact_match);

1860 \_dbus_assert (find_handler (tree, path2, &exact_match) != tree-\>root && exact_match);

1861 \_dbus_assert (find_handler (tree, path3, &exact_match) != tree-\>root && exact_match);

1862 \_dbus_assert (find_handler (tree, path4, &exact_match) != tree-\>root && exact_match);

1863 \_dbus_assert (find_handler (tree, path5, &exact_match) != tree-\>root && exact_match);

1864 \_dbus_assert (find_handler (tree, path6, &exact_match) != tree-\>root && exact_match);

1865 \_dbus_assert (find_handler (tree, path7, &exact_match) != tree-\>root && exact_match);

1866 \_dbus_assert (find_handler (tree, path8, &exact_match) != tree-\>root && exact_match);

1867

1868 /\* test the list_registered function \*/

1869

1870 {

1871 const char \*root\[\] = { NULL };

1872 char \*\*child_entries;

1873 int nb;

1874

1875 \_dbus_object_tree_list_registered_unlocked (tree, path1, &child_entries);

1876 if (child_entries != NULL)

1877 {

1878 nb = \_dbus_string_array_length ((const char\*\*)child_entries);

1879 \_dbus_assert (nb == 1);

1880 dbus_free_string_array (child_entries);

1881 }

1882

1883 \_dbus_object_tree_list_registered_unlocked (tree, path2, &child_entries);

1884 if (child_entries != NULL)

1885 {

1886 nb = \_dbus_string_array_length ((const char\*\*)child_entries);

1887 \_dbus_assert (nb == 2);

1888 dbus_free_string_array (child_entries);

1889 }

1890

1891 \_dbus_object_tree_list_registered_unlocked (tree, path8, &child_entries);

1892 if (child_entries != NULL)

1893 {

1894 nb = \_dbus_string_array_length ((const char\*\*)child_entries);

1895 \_dbus_assert (nb == 0);

1896 dbus_free_string_array (child_entries);

1897 }

1898

1899 \_dbus_object_tree_list_registered_unlocked (tree, root, &child_entries);

1900 if (child_entries != NULL)

1901 {

1902 nb = \_dbus_string_array_length ((const char\*\*)child_entries);

1903 \_dbus_assert (nb == 3);

1904 dbus_free_string_array (child_entries);

1905 }

1906 }

1907

1908 /\* Check that destroying tree calls unregister funcs \*/

1909 \_dbus_object_tree_unref (tree);

1910

1911 i = 0;

1912 while (i \< (int) \_DBUS_N_ELEMENTS (tree_test_data))

1913 {

1914 \_dbus_assert (tree_test_data\[i\].handler_unregistered);

1915 \_dbus_assert (!tree_test_data\[i\].message_handled);

1916 ++i;

1917 }

1918

1919 /\* Now start again and try the individual unregister function \*/

1920 tree = \_dbus_object_tree_new (NULL);

1921 if (tree == NULL)

1922 goto out;

1923

1924 if (!do_register (tree, path0, TRUE, 0, tree_test_data))

1925 goto out;

1926 if (!do_register (tree, path1, TRUE, 1, tree_test_data))

1927 goto out;

1928 if (!do_register (tree, path2, TRUE, 2, tree_test_data))

1929 goto out;

1930 if (!do_register (tree, path3, TRUE, 3, tree_test_data))

1931 goto out;

1932 if (!do_register (tree, path4, TRUE, 4, tree_test_data))

1933 goto out;

1934 if (!do_register (tree, path5, TRUE, 5, tree_test_data))

1935 goto out;

1936 if (!do_register (tree, path6, TRUE, 6, tree_test_data))

1937 goto out;

1938 if (!do_register (tree, path7, TRUE, 7, tree_test_data))

1939 goto out;

1940 if (!do_register (tree, path8, TRUE, 8, tree_test_data))

1941 goto out;

1942

1943 \_dbus_object_tree_unregister_and_unlock (tree, path0);

1944 \_dbus_assert (\_dbus_object_tree_get_user_data_unlocked (tree, path0) == NULL);

1945

1946 \_dbus_assert (!find_subtree (tree, path0, NULL));

1947 \_dbus_assert (find_subtree (tree, path1, NULL));

1948 \_dbus_assert (find_subtree (tree, path2, NULL));

1949 \_dbus_assert (find_subtree (tree, path3, NULL));

1950 \_dbus_assert (find_subtree (tree, path4, NULL));

1951 \_dbus_assert (find_subtree (tree, path5, NULL));

1952 \_dbus_assert (find_subtree (tree, path6, NULL));

1953 \_dbus_assert (find_subtree (tree, path7, NULL));

1954 \_dbus_assert (find_subtree (tree, path8, NULL));

1955

1956 \_dbus_object_tree_unregister_and_unlock (tree, path1);

1957 \_dbus_assert (\_dbus_object_tree_get_user_data_unlocked (tree, path1) == NULL);

1958

1959 \_dbus_assert (!find_subtree (tree, path0, NULL));

1960 \_dbus_assert (!find_subtree (tree, path1, NULL));

1961 \_dbus_assert (find_subtree (tree, path2, NULL));

1962 \_dbus_assert (find_subtree (tree, path3, NULL));

1963 \_dbus_assert (find_subtree (tree, path4, NULL));

1964 \_dbus_assert (find_subtree (tree, path5, NULL));

1965 \_dbus_assert (find_subtree (tree, path6, NULL));

1966 \_dbus_assert (find_subtree (tree, path7, NULL));

1967 \_dbus_assert (find_subtree (tree, path8, NULL));

1968

1969 \_dbus_object_tree_unregister_and_unlock (tree, path2);

1970 \_dbus_assert (\_dbus_object_tree_get_user_data_unlocked (tree, path2) == NULL);

1971

1972 \_dbus_assert (!find_subtree (tree, path0, NULL));

1973 \_dbus_assert (!find_subtree (tree, path1, NULL));

1974 \_dbus_assert (!find_subtree (tree, path2, NULL));

1975 \_dbus_assert (find_subtree (tree, path3, NULL));

1976 \_dbus_assert (find_subtree (tree, path4, NULL));

1977 \_dbus_assert (find_subtree (tree, path5, NULL));

1978 \_dbus_assert (find_subtree (tree, path6, NULL));

1979 \_dbus_assert (find_subtree (tree, path7, NULL));

1980 \_dbus_assert (find_subtree (tree, path8, NULL));

1981

1982 \_dbus_object_tree_unregister_and_unlock (tree, path3);

1983 \_dbus_assert (\_dbus_object_tree_get_user_data_unlocked (tree, path3) == NULL);

1984

1985 \_dbus_assert (!find_subtree (tree, path0, NULL));

1986 \_dbus_assert (!find_subtree (tree, path1, NULL));

1987 \_dbus_assert (!find_subtree (tree, path2, NULL));

1988 \_dbus_assert (!find_subtree (tree, path3, NULL));

1989 \_dbus_assert (find_subtree (tree, path4, NULL));

1990 \_dbus_assert (find_subtree (tree, path5, NULL));

1991 \_dbus_assert (find_subtree (tree, path6, NULL));

1992 \_dbus_assert (find_subtree (tree, path7, NULL));

1993 \_dbus_assert (find_subtree (tree, path8, NULL));

1994

1995 \_dbus_object_tree_unregister_and_unlock (tree, path4);

1996 \_dbus_assert (\_dbus_object_tree_get_user_data_unlocked (tree, path4) == NULL);

1997

1998 \_dbus_assert (!find_subtree (tree, path0, NULL));

1999 \_dbus_assert (!find_subtree (tree, path1, NULL));

2000 \_dbus_assert (!find_subtree (tree, path2, NULL));

2001 \_dbus_assert (!find_subtree (tree, path3, NULL));

2002 \_dbus_assert (!find_subtree (tree, path4, NULL));

2003 \_dbus_assert (find_subtree (tree, path5, NULL));

2004 \_dbus_assert (find_subtree (tree, path6, NULL));

2005 \_dbus_assert (find_subtree (tree, path7, NULL));

2006 \_dbus_assert (find_subtree (tree, path8, NULL));

2007

2008 \_dbus_object_tree_unregister_and_unlock (tree, path5);

2009 \_dbus_assert (\_dbus_object_tree_get_user_data_unlocked (tree, path5) == NULL);

2010

2011 \_dbus_assert (!find_subtree (tree, path0, NULL));

2012 \_dbus_assert (!find_subtree (tree, path1, NULL));

2013 \_dbus_assert (!find_subtree (tree, path2, NULL));

2014 \_dbus_assert (!find_subtree (tree, path3, NULL));

2015 \_dbus_assert (!find_subtree (tree, path4, NULL));

2016 \_dbus_assert (!find_subtree (tree, path5, NULL));

2017 \_dbus_assert (find_subtree (tree, path6, NULL));

2018 \_dbus_assert (find_subtree (tree, path7, NULL));

2019 \_dbus_assert (find_subtree (tree, path8, NULL));

2020

2021 \_dbus_object_tree_unregister_and_unlock (tree, path6);

2022 \_dbus_assert (\_dbus_object_tree_get_user_data_unlocked (tree, path6) == NULL);

2023

2024 \_dbus_assert (!find_subtree (tree, path0, NULL));

2025 \_dbus_assert (!find_subtree (tree, path1, NULL));

2026 \_dbus_assert (!find_subtree (tree, path2, NULL));

2027 \_dbus_assert (!find_subtree (tree, path3, NULL));

2028 \_dbus_assert (!find_subtree (tree, path4, NULL));

2029 \_dbus_assert (!find_subtree (tree, path5, NULL));

2030 \_dbus_assert (!find_subtree (tree, path6, NULL));

2031 \_dbus_assert (find_subtree (tree, path7, NULL));

2032 \_dbus_assert (find_subtree (tree, path8, NULL));

2033

2034 \_dbus_object_tree_unregister_and_unlock (tree, path7);

2035 \_dbus_assert (\_dbus_object_tree_get_user_data_unlocked (tree, path7) == NULL);

2036

2037 \_dbus_assert (!find_subtree (tree, path0, NULL));

2038 \_dbus_assert (!find_subtree (tree, path1, NULL));

2039 \_dbus_assert (!find_subtree (tree, path2, NULL));

2040 \_dbus_assert (!find_subtree (tree, path3, NULL));

2041 \_dbus_assert (!find_subtree (tree, path4, NULL));

2042 \_dbus_assert (!find_subtree (tree, path5, NULL));

2043 \_dbus_assert (!find_subtree (tree, path6, NULL));

2044 \_dbus_assert (!find_subtree (tree, path7, NULL));

2045 \_dbus_assert (find_subtree (tree, path8, NULL));

2046

2047 \_dbus_object_tree_unregister_and_unlock (tree, path8);

2048 \_dbus_assert (\_dbus_object_tree_get_user_data_unlocked (tree, path8) == NULL);

2049

2050 \_dbus_assert (!find_subtree (tree, path0, NULL));

2051 \_dbus_assert (!find_subtree (tree, path1, NULL));

2052 \_dbus_assert (!find_subtree (tree, path2, NULL));

2053 \_dbus_assert (!find_subtree (tree, path3, NULL));

2054 \_dbus_assert (!find_subtree (tree, path4, NULL));

2055 \_dbus_assert (!find_subtree (tree, path5, NULL));

2056 \_dbus_assert (!find_subtree (tree, path6, NULL));

2057 \_dbus_assert (!find_subtree (tree, path7, NULL));

2058 \_dbus_assert (!find_subtree (tree, path8, NULL));

2059

2060 i = 0;

2061 while (i \< (int) \_DBUS_N_ELEMENTS (tree_test_data))

2062 {

2063 \_dbus_assert (tree_test_data\[i\].handler_unregistered);

2064 \_dbus_assert (!tree_test_data\[i\].message_handled);

2065 ++i;

2066 }

2067

2068 /\* Test removal of newly-childless unregistered nodes \*/

2069 if (!do_register (tree, path2, TRUE, 2, tree_test_data))

2070 goto out;

2071

2072 \_dbus_object_tree_unregister_and_unlock (tree, path2);

2073 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path2));

2074 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path1));

2075 \_dbus_assert (find_subtree_registered_or_unregistered (tree, path0));

2076

2077 /\* Test that unregistered parents cannot be freed out from under their

2078 children \*/

2079 if (!do_register (tree, path2, TRUE, 2, tree_test_data))

2080 goto out;

2081

2082 \_dbus_assert (!find_subtree (tree, path1, NULL));

2083 \_dbus_assert (find_subtree_registered_or_unregistered (tree, path1));

2084 \_dbus_assert (find_subtree_registered_or_unregistered (tree, path0));

2085

2086\#if 0

2087 /\* This triggers the "Attempted to unregister path ..." warning message \*/

2088 \_dbus_object_tree_unregister_and_unlock (tree, path1);

2089\#endif

2090 \_dbus_assert (find_subtree (tree, path2, NULL));

2091 \_dbus_assert (!find_subtree (tree, path1, NULL));

2092 \_dbus_assert (find_subtree_registered_or_unregistered (tree, path1));

2093 \_dbus_assert (find_subtree_registered_or_unregistered (tree, path0));

2094

2095 \_dbus_object_tree_unregister_and_unlock (tree, path2);

2096 \_dbus_assert (!find_subtree (tree, path2, NULL));

2097 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path2));

2098 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path1));

2099 \_dbus_assert (find_subtree_registered_or_unregistered (tree, path0));

2100

2101 /\* Test that registered parents cannot be freed out from under their

2102 children, and that if they are unregistered before their children, they

2103 are still freed when their children are unregistered \*/

2104 if (!do_register (tree, path1, TRUE, 1, tree_test_data))

2105 goto out;

2106 if (!do_register (tree, path2, TRUE, 2, tree_test_data))

2107 goto out;

2108

2109 \_dbus_assert (find_subtree (tree, path1, NULL));

2110 \_dbus_assert (find_subtree (tree, path2, NULL));

2111

2112 \_dbus_object_tree_unregister_and_unlock (tree, path1);

2113 \_dbus_assert (!find_subtree (tree, path1, NULL));

2114 \_dbus_assert (find_subtree (tree, path2, NULL));

2115 \_dbus_assert (find_subtree_registered_or_unregistered (tree, path1));

2116 \_dbus_assert (find_subtree_registered_or_unregistered (tree, path0));

2117

2118 \_dbus_object_tree_unregister_and_unlock (tree, path2);

2119 \_dbus_assert (!find_subtree (tree, path1, NULL));

2120 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path1));

2121 \_dbus_assert (!find_subtree (tree, path2, NULL));

2122 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path2));

2123 \_dbus_assert (find_subtree_registered_or_unregistered (tree, path0));

2124

2125 /\* Test with NULL unregister_function and user_data \*/

2126 if (!\_dbus_object_tree_register (tree, TRUE, path2,

2127 &test_vtable,

2128 NULL,

2129 NULL))

2130 goto out;

2131

2132 \_dbus_assert (\_dbus_object_tree_get_user_data_unlocked (tree, path2) == NULL);

2133 \_dbus_object_tree_unregister_and_unlock (tree, path2);

2134 \_dbus_assert (!find_subtree (tree, path2, NULL));

2135 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path2));

2136 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path1));

2137 \_dbus_assert (find_subtree_registered_or_unregistered (tree, path0));

2138

2139 /\* Test freeing a long path \*/

2140 if (!do_register (tree, path3, TRUE, 3, tree_test_data))

2141 goto out;

2142

2143 \_dbus_object_tree_unregister_and_unlock (tree, path3);

2144 \_dbus_assert (!find_subtree (tree, path3, NULL));

2145 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path3));

2146 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path2));

2147 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path1));

2148 \_dbus_assert (find_subtree_registered_or_unregistered (tree, path0));

2149

2150 /\* Test freeing multiple children from the same path \*/

2151 if (!do_register (tree, path3, TRUE, 3, tree_test_data))

2152 goto out;

2153 if (!do_register (tree, path4, TRUE, 4, tree_test_data))

2154 goto out;

2155

2156 \_dbus_assert (find_subtree (tree, path3, NULL));

2157 \_dbus_assert (find_subtree (tree, path4, NULL));

2158

2159 \_dbus_object_tree_unregister_and_unlock (tree, path3);

2160 \_dbus_assert (!find_subtree (tree, path3, NULL));

2161 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path3));

2162 \_dbus_assert (find_subtree (tree, path4, NULL));

2163 \_dbus_assert (find_subtree_registered_or_unregistered (tree, path4));

2164 \_dbus_assert (find_subtree_registered_or_unregistered (tree, path2));

2165 \_dbus_assert (find_subtree_registered_or_unregistered (tree, path1));

2166

2167 \_dbus_object_tree_unregister_and_unlock (tree, path4);

2168 \_dbus_assert (!find_subtree (tree, path4, NULL));

2169 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path4));

2170 \_dbus_assert (!find_subtree (tree, path3, NULL));

2171 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path3));

2172 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path2));

2173 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path1));

2174

2175 /\* Test subtree removal \*/

2176 if (!\_dbus_object_tree_register (tree, TRUE, path12,

2177 &test_vtable,

2178 NULL,

2179 NULL))

2180 goto out;

2181

2182 \_dbus_assert (find_subtree (tree, path12, NULL));

2183

2184 if (!\_dbus_object_tree_register (tree, TRUE, path13,

2185 &test_vtable,

2186 NULL,

2187 NULL))

2188 goto out;

2189

2190 \_dbus_assert (find_subtree (tree, path13, NULL));

2191

2192 if (!\_dbus_object_tree_register (tree, TRUE, path14,

2193 &test_vtable,

2194 NULL,

2195 NULL))

2196 goto out;

2197

2198 \_dbus_assert (find_subtree (tree, path14, NULL));

2199

2200 \_dbus_object_tree_unregister_and_unlock (tree, path12);

2201

2202 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path12));

2203 \_dbus_assert (find_subtree (tree, path13, NULL));

2204 \_dbus_assert (find_subtree (tree, path14, NULL));

2205 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path9));

2206 \_dbus_assert (find_subtree_registered_or_unregistered (tree, path5));

2207

2208 if (!\_dbus_object_tree_register (tree, TRUE, path12,

2209 &test_vtable,

2210 NULL,

2211 NULL))

2212 goto out;

2213

2214 \_dbus_assert (find_subtree (tree, path12, NULL));

2215

2216 \_dbus_object_tree_unregister_and_unlock (tree, path13);

2217

2218 \_dbus_assert (find_subtree (tree, path12, NULL));

2219 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path13));

2220 \_dbus_assert (find_subtree (tree, path14, NULL));

2221 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path10));

2222 \_dbus_assert (find_subtree_registered_or_unregistered (tree, path5));

2223

2224 if (!\_dbus_object_tree_register (tree, TRUE, path13,

2225 &test_vtable,

2226 NULL,

2227 NULL))

2228 goto out;

2229

2230 \_dbus_assert (find_subtree (tree, path13, NULL));

2231

2232 \_dbus_object_tree_unregister_and_unlock (tree, path14);

2233

2234 \_dbus_assert (find_subtree (tree, path12, NULL));

2235 \_dbus_assert (find_subtree (tree, path13, NULL));

2236 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path14));

2237 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path11));

2238 \_dbus_assert (find_subtree_registered_or_unregistered (tree, path5));

2239

2240 \_dbus_object_tree_unregister_and_unlock (tree, path12);

2241

2242 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path12));

2243 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path9));

2244 \_dbus_assert (find_subtree_registered_or_unregistered (tree, path5));

2245

2246 \_dbus_object_tree_unregister_and_unlock (tree, path13);

2247

2248 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path13));

2249 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path10));

2250 \_dbus_assert (!find_subtree_registered_or_unregistered (tree, path5));

2251

2252\#if 0

2253 /\* Test attempting to unregister non-existent paths. These trigger

2254 "Attempted to unregister path ..." warning messages \*/

2255 \_dbus_object_tree_unregister_and_unlock (tree, path0);

2256 \_dbus_object_tree_unregister_and_unlock (tree, path1);

2257 \_dbus_object_tree_unregister_and_unlock (tree, path2);

2258 \_dbus_object_tree_unregister_and_unlock (tree, path3);

2259 \_dbus_object_tree_unregister_and_unlock (tree, path4);

2260\#endif

2261

2262 /\* Register it all again, and test dispatch \*/

2263

2264 if (!do_register (tree, path0, TRUE, 0, tree_test_data))

2265 goto out;

2266 if (!do_register (tree, path1, FALSE, 1, tree_test_data))

2267 goto out;

2268 if (!do_register (tree, path2, TRUE, 2, tree_test_data))

2269 goto out;

2270 if (!do_register (tree, path3, TRUE, 3, tree_test_data))

2271 goto out;

2272 if (!do_register (tree, path4, TRUE, 4, tree_test_data))

2273 goto out;

2274 if (!do_register (tree, path5, TRUE, 5, tree_test_data))

2275 goto out;

2276 if (!do_register (tree, path6, FALSE, 6, tree_test_data))

2277 goto out;

2278 if (!do_register (tree, path7, TRUE, 7, tree_test_data))

2279 goto out;

2280 if (!do_register (tree, path8, TRUE, 8, tree_test_data))

2281 goto out;

2282

2283\#if 0

2284 spew_tree (tree);

2285\#endif

2286

2287 if (!do_test_dispatch (tree, path0, 0, tree_test_data, \_DBUS_N_ELEMENTS (tree_test_data)))

2288 goto out;

2289 if (!do_test_dispatch (tree, path1, 1, tree_test_data, \_DBUS_N_ELEMENTS (tree_test_data)))

2290 goto out;

2291 if (!do_test_dispatch (tree, path2, 2, tree_test_data, \_DBUS_N_ELEMENTS (tree_test_data)))

2292 goto out;

2293 if (!do_test_dispatch (tree, path3, 3, tree_test_data, \_DBUS_N_ELEMENTS (tree_test_data)))

2294 goto out;

2295 if (!do_test_dispatch (tree, path4, 4, tree_test_data, \_DBUS_N_ELEMENTS (tree_test_data)))

2296 goto out;

2297 if (!do_test_dispatch (tree, path5, 5, tree_test_data, \_DBUS_N_ELEMENTS (tree_test_data)))

2298 goto out;

2299 if (!do_test_dispatch (tree, path6, 6, tree_test_data, \_DBUS_N_ELEMENTS (tree_test_data)))

2300 goto out;

2301 if (!do_test_dispatch (tree, path7, 7, tree_test_data, \_DBUS_N_ELEMENTS (tree_test_data)))

2302 goto out;

2303 if (!do_test_dispatch (tree, path8, 8, tree_test_data, \_DBUS_N_ELEMENTS (tree_test_data)))

2304 goto out;

2305

2306 out:

2307 if (tree)

2308 {

2309 /\* test ref \*/

2310 \_dbus_object_tree_ref (tree);

2311 \_dbus_object_tree_unref (tree);

2312 \_dbus_object_tree_unref (tree);

2313 }

2314

2315 return TRUE;

2316}

2317

2323dbus_bool_t

2324\_dbus_object_tree_test (const char \*test_data_dir \_DBUS_GNUC_UNUSED)

2325{

2326 return \_dbus_test_oom_handling ("object tree",

2327 object_tree_test_iteration,

2328 NULL);

2329}

2330

2331\#endif /\* !DOXYGEN_SHOULD_SKIP_THIS \*/

2332

2333\#endif /\* DBUS_ENABLE_EMBEDDED_TESTS \*/

\_dbus_connection_send_and_unlock

dbus_bool_t \_dbus_connection_send_and_unlock(DBusConnection \*connection, DBusMessage \*message, dbus_uint32_t \*client_serial)

Like dbus_connection_send(), but assumes the connection is already locked on function entry,...

**Definition** dbus-connection.c:2112

\_dbus_connection_unlock

DBUS_PRIVATE_EXPORT void \_dbus_connection_unlock(DBusConnection \*connection)

Releases the connection lock.

**Definition** dbus-connection.c:403

\_dbus_connection_lock

DBUS_PRIVATE_EXPORT void \_dbus_connection_lock(DBusConnection \*connection)

Acquires the connection lock.

**Definition** dbus-connection.c:392

\_dbus_connection_ref_unlocked

DBUS_PRIVATE_EXPORT DBusConnection \* \_dbus_connection_ref_unlocked(DBusConnection \*connection)

Increments the reference count of a DBusConnection.

**Definition** dbus-connection.c:1424

DBusObjectPathMessageFunction

DBusHandlerResult(\* DBusObjectPathMessageFunction)(DBusConnection \*connection, DBusMessage \*message, void \*user_data)

Called when a message is sent to a registered object path.

**Definition** dbus-connection.h:380

DBusObjectPathUnregisterFunction

void(\* DBusObjectPathUnregisterFunction)(DBusConnection \*connection, void \*user_data)

Called when a DBusObjectPathVTable is unregistered (or its connection is freed).

**Definition** dbus-connection.h:373

dbus_connection_unref

void dbus_connection_unref(DBusConnection \*connection)

Decrements the reference count of a DBusConnection, and finalizes it if the count reaches zero.

**Definition** dbus-connection.c:2832

dbus_set_error

void dbus_set_error(DBusError \*error, const char \*name, const char \*format,...)

Assigns an error name and message to a DBusError.

**Definition** dbus-errors.c:356

\_dbus_assert

\#define \_dbus_assert(condition)

Aborts with an error message if the condition is false.

**Definition** dbus-internals.h:153

\_dbus_strdup

char \* \_dbus_strdup(const char \*str)

Duplicates a string.

**Definition** dbus-internals.c:621

\_dbus_warn

void \_dbus_warn(const char \*format,...)

Prints a warning message to stderr.

**Definition** dbus-internals.c:278

\_DBUS_N_ELEMENTS

\#define \_DBUS_N_ELEMENTS(array)

Computes the number of elements in a fixed-size array using sizeof().

**Definition** dbus-internals.h:189

\_dbus_string_array_length

size_t \_dbus_string_array_length(const char \*\*array)

Returns the size of a string array.

**Definition** dbus-internals.c:735

\_dbus_memdup

void \* \_dbus_memdup(const void \*mem, size_t n_bytes)

Duplicates a block of memory.

**Definition** dbus-internals.c:649

\_dbus_list_get_first_link

DBusList \* \_dbus_list_get_first_link(DBusList \*\*list)

Gets the first link in the list.

**Definition** dbus-list.c:597

\_dbus_list_remove_link

void \_dbus_list_remove_link(DBusList \*\*list, DBusList \*link)

Removes a link from the list.

**Definition** dbus-list.c:530

\_dbus_list_get_length

int \_dbus_list_get_length(DBusList \*\*list)

Gets the length of a list.

**Definition** dbus-list.c:760

\_dbus_list_append

dbus_bool_t \_dbus_list_append(DBusList \*\*list, void \*data)

Appends a value to the list.

**Definition** dbus-list.c:273

\_dbus_list_get_next_link

\#define \_dbus_list_get_next_link(list, link)

Gets the next link in the list, or NULL if there are no more links.

**Definition** dbus-list.h:121

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

dbus_free

void dbus_free(void \*memory)

Frees a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:710

dbus_realloc

void \* dbus_realloc(void \*memory, size_t bytes)

Resizes a block of memory previously allocated by dbus_malloc() or dbus_malloc0().

**Definition** dbus-memory.c:610

dbus_malloc0

void \* dbus_malloc0(size_t bytes)

Allocates the given number of bytes, as with standard malloc(), but all bytes are initialized to zero...

**Definition** dbus-memory.c:540

dbus_new0

\#define dbus_new0(type, count)

Safe macro for using dbus_malloc0().

**Definition** dbus-memory.h:60

dbus_free_string_array

void dbus_free_string_array(char \*\*str_array)

Frees a NULL-terminated array of strings.

**Definition** dbus-memory.c:758

dbus_message_iter_append_basic

dbus_bool_t dbus_message_iter_append_basic(DBusMessageIter \*iter, int type, const void \*value)

Appends a basic-typed value to the message.

**Definition** dbus-message.c:2771

dbus_message_new_method_return

DBusMessage \* dbus_message_new_method_return(DBusMessage \*method_call)

Constructs a message that is a reply to a method call.

**Definition** dbus-message.c:1418

dbus_message_new_method_call

DBusMessage \* dbus_message_new_method_call(const char \*destination, const char \*path, const char \*iface, const char \*method)

Constructs a new message to invoke a method on a remote object.

**Definition** dbus-message.c:1378

dbus_message_unref

void dbus_message_unref(DBusMessage \*message)

Decrements the reference count of a DBusMessage, freeing the message if the count reaches 0.

**Definition** dbus-message.c:1735

dbus_message_is_method_call

dbus_bool_t dbus_message_is_method_call(DBusMessage \*message, const char \*iface, const char \*method)

Checks whether the message is a method call with the given interface and member fields.

**Definition** dbus-message.c:3865

dbus_message_get_path_decomposed

dbus_bool_t dbus_message_get_path_decomposed(DBusMessage \*message, char \*\*\*path)

Gets the object path this message is being sent to (for DBUS_MESSAGE_TYPE_METHOD_CALL) or being emitt...

**Definition** dbus-message.c:3427

dbus_message_iter_init_append

void dbus_message_iter_init_append(DBusMessage \*message, DBusMessageIter \*iter)

Initializes a DBusMessageIter for appending arguments to the end of a message.

**Definition** dbus-message.c:2533

\_dbus_object_tree_free_all_unlocked

void \_dbus_object_tree_free_all_unlocked(DBusObjectTree \*tree)

Free all the handlers in the tree.

**Definition** dbus-object-tree.c:723

\_dbus_object_tree_unregister_and_unlock

void \_dbus_object_tree_unregister_and_unlock(DBusObjectTree \*tree, const char \*\*path)

Unregisters an object subtree that was registered with the same path.

**Definition** dbus-object-tree.c:628

\_dbus_object_tree_unref

void \_dbus_object_tree_unref(DBusObjectTree \*tree)

Decrement the reference count.

**Definition** dbus-object-tree.c:146

\_dbus_object_tree_list_registered_and_unlock

dbus_bool_t \_dbus_object_tree_list_registered_and_unlock(DBusObjectTree \*tree, const char \*\*parent_path, char \*\*\*child_entries)

Lists the registered fallback handlers and object path handlers at the given parent_path.

**Definition** dbus-object-tree.c:1211

\_dbus_decompose_path

dbus_bool_t \_dbus_decompose_path(const char \*data, int len, char \*\*\*path, int \*path_len)

Decompose an object path.

**Definition** dbus-object-tree.c:1247

\_dbus_object_tree_register

dbus_bool_t \_dbus_object_tree_register(DBusObjectTree \*tree, dbus_bool_t fallback, const char \*\*path, const DBusObjectPathVTable \*vtable, void \*user_data, DBusError \*error)

Registers a new subtree in the global object tree.

**Definition** dbus-object-tree.c:396

\_dbus_object_tree_get_user_data_unlocked

void \* \_dbus_object_tree_get_user_data_unlocked(DBusObjectTree \*tree, const char \*\*path)

Looks up the data passed to \_dbus_object_tree_register() for a handler at the given path.

**Definition** dbus-object-tree.c:1080

\_dbus_object_tree_dispatch_and_unlock

DBusHandlerResult \_dbus_object_tree_dispatch_and_unlock(DBusObjectTree \*tree, DBusMessage \*message, dbus_bool_t \*found_object)

Tries to dispatch a message by directing it to handler for the object path listed in the message head...

**Definition** dbus-object-tree.c:908

\_dbus_object_tree_ref

DBusObjectTree \* \_dbus_object_tree_ref(DBusObjectTree \*tree)

Increment the reference count.

**Definition** dbus-object-tree.c:132

\_dbus_object_tree_new

DBusObjectTree \* \_dbus_object_tree_new(DBusConnection \*connection)

Creates a new object tree, representing a mapping from paths to handler vtables.

**Definition** dbus-object-tree.c:95

DBUS_INTROSPECT_1_0_XML_DOCTYPE_DECL_NODE

\#define DBUS_INTROSPECT_1_0_XML_DOCTYPE_DECL_NODE

XML document type declaration of the introspection format version 1.0.

**Definition** dbus-protocol.h:477

DBUS_ERROR_OBJECT_PATH_IN_USE

\#define DBUS_ERROR_OBJECT_PATH_IN_USE

There's already an object with the requested object path.

**Definition** dbus-protocol.h:456

DBUS_TYPE_STRING

\#define DBUS_TYPE_STRING

Type code marking a UTF-8 encoded, nul-terminated Unicode string.

**Definition** dbus-protocol.h:104

DBusHandlerResult

DBusHandlerResult

Results that a message handler can return.

**Definition** dbus-shared.h:69

DBUS_INTERFACE_INTROSPECTABLE

\#define DBUS_INTERFACE_INTROSPECTABLE

The interface supported by introspectable objects.

**Definition** dbus-shared.h:97

DBUS_HANDLER_RESULT_NEED_MEMORY

@ DBUS_HANDLER_RESULT_NEED_MEMORY

Need more memory in order to return DBUS_HANDLER_RESULT_HANDLED or DBUS_HANDLER_RESULT_NOT_YET_HANDLE...

**Definition** dbus-shared.h:72

DBUS_HANDLER_RESULT_HANDLED

@ DBUS_HANDLER_RESULT_HANDLED

Message has had its effect - no need to run more handlers.

**Definition** dbus-shared.h:70

DBUS_HANDLER_RESULT_NOT_YET_HANDLED

@ DBUS_HANDLER_RESULT_NOT_YET_HANDLED

Message has not had any effect - see if other handlers want it.

**Definition** dbus-shared.h:71

\_dbus_string_append

dbus_bool_t \_dbus_string_append(DBusString \*str, const char \*buffer)

Appends a nul-terminated C-style string to a DBusString.

**Definition** dbus-string.c:980

\_dbus_string_init

dbus_bool_t \_dbus_string_init(DBusString \*str)

Initializes a string.

**Definition** dbus-string.c:182

\_dbus_string_steal_data

dbus_bool_t \_dbus_string_steal_data(DBusString \*str, char \*\*data_return)

Like \_dbus_string_get_data(), but removes the gotten data from the original string.

**Definition** dbus-string.c:686

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_string_append_byte

dbus_bool_t \_dbus_string_append_byte(DBusString \*str, unsigned char byte)

Appends a single byte to the string, returning FALSE if not enough memory.

**Definition** dbus-string.c:1190

\_dbus_string_append_printf

dbus_bool_t \_dbus_string_append_printf(DBusString \*str, const char \*format,...)

Appends a printf-style formatted string to the DBusString.

**Definition** dbus-string.c:1147

\_dbus_string_get_const_data

const char \* \_dbus_string_get_const_data(const DBusString \*str)

Gets the raw character buffer from a const string.

**Definition** dbus-string.c:513

\_dbus_atomic_dec

dbus_int32_t \_dbus_atomic_dec(DBusAtomic \*atomic)

Atomically decrement an integer.

**Definition** dbus-sysdeps-unix.c:3205

\_dbus_atomic_inc

dbus_int32_t \_dbus_atomic_inc(DBusAtomic \*atomic)

Atomically increments an integer.

**Definition** dbus-sysdeps-unix.c:3178

DBusAtomic

An atomic integer safe to increment or decrement from multiple threads.

**Definition** dbus-sysdeps.h:340

DBusConnection

Implementation details of DBusConnection.

**Definition** dbus-connection.c:259

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusList

A node in a linked list.

**Definition** dbus-list.h:37

DBusList::data

void \* data

Data stored at this element.

**Definition** dbus-list.h:40

DBusMessageIter

DBusMessageIter struct; contains no public fields.

**Definition** dbus-message.h:64

DBusMessage

Internals of DBusMessage.

**Definition** dbus-message-private.h:102

DBusObjectPathVTable

Virtual table that must be implemented to handle a portion of the object path hierarchy.

**Definition** dbus-connection.h:391

DBusObjectPathVTable::message_function

DBusObjectPathMessageFunction message_function

Function to handle messages.

**Definition** dbus-connection.h:393

DBusObjectPathVTable::unregister_function

DBusObjectPathUnregisterFunction unregister_function

Function to unregister this handler.

**Definition** dbus-connection.h:392

DBusObjectSubtree

Struct representing a single registered subtree handler, or node that's a parent of a registered subt...

**Definition** dbus-object-tree.c:74

DBusObjectSubtree::parent

DBusObjectSubtree \* parent

Parent node.

**Definition** dbus-object-tree.c:76

DBusObjectSubtree::refcount

DBusAtomic refcount

Reference count.

**Definition** dbus-object-tree.c:75

DBusObjectSubtree::message_function

DBusObjectPathMessageFunction message_function

Function to handle messages.

**Definition** dbus-object-tree.c:78

DBusObjectSubtree::unregister_function

DBusObjectPathUnregisterFunction unregister_function

Function to call on unregister.

**Definition** dbus-object-tree.c:77

DBusObjectSubtree::n_subtrees

int n_subtrees

Number of child nodes.

**Definition** dbus-object-tree.c:81

DBusObjectSubtree::invoke_as_fallback

unsigned int invoke_as_fallback

Whether to invoke message_function when child nodes don't handle the message.

**Definition** dbus-object-tree.c:83

DBusObjectSubtree::max_subtrees

int max_subtrees

Number of allocated entries in subtrees.

**Definition** dbus-object-tree.c:82

DBusObjectSubtree::user_data

void \* user_data

Data for functions.

**Definition** dbus-object-tree.c:79

DBusObjectSubtree::name

char name\[1\]

Allocated as large as necessary.

**Definition** dbus-object-tree.c:84

DBusObjectSubtree::subtrees

DBusObjectSubtree \*\* subtrees

Child nodes.

**Definition** dbus-object-tree.c:80

DBusObjectTree

Internals of DBusObjectTree.

**Definition** dbus-object-tree.c:61

DBusObjectTree::connection

DBusConnection \* connection

Connection this tree belongs to.

**Definition** dbus-object-tree.c:63

DBusObjectTree::refcount

int refcount

Reference count.

**Definition** dbus-object-tree.c:62

DBusObjectTree::root

DBusObjectSubtree \* root

Root of the tree ("/" node)

**Definition** dbus-object-tree.c:65

DBusString

**Definition** dbus-string.h:47
