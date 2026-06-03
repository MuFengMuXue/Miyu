# color_management_v1

## color management protocol

The aim of the color management extension is to allow clients to know the color properties of outputs, and to tell the compositor about the color properties of their content on surfaces. All surface contents must be readily intended for some display, but not necessarily for the display at hand. Doing this enables a compositor to perform automatic color management of content for different outputs according to how content is intended to look like. For an introduction, see the section "Color management" in the Wayland documentation at https://wayland.freedesktop.org/docs/html/ . The color properties are represented as an image description object which is immutable after it has been created. A wl_output always has an associated image description that clients can observe. A wl_surface always has an associated preferred image description as a hint chosen by the compositor that clients can also observe. Clients can set an image description on a wl_surface to denote the color characteristics of the surface contents. An image description essentially defines a display and (indirectly) its viewing environment. An image description includes SDR and HDR colorimetry and encoding, HDR metadata, and some parameters related to the viewing environment. An image description does not include the properties set through color-representation extension. It is expected that the color-representation extension is used in conjunction with the color-management extension when necessary, particularly with the YUV family of pixel formats. The normative appendix for this protocol is in the appendix.md file beside this XML file. The color-and-hdr repository (https://gitlab.freedesktop.org/pq/color-and-hdr) contains background information on the protocol design and legacy color management. It also contains a glossary, learning resources for digital color, tools, samples and more. The terminology used in this protocol is based on common color science and color encoding terminology where possible. The glossary in the color-and-hdr repository shall be the authority on the definition of terms in this protocol. Warning! The protocol described in this file is currently in the testing phase. Backward compatible changes may be added together with the corresponding interface version bump. Backward incompatible changes can only be done by creating a new major version of the extension.

## Interface `wp_color_manager_v1` version 3

color manager singleton

A singleton global interface used for getting color management extensions for wl_surface and wl_output objects, and for creating client defined image description objects. The extension interfaces allow getting the image description of outputs and setting the image description of surfaces. Compositors should never remove this global.

### Requests

- `destroy`: destroy the color manager
  Destroy the wp_color_manager_v1 object. This does not affect any other objects in any way.
- `get_output`: create a color management interface for a wl_output
  This creates a new wp_color_management_output_v1 object for the given wl_output. See the wp_color_management_output_v1 interface for more details.
  Arguments: `id` (new_id); `output` (object)
- `get_surface`: create a color management interface for a wl_surface
  If a wp_color_management_surface_v1 object already exists for the given wl_surface, the protocol error surface_exists is raised. This creates a new color wp_color_management_surface_v1 object for the given wl_surface. See the wp_color_management_surface_v1 interface for more details.
  Arguments: `id` (new_id); `surface` (object)
- `get_surface_feedback`: create a color management feedback interface
  This creates a new color wp_color_management_surface_feedback_v1 object for the given wl_surface. See the wp_color_management_surface_feedback_v1 interface for more details.
  Arguments: `id` (new_id); `surface` (object)
- `create_icc_creator`: make a new ICC-based image description creator object
  Makes a new ICC-based image description creator object with all properties initially unset. The client can then use the object's interface to define all the required properties for an image description and finally create a wp_image_description_v1 object. This request can be used when the compositor advertises wp_color_manager_v1.feature.icc_v2_v4. Otherwise this request raises the protocol error unsupported_feature.
  Arguments: `obj` (new_id) - the new creator object
- `create_parametric_creator`: make a new parametric image description creator object
  Makes a new parametric image description creator object with all properties initially unset. The client can then use the object's interface to define all the required properties for an image description and finally create a wp_image_description_v1 object. This request can be used when the compositor advertises wp_color_manager_v1.feature.parametric. Otherwise this request raises the protocol error unsupported_feature.
  Arguments: `obj` (new_id) - the new creator object
- `create_windows_scrgb`: create Windows-scRGB image description object
  This creates a pre-defined image description for the so-called Windows-scRGB stimulus encoding. This comes from the Windows 10 handling of its own definition of an scRGB color space for an HDR screen driven in BT.2100/PQ signalling mode. Windows-scRGB uses sRGB (BT.709) color primaries and white point. The transfer characteristic is extended linear. The nominal color channel value range is extended, meaning it includes negative and greater than 1.0 values. Negative values are used to escape the sRGB color gamut boundaries. To make use of the extended range, the client needs to use a pixel format that can represent those values, e.g. floating-point 16 bits per channel. Nominal color value R=G=B=0.0 corresponds to BT.2100/PQ system 0 cd/m², and R=G=B=1.0 corresponds to BT.2100/PQ system 80 cd/m². The maximum is R=G=B=125.0 corresponding to 10k cd/m². Windows-scRGB is displayed by Windows 10 by converting it to BT.2100/PQ, maintaining the CIE 1931 chromaticity and mapping the luminance as above. No adjustment is made to the signal to account for the viewing conditions. The reference white level of Windows-scRGB is unknown. If a reference white level must be assumed for compositor processing, it should be R=G=B=2.5375 corresponding to 203 cd/m² of Report ITU-R BT.2408-7. The target color volume of Windows-scRGB is unknown. The color gamut may be anything between sRGB and BT.2100. Note: EGL_EXT_gl_colorspace_scrgb_linear definition differs from Windows-scRGB by using R=G=B=1.0 as the reference white level, while Windows-scRGB reference white level is unknown or varies. However, it seems probable that Windows implements both EGL_EXT_gl_colorspace_scrgb_linear and Vulkan VK_COLOR_SPACE_EXTENDED_SRGB_LINEAR_EXT as Windows-scRGB. This request can be used when the compositor advertises wp_color_manager_v1.feature.windows_scrgb. Otherwise this request raises the protocol error unsupported_feature. The resulting image description object does not allow get_information request. The wp_image_description_v1.ready event shall be sent.
  Arguments: `image_description` (new_id)
