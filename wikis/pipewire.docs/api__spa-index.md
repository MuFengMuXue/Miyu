# SPA (Simple Plugin API)

api_spa (Simple Plugin API) is an extensible API to implement all kinds of
plugins.

It is inspired by many other plugin APIs, mostly LV2 and
GStreamer. SPA provides two parts:

- A header-only API with no external dependencies.
- A set of support libraries ("plugins") for commonly used functionality.

The usual approach is that PipeWire and PipeWire clients can use the
header-only functions to interact with the plugins. Those plugins are
usually loaded at runtime (through `dlopen(3)`).

# Motivation

SPA was designed with the following goals in mind:

- No dependencies, SPA is shipped as a set of header files that have no dependencies except for the standard C library.
- Very efficient both in space and in time.
- Very configurable and usable in many different environments. All aspects
  of the plugin environment can be configured and changed, like logging,
  poll loops, system calls, etc.
- Consistent API.
- Extensible; new API can be added with minimal effort, existing API can be updated and versioned.

The original user of SPA is PipeWire, which uses SPA to implement the
low-level multimedia processing plugins, device detection, mainloops, CPU
detection, logging, among other things. SPA however can be used outside
of PipeWire with minimal problems.

# The SPA Header-Only API

A very simple example on how SPA headers work are the spa_utils, a set
of utilities commonly required by C projects. SPA functions use the `spa_`
namespace and are easy to identify.

```
/* cc $(pkg-config --cflags libspa-0.2) -o spa-test spa-test.c */

#include <stdint.h>
#include <spa/utils/string.h>

int main(int argc, char **argv) {
	uint32_t val;

	if (spa_atoi32(argv[1], &val, 16))
		printf("argv[1] is hex %#x", val);
	else
		printf("argv[1] is not a hex number");

	return 0;
}
```

# SPA Plugins

SPA plugins are shared libraries (`.so` files) that can be loaded at
runtime. Each library provides one or more "factories", each of which may
implement several "interfaces". Code that uses SPA plugins then uses those
interfaces (through SPA header files) to interact with the plugin.

For example, the PipeWire daemon can load the normal `printf`-based logger
or a systemd journal-based logger. Both of those provide the spa_log
interface and once instantiated, PipeWire no longer has to differentiate
between the two logging facilities.

Please see SPA Plugins for the details on how to use SPA plugins.

# Further details

- api_spa
- SPA Design
- SPA Plugins
- SPA POD
- SPA Buffers

 api_spa

See: SPA (Simple Plugin API), SPA Design
