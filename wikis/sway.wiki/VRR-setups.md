This page collects test results for Variable Refresh Rate (VRR) aka. adaptive sync setups seen in the wild.

To add an entry:

- Enable VRR on your display(s) via `output <name> adaptive_sync on` (see `sway-output(5)` for details)
- Make sure VRR is enabled with `swaymsg -t get_outputs | jq '.[] | pick(.name, .adaptive_sync_status)'`
- Play with your desktop for a while, try various apps (text editing, web browsing, video, games)
- Also play with the backlight level
- You can check your actual rate with `vbltest`
- To get the VRR range, you can use: `cat /sys/class/drm/card0-DP-1/edid | edid-decode` (look for "Display Range Limits")

| Screen | GPU | VRR range | Notes
| ------ | --- | --------- | -----
| Acer VG270U P | AMD RX 480 | 40-144 Hz | No flickering
| Acer XF270HU | AMD RX 5700 XT | 40-144 Hz | 2560x1440, no flickering
| Acer XV273K | AMD RX 6700 XT | 48-120 Hz | No flickering
| AOC Q27G2U | AMD Vega 64 | 48-144 Hz | Flickering on transitions between 48-75 Hz
| ASUS VP28U | AMD RX 550 | 40-60 Hz | Flickering when only terminal open and typing intermittently
| ASUS VG249 | AMD RX 6700 | 40-165 Hz | 1920x1080, no issues found
| BenQ EL2870U | AMD RX 580 | 40-60 Hz | No flickering
| BOE NE135A1M-NY1 (Framework 13 2.8K display) | AMD Radeon 780M | 30-120 Hz | 2880x1920 - No issues, no flickering
| Dell AW3423DWF | AMD RX 6800XT | 48-165 Hz | 3440x1440, Flickers on the desktop without any input, between 48-74Hz. When moving the mouse/using the keyboard, flickers much more as it transitions from a base of 48Hz to 165Hz on every input. Does not happen on Windows
| Dell S2719DGF | AMD RX 5700XT | 40-144 Hz | 2560x1440, Flickering, especially noticeable when moving the mouse. Does not happen on a Windows boot
| Dell S2721DGF | Intel Iris Xe (1165G7) | 48-165 Hz | 2560x1440, no issues
| Dell S2721DGF | AMD RX 5500 XT | 48-165 Hz | 2560x1440, occasionally flickers at 48 Hz but not 72 Hz.
| Dell S2721DGFA | AMD RX 6800 | 165 Hz | 2560x1440, no issues
| Dell S3220DGF | AMD RX 580 | 48-164 Hz | No flickering, but image darkens at higher refresh
| Gigabyte M32U | AMD RX 6750 XT | 48-144 Hz | 3840x2160, no issues
| Gigabyte G34WQC A | AMD Radeon RX 5600 XT | 48-144 Hz | Noticeable brightness flicker especially with dark backgrounds when typing or moving the mouse |
| LG 27GL83A-B | AMD RX 480 | 48-144 Hz | Very occasional horizontal black bar while typing
| LG 27GL83A-B | AMD RX 580 | 48-144 Hz | Very occasional horizontal black bar while typing
| LG 27GL83A-B | AMD RX 5700 XT | 48-144 Hz | No flickering
| LG 27GL850-B | AMD RX 6600 | 48-144 Hz | 2560x1440, no issues
| LG 27GN800-B | AMD Vega 56 | 48-144 Hz | Occasional horizontal black bar
| LG 34GN850-B | AMD RX 5700 XT | 48-160 Hz | No flickering
| LG 34UC88 | AMD Vega 64 | 55-75 Hz | Flickering when typing or when moving the mouse 
| LG 35WN75C | AMD Vega 56 | 48-100 Hz | Noticeable brightness flicker especially with dark backgrounds when typing or moving the mouse
| MSI MAG274QRF-QD | AMD RX 6750 XT | 48-165 Hz | 2560x1440 -- occasional intense flickering episodes when outside of games and not moving the mouse
| Samsung LC49RG94 | AMD RX 580 | 48-120 Hz | 5120x1440, Flickering when moving the mouse. |
| Samsung C27HG70 | AMD RX 6700 XT | 48-144 Hz | Flickers a lot in the monitor's "ultimate" mode (48-144 Hz), no issues in standard mode (120-144 Hz). |
| Samsung LS49CG934SUXEN | AMD RX 6800 XT | 48-240 Hz | 5120x1440, no issues |
| Samsung LS49CG934SUXEN | Intel A770 OC 16GB | 48-240 Hz | 5120x1440, no issues |
| Samsung G80SD | AMD RX 7800XT | 48-240 Hz | 3840x2160, Only able to select up to 120hz, heavy flickering unless gpu power mode is set to high |