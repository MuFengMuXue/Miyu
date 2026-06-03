# single_pixel_buffer_v1

## single pixel buffer factory

This protocol extension allows clients to create single-pixel buffers. Compositors supporting this protocol extension should also support the viewporter protocol extension. Clients may use viewporter to scale a single-pixel buffer to a desired size. Warning! The protocol described in this file is currently in the testing phase. Backward compatible changes may be added together with the corresponding interface version bump. Backward incompatible changes can only be done by creating a new major version of the extension.

## Interface `wp_single_pixel_buffer_manager_v1` version 1

global factory for single-pixel buffers

The wp_single_pixel_buffer_manager_v1 interface is a factory for single-pixel buffers.

### Requests

- `destroy`: destroy the manager
  Destroy the wp_single_pixel_buffer_manager_v1 object. The child objects created via this interface are unaffected.
- `create_u32_rgba_buffer`: create a 1×1 buffer from 32-bit RGBA values
  Create a single-pixel buffer from four 32-bit RGBA values. Unless specified in another protocol extension, the RGBA values use pre-multiplied alpha. The width and height of the buffer are 1. The r, g, b and a arguments valid range is from UINT32_MIN (0) to UINT32_MAX (0xffffffff). These arguments should be interpreted as a percentage, i.e. - UINT32_MIN = 0% of the given color component - UINT32_MAX = 100% of the given color component
  Arguments: `id` (new_id); `r` (uint) - value of the buffer's red channel; `g` (uint) - value of the buffer's green channel; `b` (uint) - value of the buffer's blue channel; `a` (uint) - value of the buffer's alpha channel
