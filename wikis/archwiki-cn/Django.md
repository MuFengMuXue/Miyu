**翻译状态：**

  * 本文（或部分内容）译自 [Django](<https://wiki.archlinux.org/title/Django> "arch:Django")，最近一次同步于 2020-06-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/Django?diff=0&oldid=620335>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Django_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Django](<https://www.djangoproject.com>) 是遵循模型-视图-模板（MVT）架构模式的高级 [Python](<../zh-cn/Python.html> "Python") Web 框架。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")提供最新 Python 3 支持的 [python-django](<https://archlinux.org/packages/?name=python-django>)包 软件包。可以使用 [django-docs](<https://aur.archlinux.org/packages/django-docs/>)AUR 软件包安装文档。 

###  数据库驱动程序

Django 有不同的数据库后端可用： 

  * 对于 [PostgreSQL](<../zh-cn/PostgreSQL.html> "PostgreSQL") 后端，请安装 [python-psycopg2](<https://archlinux.org/packages/?name=python-psycopg2>)包 软件包。
  * 如果您打算将 [MySQL](<../zh-cn/MySQL.html> "MySQL") 数据库用作后端，请安装 [python-mysqlclient](<https://archlinux.org/packages/?name=python-mysqlclient>)包 软件包。

##  用法

如果要启动 Django 项目，请使用 `django-admin` 命令 
    
    $ django-admin startproject mysite
    
这将在当前目录中创建一个 `mysite` 目录。 它还将创建一个 `manage.py` 脚本，该脚本可让您与项目进行交互。 

您可以在[官方 Django 教程](<https://docs.djangoproject.com/en/2.2/intro/tutorial01/>)和 [Django 文档](<https://docs.djangoproject.com/en/>)中找到更多信息。 

##  参见

  * [awesome-django](<https://github.com/wsvincent/awesome-django>) \- Django 应用，项目和资源的精选列表。
  * [Django vs Flask](<https://devel.tech/features/django-vs-flask/>) \- Django 和 Flask 框架的比较。
