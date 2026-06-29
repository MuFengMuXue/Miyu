# Secret Service API Draft

Authors:

Stef Walter `<stefw@collabora.co.uk>`(GNOME Keyring Developer)

Michael Leupold `<lemma@confuego.org>`(KWallet Developer)

  

Publication Date: 2026-04-08, Version: Secret Service 0.2 DRAFT

Copyright © 2008-2011 The Secret Service API Authors

[I API Documentation](description.md)

[1 Introduction](ch01.md)

[2 Secrets](ch02.md)

[3 Collection and Items](ch03.md)

[4 Aliases](aliases.md)

[5 Lookup Attributes](lookup-attributes.md)

[6 Sessions](sessions.md)

[7 Transfer of Secrets](transfer-secrets.md)

[7.1 Negotiation of Algorithms](transfer-secrets.md#id-1.2.8.6)

[7.2 Algorithm: plain](ch07s02.md)

[7.3 Algorithm: dh-ietf1024-sha256-aes128-cbc-pkcs7](ch07s03.md)

[8 Locking and Unlocking](unlocking.md)

[9 Prompts and Prompting](prompts.md)

[10 What's not included in the API](ch10.md)

[11 Notes for Service Implementors](ch11.md)

[II D-Bus API Reference](ref-dbus-api.md)

[12 Object Paths](object-paths.md)

[13 Interfaces](interfaces.md)

[`org.freedesktop.Secret.Service`](org.freedesktop.Secret.Service.md) — The Secret Service manages all the sessions and collections.

[`org.freedesktop.Secret.Collection`](org.freedesktop.Secret.Collection.md) — A collection of items containing secrets.

[`org.freedesktop.Secret.Item`](org.freedesktop.Secret.Item.md) — An item contains a secret, lookup attributes and has a label.

[`org.freedesktop.Secret.Session`](org.freedesktop.Secret.Session.md) — A session tracks state between the service and a client application.

[`org.freedesktop.Secret.Prompt`](org.freedesktop.Secret.Prompt.md) — A prompt necessary to complete an operation.

[14 Types](types.md)

[14.1 Struct types](types.md#id-1.3.4.2)

[14.2 Map types](ch14s02.md)

[15 Errors](errors.md)

[References](bi01.md)

List of Examples

[13.1 Example for properties](org.freedesktop.Secret.Service.md#id-1.3.3.2.4.3.4.1.2.1.1.1)

[13.2 Example for properties](org.freedesktop.Secret.Collection.md#id-1.3.3.3.4.4.4.1.2.1.1.1)
