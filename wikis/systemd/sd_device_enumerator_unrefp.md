## Name

sd_device_enumerator_new, sd_device_enumerator_ref, sd_device_enumerator_unref, sd_device_enumerator_unrefp — Create, reference, and release a device enumerator object

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-device.h>
```

|  |  |
|----|----|
| `int `**`sd_device_enumerator_new`**`(` | sd_device_enumerator \*\*`ret``)`; |

 

|  |  |
|----|----|
| `sd_device_enumerator* `**`sd_device_enumerator_ref`**`(` | sd_device_enumerator \*`enumerator``)`; |

 

|  |  |
|----|----|
| `sd_device_enumerator* `**`sd_device_enumerator_unref`**`(` | sd_device_enumerator \*`enumerator``)`; |

 

|  |  |
|----|----|
| `void `**`sd_device_enumerator_unrefp`**`(` | sd_device_enumerator \*\*`enumerator``)`; |

 

## Description

The `sd_device_enumerator` family of functions provides a way to iterate over devices recognized by systemd-udevd(8). The enumerator allows filtering and matching devices by subsystem, properties and other attributes.

`sd_device_enumerator_new()` creates a new device enumerator object and stores the result in the pointer referenced by *`ret`*. Returns 0 on success, or a negative errno-style error code on failure.

`sd_device_enumerator_ref()` increases the reference count of the specified *`enumerator`* by one.

`sd_device_enumerator_unref()` decreases the reference count of the *`enumerator`* by one. When the reference count reaches zero, the enumerator object is destroyed and cannot be used anymore, so further calls to `sd_device_enumerator_unref() ` or `sd_device_enumerator_unrefp()` are illegal.

`sd_device_enumerator_unrefp()` is similar to `sd_device_enumerator_unref()` but takes a pointer to a pointer to an sd_device_enumerator object. This call is useful in conjunction with GCC's and LLVM's Clean-up Variable Attribute. Note that this function is defined as an inline function. Use a declaration like the following, in order to allocate a sd_device_enumerator object that is freed automatically as the code block is left:

``` programlisting
{
  __attribute__((cleanup(sd_device_enumerator_unrefp))) sd_device_enumerator *enumerator = NULL;
  int r;
  …
  r = sd_device_enumerator_new(&enumerator);
  if (r < 0)
    fprintf(stderr, "Failed to allocate sd_device_enumerator: %s\n", strerror(-r));
  …
}
```

`sd_device_enumerator_ref()` and `sd_device_enumerator_unref()` execute no operation if the *`enumerator`* is `NULL`. `sd_device_enumerator_unrefp()` will first dereference its argument, which must not be `NULL`, and will execute no operation if *that* is `NULL`.

## Return Value

`sd_device_enumerator_new()` returns 0 on success or a negative errno-style error code on failure.

`sd_device_enumerator_ref()` always returns the enumerator pointer.

`sd_device_enumerator_unref()` always returns `NULL`.

### Errors

Returned errors may indicate the following problems:

`-ENOMEM`  
Memory allocation failed.

`-EINVAL`  
The argument is invalid.

## Example

**Example 1. Using sd_device_enumerator_new()**

``` programlisting
/* SPDX-License-Identifier: MIT-0 */

#include <stdio.h>
#include <systemd/sd-device.h>

int main(void) {
    sd_device_enumerator *enumerator;
    int r;

    r = sd_device_enumerator_new(&enumerator);
    if (r < 0) {
        fprintf(stderr, "Failed to create enumerator: %s\n", strerror(-r));
        return 1;
    }

    sd_device_enumerator_ref(enumerator);
    sd_device_enumerator_unref(enumerator);

    sd_device_enumerator_unref(enumerator);

    return 0;
}
```

  

## History

`sd_device_enumerator_new()`, `sd_device_enumerator_ref()`, `sd_device_enumerator_unref()`, and `sd_device_enumerator_unrefp()` were added in version 240.

## See Also

sd_device_ref(3), sd_device_enumerator_add_match_parent(3)
