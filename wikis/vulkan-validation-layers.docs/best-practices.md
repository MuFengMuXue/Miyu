# Best Practices Validation

Best Practices Validation is implemented in the `VK_LAYER_KHRONOS_validation layer`. When enabled, the Best Practices Object is
intended to highlight potential performance issues, questionable usage patterns, common mistakes, and items not specifically prohibited
by the Vulkan specification but that may lead to application problems.

Best Practices will ideally be run periodically along with normal validation checks so that issues may be addressed in early stages of development.

The specific areas covered by this layer are currently tracked in the
[Best Practices Project](https://github.com/KhronosGroup/Vulkan-ValidationLayers/projects/1).
Requests for additional checks can be requested by creating a Github issue.

## Configuring Best Practices Validation

For an overview of how to configure layers, refer to the [Layers Overview and Configuration](https://vulkan.lunarg.com/doc/sdk/latest/windows/layer_configuration.html) document.

Best Practices Validation settings are managed by configuring the Validation Layer. These settings are described in the
[VK_LAYER_KHRONOS_validation](https://vulkan.lunarg.com/doc/sdk/latest/windows/khronos_validation_layer.html#user-content-layer-details) document.

Best Practices Validation settings can also be enabled and configured using the [Vulkan Configurator](https://vulkan.lunarg.com/doc/sdk/latest/windows/vkconfig.html) included with the Vulkan SDK.
