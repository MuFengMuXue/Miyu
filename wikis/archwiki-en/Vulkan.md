# Vulkan

From Wikipedia:

:Vulkan is a low-overhead, cross-platform 3D graphics and compute API. First released in 2016, it is a successor to OpenGL.

Learn more on Vulkan's website.

## Installation
To run a Vulkan application, you will need to install the  package (and  from the multilib repository if you also want to run 32-bit applications), as well as Vulkan drivers for your graphics card(s). There are several packages providing a vulkan-driver and lib32-vulkan-driver:

* AMD:  (or )
* Intel:  (or )
* NVIDIA: there are two implementations:
**  (or ) - NVIDIA proprietary
**  (or ) - NVK (part of Mesa project)

The following are software rasterizers, so that you can use it on devices that do not provide Vulkan support.

* Lavapipe:  (or )
* SwiftShader:

For Vulkan application development, install , and optionally ,  and  (you can find the vulkaninfo, and vkcube tools in there).

## Verification
To see which Vulkan implementations are currently installed on your system, use the following command:

 $ ls /usr/share/vulkan/icd.d/

To ensure that Vulkan is working with your hardware, install  and use the  command to pull up relevant information about your system. If you get info about your graphics card, you will know that Vulkan is working.

 $ vulkaninfo

## Switching
## Switching between devices
On systems with multiple GPUs you may need to force the usage of a specific GPU.  is required for this to work. By setting  to , you can choose the desired GPU.

To list the candidates, use:

 $ MESA_VK_DEVICE_SELECT=list vulkaninfo

Appending an  at the end of the specified value enforces this behavior. See Vulkan mesa device select layer environment variables for more information.

## Software rendering
You can install the software Vulkan rasterizer known as lavapipe, for example to debug hardware issues:  (or  for the 32-bit version).

The following example shows running vulkaninfo with the required environment variables to force a full software rendering for Vulkan and OpenGL (with  ensuring the command also works for PRIME users):

 $ LIBGL_ALWAYS_SOFTWARE=1 __GLX_VENDOR_LIBRARY_NAME=mesa VK_DRIVER_FILES=/usr/share/vulkan/icd.d/lvp_icd.json vulkaninfo

## Vulkan hardware database
The Vulkan Hardware Database provides user reported GPU/driver combinations. Supplying own information is possible by using  or .

## Troubleshooting
## NVIDIA - vulkan is not working and can not initialize
## Environment variables
Invalid or contradictory environment variable values might cause Vulkan to fail, and inappropriate values can result in the use of a different GPU than intended on machines with multiple GPUs. Properly setting the variables can also help keep a secondary GPU powered down when it is not needed.

## GPU switching
If your machine has multiple GPUs and Vulkan cannot see or use one of them, make sure it is not currently disabled by the BIOS/UEFI or in the kernel. See NVIDIA Optimus for an overview of the different methods of switching between GPUs.

Example command to check the current status with :

## GSP firmware
See NVIDIA/Troubleshooting#GSP firmware.

## No device for the display GPU found. Are the intel-mesa drivers installed?
Try to list both the intel_icd and primus_vk_wrapper configurations in VK_DRIVER_FILES

 export VK_DRIVER_FILES=/usr/share/vulkan/icd.d/intel_icd.json:/usr/share/vulkan/icd.d/nv_vulkan_wrapper.json

## AMDGPU - ERROR_INITIALIZATION_FAILED after vulkaninfo
If after running  on AMD card from GCN1 or GCN2 family you got error message like:

Then check if you have correctly enable support for this models of graphics cards (AMDGPU#Enable Southern Islands (SI) and Sea Islands (CIK) support).

One of possibility to check if gpu drivers are correctly loaded is , after running this command check kernel driver of your gpu. It should be .

Some forum threads about this problem: [https://bbs.archlinux.org/viewtopic.php?id=253843

## AMDGPU - Vulkan applications launch slowly
If you install , you might find Vulkan applications, for example, Chromium, launch slowly. It's because  provides an Vulkan driver and Vulkan would try nvidia drivers before radeon drivers. To solve it, set the environment variable  to .
