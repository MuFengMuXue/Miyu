**Resources**

[[]][Home](https://motion-project.github.io)

[[]][Package information](https://packages.gentoo.org/packages/media-video/motion)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Motion_(surveillance_software) "wikipedia:Motion (surveillance software)")

[Motion] is a software package able to use cameras to detect motion.

It supports different camera types:

-   Network cameras via RTSP, RTMP and HTTP
-   V4L2 webcams
-   Video capture cards
-   Existing movie files

Once [motion] detects motion it can write picture files and/or movie files to a storage location.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Optimization]](#Optimization)
    -   [[3.1] [Video codec]](#Video_codec)
    -   [[3.2] [Hardware acceleration]](#Hardware_acceleration)
    -   [[3.3] [Motion tuning parameters]](#Motion_tuning_parameters)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [Commandline]](#Commandline)
    -   [[4.2] [Service]](#Service)
        -   [[4.2.1] [OpenRC]](#OpenRC)
-   [[5] [Security]](#Security)
    -   [[5.1] [Password protection]](#Password_protection)
    -   [[5.2] [SSL/TLS]](#SSL.2FTLS)
    -   [[5.3] [Restrict webcontrol and streams to localhost]](#Restrict_webcontrol_and_streams_to_localhost)
-   [[6] [Database]](#Database)
-   [[7] [Housekeeping]](#Housekeeping)

## [Installation]

### [Kernel]

The linux kernel needs to be configured for V4L in case such cameras are being used.

[KERNEL] **Enable support for V4L**

    Device Drivers --->
    <M> Multimedia support  --->
        [*] Media Controller API
        [*] V4L2 sub-device userspace API
        [*] Media USB Adapters  --->
            <M> USB Video Class (UVC)
            [*]   UVC input events device support
            <M> GSPCA based webcams  --->
                ** select the correct GSPCA camera, if any **
            ** select the correct USB camera, if any **
        [*] Media PCI Adapters  --->
            ** select the correct PCI camera devices, if any ***
        [*] V4L platform devices  --->
            ** select the correct V4L platform devices, if any **
        [*] Autoselect ancillary drivers (tuners, sensors, i2c, spi, frontends)
    [*] USB support  --->
        <M> USB Gadget Support  --->
            <M> USB Gadget functions configurable through configfs
            <M> USB Webcam Gadget

### [USE flags]

### [USE flags for] [media-video/motion](https://packages.gentoo.org/packages/media-video/motion) [[]] [A software motion detector]

  ------------------------------------------------------------- ------------------------------------------------------------------------------------
  [`ffmpeg`](https://packages.gentoo.org/useflags/ffmpeg)       Enable ffmpeg/libav-based audio/video codec support
  [`mariadb`](https://packages.gentoo.org/useflags/mariadb)     Add mariadb database support
  [`mysql`](https://packages.gentoo.org/useflags/mysql)         Add mySQL Database support
  [`postgres`](https://packages.gentoo.org/useflags/postgres)   Add support for the postgresql database
  [`sqlite`](https://packages.gentoo.org/useflags/sqlite)       Add support for sqlite - embedded sql database
  [`v4l`](https://packages.gentoo.org/useflags/v4l)             Enable support for video4linux (using linux-headers or userspace libv4l libraries)
  [`webp`](https://packages.gentoo.org/useflags/webp)           Add support for the WebP image format
  ------------------------------------------------------------- ------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-05 08:44] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

[Motion] is in portage, emerge it as per normal:

`root `[`#`]`emerge --ask --verbose media-video/motion`

## [Configuration]

After emerging sample configuration files are placed in [/etc/motion]:

`root `[`#`]`ls /etc/motion`

    drwxr-xr-x 1 root root   390 Apr 10 15:14 .
    drwxr-xr-x 1 root root  3616 Apr 10 13:31 ..
    -rw-r--r-- 1 root root  2772 Apr  9 19:54 /etc/motion/camera1-dist.conf
    -rw-r--r-- 1 root root  2771 Apr  9 19:54 /etc/motion/camera2-dist.conf
    -rw-r--r-- 1 root root  2772 Apr  9 19:54 /etc/motion/camera3-dist.conf
    -rw-r--r-- 1 root root  2772 Apr  9 19:54 /etc/motion/camera4-dist.conf
    -rw-r--r-- 1 root root 27681 Apr  9 19:54 /etc/motion/motion-dist.conf

These configuration files are well documented, and can be used for creating the actual configuration files. The actual configuration files do not have \"-dist\" in their name. Note that simple renaming the files will not yield a working configuration. It may be better to create the configuration files from scratch, taking note of the individual settings needed for camera(s), and desired output options.

The structure of the configuration files is as follows:

-   [motion.conf]: contains the general and daemon settings.
-   [camera#.conf] contains the settings per camera.

[Motion] looks for the configuration files in the following order:

-   in the current working directory
-   in [\~/.motion]
-   in [/etc/motion]

** Note**\
Be aware that some of the configuration file parameters have been deprecated over time, e.g. the ffmpeg_bps parameter is now called movie_bps. Please refer to [this table](//motion-project.github.io/motion_config.html#Configuration_OptionsAlpha) on the [motion] website for details.

An example working set of configuration files for two cameras, one laptop webcam and one IP-camera is as follows.

General settings:

[FILE] **`/etc/motion/motion.conf`**

    log_level 5
    webcontrol_port 8080
    webcontrol_authentication <username:password>
    webcontrol_parms 2
    movie_output on
    movie_codec mkv
    movie_duplicate_frames false
    target_dir /tmp/motion
    output_pictures off
    camera /etc/motion/camera1.conf
    camera /etc/motion/camera2.conf

First camera, a webcam using V4L:

[FILE] **`/etc/motion/camera1.conf`**

    camera_id = 1
    camera_name = webcam
    videodevice /dev/video0
    stream_authentication <username:password>
    stream_motion on
    stream_maxrate 25
    stream_localhost on

Second camera, an IP camera:

[FILE] **`/etc/motion/camera2.conf`**

    camera_id = 2
    camera_name = livingroom
    netcam_userpass <username:password>
    netcam_url rtsp://IP-ADDRESS/stream2
    stream_authentication <username:password>
    stream_motion on
    stream_maxrate 25
    stream_localhost on

Make sure to update credentials and the URL. Please refer to [motion]\'s documentation for further details for the configuration.

## [Optimization]

[Motion] can be quite taxing on your hardware, especially if it is continuously receiving a stream of pictures, which it might need to process into video files, stream to client devices, and store somewhere on disk. It might be worth spending some time on optimization. With a modern the right optimization the system utilization could drop by as much 90%, YMMV depending on how hardware support there is available for the target system.

### [Video codec]

[Motion] supports different codecs via the parameter [movie_codec](//motion-project.github.io/motion_config.html#movie_codec). Some considerations for the choice of codec might be:

-   CPU load for the encoding: hardware acceleration might be configured to ease the load
-   Amount of disk space needed for storing the videos: some codecs are more efficient then others
-   Codec support on the devices that are used to view the video files: not all client devices support all codecs

### [Hardware acceleration]

Various CPUs and GPUs have support for offloading the task of encoding videos. A choice should to be made, depending on the video codec, the type of CPU and GPU available.

Follow the instructions at [GCC_optimization](https://wiki.gentoo.org/wiki/GCC_optimization "GCC optimization") to at least set the proper march and the CPU_FLAGS. This will configure the system to use specific instructions that can optimize video encoding, e.g. instructions like [SSSE3](https://en.wikipedia.org/wiki/SSSE3), [SSE4.2](https://en.wikipedia.org/wiki/SSE4#SSE4.2), [AVX](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions), [FMA3](https://en.wikipedia.org/wiki/FMA_instruction_set), [BMI2](https://en.wikipedia.org/wiki/Bit_Manipulation_Instruction_Sets#BMI2), and [AVX2](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#AVX2).

Evaluate the following articles to establish the support for hardware acceleration:

-   Intel CPUs:
    -   [Intel Quick Sync Video](https://en.wikipedia.org/wiki/Intel_Quick_Sync_Video#Hardware_decoding_and_encoding) hardware support
    -   [GuC/HuC firmware](https://wiki.gentoo.org/wiki/Intel#GuC.2FHuC_firmware "Intel")
-   AMD GPUs:
    -   [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU")
    -   [AMD\'s Video Coding Engine](https://en.wikipedia.org/wiki/Video_Coding_Engine)
    -   [AMD\'s Video Core Next](https://en.wikipedia.org/wiki/Video_Core_Next)
-   NVIDIA GPUs:
    -   [Nvidia\'s encode/decode support matrix](//developer.nvidia.com/video-encode-decode-gpu-support-matrix)

[Motion] uses [[[media-video/ffmpeg]](https://packages.gentoo.org/packages/media-video/ffmpeg)[]] for video encoding. Check [ffmpeg\'s hardware acceleration](//trac.ffmpeg.org/wiki/HWAccelIntro) for support.

Ffmpeg USE flags to consider include:

-   opencl
-   vaapi
-   vdpau

Support for Intel\'s libmfx is currently lacking in Gentoo, see [[[bug #590752]](https://bugs.gentoo.org/show_bug.cgi?id=590752)[]] for details. Note that hardware acceleration might require additional linux kernel configuration.

### [Motion tuning parameters]

[Motion] supports various configuration parameters which can be used for tuning purposes. These include:

-   framerate
-   movie_quality
-   movie_passthrough

Play around with it to establish the optimum between quality and resource utilization

## [Usage]

### [Commandline]

[Motion] can be simply run from the commandline for testing purposes:

`user `[`$`]`motion`

    [-1083001888:motion] [NTC] [ALL] conf_load: Processing thread 0 - config file /etc/motion/motion.conf
    [-1083001888:motion] [NTC] [ALL] config_camera: Processing camera config file /etc/motion/camera1.conf
    [-1083001888:motion] [NTC] [ALL] config_camera: Processing camera config file /etc/motion/camera2.conf
    [-1083001888:motion] [NTC] [ALL] motion_startup: Motion 4.1.1 Started
    [-1083001888:motion] [NTC] [ALL] motion_startup: Logging to syslog
    [-1083001888:motion] [NTC] [ALL] motion_startup: Using default log type (ALL)
    [-1083001888:motion] [NTC] [ALL] motion_startup: Using log type (ALL) log level (WRN)

Once [motion] runs, it provides a webpage at [[http://localhost:8080](http://localhost:8080)]. The webpage will show the live stream of the cameras, and allows for some basic control.

### [Service]

#### [OpenRC]

As of motion-4.3.1 there are new configuration parameters in [/etc/conf.d/motion]:

  ------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
  Parameter           Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           Default value
  MOTION_USER         The user [motion] will run under, provided by [[[acct-user/motion]](https://packages.gentoo.org/packages/acct-user/motion)[]]       motion
  MOTION_GROUP        The group [motion] will run under, provided by [[[acct-group/motion]](https://packages.gentoo.org/packages/acct-group/motion)[]]   motion
  MOTION_CONFIGFILE   [Motion] config file                                                                                                                                                                                                                                                                                                                                                                                                       /etc/motion/motion.conf
  MOTION_LOGFILE      A complete file name, e.g. /var/log/motion/motion.log                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Not set, meaning syslog
  MOTION_LOGTYPE      What [motion] should log: 1-9 for COR, STR, ENC, NET, DBL, EVT, TRK, VID, ALL                                                                                                                                                                                                                                                                                                                                              9, meaning all
  MOTION_LOGLEVEL     The amount of log messages: 1-9 for EMG, ALR, CRT, ERR, WRN, NTC, INF, DBG, ALL                                                                                                                                                                                                                                                                                                                                                                                                                                       6, meaning notice
  MOTION_DIR          Runtime default directory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             /var/lib/motion
  MOTION_UMASK        The umask that [motion] uses. Use 007 for read/write access by the same user and group motion runs under.                                                                                                                                                                                                                                                                                                                  Not set, meaning default umask.
  ------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------

Take note of the supervise-daemon USE flag, which, when set, will make [motion] run under [OpenRC\'s supervise-daemon](https://wiki.gentoo.org/wiki/OpenRC/supervise-daemon "OpenRC/supervise-daemon"). Once satisfied with the configuration start the [motion] daemon process:

`root `[`#`]`rc-config add motion default `

`root `[`#`]`rc-service motion start `

## [Security]

Whenever one uses cameras it should be done in a safe manner:

-   avoid to aim cameras at privacy sensitive areas
-   for IP cameras:
    -   use specific usernames or passwords on IP cameras; do not use default ones
    -   prevent direct access to or from the Internet to your cameras; block access on the firewall or router.

### [Password protection]

The webcontrol page and the streams can be protected with username and passwords, using three authentication mechanisms:\
0 = disabled\
1 = Basic authentication\
2 = MD5 digest (the safer authentication)

[FILE] **`/etc/motion/motion.conf`**

    webcontrol_authentication <username>:
    webcontrol_auth_method 2
    stream_authentication <username>:
    stream_auth_method 2

### [][SSL/TLS]

Motion-4.2.2 and later supports SSL/TLS, which is great if the webserver or the streams are exposed over LAN, WAN or the Internet. A few quick steps to get going.

It\'s possible to create own self signed certificates as follows:

`root `[`#`]`mkdir /etc/ssl/motion `

`root `[`#`]`cd /etc/ssl/motion `

`root `[`#`]`openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout motion.key -outform pem -out motion.pem -subj "/CN=*.com" `

`root `[`#`]`chown motion:motion motion.key motion.pem `

\
Update [/etc/motion/motion.conf]:

[FILE] **`/etc/motion/motion.conf`**

    webcontrol_key /etc/ssl/motion/motion.key
    webcontrol_cert /etc/ssl/motion/motion.pem
    webcontrol_tls on
    stream_tls on

The motion webserver is now accessible over https instead of http.

### [Restrict webcontrol and streams to localhost]

It might be a good idea to prevent the webcontrol page and/or the streams to be accessible on other computers:

[FILE] **`/etc/motion/motion.conf`**

    webcontrol_localhost on
    stream_localhost on

## [Database]

[Motion] contains functionality to log events in a database. Supported databases include [MySQL](https://wiki.gentoo.org/wiki/MySQL "MySQL"), [MariaDB](https://wiki.gentoo.org/wiki/MariaDB "MariaDB"), [Postgress](https://wiki.gentoo.org/wiki/PostgreSQL "PostgreSQL"), and [sqlite3](//sqlite.org). To use this functionality, the relevant USE flag has to be enabled, tables need to be created in the database, and the functionality need to be enabled in the configuration of [motion]. This chapter contains an example for sqlite, adapt as needed for other databases.

\
Create a sqlite database e.g. at [/data/motion.sqlite] and define a table called \"\"security\"\", as follows:

`root `[`#`]`sqlite3 /data/motion.sqlite`

    CREATE TABLE security (camera int, filename char(80) not null, frame int, file_type int, time_stamp timestamp(14), event_time_stamp timestamp(14), text_event char(80));

Exit with [Ctrl]-[D] .

\
Include the following to the [motion] configuration file:

[FILE] **`/etc/motion/motion.conf`**

    database_type sqlite3
    database_dbname /data/motion.sqlite
    sql_log_picture on
    sql_log_snapshot on
    sql_log_movie on
    sql_query insert into security(camera, filename, frame, file_type, time_stamp, text_event) values('%t', '%f', '%q', '%n', '%Y-%m-%d %T', '%C')

Now every time a new picture, snapshot or movie is created, a new entry with details is written in the database. An application can use these details to retrieve the relevant file.

## [Housekeeping]

Be aware that [motion] can produce many large files each day, which can take up a lot of storage. It might be a good idea to purge older files. Consider running a purging command like:

[CODE]

    /usr/bin/find <storage-location> -type f -mtime +<days> -delete

from a daily cron job, which would remove files older than \<days\> time from a folder \<storage-location\>.