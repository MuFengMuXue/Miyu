# Fbpanel

fbpanel is a lightweight NETWM compliant desktop panel.

## Installing
Install the  package.

## Starting
If you want to start fbpanel with your X session, add the following line to your  before the line where you start your window manager:

 fbpanel &

## Configuration
You can find the configuration file in . If it does not exist, copy over the default configuration file:

 $ mkdir ~/.config/fbpanel
 $ cp /usr/share/fbpanel/default ~/.config/fbpanel

## wincmd plugin (show desktop button)
This plugin is enabled by default, but it might not show up because it cannot find an existing icon. In that case, change the icon path to one that points to an existing icon. You can also use an image as its icon. In that case, replace the  key with :

{{bc|1=
Plugin {
    type = wincmd
    config {
        image = ~/images/my_image.png
        tooltip = Left click to iconify all windows. Middle click to shade them.
    }
}
}}
