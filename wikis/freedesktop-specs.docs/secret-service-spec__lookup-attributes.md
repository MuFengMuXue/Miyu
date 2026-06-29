## 5 Lookup Attributes

Attributes can and should be stored with a secret to facilitate lookup of the secret at a later date.

An attribute constists of a name, and a value. Both parts are simple strings.

The service may have additional requirements as to what can be present in an attribute name. It is recommended that attribute names are human readable, and kept simple for the sake of simplicity.

During a lookup, attribute names and values are matched via case-sensitive string equality.

It's important to remember that attributes are not part of the secret. Services implementing this API will probably store attributes in an unencrypted manner in order to support simple and effecient lookups.

In order to search for items, use the [`SearchItems()`](org.freedesktop.Secret.Service.md#org.freedesktop.Secret.Service.SearchItems "org.freedesktop.Secret.Service.SearchItems") method of the Service interface. The matched items will be returned in two sets. The *unlocked* return value will contain the object paths of all the items that are not locked. The *locked* return value will contain object paths of items that are locked, which can be [unlocked if desired](unlocking.html "Chapter 8. Locking and Unlocking").

The [`SearchItems()`](org.freedesktop.Secret.Collection.md#org.freedesktop.Secret.Collection.SearchItems "org.freedesktop.Secret.Collection.SearchItems") method of the Collection interface is similar, except for it only searches a single collection.
