# Development

Extend snap functionality with API access and customised environments for your applications and devices.

* [Environment variables](https://snapcraft.io/docs/reference/development/environment-variables/): Internal values accessible to snapped applications.
* [REST API error codes](https://snapcraft.io/docs/reference/development/error-responses/): The types of errors returned by the API.

## YAML schemas

YAML schemas define exactly what a device, kernel and snap is capable of.
 - [snap.yaml](https://snapcraft.io/docs/reference/development/yaml-schemas/the-snap-format/): The metadata for a snap.
 - [Gadget snap](https://snapcraft.io/docs/reference/development/yaml-schemas/the-gadget-snap/): System and device properties.
 - [Kernel snap](https://snapcraft.io/docs/reference/development/yaml-schemas/the-kernel-snap/): The Linux kernel snap, its metadata and setup files.

## Client libraries

* [snap-http](https://github.com/canonical/snap-http): A Python library for interacting with the snapd REST API (`pip install snap-http`).
