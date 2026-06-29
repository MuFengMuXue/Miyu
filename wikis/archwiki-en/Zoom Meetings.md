# Zoom Meetings

Zoom Meetings (commonly shortened to Zoom) is a proprietary, cross-platform, cloud-based video conferencing platform.

## Installation
Preferably, install , since the files from the website will not allow self-updating.

## Tips and tricks
## Virtual backgrounds
Zoom saves the default virtual backgrounds to  and the custom virtual backgrounds to .

## Logs
Zoom saves the logs to .

## Use system theme
Edit  and change the value of  to , then restart zoom.

## Disable Zoom mini window
Zoom's "Mini Window" feature allows to minimize the Zoom video, but keep it on top as an overlay. To disable it:

Edit  and change the value of  to , then restart zoom.

## Increase interface size
Set  environment variable before launching Zoom (see HiDPI#Qt 5). Otherwise, the embedded "Schedule" panel will not be scaled correctly.

## Disable ZoomWebviewHost
You can disable ZoomWebviewHost by setting  in  if you want to to save RAM. It disables some features such as whiteboard.

## Running on Wayland without Xwayland
You need to set  in  if you do not use Xwayland. The  process may stop with 0MB memory without Xwayland.

## Screen share
## Wayland
To share your screen on Wayland, install the required packages for WebRTC screen sharing, edit  and make sure the value  is set to , if not, then restart zoom.

There are reports that even with all the dependencies in place Zoom will still not use pipewire for screen capture.  In this situation manually configuring Zoom to use Pipewire has been reported to work.  This can be done as follows:

# Start the desktop client and go to Settings->Share Screen
# Click Advanced
# Change the Screen capture mode to Pipewire (as opposed to Automatic)

## Xorg
To enable screen share on Xorg, you must change the session type to  (i.e. set the  environment variable). Depending on how you start your graphical session, this value might not be set by default.

## Joining meetings in the browser
If you want to avoid the Zoom binary entirely, a reasonable alternative is the Zoom web client. While the web client is not fully on par with all the features offered by the client binary, it offers a smooth and stable experience, and does raise fewer security concerns than installing a proprietary binary.

If the original meeting URL is , the web client can be accessed via the URL .

## "Redirector" browser extension
In Firefox, Chromium, and Opera, it is possible to use the Redirector extension to rewrite the URL automatically. Create a rule as follows:

* Description:       Zoom web client
* Example URL:
* Include pattern:
* Redirect to:
* Pattern type:      Wildcard
