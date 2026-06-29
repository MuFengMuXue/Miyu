Other languages:

[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Improve_Font_Rendering/tr "Yazı Tipi Oluşturmayı Geliştirin (53% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Improve_Font_Rendering/ru "Улучшение рендеринга шрифтов (100% translated)")

## Contents

-   [[1] [How to improve font rendering with your installed fonts]](#How_to_improve_font_rendering_with_your_installed_fonts)
-   [[2] [See Also]](#See_Also)

## [How to improve font rendering with your installed fonts]

A little configuration maybe required to render the fonts in an optimal manner. Follow the steps illustrated below.

\
*1. Create the global fontconfig setting file /etc/fonts/local.conf*

[user \$ ][ sudo nano /etc/fonts/local.conf [COPY TO CLIPBOARD]]

\

Paste the following content in the file

    <?xml version="1.0"?>
    <!DOCTYPE fontconfig SYSTEM "fonts.dtd">
    <fontconfig>
      <match target="font">
        <edit name="antialias" mode="assign">
          <bool>true</bool>
        </edit>
        <edit name="hinting" mode="assign">
          <bool>true</bool>
        </edit>
        <edit mode="assign" name="rgba">
          <const>rgb</const>
        </edit>
        <edit mode="assign" name="hintstyle">
          <const>hintslight</const>
        </edit>
        <edit mode="assign" name="lcdfilter">
          <const>lcddefault</const>
        </edit>
      </match>
    </fontconfig>

\
After that save the file.

\
*2. Create backup of \~/.Xresources file:*

[user \$ ][ cp \~/.Xresources \~/.Xresources.bak [COPY TO CLIPBOARD]]

\

If the .Xresources file has not been already created and you get the error

***\"cp: cannot stat '\~/.Xresources': No such file or directory\"***, then skip to step No. 3.

\
*3. Open/Create \~/.Xresources file in text editor:*

[user \$ ][ nano \~/.Xresources [COPY TO CLIPBOARD]]

\

If the following is not already present, paste at the end of the file or edit existing values:

    Xft.antialias: 1
    Xft.hinting: 1
    Xft.rgba: rgb
    Xft.hintstyle: hintslight
    Xft.lcdfilter: lcddefault

Save changes to the file.

\
*4. Run the following command in terminal:*

[user \$ ][ xrdb -merge \~/.Xresources [COPY TO CLIPBOARD]]

\

\
*5. Make sure that* Anti aliasing is **On**, Hinting is set to **Slight** *and RGBA (subpixel) order is set to **rgb** in System Settings (Appearance).*

\
*6. Create symbolic links with some available presets from /usr/share/fontconfig/conf.avail/ to /etc/fonts/conf.d/*

[user \$ ][ sudo ln -s /usr/share/fontconfig/conf.avail/10-sub-pixel-rgb.conf /etc/fonts/conf.d/ [COPY TO CLIPBOARD]]

\

[user \$ ][ sudo ln -s /usr/share/fontconfig/conf.avail/10-hinting-slight.conf /etc/fonts/conf.d/ [COPY TO CLIPBOARD]]

\

[user \$ ][ sudo ln -s /usr/share/fontconfig/conf.avail/11-lcdfilter-default.conf /etc/fonts/conf.d/ [COPY TO CLIPBOARD]]

\

\
*7. Set preferred serif, sans-serif and monospace fonts (optional)*

Create local fontconfig folder and setting file

[user \$ ][ mkdir -p \~/.config/fontconfig/ [COPY TO CLIPBOARD]]

\

[user \$ ][ nano \~/.config/fontconfig/fonts.conf [COPY TO CLIPBOARD]]

\

Paste the following content in the file

    <?xml version="1.0"?>
    <!DOCTYPE fontconfig SYSTEM "fonts.dtd">
    <fontconfig>
      <alias>
        <family>serif</family>

          <family>Liberation Serif</family>
        </prefer>
      </alias>
      <alias>
        <family>sans-serif</family>

          <family>Liberation Sans</family>
        </prefer>
      </alias>
      <alias>
        <family>sans</family>

          <family>Liberation Sans</family>
        </prefer>
      </alias>
      <alias>
        <family>monospace</family>

          <family>Liberation Mono</family>
        </prefer>
      </alias>
      <alias>
        <family>mono</family>

          <family>Liberation Mono</family>
        </prefer>
      </alias>
    </fontconfig>

\

*8. Finally enable freetype2 infinality mode and reboot your computer.*

add line to end of freetype2 config file and then rebuild fontconfig cache

[user \$ ][ sudo nano /etc/profile.d/freetype2.sh [COPY TO CLIPBOARD]]

\

[user \$ ][ export FREETYPE_PROPERTIES=\"truetype:interpreter-version=38\" [COPY TO CLIPBOARD]]

\

[user \$ ][ sudo fc-cache -fv [COPY TO CLIPBOARD]]

\

## [See Also]

[The Arch Wiki](https://wiki.archlinux.org/index.php/Font_Configuration)