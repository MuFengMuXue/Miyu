# Blender

Blender is best known as a popular open source 3D modelling program.

## Installation
Install the  package.

## GPU rendering
Blender supports a multitude of hardware offloading options for rendering. After preparing your system according to your hardware (see following paragraphs), you can set these your graphics card as a compute device under Edit > Preferences... > System.

## NVIDIA GPUs
For NVIDIA, Blender supports two GPU rendering backends: CUDA and OptiX. Most modern NVIDIA GPUs are supported. In order to make use of these, you need to install . Afterwards, the rendering backends should be available in the systems options.

## Intel Arc GPUs
If you have a modern Intel Arc GPU, you can make use of Blender's built-in hardware rendering support for those devices. To do so, you need to have the  package installed.

As of this writing, you might have to launch Blender with the an additional environment variable set:

 CYCLES_ONEAPI_ALL_DEVICES=1 blender

If you experience issues with no detected OneAPI devices, the issue may be related to using the Arch Linux blender builds (). Blender's official builds may fix the issue, in this case.

For hardware raytracing support, install .

## HIP on AMD open source drivers
On supported GPUs (GFX9, CDNA, and RDNA; see the official hardware compatibility list for more info),  can be used to get GPU acceleration through HIP in Blender, using Mesa.

To get HIP working in Blender, install  and select your GPU in the Blender's Preferences, same as with proprietary drivers.

## Enable Hardware Ray tracing on supported GPUs
To enable hardware raytracing on Navi 2x (AMD 6xxx series) and upward,  must be installed. The minimum Blender version is 3.5+.

This gives a steady 20% speed boost on Navi 3x compared to software ray tracing.

## Professional rendering plugins
Blender is becoming increasingly well known in the professional industry. As such, there are now alternative rendering methods to EEVEE and Cycles, in the form of plugins. This should serve as a list of the major professional rendering plugins that are released or upcoming for Linux.

## BlendNet
BlendNet is an open source plugin that allows distributing CPU and GPU renders across multiple machines.

BlendNet natively integrates with major cloud providers like AWS, Azure or GCP, and also supports self-hosting your own render farm.

## Cloud integration
# Install the  package
# Enable the BlendNet plugin in Preferences -> Add-ons -> Enable "Render: BlendNet"
# Follow the instructions on the official BlendNet wiki to configure a render farm on AWS, Azure or GCP.

## Self-hosting
The  package provides systemd units and configuration to quickly deploy your own CUDA GPU-accelerated Blendnet render farm.

A BlendNet render farm consists of one Manager instance, which distributes tasks to multiple Agent machines.
The blender Addon connects to the Manager and the Agents to schedule renders.
See the BlendNet wiki for more information on BlendNet architecture.

To start, install  on the Manager, Agent and Addon machines, then follow these instructions.

## Setup: Manager
# Copy  and  to all Agent and Addon machines, to .
# Edit , adding a manager username and password.
# Edit , adding an agent username and password.
# Start/enable the  unit.

## Setup: Agent
# Edit , adding the same agent username and password used in the Manager.
# Start/enable the  unit.

If  is installed,  will automatically enable GPU+CPU acceleration: you can check whether GPU acceleration is in use by checking the agent logs:

 $ journalctl -xefu blendnet-agent.service

## Setup: Addon
# Enable the BlendNet plugin in Preferences -> Add-ons -> Enable "Render: BlendNet".
# Configure the plugin with the Manager/Agent usernames and passwords.
# Specify the CA certificate located in .
# Close Preferences, open the Render tab and switch to the Cycles rendering engine (**NOT** BlendNet!).
# Add all Agents using the  button in the new "BlendNet Render (local)" Cycles panel.
# Follow the BlendNet rendering instructions.

## LuxCoreRender
LuxCoreRender is an open source rendering method that can also make use of OpenCL to render. To make use of it, simply install the () package and then enable the LuxCoreRender addon in the User Preferences box in Blender.

## RenderMan
RenderMan is a Linux compatible proprietary rendering plugin that is free for use with blender under a non-commercial license. See the Renderman page for setting it up with blender.

## Pro-Render
Pro-Render is an open source Blender rendering plugin from AMD that will allow any machine using an OpenCL 1.2 compatible AMD GPU the ability to create realistic GPU renders, allowing for faster work compared to the CPU.

## Blend4Web
Blend4Web is an open source framework for creating and displaying interactive 3D graphics in web browsers. It contains a Blender add-on to create and export 3D scenes directly into the web. A Blend4Web-specific profile can be activated in the add-on settings. When switching to this profile, the Blender interface changes so that it only reveals settings relevant to Blend4Web. See the documentation on how to install Blend4Web SDK.

## Verge3D
Verge3D for Blender is a real-time renderer and a toolkit from the original creators of Blend4Web. It contains Puzzles visual editor to allow creating interactive web applications without coding.

## Troubleshooting
## Blender is slow to select objects
When using onboard Intel graphics, it may take 5-10 seconds to select an object. Change Selection in File > User Preferences > System to OpenGL Occlusion Queries.

## Blender does not show the AMD card as an OpenCL rendering device
Blender only supports the official AMD proprietary drivers for rendering with OpenCL (for now), meaning you will need to install one of the following AMD OpenCL drivers:

* Install AMDGPU PRO
* Install  driver alongside the open source AMDGPU driver

After installation, the AMD GPU should now appear as a selectable device under File > User Preferences > System > Compute Device.

Note: Blender developers decided to switch another API (HIP) and deprecate OpenCL support. This will happen in Blender 3.0 release (4th December 2021). More information.

## Blender crashes on i915
Blender gets unresponsive simply by resizing the startup cube, dmesg shows messages about a GPU hang:

Workaround based on the Upstream Bug and a question on AskUbuntu:

* Start Blender with the environment variable , i.e. by changing the .desktop file's Exec line to
* Increase the preemption timeout to 10,000 milliseconds. To persist this, add a udev rule:

## Interface text
If fonts look small or blurry, their size can be increased (by a point or two) in User Preferences > Themes > Text Style. Selecting a bold font family as Interface Font in User Preferences > Themes > System can also greatly decrease blurriness.

## Python version incompatible with plugin
Blender's releases for Windows and macOS use a bundled Python installation.Arch's  package, on the other hand, uses the system's  which might be newer than elsewhere (see ). Even if Blender itself works fine, 3rd-party plugins may fail to load:

In this case, you can switch to any of:
* , which bundles the expected Python version.
* Pre-compiled versions on https://blender.org/.
* The [https://flathub.org/en/apps/org.blender.Blender/ flatpak.
