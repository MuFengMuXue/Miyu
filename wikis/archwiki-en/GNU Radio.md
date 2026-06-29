# GNU Radio

GNU Radio is a free & open-source software development toolkit that provides signal processing blocks to implement software radios. It can be used with readily-available low-cost external RF hardware to create software-defined radios, or without hardware in a simulation-like environment. It is widely used in hobbyist, academic and commercial environments to support both wireless communications research and real-world radio systems.

## Installation
The latest stable GNU Radio version can be installed with .

Bleeding edge is , and in some cases VOLK may need to be built separately from .

If you want , just install the  package which will install GNU Radio, as well as some additional required packages.

Another popular package is  which provides the GRC source blocks for many of the popular SDR devices (Funcube Dongle, RTL-SDR, USRP, OsmoSDR, BladeRF and HackRF).

## Troubleshooting
## TypeError: in method 'source_sptr_set_gain_mode', argument 2 of type 'bool'
When using an (osmocom) RTL-SDR source, you might see this error. The workaround is to manually set the Gain Mode to  or .
