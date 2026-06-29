# How To: Discord Rich Presence RPC Support

Heroic has built-in support for Discord Rich Presence integration, to always display the Heroic games you're playing in Discord.

This feature will automatically update Discord with the name and cover art of your currently playing games.

![image](https://github.com/user-attachments/assets/026be49c-9ae1-40cc-a159-d5241e991dfa)


# Requirements:

- Enable **"Settings: General: Enable Discord Rich Presence"** in **Heroic**.
- Enable **"Activity Privacy: Share your detected activities with others"** in **Discord**.
- Ensure that **Discord RPC is enabled in your chat client**. The official Discord client always provides it, whereas [Vesktop](https://github.com/Vencord/Vesktop) for example has it under "Vesktop Settings: Enable Rich Presence via arRPC".


# Troubleshooting:

## Native (Host) Discord Clients:

- If you are using a **native Discord client** when Heroic is running in a Flatpak, then you **must** install the [discord-flatpak-rpc-bridge](https://github.com/Arcitec/discord-flatpak-rpc-bridge), to create a bridge between the Flatpak Discord RPC socket and your native Discord RPC socket. That project has a detailed description about why the Flatpak sandboxing makes that necessary, and why there will _never_ be any other solutions.


## Flatpak-based Discord Clients:

- If you are using a **Flatpak Discord client** and Flatpak Heroic, then Rich Presence should work immediately if the Flatpak Discord client is correctly configured to expose its RPC socket.
- The [official Discord Flatpak](https://flathub.org/apps/com.discordapp.Discord) is an example of a correctly configured Flatpak Discord client. Many third-party clients do not have correctly configured Flatpaks, so you may have to switch to the official client, or ask your third-party client's maintainer to improve their Flatpak wrapper. Third-party clients must expose the _exact_ same RPC socket path as the official Discord Flatpak.
