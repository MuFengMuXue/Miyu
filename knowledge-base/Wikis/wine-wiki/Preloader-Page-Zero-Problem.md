Running Wine on recent versions of Linux (in particular Ubuntu 8.04,
Hardy Heron, and Fedora 9) may generate errors or warnings such as

```
preloader: Warning: failed to reserve range 00000000-60000000
err:dosmem:setup_dos_mem Cannot use first megabyte for DOS address space, please report
```

or

```
winevdm: unable to exec 'Z:\tmp\CONFIG.EXE': DOS memory range unavailable
```

and may refuse to run Wine applications, especially ones that use DOS
calls. For instance, Microsoft Word 2000 will crash after a few seconds
(does this still happen in rc1?)

This is due to a [Linux security
patch](https://kerneltrap.org/Linux/Patching_CVE-2008-0600_Local_Root_Exploit).

One bad workaround is to run as root. **Don't do that.** If you do this,
your .wine directory will be screwed up, and can't be used anymore
without running as root. (To recover from this, either delete your .wine
directory as root, or maybe use `chown -R $LOGNAME .wine` to fix
ownership.)

The right workaround is to give the command:

```sh
sudo sysctl -w vm.mmap_min_addr=0
```

This fixes the problem until the next time you reboot. (It also reduces
security slightly.)

To avoid having to give that same command every time you reboot, also
edit the file \`/etc/sysctl.conf\`, e.g. with the command

```sh
sudo gedit /etc/sysctl.conf
```

and change the line that reads:

```
vm.mmap_min_addr = 65536
```

to:

```
vm.mmap_min_addr = 0
```

That will apply the workaround for you when the system starts.

On Ubuntu 8.10 (Intrepid) and later, the workaround is different: the
line needs to go in /etc/sysctl.d/wine.conf. e.g. with the command

```sh
sudo gedit /etc/sysctl.d/wine.conf
```

add the single line

```
vm.mmap_min_addr = 0
```

The budgetdedicated.com packages for Intrepid, as well as those shipped
with Intrepid, already have this workaround included.

Related bugs:

- Wine bug #7848 ("unable to run DOS programs")
- Wine bug #12516 ("err:dosmem:setup_dos_mem error report on every run of Wine")
- Wine bug #19732 ("Security: use CAP_SYS_RAWIO during start up to map
  the memory below mmap_min_addr instead of permanently lowering it at
  install time")
- Wine bug #20578 ("Debian/Ubuntu packages do not follow proper format
  for /etc/sysctl.d")

For more info, see

- <https://bugs.launchpad.net/ubuntu/+source/procps/+bug/256025>
- <https://launchpad.net/bugs/114025>
- <https://kerneltrap.org/Linux/2.4.36_Stable_Release>
- <https://kerneltrap.org/Linux/Patching_CVE-2008-0600_Local_Root_Exploit>
