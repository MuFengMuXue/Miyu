## 5 Merging

Sometimes two menu layouts need to be merged. This is done when folding in legacy menu hierarchies (see [Section 7, “Legacy Menu Hierarchies”](legacy-hierarchies.html "7. Legacy Menu Hierarchies")) and also for files specified in \<MergeFile\> elements. A common case is that per-user menu files might merge the system menu file. Merging is also used to avoid cut-and-paste, for example to include a common submenu in multiple menu files.

Merging involves a base \<Menu\> and a merged \<Menu\>. The base is the "target" menu and the merged \<Menu\> is being added to it. The result of the merge is termed the "combined menu."

As a preparatory step, the goal is to resolve all files into XML elements. To do so, traverse the entire menu tree. For each \<MergeFile\>, \<MergeDir\>, or \<LegacyDir\> element, replace the \<MergeFile\>, \<MergeDir\>, or \<LegacyDir\> element with the child elements of the root \<Menu\> of the file(s) being merged. As a special exception, remove the \<Name\> element from the root element of each file being merged. To generate a \<Menu\> based on a \<LegacyDir\>, see [Section 7, “Legacy Menu Hierarchies”](legacy-hierarchies.html "7. Legacy Menu Hierarchies").

Continue processing until no \<MergeFile\>, \<MergeDir\>, or \<LegacyDir\> elements remain, taking care to avoid infinite loops caused by files that reference one another.

Once all files have been loaded into a single tree, scan the tree recursively performing these steps to remove duplicates:

1.  Consolidate child menus. Each group of child \<Menu\>s with the same name must be consolidated into a single child menu with that name. Concatenate the child elements of all menus with the same name, in the order that they appear, and insert those elements as the children of the *last* menu with that name. Delete all the newly empty \<Menu\> elements, keeping the last one.

2.  Expand \<DefaultAppDirs\> and \<DefaultDirectoryDirs\> elements to \<AppDir\> and \<DirectoryDir\> elements. Consolidate duplicate \<AppDir\>, \<DirectoryDir\>, and \<Directory\> elements by keeping the last one. For \<Directory\> elements that refer to distinct directory entries, all of them should be kept - if the last one points to a nonexistent file, the one before that can be used instead, and so forth.

3.  Recurse into each child \<Menu\>, performing this list of steps for each child in order.

After recursing once to remove duplicates, recurse a second time to resolve \<Move\> elements for each menu starting with any child menu before handling the more top level menus. So the deepest menus have their \<Move\> operations performed first. Within each \<Menu\>, execute \<Move\> operations in the order that they appear. If the destination path does not exist, simply relocate the origin \<Menu\> element, and change its \<Name\> field to match the destination path. If the origin path does not exist, do nothing. If both paths exist, take the origin \<Menu\> element, delete its \<Name\> element, and prepend its remaining child elements to the destination \<Menu\> element.

If any \<Move\> operations affect a menu, then re-run the steps to resolve duplicates in case any duplicates have been created.

Finally, for each \<Menu\> containing a \<Deleted\> element which is not followed by a \<NotDeleted\> element, remove that menu and all its child menus.

Merged menu elements are kept in order because \<Include\> and \<Exclude\> elements later in the file override \<Include\> and \<Exclude\> elements earlier in the file. This means that if the user's menu file merges the system menu file, the user can always override what the system menu specifies by placing elements after the \<MergeFile\> that incorporates the system file.

To prevent that a desktop entry from one party inadvertently cancels out the desktop entry from another party because both happen to get the same desktop-file id it is recommended that providers of desktop-files ensure that all desktop-file ids start with a vendor prefix. A vendor prefix consists of \[a-zA-Z\] and is terminated with a dash ("-"). Open Source projects and commercial parties are encouraged to use a word or phrase, preferably their name, as prefix for which they hold a trademark. Open Source applications can also ask to make use of the vendor prefix of another open source project (such as GNOME or KDE) they consider themselves affiliated with, at the discretion of these projects.

For example, to ensure that GNOME applications start with a vendor prefix of "gnome-", it could either add "gnome-" to all the desktop files it installs in *`datadir`*`/applications/` or it could install desktop files in a *`datadir`*`/applications/gnome` subdirectory. When including legacy menu hierarchies the `prefix` argument of the \<LegacyDir\> element can be used to specify a prefix.
