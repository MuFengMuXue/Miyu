# VCV Rack

VCV Rack is a modular analogue synthesizer, more precisely a Virtual Eurorack DAW. It uses a plug-in systems to add more Eurorack emulated modules. As hardware Eurorack, it can be connected to midi, audio sources and destination, and other Eurorack modules. See also Wikipedia:VCV Rack. VCV Rack allow input from computer keyboard too, via the rack module MIDI-CV (included in "fundamental" modules pack).

The main principle of a modular analogue synthesizer is to add several module in the rack, and connect the different modules with wires, here by clicking on a connector and dragging in into another connector. Buttons on the modules allow you to change specifics parameters of the module.

## Installation
There are several possible ways to install VCV Rack as an Arch package, choose the one that meets your requirements:

## vcvrack
 builds completely from source code with some selected libraries like GLFW linked dynamically and includes minor patches for better system integration:

* Supports system-wide plugin packages which can be used without an online account. These are installed to  from the  package group.
* Adds a custom MIME type for .vcv files downloaded e.g. from Patchstorage which allows opening patches from the file browser
* Native Wayland support through system GLFW library
* aarch64 support (no aarch64 plugins in library though, you will need to build plugins manually or from AUR)

It's also available as a binary package through Unofficial user repositories#proaudio, which gets you automatic updates through pacman and lets you install all available system-wide plugin packages using . Since it's not officially supported by VCV Rack developers, please contact the package maintainers for help first.

## vcvrack-bin
 installs the official binary to  and only supports plugins installed from the library. Since this is the official binary, you should get support from VCV Rack developers.

## vcvrack-pro
 installs the commercial Pro version to  and its CLAP, VST 2 and 3 plugins to the appropriate system paths. It can be installed side-by-side with one of the above variants but requires a Pro/VCV+ account. During the build you are prompted for your login credentials unless a previously installed version is already logged in.

Similar to , only plugins installed from the library are supported, however these can then be shared with the Free version.

## Plugins
After logging in, free and commercial plugins (or "modules") can be installed from the library. These are installed to the Rack user directory, i.e. .

## Debug logs
Rack writes logs to , make sure to provide relevant logs when reporting issues.

## Using computer keyboard Input
To use computer keyboard Input:
* add the MIDI-CV module in your virtual Rack
* Click on the middle line on the screen of the module.
* Choose QWERTY keyboard for virtual piano keyboard
* Choose Numpad keyboard for virtual percussion keyboard
You can add two (or more) times the module, to have QWERTY part controlling some part of your setup and Numpad controlling some other part for example.

## Using computer audio input and output
The Audio-8 (8 channels) and Audio-16 (16 channels) modules, from the VCV Free (formerly Fundamental) modules pack, allow to input and output audio to JACK, PulseAudio, ALSA or (MIDI) Bridge Output. To set the desired Input or Output:
* Choose the desired sound library on the first line of the screen of the virtual module
* Select the Input or Output port on the Second line.

For using audio Input source into the modular setup use the "From device" connectors
For using audio Output destination, from the modular setup, use the "To device" connectors.

## Oscilloscope
The Scope module can show you the signal from any part of the setup; allowing you to debug your patch.

## Compiling plugins
You can find open source plugins in the Library.

## Manual build
If you're using , follow the manual making sure  is set to the SDK path. Plugins can only be installed to the user directory, system-wide plugins are not supported.

With ,  should implicitly be set to  or you might explicitly set it when building.

## PKGBUILD template
System-wide plugin packages are only supported by the  package, not by  or when manually downloading Rack from the website. Find the full template here.

{{hc|1=PKGBUILD|2=
_slug=Example # from plugin.json
_name=example # e.g. repo name
groups=(pro-audio vcvrack-plugins)
depends=(gcc-libs vcvrack)
makedepends=(simde zstd)

build() {
  cd $_name
  make SLUG=$_slug VERSION=$pkgver STRIP=: RACK_DIR=/usr/share/vcvrack dist
}

package() {
  cd $_name
  install -d "$pkgdir"/usr/lib/vcvrack/plugins
  cp -va dist/$_slug -t "$pkgdir"/usr/lib/vcvrack/plugins
}
}}
*  can be omitted when adding  to
*  disables stripping of debug symbols by Rack's makefiles, makepkg should do this instead and can optionally keep extracted debug symbols
*  points to shared makefiles by Rack
