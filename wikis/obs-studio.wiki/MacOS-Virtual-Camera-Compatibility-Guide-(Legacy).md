# Note: This page contains legacy instructions that are no longer advised and only exists for archival purposes. Please refer to the [knowledge base](https://obsproject.com/kb/virtual-camera-troubleshooting) for up-to-date information.



A list of programs this is currently compatible with. Please note that this list is not complete. Also note you have to fully restart the program you are using to recognize the virtual camera.

## Step 1
The absolute first troubleshooting step to take is to quit the app completly that you are trying to use the virtual camera in, then start the virtual camera in OBS, then see if it works in the app. 

_Note:_ These have all been tested and confirmed to work on macOS Big Sur running OBS 26.1.2

# Table of Contents 
1. [Apps that just work](#apps-that-just-work)
2. [Apps that will **not** work](#apps-that-will-not-work)
3. [Apps that may or may **not** work](#apps-that-may-or-may-not-work)
4. [App Specific Guides](#App-Specific-Guides)
5. [SIP Workaround](#sip-workaround)

## Apps that just work
* AdobeConnect
* Alibaba DingTalk
* BigBlueButton
* BlueJeans
* Brave
* D8E
* Edge
* Google Chrome
* GoTo Meeting
* iMovie
* Messenger Rooms
* QuickTime Player
* RingCentral
* TrueConf
* Webinar Jam
* Zoom (Make sure Zoom is updated to 5.1.1)

## Apps that will **not** work 
* Bluejeans Events
* Safari 
* Tencent Meeting
* FaceTime 
* Photo Booth 

## Apps that _MAY_ or may not work 
* FireFox - _Works for some people, doesn't work for others_
* Screen (screen.so) - _May work by changing the entitlements, you can try the steps listed [here](#generic-instructions-to-allow-the-dal-plugin) with `Screen` replacing `APPLICATION NAME HERE` in step 4_
* Slack - _May work by changing the entitlements, you can try the steps listed [here](#generic-instructions-to-allow-the-dal-plugin) with `Slack` replacing `APPLICATION NAME HERE` in step 4_

## App Specific Guides
1. [Discord](#discord)
2. [Microsoft Teams](#microsoft-teams)
3. [Skype](#skype)
4. [Webex (Webex Teams)](#webex-webex-teams)
5. [Webex Meetings](#Webex-Meetings)
6. [Generic instructions to allow the DAL plugin](#generic-instructions-to-allow-the-dal-plugin)

### Discord 
To get the Mac virtual camera to work on Discord:
1) Open the Terminal app which can be found in Launchpad on every Mac.
2) Paste into the terminal
```Xcode-select --install```
3) Put in your password. NOTE: you will not see the password being put in, but it will be registering it.
4) Once the previous step finishes installing, paste the following command into the terminal app and then input your password again
```sudo codesign --remove-signature "/Applications/Discord.app/Contents/Frameworks/Discord Helper (Renderer).app"```
5) Now, re-sign the application.
```sudo codesign --sign - "/Applications/Discord.app/Contents/Frameworks/Discord Helper (Renderer).app"```

_If step four doesn't allow the virtual camera to work on Discord after restarting your Mac, try using the following like you did with step four and see if that allows it to work ```sudo codesign --remove-signature "/Applications/Discord.app/Contents/Frameworks/Discord Helper.app"``` and if it still does not work, you can try ```sudo codesign --remove-signature "/Applications/Discord.app/Contents/Frameworks/Discord Helper (GPU).app"``` and if it still does not work you can try ```sudo codesign --remove-signature "/Applications/Discord.app/Contents/Frameworks/Discord Helper (plugin).app"```_

On Ventura and above you may get a permission denied when signing. If you get this you need to open System Settings, Privacy & Security, App Management and give permission to your Terminal program. Alternatively, move Discord.app to your Downloads directory, modify it there and then move it back to Applications.

### Microsoft Teams
To get the Mac virtual camera to work on Microsoft Teams:
1) Open the Terminal app which can be found in Launchpad on every Mac.
2) Paste into the terminal
```Xcode-select --install```
3) Put in your password. NOTE: you will not see the password being put in, but it will be registering it.
4) Once the previous step finishes installing, paste the following command into the terminal app and then input your password again
```sudo codesign --remove-signature "/Applications/Microsoft Teams.app/Contents/Frameworks/Microsoft Teams Helper (Renderer).app"```
5) Now, re-sign the application.
```sudo codesign --sign - "/Applications/Microsoft Teams.app/Contents/Frameworks/Microsoft Teams Helper (Renderer).app"```

_If step four doesn't allow the virtual camera to work on Microsoft Teams after restarting your Mac, try using the following like you did with step four and see if that allows it to work ```sudo codesign --remove-signature "/Applications/Microsoft Teams.app/Contents/Frameworks/Microsoft Teams Helper.app"``` and if it still does not work, you can try ```sudo codesign --remove-signature "/Applications/Microsoft Teams.app/Contents/Frameworks/Microsoft Teams Helper (GPU).app"``` and if it still does not work you can try ```sudo codesign --remove-signature "/Applications/Microsoft Teams.app/Contents/Frameworks/Microsoft Teams Helper (plugin).app"```_

### Skype
To get the Mac virtual camera to work on Skype:
1) Open the Terminal app which can be found in Launchpad on every Mac.
2) Paste into the terminal
```Xcode-select --install```
3) Put in your password. NOTE: you will not see the password being put in, but it will be registering it.
4) Once the previous step finishes installing, paste the following command into the terminal app and then input your password again
```sudo codesign --remove-signature "/Applications/Skype.app/Contents/Frameworks/Skype Helper (Renderer).app"```
5) Now, re-sign the application.
```sudo codesign --sign - "/Applications/Skype.app/Contents/Frameworks/Skype Helper (Renderer).app"```


