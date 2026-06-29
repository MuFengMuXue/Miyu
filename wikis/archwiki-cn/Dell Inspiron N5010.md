[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Dell Inspiron N5010](<../zh-cn/Talk:Dell_Inspiron_N5010.html>)讨论)

##  简介

本文是写给使用使用戴尔灵越N5010计算机用户的Arch Linux配置指南 

###  概要

### To do

  * eSata test
  * HDMI test
  * Force acpi/cpufreq to work (somehow :))
  * Need someone with wikimedia syntax skills to guide me formating this wiki page, please :).

## Hardware

### Working

#### Ethernet

Realtek Semiconductor Co., Ltd. RTL8101E/RTL8102E PCI Express Fast Ethernet controller (rev 02) Works out of the box. 

#### DVDRW

ATAPI: TSSTcorp DVD+/-RW TS-L633J, D200, max UDMA/100 

CD-ROM TSSTcorp DVD+-RW TS-L633J D200 PQ: 0 ANSI: 5 

Using driver: scsi3-mmc 

Supported extensions: 

24x/24x writer dvd-ram cd/rw xa/form2 cdda tray 

Successfully burns both cd mediums and dvd mediums, tested using K3B 2.0.2-1. 

####  触摸板

如果使用Gnome桌面环境那么可以直接使用快捷键来控制触摸板的锁定与开启 

未安装Gnome桌面环境的用户控制触摸板需要使用synaptic驱动。 

需要安装软件包xf86-input-synaptics. 

详细信息可以查看[Touchpad Synaptics (简体中文)](</wzh/index.php?title=Touchpad_Synaptics_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "Touchpad Synaptics \(简体中文\)（页面不存在）")

Todo: Needs tweaking, cause it is too anoying. 

Use this script to disable the touch pad when you do not like it: 
    
    #!/bin/bash
    
    if [ $(synclient -l | grep TouchpadOff | gawk -F '= ' '{ print $2 }') -eq 0 ]; then
        synclient TouchpadOff=1
    else
        synclient TouchpadOff=0
    fi
    
#### Wireless

Broadcom Corporation BCM4313 802.11b/g/n Wireless LAN Controller (rev 01) In kernel 2.6 it works out of the box, but in kernel 3.0 there is no wlan0, we have to blacklist some modules. 

So open "/etc/modprobe.d/modprobe.conf" and append the following line: 

blacklist bcma 

now, reboot or restart the kernel. 

When we issue iwconfig, it should now list wlan0: 
    
    lo        no wireless extensions.
    
    eth0      no wireless extensions.
    
    wlan0     IEEE 802.11bgn  ESSID:"*******"  
              Mode:Managed  Frequency:2.427 GHz  Access Point: XX:XX:XX:XX:XX:XX   
              Bit Rate=72.2 Mb/s   Tx-Power=19 dBm   
              Retry  long limit:7   RTS thr:off   Fragment thr:off
              Power Management:off
              Link Quality=70/70  Signal level=-32 dBm  
              Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
              Tx excessive retries:0  Invalid misc:968   Missed beacon:0
    
#### Bluetooth

详情查看[Bluetooth (简体中文)](</wzh/index.php?title=Bluetooth_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "Bluetooth \(简体中文\)（页面不存在）")

Both pairing, sending files and receiving files works out of the box, tested with blueman. 

#### VGA

Tested on an external CRT monitor, works out of the box on KDE 4.7. 

#### Graphic adapter

ATI Mobility Radeon HD 5600 working out of the box. 

#### Audio

Intel Corporation 5 Series/3400 Series Chipset High Definition Audio 

#### Display

Available sizes: 
    
    1366x768       60.0*+
    1280x720       59.9  
    1152x768       59.8  
    1024x768       59.9  
    800x600        59.9  
    848x480        59.7  
    720x480        59.7  
    640x480        59.4
    
Brightness controls work out of the box. 

####  Suspending to disk (Hibernation)

works out of the box - tested on KDE 4.7 

####  Suspending to ram (Sleep)

works out of the box - tested on KDE 4.7 

#### Sensors

使用lm_sensors软件可以监控计算机各设备的温度，详情查看[Lm_sensors (简体中文)](</wzh/index.php?title=Lm_sensors_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "Lm sensors \(简体中文\)（页面不存在）") 目前只能监测到三个设备的温度: 

  * radeon-pci-0100（显卡）
  * acpitz-virtual-0
  * acpi termal zone 0 Temperature

They work out of the box. 如果想监测硬盘温度可以使用[[hddtemp 

### Partially Working

### Not Working

#### Processor frequency control

  * says unsupported I think:

    :: Setting cpufreq governing rules                                                                                     [BUSY]
    grep: /sys/devices/system/cpu/cpu* /cpufreq/scaling_available_governors: No such file or directory, cpu 0 wrong, unknown or unhandled CPU?
    Error setting new values. Common errors:
    - Do you have proper administration rights? (super-user?)
    - Is the governor you requested available and modprobed?
    - Trying to set an invalid policy?
    - Trying to set a specific frequency, but userspace governor is not available,
      for example because of hardware which cannot be set to a specific frequency
      or because the userspace governor is not loaded?
                                              1wrong, unknown or unhandled CPU?
    Error setting new values. Common errors:
    - Do you have proper administration rights? (super-user?)
    - Is the governor you requested available and modprobed?
    - Trying to set an invalid policy?
    - Trying to set a specific frequency, but userspace governor is not available,
       for example because of hardware which cannot be set to a specific frequency
       or because the userspace governor is not loaded?
                                                2wrong, unknown or unhandled CPU?
    Error setting new values. Common errors:
    - Do you have proper administration rights? (super-user?)
    - Is the governor you requested available and modprobed?
    - Trying to set an invalid policy?
    - Trying to set a specific frequency, but userspace governor is not available,
       for example because of hardware which cannot be set to a specific frequency
       or because the userspace governor is not loaded?
                                                  3wrong, unknown or unhandled CPU?
    Error setting new values. Common errors:
    - Do you have proper administration rights? (super-user?)
    - Is the governor you requested available and modprobed?
    - Trying to set an invalid policy?
    - Trying to set a specific frequency, but userspace governor is not available,
       for example because of hardware which cannot be set to a specific frequency
       or because the userspace governor is not loaded?
                                                                                                                          [DONE]
    
###  Unknown / Untested

#### HDMI Video

#### Redwood HDMI Audio 5600

#### eSata port

## Installation

Normal installation with no issues to report. 

### Kernel

### ATI Mobility Raedon 5600

To do: Synaptic guide 

### Troubleshoot

  * On boot the following error is printed:

boot error message: 

intel ips 0000:00:1f.6: failed to get i915 symbols, graphics turbo disabled 

Workaround: 

Blacklist the intel_ips module, open configuration file "/etc/modprobe.d/modprobe.conf" and add: 

blacklist intel_ips 

## Links

### General

  * [Arch Linux bug report](<https://bugs.archlinux.org/task/25439>)
  * [Ubuntu bug report](<https://bugs.launchpad.net/ubuntu/+source/linux/+bug/651104>)
