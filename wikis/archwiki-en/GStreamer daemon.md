# GStreamer daemon

GStreamer Daemon (gstd)

GStreamer Daemon (gstd) is a background service for controlling GStreamer pipelines via a high-level TCP-based API. It enables remote or decoupled control of audio/video pipelines in real-time.

The main benefit of gstd is that it separates the control logic from the media processing logic. This allows pipelines to be created, played, paused, or modified dynamically through simple text messages over a TCP connection. The control application can be written in any language and run on a different machine without requiring GObject or GLib bindings.

This design makes gstd ideal for embedded devices, automated testing, and professional streaming or recording applications. It can run as a user service (for desktop integration) or a system service (for headless environments).

## Installation
Install the  package.

It is highly recommended to also install the following GStreamer plugin sets to enable a wide range of media formats and capabilities:

*
*
*
*

Additional useful packages include  for connecting independent pipelines,  for web interface examples, and  for debugging.

## Configuration
gstd is configured via the  file. This sets the address and port the daemon listens on.

Example configuration:

gstd supports multiple communication protocols with TCP being the primary method. HTTP API and D-Bus are also available for compatibility.

## Usage
The package provides two systemd services:

*  - user unit for desktop usage that can display windows and use speakers
*  - system service for headless/embedded/server use that runs as the gstd user

Only one service should be enabled at a time.

## Command Line Interface
Control pipelines using  or . The tool supports both interactive mode and single command execution.

Interactive mode:
 $ gst-client
 $ gstd> pipeline_create testpipe videotestsrc name=vts ! autovideosink
 $ gstd> pipeline_play testpipe
 $ gstd> element_set testpipe vts pattern ball
 $ gstd> pipeline_delete testpipe

Single command mode for scripts:
 $ gst-client pipeline_create testpipe videotestsrc ! autovideosink
 $ gst-client pipeline_play testpipe
 $ gst-client pipeline_delete testpipe

## Desktop usage example: Display a test video
Start/enable the  user unit, then:

 $ gst-client pipeline_create my_gui_pipe 'videotestsrc ! autovideosink'

 $ gst-client pipeline_play my_gui_pipe

 $ gst-client pipeline_delete my_gui_pipe

A test video pattern should appear in a window.

## Server usage example: Record from DeckLink (720p50)
Start/enable the .

This example demonstrates a professional use case: capturing 720p50 video from the first SDI input (device-number=0) of a DeckLink card and encoding it to an MP4 file.

The output file is saved to , which is writable by the gstd system user. This path is explicitly granted read-write access via the systemd service definition.

 $ gst-client pipeline_create decklink_rec 'decklinkvideosrc device-number=0 mode=17 connection=sdi ! videoconvert ! queue ! x264enc ! mp4mux ! filesink location=/var/lib/gstd/decklink_recording.mp4'

 $ gst-client pipeline_play decklink_rec

To gracefully stop the recording:

 $ gst-client event_eos decklink_rec

 $ gst-client pipeline_stop decklink_rec

 $ gst-client pipeline_delete decklink_rec

Check that the recording file was created:

 # ls -l /var/lib/gstd/decklink_recording.mp4

## Advanced Features
gstd supports runtime pipeline modification including seeking, speed control, and property changes:

 # Seek to 30 seconds (in nanoseconds)
 $ gst-client element_seek player 30000000000

 # Change playback speed (2x faster, 0.5x slower, -1.0 reverse)
 $ gst-client element_speed player 2.0

 # Modify element properties during playback
 $ gst-client element_set camera x264enc bitrate 1000000

## Using with Interpipe
The  package enables connecting multiple independent pipelines without data copying, useful for complex streaming setups:

 # Create source and sink pipelines
 $ gst-client pipeline_create src videotestsrc ! interpipesink name=mysink
 $ gst-client pipeline_create sink interpipesrc listen-to=mysink ! autovideosink

 # Switch connections at runtime
 $ gst-client element_set sink interpipesrc listen-to=othersink

## Direct TCP Communication
The gstd daemon offers multiple API interfaces to support diverse development environments and integration needs. Currently supported API variants include:

* C/C++ API – For high-performance native applications requiring direct system integration.
* Python API – Ideal for scripting, rapid prototyping, and automation use cases.
* JavaScript API – Enables integration with web-based applications or Node.js environments.
* HTTP API – A language-agnostic, REST-like interface suitable for remote access and lightweight clients.

Applications can communicate directly with gstd over TCP, enabling flexible and efficient integration across local or distributed systems.

## Using netcat
 $ echo "pipeline_create test videotestsrc ! fakesink" | nc -q0 localhost 5000

 $ echo "pipeline_play test" | nc -q0 localhost 5000

 $ echo "pipeline_pause test" | nc -q0 localhost 5000

 $ echo "element_set test videotestsrc1 pattern ball" | nc -q0 localhost 5000

 $ echo "pipeline_stop test" | nc -q0 localhost 5000

 $ echo "pipeline_delete test" | nc -q0 localhost 5000

Check pipeline status:

 echo "list_pipelines" | nc -q0 localhost 5000

The TCP protocol uses simple text commands similar to gst-client and is particularly reliable for element property manipulation and pipeline deletion.

## Using HTTP API (RESTful API)
For web applications and REST-style integration, gstd provides an HTTP API when enabled.

Enable HTTP protocol in /etc/conf.d/gstd:

 GSTD_OPTS="--enable-http-protocol --http-address=127.0.0.1 --http-port=5000"

Complete HTTP workflow (recommended method using --data-urlencode for proper URL encoding):

 $ curl -X POST -G --data-urlencode "name=test" --data-urlencode "description=videotestsrc ! autovideosink" http://127.0.0.1:5000/pipelines

 $ curl http://127.0.0.1:5000/pipelines/  # List pipelines

 $ curl -X PUT 'http://127.0.0.1:5000/pipelines/test/state?name=playing'

 $ curl -X PUT 'http://127.0.0.1:5000/pipelines/test/state?name=paused'

 $ curl -X PUT 'http://127.0.0.1:5000/pipelines/test/state?name=null'  # Stop

 $ curl -X DELETE 'http://127.0.0.1:5000/pipelines?name=test'  # Delete

Get pipeline information:

 $ curl http://127.0.0.1:5000/pipelines/test/state  # Get current state

 $ curl http://127.0.0.1:5000/pipelines/test/graph  # Get GraphViz representation

List all elements in pipeline:

 $ curl http://127.0.0.1:5000/pipelines/test/elements/

## Troubleshooting
## "Address already in use"
This error occurs when the specified port is already in use, either by another service or because both the user and system instances of gstd are running simultaneously.

Disable the unneded one.

## "State error" or "Bad pipeline description"
This usually means:

* A required GStreamer plugin is missing
* The pipeline syntax is invalid

Solutions:

* Ensure plugins like gst-plugins-good are installed
* Restart the gstd service after plugin installation
* Use queue, videoconvert, or audioconvert to aid negotiation

## Plugin registry issues
If new GStreamer elements don't appear after installing plugin packages, rebuild the plugin registry:

 $ rm ~/.cache/gstreamer-1.0/registry.*.bin

## Debugging
Run gstd with debug output for troubleshooting:

 $ gstd -e --gst-debug-level=3

 $ gstd -e --gst-debug=gstd:5,GST_PADS:4

Verify the service is running and listening:

 $ systemctl --user status gstd # Running as user unit
 $ systemctl status gstd-server # Running as system service

 $ ss -tlnp | grep 5000

Common solutions for pipeline issues include verifying all required plugins are installed, testing pipelines with  first, and using autovideosink/autoaudiosink for automatic output selection.
