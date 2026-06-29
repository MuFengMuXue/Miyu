# MacBookPro10,x

This page covers the following Apple models:
* MacbookPro10,1 MacBook Pro 15" Retina 2012 and Early 2013
* MacBookPro10,2 MacBook Pro 13" Retina 2012 and Early 2013

## Installation
## Preparing the Hard drive
Assuming you want to dual boot with OS X, you have to shrink its partition with the Disk Utility. You can either create your Linux partition directly here, or do that later in Linux during the installation (using  and ).

## Getting wireless firmware
In order for the Wi-Fi chipset to work, you need to get the firmware for it. You can just copy it from another b43-enabled Arch, extract it from Broadcom's driver using , or get the firmware through the  package. In the end, you should have a folder named  with a lot of  files in it.

## Booting the live image
Hold the option key, then press the power button. After a few seconds, you should see Apple's boot loader display the choice of either starting up the built-in drive with OS X or the USB drive you plugged in.

Select the live USB with the arrow keys, and press Enter to boot into the live Arch Linux environment.

## Connecting to WiFi
Copy the entire folder with the firmware for your wireless card to .

## The installation
Run the installation wizard. When asked to partition your hard drive, create a small HFS partition. This is where you put the standalone GRUB package after the installation.
The rest of the installation is pretty much the same as usual. When choosing the boot loader, select GRUB, and install it. Do not worry about any errors; we will create the bootable EFI image on our own afterwards.

After the installation has completed, directly copy the WiFi firmware to the installed system to .

Alternatively, install  to improve WiFi.

## Boot loader
## Direct EFI booting
As of August 2013, rEFInd can autodetect the Arch kernel, removing the need for copying the kernel into the EFI system partition. Simply install  and enable the  and  options in , see boot loader for instructions.

## GRUB
Another solution is to install GRUB. Edit  and edit the boot entry to load Linux mainline instead of the normal one. Also append  to the kernel line again.

Now cd into  and create the GRUB image by calling:

 grub-mkstandalone -o grub-standalone-x86_64.efi -d usr/lib/grub/x86_64-efi -O x86_64-efi -C xz boot/grub/grub.cfg

This will create file called  which contains GRUB and the config file. It is important to  into the right directory to make it pick up the config file and put it into the right place within the image.

Copy this file to the HFS partition you have created earlier. Downside of this method is that you need to repeat this step whenever you want to change the GRUB config.

Reboot the machine and boot into OS X. The HFS partition should be mounted and the GRUB standalone image in there. Follow the steps on this page to create the files needed to make the Apple boot loader pick up GRUB: https://mjg59.dreamwidth.org/7468.html.

After creating the files, use  on the GRUB image on the partition. If you want to boot automatically to Arch, append .

After another reboot, you should be able to select your installed Arch Linux by keeping the alt button pressed while booting in case you have not used  while blessing.

## Wi-Fi
The Macbook Pro 10,x comes with the Broadcom BCM4331 Wireless Chipset.

There are two major options to get this chipset working in Arch Linux:

The  package contains the open-source, reverse-engineered firmware for the chipset.

The  and  packages ship with the propriety, restricted-license drivers for the chipset.

See Broadcom wireless for more information.

## Graphics
## General Notes
The Laptop comes with an nVidia and an Intel chip. Since this device comes with a Retina (HiDPI) display, things may be really small with native resolution for some desktop environments: see HiDPI.

## Nouveau backlight
If you are using the open-source Nouveau drivers and the active GPU is the Nvidia card, backlight levels can be adjusted by echoing a value to a file:

 # echo 500 > /sys/class/backlight/gmux_backlight/brightness

To bring the backlight to its maximum level:

 # echo $(cat /sys/class/backlight/gmux_backlight/max_brightness) > /sys/class/backlight/gmux_backlight/brightness

## NVIDIA backlight
If you are using the propriety nvidia drivers, note that the backlight adjustment will not work out of the box.

To enable backlight control:

 # setpci -v -H1 -s 00:01.00 BRIDGE_CONTROL=0

## Switching to/from GPUs with gpu-switch
You can switch the display output to and from the discrete or integrated intel GPU from within Arch Linux with  if you are using the open-source  and  drivers.

Installation

You can install  from the AUR.

Then, just run the script as root.

Usage

The command switches are , to switch to the integrated card, and  for switching to the discrete GPU. In order to have the changes take effect, you will need to reboot.

## Switch to Intel integrated GPU and turn off discrete Nvidia GPU
To switch to intel card and poweroff the discrete GPU:

 $ /path/to/gpu-switch -i

Then reboot.

Poweroff the discrete GPU using :

 # echo OFF > /sys/kernel/debug/vgaswitcheroo/switch

This will take a second or to complete.

Then, check whether the discrete GPU is still on:

This is useful if you have opted to have an Arch Linux-only installation and cannot access the OS X-only tool iGPU.

## Keeping the discrete GPU off at boot
If you want to keep the discrete GPU off at boot, see .

## Graphic artifacting under b43-firmware
While on integrated graphics with the b43-firmware package, you might encounter moderate to severe graphic artifacting that appears to be correlated to wireless network traffic. (disconnected->no artifacting, connected->periodic artifacting, large transfer->severe artifacting/unusuable) This can be resolved by removing/blacklisting  and using either  or .

## Enable Vsync
To prevent screen tearing, see Intel graphics#Tearing.

## Issues
Using vgaswitcheroo to switch between iGPU / dGPU on the 15" version will result in a black screen. The system is still running and can be rebooted safely.

