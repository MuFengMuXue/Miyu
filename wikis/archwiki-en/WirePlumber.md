# WirePlumber

WirePlumber is a powerful session and policy manager for PipeWire. Based on a modular design, with Lua plugins that implement the actual management functionality, it is highly configurable and extendable.

## Installation
Install the  package. Any conflicting PipeWire Session Managers will be uninstalled.

WirePlumber uses systemd user units to manage the server.

## Configuration
## Configuration file layout
WirePlumber's configuration comprises global PipeWire-flavored JSON objects such as  and  that are modified to change its behavior. The configuration files are read from  (user configuration),  (global configuration), and then  (stock configuration).

WirePlumber starts by reading the main configuration file. This is a JSON-like file that sets up the PipeWire context, SPA plugins, modules, and components.

The single-instance configuration file at  is the default configuration, which includes the functionality of all the other configurations within one process. See the documentation for the ALSA objects, "access" objects and Bluetooth objects.

## Modifying the configuration
The recommended way to configure WirePlumber is to add an SPA-JSON file to the appropriate  directory within  or .

User configuration files have a higher priority than system files. Configuration files with the same name but in a lower priority location will be ignored. Within each configuration directory, the individual files are opened in alphanumerical order. See the documentation for details.

## Obtain interface name for rules matching
In the configuration, you need to specify  rules with a property from an object of the interface you want to configure.

Use the command  to show all objects managed by WirePlumber. Find the  assigned to the target interface. Then use command  to get a needed property.

For example, if your target interface is , consider the following output:

the interface  is .

Then use the inspect command to view the object's detail and list all properties in that object:

Choose a property that is unique and stable for use in  rules. The  or  properties are recommended.

Avoid using , as it is dynamic and may change between sessions.

Regular expressions and multiple property  are supported; see the  section in the official documentation for details.

## Changing a device/node property
To change a device or node property, such as its description or nick, you must create an SPA-JSON file and add it into  or  under the proper path and name.

For instance, to change the description of an ALSA node, you would create a file such as:

{{hc|/etc/wireplumber/wireplumber.conf.d/device-rename.conf (or ~/.config/wireplumber/wireplumber.conf.d/device-rename.conf)|output=
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

}}

If instead you wish to change something on a Bluetooth node or device, you could create a file such as:

{{hc|/etc/wireplumber/wireplumber.conf.d/bluez-rename.conf (or ~/.config/wireplumber/wireplumber.conf.d/bluez-rename.conf)|output=
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

}}

The properties that you can change as well as the matching rules to select devices or nodes are documented at ALSA configuration and Bluetooth configuration.

## Disable a device/node
Any devices or nodes can be disabled by setting the property  for devices or  for nodes:

{{hc|/etc/wireplumber/wireplumber.conf.d/alsa-disable.conf (or ~/.config/wireplumber/wireplumber.conf.d/alsa-disable.conf)|output=
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
}}

Find a unique identifier for your device or node as seen in #Obtain interface name for rules matching.
In this example, matching is done based on the , but it can also be done for any other identifying property, such as .

A common use case, for example, is disabling a graphics card's HDMI audio output.
This approach can also be used to disable audio over HDMI for specific displays only, by matching for specific nodes using something like , as this can change depending on the plugged-in device.

## Setting node priority
To change which sink or source is automatically selected, you need to set its  and  values:

{{hc|/etc/wireplumber/wireplumber.conf.d/set-priorities.conf|output=
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
}}

This example sets the priority of the speaker output sink of the on-board audio on the Asus B650E-F motherboard to 100, lowered from the original value of 1000. Consequently, the other output sinks, such as the S/PDIF output of the onboard audio device or the plugged in headphones, will be selected by default due to their higher priorities, instead of the analog speaker output.

## Simultaneous output to multiple sinks on the same sound card
See PipeWire#Simultaneous output to multiple sinks on the same sound card.

## Simultaneous output to transient devices
You may wish to output sound to onboard and external devices simultaneously - even when the external devices are not always plugged in.
To accomplish this we create a virtual node that will always be present, regardless of what hardware is plugged in. We then link the transient hardware (in this example USB headphones) to the virtual node whenever they are plugged in.