- `get_image_description` since 2: create an image description from a reference
  This request retrieves the image description backing a reference. The get_information request can be used if and only if the request that creates the reference allows it.
  Arguments: `image_description` (new_id); `reference` (object)
- `create_windows_bt2100` since 3: create Windows-BT.2100 image description object
  This creates a pre-defined image description for the so-called Windows-BT.2100 stimulus encoding. This comes from the Windows 10 handling of its own definition of a BT.2100 color space for an HDR screen driven in BT.2100/PQ signalling mode. Windows-BT.2100 uses BT.2020 color primaries and white point. The transfer characteristic is st2084_pq. Windows-BT.2100 is generally displayed by Windows 10 without any adjustments to the signal to account for viewing conditions. The reference white level of Windows-BT.2100 is unknown. If a reference white level must be assumed for compositor processing, it should be 203 cd/m² of Report ITU-R BT.2408-7. The target color volume of Windows-BT.2100 is unknown. The color gamut may be anything up to BT.2100. This request can be used when the compositor advertises wp_color_manager_v1.feature.windows_bt2100. Otherwise this request raises the protocol error unsupported_feature. The resulting image description object does not allow get_information request. The wp_image_description_v1.ready event shall be sent.
  Arguments: `image_description` (new_id)

### Events

- `supported_intent`: supported rendering intent
  When this object is created, it shall immediately send this event once for each rendering intent the compositor supports. A compositor must not advertise intents that are deprecated in the bound version of the interface.
  Arguments: `render_intent` (uint) - rendering intent
- `supported_feature`: supported features
  When this object is created, it shall immediately send this event once for each compositor supported feature listed in the enumeration. A compositor must not advertise features that are deprecated in the bound version of the interface.
  Arguments: `feature` (uint) - supported feature
- `supported_tf_named`: supported named transfer characteristic
  When this object is created, it shall immediately send this event once for each named transfer function the compositor supports with the parametric image description creator. A compositor must not advertise transfer functions that are deprecated in the bound version of the interface.
  Arguments: `tf` (uint) - Named transfer function
- `supported_primaries_named`: supported named primaries
  When this object is created, it shall immediately send this event once for each named set of primaries the compositor supports with the parametric image description creator. A compositor must not advertise names that are deprecated in the bound version of the interface.
  Arguments: `primaries` (uint) - Named color primaries
- `done`: all features have been sent
  This event is sent when all supported rendering intents, features, transfer functions and named primaries have been sent.

### Enums

- `error`
- `render_intent`: rendering intents
  See the ICC.1:2022 specification from the International Color Consortium for more details about rendering intents. The principles of ICC defined rendering intents apply with all types of image descriptions, not only those with ICC file profiles. Compositors must support the perceptual rendering intent. Other rendering intents are optional.
- `feature`: compositor supported features
- `primaries`: named color primaries
  Named color primaries used to encode well-known sets of primaries. A value of 0 is invalid and will never be present in the list of enums.
- `transfer_function`: named transfer functions
  Named transfer functions used to represent well-known transfer characteristics of displays. A value of 0 is invalid and will never be present in the list of enums. See appendix.md for the formulae.

## Interface `wp_color_management_output_v1` version 3

output color properties

A wp_color_management_output_v1 describes the color properties of an output. The wp_color_management_output_v1 is associated with the wl_output global underlying the wl_output object. Therefore the client destroying the wl_output object has no impact, but the compositor removing the output global makes the wp_color_management_output_v1 object inert.

### Requests

- `destroy`: destroy the color management output
  Destroy the color wp_color_management_output_v1 object. This does not affect any remaining protocol objects.
