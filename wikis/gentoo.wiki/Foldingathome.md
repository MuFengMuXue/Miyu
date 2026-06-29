Installing folding@home on gentoo linux.

## Contents

-   [[1] [Install:]](#Install:)
-   [[2] [Configure:]](#Configure:)
-   [[3] [Openrc]](#Openrc)
-   [[4] [Systemd]](#Systemd)
    -   [[4.1] [Enable Suspend/Hibernate Resume.]](#Enable_Suspend.2FHibernate_Resume.)
    -   [[4.2] [Service files:]](#Service_files:)
        -   [[4.2.1] [enable the 2 service-units:]](#enable_the_2_service-units:)
        -   [[4.2.2] [System-sleep script:]](#System-sleep_script:)
        -   [[4.2.3] [make the script executable.]](#make_the_script_executable.)

## [Install:]

To install folding@home client\'s package, run:

`root `[`#`]`emerge --ask sci-biology/foldingathome`

The package will install in /opt directory.

## [Configure:]

`root `[`#`]`emerge --config =foldingathome-7.5.1 `

     Configuring pkg...

    ./FAHClient: /opt/foldingathome/libssl.so.10: no version information available (required by ./FAHClient)
    ./FAHClient: /opt/foldingathome/libcrypto.so.10: no version information available (required by ./FAHClient)
    ./FAHClient: /opt/foldingathome/libcrypto.so.10: no version information available (required by ./FAHClient)
    12:09:37:INFO(1):Read GPUs.txt
    User name [Anonymous]: myuser     (put the username that you want for the Folding@home-system)
    Team number [0]:
    Passkey:
    Enable SMP [true]:
    Enable GPU [true]:

    (replace version with the one just emerged.)

## [Openrc]

To start foldingathome\'s daemon:

`root `[`#`]`rc-service foldingathome start`

Once the service has been started, one can control it from the client\'s webpage: [client.foldingathome.org](https://client.foldingathome.org/).

To stop the daemon:

`root `[`#`]`rc-service foldingathome stop`

To add the foldingathome\'s daemon client to the default runlevel, run:

`root `[`#`]`rc-update add foldingathome default`

To remove the foldingathome\'s daemon client from the default runlevel, run:

`root `[`#`]`rc-update del foldingathome default`

## [Systemd]

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Foldingathome&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

### [][Enable Suspend/Hibernate Resume.]

When suspending or hibernating without stopping the foldingathome service OpenCl becomes inoperative, (after a suspend one must also reload the nvidia_uvm module.

### [Service files:]

[FILE] **`/etc/systemd/system/Stop_Foldingathome_before_Hibernate.service`**

    [Unit]
    Description=Stop foldingathome before hibernate
    Before=suspend.target
    Before=hibernate.target
    Before=hybrid-sleep.target

    [Service]
    ExecStart=/bin/bash -c "/bin/systemctl stop foldingathome"
    ExecStartPost=/bin/sleep 10

    [Install]
    WantedBy=suspend.target
    WantedBy=hibernate.target
    WantedBy=hybrid-sleep.target

[FILE] **`/etc/systemd/system/Start_Foldingathome_after_Hibernate.service`**

    [Unit]
    Description=Restart foldingathome after hibernate
    #After=suspend.target
    After=hibernate.target
    #After=hybrid-sleep.target

    [Service]
    Type=simple
    ExecStart=/bin/systemctl start foldingathome

    [Install]
    #WantedBy=suspend.target
    WantedBy=hibernate.target
    #WantedBy=hybrid-sleep.target

#### [enable the 2 service-units:]

`root `[`#`]`systemctl enable Stop_Foldingathome_before_Hibernate.service `

`root `[`#`]`systemctl enable Start_Foldingathome_after_Hibernate.service `

    !!!foldingathome-service is not started by the Start_Foldingathome_after_Hibernate-service!!!
    !!!we need also to reload teh nvidia_uvm module!!!
    !!!folingdathome is started by a suspend-resumescript (see next charpter)!!!

#### [System-sleep script:]

[FILE] **`/lib/systemd/system-sleep/suspend-resume.sh`**

    #!/bin/bash

    echo $1/$2

    case $1/$2 in
       pre/hibernate)
        echo "Going to $1 $2..."

        # flush caches before hibernating to save time on sleep/wakeup

        sync
        echo 1 > /proc/sys/vm/drop_caches
        sync
        echo 2 > /proc/sys/vm/drop_caches
        sync
        echo 3 > /proc/sys/vm/drop_caches
        sync

       ;;
       post/hibernate)
        echo "Waking up from $1 $2..."

       ;;
       pre/suspend)
        echo "Going to $2..."

       ;;
       post/suspend)
        echo "Waking up from $2..."

        # reload the nvidia_uvm module to enable cuda again after resume from suspend

        rmmod nvidia_uvm
        modprobe nvidia_uvm
        systemctl start foldingathome

       ;;
    esac

#### [make the script executable.]

`root `[`#`]`chmod a+x /lib/systemd/system-sleep/suspend-resume.sh `

    to do: procedure for other videocards.