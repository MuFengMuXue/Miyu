[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Gapless Audio CD Creation from MP3s](<../zh-cn/Talk:Gapless_Audio_CD_Creation_from_MP3s.html>)讨论)

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 内容已经脱节（在 [Talk:Gapless Audio CD Creation from MP3s#](<../zh-cn/Talk:Gapless_Audio_CD_Creation_from_MP3s.html>) 中讨论）

##  安装

我们将要用到一些程序。 
    
    pacman -S lame cdrdao
    
把cdrdao配置成为我们的CD刻录机。打开 `/etc/cdrdao.conf` (以root用户),加入刻录设备，格式如下： 
    
    write_device: "/dev/hdc"
    
检查看看cdrdao是否有正确的组权限，否则可能不能正常工作。 
    
    ls -l /usr/bin/cdrdao
    
输出的信息与以下类似： 
    
    -rwxr-xr-x 1 root optical 569040 2006-10-27 05:56 /usr/bin/cdrdao
    
如果不是，你可能要改变cdrdao属主chown为以下组： 
    
    # chown root:optical /usr/bin/cdrdao
    
##  将MP3解码

首先将所有你要刻录到CD的歌曲复制到一个文件夹。最好将他们按音轨顺序重命名(比如01.mp3, 02.mp3,等等). 现在我们将把全部MP3解码为未压缩的wav文件。请记住整张专辑可能解码超过800MB的wav文件，需要花费些时间。 
    
    mkdir wav
    for file in *.mp3 ; do
       lame --decode "$file" "wav/$file.wav"
    done
    
##  创建一个目录文件表格

完成后，让我们创建一个目录文件表格来描述CD规划。 
    
    cd wav
    {
      echo "CD_DA"
      for file in *.wav ; do
        echo "TRACK AUDIO"
        # echo "PREGAP 00:02:00"  # insert a 2-second silent gap before each track
        echo "FILE \"$file\" 0"
      done
    } > toc
    
##  刻录

最后我们只要做的就是刻录了。 
    
    cdrdao write toc
    