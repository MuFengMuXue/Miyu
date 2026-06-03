## Name

sd_bus_get_n_queued_read, sd_bus_get_n_queued_write — Get the number of pending bus messages in the read and write queues of a bus connection object

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                         |                      |
|-----------------------------------------|----------------------|
| `int `**`sd_bus_get_n_queued_read`**`(` | sd_bus \*`bus`,      |
|                                         | uint64_t \*`ret``)`; |

 

|                                          |                      |
|------------------------------------------|----------------------|
| `int `**`sd_bus_get_n_queued_write`**`(` | sd_bus \*`bus`,      |
|                                          | uint64_t \*`ret``)`; |

 

## Description

`sd_bus_get_n_queued_read()` may be used to query the number of bus messages in the read queue of a bus connection object. The read queue contains all messages read from the transport medium (e.g. network socket) but not yet processed locally. The function expects two arguments: the bus object to query, and a pointer to a 64-bit counter variable to write the current queue size to. Use `sd_bus_process()` in order to process queued messages, i.e. to reduce the size of the read queue (as well as, in fact, the write queue, see below).

Similarly, `sd_bus_get_n_queued_write()` may be used to query the number of currently pending bus messages in the write queue of a bus connection object. The write queue contains all messages enqueued into the connection with a call such as `sd_bus_send()` but not yet written to the transport medium. The expected arguments are similar to `sd_bus_get_n_queued_read()`. Here too, use `sd_bus_process()` to reduce the size of the write queue. Alternatively, use `sd_bus_flush()` to synchronously write out any pending bus messages until the write queue is empty.

## Return Value

On success, these functions return 0 or a positive integer. On failure, they return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-ECHILD`  
The bus connection was created in a different process, library or module instance.

## History

`sd_bus_get_n_queued_read()` and `sd_bus_get_n_queued_write()` were added in version 238.

## See Also

systemd(1), sd-bus(3), sd_bus_process(3), sd_bus_send(3), sd_bus_flush(3)
