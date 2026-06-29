OBS Studio supports the use of webpages as both Sources and Docks in the UI through [obs-browser](https://github.com/obsproject/obs-browser).

obs-browser introduces a cross-platform Browser Source, powered by the [Chromium Embedded Framework](https://bitbucket.org/chromiumembedded/cef/src/master/README.md) (CEF). CEF is a popular framework around [Chromium](https://www.chromium.org/Home/) which is the underlying engine powering many modern browsers like Google Chrome and Microsoft Edge. A Browser Source allows the user to integrate web-based overlays into their scenes, with complete access to modern web APIs.

Additionally, obs-browser enables Service Integration (linking third party services) and Browser Docks (webpages loaded into the interface itself) on all supported platforms, except for Wayland (Linux).

## Browser Drag and Drop

OBS supports dragging URLs into OBS in order to add them as a browser source which can be incredibly useful for things like stream widgets and overlays. Some source properties can be preconfigured via URL arguments or using the DataTransfer API.

Some examples and additional details are available on this [demonstration page](https://obsproject.com/tools/browser-drag-and-drop).


## Dev Tools

Developers of websites and scripts intended to be used within OBS will often desire to utilize [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) which is normally accessed from within the same application as the page. Since these pages are embedded within OBS Studio this is not possible to access through normal means. You can instead utilize Chromium's remote debugging functionality to access Dev Tools from another browser.

OBS Studio supports a number of [launch parameters](https://obsproject.com/kb/launch-parameters) and Chromium itself has a large number of [command line switches](https://peter.sh/experiments/chromium-command-line-switches/). On Windows these flags are also passed along to subprocesses which means CEF will also receive any parameters that OBS Studio is launched with. We explicitly reproduce that behavior on non-Windows operating systems for CEF.

The following switches are needed to connect to Dev Tools from another browser on the same system as OBS Studio

- `--remote-debugging-port`  
Enables remote debug over HTTP on the specified port  
Ex. `--remote-debugging-port=1234`

- `--remote-allow-origins`  
Enables web socket connections from the specified origins only. '*' allows any origin.  
Ex. `--remote-allow-origins=http://localhost:1234`