The dGPU/nouveau is active on boot. As of 3.10.3-1, the only known way to switch to the iGPU/intel is to force this through gfxCardStatus v2.2.1 on MacOS (later versions of gfxCardStatus do *not* work.) This setting will survive reboots. To revert it, you must reboot into MacOS *twice* and/or reset the SMC (shutdown and press shift+control+alt+power at the same time. Press power again to boot.)

Another way to force iGPU/intel is to add following commands into one of the  in ,

The screen will remain blank until intel driver is fully loaded. Notice that dGPU will not be powered down (adding code above will prevent the system from booting up). Workaround is to compile and run following program (need ) after system is fully booted up.
{{bc|1=
#include
#include

#define GMUX_PORT_SWITCH_DISPLAY	0x10
#define GMUX_PORT_SWITCH_DDC		0x28
#define GMUX_PORT_SWITCH_EXTERNAL	0x40
#define GMUX_PORT_DISCRETE_POWER	0x50
#define GMUX_PORT_VALUE			0xc2
#define GMUX_PORT_READ			0xd0
#define GMUX_PORT_WRITE			0xd4

#define GMUX_IOSTART		0x700

typedef unsigned char u8;

enum discrete_state {STATE_ON, STATE_OFF};
enum gpu_id {IGD, DIS};

static void index_write8(int port, u8 val)
{
	outb(val, GMUX_IOSTART + GMUX_PORT_VALUE);
	outb((port & 0xff), GMUX_IOSTART + GMUX_PORT_WRITE);
}

static u8 index_read8(int port)
{
	u8 val;
	outb((port & 0xff), GMUX_IOSTART + GMUX_PORT_READ);
	val = inb(GMUX_IOSTART + GMUX_PORT_VALUE);

	return val;
}

static void set_discrete_state(enum discrete_state state)
{
	if (state == STATE_ON) {	// switch on dGPU
		index_write8(GMUX_PORT_DISCRETE_POWER, 1);
		index_write8(GMUX_PORT_DISCRETE_POWER, 3);
	} else {			// switch off dGPU
		index_write8(GMUX_PORT_DISCRETE_POWER, 1);
		index_write8(GMUX_PORT_DISCRETE_POWER, 0);
	}
}

static u8 get_discrete_state()
{
	return index_read8(GMUX_PORT_DISCRETE_POWER);
}

static void switchto(enum gpu_id id)
{
	if (id == IGD) {	// switch to iGPU
		index_write8(GMUX_PORT_SWITCH_DDC, 1);
		index_write8(GMUX_PORT_SWITCH_DISPLAY, 2);
		index_write8(GMUX_PORT_SWITCH_EXTERNAL, 2);
	} else {		// switch to dGPU
		index_write8(GMUX_PORT_SWITCH_DDC, 2);
		index_write8(GMUX_PORT_SWITCH_DISPLAY, 3);
		index_write8(GMUX_PORT_SWITCH_EXTERNAL, 3);
	}
}

int main(int argc, char **argv)
{
	if (iopl(3)

"rmmod nouveau" will crash if the dGPU is manually powered off via vgaswitcheroo. Once this happens, it will be impossible to shutdown / reboot cleanly. Fresh patches (2 August) will hopefully fix this in the future. (Note: to enter this failure state, you must use gfxCardStatus to force the iGPU, then use vgaswitcheroo explicitly. This is rather uncommon.)

The dGPU / iGPU issues do not affect the 13" rmbp, which only has an intel adapter. Much simpler!

Nvidia drivers 319.32 fail to suspend / resume or control the backlight out of the box.

Nouveau and intel work fine.

If you are experiencing problems with Nvidia drivers, try using emulated BIOS boot instead of EFI boot.

## Audio
On the MacBookPro10,2 you may need to use the 'snd_hda_intel' driver with the model option 'mbp101'. This model option goes in the modprobe configuration; for example, add the following to /etc/modprobe.d/alsa-base.conf (forum post):
  options snd-hda-intel model=mbp101

Note this model option is undocumented in the list of models available online, but it works admirably. (Until you do this, the sound may seem fine through HDMI, but the built-in speakers and internal microphone may not work properly.)

For additional microphone troubleshooting tips, see Advanced Linux Sound Architecture/Troubleshooting#Microphone.

## Touchpad
While  will work, the integrated button of the touchpad may cause issues. Using the  driver, with a tweaked configuration should lead to a better end result:

The following config uses a single touch for left, two for middle, three for right:
 Section "InputClass"
     MatchIsTouchpad "on"
     Identifier      "Touchpads"
     Driver          "mtrack"
     Option          "Sensitivity" "0.65"
     Option          "IgnoreThumb" "true"
     Option          "IgnorePalm" "true"
     Option          "TapButton1" "1"
     Option          "TapButton2" "3"
     Option          "TapButton3" "2"
     Option          "ClickFinger1" "1"
     Option          "ClickFinger2" "3"
     Option          "ClickFinger3" "2"
     Option          "BottomEdge" "25"
 EndSection

To use natural scrolling, also add the following inside this section:

     Option          "ScrollDownButton"  "4"
     Option          "ScrollUpButton"    "5"
     Option          "ScrollLeftButton"  "7"
     Option          "ScrollRightButton" "6"

For more configurations, check the document of .

To disable the trackpad when typing, install the  utility.

## Memory Card (SDHCI/SDX) Reader
There is currently a bug in the kernel (4.7.x) where the internal SD card reader times out.

As a workaround you will need to reload the sdhci kernel modules, as per: https://bugzilla.kernel.org/show_bug.cgi?id=73241#c55

 # rmmod sdhci-pci sdhci
 # modprobe sdhci debug_quirks2=4
 # modprobe sdhci-pci
