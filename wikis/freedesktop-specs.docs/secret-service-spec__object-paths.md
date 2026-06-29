## 12 Object Paths

The various DBus object paths used with the Secret Service API are designed to be human readable but not displayed to the user. The object path of an item or collection should not change for its lifetime, under normal circumstances.

``` programlisting
/org/freedesktop/secrets
```

The object path for the service.

``` programlisting
/org/freedesktop/secrets/collection/xxxx
```

The object path for a collection, where *xxxx* represents a possibly encoded or truncated version of the initial label of the collection.

``` programlisting
/org/freedesktop/secrets/collection/xxxx/iiii
```

The object path for an item, where *xxxx* is the collection (above) and *iiii* is an auto-generated item specific identifier.

``` programlisting
/org/freedesktop/secrets/session/ssss
```

The object path for a session, where *ssss* is an auto-generated session specific identifier.

``` programlisting
/org/freedesktop/secrets/aliases/default
```

The default collection for client applications to store secrets is available under this object path in addition to its real object path (above). Other aliases may also be present.
