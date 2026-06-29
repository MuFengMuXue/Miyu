# Nimf

Nimf is a multilingual input method framework which inherits Dasom.

## Installation
Install the  package.

## Input method engines
The following engines are bundled in :

* nimf-libhangul — for typing Korean hangul, based on
* nimf-anthy — for typing Japanese, based on
* nimf-chewing — for typing Chinese using Zhuyin, based on
* nimf-rime — for typing Chinese, based on

## Initial setup
Add the following lines to your desktop start up script files to register the input method modules and support XIM programs.

* Use .xprofile if you are using a graphical display manager like GDM, LightDM or SDDM.
* Use .xinitrc if you are using  or SLiM.

 export GTK_IM_MODULE=nimf
 export QT4_IM_MODULE="nimf"
 export QT_IM_MODULE=nimf
 export XMODIFIERS="@im=nimf"
 nimf &

Re-login to make these environment changes effective.

If you are using GNOME, you may need to run the following commands to use :

 $ gsettings set org.gnome.settings-daemon.plugins.keyboard active false
 $ gsettings set org.gnome.settings-daemon.plugins.xsettings overrides "{'Gtk/IMModule':}"

If the indicator does not display the current state, then run the instance explicitly:

 $ nimf-daemon
 $ nimf-indicator

## Editing Settings
Use  to edit nimf settings. You can launch  from your preferred terminal, or from the Nimf indicator menu which appears in system tray area.
