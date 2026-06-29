### If you tried everything in this guide and are still having issues, please make a post on the [forums](https://obsproject.com/forum) or stop by the [OBS Discord server](https://obsproject/discord).

***

When using OBS on a laptop or multi-GPU system, you may run into performance issues or issues using a specific capture type, for example Display or Game Capture). This can be very frustrating. The reason this happens is because most modern laptops will come with two GPUs:

- A integrated, power-saving GPU (usually by Intel) for applications and desktop usage
- A discrete graphics chip (either NVIDIA or AMD) for demanding 3D apps and games

OBS can only run on one of these GPUs, but your open applications and games could be running on either. For example, if OBS is running on the Intel GPU, you will not be able to use Game Capture for your games running on the discrete (NVIDIA or AMD) GPU. Additionally, if OBS is not running on the discrete GPU, you might run into performance issues. In rare cases, trying to capture a game running on a different GPU than OBS can cause the game to crash. This is not really an issue with OBS, but rather a design choice by laptop manufacturers in order to save power and there's little that can be done on our side. However, we do have several troubleshooting suggestions to try and assist with any issues.

***

### If you are getting a black screen with your Capture Sources or are otherwise having performance issues with OBS on your laptop or multi-GPU system, read the following as it applies to you:

- [I want to use Display Capture](#configure-your-system-for-display-capture)
- [I want to use Game or Window Capture](#configure-your-system-for-game-or-window-capture)
- [I need to use compatibility mode](#compatibility-capture-modes)
- [I want to capture a browser window (e.g. Chrome), Discord or Skype](#browser-based-applications)
- [I'm having trouble using the OBS Browser Source](#obs-browser-sources)

***

## Configure your system for Display Capture

If Display Capture is not working, chances are you need to set OBS to run on the integrated, power-saving GPU.

Jump to our [Guide section](#guides) on how to setup your computer.

***

## Configure your system for Game or Window Capture

If Window Capture or Game Capture is not working, chances are you need to set OBS to run on the discrete, high-performance GPU.

Jump to our [Guide section](#guides) on how to setup your computer.

***

## Compatibility Capture Modes

If you cannot set the preferred GPU (on AMD laptops typically), or wish to cross-capture an image from the other GPU after that (for example, the League of Legends lobby window), Window Capture and Game Capture have compatibility modes, that basically guarantee a capture at the cost of higher CPU usage.

- For Window Capture, enable "Multi-adapter compatibility"
- For Game Capture, enable "SLI/Crossfire Capture Mode (Slow)"

"SLI/Crossfire Capture Mode (Slow)" is not recommended for use with 3D games due to the high performance impact and should be treated as a last resort method.

***

## Browser-based Applications

Modern browser (Chrome, Firefox and everything based on them) as well as CEF/Electron-based application (e.g. Discord, new Skype) use very advanced hardware acceleration features of your graphics card and can fail to capture properly with Window Capture.

In those cases you need to switch to [Display Capture in OBS](#configure-your-system-for-display-capture) or disable the hardware acceleration in those applications (can reduce performance).

***

## OBS Browser Sources

In OBS Studio v22 and upwards, there is an updated version of the browser source that comes with hardware acceleration on by default. This means that browser sources will be rendered on the GPU. However, on laptops or multi-GPU systems, it may not always run on the same GPU that OBS is running on, and tends to favor the high performance GPU.

You can manually select the GPU that the browser source is run on by following the [appropriate instructions](#guides), and adjusting the settings for `obs-browser-page.exe`. By default, OBS Studio's installation of obs-browser-page will be at either `C:\Program Files\obs-studio\obs-plugins\64bit\obs-browser-page.exe` or `C:\Program Files (x86)\obs-studio\obs-plugins\64bit\obs-browser-page.exe`.

If you're still having difficulty getting browser sources to render on a laptop or multi-GPU system, you can disable the new hardware acceleration feature. In OBS Studio, go to **File → Settings → Advanced**, and uncheck the "Enable Browser Source Hardware Acceleration" option.

***

## Guides

The step by step guides on how to switch to another GPU varies by the type of your system. Select one from the list below:

- [Universal guide for computers with Windows 10](Laptop-GPU-Selection-Windows-10)
- [NVIDIA-based Laptops](Laptop-GPU-Selection-Nvidia)
- [AMD-based Laptops](Laptop-GPU-Selection-Amd)

If you are unsure what type applies to your computer, ask in the [forums](https://obsproject.com/forum) or stop by the [OBS Discord server](https://obsproject/discord).
