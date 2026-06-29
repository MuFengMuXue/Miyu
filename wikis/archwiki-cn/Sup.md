[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Sup](<../zh-cn/Talk:Sup.html>)讨论)

[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** Last updated in 2015, out of sync with English page（在 [Talk:Sup#](<../zh-cn/Talk:Sup.html>) 中讨论）

**Sup** 是一套为了拥有大量邮件用户所开发，崭新且强大的邮件客户端程序。您可以将它想成 Mutt 和 Gmail 的混合体，拥有非常快速地操作和搜索，标签，自动通讯录管理，支持大量账号，以及更多功能。 

##  安装

从 [AUR](<../zh-cn/AUR_\(%E6%AD%A3%E9%AB%94%E4%B8%AD%E6%96%87\).html> "AUR \(繁体中文\)") 安装 [sup-git](<https://aur.archlinux.org/packages/sup-git/>)AUR。 不过开发团队建议您用以下方式安装： 
    
    $ gem install sup
    
好让您直接从开发团队那儿获取最新版本。 

##  设置

Sup 附带一款名为 `sup-config` 的简便设置工具。要使用它，请在终端内执行它然后完成下面列出的几项步骤： 

  1. 输入您的全名。
  2. 输入您的主要电子邮件信箱，以及任何额外的电子邮件信箱。
  3. 输入您签名档的位置，如果您拥有的话。
  4. 输入您要用来撰写新邮件的编辑器，以及任何您该传入的参数。
  5. 新增您邮件的来源，包括： 
     1. mbox 文件
     2. maildir 文件夹

支持远程来源 (POP3, IMAP, IMAPS, 和 mbox + ssh) 的功能已经在 0.12 版发布时移除。 

Sup 目前专注于 MUA (mail user agent) 之功能且不自行处理下载邮件的工作。您可以使用像是 offlineimap, fetchmail, 和 rsync 等工具来将电子邮件发送到本机系统的 mbox 或 maildir 文件夹。 

[sup wiki 内的示范](<https://github.com/sup-heliotrope/sup/wiki/Complete-gmail-configuration>)简介了如何使用 offlineimap 设置 gmail+imap 来源。[Mutt#设置POP方式接收电邮](<../zh-cn/Mutt_\(%E6%AD%A3%E9%AB%94%E4%B8%AD%E6%96%87\).html#%E8%A8%AD%E7%BD%AEPOP%E6%96%B9%E5%BC%8F%E6%8E%A5%E6%94%B6%E9%9B%BB%E9%83%B5> "Mutt \(繁体中文\)")子章节介绍一些额外的邮件发送方法。 

在新增好电子邮件来源后，`sup-config` 会执行 `sup-sync` 指令来导入邮件到您的信箱内。 

##  使用

执行 `sup` 指令来开启 Sup 邮件客户端程序。该程序应该会显示由 `sup-config` 导入的消息。 

对新用户来说最该记得的按键就是 `?` 按键。在任何时间点它都会显示所有的键盘指令，提示新用户该如何导览程序。 

使用箭头键或是 `j` 和 `k` 键巡览讨论串 (`Shift+j` 和 `Shift+k` 的功能如同 Page Up 和 Page Down 键)。按下 Tab 键，则能在有新消息的讨论串中快速穿梭。Sup 默认并不会读入所有讨论串；按下 `Shift+m` 将读取更多讨论串 (更多消息将被自动读取直到视窗被填满)。 

选择欲查看的讨论串然后按下 `Enter` 键即可查看它。在查看讨论串时，如果想要展开或折叠某一消息，请选择该消息然后按下 `Enter` 键。按下 `Shift+n` 将只展开新消息 (同默认画面) 或 `Shift+e` 切换所有消息的状态。按下 `o` 将显示或隐藏部分消息内容 (像是签名档)。 

按下 `n` 和 `p` 键巡览讨论串内的消息。按下 `h` 键显示消息的标头。 

按下 `b` 键循环切换缓冲，或者按下 `;` 键查看已开启缓冲的清单。按下 `x` 键抹杀某个缓冲。 

按下 `a` 键封存讨论串。这会将该讨论串从 inbox 内隐藏直到其他人回复它，到时候它就会重新出现。按下 `&` 键抹杀讨论串。这等同于 Gmail 中的 "静音" 功能，即使有人回复该讨论串它依然会被隐藏。该讨论串将永远不会出现在 inbox 内，不过依然能在搜索结果找到它。 

按下 `*` 键替讨论串标记星号。按下 `Shift+s` 键将讨论串标记为垃圾消息。Sup 并没有任何内置的垃圾消息分类器；要做到这个功能，可以考虑像是 [spamassassin](<https://archlinux.org/packages/?name=spamassassin>)包 之类的程序。 

按下 `t` 键标记讨论串。按下 `l` 键替讨论串内的消息加上标签。按下 `Shift+l` 键搜索标签。输入欲搜索的标签后按下 `Enter` 键或是直接按下 `Enter` 键来列出所有标签。按下 `\` 键将执行全文字搜索。 

按下 `Shift+c` 键来查看联系人清单。要对清单中的人寄送电子邮件，选择他或她的姓名然后按下 `Enter` 键。 

##  备份和撤销

备份电子邮件非常重要。为了保证您不会弄丢任何东西，第一要先备份来源，像是 mbox 文件和 maildir 目录，然后执行： 
    
    $ sup-dump > _檔案名稱_
    
这将会备份所有消息状态到文本文件内。要从文本文件内撤销您的消息状态，只要执行： 
    
    $ sup-sync [<來源>+] --restored --restore _檔案名稱_
    
谨记，上面的指令只会备份和撤销消息状态。消息本身需要另行备份。 

##  按键绑定列表

###  inbox-mode 下的按键绑定
    
    a：封存討論串 (從 inbox 中移除)
    A：封存討論串 (從 inbox 中移除) 且標記爲已讀
    
###  thread-index-mode 下的按键绑定
    
       M：再讀取 20 份討論串
      !!：讀取所有討論串 (可能會列出很多討論串)
      ^G：取消目前的搜尋
       @：刷新畫面    
       *：標記星號/取消星號整個討論串內的訊息
       N：切換討論串內所有訊息的未讀/已讀狀態
       l：編輯或新增討論串的標籤
       e：編輯訊息 (僅可對草稿使用)
       S：標記/取消標記討論串爲垃圾郵件
       d：刪除/取消刪除討論串
       &：抹殺討論串 (再也不會出現在 inbox)
       $：馬上儲存變更
     tab：跳到下一個新討論串
       r：回覆討論串內最新的訊息
       f：轉寄討論串內最新的訊息
       t：標記/取消標記所選的討論串
       T：標記/取消標記所有的討論串
       g：標記符合的討論串
    +, =：套用下一個操作到所有已標記的討論串
       #：強制所有已標記的討論串合併成一個討論串
       u：重做上一個操作
    
###  thread-view-mode 下的按键绑定
    
          h：切換詳細標頭
          H：顯示完整訊息標頭
          V：顯示完整訊息 (原生格式)
    <enter>：開啓/摺疊或啓動項目
          E：開啓/摺疊所有訊息
          e：編輯草稿
          y：寄出草稿
          l：替討論串編輯或新增標籤
          o：開啓/摺疊訊息中所有的引用
          n：跳到下一個開啓的訊息
          p：跳到前一個開啓的訊息
          z：對齊目前訊息在緩衝中的位置
          *：替訊息標記星號/取消標記星號
          N：切換訊息的未讀/已讀狀態
          r：恢復一個訊息
          f：轉寄訊息或附件
          i：編輯某人的別名/暱稱
          D：將訊息視爲新郵件來編輯
          s：儲存訊息/附件到磁碟
          S：從特定人士搜尋訊息
          m：編寫訊息給某人
          (：訂閱/取消訂閱郵件清單
          )：訂閱/取消訂閱郵件清單
          |：將訊息或附件重導給 shell 指令
         .a：封存該討論串然後抹殺緩衝
         .d：刪除該討論串然後抹殺緩衝
         .s：標記該討論串爲垃圾訊息然後抹殺緩衝
         .N：標記該討論串爲未讀然後抹殺緩衝
         ,a：封存該討論串，抹殺緩衝，然後檢視下一個
         ,d：刪除該討論串，抹殺緩衝，然後檢視下一個
         ,s：標記該討論串爲垃圾訊息，抹殺緩衝，然後檢視下一個
         ,N：標記該討論串爲未讀，抹殺緩衝，然後檢視下一個
         ,n：抹殺緩衝，然後檢視下一個
         ]a：封存該討論串，抹殺緩衝，然後檢視前一個
         ]d：刪除該討論串，抹殺緩衝，然後檢視前一個
         ]s：標記該討論串爲垃圾訊息，抹殺緩衝，然後檢視前一個
         ]N：標記該討論串爲未讀，抹殺緩衝，然後檢視前一個
         ]n：抹殺緩衝，然後檢視前一個
    
###  contact-list-mode 下的按键绑定
    
       M：再讀取 10 個聯絡人
       D：放棄通訊錄然後重新讀取
    a, i：編輯聯絡人的代稱或是姓名
       t：標記/取消標機該行
       +：套用下一個操作到所有已標記的項目
       S：從特定人士開始搜尋訊息
    
###  line-cursor-mode 下的按键绑定
    
    <down arrow>, j：將遊標向下移動一行
      <up arrow>, k：將遊標向上移動一行
            <enter>：選擇該項目
    
###  scroll-mode 下的按键绑定
    
                            J, ^E：向下一行
                            K, ^Y：向上一行
                  <left arrow>, h：向左一排
                    <right arrow>：向右一排
         <page down>, <space>, ^F：向下一頁
    <page up>, p, <backspace>, ^B：向上一頁
                               ^D：向下半頁
                               ^U：向上半頁
                     <home>, ^, 1：跳到頁首
                         <end>, 0：跳到頁尾
                                [：跳到左邊
                                /：在目前的緩衝內搜尋
                                n：跳到下個緩衝內搜尋到的項目
    
###  全局按键绑定
    
       q：離開 Sup，但是需要確認
       Q：直接離開 Sup
       ?：顯示幫助
       b：切換到下一個緩衝
       B：切換到前一個緩衝
       x：抹殺目前的緩衝
       ;：列出所有緩衝
       C：列出通訊錄
      ^L：重繪畫面
    \, F：搜尋所有訊息
       U：顯示所有未讀訊息
       L：列出標籤
       P：輪查有無新訊息
    m, c：撰寫新訊息
      ^G：什麼也不做
       R：編輯最近的訊息草稿
    
##  疑难解答

###  因为 Illegal instruction (core dumped) 而当掉

`sup` 使用一套名为 [Xapian](<https://xapian.org/>) 的搜索引擎，且它被编译为使用 SSE2 指令集。如果您的 CPU 不支持 SSE2 指令集，您将碰上错误消息： 
    
       Illegal instruction (core dumped)
    
要解决这问题，您必须在编译 Xapian 时加入 `--disable-sse` 选项。 

1\. 查看 [ruby-xapian-ruby](<https://aur.archlinux.org/packages/ruby-xapian-ruby/>)AUR 的 `PKGBUILD` 您可以得知它从 <https://rubygems.org/gems/xapian-ruby> 下载了一份 gem。下载那份 gem。 

2\. 执行这些指令 
    
       gem unpack xapian-ruby.gem
       gem unpack --spec xapian-ruby.gem
       mv xapian-ruby.gemspec xapian-ruby/
       cd xapian-ruby
    
3\. 您需要编辑 `Rakefile`。您的目标是修改两行有执行设置参数的指令。您所要做的就是将 `--disable-sse` 加到这些设置指令后面： 
    
       system! "./configure --prefix=#{prefix} --exec-prefix=#{prefix} --disable-sse"
       system! "./configure --prefix=#{prefix} --exec-prefix=#{prefix} --with-ruby --disable-sse"
    
然后存储所做的修改。 

4\. 执行 
    
       gem build xapian-ruby.gemspec
       gem install --local xapian-ruby.gem
    
这样应该能解决旧歀 CPU 不能执行 Xapian 的问题。附带一提，如果您第一次执行 `sup-config` 且正确地完成所有设置，却依然得到下列错误消息 
    
       This Sup version expects a v4 index, but you have an existing v0 index. Please run sup-dump to save your labels, move /home/user/.sup/xapian out of the way, and run sup-sync --restore. (RuntimeError)
       Rats, that failed. You may have to do it manually.
    
那么您可能也碰上了该问题，尝试执行其他如 `sup` 或 `sup-dump` 等可执行文件，看看有无显示 Illegal instruction (core dumped) 的错误消息。 

##  另请参阅

  * [网站](<http://supmua.org/>)
  * [Wiki](<https://github.com/sup-heliotrope/sup/wiki>)
  * [README](<https://github.com/sup-heliotrope/sup/blob/develop/README.md>)
  * [FAQ](<https://github.com/sup-heliotrope/sup/blob/develop/doc/FAQ.txt>)
  * [哲学阐述](<https://github.com/sup-heliotrope/sup/blob/develop/doc/Philosophy.txt>)
