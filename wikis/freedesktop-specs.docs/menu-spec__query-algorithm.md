## 6 Generating the menus

After merging the menus, the result should be a single menu layout description. For each \<Menu\>, we have a list of directories where desktop entries can be found, a list of directories where directory entries can be found, and a series of \<Include\> and \<Exclude\> directives.

For each \<Menu\> element, build a pool of desktop entries by collecting entries found in each \<AppDir\> for the menu element. If two entries have the same desktop-file id, the entry for the earlier (closer to the top of the file) \<AppDir\> must be discarded. Next, add to the pool the entries for any \<AppDir\>s specified by ancestor \<Menu\> elements. If a parent menu has a duplicate entry (same desktop-file id), the entry for the child menu has priority.

Next, walk through all \<Include\> and \<Exclude\> statements. For each \<Include\>, match the rules against the pool of all desktop entries. For each desktop entry that matches one of the rules, add it to the menu to be displayed and mark it as having been allocated. For each \<Exclude\>, match the rules against the currently-included desktop entries. For each desktop entry that matches, remove it again from the menu. Note that an entry that is included in a menu but excluded again by a later \<Exclude\> is still considered allocated (for the purposes of \<OnlyUnallocated\>) even though that entry no longer appears in the menu.

Two passes are necessary, once for regular menus where any entry may be matched, and once for \<OnlyUnallocated\> menus where only entries which have not been marked as allocated may be matched.

The result is a tree of desktop entries, of course.
