**翻译状态：**

  * 本文（或部分内容）译自 [Xc3sprog](<https://wiki.archlinux.org/title/Xc3sprog> "arch:Xc3sprog")，最近一次同步于 2020-05-04，若英文版本有所[更改](<https://wiki.archlinux.org/title/Xc3sprog?diff=0&oldid=610389>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Xc3sprog_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[xc3sprog](<http://xc3sprog.sourceforge.net/>) 是一套实用程序套件，用于使用 Xilinx 并行电缆和其他 JTAG 适配器对 Xilinx FPGA，CPLD 和 EEPROM 进行编程 

##  安装

从 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [xc3sprog-svn](<https://aur.archlinux.org/packages/xc3sprog-svn/>)AUR 包。 

##  设备

### Xilinx USB JTAG

最初有 `USBID=03fd:000f`，经过适当的初始化后变成 `03fd:0008`。 

  * 从 AUR 安装 [fxload](<https://aur.archlinux.org/packages/fxload/>)AUR。
  * 从 [Xilinx ISE](</wzh/index.php?title=Xilinx_ISE_WebPACK&action=edit&redlink=1> "Xilinx ISE WebPACK（页面不存在）") 提取 xusb_xlp.hex
  * 创建 `/etc/udev/rules.d/99-xilinx.rules` 文件

     SUBSYSTEM=="usb", ACTION=="add", ATTR{idVendor}=="03fd", ATTR{idProduct}=="000f", RUN+="/usr/bin/fxload -v -t fx2 -I /path/to/xusb_xlp.hex -D $tempnode"
    
  * 使用 `udevadm control --reload` 重新加载 udev 规则并重新插入 JTAG
  * 测试连接使用 `xc3sprog -c xpc -j`
