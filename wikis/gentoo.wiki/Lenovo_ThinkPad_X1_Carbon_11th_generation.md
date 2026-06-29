**Resources**

[[]][Product Information](https://www.lenovo.com/us/en/p/laptops/thinkpad/thinkpadx1/thinkpad-x1-carbon-gen-11-(14-inch-intel)/len101t0049)

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-x-series-laptops/thinkpad-x1-carbon-11th-gen-type-21hm-21hn)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_X1_Carbon_Gen_11/ThinkPad_X1_Carbon_Gen_11_Spec.pdf)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/ThinkPad/ThinkPad_X1_Carbon_Gen_11?tab=model)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/x1carbon_gen11_x1yoga_gen8_hmm_en.pdf)

[[]][User Guide](https://download.lenovo.com/pccbbs/mobiles_pdf/x1carbon_gen11_x1yoga_gen8_linux_ug.pdf)

[[]][BIOS Setup](https://download.lenovo.com/pccbbs/mobiles_pdf/lenovo_bios_setup_linux_wmi_sysfs_1.2.pdf)

[[]][ThinkPad X1 series](https://en.wikipedia.org/wiki/ThinkPad_X1_series "wikipedia:ThinkPad X1 series")

\

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [System Model Verfication]](#System_Model_Verfication)
    -   [[1.2] [Standard]](#Standard)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USEflags]](#USEflags)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Intel MIPI Camera]](#Intel_MIPI_Camera)
-   [[4] [See also]](#See_also)
-   [[5] [References]](#References)

## [Hardware]

### [System Model Verfication]

`root `[`#`]`dmidecode -s system-version`

    ThinkPad X1 Carbon Gen 11

### [Standard]

  ------------ ------------------------------------- -------- ------------------------ -------------------------------------- ---------------- -------
  Device       Make/model                            Status   Vendor ID / Product ID   Kernel driver(s)                       Kernel version   Notes
  CPU          13th Gen Intel(R) Core(TM) i7-1370P   Works    N/A                      N/A                                    6.7.7
  Video card   Iris Xe Graphics                      Works    8086:a7a0                i915                                   6.7.7
  Wireless     Intel Corporation Wireless-AC 9462    Works    8086:0090                iwlwifi                                6.7.7
  Speakers     Lenovo Raptor Lake-P/U/H              Works    17aa:2315                snd_hda_intel, snd_sof_pci_intel_tgl   6.7.7
  Microphone   Lenovo Raptor Lake-P/U/H              Works    17aa:2315                snd_hda_intel, snd_sof_pci_intel_tgl   6.7.7
  ------------ ------------------------------------- -------- ------------------------ -------------------------------------- ---------------- -------

## [Installation]

### [USEflags]

  --------------- -----------------------------------------------------------------------
  USEflag         Purpose
  `bluetooth`     Bluetooth for Linux
  `nvme`          nvme disk support and firmware update
  `synaptics`     Synaptics touchpad and fingerprint reader support und firmware update
  `thunderbolt`   Thunderbolt support and firwmare update
  `tpm`           Trusted Platform support and firmware update
  `uefi`          UEFI support and firmware update
  --------------- -----------------------------------------------------------------------

## [Troubleshooting]

Troubleshooting specific hardware issues can be challenging, especially when dealing with complex components like the Intel MIPI camera, which is known for its compatibility issues on Linux.

### [Intel MIPI Camera]

Getting the Intel MIPI camera to work can be particularly tricky due to the lack of open-source drivers and specific firmware requirements. Users might experience difficulties in making the camera fully operational under Linux.

For advanced configurations, troubleshooting tips, and ongoing driver development efforts, refer to the Intel camera IPU6 GitHub repository. This resource provides valuable insights, community support, and potential workarounds for getting the Intel MIPI camera up and running.

External Resource: [Intel ipu6 Camera](https://github.com/intel/ipu6-drivers)

## [See also]

-   [Lenovo_ThinkPad_X1_Carbon_8th_generation](https://wiki.gentoo.org/wiki/Lenovo_ThinkPad_X1_Carbon_8th_generation "Lenovo ThinkPad X1 Carbon 8th generation")

\

## [References]