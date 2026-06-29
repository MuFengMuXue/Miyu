## Chapter 17. Using the NVIDIA Driver with Optimus Laptops

Some laptops with NVIDIA GPUs make use of Optimus technology to allow switching between an integrated GPU and a discrete NVIDIA GPU. The NVIDIA Linux driver can be used on these systems.

### Installing the NVIDIA Driver on an Optimus Laptop

The driver may be installed normally on Optimus systems, but the NVIDIA X driver and the NVIDIA OpenGL driver may not be able to display to the laptop's internal display panel unless a means to connect the panel to the NVIDIA GPU (for example, a hardware multiplexer, or "mux", often controllable by a BIOS setting) is available. On systems without a mux, the NVIDIA GPU can still be useful for offscreen rendering, PRIME render offload, running CUDA applications, and other uses that don't require driving a display.

On muxless Optimus laptops, or on laptops where a mux is present, but not set to drive the internal display from the NVIDIA GPU, the internal display is driven by the integrated GPU. On these systems, it's important that the X server not be configured to use the NVIDIA X driver after the driver is installed. Instead, the correct driver for the integrated GPU should be used. Often, this can be determined automatically by the X server, and no explicit configuration is required, especially on newer X server versions. If your X server autoselects the NVIDIA X driver after installation, you may need to explicitly select the driver for your integrated GPU.

As an alternative to using only the integrated graphics device, support for the display output source functionality provided by the X Resize and Rotate extension version 1.4 is available. This functionality allows for graphics to be rendered on the NVIDIA GPU and displayed on the integrated graphics device. For information on how to use this functionality, see [Chapter 34, *Offloading Graphics Display with RandR 1.4*](randr14.html "Chapter 34. Offloading Graphics Display with RandR 1.4").

A second alternative is to use PRIME render offload, such that the integrated graphics device is used to drive the X screen, but the NVIDIA GPU is used on a per-application basis to accelerate rendering of specific applications. For details, see [Chapter 35, *PRIME Render Offload*](primerenderoffload.html "Chapter 35. PRIME Render Offload").

### Loading the Kernel Module and Creating the Device Files without X

In order for programs that use the NVIDIA driver to work correctly (e.g.: X, OpenGL, and CUDA applications), the kernel module must be loaded, and the device files `/dev/nvidiactl` and `/dev/nvidia[0-9]+` must exist with read and write permissions for any users of such applications. If the setuid root nvidia-modprobe(1) utility is installed (the default when the driver is installed from .run file), this should be handled automatically. Otherwise, the kernel module will need to be loaded, and the device files created, through your Linux distribution's mechanisms.

See [“How and when are the NVIDIA device files created?”](faq.html#devicenodes) for more information.

Note that on some Optimus notebooks the driver may fail to initialize the GPU due to system-specific ACPI interaction problems: see [“Why does the VBIOS fail to load on my Optimus system?”](commonproblems.html#optimusacpivbios) for more information.
