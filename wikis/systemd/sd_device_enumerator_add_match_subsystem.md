## Name

sd_device_enumerator_add_match_parent, sd_device_enumerator_add_match_property, sd_device_enumerator_add_match_property_required, sd_device_enumerator_add_match_subsystem, sd_device_enumerator_add_match_sysattr, sd_device_enumerator_add_match_sysname, sd_device_enumerator_add_nomatch_sysname, sd_device_enumerator_add_match_tag, sd_device_enumerator_allow_uninitialized, sd_device_enumerator_add_all_parents — Add a filter to the device enumerator

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-device.h>
```

|  |  |
|----|----|
| `int `**`sd_device_enumerator_add_match_parent`**`(` | sd_device_enumerator \*`enumerator`, |
|   | sd_device \*`parent``)`; |

 

|  |  |
|----|----|
| `int `**`sd_device_enumerator_add_match_property`**`(` | sd_device_enumerator \*`enumerator`, |
|   | const char \*`property`, |
|   | const char \*`value``)`; |

 

|  |  |
|----|----|
| `int `**`sd_device_enumerator_add_match_property_required`**`(` | sd_device_enumerator \*`enumerator`, |
|   | const char \*`property`, |
|   | const char \*`value``)`; |

 

|  |  |
|----|----|
| `int `**`sd_device_enumerator_add_match_subsystem`**`(` | sd_device_enumerator \*`enumerator`, |
|   | const char \*`subsystem`, |
|   | int `match``)`; |

 

|  |  |
|----|----|
| `int `**`sd_device_enumerator_add_match_sysattr`**`(` | sd_device_enumerator \*`enumerator`, |
|   | const char \*`sysattr`, |
|   | const char \*`value`, |
|   | int `match``)`; |

 

|  |  |
|----|----|
| `int `**`sd_device_enumerator_add_match_sysname`**`(` | sd_device_enumerator \*`enumerator`, |
|   | const char \*`sysname``)`; |

 

|  |  |
|----|----|
| `int `**`sd_device_enumerator_add_nomatch_sysname`**`(` | sd_device_enumerator \*`enumerator`, |
|   | const char \*`sysname``)`; |

 

|  |  |
|----|----|
| `int `**`sd_device_enumerator_add_match_tag`**`(` | sd_device_enumerator \*`enumerator`, |
|   | const char \*`tag``)`; |

 

|  |  |
|----|----|
| `int `**`sd_device_enumerator_allow_uninitialized`**`(` | sd_device_enumerator \*`enumerator``)`; |

 

|  |  |
|----|----|
| `int `**`sd_device_enumerator_add_all_parents`**`(` | sd_device_enumerator \*`enumerator``)`; |

 

## Description

The `sd_device_enumerator_add_match_parent()` function adds a filter to the *`enumerator`* so that only devices under the tree of the specified *`parent`* device are enumerated. If this is called multiple times the previously set *`parent`* device is cleared and only the last call takes an effect.

The `sd_device_enumerator_add_match_property()` function adds a filter to the *`enumerator`* so that only devices with the specified *`property`* equals to the *`value`* are enumerated. Both *`property`* and *`value`* can be a glob pattern. When this is called multiple times, devices that have at least one of the specified properties with matching values are enumerated. That is, filters are ORed.

The `sd_device_enumerator_add_match_property_required()` function adds a filter to the *`enumerator`* so that only devices with the specified *`property`* equals to the *`value`* are enumerated. This function is similar to `sd_device_enumerator_add_match_property()`, but when this is called multiple times, devices that have *all* specified properties with matching values are enumerated. That is, filters are ANDed.

The `sd_device_enumerator_add_match_subsystem()` function adds a filter to the *`enumerator`* so that all devices in the specified *`subsystem`*, when *`match`* is `true`. When *`match`* is `false`, then all devices except those in the specified *`subsystem`* are enumerated. When called multiple times, positive filters are ORed, and negative ones are ANDed.

The `sd_device_enumerator_add_match_sysattr()` function adds a filter on the sysfs attribute *`sysattr`* matching *`value`*. *`value`* can be a glob pattern. If *`value`* is `NULL`, devices that either have (if *`match`* is `true`) or do not have (if *`match`* is `false`) the specified *`sysattr`* are included, regardless of its value. That is, `NULL` is mostly equivalent to "`*`". When this function is called multiple times, only devices that match all specified *`sysattr`* filters are enumerated. That is, these filters are ANDed.

The `sd_device_enumerator_add_match_sysname()` function adds a filter so that only devices whose sysname equals to *`sysname`* are enumerated. *`sysname`* can be a glob pattern. When called multiple times, filters are ORed.

The `sd_device_enumerator_add_nomatch_sysname()` function adds a filter so that devices whose sysname equals to *`sysname`* are excluded from the enumeration. This is useful for excluding specific devices from the enumeration process. When called multiple times, features are ANDed.

The `sd_device_enumerator_add_match_tag()` function adds a filter so that only devices tagged with *`tag`* are enumerated. When called multiple times, filters are ORed.

The `sd_device_enumerator_allow_uninitialized()` function allows devices that have not yet been initialized by udev to be included in the enumeration.

The `sd_device_enumerator_add_all_parents()` function enumerates all parent devices of the matching devices. This is useful for cases where you want to include all parent devices in the enumeration, such as when you are interested in the entire device tree leading up to a specific device.

## Return Value

All functions return `0` or a positive integer on success, or a negative errno-style error code on failure.

### Errors

Returned errors may indicate the following problems:

`-ENOMEM`  
Memory allocation failed.

`-EINVAL`  
One of the arguments is invalid.

## Examples

**Example 1. Detect Removable USB Devices (Using Match and Exclude)**

``` programlisting
/* SPDX-License-Identifier: MIT-0 */

