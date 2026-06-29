
How you set variables will depend on how sway was started. 
The explanation below was based in part on these [sources][webref1], with further details added by contributors to this wiki page.

Environment variables are inherited from the process that starts sway. You need to set variables there.

**We will discuss the following solutions:** 
- Display Manager (Which is usually also the login manager)
- systemd / environment.d: use the EnvironmentFile= key and an environment file
- PAM
- login shell: export them there before launching sway
- Distro-Specific solutions
    - Fedora

**Note**: The display manager and the login manager are usually the same program on modern distros (GDM/SDDM/LightDM). We will use Display Manager to refer to these programs, even though it's the login manager component they implement that actually responsible for launching the sway session.

## Display Manager

Solution depends on both your DM and distro. In addition to the other mechanisms described below, which your Display manager (GDM/SDDM/LightDM/etc') may or may not support, it may also source environment files from other locations, like your `.profile`, `.xprofile` or `.zprofile` files. It depends on the manager, and quite possibly on the whims of the packager who maintains its package in your distro.

## Systemd / environment.d

systemd provides the [environment.d][webref-envd] mechanism, which lets you set both system-wide, and per-user environment variables through config files. This is a systemd specific mechanism, so whether or not these variables propegate to sway depends on the setup. There are a couple of possible alternatives:

1. If Sway is launched as a systemd user service, then sway will have these environment.d variables in its environment. Therefore, every process you launch within sway will also inherit this environment, and so environment.d variables will be visible to them.
2. if Sway is launched via a display manager (like GDM/SDDM/LightDM), then sway is not technically managed by systemd, and environment.d variables will not automatically appear in its environment. However, the session script(s) invoked by the display manager when you login, **may** (or may not) explicitly import the systemd environment before launching the sway process. If it does, sway and the processes it launches will have environment.d variables defined in their process environment.  

**TL;DR** Users report that GDM/SDDM do import environment.d and, at least on fedora+LightDM, the session script provided by the `sway-config-fedora` package also import them. 
On other setups, you'll just have to test.

For more info: ```man environment.d```  

**Note**: changes to environment.d files do not immediately take effect. You must explicitly tell systemd to reread the environment.d files:
```
systemctl daemon-reload
systemctl import-environment
systemctl --user daemon-reload
systemctl --user import-environment 
```
Then, you must log out and back into sway.

**Note**: if you rely on the display manager to import environment.d variables, they will only be read if you actually log in using the display manager. If, for example, you start a headless wayvnc session in order to connect to sway from a remote machine, you've bypassed The display manager, and environment.d variables will not be read.

[Example with the SDDM Display manager][webref2], GDM also supports environment.d


## PAM
You can set environment variables through `pam_env`, however they will be set system-wide, including across different sessions and users.  
There are two ways you can configure PAM to load environment variables, by editing `/etc/security/pam_env.conf` or `/etc/environment`.

Example for `/etc/security/pam_env.conf` (`QT_QPA_PLATFORMTHEME` being the variable we want to edit, `qt5ct` being the value we want to set): 
```
QT_QPA_PLATFORMTHEME DEFAULT=qt5ct
```

Example for `/etc/environment` consisting of the same variable/value:
```
QT_QPA_PLATFORMTHEME=qt5ct
```

~You could also edit `~/.pam_environment` the same way you would with `/etc/environment`~, however this is disabled by default since [PAM 1.4.0][webref3a], and slated for removal since [PAM 1.5.0][webref3b] (2020). It is recommended that you do not rely on it for setting per-user environment variables.

For more information about this approach, see [this ArchWiki page][webref4].

## Login Shell

If you launch sway from your login shell, whatever is in your environment gets passed on to sway.
In particular, you can export variables in your ~/.zprofile or ~/.profile to make them available to sway and processes it launches.

Certain session scripts may also read these files, it depends. See section on the display manager.

## Distro-Specific solutions

### Fedora

The `sway-config-fedora` package (available since FC38) supports multiple ways of defining environment variables. 

**How it works**: The package provides a desktop session file `/usr/share/wayland-sessions/sway.desktop` for Display Managers, that invokes the session script `/usr/bin/start-sway`, also included in the package. 

- The session script import variables defined via systemd/environment.d (see section above).
- The session script also sources the system-global `/etc/sway/environment` file, and the user-specific `$HOME/.config/sway/environment` file, if they exist. 

Any variables defined by either of these mechanisms, will be visible to sway and any processes launched from it.

Tested on: FC42 (vanilla desktop, not a spin), using LightDM. (Oct 2025)

**Note**: Fedora also ships an alternative `sway-config-upstream` package, which does not provide support for defining env variables. I believe `sway-config-fedora` is installed by default only with the sway spin. I had to manually install it.

## Setting Variables in the Sway Config does NOT work

Variables defines in the sway config file via `set $foo bar` have nothing to do with process environment variables. You **cannot** define env variables this way.

Also, calling `exec sh -c 'export FOO=bar'` only defines an environment variable in a sub-shell that immediately exits. This has no effect on anything.


[webref1]: https://www.reddit.com/r/swaywm/comments/eewutx/how_to_set_environment_variables_before_starting/
[webref2]: https://github.com/gdamjan/sway-setup
[webref3a]: https://github.com/linux-pam/linux-pam/releases/tag/v1.4.0
[webref3b]: https://github.com/linux-pam/linux-pam/releases/tag/v1.5.0
[webref4]: https://wiki.archlinux.org/title/Environment_variables#Using_pam_env
[webref-envd]: https://man.archlinux.org/man/environment.d.5