- `get_image_description`: get the image description of the output
  This creates a new wp_image_description_v1 object for the current image description of the output. There always is exactly one image description active for an output so the client should destroy the image description created by earlier invocations of this request. This request is usually sent as a reaction to the image_description_changed event or when creating a wp_color_management_output_v1 object. The image description of an output represents the color encoding the output expects. There might be performance and power advantages, as well as improved color reproduction, if a content update matches the image description of the output it is being shown on. If a content update is shown on any other output than the one it matches the image description of, then the color reproduction on those outputs might be considerably worse. The created wp_image_description_v1 object preserves the image description of the output from the time the object was created. The resulting image description object allows get_information request. If this protocol object is inert, the resulting image description object shall immediately deliver the wp_image_description_v1.failed event with the no_output cause. If the interface version is inadequate for the output's image description, meaning that the client does not support all the events needed to deliver the crucial information, the resulting image description object shall immediately deliver the wp_image_description_v1.failed event with the low_version cause. Otherwise the object shall immediately deliver the ready event.
  Arguments: `image_description` (new_id)

### Events

- `image_description_changed`: image description changed
  This event is sent whenever the image description of the output changed, followed by one wl_output.done event common to output events across all extensions. If the client wants to use the updated image description, it needs to do get_image_description again, because image description objects are immutable.

## Interface `wp_color_management_surface_v1` version 3

color management extension to a surface

A wp_color_management_surface_v1 allows the client to set the color space and HDR properties of a surface. If the wl_surface associated with the wp_color_management_surface_v1 is destroyed, the wp_color_management_surface_v1 object becomes inert.

### Requests

- `destroy`: destroy the color management interface for a surface
  Destroy the wp_color_management_surface_v1 object and do the same as unset_image_description.
- `set_image_description`: set the surface image description
  If this protocol object is inert, the protocol error inert is raised. Set the image description of the underlying surface. The image description and rendering intent are double-buffered state, see wl_surface.commit. It is the client's responsibility to understand the image description it sets on a surface, and to provide content that matches that image description. Compositors might convert images to match their own or any other image descriptions. Image descriptions which are not ready (see wp_image_description_v1) are forbidden in this request, and in such case the protocol error image_description is raised. All image descriptions which are ready (see wp_image_description_v1) are allowed and must always be accepted by the compositor. When an image description is set on a surface, it establishes an explicit link between surface pixel values and surface colorimetry. This link may be undefined for some pixel values, see the image description creator interfaces for the conditions. Non-finite floating-point values (NaN, Inf) always have an undefined colorimetry. A rendering intent provides the client's preference on how surface colorimetry should be mapped to each output. The render_intent value must be one advertised by the compositor with wp_color_manager_v1.render_intent event, otherwise the protocol error render_intent is raised. By default, a surface does not have an associated image description nor a rendering intent. The handling of color on such surfaces is compositor implementation defined. Compositors should handle such surfaces as sRGB, but may handle them differently if they have specific requirements. Setting the image description has copy semantics; after this request, the image description can be immediately destroyed without affecting the pending state of the surface.
  Arguments: `image_description` (object); `render_intent` (uint) - rendering intent
- `unset_image_description`: remove the surface image description
  If this protocol object is inert, the protocol error inert is raised. This request removes any image description from the surface. See set_image_description for how a compositor handles a surface without an image description. This is double-buffered state, see wl_surface.commit.

### Enums

- `error`: protocol errors

## Interface `wp_color_management_surface_feedback_v1` version 3

color management extension to a surface

A wp_color_management_surface_feedback_v1 allows the client to get the preferred image description of a surface. If the wl_surface associated with this object is destroyed, the wp_color_management_surface_feedback_v1 object becomes inert.

### Requests

- `destroy`: destroy the color management interface for a surface
  Destroy the wp_color_management_surface_feedback_v1 object.
- `get_preferred`: get the preferred image description
  If this protocol object is inert, the protocol error inert is raised. The preferred image description represents the compositor's preferred color encoding for this wl_surface at the current time. There might be performance and power advantages, as well as improved color reproduction, if the image description of a content update matches the preferred image description. This creates a new wp_image_description_v1 object for the currently preferred image description for the wl_surface. The client should stop using and destroy the image descriptions created by earlier invocations of this request for the associated wl_surface. This request is usually sent as a reaction to the preferred_changed event or when creating a wp_color_management_surface_feedback_v1 object if the client is capable of adapting to image descriptions. The created wp_image_description_v1 object preserves the preferred image description of the wl_surface from the time the object was created. The resulting image description object allows get_information request. If the image description is parametric, the client should set it on its wl_surface only if the image description is an exact match with the client content. Particularly if everything else matches, but the target color volume is greater than what the client needs, the client should create its own parameric image description with its exact parameters. If the interface version is inadequate for the preferred image description, meaning that the client does not support all the events needed to deliver the crucial information, the resulting image description object shall immediately deliver the wp_image_description_v1.failed event with the low_version cause, otherwise the object shall immediately deliver the ready event.
  Arguments: `image_description` (new_id)
