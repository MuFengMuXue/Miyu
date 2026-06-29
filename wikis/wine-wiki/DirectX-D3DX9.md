# D3DX utility library

[Relevant MSDN
section](https://msdn.microsoft.com/en-us/library/windows/desktop/bb172965%28v=vs.85%29.aspx),
although unfortunately MSDN URLs tend to break over time.

## A Brief Overview

The D3DX utility library is a legacy module containing a motley
collection of high-level functions and interfaces that might be
generally useful for graphics programming. A peculiar characteristic of
D3DX is that it doesn't follow the common Win32 API pattern of
maintaining backwards compatibility: there are multiple versions of e.g.
d3dx9, each with a different filename and that differ in exported
functionality or otherwise visible behavior. For reference, for d3dx9
that's d3dx9_24.dll to d3dx9_43.dll. Applications generally hardcode a
specific D3DX library name, which means that they could potentially end
up depending on quirks or caveats of the particular D3DX version in use.

In order to reduce source code duplication, the current implementation
of d3dx9_xx DLLs in Wine uses the PARENTSRC build mechanism with all the
code being stored in dlls/d3dx9_36/. That's currently (Wine 3.0) not the
case for d3dx10 and d3dx11 DLLs, which still use the old forward
mechanism. d3dx10_43 and d3dx11_43 are the DLLs with the implementation
for d3dx10 and d3dx11 respectively.

As of 3.0, Wine's implementation of the d3dx9 API includes:

- most math functions
- ID3DXSprite interface
- partial ID3DXFont interface (currently missing text drawing)
- most surface and texture functions
- some mesh functions
- most of the effect framework

d3dx10 and d3dx11 are still stubs for the most part.

Also note that the shader assembler and compiler functions currently
"forward" to d3dcompiler_43.dll, which is the "modern" API for these
features.

## Games for Testing

Here is a table of games that rely on d3dx9, along with which module
they primarily (?) depend on:

| Title                               | d3dx9_?? |
|-------------------------------------|----------|
| FEAR                                | 25       |
| Black & White 2                     | 25       |
| Universal Combat                    | 25       |
| Civilization IV                     | 26       |
| Just Cause                          | 26       |
| Dreamfall: The Longest Journey 2    | 27       |
| Oblivion                            | 27       |
| Sid Meier's Railroads               | 28       |
| Warlords Battlecry III              | 28       |
| Settlers 2: The Next Generation     | 29       |
| Caesar IV                           | 29       |
| Command and Conquer 3               | 29       |
| Need for Speed Carbon               | 30       |
| The Sims: Pet Stories (others too?) | 30       |
| Entropia Universe                   | 30       |
| Lego Star Wars II                   | 30       |
| EverQuest                           | 30       |
| Avencast: Rise of the Mage          | 30       |
| Transformers                        | 31       |
| Touhou 10                           | 31       |
| Tabula Rasa                         | 33       |
| Lost Planet                         | 33       |
| Need For Speed: Pro Street          | 34       |
| Lego Indiana Jones                  | 35       |
| Lego Island                         | 35       |
| Chessmaster 11                      | 35       |
| The Witcher                         | 35       |
| Medieval 2: Total War               | 36       |
| Rainbow Six Vegas                   | 36       |
| Age of Empires III                  | 36       |
| Fable: The Lost Chapters            | 36       |
| TrackMania Nations Forever          | 36       |
| Europa Universalis Rome             | 36       |
| Age of Conan                        | 36       |
| Overlord                            | 36       |
| Guitar Hero 3                       | 36       |
| PatchCon                            | 36?      |
| Resident Evil 4                     | 36?      |
| Flatout 2                           | 36?      |
| Battlefield 2                       | 36?      |
| Psychonauts                         | 36?      |
| Crysis                              | 36?      |
| Titan Quest                         | 36?      |
| IrrEdit                             | 36?      |

## See Also

- [DirectDraw](DirectDraw)
- [DirectPlay Games](DirectPlay-Games)
