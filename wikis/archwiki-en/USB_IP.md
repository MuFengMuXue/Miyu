# USB/IP

From the USB/IP site:
:USB/IP Project aims to develop a general USB device sharing system over IP network. To share USB devices between computers with their full functionality, USB/IP encapsulates "USB I/O messages" into TCP/IP payloads and transmits them between computers.

## Installation
Install the  package.

## Usage
## Server setup
The server should have the physical USB device connected to it, and the  USB/IP kernel module loaded. Then start and enable the USB/IP systemd service . The daemon will accept connections on TCP port 3240.

List the connected devices:

 $ usbip list -l

Bind the required device. For example, to share the device having busid 1-1.5:

 # usbip bind -b 1-1.5

To unbind the device:

 # usbip unbind -b 1-1.5

After binding, the device can be accessed from the client.

## Binding with systemd service
In order to make binding persistent following systemd template unit file can be used:

So, e.g., to share the device having busid 1-1, one should start/enable .

## Client setup
Make sure the  kernel module is loaded.

Then list devices available on the server:

 $ usbip list -r server_IP_address

Attach the required device. For example, to attach the device having busid 1-1.5:

 # usbip attach -r server_IP_address -b 1-1.5

## Disconnecting devices
A device can be disconnected only after detaching it on the client.

List attached devices:

 $ usbip port

Detach the device:

 # usbip detach -p port_number

Unbind the device on the server:

 # usbip unbind -b busid

## Tips and tricks
## Binding by vendor/device ID
If bus ids are inconsistent and dynamically assigned at each system boot, binding by vendor/device ID can be used alternatively:

So, e.g., to share the device having vendor/device ID 0924:3d68, one should start/enable .

Then client setup will be like this:
* Linux clients

 $ usbip attach -r server_IP_address --$(/usr/sbin/usbip list -p -r server_IP_address | grep '#usbid=0924:3d68#' | cut '-d#' -f1)

{{Note|If the previous command fails, check if -p flag in  is working properly. If not, use the following line instead:

{{bc|
$ usbip attach -r server_IP_address -b $(/usr/sbin/usbip list -p -r server_IP_address  grep '0924:3d68'  cut '-d:' -f1  awk '{print $1}')
}}
}}
* Windows clients

 c:\> for /f "tokens=1 delims=:, " %a in ('usbip list -r server_IP_address ^| findstr /r /c:"0924:3d68"') do start usbip attach -r server_IP_address -b %a

## Sharing devices configured with files in /etc/..
 provides systemd service files for binding by vendor/device id and for connecting by hostname and vendor/device id.

## Server setup
For each device create a device.conf in  with USBIP_DEVICE set to the vendor/product id, e.g.:

To bind a cofigured device start/enable the service

## Client setup
For each host/device create a device.conf in  with HOST set and USBIP_DEVICE set to the vendor/product id, e.g.:

Make sure your server is running and the configured device is bound, then start or stop the service
