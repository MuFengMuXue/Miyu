DOSBox is a DOS-emulator that uses the SDL-library which makes DOSBox
very easy to port to different platforms. DOSBox also emulates
CPU:286/386 realmode/protected mode. We use it to replace our Virtual
8086 Mode.

We started searching for native dosbox on non-x86 targets with
wine-1.3.12. For Wine releases 1.3.30 and later, we added code in Wine
and DOSBox for more compatiblity.

For the updated DOSBox code, you need at least DOSBox 0.74-2, since
DOSBox 0.75 is not yet released. For DOSBox 0.74 there are also patched
versions available in some Distributions, for example since October 2015
Debian and Ubuntu ships them in their dosbox 0.74-4.1 and Gentoo ships
it in dosbox-0.74-r1 since June 2016.

### Related Wine Bugs

- ~~Bug #18118~~

- ~~Bug #25887~~

- ~~Bug #26423~~

### See also

- [DOSBox commit for changing the
  Z-Drive](https://sourceforge.net/p/dosbox/code-0/3736/tree/)
  ([diff](https://sourceforge.net/p/dosbox/code-0/3736))

- [DOSBox commit for Wine style name
  mangling](https://sourceforge.net/p/dosbox/code-0/3743/tree/)
  ([diff](https://sourceforge.net/p/dosbox/code-0/3743/))

- [DOSBox.com](https://www.dosbox.com/)
