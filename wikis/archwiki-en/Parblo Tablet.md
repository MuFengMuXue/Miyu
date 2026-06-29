# Parblo Tablet

Parblo tablets does not have an official support for Linux by Parblo. Even with no community support as well, there is a workaround to make it works on Arch Linux.

## Configuration
## Identifying
The Arch Linux must be able to recognize the tablet inputs with no problems, but the preset buttons should be in an odd configuration and should not be able to be modified. Some of them should be even with no functionality.

With the tablet connected, the first step must be identify your tablet using the command . The output should be something like

 Bus 001 Device 009: ID 0483:a640 STMicroelectronics Parblo A640 V2(F1)

(In this example we have a Parblo A640 V2 tablet. Make sure to match the output with your tablet.) It is important to grab the Vendor ID, which is found in the output in , so in this example is .

After identifying the Vendor ID, you must find the most generic  that match with your tablet. To get this information, you should run in terminal the following command:

 # find /sys -name *modalias | xargs grep -i vendor_id

The output should display something like:

You must find the most generic term that correspond to all of  you found. In this example the most generic term is .

## Creating a hwdb rule
In order to create a hwdb rule to set your tablet, you must identify the input file associated to the buttons you want remap. You should install , run the command :

Now look for your tablet and then run the command , where you have to replace  to the corresponding events associated with your tablet, then press your tablet buttons trying to find what event is associated with each button.

When you found the buttons you wanna remap, take note of their values. In this case we had a  as an entry value.

After identifying the  and the key , you must create a  rule.

Create a file called  in  with the following content, replacing  with your corresponding  and  with your corresponding key :

You can insert more  below, if you need.

In this example we are changing the key code to an arbitrary number  and it may not work with you. But you can check the full key code list in .

## Remapping keys
After remapping your keys to something your OS can recognize, you can edit manually the  file to remap the keys to what you need. Else, you can download  and use a graphical interface to easily manage your keys.
