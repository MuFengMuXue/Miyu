# Hypnotix

Hypnotix is an open-source IPTV streaming application with support for live TV channels, movies, and series. Originally developed by the Linux Mint team, it uses mpv as its playback engine. By default, it includes a free IPTV provider (Free-TV) with channels from around the world.

## Installation
To use Hypnotix, install the  package.

## Configuration
When launching Hypnotix for the first time, the "Free-TV" provider will appear automatically. To add your own services, follow these steps:

# Click on the Providers icon (the list icon in the top bar).
# Select Add a new provider.
# Enter the details according to your service:
:* Name: An identifier for your list.
:* Type: M3U URL (remote list), Local M3U (file on disk), or Xtream API (services with username/password).
:* URL/Path: The address of your channel list.

## Troubleshooting
## Black screen or playback error
If channels do not load or show a black screen, it is usually due to missing video codecs. Verify that you have the  and  package groups installed.

If you are using an NVIDIA graphics card, ensure that hardware acceleration is correctly configured for MPV. Refer to the Hardware video acceleration page for further details.
