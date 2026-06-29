# Plymouth

Plymouth is a project from Fedora and now listed among the freedesktop.org's official resources providing a flicker-free graphical boot process. It relies on kernel mode setting (KMS) to set the native resolution of the display as early as possible, then provides an eye-candy splash screen leading all the way up to the login manager.

## Preparation
Plymouth primarily uses KMS to display graphics, but on UEFI systems it can utilize the EFI framebuffer.

If you have neither KMS nor a framebuffer, Plymouth will fall back to text-mode.

## Installation
Plymouth can be installed with the  package.

By default, Plymouth logs the boot messages into , and does not show the graphical splash screen.

* If you want to see the splash screen, append  to the kernel parameters.
* If you want silent boot, append  too.
* If you want to disable the logging, append . Alternatively, add  which also disables console redirection.

To start Plymouth on early boot, you must configure your initramfs generator to create images including Plymouth.

## mkinitcpio
Add  to the  array in mkinitcpio.conf.

If you are using the  hook, it must be before .

Furthermore make sure you place  before the  or  hook if your system is encrypted with dm-crypt.

Finally, regenerate the initramfs.

## dracut
After installing Plymouth, dracut will automatically detect it and add it to your initramfs images. If autodetection fails, you can force dracut to include Plymouth by adding the following line to your dracut configuration:

## Configuration
Plymouth can be configured in file . You can see the default values in .

## Changing the theme
Plymouth comes with a selection of themes:

# BGRT: A variation of Spinner that keeps the OEM logo if available (BGRT stands for Boot Graphics Resource Table)
# Fade-in: "Simple theme that fades in and out with shimmering stars"
# Glow: "Corporate theme with pie chart boot progress followed by a glowing emerging logo"
# Script: "Script example plugin" (Despite the description seems to be a quite nice Arch logo theme)
# Solar: "Space theme with violent flaring blue star"
# Spinner: "Simple theme with a loading spinner"
# Spinfinity: "Simple theme that shows a rotating infinity sign in the center of the screen"
# Tribar: "Text mode theme with tricolor progress bar"
# Text: "Text mode theme with tricolor progress bar"
# Details: "Verbose fallback theme"

Arch sets the default theme to bgrtThis can be confirmed by running:

 $ plymouth-set-default-theme

The theme can be changed by editing the configuration file:

or by running:

 # plymouth-set-default-theme -R theme

Every time a theme is changed, the initramfs must be rebuilt. The  option ensures that it is rebuilt (otherwise regenerate the initramfs manually).

## Install new themes
You can install other themes from AUR. [https://aur.archlinux.org/packages?K=plymouth-theme-, alternatively
 provides integration into KDE Plasma's settings and offers themes not available on the AUR.

All currently installed themes can be listed by using this command:

 $ plymouth-set-default-theme -l

or:

## Show delay
Plymouth has a configuration option to delay the splash screen:

On systems that boot quickly, you may only see a flicker of your splash theme before your DM or login prompt is ready. You can set  to an interval (in seconds) longer than your boot time to prevent this flicker and only show a blank screen. The default is 0 seconds, so you should not need to change this to a different value to see your splash earlier during boot.

## HiDPI
Edit the configuration file:

and regenerate the initramfs.

## Tips and tricks
## Show boot messages
During boot you can switch to boot messages by pressing the  key.

## Smooth transition
GDM supports smooth transition out of the box.

## Preview themes
The currently configured theme can be previewed by running this command in your getty# plymouthd; plymouth --show-splash; sleep 5; plymouth --quit

## Change background image
You can add a background image for two-step-based themes (such as spinner and bgrt). Just place your desired image into . Do not forget to regenerate the initramfs once the theme changed.

## Missing BGRT image
In case you are using the BGRT theme but the UEFI does not provide a vendor logo, you can place a fallback image into  to show it instead.

Alternatively, set the following to keep the firmware background:

## Slow down boot to show the full animation
On systems with a very fast boot time, it might be necessary to add a delay to  with a drop-in snippet containing  if showing the whole animation is desired. See [https://old.reddit.com/r/archlinux/comments/u5fjbi/how_do_i_make_my_boot_time_slower/ this reddit post.

Alternatively, it is possible to use a new systemd service starting at the same time as plymouth and waiting the whole duration needed for the animation. This method will ensure that inconsistencies in the boot time will not be perceived, as it is not time added after the animation but a delay running during the animation.

Then enable the service.

## Using SimpleDRM
On devices using UEFI, Plymouth uses the SimpleDRM driver by default to display the boot splash on the UEFI framebuffer. This allows the boot splash to appear on faster machines where loading the GPU driver takes too long (for example, systems with AMD GPUs), and also removes any flicker between the motherboard splash screen and Plymouth.

On old UEFI systems where efifb does not come up in native mode, but rather in 640x32, 800x600 or 1024x768, Plymouth will not use SimpleDRM by default.

To disable SimpleDRM, append  to your kernel parameters. See Plymouth issue 264 for more information about this option.

## Troubleshooting
## Disable with kernel parameters
If you experience problems during boot, you can temporary disable Plymouth with the following kernel parameters:

 plymouth.enable=0 disablehooks=plymouth

## Debugging
To write debug output into , add the following kernel parameter:

 plymouth.debug

## Password prompt does not update
When using  instead of  hooks in Mkinitcpio, the password prompt may not update on themes that handle it via Plymouth scripting.

You can try switching to development version  or using substitutes from Mkinitcpio#Common hooks.

## Display is not centered
Certain themes may have trouble centering the display when there is more than one monitor enabled during boot.

You can use Kernel mode setting#Forcing modes to disable specific monitors.
