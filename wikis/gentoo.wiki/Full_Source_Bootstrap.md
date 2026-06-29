**[Full Source Bootstrap](https://guix.gnu.org/manual/en/html_node/Bootstrapping.html)** refers to building everyting from source with minimal binaries.

## [Preparing]

** Note**\
The instructions follow from this [text file](https://mid-kid.root.sx/git/mid-kid/bootstrap/src/branch/master/gentoo-2025/gentoo.txt).

First, download from fosslinux:

`user `[`$`]`git clone --depth=1 --recursive `[`https://github.com/fosslinux/live-bootstrap`](https://github.com/fosslinux/live-bootstrap)

`user `[`$`]`cd live-bootstrap`

Then download the required files:

`user `[`$`]`./download-distfiles.sh`

If this does not work, try downloading from [link](https://github.com/fosslinux/live-bootstrap/wiki/Mirrors):

`user `[`$`]`./download-distfiles.sh `[`https://live-bootstrap.stikonas.eu/`](https://live-bootstrap.stikonas.eu/)

Now bootstrap from scratch:

`root `[`#`]`./rootfs.py -c --external-sources --cores $(nproc)`