- `get_preferred_parametric`: get the preferred image description
  The same description as for get_preferred applies, except the returned image description is guaranteed to be parametric. This is meant for clients that can only deal with parametric image descriptions. If the compositor doesn't support parametric image descriptions, the unsupported_feature error is emitted.
  Arguments: `image_description` (new_id)

### Events

- `preferred_changed`: the preferred image description changed (32-bit)
  Starting from interface version 2, 'preferred_changed2' is sent instead of this event. See the 'preferred_changed2' event for the definition.
  Arguments: `identity` (uint) - the 32-bit image description id number
- `preferred_changed2` since 2: the preferred image description changed
  The preferred image description is the one which likely has the most performance and/or quality benefits for the compositor if used by the client for its wl_surface contents. This event is sent whenever the compositor changes the wl_surface's preferred image description. This event sends the identity of the new preferred state as the argument, so clients who are aware of the image description already can reuse it. Otherwise, if the client client wants to know what the preferred image description is, it shall use the get_preferred request. The preferred image description is not automatically used for anything. It is only a hint, and clients may set any valid image description with set_image_description, but there might be performance and color accuracy improvements by providing the wl_surface contents in the preferred image description. Therefore clients that can, should render according to the preferred image description
  Arguments: `identity_hi` (uint) - high 32 bits of the 64-bit image description id number; `identity_lo` (uint) - low 32 bits of the 64-bit image description id number

### Enums

- `error`: protocol errors

## Interface `wp_image_description_creator_icc_v1` version 3

holder of image description ICC information

This type of object is used for collecting all the information required to create a wp_image_description_v1 object from an ICC file. A complete set of required parameters consists of these properties: - ICC file Each required property must be set exactly once if the client is to create an image description. The set requests verify that a property was not already set. The create request verifies that all required properties are set. There may be several alternative requests for setting each property, and in that case the client must choose one of them. Once all properties have been set, the create request must be used to create the image description object, destroying the creator in the process. The link between a pixel value (a device value in ICC) and its respective colorimetry is defined by the details of the particular ICC profile. Those details also determine when colorimetry becomes undefined.

### Requests

- `create`: Create the image description object from ICC data
  Create an image description object based on the ICC information previously set on this object. A compositor must parse the ICC data in some undefined but finite amount of time. The completeness of the parameter set is verified. If the set is not complete, the protocol error incomplete_set is raised. For the definition of a complete set, see the description of this interface. If the particular combination of the information is not supported by the compositor, the resulting image description object shall immediately deliver the wp_image_description_v1.failed event with the 'unsupported' cause. If a valid image description was created from the information, the wp_image_description_v1.ready event will eventually be sent instead. This request destroys the wp_image_description_creator_icc_v1 object. The resulting image description object does not allow get_information request.
  Arguments: `image_description` (new_id)
- `set_icc_file`: set the ICC profile file
  Sets the ICC profile file to be used as the basis of the image description. The data shall be found through the given fd at the given offset, having the given length. The fd must be seekable and readable. Violating these requirements raises the bad_fd protocol error. If reading the data fails due to an error independent of the client, the compositor shall send the wp_image_description_v1.failed event on the created wp_image_description_v1 with the 'operating_system' cause. The maximum size of the ICC profile is 32 MB. If length is greater than that or zero, the protocol error bad_size is raised. If offset + length exceeds the file size, the protocol error out_of_file is raised. A compositor may read the file at any time starting from this request and only until whichever happens first: - If create request was issued, the wp_image_description_v1 object delivers either failed or ready event; or - if create request was not issued, this wp_image_description_creator_icc_v1 object is destroyed. A compositor shall not modify the contents of the file, and the fd may be sealed for writes and size changes. The client must ensure to its best ability that the data does not change while the compositor is reading it. The data must represent a valid ICC profile. The ICC profile version must be 2 or 4, it must be a 3 channel profile and the class must be Display or ColorSpace. Violating these requirements will not result in a protocol error, but will eventually send the wp_image_description_v1.failed event on the created wp_image_description_v1 with the 'unsupported' cause. See the International Color Consortium specification ICC.1:2022 for more details about ICC profiles. If ICC file has already been set on this object, the protocol error already_set is raised.
  Arguments: `icc_profile` (fd) - ICC profile; `offset` (uint) - byte offset in fd to start of ICC data; `length` (uint) - length of ICC data in bytes

### Enums

- `error`: protocol errors

## Interface `wp_image_description_creator_params_v1` version 3

holder of image description parameters

