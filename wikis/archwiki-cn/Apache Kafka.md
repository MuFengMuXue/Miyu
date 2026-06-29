**翻译状态：**

  * 本文（或部分内容）译自 [Apache Kafka](<https://wiki.archlinux.org/title/Apache_Kafka> "arch:Apache Kafka")，最近一次同步于 2020-06-19，若英文版本有所[更改](<https://wiki.archlinux.org/title/Apache_Kafka?diff=0&oldid=621039>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Apache_Kafka_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Apache Kafka](<https://kafka.apache.org>) 是一个分布式流平台，可以： 

  1. 使您可以发布和订阅记录流。在这方面，它类似于消​​息队列或企业消息传递系统。
  2. 使您可以以容错的方式存储记录流。
  3. 使您可以在记录流出现时对其进行处理。

##  安装

安装 [kafka](<https://archlinux.org/packages/?name=kafka>)包。 

使用 systemctl 启动 `kafka.service`，它也应该自动[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")/[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `zookeeper@kafka.service`。 

##  用法

有关用法，请参阅[官方文档](<https://kafka.apache.org/quickstart#quickstart_createtopic>)

##  客户端

  * C - [librdkafka-git](<https://aur.archlinux.org/packages/librdkafka-git/>)AUR
  * Python - <https://github.com/dpkp/kafka-python>
  * Php - [php-rdkafka](<https://aur.archlinux.org/packages/php-rdkafka/>)AUR
  * Perl - [perl6-pkafka](<https://aur.archlinux.org/packages/perl6-pkafka/>)AUR
