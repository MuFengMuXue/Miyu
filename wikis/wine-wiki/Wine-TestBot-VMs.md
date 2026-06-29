## WineTestBot VMs

This page describes the new WineTestBot VMs and how they are configured.

## Windows 11

The normal way to create a Windows 11 VM would be to set it up with
[UEFI](https://getlabsdone.com/how-to-install-windows-11-on-kvm/)
(ovmf), secure boot and a
[TPM](https://getlabsdone.com/how-to-enable-tpm-and-secure-boot-on-kvm/)
(swtpm-tools). There are a couple catches:

- Guides typically recommend using OVMF_CODE.fd but it has been replaced
  by OVMF_CODE_4M.fd (same thing just larger firmware).
- On Debian it may be necessary to fix the permissions of a couple of
  swtpm files. But then you may be able to avoid this step by restarting
  Libvirt or rebooting.

   ```sh
   chown tss /var/lib/swtpm-localca/.lock.swtpm-localca
   chown tss /var/lib/swtpm-localca/signkey.pem
   ```

- Setting up the TPM can be done in the virt-manager GUI, there is no
  need to manually edit the XML file.

However there is a blocker that prevents using this approach for the
TestBot: Libvirt does not support taking snapshots of UEFI VMs, whether
live or not. More precisely internal qcow2 snapshots, the only type
supported by Libvirt, are incompatible with UEFI. The QEmu developers
won't fix that and instead recommend using external snapshots. But that
[requires a lot of
work](https://bugzilla.redhat.com/show_bug.cgi?id=1881850) to be
supported in Libvirt (i.e. it could still take years). Currently it
would be possible to create an external disk-only snapshot by changing
the TestBot's Libvirt code but it would not be possible to restore it
without running QEmu manually (i.e. give up on the snapshot VM XML
description file and Libvirt's remote access support). So that rules out
this approach.

So instead use [Rufus](https://rufus.ie/) to [remove the UEFI, secure
boot, and TPM
requirements](https://nerdschalk.com/how-to-use-rufus-to-disable-tpm-and-secure-boot-in-bootable-windows-11-usb-drive/).
Start with a preexisting Windows VM:

- Download the Windows 11 ISO to the VM (attaching the ISO to the VM's
  CDROM drive will not work: Rufus needs the ISO file).
- Add a 32 GB disk using USB as the disk controller (otherwise Rufus
  will not find that disk).
- In Rufus, expand the 'Show advanced drive properties' section and
  select 'List USB Hard Drives'.
- Pick MBR as the partitioning scheme. Verify that the target system is
  'BIOS (or UEFI-CSM)'.
- Select the Windows ISO and make sure 'Standard Windows installation'
  is selected as the image option.
- Click on Start and then select the option to disable the (4GB+ RAM)
  secure boot and TPM checks.
- You may also ask Rufus to create a local user account matching the one
  you are currently using (otherwise you will have to use an online
  Microsoft account).
- Let Rufus continue and start grinding them coffee beans.
- Once done power off the VM and remove the USB drive.

When creating the Windows 11 VM:

- Connect the [Virtio drivers
  ISO](https://pve.proxmox.com/wiki/Windows_VirtIO_Drivers) to the VM's
  CDROM drive.
- Add the disk image created by Rufus to the VM, preferably still as a
  USB drive to limit drive letter assignment issues.
- Adjust the boot order so that the USB drive comes first.
- Add a Virtio SCSI storage driver and set the main disk to SCSI.
- Adjust other peripherals to virtio as desired.
- During installation tell Windows to look for drivers on the CDROM
  drive.
- Once the installation is done remove the USB drive and optionally move
  the CDROM to SCSI.
- On the Windows first boot start the Device Manager and install the
  drivers from the Virtio ISO for all unrecognized devices and also
  upgrade the display driver.

You can also find various configuration tidbits to optimize the QEmu
configuration for Windows 11 on [Kevin Locke's
blog](https://kevinlocke.name/bits/2021/12/10/windows-11-guest-virtio-libvirt/).

## PCI-Passthrough

ArchLinux has a [good
guide](https://wiki.archlinux.org/title/PCI_passthrough_via_OVMF) but
they recommend configuring the VM with a UEFI firmware which is a
non-starter for the TestBot (see the Windows 11 section above), and also
it's not Debian. But it still has a lot of relevant information that
carries over.

So here's a TestBot-focused summary of how to proceed. First you need to
configure the host:

- Get a compatible processor (Intel with VT-x and VT-d or any AMD \*Zen)
  and motherboard. Make sure the relevant support is enabled in the
  BIOS.
- You will also want to be able to connect the passthrough GPU to a
  screen otherwise Windows will not boot to the desktop. If your monitor
  has multiple inputs (e.g. HDMI and DisplayPort) that can work. For the
  TestBot we don't actually use the screen so the VM hosts instead have
  HDMI / DisplayPort dummy plugs.
- Identify the PCI ids of the graphics card to use for the
  PCI-passthrough. Typically the ids start with 1002 for AMD and 10de
  for NVIDIA.

   ```
   # lspci -nn | grep AMD
   01:00.0 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD/ATI] Navi 10 XL Upstream Port of PCI Express Switch [1002:1478] (rev c7)
   02:00.0 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD/ATI] Navi 10 XL Downstream Port of PCI Express Switch [1002:1479]
   03:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Navi 23 [1002:73ff] (rev c7)
   03:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Device [1002:ab28]
   ```

- Configure the kernel to use IOMMU and bind the GPUs to vfio-pci.

To do so edit the GRUB_CMDLINE_LINUX_DEFAULT line in /etc/default/grub
to add these options, adjusting the list of PCI ids for your GPU(s).

Note that `intel_iommu=on` should be replaced with `amd_iommu=on` for
AMD hosts.

- `iommu=pt` is essentially an optimization so the host treats devices
  that cannot be passed through normally.

- Disabling efifb is necessary to prevent it from grabbing some I/O
  memory that the GPU will need when running in the guest. A symptom
  that you forgot this is "vfio-pci ... BAR 0: can't reserve" errors
  in dmesg and the generic code 43 driver error in Windows.

   ```
   GRUB_CMDLINE_LINUX_DEFAULT="intel_iommu=on iommu=pt vfio-pci.ids=1002:1478,1002:1479,1002:73ff,1002:ab28 video=efifb:off"
   ```

- Also tell the kernel to load the vfio modules:

   ```
   echo vfio vfio_iommu_type1 vfio_pci vfio_virqfd >>/etc/modules
   ```

- It may also be a good idea to prevent the host from loading the
  passthrough GPU drivers. But you may need to find another way if your
  host needs them for its own display.

   ```sh
   echo blacklist radeon >>/etc/modprobe.d/local-qemu.conf
   echo blacklist nouveau >>/etc/modprobe.d/local-qemu.conf
   echo blacklist nvidia >>/etc/modprobe.d/local-qemu.conf
   ```

- You should also set ignore_msrs to potentially avoid some Windows
  1803+ update issue and prevent some Windows applications from crashing
  the guest. Furthermore you should add report_ignored_msrs to avoid
  flooding dmesg with rdmsr errors.

   ```sh
   echo options kvm ignore_msrs=1 >>/etc/modprobe.d/local-qemu.conf
   echo options kvm report_ignored_msrs=0 >>/etc/modprobe.d/local-qemu.conf
   ```

- Each PCI device is part of an IOMMU group. An IOMMU group is the
  smallest set of physical devices that can be passed to a VM. That's a
  problem if the host's network card is in the same IOMMU group as your
  VM's GPU. You can check [there how PCI devices are
  grouped](https://wiki.archlinux.org/title/PCI_passthrough_via_OVMF#Ensuring_that_the_groups_are_valid).
  If the grouping is wrong you may try moving the GPU to another PCI
  slot. Otherwise you will have to use the [ACS kernel
  patch](https://wiki.archlinux.org/title/PCI_passthrough_via_OVMF#Bypassing_the_IOMMU_groups_(ACS_override_patch)).

For the following section I will assume you want to use the GPU in a
preexisting Windows VM:

- First edit the VM configuration: virsh edit wtbw11pro64

   Replace the <domain type='kvm'> line with the following four lines:

   ```
   <domain type='kvm' xmlns:qemu='https://libvirt.org/schemas/domain/qemu/1.0'>
    <qemu:commandline>
      <qemu:arg value='-set'/>
      <qemu:arg value='device.hostdev0.x-vga=on'/>
    </qemu:commandline>
   ```

- Then in virt-manager add your GPU devices to the VM. Note that you
  should most likely at least pass both the video and audio devices.
- Boot the VM.
- If your VM is going to be 'headless', install
  [TightVNC](https://www.tightvnc.com/download.php) so you can still
  access it remotely. During installation set up the service so you can
  access the VM after a reboot. If that fails it may be that you picked
  the wrong TightVNC bitness for your VM!
- Note: It's better to avoid RDP because it uses a separate desktop with
  its own graphics driver, changes the resolution and disables sound.
  That's fine for general remote access but is useless for making sure
  the VM can use the GPU as intended.
- Then install the [AMD](https://www.amd.com/en/support) /
  [NVIDIA](https://www.nvidia.com/en-us/geforce/drivers/) graphics card
  driver, or let Windows find it on its own if Windows updates are
  allowed.
- If you got no error in the previous step and the device is not in
  error in the Device Manager then the PCI-passthrough procedure was
  successful.
- At this point if the Windows display configuration dialog does not
  show a second screen it is probably because your graphics card is not
  connected to a monitor. See the VM host configuration section for more
  details.
- You can now shut down Windows and remove the following devices:
  - Spice
  - VGA / QXL / ... *(go back to a single GPU configuration)*
  - \*Tablet
  - ich9 *(it makes more sense for the VM to use the GPU audio device
    instead)*
- Check that you can still boot the VM and connect to it via VNC. If it
  does not look like the VM is booting, it is probably because the QEmu
  XML configuration was not updated.
- Note that if you opted for the second monitor route you may need to
  additionally pass a USB keyboard and mouse to the VM as the QEmu ones
  will not react without an active Libvirt video device.

## Virtualization

### Memory Ballooning

Memory ballooning allows the host to reclaim memory from the VM. In
concrete terms this corresponds to the "Current Allocation" and "Maximum
allocation" fields of the Memory settings page. However with Libvirt
this mechanism is [not
dynamic](https://pmhahn.github.io/virtio-balloon/) (this may be
different with [Proxmox](https://www.proxmox.com/en/proxmox-ve)). This
means your VM will remain stuck with the "Current Allocation" setting
until you manually run a specific virsh command to increase the amount
of memory it is allowed to use.

So when setting up a VM for the TestBot one should always make sure the
value in the "Current Allocation" field is high enough, which probably
means it should be the same as "Maximum allocation".

### QEMU / KVM

Here is a list of QEMU / KVM bugs relevant to the WineTestBot:

- [QEMU bug 1119281](https://bugs.launchpad.net/qemu/+bug/1119281) - The
  virtio network device breaks UuidCreateSequential().
- [QEMU bug
  930962](https://bugs.launchpad.net/ubuntu/+source/isc-dhcp/+bug/930962) -
  Bad checksum errors caused by a bad interaction between the virtio
  network device and the dhcp server. Not necessarily a big issue but
  pollutes the logs.
- [QEMU bug 1119861](https://bugs.launchpad.net/qemu/+bug/111981) - Poor
  console performance in Windows 7.
- We worked around this one by [reducing the console buffer
  size](c2a5b04d01882668f433e74bcaf4ff1c11be4167)
  in kernel32:console.

## VM hardware and drivers

### Compatibility tables

#### Sound

| Windows      | ac97             | es1370           | ich6       | sb16       |
|--------------|------------------|------------------|------------|------------|
| 2000         | ok               | broken (1)       | no driver  | broken (2) |
| XP           | 52 test failures | 60 test failures | no driver  | broken (3) |
| 2003         | ok               | no driver        | no driver  | no driver  |
| Vista        | ok               | 3 test failures  | no driver  | no driver  |
| Vista 64-bit | no driver        | no driver        | broken (4) | no driver  |
| 2008 64-bit  | no driver        | no driver        | broken (5) | no driver  |
| 7            | no driver        | no driver        | ok         | no driver  |
| 7 64-bit     | no driver        | no driver        | ok         | no driver  |

Notes:

1.  With the es1370 driver dsound:capture causes Windows 2000 to freeze.
2.  Windows 2000 does not detect the Sound Blaster 16 card but its
    driver can be installed manually. However the driver then fails to
    load with code 10.
3.  Windows XP does not detect the PCI Sound Blaster 16 card but its
    driver can be installed manually. However that then breaks the
    network cards (rtl8139, e1000 and virtio).
4.  The High Definition Audio Device driver (6.0.6000.16386) fails to
    load with code 10.
5.  The High Definition Audio Device driver (6.0.6001.18000) fails to
    load with code 10.
6.  pcspk does not count as a sound card.

#### Video

| Windows      | cirrus                          | qxl                   | vga               | vmvga            |
|--------------|---------------------------------|-----------------------|-------------------|------------------|
| 2000         | 317 test failures               | vga fallback (1)      | vga fallback (1)  | vga fallback (1) |
| XP           | 236 test failures               | 117 test failures (2) | empty driver name | ok               |
| 2003         | ok (5, 7)                       | ok                    | ok                | ok (5)           |
| Vista        | vga fallback; 234 test failures | ok (2)                | ok                | ok (3)           |
| Vista 64-bit | vga fallback; 233 test failures | 1 test failure        | ok                | ok (4)           |
| 2008 64-bit  | vga fallback; 233 test failures | broken (6)            | ok                | ok (4)           |
| 7            | vga fallback; 234 test failures | ok (2)                | ok                | ok (4)           |
| 7 64-bit     | vga fallback; 234 test failures | ok (2)                | ok                | ok (4)           |

Notes:

1.  The Windows 2000 fallback driver only support the standard VGA mode:
    640x480x4.
2.  Using the 'Red Hat QXL GPU' 6.1.0.10016 driver.
3.  Using the 'VMware SVGA II' 11.9.1.0 XPDM driver from VMware Tools
    9.0.1-913578.
4.  Using the 'VMware SVGA II' 11.6.0.38 XPDM driver from VMware Tools
    8.3.17-870839.
5.  Using the default VGA driver.
6.  The 'Red Hat QXL GPU' 6.1.0.10016 driver fails to load with code 39.
7.  Operates in 24bpp only.
8.  None of the Windows versions has a xen driver.

#### Network card

| Windows      | e1000     | ne2k_pci  | pcnet     | rtl8139   | virtio         |
|--------------|-----------|-----------|-----------|-----------|----------------|
| 2000         | no driver | ok (1)    | ok        | crash (2) | no driver      |
| XP           | no driver | ok        | ok        | ok        | 1 test failure |
| 2003         | ok        | ok        | ok        | ok        | ???            |
| Vista 64-bit | ok        | no driver | no driver | ok        | 1 test failure |
| 2008 64-bit  | ok        | no driver | no driver | ok        | 1 test failure |
| 7            | ok        | no driver | no driver | ok        | 1 test failure |

Notes:

1.  With the ne2k_pci card network transfers cause high CPU usage and
    are slow (~10Mbps).
2.  The rtl8139 card causes Windows 2000 to crash on startup.

### Processors

Make sure the virtual CPU topology is compatible with the Windows
version: at the time of writing the Home edition can only use one
processor and the Pro edition two. So configure a Home edition VM as a
single processor system with either two cores or two threads, rather
than as a dual-processor system.

### Clock

Windows 10 needs the High Precision Event Timer (HPET) otherwise it
causes a high CPU usage on the host. Use *virsh edit* and in the
`<clock>` section add:

```
<clock>
  <timer name='hpet' present='yes'/>
  ...
```

### Virtual disk

Some tests require reasonable disk performance otherwise they time out
(in particular the msi tests). For these we need to make sure to use
QEMU's paravirtualized 'virtio' disk. The driver comes from KVM/Fedora:
[VirtIO drivers for Windows from
Fedora](https://pve.proxmox.com/wiki/Windows_VirtIO_Drivers).

### QXL graphics driver

Some VMs use the QXL paravirtualized graphics card together with the
driver from Spice's [Windows Guest
Tools](https://spice-space.org/download.html) pack.

- Mount spice-guest-tools-0.3.iso
- Then run spice-guest-tools-0.3.exe from the CD to install the driver.
- Windows will warn about each driver because they are unsigned but will
  still use any you install.

Also on Windows Vista Spice's Windows Guest Tools pack (0.3) does not
install the QXL driver. It is possible to work around that by manually
installing the driver directly from c:\Program Files\SPICE Guest
Tools\drivers. One can either pick the Windows XP or Windows 7 one, they
seem to behave identically. However the problem is that this immediately
shows a very visible transparency/alpha blending issue in the Desktop
Gadgets area (see ([bug
61124](https://bugs.freedesktop.org/show_bug.cgi?id=61124)). That does
not seem to impact the tests though that configuration has a bunch of
d3d8:device test failures like on Windows XP.

### VMware graphics driver

QEMU can also emulate the paravirtualized VMware graphics card. However
so far the VMware graphics driver has not shown to reduce the number
failing tests or to improve the performance. Thus it is not used for
now. Still here is how to install the driver on Windows 7 for further
testing.

- These instructions are based on the [I roughly followed 1
  to](https://www.linux-kvm.com/content/using-vmware-vga-kvm-windows-guests)
  comment in a discussion thread on [Linux
  KVM](https://www.linux-kvm.com).
- First go to VMware's [site](https://packages.vmware.com/tools) to
  download a VMware Tools ISO.
- Do not pick the latest VMware version because it only works with the
  VMware 7 hardware which QEMU 1.1.2 does not implement. The driver
  would install but then fail to load with error code 43 when it does
  not recognize the graphics card.
- Pick the ISO from the esx/4.1latest/windows directory which
  corresponds to VMware Tools 8.3.17.
- Mount the ISO and run 'setup.exe /a' and extract the drivers to
  c:\vmwaretools.
- Then right-click on the desktop background, and follow this sequence
  of buttons Screen Resolution -\> Advanced Settings -\> Properties -\>
  Driver -\> Update Driver -\> Browse my computer.
- Pick the 'C:\vmwaretools\Common\VMware\Drivers\video' directory (or
  Common64 for the 64-bit drivers). This will install the 'VMware SVGA
  II' driver. This is in fact the legacy XPDM driver but it will still
  work in Windows 7.
- Do not pick the 'wddm_video' directory! It contains the same 'VMware
  SVGA 3D' that requires the VMware 7 hardware that is not supported by
  QEMU.
- Note that this procedure will not work in Windows 8 because it
  completely dropped support for the XPDM drivers. This means it is
  impossible to use the VMware drivers with QEMU on Windows 8.

### Network card

The paravirtualized 'Virtio' network card causes errors (see [Bug
1119281](https://bugs.launchpad.net/qemu/+bug/1119281)). Thus the VMs
use either the e1000 or rtl8139 network cards with the standard Windows
drivers.

## Windows configuration

- **Installing unsigned drivers**

  The Virtio drivers are unsigned and some Windows versions may require
  special steps to allow installing them.

  *Windows 7* may need updates \> SP1 before it will allow installing
  unsigned drivers. Then there are two options.

  Run gpedit.msc and in 'User Configuration' -\> 'Administrative
  Templates' -\> 'System' -\> 'Driver Installation' look for 'Code Signing
  for Device Drivers' and set it to Enabled and either Warn or Ignore.

  Or on the command line run:

  ```
  bcdedit.exe -set loadoptions DDISABLE_INTEGRITY_CHECKS
  bcdedit.exe -set TESTSIGNING ON
  # To undo
  bcdedit.exe -deletevalue DDISABLE_INTEGRITY_CHECKS
  bcdedit.exe -deletevalue TESTSIGNING
  ```

- **Start Internet Explorer and answer the initial configuration
  questions.**

  *Rationale*: It is not known if leaving these questions unanswered would
  modify the test results. However this would not correspond to any
  configuration that Windows applications would expect so in doubt it's
  best to answer them with something as close as possible to 'default'
  answers.

  *Windows 10*: Run iexplore.exe

- **Disable the Internet Explorer automatic updates.**

  Starting with version 10 Internet Explorer has its own independent
  update mechanism. The rationale for disabling it is the same as for
  Windows Update.

- **Stop Edge from starting at boot**

  *Rationale*: This could slow down boot for PCI passthrough
  configurations and create unneeded activity during the tests.

  Start Edge. Then in the burger menu go to Settings -\> Settings (yes
  twice) -\> System and performance.

  Disable 'Startup boost' and 'Continue running background extensions and
  apps when Microsoft Edge is closed'.

- **Stop Teams/OneDrive from starting at boot**

  *Rationale*: This could slow down boot for PCI passthrough
  configurations and create unneeded activity during the tests.

  Settings -\> Apps -\> Startup Apps.

- **Disable screensaver.**

  *Rationale*: The VMs can remain idle for a long time so that the
  screensaver would possibly be running before before we start the tests.
  The screensaver could also trigger during the long WineTest.exe runs. In
  either case it seems better nor to risk having them interfere. Also we
  don't want half a dozen VMs to waste time on animated screensavers while
  waiting for a test to run.

  *Windows 7*: Control Panel -\> Hardware and Sound -\> Change when the
  computer sleeps

  *Windows 10*: Settings -\> System -\> Power & sleep

- **Disable disk and computer suspend.**

  *Rationale*: The VMs may remain idle for quite some time waiting for a
  test to run. We would not want them to 'suspend to RAM' as it's not
  clear they would successfully wake up when called upon. Similarly
  suspending the disk seems pointless and just asking for trouble.

- **Disable Windows update.**

  *Rationale*: After each test the VM is restored to a clean snapshot. So
  any work done by the Windows update process would be lost at that point.
  So the only effect it could have is messing the test environment and
  wasting computing resources.

  *Windows 10*: Disabling Windows Update can only be done by putting the
  network connection in metered mode. Note that Windows 11 has separate
  data cap and metered settings and that the former does not prevent
  Windows from updating.

  *Early Windows 10*: Note that Windows 10 1607 and older does not have a
  GUI to do this for an ethernet connection. But it can be done through
  the registry:

  \[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows
  NT\CurrentVersion\NetworkList\DefaultMediaCost\]

  Right-Click on DefaultMediaCost -\> Properties -\> Advanced -\> Change
  Owner -\> Administrators -\> OK

  Check "Replace owner on subcontainers and objects" -\> OK

  Select Administrators -\> Check "Full Control" -\> OK

  Ethernet = dword:2.

  You can optionally change the DefaultMediaCost permissions and ownership
  to "NT Service\TrustedInstaller".

  *In progress updates*: Windows may have downloaded updates right before
  the network connection was put in metered mode which means if you
  immediately take a snapshot it will install those after some delay on
  the next boot, resulting in a busy host and interference with the tests.
  So it is recommended to reboot Windows, wait a bit and check that
  Windows is really idle before taking a snapshot.

- **Disable Delivery Optimization.**

  *Rationale*: It seems like this service can use network bandwidth to
  exchange windows update data with the other Windows machines on the LAN
  even when Windows update is disabled. To do so, look for it near the
  Windows Update settings.

  Windows 10: Settings -\> Update & Security -\> Delivery Optimization

- **Disable restore points.**

  *Rationale*: Our MSI tests normally disable restore points and so should
  not need this. However restore points are redundant with the VM
  snapshots and just waste disk space.

  *Windows 7/10*: Run control -\> Search Advanced -\> View advanced system
  settings -\> System Protection

- **Reduce the boot delay.**

  *Rationale*: When Windows crashes it waits for 30 seconds before
  rebooting. This may cause the Task to time out before the TestBot server
  has time to reconnect to the VM to retrieve the pre-crash test report.

  Run control -\> Search Advanced -\> View advanced system settings -\>
  Startup and Recovery -\> reduce the timeout to 5 seconds or so

- **Disable Windows Internet Time.**

  *Rationale*: We don't want something to change the time while we run
  timing tests, even if it's just moving the time by a few hundred
  milliseconds.

  *Windows 10*: Settings -\> Time & Language -\> Date & Time -\> Set time
  automatically = Off

- **Disable search indexing.**

  *Rationale*: Any indexing will have to be redone when the VM is reverted
  to the clean snapshot after the test. So all it can do is trash the
  disk, likely causing tests to time out.

  *Windows 7/10*: Run services.msc -\> 'Windows Search' and switch it from
  'Automatic (Delayed)' to 'Disabled'.

- **Disable defragmentation.**

  *Rationale*: Windows 10 regularly defragments the disk. Even though this
  is a low priority task it can slow down disk I/O and increase disk usage
  on the host.

  *Windows 10*: Right-click on the drive -\> Properties -\> Tools -\>
  Optimize -\> Disable Scheduled optimization.

- **Disable OneDrive.**

  *Rationale*: OneDrive would normally not be configured anyway and thus
  should not be using much resources. But it typically starts up on boot
  and can pop up Windows at inopportune times.

  *Windows 10*: Right-click on the OneDrive systray icon, and tell it not
  to run on startup.

  or (64-bit) run `%SystemRoot%\SysWOW64\OneDriveSetup.exe /uninstall`

  or (32-bit) run `%SystemRoot%\System32\OneDriveSetup.exe /uninstall`

- **Disable time of last access.**

  *Rationale*: Keeping track of the time of last access requires
  additional writes.

  *Windows 10*: fsutil behavior set disablelastaccess 1

- **Disable Windows Defender.**

  *Rationale*: Windows Defender sometimes mistakenly flags WineTest.exe as
  being infected. Also when restoring an old snapshot it may start a full
  disk scan which slows the tests.

  *Windows 10*: Set
  \[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\]
  DisableAntiSpyware=dword:1


  Note that recent Windows Defender versions automatically reset this
  setting and re-enable themselves. This can be overridden through the
  Group Policy but only on Professional and Enterprise versions.

  *Windows 10*: Prevent Windows Defender from scanning files in the folder
  where WineTest is downloaded.


  Settings -\> Update & Security -\> Windows Security -\> Virus & threat
  protection -\> Manage settings -\> Add or remove exclusions -\> Add an
  exclusion

- **Disable Windows Defender notifications.**

  *Rationale*: If Windows Defender cannot be completely disabled (e.g. on
  the latest Windows 10), disable its most annoying notifications to avoid
  windows popping up during the user32:msg tests.

  *Windows 10*: Settings -\> Update & Security -\> Windows Security -\>
  Open Windows Security Virus & threat protection -\> Manage settings -\>
  Change notification settings

- **Hide the Windows 10 upgrade notifications and application ads.**

  *Rationale*: Avoid windows popping up during the user32:msg tests.

  *Windows 10*: Setting -\> System -\> Notifications & actions
  - In Notifications & Actions: uncheck Windows experience, setup, tips &
    tricks
  - In Get notifications from these senders: uncheck Suggested and Backup
    settings

- **Disable Windows Telemetry and the Customer Experience Improvement
  Program.**

  One may want to avoid KB3068708, KB3075249, KB3080149. Also, in the Task
  Scheduler, [disable the
  tasks](https://pubs.vmware.com/view-51/topic/com.vmware.view.administration.doc/GUID-E712DAE6-88DF-4208-BEFA-09513A01A26E.html)
  in Microsoft \> Windows

  - Application Experience
    - AitAgent
    - Microsoft Compatibility Appraiser *(generates lots of I/O)*
    - ProgramDataUpdater
  - Customer Experience Improvement Program.
    - BthSQM
    - Consolidator
    - KernelCeipTask
    - Uploader
    - UsbCeip

  *Rationale*: They involve tasks that get run on boot and cause a
  significant amount of disk activity.

- **Set the password to not expire**

  *Rationale*: Causes a user notification to pop up after login. Plus it
  makes no sense to change the VM's password monthly in the first place!

  Run lusrmgr.msc -\> right-click on the user -\> Properties -\> Password
  never expires

- **Activate Windows!**

  Preferably once the hardware configuration is pretty much settled down
  to avoid having to reactivate again.

  *Windows 10*: Settings -\> Update & Security -\> Activation

- **Lower the volume.**

  *Rationale*: To preserve the ears of whoever is going to connect to the
  VM to perform maintenance.

- **Reset TestAgentd's reboot count**

  Last thing to do before the snapshot. Delete TestAgentd.exe.data.

  The following configuration configuration options are not really
  important for the WineTestBot VMs but can help optimize real Windows
  partitions used for running WineTest.

- **Configure auto-login.**

  *Rationale*: This is necessary to get the tests to start automatically
  on boot.

  *Windows 10:* control userpasswords2 + uncheck "Users must enter a user
  name and password"


  or netplwiz + uncheck "Users must enter a user name and password"

  or \[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows
  NT\CurrentVersion\Winlogon\]


  DefaultUserName = string:<username>

  DefaultPassword = string:<password>

  AutoAdminLogon = string:"1"

- **Disable hibernation.**

  *Rationale*: This helps save a lot of space when taking the image of the
  Windows partition.

  *Windows 10*: powercfg -h off

- **Disable swap.**

  *Rationale*: This helps save a lot of space when taking the image of the
  Windows partition.

  *Windows 7/10*: Run control -\> Search Advanced -\> View advanced system
  settings -\> Performance Settings -\> Advanced

  Use `dir /A:H c:\\` to check that there is no *pagefile.sys* file.

See also VMware's recommendations to [Optimize Windows Guest Operating
System
Performance](https://pubs.vmware.com/view-51/index.jsp#com.vmware.view.administration.doc/GUID-06DF65D1-7151-479A-B388-162535251F6F.html).

## Missing Windows dlls

Even with the latest Windows version and all updates some of the dlls
Wine tests are missing. This section describes the recommended way to
install them.

### msvcr70

**FIXME**: This is part of the Visual Studio 7.0 redistributables but
there is no known way to install this dll.

### fusion, msvcr71

These are part of Visual Studio .Net and only the 32-bit version is
available. To get them one has to install the .Net Framework 1.1 package
which is not downloadable anymore (see [Chocolatey
dotnet1.1](https://community.chocolatey.org/packages/dotnet1.1#versionhistory)).

### atl80

Install the 8.0.50727.6195
[x86](https://download.microsoft.com/download/8/B/4/8B42259F-5D70-43F4-AC2E-4B208FD8D66A/vcredist_x86.EXE)/[x64](https://download.microsoft.com/download/8/B/4/8B42259F-5D70-43F4-AC2E-4B208FD8D66A/vcredist_x64.EXE)
Visual C++ 2005 redistributables (see [Chocolatey
vcredist2005](https://community.chocolatey.org/packages/vcredist2005#versionhistory)).

Note that atl80.dll is not found in c:\Windows\System32. Instead look
for this set of dlls in c:\Windows\WinSxS\\.vc80.\*, and optionally
check the compatible versions in
c:\Windows\WinSxS\Manifests\\.vc80.atl\*.manifest.

### atl90, msvcp90, msvcr90

Install the
[x86](https://download.microsoft.com/download/5/D/8/5D8C65CB-C849-4025-8E95-C3966CAFD8AE/vcredist_x86.exe)/[x64](https://download.microsoft.com/download/5/D/8/5D8C65CB-C849-4025-8E95-C3966CAFD8AE/vcredist_x64.exe)
Visual C++ 2008 redistributables (see [Chocolatey
vcredist2008](https://community.chocolatey.org/packages/vcredist2008#versionhistory)).

Note that these libraries are not found in c:\Windows\System32. Instead
look for this set of dlls in c:\Windows\WinSxS\\.vc90.\*, and optionally
check the compatible versions in
c:\Windows\WinSxS\Manifests\\.vc90.atl\*.manifest.

### atl100, msvcp100, msvcr100

Install the 10.0.40219.325
[x86](https://download.microsoft.com/download/1/6/5/165255E7-1014-4D0A-B094-B6A430A6BFFC/vcredist_x86.exe)/[x64](https://download.microsoft.com/download/1/6/5/165255E7-1014-4D0A-B094-B6A430A6BFFC/vcredist_x64.exe)
Visual C++ 2010 redistributables (see [Chocolatey
vcredist2010](https://community.chocolatey.org/packages/vcredist2010#versionhistory)).

### atl110, msvcp110, msvcr110, vcomp110

Install the 11.0.51106.1
[x86](https://download.microsoft.com/download/1/6/B/16B06F60-3B20-4FF2-B699-5E9B7962F9AE/VSU_4/vcredist_x86.exe)/[x64](https://download.microsoft.com/download/1/6/B/16B06F60-3B20-4FF2-B699-5E9B7962F9AE/VSU_4/vcredist_x64.exe)
Visual C++ 2012 redistributables (see [Chocolatey
vcredist2012](https://community.chocolatey.org/packages/vcredist2012#versionhistory)).

See also the original Microsoft download page for the older [Visual C++
2012 Update
4](https://www.microsoft.com/en-us/download/details.aspx?id=30679)
redistributable.

### msvcp120, msvcr120

Install the 12.0.40660.0
[x86](https://download.microsoft.com/download/0/5/6/056dcda9-d667-4e27-8001-8a0c6971d6b1/vcredist_x86.exe)/[x64](https://download.microsoft.com/download/0/5/6/056dcda9-d667-4e27-8001-8a0c6971d6b1/vcredist_x64.exe)
Visual C++ 2013 redistributables (see [Chocolatey
vcredist2013](https://community.chocolatey.org/packages/vcredist2013#versionhistory)).

See also the original Microsoft download page for the older [Visual C++
2013](https://www.microsoft.com/en-us/download/details.aspx?id=40784)
redistributable.

### msvcp140, msvcr140, ucrtbase

Install the 14.29.30037
[x86](https://download.visualstudio.microsoft.com/download/pr/76a91598-ca94-410b-b874-c7fa26e400da/91C21C93A88DD82E8AE429534DACBC7A4885198361EAE18D82920C714E328CF9/VC_redist.x86.exe)/[x64](https://download.visualstudio.microsoft.com/download/pr/f1998402-3cc0-466f-bd67-d9fb6cd2379b/A1592D3DA2B27230C087A3B069409C1E82C2664B0D4C3B511701624702B2E2A3/VC_redist.x64.exe)
Visual C++ 2015 redistributables (see [Chocolatey
vcredist140](https://community.chocolatey.org/packages/vcredist140#versionhistory)).

See also the Microsoft download page for the latest [Visual C++
redistributables](https://support.microsoft.com/en-us/topic/the-latest-supported-visual-c-downloads-2647da03-1eea-4433-9aff-95f26a218cc0).

### msvcrtd, vcomp

**FIXME**: There is no known way to install these libraries.

### conhost.exe, ntoskrnl.exe, services.exe

These are Windows services and are only available in the OS native
bitness.

### d3d8

It may look like this file is missing when running the 64-bit tests on a
64-bit version of Windows. This is because Direct3D 8 is deprecated and
no 64-bit support for it is provided by Windows.

### d3dcompiler_43, d3dx9_36, xinput1_3

To get these dlls it is
[necessary](https://support.microsoft.com/kb/179113/en-us) to install the
[optional Direct X
components](https://www.microsoft.com/en-us/download/details.aspx?id=35),
even on the latest Windows systems.

**WARNING**: Uncheck the Bing Bar installation!

### d3dxof

If the 32-bit version is missing install the optional Direct X
components as documented above.

It may look like this file is missing when running the 64-bit tests on a
64-bit version of Windows. This is because d3dxof is deprecated and no
64-bit support for it is provided by Windows.

### d3dcompiler_46

**FIXME**: There is no known way to install this dll.

### d3drm

**FIXME**: There is no known way to install this dll.

### dmband, dmime, dplayx

WineTest may incorrectly claim that these dlls is missing. Check the
actual test results. If the 32-bit version is missing install the
optional Direct X components as documented above. No 64-bit version was
ever available because DirectMusic and DirectPlay are deprecated.

### dpnet, dpvoice

**FIXME**: There is no known way to install these libraries.

### infosoft

WineTest may incorrectly claim that this dll is missing. Check the
actual test results.

### localspl, localui, spoolss

**FIXME**: There is no known way to install these dlls.

### msado15, msdasql

These dlls are part of Microsoft Data Access Components. WineTest may
incorrectly claim that these dlls are missing. Check the actual test
results.

### msscript.ocx

**FIXME**: There is no known way to install this library.

### msxml4

MSXML4 SP3 is available
[here](https://www.microsoft.com/en-us/download/details.aspx?id=15697).
You may also want to apply the
[KB973685](https://support.microsoft.com/kb/973685) update. Note that
there is [no 64-bit
version](https://en.wikipedia.org/wiki/MSXML#Versions).

### msxml6

Wine implements the msxml6 dll but has no test for it yet. Still one can
get MSXML6 SP1
[here](https://www.microsoft.com/en-us/download/details.aspx?id=6276).

### ndis.sys

WineTest may incorrectly claim that this dll is missing. Check the
actual test results.

### qmgr

This is Windows' BITS download manager. WineTest may incorrectly claim
that this dll is missing. Check the actual test results.

### sapi

This is Windows' speech API library. WineTest may incorrectly claim that
this dll is missing. Check the actual test results.

### schedsvc

WineTest may incorrectly claim that this dll is missing. Check the
actual test results.

### vulkan-1

This library is installed by the graphics driver only if the GPU
supports the [Vulkan API](https://fr.wikipedia.org/wiki/Vulkan_(API)).

### wiaserv

WineTest may incorrectly claim that this dll is missing. Check the
actual test results.

### wintab32

**FIXME**: There is no known way to install this library.

### windows.devices.enumeration, windows.gaming.input, windows.gaming.ui.gamebar, windows.globalization, windows.media windows.media.devices, windows.media.speech

**FIXME**: There is no known way to install these dlls on Windows.

### xaudio2_7, xaudio2_8

This is the lastest audio API for Windows 7+. It may be installed
through this
[download](https://www.microsoft.com/en-us/download/details.aspx?id=35).

## Unix configuration

- Use the fvwm window manager

  *Rationale*: Most window managers are buggy, in particular the GNOME and
  KDE ones, and cause some tests to fail or even crash. fvwm is the one
  known 'good' windows manager.

- Use a Windows-compatible fvwm configuration

  *Rationale*: Some tests verify that Windows applications get the right
  sequence of messages when windows lose/gain focus, etc. The sequence of
  messages depends in part on the window manager and cannot be right if
  the Unix window manager does not behave like Windows does, particularly
  wrt. focus-follows-mouse, transient window decorations, etc.

  ```
  # The default fvwm config is pretty long and has tons of features of
  # dubious relevance for a test environment:
  # - It has a sidebar which may be causing the ole32:dragdrop test to fail.
  # - The virtual desktops are just an annoyance when accessing the machine
  #   through VNC.
  # So this configuration file completely replaces the default one and is
  # built from scratch with only the settings that have been deemed necessary.

  # fvwm's default SloppyFocus policy does not match the Windows behavior and
  # causes a lot of failures. So use ClickToFocus instead which best matches the
  # Windows behavior.
  Style * ClickToFocus

  # DontStackTransientParent is needed to avoid some failures in user32:win.
  # See https://www.winehq.org/pipermail/wine-devel/2018-February/122021.html
  Style * DontStackTransientParent

  # Wine uses MWM hints to get the proper window behavior.
  # So tell fvwm to obey these hints.
  Style * MwmDecor

  # Wine needs to be able to position windows as it wants.
  Style * UsePPosition

  # DecorateTransient does not seem to be needed for the tests but gives a proper
  # border to transient Windows like File Open dialogs. This makes them much more
  # usable and better matches the Windows behavior.
  Style * DecorateTransient

  # Don't use virtual desktops to avoid aggravation when the mouse goes out of
  # the VNC window.
  DesktopSize 1x1
  ```

- Install ttf-mscorefonts-installer (non-free) or fonts-liberation

  *Rationale*: No Windows system would ship without a base set of fonts of
  various families (Serif, Sans Serif). Since the lack of such fonts is
  not a valid Windows configuration, it is reasonable for tests (e.g.
  gdiplus:font) to depend on them and fail if they are missing.
  Furthermore ttf-mscorefonts-installer is preferred because it provides
  Arial which some tests need (but they skip if Arial is missing).

- Locking the screen may cause some extra failures. In particular
  locking the screen in KDE is known to cause comctl32:tooltips (bug
  54852), user32:input (bug 54853) and user32:win (bug 54854) to fail.

- Depending on the desktop environment and sound setup, some tests may
  need `XDG_RUNTIME_DIR` to be set. In particular this is known to be
  the case for a number of audio tests: quartz:dsoundrender,
  mmdevapi:capture, mmdevapi:render, winmm:mci and winmm:wave. This is
  particularly important if running the tests from cron for instance.
