# Hybrid Gpus: NVIDIA Optimus And AMD Dynamic Switchable Graphics

On system with hybrid graphic cards (using NVIDIA Optimus/Prime and AMD Dynamic Switchable Graphics), some games may fail to detect the dedicated graphics card and use the integrated GPU incorrectly on Linux.

## DirectX games

When running a DirectX game, DXVK is used and it can [already automatically detect](https://github.com/doitsujin/dxvk/blob/master/src/dxvk/dxvk_instance.cpp#L322) the correct GPU to use. There's no need to change any setting in Heroic (the setting in the `Other` tab to force the use of these GPUs must be turned OFF).

## OpenGL and Vulkan games

OpenGL and Vulkan cannot reliably detect the correct GPU to use, and in these cases it is important to configure Heroic to force the use of the dedicated GPU.

## How to enable

A configuration can be found in the game's setting dialog > `Other` tab > "Force use of NVIDIA Optimus or AMD Dynamic Switchable Graphics GPU".