This type of object is used for collecting all the parameters required to create a wp_image_description_v1 object. A complete set of required parameters consists of these properties: - transfer characteristic function (tf) - chromaticities of primaries and white point (primary color volume) The following properties are optional and have a well-defined default if not explicitly set: - primary color volume luminance range - reference white luminance level - mastering display primaries and white point (target color volume) - mastering luminance range The following properties are optional and will be ignored if not explicitly set: - maximum content light level - maximum frame-average light level Each required property must be set exactly once if the client is to create an image description. The set requests verify that a property was not already set. The create request verifies that all required properties are set. There may be several alternative requests for setting each property, and in that case the client must choose one of them. Once all properties have been set, the create request must be used to create the image description object, destroying the creator in the process. A viewer, who is viewing the display defined by the resulting image description (the viewing environment included), is assumed to be fully adapted to the primary color volume's white point. Any of the following conditions will cause the colorimetry of a pixel to become undefined: - Values outside of the defined range of the transfer characteristic. - Tristimulus that exceeds the target color volume. - If extended_target_volume is not supported: tristimulus that exceeds the primary color volume. The closest correspondence to an image description created through this interface is the Display class of profiles in ICC.

### Requests

- `create`: Create the image description object using params
  Create an image description object based on the parameters previously set on this object. The completeness of the parameter set is verified. If the set is not complete, the protocol error incomplete_set is raised. For the definition of a complete set, see the description of this interface. When both max_cll and max_fall are set, max_fall must be less or equal to max_cll otherwise the invalid_luminance protocol error is raised. In version 1, these following conditions also result in the invalid_luminance protocol error. Version 2 and later do not have this requirement. - When max_cll is set, it must be greater than min L and less or equal to max L of the mastering luminance range. - When max_fall is set, it must be greater than min L and less or equal to max L of the mastering luminance range. If the particular combination of the parameter set is not supported by the compositor, the resulting image description object shall immediately deliver the wp_image_description_v1.failed event with the 'unsupported' cause. If a valid image description was created from the parameter set, the wp_image_description_v1.ready event will eventually be sent instead. This request destroys the wp_image_description_creator_params_v1 object. The resulting image description object does not allow get_information request.
  Arguments: `image_description` (new_id)
- `set_tf_named`: named transfer characteristic
  Sets the transfer characteristic using explicitly enumerated named functions. When the resulting image description is attached to an image, the content should be decoded according to the industry standard practices for the transfer characteristic. Only names advertised with wp_color_manager_v1 event supported_tf_named are allowed. Other values shall raise the protocol error invalid_tf. If transfer characteristic has already been set on this object, the protocol error already_set is raised.
  Arguments: `tf` (uint) - named transfer function
- `set_tf_power`: transfer characteristic as a power curve
  Sets the color component transfer characteristic to a power curve with the given exponent. Negative values are handled by mirroring the positive half of the curve through the origin. The valid domain and range of the curve are all finite real numbers. This curve represents the conversion from electrical to optical color channel values. The curve exponent shall be multiplied by 10000 to get the argument eexp value to carry the precision of 4 decimals. The curve exponent must be at least 1.0 and at most 10.0. Otherwise the protocol error invalid_tf is raised. If transfer characteristic has already been set on this object, the protocol error already_set is raised. This request can be used when the compositor advertises wp_color_manager_v1.feature.set_tf_power. Otherwise this request raises the protocol error unsupported_feature.
  Arguments: `eexp` (uint) - the exponent * 10000
- `set_primaries_named`: named primaries
  Sets the color primaries and white point using explicitly named sets. This describes the primary color volume which is the basis for color value encoding. Only names advertised with wp_color_manager_v1 event supported_primaries_named are allowed. Other values shall raise the protocol error invalid_primaries_named. If primaries have already been set on this object, the protocol error already_set is raised.
  Arguments: `primaries` (uint) - named primaries
- `set_primaries`: primaries as chromaticity coordinates
  Sets the color primaries and white point using CIE 1931 xy chromaticity coordinates. This describes the primary color volume which is the basis for color value encoding. Each coordinate value is multiplied by 1 million to get the argument value to carry precision of 6 decimals. If primaries have already been set on this object, the protocol error already_set is raised. This request can be used if the compositor advertises wp_color_manager_v1.feature.set_primaries. Otherwise this request raises the protocol error unsupported_feature.
  Arguments: `r_x` (int) - Red x * 1M; `r_y` (int) - Red y * 1M; `g_x` (int) - Green x * 1M; `g_y` (int) - Green y * 1M; `b_x` (int) - Blue x * 1M; `b_y` (int) - Blue y * 1M; `w_x` (int) - White x * 1M; `w_y` (int) - White y * 1M
