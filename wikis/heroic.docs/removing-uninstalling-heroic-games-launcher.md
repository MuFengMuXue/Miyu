# Removing Uninstalling Heroic Games Launcher

Depending on the Operating System and the method Heroic was installed, the way to get rid of it completely changes.

## Linux

### Native package (.deb, .rpm, etc)

- Uninstall Heroic using your package manager
- Delete Heroic's config folder: `/home/<your user>/.config/heroic`
- If you want, delete the folder where games are installed (defaults to `/home/<your user>/Games/Heroic`)
- If you want, delete the folder where the prefixes are created (defaults to `/home/<your user>/Games/Heroic/Prefixes`)

### AppImage

- Delete the `.appImage` file
- Delete Heroic's config folder: `/home/<your user>/.config/heroic`
- If you want, delete the folder where games are installed (defaults to `/home/<your user>/Games/Heroic`)
- If you want, delete the folder where the prefixes are created (defaults to `/home/<your user>/Games/Heroic/Prefixes`)

### Flatpak

- Uninstall Heroic using your flatpaks' manager (i.e.: Discover on the Steam Deck), or run `flatpak uninstall com.heroicgameslauncher.hgl` on a terminal
- Delete Heroic's config folder: `/home/<your user>/.var/app/com.heroicgameslauncher.hgl`
- If you want, delete the folder where games are installed (defaults to `/home/<your user>/Games/Heroic`)
- If you want, delete the folder where the prefixes are created (defaults to `/home/<your user>/Games/Heroic/Prefixes`)


## Mac

- Delete the `.app` file from your Applications directory
- Delete Heroic's config folder: `/Users/<your user>/Library/Application Support/heroic`
- If you want, delete the folder where games are installed (defaults to `/Users/<your user>/Games/Heroic`)
- If you want, delete the folder where the prefixes are created (defaults to `/Users/<your user>/Games/Heroic/Prefixes`)


## Windows

### Installable

- Use the uninstaller or uninstall with the app manager if one was used
- Delete Heroic's config folder: `C:\Users\<your user>\AppData\Local\Programs\heroic`
- If you want, delete the folder where games are installed (defaults to `C:\Users\<your user>/Games/Heroic`)
- If you want, delete the folder where the prefixes are created (defaults to `C:\Users\<your user>/Games/Heroic/Prefixes`)

### Portable

- Delete the portable `.exe` file
- Delete Heroic's config folder: `C:\Users\<your user>\AppData\Local\Programs\heroic`
- If you want, delete the folder where games are installed (defaults to `C:\Users\<your user>/Games/Heroic`)
- If you want, delete the folder where the prefixes are created (defaults to `C:\Users\<your user>/Games/Heroic/Prefixes`)
