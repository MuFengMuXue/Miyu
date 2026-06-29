## `org.freedesktop.Secret.Service`

org.freedesktop.Secret.Service — The Secret Service manages all the sessions and collections.

## Synopsis

### Methods

|                          |                             |
|--------------------------|-----------------------------|
| ` `**`OpenSession`**` (` | IN String `algorithm`,      |
|                          | IN Variant `input`,         |
|                          | OUT Variant `output`,       |
|                          | OUT ObjectPath `result``)`; |

 

|                               |                                         |
|-------------------------------|-----------------------------------------|
| ` `**`CreateCollection`**` (` | IN Dict\<String,Variant\> `properties`, |
|                               | IN String `alias`,                      |
|                               | OUT ObjectPath `collection`,            |
|                               | OUT ObjectPath `prompt``)`;             |

 

|                          |                                        |
|--------------------------|----------------------------------------|
| ` `**`SearchItems`**` (` | IN Dict\<String,String\> `attributes`, |
|                          | OUT Array\<ObjectPath\> `unlocked`,    |
|                          | OUT Array\<ObjectPath\> `locked``)`;   |

 

|                     |                                     |
|---------------------|-------------------------------------|
| ` `**`Unlock`**` (` | IN Array\<ObjectPath\> `objects`,   |
|                     | OUT Array\<ObjectPath\> `unlocked`, |
|                     | OUT ObjectPath `prompt``)`;         |

 

|                   |                                   |
|-------------------|-----------------------------------|
| ` `**`Lock`**` (` | IN Array\<ObjectPath\> `objects`, |
|                   | OUT Array\<ObjectPath\> `locked`, |
|                   | OUT ObjectPath `Prompt``)`;       |

 

|                         |                                             |
|-------------------------|---------------------------------------------|
| ` `**`GetSecrets`**` (` | IN Array\<ObjectPath\> `items`,             |
|                         | IN ObjectPath `session`,                    |
|                         | OUT Dict\<ObjectPath,Secret\> `secrets``)`; |

 

|                        |                                 |
|------------------------|---------------------------------|
| ` `**`ReadAlias`**` (` | IN String `name`,               |
|                        | OUT ObjectPath `collection``)`; |

 

|                       |                                |
|-----------------------|--------------------------------|
| ` `**`SetAlias`**` (` | IN String `name`,              |
|                       | IN ObjectPath `collection``)`; |

 

### Signals

|                                |                                 |
|--------------------------------|---------------------------------|
| ` `**`CollectionCreated`**` (` | OUT ObjectPath `collection``)`; |

 

|                                |                                 |
|--------------------------------|---------------------------------|
| ` `**`CollectionDeleted`**` (` | OUT ObjectPath `collection``)`; |

 

|                                |                                 |
|--------------------------------|---------------------------------|
| ` `**`CollectionChanged`**` (` | OUT ObjectPath `collection``)`; |

 

### Properties

## 

`READ Array<ObjectPath> Collections ;`

## Methods

### `org.freedesktop.Secret.Service.OpenSession`

|                          |                             |
|--------------------------|-----------------------------|
| ` `**`OpenSession`**` (` | IN String `algorithm`,      |
|                          | IN Variant `input`,         |
|                          | OUT Variant `output`,       |
|                          | OUT ObjectPath `result``)`; |

 

Open a unique session for the caller application.

`algorithm`  
The algorithm the caller wishes to use.

`input`  
Input arguments for the algorithm.

`output`  
Output of the session algorithm negotiation.

`result`  
The object path of the session, if session was created.

### `org.freedesktop.Secret.Service.CreateCollection`

|                               |                                         |
|-------------------------------|-----------------------------------------|
| ` `**`CreateCollection`**` (` | IN Dict\<String,Variant\> `properties`, |
|                               | IN String `alias`,                      |
|                               | OUT ObjectPath `collection`,            |
|                               | OUT ObjectPath `prompt``)`;             |

 

Create a new collection with the specified properties.

`properties`  
Properties for the new collection. This allows setting the new collection's properties upon its creation. All READWRITE properties are useable. Specify the property names in full interface.Property form.

###### Example 13.1: Example for properties

``` programlisting

properties = { "org.freedesktop.Secret.Collection.Label": "MyCollection" }

                                
```

