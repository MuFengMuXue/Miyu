## Chapter 23. Dynamic Boost on Linux

## Introduction

The `nvidia-powerd` daemon provides support for the NVIDIA Dynamic Boost feature on Linux platforms. Dynamic Boost is a system-wide power controller which manages GPU and CPU power, according to the workload on the system. By shifting power between the GPU and the CPU, Dynamic Boost can deliver more power to the component that would benefit most from it, without impacting the system's total thermal and electrical budgets. This optimizes overall system performance per watt.

Dynamic Boost will be active when the notebook system is powered by AC or running on battery, provided there is enough load on the GPU. Dynamic Boost is intended to improve performance on balanced as well as heavily GPU-bound or CPU-bound applications. Dynamic Boost requests the CPUFreq Governor to set the CPU frequency by updating the `/sys/devices/system/cpu/cpu*/cpufreq/scaling_max_freq` sysfs entries.

Note: Dynamic Boost will enforce that the total power consumption of the system remains within the total power limit reported by the SBIOS. In some rare cases when running on DC battery, this may result in a performance loss relative to performance with Dynamic Boost disabled, but will help preserve battery life.

## Hardware Requirements

Dynamic Boost is supported only on platforms that meet all of the following requirements:

1.  Notebook form factor.

2.  Ampere or newer GPUs.

3.  Intel CometLake or newer Intel chipsets, or AMD Renoir, Cezanne, Rembrandt, or newer AMD chipsets.

4.  SBIOS support for Dynamic Boost

    Run the following command to check if the SBIOS supports Dynamic Boost:

    **`cat /proc/driver/nvidia/gpus/domain:bus:device.function/power`**

    See [“What is the format of a PCI Bus ID?”](faq.html#busid) for information on how to determine the PCI-BUS-ID.

    Alternatively, use the following command:

    **`nvidia-settings -q DynamicBoostSupport`**

## Software Requirements

The system must fulfill all of the following requirements:

1.  Use the **systemd** init daemon.

2.  Support the **D-Bus** message bus system.

3.  Use the **cpufreq** infrastructure.

## Configuration Steps

Note: The following commands must be run with root permissions

1.  Copy the dbus configuration file `nvidia-dbus.conf` from `/usr/share/doc/NVIDIA_GLX-1.0/` to `/etc/dbus-1/system.d`. If the `/etc/dbus-1/system.d` directory does not exist, create it before copying the file and reboot the system so that dbus can scan the newly created directory in the next boot.

2.  To enable the nvidia-powerd service, causing it to start automatically on boot:

    **`systemctl enable nvidia-powerd.service`**

3.  To start the nvidia-powerd service:

    **`systemctl start nvidia-powerd.service`**

Steps to Stop and disable the nvidia-powerd service:

1.  To stop the service:

    **`systemctl stop nvidia-powerd.service`**

2.  To disable the service such that it does not automatically start on boot:

    **`systemctl disable nvidia-powerd.service`**
