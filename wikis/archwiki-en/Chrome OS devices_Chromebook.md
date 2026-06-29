# Chrome OS devices/Chromebook

The first generation of Chromebooks: Google Cr-48, Samsung Series 5 500 and Acer AC700 use Insyde H2O firmware and not Coreboot firmware. There are three approaches how to install Arch Linux on these devices:

* Flash a custom H2C firmware (only available for Google Cr-48) and install Arch as on any other UEFI laptop.
* Take the ChrUbuntu approach which uses the Chrome OS kernel and modules.
* Build and sign your own kernel, see == Hardware comparisons ==

For a more extensive list, please have a look at the one maintained by the [https://docs.chrultrabook.com/docs/devices.html Chultrabook community.

{| class="wikitable sortable"
|-
! colspan=11
|-
! Available
! Brand
! Model
! Processor
! RAM
! Storage
! Upgradable
! Screen
! Resolution
! SeaBIOS
! Remarks
|-
| Dec 2010
| Google
| Cr-48
| Intel Atom N455
| rowspan="3"|2GBDDR3
| rowspan="4"|16GB SSD
|
| rowspan="2"|12.1 in(30.7 cm)
| rowspan="2"|1280x800(16:10)
|
|
|-
| Jun 2011
| Samsung
| Series 5XE500C21
| rowspan="2"|Intel Atom N570
|
|
|
|-
| Jul 2011
| Acer
| AC700
|
| 11.6 in(29.5 cm)
| 1366x768(16:9)
|
|
|-
| May 2012
| Samsung
| Series 5XE550C22
| Intel Celeron 867Intel Core i5 2467M
| 4GBDDR3
|
| 12.1 in(30.7 cm)
| 1280x800(16:10)
|
|
|-
| Nov 2012
| Acer
| C710
| Intel Celeron 847Intel Celeron 1007U
| rowspan="2"|2-4GBDDR3
| rowspan="2"|320GB HDD16GB SSD
|
| 11.6 in(29.5 cm)
| rowspan="3"|1366x768(16:9)
|
|
|-
| rowspan="3"|Feb 2013
| HP
| Pavilion 14Chromebook
| Intel Celeron 847
|
| 14 in(35.6 cm)
|
|
|-
| Lenovo
| ThinkPad X131eChromebook
| Intel Celeron 1007U
| 4GBDDR3
| 16GB SSD
|
| 11.6 in(29.5 cm)
|
|
|-
| Google
| ChromebookPixel
| Intel Core i5 3427U
| 4GBDDR3
| 32GB iSSD64GB iSSD
|
| 12.85 in(32.6 cm)
| 2560x1700(3:2)
|
|
|-
| rowspan="2"|Nov 2013
| HP
| Chromebook 14
| Intel Celeron 2955U
| rowspan="2"|2GB DDR34GB DDR3
| rowspan="2"|16GB SSD32GB SSD
|
| 14 in( 35.6 cm)
| rowspan="9"|1366x768(16:9)
|
|
|-
| Acer
| C720/C720PChromebook
| Intel Celeron 2955UIntel Core i3-4005U
|
| 11.6 in(29.5 cm)
|
|
|-
| Jan 2014
| Toshiba
| CB30/CB35Chromebook
| Intel Celeron 2955U
| 2GB DDR3
| 16GB eMMC
|
| 13.3 in(33.8 cm)
|
|
|-
| Apr 2014
| Dell
| Chromebook 11
| Intel Celeron 2955UIntel Core i3-4005U
| 2GB DDR34GB DDR3
| rowspan="2"| 16GB eMMC
|
| rowspan="2"| 11.6 in(29.5 cm)
|
|
|-
| rowspan="4"|Jun 2014
| Lenovo
| N20/N20PChromebook
| rowspan="2"|Intel BayTrail-M N2830
| 2GB DDR3
|
|
|
|-
| Asus
| Chromebook C200/C300
| 2GB DDR34GB DDR3
| 16GB eMMC32GB eMMC
|
| 11.6 in(29.5 cm)13.3 in(33.8 cm)
|
|
|-
| rowspan="2"|Lenovo
| ThinkPad 11eChromebook
| rowspan="2"|Intel BayTrail-M N2930
| rowspan="3"|4GB DDR3
| rowspan="2"|16GB eMMC
|
| rowspan="3"|11.6 in(29.5 cm)
|
|
|-
| ThinkPad Yoga 11eChromebook
|
|
|
|-
| Jul 2014
| HEXA
| Chromebook Pi
| Intel BayTrail-M N2830
| 32GB eMMC
|
|
|
|-
| rowspan="2"|Sep 2014
| Toshiba
| CB30/CB35Chromebook 2
| Intel BayTrail-M N2840
| 2GB DDR34GB DDR3
| rowspan="2"| 16GB eMMC
|
| 13.3 in(33.8 cm)
| 1366x768(16:9)1920x1080(16:9)
|
|
|-
| rowspan="2"|Acer
| CB3-111Chromebook 11
| Intel BayTrail-M N2830
| 2GB DDR3
|
| rowspan="6"|11.6 in(29.5 cm)
| rowspan="6"|1366x768(16:9)
|
|
|-
| rowspan="3"|Oct 2014
| C730Chromebook 11
| rowspan="4"|Intel BayTrail-M N2840
| rowspan="2"|2GB DDR34GB DDR3
| 16GB eMMC32GB eMMC
|
|
|
|-
| HP
| Chromebook 11G3
| rowspan="3"|16GB eMMC
|
|
|
|-
| Samsung
| Chromebook 2XE500C12
| 2GB DDR3
|
|
|
|-
| rowspan="3"|Feb 2015
| Dell
| Chromebook 113120
| rowspan="3"| 2GB DDR34GB DDR3
|
|
|
|-
| rowspan="3"|Acer
| C740 (EDU)Chromebook 11
| rowspan="2"|Intel Celeron 3205UIntel Core i3-5005U
| 16GB SSD32GB SSD
|
|
|
|-
| CB5-571Chromebook 15
| 16GB32GB
|
| rowspan="2"|15.6 in(39.6 cm)
| rowspan="2"|1366x768(16:9)1920x1080(16:9)
|
|
|-
| rowspan="3"|Mar 2015
| C910 (EDU)Chromebook 15
| Intel Celeron 3205UIntel Core i3-5005UIntel Core i5-5200U
| 4GB DDR3
| 16GB SSD32GB SSD
|
|
|
|-
| Google
| ChromebookPixel 2
| Intel Core i5-5200UIntel Core i7-5500U
| 8GB DDR316GB DDR3
| 32GB64GB
|
| 12.85 in(32.6 cm)
| 2560x1700 (3:2)
|
|
|-
| Lenovo
| N21Chromebook
| rowspan="2"|Intel BayTrail-M N2840
| 2GB DDR34GB DDR3
| rowspan="2"|16GB eMMC
|
| rowspan="2"|11.6 in(29.5 cm)
| rowspan="2"|1366x768(16:9)
|
|
|-
| Jan 2016
| Acer
| CB3-131-C8GZ(Chromebook 11)
| 4GBDDR3
|
|
|
|-
| Jun 2016
| Lenovo
| ThinkPad 13 Chromebook (sentry)
| Intel Core i5-6300U (Skylake)
| 8GBLPDDR3
| 32GB eMMC
|
| 13.3&nbsp;in(33.8&nbsp;cm)
| 1366x768 (16:9)
|
|
|-
| Oct 2017
| Google
| Pixelbook
| Intel Core i5-7Y57Intel Core i5-7Y57Intel Core i7-7Y75
| 8GB DDR38GB DDR316GB DDR3
| 128GB256GB512GB
|
| 12.3 in(31.2 cm)
| 2400x1600 (3:2)
|
|
|-
| March 2018
| Acer
| Chromebook 11 (C732) Astronaut
| Intel Celeron N3450
| 4GB LPDDR48GB LPDDR4
| 32GB64GB
|
| 11.6 in  (29.5 cm)
| 1366 x 768 (16:9)
|
|
|-
| March 2020
| Lenovo
| IdeaPad Flex 5 13IML05 Chromebook
| Intel Celeron 5205UIntel Core i3-10110UIntel Core i5-10210U
| 4GB DDR48GB DDR4
| 32GB eMMC64GB eMMC128GB SSD256GB SSD
|
| 13.3 in  (33.8 cm)
| 1920 x 1080 (16:9)
|
|
|-
| September 2020
| Lenovo
| IdeaPad Flex 3 CB 11IGL05
| Intel Celeron N4020
| 4GB LPDDR4-24008GB LPDDR4-2400
| 32GB eMMC64GB eMMC128GB SSD
|
| 11.6 in  (29.5 cm)
| 1366 x 768 (16:9)
|
|
|-
| April 2021
| Lenovo
| ThinkPad C13 Yoga
| AMD Ryzen™ 7 3700C
| 16GB Soldered DDR4-2400
| 256GB SSD
| 80mm M.2 NGFF
| 13.3 in(33.8 cm)
| 1920 x 1080 (16:9)
|
|
|-
| August 2021
| Acer
| Chromebook CX5500
| Intel Core i3-1115G4Intel Core i5-1135G7Intel Core i7-1165G7
| 8G LPDDR416G LPDDR4X
| 128GB SSD256GB SSD512GB SSD
|
| 15.6 in(39.6 cm)
| 1920 x 1080 (16:9)
|
|
|-
| October 2021
| Lenovo
| Ideapad 3i Chrome 15IJL6
| Intel N4500
| 4G LPDDR4
| 64GB SSD
|
| 15.6 in(39.6 cm)
| 1920 x 1080 (16:9)
|
|
|}
