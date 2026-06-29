Checkpoint Solutions\' proprietary VPN Firewall solution is called SSL Network Extender. This article documents the manual setup required to properly tunnel into this firewall from a Gentoo Linux host.

To access the VPN from a Linux host, a user logs into a web site using Firefox, then launches a Java applet, which runs a pre-installed local binary (snx) which initiates and configures the tunnel. The setup is elaborate and runs a setuid-root binary, so only attempt this if you trust the firewall server and its administrator, and if you are otherwise confident in the security of the Gentoo host.

## Contents

-   [[1] [Download the client install script]](#Download_the_client_install_script)
-   [[2] [Install the client software]](#Install_the_client_software)
-   [[3] [Kernel setup]](#Kernel_setup)
-   [[4] [Browser and java plugin]](#Browser_and_java_plugin)
-   [[5] [Tunnel connection]](#Tunnel_connection)
-   [[6] [External Resources]](#External_Resources)

### [Download the client install script]

The client software is only available for download from the firewall appliance itself. The VPN administrator must provide a URL (something like https://vpn.example.com/Login/Login) and credentials.

Log in and click the Settings link.

[![Settingslink.png](/images/5/57/Settingslink.png)](https://wiki.gentoo.org/wiki/File:Settingslink.png)

There is a link to download the software. Click to save the file locally.

[![Download.png](/images/f/f1/Download.png)](https://wiki.gentoo.org/wiki/File:Download.png)

### [Install the client software]

There is currently not an ebuild for snx. Run the install script as root.

`root `[`#`]`sh snx_install.sh`

    Installation successfull

The script installs [/usr/bin/snx] and also [/usr/bin/snx_uninstall]. The main binary is setuid-root, which means that when a non-privileged user runs it, it will run as the root user. Generally this is ill-advised for a system\'s security, but it is done here so that a normal user can trigger setting up the tunnel networking.

`root `[`#`]`ls -l /usr/bin/snx`

    r-s--x--x 1 root root 3286232 Aug 24 02:46 /usr/bin/snx

This binary is also 32-bit and will have linkage errors until the required libraries are installed.

`root `[`#`]`ldd /usr/bin/snx`

            linux-gate.so.1 (0xf773f000)
            libX11.so.6 => not found
            libpthread.so.0 => /lib32/libpthread.so.0 (0xf770e000)
            libresolv.so.2 => /lib32/libresolv.so.2 (0xf76f6000)
            libdl.so.2 => /lib32/libdl.so.2 (0xf76f1000)
            libpam.so.0 => not found
            libnsl.so.1 => /lib32/libnsl.so.1 (0xf76d6000)
            libstdc++.so.5 => not found
            libc.so.6 => /lib32/libc.so.6 (0xf752b000)
            /lib/ld-linux.so.2 (0xf7740000)

For the three missing linkages it is possible to deduce the packages (with dependencies) that must be installed with 32-bit versions. Configure the necessary changes in package.use.

`root `[`#`]`cat >/etc/portage/package.use/snx`

    # for libX11
    x11-proto/xproto abi_x86_32
    x11-proto/inputproto abi_x86_32
    x11-proto/kbproto abi_x86_32
    x11-proto/xf86bigfontproto abi_x86_32
    x11-proto/xextproto abi_x86_32
    dev-libs/libpthread-stubs abi_x86_32
    x11-proto/xcb-proto abi_x86_32
    x11-libs/libXdmcp abi_x86_32
    x11-libs/libXau abi_x86_32
    x11-libs/libxcb abi_x86_32
    x11-libs/libX11 abi_x86_32

    # for libpam
    sys-libs/pam abi_x86_32
    virtual/libintl abi_x86_32
    sys-libs/zlib abi_x86_32
    sys-libs/db abi_x86_32
    sys-libs/cracklib abi_x86_32
    sys-devel/flex abi_x86_32

    # for libstdc++-v3
    sys-libs/libstdc++-v3 multilib

Now the missing libs can be installed.

`root `[`#`]`emerge libX11 pam libstdc++-v3`

and the linkage is fixed

`root `[`#`]`ldd /usr/bin/snx`

            linux-gate.so.1 (0xf7784000)
            libX11.so.6 => /usr/lib32/libX11.so.6 (0xf761f000)
            libpthread.so.0 => /lib32/libpthread.so.0 (0xf7603000)
            libresolv.so.2 => /lib32/libresolv.so.2 (0xf75eb000)
            libdl.so.2 => /lib32/libdl.so.2 (0xf75e6000)
            libpam.so.0 => /usr/lib32/libpam.so.0 (0xf75d5000)
            libnsl.so.1 => /lib32/libnsl.so.1 (0xf75bb000)
            libstdc++.so.5 => /usr/lib32/libstdc++.so.5 (0xf74ff000)
            libc.so.6 => /lib32/libc.so.6 (0xf7354000)
            libxcb.so.1 => /usr/lib32/libxcb.so.1 (0xf7327000)
            /lib/ld-linux.so.2 (0xf7785000)
            libm.so.6 => /lib32/libm.so.6 (0xf72d3000)
            libgcc_s.so.1 => /usr/lib/gcc/x86_64-pc-linux-gnu/5.4.0/32/libgcc_s.so.1 (0xf72b8000)
            libXau.so.6 => /usr/lib32/libXau.so.6 (0xf72b3000)
            libXdmcp.so.6 => /usr/lib32/libXdmcp.so.6 (0xf72ac000)

Note that while it is now possible to run [snx] directly at the command line, it will not result in a successful login. In recent versions it will only work when run as intended, from the browser.

### [Kernel setup]

The [snx] binary attempts to fork the command `modprobe tun` and expects a successful exit code. Therefore, CONFIG_TUN must be compiled as a module.

[KERNEL]

    Device drivers -->
      Network device support -->
        Network core driver support -->
          <M> Universal TUN/TAP device driver support

Test that the module loads.

`root `[`#`]`modprobe tun`

`root `[`#`]`echo $?`

    0

### [Browser and java plugin]

Chrome/Chromium no longer support the NPAPI required to launch java applets, which leaves Firefox as a required browser.

Firefox must launch a java applet. One document on the web stated that Oracle\'s JRE is required, and a different document suggested that OpenJDK is acceptable. This document\'s author tested using Oracle. Be sure to enable the `nsplugin` use flag. Before trying to log into the tunnel, run a web search for java test applets and confirm that Firefox is generally successful at launching applets.

### [Tunnel connection]

The system should now be ready to connect to the tunnel. Press the Connect button in the browser.

[![Connect.png](/images/5/5f/Connect.png)](https://wiki.gentoo.org/wiki/File:Connect.png)

There will be a variety of trust warnings to click through. The applet will even prompt for your root password and appear to install the binary again. The connection should succeed, however, and subsequent connections will trigger fewer warnings.

### [External Resources]

-   [https://www.checkpoint.com/products-solutions/next-generation-firewalls/enterprise-firewall/](https://www.checkpoint.com/products-solutions/next-generation-firewalls/enterprise-firewall/)
-   [http://kenfallon.com/checkpoint-snx-install-instructions-for-major-linux-distributions/](http://kenfallon.com/checkpoint-snx-install-instructions-for-major-linux-distributions/)