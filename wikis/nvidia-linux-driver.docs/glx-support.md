## Appendix D. GLX Support

This release supports GLX 1.4.

Additionally, the following GLX extensions are supported on appropriate GPUs:

- GLX_EXT_visual_info

- GLX_EXT_visual_rating

- GLX_SGIX_fbconfig

- GLX_SGIX_pbuffer

- GLX_ARB_get_proc_address

- GLX_SGI_video_sync

- GLX_SGI_swap_control

- GLX_ARB_multisample

- GLX_NV_float_buffer

- GLX_ARB_fbconfig_float

- GLX_NV_swap_group

- GLX_NV_video_out

- GLX_EXT_texture_from_pixmap

- GLX_NV_copy_image

- GLX_ARB_create_context

- GLX_EXT_import_context

- GLX_EXT_fbconfig_packed_float

- GLX_EXT_framebuffer_sRGB

- GLX_NV_present_video

- GLX_NV_multisample_coverage

- GLX_EXT_swap_control

- GLX_NV_video_capture

- GLX_ARB_create_context_profile

- GLX_EXT_create_context_es_profile

- GLX_EXT_create_context_es2_profile

- GLX_EXT_swap_control_tear

- GLX_EXT_buffer_age

- GLX_ARB_create_context_robustness

- GLX_ARB_context_flush_control

- GLX_ARB_create_context_no_error

- GLX_EXT_libglvnd

- GLX_EXT_stereo_tree

- GLX_NV_copy_buffer

- GLX_NV_delay_before_swap

- GLX_NV_robustness_video_memory_purge

- GLX_NV_multigpu_context

For a description of these extensions, see the OpenGL extension registry at http://www.opengl.org/registry/

Some of the above extensions exist as part of core GLX 1.4 functionality, however, they are also exported as extensions for backwards compatibility.

Unofficial GLX protocol support exists in NVIDIA's GLX client and GLX server implementations for the following OpenGL extensions:

- GL_ARB_geometry_shader4

- GL_ARB_shader_objects

- GL_ARB_texture_buffer_object

- GL_ARB_vertex_buffer_object

- GL_ARB_vertex_shader

- GL_EXT_bindable_uniform

- GL_EXT_compiled_vertex_array

- GL_EXT_geometry_shader4

- GL_EXT_gpu_shader4

- GL_EXT_texture_buffer_object

- GL_NV_geometry_program4

- GL_NV_vertex_program

- GL_NV_parameter_buffer_object

- GL_NV_vertex_program4

Until the GLX protocol for these OpenGL extensions is finalized, using these extensions through GLX indirect rendering will require the AllowUnofficialGLXProtocol X configuration option, and the \_\_GL_ALLOW_UNOFFICIAL_PROTOCOL environment variable in the environment of the client application. Unofficial protocol requires the use of NVIDIA GLX libraries on both the client and the server. Note: GLX protocol is used when an OpenGL application indirect renders (i.e., runs on one computer, but submits protocol requests such that the rendering is performed on another computer). The above OpenGL extensions are fully supported when doing direct rendering.

GLX visuals and FBConfigs are only available for X screens with depths 16, 24, or 30.
