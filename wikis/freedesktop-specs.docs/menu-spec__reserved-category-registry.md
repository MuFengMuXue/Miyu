## A.3 Reserved Categories

Reserved Categories have a desktop-specific meaning that has not been standardized (yet). Desktop entry files that use a reserved category MUST also include an appropriate OnlyShowIn= entry to restrict themselves to those environments that properly support the reserved category as used.

The table below describes Reserved Categories.

| Reserved Category | Description |
|----|----|
| Screensaver | A screen saver (launching this desktop entry should activate the screen saver) |
| TrayIcon | An application that is primarily an icon for the "system tray" or "notification area" (apps that open a normal window and just happen to have a tray icon as well should not list this category) |
| Applet | An applet that will run inside a panel or another such application, likely desktop specific |
| Shell | A shell (an actual specific shell such as `bash` or `tcsh`, not a TerminalEmulator) |
