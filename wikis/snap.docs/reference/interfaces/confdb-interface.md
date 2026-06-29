#  confdb interface

The `confdb` interface enables snaps to access to specific  [confdb](https://snapcraft.io/docs/explanation/how-snaps-work/confdb-configuration-mechanism/) views.

There are two fields that together identify the view being accessed: `account` and `view`. There is also an optional `role` field which may only take the value of "custodian", if the snap is a custodian for the confdb-schema being accessed.

See the [Confdb configuration mechanism](https://snapcraft.io/docs/explanation/how-snaps-work/confdb-configuration-mechanism/) for implementation details, and [Configure snaps with confdb](https://snapcraft.io/docs/how-to-guides/manage-snaps/configure-snaps-with-confdb/) to use confdb with your own snaps.

```
[...]
 read-sensor-params:
  interface: confdb
  account: acme
  view: sensors/read-sensor1-parameters
```

> Warning:
>  Confdb is currently considered an [Experimental feature](https://snapcraft.io/docs/reference/development/experimental-features/) and implementation details may change as development progresses.

## Developer details

**Auto-connect**: no, but plugs are auto-connected if the confdb's account is the same as the snap's publisher.

### Code examples

The test code can be found in the snapd repository:
https://github.com/canonical/snapd/blob/master/interfaces/builtin/confdb_test.go

The source code for the interface is in the snapd repository:

https://github.com/canonical/snapd/blob/master/interfaces/builtin/confdb.go
