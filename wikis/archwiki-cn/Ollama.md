相关文章

  * [General-purpose computing on graphics processing units](</wzh/index.php?title=General-purpose_computing_on_graphics_processing_units&action=edit&redlink=1> "General-purpose computing on graphics processing units（页面不存在）")
  * [llama.cpp](</wzh/index.php?title=Llama.cpp&action=edit&redlink=1> "Llama.cpp（页面不存在）")
  * [Vulkan](<../zh-cn/Vulkan.html> "Vulkan")

**翻译状态：**

  * 本文（或部分内容）译自 [Ollama](<https://wiki.archlinux.org/title/Ollama> "arch:Ollama")，最近一次同步于 2026-02-11，若英文版本有所[更改](<https://wiki.archlinux.org/title/Ollama?diff=0&oldid=863883>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Ollama_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Ollama](<https://ollama.com>) 可以让用户在离线情况下，使用本地版大语言模型。 

##  安装并运行第一个大模型

  * 使用 CPU 运行模型: 
    * [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [ollama](<https://archlinux.org/packages/?name=ollama>)包
  * 联合显卡运行模型: 
    * 使用 [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA") 显卡，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [ollama-cuda](<https://archlinux.org/packages/?name=ollama-cuda>)包
    * 使用 [AMD](<../zh-cn/AMDGPU.html> "AMDGPU") 显卡，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [ollama-rocm](<https://archlinux.org/packages/?name=ollama-rocm>)包
    * 使用 [Vulkan](<../zh-cn/Vulkan.html> "Vulkan") ，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [ollama-vulkan](<https://archlinux.org/packages/?name=ollama-vulkan>)包 （[实验性](<https://docs.ollama.com/gpu#vulkan-gpu-support>)）

完成上述安装后，[启用/启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用/启动") `ollama.service` 。然后验证 Ollama 是否成功启动： 
    
    $ ollama --version
    
如果输出提示 `Warning: could not connect to a running Ollama instance` ，则 Ollama 服务没有成功启动；否则， Ollama 服务启动成功并且进入 Ollama 程序的命令行界面，等待用户输入命令。 

然后，运行第一个本地离线大模型。下面的例子将会下载并运行最新的 [DeepSeek-R1 蒸馏模型 1.5b 参数版](<https://ollama.com/library/deepseek-r1:1.5b>)。出现 `Send a message (/? for help)` 即可输入文字，向大模型提问。 
    
    $ ollama run deepseek-r1:1.5b
    
    >>> Send a message (/? for help)
    
##  常用命令

Ollama 命令行工具没有类似 `ollama search` 的命令用来搜索具体的模型，需要查询 Ollama 是否支持某个模型，请使用 Ollama 官网的[搜索功能](<https://ollama.com/search>)。 

运行模型： 
    
    $ ollama run _模型名称_
    
停止模型： 
    
    $ ollama stop _模型名称_
    
更新模型： 
    
    $ ollama pull _模型名称_
    
删除模型： 
    
    $ ollama rm _模型名称_
    
查看本地可用模型：
    
    ollama list
    
##  可能出现的问题

###  当使用 AMD 的集成显卡， ROCm 程序没有成功调用显卡

在运行 Ollama 会话，并通过类似 [amdgpu_top](<https://archlinux.org/packages/?name=amdgpu_top>)包 去监控集成显卡时，发现集成显卡根本没有被使用，为了解决这个问题，我们需要一些额外的配置。 

配置很简单，你只需要针对 `ollama.service` 创建一个[附加配置片段](<../zh-cn/Systemd.html#%E9%99%84%E5%8A%A0%E9%85%8D%E7%BD%AE%E7%89%87%E6%AE%B5> "附加配置片段")，文件内容如下： 
    
    /etc/systemd/system/ollama.service.d/override_gfx_version.conf
    
    [Service]
    Environment="HSA_OVERRIDE_GFX_VERSION=A.B.C"

其中X.Y.Z版本号使用当前系统中系统已安装的 [rocblas](<https://archlinux.org/packages/?name=rocblas>)包 核心版本，具体选择哪个 [rocblas](<https://archlinux.org/packages/?name=rocblas>)包 核心版本需要通过GFX版本判断。 

第一步，我们需要安装和使用 [rocminfo](<https://archlinux.org/packages/?name=rocminfo>)包 来查询当前系统准确的GFX版本。在安装 [ollama-rocm](<https://archlinux.org/packages/?name=ollama-rocm>)包 时， [rocminfo](<https://archlinux.org/packages/?name=rocminfo>)包 会被作为间接依赖一同安装（ [ollama-rocm](<https://archlinux.org/packages/?name=ollama-rocm>)包 依赖 [rocblas](<https://archlinux.org/packages/?name=rocblas>)包 ， [rocblas](<https://archlinux.org/packages/?name=rocblas>)包 依赖 [rocminfo](<https://archlinux.org/packages/?name=rocminfo>)包 ）。 
    
    $ /opt/rocm/bin/rocminfo | grep amdhsa
    
  * 如果显示 `gfx` 后的数字为4位数，前两个数字作为 `X` ，后两个数字分别为 `YZ` 。
  * 如果显示 `gfx` 后的数字为3位数，三位数字分别是 `XYZ` 。

第二步，查询已安装的 [rocblas](<https://archlinux.org/packages/?name=rocblas>)包 核心版本。我们需要选取某个 [rocblas](<https://archlinux.org/packages/?name=rocblas>)包 核心的版本号本来配置[附加配置片段](<../zh-cn/Systemd.html#%E9%99%84%E5%8A%A0%E9%85%8D%E7%BD%AE%E7%89%87%E6%AE%B5> "附加配置片段")，其中版本 `A==X, B<=Y, C<=Z` ，即 `A.B.C` 为 `X.*<=Y.*<=Z` 。 
    
    $ find /opt/rocm/lib/rocblas/library -name 'Kernels.so-*'
    
例如，GFX 版本号为 `11.2.9` , 则选取 [rocblas](<https://archlinux.org/packages/?name=rocblas>)包 核心版本 `11.*<=2.*<=9` （例如 `11.0.2` ）。 

[附加配置片段](<../zh-cn/Systemd.html#%E9%99%84%E5%8A%A0%E9%85%8D%E7%BD%AE%E7%89%87%E6%AE%B5> "附加配置片段")修改为： 
    
    /etc/systemd/system/ollama.service.d/override_gfx_version.conf
    
    [Service]
    Environment="HSA_OVERRIDE_GFX_VERSION=11.0.2"

最后，我们执行 [daemon-reload](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Daemon-reload") 并[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `ollama.service` 来重新加载守护进程，使得配置生效。 

现在，你可以重新运行 Ollama 会话，并通过类似 [amdgpu_top](<https://archlinux.org/packages/?name=amdgpu_top>)包 去监控集成显卡的使用情况。 

###  卸载 Ollama 后模型仍存在

你可以手动删掉这些模型，这些文件存在 `/var/lib/ollama/blobs` 目录中。 

##  另请参阅

  * [Ollama Blog](<https://ollama.com/blog>)
  * [Ollama Docs](<https://github.com/ollama/ollama/tree/main/docs>)
  * [What is rocBLAS](<https://rocm.docs.amd.com/projects/rocBLAS/en/latest/how-to/what-is-rocblas.html>)
