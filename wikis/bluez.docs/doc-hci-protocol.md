# hci

## Bluetooth HCI protocol

Version
BlueZ

Copyright
Free use of this software is granted under the terms of the GNU Lesser General Public Licenses (LGPL).

Date
October 2024

Manual section
7

Manual group
Linux System Administration

### SYNOPSIS

```
#include <sys/socket.h>
#include <bluetooth/bluetooth.h>
#include <bluetooth/hci.h>

hci_socket = socket(PF_BLUETOOTH, SOCK_RAW, BTPROTO_HCI);
```

### DESCRIPTION

Bluetooth Host Controller Interface (HCI) is the standard protocol to communicate with Bluetooth adapters. HCI protocol provides a uniform command method for the Host to access Controller capabilities and to control connections to other Controllers.

### SOCKET ADDRESS

```
struct sockaddr_hci {
    sa_family_t    hci_family;
    unsigned short hci_dev;
    unsigned short hci_channel;
};
```

Possible values for hcichannel:

| Define | Value | Description |
|----|----|----|
| **HCI_CHANNEL_RAW** | 0x00 | Raw channel - Used for raw HCI communication |
| **HCI_CHANNEL_USER** | 0x01 | User channel - Used for userspace HCI communication (disables kernel processing) |
| **HCI_CHANNEL_MONITOR** | 0x02 | Monitor channel - Used for monitoring HCI traffic (btmon(1)) |
| **HCI_CHANNEL_CONTROL** | 0x03 | Control channel - Used to manage local adapters (bluetoothd(7)) |
| **HCI_CHANNEL_LOGGING** | 0x04 | Logging channel - Used to inject logging messages (bluetoothd(7)) |

Example:

```
struct sockaddr_hci addr;

memset(&addr, 0, sizeof(addr));
addr.hci_family = AF_BLUETOOTH;
addr.hci_dev = HCI_DEV_NONE;
addr.hci_channel = HCI_CHANNEL_CONTROL;
```

### SOCKET OPTIONS

The socket options listed below can be set by using **setsockopt(2)** and read with **getsockopt(2)** with the socket level set to SOLBLUETOOTH or SOLHCI (HCIFILTER).

#### HCIFILTER (since Linux 2.6)

Filter by HCI events, requires hcichannel to be set to HCICHANNEL_RAW, possible values:

```
struct hci_filter {
    uint32_t type_mask;
    uint32_t event_mask[2];
    uint16_t opcode;
};
```

Example:

```
struct hci_filter flt;

memset(&flt, 0, sizeof(flt));
flt.type_mask = 1 << BT_H4_EVT_PKT;
flt.event_mask[0] = 0xffffffff;
flt.event_mask[1] = 0xffffffff;

setsockopt(fd, SOL_HCI, HCI_FILTER, &flt, sizeof(flt));
```

#### BTSNDBUF (since Linux 5.16)

Set send buffer size, requires hcichannel to be set to HCICHANNEL_MONITOR, HCICHANNEL_CONTROL or HCICHANNEL_LOGGING.

Default value is 1028.

Example:

```
uint16_t mtu = UINT16_MAX;
int err;

err = setsockopt(fd, SOL_BLUETOOTH, BT_SNDMTU, &mtu, sizeof(mtu));
```

#### BTRCVBUF (since Linux 5.16)

Set receive buffer size, requires hcichannel to be set to HCICHANNEL_MONITOR, HCICHANNEL_CONTROL or HCICHANNEL_LOGGING.

Default value is 1028.

Example:

```
uint16_t mtu;
socklen_t len;
int err;

len = sizeof(mtu);
err = getsockopt(sock, SOL_BLUETOOTH, BT_RCVMTU, mtu, &len);
```

### RESOURCES

<http://www.bluez.org>

### REPORTING BUGS

<linux-bluetooth@vger.kernel.org>

### SEE ALSO

socket(7)
