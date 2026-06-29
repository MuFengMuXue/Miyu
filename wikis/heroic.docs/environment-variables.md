# Environment Variables


- [Introduction](#introduction)
- [External Documentation](#external-documentation)
- [%command%](#command)
- [Commonly Used Environment Variables](#commonly-used-environment-variables)
- [How to Set Environment Variables](#how-to-set-environment-variables)
- [How to Convert Steam Environment Variables to Heroic](#how-to-convert-steam-environment-variables-to-heroic)

## Introduction

In short, environment variables are a way to pass settings to a game on launch. Environment variables can tell the Proton runner to output a verbose log which can then allow the user to debug the game. Environment variables can also tell Proton to use different DLLs, either those bundled with Proton or those bundled with the game in the game's installed directory.

Do note many guides online will include tutorials on how to set environment variables in Steam. If you are using the Heroic Games Launcher, **do** not set environment variables in Steam. Instead set these variables directly in the Heroic Games Launcher. This page will cover how to do so. In addition, many guides will include `%command%`, this bit is **specifically for Steam**. It does **not** apply to Heroic. Do **not** add `%command% to environment variables you set in the Heroic Games Launcher.

Another important thing to keep in mind is that many guides can be frivolous with setting environment variables. These can be seen as a "magic bullet" to fix a game but in some cases, these environment variables can be unnecessary which can either not fix the game at all or mask the actual issue at hand.

Typically the most common use-case for an environment variable is debugging. In these cases, you will set an environment variable that prints out a verbose log which can allow you to further investigate the issue at hand. After you have resolved the issue, you can disable the environment variable. For specific instructions on debugging using environment variables, see [How to Debug Games Using Environment Variables)[https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/How-to-Debug-Games-Using-Environment-Variables]

## External Documentation

* [DXVK Debug Variables](https://github.com/doitsujin/dxvk/blob/master/README.md#debugging)
* [Proton Environment Variables](https://github.com/ValveSoftware/Proton#runtime-config-options)
* [VKD3D Environment Variables](https://github.com/HansKristian-Work/vkd3d-proton#environment-variables)
* [Wine Debug Variables](https://gitlab.winehq.org/wine/wine/-/wikis/Debug-Channels#examples)
* [Wine DLL Overrides](https://gitlab.winehq.org/wine/wine/-/wikis/Wine-User's-Guide#dll-overrides)
* [Wine Environment Variables](https://gitlab.winehq.org/wine/wine/-/wikis/Wine-User's-Guide#environment-variables)

## %command%

As noted in the introduction, `%command%` is **specifically for Steam**. **Do not** use `%command%` when setting environment variables in the Heroic Games Launcher.


## Commonly Used Environment Variables

* `WINEDEBUG=+fixme`
   * Outputs verbose logging information.
* `WINEDLLOVERRIDE=DLLNAME=n,b`
   * The `n` and `b` stand for `native` and `built-in`. This environment variable tells Proton to first check for any DLLs in the game's directory. If this fails or if it cannot find a DLL, it falls back to the DLL bundled with Proton.
   * For more information, see [Wine Environment Variables](https://gitlab.winehq.org/wine/wine/-/wikis/Wine-User's-Guide#environment-variables)
   * `WINEDLLOVERRIDES` is a common environment variable used for modding games.

## How to Set Environment Variables

Though Heroic Games Launcher does not require an `=`, these will often be included when sharing environment variables to clearly convey that the left side of the `=` is the `NAME` field and the right side is the `Value` field.

1. Open the Heroic Games Launcher.
2. Select a game and open the game's page.
3. In the top right, click the `Settings` button.
   * <img src="https://github.com/user-attachments/assets/4b03ffe5-3c30-490b-bf53-38edad2c2e85" height="300">
4. Click the `Advanced` tab and scroll down to the `Environment Variables` section.
   * <img src="https://github.com/user-attachments/assets/fb9d5948-10c3-4268-b245-63a009e7fd6b" height="300">
   * <img src="https://github.com/user-attachments/assets/bdf60c91-5739-46ba-b5ed-600488cdf3a5" height="300">
5. Set your environment variable(s), this example will use `WINEDEBUG=+fixme` as an example:
   * <img src="https://github.com/user-attachments/assets/4b635a92-4b45-429c-a661-1dd0d435a0fc" height="300">
6. Click the green `+` icon to save the environment variable(s).
   * <img src="https://github.com/user-attachments/assets/2311ef00-7db8-414f-8f6d-387fb5b6ae0a" height="300">
7. Your environment variable(s) will now be applied to this game in specific.

## How to Convert Steam Environment Variables to Heroic

On occasion, you may see users suggesting environment variables for Steam games as shown in the images below. However, these need to be converted slightly in order to be used in the Heroic Games Launcher.

* <img src="https://github.com/user-attachments/assets/4eb4c6f4-d1fb-46af-a9f5-c8415f5cae0b" width="500">
* <img src="https://github.com/user-attachments/assets/36346d8b-9ae5-44f5-affd-43f39849e511" height="200">

Using the second example in the image above, `WINEDLLOVERRIDES="winhttp=n,b" %command%`, Heroic does not need a `=` or `%command`. It also does not need quotes surrounding `winhttp=n,b`. In the Heroic Games Launcher, you will need to set `WINEDLLOVERRIDES` as the `NAME` field and `winhttp=n,b` **without quotes** as the `Value` field. For a step by step guide, see below.

Though Heroic Games Launcher does not require an `=`, these will often be included when sharing environment variables to clearly convey that the left side of the `=` is the `NAME` field and the right side is the `Value` field.

1. Open the Heroic Games Launcher.
2. Select a game and open the game's page.
3. In the top right, click the `Settings` button.
   * <img src="https://github.com/user-attachments/assets/4b03ffe5-3c30-490b-bf53-38edad2c2e85" height="300">
4. Click the `Advanced` tab and scroll down to the `Environment Variables` section.
   * <img src="https://github.com/user-attachments/assets/fb9d5948-10c3-4268-b245-63a009e7fd6b" height="300">
   * <img src="https://github.com/user-attachments/assets/bdf60c91-5739-46ba-b5ed-600488cdf3a5" height="300">
5. Using `WINEDLLOVERRIDES="winhttp=n,b" %command%` as an example, in the Heroic Games Launcher, it will look like the below image:
   * `WINEDLLOVERRIDES` is in the `NAME` field and `winhttp=n,b` is in the `Value` field.
   * <img src="https://github.com/user-attachments/assets/60f1fcb6-d77e-47c5-ac64-73c3c747b845" height="300">
6. Click the green `+` icon to save the environment variable.
7. Your environment variable will now be applied to this game in specific.


***
