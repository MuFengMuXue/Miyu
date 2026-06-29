# Professional audio

This article describes how to configure your system for multitrack recording, mixing and playing back audio as well as using it to synthesize and generate sounds. Those activities are subsumed under the term professional audio (pro audio) and typically require low latency performance.

Most applications do not need as much high-end hardware, compared to video production or gaming. For more information, refer to The Right Computer System for Digital Audio.

## Getting started
Advanced Linux Sound Architecture (ALSA) is part of the Linux kernel and used for drivers and low-level interface on Arch Linux as the default sound system. ALSA should work out of the box with a default Arch Linux installation. If this is not the case, you must solve the problem before going any further.

Have I set up sound properly?

 $ speaker-test

: See ALSA for troubleshooting.

A vanilla Arch Linux kernel is sufficient for low latency operation in most use cases. #Optimizing system configuration will be necessary only if you are experiencing audio drop-outs (also known as glitches) or if you need (or want) to reach ultra-low latency operations.

To finish with optimizations, these ultra low latency operations may require you to set up a #Realtime kernel.

Although some pro audio software can work with ALSA directly, most of the #Applications mentioned later are JACK Audio Connection Kit or JACK clients. Therefore, you will need to install and setup one of the available sound servers which are outlined soon.

## Choosing a sound server
Sound hardware cannot play back sound from more than one application simultaneously. While ALSA can theoretically be configured to mix applications in software this is typically left to a sound server.

As ALSA alone cannot achieve low latencies easily and cannot synchronise multiple audio applications to play on time, starting all at the same time, at the same tempo, etc., and as it can not share audio flux between applications simply by connecting all its clients together, you need not just any sound server, but professional audio class one:

* PipeWire is a replacement of JACK and PulseAudio at the same time for the audio part. It also handles video routing, which is not described in this article.
:
* JACK Audio Connection Kit (JACK) has been developed with all the needs of professional audio and has been in use all over the world for many years and is therefore very stable and mature. Most of professional audio applications are written for the JACK API.

The sound server setup strongly depends on the use case as well as on the workflow and capabilities of some application interaction. JACK was designed to share audio between applications and access an audio device simultaneously by providing the synchronous execution of clients while maintaining constant low latency. Its PipeWire replacement provides a sufficient server for most of the use cases.

This layout illustrates a layer model of the sound server setups to be discussed:

## PipeWire-only
The newer PipeWire framework replaces JACK as well as other sound servers for the sake of simplicity. Thus, it is recommended to first go for a PipeWire-only setup implementing support for JACK clients by installing  and using the vanilla Arch Linux kernel.

For pro audio use, you also have to select the Pro Audio profile installing and using , PulseAudio's mixer.

## PipeWire-as-JACK-Client
PipeWire can also be used as a JACK client by installing . This is explained in PipeWire#Run PipeWire on top of native JACK.

## JACK-only
The principle of versatility allows you to employ JACK and the #Realtime kernel with #Optimizing system configuration to achieve low latencies for advanced use cases known as JACK-only setup. Using JACK as the only sound server requires any software, that is intended for interaction and audio device access, to run as a JACK client.

Unfortunately, popular desktop applications such as Firefox or most games either dropped JACK support or never implemented it. For that reason this setup should be used for a dedicated pro audio system where non-JACK software can be neglected. If you still need to use software that cannot connect to JACK, refer to Professional audio/Examples#Advanced sound server setups after following the setup described here. Before installing and running JACK you should ensure it can access your audio device.

Is PulseAudio or something else grabbing my device?

 $ lsof +c 0 /dev/snd/pcm* /dev/dsp*

or

 $ fuser -fv /dev/snd/pcm* /dev/dsp*

If your audio device is not listed, it may be used by PulseAudio (which was probably installed as dependency of another application). Remove those alongside PulseAudio, if you are not intending to use Professional audio/Examples#PulseAudio+JACK in order to make PulseAudio release your audio device.