- `set_luminances`: primary color volume luminance range and reference white
  Sets the primary color volume luminance range and the reference white luminance level. These values include the minimum display emission, but not external flare. The minimum display emission is assumed to have the chromaticity of the primary color volume white point. The default luminances from https://www.color.org/chardata/rgb/srgb.xalter are - primary color volume minimum: 0.2 cd/m² - primary color volume maximum: 80 cd/m² - reference white: 80 cd/m² Setting a named transfer characteristic can imply other default luminances. The default luminances get overwritten when this request is used. With transfer_function.st2084_pq the given 'max_lum' value is ignored, and 'max_lum' is taken as 'min_lum' + 10000 cd/m². 'min_lum' and 'max_lum' specify the minimum and maximum luminances of the primary color volume as reproduced by the targeted display. 'reference_lum' specifies the luminance of the reference white as reproduced by the targeted display, and reflects the targeted viewing environment. Compositors should make sure that all content is anchored, meaning that an input signal level of 'reference_lum' on one image description and another input signal level of 'reference_lum' on another image description should produce the same output level, even though the 'reference_lum' on both image representations can be different. 'reference_lum' may be higher than 'max_lum'. In that case reaching the reference white output level in image content requires the 'extended_target_volume' feature support. If 'max_lum' or 'reference_lum' are less than or equal to 'min_lum', the protocol error invalid_luminance is raised. The minimum luminance is multiplied by 10000 to get the argument 'min_lum' value and carries precision of 4 decimals. The maximum luminance and reference white luminance values are unscaled. If the primary color volume luminance range and the reference white luminance level have already been set on this object, the protocol error already_set is raised. This request can be used if the compositor advertises wp_color_manager_v1.feature.set_luminances. Otherwise this request raises the protocol error unsupported_feature.
  Arguments: `min_lum` (uint) - minimum luminance (cd/m²) * 10000; `max_lum` (uint) - maximum luminance (cd/m²); `reference_lum` (uint) - reference white luminance (cd/m²)
- `set_mastering_display_primaries`: mastering display primaries as chromaticity coordinates
  Provides the color primaries and white point of the mastering display using CIE 1931 xy chromaticity coordinates. This is compatible with the SMPTE ST 2086 definition of HDR static metadata. The mastering display primaries and mastering display luminances define the target color volume. If mastering display primaries are not explicitly set, the target color volume is assumed to have the same primaries as the primary color volume. The target color volume is defined by all tristimulus values between 0.0 and 1.0 (inclusive) of the color space defined by the given mastering display primaries and white point. The colorimetry is identical between the container color space and the mastering display color space, including that no chromatic adaptation is applied even if the white points differ. The target color volume can exceed the primary color volume to allow for a greater color volume with an existing color space definition (for example scRGB). It can be smaller than the primary color volume to minimize gamut and tone mapping distances for big color spaces (HDR metadata). To make use of the entire target color volume a suitable pixel format has to be chosen (e.g. floating point to exceed the primary color volume, or abusing limited quantization range as with xvYCC). Each coordinate value is multiplied by 1 million to get the argument value to carry precision of 6 decimals. If mastering display primaries have already been set on this object, the protocol error already_set is raised. This request can be used if the compositor advertises wp_color_manager_v1.feature.set_mastering_display_primaries. Otherwise this request raises the protocol error unsupported_feature. The advertisement implies support only for target color volumes fully contained within the primary color volume. If a compositor additionally supports target color volume exceeding the primary color volume, it must advertise wp_color_manager_v1.feature.extended_target_volume. If a client uses target color volume exceeding the primary color volume and the compositor does not support it, the result is implementation defined. Compositors are recommended to detect this case and fail the image description gracefully, but it may as well result in color artifacts.
  Arguments: `r_x` (int) - Red x * 1M; `r_y` (int) - Red y * 1M; `g_x` (int) - Green x * 1M; `g_y` (int) - Green y * 1M; `b_x` (int) - Blue x * 1M; `b_y` (int) - Blue y * 1M; `w_x` (int) - White x * 1M; `w_y` (int) - White y * 1M
- `set_mastering_luminance`: display mastering luminance range
  Sets the luminance range that was used during the content mastering process as the minimum and maximum absolute luminance L. These values include the minimum display emission and ambient flare luminances, assumed to be optically additive and have the chromaticity of the primary color volume white point. This should be compatible with the SMPTE ST 2086 definition of HDR static metadata. The mastering display primaries and mastering display luminances define the target color volume. If mastering luminances are not explicitly set, the target color volume is assumed to have the same min and max luminances as the primary color volume. If max L is less than or equal to min L, the protocol error invalid_luminance is raised. Min L value is multiplied by 10000 to get the argument min_lum value and carry precision of 4 decimals. Max L value is unscaled for max_lum. This request can be used if the compositor advertises wp_color_manager_v1.feature.set_mastering_display_primaries. Otherwise this request raises the protocol error unsupported_feature. The advertisement implies support only for target color volumes fully contained within the primary color volume. If a compositor additionally supports target color volume exceeding the primary color volume, it must advertise wp_color_manager_v1.feature.extended_target_volume. If a client uses target color volume exceeding the primary color volume and the compositor does not support it, the result is implementation defined. Compositors are recommended to detect this case and fail the image description gracefully, but it may as well result in color artifacts.
  Arguments: `min_lum` (uint) - min L (cd/m²) * 10000; `max_lum` (uint) - max L (cd/m²)
