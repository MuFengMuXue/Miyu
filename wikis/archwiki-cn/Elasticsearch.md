**翻译状态：**

  * 本文（或部分内容）译自 [Elasticsearch](<https://wiki.archlinux.org/title/Elasticsearch> "arch:Elasticsearch")，最近一次同步于 2024-04-04，若英文版本有所[更改](<https://wiki.archlinux.org/title/Elasticsearch?diff=0&oldid=805270>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Elasticsearch_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

摘自[维基百科](<https://zh.wikipedia.org/wiki/Elasticsearch> "zhwp:Elasticsearch"): 

     [Elasticsearch](<https://www.elastic.co/products/elasticsearch>) 是一个基于 [Lucene](<https://lucene.apache.org/>) 库的搜索引擎。它提供了一个分布式、支持多租户的全文搜索引擎，具有 HTTP web 接口和无模式 JSON 文档。Elasticsearch 是用 Java 开发的，以 Apache 许可证开源。

##  安装

Elasticsearch 依赖于 [jre-openjdk-headless](<https://archlinux.org/packages/?name=jre-openjdk-headless>)包，详细信息请参考 [Java](<../zh-cn/Java.html> "Java")。 

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [elasticsearch](<https://aur.archlinux.org/packages/elasticsearch/>)AUR。 

##  运行

如果你在 `/usr/share/elasticsearch/config/elasticsearch.keystore` 位置下还没有密钥库，需要在启动 Elasticsearch 前先创建一个： 
    
    # elasticsearch-keystore create
    
之后就可以[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `elasticsearch.service`。 

使用 [curl](<https://archlinux.org/packages/?name=curl>)包 来确保 Elasticsearch 正在运行且可被访问，用法为 `curl '<protocol>://<host>:<port>'`： 
    
    curl <http://127.0.0.1:9200>
    
    {
      "name" : "Sunder",
      "cluster_name" : "elasticsearch",
      "cluster_uuid" : "*cluster-uuid*",
      "version" : {
        "number" : "2.4.1",
        "build_hash" : "c67dc32e24162035d18d6fe1e952c4cbcbe79d16",
        "build_timestamp" : "2016-09-27T18:57:55Z",
        "build_snapshot" : false,
        "lucene_version" : "5.5.2"
      },
      "tagline" : "You Know, for Search"
    }
    
##  配置

Elasticsearch 的主配置文件位于 `/etc/elasticsearch/elasticsearch.yml` 位置下，有着完善的说明文档。 

  * 默认情况下 Elasticsearch 可被公开访问，建议仅允许本机访问：

    network.host: 127.0.0.1
    
  * 可以自定义其它端口，而不是使用默认的 `9200` 端口：

    http.port: 9200
    
**警告：** elasticsearch.service 可能会因内存不足而被中断：“A process of this unit has been killed by the OOM killer.”

你可以修改默认初始及最大可用内存量 [[1]](<https://www.elastic.co/guide/en/elasticsearch/reference/current/heap-size.html>)： 
    
    /etc/elasticsearch/jvm.options.d/.options
    
    # Xms represents the initial size of total heap space
    # Xmx represents the maximum size of total heap space
    
    -Xms2g # e.g. 256m, 512m, 1g, 2g, ..
    -Xmx2g # e.g. 256m, 512m, 1g, 2g, ..
    
如果你碰到了 Linux 内存不足报错，可以将其从 4g 修改到 2g。 

你可能会需要更新系统 [vm.max_map_count](<https://www.elastic.co/guide/en/elasticsearch/reference/5.2/vm-max-map-count.html>) 限制： 
    
    # sysctl -w vm.max_map_count=262144
    
**注意：** 安装 [elasticsearch](<https://aur.archlinux.org/packages/elasticsearch/>)AUR 后就已通过 `/usr/lib/sysctl.d/elasticsearch.conf` 提高了 `vm.max_map_count` 大小。

##  用法

Elasticsearch 使用了 REST API，更多信息请参考 [Wikipedia:RESTful API](<https://en.wikipedia.org/wiki/RESTful_API> "wikipedia:RESTful API")。 

[Elasticsearch 向导](<https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html>)中的[快速指引](<https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html>)一节中提供了基础和详细的用法。 

Elasticsearch 服务器管理任务（文档管理，执行搜索等）通常是通过[客户端](<https://www.elastic.co/guide/en/elasticsearch/client/index.html>)来完成的，应能和你喜欢的编程语言无缝结合。 

你也可以使用 [ElasticHQ](<http://www.elastichq.org>)，[Elasticsearch GUI](<https://github.com/jettro/elasticsearch-gui>)，[Kibana](<https://www.elastic.co/products/kibana>) 和 [Adminer](<../zh-cn/Adminer.html> "Adminer") 等工具简化 ElasticSearch 实例和集群的管理。 

##  基础安全功能

Elasticsearch 从 8.0 开始会默认启用及配置安全功能。 

Elasticsearch 提供了一系列[文档](<https://www.elastic.co/guide/en/elasticsearch/reference/8.1/security-basic-setup.html>)来帮助配置强制基础安全特性。 