### Webex (Webex Teams) 
To get the Mac virtual camera to work on Webex Teams:
1) Open the Terminal app which can be found in Launchpad on every Mac.
2) Paste into the terminal
```Xcode-select --install```
3) Put in your password. NOTE: you will not see the password being put in, but it will be registering it.
4) Once the previous step finishes installing, paste the following command into the terminal app and then input your password again
```sudo codesign --remove-signature "/Applications/Webex.app/"```
5) Now, re-sign the application.
```sudo codesign --sign - "/Applications/Webex.app/"```

### Webex Meetings 
Possible to run by changing entitlements as described [here](#generic-instructions-to-allow-the-dal-plugin) with `Webex Meetings` replacing `APPLICATION NAME HERE` in step 4. Can be fixed by removing the signature of the Meeting Centre.app (needs to be done for every version that may be called). Then launch the meeting which will fail, then from a command line launch the app by hand. The apps are in the folder ```~/Library/Application Support/WebEx``` Folder with versions being in the format T33_64UMC_40.9.6.11 and the manual launch command is ```Meeting\ Center.app/Contents/MacOS/Meeting\ Center```. This will lose the menu at the top of the screen so is a partial workaround. Webex (Webex Teams) is easier to get working.
An easier and a more confirmed way to get it to work is to run Webex Web app in the browser instead of the desktop app. Open the URL for your meeting, select Cancel when prompted to "Open Cisco Webex Start?", click "Join from your browser", login and select the OBS Virtual Camera.

### Generic instructions to allow the DAL plugin
To get the Mac virtual camera to work on a generic app not already listed:
1) Open the Terminal app which can be found in Launchpad on every Mac.
2) Paste into the terminal
```Xcode-select --install```
3) Put in your password. NOTE: you will not see the password being put in, but it will be registering it.
4) Once the previous step finishes installing, paste the following command into the terminal app and then input your password again
```sudo codesign --remove-signature "/Applications/APPLICATION NAME HERE.app/"```
5) Now, re-sign the application.
```sudo codesign --sign - "/Applications/APPLICATION NAME HERE.app/"```

If that does not work you can try the following, test one at a time
* ```sudo codesign --remove-signature "/Applications/APPLICATION NAME HERE.app/Contents/Frameworks/APPLICATION NAME HERE Helper (Renderer).app"``` 
* ```sudo codesign --remove-signature "/Applications/APPLICATION NAME HERE.app/Contents/Frameworks/APPLICATION NAME HERE Helper (GPU).app"``` 
* ```sudo codesign --remove-signature "/Applications/APPLICATION NAME HERE.app/Contents/Frameworks/APPLICATION NAME HERE Helper (Plugin).app"``` 


## SIP Workaround 
### ***WARNING*** 

Only do this if you understand the possible consequences that this can have, please read more about it [here](https://eclecticlight.co/2017/04/28/sierras-system-integrity-protection-sip-beyond-root/) before making any changes.

One option to allow macOS to allow DAL plugins in system apps / codesigned apps is to disable the system integrity protections (SIP) that cause these plugins to fail to load.

This cannot be stressed enough, but while you do not need to fully disable SIP to have DAL plugins start working (which is good), **DO THIS AT YOUR OWN RISK** as it could bring security implications for your entire system. You can read more about the details of SIP [here](https://eclecticlight.co/2017/04/28/sierras-system-integrity-protection-sip-beyond-root/). In case you are doing this on a company device, make sure this is not going against work policy.

To disable the filesystem part of SIP (that blocks the DAL plugins from loading) run the following command in recovery mode (reboot holding Command + R):

```csrutil enable --without fs```

Again this cannot be stressed enough that this will be disabling a main part system integrity and that you will be doing this **AT YOUR OWN RISK**