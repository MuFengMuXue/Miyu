# GE-Proton (Proton-GE-Custom)

Custom build of Proton with bleeding-edge Proton Experimental Wine.

Source: https://github.com/GloriousEggroll/proton-ge-custom

**Note:** This is a custom build of Proton, not affiliated with Valve's Proton.

**Note:** If you have an issue with GE-Proton that does not happen on Valve's Proton, open an issue on the GE-Proton repository, not Valve's bug tracker.

## Overview

GE-Proton contains features that Valve's Proton currently does not:

- Additional media foundation patches for better video playback support
- AMD FSR patches added directly to fullscreen hack (toggle with WINE_FULLSCREEN_FSR=1)
- NVIDIA CUDA support for PhysX and NVAPI
- Raw input mouse support
- 'protonfixes' system - automated per-game fixes (winetricks changes, environment variables, EAC workarounds, overrides, etc.)
- Various upstream Wine patches backported
- Various wine-staging patches applied as needed
- NTSync enablement if the kernel supports it

## Important Notes

- Running non-Steam games with GE-Proton outside of Steam is only supported using umu: https://github.com/Open-Wine-Components/umu-launcher
- Proton runs in a container with a specific runtime environment. Not running it as intended breaks library compatibility.
- umu-launcher is designed to mimic Steam's containerized runtime environment without needing Steam.
- Heroic has enabled umu by default when using GE-Proton.
- Lutris has integrated umu as the default backend when GE-Proton (Latest) is selected.

## Installation

### Prerequisites

You must have proper Vulkan drivers and packages installed. VKD3D on AMD requires Mesa 22.0.0 or higher for the VK_KHR_dynamic_rendering extension.

### Via ProtonPlus (GUI Manager)

ProtonPlus is a GUI frontend for managing proton versions including GE-Proton. Select the "Proton-GE" dropdown and choose a version or "Proton-GE Latest" for automatic updates. After install, restart Steam and enable GE-Proton.

### Via asdf (Version Manager)

Unofficial plugin for installing and managing GE-Proton versions:
```bash
asdf plugin add protonge
asdf install protonge latest
```

### Native Steam (Manual)

1. Download a release from https://github.com/GloriousEggroll/proton-ge-custom/releases
2. Create ~/.steam/steam/compatibilitytools.d if it does not exist
3. Extract: `tar -xf GE-Proton*.tar.gz -C ~/.steam/steam/compatibilitytools.d/`
4. Restart Steam
5. Enable GE-Proton in Steam properties

#### Quick Install Script (Native)

```bash
rm -rf /tmp/proton-ge-custom
mkdir /tmp/proton-ge-custom && cd /tmp/proton-ge-custom

tarball_url=$(curl -s https://api.github.com/repos/GloriousEggroll/proton-ge-custom/releases/latest | grep browser_download_url | cut -d\" -f4 | grep .tar.gz)
curl -# -L $tarball_url -o $(basename $tarball_url) --no-progress-meter

checksum_url=$(curl -s https://api.github.com/repos/GloriousEggroll/proton-ge-custom/releases/latest | grep browser_download_url | cut -d\" -f4 | grep .sha512sum)
curl -# -L $checksum_url -o $(basename $checksum_url) --no-progress-meter

sha512sum -c $(basename $checksum_url)

mkdir -p ~/.steam/steam/compatibilitytools.d
tar -xf $(basename $tarball_url) -C ~/.steam/steam/compatibilitytools.d/
```

### Flatpak Steam (Manual)

1. Download a release from https://github.com/GloriousEggroll/proton-ge-custom/releases
2. Create directory: `~/.var/app/com.valvesoftware.Steam/data/Steam/compatibilitytools.d/`
3. Extract: `tar -xf GE-Proton*.tar.gz -C ~/.var/app/com.valvesoftware.Steam/data/Steam/compatibilitytools.d/`
4. Restart Steam and enable GE-Proton

### Flatpak Steam (Flathub - Unofficial)

```bash
flatpak install com.valvesoftware.Steam.CompatibilityTool.Proton-GE
```
Note: This unofficial build is not supported by GloriousEggroll or Valve.

### Snap Steam (Manual)

1. Download a release
2. Create: `~/snap/steam/common/.steam/steam/compatibilitytools.d/`
3. Extract: `tar -xf GE-Proton*.tar.gz -C ~/snap/steam/common/.steam/steam/compatibilitytools.d/`
4. Restart Steam and enable GE-Proton

## Building

1. Clone the repository:
   ```bash
   git clone --recurse-submodules https://github.com/gloriouseggroll/proton-ge-custom
   ```

2. Add custom patches to patches/, then edit patches/protonprep-valve-staging.sh

3. Apply patches:
   ```bash
   ./patches/protonprep-valve-staging.sh &> patchlog.txt
   grep -i fail patchlog.txt
   grep -i error patchlog.txt
   ```

4. Build:
   ```bash
   mkdir build && cd build
   ../configure.sh --build-name=SOME-BUILD-NAME
   make redist &> log
   ```

