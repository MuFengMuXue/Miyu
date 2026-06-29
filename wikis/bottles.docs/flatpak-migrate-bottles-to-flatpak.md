# Migrate directories to Flatpak

## Migrate to Flatpak

In recent versions of the Flatpak and, the bottles are saved in a different location than the other packages, respecting the structure of the Flatpak package.

#### Paths differences

The other packages save the essential Bottles files, such as components, temps, and bottles, in the directory: `$HOME/.local/share/bottles` . Flatpak saves these files in the Flatpak `data` directory: `$HOME/.var/app/com.usebottles.bottles/data/bottles`.

#### Migrate old bottles to Flatpak

The migration is simple as it sounds - just move (or copy) the content of the path `$HOME/.local/share/bottles` to the new one `$HOME/.var/app/com.usebottles.bottles/data/bottles`

```bash
# make a copy
yes | cp -rf \
$HOME/.local/share/bottles/* \
$HOME/.var/app/com.usebottles.bottles/data/bottles

# or move (using rsync to take care of existing files)
rsync -a \
$HOME/.local/share/bottles/* \
$HOME/.var/app/com.usebottles.bottles/data/bottles
```

Restart Bottles and that's it.
