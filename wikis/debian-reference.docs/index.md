> **原文链接：** [https://www.debian.org/doc/manuals/debian-reference/index.zh-cn.html](https://www.debian.org/doc/manuals/debian-reference/index.zh-cn.html)

---

::: navheader
  Debian 参考手册       
  ----------------- --- ---------------------------------------------------------------
                           [![下一页](images/next.png)](pr01.zh-cn.html){accesskey="n"}

------------------------------------------------------------------------
:::

::::::::::::::: {.book lang="zh-cn"}
:::::::::::: titlepage
<div>

<div>

# []{#id768}Debian 参考手册 {#debian-参考手册 .title}

</div>

<div>

::: author
### [Osamu Aoki (青木 修)]{.othername} {#osamu-aoki-青木-修 .author}
:::

</div>

<div>

版权 © 2013-2024 青木修

</div>

<div>

::: legalnotice
[]{#id770}

Debian 参考手册（版本 2.139）(2026-04-22 04:01:24 UTC) 旨在作为一份 Debian 系统安装后的用户指南，为 Debian 系统的使用与管理提供广泛的概览。它通过为非开发者编写的 shell 命令示例来涵盖系统管理的方方面面。
:::

</div>

<div>

::: abstract
**摘要**

这本书是自由的；你可以在与 Debian 自由软件指导方针（DFSG）兼容的任意版本的 GNU 通用公共许可证的条款下重新分发和修改本书。
:::

</div>

</div>

------------------------------------------------------------------------
::::::::::::

::: toc
**目录**

[ [序言](pr01.zh-cn.html) ]{.preface}

[ [1. 免责声明](pr01.zh-cn.html#_disclaimer) ]{.section}

[ [2. 什么是 Debian](pr01.zh-cn.html#_what_is_debian) ]{.section}

[ [3. 关于本文档](pr01.zh-cn.html#_about_this_document) ]{.section}

[ [3.1. 指导原则](pr01.zh-cn.html#_guiding_rules) ]{.section}

[ [3.2. 预备知识](pr01.zh-cn.html#_prerequisites) ]{.section}

[ [3.3. 排版约定](pr01.zh-cn.html#_conventions) ]{.section}

[ [3.4. popcon 流行度](pr01.zh-cn.html#_the_popcon) ]{.section}

[ [3.5. 软件包大小](pr01.zh-cn.html#_the_package_size) ]{.section}

[ [3.6. 给本文档报告 Bug](pr01.zh-cn.html#_bug_reports_on_this_document) ]{.section}

[ [4. 一些对新使用者的提醒](pr01.zh-cn.html#_reminders_for_new_users) ]{.section}

[ [5. 一些对新使用者的引导](pr01.zh-cn.html#_some_quotes_for_new_users) ]{.section}

[ [1. GNU/Linux 教程](ch01.zh-cn.html) ]{.chapter}

[ [1.1. 控制台基础](ch01.zh-cn.html#_console_basics) ]{.section}

[ [1.1.1. shell 提示符](ch01.zh-cn.html#_the_shell_prompt) ]{.section}

[ [1.1.2. GUI 下的 shell 提示符](ch01.zh-cn.html#_the_shell_prompt_under_gui) ]{.section}

[ [1.1.3. root 账户](ch01.zh-cn.html#_the_root_account) ]{.section}

[ [1.1.4. root shell 提示符](ch01.zh-cn.html#_the_root_shell_prompt) ]{.section}

[ [1.1.5. GUI 系统管理工具](ch01.zh-cn.html#_gui_system_administration_tools) ]{.section}

[ [1.1.6. 虚拟控制台](ch01.zh-cn.html#_virtual_consoles) ]{.section}

[ [1.1.7. 怎样退出命令行提示符](ch01.zh-cn.html#_how_to_leave_the_command_prompt) ]{.section}

[ [1.1.8. 怎样关闭系统](ch01.zh-cn.html#_how_to_shutdown_the_system) ]{.section}

[ [1.1.9. 恢复一个正常的控制台](ch01.zh-cn.html#_recovering_a_sane_console) ]{.section}

[ [1.1.10. 建议新手安装的额外软件包](ch01.zh-cn.html#_additional_package_suggestions_for_the_newbie) ]{.section}

[ [1.1.11. 额外用户账号](ch01.zh-cn.html#_an_extra_user_account) ]{.section}

[ [1.1.12. sudo 配置](ch01.zh-cn.html#_sudo_configuration) ]{.section}

[ [1.1.13. 动手时间](ch01.zh-cn.html#_play_time) ]{.section}

[ [1.2. 类 Unix 文件系统](ch01.zh-cn.html#_unix_like_filesystem) ]{.section}

[ [1.2.1. Unix 文件基础](ch01.zh-cn.html#_unix_file_basics) ]{.section}

[ [1.2.2. 文件系统深入解析](ch01.zh-cn.html#_filesystem_internals) ]{.section}

[ [1.2.3. 文件系统权限](ch01.zh-cn.html#_filesystem_permissions) ]{.section}

[ [1.2.4. 控制新建文件的权限：umask](ch01.zh-cn.html#_control_of_permissions_for_newly_created_files_umask) ]{.section}

[ [1.2.5. 一组用户的权限（组）](ch01.zh-cn.html#_permissions_for_groups_of_users_group) ]{.section}

[ [1.2.6. 时间戳](ch01.zh-cn.html#_timestamps) ]{.section}

[ [1.2.7. 链接](ch01.zh-cn.html#_links) ]{.section}

[ [1.2.8. 命名管道（先进先出）](ch01.zh-cn.html#_named_pipes_fifos) ]{.section}

[ [1.2.9. 套接字](ch01.zh-cn.html#_sockets) ]{.section}

[ [1.2.10. 设备文件](ch01.zh-cn.html#_device_files) ]{.section}

[ [1.2.11. 特殊设备文件](ch01.zh-cn.html#_special_device_files) ]{.section}

[ [1.2.12. procfs 和 sysfs](ch01.zh-cn.html#_procfs_and_sysfs) ]{.section}

[ [1.2.13. tmpfs](ch01.zh-cn.html#_tmpfs) ]{.section}

[ [1.3. Midnight Commander (MC)](ch01.zh-cn.html#_midnight_commander_mc) ]{.section}

[ [1.3.1. 自定义 MC](ch01.zh-cn.html#_customization_of_mc) ]{.section}

[ [1.3.2. 启动 MC](ch01.zh-cn.html#_starting_mc) ]{.section}

[ [1.3.3. MC 文件管理](ch01.zh-cn.html#_file_manager_in_mc) ]{.section}

[ [1.3.4. MC 命令行技巧](ch01.zh-cn.html#_command_line_tricks_in_mc) ]{.section}

[ [1.3.5. MC 内部编辑器](ch01.zh-cn.html#_the_internal_editor_in_mc) ]{.section}

[ [1.3.6. MC 内部查看器](ch01.zh-cn.html#_the_internal_viewer_in_mc) ]{.section}

[ [1.3.7. 自动启动 MC](ch01.zh-cn.html#_auto_start_features_of_mc) ]{.section}

[ [1.3.8. MC 中的 虚拟文件系统](ch01.zh-cn.html#_virtual_filesystem_of_mc) ]{.section}

[ [1.4. 类 Unix 工作环境基础](ch01.zh-cn.html#_the_basic_unix_like_work_environment) ]{.section}

[ [1.4.1. 登录 shell](ch01.zh-cn.html#_the_login_shell) ]{.section}

[ [1.4.2. 定制 bash](ch01.zh-cn.html#_customizing_bash) ]{.section}

[ [1.4.3. 特殊按键](ch01.zh-cn.html#_special_key_strokes) ]{.section}

[ [1.4.4. 鼠标操作](ch01.zh-cn.html#_mouse_operations) ]{.section}

[ [1.4.5. 分页程序](ch01.zh-cn.html#_the_pager) ]{.section}

[ [1.4.6. 文本编辑器](ch01.zh-cn.html#_the_text_editor) ]{.section}

[ [1.4.7. 设置默认文本编辑器](ch01.zh-cn.html#_setting_a_default_text_editor) ]{.section}

[ [1.4.8. 使用 vim](ch01.zh-cn.html#_using_vim) ]{.section}

[ [1.4.9. 记录 shell 活动](ch01.zh-cn.html#_recording_the_shell_activities) ]{.section}

[ [1.4.10. 基本的 Unix 命令](ch01.zh-cn.html#_basic_unix_commands) ]{.section}

[ [1.5. 简单 shell 命令](ch01.zh-cn.html#_the_simple_shell_command) ]{.section}

[ [1.5.1. 命令执行和环境变量](ch01.zh-cn.html#_command_execution_and_environment_variable) ]{.section}

[ [1.5.2. "`$LANG`{.literal}"变量](ch01.zh-cn.html#_the_literal_lang_literal_variable) ]{.section}

[ [1.5.3. \"`$PATH`{.literal}\" 变量](ch01.zh-cn.html#_the_literal_path_literal_variable) ]{.section}

[ [1.5.4. \"`$HOME`{.literal}\" 变量](ch01.zh-cn.html#_the_literal_home_literal_variable) ]{.section}

[ [1.5.5. 命令行选项](ch01.zh-cn.html#_command_line_options) ]{.section}

[ [1.5.6. Shell 通配符](ch01.zh-cn.html#_shell_glob) ]{.section}

[ [1.5.7. 命令的返回值](ch01.zh-cn.html#_return_value_of_the_command) ]{.section}

[ [1.5.8. 典型的顺序命令和 shell 重定向](ch01.zh-cn.html#_typical_command_sequences_and_shell_redirection) ]{.section}

[ [1.5.9. 命令别名](ch01.zh-cn.html#_command_alias) ]{.section}

[ [1.6. 类 Unix 的文本处理](ch01.zh-cn.html#_unix_like_text_processing) ]{.section}

[ [1.6.1. Unix 文本工具](ch01.zh-cn.html#_unix_text_tools) ]{.section}

[ [1.6.2. 正则表达式](ch01.zh-cn.html#_regular_expressions) ]{.section}

[ [1.6.3. 替换表达式](ch01.zh-cn.html#_replacement_expressions) ]{.section}

[ [1.6.4. 正则表达式的全局替换](ch01.zh-cn.html#_global_substitution_with_regular_expressions) ]{.section}

[ [1.6.5. 从文本文件的表格中提取数据](ch01.zh-cn.html#_extracting_data_from_text_file_table) ]{.section}

[ [1.6.6. 用于管道命令的小片段脚本](ch01.zh-cn.html#_script_snippets_for_piping_commands) ]{.section}

[ [2. Debian 软件包管理](ch02.zh-cn.html) ]{.chapter}

[ [2.1. Debian 软件包管理的前提](ch02.zh-cn.html#_debian_package_management_prerequisites) ]{.section}

[ [2.1.1. Debian 软件包管理](ch02.zh-cn.html#_debian_package_management_system) ]{.section}

[ [2.1.2. 软件包配置](ch02.zh-cn.html#_package_configuration) ]{.section}

[ [2.1.3. 基本的注意事项](ch02.zh-cn.html#_basic_precautions) ]{.section}

[ [2.1.4. 持续升级的生活](ch02.zh-cn.html#_life_with_eternal_upgrades) ]{.section}

[ [2.1.5. Debian 档案库基础](ch02.zh-cn.html#_debian_archive_basics) ]{.section}

[ [2.1.6. Debian 是100% 的自由软件](ch02.zh-cn.html#_debian_is_100_free_software) ]{.section}

[ [2.1.7. 软件包依赖关系](ch02.zh-cn.html#_package_dependencies) ]{.section}

[ [2.1.8. 包管理的事件流](ch02.zh-cn.html#_the_event_flow_of_the_package_management) ]{.section}

[ [2.1.9. 对包管理问题的第一个回应](ch02.zh-cn.html#_first_response_to_package_management_troubles) ]{.section}

[ [2.1.10. 如何挑选 Debian 软件包](ch02.zh-cn.html#_how_to_pick_debian_packages) ]{.section}

[ [2.1.11. 怎样和不一致的要求协作](ch02.zh-cn.html#_how_to_cope_with_conflicting_requirements) ]{.section}

[ [2.2. 基础软件包管理操作](ch02.zh-cn.html#_basic_package_management_operations) ]{.section}

[ [2.2.1. `apt`{.literal} vs. `apt-get`{.literal} / `apt-cache`{.literal} vs. `aptitude`{.literal}](ch02.zh-cn.html#_literal_apt_literal_vs_literal_apt_get_literal_literal_apt_cache_literal_vs_literal_aptitude_literal) ]{.section}

[ [2.2.2. 命令行中的基础软件包管理操作](ch02.zh-cn.html#_basic_package_management_operations_with_the_commandline) ]{.section}

[ [2.2.3. aptitude 的交互式使用](ch02.zh-cn.html#_interactive_use_of_aptitude) ]{.section}

[ [2.2.4. aptitude 的按键绑定](ch02.zh-cn.html#_key_bindings_of_aptitude) ]{.section}

[ [2.2.5. aptitude 软件包视图](ch02.zh-cn.html#_package_views_under_aptitude) ]{.section}

[ [2.2.6. aptitude 搜索方式选项](ch02.zh-cn.html#_search_method_options_with_aptitude) ]{.section}

[ [2.2.7. aptitude 正则表达式](ch02.zh-cn.html#_the_aptitude_regex_formula) ]{.section}

[ [2.2.8. aptitude 的依赖解决](ch02.zh-cn.html#_dependency_resolution_of_aptitude) ]{.section}

[ [2.2.9. 软件包活动日志](ch02.zh-cn.html#_package_activity_logs) ]{.section}

[ [2.3. aptitude 操作范例](ch02.zh-cn.html#_examples_of_aptitude_operations) ]{.section}

[ [2.3.1. 查找感兴趣的软件包](ch02.zh-cn.html#_seeking_interesting_packages) ]{.section}

[ [2.3.2. 通过正则表达式匹配软件包名称来列出软件包](ch02.zh-cn.html#_listing_packages_with_regex_matching_on_package_names) ]{.section}

[ [2.3.3. 使用正则表达式匹配浏览](ch02.zh-cn.html#_browsing_with_the_regex_matching) ]{.section}

[ [2.3.4. 完整地清理已删除软件包](ch02.zh-cn.html#_purging_removed_packages_for_good) ]{.section}

[ [2.3.5. 调整自动/手动安装状态](ch02.zh-cn.html#_tidying_auto_manual_install_status) ]{.section}

[ [2.3.6. 全面的系统升级](ch02.zh-cn.html#_system_wide_upgrade) ]{.section}

[ [2.4. 高级软件包管理操作](ch02.zh-cn.html#_advanced_package_management_operations) ]{.section}

[ [2.4.1. 命令行中的高级软件包管理操作](ch02.zh-cn.html#_advanced_package_management_operations_with_commandline) ]{.section}

[ [2.4.2. 验证安装的软件包文件](ch02.zh-cn.html#_verification_of_installed_package_files) ]{.section}

[ [2.4.3. 预防软件包故障](ch02.zh-cn.html#_safeguarding_for_package_problems) ]{.section}

[ [2.4.4. 搜索软件包元数据](ch02.zh-cn.html#_searching_on_the_package_meta_data) ]{.section}

[ [2.5. Debian 软件包内部管理](ch02.zh-cn.html#_debian_package_management_internals) ]{.section}

[ [2.5.1. 档案库元数据](ch02.zh-cn.html#_archive_meta_data) ]{.section}

[ [2.5.2. 顶层"Release"文件及真实性](ch02.zh-cn.html#_top_level_release_file_and_authenticity) ]{.section}

[ [2.5.3. 档案库层的"Release"文件](ch02.zh-cn.html#_archive_level_release_files) ]{.section}

[ [2.5.4. 获取用于软件包的元数据](ch02.zh-cn.html#_fetching_of_the_meta_data_for_the_package) ]{.section}

[ [2.5.5. APT 的软件包状态](ch02.zh-cn.html#_the_package_state_for_apt) ]{.section}

[ [2.5.6. aptitude 的软件包状态](ch02.zh-cn.html#_the_package_state_for_aptitude) ]{.section}

[ [2.5.7. 获取的软件包的本地副本](ch02.zh-cn.html#_local_copies_of_the_fetched_packages) ]{.section}

[ [2.5.8. Debian 软件包文件名称](ch02.zh-cn.html#_debian_package_file_names) ]{.section}

[ [2.5.9. dpkg 命令](ch02.zh-cn.html#_the_dpkg_command) ]{.section}

[ [2.5.10. update-alternatives 命令](ch02.zh-cn.html#_the_update_alternatives_command) ]{.section}

[ [2.5.11. dpkg-statoverride 命令](ch02.zh-cn.html#_the_dpkg_statoverride_command) ]{.section}

[ [2.5.12. dpkg-divert 命令](ch02.zh-cn.html#_the_dpkg_divert_command) ]{.section}

[ [2.6. 从损坏的系统中恢复](ch02.zh-cn.html#_recovery_from_a_broken_system) ]{.section}

[ [2.6.1. 不兼容旧的用户配置](ch02.zh-cn.html#_incompatibility_with_old_user_configuration) ]{.section}

[ [2.6.2. 软件包数据缓存错误](ch02.zh-cn.html#_caching_errors_of_the_package_data) ]{.section}

[ [2.6.3. 使用 dpkg 命令进行救援](ch02.zh-cn.html#_rescue_with_the_dpkg_command) ]{.section}

[ [2.6.4. 缺少依赖导致的安装失败](ch02.zh-cn.html#_failed_installation_due_to_missing_dependencies) ]{.section}

[ [2.6.5. 具有相同文件的不同软件包](ch02.zh-cn.html#_different_packages_with_overlapped_files) ]{.section}

[ [2.6.6. 修复损坏的软件包脚本](ch02.zh-cn.html#_fixing_broken_package_script) ]{.section}

[ [2.6.7. 恢复软件包选择数据](ch02.zh-cn.html#_recovering_package_selection_data) ]{.section}

[ [2.7. 软件包管理技巧](ch02.zh-cn.html#_tips_for_the_package_management) ]{.section}

[ [2.7.1. 上传软件包的是谁？](ch02.zh-cn.html#_who_uploaded_the_package) ]{.section}

[ [2.7.2. 限制 APT 的下载带宽](ch02.zh-cn.html#_limiting_download_bandwidth_for_apt) ]{.section}

[ [2.7.3. 自动下载和升级软件包](ch02.zh-cn.html#_automatic_download_and_upgrade_of_packages) ]{.section}

[ [2.7.4. 更新和向后移植](ch02.zh-cn.html#_updates_and_backports) ]{.section}

[ [2.7.5. 外部软件包档案库](ch02.zh-cn.html#_external_package_archives) ]{.section}

[ [2.7.6. 不使用 [**apt-pinning**]{.strong} 的混合源档案库软件包](ch02.zh-cn.html#_packages_from_mixed_source_of_archives) ]{.section}

[ [2.7.7. 使用 [**apt-pinning**]{.strong} 调整获选版本](ch02.zh-cn.html#_tweaking_candidate_version) ]{.section}

[ [2.7.8. 阻止推荐的软件包的安装](ch02.zh-cn.html#_blocking_packages_installed_by_recommends) ]{.section}

[ [2.7.9. 使用带有 `unstable`{.literal} 软件包的 `testing`{.literal} 版本](ch02.zh-cn.html#_tracking_literal_testing_literal_with_some_packages_from_literal_unstable_literal) ]{.section}

[ [2.7.10. 使用带有 `experimental`{.literal} 软件包的 `unstable`{.literal} 版本](ch02.zh-cn.html#_tracking_literal_unstable_literal_with_some_packages_from_literal_experimental_literal) ]{.section}

[ [2.7.11. 紧急降级](ch02.zh-cn.html#_emergency_downgrading) ]{.section}

[ [2.7.12. equivs 软件包](ch02.zh-cn.html#_the_equivs_package) ]{.section}

[ [2.7.13. 移植一个软件包到 stable 系统](ch02.zh-cn.html#_porting_a_package_to_the_stable_system) ]{.section}

[ [2.7.14. 用于 APT 的代理服务器](ch02.zh-cn.html#_proxy_server_for_apt) ]{.section}

[ [2.7.15. 更多关于软件包管理的文档](ch02.zh-cn.html#_more_readings_for_the_package_management) ]{.section}

[ [3. 系统初始化](ch03.zh-cn.html) ]{.chapter}

[ [3.1. 启动过程概述](ch03.zh-cn.html#_an_overview_of_the_boot_strap_process) ]{.section}

[ [3.1.1. 第一阶段：UEFI](ch03.zh-cn.html#_stage_1_the_uefi) ]{.section}

[ [3.1.2. 第二阶段：引载加载程序](ch03.zh-cn.html#_stage_2_the_boot_loader) ]{.section}

[ [3.1.3. 第三阶段：迷你 Debian 系统](ch03.zh-cn.html#_stage_3_the_mini_debian_system) ]{.section}

[ [3.1.4. 第四阶段：常规 Debian 系统](ch03.zh-cn.html#_stage_4_the_normal_debian_system) ]{.section}

[ [3.2. 应急救援系统](ch03.zh-cn.html#_rescue_system) ]{.section}

[ [3.2.1. USB 上的 GRUB UEFI 应急救援系统](ch03.zh-cn.html#_grub_uefi_rescue_system_on_usb) ]{.section}

[ [3.2.2. USB 上的 Linux 即用救援系统](ch03.zh-cn.html#_linux_live_rescue_system_on_usb) ]{.section}

[ [3.2.3. 从 GRUB 启动的 Linux 即用应急救援系统](ch03.zh-cn.html#_linux_live_rescue_system_from_grub) ]{.section}

[ [3.3. Systemd](ch03.zh-cn.html#_systemd) ]{.section}

[ [3.3.1. Systemd 初始化](ch03.zh-cn.html#_systemd_init) ]{.section}

[ [3.3.2. Systemd 登录](ch03.zh-cn.html#_systemd_login) ]{.section}

[ [3.4. 内核消息](ch03.zh-cn.html#_the_kernel_message) ]{.section}

[ [3.5. 系统消息](ch03.zh-cn.html#_the_system_message) ]{.section}

[ [3.6. 系统管理](ch03.zh-cn.html#_system_management_operations) ]{.section}

[ [3.7. 其它系统监控](ch03.zh-cn.html#_other_system_monitors) ]{.section}

[ [3.8. 系统配置](ch03.zh-cn.html#_system_configuration) ]{.section}

[ [3.8.1. 主机名](ch03.zh-cn.html#_the_hostname) ]{.section}

[ [3.8.2. 文件系统](ch03.zh-cn.html#_the_filesystem) ]{.section}

[ [3.8.3. 网络接口初始化](ch03.zh-cn.html#_network_interface_initialization) ]{.section}

[ [3.8.4. 云系统初始化](ch03.zh-cn.html#_cloud_system_initialization) ]{.section}

[ [3.8.5. 调整 sshd 服务的个性化例子](ch03.zh-cn.html#_customization_example_to_tweak_sshd_service) ]{.section}

[ [3.9. udev 系统](ch03.zh-cn.html#_the_udev_system) ]{.section}

[ [3.10. 内核模块初始化](ch03.zh-cn.html#_the_kernel_module_initialization) ]{.section}

[ [4. 认证和访问控制](ch04.zh-cn.html) ]{.chapter}

[ [4.1. 一般的 Unix 认证](ch04.zh-cn.html#_normal_unix_authentication) ]{.section}

[ [4.2. 管理账号和密码信息](ch04.zh-cn.html#_managing_account_and_password_information) ]{.section}

[ [4.3. 好密码](ch04.zh-cn.html#_good_password) ]{.section}

[ [4.4. 设立加密的密码](ch04.zh-cn.html#_creating_encrypted_password) ]{.section}

[ [4.5. PAM 和 NSS](ch04.zh-cn.html#_pam_and_nss) ]{.section}

[ [4.5.1. PAM 和 NSS 访问的配置文件](ch04.zh-cn.html#_configuration_files_accessed_by_pam_and_nss) ]{.section}

[ [4.5.2. 现代的集中式系统管理](ch04.zh-cn.html#_the_modern_centralized_system_management) ]{.section}

[ [4.5.3. "为什么 GNU su 不支持 wheel 组"](ch04.zh-cn.html#_why_gnu_su_does_not_support_the_wheel_group) ]{.section}

[ [4.5.4. 严格的密码规则](ch04.zh-cn.html#_stricter_password_rule) ]{.section}

[ [4.6. 安全认证](ch04.zh-cn.html#_security_of_authentication) ]{.section}

[ [4.6.1. 确保互联网上的的密码安全](ch04.zh-cn.html#_secure_password_on_the_internet) ]{.section}

[ [4.6.2. 安全 Shell](ch04.zh-cn.html#_secure_shell) ]{.section}

[ [4.6.3. 互联网额外的安全方式](ch04.zh-cn.html#_extra_security_measures_for_the_internet) ]{.section}

[ [4.6.4. root 密码安全](ch04.zh-cn.html#_securing_the_root_password) ]{.section}

[ [4.7. 其它的访问控制](ch04.zh-cn.html#_other_access_controls) ]{.section}

[ [4.7.1. 访问控制列表(ACLs)](ch04.zh-cn.html#_access_control_lists) ]{.section}

[ [4.7.2. sudo](ch04.zh-cn.html#_sudo) ]{.section}

[ [4.7.3. PolicyKit](ch04.zh-cn.html#_policykit) ]{.section}

[ [4.7.4. 限制访问某些服务端的服务](ch04.zh-cn.html#_restricting_access_to_some_server_services) ]{.section}

[ [4.7.5. Linux 安全特性](ch04.zh-cn.html#_linux_security_features) ]{.section}

[ [5. 网络设置](ch05.zh-cn.html) ]{.chapter}

[ [5.1. 基本网络架构](ch05.zh-cn.html#_the_basic_network_infrastructure) ]{.section}

[ [5.1.1. 主机名解析](ch05.zh-cn.html#_the_hostname_resolution) ]{.section}

[ [5.1.2. 网络接口名称](ch05.zh-cn.html#_the_network_interface_name) ]{.section}

[ [5.1.3. 局域网网络地址范围](ch05.zh-cn.html#_the_network_address_range_for_the_lan) ]{.section}

[ [5.1.4. 网络设备支持](ch05.zh-cn.html#_the_network_device_support) ]{.section}

[ [5.2. 现代的桌面网络配置](ch05.zh-cn.html#_the_modern_network_configuration_for_desktop) ]{.section}

[ [5.2.1. 图形界面的网络配置工具](ch05.zh-cn.html#_gui_network_configuration_tools) ]{.section}

[ [5.3. 没有图像界面的现代网络配置](ch05.zh-cn.html#_the_modern_network_configuration_without_gui) ]{.section}

[ [5.4. 现代云网络配置](ch05.zh-cn.html#_the_modern_network_configuration_for_cloud) ]{.section}

[ [5.4.1. 使用 DHCP 的现代云网络配置](ch05.zh-cn.html#_the_modern_network_configuration_for_cloud_with_dhcp) ]{.section}

[ [5.4.2. 使用静态 IP 的现代云网络配置](ch05.zh-cn.html#_the_modern_network_configuration_for_cloud_with_static_ip) ]{.section}

[ [5.4.3. 使用 Network Manager 的现代云网络配置](ch05.zh-cn.html#_the_modern_network_configuration_for_cloud_with_network_manager) ]{.section}

[ [5.5. 底层网络配置](ch05.zh-cn.html#_the_low_level_network_configuration) ]{.section}

[ [5.5.1. Iproute2 命令](ch05.zh-cn.html#_iproute2_commands) ]{.section}

[ [5.5.2. 安全的底层网络操作](ch05.zh-cn.html#_safe_low_level_network_operations) ]{.section}

[ [5.6. 网络优化](ch05.zh-cn.html#_network_optimization) ]{.section}

[ [5.6.1. 找出最佳 MTU](ch05.zh-cn.html#_finding_optimal_mtu) ]{.section}

[ [5.6.2. WAN TCP 优化](ch05.zh-cn.html#_wan_tcp_optimization) ]{.section}

[ [5.7. Netfilter 网络过滤框架](ch05.zh-cn.html#_netfilter_infrastructure) ]{.section}

[ [6. 网络应用](ch06.zh-cn.html) ]{.chapter}

[ [6.1. 网页浏览器](ch06.zh-cn.html#_web_browsers) ]{.section}

[ [6.1.1. 伪装用户代理字符串](ch06.zh-cn.html#_spoofing_the_user_agent_string) ]{.section}

[ [6.1.2. 浏览器扩展](ch06.zh-cn.html#_browser_extension) ]{.section}

[ [6.2. 邮件系统](ch06.zh-cn.html#_the_mail_system) ]{.section}

[ [6.2.1. 电子邮件基础](ch06.zh-cn.html#_email_basics) ]{.section}

[ [6.2.2. 现代邮件服务限制](ch06.zh-cn.html#_modern_mail_service_limitation) ]{.section}

[ [6.2.3. 历史邮件服务端期望](ch06.zh-cn.html#_historic_mail_service_expectation) ]{.section}

[ [6.2.4. 邮件传输代理 (MTA)](ch06.zh-cn.html#_mail_transport_agent_mta) ]{.section}

[ [6.2.4.1. exim4 的配置](ch06.zh-cn.html#_the_configuration_of_exim4) ]{.section}

[ [6.2.4.2. 带有 SASL 的 postfix 配置](ch06.zh-cn.html#_the_configuration_of_postfix_with_sasl) ]{.section}

[ [6.2.4.3. 邮件地址配置](ch06.zh-cn.html#_the_mail_address_configuration) ]{.section}

[ [6.2.4.4. 基础 MTA 操作](ch06.zh-cn.html#_basic_mta_operations) ]{.section}

[ [6.3. 服务器远程访问和工具 (SSH)](ch06.zh-cn.html#_the_remote_access_server_and_utilities_ssh) ]{.section}

[ [6.3.1. SSH 基础](ch06.zh-cn.html#_basics_of_ssh) ]{.section}

[ [6.3.2. 远程主机上的用户名](ch06.zh-cn.html#_user_name_on_the_remote_host) ]{.section}

[ [6.3.3. 免密码远程连接](ch06.zh-cn.html#_connecting_without_remote_passwords) ]{.section}

[ [6.3.4. 处理其它 SSH 客户端](ch06.zh-cn.html#_dealing_with_alien_ssh_clients) ]{.section}

[ [6.3.5. 建立 ssh 代理](ch06.zh-cn.html#_setting_up_ssh_agent) ]{.section}

[ [6.3.6. 从远程主机发送邮件](ch06.zh-cn.html#_sending_a_mail_from_a_remote_host) ]{.section}

[ [6.3.7. SMTP/POP3 隧道的端口转发](ch06.zh-cn.html#_port_forwarding_for_smtp_pop3_tunneling) ]{.section}

[ [6.3.8. 怎样通过 SSH 关闭远程系统](ch06.zh-cn.html#_how_to_shutdown_the_remote_system_on_ssh) ]{.section}

[ [6.3.9. SSH 故障排查](ch06.zh-cn.html#_troubleshooting_ssh) ]{.section}

[ [6.4. 打印服务和工具](ch06.zh-cn.html#_the_print_server_and_utilities) ]{.section}

[ [6.5. 其它网络应用服务](ch06.zh-cn.html#_other_network_application_servers) ]{.section}

[ [6.6. 其它网络应用客户端](ch06.zh-cn.html#_other_network_application_clients) ]{.section}

[ [6.7. 系统后台守护进程（daemon）诊断](ch06.zh-cn.html#_the_diagnosis_of_the_system_daemons) ]{.section}

[ [7. GUI（图形用户界面）系统](ch07.zh-cn.html) ]{.chapter}

[ [7.1. GUI（图形用户界面）桌面环境](ch07.zh-cn.html#_gui_desktops) ]{.section}

[ [7.2. GUI（图形用户界面）通信协议](ch07.zh-cn.html#_gui_communication_protocol) ]{.section}

[ [7.3. GUI（图形用户界面）架构](ch07.zh-cn.html#_gui_infrastructure) ]{.section}

[ [7.4. GUI（图形用户界面）应用](ch07.zh-cn.html#_gui_applications) ]{.section}

[ [7.5. 用户目录](ch07.zh-cn.html#_user_directories) ]{.section}

[ [7.6. 字体](ch07.zh-cn.html#_fonts) ]{.section}

[ [7.6.1. 基础字体](ch07.zh-cn.html#_basic_fonts) ]{.section}

[ [7.6.2. 字体栅格化](ch07.zh-cn.html#_font_rasterization) ]{.section}

[ [7.7. 沙盒](ch07.zh-cn.html#_sandbox) ]{.section}

[ [7.8. 远程桌面](ch07.zh-cn.html#_remote_desktop) ]{.section}

[ [7.9. X 服务端连接](ch07.zh-cn.html#_x_server_connection) ]{.section}

[ [7.9.1. X 服务端本地连接](ch07.zh-cn.html#_x_server_local_connection) ]{.section}

[ [7.9.2. X 服务端远程连接](ch07.zh-cn.html#_x_server_remote_connection) ]{.section}

[ [7.9.3. X 服务端 chroot 连接](ch07.zh-cn.html#_x_server_chroot_connection) ]{.section}

[ [7.10. 剪贴板](ch07.zh-cn.html#_clipboard) ]{.section}

[ [8. 国际化和本地化](ch08.zh-cn.html) ]{.chapter}

[ [8.1. 语言环境](ch08.zh-cn.html#_the_locale) ]{.section}

[ [8.1.1. UTF-8 语言环境的基本原理](ch08.zh-cn.html#_rationale_for_utf_8_locale) ]{.section}

[ [8.1.2. 语言环境的重新配置](ch08.zh-cn.html#_the_reconfiguration_of_the_locale) ]{.section}

[ [8.1.3. 文件名编码](ch08.zh-cn.html#_filename_encoding) ]{.section}

[ [8.1.4. 本地化信息和翻译文档](ch08.zh-cn.html#_localized_messages_and_translated_documentation) ]{.section}

[ [8.1.5. 语言环境的影响](ch08.zh-cn.html#_effects_of_the_locale) ]{.section}

[ [8.2. 键盘输入](ch08.zh-cn.html#_the_keyboard_input) ]{.section}

[ [8.2.1. Linux 控制台和 X 窗口的键盘输入](ch08.zh-cn.html#_the_keyboard_input_for_linux_console_and_x_window) ]{.section}

[ [8.2.2. Wayland 键盘输入](ch08.zh-cn.html#_the_keyboard_input_for_wayland) ]{.section}

[ [8.2.3. IBus 支持的输入法](ch08.zh-cn.html#_the_input_method_support_with_ibus) ]{.section}

[ [8.2.4. 一个日语的例子](ch08.zh-cn.html#_an_example_for_japanese) ]{.section}

[ [8.3. 显示输出](ch08.zh-cn.html#_the_display_output) ]{.section}

[ [8.4. 东亚环境下宽度有歧义的字符](ch08.zh-cn.html#_east_asian_ambiguous_character_width_characters) ]{.section}

[ [9. 系统技巧](ch09.zh-cn.html) ]{.chapter}

[ [9.1. 控制台技巧](ch09.zh-cn.html#_the_console_tips) ]{.section}

[ [9.1.1. 清晰的记录 shell 活动](ch09.zh-cn.html#_recording_the_shell_activities_cleanly) ]{.section}

[ [9.1.2. screen 程序](ch09.zh-cn.html#_the_screen_program) ]{.section}

[ [9.1.3. 在目录间游走](ch09.zh-cn.html#_navigating_around_directories) ]{.section}

[ [9.1.4. Readline 封装](ch09.zh-cn.html#_readline_wrapper) ]{.section}

[ [9.1.5. 扫描源代码树](ch09.zh-cn.html#_scanning_the_source_code_tree) ]{.section}

[ [9.2. 定制 vim](ch09.zh-cn.html#_customizing_vim) ]{.section}

[ [9.2.1. 用内部特性定制 vim](ch09.zh-cn.html#_customizing_vim_with%20internal_features) ]{.section}

[ [9.2.2. 用外部软件包定制 vim](ch09.zh-cn.html#_customizing_vim_with_external_packages) ]{.section}

[ [9.3. 数据记录和展示](ch09.zh-cn.html#_data_recording_and_presentation) ]{.section}

[ [9.3.1. 日志后台守护进程（daemon）](ch09.zh-cn.html#_the_log_daemon) ]{.section}

[ [9.3.2. 日志分析](ch09.zh-cn.html#_log_analyzer) ]{.section}

[ [9.3.3. 定制文本数据的显示](ch09.zh-cn.html#_customized_display_of_text_data) ]{.section}

[ [9.3.4. 定制时间和日期的显示](ch09.zh-cn.html#_customized_display_of_time_and_date) ]{.section}

[ [9.3.5. shell 中 echo 的颜色](ch09.zh-cn.html#_colorized_shell_echo) ]{.section}

[ [9.3.6. 有颜色输出的命令](ch09.zh-cn.html#_colorized_commands) ]{.section}

[ [9.3.7. 记录编辑器复杂的重复操作动作](ch09.zh-cn.html#_recording_the_editor_activities_for_complex_repeats) ]{.section}

[ [9.3.8. 记录 X 应用程序的图像](ch09.zh-cn.html#_recording_the_graphic_image_of_an_x_application) ]{.section}

[ [9.3.9. 记录配置文件的变更](ch09.zh-cn.html#_recording_changes_in_configuration_files) ]{.section}

[ [9.4. 监控、控制和启动程序活动](ch09.zh-cn.html#_monitoring_controlling_and_starting_program_activities) ]{.section}

[ [9.4.1. 进程耗时](ch09.zh-cn.html#_timing_a_process) ]{.section}

[ [9.4.2. 调度优先级](ch09.zh-cn.html#_the_scheduling_priority) ]{.section}

[ [9.4.3. ps 命令](ch09.zh-cn.html#_the_ps_command) ]{.section}

[ [9.4.4. top 命令](ch09.zh-cn.html#_the_top_command) ]{.section}

[ [9.4.5. 列出被一个进程打开的文件](ch09.zh-cn.html#_listing_files_opened_by_a_process) ]{.section}

[ [9.4.6. 跟踪程序活动](ch09.zh-cn.html#_tracing_program_activities) ]{.section}

[ [9.4.7. 识别使用文件和套接字的进程](ch09.zh-cn.html#_identification_of_processes_using_files_or_sockets) ]{.section}

[ [9.4.8. 使用固定间隔重复一个命令](ch09.zh-cn.html#_repeating_a_command_with_a_constant_interval) ]{.section}

[ [9.4.9. 使用文件循环来重复一个命令](ch09.zh-cn.html#_repeating_a_command_looping_over_files) ]{.section}

[ [9.4.10. 从 GUI 启动一个程序](ch09.zh-cn.html#_starting_a_program_from_gui) ]{.section}

[ [9.4.11. 自定义被启动的程序](ch09.zh-cn.html#_customizing_program_to_be_started) ]{.section}

[ [9.4.12. 杀死一个进程](ch09.zh-cn.html#_killing_a_process) ]{.section}

[ [9.4.13. 单次任务时间安排](ch09.zh-cn.html#_scheduling_tasks_once) ]{.section}

[ [9.4.14. 定时任务安排](ch09.zh-cn.html#_scheduling_tasks_regularly) ]{.section}

[ [9.4.15. 基于事件的计划任务](ch09.zh-cn.html#_scheduling_tasks_on_event) ]{.section}

[ [9.4.16. Alt-SysRq 键](ch09.zh-cn.html#_alt_sysrq_key) ]{.section}

[ [9.5. 系统维护技巧](ch09.zh-cn.html#_system_maintenance_tips) ]{.section}

[ [9.5.1. 谁在系统里？](ch09.zh-cn.html#_who_is_on_the_system) ]{.section}

[ [9.5.2. 警告所有人](ch09.zh-cn.html#_warning_everyone) ]{.section}

[ [9.5.3. 硬件识别](ch09.zh-cn.html#_hardware_identification) ]{.section}

[ [9.5.4. 硬件配置](ch09.zh-cn.html#_hardware_configuration) ]{.section}

[ [9.5.5. 系统时间和硬件时间](ch09.zh-cn.html#_system_and_hardware_time) ]{.section}

[ [9.5.6. 终端配置](ch09.zh-cn.html#_the_terminal_configuration) ]{.section}

[ [9.5.7. 声音基础设施](ch09.zh-cn.html#_the_sound_infrastructure) ]{.section}

[ [9.5.8. 关闭屏幕保护](ch09.zh-cn.html#_disabling_the_screen_saver) ]{.section}

[ [9.5.9. 关闭蜂鸣声](ch09.zh-cn.html#_disabling_beep_sounds) ]{.section}

[ [9.5.10. 内存使用](ch09.zh-cn.html#_memory_usage) ]{.section}

[ [9.5.11. 系统安全性和完整性检查](ch09.zh-cn.html#_system_security_and_integrity_check) ]{.section}

[ [9.6. 数据存储技巧](ch09.zh-cn.html#_data_storage_tips) ]{.section}

[ [9.6.1. 硬盘空间使用情况](ch09.zh-cn.html#_disk_space_usage) ]{.section}

[ [9.6.2. 硬盘分区配置](ch09.zh-cn.html#_disk_partition_configuration) ]{.section}

[ [9.6.3. 使用 UUID 访问分区](ch09.zh-cn.html#_accessing_partition_using_uuid) ]{.section}

[ [9.6.4. LVM2](ch09.zh-cn.html#_lvm2) ]{.section}

[ [9.6.5. 文件系统配置](ch09.zh-cn.html#_filesystem_configuration) ]{.section}

[ [9.6.6. 文件系统创建和完整性检查](ch09.zh-cn.html#_filesystem_creation_and_integrity_check) ]{.section}

[ [9.6.7. 通过挂载选项优化文件系统](ch09.zh-cn.html#_optimization_of_filesystem_by_mount_options) ]{.section}

[ [9.6.8. 通过超级块（superblock）优化文件系统](ch09.zh-cn.html#_optimization_of_filesystem_via_superblock) ]{.section}

[ [9.6.9. 硬盘优化](ch09.zh-cn.html#_optimization_of_hard_disk) ]{.section}

[ [9.6.10. 固态硬盘优化](ch09.zh-cn.html#_optimization_of_solid_state_drive) ]{.section}

[ [9.6.11. 使用 SMART 预测硬盘故障](ch09.zh-cn.html#_using_smart_to_predict_hard_disk_failure) ]{.section}

[ [9.6.12. 通过 \$TMPDIR 指定临时存储目录](ch09.zh-cn.html#_specify_temporary_storage_directory_via_tmpdir) ]{.section}

[ [9.6.13. 通过 LVM 扩展可用存储空间](ch09.zh-cn.html#_expansion_of_usable_storage_space_via_lvm) ]{.section}

[ [9.6.14. 通过挂载另一个分区来扩展可用存储空间](ch09.zh-cn.html#_expansion_of_usable_storage_space_by_mounting_another_partition) ]{.section}

[ [9.6.15. 通过 "mount \--bind" 挂载另一个目录来扩展可用存储空间](ch09.zh-cn.html#_expansion_of_usable_storage_space_by_bind_mounting_another_directory) ]{.section}

[ [9.6.16. 通过 overlay 挂载（overlay-mounting）另一个目录来扩展可用存储空间](ch09.zh-cn.html#_expansion_of_usable_storage_space_by_overlay_mounting_another_directory) ]{.section}

[ [9.6.17. 使用符号链接扩展可用存储空间](ch09.zh-cn.html#_expansion_of_usable_storage_space_using_symlink) ]{.section}

[ [9.7. 磁盘映像](ch09.zh-cn.html#_the_disk_image) ]{.section}

[ [9.7.1. 制作磁盘映像文件](ch09.zh-cn.html#_making_the_disk_image_file) ]{.section}

[ [9.7.2. 直接写入硬盘](ch09.zh-cn.html#_writing_directly_to_the_disk) ]{.section}

[ [9.7.3. 挂载磁盘映像文件](ch09.zh-cn.html#_mounting_the_disk_image_file) ]{.section}

[ [9.7.4. 清理磁盘映像文件](ch09.zh-cn.html#_cleaning_a_disk_image_file) ]{.section}

[ [9.7.5. 制作空的磁盘映像文件](ch09.zh-cn.html#_making_the_empty_disk_image_file) ]{.section}

[ [9.7.6. 制作 ISO9660 镜像文件](ch09.zh-cn.html#_making_the_iso9660_image_file) ]{.section}

[ [9.7.7. 直接写入文件到 CD/DVD-R/RW](ch09.zh-cn.html#_writing_directly_to_the_cd_dvd_r_rw) ]{.section}

[ [9.7.8. 挂载 ISO9660 镜像文件](ch09.zh-cn.html#_mounting_the_iso9660_image_file) ]{.section}

[ [9.8. 二进制数据](ch09.zh-cn.html#_the_binary_data) ]{.section}

[ [9.8.1. 查看和编辑二进制数据](ch09.zh-cn.html#_viewing_and_editing_binary_data) ]{.section}

[ [9.8.2. 不挂载磁盘操作文件](ch09.zh-cn.html#_manipulating_files_without_mounting_disk) ]{.section}

[ [9.8.3. 数据冗余](ch09.zh-cn.html#_data_redundancy) ]{.section}

[ [9.8.4. 数据文件恢复和诊断分析](ch09.zh-cn.html#_data_file_recovery_and_forensic_analysis) ]{.section}

[ [9.8.5. 把大文件分成多个小文件](ch09.zh-cn.html#_splitting_a_large_file_into_small_files) ]{.section}

[ [9.8.6. 清空文件内容](ch09.zh-cn.html#_clearing_file_contents) ]{.section}

[ [9.8.7. 样子文件](ch09.zh-cn.html#_dummy_files) ]{.section}

[ [9.8.8. 擦除整块硬盘](ch09.zh-cn.html#_erasing_an_entire_hard_disk) ]{.section}

[ [9.8.9. 擦除硬盘上的未使用的区域](ch09.zh-cn.html#_erasing_unused_area_of_an_hard_disk) ]{.section}

[ [9.8.10. 恢复已经删除但仍然被打开的文件](ch09.zh-cn.html#_undeleting_deleted_but_still_open_files) ]{.section}

[ [9.8.11. 查找所有硬链接](ch09.zh-cn.html#_searching_all_hardlinks) ]{.section}

[ [9.8.12. 不可见磁盘空间消耗](ch09.zh-cn.html#_invisible_disk_space_consumption) ]{.section}

[ [9.9. 数据加密提示](ch09.zh-cn.html#_data_encryption_tips) ]{.section}

[ [9.9.1. 使用 dm-crypt/LUKS 加密移动磁盘](ch09.zh-cn.html#_removable_disk_encryption_with_dm_crypt_luks) ]{.section}

[ [9.9.2. 使用 dm-crypt/LUKS 挂载加密的磁盘](ch09.zh-cn.html#_mounting_encrypted_disk_with_dm_crypt_luks) ]{.section}

[ [9.10. 内核](ch09.zh-cn.html#_the_kernel) ]{.section}

[ [9.10.1. 内核参数](ch09.zh-cn.html#_kernel_parameters) ]{.section}

[ [9.10.2. 内核头文件](ch09.zh-cn.html#_kernel_headers) ]{.section}

[ [9.10.3. 编译内核和相关模块](ch09.zh-cn.html#_compiling_the_kernel_and_related_modules) ]{.section}

[ [9.10.4. 编译内核源代码：Debian 内核团队推荐](ch09.zh-cn.html#_compiling_the_kernel_source_debian_kernel_team_recommendation) ]{.section}

[ [9.10.5. 硬件驱动和固件](ch09.zh-cn.html#_hardware_drivers_and_firmware) ]{.section}

[ [9.11. 虚拟化系统](ch09.zh-cn.html#_virtualized_system) ]{.section}

[ [9.11.1. 虚拟化和模拟器工具](ch09.zh-cn.html#_virtualization_tools) ]{.section}

[ [9.11.2. 虚拟化工作流](ch09.zh-cn.html#_virtualization_work_flow) ]{.section}

[ [9.11.3. 挂载虚拟磁盘映像文件](ch09.zh-cn.html#_mounting_the_virtual_disk_image_file) ]{.section}

[ [9.11.4. Chroot 系统](ch09.zh-cn.html#_chroot_system) ]{.section}

[ [9.11.5. 多桌面系统](ch09.zh-cn.html#_multiple_desktop_systems) ]{.section}

[ [10. 数据管理](ch10.zh-cn.html) ]{.chapter}

[ [10.1. 共享，拷贝和存档](ch10.zh-cn.html#_sharing_copying_and_archiving) ]{.section}

[ [10.1.1. 存档和压缩工具](ch10.zh-cn.html#_archive_and_compression_tools) ]{.section}

[ [10.1.2. 复制和同步工具](ch10.zh-cn.html#_copy_and_synchronization_tools) ]{.section}

[ [10.1.3. 归档语法](ch10.zh-cn.html#_idioms_for_the_archive) ]{.section}

[ [10.1.4. 复制语法](ch10.zh-cn.html#_idioms_for_the_copy) ]{.section}

[ [10.1.5. 查找文件的语法](ch10.zh-cn.html#_idioms_for_the_selection_of_files) ]{.section}

[ [10.1.6. 归档媒体](ch10.zh-cn.html#_archive_media) ]{.section}

[ [10.1.7. 可移动存储设备](ch10.zh-cn.html#_removable_storage_device) ]{.section}

[ [10.1.8. 选择用于分享数据的文件系统](ch10.zh-cn.html#_filesystem_choice_for_sharing_data) ]{.section}

[ [10.1.9. 网络上的数据分享](ch10.zh-cn.html#_sharing_data_via_network) ]{.section}

[ [10.2. 备份和恢复](ch10.zh-cn.html#_backup_and_recovery) ]{.section}

[ [10.2.1. 备份和恢复策略](ch10.zh-cn.html#_backup_and_recovery_policy) ]{.section}

[ [10.2.2. 实用备份套件](ch10.zh-cn.html#_backup_utility_suites) ]{.section}

[ [10.2.3. 备份技巧](ch10.zh-cn.html#_backup_tips) ]{.section}

[ [10.2.3.1. GUI（图形用户界面）备份](ch10.zh-cn.html#_gui_backup) ]{.section}

[ [10.2.3.2. 挂载事件触发的备份](ch10.zh-cn.html#_mount_event_triggered_backup) ]{.section}

[ [10.2.3.3. 时间事件触发的备份](ch10.zh-cn.html#_timer_event_triggered_backup) ]{.section}

[ [10.3. 数据安全基础](ch10.zh-cn.html#_data_security_infrastructure) ]{.section}

[ [10.3.1. GnuPG 密钥管理](ch10.zh-cn.html#_key_management_for_gnupg) ]{.section}

[ [10.3.2. 在文件上使用 GnuPG](ch10.zh-cn.html#_using_gnupg_on_files) ]{.section}

[ [10.3.3. 在 Mutt 中使用 GnuPG](ch10.zh-cn.html#_using_gnupg_with_mutt) ]{.section}

[ [10.3.4. 在 Vim 中使用 GnuPG](ch10.zh-cn.html#_using_gnupg_with_vim) ]{.section}

[ [10.3.5. MD5 校验和](ch10.zh-cn.html#_the_md5_sum) ]{.section}

[ [10.3.6. 密码密钥环](ch10.zh-cn.html#_password_keyring) ]{.section}

[ [10.4. 源代码合并工具](ch10.zh-cn.html#_source_code_merge_tools) ]{.section}

[ [10.4.1. 从源代码文件导出差异](ch10.zh-cn.html#_extracting_differences_for_source_files) ]{.section}

[ [10.4.2. 源代码文件移植更新](ch10.zh-cn.html#_merging_updates_for_source_files) ]{.section}

[ [10.4.3. 交互式移植](ch10.zh-cn.html#_interactive_merge) ]{.section}

[ [10.5. Git](ch10.zh-cn.html#_git) ]{.section}

[ [10.5.1. 配置 Git 客户端](ch10.zh-cn.html#_configuration_of_git_client) ]{.section}

[ [10.5.2. 基本的 Git 命令](ch10.zh-cn.html#_basic_git_commands) ]{.section}

[ [10.5.3. Git 技巧](ch10.zh-cn.html#_git_tips) ]{.section}

[ [10.5.4. Git 参考](ch10.zh-cn.html#_git_references) ]{.section}

[ [10.5.5. 其它的版本控制系统](ch10.zh-cn.html#_other_version_control_systems) ]{.section}

[ [11. 数据转换](ch11.zh-cn.html) ]{.chapter}

[ [11.1. 文本数据转换工具](ch11.zh-cn.html#_text_data_conversion_tools) ]{.section}

[ [11.1.1. 用 iconv 命令来转换文本文件](ch11.zh-cn.html#_converting_a_text_file_with_iconv) ]{.section}

[ [11.1.2. 用 iconv 检查文件是不是 UTF-8 编码](ch11.zh-cn.html#_checking_file_to_be_utf_8_with_iconv) ]{.section}

[ [11.1.3. 使用 iconv 转换文件名](ch11.zh-cn.html#_converting_file_names_with_iconv) ]{.section}

[ [11.1.4. 换行符转换](ch11.zh-cn.html#_eol_conversion) ]{.section}

[ [11.1.5. TAB 转换](ch11.zh-cn.html#_tab_conversion) ]{.section}

[ [11.1.6. 带有自动转换功能的编辑器](ch11.zh-cn.html#_editors_with_auto_conversion) ]{.section}

[ [11.1.7. 提取纯文本](ch11.zh-cn.html#_plain_text_extraction) ]{.section}

[ [11.1.8. 高亮并格式化纯文本数据](ch11.zh-cn.html#_highlighting_and_formatting_plain_text_data) ]{.section}

[ [11.2. XML 数据](ch11.zh-cn.html#_xml_data) ]{.section}

[ [11.2.1. XML 的基本提示](ch11.zh-cn.html#_basic_hints_for_xml) ]{.section}

[ [11.2.2. XML 处理](ch11.zh-cn.html#_xml_processing) ]{.section}

[ [11.2.3. XML 数据提取](ch11.zh-cn.html#_the_xml_data_extraction) ]{.section}

[ [11.2.4. XML 数据检查](ch11.zh-cn.html#_the_xml_data_lint) ]{.section}

[ [11.3. 排版](ch11.zh-cn.html#_type_setting) ]{.section}

[ [11.3.1. roff 排版](ch11.zh-cn.html#_roff_typesetting) ]{.section}

[ [11.3.2. TeX/LaTeX](ch11.zh-cn.html#_tex_latex) ]{.section}

[ [11.3.3. 漂亮的打印手册页](ch11.zh-cn.html#_pretty_print_a_manual_page) ]{.section}

[ [11.3.4. 创建手册页](ch11.zh-cn.html#_creating_a_manual_page) ]{.section}

[ [11.4. 可打印的数据](ch11.zh-cn.html#_printable_data) ]{.section}

[ [11.4.1. Ghostscript](ch11.zh-cn.html#_ghostscript) ]{.section}

[ [11.4.2. 合并两个 PS 或 PDF 文件](ch11.zh-cn.html#_merge_two_ps_or_pdf_files) ]{.section}

[ [11.4.3. 处理可印刷数据的工具](ch11.zh-cn.html#_printable_data_utilities) ]{.section}

[ [11.4.4. 用 CUPS 打印](ch11.zh-cn.html#_printing_with_cups) ]{.section}

[ [11.5. 邮件数据转换](ch11.zh-cn.html#_the_mail_data_conversion) ]{.section}

[ [11.5.1. 邮件数据基础](ch11.zh-cn.html#_mail_data_basics) ]{.section}

[ [11.6. 图形数据工具](ch11.zh-cn.html#_graphic_data_tools) ]{.section}

[ [11.6.1. 图形数据工具（元软件包）](ch11.zh-cn.html#_graphic_data_tools_meta) ]{.section}

[ [11.6.2. 图形数据工具（GUI 图形用户界面）](ch11.zh-cn.html#_graphic_data_tools_gui) ]{.section}

[ [11.6.3. 图形数据工具 (CLI 命令行)](ch11.zh-cn.html#_graphic_data_tools_cli) ]{.section}

[ [11.7. 不同种类的数据转换工具](ch11.zh-cn.html#_miscellaneous_data_conversion) ]{.section}

[ [12. 编程](ch12.zh-cn.html) ]{.chapter}

[ [12.1. Shell 脚本](ch12.zh-cn.html#_the_shell_script) ]{.section}

[ [12.1.1. POSIX shell 兼容性](ch12.zh-cn.html#_posix_shell_compatibility) ]{.section}

[ [12.1.2. Shell 参数](ch12.zh-cn.html#_shell_parameters) ]{.section}

[ [12.1.3. Shell 条件语句](ch12.zh-cn.html#_shell_conditionals) ]{.section}

[ [12.1.4. shell 循环](ch12.zh-cn.html#_shell_loops) ]{.section}

[ [12.1.5. Shell 环境变量](ch12.zh-cn.html#_shell_environment_variables) ]{.section}

[ [12.1.6. shell 命令行的处理顺序](ch12.zh-cn.html#_the_shell_command_line_processing_sequence) ]{.section}

[ [12.1.7. 用于 shell 脚本的应用程序](ch12.zh-cn.html#_utility_programs_for_shell_script) ]{.section}

[ [12.2. 解释性语言中的脚本](ch12.zh-cn.html#_scripting_in_interpreted_languages) ]{.section}

[ [12.2.1. 调试解释性语言代码](ch12.zh-cn.html#_debugging_interpreter_codes) ]{.section}

[ [12.2.2. 使用 shell 脚本的 GUI 程序](ch12.zh-cn.html#_gui_program_with_the_shell_script) ]{.section}

[ [12.2.3. 定制 GUI（图形用户界面）文件管理器的行为](ch12.zh-cn.html#_custom_actions_for_gui_filer) ]{.section}

[ [12.2.4. Perl 短脚本的疯狂](ch12.zh-cn.html#_perl_short_script_madness) ]{.section}

[ [12.3. 编译型语言代码](ch12.zh-cn.html#_coding_in_compiled_languages) ]{.section}

[ [12.3.1. C](ch12.zh-cn.html#_c) ]{.section}

[ [12.3.2. 简单的 C 程序（gcc）](ch12.zh-cn.html#_simple_c_program_gcc) ]{.section}

[ [12.3.3. Flex --- 一个更好的 Lex](ch12.zh-cn.html#_flex_a_better_lex) ]{.section}

[ [12.3.4. Bison --- 一个更好的 Yacc](ch12.zh-cn.html#_bison_a_better_yacc) ]{.section}

[ [12.4. 静态代码分析工具](ch12.zh-cn.html#_static_code_analysis_tools) ]{.section}

[ [12.5. 调试](ch12.zh-cn.html#_debug) ]{.section}

[ [12.5.1. 基本的 gdb 使用命令](ch12.zh-cn.html#_basic_gdb_execution) ]{.section}

[ [12.5.2. 调试 Debian 软件包](ch12.zh-cn.html#_debugging_the_debian_package) ]{.section}

[ [12.5.3. 获得栈帧](ch12.zh-cn.html#_obtaining_backtrace) ]{.section}

[ [12.5.4. 高级 gdb 命令](ch12.zh-cn.html#_advanced_gdb_commands) ]{.section}

[ [12.5.5. 检查库依赖性](ch12.zh-cn.html#_check_dependency_on_libraries) ]{.section}

[ [12.5.6. 动态调用跟踪工具](ch12.zh-cn.html#_dynamic_call_tracing_tools) ]{.section}

[ [12.5.7. 调试与 X 相关的错误](ch12.zh-cn.html#_debugging_x_errors) ]{.section}

[ [12.5.8. 内存泄漏检测工具](ch12.zh-cn.html#_memory_leak_detection_tools) ]{.section}

[ [12.5.9. 反汇编二进制程序](ch12.zh-cn.html#_disassemble_binary) ]{.section}

[ [12.6. 编译工具](ch12.zh-cn.html#_build_tools) ]{.section}

[ [12.6.1. make](ch12.zh-cn.html#_make) ]{.section}

[ [12.6.2. Autotools（自动化工具）](ch12.zh-cn.html#_autotools) ]{.section}

[ [12.6.2.1. 编译并安装程序](ch12.zh-cn.html#_compile_and_install_a_program) ]{.section}

[ [12.6.2.2. 卸载程序](ch12.zh-cn.html#_uninstall_program) ]{.section}

[ [12.6.3. Meson](ch12.zh-cn.html#_meson) ]{.section}

[ [12.7. Web](ch12.zh-cn.html#_web) ]{.section}

[ [12.8. 源代码转换](ch12.zh-cn.html#_the_source_code_translation) ]{.section}

[ [12.9. 制作 Debian 包](ch12.zh-cn.html#_making_debian_package) ]{.section}

[ [A. 附录](apa.zh-cn.html) ]{.appendix}

[ [A.1. Debian 迷宫](apa.zh-cn.html#_the_debian_maze) ]{.section}

[ [A.2. 版权历史](apa.zh-cn.html#_copyright_history) ]{.section}

[ [A.3. 简体中文翻译](apa.zh-cn.html#_zh-CN_translate) ]{.section}

[ [A.4. 文档格式](apa.zh-cn.html#_document_format) ]{.section}
:::

::: list-of-tables
**表格清单**

1.1. [有趣的文本模式程序包列表](ch01.zh-cn.html#listofinterestineprogrampackages)

1.2. [软件包信息文档列表](ch01.zh-cn.html#listofinformativentationpackages)

1.3. [重要目录的用途列表](ch01.zh-cn.html#listofusageofkeydirectories)

1.4. ["`ls -l`{.literal}"输出的第一个字符列表](ch01.zh-cn.html#listofthefirstchacteroflsloutput)

1.5. [`chmod`{.literal}(1) 命令文件权限的数字模式](ch01.zh-cn.html#thenumericmodefoinchmodbcommands)

1.6. [[umask]{.strong} 值举例](ch01.zh-cn.html#theumaskvalueexamples)

1.7. [关于文件访问的由系统提供的著名组列表](ch01.zh-cn.html#listofnotablesysupsforfileaccess)

1.8. [著名的由系统提供用于特定命令运行的组列表](ch01.zh-cn.html#listofnotablesysommandexecutions)

1.9. [时间戳类型列表](ch01.zh-cn.html#listoftypesoftimestamps)

1.10. [特殊设备文件列表](ch01.zh-cn.html#listofspecialdevicefiles)

1.11. [MC 快捷键绑定](ch01.zh-cn.html#thekeybindingsofmc)

1.12. [MC 中对回车键的响应](ch01.zh-cn.html#thereactiontotheenterkeyinmc)

1.13. [shell 程序列表](ch01.zh-cn.html#list-of-shell-programs)

1.14. [bash 的按键绑定列表](ch01.zh-cn.html#listofkeybindingsforbash)

1.15. [Debian上的鼠标操作和相关按键操作列表](ch01.zh-cn.html#listofmouseoperayactionsondebian)

1.16. [基本的 Vim 按键列表](ch01.zh-cn.html#listofbasicvimkeystrokes)

1.17. [基本的 Unix 命令列表](ch01.zh-cn.html#listofbasicunixcommands)

1.18. [语言环境值的 3 个部分](ch01.zh-cn.html#thedpartsoflocalevalue)

1.19. [语言环境推荐列表](ch01.zh-cn.html#listoflocalerecommendations)

1.20. [\"`$HOME`{.literal}\" 变量值列表](ch01.zh-cn.html#listofhomevalues)

1.21. [Shell glob 模式](ch01.zh-cn.html#shellglobpatterns)

1.22. [命令的退出代码](ch01.zh-cn.html#commandexitcodes)

1.23. [Shell 命令常见用法](ch01.zh-cn.html#shellcommandidioms)

1.24. [预定义的文件描述符](ch01.zh-cn.html#predefinedfiledescriptors)

1.25. [BRE 和 ERE 中的元字符](ch01.zh-cn.html#metacharactersforbreandere)

1.26. [替换表达式](ch01.zh-cn.html#thereplacementexpression)

1.27. [管道命令的小片段脚本列表](ch01.zh-cn.html#listofscriptsniporpipingcommands)

2.1. [Debian 软件包管理工具列表](ch02.zh-cn.html#listofdebianpackemanagementtools)

2.2. [Debian 档案库站点列表](ch02.zh-cn.html#listofdebianarchivesites)

2.3. [Debian 归档区域（area）列表](ch02.zh-cn.html#listofdebianarchivearea)

2.4. [套件和代号的关系](ch02.zh-cn.html#therelationshipbsuiteandcodename)

2.5. [解决特定软件包问题的主要网站](ch02.zh-cn.html#listofkeywebsiteaspecificpackage)

2.6. [使用 `apt`{.literal}(8), `aptitude`{.literal}(8) 和 `apt-get`{.literal}(8) / `apt-cache`{.literal}(8) 的命令行基本软件包管理操作](ch02.zh-cn.html#basicpackagemanaaptgetiaptcachei)

2.7. [`aptitude`{.literal}(8) 中重要的命令选项](ch02.zh-cn.html#notablecommandopionsforaptitudei)

2.8. [aptitude 的按键绑定](ch02.zh-cn.html#listofkeybindingsforaptitude)

2.9. [aptitude 视图](ch02.zh-cn.html#listofviewsforaptitude)

2.10. [标准软件包视图的分类](ch02.zh-cn.html#standard-package-views)

2.11. [aptitude 正则表达式](ch02.zh-cn.html#listoftheaptituderegexformula)

2.12. [软件包活动日志文件](ch02.zh-cn.html#thelogfilesforpackageactivities)

2.13. [高级软件包管理操作](ch02.zh-cn.html#listofadvancedpagementoperations)

2.14. [Debian 档案库元数据的内容](ch02.zh-cn.html#thecontentofthednarchivemetadata)

2.15. [Debian 软件包的名称结构](ch02.zh-cn.html#thenamestructureofdebianpackages)

2.16. [Debian 软件包名称中每一个组件可以使用的字符](ch02.zh-cn.html#theusablecharactbianpackagenames)

2.17. [`dpkg`{.literal} 创建的重要文件](ch02.zh-cn.html#thenotablefilescreatedbydpkg)

2.18. [用于 [apt-pinning]{.strong} 技术的值得注意的 Pin-Priority 值列表。](ch02.zh-cn.html#listofnotablepinpinningtechnique)

2.19. [Debian 档案库的专用代理工具](ch02.zh-cn.html#listoftheproxytofordebianarchive)

3.1. [引导加载程序列表](ch03.zh-cn.html#listofbootloaders)

3.2. [`/boot/grub/grub.cfg`{.literal} 文件上面部分菜单条目意义](ch03.zh-cn.html#themeaningofthemfbootgrubgrubcfg)

3.3. [Debian 系统启动工具列表](ch03.zh-cn.html#listofbootutilitrthedebiansystem)

3.4. [内核错误级别表](ch03.zh-cn.html#listofkernelerrorlevels)

3.5. [典型的 `journalctl`{.literal} 命令片段列表](ch03.zh-cn.html#listoftypicaljoulcommandsnippets)

3.6. [典型的 `systemctl`{.literal} 命令片段列表](ch03.zh-cn.html#listoftypicalsyslcommandsnippets)

3.7. [`systemd`{.literal} 下其它零星监控命令列表](ch03.zh-cn.html#listofothermonitpetsundersystemd)

4.1. [`pam_unix`{.literal}(8) 使用的 3 个重要配置文件](ch04.zh-cn.html#dimportantconfigilesforpam_unixi)

4.2. ["`/etc/passwd`{.literal}" 第二项的内容](ch04.zh-cn.html#thesecondentrycontentofetcpasswd)

4.3. [管理账号信息的命令](ch04.zh-cn.html#listofcommandstocountinformation)

4.4. [生成密码的工具](ch04.zh-cn.html#listoftoolstogeneratepassword)

4.5. [PAM 和 NSS 系统中重要的软件包](ch04.zh-cn.html#listofnotablepamandnsssystems)

4.6. [PAM 和 NSS 访问的配置文件](ch04.zh-cn.html#listofconfiguratessedbypamandnss)

4.7. [安全和不安全的服务端口列表](ch04.zh-cn.html#listofinsecureanservicesandports)

4.8. [提供额外安全方式的工具列表](ch04.zh-cn.html#listoftoolstoprosecuritymeasures)

5.1. [网络配置工具一览表](ch05.zh-cn.html#listofnetworkconfigurationtools)

5.2. [网络地址范围列表](ch05.zh-cn.html#listofnetworkaddressranges)

5.3. [从旧的 `net-tools`{.literal} 命令集到新的 `iproute2`{.literal} 命令集转换表](ch05.zh-cn.html#translationtableiprouteccommands)

5.4. [底层网络命令列表](ch05.zh-cn.html#listoflowlevelnetworkcommands)

5.5. [网络优化工具列表](ch05.zh-cn.html#listofnetworkoptimizationtools)

5.6. [最佳 MTU 值的基本指引方法](ch05.zh-cn.html#basicguidelinesoeoptimalmtuvalue)

5.7. [防火墙工具列表](ch05.zh-cn.html#listoffirewalltools)

6.1. [网页浏览器列表](ch06.zh-cn.html#listofwebbrowsers)

6.2. [邮件用户代理列表 (MUA)](ch06.zh-cn.html#listofmailuseragentmua)

6.3. [基础的邮件传输代理相关的软件包列表](ch06.zh-cn.html#listofbasicmailttrelatedpackages)

6.4. [重要的 postfix 手册页列表](ch06.zh-cn.html#listofimportantpstfixmanualpages)

6.5. [与邮件地址相关的配置文件列表](ch06.zh-cn.html#listofmailaddresnfigurationfiles)

6.6. [基础 MTA 操作列表](ch06.zh-cn.html#listofbasicmtaoperation)

6.7. [服务器远程访问和工具列表](ch06.zh-cn.html#listofremoteaccerverandutilities)

6.8. [SSH 配置文件列表](ch06.zh-cn.html#listofsshconfigurationfiles)

6.9. [SSH 客户端启动例子列表](ch06.zh-cn.html#listofsshclientstartupexamples)

6.10. [其它平台上免费 SSH 客户端列表](ch06.zh-cn.html#listoffreesshcliorotherplatforms)

6.11. [打印服务和工具列表](ch06.zh-cn.html#listofprintserversandutilities)

6.12. [其它网络应用服务列表](ch06.zh-cn.html#listofothernetwoplicationservers)

6.13. [网络应用客户端列表](ch06.zh-cn.html#listofnetworkapplicationclients)

6.14. [常用 RFC 列表](ch06.zh-cn.html#listofpopularrfcs)

7.1. [桌面环境列表](ch07.zh-cn.html#listofdesktopenvironment)

7.2. [著名的 GUI 架构软件包列表](ch07.zh-cn.html#listofnotableguitructurepackages)

7.3. [著名的的 GUI（图形用户界面）应用列表](ch07.zh-cn.html#listofnotableguiapplications)

7.4. [著名的 TrueType 和 OpenType 字体列表](ch07.zh-cn.html#listofnotabletruandopentypefonts)

7.5. [著名的字体环境和相关软件包列表](ch07.zh-cn.html#listofnotablefondrelatedpackages)

7.6. [著名的沙盒环境和相关软件包列表](ch07.zh-cn.html#listofnotablesandrelatedpackages)

7.7. [著名的远程访问服务端列表](ch07.zh-cn.html#listofnotableremoteaccessserver)

7.8. [连接到 X 服务端的方式](ch07.zh-cn.html#listofconnectionhodstothexserver)

7.9. [操作字符剪贴板相关程序列表](ch07.zh-cn.html#listofprogramsrearacterclipboard)

8.1. [IBus 和它的引擎软件包列表](ch08.zh-cn.html#listofibusanditsenginepackages)

8.2. [Fcitx5 和它的引擎软件包列表](ch08.zh-cn.html#listoffcitxfanditsenginepackages)

9.1. [支持控制台活动的程序列表](ch09.zh-cn.html#listofprogramstoonsoleactivities)

9.2. [screen 键绑定列表](ch09.zh-cn.html#listofkeybindingsforscreen)

9.3. [`vim`{.literal} 的初始化信息](ch09.zh-cn.html#informationonthetializationofvim)

9.4. [系统日志分析软件列表](ch09.zh-cn.html#listofsystemloganalyzers)

9.5. [使用 [时间样式值]{.strong} 的\"`ls -l`{.literal}\" 命令的时间和日期的显示例子](ch09.zh-cn.html#displayexamplesohetimestylevalue)

9.6. [图形图像处理工具列表](ch09.zh-cn.html#listofgraphicsimanipulationtools)

9.7. [记录配置历史的软件包列表](ch09.zh-cn.html#listofpackageswhigurationhistory)

9.8. [监控和控制程序活动工具列表](ch09.zh-cn.html#listoftoolsformorogramactivities)

9.9. [调度优先级值列表](ch09.zh-cn.html#listofnicevalueshedulingpriority)

9.10. [ps 命令样式列表](ch09.zh-cn.html#listofpscommandstyles)

9.11. [kill 命令常用信号列表](ch09.zh-cn.html#listoffrequentlylsforkillcommand)

9.12. [著名的 SAK 命令键列表](ch09.zh-cn.html#listofnotablesakcommandkeys)

9.13. [硬件识别工具列表](ch09.zh-cn.html#listofhardwareidntificationtools)

9.14. [硬件配置工具列表](ch09.zh-cn.html#listofhardwareconfigurationtools)

9.15. [声音软件包](ch09.zh-cn.html#listofsoundpackages)

9.16. [关闭屏幕保护命令列表](ch09.zh-cn.html#listofcommandsfongthescreensaver)

9.17. [报告的内存大小](ch09.zh-cn.html#listofmemorysizesreported)

9.18. [用于系统安全性和完整性检查的工具](ch09.zh-cn.html#listoftoolsforsyndintegritycheck)

9.19. [硬盘分区管理软件包](ch09.zh-cn.html#listofdiskpartitnagementpackages)

9.20. [文件系统管理包列表](ch09.zh-cn.html#listoffilesystemnagementpackages)

9.21. [查看和修改二进制数据的软件包列表](ch09.zh-cn.html#listofpackageswhndeditbinarydata)

9.22. [不挂载磁盘操作文件的软件包列表](ch09.zh-cn.html#listofpackagestohoutmountingdisk)

9.23. [向文件添加数据冗余的工具列表](ch09.zh-cn.html#listoftoolstoaddedundancytofiles)

9.24. [数据文件恢复和诊断分析软件包列表](ch09.zh-cn.html#listofpackagesfoforensicanalysis)

9.25. [数据加密工具列表](ch09.zh-cn.html#listofdataencryptionutilities)

9.26. [Debian 系统内核编译需要安装的主要软件包列表](ch09.zh-cn.html#listofkeypackagenthedebiansystem)

9.27. [虚拟化工具列表](ch09.zh-cn.html#listofvirtualizationtools)

10.1. [存档和压缩工具列表](ch10.zh-cn.html#listofarchiveandcompressiontools)

10.2. [复制和同步工具列表](ch10.zh-cn.html#listofcopyandsynhronizationtools)

10.3. [典型使用场景下可移动存储设备可选择的文件系统列表](ch10.zh-cn.html#listoffilesystemalusagescenarios)

10.4. [典型使用场景下可选择的网络服务列表](ch10.zh-cn.html#listofthenetworkcalusagescenario)

10.5. [实用备份程序套件列表](ch10.zh-cn.html#listofbackupsuiteutilities)

10.6. [数据安全基础工具列表](ch10.zh-cn.html#listofdatasecurirastructuretools)

10.7. [GNU 隐私卫士密钥管理命令的列表](ch10.zh-cn.html#listofgnuprivacythekeymanagement)

10.8. [信任码含义列表](ch10.zh-cn.html#listofthemeaningofthetrustcode)

10.9. [在文件上使用的 GNU 隐私卫士的命令列表](ch10.zh-cn.html#listofgnuprivacydcommandsonfiles)

10.10. [源代码合并工具列表](ch10.zh-cn.html#listofsourcecodemergetools)

10.11. [git 相关包和命令列表](ch10.zh-cn.html#listofgitrelatedkagesandcommands)

10.12. [主要的 Git 命令](ch10.zh-cn.html#maingitcommands)

10.13. [Git 技巧](ch10.zh-cn.html#gittips)

10.14. [其它版本控制系统工具列表](ch10.zh-cn.html#list-of-vcs)

11.1. [文本数据转化工具列表](ch11.zh-cn.html#listoftextdataconversiontools)

11.2. [编码值和用法的列表](ch11.zh-cn.html#list-of-encoding-values)

11.3. [不同平台的换行符样式列表](ch11.zh-cn.html#listofeolstylesffferentplatforms)

11.4. [`bsdmainutils`{.literal} 和 `coreutils`{.literal} 包中的用于转换 TAB 的命令列表](ch11.zh-cn.html#listoftabconversoreutilspackages)

11.5. [用于提取纯文本数据的工具列表](ch11.zh-cn.html#listoftoolstoextactplaintextdata)

11.6. [高亮纯文本数据的工具列表](ch11.zh-cn.html#listoftoolstohigghtplaintextdata)

11.7. [XML 预定义实体列表](ch11.zh-cn.html#listofpredefinedentitiesforxml)

11.8. [XML 工具列表](ch11.zh-cn.html#listofxmltools)

11.9. [DSSSL 工具列表](ch11.zh-cn.html#listofdsssltools)

11.10. [XML 数据提取工具列表](ch11.zh-cn.html#listofxmldataextractiontools)

11.11. [XML 美化打印工具列表](ch11.zh-cn.html#listofxmlprettyprinttools)

11.12. [排版工具的列表](ch11.zh-cn.html#listoftypesettingtools)

11.13. [创建手册页的工具列表](ch11.zh-cn.html#listofpackagestoeatingthemanpage)

11.14. [Ghostscript PostScript 解释器列表](ch11.zh-cn.html#listofghostscripriptinterpreters)

11.15. [处理可印刷数据的工具列表](ch11.zh-cn.html#listofprintabledatautilities)

11.16. [有助于邮件数据转换的软件包列表](ch11.zh-cn.html#listofpackagestoildataconversion)

11.17. [图形数据工具列表（元软件包）](ch11.zh-cn.html#listofgraphicsdatoolsmetapackage)

11.18. [图形数据工具（GUI 图形用户界面）列表](ch11.zh-cn.html#listofgraphicsdatatoolsgui)

11.19. [图形数据工具(CLI 命令行)列表](ch11.zh-cn.html#listofgraphicsdatatoolscli)

11.20. [不同种类的数据转换工具列表](ch11.zh-cn.html#listofmiscellaneaconversiontools)

12.1. [典型 bashism 语法列表](ch12.zh-cn.html#listoftypicalbashisms)

12.2. [shell 参数列表](ch12.zh-cn.html#listofshellparameters)

12.3. [shell 参数展开列表](ch12.zh-cn.html#listofshellparameterexpansions)

12.4. [重要的 shell 参数替换列表](ch12.zh-cn.html#listofkeyshellpatersubstitutions)

12.5. [在条件表达式中进行文件比较](ch12.zh-cn.html#listoffilecompartionalexpression)

12.6. [在条件表达式中进行字符串比较](ch12.zh-cn.html#listofstringcomptionalexpression)

12.7. [包含用于 shell 脚本的小型应用程序的软件包](ch12.zh-cn.html#listofpackagescosforshellscripts)

12.8. [解释器相关软件包列表](ch12.zh-cn.html#listofinterpreterrelatedpackages)

12.9. [对话（dialog ）程序列表](ch12.zh-cn.html#listofdialogprograms)

12.10. [编译相关软件包列表](ch12.zh-cn.html#listofcompilerrelatedpackages)

12.11. [兼容 Yacc 的 LALR 解析器生成器列表](ch12.zh-cn.html#listofyacccompatparsergenerators)

12.12. [静态代码分析工具的列表](ch12.zh-cn.html#listoftoolsforstaticcodeanalysis)

12.13. [调试软件包列表](ch12.zh-cn.html#listofdebugpackages)

12.14. [高级 gdb 命令列表](ch12.zh-cn.html#listofadvancedgdbcommands)

12.15. [内存泄漏检测工具的列表](ch12.zh-cn.html#listofmemoryleakdetectiontools)

12.16. [编译工具软件包列表](ch12.zh-cn.html#listofbuildtoolpackages)

12.17. [自动变量的列表](ch12.zh-cn.html#listofmakeautomaticvariables)

12.18. [变量扩展的列表](ch12.zh-cn.html#listofmakevariableexpansions)

12.19. [源代码转换工具列表](ch12.zh-cn.html#listofsourcecodetranslationtools)
:::
:::::::::::::::

::: navfooter

------------------------------------------------------------------------

  --- --- ---------------------------------------------------------------
             [![下一页](images/next.png)](pr01.zh-cn.html){accesskey="n"}
                                                                     序言
  --- --- ---------------------------------------------------------------
:::
