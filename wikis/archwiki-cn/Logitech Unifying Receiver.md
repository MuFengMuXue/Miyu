[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Logitech Unifying Receiver](<../zh-cn/Talk:Logitech_Unifying_Receiver.html>)讨论)

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本条目或段落需要进行[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")。**

**注记:** 请提供模板的第一个位置参数以more detailed indications。 ([讨论](<../zh-cn/Talk:Logitech_Unifying_Receiver.html>))

[罗技 Unifying 接收器](<https://www.logitech.com/zh-tw/resource-center/what-is-unifying.html>)是无线设备的接收器，可同时连接最多六个兼容鼠标及键盘。 和该接收器一组的输入设备已预先配对，并能即插即用。而针对额外的输入设备，罗技仅提供 Windows 软件以供配对。 不过 [Benjamin Tissoires](<https://groups.google.com/g/linux.kernel/c/zYS6yddI8yU>) 在 kernel mailing list 发表了一支程序，令 Linux 下也有其功能。 

##  编译 unifying_pair

此程序亦可于 [AUR](<https://github.com/aur-archive/pairingtool>) 找到。 

首先确定系统已安装了 C 编译器。 
    
    # pacman -S gcc 
    
将下列代码复制到文件并命名，假设名为 _unifying_pair.c_ 。 
    
    /*
    * Copyright 2011 Benjamin Tissoires 
    *
    * This program is free software: you can redistribute it and/or modify
    * it under the terms of the GNU General Public License as published by
    * the Free Software Foundation, either version 3 of the License, or
    * (at your option) any later version.
    *
    * This program is distributed in the hope that it will be useful,
    * but WITHOUT ANY WARRANTY; without even the implied warranty of
    * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    * GNU General Public License for more details.
    *
    * You should have received a copy of the GNU General Public License
    * along with this program.  If not, see .
    */
    
    #include <linux/input.h>
    #include <linux/hidraw.h>
    #include <sys/ioctl.h>
    #include <fcntl.h>
    #include <unistd.h>
    #include <stdio.h>
    #include <errno.h>
    
    #define USB_VENDOR_ID_LOGITECH                  (__u32)0x046d
    #define USB_DEVICE_ID_UNIFYING_RECEIVER         (__s16)0xc52b
    #define USB_DEVICE_ID_UNIFYING_RECEIVER_2       (__s16)0xc532
    
    int main(int argc, char **argv)
    {
           int fd;
           int res;
           struct hidraw_devinfo info;
           char magic_sequence[] = {0x10, 0xFF, 0x80, 0xB2, 0x01, 0x00, 0x00};
    
           if (argc == 1) {
                   errno = EINVAL;
                   perror("No hidraw device given");
                   return 1;
           }
    
           /* Open the Device with non-blocking reads. */
           fd = open(argv[1], O_RDWR|O_NONBLOCK);
    
           if (fd < 0) {
                   perror("Unable to open device");
                   return 1;
           }
    
           /* Get Raw Info */
           res = ioctl(fd, HIDIOCGRAWINFO, &info);
           if (res < 0) {
                   perror("error while getting info from device");
           } else {
                   if (info.bustype != BUS_USB ||
                       info.vendor != USB_VENDOR_ID_LOGITECH ||
                       (info.product != USB_DEVICE_ID_UNIFYING_RECEIVER &&
                        info.product != USB_DEVICE_ID_UNIFYING_RECEIVER_2)) {
                           errno = EPERM;
                           perror("The given device is not a Logitech "
                                   "Unifying Receiver");
                           return 1;
                   }
           }
    
           /* Send the magic sequence to the Device */
           res = write(fd, magic_sequence, sizeof(magic_sequence));
           if (res < 0) {
                   printf("Error: %d\n", errno);
                   perror("write");
           } else if (res == sizeof(magic_sequence)) {
                   printf("The receiver is ready to pair a new device.\n"
                   "Switch your device on to pair it.\n");
           } else {
                   errno = ENOMEM;
                   printf("write: %d were written instead of %ld.\n", res,
                           sizeof(magic_sequence));
                   perror("write");
           }
           close(fd);
           return 0;
    }
    
将源代码编译成可执行档 _unifying_pair_ ： 
    
    $ gcc -o unifying_pair unifying_pair.c
    
##  兼容设备配对

下一步需要查找接收器设备的位置，因此观察下列命令的输出 
    
    $ cat /sys/class/hidraw/hidraw**X** /device/uevent |grep NAME
    
(你必须把 **X** 替换成系统上存在的整数) 直到找到 _Logitech USB Receiver_ 为止(在此假设 X 恰为 **0**) 
    
    $ cat /sys/class/hidraw/hidraw0/device/uevent |grep NAME
      HID_NAME=Logitech USB Receiver
    
如果想要配对的设备现在是开着时，关掉并执行适才编译过的程序，以合适的设备做为其参数： 
    
    # ./unifying_pair /dev/hidraw0
    
若顺利该程序会告知你打开欲配对的设备，且该设备应该也会正常运作。 

## Known Problems

### Keyboard Layout via xorg.conf

With kernel 3.2 the Unifying Receiver got its own kernel module _hid_logitech_dj_ which does not work flawlessly together with keyboard layout setting set via [xorg.conf](<../zh-cn/Xorg.html#Keyboard_settings> "Xorg"). A temporary workaround is to use [xorg-setxkbmap](<https://archlinux.org/packages/?name=xorg-setxkbmap>)包 and set the layout manually. For example for a German layout with no deadkeys one has to execute: 
    
    $ setxkbmap -layout de -variant nodeadkeys
    
To automate this process one could add this line to [xinitrc](<../zh-cn/Xinit.html#xinitrc> "Xinitrc"). 
