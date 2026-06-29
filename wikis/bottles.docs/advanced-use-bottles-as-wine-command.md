# Use Bottles as wine command

In some specific cases it may be useful to have Bottles as a system WINE command, for example when a program needs to access the command and we want it to use a specific bottle.

### Custom wine command

Make sure you don't have wine installed on your system before proceeding.

Make a new file named `wine` in `$HOME/.local/bin` or any directory in your `PATH` with the following content:

```
#!/bin/sh
flatpak run --command='bottles-cli' com.usebottles.bottles run -b MyBottle -e "$@"
```

or the following if you are not using the Flatpak:

```
#!/bin/sh
bottles-cli  run -b MyBottle -e "$@"
```

and change `MyBottle` to the name of your chosen bottle. Then make it executable:

```
chmod +x $HOME/.local/bin/wine
```

### Usage

Now just run:

```
wine program_name.exe # or installer_name.msi
```

to launch it with Bottles. It will automatically use your chosen bottle.
