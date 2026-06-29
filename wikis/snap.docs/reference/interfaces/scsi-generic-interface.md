#  scsi-generic interface

The `scsi-generic` interface allows read and write access to [SCSI Generic driver](https://www.kernel.org/doc/html/latest/scsi/scsi-generic.html) (sg) devices.

## Developer details

**[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/)** : no

**[Super-privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/)** : yes
 * `shared-memory` (slot and plug):

### Code examples

```yaml
apps:
 app:
  command: foo
  plugs: [scsi-generic]
```

The test code can be found in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/scsi_generic_test.go

The source code for the interface is in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/scsi_generic.go
