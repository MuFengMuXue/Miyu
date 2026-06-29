# Steam Remote Play

Steam Remote Play allows games to be launched on one computer, while being played from other devices connected to Steam. With Remote Play Together, you can invite your Steam Friends to join your local co-op sessions remotely, without having to own or launch the game themselves.

By utilizing the (https://store.steampowered.com/steamlink/about), Remote Play access can be extended to any supported device with the app installed.


- [How does Remote Play work?](#how)

- [How can I tell if a game supports Remote Play?](#support)

- [How do I use Remote Play?](#howdoiuseit)

- [How do I disable Remote Play?](#howdoidisableit)

- [How do I improve my streaming experience?](#improvement)

- [Is there a community group?](#communitygroup)

Troubleshooting:


- (#basic)

- (#knownissues)

# How does Remote Play work?

Steam Remote Play works by connecting you to a game on one computer when the game process is actually running on another computer elsewhere. Through Steam, game audio and video is captured on the remote computer and sent to the device. The game input (keyboard, mouse or gamepad) is sent from the device you are using to the game process on the remote computer.

Any two computers connected to Steam can be used to stream a gameplay session and this can enable playing games on systems that would not traditionally be able to run those games. For example, a Windows only game could be streamed from a Windows PC to a Steam Machine running Linux in the living room. A graphically intensive game could be streamed from a beefy gaming rig in the office to your low powered laptop that you are using in bed. You could even start a game on one computer and move to a more comfortable location and continue playing it there.

http://media.steampowered.com/apps/steamhardware/InHomeStreamingDiagram_t.jpg
Overview of streaming from a PC to a Steam Machine

# How can I tell if a game supports Remote Play?

All Steam games can be played streaming between your own computers. If a game supports Remote Play Together or has been identified as a good game for streaming to devices using the Steam Link app, that will be listed on the game's Steam store page, in the game details on the right side of the page.

# How do I use Remote Play?

**Remote Play Anywhere**


- Log in to the Steam client on the computer with the installed game you wish to play.

- Now, Log into Steam on another computer or a supported device with (https://store.steampowered.com/steamlink/about/) installed.

- From there, you can launch and play the game remotely from the Steam Library.

**Remote Play Together**


- Launch your game.

- Make sure your friend is logged in to Steam from a supported device.

- Open your Steam Overlay in-game (Shift+Tab).

- From your friends list, right-click your friend and select 'Remote Play Together'.

- Once your friend accepts the invite, they will be in-game with you.

# How do I disable Remote Play?

Steam Remote Play allows access to the host computer outside of the game being streamed. Because you are logged into your Steam account on both computers, it is assumed you have full access to both computers. If you don’t want a remote Steam session to be able to access your computer, you can easily turn off the feature in the Steam Remote Play settings.

# How do I improve my streaming experience?

**Hardware:**
We recommend a minimum of a quad-core CPU for the computer running the game. The client has more modest requirements, but should have a GPU that supports hardware accelerated H264 decoding. Any recent laptop or PC should meet the client requirements.

**Network:**
We recommend using a wired network for the best streaming experience. People have had some success with powerline networks and wireless N and AC networks with good signal, though your experience may vary.

**Game Settings:**
To improve your streaming experience, you can go into your game settings and lower your resolution and turn off vertical sync.

**Steam Settings:**
In the Remote Play settings you can change a number of things that can affect your experience. You can change your preference for speed vs quality, limit the network bandwidth, and adjust the maximum capture resolution.

# Is there a community group?

Yes, you can join the (http://steamcommunity.com/groups/homestream) community group and discuss the feature with thousands of other players.

# Issues & Troubleshooting
Steam Remote Play is designed to require minimal setup, provided the game you are trying to play is already launching correctly on the primary PC. If you are experiencing a problem, try resolving it by following the troubleshooting info in this article. If you continue to experience the problem, or are encountering an issue that isn't covered here, you can always reach out and submit a detailed report to (https://help.steampowered.com/en/wizard/HelpWithSteamLinkApp).


- (#knownissues)[/*]
- [What network ports does streaming use?](#networkports)[/*]
- [The computers don't see each other](#broadcastfailed)[/*]
- [I haven't updated video drivers](#updatedrivers)[/*]
- (#dpiaware)[/*]
- [I get "The streaming client exited unexpectedly (2)"](#quiterror2)[/*]
- (#nvidialaptop)[/*]
- (#blackscreen)[/*]
- [How do I enable Intel hardware encoding?](#intelhardwareencoding)[/*]
- [How do I enable NVIDIA hardware encoding?](#nvidiahardwareencoding)[/*]
- (#nvidiadeblockingsoftware)[/*]
- (#nvidiadeblockingmacosx)[/*]
- [I don't hear any audio when streaming a game](#muteaudio)[/*]
- [My game controller input doesn't affect the game](#nocontrollerinput)[/*]
- [My mouse and keyboard input don't affect the game](#nomousekeyboardinput)[/*]
- (#invisiblemouse)[/*]
- [How do I diagnose streaming performance problems?](#advancedtroubleshooting)[/*]

## Basic Troubleshooting
Before you get too far down the troubleshooting path, it's a good idea to complete the entire setup process to ensure you are ready to use Remote Play.


- First, you'll want to make sure that Steam is up to date on both PCs. If you are using the Steam Link app, follow the appropriate setup guide (https://help.steampowered.com/en/faqs/view/7E9D-27C8-EB08-21D9).[/*]
- Now, from the machine that will be hosting the Remote Play session, you'll want to launch the game at least once to ensure it's up to date and working correctly.[/*]
- If you are using Remote Play Anywhere, make sure you are logged in to the same Steam account on the remote device. From that Library, you should see the game listed as installed, with the option to 'Stream' instead of 'Play'[/*]
- If you are using Remote Play Together, your friend should see that you are in-game in their friends list. You should see them as online.[/*]
- If the game supports Remote Play Together, you can open the overlay in-game (Shift+Tab) and invite your friend from the friends list.[/*]

If Remote Play still isn't working correctly, you'll want to have a look at the known issues below for more information. If that fails, you can always reach out and submit a ticket to (https://help.steampowered.com/en/wizard/HelpWithSteamLinkApp). We ask that you provide a detailed report including the exact steps that you take to reproduce the behavior, so that we can isolate the issue and better provide a solution.

# Known issues

General:


- There is currently no indication of whether Steam is able to bind the discovery port 27036, but if that fails no other computers will show up in the remote computer list in the Remote Play settings.[/*]
- If a game takes a long time to launch, it will time out on the client but will start anyway. Retrying the launch will connect to the running game. If this happens consistently for any particular game, please report it on the (http://steamcommunity.com/groups/homestream/discussions/1).[/*]
- If your game loses focus, Steam will start streaming the desktop so that you can get back to it. This is a feature of Steam Remote Play.[/*]
- Streaming non-Steam games in the Steam library may work but is not officially supported.[/*]
- Voice recording over streaming is not currently supported.[/*]
- Streaming may not perform well when streaming to older systems with a single or dual core CPU and no hardware accelerated H264 decoding.[/*]
- DirectInput controllers other than gamepad style controllers (wheels, flight controllers, etc.) are not currently supported. Other controllers using XInput are fully supported.[/*]
- Certain games like "Rome: Total War" use older DirectX technology which is not currently supported.[/*]

Windows:


- Streaming from a Windows XP host is not supported.[/*]
- UAC dialogs prevent streaming. If you're a game developer, please avoid requiring elevated permissions to run your game.[/*]

macOS:


- Streaming from a macOS host is supported on macOS 10.8 and newer.[/*]

SteamOS / Linux:


- In order to support streaming game controllers on a Linux host computer, /dev/uinput or /dev/input/uinput needs to be readable and writable by Steam.[/*]
- Currently, there is no rumble support for Linux machines.[/*]

### What network ports does streaming use?
Streaming uses UDP ports 27031 and 27036 and TCP ports 27036 and 27037. Please make sure Steam can listen on these ports in your firewall software.

### The computers don't see each other
Make sure they are on the same subnet and no other program is using UDP port 27036, which is used for the initial discovery protocol. If another program has bound this port, please report which program it is on the (http://steamcommunity.com/groups/homestream/discussions/1).

If you're running a Mac client, try rebooting after Steam is updated.

Some people have also reported that custom firewalls or software like Hamachi interferes with the discovery process.

### I haven't updated video drivers
A number of bugs have been fixed in the latest video driver releases that may affect streaming. If you are getting poor performance, graphical glitches or black screens please make sure you have the latest drivers installed from your video card vendor's website.

### Steam looks really small on the host after streaming
Exit Steam, right click Steam.exe and bring up the compatibility properties, uncheck "Disable display scaling on high DPI settings", save the changes and restart Steam.

### I get "The streaming client exited unexpectedly (2)"
You can look in the streaming client log to get more details about what happened. On Windows this file is on the local computer in streaming_client.exe.log in the Steam directory. On Linux this file is on the local computer in /tmp/streaming_client.log.

### Steam crashes or black screen when hosting from an NVIDIA laptop
There is a bug in the NVIDIA driver which causes a crash or black screen if you're streaming from a laptop with Windows 8.1. Try opening the NVIDIA control panel and under 3D settings, set Steam to use integrated graphics, and then restart Steam.

### I see a black screen when streaming a game.
If it's a specific game that is having the issue, please report which game is having the issue on the (http://steamcommunity.com/groups/homestream/discussions/1).

If all games are having the issue, please try the following:


- Update your video drivers on both computers, if you haven't already[/*]
- Try disabling hardware encoding in the advanced host settings on the remote computer. If this works, please report your host video card and driver version to the (http://steamcommunity.com/groups/homestream/discussions/1)[/*]
- Try disabling hardware decoding in the advanced client settings. If this works, please report your client video card and driver version to the (http://steamcommunity.com/groups/homestream/discussions/1)[/*]

### How do I enable Intel hardware encoding?
If you have an Ivy Bridge or newer system with an integrated GPU, you may be able to take advantage of Intel QuickSync hardware acceleration. To enable this, go to the Steam Remote Play settings on the remote computer, open the advanced host options and check "Enable hardware encoding"

You can check to see what encoder and decoder is being used by setting "Performance Overlay" to "Details" from the drop down in the advanced client options on the client computer and then pressing F6 during the streaming session. If you see the word "QuickSync" in the encoder description, you are using Intel hardware accelerated encoding.

### How do I enable NVIDIA hardware encoding?
If you have a GTX 650 or newer and the latest NVIDIA drivers, you may be able to take advantage of NVIDIA hardware acceleration. To enable this, go to the Steam Remote Play settings on the remote computer, open the advanced host options and check "Enable hardware encoding"

You can check to see what encoder and decoder is being used by setting "Performance Overlay" to "Details" from the drop down in the advanced client options on the client computer and then pressing F6 during the streaming session. If you see the words "NVFBC" or "NVIFR" in the encoder description, you are using NVIDIA hardware accelerated encoding.

### I see persistent smearing on the screen with NVIDIA hardware encoding
This is a known incompatibility between NVIDIA hardware encoding and the software decoder. Try enabling hardware decoding on the client or disabling hardware encoding in the advanced host options on the remote computer.

### I see big blocky color areas with NVIDIA hardware encoding
This is a known incompatibility between NVIDIA hardware encoding and the hardware decoder on macOS. Try disabling hardware encoding in the advanced host options on the remote computer.

### I don't hear any audio when streaming a game


- See if there is an audio error listed in logs\\streaming_log.txt on the remote computer[/*]
- See if audio or the Steam application is muted on the remote computer[/*]
- See if audio is muted on the local computer[/*]

### My game controller input doesn't affect the game
If your game controller isn't recognized by any game, check to see if Steam Big Picture recognizes it in the controller settings on the client computer. You may need to configure your controller there in order to use it for streaming.

Some games use raw input instead of XInput or DirectInput and are not yet supported.

If you are using an Xbox 360 controller on a Mac, there is a publicly available driver that may work for you.

### My mouse and keyboard input don't affect the game
Some games run with elevated permissions and Windows prevents remote input from affecting them, as a security measure.

The following is a list of known games with this limitation:


- Age of Empires 3[/*]
- The Bard's Tale[/*]
- Nether[/*]

If you have a mouse and keyboard input problem with games not listed here, please report it on the (http://steamcommunity.com/groups/homestream/discussions/1).

### My mouse cursor is invisible on Windows 8 or Windows 10
Try plugging a mouse in on the remote computer.

### How do I diagnose streaming performance problems?
You can look in streaming_log.txt in the Steam logs folder on the remote computer after you play a game to get a detailed breakdown of how much time was spent in each component of the streaming system.

While the game is running, you can hit F6 or the Guide button combined with the Y button on your game controller to turn on live statistics for the session. While the statistics are visible the game collects more detailed information which is saved in logs\\SteamVideoTrace.txt and logs\\SteamAudioTrace.txt at the end of the session.

While the statistics are visible, you can hit F8 or the Guide button combined with the X button on your game controller to save a screenshot and 10 seconds worth of stats to a zip file in the streaming directory in the Steam folder on the remote computer.

There is a good article on how to interpret the log information here: (http://steamcommunity.com/groups/homestream/discussions/0/540733523404402134/)
