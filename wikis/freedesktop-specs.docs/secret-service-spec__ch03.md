## 3 Collection and Items

Each secret is stored together with [lookup attributes](lookup-attributes.html "Chapter 5. Lookup Attributes") and a label. These together form an [item](org.freedesktop.Secret.Item.html "org.freedesktop.Secret.Item").

A group of items together form a [collection](org.freedesktop.Secret.Collection.html "org.freedesktop.Secret.Collection"). A collection is similar in concept to the terms 'keyring' or 'wallet'.

Collections and items are represented as DBus objects, and each has its own object path. Under normal circumstances, the object path of a collection or item should not change for its lifetime.

It is strongly recommended that client applications use [lookup attributes](lookup-attributes.html "Chapter 5. Lookup Attributes") to find items rather than recording the object path of a stored item. This allows maximum interoperability.

An item or a collection may be initially in a locked state. When in a locked state the item or collection may not be modified in any way, and the secret may not be read. Client applications that require access to the secret of a locked item, or desire to modify a locked item, must [unlock it](unlocking.html "Chapter 8. Locking and Unlocking") before use.

The service must prevent modification of locked collections or items. On such an invalid access the [IsLocked](errors.md#org.freedesktop.Secret.Error.IsLocked) error should be raised.

Client applications without special requirements should store in the default collection. The default collection is always accessible through a [specific object path](object-paths.html "Chapter 12. Object Paths").

A new item can be created with the [`CreateItem()`](org.freedesktop.Secret.Collection.md#org.freedesktop.Secret.Collection.CreateItem "org.freedesktop.Secret.Collection.CreateItem") method on the Collection interface. When creating an item, the properties of the new item are specified. The service may ignore or change these properties when creating the item.

When creating an item, the service may need to prompt the user for additional information. In this case, a [prompt object](prompts.html "Chapter 9. Prompts and Prompting") is returned. It must be [acted upon](org.freedesktop.Secret.Prompt.md#org.freedesktop.Secret.Prompt.Prompt "org.freedesktop.Secret.Prompt.Prompt") in order for the collection to be created. In this case, the [result of the prompt](org.freedesktop.Secret.Prompt.md#org.freedesktop.Secret.Prompt.Completed "org.freedesktop.Secret.Prompt.Completed") will contain the object path of the new item.

An item can be deleted by calling the [`Delete()`](org.freedesktop.Secret.Item.md#org.freedesktop.Secret.Item.Delete "org.freedesktop.Secret.Item.Delete") method on the Item interface.

When deleting an item, the service may need to prompt the user for additional information. In this case, a [prompt object](prompts.html "Chapter 9. Prompts and Prompting") is returned. It must be [acted upon](org.freedesktop.Secret.Prompt.md#org.freedesktop.Secret.Prompt.Prompt "org.freedesktop.Secret.Prompt.Prompt") in order for the item to be deleted.

Client applications with special needs can create a new collection by calling the [`CreateCollection()`](org.freedesktop.Secret.Service.md#org.freedesktop.Secret.Service.CreateCollection "org.freedesktop.Secret.Service.CreateCollection") method on the Service interface. When creating a collection, the properties of the new collection are specified. The service may ignore or change these properties when creating the collection.

When creating a collection, the service may need to prompt the user for additional information. In this case, a [prompt object](prompts.html "Chapter 9. Prompts and Prompting") is returned. It must be [acted upon](org.freedesktop.Secret.Prompt.md#org.freedesktop.Secret.Prompt.Prompt "org.freedesktop.Secret.Prompt.Prompt") in order for the collection to be created. In this case, the [result of the prompt](org.freedesktop.Secret.Prompt.md#org.freedesktop.Secret.Prompt.Completed "org.freedesktop.Secret.Prompt.Completed") will contain the object path of the new collection.

A collection can be deleted by calling the [`Delete()`](org.freedesktop.Secret.Collection.md#org.freedesktop.Secret.Collection.Delete "org.freedesktop.Secret.Collection.Delete") method on the Collection interface.

When deleting a collection, the service may need to prompt the user for additional information. In this case, a [prompt object](prompts.html "Chapter 9. Prompts and Prompting") is returned. It must be [acted upon](org.freedesktop.Secret.Prompt.md#org.freedesktop.Secret.Prompt.Prompt "org.freedesktop.Secret.Prompt.Prompt") in order for the collection to be deleted.
