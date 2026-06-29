DirectDraw is the part of DirectX which handles displaying graphics on
the screen.

In the Wine context, when one speaks about DDraw, one speaks about all
the 2D APIs (DirectX 1 to DirectX 7) but also all the 'old' 3D APIs
(Direct3D1 to Direct3D7). This is to prevent confusion with Direct3D8
and Direct3D9 which, while keeping the same name, are a completely
different set of APIs.

## DirectDraw Versions and Interfaces

The DirectDraw interface numbers don't totally match up to the version
of DirectX they were introduced:

- DX 1 brings *IDirectDraw* and *IDirectDrawSurface*
- DX 2 *IDirectDraw2* and *IDirectDrawSurface2*
- DX 3 adds *IDirectDrawSurface3*, *IDirect3D*, and *IDirect3DDevice*
  (*IDirectDraw3* is an IE specific interface that lives in ddrawex.dll)
- DX 4 adds *IDirect3D2* and *IDirect3DDevice2*
- DX 6 adds *IDirectDraw4*, *IDirectDrawSurface4*, *IDirect3D3* and
  *IDirect3DDevice3*
- DX 7 adds *IDirectDraw7*, *IDirectDrawSurface7*, *IDirect3D7* and
  *IDirect3DDevice7*
