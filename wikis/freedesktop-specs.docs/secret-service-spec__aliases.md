## 4 Aliases

Collections may be accessed via well known aliases. For example an alias called `default` tells applications which is the default collection to store secrets.

The aliased collections will be available at a [well-known DBus object path](object-paths.html "Chapter 12. Object Paths").

If an application needs to create a collection with a given alias, this can be done in a race free fashion by specifying the alias parameter of the [CreateCollection()](org.freedesktop.Secret.Service.md#org.freedesktop.Secret.Service.CreateCollection "org.freedesktop.Secret.Service.CreateCollection") method on the service interface. If a collection with that alias already exists, then it will be returned instead of creating a new one.

For applications like password managers it can be useful to allow the user to configure which collection is associated with which well known alias. To alias or unalias a collection use the [SetAlias()](org.freedesktop.Secret.Service.md#org.freedesktop.Secret.Service.SetAlias "org.freedesktop.Secret.Service.SetAlias") method on the service interface. Use the [ReadAlias()](org.freedesktop.Secret.Service.md#org.freedesktop.Secret.Service.ReadAlias "org.freedesktop.Secret.Service.ReadAlias") method on the service interface to discover which collection is associated with a given alias.
