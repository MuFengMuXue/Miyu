* [GPU Selection Guide](#gpu-selection-guide) (for laptops and all-in-one computers with multiple GPUs)
  * [Windows 10/11](#windows-10--11)
  * [Legacy Windows (7, 8 and legacy 10)](#windows-7-8-and-windows-10-up-to-and-including-1809)
* [Notes on Specific Sources](#specific-sources)
    * [Display Capture](#display-capture)
    * [Browser Source](#browser-source)

***

# GPU Selection Guide

When using OBS on a laptop or multi-GPU system, you may run into performance issues or issues using a specific capture type (i.e. Game or Window capture). This can be very frustrating. The reason this happens is because most modern laptops will come with two GPUs:

- An integrated GPU (iGPU) for 2D applications/your desktop, and
- A discrete/external GPU (either NVIDIA or AMD) for 3D apps and games.

OBS can only run on one of these GPUs, but your open applications and games could be running on either. For example, if OBS is running on the integrated GPU, you will not be able to use Game Capture for your games running on the discrete (NVIDIA or AMD) GPU.

Additionally, if OBS is not running on the discrete GPU, you might run into performance issues. In rare cases, trying to capture a game running on a different GPU than OBS can cause the game to crash. This is not really an issue with OBS, but rather a design choice by laptop manufacturers in order to save power and there's little that can be done on our side. However, we do have several troubleshooting suggestions to try and assist with any issues.

This guide will show you how to select the graphics card OBS is running on using built-in Windows settings. It is applicable if you are running **Windows 10 version 1903 or newer**.

## Windows 10 & 11

To check your version:
* Open the Settings App (Start button → Cogwheel icon)
* Go to System → About and scroll down to "Windows specification".

![Windows 10 About](https://raw.githubusercontent.com/wiki/obsproject/obs-studio/images/laptop-troubleshooting/win10/06-find-version.png)

* Close OBS Studio if it is currently open.
* Open the Settings App (Start button → Cogwheel icon)
    * Windows 10: Go to System → Display and select "Graphics settings" near the bottom
    * Windows 11: On the left, click System. On the right, click Display → "Graphics" near the bottom
    ![Graphics settings](https://raw.githubusercontent.com/wiki/obsproject/obs-studio/images/laptop-troubleshooting/win10/01-graphics-settings.png)

* Select "Classic app" or "Desktop app" and click "Browse" under Graphics performance preference
    ![Adding an app](https://raw.githubusercontent.com/wiki/obsproject/obs-studio/images/laptop-troubleshooting/win10/02-add-application.png)
* Navigate and find your OBS Studio executable. By default this is `C:\Program Files\obs-studio\bin\64bit\obs64.exe`
* Once selected, click "Options" under the OBS Studio entry
    ![Graphics options](https://raw.githubusercontent.com/wiki/obsproject/obs-studio/images/laptop-troubleshooting/win10/03-open-options.png)

Then follow the steps below, depending on which mode you need.

* For **Window Capture** and **Game Capture**
    * Choose "High performance" and click Save
    ![Game capture setting](https://raw.githubusercontent.com/wiki/obsproject/obs-studio/images/laptop-troubleshooting/win10/05-high-perf.png)
* For **Display Capture**
    * Choose "Power saving" and click Save
    * Also read the [Display Capture](#display-capture) section below
    ![Display capture setting](https://raw.githubusercontent.com/wiki/obsproject/obs-studio/images/laptop-troubleshooting/win10/04-power-saving.png)

***

## Windows 7, 8, and Windows 10 up to (and including) 1809

If you run Windows 7 or 8, or Windows 10 up to (and including) version 1809, use our separate guides:
- [NVIDIA](Laptop-GPU-Selection-Nvidia)
- [AMD](Laptop-GPU-Selection-Amd)

# Notes on Specific Sources

## Display Capture

If you have OBS Studio 27.0 or newer and Windows 10 (1903) or newer, see the steps below in case the "automatic" method doesn't work.

Click 'Properties' of your display capture source, and you should see "Automatic", "DXGI" or "Windows 10 (1903 and up)". If you have a multi-GPU system, you will want to select "Windows 10 (1903 and up)" to get it to display properly, and make sure your OBS Studio is running on the high-performance GPU. If you are on a single GPU system, automatic will work (using DXGI method).

![](https://i.imgur.com/fB4PeDS.png)

For a video showing this, here is a [quick setup guide video](https://www.youtube.com/watch?v=Z77oCZ3lojE) which goes over how to set up Display Capture with the new method, should you have problems with it. If your display capture still doesn't work after following that, seek support in the OBS discord or forums.

## Browser Source

In OBS Studio v22 and upwards, there is an updated version of the browser source that comes with hardware acceleration on by default. This means that browser sources will be rendered on the GPU. However, on laptops or multi-GPU systems, it may not always run on the same GPU that OBS is running on, and tends to favor the high performance GPU.

You can manually select the GPU that the browser source is run on by following the appropriate instructions for your version of Windows (follow the guide specific to your GPU if you have Windows 10 1809 or older), and adjusting the settings for `obs-browser-page.exe`. By default, OBS Studio's installation of obs-browser-page will be at either `C:\Program Files\obs-studio\obs-plugins\64bit\obs-browser-page.exe` or `C:\Program Files (x86)\obs-studio\obs-plugins\64bit\obs-browser-page.exe`.

If you're still having difficulty getting browser sources to render on a laptop or multi-GPU system, you can disable the new hardware acceleration feature. In OBS Studio, go to **File > Settings > Advanced**, and uncheck the "Enable Browser Source Hardware Acceleration" option.

***

**If you tried everything in this guide and are still having issues, please make a post on the [forums](https://obsproject.com/forum) or stop by the [OBS Discord server](https://obsproject.com/discord).**

***

## Special note from Lain
I know it's annoying. I'm not happy that this is the case either. Unfortunately, there's nothing anyone can really do about it. This is just the way laptops are designed in order to save power and battery life.