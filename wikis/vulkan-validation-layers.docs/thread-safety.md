# Thread Safety Validation

The thread safety validation object checks multi-threading of API calls for validity.  Checks performed
include ensuring that only one thread at a time uses an object in free-threaded API calls.

## Configuring Thread Safety Validation

For an overview of how to configure layers, refer to the [Layers Overview and Configuration](https://vulkan.lunarg.com/doc/sdk/latest/windows/layer_configuration.html) document.

The Thread Safety Validation settings are managed by configuring the Validation Layer. These settings are described in the
[VK_LAYER_KHRONOS_validation](https://vulkan.lunarg.com/doc/sdk/latest/windows/khronos_validation_layer.html#user-content-layer-details) document.
