> 

# Core

The `WpCore <core_api>` API is mostly transparent to lua, as the core object is not exposed to the scripts.

For some functionality, though, the following static functions are exposed.

Core.getproperties()

Binds `wp_core_get_properties`

Returns a table with the properties of the core. These are the same properties that appear on WirePlumber's *client* object in the PipeWire global registry.

returns  
the properties of the core

rtype  
table

Core.getinfo()

Returns a table with information about the core. The table contains the following fields:

| Field | Contains |
|----|----|
| cookie | The value of `wp_core_get_remote_cookie` |
| name | The value of `wp_core_get_remote_name` |
| username | The value of `wp_core_get_remote_user_name` |
| hostname | The value of `wp_core_get_remote_host_name` |
| version | The value of `wp_core_get_remote_version` |
| properties | The value of `wp_core_get_remote_properties` |

returns  
information about the core

rtype  
table

Core.idleadd(callback)

Binds `wp_core_idle_add_closure`

Schedules to call *callback* the next time that the event loop will be idle

param function callback  
the function to call; the function takes no arguments and must return true/false, as it is a GSourceFunc: return true to have the event loop call it again the next time it is idle, false to stop calling it and remove the associated GSource

returns  
the GSource associated with this idle callback

rtype  
GSource, see `GSource.destroy`

Core.timeoutadd(timeoutms, callback)

Binds `wp_core_timeout_add_closure`

Schedules to call *callback* after *timeout_ms* milliseconds

param function callback  
the function to call; the function takes no arguments and must return true/false, as it is a GSourceFunc: return true to have the event loop call it again periodically every *timeout_ms* milliseconds, false to stop calling it and remove the associated GSource

returns  
the GSource associated with this idle callback

rtype  
GSource, see `GSource.destroy`

GSource.destroy(self)

For the purpose of working with `Core.idle_add` and `Core.timeout_add`, the GSource object that is returned by those functions contains this method.

Call this method to destroy the source, so that the associated callback is not called again. This can be used to stop a repeating timer callback or just to abort some idle operation

This method binds *g_source_destroy*

Core.sync(callback)

Binds `wp_core_sync`

Calls *callback* after synchronizing the transaction state with PipeWire

param function callback  
a function to be called after syncing with PipeWire; the function takes one argument that will be an error string, if something went wrong and nil otherwise and returns nothing

Core.quit()

Quits the current *wpexec* process

> [!NOTE]
> This can only be called when the script is running in *wpexec*; if it is running in the main WirePlumber daemon, it will print a warning and do nothing

Core.requireapi(..., callback)

Ensures that the specified API plugins are loaded.

API plugins are plugins that provide some API extensions for use in scripts. These plugins must always have their name end in "-api" and the names specified here must not have the "-api" extension.

For instance, the "mixer-api" module provides an API to change volume/mute controls from scripts, via action signals. It can be used like this:

``` lua
Core.require_api("mixer", function(mixer)
  -- get the volume of node 35
  local volume = mixer:call("get-volume", 35)

  -- the return value of "get-volume" is a GVariant(a{sv}),
  -- which gets translated to a Lua table
  Debug.dump_table(volume)
end)
```

See also the example in `GObject.call`

> [!NOTE]
> This can only be called when the script is running in *wpexec*; if it is running in the main WirePlumber daemon, it will print a warning and do nothing

param strings ...  
a list of string arguments, which specify the names of the api plugins to load, if they are not already loaded

param callback  
the function to call after the plugins have been loaded; this function takes references to the plugins as parameters

Core.testfeature()

Binds `wp_core_test_feature`

Tests if the specified feature is provided in the current WirePlumber configuration.

param string feature  
the name of the feature to test

returns  
true if the feature is provided, false otherwise

rtype  
boolean
