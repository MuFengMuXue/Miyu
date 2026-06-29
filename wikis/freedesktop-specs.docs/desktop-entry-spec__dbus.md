## 8 D-Bus Activation

Applications that support being launched by D-Bus must implement the following interface (given in D-Bus introspection XML format):

``` programlisting
  <interface name='org.freedesktop.Application'>
    <method name='Activate'>
      <arg type='a{sv}' name='platform_data' direction='in'/>
    </method>
    <method name='Open'>
      <arg type='as' name='uris' direction='in'/>
      <arg type='a{sv}' name='platform_data' direction='in'/>
    </method>
    <method name='ActivateAction'>
      <arg type='s' name='action_name' direction='in'/>
      <arg type='av' name='parameter' direction='in'/>
      <arg type='a{sv}' name='platform_data' direction='in'/>
    </method>
  </interface>
    
```

The application must name its desktop file in accordance with the naming recommendations in the introduction section (e.g. the filename must be like `org.example.FooViewer.desktop`). The application must have a D-Bus service activatable at the well-known name that is equal to the desktop file name with the `.desktop` portion removed (for our example, `org.example.FooViewer`). The above interface must be implemented at an object path determined as follows: starting with the well-known D-Bus name of the application, change all dots to slashes and prefix a slash. If a dash ('`-`') is found, convert it to an underscore ('`_`'). For our example, this is `/org/example/FooViewer`.

The `Activate` method is called when the application is started without files to open.

The `Open` method is called when the application is started with files. The array of strings is an array of URIs, in UTF-8.

The `ActivateAction` method is called when [Desktop Actions](extra-actions.html "11. Additional applications actions") are activated. The `action-name` parameter is the name of the action.

All methods take a `platform-data` argument that is used in a similar way to how environment variables might be used. Current fields described by the specification are:

- `desktop-startup-id`: This should be a string of the same value as would be stored in the `DESKTOP_STARTUP_ID` environment variable, as specified by the [Startup Notification Protocol Specification (http://www.freedesktop.org/Standards/startup-notification-spec)](http://www.freedesktop.org/Standards/startup-notification-spec).

- `activation-token`: This should be a string of the same value as would be stored in the `XDG_ACTIVATION_TOKEN` environment variable, as specified by the [XDG Activation (https://gitlab.freedesktop.org/wayland/wayland-protocols/-/blob/main/staging/xdg-activation/xdg-activation-v1.xml)](https://gitlab.freedesktop.org/wayland/wayland-protocols/-/blob/main/staging/xdg-activation/xdg-activation-v1.xml) protocol for Wayland.
