# For AMD users having issues with non-OpenGL games

Vulkan requires the `amdgpu` driver, it doesn't detect the graphics adapter when using `radeon`.

If you're experiencing crashes or the game doesn't load at all, it's probably because your distribution defaults to the `radeon` driver and Vulkan may be using Intel's graphics adapter instead (if available).

If that's the case, `amdgpu` has to be enabled explicitly in the kernel commandline.

## Instructions for Debian/Ubuntu

Open your terminal and run `sudo nano /etc/default/grub`.

Append to `GRUB_CMDLINE_LINUX_DEFAULT`:
- `radeon.si_support=0 amdgpu.si_support=1` if you have a Southern Islands card.
- `radeon.cik_support=0 amdgpu.cik_support=1` if you have a Sea Islands card.

For example: `GRUB_CMDLINE_LINUX_DEFAULT="quiet radeon.cik_support=0 amdgpu.cik_support=1"`

Note: You can safely append both variants if you are unsure which family your card belongs to.

Save with `CTRL+X` followed by `Y` and then `Enter`.

Run `sudo update-grub` and then reboot your system.

You can check which driver is loaded by running `lspci -k`:
```
01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Hawaii PRO [Radeon R9 290/390]
        Subsystem: PC Partner Limited / Sapphire Technology Hawaii PRO [Radeon R9 290/390]
        Kernel driver in use: amdgpu
        Kernel modules: radeon, amdgpu
```

If your desktop environment doesn't load, check the kernel log by running `sudo dmesg`. If you see that `amdgpu` is crashing, append `amdgpu.dc=0` to the kernel commandline.

## Instructions for Arch Linux

https://wiki.archlinux.org/index.php/AMDGPU

## Instructions for Gentoo Linux

https://wiki.gentoo.org/wiki/AMDGPU

## If you're still encountering issues

Write a message in https://github.com/ValveSoftware/Proton/issues/813.