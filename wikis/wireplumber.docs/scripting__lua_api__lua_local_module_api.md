> 

# Local Modules

The LocalModule object (which binds the `WpImplModule` C API) provides a way to load PipeWire modules in the WirePlumber process. Instantiating the object loads the module, and when the last reference to the returned module object is dropped, the module is unloaded.

## Constructors

LocalModule(name, arguments, properties)

Loads the named module with the provided arguments and properties (either of which can be `nil`).

param string name  
the module name, such as `"libpipewire-module-loopback"`

param string arguments  
should be either `nil` or a string with the desired module arguments

param table properties  
can be `nil` or a table that can be `converted <lua_gobject_lua_to_c>` to `WpProperties`

returns  
a new LocalModule

rtype  
LocalModule (`WpImplModule`)

since  
0.4.2
