#  snap-interfaces-requests-control interface

The `snap-interfaces-requests-control` interface enables the prompting API and its access to prompting-related notice types. This is used internally by snapd to request and manage system resource access.

> Tip:
>
> See [Interface management](https://snapcraft.io/docs/how-to-guides/manage-snaps/connect-interfaces/) and [Supported interfaces](https://snapcraft.io/docs/reference/interfaces/) for further details on how interfaces are used.
>

## Developer details

**Auto-connect**: no

### Endpoint access permissions
<ul>
<li>/v2/system-info</li>
<li>/v2/icons/{name}/icon</li>
<li>/v2/notices</li>
<li>/v2/notices/{id}</li>
<li>/v2/snaps/{name}</li>
<li>/v2/interfaces/requests/prompts</li>
<li>/v2/interfaces/requests/prompts/{id}</li>
<li>/v2/interfaces/requests/rules</li>
<li>/v2/interfaces/requests/rules/{id}</li>
</ul>

### Code examples

The test code can be found in the snapd repository:
https://github.com/canonical/snapd/blob/master/interfaces/builtin/snap_interfaces_requests_control_test.go

The source code for the interface is in the snapd repository:

https://github.com/canonical/snapd/blob/master/interfaces/builtin/snap_interfaces_requests_control.go
