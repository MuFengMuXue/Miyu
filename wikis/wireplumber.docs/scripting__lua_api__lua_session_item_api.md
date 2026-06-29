> 

# Session Item

Lua objects that bind a `WpSessionItem <session_item_api>` contain the following methods:

SessionItem.getassociated_proxy(self, type)

Binds `wp_session_item_get_associated_proxy`

param self  
the session item

param string type  
the proxy type name

returns  
the proxy object or nil

SessionItem.reset(self)

Binds `wp_session_item_reset`

param self  
the session item

SessionItem.configure(self, properties)

Binds `wp_session_item_configure`

param self  
the session item

param table properties  
The configuration properties

returns  
true on success, false on failure

rtype  
boolean

SessionItem.register(self)

Binds `wp_session_item_register`

param self  
the session item

SessionItem.remove(self)

Binds `wp_session_item_remove`

param self  
the session item
