# Configuration

WirePlumber is a heavily modular daemon. By itself, it doesn't do anything except load its configured components. The actual management logic is implemented inside those components.

At startup, WirePlumber reads its configuration file (combined with all the fragments it may have) and loads the components specified in the selected profile. This configures the operation context. Then, the components take over and drive the entirety of the daemon's operation.

The sections below describe in more detail the configuration file format and the various options available.
