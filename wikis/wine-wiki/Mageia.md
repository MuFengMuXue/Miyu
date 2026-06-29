<small>
&nbsp;[:flag_cn: 简体中文](zh_CN/Mageia)
</small>

-----

## Installing WineHQ Packages

**Packages for Mageia have been discontinued as of 2018-12-19. Old
packages are still available in the repository.**

(64 bit Mageia) Enable multiarch:

```
sudo dnf config-manager --set-enabled mageia-i586 updates-i586
```

Add the repository:

```
sudo dnf config-manager --add-repo https://dl.winehq.org/wine-builds/mageia/6/winehq.repo
```

Install **one of the following packages**:

|                    |                                   |
|--------------------|-----------------------------------|
| Development branch | `sudo dnf install winehq-devel`   |
| Stable branch      | `sudo dnf install winehq-stable`  |
| Staging branch     | `sudo dnf install winehq-staging` |