## Enabling GE-Proton in Steam

1. Right click any game in Steam -> Properties
2. In the Compatibility tab, check "Force the use of a specific Steam Play compatibility tool"
3. Select the desired GE-Proton version
4. Launch the game

## Environment Variables / Options

### HDR

Requires: HDR-supporting compositor, game, and monitor. Enables wine-wayland driver automatically.
```bash
PROTON_ENABLE_HDR=1 %command%
```
Note: In-game Steam overlay will not work with Wayland enabled. Steam Input does not work properly with wine-wayland driver.

### NTSync

Requires kernel 6.14+ with CONFIG_NTSYNC=y or CONFIG_NTSYNC=m.

If using CONFIG_NTSYNC=m, add to /etc/modules-load.d/ntsync.conf:
```
ntsync
```

Or manually: `sudo modprobe ntsync`

### Full Environment Variable Reference

| Config String | Variable | Description |
| :--- | :--- | :--- |
| | PROTON_LOG | Dump debug log to $HOME/steam-$APPID.log |
| | PROTON_DUMP_DEBUG_COMMANDS | Write debug scripts to $PROTON_DEBUG_DIR/proton_$USER/ |
| | PROTON_DEBUG_DIR | Root dir for debug scripts (default: /tmp) |
| wined3d | PROTON_USE_WINED3D | Use OpenGL wined3d instead of Vulkan DXVK |
| nod3d12 | PROTON_NO_D3D12 | Disable DX12 |
| nod3d11 | PROTON_NO_D3D11 | Disable DX11 |
| nod3d10 | PROTON_NO_D3D10 | Disable DX10 |
| nod3d9 | PROTON_NO_D3D9 | Disable DX9 |
| noesync | PROTON_NO_ESYNC | Disable eventfd-based sync |
| nofsync | PROTON_NO_FSYNC | Disable futex-based sync |
| nontsync | PROTON_NO_NTSYNC | Disable ntsync kernel module |
| forcelgadd | PROTON_FORCE_LARGE_ADDRESS_AWARE | Force LARGE_ADDRESS_AWARE for all executables |
| heapdelayfree | PROTON_HEAP_DELAY_FREE | Delay freeing memory (workaround for use-after-free bugs) |
| | HOST_LC_ALL | Override system locale for a game |
| enablenvapi | PROTON_ENABLE_NVAPI | Enable NVIDIA NVAPI GPU support |
| noforcelgadd | | Disable forcelgadd |
| oldglstr | PROTON_OLD_GL_STRING | Limit GL extension string length for old games |
| cmdlineappend: | | Append string as game argument (escape commas/backslashes) |
| xalia / noxalia | PROTON_USE_XALIA | Enable/disable Xalia gamepad UI for keyboard/mouse interfaces |
| seccomp | PROTON_USE_SECCOMP | Enable seccomp-bpf for DRM protections |
| nowritewatch | PROTON_NO_WRITE_WATCH | Disable memory write watches (can improve performance for specific games) |
| | WINE_FULLSCREEN_FSR | Enable AMD FSR (Vulkan games only) |
| | WINE_FULLSCREEN_FSR_STRENGTH | FSR sharpening (0=max sharp, 5=least sharp, default=2) |
| | WINE_FULLSCREEN_FSR_CUSTOM_MODE | Set fake screen resolution (WIDTHxHEIGHT) |
| | WINE_DO_NOT_CREATE_DXGI_DEVICE_MANAGER | Fix miscolored video playback in some games |
| | COPYPREFIX | Copy game prefix and shader cache (for SteamDeck) |
| fsr4 | PROTON_FSR4_UPGRADE | Auto-download and upgrade FSR 3.1 to FSR 4 |
| fsr4hud | PROTON_FSR4_INDICATOR | Enable FSR4 watermark |
| fsr4rdna3 | PROTON_FSR4_RDNA3_UPGRADE | FSR4 upgrade for RDNA3 GPUs |
| fsr3 | PROTON_FSR3_UPGRADE | FSR3 upgrade |
| dlss | PROTON_DLSS_UPGRADE | Auto-download newer DLSS DLLs |
| dlsshud | PROTON_DLSS_INDICATOR | Enable DLSS overlay |
| xess | PROTON_XESS_UPGRADE | XeSS upgrade |
| sdlinput | PROTON_USE_SDL / PROTON_PREFER_SDL | Use SDL input instead of HIDRAW/Steam Input |
| wayland | PROTON_USE_WAYLAND / PROTON_ENABLE_WAYLAND | Enable Wayland driver |
| wow64 | PROTON_USE_WOW64 | Enable wow64 |
| | WAYLANDDRV_PRIMARY_MONITOR | Specify primary monitor (e.g. eDP-1) |
| | PROTON_ENABLE_MEDIACONV | Enable media converter for winegstreamer |
| | WAYLANDDRV_RAWINPUT | Adjust raw input sensitivity (0=accelerated, positive=unaccelerated with sensitivity) |
