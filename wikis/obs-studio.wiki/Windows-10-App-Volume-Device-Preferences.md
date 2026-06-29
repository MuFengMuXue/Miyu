***
 - **[The basics](#the-basics)**
 - [The new capabilities](#the-new-capabilities)
 - [Usage](#usage)
 - **[FAQ](#faq)**
 - [Why this is useful](#why-this-is-useful)
 - [Do I still need virtual cables or Voicemeeter Banana?](#do-i-still-need-virtual-cables-or-voicemeeter-banana)
 - [Alternatives (for those not on 1803) / How to update](#alternatives-for-those-not-on-1803--how-to-update)
 - [Accessing the old settings](#accessing-the-old-settings)
 - [Downsides and flaws](#downsides-and-flaws)

***

# The Basics

* Everything related to the new options are available in the Windows 10 **Settings** app, found in the Start menu - Settings -> System -> Sound or by right clicking on the speaker icon in the taskbar and selecting "Open Sound settings".
* The Volume Mixer hasn't moved and it hasn't changed - it works exactly as it has since Windows Vista, allowing you to set volumes per-application for each audio device in a small, resizable window

## The new capabilities

The Windows 10 April 2018 Update (1803) allows you to set audio Input and Output devices for each running application directly via the system, even if the application's settings don't support it. It is a native, official way to route audio to individual devices. This replaces tools like Audio Router.

## Usage

![System -> Sound](https://i.imgur.com/A7VQZY4.png)

* Open your Start menu and click on Settings. If you're not sure which button that is, you can click the button on the top left with the 3 horizontal lines (the "hamburger button") and it'll show labels.
* Click on System, then in the left sidebar select Sound. This is the screen where you can do the basics - set your default input/output device.
* Scroll down to "Advanced sound options" and select "App volume device preferences"
* Here you'll see every application that has recently played sounds, with the ability to control volumes, and most importantly, allows you to choose an Output device and an Input device.
* If something breaks and you need to start from the beginning, scroll to the bottom and select "Reset"

![App volume and device preferences window](https://i.imgur.com/0Sd6Mfm.png)

# FAQ

## Why this is useful

The most common use case for routing application audio to different devices is in combination with virtual cables, allowing you to individually control volumes for Discord, your game audio, and music (for example) directly within OBS Studio. This can also be used to play certain audio just to your headset or speakers while everything else is sent to OBS.

## Do I still need virtual cables or Voicemeeter Banana?

Yes. Unfortunately, at this time Windows does not include ways to natively create virtual outputs or to route audio to **applications** specifically. The most commonly recommended (and free!) application for this is [Voicemeeter Banana](https://www.vb-audio.com/Voicemeeter/banana.htm), which provides 2 virtual inputs and an easy-to-use control panel. Alternatively, [VB-CABLE](https://www.vb-audio.com/Cable/) allows you to get one virtual outputs for free, and [two more if you donate](https://www.vb-audio.com/Cable/#DownloadCable) - but without the control panel.

Providing virtual cables like this natively via OBS Studio is often requested because some alternative streaming applications do this, however it would require a lot of work and is very low on the list of priorities compared to other features & fixes.

## Alternatives (for those not on 1803) / How to update

If you're running Windows 10, it may just be easier to update to the April 2018 Update. To do that, open Windows Update and it'll start downloading (Start -> Settings -> Update & Security -> Windows Update -> Check for updates). Keep in mind it's a pretty large update - it'll take time to download, and the installation itself can take around half an hour for most setups.

If you'd rather not upgrade, or you're running another operating system, Audio Router is the most commonly recommended application for this purpose. Unfortunately, [the original hasn't been touched](https://github.com/audiorouterdev/audio-router/releases) since 2016 (but should still work). After a bit of digging, [here's a version](https://github.com/a-sync/audio-router/releases) that was updated in early 2018.

Other alternatives are commercial (not free). You can browse [them here](https://alternativeto.net/software/audio-router/).

## Accessing the old settings

You can no longer directly access Playback/Recording devices by right clicking the speaker icon in the taskbar. There is a new option "Open Sound settings" instead - this will take you to the new Settings screen as mentioned earlier. From this screen, you need to click "Sound Control Panel." Depending on the size of the window this will either be in the right sidebar or near the bottom, under the heading "Related Settings".

## Downsides and flaws

As with any new system, you'll occasionally find quirks. 

* The most obvious is that certain applications like web browsers will show multiple entries. This is because each tab and extension runs on a separate process, so Windows assumes you'd want to control them independently. Unfortunately, the name of each tab is not shown, so it can sometimes be hard to set the devices correctly.
* The volume sliders in the "App volume device preferences" screen do not visually change when there's audio playing, like a mixer would. This would be incredibly helpful in situations like the one mentioned previously.
* If you make the window for "App volume device preferences" too small, it can be hard to determine which sliders and menus are associated with each device. It's recommended to resize the window until all 4 elements show up aligned in the same row.