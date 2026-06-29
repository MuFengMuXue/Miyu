# xdg_foreign_unstable_v2

## Protocol for exporting xdg surface handles

This protocol specifies a way for making it possible to reference a surface of a different client. With such a reference, a client can, by using the interfaces provided by this protocol, manipulate the relationship between its own surfaces and the surface of some other client. For example, stack some of its own surface above the other clients surface. In order for a client A to get a reference of a surface of client B, client B must first export its surface using xdg_exporter.export_toplevel. Upon doing this, client B will receive a handle (a unique string) that it may share with client A in some way (for example D-Bus). After client A has received the handle from client B, it may use xdg_importer.import_toplevel to create a reference to the surface client B just exported. See the corresponding requests for details. A possible use case for this is out-of-process dialogs. For example when a sandboxed client without file system access needs the user to select a file on the file system, given sandbox environment support, it can export its surface, passing the exported surface handle to an unsandboxed process that can show a file browser dialog and stack it above the sandboxed client's surface. Warning! The protocol described in this file is experimental and backward incompatible changes may be made. Backward compatible changes may be added together with the corresponding interface version bump. Backward incompatible changes are done by bumping the version number in the protocol and interface names and resetting the interface version. Once the protocol is to be declared stable, the 'z' prefix and the version number in the protocol and interface names are removed and the interface version number is reset.

## Interface `zxdg_exporter_v2` version 1

interface for exporting surfaces

A global interface used for exporting surfaces that can later be imported using xdg_importer.

### Requests

- `destroy`: destroy the xdg_exporter object
  Notify the compositor that the xdg_exporter object will no longer be used.
- `export_toplevel`: export a toplevel surface
  The export_toplevel request exports the passed surface so that it can later be imported via xdg_importer. When called, a new xdg_exported object will be created and xdg_exported.handle will be sent immediately. See the corresponding interface and event for details. A surface may be exported multiple times, and each exported handle may be used to create an xdg_imported multiple times. Only xdg_toplevel equivalent surfaces may be exported, otherwise an invalid_surface protocol error is sent.
  Arguments: `id` (new_id) - the new xdg_exported object; `surface` (object) - the surface to export

### Enums

- `error`: error values
  These errors can be emitted in response to invalid xdg_exporter requests.

## Interface `zxdg_importer_v2` version 1

interface for importing surfaces

A global interface used for importing surfaces exported by xdg_exporter. With this interface, a client can create a reference to a surface of another client.

### Requests

- `destroy`: destroy the xdg_importer object
  Notify the compositor that the xdg_importer object will no longer be used.
- `import_toplevel`: import a toplevel surface
  The import_toplevel request imports a surface from any client given a handle retrieved by exporting said surface using xdg_exporter.export_toplevel. When called, a new xdg_imported object will be created. This new object represents the imported surface, and the importing client can manipulate its relationship using it. See xdg_imported for details.
  Arguments: `id` (new_id) - the new xdg_imported object; `handle` (string) - the exported surface handle

## Interface `zxdg_exported_v2` version 1

an exported surface handle

An xdg_exported object represents an exported reference to a surface. The exported surface may be referenced as long as the xdg_exported object not destroyed. Destroying the xdg_exported invalidates any relationship the importer may have established using xdg_imported.

### Requests

- `destroy`: unexport the exported surface
  Revoke the previously exported surface. This invalidates any relationship the importer may have set up using the xdg_imported created given the handle sent via xdg_exported.handle.

### Events

- `handle`: the exported surface handle
  The handle event contains the unique handle of this exported surface reference. It may be shared with any client, which then can use it to import the surface by calling xdg_importer.import_toplevel. A handle may be used to import the surface multiple times.
  Arguments: `handle` (string) - the exported surface handle

## Interface `zxdg_imported_v2` version 1

an imported surface handle

An xdg_imported object represents an imported reference to surface exported by some client. A client can use this interface to manipulate relationships between its own surfaces and the imported surface.

### Requests

- `destroy`: destroy the xdg_imported object
  Notify the compositor that it will no longer use the xdg_imported object. Any relationship that may have been set up will at this point be invalidated.
- `set_parent_of`: set as the parent of some surface
  Set the imported surface as the parent of some surface of the client. The passed surface must be an xdg_toplevel equivalent, otherwise an invalid_surface protocol error is sent. Calling this function sets up a surface to surface relation with the same stacking and positioning semantics as xdg_toplevel.set_parent.
  Arguments: `surface` (object) - the child surface

### Events

- `destroyed`: the imported surface handle has been destroyed
  The imported surface handle has been destroyed and any relationship set up has been invalidated. This may happen for various reasons, for example if the exported surface or the exported surface handle has been destroyed, if the handle used for importing was invalid.

### Enums

- `error`: error values
  These errors can be emitted in response to invalid xdg_imported requests.
