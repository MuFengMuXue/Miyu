# Elgato EyeTV DTT Deluxe v2

Also called Elgato EyeTV DTT Deluxe 2009, it is a DVB-T USB device from Elgato intended for use with Apple Computer based systems.

## Installation
Install .

Download the firmware and copy the files to

 $ wget https://kernellabs.com/firmware/as102/as102_data1_st.hex
 $ wget https://kernellabs.com/firmware/as102/as102_data2_st.hex
 # mv as102_data* /usr/lib/firmware
 # chmod 644 /usr/lib/firmware/as102_data*

Now you can plug it in and you are ready to go.

## Use
When plugged, you should see the following:

More info on DVB-T can be found on the DVB-S page.

A common use can be installing the  package, then doing the following:

 $ scan /usr/share/dvb/dvb-t/de-Nordrhein-Westfalen | tee channels.conf
 $ vlc channels.conf
