# Cardinal

Cardinal is virtual modular synthesizer plugin, available as JACK standalone and AU, LV2, VST2 and VST3 audio plugin for FreeBSD, Linux, macOS and Windows.

It is based on the popular VCV Rack but with a focus on being a fully self-contained plugin version. It is DPF-based Rack wrapper that uses compiled-in modules and provides LV2/VST plugins plus a JACK app.

## Installation
Install .

When using PipeWire install .

Otherwise start up Jack.

## Usage
Using  connect Cardinal's audio_out_1 and 2 (for stereo) to your audio output.

Cardinal contains Rack, some third party modules (list here) and a few internal utilities all in a single binary.

Compared to VCV Rack Cardinal does not load external modules and does not connect to the official Rack library/store. All "Core" modules from Rack have been replaced by Cardinal equivalents, simplified to better work for an audio plugin.
However the usage is very similar if not same.
Left click and hold from jack to jack to make a connection using color from sequence, or right click to select specific color. For example you can follow Omhri Cohen's RBYG color coding.
Control and click lets you connect more cables from the same jack (in other words stacking them up).
You can follow up using many tutorials online. For example Red Means Recording's Intro to Eurorack (ft. VCV Rack) 2.5h long 4 part tutorial.

## Troubleshooting
## Clicking Save As / Export does nothing
You are missing  see FAQ
