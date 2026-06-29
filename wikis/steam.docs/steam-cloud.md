# Steam Cloud

The Steam Cloud allows games and the platform to utilize cloud storage hosted by Steam. Games can utilize Steam Cloud for storage of many different types of data, including game settings, save games, profile stats and other user-specific bits. Many Steam client settings are also saved via the cloud, including collections, friend nicknames and anything changed via the Steam client Settings menu. These settings will persist on an account regardless of which machine it is logged into, as the settings are pulled from the cloud upon login.


- [How do I tell if a game uses Steam Cloud?](#howto)

- [How can I enable or disable The Steam Cloud?](#enabling)

- [Where are cloud files stored locally?](#where)

- [Is there a log of Steam Cloud activity?](#log)


### Issues & Troubleshooting
Because of the automated nature of cloud synchronization, Steam Support has a limited ability to address issues with the cloud. If any saves or other data have been lost, it is not likely that we will be able to recover them. It is for this reason that we encourage users to make sure they understand behaviors that can affect the cloud, so that when they are encountered, the loss of data can potentially be avoided.


- [How do I resolve a Steam Cloud conflict?](#conflicts)

- [What if Steam is unable to sync files to the cloud?](#sync)

- [What if I lost a file or progress after moving to a different machine?](#lostdata)

- [What if I have an issue with cross-platform cloud data?](#crossplat)
- (#basic)

  # How do I tell if my game uses Steam Cloud?
Developers are able to completely customize how The Steam Cloud is used for their games, including which user files are uploaded.

The Steam Storepage will show a Steam Cloud logo in the upper right if a game uses the Steam Cloud. But, you may need to work with the developer or the community to determine exactly which files or settings are integrated.

# How can I enable or disable The Steam Cloud?

The Steam Cloud can be toggled for individual games, or as a global Steam setting for all games. When Steam Cloud functionality of a game is disabled, all progress that would normally be saved via the cloud will only be saved locally on the machine where the progress was made.

### Individual games:


- From the Steam Library, right click on any game and select *Properties...*.
- Under the *General* tab, the Cloud Synchronization setting can be toggled.

### All games:


- From the Steam client Settings window, navigate to the *Cloud* tab.
- Cloud can be enabled or disabled using the toggle next to *Enable Steam Cloud Sync for applications that support it*.


# Where are cloud files stored locally?

Cloud files are stored locally in the following locations by default:


- **Windows:** C:\\Program Files (x86)\\Steam\\userdata

- **MacOS:** $HOME/Library/Application Support/Steam/userdata

- **Linux:** $HOME/.local/share/Steam/userdata


### Game specific cloud files:

The *userdata* folder will contain unique Steam IDs, which correspond to the Steam accounts that have logged in on that machine.

Within the Steam ID folders are the respective games associated with those Steam accounts, listed by appID. The following example is for Dota 2 (appID 570):

- Steam\\userdata\\\\570\\

### Steam client cloud files:

Changes made to your Steam client settings are stored in the cloud, as well as locally in the following folder:

- Steam\\userdata\\\\7\\


# Is there a log of Steam Cloud activity?

Steam creates an log entry any time that files are written to the cloud or retrieved from it.

These are logged in the *cloud_log.txt* file, which is stored in the following location by default:


- **Windows:** C:\\Program Files (x86)\\Steam\\logs

- **MacOS:** $HOME/Library/Application Support/Steam/logs

- **Linux:** $HOME/.local/share/Steam/logs


# How do I resolve a Steam Cloud conflict?

{STEAM_CLAN_IMAGE}/39983882/697138d8ffe44bc2c6793abf3239e76c4a027dbd.png

The Steam Cloud conflict window will be shown when a game is launched, if Steam detects that the local files associated with that game differ from the ones stored on the cloud.

This may have occurred on the machine you were using at the time that window was shown, or it may have occurred on another machine previously. Because the file was modified in two different locations without a synchronization between them, Steam cannot automatically pick which version of the file to keep.

You will most likely want to pick the version of the files that was modified most recently. This means you will have the progress made the last time you played the game. However, you would want to carefully consider how the dates and times in the conflict window for the cloud save files correspond to your behavior and progress within the game. This context will help you decide which files to select.

Note that playing games in Offline Mode will keep games from syncing until you've gone back online, and this is very likely to cause a conflict.


# What if Steam is unable to sync files to the cloud?

{STEAM_CLAN_IMAGE}/39983882/d748d6d0e9a247933e898ca694a491eaf0248090.png

This error indicates that Steam could not sync your local files to the Steam Cloud. It could be a temporary issue, or something could be wrong with your network that would need to be addressed.

Users are encouraged to address the underlying cause of the error prior to launching the game.

Ignoring the message and selecting "play game" could potentially cause a conflict between the cloud and your local files, resulting in lost data or progress.


# What if I lost a file or progress after moving to a different machine?

If you are not seeing your most recent progress and you have double-checked that the game uses Steam Cloud on its store page, either Steam was not able to sync successfully with Steam Cloud before closing, or the sync resulted in a previous version of your data being uploaded to the cloud.

It’s possible that the original file or progress is still on the older machine, but was unable to sync. It may be possible to launch Steam from that machine and see if it will Sync the game. If that works, the progress should be available on the newer machine the next time you launch.

Also, many games do not use Steam cloud to store save games. The game developer will be able to help you find and transfer those files if you are using a new machine and still have access to the old one. If you no longer have access to the previous machine, those save game cannot be recovered.

Steam Support can provide further clarification on how the Cloud system works, but they cannot recover lost saves or assist in resolving cloud conflicts.


# What if I have an issue with cross-platform cloud data?

Steam supports cross-platform integration of cloud data between different operating systems.

However, not all games make use of this feature. You would want to check with the community or the developer to confirm the details of cross-platform cloud integration.


# Steam Cloud Troubleshooting

If you are continually experiencing issues with Steam cloud functionality, it's possible that something is interfering with the cloud or preventing it from working as expected.

It's a good idea to investigate each of the following scenarios to make sure that your machine is capable of using the cloud successfully.

Because some of these are advanced troubleshooting steps that involve areas outside of Steam, we highly recommend that you contact a local IT support specialist in your area to make sure that they are performed correctly.

## Refresh Local Network Hardware
This includes restarting all modems & routers. Network hardware can get into slow/broken state after running for a long time. This can cause cloud sync to take longer than normal, or to fail completely.

If you are using a wireless network connection, you will want to bypass this with a direct Ethernet connection between your machine and network hardware.

## Test Online Connection
Some Internet providers cache or compress online data to save bandwidth (especially cellphone networks). This can cause issues with Steam. It is a good idea to test the issue by connecting to an entirely different network, preferably from a different service provider.

## Investigate Firewalls
Certain firewalls may prevent Steam from talking to its servers. You'll want to work with a tech support specialist to ensure that the Firewall is not interfering. You may even need to temporarily disable it for testing purposes or add exceptions to your firewalls for Steam.

## Investigate Anti-Virus Software
AV software hooks very deep into user systems and can affect disk and network operations which may cause issues with Steam. Some games also use copy protection technology that can appear as malicious software to an AV scanner, resulting in potential false-positive alerts.

You'll want to work with a tech support specialist to ensure that your AV software is not interfering with Steam functionality. You may even need to temporarily disable it for testing purposes. It may also be necessary to add exceptions for Steam in your AV configuration (for example, excluding Steam cloud folders like ...\\Steam\\userdata and installation folders for Steam games from live monitoring services).

## Investigate Other Programs & Services
Any software that modifies or monitors system, disk or network activity can cause issues while downloading or running a game. These programs and services can run in the background and are typically associated with software like Anti-Virus, ad-blockers, web-optimizers, firewalls, system cleaners, recording software, proxies, performance boosters etc.

You'll want to work with a tech support specialist to ensure that these services & programs are not interfering with Steam. You may even need to temporarily disable them for testing purposes.