#include <stdbool.h>
#include <stdio.h>
#include <systemd/sd-device.h>

int main(void) {
    __attribute__((cleanup(sd_device_enumerator_unrefp))) sd_device_enumerator *enumerator = NULL;
    sd_device *device;
    int r;

    /* Create a new device enumerator */
    r = sd_device_enumerator_new(&enumerator);
    if (r < 0) {
        fprintf(stderr, "Failed to create device enumerator: %s\n", strerror(-r));
        return 1;
    }

    /* Include only devices from the "usb" subsystem */
    r = sd_device_enumerator_add_match_subsystem(enumerator, "usb", true);
    if (r < 0) {
        fprintf(stderr, "Failed to add subsystem match: %s\n", strerror(-r));
        return 1;
    }

    /*
     * Exclude devices where the "removable" sysattr is "0"
     * These are typically non-removable devices like built-in USB interfaces
     */
    r = sd_device_enumerator_add_match_sysattr(enumerator, "removable", "0", false);
    if (r < 0) {
        fprintf(stderr, "Failed to add sysattr match: %s\n", strerror(-r));
        return 1;
    }

    /* Begin enumerating matching devices */
    for (device = sd_device_enumerator_get_device_first(enumerator);
         device;
         device = sd_device_enumerator_get_device_next(enumerator)) {
        const char *syspath;

        /* Get syspath for the device */
        if (sd_device_get_syspath(device, &syspath) >= 0)
            printf("Removable USB device found: %s\n", syspath);
    }
    return 0;
}
```

  

## History

`sd_device_enumerator_add_match_parent()`, `sd_device_enumerator_add_match_property()`, `sd_device_enumerator_add_match_subsystem()`, `sd_device_enumerator_add_match_sysattr()`, `sd_device_enumerator_add_match_sysname()`, `sd_device_enumerator_add_match_tag()`, and `sd_device_enumerator_allow_uninitialized()` were added in version 240.

`sd_device_enumerator_add_nomatch_sysname()` was added in version 251.

`sd_device_enumerator_add_match_property_required()` was added in version 255.

`sd_device_enumerator_add_all_parents()` was added in version 258.

## See Also

sd_device_ref(3), sd_device_enumerator_new(3), sd_device_enumerator_get_device_first(3)
