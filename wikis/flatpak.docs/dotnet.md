# Dotnet

## Prerequisites

- [Building your first Flatpak](first-build.md)

- The application is built with a Linux-compatible .NET desktop application framework such as:  
  - [Avalonia UI](https://avaloniaui.net/)

  - [Uno Platform](https://platform.uno/)

  - [Eto](https://github.com/picoe/Eto)

  - [GTKSharp](https://github.com/GtkSharp/GtkSharp)

  - [Gir.Core](https://gircore.github.io/)

- The application’s source code is hosted on a Git server such as GitHub, GitLab, or Bitbucket

## Steps for Packaging

### Installing Flatpak and Flatpak builder

1.  Install Flatpak using the method provided for your distribution [Flatpak - Quick Setup](https://flatpak.org/setup/)

2.  Install Flatpak Builder through your distribution package manager (e.g. `apt` / `dnf`)

    sudo apt install flatpak-builder

### Creating the Flatpak

A few placeholders have been used in the steps below, while going through the steps replace these with the ones respective to your project:

- `<app-id>`: The name of your Flatpak, see [Application IDs](conventions.md#application-ids).

- `<app-name>`: The name of the root folder of your app repository

- `<project-name>`: The name of your `.csproj` file

- `<git-url>`: The URL to the git repository of the project

3.  Create a new folder somewhere different from your existing project

4.  Create a YAML file titled `<app-id>.yaml` with the following example template, replacing the placeholders with the appropriate information. (Note: If your project file lives in a subfolder, be sure to include that in the build paths in this file and subsequent commands as well.):

    id: <app-id>
    runtime: org.freedesktop.Platform
    runtime-version: '24.08'
    sdk: org.freedesktop.Sdk
    sdk-extensions:
      - org.freedesktop.Sdk.Extension.dotnet8
    build-options:
      prepend-path: "/usr/lib/sdk/dotnet8/bin"
      append-ld-library-path: "/usr/lib/sdk/dotnet8/lib"
      prepend-pkg-config-path: "/usr/lib/sdk/dotnet8/lib/pkgconfig"

    command: <project-name>

    finish-args:
      - --device=dri
      # TODO: Replace this with wayland and fallback-x11 once Wayland support
      #       becomes available:
      #       https://github.com/AvaloniaUI/Avalonia/pull/8003
      - --socket=x11
      - --share=ipc
      - --env=DOTNET_ROOT=/app/lib/dotnet

    modules:
      - name: dotnet
        buildsystem: simple
        build-commands:
        - /usr/lib/sdk/dotnet8/bin/install.sh

      - name: <app-name>
        buildsystem: simple
        sources:
          - type: git
            url: <git-url>
          - ./nuget-sources.json
        build-commands:
          - dotnet publish <project-name>.csproj -c Release --no-self-contained --source ./nuget-sources
          - mkdir -p ${FLATPAK_DEST}/bin
          - cp -r bin/Release/net8.0/publish/* ${FLATPAK_DEST}/bin

Note

For providing access to other things such as the network or filesystem, see [Sandbox Permissions](sandbox-permissions.md)

5.  Copy and save the dotnet NuGet sources generator script `flatpak-dotnet-generator.py` from the [Flatpak Builder Tools repository](https://github.com/flatpak/flatpak-builder-tools), to the current folder, or run the following command to download it:

    wget https://raw.githubusercontent.com/flatpak/flatpak-builder-tools/master/dotnet/flatpak-dotnet-generator.py

6.  Clone down your project repository to the folder

    git clone <git-url>

7.  Install dependencies from Flathub

    flatpak-builder build-dir --user --install-deps-from=flathub --download-only <app-id>.yaml

8.  Run the NuGet source config generator script `flatpak-dotnet-generator.py` with the following arguments:

    python3 flatpak-dotnet-generator.py --dotnet 8 --freedesktop 24.08 nuget-sources.json <app-name>/<project-name>.csproj

9.  Build and install using Flatpak builder

    flatpak-builder build-dir --user --force-clean --install --repo=repo <app-id>.yaml

### Testing the build

10. Run the installed Flatpak application

    flatpak run <app-id>
