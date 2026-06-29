## [Create a custom application launcher in GNOME Shell]

Create a [APP_NAME.desktop] (APP_NAME application name) file under [/usr/share/applications] (or [\~/.local/share/applications] or directly in [\~/Desktop]) with the following content:

[FILE] **`APP_NAME.desktop`APP_NAME.desktop file**

    [Desktop Entry]
    Encoding=UTF-8
    Name=APP_NAME
    Exec=/PATH/TO/APP/EXECUTABLE
    Icon=/PATH/TO/APP/ICON
    Type=Application
    Categories=APPLICATION_CATEGORY_NAME;

For detailed `.desktop` specification (eg. list of [Registered Categories](https://specifications.freedesktop.org/menu-spec/latest/apa.html)) see: [specifications.freedesktop.org](https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html).