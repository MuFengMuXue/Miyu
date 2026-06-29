[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Openbox&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Openbox "Openbox (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Openbox/ru "Openbox (100% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Installing Openbox]](#Installing_Openbox)
-   [[3] [Adjusting keybindings]](#Adjusting_keybindings)
    -   [[3.1] [Example: screen brightness]](#Example:_screen_brightness)
    -   [[3.2] [Example: volume keys (ALSA)]](#Example:_volume_keys_.28ALSA.29)

# [Overview]

The [Openbox Window Manager](http://openbox.org/wiki/Main_Page) is designed to be highly configurable and customisable with extensive standards support.

\

[![Openbox-wm-18.jpg](/images/thumb/3/35/Openbox-wm-18.jpg/600px-Openbox-wm-18.jpg)](//wiki.manjaro.org/index.php?title=File:Openbox-wm-18.jpg)

\

# [Installing Openbox]

For information on how to install a basic Openbox environment please review the [Openbox installation instructions](//wiki.manjaro.org/index.php?title=Install_Desktop_Environments#Openbox "Install Desktop Environments").

\

# [Adjusting keybindings]

Openbox is built to be customized, and this includes the ability to create your own custom **keybindings**. These are combinations of key presses that may be used to undertake virtually any action, usually much faster and more directly than other means, such as by sifting through a menu. Although the Manjaro Openbox Edition provides a user-friendly graphical interface that may be used to alter or create custom keybindings, some combinations of special keys are not easily managed through this interface.

In this instance it will be necessary to manually edit the Openbox `rc.xml` file. One of the many functions of this file is to store and enable keybindings in the Openbox environment. This file is located at `~/.config/openbox/rc.xml` and you can edit it with a standard [text editor](//wiki.manjaro.org/index.php?title=Viewing_and_editing_configuration_files "Viewing and editing configuration files").

## [Example: screen brightness]

Once the file has been opened, you will be presented with a substantial amount of commands contained within it. Don\'t worry about this, as you will only need to add a new block of code, rather than amend anything that is there. The code that must be added to enable full manual control over the screen brightness is as follows:

        <keybind key="XF86MonBrightnessUp">
          <action name="Execute">
            <command>xbacklight +10</command>
          </action>
        </keybind>
        <keybind key="XF86MonBrightnessDown">
          <action name="Execute">
            <command>xbacklight -10</command>
          </action>
        </keybind>

\

**Warning**

------------------------------------------------------------------------

This code cannot just be placed anywhere in the file. It must be placed in a particular section in order to work. Please follow the instructions below to do so.

To find the correct place to insert the above commands, it is recommended to use the **Find** or **Search** functions provided by your editor. If your text editor does not have the ability to search, it will be necessary to manually scroll down to about the mid-way point (perhaps using the **Page Down** key) to locate the following code:

    </keyboard>

The overall section of the code should look like this:

        </keybind>
       </keyboard>
      <mouse>

Once located, the new code above can be inserted between the \</keybind\> and \</keyboard\> codes. Press \<enter\> after the \</keybind\> code to provide a space to do so. Below is an example where this has taken place. The new code inserted has been **highlighted in green** for illustrative purposes:

        </keybind>
         <keybind key="XF86MonBrightnessUp">
           <action name="Execute">
             <command>xbacklight +10</command>
           </action>
         </keybind>
         <keybind key="XF86MonBrightnessDown">
           <action name="Execute">
             <command>xbacklight -10</command>
           </action>
        </keybind>
      </keyboard>
      <mouse>

If the command \"xbacklight +10\" does nothing, find out the minimum value to put instead of 10 by trying to set the brightness to 20, then 40. You can use the following commands:

-   \`xbacklight =X\` to change the brightness, and
-   \`xbacklight -get\` to see if the minimum value has been reached.

Once you have made the necessary amendments to the file, save the changes and close it.

Now logout and back in again for the changes to take effect.

\

## [][Example: volume keys (ALSA)]

Once the file has been opened, you will be presented with a substantial amount of commands contained within it. Don\'t worry about this, as you will only need to add a new block of code, rather than amend anything that is there. The code that must be added to enable full manual control over the volume (i.e. to raise, lower, and mute it) is as follows:

       <keybind key="XF86AudioRaiseVolume">
         <action name="Execute">
           <command>amixer set Master 10%+</command>
         </action>
      </keybind>
       <keybind key="XF86AudioLowerVolume">
         <action name="Execute">
           <command>amixer set Master 10%-</command>
         </action>
       </keybind>
       <keybind key="XF86AudioMute">
         <action name="Execute">
           <command>amixer set Master toggle</command>
         </action>
      </keybind>

\

**Warning**

------------------------------------------------------------------------

This code cannot just be placed anywhere in the file. It must be placed in a particular section in order to work. Please follow the instructions below to do so.

To find the correct place to insert the above commands, it is recommended to use the **Find** or **Search** functions provided by your editor. If your text editor does not have the ability to search, it will be necessary to manually scroll down to about the mid-way point (perhaps using the **Page Down** key) to locate the following code:

    </keyboard>

The overall section of the code should look like this:

        </keybind>
       </keyboard>
      <mouse>

Once located, the new code above can be inserted between the \</keybind\> and \</keyboard\> codes. Press \<enter\> after the \</keybind\> code to provide a space to do so. Below is an example where this has taken place. The new code inserted has been **highlighted in green** for illustrative purposes:

        </keybind>
        <keybind key="XF86AudioRaiseVolume">
          <action name="Execute">
            <command>amixer set Master 10%+</command>
          </action>
       </keybind>
        <keybind key="XF86AudioLowerVolume">
         <action name="Execute">
            <command>amixer set Master 10%-</command>
          </action>
        </keybind>
        <keybind key="XF86AudioMute">
          <action name="Execute">
            <command>amixer set Master toggle</command>
          </action>
       </keybind>
      </keyboard>
      <mouse>

Once you have made the necessary amendments to the file, save the changes and close it.