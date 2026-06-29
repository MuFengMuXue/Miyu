# security_context_v1

## Interface `wp_security_context_manager_v1` version 1

client security context manager

This interface allows a client to register a new Wayland connection to the compositor and attach a security context to it. This is intended to be used by sandboxes. Sandbox engines attach a security context to all connections coming from inside the sandbox. The compositor can then restrict the features that the sandboxed connections can use. Compositors should forbid nesting multiple security contexts by not exposing wp_security_context_manager_v1 global to clients with a security context attached, or by sending the nested protocol error. Nested security contexts are dangerous because they can potentially allow privilege escalation of a sandboxed client. Warning! The protocol described in this file is currently in the testing phase. Backward compatible changes may be added together with the corresponding interface version bump. Backward incompatible changes can only be done by creating a new major version of the extension.

### Requests

- `destroy`: destroy the manager object
  Destroy the manager. This doesn't destroy objects created with the manager.
- `create_listener`: create a new security context
  Creates a new security context with a socket listening FD. The compositor will accept new client connections on listen_fd. listen_fd must be ready to accept new connections when this request is sent by the client. In other words, the client must call bind(2) and listen(2) before sending the FD. close_fd is a FD that will signal hangup when the compositor should stop accepting new connections on listen_fd. The compositor must continue to accept connections on listen_fd when the Wayland client which created the security context disconnects. After sending this request, closing listen_fd and close_fd remains the only valid operation on them.
  Arguments: `id` (new_id); `listen_fd` (fd) - listening socket FD; `close_fd` (fd) - FD signaling when done

### Enums

- `error`

## Interface `wp_security_context_v1` version 1

client security context

The security context allows a client to register a new client and attach security context metadata to the connections. When both are set, the combination of the application ID and the sandbox engine must uniquely identify an application. The same application ID will be used across instances (e.g. if the application is restarted, or if the application is started multiple times). When both are set, the combination of the instance ID and the sandbox engine must uniquely identify a running instance of an application.

### Requests

- `destroy`: destroy the security context object
  Destroy the security context object.
- `set_sandbox_engine`: set the sandbox engine
  Attach a unique sandbox engine name to the security context. The name should follow the reverse-DNS style (e.g. "org.flatpak"). A list of well-known engines is maintained at: https://gitlab.freedesktop.org/wayland/wayland-protocols/-/blob/main/staging/security-context/engines.md It is a protocol error to call this request twice. The already_set error is sent in this case.
  Arguments: `name` (string) - the sandbox engine name
- `set_app_id`: set the application ID
  Attach an application ID to the security context. The application ID is an opaque, sandbox-specific identifier for an application. See the well-known engines document for more details: https://gitlab.freedesktop.org/wayland/wayland-protocols/-/blob/main/staging/security-context/engines.md The compositor may use the application ID to group clients belonging to the same security context application. Whether this request is optional or not depends on the sandbox engine used. It is a protocol error to call this request twice. The already_set error is sent in this case.
  Arguments: `app_id` (string) - the application ID
- `set_instance_id`: set the instance ID
  Attach an instance ID to the security context. The instance ID is an opaque, sandbox-specific identifier for a running instance of an application. See the well-known engines document for more details: https://gitlab.freedesktop.org/wayland/wayland-protocols/-/blob/main/staging/security-context/engines.md Whether this request is optional or not depends on the sandbox engine used. It is a protocol error to call this request twice. The already_set error is sent in this case.
  Arguments: `instance_id` (string) - the instance ID
- `commit`: register the security context
  Atomically register the new client and attach the security context metadata. If the provided metadata is inconsistent or does not match with out of band metadata (see https://gitlab.freedesktop.org/wayland/wayland-protocols/-/blob/main/staging/security-context/engines.md), the invalid_metadata error may be sent eventually. It's a protocol error to send any request other than "destroy" after this request. In this case, the already_used error is sent.

### Enums

- `error`
