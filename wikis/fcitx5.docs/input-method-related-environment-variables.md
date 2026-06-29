# Input Method Related Environment Variables

This page introduces the meaning of following environment variables. You don't need to understand it to use Fcitx, but it might help when you meet some problem, and let you examine what's going wrong.

## XMODIFIERS

This variable affects XIM only. The format is

XMODIFIERS=@im=<xim server name>

When XIM server starts, it register a name, which will be used here. The name can not be same as other XIM server, so you cannot run two Fcitx under same X server. In general case, the XIM server name of Fcitx will be fcitx.

So the settings for Fcitx will be

XMODIFIERS=@im=fcitx

In non-CJK locale, if this variable is not specified, XIM will not work for some application, which means you should always set it. And XIM will also need you to have correct locale, which means your locale is must in the output of

locale -a

You can check your locale by

locale

In order to use XIM, your locale also must NOT be C or POSIX.

## GTK_IM_MODULE

This will override the system automatic gtk im module selection. By default gtk select im module by the language provided by im module. Fcitx declares that it support "zh:ja:ko:\*". And this information will be record in a file, on most linux system it's /etc/gtk-2.0/gtk.immodules and /etc/gtk-3.0/gtk.immodules, or suffixed with -32 or -64.

You need to use

gtk-query-immodules-2.0 \> \<gtk-2.0 immodule file\>

to do update for gtk2.

Or if your gtk2 version is newer than 2.24.20, you should use

gtk-query-immodules-2.0 --update-cache

instead just like gtk3.

and

gtk-query-immodules-3.0 --update-cache

to do update for gtk3.

Otherwise new im module will not be recognized.

If no im module specified by GTK_IM_MODULE is found, it will fallback to auto select method.

## QT_IM_MODULE

Qt's im module is similar with Gtk, but don't need extra file to recognize. If QT_IM_MODULE is not specified, qtconfig (Ubuntu/Debian/ArchLinux qtconfig-qt4) can be used to configure the default one.

Otherwise it will be override by QT_IM_MODULE.

## LC_CTYPE

System locale should not be changed in all case. It might brings unpredictable effect.

This should only be used in some case, including emacs and java. Emacs has a [historical bug](http://lists.gnu.org/archive/html/bug-gnu-emacs/2012-02/msg00761.html), that under en_US.UTF-8 or similar locale, it will never use XIM (Though emacs is a gtk app, it use XIM). The only way to walkaround this is to use LC_CTYPE to fix this.

For example, to only set this with emacs, run emacs with

LC_CTYPE=zh_CN.UTF-8 emacs

It will not effect the display language of emacs.

Notice, even if you are not using Chinese, you should also try to set it so LC_CTYPE=zh_CN.UTF-8, due to some limitation of XIM.
