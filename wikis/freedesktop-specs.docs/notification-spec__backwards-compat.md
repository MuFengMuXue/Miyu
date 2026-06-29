## 3 Backwards Compatibility

Clients should try and avoid making assumptions about the presentation and abilities of the notification server. The message content is the most important thing.

Clients can check with the server what capabilities are supported using the `GetCapabilities` message. See [Protocol](protocol.html "9. D-BUS Protocol").

If a client requires a response from a passive popup, it should be coded such that a non-focus-stealing message box can be used in the case that the notification server does not support this feature.
