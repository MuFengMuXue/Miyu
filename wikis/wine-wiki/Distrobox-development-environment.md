# Why `distrobox`?
* Container-based solution, keeps the host clean.
* It provides tight integration with the host out of the box.
* Simple and fast to setup (10 minutes, probably less) and to bring up (seconds).
* See project [repo](https://github.com/89luca89/distrobox) and [website](https://distrobox.it/) for more.

# Prerequisites
Install `distrobox`:
* The easiest way to do this is to use your package manager. On Ubuntu, for example, you can do this with:
  ```shell
  apt install distrobox
  ```
 * If your distribution does not provide a package (or provides an outdated version), check the ["Alternative methods"](https://github.com/89luca89/distrobox?tab=readme-ov-file#alternative-methods) sub-section of the installation documentation.

# Create a `wine-devel` distrobox (i.e. container)
* Run the below, replacing `wine-devel` with whatever you want to call your distrobox. It will create:
  - `wine-devel.ini`, the `distrobox` manifest file (in the working directory).
  - `setup-wine-devel.sh`, a simple wrapper script (in the working directory). This calls `distrobox assemble create` with the parameters needed to end up with a container based on the latest `Ubuntu LTS` version with all build dependencies met for Wine. Have a look inside this file to understand what it does and, perhaps, add/remove build dependencies depending on your needs.
  - `devenv-init.sh` - this is to be run **from within the container** and is optional, but recommended:
    - It appends a `cd` to your container's `~/.${SHELL}.rc`, which ensures that you always start in the container's `HOME` directory every time you run `distrobox enter` (rather than the current working directory). This helps avoid littering other directories unintentionally. Note that you can achieve the same result by using `--no-workdir` _every time_ you enter the container:
      ```shell
      distrobox enter wine-devel --no-workdir
      ```
    - Another one-off configuration I found useful is to define or command aliases or environment variables such as `WINE_SOURCE=~/wine-source` within the container's `~/.${SHELL}.rc` file. You can then reference these aliases/variables in whatever scripts/one-liners you use for your usual day-to-day activities, e.g. building Wine, or shrinking down large log files when debugging.
    - You can also add to `devenv-init.sh` any one-off configuration/setup that you might want within your container, like cloning a repo.

  ```shell
  DISTROBOX_NAME=wine-devel
  DISTROBOX_HOME=$HOME/$DISTROBOX_NAME
  mkdir -p $DISTROBOX_HOME # Distrobox will create the container's HOME directory anyway, but create it beforehand to store `devenv-init.sh`
  
  # Host
  DISTROBOX_ASSEMBLE_SCRIPT=setup-$DISTROBOX_NAME.sh
  DISTROBOX_MANIFEST=$DISTROBOX_NAME.ini
  
  # Container
  DEVENV_INIT_SCRIPT=$DISTROBOX_HOME/devenv-init.sh
  
  cat << EOF > setup-$DISTROBOX_NAME.sh
  #! /bin/sh
  DISTROBOX_NAME=$DISTROBOX_NAME
  DISTROBOX_MANIFEST=$DISTROBOX_MANIFEST
  
  export DISTROBOX_HOME=$DISTROBOX_HOME
  
  ADD_PKGS_BASE="git gdb ccache valgrind"
  ADD_PKGS_UTILS="vim tmux meld icecc"
  ADD_PKGS_WINE_DEVEL_DEPS="make \\
                            flex \\
                            bison \\
                            gcc-multilib \\
                            gcc-mingw-w64 \\
                            libglib2.0-dev libglib2.0-dev:i386 \\
                            libasound2-dev libasound2-dev:i386 \\
                            bluez \\
                            libpulse-dev libpulse-dev:i386 \\
                            libdbus-1-dev libdbus-1-dev:i386 \\
                            libfontconfig-dev libfontconfig-dev:i386 \\
                            libfreetype-dev libfreetype-dev:i386 \\
                            libgnutls28-dev libgnutls28-dev:i386 \\
                            libgl-dev libgl-dev:i386 \\
                            libunwind-dev libunwind-dev:i386 \\
                            libx11-dev libx11-dev:i386 \\
                            libxcomposite-dev libxcomposite-dev:i386 \\
                            libxcursor-dev libxcursor-dev:i386 \\
                            libxfixes-dev libxfixes-dev:i386 \\
                            libxi-dev libxi-dev:i386 \\
                            libxrandr-dev libxrandr-dev:i386 \\
                            libxrender-dev libxrender-dev:i386 \\
                            libxext-dev libxext-dev:i386 \\
                            libwayland-bin \\
                            libwayland-dev libwayland-dev:i386 \\
                            libegl-dev libegl-dev:i386 \\
                            libxkbcommon-dev libxkbcommon-dev:i386 \\
                            libxkbregistry-dev libxkbregistry-dev:i386 \\
                            libgstreamer1.0-dev libgstreamer1.0-dev:i386 \\
                            libosmesa6-dev libosmesa6-dev:i386 \\
                            libsdl2-dev libsdl2-dev:i386 \\
                            libudev-dev libudev-dev:i386 \\
                            libvulkan-dev libvulkan-dev:i386 \\
                            libavformat-dev libavformat-dev:i386 \\
                            libgstreamer-plugins-base1.0-dev:i386" # libgstreamer-plugins-base1.0-dev skipped, conflicts with i386 variant - see https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1016631
  
  export ADD_PKGS="\$ADD_PKGS_BASE \$ADD_PKGS_UTILS \$ADD_PKGS_WINE_DEVEL_DEPS"
  
  export PRE_INIT_HOOKS="dpkg --add-architecture i386" # 32-bit dependencies
  
  distrobox assemble create --file \$DISTROBOX_MANIFEST
  EOF
  
  cat << EOF > $DISTROBOX_MANIFEST
  [$DISTROBOX_NAME]
  image=ubuntu:latest # Latest LTS release
  home=\$DISTROBOX_HOME
  additional_packages=\$ADD_PKGS
  root=false
  start_now=true
  pre_init_hooks=\$PRE_INIT_HOOKS
  EOF
  
  cat << EOF > $DEVENV_INIT_SCRIPT
  #! /bin/sh
  printf "\ncd" >> \$HOME/.\${SHELL}rc
  EOF
  
  reset
  
  echo "1. Run the generated script \"./$DISTROBOX_ASSEMBLE_SCRIPT\" to create a distrobox container."
  echo "2. Run \"distrobox enter $DISTROBOX_NAME\" to enter the container."
  echo "3. Within the $DISTROBOX_NAME container, run the devenv init script with \"$DEVENV_INIT_SCRIPT\"."
  ```
* Follow the printed instructions (`distrobox enter` will clear the console output, so copy them to a text editor):
  1. Run the generated script `./setup-wine-devel.sh` to create a container with build dependencies for Wine met. This will take a few minutes, depending on your connection, computer's speed, etc.
  2. Run `distrobox enter wine-devel` to enter the container.
  3. [OPTIONAL] **Within the `wine-devel` container**, run the devenv init script:
     ```shell
     chmod +x $HOME/devenv-init.sh
     $HOME/devenv-init.sh
     ```
* That's it, you're now inside the development environment:
  - You can pull the Wine source code, [build it](https://gitlab.winehq.org/wine/wine/-/wikis/Building-Wine#plain-vanilla-compiling), and run Wine within the container.
  - You can also install tools you use for Wine development (e.g. an IDE or a diff tool), configure git and SSH keys, etc.
  - Graphical applications that you start from the container will utilise the host's desktop environment/window system. Likewise for any Windows applications that you launch with Wine from the container.

# Remarks
* The container will "inherit" the same shell as the host. `Distrobox` provides a way to override this if desired.

# Delete the container
* You can run the below. It will prompt you to stop, delete the `wine-devel` distrobox - along with its home directory (skip `--rm-home` if you don't want this).
  ```shell
  distrobox stop wine-devel
  distrobox rm wine-devel --rm-home
  ```
