So you want to contribute programming for OBS Studio? Great! Whether you're making a new plugin or tinkering with OBS's core, we appreciate all contributions to the project. Follow this guide to get up and running.

## A few things to know
If you're interested in doing OBS Studio development, you should be experienced in both the C and C++ programming languages, and Objective-C for Apple systems (optionally). It is highly recommended that you read [OBS Studio's Contributing guide](https://github.com/obsproject/obs-studio/blob/master/CONTRIBUTING.md) so that you know code guidelines as well as what is required when you want to submit a change.

## Developer Chat
Our developer community is always helpful to new developers wanting to get their feet wet with OBS programming. If you ever need help you can join the developer chat on Discord here: **[https://discord.gg/obsproject](https://discord.gg/obsproject)**

## Starting OBS Development

### 1. Get the code
Check out the source code for OBS Studio from Github: [https://github.com/obsproject/obs-studio](https://github.com/obsproject/obs-studio)

```
git clone --recursive https://github.com/obsproject/obs-studio.git
```

Don't forget the `--recursive` argument to get all submodules.

### 2. Build the code
The next step is to get the program building so that you can start making your modifications or plugins.

A guide for building OBS Studio for your platform can be found here: [https://github.com/obsproject/obs-studio/wiki/Building-OBS-Studio](https://github.com/obsproject/obs-studio/wiki/Building-OBS-Studio)

### 3. Read the documentation
OBS's reference documentation can be found here: [https://obsproject.com/docs/](https://obsproject.com/docs/)

It's also recommended to examine some of the default plugins to see how they interact with the API in OBS Studio. Note that the OBS core (/libobs) is separate from the OBS UI (/ui), which is also separate from OBS core plugins (/plugins), so you can begin to see how the different modules of code fit together.

### 4. Check out issues on the Ideas page and the Bug Tracker

Many user post ideas and suggestions for improvements to OBS on the OBS Ideas page. You can find the Ideas page (Fider) here: [https://ideas.obsproject.com/](https://ideas.obsproject.com/)

OBS Studio currently tracks bugs on [GitHub Issues](https://github.com/obsproject/obs-studio/issues).

Feel free to explore ideas, issues, suggestions, and bugs, and if you feel so inclined, try your hand at implementing one!

## Plugin Development

Many people want to get into OBS Studio development in order to make a plugin, rather than alter core functionality. It turns out that OBS code is already pretty modular, and many features that are considered "core" features are actually plugins that just come bundled with OBS, so learning about OBS development really means learning about plugin development as well.

For more details on plugin development, check this page of the documentation: [https://obsproject.com/docs/plugins.html](https://obsproject.com/docs/plugins.html)

We strongly recommend using the OBS plugin template as a starting point for new plugin development: **[https://github.com/obsproject/obs-plugintemplate](https://github.com/obsproject/obs-plugintemplate)**

### Example plugins

* Example source plugin: [Color Source](https://github.com/obsproject/obs-studio/blob/master/plugins/image-source/color-source.c)
* Example service plugin: [Custom RTMP Service](https://github.com/obsproject/obs-studio/blob/master/plugins/rtmp-services/rtmp-custom.c)
* Example encoder plugin: [x264 Encoder](https://github.com/obsproject/obs-studio/blob/master/plugins/obs-x264/obs-x264.c)
* Example output plugin: [FLV Output](https://github.com/obsproject/obs-studio/blob/master/plugins/obs-outputs/flv-output.c)

## Scripting

Many people want to write modules for OBS, but are not familiar with C/C++, or don't want to go through the trouble of setting up a build environment. Fortunately, OBS is capable of running Lua and Python scripts via the bundled LuaJIT or your system's Python environment. These scripts are capable of accessing the OBS API and doing many of the same things you could do by writing OBS C/C++ code directly. In fact, you can even make new plugins with Lua (though not with Python).

For more details on scripting, check this page of the documentation: https://obsproject.com/docs/scripting.html

## A quick note about licensing

OBS Studio is an open source program licensed under the [GPLv2](https://github.com/obsproject/obs-studio/blob/master/COPYING). That means that if you create a plugin for OBS Studio or a modified version of OBS Studio and distribute it in binary form, you must give users a way to access the source code of your binary. Otherwise, you will be in violation of the license. The easiest way to do this is to have a public Github repository of your fork or plugin, and include a text file in your download for the binary containing a link to the repo. The relevant part of the license is under section 3 of the GPLv2.

Thanks for being willing to help out, and good luck!