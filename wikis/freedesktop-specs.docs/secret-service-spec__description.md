# Part I API Documentation

[1 Introduction](ch01.md)  
The Secret Service API allows client applications to store secrets securely in a service running in the user's login session.

[2 Secrets](ch02.md)  
A secret is something an application wishes to store securely. A good example is a password that an application needs to save and use at a later date.

[3 Collection and Items](ch03.md)  
Each secret is stored together with [lookup attributes](lookup-attributes.html "Chapter 5. Lookup Attributes") and a label. These together form an [item](org.freedesktop.Secret.Item.html "org.freedesktop.Secret.Item").

[4 Aliases](aliases.md)  
Collections may be accessed via well known aliases. For example an alias called `default` tells applications which is the default collection to store secrets.

[5 Lookup Attributes](lookup-attributes.md)  
Attributes can and should be stored with a secret to facilitate lookup of the secret at a later date.

[6 Sessions](sessions.md)  
A session is established between a client application and a service. A session is used to [transfer secrets](transfer-secrets.html "Chapter 7. Transfer of Secrets") between the client application and the service.

[7 Transfer of Secrets](transfer-secrets.md)  
To access or store secrets, use the [`GetSecret()`](org.freedesktop.Secret.Item.md#org.freedesktop.Secret.Item.GetSecret "org.freedesktop.Secret.Item.GetSecret"), [`SetSecret()`](org.freedesktop.Secret.Item.md#org.freedesktop.Secret.Item.SetSecret "org.freedesktop.Secret.Item.SetSecret") methods on the item interface, or the [`GetSecrets()`](org.freedesktop.Secret.Service.md#org.freedesktop.Secret.Service.GetSecrets "org.freedesktop.Secret.Service.GetSecrets"), method on the service interface.

[8 Locking and Unlocking](unlocking.md)  
Some items and/or collections may be marked as locked by the service. The secrets of locked items cannot be accessed. Additionally, locked items or collections cannot be modified by the client application.

[9 Prompts and Prompting](prompts.md)  
In order to complete various operations, such as unlocking a collection, the service may need to prompt the user for additional information, such as a master password.

[10 What's not included in the API](ch10.md)  
A service may implement additional DBus interfaces for further capabilities not included in this specification. Password management applications or other narrowly focused tools should make use of these when necessary.

[11 Notes for Service Implementors](ch11.md)  
\[TODO: complete\]
