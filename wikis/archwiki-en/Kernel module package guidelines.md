# Kernel module package guidelines

## Package separation
Packages that contain kernel modules should be treated specially, to support users who wish to have more than one kernel installed on a system.

When packaging software containing a kernel module and other non-module supporting files/utilities, it is important to separate the kernel modules from the supporting files.

## Guidelines
When packaging such software (using the NVIDIA drivers as an example) the convention is:

* create an nvidia package containing just the kernel modules built for the vanilla kernel
* create an nvidia-utils package containing the supporting files
* make sure nvidia depends on nvidia-utils (unless there is a good reason not to do so)
* for another kernel like linux-mm, create nvidia-mm containing the kernel modules built against that kernel which provides nvidia and also depends on nvidia-utils
* make sure nvidia depends on the kernel, for example:

## Rationale
While kernel modules built for different kernels always live in different directories and can peacefully coexist, the supporting files are expected to be found in one location. If one package contained module and supporting files, you would be unable to install the modules for more than one kernel because the supporting files in the packages would cause pacman file conflicts.

The separation of modules and accompanying files allows multiple kernel module packages to be installed for multiple kernels on the same system while sharing the supporting files among them in the expected location.

## File placement
If a package includes a kernel module that is meant to override an existing module of the same name, such module should be placed in the  directory.  When depmod is run, modules in this directory will take precedence.
