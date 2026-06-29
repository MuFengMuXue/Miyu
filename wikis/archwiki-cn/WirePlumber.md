**翻译状态：**

  * 本文（或部分内容）译自 [WirePlumber](<https://wiki.archlinux.org/title/WirePlumber> "arch:WirePlumber")，最近一次同步于 2025-08-05，若英文版本有所[更改](<https://wiki.archlinux.org/title/WirePlumber?diff=0&oldid=842690>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/WirePlumber_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [PipeWire](<../zh-cn/PipeWire.html> "PipeWire")

[WirePlumber](<https://pipewire.pages.freedesktop.org/wireplumber>) 是一款强大的[PipeWire](<../zh-cn/PipeWire.html> "PipeWire") 会话和策略管理器。其采用模块化设计，使用 Lua 插件进行管理，具有高度可配置性及可扩展性。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [wireplumber](<https://archlinux.org/packages/?name=wireplumber>)包。任何冲突的 PipeWire 会话管理器会被卸载。 

WirePlumber 使用 systemd [用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "用户单元")管理 PipeWire 服务。 

##  配置

###  配置文件布局

[WirePlumber 的配置](<https://pipewire.pages.freedesktop.org/wireplumber/daemon/configuration.html>)使用 PipeWire 的 JSON 对象如 `context` 和 `alsa_monitor`，通过修改这些对象来控制其行为。配置文件位于 `~/.config/wireplumber/`（用户配置）、`/etc/wireplumber/`（全局配置）以及 `/usr/share/wireplumber/`（默认配置）。 

WirePlumber 启动时首先会读取[主配置文件](<https://pipewire.pages.freedesktop.org/wireplumber/daemon/configuration/conf_file.html>)。这是一个类 JSON 文件，用于设定 PipeWire 上下文环境（context）、[SPA 插件](<https://docs.pipewire.org/page_spa_plugins.html>)、模块以及组件。 

默认配置文件位于 `/usr/share/wireplumber/wireplumber.conf`，其是一个单实例配置文件，集成其他配置到一个进程中。请参阅文档 [ALSA 对象](<https://pipewire.pages.freedesktop.org/wireplumber/daemon/configuration/alsa.html>)、["access" 对象](<https://pipewire.pages.freedesktop.org/wireplumber/daemon/configuration/access.html>)和[蓝牙对象](<https://pipewire.pages.freedesktop.org/wireplumber/daemon/configuration/bluetooth.html>)。 

###  修改配置

推荐向 `/etc/wireplumber/` 或 `~/.config/wireplumber/` 目录下的 `wireplumber.conf.d/` 文件夹内添加 [SPA-JSON](<https://pipewire.pages.freedesktop.org/wireplumber/daemon/configuration/conf_file.html#the-spa-json-format>) 文件来配置 WirePlumber。 

用户配置较系统配置具有更高优先级，低优先级的同名配置文件会被忽略。在配置目录中，各文件按照字母数字顺序被读取，请参阅[文档](<https://pipewire.pages.freedesktop.org/wireplumber/daemon/locations.html#config-locations>)以了解详细信息。 

### Obtain interface name for rules matching

In the configuration, you need to specify `matches` rules with a property from an [object](<https://docs.pipewire.org/page_objects_design.html>) of the interface you want to configure. 

Use the command `wpctl status` to show all objects managed by WirePlumber. Find the `_ID_` assigned to the target interface. Then use command `wpctl inspect _ID_` to get a needed property. 

For example, if your target interface is `HD Audio Controller Analog Stereo`, consider the following output: 
    
    $ wpctl status
    
    PipeWire 'pipewire-0' [0.3.56, user@hostname, cookie:1163266174]
    
    Audio
     ├─ Devices:
     │      42. HD Audio Controller                 [alsa]
     │     105. USB PnP Audio Device                [alsa]
     │
     ├─ Sinks:
     │  *   **48. HD Audio Controller Analog Stereo**   [vol: 0.50]
     │
     ├─ ...
     │
     ├─ Sources:
     │  *  101. USB PnP Audio Device Mono           [vol: 0.74]
     │
     └─ ...

the interface `_ID_` is `48`. 

Then use the inspect command to view the object's detail and list all properties in that object: 
    
    $ wpctl inspect 48
    
    id 48, type PipeWire:Interface:Node
        ...
        device.api = "alsa"
        device.class = "sound"
      * device.id = "42"
        device.profile.description = "Analog Stereo"
        device.profile.name = "analog-stereo"
        ...
      * factory.id = "18"
        factory.mode = "merge"
        factory.name = "api.alsa.pcm.sink"
        ...
      * media.class = "Audio/Sink"
      * node.description = "HD Audio Controller Analog Stereo"
      * node.name = "alsa_output.pci-0000_08_00.4.analog-stereo"
      * node.nick = "ALC1220 Analog"
        ...
      * object.path = "alsa:pcm:1:front:1:playback"
      * object.serial = "49"
        ...

Choose the `device.name` or `node.name` property to use with the `matches` rules in the configuration. 

Avoid using `device.id`; it is dynamic and changes often. 

Multiple properties in `matches` rules are possible; see the `alsa_monitor.rules` section in the [documentation for the WirePlumber ALSA configuration](<https://web.archive.org/web/20231226224659/https://pipewire.pages.freedesktop.org/wireplumber/configuration/alsa.html#modifying-the-default-configuration>). 

**注意：**

  * You can determine the `Endpoint` class of this object from the `media.class` property.
  * For ALSA, `node` objects are Sinks or Sources / `device` objects correspond to the card.
  * Since v0.4.9, ALSA nodes use the PCM name to populate `node.nick`, which is useful at least on HDA cards using UCM, where all outputs (analog, HDMI, etc.) are exposed as `Node` on a single profile.

**提示：**

  * The command `pw-top` shows the PipeWire `Device` and `Node` currently in use.
  * Similar inspection command from PipeWire is `pw-cli info _ID_`.

###  Changing a device/node property

To change a device or node property, such as its description or nick, you must create an [SPA-JSON](<https://pipewire.pages.freedesktop.org/wireplumber/daemon/configuration/conf_file.html#the-spa-json-format>) file and add it into `/etc/wireplumber/` or `~/.config/wireplumber/` under the proper path and name. 

For instance, to change the description of an ALSA node, you would create a file such as: 
    
    /etc/wireplumber/wireplumber.conf.d/device-rename.conf (or ~/.config/wireplumber/wireplumber.conf.d/device-rename.conf)
    
    monitor.alsa.rules = [
      {
        matches = [
          {
            node.name = "alsa_output.pci-0000_00_1f.3.output_analog-stereo"
          }
        ]
        actions = {
          update-props = {
            node.description = "Laptop"
          }
        }
      }
    ]

If instead you wish to change something on a Bluetooth node or device, you could create a file such as: 
    
    /etc/wireplumber/wireplumber.conf.d/bluez-rename.conf (or ~/.config/wireplumber/wireplumber.conf.d/bluez-rename.conf)
    
    monitor.bluez.rules = [
      {
        matches = [
          {
            node.name = "bluez_output.02_11_45_A0_B3_27.a2dp-sink"
          }
        ]
        actions = {
          update-props = {
            node.nick = "Headphones"
          }
        }
      }
    ]

The properties that you can change as well as the matching rules to select devices or nodes are documented at [ALSA configuration](<https://pipewire.pages.freedesktop.org/wireplumber/daemon/configuration/alsa.html>) and [Bluetooth configuration](<https://pipewire.pages.freedesktop.org/wireplumber/daemon/configuration/bluetooth.html>). 

###  Disable a device/node

Since WirePlumber v0.4.7, users could now disable any devices or nodes by property `device.disabled` or `node.disabled`: 
    
    /etc/wireplumber/wireplumber.conf.d/alsa-disable.conf (or ~/.config/wireplumber/wireplumber.conf.d/alsa-disable.conf)
    
    monitor.alsa.rules = [
      {
        matches = [
          {
            device.name = "alsa_card.pci-0000_08_00.4"
          }
        ]
        actions = {
          update-props = {
             device.disabled = true
          }
        }
      }
    ]

For the name of `alsa_card.*` in your system, see [#Obtain interface name for rules matching](<#Obtain_interface_name_for_rules_matching>). 

**注意：** A common use case, for example, is disabling NVIDIA's HDMI audio output.

### Setting node priority

To change which sink or source is automatically selected, you need to set its `priority.driver` and `priority.session` values: 
    
    /etc/wireplumber/wireplumber.conf.d/set-priorities.conf
    
    monitor.alsa.rules = [
      {
        matches = [
          {
            node.name = "alsa_output.usb-Generic_USB_Audio-00.HiFi__Speaker__sink"
          }
        ]
        actions = {
          update-props = {
            priority.driver = 100
            priority.session = 100
          }
        }
      }
    ]

This example sets the priority of the speaker output sink of the on-board audio on the Asus B650E-F motherboard to 100, lowered from the original value of 1000. Consequently, the other output sinks, such as the S/PDIF output of the onboard audio device or the plugged in headphones, will be selected by default due to their higher priorities, instead of the analog speaker output. 

### Simultaneous output to multiple sinks on the same sound card

See [PipeWire#Simultaneous output to multiple sinks on the same sound card](<../zh-cn/PipeWire.html#Simultaneous_output_to_multiple_sinks_on_the_same_sound_card> "PipeWire"). 

### Simultaneous output to transient devices

You may wish to output sound to onboard and external devices simultaneously - even when the external devices are not always plugged in. To accomplish this we create a virtual node that will always be present, regardless of what hardware is plugged in. We then link the transient hardware (in this example USB headphones) to the virtual node whenever they are plugged in. 

First, create a script to run during login; this is usually easiest to do via your window manager's Startup function. 
    
    /usr/local/sbin/create-virtual-sink.sh
    
    #!/bin/bash
    
    # Create a new sink called Simultaneous Output
    pw-cli create-node adapter '{ factory.name=support.null-audio-sink node.name="Simultaneous Output" node.description="Simultaneous Output" media.class=Audio/Sink object.linger=true audio.position=[FL FR] }'
    
    # Connect the normal permanent sound card output to the new sink
    pw-link "Simultaneous Output:monitor_FL" alsa_output.pci-0000_05_04.0.analog-stereo:playback_FL
    pw-link "Simultaneous Output:monitor_FR" alsa_output.pci-0000_05_04.0.analog-stereo:playback_FR
    
    # Switch the default output to the new virtual sink
    wpctl set-default `wpctl status | grep "\. Simultaneous Output" | egrep '^ │( )*[0-9]*' -o | cut -c6-55 | egrep -o '[0-9]*'`

In the above example, initially the only output device is our 'normal' on-board soundcard (alsa_output.pci-0000_05_04.0.analog-stereo). You can find the designator for your card by running `wpctl status` and `wpctl inspect`. 

Run the following script when your USB headphones are inserted in order to link them to the virtual sink: 
    
    link-virtual-sink-headphones.sh
    
    #!/bin/bash
    # link the virtual sync to your headphones should run when detected by UDEV
    
    # wait a second for the drivers to load
    sleep 1s
    
    # link the headphones to your virtual sink
    sudo -u user1 env XDG_RUNTIME_DIR=/run/user/1000 pw-link "Simultaneous Output:monitor_FL" alsa_output.usb-Kingston_HyperX_Cloud_Flight_S_000000000001-00.analog-stereo:playback_FL
    sudo -u user1 env XDG_RUNTIME_DIR=/run/user/1000 pw-link "Simultaneous Output:monitor_FR" alsa_output.usb-Kingston_HyperX_Cloud_Flight_S_000000000001-00.analog-stereo:playback_FR
    
    # finish and return the code for success
    exit 0

Ideally you would run this script automatically when your headphones are inserted. The instructions on the [udev](<../zh-cn/Udev.html> "Udev") page describe how you would create a custom rule for that. (Although note that you cannot run this script directly - because udev will not load drivers until _after_ any specified script has run. So you will have to have an intermediate script with some nohup trickery or something like that). You will also need to modify the above script so that the XDG_RUNTIME_DIR matches your user id number and **user1** will need to be replaced with your username. 

You can add any arbitrary number of devices to this virtual sink in the same manner. 

If you are having trouble keeping track what devices are connected where, the [qpwgraph](<https://archlinux.org/packages/?name=qpwgraph>)包 tool is excellent for getting a visual representation of which devices are connected to each other. 

## Tips and tricks

### Delete corrupt settings

If the settings of WirePlumber are corrupted it is possible to delete all user settings: 
    
    $ systemctl --user stop wireplumber.service
    $ rm -r ~/.local/state/wireplumber # deletes settings
    $ systemctl --user start wireplumber.service
    
###  键盘控制音量

See [Keyboard shortcuts#Xorg](<../zh-cn/Keyboard_shortcuts.html#Xorg> "Keyboard shortcuts") to bind the following commands to your volume keys: `XF86AudioRaiseVolume`, `XF86AudioLowerVolume`, `XF86AudioMute` and `XF86AudioMicMute`. 

To raise the volume, with a limit of 150%: 
    
    $ wpctl set-volume -l 1.5 @DEFAULT_AUDIO_SINK@ 5%+
    
To lower the volume: 
    
    $ wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-
    
To mute/unmute the volume: 
    
    $ wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle
    
To mute/unmute the microphone: 
    
    $ wpctl set-mute @DEFAULT_AUDIO_SOURCE@ toggle
    
**提示：** To use sinks or sources other than the default ones, run `wpctl status` to list all available sinks, and use sink or source numbers in place of `@DEFAULT_AUDIO_SINK@` or `_SOURCE@`.

### Show volume level

To get the volume level and mute status of the default sink: 
    
    $ wpctl get-volume @DEFAULT_AUDIO_SINK@
    
    Volume: 0.45

**注意：** The mute status is only visible when the sink is muted.

### Disable Bluetooth profile auto-switching

See [PipeWire#Automatic profile selection](<../zh-cn/PipeWire.html#Automatic_profile_selection> "PipeWire"). 

###  Keep Bluetooth running after logout / Headless Bluetooth

**注意：** You also need to enable [lingering](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html#Automatic_start-up_of_systemd_user_instances> "Systemd/User") for the user running [PipeWire](<../zh-cn/PipeWire.html> "PipeWire")/Wireplumber.

Since 0.4.8 the requirement to `support.logind` has to be disabled for the bluez seat-monitoring. 
    
    ~/.config/wireplumber/wireplumber.conf.d/disable-logind.conf
    
    wireplumber.profiles = {
      main = {
        monitor.bluez.seat-monitoring = disabled
      }
    }

### Disable audio stack integration

If you do not want [PipeWire](<../zh-cn/PipeWire.html> "PipeWire")/Wireplumber to take over control of your audio devices because you are opting for a different audio solution (e.g. [PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio")/[JACK](</wzh/index.php?title=JACK&action=edit&redlink=1> "JACK（页面不存在）")/[ALSA](<../zh-cn/ALSA.html> "ALSA")) but still want it to be available for screen sharing/video purposes you can make use of the `wireplumber@.service` [template unit](<../zh-cn/Systemd.html#Using_units> "Systemd") to enable a different set of default profiles. Wireplumber ships with a profile configuration that enables only the video parts and disables audio integration (including Bluetooth audio) by enabling the `video-only` template [user unit](<../zh-cn/User_unit.html> "User unit"). 

[Disable](</wzh/index.php?title=Disable&action=edit&redlink=1> "Disable（页面不存在）") `wireplumber.service` [user unit](<../zh-cn/User_unit.html> "User unit") and [enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") `wireplumber@video-only.service` user unit. 

### Adjust volume for applications not currently playing audio

Some applications (e.g. launchers) play sound too briefly to adjust their volume using GUI mixers. WirePlumber stores per-application and per-node volume and mute states in a text file at `$HOME/.local/state/wireplumber/stream-properties`. This file can be edited manually to change these settings. Ensure WirePlumber is _not_ running while editing, or it may overwrite the changes. 

## Troubleshooting

Since WirePlumber only exists to manage PipeWire sessions, WirePlumber-related fixes may be found in [PipeWire#Troubleshooting](<../zh-cn/PipeWire.html#Troubleshooting> "PipeWire"). 

## See also

  * [Documentation](<https://pipewire.pages.freedesktop.org/wireplumber/>) — Official documentation
  * [WirePlumber, the PipeWire session manager](<https://www.collabora.com/news-and-blog/blog/2020/05/07/wireplumber-the-pipewire-session-manager/>) — Blog post by George Kiagiadakis (Collabora) from May 2020, detailing how WirePlumber works
