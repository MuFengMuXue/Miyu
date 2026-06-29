# Bug lists
* [Regressions](https://bugs.winehq.org/buglist.cgi?bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&component=directx-d3d&component=d2d&component=directx-d3dx9&component=directx-d3dx10&component=dwrite&keywords=regression&columnlist=bug_id,cf_regression_sha1sum,short_desc,bug_status,resolution&order=bug_id%20DESC)
* [Valgrind](https://bugs.winehq.org/buglist.cgi?bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&component=directx-d3d&component=d2d&component=directx-d3dx9&component=directx-d3dx10&component=dwrite&keywords=valgrind&columnlist=bug_id,short_desc,bug_status,resolution&order=bug_id%20DESC)
* [D3D + download](https://bugs.winehq.org/buglist.cgi?bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&component=directx-d3d&keywords=download&columnlist=bug_id,short_desc,bug_status,resolution&order=bug_id%20DESC)
* [D2D + download](https://bugs.winehq.org/buglist.cgi?bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&component=d2d&keywords=download&columnlist=bug_id,short_desc,bug_status,resolution&order=bug_id%20DESC)
* [D3DX + download](https://bugs.winehq.org/buglist.cgi?bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&component=directx-d3d-util&keywords=download&columnlist=bug_id,short_desc,bug_status,resolution&order=bug_id%20DESC)
* [DWrite + download](https://bugs.winehq.org/buglist.cgi?bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&component=dwrite&keywords=download&columnlist=bug_id,short_desc,bug_status,resolution&order=bug_id%20DESC)

# Todo

## vkd3d

On the WineHQ wiki here: https://wiki.winehq.org/Vkd3d-todo

## Direct3D

* Finish the Vulkan renderer for d3d < 10. This is a bit of a cumbersome task to name so it's sometimes called "Himavant" after Elizabeth's branch for this.
  * Implement sm1-specific instructions in vkd3d-shader: ~bem,~ breakc, breakp, call/label, callnz, cnd, crs, ~dp2add,~ dst, expp, if (b#), lit, logp, ~loop/endloop, lrp, m*x*, nrm, phase, pow, rep/endrep,~ setp, sgn, ~tex, texcoord, texld (1.4), texcrd, texdepth,~ texdp3, texdp3tex, texm*, ~texreg*.~
  * Implement sm1-specific other instruction features in vkd3d-shader: predicate, shift (x2 etc), ~1.4 projection (dw/dz), relative addressing,~ BIAS, SIGN, NOT, ~1.1-1.3 t# temps, vPos,~ vFace
  * ~Implement an interface for remaining "extra" states in vkd3d-shader: bump mapping constants (for bem, texbem), 1.x texture type, projection~
  * Hook up remaining "extra" states: fog, bump mapping constants, ~1.x texture type,~ projection
  * Implement legacy formats: B8G8R8, B2G3R3, B4G4R4X4, R8G8B8X8, B10G10R10A2, P8, L8, L8A8, L4A4, R5G5_L6, R8G8_L8X8, D16_LOCKABLE, X8D24, L16, S8_UINT_D24_FLOAT, NV12 (opaque ver), YV12, UYVY, YUY2, MULTI2_ARGB8, G8R8_G8B8, R8G8_B8G8, ATI1N, ATI2N, INTZ, NULL
  * ~Implement missing TSS_TCI_* support in the HLSL shader backend.~
  * Blit features: ~format conversion, scaling,~ colour keys, alpha test
  * ~Set the necessary feature flags; we're missing a lot of them~
  * d3d9 SRGB texture location
* Windowless wined3d.
  * Ddraw has some code for this to handle rendering to the desktop / full screen. This should be moved to wined3d.
  * D3d10+ needs this. You can render before even setting up a swapchain. Currently it creates a "frontbuffer-only" implicit swapchain.
* Maintain the card / driver info database in a separate file or the registry. We'd like to be able to update the card database without recompiling wined3d. This means the format should be somewhat stable though. How do we want to distribute updates for this?
* Most format capabilities are just recorded in the flags field of the wined3d_format structure now. Exceptions to this are CheckSurfaceCapability(), CheckDepthStencilCapability() and CheckRenderTargetCapability(). These should go away.
* DirectDraw should get its pixel format information from wined3d. We could for example ask wined3d for a format matching a set of masks.
* D3d9 and earlier handle multiplies with zero in shaders differently than OpenGL and d3d10+. In d3d9 and earlier anything multiplied by zero results in zero, including floating point specials like INF or NaN. OpenGL allows hardware to e.g. return NaN for 0 * +INF. We'd need an extension to request a specific behaviour from OpenGL. It looks like EXT_zero_mul_conventions never went anywhere, but we could perhaps get a similar extension into Mesa instead.
* Cleanup the tests.
  * There are a number of tests in d3d9 that have no corresponding d3d8 or ddraw test, but don't require d3d9 specific features.
  * Move the existing ddraw tests over to the new ddraw1/2/4/7 setup.
  * We still have a number of test failures on the testbot.
* Ddraw flips need to be able to be vsync'ed. We can do this by blitting to the (real) backbuffer first and then doing a present instead of blitting directly from the shadow frontbuffer to the real frontbuffer.
* The way P8 textures (ddraw) are implemented is less than optimal. Stefan did some work on this, the basic idea is to keep surfaces as P8, including the ddraw frontbuffer, until they're blitted to the screen or uploaded to a texture.
* Review locking for ddraw, dxgi and d3d11. Dxgi mostly doesn't do locking at all, ddraw is probably broken.
* Wined3d locking could probably be more fine-grained. For example, (D3D) state updates typically don't need to wait for resource updates at all and draws only need to wait for resources used by that draw. This has interactions with the command thread above.
* We really shouldn't screw around with the window styles when switching to fullscreen. We have tests to prove this, and e.g. [https://bugs.winehq.org/show_bug.cgi?id=29301 WineHQ 29301] is caused by this. Creating a GL context on the window DC works, but can still only draw to the client rect (see test_window_dc() in dlls/opengl32/tests/opengl.c). Is there some way to *really* create a GL context on the window DC, perhaps by calling the OpenGL ICD directly? It probably wouldn't be terribly hard to add some special calls to winex11 to create a GL context on the whole window, but that would break the Win32 build of wined3d. How is this supposed to work in native D3D, are there DDI interfaces for this? Or does the d3d client library just tell the driver to draw to the entire screen? But in that case, is e.g. WS_CLIPCHILDREN supposed to work in fullscreen?
* We should add a Wine specific GL extension to winex11.drv, essentially the successor to WGL_WINE_pixel_format_passthrough. The purpose would be to allow wined3d to properly co-exist with OpenGL applications. See [https://bugs.winehq.org/show_bug.cgi?id=28869 WineHQ 28869] and [https://bugs.winehq.org/show_bug.cgi?id=29934 WineHQ 29934] for some of the issues involved. We'd need a function to create a "wined3d" WGL context and the equivalent of context_enter() / context_release(). There may be a role for switching a context to fullscreen / exclusive mode.
* We should add support for ARB_separate_shader_objects, and try to compile shaders with reasonable defaults in advance to reduce stutter on first use.

## Direct2D
* d2d_geometry_intersect_self() is pretty slow.
* Cubic beziers are currently approximated by quadratic ones. This has acceptable results for things like font glyphs since those are mostly elevated quadratics or something close, but doesn't work so well for real cubics.
* Drawing arcs is unimplemented.
* Layers are unimplemented.
* Anti-aliasing is unimplemented.
* Gradient brushes are unimplemented.
