WIM是英文Microsoft Windows Imaging Format(WIM)的简称，它是Windows基于文件的映像格式。 

WIM格式常被用于 Windows 的安装程式中。 

在Linux下，[wimlib](<https://archlinux.org/packages/?name=wimlib>)包可以操作它。 

##  查看信息

可以通过 
    
    $ wiminfo _映像档案_
    
查看 WIM 档案的信息（包括但不限于：名称、索引等）。 

##  挂载

WIM 作为一个映像档案，可通过以下指令挂载 

###  只读挂载
    
    # wimmount _映像档案_ _索引_ _目录_
    
###  挂载为可读写
    
    # winmountrw  _映像档案_ _索引_ _目录_
    
###  卸载
    
    # wimunmount _目录_ --commit
    
来应用可读写挂载中的更改。 

**警告：** 如果没有参数 --commit ，将不会应用更改。

##  目录结构

要查看 WIM 映像的目录结构，使用： 
    
    # wimdir _映像档案_ _索引_
    
##  应用映像

使用： 
    
    # wimapply _映像档案_ _索引_ _目标目录_
    
来应用映像， 

##  压缩

一般制作启动盘都需要格式化为 fat32 文件，windows.iso 大于 4GiB 以至于无法拷贝到 fat32 文件系统，你需要压缩 install.wim 才能完成这项操作。 
    
    # wimlib-imagex optimize install.wim --solid
    