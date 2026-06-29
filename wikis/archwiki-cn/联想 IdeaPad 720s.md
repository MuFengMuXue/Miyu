[Lenovo IdeaPad 720s](<https://www3.lenovo.com/de/de/laptops/ideapad/700-series/Ideapad-720S-13-Intel/p/88IP70S0893#tab-techspec>)笔记本有一块13.3"的屏幕, 7代或者8代的 Intel i5/i7 处理器, 摄像头, 麦克风, 音频I/O, 带有蓝牙4.1的802.11ac无线网卡, 一个USB Type-C接口 (支持DP,PD和雷电), 一个USB Type-C接口(PD+USB 3.0), 两个USB3接口和指纹识别器。 

##  硬件支持

唯一不支持的硬件是指纹识别器(see remarks for USB ID 06cb:0081 at [Validity90 on GitHub](<https://github.com/nmikhailov/Validity90>))。 

### UEFI Bios

在安装前，在BIO中关闭安全启动。可以通过按右手边的一键恢复按钮或者是在启动过程中按`F2`来进入BIOS。可以按`F12`进入BOOT 菜单。 

###  电池保护模式

联想笔记本电脑配备了一个名为“电池保护模式”的电池控制器设置，将通常的负载阈值从95/100%切换到55/60%，以减少电池损耗。要启用此功能，请安装[acpi_call](<https://archlinux.org/packages/?name=acpi_call>)包包。该模式通过以下方式启用： 
    
    # echo '\_SB.PCI0.LPCB.EC0.VPC0.SBMC 3' | tee /proc/acpi/call
    
通过以下方式禁用： 
    
    # echo '\_SB.PCI0.LPCB.EC0.VPC0.SBMC 5' | tee /proc/acpi/call
    