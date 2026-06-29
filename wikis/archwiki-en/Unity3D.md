# Unity3D

From https://unity.com:

:The leading platform for creating interactive, real-time content
:Build 2D, 3D and VR games and apps at speed. From artist tools to LiveOps – everything you need to bring your vision to life today.

Not to be confused with Canonical's Unity (which is now maintained by the UBPorts Foundation and renamed to Lomiri).

## Installation
Unity has made available a program called Unity Hub that is designed to streamline your workflow by providing a centralized location where you can manage your Unity Projects and simplifies how you find, download, and manage your Unity Editor installs. The application comes available as a Deb or RPM package. To install the Unity Hub, simply install the  package.

To install the beta version, simply install the  package.

## Android Remote
Unity Remote is an Android app to help test input for Android devices. It achieves this by sending a compressed screenshot to the device each frame.

## Prepare computer
## Install packages
Install the  package, which will ensure you have correct udev rules for your device.

Install the  package.

## Configure the Editor
Open the editor, navigate to Edit > Preferences and set the correct paths to the Android SDK and the JDK.

Then navigate to Edit > Project Settings > Editor and set  to .

For more help see the Unity documentation.

## Prepare Android
Install Unity Remote 5 from the Play Store. Alternatively you can download and build it yourself from the Asset Store.

It is also recommended to set your Android device to PTP mode.

For more help see the Unity documentation.

## Test
If you have Unity opened, close it.

Connect the phone to the computer and launch Unity Remote.

Open the Editor and press play. You should now see your game transmitted to your Android device.

If it does not work or you have questions, see the Unity Documentation.

## Visual Studio Code
For those using the Visual Studio Code as their script editor, there are a few additional steps you need to do to get it running without displaying errors similar to:

 The reference assemblies for framework ".NETFramework,Version=v3.5" were not found

 [warn: OmniSharp.MSBuild.ProjectFile.ProjectFileInfo Unable to create directory "/Debug/". Access to the path "/Debug/" is denied.
 OmniSharp.MSBuild.ProjectFile.ProjectFileInfo Could not write lines to file "/Debug/Assembly-CSharp.csproj.CoreCompileInputs.cache". Could not find a part of the path "/Debug/Assembly-CSharp.csproj.CoreCompileInputs.cache".

To eliminate these errors you need to install the following packages: , , , , and . You also need to install  if you want to use the C# Dev Kit or Unity extension. Finally remember to install the C# extension from the VS Code Marketplace by pressing Ctrl-P and entering:

 ext install ms-dotnettools.csharp

To use the system-provided .NET SDK, you will also have to disable the following option:

 "omnisharp.useModernNet": false

After this configuration change, you may need to restart Visual Studio Code.

## Troubleshooting
Crash logs are available at

## Unity crashes on first launch before/while signing in
This is a rare bug where Unity's configuration gets created wrongly. You can try resetting it by:

{{bc|$ rm -rf ~/.config/unity3d/{*.prefs,*.log,Preferences} }}

## Unity crashes when trying to load project
Users have [https://forum.unity.com/threads/unity-on-arch-manjaro-linux.350315/page-3#post-2271637 reported that unsetting  prevents the crash.

## Unity crashes if ~/.config/user-dirs.dirs is missing
See how to generate the xdg files here: XDG user directories

## Unity crashes with DllNotFoundException
In unity 2019 and newer, if you see a message along the lines of:

, try installing .

## Unity fails to build project to webGL platform
IL2CPP needs libtinfo-5.so library for the building process and ncurses5 provides it. So make sure to install  if you want to build to webGL.

## Minor stuttering while playtesting (NVIDIA)
Vsync does not seem to work correctly with NVIDIA graphics cards / drivers. Solution: In  go to "OpenGL Settings" and turn off "Sync to VBlank".

The behaviour occured/noticed when used "transform.Rotate" in combination with "Input.GetKey".

## Error: Multiple Unity instances cannot open the same project
Unity probably did not shutdown properly, in this case you should navigate to your project folder and delete Temp folder.

## Android Remote not working / Running Android build fails with "Unable to forward network traffic to device"
Try this workaround :

# Close Unity.
# Shutdown adb daemon with
# Plug in the android device.
# Find your device ID with
# Use  replacing  with the correct one.

That's it now you can open unity and test it, an error "socket bind failed" will appear that you can safely ignore.

## No window opens: Desktop is 0 x 0 @ 0 Hz
If using Wayland, try using the Xorg backend of SDL by setting the environment variable .

## Brotli invalid ELF header
If you see an error similar to:

 Failed running python2 "$EDITOR_PATH/Editor/Data/PlaybackEngines/WebGLSupport/BuildTools/Brotli/python/bro.py"

Either replace the Brotli Mac OS X egg with a Linux egg at , or switch from Brotli to gzip in File > Build Settings > Player Settings > Player > Publishing Settings > Compression Format.

## Cannot load assets in package manager
If you have proxy/VPN configured, reset it. Resetting your firewall may also work (e.g., iptables#Resetting rules for iptables).

## Menus don't react to clicks after entering play mode
First, install .

Then, run
 downgrade glib2
and select version "2.72.1".

## UI isn't redrawn after opening menus
This is a known bug that, as of May 2025, is marked as "Won't Fix" on Unity's issue tracker. The workaround is to enable display compositing. See Xorg#Composite for more info.

## Unity fails to save preferences
Unity Hub or the editor fails to create the folder where it's storing preferences.

If this happens create the  folder manually in .
Full path should be:

If done successfully, the editor will create a prefs file in it.

## Dropdown and context menus open very slowly on GNOME
On GNOME, Unity interacts badly with , causing context and dropdown menus to open very slowly (more than half a seconds delay on particularly large menus).

The solution is to install  (replacing ).

If you run in to issues with SVG rendering after this, especially if you also choose to uninstall , you can also install .

## Cannot validate Editor while installing in Hong Kong
Since Unity forces users in Hong Kong to redirect to the Mainland China version of the Unity Engine, which does not contain the version installed via , it is strongly recommended to use a VPN connected to the United States, to circumvent the redirection.
