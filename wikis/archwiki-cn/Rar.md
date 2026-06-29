[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Rar](<../zh-cn/Talk:Rar.html>)讨论)

RAR (and UNRAR) is the Linux port of the commandline-only version of [WinRAR](<https://www.rarlab.com/download.htm>) available in both the i686 and x86-64 flavors. 

##  主要特点

  * Variable amounts of redundancy ("recovery record" or "recovery volumes" both of which are demonstrated below) can be added to an archive, making it more resistant to corruption. Even if parts of an archive are damaged, it is possible to fully recover the stored data if a large enough recovery record exists. On its own, [Tar](<../zh-cn/%E5%BD%92%E6%A1%A3%E4%B8%8E%E5%8E%8B%E7%BC%A9.html> "Tar") does not have this ability.
  * RAR is able to efficiently handle split volumes. Built-in support for multi-volume files enables the unpacking program to simply prompt the user for the next .partXXX RAR file, without the need to manually copy and then rejoin the pieces, or for extracting a file from a single piece without needing all pieces. RAR does not support tapes, as it uses seek and rename operations on its files.
  * RAR archives can be of a solid format, in which all of the compressed files are treated as a single data block. Most currently used compression formats (with the exception of the older ZIP) allow solid structuring.
  * Strong encryption capabilities. Older versions of the file format used a proprietary algorithm; newer versions use the AES encryption algorithm, a block cipher adopted as an encryption standard by the U.S. government. The only known ways to recover an encrypted file are via dictionary or brute force attacks. In newer versions, password protection can optionally protect filenames too, so that the filenames contained within the archive will not be displayed without the right password.

##  安装

### RAR

可以通过 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 来安装 [rar](<https://aur.archlinux.org/packages/rar/>)AUR（除 UNRAR 外的所有功能）。 

### UNRAR

[官方仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方仓库")单独提供了 [unrar](<https://archlinux.org/packages/?name=unrar>)包 ，可以像平常一样通过 [pacman](<../zh-cn/Pacman.html> "Pacman") 来安装。 

##  配置文件

Linux 版的 RAR 从 `~/.rarrc` （即用户的 home 目录下）读取配置信息，又或者可以在 /etc 目录下，定义一个全局配置文件，供所有用户使用。 

这个文件的语法如下： 
    
    switches=any RAR switches, separated by spaces
    
举个例子： 
    
    switches=-m5 -rr5 -ol -msjpg;mp3;avi;zip;rar;tar;gz;jpg
    
要想获得关于 RAR 选项的完整清单及详细解释，可以访问[用户手册](<https://ss64.com/bash/rar.html>)。 

##  RAR 压缩例子

###  基本语法
    
    $ rar _command_ -_switch 1_ -_switch N_ _archive_ _files.rar_ _@listfiles..._
    
要想获得完整的命令及选项，请参阅本文的最后一部分，或者运行 `rar` 。 

### Recursively compress an entire directory structure

  * Task: backup `/home/darkhorse` to `/media/data/darkhorse-backup.rar` using 10 % recovery records:

    $ rar a -r -rr10 /media/data/darkhorse-backup.rar /home/darkhorse
    
  * Explained:

Switch | Action   
---|---  
a |  **a** dds files to archives.   
-r |  **r** ecurse subdirectories (includes all dirs/files under the parent directory).   
-rr10 | adds **r** ecovery **r** ecords to the archive. This way up to 10% of the compressed archive can become corrupt or unusable, and it will be able to recover the data through parity.   
  
### Mixed-mode archives

You can also use mixed-mode archives which means that file types you specifiy do not get compressed - they simply get stored. 

  * Task: backup `/home/darkhorse` to `/media/data/darkhorse-backup.rar`:

    $ rar a -r -rr10 -s -m5 -msjpg;mp3;tar /media/data/darkhorse-backup.rar /home/darkhorse
    
  * Explained:

Switch | Action   
---|---  
a |  **a** dds files to archives.   
-r |  **r** ecurse subdirectories (includes all dirs/files under the parent directory).   
-rr10 | adds **r** ecovery **r** ecords to the archive. This way up to 10% of the compressed archive can become corrupt or unusable, and it will be able to recover the data through parity.   
-m5 | Use the highest level of compression (m0 = store ... m3 = default ... m5 = maximal level of compression.   
-msjpg;mp3;tar | ignore the compression option and store all .jpg and .mp3 and .tar files.   
  
### Recursively compress many directory structures using a list

  * Task: backup `/home/darkhorse` and `/home/palomino` and `/home/seabiscuit` to `/media/data/homes-backup.rar`.

First create a list (simple text file) containing the various targets. In this example, the list will be three lines long. I named it 'home-list' in this example but you can call it anything you want: 
    
    /home/darkhorse
    /home/palomino
    /home/seabiscuit
    
    $ rar a -r -rr10 -s /media/data/homes-backup.rar @/path/to/home-list
    
##  UNRAR 例子

###  基本语法
    
    $ unrar _command_ -_switch 1_ -_switch N_ _archive_ _files..._ _@listfiles..._ _path_to_extract\_
    
想了解完整的命令及选项，只需运行： 
    
    $ unrar --help
    
解压到一个新的目录： 
    
    $ unrar x /media/data/homes-backup.rar homes-backup/
    
运行以下命令，来解压分卷压缩文件： 
    
    $ unrar x homes-backup.part1.rar homes-backup/
    