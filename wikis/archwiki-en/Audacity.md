# Audacity

From Audacity:
: Audacity is an easy-to-use, multi-track audio editor and recorder for Windows, macOS, GNU/Linux and other operating systems.

## Installation
Install the  package.

## Tips and tricks
## Tenacity fork
In May 2021, after the project was acquired by Muse Group there was a draft proposal to add opt-in telemetry to the code to record application usage. As an alternative, a group of volunteers created Tenacity, a community-driven fork maintained as open-source software.

## Troubleshooting
## High memory usage on Wayland
When recording or playing audio in Audacity under Wayland, memory usage is drastically growing while the Audacity window is in focus. This can cause the entire system to freeze and fail the recording. Until this memory leak is fixed, it is recommended to start Audacity with

 $ GDK_BACKEND=x11 audacity

See  for more context.

This issue appears to have been fixed as of February 2024, with Audacity pushing

 $ Exec=env GDK_BACKEND=x11 UBUNTU_MENUPROXY=0 audacity %F

to the audacity.desktop file.

## Cannot record from microphone under PulseAudio
Refer to PulseAudio/Troubleshooting#Audacity