`alias`  
If creating this connection for a well known alias then a string like `default`. If an collection with this well-known alias already exists, then that collection will be returned instead of creating a new collection. Any readwrite properties provided to this function will be set on the collection.

Set this to an empty string if the new collection should not be associated with a well known alias.

`collection`  
The new collection object, or '/' if prompting is necessary.

`prompt`  
A prompt object if prompting is necessary, or '/' if no prompt was needed.

### `org.freedesktop.Secret.Service.SearchItems`

|                          |                                        |
|--------------------------|----------------------------------------|
| ` `**`SearchItems`**` (` | IN Dict\<String,String\> `attributes`, |
|                          | OUT Array\<ObjectPath\> `unlocked`,    |
|                          | OUT Array\<ObjectPath\> `locked``)`;   |

 

Find items in any collection.

`attributes`  
Find secrets in any collection.

`unlocked`  
Items found.

`locked`  
Items found that require authentication.

### `org.freedesktop.Secret.Service.Unlock`

|                     |                                     |
|---------------------|-------------------------------------|
| ` `**`Unlock`**` (` | IN Array\<ObjectPath\> `objects`,   |
|                     | OUT Array\<ObjectPath\> `unlocked`, |
|                     | OUT ObjectPath `prompt``)`;         |

 

Unlock the specified objects.

`objects`  
Objects to unlock.

`unlocked`  
Objects that were unlocked without a prompt.

`prompt`  
A prompt object which can be used to unlock the remaining objects, or the special value '/' when no prompt is necessary.

### `org.freedesktop.Secret.Service.Lock`

|                   |                                   |
|-------------------|-----------------------------------|
| ` `**`Lock`**` (` | IN Array\<ObjectPath\> `objects`, |
|                   | OUT Array\<ObjectPath\> `locked`, |
|                   | OUT ObjectPath `Prompt``)`;       |

 

Lock the items.

`objects`  
Objects to lock.

`locked`  
Objects that were locked without a prompt.

`Prompt`  
A prompt to lock the objects, or the special value '/' when no prompt is necessary.

### `org.freedesktop.Secret.Service.GetSecrets`

|                         |                                             |
|-------------------------|---------------------------------------------|
| ` `**`GetSecrets`**` (` | IN Array\<ObjectPath\> `items`,             |
|                         | IN ObjectPath `session`,                    |
|                         | OUT Dict\<ObjectPath,Secret\> `secrets``)`; |

 

Retrieve multiple secrets from different items.

`items`  
Items to get secrets for.

`session`  
The session to use to encode the secrets.

`secrets`  
Secrets for the items.

### `org.freedesktop.Secret.Service.ReadAlias`

|                        |                                 |
|------------------------|---------------------------------|
| ` `**`ReadAlias`**` (` | IN String `name`,               |
|                        | OUT ObjectPath `collection``)`; |

 

Get the collection with the given alias.

`name`  
An alias, such as 'default'.

`collection`  
The collection or the path '/' if no such collection exists.

### `org.freedesktop.Secret.Service.SetAlias`

|                       |                                |
|-----------------------|--------------------------------|
| ` `**`SetAlias`**` (` | IN String `name`,              |
|                       | IN ObjectPath `collection``)`; |

 

Setup a collection alias.

`name`  
An alias, such as 'default'.

`collection`  
The collection to make the alias point to. To remove an alias use the special value '/'.

## Signals

### `org.freedesktop.Secret.Service.CollectionCreated`

|                                |                                 |
|--------------------------------|---------------------------------|
| ` `**`CollectionCreated`**` (` | OUT ObjectPath `collection``)`; |

 

A collection was created.

`collection`  
Collection that was created

### `org.freedesktop.Secret.Service.CollectionDeleted`

|                                |                                 |
|--------------------------------|---------------------------------|
| ` `**`CollectionDeleted`**` (` | OUT ObjectPath `collection``)`; |

 

A collection was deleted.

`collection`  
Collection that was deleted.

### `org.freedesktop.Secret.Service.CollectionChanged`

|                                |                                 |
|--------------------------------|---------------------------------|
| ` `**`CollectionChanged`**` (` | OUT ObjectPath `collection``)`; |

 

A collection was changed.

`collection`  
Collection that was changed.

## D-Bus Properties

Accessed using the org.freedesktop.DBus.Properties interface.

`READ Array<ObjectPath> Collections ;`

The object paths of all collections (ie: keyrings)
