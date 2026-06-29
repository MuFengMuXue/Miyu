Other languages:

[English] • ‎[français](//wiki.manjaro.org/index.php?title=Power_Management/fr "Gestion de l'énergie (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Power_Management/ru "Управление питанием (100% translated)") • ‎[中文（中国大陆）‎](//wiki.manjaro.org/index.php?title=Power_Management/zh-cn "电源管理 (17% translated)")

## Contents

-   [[1] [Power Management Software]](#Power_Management_Software)
    -   [[1.1] [TLP]](#TLP)
        -   [[1.1.1] [Installing TLP]](#Installing_TLP)
        -   [[1.1.2] [Configuring TLP]](#Configuring_TLP)
    -   [[1.2] [Laptop Mode Tools]](#Laptop_Mode_Tools)
        -   [[1.2.1] [Installing LMT]](#Installing_LMT)
        -   [[1.2.2] [LMT Configuration]](#LMT_Configuration)
    -   [[1.3] [PowerTOP]](#PowerTOP)
        -   [[1.3.1] [Installing PowerTop]](#Installing_PowerTop)
        -   [[1.3.2] [Generating Reports]](#Generating_Reports)
        -   [[1.3.3] [Automated Tuning with PowerTop]](#Automated_Tuning_with_PowerTop)
-   [[2] [Temperature/Thermal Management]](#Temperature.2FThermal_Management)
    -   [[2.1] [ThermalD]](#ThermalD)
-   [[3] [See Also]](#See_Also)

Power Saving techniques can be used to minimize the heat produced and conserve energy. On laptops, this can be especially important as it can significantly extend battery life and excessive heat can be both uncomfortable and loud on portable devices.

\

# [Power Management Software]

[![Battery.png](/images/thumb/6/6d/Battery.png/96px-Battery.png)](//wiki.manjaro.org/index.php?title=File:Battery.png)

\
There are several options for managing power under Manjaro. In this article, we will introduce three of the more popular options.

\

**Note**

------------------------------------------------------------------------

In most cases running more than one power management tool at a time can cause conflicts so it is best practice to only use one of the below options

\

## [TLP]

[TLP](http://linrunner.de/en/tlp/tlp.html) is the most commonly used option for automatic power management.

\

### [Installing TLP]

TLP is available from the Manjaro repositories, can be installed with your favorite package manager or by using entering the following command into your terminal:

    pamac install tlp

Now that it is installed, you need to start and enable the service. This can be accomplished with the command:

    systemctl enable tlp --now

\

**Note**

------------------------------------------------------------------------

TLP 1.2.2 and lower need another service as well: tlp-sleep.service

\

### [Configuring TLP]

[![Tlpui.png](/images/thumb/4/41/Tlpui.png/400px-Tlpui.png)](//wiki.manjaro.org/index.php?title=File:Tlpui.png)

\
TLP can manually configured by editing the file **/etc/default/tlp** as described in [The Official Documentation](http://linrunner.de/en/tlp/docs/tlp-configuration.html).

\
A simpler way to configure TLP is via the GUI tool [TLPUI](https://github.com/d4nj1/TLPUI)

\
To install TLPUI install the package **tlpui** using your favorite package manager or with the command

    pamac install tlpui

\

## [Laptop Mode Tools]

An Alternative to TLP for laptops is [Laptop Mode Tools(LMT)](https://github.com/rickysarraf/laptop-mode-tools).

\

### [Installing LMT]

To install `laptop-mode-tools`, enter the following command into your terminal:

    pamac install laptop-mode-tools

Once installed, to enable LMT to start automatically every time you boot your computer, enter the following into your terminal:

    sudo systemctl enable --now laptop-mode.service

LMT automatically configures some settings for you in order to optimize your laptop\'s battery life.

\

### [LMT Configuration]

For configuration, the file to edit is `/etc/laptop-mode/laptop-mode.conf`}

The individual kernel modules can be configured from the configuration files present in `/etc/laptop-mode/conf.d/`

\

## [PowerTOP]

PowerTop a diagnostic tool used to identify and report issues with power consumption and management. It can be used as a reporting tool, an automated power management tool or both.

\

### [Installing PowerTop]

It can be installed as

    pamac install powertop

\

### [Generating Reports]

You can generate a report using powertop with the command:

    sudo powertop --html

This will create the file `powertop.html` in the current directory. You can open this file in any web browser.

If you are using TLP for power management you may notice some differences in the recommendations between the tools. The article [Comparing TLP with PowerTop reporting](http://linrunner.de/en/tlp/docs/tlp-faq.html#powertop) describes some of the reasons for these differences.

\

### [Automated Tuning with PowerTop]

The command `sudo powertop --auto-tune"` will allow PowerTop to automatically tune power management based on it\'s recommendations.

From a practical perspective, the best way to use PowerTops auto-tuning is with a systemd service.

To create, start and enable a systemd service for PowerTop you can use the commands:

    sudo sh -c "echo -e '[Unit]\nDescription=PowerTop\n\n[Service]\nType=oneshot\nRemainAfterExit=true\nExecStart=/usr/bin/powertop --auto-tune\n\n[Install]\nWantedBy=multi-user.target\n' > /etc/systemd/system/powertop.service"
    sudo systemctl enable --now powertop.service

\

# [][Temperature/Thermal Management]

## [ThermalD]

[ThermalD](https://github.com/intel/thermal_daemon), the Linux Thermal Daemon can be used to automatically handle CPU frequency scaling according to system load.

To install it, install `thermald` in your favorite package manager or use the command:

    pamac install thermald

After installing it needs to be configured to automatically start at boot in order to work:

    sudo systemctl enable --now thermald

# [See Also]

-   [How to undervolt Intel CPUs](//wiki.manjaro.org/index.php?title=Undervolt_intel_CPU "Undervolt intel CPU")
-   [TLP website](http://linrunner.de/en/tlp/tlp.html)
-   [LaptopModeTools - Arch Wiki](https://wiki.archlinux.org/index.php/Laptop_Mode_Tools)
-   [TLP - Arch wiki](https://wiki.archlinux.org/index.php/TLP)