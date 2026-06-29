If you are a casual user simply searching for some bass boost, or you don't want to dive in the thousand of thousand options that EasyEffects (previously known as PulseEffects) offers, you'll be happy knowing that some users have created some presets, and maybe you could find the one you are searching for.

Note: there are some PulseEffects-specific presets listed [here](https://github.com/wwmm/easyeffects/wiki/PulseEffects-Wiki#community-presets).

Below is a list of repositories containing some presets (for output - speakers):
- https://github.com/Bundy01/EasyEffects-Presets (Bose, Music, Sony and Video)
- https://github.com/p-chan5/EasyPulse (HQ Easy Effects presets for headphones)
- https://github.com/Digitalone1/EasyEffects-Presets (Loudness Equalizer)
- https://github.com/JackHack96/EasyEffects-Presets
- https://github.com/EvoXCX/EasyEffect-Preset (OpenEQ Equalizer)
- https://github.com/Rabcor/Heavy-Bass-EE
- https://github.com/servimo/AAAAAAAaaaaa (for earbuds)
- https://github.com/FaridZelli/EasyEffects-Pavilionx360 (for HP Pavilion x360 built-in speakers)
- https://github.com/sebastian-de/easyeffects-thinkpad-unsuck (for Lenovo Thinkpad P14s Gen 2 AMD built-in speakers)
- https://github.com/BayouGuru67/Linux_Audio (A variety of Media/HTPC-oriented output effects presets primarily designed for larger speaker systems as well as other real-time HTPC audio processing options and information)
- https://gitlab.com/lukasfink1/easyeffects-presets (for Lenovo ThinkPad X1 Yoga Gen2 built-in speakers)
- https://gist.github.com/Mlocik97/4e50977f27404fa62bde2d5f44e24581 (for Logitech Z333/337 speakers)
- https://github.com/droidwayin/GentleDynamics (GentleDynamics preset shapes audio and deliver a dynamically balanced, detail-rich sound that evolves in real time with the incoming audio signal. Two presets for music and one for movie dialogue leveling.)

Below is a list containing some presets (for input - microphone):
- [jtrv/Masc NPR Voice + Noise Reduction.json](https://gist.github.com/jtrv/47542c8be6345951802eebcf9dc7da31) (NPR-like tuning for masculine voices + noise reduction. Can be modified for feminine voices.)

# Installation
You can use the `Import Preset` button that is beside the `Add` preset button. But you can also do the process manually. Just copy the `.preset` files into the `EasyEffects` directory you can find in the local `config` directory. The location of that directory depends on how you installed the package. If you installed it through Flatpak, you can find it in `~/.var/app/com.github.wwmm.easyeffects/config/easyeffects`, or if you used the PPA for Ubuntu (or the AUR package for Arch) it should be `~/.local/share/easyeffects/output` and `~/.local/share/easyeffects/input` respectively.

# Converting PulseEffects presets to EasyEffects presets
Due to changes in [EasyEffects 6.0.0](https://github.com/wwmm/easyeffects/blob/master/CHANGELOG.md#600) preset structure changed a little. Thanks to AbsurdlySuspicious, there is a bash shell script converter that can
convert all your presets. Just run `bash convert.sh *.json` in directory with presets and it will convert the entire directory. (Note: it requires `jq` and `perl` installed.)

The script is provided in this issue comment: https://github.com/wwmm/easyeffects/issues/1013#issuecomment-880929524.

# Converting Dolby Atmos presets to EasyEffects presets
If your computer ships with Dolby Atmos on Windows, https://github.com/antoinecellerier/speaker-tuning-to-easyeffects is an attempt at automating conversion from the relevant Dolby Atmos DAX3 profiles to Easy Effects. It's not a perfect match but gets you a reasonable starting point.