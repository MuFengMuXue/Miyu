# VK_KHR_portability_subset Validation

## Requirements

Either
- The [VK_LAYER_KHRONOS_profiles](https://github.com/KhronosGroup/Vulkan-Profiles) layer with portability enabled _or_
- A driver that supports `VK_KHR_portability_subset`.

## Running the portability tests

All tests can be tested with `--gtest_filter=VkPortability*`

The [./tests README](../tests/README.md) explains how to use the `VK_LAYER_KHRONOS_profiles` to test the Validation Layers

**NOTE** that for portability tests to make sure `VK_KHR_portability_subset` is exposed from the `VVL Test Driver`

```bash
export VK_KHRONOS_PROFILES_EMULATE_PORTABILITY=false
```
