# API Reference

Portal interfaces are available to sandboxed applications with the default filtered session bus access of Flatpak.

Desktop portals appear under the bus name `org.freedesktop.portal.Desktop` and the object path `/org/freedesktop/portal/desktop` on the session bus, unless specified otherwise.

Apps running on the host system have access to a special interface for registering themselves with XDG Desktop Portal. Registering a host app with XDG Desktop Portal overwrites the automatic detection based on the [XDG cgroup pathname standardization for applications](https://systemd.io/DESKTOP_ENVIRONMENTS/#xdg-standardization-for-applications). This might improve the user experience when the host app was launched in a way that doesn’t follow the standard. See [org.freedesktop.host.portal.Registry](doc-org.freedesktop.host.portal.Registry.md)

Disclaimer: The host app registry is expected to eventually be deprecated and may be removed. Applications should gracefully handle interface or method no longer being available to be forward compatible. App launchers, or apps themselves, should place the app in a cgroup named according to specific naming conventions. When the host app registry becomes deprecated, the details of the replacement will be documented in [org.freedesktop.host.portal.Registry](doc-org.freedesktop.host.portal.Registry.md).

All apps have access to the portals below:

- [Account](doc-org.freedesktop.portal.Account.md)
- [Background](doc-org.freedesktop.portal.Background.md)
- [Camera](doc-org.freedesktop.portal.Camera.md)
- [Clipboard](doc-org.freedesktop.portal.Clipboard.md)
- [Documents](doc-org.freedesktop.portal.Documents.md)
- [Dynamic Launcher](doc-org.freedesktop.portal.DynamicLauncher.md)
- [Email](doc-org.freedesktop.portal.Email.md)
- [File Chooser](doc-org.freedesktop.portal.FileChooser.md)
- [File Transfer](doc-org.freedesktop.portal.FileTransfer.md)
- [Game Mode](doc-org.freedesktop.portal.GameMode.md)
- [Global Shortcuts](doc-org.freedesktop.portal.GlobalShortcuts.md)
- [Inhibit](doc-org.freedesktop.portal.Inhibit.md)
- [Input Capture](doc-org.freedesktop.portal.InputCapture.md)
- [Location](doc-org.freedesktop.portal.Location.md)
- [Memory Monitor](doc-org.freedesktop.portal.MemoryMonitor.md)
- [Network Monitor](doc-org.freedesktop.portal.NetworkMonitor.md)
- [Notification](doc-org.freedesktop.portal.Notification.md)
- [OpenURI](doc-org.freedesktop.portal.OpenURI.md)
- [Power Profile Monitor](doc-org.freedesktop.portal.PowerProfileMonitor.md)
- [Print](doc-org.freedesktop.portal.Print.md)
- [Proxy Resolver](doc-org.freedesktop.portal.ProxyResolver.md)
- [Realtime](doc-org.freedesktop.portal.Realtime.md)
- [Remote Desktop](doc-org.freedesktop.portal.RemoteDesktop.md)
- [Request](doc-org.freedesktop.portal.Request.md)
- [ScreenCast](doc-org.freedesktop.portal.ScreenCast.md)
- [Screenshot](doc-org.freedesktop.portal.Screenshot.md)
- [Secret](doc-org.freedesktop.portal.Secret.md)
- [Session](doc-org.freedesktop.portal.Session.md)
- [Settings](doc-org.freedesktop.portal.Settings.md)
- [Trash](doc-org.freedesktop.portal.Trash.md)
- [Usb](doc-org.freedesktop.portal.Usb.md)
- [Wallpaper](doc-org.freedesktop.portal.Wallpaper.md)
