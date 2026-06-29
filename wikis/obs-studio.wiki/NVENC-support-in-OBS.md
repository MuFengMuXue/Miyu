* [NVIDIA GPUs without NVENC Support](#NVIDIA-GPUs-without-NVENC-support)
  * [Turing (TU117)](#turing-tu117)
  * [Pascal (GP108/GP108B)](#pascal)
  * [Maxwell (GM108)](#maxwell-gm108)
  * [Older generations](#older-generations)

****

Some GPUs from the Kepler generation and most GPUs from the Maxwell generation onwards support NVENC. This covers most GPUs manufactured 2012 onwards, starting with select entries GeForce 600 series and the majority of the GeForce 700 series.

If your GPU's name starts with GTX or RTX, it more than likely supports NEVNC.

In each generation, there were many exceptions that do *not* support NVENC. These are mostly mobile and low-end GPUs. Please check the listing below. If your card does not support NVENC, you may need to use another hardware encoder (such as Intel Quick Sync) or use a software encoder, normally x264.

## NVIDIA GPUs without NVENC Support

### Turing (TU117)

- Consumer
  - GeForce MX450
- Professional
  - NVIDIA T500 Mobile

### Pascal

#### GP108

- Consumer
  - GeForce GT 1030
  - GeForce MX150
  - GeForce MX230
  - GeForce MX250
- Professional
  - Quadro P500 Mobile
  - Quadro P520

#### GP108B

- GeForce MX250

### Maxwell (GM108)

- Consumer
  - GeForce 830M
  - GeForce 840M
  - GeForce 845M
    - GM107 revision supports NVENC
    - GM108 revision does **not** support NVENC
  - GeForce 920MX
  - GeForce 930M
  - GeForce 930MX
  - GeForce 940M
  - GeForce 940MX
  - GeForce 945M
  - GeForce MX110
  - GeForce MX130
- Professional
  - Quadro K620M
  - Quadro M500M
  - Quadro M520 Mobile

### Older generations

- GeForce GTX 550 Ti (Fermi 2.0)
- GeForce GT 705 (Fermi)
- GeForce GT 730
  - Fermi (GF108) revision supports NVENC
  - Older Kepler (GK208) revision does **not** support NVENC

----

### TechPowerUp GPU Database

- [https://www.techpowerup.com/gpu-specs/-gm108.g761](https://www.techpowerup.com/gpu-specs/-gm108.g761)
- [https://www.techpowerup.com/gpu-specs/-gp108.g808](https://www.techpowerup.com/gpu-specs/-gp108.g808)
- [https://www.techpowerup.com/gpu-specs/-gp108b.g887](https://www.techpowerup.com/gpu-specs/-gp108b.g887)

### Nvidia Developer Site Outlining encode/decode support including NVENC

- [https://developer.nvidia.com/video-encode-decode-support-matrix](https://developer.nvidia.com/video-encode-decode-support-matrix)