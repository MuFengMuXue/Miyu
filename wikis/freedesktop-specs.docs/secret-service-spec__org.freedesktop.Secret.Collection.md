## `org.freedesktop.Secret.Collection`

org.freedesktop.Secret.Collection — A collection of items containing secrets.

## Synopsis

### Methods

|                     |                             |
|---------------------|-----------------------------|
| ` `**`Delete`**` (` | OUT ObjectPath `prompt``)`; |

 

|                          |                                        |
|--------------------------|----------------------------------------|
| ` `**`SearchItems`**` (` | IN Dict\<String,String\> `attributes`, |
|                          | OUT Array\<ObjectPath\> `results``)`;  |

 

|                         |                                         |
|-------------------------|-----------------------------------------|
| ` `**`CreateItem`**` (` | IN Dict\<String,Variant\> `properties`, |
|                         | IN Secret `secret`,                     |
|                         | IN Boolean `replace`,                   |
|                         | OUT ObjectPath `item`,                  |
|                         | OUT ObjectPath `prompt``)`;             |

 

### Signals

|                          |                           |
|--------------------------|---------------------------|
| ` `**`ItemCreated`**` (` | OUT ObjectPath `item``)`; |

 

|                          |                           |
|--------------------------|---------------------------|
| ` `**`ItemDeleted`**` (` | OUT ObjectPath `item``)`; |

 

|                          |                           |
|--------------------------|---------------------------|
| ` `**`ItemChanged`**` (` | OUT ObjectPath `item``)`; |

 

### Properties

## 

`READ Array<ObjectPath> Items ;`  
`READWRITE String Label ;`  
`READ Boolean Locked ;`  
`READ UInt64 Created ;`  
`READ UInt64 Modified ;`

## Methods

### `org.freedesktop.Secret.Collection.Delete`

|                     |                             |
|---------------------|-----------------------------|
| ` `**`Delete`**` (` | OUT ObjectPath `prompt``)`; |

 

Delete this collection.

`prompt`  
A prompt to delete the collection, or the special value '/' when no prompt is necessary.

### `org.freedesktop.Secret.Collection.SearchItems`

|                          |                                        |
|--------------------------|----------------------------------------|
| ` `**`SearchItems`**` (` | IN Dict\<String,String\> `attributes`, |
|                          | OUT Array\<ObjectPath\> `results``)`;  |

 

Search for items in this collection matching the lookup attributes.

`attributes`  
Attributes to match.

`results`  
Items that matched the attributes.

### `org.freedesktop.Secret.Collection.CreateItem`

|                         |                                         |
|-------------------------|-----------------------------------------|
| ` `**`CreateItem`**` (` | IN Dict\<String,Variant\> `properties`, |
|                         | IN Secret `secret`,                     |
|                         | IN Boolean `replace`,                   |
|                         | OUT ObjectPath `item`,                  |
|                         | OUT ObjectPath `prompt``)`;             |

 

Create an item with the given attributes, secret and label. If replace is set, then it replaces an item already present with the same values for the attributes.

`properties`  
The properties for the new item.

Properties for the new item. This allows setting the new item's properties upon its creation. All READWRITE properties are useable. Specify the property names in full interface.Property form.

###### Example 13.2: Example for properties

``` programlisting

properties = {
               "org.freedesktop.Secret.Item.Label": "MyItem",
               "org.freedesktop.Secret.Item.Attributes": {
                          "Attribute1": "Value1",
                          "Attribute2": "Value2"
                    }
             }

                                
```

###### Note

Please note that there is a distinction between the terms *Property*, which refers to a D-Bus properties of an object, and *Attribute*, which refers to one of a secret item's string-valued attributes.

`secret`  
The secret to store in the item, encoded with the included session.

`replace`  
Whether to replace an item with the same attributes or not.

`item`  
The item created, or the special value '/' if a prompt is necessary.

`prompt`  
A prompt object, or the special value '/' if no prompt is necessary.

## Signals

### `org.freedesktop.Secret.Collection.ItemCreated`

|                          |                           |
|--------------------------|---------------------------|
| ` `**`ItemCreated`**` (` | OUT ObjectPath `item``)`; |

 

A new item in this collection was created.

`item`  
The item that was created.

### `org.freedesktop.Secret.Collection.ItemDeleted`

|                          |                           |
|--------------------------|---------------------------|
| ` `**`ItemDeleted`**` (` | OUT ObjectPath `item``)`; |

 

An item in this collection was deleted.

`item`  
The item that was deleted.

### `org.freedesktop.Secret.Collection.ItemChanged`

|                          |                           |
|--------------------------|---------------------------|
| ` `**`ItemChanged`**` (` | OUT ObjectPath `item``)`; |

 

An item in this collection changed.

`item`  
The item that was changed.

## D-Bus Properties

Accessed using the org.freedesktop.DBus.Properties interface.

`READ Array<ObjectPath> Items ;`  

Items in this collection.

`READWRITE String Label ;`  

The displayable label of this collection.

`READ Boolean Locked ;`  

Whether the collection is locked and must be authenticated by the client application.

`READ UInt64 Created ;`  

The unix time when the collection was created.

`READ UInt64 Modified ;`

The unix time when the collection was last modified.