First, create a script to run during login; this is usually easiest to do via your window manager's Startup function.

{{hc|head=/usr/local/sbin/create-virtual-sink.sh|output=
#!/bin/bash

# Create a new sink called Simultaneous Output
pw-cli create-node adapter '{ factory.name=support.null-audio-sink node.name="Simultaneous Output" node.description="Simultaneous Output" media.class=Audio/Sink object.linger=true audio.position=FR }'

# Connect the normal permanent sound card output to the new sink
pw-link "Simultaneous Output:monitor_FL" alsa_output.pci-0000_05_04.0.analog-stereo:playback_FL
pw-link "Simultaneous Output:monitor_FR" alsa_output.pci-0000_05_04.0.analog-stereo:playback_FR

# Switch the default output to the new virtual sink
wpctl set-default `wpctl status  grep "\. Simultaneous Output"  egrep '^ │( )*-o  cut -c6-55  egrep -o '[0-9*'`
}}

In the above example, initially the only output device is our 'normal' on-board soundcard (alsa_output.pci-0000_05_04.0.analog-stereo). You can find the designator for your card by running  and .

Run the following script when your USB headphones are inserted in order to link them to the virtual sink:

Ideally you would run this script automatically when your headphones are inserted. The instructions on the udev page describe how you would create a custom rule for that. (Although note that you cannot run this script directly - because udev will not load drivers until after any specified script has run. So you will have to have an intermediate script with some nohup trickery or something like that).
You will also need to modify the above script so that the XDG_RUNTIME_DIR matches your user id number and user1 will need to be replaced with your username.

You can add any arbitrary number of devices to this virtual sink in the same manner.

If you are having trouble keeping track what devices are connected where, the  tool is excellent for getting a visual representation of which devices are connected to each other.

## Tips and tricks
## Delete corrupt settings
If the settings of WirePlumber are corrupted it is possible to delete all user settings. Stop the  user unit, delete the settings with:

 $ rm -r ~/.local/state/wireplumber

Then, you can start the  user unit back.

## Keyboard volume control
See Keyboard shortcuts#Xorg to bind the following commands to your volume keys: , ,  and .

To raise the volume, with a limit of 150%:

 $ wpctl set-volume -l 1.5 @DEFAULT_AUDIO_SINK@ 5%+

To lower the volume:

 $ wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-

To mute/unmute the volume:

 $ wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle

To mute/unmute the microphone:

 $ wpctl set-mute @DEFAULT_AUDIO_SOURCE@ toggle

## Show volume level
To get the volume level and mute status of the default sink:

## Disable Bluetooth profile auto-switching
See PipeWire#Automatic profile selection.

## Keep Bluetooth running after logout / Headless Bluetooth
Since 0.4.8 the requirement to  has to be disabled for the bluez seat-monitoring.

{{hc|~/.config/wireplumber/wireplumber.conf.d/disable-logind.conf|2=
wireplumber.profiles = {
  main = {
    monitor.bluez.seat-monitoring = disabled
  }
}
}}

## Disable audio stack integration
If you do not want PipeWire/Wireplumber to take over control of your audio devices because you are opting for a different audio solution (e.g. PulseAudio/JACK/ALSA) but still want it to be available for screen sharing/video purposes you can make use of the  template unit to enable a different set of default profiles. Wireplumber ships with a profile configuration that enables only the video parts and disables audio integration (including Bluetooth audio) by enabling the  template user unit.

Disable  user unit and enable  user unit.

## Adjust volume for applications not currently playing audio
Some applications (e.g. launchers) play sound too briefly to adjust their volume using GUI mixers. WirePlumber stores per-application and per-node volume and mute states in a text file at . This file can be edited manually to change these settings. Ensure WirePlumber is not running while editing, or it may overwrite the changes.

## Troubleshooting
Since WirePlumber only exists to manage PipeWire sessions, WirePlumber-related fixes may be found in PipeWire#Troubleshooting.