- `set_max_cll`: maximum content light level
  Sets the maximum content light level (max_cll) as defined by CTA-861-H. max_cll is undefined by default.
  Arguments: `max_cll` (uint) - Maximum content light level (cd/m²)
- `set_max_fall`: maximum frame-average light level
  Sets the maximum frame-average light level (max_fall) as defined by CTA-861-H. max_fall is undefined by default.
  Arguments: `max_fall` (uint) - Maximum frame-average light level (cd/m²)

### Enums

- `error`: protocol errors

## Interface `wp_image_description_v1` version 3

Colorimetric image description

An image description carries information about the pixel color encoding and its intended display and viewing environment. The image description is attached to a wl_surface via wp_color_management_surface_v1.set_image_description. A compositor can use this information to decode pixel values into colorimetrically meaningful quantities, which allows the compositor to transform the surface contents to become suitable for various displays and viewing environments. Note, that the wp_image_description_v1 object is not ready to be used immediately after creation. The object eventually delivers either the 'ready' or the 'failed' event, specified in all requests creating it. The object is deemed "ready" after receiving the 'ready' event. An object which is not ready is illegal to use, it can only be destroyed. Any other request in this interface shall result in the 'not_ready' protocol error. Attempts to use an object which is not ready through other interfaces shall raise protocol errors defined there. Once created and regardless of how it was created, a wp_image_description_v1 object always refers to one fixed image description. It cannot change after creation.

### Requests

- `destroy`: destroy the image description
  Destroy this object. It is safe to destroy an object which is not ready. Destroying a wp_image_description_v1 object has no side-effects, not even if a wp_color_management_surface_v1.set_image_description has not yet been followed by a wl_surface.commit.
- `get_information`: get information about the image description
  Creates a wp_image_description_info_v1 object which delivers the information that makes up the image description. Not all image description protocol objects allow get_information request. Whether it is allowed or not is defined by the request that created the object. If get_information is not allowed, the protocol error no_information is raised.
  Arguments: `information` (new_id)

### Events

- `failed`: graceful error on creating the image description
  If creating a wp_image_description_v1 object fails for a reason that is not defined as a protocol error, this event is sent. The requests that create image description objects define whether and when this can occur. Only such creation requests can trigger this event. This event cannot be triggered after the image description was successfully formed. Once this event has been sent, the wp_image_description_v1 object will never become ready and it can only be destroyed.
  Arguments: `cause` (uint) - generic reason; `msg` (string) - ad hoc human-readable explanation
- `ready`: the object is ready to be used (32-bit)
  Starting from interface version 2, the 'ready2' event is sent instead of this event. For the definition of this event, see the 'ready2' event. The difference to this event is as follows. The id number is valid only as long as the protocol object is alive. If all protocol objects referring to the same image description record are destroyed, the id number may be recycled for a different image description record.
  Arguments: `identity` (uint) - the 32-bit image description id number
- `ready2` since 2: the object is ready to be used
  Once this event has been sent, the wp_image_description_v1 object is deemed "ready". Ready objects can be used to send requests and can be used through other interfaces. Every ready wp_image_description_v1 protocol object refers to an underlying image description record in the compositor. Multiple protocol objects may end up referring to the same record. Clients may identify these "copies" by comparing their id numbers: if the numbers from two protocol objects are identical, the protocol objects refer to the same image description record. Two different image description records cannot have the same id number simultaneously. The id number does not change during the lifetime of the image description record. Image description id number is not a protocol object id. Zero is reserved as an invalid id number. It shall not be possible for a client to refer to an image description by its id number in protocol. The id numbers might not be portable between Wayland connections. A compositor shall not send an invalid id number. Compositors must not recycle image description id numbers. This identity allows clients to de-duplicate image description records and avoid get_information request if they already have the image description information.
  Arguments: `identity_hi` (uint) - high 32 bits of the 64-bit image description id number; `identity_lo` (uint) - low 32 bits of the 64-bit image description id number

### Enums

- `error`: protocol errors
- `cause`: generic reason for failure

## Interface `wp_image_description_info_v1` version 3

Colorimetric image description information

Sends all matching events describing an image description object exactly once and finally sends the 'done' event. This means - if the image description is parametric, it must send - primaries - named_primaries, if applicable - at least one of tf_power and tf_named, as applicable - luminances - target_primaries - target_luminance - if the image description is parametric, it may send, if applicable, - target_max_cll - target_max_fall - if the image description contains an ICC profile, it must send the icc_file event Once a wp_image_description_info_v1 object has delivered a 'done' event it is automatically destroyed. Every wp_image_description_info_v1 created from the same wp_image_description_v1 shall always return the exact same data.

### Events

