# PipeWire API

The PipeWire API consists of several parts:

- The pw_stream for a convenient way to send and receive data streams from/to PipeWire.

- The pw_filter for a convenient way to implement processing filters.

- The api_pw_core to access a PipeWire instance. This API is used
by all clients that need to communicate with the PipeWire Daemon and provides
the necessary structs to interface with the daemon.

- The api_pw_impl is primarily used by the PipeWire Daemon itself but also by the
PipeWire Session Manager and modules/extensions that need to build objects in
the graph.

- The api_pw_util containing various utility functions and structures.

- The api_pw_ext for interfacing with certain extension modules.

The APIs work through proxy objects, so that calling a method on an object
invokes that same method on the remote side. Marshalling and de-marshalling is
handled transparently by the Protocol Native.
The below graph illustrates this approach:

digraph API {
  compound=true;
  node [shape="box"];
  rankdir="RL";

  subgraph cluster_daemon {
       rankdir="TB";
       label="PipeWire daemon";
       style="dashed";

       impl_core [label="Core Impl. Object"];
       impl_device [label="Device Impl. Object"];
       impl_node [label="Node Impl. Object"];
  }

  subgraph cluster_client {
       rankdir="TB";
       label="PipeWire client";
       style="dashed";

       obj_core [label="Core Object"];
       obj_device [label="Device Object"];
       obj_node [label="Node Object"];
  }

  obj_core -> impl_core;
  obj_device -> impl_device;
  obj_node -> impl_node;

}

It is common for clients to use both the api_pw_core and the api_pw_impl
and both APIs are provided by the same library.

- SPA (Simple Plugin API)
- Client Impl
- Proxy
- Streams
- Thread Loop

 api_pw_core Core API

The Core API to access a PipeWire instance. This API is used by all
clients to communicate with the PipeWire Daemon.

If you are familiar with Wayland implementation, the Core API is
roughly equivalent to libwayland-client.

See: PipeWire API

 api_pw_impl Implementation API

The implementation API provides the tools to build new objects and
modules.

If you are familiar with Wayland implementation, the Implementation API is
roughly equivalent to libwayland-server.

See: PipeWire API
