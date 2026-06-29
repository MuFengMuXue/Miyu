# Qnix QX2710

This article is a short tutorial on how to get the QX2710 to work well on Linux.

## Fixing X11 with Nvidia
By default, on some graphics drivers, the QX2710 will enter a debug mode and flip through colors when you start up X. The reason for this is that the driver is having issues reading the EDID from the monitor.

This issue with reading the EDID does not occur on Windows, so the read EDID can be acquired with a live Windows media. An example EDID bin that was exported using Monitor Asset Manager from Windows 11 is available for download QX2710.bin

* Copy the edid file to  (create the directory if needed)
* Remove any nvidia-generated xorg configs in
* Find the ID of the monitor through the following command
 $ nvidia-xconfig --query-gpu-info
Another possibility is to look up the monitor id in the  file.
* Create  and add the following to it (remember to change DFP-0 to your monitor ID)

* Save the file then restart X. Your monitor should now be working.
Yet another possibility is to write a fixed EDID to the monitor with EDID/DisplayID Writer the program will detect that the checksum indicates the EDID is corrupt and will offer to fix the problem.
