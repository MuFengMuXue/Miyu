# color_representation_v1

## color representation protocol extension

This protocol extension delivers the metadata required to define alpha mode, the color model, sub-sampling and quantization range used when interpreting buffer contents. The main use case is defining how the YCbCr family of pixel formats convert to RGB. Note that this protocol does not define the colorimetry of the resulting RGB channels / tristimulus values. Without the help of other extensions the resulting colorimetry is therefore implementation defined. If this extension is not used, the color representation used is compositor implementation defined. Recommendation ITU-T H.273 "Coding-independent code points for video signal type identification" shall be referred to as simply H.273 here.

## Interface `wp_color_representation_manager_v1` version 1

color representation manager singleton

A singleton global interface used for getting color representation extensions for wl_surface. The extension interfaces allow setting the color representation of surfaces. Compositors should never remove this global.

### Requests

- `destroy`: destroy the manager
  Destroy the wp_color_representation_manager_v1 object. This does not affect any other objects in any way.
- `get_surface`: create a color representation interface for a wl_surface
  If a wp_color_representation_surface_v1 object already exists for the given wl_surface, the protocol error surface_exists is raised. This creates a new color wp_color_representation_surface_v1 object for the given wl_surface. See the wp_color_representation_surface_v1 interface for more details.
  Arguments: `id` (new_id); `surface` (object)

### Events

- `supported_alpha_mode`: supported alpha modes
  When this object is created, it shall immediately send this event once for each alpha mode the compositor supports. For the definition of the supported values, see the wp_color_representation_surface_v1::alpha_mode enum.
  Arguments: `alpha_mode` (uint) - supported alpha mode
- `supported_coefficients_and_ranges`: supported matrix coefficients and ranges
  When this object is created, it shall immediately send this event once for each matrix coefficient and color range combination the compositor supports. For the definition of the supported values, see the wp_color_representation_surface_v1::coefficients and wp_color_representation_surface_v1::range enums.
  Arguments: `coefficients` (uint) - supported matrix coefficients; `range` (uint) - full range flag
- `done`: all features have been sent
  This event is sent when all supported features have been sent.

### Enums

- `error`: protocol errors

## Interface `wp_color_representation_surface_v1` version 1

color representation extension to a surface

A wp_color_representation_surface_v1 allows the client to set the color representation metadata of a surface. By default, a surface does not have any color representation metadata set. The reconstruction of R, G, B signals on such surfaces is compositor implementation defined. The alpha mode is assumed to be premultiplied_electrical when the alpha mode is unset. If the wl_surface associated with the wp_color_representation_surface_v1 is destroyed, the wp_color_representation_surface_v1 object becomes inert.

### Requests

- `destroy`: destroy the color representation
  Destroy the wp_color_representation_surface_v1 object. Destroying this object unsets all the color representation metadata from the surface. See the wp_color_representation_surface_v1 interface description for how a compositor handles a surface without color representation metadata. Unsetting is double-buffered state, see wl_surface.commit.
- `set_alpha_mode`: set the surface alpha mode
  If this protocol object is inert, the protocol error inert is raised. Assuming an alpha channel exists, it is always linear. The alpha mode determines whether and how the color channels include pre-multiplied alpha. Using straight alpha might have performance benefits. Only alpha modes advertised by the compositor are allowed to be used as argument for this request. The "alpha_mode" protocol error is raised otherwise. Alpha mode is double buffered, see wl_surface.commit.
  Arguments: `alpha_mode` (uint) - alpha mode
- `set_coefficients_and_range`: set the matrix coefficients and range
  If this protocol object is inert, the protocol error inert is raised. Set the matrix coefficients and video range which defines the formula and the related constants used to derive red, green and blue signals. Usually coefficients correspond to MatrixCoefficients code points in H.273. Only combinations advertised by the compositor are allowed to be used as argument for this request. The "coefficients" protocol error is raised otherwise. A call to wl_surface.commit verifies that the pixel format and the coefficients-range combination in the committed surface contents are compatible, if contents exist. The "pixel_format" protocol error is raised otherwise. A pixel format is compatible with the coefficients-range combination if the related equations and conventions as defined in H.273 can produce the color channels (RGB or YCbCr) of the pixel format. For the definition of the supported combination, see the wp_color_representation_surface_v1::coefficients and wp_color_representation_surface_v1::range enums. The coefficients-range combination is double-buffered, see wl_surface.commit.
  Arguments: `coefficients` (uint) - matrix coefficients; `range` (uint) - range
- `set_chroma_location`: set the chroma location
  If this protocol object is inert, the protocol error inert is raised. Set the chroma location type which defines the position of downsampled chroma samples, corresponding to Chroma420SampleLocType code points in H.273. An invalid chroma location enum value raises the "chroma_location" protocol error. A call to wl_surface.commit verifies that the pixel format and chroma location type in the committed surface contents are compatible, if contents exist. The "pixel_format" protocol error is raised otherwise. For the definition of the supported chroma location types, see the wp_color_representation_surface_v1::chroma_location enum. The chroma location type is double-buffered, see wl_surface.commit.
  Arguments: `chroma_location` (uint) - chroma sample location

### Enums

- `error`: protocol errors
- `alpha_mode`: alpha mode
  Specifies how the alpha channel affects the color channels.
- `coefficients`: named coefficients
  Named matrix coefficients used to encode well-known sets of coefficients. H.273 is the authority, when it comes to the exact values of coefficients and authoritative specifications, where an equivalent code point exists. A value of 0 is invalid and will never be present in the list of enums. Descriptions do list the specifications for convenience.
- `range`: Color range values
  Possible color range values. A value of 0 is invalid and will never be present in the list of enums.
- `chroma_location`: Chroma sample location for 4:2:0 YCbCr
  Chroma sample location as defined by H.273 Chroma420SampleLocType. A value of 0 is invalid and will never be present in the list of enums. The descriptions list the matching Vulkan VkChromaLocation combinations for convenience.
