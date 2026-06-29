# Paradox Launcher For Native Linux Games From GOG

The Paradox Launcher will fail to launch with the following error for native Linux versions of Paradox Interactive games from GOG if Heroic is running in a flatpak:

    Could not locate a valid installation of the Paradox Launcher:
    open /home/$USER/.var/app/com.heroicgameslauncher.hgl/data/Paradox Interactive/launcherpath: no such file or directory

To resolve, a simple symlink can be created with the following command:

`ln -s /home/$USER/.var/app/com.heroicgameslauncher.hgl/.local/share/Paradox\ Interactive /home/$USER/.var/app/com.heroicgameslauncher.hgl/data/Paradox\ Interactive`

> This only needs to be done once, even if you have multiple games with the Paradox Launcher experiencing this problem.

> Paradox staff are aware of the issue. The issue is likely to be properly fixed in a future update of the Paradox Launcher.
> https://forum.paradoxplaza.com/forum/threads/linux-the-launcher-fails-to-install-when-custom-xdg_data_home-is-set.1742531/
