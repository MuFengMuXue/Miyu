# Vulkan Validation Layers (VVL)

## Introduction

Vulkan is an Explicit API, enabling direct control over how GPUs actually work. By design, minimal error checking is done inside
a Vulkan driver. Applications have full control and responsibility for correct operation. Any errors in
how Vulkan is used can result in a crash. This project provides Vulkan validation layers that can be enabled
to assist development by enabling developers to verify their applications correct use of the Vulkan API.

## Getting Binaries

For those who don't want to build from source, there are few ways to get working binaries to use
- The [Vulkan SDK](https://vulkan.lunarg.com/sdk/home) will have the most well tested versions of the layer
- For Android, each SDK tag will have binaries to download (example: [vulkan-sdk-1.3.280.0 tag](https://github.com/KhronosGroup/Vulkan-ValidationLayers/releases/tag/vulkan-sdk-1.3.280.0))
- Every change applied to the main branch runs through GitHub action and will [produce artifacts](https://github.com/KhronosGroup/Vulkan-ValidationLayers/actions?query=branch%3Amain) of the latest commit.

## Ways to enable the layer

* Use [*Vulkan Configurator*](https://www.lunarg.com/introducing-the-new-vulkan-configurator-vkconfig/)
* Set environment variables
     * Windows `set VK_INSTANCE_LAYERS=VK_LAYER_KHRONOS_validation`
     * Linux `export VK_INSTANCE_LAYERS=VK_LAYER_KHRONOS_validation`
     * [Android](https://developer.android.com/ndk/guides/graphics/validation-layer)
* [More information](https://vulkan.lunarg.com/doc/view/latest/windows/layer_configuration.html)

## Adjusting Settings

See [documentation](./docs/khronos_validation_layer.md#configuring-the-validation-layer).
