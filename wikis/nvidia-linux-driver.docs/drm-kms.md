## Chapter 36. Direct Rendering Manager Kernel Modesetting (DRM KMS)

## Known Issues

- The NVIDIA DRM KMS implementation forces all VRR capable displays into VRR mode by default. The conceal_vrr_caps module parameter for the nvidia_modeset kernel module may be used to hide VRR capabilities from the driver to prevent forced enabling of VRR. This is useful for allowing features such as ULMB (Ultra Low Motion Blur) to function.

- The NVIDIA DRM KMS implementation is currently incompatible with SLI Mosaic. The X server will fail to initialize SLI Mosaic if DRM KMS is enabled.

- The NVIDIA DRM KMS implementation does not yet register an overlay plane: only primary and cursor planes are currently provided.

- Buffer allocation and submission to DRM KMS using gbm is not currently supported.
