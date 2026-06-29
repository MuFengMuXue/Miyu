**Question 1**. When I try to [install from source](https://github.com/wwmm/easyeffects/wiki/Installation-from-Source) I get the following error: `wrong parameters to Project(), minimum project name and one language is required`. How do I solve this?

**Answer:** Your version of [Meson](http://mesonbuild.com/index.html) is too old. Try to install the latest one from the [Python Package Index](https://pypi.python.org/pypi/meson/). See the [official instructions for getting meson](http://mesonbuild.com/Getting-meson.html) for more information.

---

**Question 2**. System dark mode setting doesn't work.

**Answer:** 

EasyEffects uses the Color Scheme portal to automatically follow your system's dark mode preference.

##### On KDE Plasma 5.24 or later:

Go to System Settings and set light or dark theme which EasyEffects will follow. 

##### On GNOME 42 or later:

You can set light or dark within GNOME Settings which EasyEffects will follow. 

##### On elementary OS 6.1 or later:

Set dark mode in elementary settings.

If your desktop does not yet have support, you can temporarily use the dark mode toggle in EasyEffects Preferences. There may be a 3 option switch in the future (follow system preference, force light, and force dark).

---

**Question 3**. I can not enable effects for applications when using Deepin.

**Answer:** Try to disable audio from dconf (com.deepin.dde.daemon) and restart Deepin. See [#240](https://github.com/wwmm/easyeffects/issues/240)

---

**Question 4** - EasyEffects is available in my language, but I see it in English. Where do I can switch language?

**Answer:** You are probably using EasyEffects under Plasma 5 desktop environment. Sometimes Plasma makes a little mess with locale settings. Just delete `~/.config/plasma-locale-settings.sh` and restart the session.

---

**Question 5** - How to disable EasyEffects config when using headphones?

**Answer:** One solution for this is to create a preset where all plugins are disabled and create a preset autoloading profile that loads this preset when the headphone is plugged. 

---

**Question 6** - Input processing does not apply to Firefox - how to enable it?

**Answer:** See [this](https://github.com/wwmm/easyeffects/issues/957#issuecomment-830640221) comment. When Firefox asks which input device to use, choose "EasyEffects Source". Don't check "Remember this device", otherwise, the next time something uses your microphone, it'll use the default non-processed input, rather than EasyEffects Source.

---

**Question 7** - No sound or low sound in EasyEffects after loading a PulseEffects preset?

**Answer:** PulseEffects presets are not compatible with EasyEffects. IF you tried that without converting the preset to new format as explained at in [Community Presets](https://github.com/wwmm/easyeffects/wiki/Community-Presets#converting-pulseeffects-presets-to-easyeffects-presets) reset EasyEffects so that the bad configuration can be undone.

---

**Question 8** - Why do the start at login and shutdown on window close switches not work?

**Answer:** The Flatpak package uses the background portal to ask the system for background/autostart access. Unfortunately, not all distros ship working support for the background portal out of the box.

In that case, you can manually add an autostart file [as described here](https://github.com/flathub/com.github.wwmm.easyeffects/issues/3#issuecomment-908632842).

In case you accidentally denied background access to EasyEffects, run `flatpak permission-reset com.github.wwmm.easyeffects` to let EasyEffects ask again for the background portal.

---

**Question 9** - Can I set up a default profile for Autoloading with new/unknown devices?

**Answer:** This is currently not supported. See [1359](https://github.com/wwmm/easyeffects/issues/1359) for a discussion of this feature.

---

**Question 10** - Why is the Deep Noise Remover effect showing as not available/not installed for me on Fedora?

**Answer:** The LADSPA version of DeepFilterNet's shared library, `libdeep_filter_ladspa.so`, is not available via the official Fedora RPM or Flatpak repositories. 

If you're using the Flatpak version of EasyEffects, enabling Flathub as a repository and reinstalling it via Flathub should fix the issue.

If you've installed EasyEffects via the official Fedora RPM repository, you can manually install the shared library: 

1. Download the DeepFilterNet's LADSPA file from its repository: https://github.com/Rikorose/DeepFilterNet/releases/download/v0.5.6/libdeep_filter_ladspa-0.5.6-x86_64-unknown-linux-gnu.so
2. Copy the file `libdeep_filter_ladspa-0.5.6-x86_64-unknown-linux-gnu.so` to the path `/usr/lib64/ladspa/libdeep_filter_ladspa.so`

After restarting EasyEffects, the effect should then be available. 

See issue [!3469](https://github.com/wwmm/easyeffects/issues/3469), specifically [balcala's comment](https://github.com/wwmm/easyeffects/issues/3469#issuecomment-2566185201) which contains more information.

---

**Question 11** - Why does EasyEffects randomly close for me?

**Answer:** This can be caused by a variety of reasons many of which can be hard to pinpoint. One way to get around these issues is to [let systemd manage EasyEffects.](https://github.com/wwmm/easyeffects/discussions/4866)