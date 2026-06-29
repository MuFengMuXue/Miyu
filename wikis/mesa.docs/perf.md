# Performance Tips

## Intel GPUs

1. Keep the system updated with the latest kernel and Mesa versions.
1. Ensure SoC firmware is up-to-date. These firmware updates currently
   require installing the Windows graphics driver; firmware updates
   via `fwupd` are in progress.
1. Use Wayland where possible, as it supports additional modifiers for
   better performance.
1. For MTL and newer integrated GPUs, disable VT-d if virtualization is
   not needed.
1. For discrete GPUs:

1. Enable ReBAR
1. For workloads that keep the GPU busy (e.g. 3D videogames), 
      minimize idle power consumption by enabling ASPM powersave mode.
1. For "bursty", latency-sensitive workloads (e.g. AI inference),
      enable ASPM performance mode.
1. Enable the 'performance' cpufreq governor.
