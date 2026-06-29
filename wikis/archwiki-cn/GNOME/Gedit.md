[gedit](<https://en.wikipedia.org/wiki/gedit> "wikipedia:gedit")是GNOME的通用文本编辑器。 

##  安装

[安装](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")[gedit](<https://archlinux.org/packages/?name=gedit>)包软件包。 

若要使用额外功能，请安装[gedit-plugins](<https://archlinux.org/packages/?name=gedit-plugins>)包软件包。 

Gedit有许多拼写检查词典可供使用，见[Language checking](<../../zh-cn/Language_checking.html> "Language checking")。 

##  配置

###  不在新的一行结束文档

若想确保gedit不会在新的一行结束文档，请执行以下操作： 
    
    $ gsettings set org.gnome.gedit.preferences.editor ensure-trailing-newline false
    
###  为编辑过的文件保存备份

若有需要，gedit可以为编辑过的文件创建备份副本，副本的名称和内容将与编辑前的原始文件的内容相同，但名称后面添加了“~”后缀。例如文件`file1`的副本名称为`file1~`。备份文件默认隐藏。 

若要开启此功能，请访问gedit的首选项（GNOME Shell用户可以在gedit的全局菜单中找到）。在首选项中点击“编辑器”标签栏，勾选“在保存前创建备份文件”选项。 

##  另见

  * [Apps/Gedit - GNOME Wiki!](<https://wiki.gnome.org/Apps/Gedit>)
