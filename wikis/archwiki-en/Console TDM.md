# Console TDM

Console TDM is an extension for xorg-xinit written in pure bash. It is inspired by CDM, which aimed to be a replacement of display managers such as GDM.

## Installation
Install the  package.

Now ensure no other display managers get started by disabling their systemd services.

After installing Console TDM, you should modify your , and add a line:
 source /usr/bin/tdm
If you use zsh, add to your  the following line:
 bash /usr/bin/tdm
or
 tdm

Regardless of which shell is used you should edit  and replace your existing  line with:
 exec tdm --xstart

## Configuration
You should copy the links to your WM/DE starter to , and links to non-X programs to . For convenience, you can just run .

The use of the program  is much like , and it is a powerful tool to configure Console TDM.

You can customize Console TDM by editing  (sourced before the user is prompted for a session) and  (sourced before the session is actually started).
