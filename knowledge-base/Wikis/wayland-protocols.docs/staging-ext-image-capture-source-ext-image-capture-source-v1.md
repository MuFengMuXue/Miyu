# ext_image_capture_source_v1

## opaque image capture source objects

This protocol serves as an intermediary between capturing protocols and potential image capture sources such as outputs and toplevels. This protocol may be extended to support more image capture sources in the future, thereby adding those image capture sources to other protocols that use the image capture source object without having to modify those protocols. Warning! The protocol described in this file is currently in the testing phase. Backward compatible changes may be added together with the corresponding interface version bump. Backward incompatible changes can only be done by creating a new major version of the extension.

## Interface `ext_image_capture_source_v1` version 1

opaque image capture source object

The image capture source object is an opaque descriptor for a capturable resource. This resource may be any sort of entity from which an image may be derived. Note, because ext_image_capture_source_v1 objects are created from multiple independent factory interfaces, the ext_image_capture_source_v1 interface is frozen at version 1.

### Requests

- `destroy`: delete this object
  Destroys the image capture source. This request may be sent at any time by the client.

## Interface `ext_output_image_capture_source_manager_v1` version 1

image capture source manager for outputs

A manager for creating image capture source objects for wl_output objects.

### Requests

- `create_source`: create source object for output
  Creates a source object for an output. Images captured from this source will show the same content as the output. Some elements may be omitted, such as cursors and overlays that have been marked as transparent to capturing.
  Arguments: `source` (new_id); `output` (object)
- `destroy`: delete this object
  Destroys the manager. This request may be sent at any time by the client and objects created by the manager will remain valid after its destruction.

## Interface `ext_foreign_toplevel_image_capture_source_manager_v1` version 1

image capture source manager for foreign toplevels

A manager for creating image capture source objects for ext_foreign_toplevel_handle_v1 objects.

### Requests

- `create_source`: create source object for foreign toplevel
  Creates a source object for a foreign toplevel handle. Images captured from this source will show the same content as the toplevel.
  Arguments: `source` (new_id); `toplevel_handle` (object)
- `destroy`: delete this object
  Destroys the manager. This request may be sent at any time by the client and objects created by the manager will remain valid after its destruction.
