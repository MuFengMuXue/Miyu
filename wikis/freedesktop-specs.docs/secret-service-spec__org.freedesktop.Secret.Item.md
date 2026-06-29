## `org.freedesktop.Secret.Item`

org.freedesktop.Secret.Item — An item contains a secret, lookup attributes and has a label.

## Synopsis

### Methods

|                     |                             |
|---------------------|-----------------------------|
| ` `**`Delete`**` (` | OUT ObjectPath `Prompt``)`; |

 

|                        |                          |
|------------------------|--------------------------|
| ` `**`GetSecret`**` (` | IN ObjectPath `session`, |
|                        | OUT Secret `secret``)`;  |

 

|                        |                        |
|------------------------|------------------------|
| ` `**`SetSecret`**` (` | IN Secret `secret``)`; |

 

### Properties

## 

`READ Boolean Locked ;`  
`READWRITE Dict<String,String> Attributes ;`  
`READWRITE String Label ;`  
`READ UInt64 Created ;`  
`READ UInt64 Modified ;`

## Methods

### `org.freedesktop.Secret.Item.Delete`

|                     |                             |
|---------------------|-----------------------------|
| ` `**`Delete`**` (` | OUT ObjectPath `Prompt``)`; |

 

Delete this item.

`Prompt`  
A prompt object, or the special value '/' if no prompt is necessary.

### `org.freedesktop.Secret.Item.GetSecret`

|                        |                          |
|------------------------|--------------------------|
| ` `**`GetSecret`**` (` | IN ObjectPath `session`, |
|                        | OUT Secret `secret``)`;  |

 

Retrieve the secret for this item.

`session`  
The session to use to encode the secret.

`secret`  
The secret retrieved.

### `org.freedesktop.Secret.Item.SetSecret`

|                        |                        |
|------------------------|------------------------|
| ` `**`SetSecret`**` (` | IN Secret `secret``)`; |

 

Set the secret for this item.

`secret`  
The secret to set, encoded for the included session.

## D-Bus Properties

Accessed using the org.freedesktop.DBus.Properties interface.

`READ Boolean Locked ;`  

Whether the item is locked and requires authentication, or not.

`READWRITE Dict<String,String> Attributes ;`  

The lookup attributes for this item.

`READWRITE String Label ;`  

The displayable label for this item.

`READ UInt64 Created ;`  

The unix time when the item was created.

`READ UInt64 Modified ;`

The unix time when the item was last modified.
