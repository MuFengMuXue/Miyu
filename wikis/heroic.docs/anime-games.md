# Genshin Impact (Linux)

Since around April 2023, Genshin Impact has been playable in Linux. As of HoyoPlay Launcher v1.5.2, a runner based on Wine 10 must be used. The launcher can technically run with GE-Proton, but the game's anticheat behaves differently when using stock Proton versus GE-Proton, so stock Proton (e.g., Proton 10) installed via Steam is required to run the actual game.

1. Set the game's runner to Proton 10 or newer. (Note Steam's Proton is not displayed as an option by default in Heroic, go to the general settings > advanced and enable them as needed)
2. Ensure that umu is enabled (In Game Settings > Advanced, make sure the `Disable UMU` check is NOT checked)
3. If you get a `Wine C++ Runtime Library` error, add an environment variable for `WINEDLLOVERRIDES = lsteamclient=d`.

# Genshin Impact (macOS)

Use https://github.com/yaagl/yet-another-anime-game-launcher instead

# Zenless Zone Zero (Linux)

Zenless Zone Zero does not have the same anticheat restrictions as Genshin Impact. You can follow the above directions above if you prefer to use stock Proton. Otherwise, you can run HoyoPlay Launcher and the game with GE-Proton10-x with umu enabled.

# Zenless Zone Zero (macOS)

Use https://github.com/yaagl/yet-another-anime-game-launcher instead

# Infinity Nikki (Linux)

The EGS build of Infinity Nikki currently does work SteamOS running on the Steam Deck. However, any other device or distro, even if running on a Steam Deck, will not work.

# Wuthering Waves (Linux)

The [Steam version](https://store.steampowered.com/app/3513350/Wuthering_Waves/) includes a note stating "We're working to resolve Wuthering Waves' compatibility with STEAM DECK and will share updates in the community. Thanks for your understanding!"

# Arknights: Endfield (Linux)

The game works using DW-Proton which can be installed using ProtonPlus https://github.com/Vysp3r/protonplus

<img width="803" height="113" alt="image" src="https://github.com/user-attachments/assets/90251686-b503-45bf-90f8-e90221196470" />

Also `Ntsync` seems to be needed for the game to not crash constantly. You need a kernel version that supports ntsync and it will be enabled by default when available.