As JACK version 1 is planned to be "slowly phased out" does not support Symmetric Multiprocessing (SMP), lacks D-Bus and systemd integration, you would want to use version 2 which is available as the  package. If you are going to use a JACK control GUI or a systemd user service for starting the audio graph, also install .

: More details in JACK Audio Connection Kit#Comparison of JACK implementations

The article on JACK describes a GUI-based and a shell-based example setup as a point of reference for your own scenario. Parameter values of JACK are discussed in detail in the #JACK parameters section and may depend on other system factors covered by the #Optimizing system configuration section below.

## JACK parameters
The aim here is to find the best possible combination of buffer size and periods, given the hardware you have. Frames/Period = 256 is a sane starter. For onboard and USB devices, try Periods/Buffer = 3 before lowering both values. Commonly used values are: 256/3, 256/2, 128/3, 128/2.

Also, the sample rate must match the hardware sample rate. To check what sample and bit rates your device supports:

 $ cat /proc/asound/card0/codec#0

Replace card0 and codec#0 depending on what you have. You will be looking for rates or VRA in Extended ID. A common sample rate across many of today's devices is 48000 Hz. Others common rates include 44100 Hz, 96000 Hz and 192000 Hz.

Almost always, when recording or sequencing with external gear is concerned, realtime is a must. Also, you may like to set maximum priority (at least 10 lower than system limits defined in ; the highest is for the device itself).

Start jack with the options you just found out:

 $ /usr/bin/jackd -R -P89 -dalsa -dhw:0 -r48000 -p128 -n2

, ,  and  can all be used to as GUIs to monitor JACK's status and simplify its configuration.

