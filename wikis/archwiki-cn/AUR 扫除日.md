**翻译状态：**

  * 本文（或部分内容）译自 [AUR Cleanup Day](<https://wiki.archlinux.org/title/AUR_Cleanup_Day> "arch:AUR Cleanup Day")，最近一次同步于 2025-10-23，若英文版本有所[更改](<https://wiki.archlinux.org/title/AUR_Cleanup_Day?diff=0&oldid=850339>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/AUR_Cleanup_Day_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

##  关于

AUR 扫除日（AUR Cleanup Day）是隔年（奇数年）9 月 20 号进行一次的活动。 

[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 上存在大量可清理的过时软件包。你可以使用以下模板，将建议清理的软件包提交到公告邮件中提供的协作文档中，也可以将它们提交到 [aur-general 邮件列表](<https://lists.archlinux.org/mailman3/lists/aur-general.lists.archlinux.org/>)，或是直接发起[请求](<../zh-cn/AUR_%E6%8F%90%E4%BA%A4%E5%87%86%E5%88%99.html#%E8%AF%B7%E6%B1%82> "AUR 提交准则")。[软件包维护者](<../zh-cn/%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%BB%B4%E6%8A%A4%E8%80%85.html> "软件包维护者")们会共同决定要被移除的软件包清单。 

请加入 [#archlinux-aur](<../zh-cn/Arch_%E7%9A%84_IRC_%E9%A2%91%E9%81%93.html> "Arch 的 IRC 频道") 进行协作和探讨。 

##  模板
    
    # AUR Cleanup Day September 20th 20XY
    
    ## About
    
    AUR Cleanup Day is a bi-yearly (odd years) event on the 20th of September.
    
    The [AUR](https://wiki.archlinux.org/title/Arch_User_Repository) has a large number of obsolete packages which could use cleaning up. Post suggestions of packages below, submit them to the [aur-general mailing list](https://lists.archlinux.org/listinfo/aur-general), or file [requests](https://wiki.archlinux.org/title/AUR_submission_guidelines#Requests) directly. [Package Maintainers](https://wiki.archlinux.org/title/Package_Maintainers) will get together and confirm which packages should be removed.
    
    Join [#archlinux-aur](https://wiki.archlinux.org/title/Arch_IRC_channels) to collaborate and chat.
    
    ## Template (Package list)
    
    ### Candidates
    
    Check for the package in the sorted lists below before adding.
    
    - [PKGNAME](https://aur.archlinux.org/packages/PKGNAME) - Reason
    
    #### Informative heading
    
    - [PKGBASE](https://aur.archlinux.org/pkgbase/PKGBASE) - Reason
    
    ### Possible reasons
    
    - Does not work anymore
    
    - Deprecated by [PKGNAME](https://aur.archlinux.org/packages/PKGNAME)
    
    - Obsoleted by [PKGNAME](https://aur.archlinux.org/packages/PKGNAME)
    
    - Replaced by [PKGNAME](https://aur.archlinux.org/packages/PKGNAME)
    
    - Duplicate of [PKGNAME](https://aur.archlinux.org/packages/PKGNAME)
    
    - Project page and sources are not available
    
    - "Dead" project; it's very old and does not work with the latest versions of its dependencies
    
    - "Dead" project and too old to be useful
    
    - Project page and sources are not available
    
    - Not needed anymore (it's for old PKGNAME), broken source link
    
    - Old dev-version (CVS/SVN/etc), PKGNAME project uses Git now
    
    - Is it needed in Arch Linux?
    
    - Broken links (see comment by USERNAME)
    
    - Outdated for a long time
    
    - This one should be renamed
    
    - Deprecated by upstream
    
    - Outdated, orphaned
    
    - Broken links, too old, not maintained
    
    - Included in extra/PKGNAME
    
    - Already included in core/PKGNAME
    
    - Old beta version, broken source link, replaced by [PKGNAME](https://aur.archlinux.org/packages/PKGNAME)
    
    - Maintainer wrote that it may be deleted
    
    - Dropped upstream
    
    - Depends on [PKGNAME](https://aur.archlinux.org/packages/PKGNAME) and has not been updated for N years...
    
    - Development discontinued, project page deleted and current version does not work
    
    - Too old to be useful, broken source link -- hm, what is USERNAME's Opinion?
    
    - This package is no longer needed (see comments)
    
    ## Template (TU)
    
    **For editing by TUs only!**
    
    ### Packages to Remove
    
    In extra:
    
    - [PKGNAME](https://aur.archlinux.org/packages/PKGNAME) - Replaced by PKGNAME
    
    ### Packages to Keep
    
    - [PKGNAME](https://aur.archlinux.org/packages/PKGNAME) - Reason
    
    #### Possible reasons
    
    - It is for compiling old stuff, let's keep it, does not harm
    
    - Seems to be actively maintained
    
    - Still useful, because ...
    
    - So this package should maybe be orphaned, no obvious reason to delete it
    
    - Needed by PKGNAME
    
    - Package has new and active maintainer
    
    - Seems to be down sometimes, but sometimes it works again. Package is maintained and has votes
    
    - Should be rewritten, not dropped
    
    - I orphaned the package
    
    - It's not dead, it only needs some changes to work again
    
    - Package builds with little tweaking
    
    - Builds fine with a little patch in pkgrel N
    