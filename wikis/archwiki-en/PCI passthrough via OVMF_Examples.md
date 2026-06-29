# PCI passthrough via OVMF/Examples

As PCI passthrough is quite tricky to get right (both on the hardware and software configuration sides), this page presents working, complete VFIO setups. Feel free to look up users' scripts, BIOS/UEFI configuration, configuration files and specific hardware. If you have a problem, it might have been stumbled upon by other VFIO users and fixed in the examples below.

## Users' setups
## mstrthealias: Intel 7800X / X299, GTX 1070
Hardware:

* CPU: Intel(R) Core(TM) i7-7800X CPU
* Motherboard: ASRock X299 Taichi (Revision: A, BIOS/UEFI Version: 1.60A)
* GPU: Asus STRIX GTX 1070
* RAM: 32GB DDR4

Configuration:

* Kernel: Kernel version 4.14.8-1-skx (patched crystal_khz=24000).
** Custom patches:
*** skylakex-crystal_khz-24000.patch (see below)
** Patches used from linux-ck:
*** enable_additional_cpu_optimizations_for_gcc_v4.9+_kernel_v4.13+.patch
*** 0001-add-sysctl-to-disallow-unprivileged-CLONE_NEWUSER-by.patch
*** 0001-e1000e-Fix-e1000_check_for_copper_link_ich8lan-retur.patch
*** 0002-dccp-CVE-2017-8824-use-after-free-in-DCCP-code.patch
** Config:
*** PREEMPT, NO_HZ_IDLE, 300HZ, MSKYLAKE
* GitHub: Link TBD
* Benchmarks: https://imgur.com/a/hIfQD
* Using libvirt/QEMU: libvirt 3.10.0 / QEMU 2.11.0
* Issues you have encountered, special steps taken to make something work a bit better, etc.
** Skylake-X default clock incorrect in 4.14.8 (https://bugzilla.kernel.org/show_bug.cgi?id=197299)
*** Was unable to resolve timing issue using adjtimex
*** Patching kernel source to crystal_khz = 24000 resolved timing/performance issues
** Enable 'Intel SpeedShift' in BIOS, installed cpupower', set governor='performance'
*** Verify: Run  as root
**** intel_pstate: HWP enabled
** Enable HT in BIOS
** Enable 'deadline' IO sceduler:
*** echo 'ACTION=="add|change", KERNEL=="sd*ATTR{queue/scheduler}="deadline"' >> /etc/udev/rules.d/60-schedulers.rules
** Bypass x2apic opt-out:
*** GRUB_CMDLINE_LINUX="... intremap=no_x2apic_optout ..."
** Isolate cores for Windows VM:
*** GRUB_CMDLINE_LINUX="... isolcpus=2-5,8-11 nohz_full=2-5,8-11 rcu_nocbs=2-5,8-11 ..."
** Use hugepages (2MB) for all VM memory allocation
** memoryBacking:
** Extracted rom from GPU; used for  config
** Using MSI for GPU and GPU Audio (configured in Windows registry; FPS seems same as using line-based interrupts)
* Hardware setup
** PCIE1: NVIDIA GeForce GT 710B (for host)
** Onboard: ASRock XHCI 3.1 USB (for host)
** Onboard: Intel I219 NIC (bridged)
** PCIE3: Asus Xonar STX (passthrough to Win10)
** PCIE5: NVIDIA GeForce GTX 1070 (passthrough to Win10)
** M2_1: Samsung 960 EVO 500GB (passthrough to Win10)
** Onboard: Intel XHCI USB 3.0 (passthrough to Win10)
** Onboard: Intel HDA (passthrough to Win10)
** Onboard: Intel I211 NIC (passthrough to Win10)
** Onboard: ASRock AHCI SATA A1/A2 (passthrough to Linux)

## DragoonAethis: 6700K, GA-Z170X-UD3, GTX 1070
Hardware:

* CPU: Intel Core i7-6700K (using iGPU as the host GPU)
* Motherboard: Gigabyte GA-Z170X-UD3 (Revision 1.0, BIOS/UEFI Version: F23d)
* GPU: MSI GeForce 1070 Gaming X (10Gbps)
* RAM: 16GB DDR4 2400MHz

Configuration:

* Kernel: "Vanilla" Linux (no ACS patch needed).
* Using libvirt: XML domain, helper scripts, IOMMU groups, etc available in [https://github.com/DragoonAethis/VFIO my VFIO repository.
* Guest OS: Windows 8.1 Pro.
* The entire HDD is passed to the VM as a raw device (formatted as a single NTFS partition).
* USB keyboard and mouse are passed to the guest VM and shared with the host with Synergy.
* Virtualized audio: PulseAudio -> local Unix socket. Previously, I have had a bit more complex setup in which PA on the host was configured to accept TCP connections, and the environment variables required for QEMU to use PA were pointed at the PA server running on 127.0.0.1. This way it was not required to change the QEMU user (exact details in the repository), but introduced other minor issues I have resolved later.
* Bridged networking (with NetworkManager's and this tutorial's help) is used.  is created,  interface is bound to it. STP disabled, VirtIO NIC is configured in the VM and that VM is seen in the network just as any other computer (and is being assigned an IP address from the router itself, can communicate freely with other computers).
* For some reason, enabling  on the kernel command line without CSM support enabled in UEFI causes a black screen on boot. Enable it (Windows 8/10 features need to be enabled to show "CSM Support", selecting "Other OS" hides that).

## Manbearpig3130's Original Virtual Gaming Machine
Hardware:

* CPU: Intel Core i7-6850K 3.6GHz
* Motherboard: Gigabyte x99-Ultra Gaming (Revision 1.0, BIOS/UEFI Version: F4)
* Host GPU: AMD Radeon HD6950 1GB
* Guest GPU: AMD R9 390 8GB
* RAM: 32GB G-Skill Ripjaws DDR4 running at 3200MHz

Configuration:

* Host Kernel: Kernel version Linux 4.7.2-1.
* Using libvirt QEMU/KVM with OVMF: link to domain XMLs/scripts/notes: https://github.com/manbearpig3130/MBP-VT-d-gaming-machine
* Host OS: Arch Linux
* Guest OS: Windows 10 Pro
* 2x 480GB SSDs set up in LVM striped mode (with mdadm) formatted to ext4 are mounted in linux which contains the guest's qcow2 virtual VirtIO disk file.
* USB Host controller is passed through, giving most USB ports to the VM, leaving my USB 3.1 controller with attached USB hub for the host.
* Motherboard has two NICs, one is passed into VM (Works perfectly after installing Killer NIC Driver).
* VM gets dedicated 16GB RAM via static hugepages.
* CPU pinning increased performance considerably.
* Windows boots straight into Steam big picture mode on primary display (43" Sony Bravia). Overall an awesome gaming machine that meets my gaming needs and wants for GNU/Linux at the same time.

Quirks:

* I sometimes have to reinstall the AMD drivers in Windows to get HDMI audio working properly, or roll back to Windows HDMI driver. I normally use a USB headset which works fine anyway.

## Manbearpig3130's Evolved Virtual Gaming Machine
Hardware:

* CPU: Intel Core i7-6850K 3.6GHz
* Motherboard: Gigabyte x99-Ultra Gaming (Revision 1.0, BIOS/UEFI Version: F4)
* Host GPU: AMD Radeon R9 390
* Guest GPU: Nvidia 2080ti
* RAM: 32GB G-Skill Ripjaws DDR4 running at 3200MHz

Configuration:

* Host Kernel: Kernel version Linux 5.3.12-arch1-1
* Using libvirt QEMU/KVM with OVMF: link to domain XMLs/scripts/notes: https://github.com/manbearpig3130/MBP-VT-d-gaming-machine
* Host OS: Arch Linux
* Guest OS: Windows 10 Pro
* 2TB Intel 660P NVMe SSD passed through as storage. This needed a firmware update (sm2262 chipset) to pass through properly, but now that it works I also have the option to boot directly into Windows exclusively if I want to
* USB Host controller is passed through, giving most USB ports to the VM, leaving my USB 3.1 controller with attached USB hub for the host.
* Motherboard has two NICs, one is passed into VM (Works perfectly after installing Killer NIC Driver).
* VM gets dedicated 16GB RAM via static hugepages.
* CPU pinning increased performance considerably.
* Windows boots straight into Steam big picture mode on primary display.
* Intel 9260 Wi-Fi + Bluetooth M.2 card passed through for Xbox Series X/S controller
* Valve Index VR headset works perfectly in VM

Quirks:
* I have issues with one of my USB controllers, it seems like it stutters or resets. I can mitigate this by plugging devices into other USB busses, such as that on the 2080ti and also my USB 3.1 bus. This problem only occues in Windows. I originally thought it was due to it being in a VM, but since I set up my NVMe passthrough and can boot into Windows directly now I still have the same problem. Does not happen at all on Linux

## Bretos' Virtual Gaming Setup
Hardware:

* CPU: Intel Core i7-7700k
* Motherboard: Z270 GAMING M3 (MS-7A62)
* GPU: ASUS GeForce GTX960
* RAM: Kingston HyperX 3x8GB DDR4 2.4GHz
* Storage: 2x Corsair MP500 m.2 240G SSDs in mdadm RAID0, 1x WD Black 1TB for storage. 100GB LVM volume as writeback cache for HDD

Configuration:

* Kernel: vanilla
* Host OS: Arch Linux
* Guest OS: Windows 10 Pro
* Using libvirt/QEMU: GitHub config repository: * Issues you have encountered: AUDIO. Had to get USB audio adapter and pass it through.
* No issues other than audio. Works like a charm.

## droserasprout poor man's setup
Hardware:

* CPU: Intel Core i3-6100
* Motherboard: ASRock H110M2 D3 (BIOS version 0603)
* Host GPU: Intel HD 530
* Guest GPU: Sapphire Radeon R7 360
* RAM: Apacer 8Gb 75.C93DE.G040C, Kingston 4Gb 99U5401-011.A00LF

Configuration:

* Kernel: linux-lts 4.9.67-1 (vanilla)
* Host OS: Arch Linux
* Guest OS: Windows 10 Pro 1709 (build 16299.98)
* Using libvirt/QEMU: See my configs and IOMMU groups on [https://github.com/droserasprout/win10-vfio-configs Github
* HDD partition is passed to the VM as a raw virtio device.
* HD Audio is passed too. Works fine with both playing and recording, no latency issues or glitches. After VM is powered off host audio works fine too.
* Guest's latency is slightly better when CPU cores are isolated for VM.
* i2c-dev module added to bypass 'EDID signature' error when switching HDMI. Without it I had to switch video output before starting VM for some reason.
* intremap=no_x2apic_optout kernel option added to bypass motherboard firmware falsely reporting x2APIC method is not supported. Seems to have a strong influence on the guest's latency.
* Overall performance is pretty close to the native OS setup.

## prauat: 2xIntel(R) Xeon(R) CPU E5-2609 v4, 2xGigabyte GeForce GTX 1060 6GB G1 Gaming, Intel S2600CWTR
Hardware:

* CPU:2xIntel(R) Xeon(R) CPU E5-2609 v4
* Motherboard: Intel S2600CWTR(Revision ???, BIOS/UEFI Version: SE5C610.86B.01.01.0022.062820171903)
* GPU: 2xGigabyte GeForce GTX 1060 6GB G1 Gaming GTX 1060 6GB (rev a1)
* RAM: Samsung M393A2G40EB1-CPB  2133 MHz 64GB (4x16GB)

Configuration:

* Kernel: Linux 4.14.15-1-ARCH #1 SMP PREEMPT
* Using libvirt/QEMU: https://github.com/prauat/passvm/blob/master/generic.xml
* Most important:
* When using nvidia driver hide virtualization to guest
* Configuration works with Arch Linux guest os, still work in progress.

## Dinkonin's virtual gaming/work setup
Hardware:

* CPU:  Intel(R) Core(TM) i7-7700K CPU @ 4.60GHz
* Motherboard: MSI Z270 GAMING PRO CARBON (MS-7A63) BIOS Version: 1.80
* GPU: 1x Gigabyte GeForce GTX 1050 2GB (host), 1x MSI GeForce 1080 AERO 8GB(guest)
* RAM: 32GB DDR4

Configuration:

* Kernel: Kernel version linux 4.15.2-2-ARCH.
* Using libvirt/QEMU (patched from AUR) with OVMF
* Installed qemu-patched from AUR because of crackling/delayed sound with pulseaduio (still hear ocasional pops/clicks while gaming.
* Patched video bios with https://github.com/Matoking/NVIDIA-vBIOS-VFIO-Patcher, because of error:
 vfio-pci 0000:01:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0xffff
* Single monitor setup, implemented full software KVM(for host and guest) described here: https://rokups.github.io/#!pages/full-software-kvm-switch.md

## pauledd's unexeptional setup
Hardware:

* CPU: Intel Core i7 6700K
* Motherboard: Gigabyte GA-Z170N-WIFI Retail (Revision 1.0 , BIOS/UEFI Version: F20)
* GPU: 8GB Palit GeForce GTX 1070 Dual Aktiv PCIe 3.0 x16 (Retail)
* RAM: 16GB G.Skill RipJaws V DDR4-3200 DIMM CL16 Dual Kit

Configuration:

* Kernel: 4.15.2-gentoo
* Using libvirt/QEMU: libvirt-4.0.0, qemu-2.11.1, https://github.com/pauledd/GPU-Passthrough/blob/master/win10-2.xml , using vfio kernel module
* Had to dump VBIOS in at the host while GPU was normally attached (and drivers loaded) (see https://stackoverflow.com/a/42441234), had to set CPU settings manually according to my cpu (host-passthrough, sockets 1, cores: 4, threads: 2 ) or some games will regularly crash, see my xml how to insert vbios, still have audio clicking/lag with PulseAudio but that's ok for me, no further patching etc… works out of the box without any issues.
* 3DMark Results Time Spy Graphic Score: Native Windows 10: 5564 , GPU-Passthrough: 5541

## hkk's Windows gaming machine (6700K, 1070, 16GB)
Hardware:

* CPU: Intel Core i7-6700K 4.5GHz
* Motherboard: AsRock Fatality Gaming K6 Z170 (rev. 1.05)
* Host GPU: Intel GPU HD530 with 1GB shared memory
* Guest GPU: Gigabyte GeForce GTX1070 G1 Gaming 8GB
* RAM: 16GB G.Skill RipjawsV @ 3333 MHz CL14-15-15-31-2T Configuration:

* Host Kernel: Kernel version Linux 4.15.7-1-vfio (with ACS patch included).
* Using libvirt QEMU/KVM with OVMF
* Host OS: Arch Linux
* Guest OS: Windows 10 Pro
* 128GB Intel 600p SSD splited into 3 partitions: 512MB for EFI, 30GB for / in Btrfs and other gigs for Windows 10 installed straight on SSD.
* Two more HDDs for Windows. 1TB and 650GB
* Passed specific devices like X360 and some of single USB ports.
* One NIC behind NAT on VM machine.
* VM gets dedicated 8GB RAM via static hugepages.
* CPU pinning increased performance considerably and machine gets 4/4 cores of my 4/8 CPU
* Windows boots on second screen with simple script which shutting down display with xrandr.
* Using Synergy to share mouse and keyboard between systems.
* Quirks:
* Synergy is not perfect and will not entirely work in some games.
* No boot screen. Display is turning on only when Windows is up and ready to go.

## sitilge's treachery
Full info: https://github.com/sitilge/virtualization

Hardware:

* CPU: Intel Core i5 6600K
* Motherboard: Asus Z170i
* GPU: Gigabyte Radeon RX460 OC 2GB
* Storage: Samsung 850 EVO 500GB
* RAM: Corsair 16GB DDR4
* Mouse, Keyboard: Logitech M90, Vortex Pok3r

Host Configuration:

* Kernel: linux-vfio
* Packages: qemu-git, virtio-win, ovmf

Guest Configuration:

* OS: Windows 10 Pro
* CPU: host
* Motherboard: host
* GPU:  passthrough
* Storage: 64GB
* RAM: 8GB
* Mouse, Keyboard: passthrough

Notes:

* You can easy simlink the config files using  and then .
*  - guest might utilize only one core otherwise.
*  - I am passing mobo audio thus ac97. Download, unzip and install the Realtek AC97 drivers within a guest.
* Use virtio drivers for both block devices and network. For example, the ping went down from 250 to 50.
* Mouse and keyboard passthrough solved the terrible lag problem which was present in emulation mode.
* Make sure virtualization is supported and enabled in your firmware (UEFI). The option was hidden in a submenu in my case.
* As trivial as it sounds, check your cables.
* Be patient - it took more than 10 minutes for the guest to recognize the GPU.

## chestm007's "new" hackery
Hardware:

* CPU: Ryzen 9 9950x3D
* Motherboard: Asus ROG STRIX X870-F GAMING WIFI (BIOS/UEFI Version: 1605)
* GPU: Powercolor RedDevil RX 6800XT (EK waterblock)
* RAM: 128gb(4x32gb) Corsair 6000mhz

Configuration:

* Kernel: 6.17.1-zen1-1.1-zen.
* Using libvirt/QEMU: libvirtd (libvirt) 11.8.0, QEMU 10.1.0
*Window Manager: Hyprland

Notes:

* Dedicated GPU is passed to and from the host as needed, so it can still be used by games that work under linux. Prime Render Offload handles it appearing/disappearing.
* Q35 chipset, Firmware: UEFI
* HDA (ICH9) Audio
* have a working looking-glass setup, with a dummy output driver in windows
* Hard disks are all passed through raw
* an entire CCX is dedicated to the VM, as is 64gb of ram
* 4 iothread workers assigned to the "host" CCX

Issues:
* low FPS / stuttering, presumably caused by the iGPU being locked at 100% when using VM

## Eduxstad's Infidelity
Hardware:

* CPU: Ryzen 2600X @ 3.7 GHZ
* Motherboard: ASUS PRIME B350-PLUS(BIOS/UEFI Version: 4011)
* GPU1 (Guest): MSI 390 8GB @ Stock
* GPU2 (Host): XFX 550 4GB @ Stock
* RAM: 2 x 8GB (16GB) @ 3000 HZ
* Guest OS: Windows 8.1 Embedded Pro

Configuration:

* Kernel: 4.17.3-1-ARCH (vanilla).
* Using libvirt/QEMU: libvirt/virt-manager (https://github.com/eduxstad/vfio-config).
* Look in the repository for complete documentation of extra steps taken
* Overview: VM managed using virt-manager, using looking glass for primary io and built in spice display server as backup. Passing vm audio back to PulseAudio. Using hugepages for RAM. SCSI Drivers installed for hardware drive support.

## Pi's vr-vm
Hardware:

* CPU: i7-8700k @ 4.8 GHz
* Motherboard: MSI Gaming Pro Carbon (BIOS/UEFI Version: A.40/5.12)
* GPU: Palit RTX 2080 Ti
* RAM: 4x8GB G.Skill DDR4 @ 3000 MHz

Configuration:

* Kernel: latest mainline (rc if available)
** custom built with ZFS, WireGuard
** CONFIG_PREEMPT_VOLUNTARY=y to work around QEMU bug with long guest boot times
* Startup scripts/additional info: https://github.com/PiMaker/Win10-VFIO
* Issues encountered:
** PUBG would not launch at all
*** Solution: Enable the HyperV clock with  and disable hpet with
** VR would start to stutter badly after about 20-30 minutes of playtime (this one took me about 2 weeks to finally figure out :-)
*** Solution:
**** Enable invariant tsc passthrough with  (required even if using host-passthrough!)
**** Enable MSI for the GPU (using tool from [https://forums.guru3d.com/threads/windows-line-based-vs-message-signaled-based-interrupts-msi-tool.378044/ here)
**** Enable vAPIC and synic in the HyperV configuration
**** Manually move all IRQs to host cores using qemu_fifo.sh script from my GitHub repository above
* Overview: SteamVR-capable gaming and workstation rig, passing through NVIDIA GPU and onboard USB-controller (leaving an additional ASMedia USB port to the host). 22 GB hugepages memory, 10 of 12 cores (with SMT) passed through. Audio working via Scream (https://github.com/duncanthrax/scream) - with IVSHMEM, surprisingly low latency and no stutters.

## coghex's gaming box
Hardware:

* CPU: i7-8086k @ 5.0 GHZ (8086k is just a binned 8700k)
* Motherboard: GIGABYTE Z370 AORUS Gaming 7 rev1.0 (BIOS/UEFI Version: F15a)
* GPU: GIGABYTE GV-N108TAORUSX WB-11GD AORUS GeForce GTX 1080 Ti Waterforce WB Xtreme Edition 11G @ ~2Ghz
* RAM: 4 x 8GB (32GB) Corsair Dominator Platinum @ 3600 HZ (XMP)
Configuration:

* Kernel: linux-zen-5.5.8.zen1-1
* Modules: raid0 raid1 md_mod ext4 vfat ahci vfio_pci vfio vfio_iommu_type1 vfio_virqfd usbhid it87 (aur version is unmaintained and the support for the ITE8686E chip on this board is limited, replace it87 source with that which is found here for more comprehensive support)
* Virsh: virsh-5.10.0
* Qemu: qemu-system-x86_64-4.2.0 machine='pc-i440fx-4.2'
* Performance Services: irqbalance-1.6.0, ananicy-git-2.1.0.r22, cpupower5.5-1
* EDIT(2020): much has changed since this setup was posted years ago and a custom kernel is no longer needed on this hardware, everything works perfectly...
* scripts, libvirt XML, and personal configs can be found here: https://github.com/coghex/hoest
* host boot options: intel_iommu=on iommu=pt rd.driver.pre=vfio-pci acpi_enforce_resources=lax
* systemd modprobe.d options: kvm ignore_msrs=1 (avoids critical bugs), kvm report_ignored_msrs=N (cleans up journal logs)
* libvirt features: acpi, apic, kvm hidden state='on', vmport state='off'
* guest hyper-v options: hv-relaxed, hv-vapic, hv-spinlocks (retries='8191'), hv-vpindex, hv-runtime, hv-synic, hv-stimer, hv-stimer-direct, hv-reset, hv-vendor_id (value='1234567890ab'), hv-frequencies, hv-reenlightenment, hv-tlbflush, hv-ipi, (hv-evmcs and hv-no-nonarch-coresharing seemingly do not work yet in virsh)
* make sure to use the multifunction field for the GPU's hdmi audio controller and set them to the same slot, otherwise the audio interrupts will hang.  Someone should probably add that to the guide...
* im running the clock at 100Hz, the people running it at 1000 with the zen or ck kernel should know that the MuQSS scheduler works the same regardless of this speed and 1000 will just add more useless interrupts.
* cpu pinning works best for single VM performance, default host-passthrough works best for multiple running VMs.
* on windows, the MSI_util_v2 gets used every update to reset MSI interrupts on the GPU.
Hardware Specific:

* Fully-Functional Passthrough Devices: this motherboard has many PCI slots, all of these devices have been working flawlessly with little setup for years now:
** Inatek USB Card: KT5001 ** Creative Sound Card: 70SB155000001 [https://www.amazon.com/Creative-Labs-70SB155000001-Blaster-PCI-Express/dp/B01LYT7U99
** EDUP Wi-Fi Card: AC9636GS (must use virtio usb passthrough for bluetooth functionality) ** Intel Optane SSD: SSDPED1D480GASX [https://www.amazon.com/Intel-Optane-900P-480GB-XPoint/dp/B0772T4BVZ
** Zotac GeForce GT 710: ZT-71304-20L (this one does not seem to be available on amazon anymore, a shame since its one of the few high performance PCIEx1 cards...) * none of the proprietary gigabyte software works, in fact, it blue screens windows and installs itself as a startup program, forever locking you out.
* if anyone else uses this exact motherboard, there are two internal USB IOMMU groups, even with the ACS patch.  one will include the usb labeled "USB 3.1", and the other will include all the other USBs.  this means if you want more than just a keyboard and mouse, you will need either a usb hub to plug into the 3.1 slot and passthrough, or a PCIE USB bus.
* the two ethernet ports are in different IOMMU groups, making this a perfect motherboard for vfio.
* the ACS patch is needed on this motherboard if you want to use two graphics cards at once in separate IOMMU groups.  this sets the main GPU to PCIEx8 instead of x16.

## Roobre's VFIO setup
Hardware:

* CPU: Intel(R) Core(TM) i9-9900K CPU @ 3.60GHz
* Motherboard: Gigabyte Z390 M GAMING
* GPU: EVGA GTX 1080Ti
* RAM: 32GB DDR4 2400 (2x Ballistix)

Configuration:

* Kernel: Latest -ARCH (5.9.1-arch1-1 at the time of writing)
* Using libvirt/QEMU: libvirt 1:6.5.0-3, qemu 5.1.0-2. Config: https://gist.github.com/roobre/8f2d86a51a6b619a6622a64a58f9fc94
* ZFS volumes passed as raw devices for hard drives with virtio-scsi.
* VirtIO all the things! Download drivers from https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/

Issues:

* PulseAudio never worked good (too much crackling), so I ended up passing-through an USB 3.1 PCI controller and connecting an USB audio card to it. That card is then connected to one of my MoBo's inputs, and echoed using PulseAudio  module.

* Synergy works really great. On some games (ones who take control of the mouse pointer, e.g. first-person), you need to lock the mouse cursor to the VM window to avoid issues (camera moving too fast).

* Do not forget to add the needed snippet for the nvidia driver to run (PCI passthrough via OVMF#"Error 43: Driver failed to load" with mobile (Optimus/max-q) nvidia GPUs)

## laenco's VFIO setup
Hardware:

* CPU: Ryzen 9 3950X @ 4.15Ghz all-cores via PBO
* Motherboard: Asus ROG STRIX X470-F GAMING (BIOS/UEFI Version: 5406)
* GPU1 (Guest): Palit GeForce GTX 1080 8GB @ Stock
* GPU2 (Host): MSI RX 570 8GB @ Stock
* RAM: 4 x 16GB (64GB) @ 3333 MHz

Configuration:

* Guest OS: Windows 10 Pro
* Kernel: 5.4.13-arch1-1-gc (-ck is also good). No ACS patch.
* Using vanilla QEMU 4.2.0
* AMD Ryzen currently (2020.01.20) got bugged with SMP threads option - VM stuck on start.
* Got classic Nvidia error 43 - classically fixed. But also added some CPU flags which are set automatically with kvm=on found here https://github.com/qemu/qemu/blob/master/target/i386/cpu.c#L4008
* As pure QEMU have no option to pin CPU cores and self threads - using python script "cpu_affinity" - credits to https://github.com/zegelin/qemu-affinity/ and also a copy in my repository. Requires debug-threads=on
* Using dynamically allocated hugepages 2Mb
* Hardly using VirtIO
* Using hardware USB switch like Aten US224-AT and HDMI switch "many-to-one", which allow me to have one monitor, mouse, keyboard and some USB devices, and switch them by button between host and guest.
* Repository with current major system config and script for VM could be found here https://github.com/laenco/vfio-config

## zane's not working box
Hardware:

* MacBook Pro 11,x (2014 Model)
* CPU: Intel Core i7-4770HQ
* Motherboard: Apple
* GPU: Iris Pro 5200 for host, GTX 1660 eGPU over Thunderbolt 2 for guest
* RAM: 16GB

Configuration:

* Kernel: linux-vfio from aur 5.5.8
* qemu: 4.2.0
* libvirt: 5.10.0
* ovmf: 1:r26976.bd85bf54c2
* libvirt/QEMU: [https://gist.github.com/xzn/ef338049c91d21e9c1900982b21d9d32 libvirt setup; qemu setup

Description:
* The qemu script include lines for setting up device mapped file for raw disk access. 3D Performace is about 40% to 80% native depending on the application, with periodic lag spike/stutter.

Issues:
* Use apple_set_os.efi or  with refind to avoid black screen on start. This prevents Apple firmware from shutting down host iGPU when booting Linux/Windows.
* CPU pinning for guest is mandatory as it removes majority of stutters. After that isolate host CPU cores and pin emulator/IO threads as well. Pi's script for pinning IRQ handlers also helps. Hugepages for memory helps.
* Kernel parameters: . Everything starting with  are optional.  is mandatory or you will get  error in dmesg and Error 43 for the Nvidia driver in guest.
* Add  to your  as normal. Add  and  to your  as well.
* For me ACSO patch is mandatory, available from linux-vfio aur.
* Enabling MSI for guest GPU seemingly helps. Using  device and passthrough GPU on top of that DOES NOT seem to help, while making PulseAudio output cracks badly. Setting  for PulseAudio also makes it cracks badly so consider USB soundcard if needed. (I personally use the sound out on my monitor from guest). While I am not sure what this option does, setting  on PulseAudio audiodev reduces cracks.

## Muata's VFIO setup
Hardware:

* CPU: i7 4790
* Motherboard: MSI B85M-G43 BIOS/UEFI Version: V3.9 (03/30/2015)
* GPU: NVIDIA GeForce GTX 1060 6GB (MSI Gaming+)
* RAM: 16GB

Configuration:

* Kernel: linux-zen 5.5.11-1
* Using libvirt/QEMU: VFIO setup;
* qemu: 4.2.0
* libvirt: 5.10.0
* No issues at moment of writing this.

> I had some issues with the network, for example, I could not connect to Activision games servers (CoD: MW, Overwatch) but I have changed firewall settings from public to private and everything is good for now.

> For the first time, I had windows on .raw image and disk was throttling a lot, I have set up raid0 on my 2 HDD's, then I created 3 partitions with LVM - 120GB for windows, 700GB for data(games), 700gb for Linux data and passthrough two of partition as Virtio-BLK. RAID&LVM

> Audio passthrough is done through the usual PulseAudio solution, works nicely.

> For some people who, maybe looking how to passthrough GPU - because it's not obvious when you doing it for the first time and it's not on the wiki though, so when you pass a correct group of vfio-pci.ids then you need to add in (easiest way) a Virtual Machine Manager - Add hardware - PCI Host Device - You graphic card (for me it was 0000:01:00:0 NVIDIA Corporation GP106 GTX 1060 6GB).

## peterge's VFIO setup
Hardware:

* CPU: AMD Ryzen 5 3700X
* Motherboard: MSI x370 Gaming Pro Carbon
* GPU: SAPPHIRE PULSE Radeon RX 5700 XT (Host), MSI RX 570 (VM)
* RAM: 32GB

Configuration:

* Kernel: 5.11.11-arch1-1
* Using libvirt/QEMU: Xml File
* No issues right now.

> Mouse and keyboard passthrough with evdev.

> Monitor connected to both GPUs to display native 144hz.

> Needed this option in , related to my Ryzen CPU:

> Had problems passing sound to host with a ICH6 device, sound was crackeling and a bit delayed. Then switched to
scream-ivshmem and sound is working perfectly now. Its great in combination with looking-glass.

> Tried to build a solution where i can use my main GPU (GTX 1080) on Host and VM, by rebinding drivers. Rebinding drivers worked on the GTX 1080, but it was not able to use it to offload games from my host gpu back then Reddit Post (Got it working with an R9 380 for the host, but needed to restart xorg every time). Then bought the RX 5700 XT, where GPU offloading worked like a charm, but due to the early stage of driver support driver rebinding is not supported Reddit Post. So i currently have 2 GPUs in my rig.

## CaptainSolidus's VFIO Setup
Hardware:

* CPU: Intel Xeon E3-1245 V2
* Motherboard: Gigabyte Z77A-G45 (BIOS/UEFI Version: 2.12)
* Host GPU: AMD ATI Radeon HD 7950/8950 / R9 280 (AMDGPU with SI support enabled)
* Guest GPU: NVIDIA GeForce GTX 1060 6GB
* RAM: 2x8GB DDR3 1600 (8 for the host, 8 for the guest)

Configuration:

* Kernel: 5.7.4-1 (ACS-patched)
* Using libvirt/QEMU: libvirt 6.4.0/QEMU 5.0.0 VFIO repository
* Guest OS: Windows 10 Pro 2004
* Motherboard puts all PCIe lanes in a single IOMMU group, and no way to edit in BIOS, thus the ACS patch. There seems to be no issues having with this.
* CPU Pinning worked best, passing through CPUs 1,2,3,5,6,7 and leaving 0 & 4 for the host. Using "host-model" as CPU type and setting a topology helped with edge case crashes during benchmarking
* The Intel integrated graphics worked fine as well, but I kept the R9 280 for anything Linux native or older. Both GPUs work with Looking Glass.
* Switched to VirtIO drivers for SCSI and Networking, and ICH9 for audio.
* Keyboard and mouse are passed through via the evdev method
* Audio crackled using PulseAudio passthrough, so I switched to Scream over the bridged network, which works perfectly. The Scream client starts with the system, so I do not need to enable it on boot.
* Looking Glass is also set up, and works well on the client. The Looking Glass client is set to boot with the VM, and the VM is set to automatically login (via netplwiz)
* Setting up sleep prevention will help prevent the host machine sleeping while gaming in the VM

## ash's gaming machine
Hardware:

* CPU: Intel i5-8600k
* Motherboard: Aorus Z390 Ultra, rev. 1
* GPU: passthrough: AsRock Radeon Vega 56. host: Intel UHD 630
* RAM: 32GB G.SKILL Trident Z Neo, 16GB for Windows

Configuration:

* Kernel: 5.12.5-zen1-3-zen-ash-patches (custom kernel) or my custom tkg kernel, made with this

* Using libvirt/QEMU: libvirt through , QEMU with custom patches, found here

* i had a lot of issues getting my VM to boot. i first had to completely disable my  kernel driver, mainly in . i then had to add my GPU id from  to . i also had to force Xorg to use my Intel GPU in a file called . after combining all that with the information in the main PCI pass-through page, i was able to get everything to boot.

* all my configuration files are here

* i use  for audio, and barrier for moving my mouse from one monitor to another, like you would on a single OS system.

* i patched a couple upstream arch packages, mainly for VM detection evasion. those packages are QEMU, OVMF (edk2), and the linux-zen kernel. those patches are found at this repository. it also includes pre-built versions of the packages under the releases section. go check them out!

## Redecorating's vfio on a MacBookPro
Hardware:

* CPU: Intel i7-9750H
* Motherboard: MacBookPro16,1 (BIOS/UEFI Version: 1554.80.3.0.0 (iBridge: 18.16.14347.0.0,0))
* Guest GPU: AMD ATI Radeon RX Pro 5300M + Intel gvt-t virtual gpu
* Host GPU: Intel UHD Graphics 630
* RAM: 16GB, 8GB for guest

Configuration:

* Kernel: 5.10.12 (linux-mbp, which is for macs with the t2 chip).
* Using libvirt/QEMU: Libvirt (qemu backend)
* Enabled iGPU as described here.
* Had to isolate dGPU with vfio-pci from boot and use vendor-reset. Needed to pass through my usb-c ports as they are in the same iommu group, but not thunderbolt (guest gpu driver does not load if they are passed through). Only could install guest gpu drivers included with apple's "bootcamp support software".
* Libvirt xml and a more detailed explanation of quirks I had to work around are on this gist.
* Although there is a gmux chip in this laptop, it's unknown how to make the internal display switch between the iGPU and dGPU without rebooting.

## sashok724's VFIO setup
Hardware:

* CPU: Ryzen 3950X
* Motherboard: ASUS X570 Hero WiFi
* GPU (Host): RX 5700 XT
* GPU (Guest): GTX 1080 Ti
* RAM: 16x4 GB (64GB) @ 3600MHz CL16

Configuration:

* Kernel: Stock
* Using QEMU: 6.0.0
* Everything mostly worked out of the box. I only needed to enable IOMMU in UEFI.
* Repository with my configuration: https://github.com/new-sashok724/windows.sh/
* I am using systemd unit to start VM
* I have also passed through separate USB controller inside VM
* KVM hidden state is not needed in my case, since NVidia allowed using their GPUs in VMs recently
* Audio (HDA) also works fine without any stuttering out of the box

## QGJ's VFIO setup (CPU: Ryzen 5 3600XT / GPU: AMD RX 570)
Hardware:

* CPU: AMD Ryzen 5 3600XT
* Motherboard: MSI X470 Gaming Plus Max; BIOS version: 7B79vHC
* GPU (host): AMD Radeon R5 230
* GPU (guest): MSI Radeon RX 570 Gaming X 4GB
* RAM: 32 GB DDR4 in dual channel mode @ 3000 MHz

Configuration:

* Distribution: Gentoo
* Kernel: sys-kernel/gentoo-sources:5.15.5
* libvirt: 7.7.0
* QEMU: 6.0.0 (with ACPI table patch - needed for Red Dead Redemption 2)
* Guest VMs: Windows 11 Pro, macOS Monterey
* Link to my setup: https://github.com/q-g-j/gentoo-stuff

Notes:

* need the vendor-reset kernel module (strangely only when using macOS)
* enabled avic in kernel module kvm_amd
* fixed the L3 cache for my Ryzen
* passing through the onboard USB 3 controller
* using a custom libvirt hook script with the following features:- set the cpu governor- enable / disable some kernel optimizations- enable / disable hugepages- enable / disable WLAN bridging- start / stop scream audio with custom parameters- use one or more PCI devices alternately in the host and in the guest (virsh nodedev-detach / nodedev-reattach)
* WLAN bridging: uses "parprouted" to "join" the wlan interface and the bridge to one subnet
* patched QEMU and modified the xml to avoid crashes in the game "Red Dead Redemption 2"
* macOS: use my own OpenCore image optimized for Ryzen CPUs (AMD vanilla patches) and with some additional kexts
* installed a minimal Arch Linux as my 2nd distribution (dual-boot with Gentoo). This one runs headless and automatically boots two Windows 10 instances - one on each GPU. Works well for Multiplayer. Just needed to blacklist both radeon and amdgpu.

## Zexceil's VFIO setup
Hardware:

* CPU: AMD Ryzen 5 1600(Non-AF)
* Motherboard: ASUS Crosshair VII Hero(Wi-Fi) (BIOS/UEFI Version: 4402, AGESA V2 PI 1.2.0.3 Patch A)
* Host GPU: Nvidia Quadro NVS 510 2GB
* Guest GPU: XFX RX 580 8GB GTS XXX
* RAM: 4x8GB, 32GB~2666Mhz

Configuration:

* Distribution: Endeavour OS
* Kernel: Default packaged kernel(5.13.8-arch1-1 07/08/2021) patched with vendor-reset
* libvirt: 7.6.0
* QEMU: 6.0.0
* Guest VMs: Windows 10 Pro
* Guest VM XML: https://pastebin.com/50ZhZA1c
* Using libvirt/QEMU:
* Ensure that all CPUs except emulatorpin/iothread ones are using perfomance governer else choppiness experienced throughout, other CPUs use powersave to keep thermals good.
* Had to run modules "kvm" & "kvm_amd" with options "ignore msrs=1" & "nested=1" else cpu passthrough does not work, neither does Hyper-V in Win10(Delivers decent non-buggy perf).
* I do not use anything such as spice/looking-glass, guest gpu is connected to secondary monitor input.
* To get decent perfomance I have overclocked my CPU to 4Ghz.
* Resize-BAR is working.
* Tested on kernel 5.14-rc4(compiled from source), working fine.
* Ensure installation of VirtIO drivers for KB/Mouse(Obvious thing to do but I experienced horrible KB/Mouse perf without it and then came to realization)

## UtkarshVerma's VFIO Setup
Hardware:

* CPU: AMD Ryzen 3550H
* Motherboard: TUF Gaming FX505DT_FX505DT 1.0 (BIOS/UEFI Version: FX505DT.316)
* GPU: NVIDIA GeForce GTX 1650
* RAM: 8GB

Configuration:

* Scripts: https://github.com/UtkarshVerma/qemu-vfio-win10
* Kernel: Linux 5.14.1
* Using libvirt/QEMU: QEMU (plain QEMU)
* Running the VM is as simple as `sudo ./launch.sh`. It takes care of everything mentioned below in a distribution-agnostic way.
* Hugepages
* HyperV enlightenments
* Dynamic VFIO passthrough for NVIDIA GPU, i.e. GPU is usable by host after guest exits.
* Respects NVIDIA Runtime D3 power management
* evdev passthrough using persistent-evdev.py
* Looking Glass: SPICE input and clipboard sharing; DMA buffer support; Auto shared memory creation
* virtio devices
* PulseAudio audio device passthrough
* CPU pinning with qemu-affinity
* CPU governor configuration
* Runs QEMU with jemalloc() memory allocator

## Shimmy's VFIO Setup
Hardware:

* CPU: AMD Ryzen 5 1600 (original, non-AF) OC @ 3.6 GHz
* Motherboard: MSI B350 Gaming Plus (BIOS/UEFI Version: 7A34vMHS)
* Host GPU: XFX AMD Radeon RX 550 2 GB
* Guest GPU: ASUS AMD RX 6600 XT DUAL OC 8GB GDDR6
* RAM: 32 GB, 2x16GB @ 3200 MHz OC (in BIOS for the setup, RAM is native 3200) in dual channel
* Storage: Crucial MX500 1 TB (dedicated entirely to the VM)

Configuration:

* Host OS: Arch Linux 5.16.11
* Guest OS: Windows 10 Home
* Using libvirt/QEMU: QEMU 6.2.0, libvirt 8.0.0
* XML config
* Used to run Gigabyte GTX 1050 Ti as guest GPU
* To achieve CPU passthrough I had to run `kvm ignore_msrs` options.
* CPU cores pinning + systemd separation while the VM is running
* Running the VM both directly to a 4K @ 144Hz dispaly and via Steam Link to TV
* Looking Glass setup but rarely used
* Running a bridged network to allow LAN access from TV
* Managing by virt-manager or Cockpit to remotely start the VM
* I have a separate "no evdev" setup in case I want to run the VM without any evdev devices
* Needed `softdep amdgpu pre: vfio-pci` modprobe in my config for the amdgpu driver to not pickup guest GPU first. For some reason MODULES orderd in mkinitcpio didn't cut it.

## yv-fr VFIO setup (CPU: Ryzen 3900 / GPU: 1080 & 3090)
Hardware:
* CPU: AMD Ryzen 9 3900X 12-Core @ 24x 3.8GHz
* Motherboard: ASRock x570 Taichi / Bios version=P4.40
* Host GPU: NVIDIA GeForce GTX 1080 WATERCOOLED
* Guest GPU: NVIDIA GeForce GTX 3090 WATERCOOLED
* RAM: GSKILL GTRZ 16GB 4200 @3333
* Storage: Dedicated SSD for guest.

Configuration:
*Distribution: Archcraft
*Kernel: x86_64 Linux 5.16.11-arch1-1
*QEMU:(ACPI table patch version from this REDDIT before running anything. If not windows hold the pre patched ACPI info - needed for Red Dead Redemption 2)
*Guest VMs: Windows 11 Pro
*Link to my setup: XML
*passthrough GPU is not usable by host after guest exits.
*On this X570 All USB port are not on the same IOMMU group.

Notes:
*fixed the L3 cache by using vcpu used in pastebin link.
*using udev keyboard+mouse passthrough
*sound from the host without tear
*here' s links that help me verry well uppon the wiki to construct this virtualisation. Gratefull to them
https://www.tauceti.blog/posts/linux-amd-x570-nvidia-gpu-pci-passthrough-1-the-hardware/
https://www.heiko-sieger.info/windows-10-vfio-passthrough-configuration/

## Drakensons VFIO Setup
Hardware:

* CPU: Ryzen 5700G
* Motherboard: MAG B550 TOMAHAWK
* GPU: Nvidia GTX1070
* Host GPU: iGPU of the CPU - Tipp: When choosing a mainboard, look for one with enough onboard video outputs!
* RAM: 32GB Crucial Ballistix DDR4-3200 (16G goes to the VM)
* Storage: 1x 512G Samsung 970 Evo Plus (NVMe), 1x 1TB WD blue SSD (SATA), 1x 2TB Samsung 970 Evo Plus (NVMe) - each one contains next to other data from my host a .raw-image file, maped to the VM, using BTRFS on the host, these files rest in a separate subvol with disabled COW.

Configuration:

* Kernel: Vanilla Arch Kernel, no patches
* libvirt/QEMU: Using libvirt
* Guest: Windows 10 Professional (for the possiblity to log into the guest using RDP)
* config files: Github
* Optimizations:
* CPU Pinning used, giving 6 Cores (12 threads) to the VM, using both threats of core 7 for the iothread, leaving core 8 and its thread for the host system for Youtube etc.
* Using Looking Glass to access the machine, my old build had only 3 Cores for the VM, there i've encountered massive frame drops, on this system it runs absolutly smoothly at 1920x1080@60
* Using Scream to redirect audio to the host, same as with looking glass applies here, with the current system no problems at all.
* I've had some problems with the vfio driver, where the nvidia card initialized the efi framebuffer, which lead to some problems like nonbooting vms oder no image outboot during host boot. These problems could be solved using the  kernel parameter.
* I am using dynamic hugepages for the slight placebo-like feeling that the VM runs smoother this way, to initialize these I'm using the qemu libvirt hook as seen in my config files.
* Keyboard and Mouse is passed through using evdev - while using razer peripherals this has the plus, that colors and macro keys can be configured under linux, eliminating the need to install the synapse driver onto the guest.

## JudgeHolden's Setup
Hardware:

* CPU: Ryzen 5900x
* Motherboard: x570 Aorus Master
* GPU: Nvidia RTX 3070, Nvidia RTX 3080 Ti
* RAM: 32 GB (16x2), DDR4-3200 CL 14-14-14-34

Configuration:

* Kernel: Vanilla Arch ACS-Patch
* Using libvirt/QEMU
* The only pronounced problem I've encountered is having performance issues after a lot of uptime the virtual machine(s) seem to start being randomly sluggish. I remedied this by implementing hugepagesz via kernel command line: `BOOT_IMAGE=/vmlinuz-linux root=UUID=4c86c780-3d89-4763-8f94-74f71dd009f1 rw loglevel=3 quiet kvm.ignore_msrs=1 video=efifb:off pcie_aspm=off pcie_acs_override=downstream,multifunction mitigations=off default_hugepagesz=1G hugepagesz=1G hugepages=16`
* I do not pin or isolate any cores. I run an VM instance of win10 enterprise utilizing each GPU. I use my motherboard's soundcard for my 3080 Ti VM, I use my 3070's audio card (monitor aux output) for the other VM. I have a bridge set up (via nmtui) so all drives can be shared on the network (as well as host the occasional gameserver) from the guests and host. I use USB controller passthrough for both VMs. The 3080 Ti is plugged into a 4k 55" TV that is sitting 3-4 ft in front of a loveseat (xbox controller, wireless kbm/touchpad, wired kbm, and usb switch are in this vicinity), while the 3070 is plugged into a single 240hz monitor at a desk with a gaming mouse and keyboard. The only device that is virtual/virtio device on either VM is the virtio NICs (if you don't count the CPU), and one block device HDD on the 3080 Ti VM.
3080 Ti XML: http://ix.io/4jyV
3070 XML: http://ix.io/4jyW

I used to have 28 hugepagesz allotted for both VMs, but have since been utilizing the host desktop a bit more so I needed to free up the RAM. So far there's been no performance problems on the 3070 VM since only giving hugepagesz to the 3080 Ti VM

## Nedia's Setup
Hardware:

* CPU: i5 13600K
* Motherboard: MSI MPG Z790I EDGE WIFI
* GPU: MSI Radeon RX 6750 XT
* RAM: 32GB 5200MHz DDR5

Configuration:

* Kernel: Vanilla
* Using libvirt/QEMU: libvirt
* XML: https://git.sr.ht/~nedia/vm/tree/main/item/win11.xml
* Guest: Windows 11 for gaming.
* Resizable BAR disabled in BIOS.
* CPU core 0 not pinned, left for host, and cores 1-5 (threads 2-11) pinned so my VM will use all of my CPU's performance cores. Initially had pinned threads 2-13 which caused issues (stutters).
* Dedicated bluetooth dongle for connecting bluetooth devices (headphones, controller).
* 512GB SCSI disk for games, as well as 2 NVMe SSD's for games (PCI passthrough).

## Aym vfio setup
Using on X570 setup for operating Host (archlinux) and two additional VM with their own GPUs

Hardware:

* CPU: Ryzen 5950x
* Motherboard: Gigabyte Aorus X570 Master 1.2 newest bios
* GPU:
**           Host: Nvidia RTX 3060Ti
**           Guest1: Nvidia RTX 3070
**           Guest2: Nvidia RTX 3070
* RAM: 4x16Gb Gskill B-Die 3200 cl14
* USB: Additional USB Pciex1 by Fresco Logic FL1100
* Monitors: 3x IPS with 144hz , 240 hz , 280 hz

Configuration:

* Kernel: Arch Linux kernel 6.4 (with kernel >6.0 there is bug so vfio is done later when loading modules post)
* Using libvirt/QEMU KVM 8.1:
* In same time using Host and 2 VMs (Windows or Arch Linux)
* scripts, libvirt XML, and personal configs can be found here: config
* USB are passthough by own group so 2 VM had their own USB controllers (one from MB and one from Fresco)
* GPU are connected by risers with Pcie4.0 standard
* 2xNVME are passthrough by their own group to VM's and one NVME for host
* Used Isolated NIC for internal talk to VMs
* Used Barrier to communicate via TCP for taking mouse and keyboard on VM's
* CPU pinning was done VM1:cpuset="8-11,24-27">8 cores VM2:cpuset="12-15,28-31">8 cores
* DKMS vendor-reset-dkms-git get rid of errors when restarting VMs
* Audio passthrough by Pipewire-pulse
* Added CPU affinity by this this tutorial's
* NIC has been pass by MACTAP
* Latency is super stable, spikes are only generated by Nvidia Kernel Driver occasionally
* MSI interrupt done via MSI_util_v2
* Scaling governor is triggered by Hooks as MASK affinity Hooks/qemu.conf
* Host GPU is in PCiex16 slot3 marked to boot from Gigabyte bios. No chipset bandwitch affected or noiced.
* Hugepages are divided 2x16Gb ram for each VM

## Alydev vfio setup
Hardware:

* Laptop: Acer Nitro 5 AN515-57
* CPU: i5-11400H @ 2.70GHz
* GPU: GeForce RTX 3050 Mobile
* RAM: 24gb generic SODIMM DDR4

Configuration:

* Summary: OVMF on NVIDIA laptop with Arch host, Windows 10 guest, pcie passthrough, Looking Glass for laptop monitor, synchronized screen idle blanking, bluetooth device passthrough and hotplugging with evdev, GRUB boot entries to switch between Windows having the GPU and Arch retaining control of it

Details and configurations can be found on the user's GitHub repository.

* Kernel: 6.7.4-arch1-1
* Using libvirt 10.0.0, QEMU 8.2.0
* Using persistent-evdev for hotplugging and bluetooth peripheral passthrough: aiberia/persistent-evdev
* Looking Glass on Windows for laptop monitor
* DPMS trigger over SSH to synchronize screen blanking

## 0xMrRobot's gaming setup
I set this win11 VM to play games that don't run via Proton, as well as windows-exclusive programs that I need to use at my university.

Hardware:
* Laptop: Alienware m16 R1
* CPU: Intel i9-13900HX
* GPU: Nvidia RTX 4070 Laptop GPU
* RAM: 32 GB SODIMM DDR5 @ 5600 MT/s

Configuration:
* Kernel:
* Using libvirt/QEMU/KVM: Yes
* I use a patch to make virtiofsd work alongside Looking Glass, and a physical SSD as the VM's storage for better I/O performance. I pin 8 vCPUs to the VM, and 8 more for the emulator/iothread, leaving 16 to the host. I passthrough my dGPU and use a dummy miniDP plug for Looking Glass to work.
* I explain my setup in extensive detail in my personal laptop's page.

## Adding your own setup
Add a new section with your nickname, CPU, motherboard and GPU models, then copy and paste this template to your section:

Replace proper sections with your own data. Make sure to provide the exact motherboard model, revision (if possible - should be on both the motherboard itself and the box it came in) and BIOS/UEFI version you are using. Describe your exact software setup and add a link to your configuration files. (GitHub, GitLab, BitBucket, etc can host a public repository which you may update once in a while, but uploading them to pastebins is fine, too. Do not post the entire config file contents here.)
