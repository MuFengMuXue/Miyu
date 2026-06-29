# Hardware raytracing

This page will serve as a guide to the current state of Hardware raytracing support on Linux as well as provide information on how to set everything up.

In all cases it is assumed you will be running the game through Proton, VKD3D is required, DXVK will not work.

## AMD
AMD RDNA2 GPUs offer hardware raytracing support through onboard compute units, current performance is mixed. Since mesa 23, raytracing is enabled on a per game basis, and from mesa 23.2 raytracing will be enabled by default for all applications.

*GPU - AMD RDNA2 series or newer
*Driver -  23 or newer,

## Usage
For mesa versions below 23.2, use the following environment variables:

 RADV_PERFTEST='rt'

## Intel
Intel ARC GPUs offer hardware raytracing support through onboard TSUs, current performance is mixed.

*GPU - Intel ARC GD/2 series or newer
*Driver -  22.3 or newer,
*Kernel -  (firmware is needed for GuC support)

## Usage
Use the following environment variables:

 VKD3D_CONFIG=dxr11,dxr

## NVIDIA
NVIDIA's raytracing implementation for Linux is pretty much on par with Windows, that is to say, with supported hardware and the correct drivers RTX works well on Linux.

*GPU - Any card with the RTX moniker (RTX 2060+, RTX 3050+, RTX 4050+)
*Driver - nvidia or  with  and  (with their lib32 variants). Driver version 510.60.02 or newer.

## Testing
Install the package  then from a terminal run:

 $ cd /opt/raytracinginvulkan/bin/
 $ ./RayTracer
