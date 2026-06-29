**[_Originally posted by c3r1c3 on the official OBS Forums_](https://obsproject.com/forum/resources/post-production-tools-you-can-use.234/)**

So you've just finished your Ultra-Mega-Marathon Streaming session... but now you need to cut out those not-so-funny-parts, the false starts, all those flubs, add some lower thirds, clean up/normalize your audio levels, etc.

In other words you want to take it up a notch. So you think "Hey I'm gonna edit/clean up/layer on some nice visuals for my videos", but you don't want to pay $800 for Final Cut Pro+Logic+Motion, or $50/month to Adobe to use Audition/Premiere/After Effects.

OBS is free (as in beer and speech) software, so aren't there other tools out there that are that are also free (maybe even open source)?

**Yes!**

And here is a list of them just for you:

1. **Video Editors** are here (as their namesake) mostly to edit videos. Some can also be used as compositors and/or audio post-production work, but their main focus is on helping you take your video and add/remove/layer parts of your video and audio to help create the final file.

    1. **[AVI Demux](http://fixounet.free.fr/avidemux/) _(Mac/Windows/Linux)_**: A simple editor that seems to be able to load almost any format, and provides a simple (but fast and efficient) cuts-only, single-track editor. Good if you want to just remove content from a file quickly and simply.

    2. **[OpenShot (2.1+)](http://www.openshot.org/) _(Mac/Windows/Linux)_**: A multi-format editor with some neat features. Open Source and multi-platform, but unstable (i.e. crashes) a lot. I would recommend using something else until they fix their stability issues.

    3. **[Blender (from the Blender Foundation)](https://www.blender.org/) _(Linux/Mac/Windows)_**: This program started off it's life as a 3D Graphics program, but has expanded in recent years to include decent/basic video editing and compositing tools as well. Also open source.

    4. **[LightWorks (from EditShare)](https://www.lwks.com/) _(Mac/Windows/Linux)_**: A world-class editor available for Linux, OS X and Windows. Free licenses available that lets you edit up to HD (1920x1080) material, and can export up to 720p directly to Youtube, and 1080p to Vimeo. Excellent free training material from the creators that not only teach you the program, but also some of the "Art of Editing."

    5. **[DaVinci Resolve (from Blackmagic Design)](https://www.blackmagicdesign.com/products/davinciresolve/) _(Mac/Windows/Linux)_**: A program that started out as a color-corrector/grading tool, but in the past several releases has gotten a ton of video editing features. If you like world-class color grading, color correction, masking, and decent to excellent video and audio editing, this one might be good for you. (Also now includes Fusion integrated for even faster work/turnaround).

    6. **[KDEnlive](https://kdenlive.org/) _(Linux, MacOS and Windows)_**: I haven't used this editor, but people say good things about it. On Linux check your repos for it (for everyone else grab the installer from their website), install it and give it a whirl.

    7. **[Shotcut](https://www.shotcutapp.com/) _(Windows/Mac/Linux)_**: EBrito recommends checking this one out. Make sure to follow the tutorials on their website.

    8. **[Avid Media Composer First](http://www.avid.com) _(Windows/Mac)_**:  If you want to go pro, then this is it. What Hollywood, the big studios and a lot of independents use. Even though it's free (as in beer) it still has more than enough features to satisfy 99%+ of video editor needs. Loads of video tutorials are available on Youtube as well.

    9. **[XSplit Express Video Editor](https://www.xsplit.com/video-editor) _(Windows)_**: Simple editor for quick cutting/combining recorded clips. Does not require rendering/encoding the entire video when exporting so very useful to create videos for YouTube and other social media where only cutting down or adding a short intro is required. The editor is free but requires signing in via a XSplit or one of various social media networks.

2. **Audio Editors/Digital Audio Workstations (DAW)** are very helpful in getting your audio to a good quality level, so that people won't turn you off the moment they hear you speak. Remember that most people will watch video that sucks in quality, but most people won't listen to bad/too quiet/distorted audio for very long. So help get your audio in shape with these programs:

    1. **[Pro Tools First (from Avid Technologies)](http://apps.avid.com/ProToolsFirst/) _(Mac/Windows)_**: If you like Pro(fessional) Tools with an interface that takes some time to learn (but can take you places), then this is it. Biggest and baddest of the pro-audio software world, for free.

    2. **[Audacity (from Team Audacity)](http://web.audacityteam.org/) _(Linux/Mac/Windows)_**: Open source, and only actual editor in the list (all the other listed software are DAWs). Used by many, with many tutorials online available to help you get past the learning curve of this program.

    3. **[Ardour](https://ardour.org/) _(Linux/Mac/Windows)_**: Open source, and professional, this tool falls in the same league as Pro-Tools and Reaper. Good if you like a professional DAW interface and the learning curve that goes with it. (Can also be used as a JACK source for pre-processing audio to feed to OBS on Linux and MacOS). Version 5 now includes an official Windows release.

    4. **[LMMS](https://lmms.io/) _(Linux/Mac/Windows)_**: Open source, free and (IMO) not bad at all. The interface seems to be more geared towards song writing/looping then straight-up editing, but if none of the above catch your fancy, you might want to check this one out.

    5. **Some honorable mentions**: CuBase LE 9 (for Mac and Windows) and Cakewalk/SONAR by Bandlab (Windows only?). Free (as in beer), but not open source. Professional-class tools with the interfaces (and the learning curve) to go along with them.

3. **Compositors/Motion Graphics.** Ever seen a fancy opening to a stream or video? Ever seen overlays (static or moving) that grab your attention? Ever wondered "How'd they do that?" Well compositing software (e.g. After Effects) is usually the tool involved, and below are some (very) powerful programs:

    1. **[Fusion (from Blackmagic Design)](https://www.blackmagicdesign.com/products/fusion/) _(Windows/Mac/Linux)_**: Hollywood level effects, but with a bit of a learning curve (no more than After Effects though). Once you learn it you'll be blowing by anything done in After Effects. Also has powerful color correction, masking and keying tools. Takes advantage of your GPUs for faster rendering. (Fusion is now integrated with Resolve, so you might be able to take advantage of that integration by using Resolve outright).

    2. **[Blender (from the Blender Foundation)](https://www.blender.org/) _(Linux/Mac/Windows)_**: Wait, Blender again? Well it's a versatile program that in recent years has added compositing tools to it's arsenal. Also open source.
Linux/Mac/Windows 
    3. **[Natron](https://natrongithub.github.io/) _(Linux/Mac/Windows)_**: A Multi-platform compositor. On the surface appears to be similar to Blackmagic Designs' Fusion. Open source as well.

4. **3D Graphics.** 3D is hard, but the stuff you can create with even just a little bit of skill can truly separate your content from everyone else. Even if just used as elements that you composit together, 3D is a very powerful tool in your post-production toolkit.

    1. **[Blender (from the Blender Foundation)](https://www.blender.org/) _(Linux/Mac/Windows)_**: Again? Well this time we're actually addressing what Blender does best and has been doing the longest, 3D.

Remember that no matter what the software, there is a learning curve involved. So use Google to find tutorials, hit the software creator's forums and most importantly be patient with yourself. It can take some time, but you'll be able to put out higher quality work and help differentiate yourself from the masses of streaming/Let's Players/videos out there with just a little bit of Post-Production Tender-Loving-Care.