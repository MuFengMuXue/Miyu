这篇文章描述了如何利用CUE文件的元数据来分割音频文件。 

##  安装

需要 [shntool](<https://aur.archlinux.org/packages/shntool/>)AUR 以分割音频文件。 对于ISO内的CD镜像或其它原始数据则需要 [bchunk](<https://archlinux.org/packages/?name=bchunk>)包 。 

原生支持WAV格式的输入与输出。对于其它格式则需要对应的编解码器如 [flac](<https://archlinux.org/packages/?name=flac>)包，[mac](<https://archlinux.org/packages/?name=mac>)包 或 [wavpack](<https://archlinux.org/packages/?name=wavpack>)包。 

标记音频文件则需要其它软件 [cuetools](<https://archlinux.org/packages/?name=cuetools>)包，[mp3info](<https://archlinux.org/packages/?name=mp3info>)包 或 [vorbis-tools](<https://archlinux.org/packages/?name=vorbis-tools>)包。 

##  分割

使用 _shnsplit_ 命令分割 _.wav_ 文件： 
    
    $ shnsplit -f file.cue file.wav
    
使用 _bchunk_ 命令分割 _.bin_ 文件并转换为 _.wav_ 格式: 
    
    $ bchunk -v -w file.bin file.cue out
    
输出文件名可利用 `-t` 进行格式化 (`%p` 艺术家, `%a` 专辑, `%t` 标题, 以及 `%n` 轨数): 
    
    $ shnsplit -f file.cue -t "%n %t" file.wav
    
_shnsplit_ 支持许多无损格式（参见 `shntool(1)`）。 以 _.flac_ 格式为例： 
    
    $ shnsplit -f file.cue -o flac file.flac
    
输出格式，包括编码器，可用 `-o` 命令指定 (参见 `shntool(1)`): 
    
    $ shnsplit -f file.cue -o "flac flac -s -8 -o %f -" file.flac
    
可用 `shntool -a` 命令查看 _shntool_ 原生支持的格式和编码器。如果没有原生支持，可以手动指定。例如输出ogg格式： 
    
    $ shnsplit -f file.cue -o "cust ext=ogg oggenc -b 192 -o %f -" file.ape
    
##  标记

需要 [cuetools](<https://archlinux.org/packages/?name=cuetools>)包 来运行 _cuetag.sh_ 。 

可以用以下命令复制 _.cue_ 的元数据至 _.mp3_ 文件。 
    
    $ cuetag.sh file.cue *.mp3
    
或指定某些文件: 
    
    $ cuetag.sh file.cue track01.mp3 track02.mp3 track03.mp3 track04.mp3
    
_cuetag.sh_ 支持 _.mp3_ 文件的 id3 标签和 _.ogg_ 和 _.flac_ 文件的 vorbis 标签。 

##  替代

  * 自动分割并标记 _.flac_ 文件的脚本：[https://bbs.archlinux.org/viewtopic.php?id=75774。](<https://bbs.archlinux.org/viewtopic.php?id=75774%E3%80%82>)
  * [flacon](<https://aur.archlinux.org/packages/flacon/>)AUR 或 [flacon-git](<https://aur.archlinux.org/packages/flacon-git/>)AUR 是基于Qt框架，有图形界面的分割重编码软件。它们还具有 CUE 文件的自动字符集检测功能。
  * 对于有损格式，[mp3splt-gtk](<https://archlinux.org/packages/?name=mp3splt-gtk>)包 或 [mp3splt](<https://archlinux.org/packages/?name=mp3splt>)包 可用于直接切割mp3文件以避免重编码带来的音质下降。

## References

  * [What is APE?](<https://en.wikipedia.org/wiki/Monkey%27s_Audio> "wikipedia:Monkey's Audio")
  * [What is CUE?](<https://en.wikipedia.org/wiki/Cue_file> "wikipedia:Cue file")
  * [Rip Audio CDs](</wzh/index.php?title=Rip_Audio_CDs&action=edit&redlink=1> "Rip Audio CDs（页面不存在）")