- `done`: end of information
  Signals the end of information events and destroys the object.
- `icc_file`: ICC profile matching the image description
  The icc argument provides a file descriptor to the client which may be memory-mapped to provide the ICC profile matching the image description. The fd is read-only, and if mapped then it must be mapped with MAP_PRIVATE by the client. The ICC profile version and other details are determined by the compositor. There is no provision for a client to ask for a specific kind of a profile.
  Arguments: `icc` (fd) - ICC profile file descriptor; `icc_size` (uint) - ICC profile size, in bytes
- `primaries`: primaries as chromaticity coordinates
  Delivers the primary color volume primaries and white point using CIE 1931 xy chromaticity coordinates. Each coordinate value is multiplied by 1 million to get the argument value to carry precision of 6 decimals.
  Arguments: `r_x` (int) - Red x * 1M; `r_y` (int) - Red y * 1M; `g_x` (int) - Green x * 1M; `g_y` (int) - Green y * 1M; `b_x` (int) - Blue x * 1M; `b_y` (int) - Blue y * 1M; `w_x` (int) - White x * 1M; `w_y` (int) - White y * 1M
- `primaries_named`: named primaries
  Delivers the primary color volume primaries and white point using an explicitly enumerated named set.
  Arguments: `primaries` (uint) - named primaries
- `tf_power`: transfer characteristic as a power curve
  The color component transfer characteristic of this image description is a pure power curve. This event provides the exponent of the power function. This curve represents the conversion from electrical to optical pixel or color values. The curve exponent has been multiplied by 10000 to get the argument eexp value to carry the precision of 4 decimals.
  Arguments: `eexp` (uint) - the exponent * 10000
- `tf_named`: named transfer characteristic
  Delivers the transfer characteristic using an explicitly enumerated named function.
  Arguments: `tf` (uint) - named transfer function
- `luminances`: primary color volume luminance range and reference white
  Delivers the primary color volume luminance range and the reference white luminance level. These values include the minimum display emission and ambient flare luminances, assumed to be optically additive and have the chromaticity of the primary color volume white point. The minimum luminance is multiplied by 10000 to get the argument 'min_lum' value and carries precision of 4 decimals. The maximum luminance and reference white luminance values are unscaled.
  Arguments: `min_lum` (uint) - minimum luminance (cd/m²) * 10000; `max_lum` (uint) - maximum luminance (cd/m²); `reference_lum` (uint) - reference white luminance (cd/m²)
- `target_primaries`: target primaries as chromaticity coordinates
  Provides the color primaries and white point of the target color volume using CIE 1931 xy chromaticity coordinates. This is compatible with the SMPTE ST 2086 definition of HDR static metadata for mastering displays. While primary color volume is about how color is encoded, the target color volume is the actually displayable color volume. Each coordinate value is multiplied by 1 million to get the argument value to carry precision of 6 decimals.
  Arguments: `r_x` (int) - Red x * 1M; `r_y` (int) - Red y * 1M; `g_x` (int) - Green x * 1M; `g_y` (int) - Green y * 1M; `b_x` (int) - Blue x * 1M; `b_y` (int) - Blue y * 1M; `w_x` (int) - White x * 1M; `w_y` (int) - White y * 1M
- `target_luminance`: target luminance range
  Provides the luminance range that the image description is targeting as the minimum and maximum absolute luminance L. These values include the minimum display emission and ambient flare luminances, assumed to be optically additive and have the chromaticity of the primary color volume white point. This should be compatible with the SMPTE ST 2086 definition of HDR static metadata. This luminance range is only theoretical and may not correspond to the luminance of light emitted on an actual display. Min L value is multiplied by 10000 to get the argument min_lum value and carry precision of 4 decimals. Max L value is unscaled for max_lum.
  Arguments: `min_lum` (uint) - min L (cd/m²) * 10000; `max_lum` (uint) - max L (cd/m²)
- `target_max_cll`: target maximum content light level
  Provides the targeted max_cll of the image description. max_cll is defined by CTA-861-H. This luminance is only theoretical and may not correspond to the luminance of light emitted on an actual display.
  Arguments: `max_cll` (uint) - Maximum content light-level (cd/m²)
- `target_max_fall`: target maximum frame-average light level
  Provides the targeted max_fall of the image description. max_fall is defined by CTA-861-H. This luminance is only theoretical and may not correspond to the luminance of light emitted on an actual display.
  Arguments: `max_fall` (uint) - Maximum frame-average light level (cd/m²)

## Interface `wp_image_description_reference_v1` version 1

Reference to an image description

This object is a reference to an image description. This interface is frozen at version 1 to allow other protocols to create wp_image_description_v1 objects. The wp_color_manager_v1.get_image_description request can be used to retrieve the underlying image description.

### Requests

- `destroy`: destroy the reference
  Destroy this object. This has no effect on the referenced image description.
