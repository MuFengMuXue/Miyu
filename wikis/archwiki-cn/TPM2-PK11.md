[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:TPM2-PK11](<../zh-cn/Talk:TPM2-PK11.html>)讨论)

**翻译状态：**

  * 本文（或部分内容）译自 [TPM2-PK11](<https://wiki.archlinux.org/title/TPM2-PK11> "arch:TPM2-PK11")，最近一次同步于 2020-05-20，若英文版本有所[更改](<https://wiki.archlinux.org/title/TPM2-PK11?diff=0&oldid=614501>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/TPM2-PK11_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[tpm2-pk11-git](<https://aur.archlinux.org/packages/tpm2-pk11-git/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] 为 [TPM](<../zh-cn/%E5%8F%AF%E4%BF%A1%E5%B9%B3%E5%8F%B0%E6%A8%A1%E5%9D%97.html> "TPM") 芯片提供了 [PKCS#11](<https://github.com/irtimmer/tpm2-pk11>) 后端。这可以用来保护您的 [SSH 密钥](<../zh-cn/SSH_keys.html> "SSH keys")。 

**注意：** 截至 2017 年 11 月，仅支持 OpenSSH 客户端。

##  SSH 用法

创建密钥： 
    
    $ mkdir ~/.tpm2 && cd ~/.tpm2
    $ tpm2_createprimary -A e -g 0x000b -G 0x0001 -C po.ctx
    $ tpm2_create -c po.ctx -g 0x000b -G 0x0001 -o key.pub -O key.priv
    $ tpm2_load -c po.ctx -u key.pub -r key.priv -n key.name -C obj.ctx
    $ tpm2_evictcontrol -A o -c obj.ctx -S 0x81010010
    $ rm key.name *.ctx
    
创建配置文件并为您的设置进行更改： 
    
    $ cp config.sample ~/.tpm2/config
    
提取公钥： 
    
    $ ssh-keygen -D libtpm2-pk11.so
    
使用您的 TPM 密钥： 
    
    $ ssh -I libtpm2-pk11.so ssh.example.com
    
或在 `~/.ssh/config` 中将 PKCS#11 模块添加到您的 ssh 配置中： 
    
    Host *
        PKCS11Provider libtpm2-pk11.so
    