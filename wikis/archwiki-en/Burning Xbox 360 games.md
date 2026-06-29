# Burning Xbox 360 games

Xbox 360 games come in two image formats: .iso and .000. They are burned on dual layer DVD+R discs. This requires a dual-layer DVD burner. No specific brand or burner is needed for XGD1- or XGD2-formatted games, but XGD3-formatted games require a LiteOn drive with either flashed iHAS firmware or the BurnerMAX payload to burn successfully and reliably. In order to maximize the success of your burn, you should verify your disc images with abgx360 and burn at the slowest speed your burner and media allow. The manufacturer of your discs is also important; Verbatim DVD+R DL discs are the most reliable.

## Burning ISOs
Burning an ISO is best done through the command line with growisofs. This is found in the  package.

There are other applications you can use to burn the image ( etc) but you may miss some configuration options and end up with a dud burn. Use the following commands to burn the image to disc.

XGD1 (Xbox1):

 # growisofs -use-the-force-luke=dao -use-the-force-luke=break:1913776 -dvd-compat -speed=2 -Z /dev/sr0=rom.iso

XGD2:

 # growisofs -use-the-force-luke=dao -use-the-force-luke=break:1913760 -dvd-compat -speed=2 -Z /dev/sr0=rom.iso

XGD3 (iXtreme Burner Max Firmware):

 # cdrecord -v speed=4 -force -sao -overburn driveropts=burnfree rom.iso

This should determine the necessary layerbreak on its own.

XGD3 (truncated):

 $ truncate --size=8547991552 rom.iso
 # growisofs -use-the-force-luke=dao -use-the-force-luke=break:2086912 -dvd-compat -speed=2 -Z /dev/sr0=rom.iso

Replace  with the path to your dual layer drive. For most systems it will be .

If everything has been set up correctly you should see a messages like this:

 Executing 'builtin_dd if=rom.iso of=/dev/sr0 obs=32k seek=0'
 /dev/sr0: splitting layers at 1913760 blocks
 /dev/sr0: "Current Write Speed" is 2.5x1352KBps.
 3538944/7835492352 ( 0.0%) @0.8x, remaining 45:39 RBU  89.7% UBU   7.1%

The burn should take around approximately 40 minutes at 2.4x write speed, depending on the size of the iso.

## xbox360_burn
It is obviously possible to create an executable file containing the command to burn DVDs. Someone has created a bash script to allow for a more user-friendly interface. It has since been rewritten into python.

To burn, you then only have to use this command:

 # xbox360_burn -ib /dev/sr0 rom.iso

Replace  with the path to your dual layer drive. For most systems it will be .
