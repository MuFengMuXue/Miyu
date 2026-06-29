# EOS Overlay

First things first: On Linux, the EOS Overlay is *installed* once (globally) but *enabled* per-game. You'll have to repeat the instructions below for each game you want to use the overlay with

1. Click on the game's logo in the library to get to the **Game Page**:
   ![](https://user-images.githubusercontent.com/34034631/193338961-db808e22-b056-4b58-8cdd-e6f8cf870d36.png)
2. Click "Tools" -> "Enable EOS Overlay":
   ![](https://user-images.githubusercontent.com/34034631/193339394-6cbcdeb0-b517-43ab-978c-d99a721eb244.png)
   Heroic will now install the overlay (if not installed already) and enable it *for this game*
3. Enable DXVK:
   Go back to the "Info" tab and click "Settings":
   ![](https://user-images.githubusercontent.com/34034631/193340192-09942804-3b7f-4932-a3a3-2f968e56cfce.png)
   In the "Wine Extensions" tab, make sure "Auto Install/Update DXVK on Prefix" is checked:
   ![](https://user-images.githubusercontent.com/34034631/193340796-de6d55e7-8a46-4eb7-9c2b-310a8168d043.png)
4. Install `corefonts`
   Go back to the "Wine" tab of the Game Settings & click the "Winetricks" button (scrolling down might be necessary):
   ![](https://user-images.githubusercontent.com/34034631/193341307-51666b22-d58c-4eeb-8e54-78da20417026.png)
   After a while, this window should pop up:
   ![image](https://user-images.githubusercontent.com/34034631/193342230-12d718d3-c7a7-451c-b43b-8054088ec2d3.png)
   Make sure "Select the default wineprefix" is selected, then click "OK" at the bottom.
   After that, select "Install a font" & again click OK:
   ![](https://user-images.githubusercontent.com/34034631/193343407-e54190a5-0a81-4007-82da-01a68542b92b.png)
   In the font list, make sure `corefonts` is ticked, then click OK:
   ![](https://user-images.githubusercontent.com/34034631/193343654-6242a4e3-efcc-43ed-b430-ef6c5c7e23d6.png)
   Winetricks will now close and install the fonts. It might take a couple of minutes. Any warning messages about a 64-bit prefix can be ignored.
   Once everything's installed, the font list will open up again. Click "Cancel"/close the window 3 times to quit out of Winetricks
