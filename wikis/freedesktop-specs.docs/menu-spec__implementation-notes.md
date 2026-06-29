## D Implementation notes

## D.1 Menu editing

To implement menu editing, the intent is that a per-user file is created. The per-user file should specify a \<MergeFile\> with the system wide file, so that system changes are inherited. When the user deletes a menu item, you add `<Exclude><Filename>foo.desktop</Filename></Exclude>`. If the user adds a menu item, you use `<Include><Filename>foo.desktop</Filename></Include>`.

If the user moves a folder you can use \<Move\> elements to represent the move. \<Move\> elements used for menu-editing should always be added to the most top-level menu to ensure that moves are performed in the order in which they are specified; moves specified in child menus are always performed before moves specified in a more top level menu regardless of their location in the menu file.

To delete a folder, simply append the \<Deleted\> element.

When adding a new folder or moving an existing folder, menu editing implementations are advised not to re-use the menu path of a previously deleted folder.

Menu editors probably need to do some kind of consolidation/compression to avoid an XML tree that grows infinitely over time.