: Further reading: [https://www.linux-magazine.com/content/download/63041/486886/version/1/file/JACK_Audio_Server.pdf Linux Magazine article (2006) for basic understanding on JACK parameter finding

## Latency verification
JACK parameters are most significant for controlling the round-trip delay (RTD). In the context of this article that is the overall time it takes for an audio signal to be recorded, processed and played back. The next subsection deals with theoretical background on the sources of latency adding up to the RTD. If you are already familiar with that, you can go to #Measuring latency to verify your RTD or skip this section completely.

## Latency sources
Consider a typical recording situation of a singer performance. The voice is being captured with a microphone as it propagates trough the air with the speed of sound. An analog-to-digital-conversion enables the electrical signal to be recorded by a computer for digital signal processing. Finally, a digital-to-analog conversion returns the signal to be played back at the singer's headphones for monitoring similar to stage monitor system usage.

In that voice recording situation there are five significant latency sources constructing the RTD and occuring in the following order:
# Sound propagation through the air from the mouth of the singer
# Analog-to-digital conversion
# Digital signal processing
# Digital-to-analog conversion
# Sound propagation through the air to the ear of the singer

The first and last latency source is hard to change as a particular distance is technically necessary to create an intended sound during recording or playback, respectively. Additionally, when using closer miking for capturing and headphones for monitoring both sound propagation latencies are typically within the range of a few microseconds which is not noticeable by humans. Thus, an objective for RTD minimization is to reduce the other sources of latency.

## Conversion latency
In theory JACK maintains a constant low latency by using fixed values (frames, periods, sample rate) for sampling and buffering of audio to be converted analog-to-digital and vice versa. The latency occurring in the capturing process is described by the following equation:

: Lc = n / f

Lc: Capture latency in milliseconds (ms), n: Frames or buffer (multiples of 2, starting at 16), f: Sample rate in Hertz (Hz).

The playback latency is also employing the periods value:

: Lp = n * p / f

Lp: Playback latency in milliseconds (ms), n: Frames or buffer (multiples of 2, starting at 16), p: Periods, f: Sample rate in Hertz (Hz).

As already stated before, the capabilities of the audio interface define working combinations. You have to trial and error to find a setup. Sure, it is a trade-off between xrun prevention and achieving low latency, but recent audio interfaces can be used at high sample rates (up to 192 kHz) to deal with that requirement. The audio flux of JACK clients in the digital domain is about zero and thus, negligible for latency measurements : See [https://www.alsa-project.org/main/index.php/FramesPeriods FramesPeriods in the ALSA wiki for more information.

## Measuring latency
Once you have set up #JACK parameters you might want to verify the RTD described above. For example, using a frames or buffer size of n = 128, a periods value of p = 2, and a sample rate of f = 48000 results in a capture latency of about Lc = 2,666... ms and a playback latency of about Lp = 5,333... ms summing up to a total round-trip delay of RTD = 8 ms.

The  utility by Fons Adriaensen measures RTD by emitting test tones out a playback channel and capturing them again at a capture channel for measuring the phase differences to estimate the round-trip time the signal has taken through the whole chain. Use an appropriate cable to connect an input and output channel of your audio device or put a speaker close to a microphone as described by JACK Latency tests.

For example, running  for a JACK-only setup using a cable connection between the ports playback_1 and capture_1 (the description may differ depending on your hardware) to close the loop, as well as the values discussed before yields the following insights:

As the output indicates further optimization of JACK can be done by using the parameters  and  to compensate for the reported extra loopback latency in the chain:

 $ /usr/bin/jackd -R -P89 -dalsa -dhw:0 -r48000 -p128 -n2 -I19 -O19

: More details can be found in the Ardour Manual page about latency and latency compensation.

## Realtime kernel
"Realtime" in the context of an operating system is defined that the results of a computation are available within a fixed period of time. Only in a broader sense does it mean "time running simultaneously with reality", for example, that a sound is produced immediately in response to musical user input. The latter is called "low latency" and its setup is one of the main goals of this article.

Since a while ago, the stock Linux kernel (with , default in Arch Linux vanilla kernel) has proven to be adequate for low latency operation. Latency in an operating system context is the time between the moment an interrupt occurs in hardware, and the moment the corresponding interrupt-thread gets running. Unfortunately, some device drivers can introduce higher latencies. So depending on your hardware, drivers, and requirements, you might want a kernel with hard realtime capabilities.

## Pros and cons
The RT_PREEMPT patch by Ingo Molnar and Thomas Gleixner is an interesting option for hard and firm realtime applications, reaching from professional audio to industrial control. Most audio-specific Linux distributions ships with this patch applied. A realtime-preemptible kernel will also make it possible to tweak priorities of IRQ handling threads and help ensure smooth audio almost regardless of the load.

## Installation
Install either the  or  package.

## Compilation
If you are going to compile your own kernel as a realtime kernel, remember that removing modules/options does not equate to a "leaner and meaner" kernel. It is true that the size of the kernel image is reduced, but in today's systems it is not as much of an issue as it was back in 1995.

: See HOWTO setup Linux with PREEMPT_RT properly for further general instructions.

In any way, you should also ensure that:

* Timer Frequency is set to 1000Hz (; if you do not do MIDI you can ignore this)
* APM is DISABLED (; Troublesome with some hardware - default in x86_64)

If you truly want a slim system, we suggest you go your own way and deploy one with static /devs. You should, however, set your CPU architecture. Selecting "Core 2 Duo" for appropriate hardware will allow for a good deal of optimisation, but not so much as you go down the scale.

General issue(s) with (realtime) kernels:

* Hyperthreading (if you suspect, disable in UEFI settings)

## Optimizing system configuration
You may want to consider the following system optimizations:

* Setting the CPU frequency scaling governor to performance.
* Configuring pam_limits (e.g. by installing  and adding your user to the  group).
* Using the  kernel parameter (consult for reference) - enforced by default by the realtime kernel.
* Using the realtime kernel.
* Add  to fstab (see Improving performance#Mount options).
* Increasing the highest requested RTC interrupt frequency (default is 64 Hz) by running the following at boot:

 # echo 2048 > /sys/class/rtc/rtc0/max_user_freq
 # echo 2048 > /proc/sys/dev/hpet/max-user-freq

* Reducing swappiness—swap frequency, set to  by default—to e.g.  will make the system wait much longer before trying to swap to disk. More precisely, it makes the kernel to prefer keeping all applications in RAM instead of swapping background applications out. This can be done on the fly with —see —or set up permanently using a configuration file—see —such as:

* Increasing the maximum watches on files (defaults to ) to e.g. , that inotify keeps track of for your user, can help with applications, that require many file handles (such as DAWs). This again can be done on the fly with  or in a dedicated configuration file:

You may also want to maximize the PCI latency timer of the PCI sound card and raise the latency timer of all other PCI peripherals (default is 64).

 $ setpci -v -d *:* latency_timer=b0
 # setpci -v -s $SOUND_CARD_PCI_ID latency_timer=ff

E.g. .

The SOUND_CARD_PCI_ID can be obtained like so:

## Tips and tricks
* Disable Wi-Fi and close any programs that do not need to be open when recording such as browsers. Many have reported disabling Wi-Fi has led to more reliable JACK performance.

* Some USB audio hardware is known not to work properly when plugged into USB 3 ports so try USB 2/1 ports instead.

* IRQ issues can occur and cause problems. An example is video hardware reserving the bus, causing needless interrupts in the system I/O path. See discussion at [https://web.archive.org/web/20231010103345/http://subversion.ffado.org/wiki/IrqPriorities FFADO IRQ Priorities How-To. If you have a realtime or a recent kernel, you can use  to adjust priorities of IRQ handling threads.

* Do not use the irqbalance daemon, or do so carefully * If you need to use multiple audio devices with JACK2, the alsa_in and alsa_out utilities can be used to have extra devices wrapped and show up as outputs in the JACK patchbay.

* Some daemons/processes can unexpectedly cause xruns. If you do not need it - kill it. No questions asked.

 $ ls /var/run/daemons
 $ top # or htop, ps aux, whatever you are comfortable with
 $ killall -9 $processname
 # systemctl stop $daemonname

* If you are facing a lot of xruns especially with NVIDIA, disable your GPU throttling. This can be done via the card's control applet and for NVIDIA it is "prefer maximum performance" (thanks to a post in LAU by Frank Kober[http://lalists.stanford.edu/lau/2009/10/0467.html).

## Applications
Arch Linux provides the package group  holding all relevant (semi-) professional applications. All applications in the pro-audio package group are JACK clients. Also , , ,  and  are subgroups of the pro-audio group.

An overview and brief information on some applications is found in List of applications/Multimedia#Audio. Especially the categories Digital audio workstations, Audio effects and Music trackers, as well as Audio synthesis environments and Sound generators provide examples of pro audio software for recording, mixing, mastering, and sound design. Other categories include Scorewriters, Audio editors, Audio converters, and DJ software.

Packages not (yet) in the official repositories can be found in proaudio. Browse the list of packages to find the application you need or request packaging of your desired applications via GitHub.

## Hardware
The majority of sound cards and audio devices will work with no extra configuration or packages, simply set JACK to use the desired one.

This is not true for all devices, have a look at the Sound, /Hardware as well as Envy24control#Supported cards for those special cases.

## Get help
## Mailing lists
* Arch Linux Pro-audio Discussion about real-time multimedia, including (semi-)pro audio and video.
* Linux Audio User The Linux pro-audio related mailing list with much traffic and a huge subscriber community of users and developers.

## IRC
* #archlinux-proaudio - Arch Linux pro-audio channel
* #lau - General Linux Audio channel for users
* #jack - Development and support related to JACK audio system
* #lv2 - Development and support related to the LV2 plugin format
* #ardour - Discussion and support relating to the Ardour DAW
* #opensourcemusicians - Large general OSS musician discussion channel
