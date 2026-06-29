# About AppStream

## What is AppStream?

AppStream is a cross-distro effort for enhancing the metadata available about software components in the Linux and free-software ecosystem. One of the project's goals is to make building software-center applications possible, and make interaction with the package sources of a distribution smarter. AppStream provides specifications for meta-information which is shipped by upstream projects and can be consumed by other software. The meta-information includes data which is interesting to display in software centers and is mainly useful for end-users, as well as descriptions about the public interfaces a software component provides, which is mainly useful for developers, 3rd-party software installers and for automatically installing missing components on a distribution, for example missing firmware or mimetype-handlers.

Distributors provide metadata as well, which describes all components available in a software repository. That data is composed of the upstream-metainfo and some other sources. AppStream also provides specifications for things like a screenshot-service, application ratings & reviews etc.

All parts of AppStream are distribution-agnostic, and therefore it is easily possible to build software management tools with it that work on any distribution implementing the AppStream specification.

### Architecture

# Upstream Metadata

AppStream allows upstream projects to define metadata about the components they provide using small XML files, metainfo files, which get installed into locations on the client system and are used by distributors to enhance their metadata.

A "component" is a piece of software, like an application, a library, a font or a codec. For several components, especially those which are shown in software-centers, we provide specialized metainfo files to define specific properties and data of these components. For example, applications and fonts support screenshots, while codecs don't.

All metainfo files need to contain a minimal amount of information, defined in the "Generic Component" section, which also describes some optional elements which can be used. Specialized components might require more information to be complete and valid.

The XML in metainfo files does not need any XML namespace, and adding one should generally be avoided. If you want to use a namespace though (maybe in case you want to embed the data in other contexts), the xmlns should be `https://specifications.freedesktop.org/metainfo/1.0`.

## Generic Component

### Introduction

For a distribution, it is good to know more about the content of a package. Which public interfaces (libraries? Python modules?) does it provide? Does it contain codecs? Does it contain firmware? Fonts? An application? All of this information can be used to automatically install missing software or to offer users a choice on what they want to install from a software center.

To provide this information, we created the *metainfo* files, which allow **upstream projects** to describe the content of their software package. If a metainfo file contains a `<provides/>` tag, distributors must also ensure that the package providing the file contains all items referenced by that statement, or is installed by a metapackage depending on packages which provide these items. This gives upstream projects a (very light) way to influence distributor packaging. More information about that can be found below.

Several specialized component-metainfo files exist, for example for applications or fonts. These are all based on this generic component XML specification, and are described in the following chapters.

### Filesystem locations

Upstream projects can ship one or more metainfo files in `/usr/share/metainfo/%{id}.metainfo.xml`, where `id` is a unique identifier of this specific component.

> [!NOTE]
> Component metadata of type `desktop-application` as described in [Desktop Applications](#sect-Metadata-Application) can be installed with an `.appdata.xml` extension as well for historical reasons. AppStream implementations will read the XML files as long as they end up in the right location on the filesystem.

> [!IMPORTANT]
> AppStream tools scan the `/usr/share/appdata/` path for legacy compatibility as well. It should not be used anymore by new software though, even on older Linux distributions (like RHEL 7 and Ubuntu 16.04 LTS) the metainfo path is well supported. Support for the legacy path will likely be dropped completely with a future AppStream 1.0 release.

### XML Specification

The XML for a generic component definition starts with a `<component>` tag as the root element. The `<component>` element must at least have an `id`, `name` and `summary` tag; a `provides` tag with appropriate children is highly recommended.

In addition to the `type` attribute denoting the component type in case the component is not a `generic` component, the `component` tag may also have a `date_eol` attribute that sets a date when the component stops to be supported entirely (this may be the case for superseded legacy software like `org.python.python2`). The attribute value can be any complete date or time in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601).

All possible tags which can be used with components of all types are:

\<id/\>  
The `id` tag is a unique identifier for this component. It must contain only alphanumeric ASCII characters, dots, hyphens and underscores. Spaces are not allowed. While hyphens are allowed for legacy compatibility, their usage is strongly discouraged to ensure interoperability of the AppStream ID with other tools such as D-Bus (and thereby making the ID more generic and useful). For the same reason it is also strongly discouraged to start any segment of the ID with a digit. Additionally, even though uppercase letters are permitted in a component-ID, it is strongly encouraged to only use lowercase letters for the ID.

The ID must follow a reverse-DNS scheme, consisting of `{tld}.{vendor}.{product}`, for example `org.kde.gwenview` or `com.hugski.colorhug2`. Ownership of `{vendor}.{tld}` in the domain name system guarantees uniqueness of IDs.

To increase the uniqueness and to distinguish between different pieces of a software suite, it is suggested to append the type name to the component-id in these cases. For example, one can use `com.hugski.colorhug2` for the client tools to control hardware, and `com.hugski.colorhug2.firmware` for the runtime firmware files.

Note that the value of this tag must be *unique* across all distributions and software deployment platforms. In case it is not unique, distributors are expected to reject the conflicting components from inclusion into their metadata and notify the upstream projects about this issue.

> [!IMPORTANT]
> To ensures the greatest possible compatibility of an AppStream ID, it is recommended to replace any hyphens in the ID in all but the last segment of it with underscores, and prefix every leading digit of a segment with an underscore as well. Since the underscore is not a valid character in domain names, the uniqueness of the ID is kept. For example, the ID `org.7-zip.7-zip` could become `org._7_zip._7-zip`.

\<metadata_license/\>  
The `<metadata_license/>` tag indicates the content license that you are releasing the one metainfo XML file under. This is typically not the same as the project license. Omitting the license value will result in the metainfo data not being incorporated into metadata collections as used by Linux distributions. This tag is required for all metainfo files.

The value of this tag has to be one of the recognized SPDX license IDs for `<metadata_license/>` tags, or a simple SPDX expression (only `AND` and `OR` operators allowed) allowing the use of the metadata file under one of the recognized licenses.

We do recognize a set of [permissive](https://en.wikipedia.org/wiki/Permissive_software_licence) licenses that have been vetted for mutual compatibility. This is important in order to allow the metainfo metadata to be combined with arbitrary other data in one file. While copyleft licenses like the GPL are great for code, it is not feasible to test every copyleft license for mutual compatibility and compliance when combining metainfo metadata with other data into one larger assembly fully automatically.

Currently, the following licenses have been reviewed and can be used as metadata licenses:

- `FSFAP`

- `MIT`

- `0BSD`

- `CC0-1.0`

- `CC-BY-3.0`

- `CC-BY-4.0`

- `CC-BY-SA-3.0`

- `CC-BY-SA-4.0`

- `GFDL-1.1`

- `GFDL-1.2`

- `GFDL-1.3`

- `BSL-1.0`

- `FTL`

- `FSFUL`

The license codes correspond to the identifiers found at the [SPDX OpenSource License Registry](https://spdx.org/licenses/). For instance, `CC-BY-SA-3.0` corresponds to the license at [creativecommons.org/licenses/by-sa/3.0](https://creativecommons.org/licenses/by-sa/3.0/). If you are looking for the simplest license to use for your metadata, using the `FSFAP` license is suggested.

\<name/\>  
A human-readable name for this software component. For example, if the component ID was "libc", its name might be "GNU Standard C Library".

\<summary/\>  
A short summary of what this component does. If the component is "PackageKit", the summary could be "Provides a package-management abstraction layer". This element is translatable.

\<icon/\>  
The `<icon/>` tag describes the component icon. It is mostly used for GUI applications (component-type `desktop-application`). It can be of type `stock`, `local` or `remote`.

`stock` icons are loaded from the icon stock (the current or hicolor/locolor fallback themes). The icon name must not include any file-extension or path.

`local` icons are loaded from a file in the filesystem. They should specify a full file path. This icon type may have `width` and `height` properties. If targeting a hi-DPI screen, this icon type may have a `scale` property.

`remote` icons loaded from a remote URL. Currently, only HTTP/HTTPS urls are supported. This icon type should have `width` and `height` properties. If targeting a hi-DPI screen, this icon type may have a `scale` property.

The semantics of each property in the `<icon/>` tag are the same as for the `<icon/>` tag for catalog metadata. See [varlistentry_title](#tag-ct-icon).

\<description/\>  
A long description of this component. Some markup can be used.

Do not assume the format is HTML. This list contains all currently supported formatting options:

- Paragraph (`p`)

- Ordered list (`ol`), with list items (`li`)

- Unordered list (`ul`), with list items (`li`)

- Within paragraphs and list items, emphasis (`em`) and inline code (`code`) text styles are supported. The emphasis is commonly rendered in italic, while inline code is shown in a monospaced font.

- Nested lists are not supported

In MetaInfo files, this tag should be translated by-paragraph. For enumerations, items are translated individually as well, and not the whole enumeration block. This means that in a translated file, only `<p/>` and `<li/>` elements may carry an `xml:lang` property.

All text must be in paragraphs or list item elements - text that contained directly in a `description` element is not permitted.

\<categories/\>  
This tag can contain one or more `<category>` entries, describing the categories this software component is associated with. This tag is usually applied to components of type `desktop-application`, but can be used with any component. A list of valid category names can be found in the [Freedesktop menu specification](https://specifications.freedesktop.org/menu-spec/latest/category-registry.html). Example:

``` XML
<categories>
    <category>Game</category>
    <category>ArcadeGame</category>
</categories>
```

\<keywords/\>  
This tag can contain one or more `<keyword>` children, describing keywords for the component, to make it easier to find in a software center. For translated keywords in metainfo files, the individual `keyword` tags should be translated.

Example:

``` XML
<keywords>
  <keyword translate="no">IDE</keyword>
  <keyword>development</keyword>
  <keyword>programming</keyword>
  <keyword xml:lang="de">entwicklung</keyword>
  <keyword xml:lang="de">programmierung</keyword>
</keywords>
```

\<url/\>  
Defines web URLs for this component. There are several different URL types allowed:

homepage  
Should be a link to the upstream homepage for the component.

bugtracker  
Should point to the software's bug tracking system, for users to report new bugs.

faq  
Should link a FAQ page for this software, to answer some of the most-asked questions in detail, something which you cannot do in the component's description.

help  
Should provide a web link to an online user's reference, a software manual or help page.

donation  
URLs of this type should point to a webpage showing information on how to donate to the described software project.

translate  
URLs of this type should point to a webpage where users can submit or modify translations of the upstream project.

Typically this should be a link to the project page in Weblate, Transifex or Zanata, but could also be a link to an upstream-hosted wiki page describing how to send translations upstream.

contact  
URLs of this type should allow the user to contact the developer.

This could for example be an HTTPS URL to an online form or a page describing how to contact the developer.

vcs-browser  
URLs of this type should point to a webpage on which the user can browse the sourcecode.

contribute  
URLs of this type should point to a webpage showing information on how to contribute to the described software project.

\<launchable/\>  
This tag indicates possible methods to launch the software described in this component. It is allowed to appear multiple times in MetaInfo data.

The `<launchable/>` tag has a required `type` property indicating the system that is used to launch the component. The following types are allowed:

desktop-id  
The application can be launched via a desktop file. The value of the tag is a [desktop-file id](https://specifications.freedesktop.org/desktop-entry-spec/latest/file-naming.html#desktop-file-id).

In case a software component has multiple launchable entries, the software center might display a dialog to choose which entry to launch. If possible though, it should be avoided to add multiple `launchable` tags of type `desktop-id`.

service  
The software can be started, stopped, and monitored by the OS "init" facility, such as systemd. The value of the tag is a name that can be used with that facility, such as a systemd unit name.

Multiple `launchable` tags of type `service` are not alternatives to start the same service, but the component does contain multiple services that might all need to be started.

Only those services should be listed as launchables that the user is actually expected to start and stop manually. Services that are started/stopped indirectly via dependencies of other services should not be listed.

For systemd units, the services listed as launchables are expected to support enabling and disabling.

cockpit-manifest  
The software can be launched from the menus of the [Cockpit](https://cockpit-project.org) admin interface. The value of the tag is the name of a [Cockpit package](https://cockpit-project.org/guide/latest/packages.html).

url  
The application is a web site that is viewed through a browser. The value of the tag is a direct HTTP/HTTPS URL that the browser must navigate to.

Example:

``` XML
<launchable type="desktop-id">org.gnome.sysprof2.desktop</launchable>
```

\<releases/\>  
The `<releases>` tag contains multiple `release` children that themselves contain metadata about releases made for this software component. The release information XML is described in-depth in [Release Information](#sect-Metadata-Releases), examples for a valid `releases` tag with artifacts are also provided there.

Release information can be embedded in the component's metainfo file, following the XML description outlined in [Release Information](#sect-Metadata-Releases). Alternatively, it can also be split into its own metadata file as described in that section. In case of external metadata, a `releases` tag must still be present in the component's metainfo file, and must have a `type` property set to value `external` (if the `type` property is missing, a value of `embedded` is implicitly assumed for it).

In case of external metadata, the `releases` tag may also have an `url` property linking to a web location where the release XML can be found and updated separately from the main component metadata. An `url` property must not be present without `type` set to `external`.

Only HTTPS links are allowed for the web URL, and any `artifact` defined in a release description from an external website should not be trusted without further verification, as external release information can currently not be signed.

AppStream catalog metadata generators may choose to update the locally provided release information with the data from the web location provided by the URL in `url`. This allow projects to complete release localization after a release was made, or include further information that was not yet available directly at release time. The generated catalog XML data must be complete and must not contain references to external release information.

Example for a `releases` block that points to an external metadata file:

``` XML
<releases type="external" url="https://example.org/releases/org.example.myapp.releases.xml" />
```

> [!IMPORTANT]
> Please note that even if release data is external and also provided on a remote location, it also *must* be available locally, installed as a file into `/usr/share/metainfo/releases/%{cid}.releases.xml`. The local file may not contain all information (for example it may not have a complete release description or all translations), but basic data such as the released versions and their release dates should be present.
>
> It is an error to reference an external release data file, but not provide a local copy of it.

\<provides/\>  
The `provides` tag and its children describe the public interfaces this application provides. A public interface can be anything which other applications, which are not part of the upstream project, can access or reference. This includes binaries and libraries. Private interfaces should never be added to a `provides` tag.

A `provides` tag contains a number of children describing the type and name of the provided public interface items. It is suggested that the build system auto-generates this tag and its children. Currently allowed item types are listed below. If you miss something, [file a bug against AppStream](https://github.com/ximion/appstream/issues/new) so we can add the new type.

\<mediatype/\>  
Describes the media types (also known as MIME types) this software supports, meaning it can open, edit or otherwise handle them. This tag is especially useful for generic components and addon-type components. For applications, the metadata may automatically be fetched from their `.desktop` files by the distribution's metadata generator if a desktop-entry file is set as [varlistentry_title](#tag-launchable). Example:

``` XML
<provides>
    <mediatype>text/html</mediatype>
    <mediatype>image/jpeg</mediatype>
    <mediatype>application/rss+xml</mediatype>
 </provides>
```

\<library/\>  
Contains the name of a shared library placed in a publicly accessible library path, such as `/usr/lib`, `/usr/lib/<triplet>` or `/lib`. For example, for the `libappstream` library, the value for `library` would be `libappstream.so.1`.

\<binary/\>  
Name of a binary installed into a location in `PATH`.

\<font/\>  
Full name of a font provided by this component. See [Fonts](#sect-Metadata-Fonts) for more information.

\<modalias/\>  
A modalias glob representing the hardware types (for example USB, PCI, ACPI, DMI) this component handles. Useful for installing printer drivers or other USB protocol drivers for smartphones, firmware, and out of tree kernel drivers.

\<firmware/\>  
This provided element is described in detail for the `firmware` component type, where it is mandatory. Please see [varlistentry_title](#tag-firmware-provides) for more information.

\<python3/\>  
Name of a Python 3 module this component provides.

\<dbus/\>  
Contains the well-known name of a D-Bus service as its value. The type of the service must be specified using the `type` property of this tag. Allowed values are `user` and `system`.

Example:

``` XML
<provides>
  <dbus type="system">org.freedesktop.packagekit</dbus>
</provides>
```

\<id/\>  
Contains the component-ID of another software component. The presence of this tag indicates that the software component containing it is able to provide all functionality of the one referenced in the `<provides/> ↪ <id/>` tag.

This is useful in case a component-id had to be renamed in the past, e.g. because its domain-name changed.

\<requires/\>, \<recommends/\> & \<supports/\>  
The `requires` tag denotes an *absolute* requirement on a different entity. For example, a component can require certain hardware to be present, require a specific minimum kernel version, or another component to be installed first. If a requirement specified in a `requires` tag is not met, AppStream clients should prevent the installation of the particular software component.

If it is not essential that a certain requirement is met by the system, but just recommended to be available, a `recommends` tag should be used. In this case, AppStream clients should allow the installation of the software component, but may display a warning before allowing the installation. It is permissible, but not required, to prevent installation of software which does not have all items specified as `recommends` met on the system that it is installed to.

Components may also set a `supports` tag. This is an even weaker relation than `recommends`, and means the particular component can make use of certain hardware capabilities or other software if it is available, but will also be usable if it is not.

A `requires`, `recommends` or `supports` tag contains children describing the type, value and version relation of the required item. Each child can have a `version` and a `compare` property, to allow depending on a certain minimal version of the respective item. The `version` property contains the version to be compared against, while the `compare` property contains a two-letter code denoting how to compare the version of a present item with the version listed in the property. If no `compare` property is given, but a `version` property is found, AppStream implementations should implicitly assume a value of `ge` for comparison of the versions. The installed version is on the left side of the required version when comparing them. See [Version Comparison Algorithm](#sect-AppStream-Misc-VerCmp) for a description of the version comparison algorithm.

Possible two-letter codes for version comparisons are:

- `eq` - Equal to

- `ne` - Not equal to

- `lt` - Less than

- `gt` - Greater than

- `le` - Less than or equal to

- `ge` - Greater than or equal to

Please note that not all item types are valid for all relation types. Generally valid item types are listed below, with information as for which relation kins they are valid.

\<id/\>  
A relation to another software component. The value should be another component-ID. Example:

``` XML
<requires>
  <id version="1.0" compare="ge">org.example.my_software</id>
</requires>
```

Valid for: `requires`, `recommends`, `supports`

\<modalias/\>  
Check for specific hardware to be present via its modalias. The modalias may contain a wildcard expression. Example:

``` XML
<recommends>
  <modalias>usb:v1130p0202d*</modalias>
</recommends>
```

Valid for: `requires`, `recommends`, `supports`

\<kernel/\>  
Check for a specific kernel to be running on the system. The kernel name is the output of `uname -s`. Example:

``` XML
<requires>
  <kernel version="4.14" compare="ge">Linux</kernel>
</requires>
```

Valid for: `requires`, `recommends`

\<memory/\>  
Set a relation to the amount of physical memory (RAM) the system should have to run the software component. The memory size is set in MiB. You usually only want to use this with the `recommends` tag, because users might want to install the software on systems even if they have a lesser amount of memory compared to what would be ideal. Example:

``` XML
<recommends>
  <memory>2048</memory> <!-- recommend at least 2GiB of memory -->
</recommends>
```

Valid for: `requires`, `recommends`

\<firmware/\>  
Depend on a specific device firmware. The value of this tag should either be a name like `bootloader`, be empty to reference the firmware itself described by the `firmware`-type component this tag is contained in, or contain a GUID. This tag is commonly used and interpreted by the [LVFS](https://fwupd.org/). Example:

``` XML
<requires>
  <firmware compare="ge" version="0.1.2">6de5d951-d755-576b-bd09-c5cf66b27234</firmware>
  <firmware compare="ge" version="0.1.2"/>
  <firmware compare="ge" version="0.3.4">bootloader</firmware>
</requires>
```

Valid for: `requires`, `recommends`

\<hardware/\>  
Require, recommend or support a specific system hardware configuration. The value of this item is a [Computer Hardware ID (CHID)](https://docs.microsoft.com/en-us/windows-hardware/drivers/dashboard/using-chids) without any surrounding braces.

On Linux systems, the CHIDs of the system can be queried using the `sudo fwupdtool hwids` command.

This tag is commonly used and interpreted by the [LVFS](https://fwupd.org/) and fwupd tool. Example:

``` XML
<requires>
  <hardware>be6ab11f-af5f-572e-be18-84301d880764</hardware>
</requires>
```

Valid for: `requires`, `recommends`, `supports`

\<control/\>  
This item type can be used to indicate support for or require certain ways a user can control the software. This usually maps to certain methods of input. If multiples `control` tags with different values are found within a requires/supports block, only one of them needs to be satisfied on the system to mark an application as compatible. This means if `touch` and `pointing` are both supported as controls for an application-type component, a system that only has a mouse and no touchscreen will still be considered able to run the application. Valid values for this tag are:

- `pointing` - Input via mouse/cursors/other pointing devices is possible

- `keyboard` - Keyboard input is possible

- `console` - Control via a console / command-line interface

- `tablet` - Graphics tablet input

- `touch` - Input by touching a surface with fingers is possible

- `gamepad` - The component supports gamepads (any game controller with wheels/buttons/joysticks)

- `tv-remote` - Input via a TV remote (with arrow keys, number pad, other basic inputs) is supported.

- `voice` - The software can be controlled via voice recognition/activation

- `vision` - The software can be controlled by computer vision / visual object and sign detection

If a control type is *supported* (= in a `supports` block), it means the software supports the given method of user input. As long as one of the input methods is available on the system, the software can be used. Installation on systems without the given control may still be permitted, but the software may not be easily usable.

If a control type is *recommended* (= in a `recommends` block), it means the software prefers the given method of user input. The software may still be installed if the input control method is not available, but functionality may be severely degraded.

If a control type is *required* (= in a `requires` block), the same applies, but the software installer should refuse to install the software on devices which do not have at least one of the input methods. It is therefore advised to only use the `control` tag in `supports` and possibly `recommends` blocks, and avoid to use it in `requires`.

For certain component types, some permitted controls are implicitly assumed: For [desktop-application](#sect-Metadata-Application) and [web-application](#sect-Metadata-WebApplication) components, `pointing` and `keyboard` controls are assumed supported, unless explicit support is defined by the metadata author. For [console-application](#sect-Metadata-ConsoleApplication), control via `console` is assumed.

For any other, non-application-like component types, the `control` relation item is currently considered unsupported.

Example control support block:

``` XML
<supports>
  <control>pointing</control>
  <control>keyboard</control>
  <control>touch</control>
</supports>
```

Valid for: `requires`, `recommends`, `supports`

\<display_length/\>  
Set a relation to the display length defined as an integer value in *logical pixels* (device pixels divided by scaling factor, roughly equivalent to 0.26mm (1/96in), also known as device-independent pixels). Setting the `side` property to either `shortest` or `longest` will apply the selected size constraint to either the shortest or longest side of the display rectangle, with `shortest` being implicitly assumed if no value is set.

> [!NOTE]
> One logical pixel (= device independent pixel) roughly corresponds to the visual angle of one pixel on a device with a pixel density of 96dpi and a distance from the observer of about 52cm, making the physical pixel about 0.26mm in size. When using logical pixels as unit, they might not always map to exact physical lengths as their exact size is defined by the device providing the display. They do however accurately depict the maximum amount of pixels that can be drawn in the depicted direction on the device's display space.

Relations for the display length can be defined using a `compare` property as described in [varlistentry_title](#tag-relations). If this property is not present, a value of `ge` (greater-or-equal) is implicitly assumed.

> [!NOTE]
> Please note that a display with a lot of vertical space may not be a television screen, but could also be a large gaming monitor. Similar logic applies to the smaller screen sizes. Therefore, to indicate that an application runs well on a certain *device* and not just on a certain *display*, additional metadata is needed, like the application's supported input controls as defined via [varlistentry_title](#tag-relations-control).

> [!NOTE]
> The sizes below are for reference if you do not know the exact dimensions your application will fit into, and just need a rough guideline as to what device type you can expect at a given size:
>
> - Very small screens, as used in watches, wearables and other small-display devices: about \<= 360px
>
> - Small screens often used in handheld devices, such as phone screens, small phablets: about \< 768px
>
> - Screens in laptops, tablets: about \>= 768px
>
> - Bigger computer monitors: about \>= 1024px
>
> - Television screens, large projected images: about \>= 3840px

This tag may appear up to four times to set a minimum and maximum dimension required. If multiple displays are connected to a device, it is acceptable to test against either the largest screen attached to the device, or the combined amount of display space (depending on what makes the most sense for the respective device / setup). A software center application may test for the maximum possible resolution of an attached display, and not the currently set display resolution in case it wants to check against hardware capability and not be influenced by user configuration.

If used in a `requires` block, this relation can be used to restrict an application to only be installable on systems which have a minimum usable display length available for it. If used in a `recommends` block, the application will still be installable, but the user may be shown a warning.

If no `display_length` relation is present, a minimum required display (`ge`) relation of `768px` is implicitly assumed to preserve backwards compatibility (so applications capable of running on smaller screens need to make their support for that configuration explicit).

Examples:

``` XML
<!-- recommend at least 600 logical pixels of space -->
<recommends>
  <display_length compare="ge">600</display_length>
</recommends>

<!-- ensure this application is not run on a very large screen, or
     very small screen (no tiny handhelds or television screens) -->
<requires>
  <display_length compare="lt">3840</display_length>
  <display_length compare="gt">360</display_length>
</requires>
```

Valid for: `requires`, `recommends`

\<internet/\>  
Require, recommend or support connectivity to the internet. The value of this item one of the following:

- `always` - Needs internet connectivity to work. If used in a `recommends` element, then this indicates that the app can work without internet, but the experience will be degraded.

- `offline-only` - Never uses the internet, even if it’s available.

- `first-run` - Uses the internet the first time the application is run, but not normally afterwards.

If the value of `<internet/>` is not `offline-only`, the `bandwidth_mbitps` attribute can be set to a bandwidth (in Mbit/s) which is the minimum internet bandwidth needed for the application to be usable. If this attribute is not set, it’s assumed that the application is usable with all internet connections.

Examples:

``` XML
<!-- always needs the internet -->
<requires>
  <internet>always</internet>
</requires>

<!-- always needs the internet and has a degraded experience if it’s not at least 2Mbit/s -->
<requires>
  <internet bandwidth_mbitps="2">always</internet>
</requires>

<!-- never uses the internet, even if available -->
<requires>
  <internet>offline-only</internet>
</requires>

<!-- the software explicitly supports running offline (but may also be able to use online features) -->
<supports>
  <internet>offline-only</internet>
</supports>

<!-- requires the internet on first run -->
<requires>
  <internet>first-run</internet>
</requires>

<!-- can work without the internet, but with a degraded experience -->
<recommends>
  <internet>always</internet>
</recommends>

<!-- recommends the internet for when it’s first run, but can work without -->
<recommends>
  <internet>first-run</internet>
</recommends>

<!-- requires the internet on first run, can run without it afterwards but with a degraded experience -->
<requires>
  <internet>first-run</internet>
</requires>
<recommends>
  <internet>always</internet>
</recommends>
```

Valid for: `requires`, `recommends`, `supports`

\<replaces/\>  
The `replaces` tag denotes indicates that the given component completely replaces another one on the system. In most cases, the replaced component and the one that replaces it can not be coinstalled. Compared to a [varlistentry_title](#tag-provides) ↪ `id` relationship, for a replaced component there is no common interface that two components can provide at once.

A `replaces` tag has `id` children which have the component-IDs of the components that the current component replaces as value.

This feature is usually used for components that have to change their ID. While metainfo data may contain `replaces` tags, software repository providers should filter these tags carefully to ensure that the new component has the right to replace an old one.

Example:

``` XML
<!-- the 7-zip application changes its ID and therefore replaces the component with its old ID -->
<id>org._7_zip._7zip</id>
[...]
<replaces>
  <id>org.7-zip.7zip</id>
</replaces>
```

\<mimetypes/\>  
This tag can contain one or more `<mimetype/>` children, describing the MIME types this application supports.

> [!IMPORTANT]
> This tag is deprecated and should not be used for new metadata. Please use [varlistentry_title](#tag-provides) ↪ `mediatype` tags instead.

\<project_group/\>  
If you include the `<project_group/>` tag then this identifies your project with a specific upstream umbrella project. Known values include `GNOME`, `KDE`, `XFCE`, `MATE` and `LXDE`, although other umbrella projects like Yorba or Mozilla make sense too.

> [!NOTE]
> You should only identify with an umbrella project if you use *all* their infrastructure and policies, for instance string freezes dates, bugtracker and source control instance.

\<compulsory_for_desktop/\>  
The `<compulsory_for_desktop>` tag indicates that the component which the metadata belongs to is essential for the functionality of the defined desktop environment. Examples for compulsory components are the `GNOME Shell` by the GNOME Project, or the `Plasma Desktop` by KDE, as well as things like `iBus` or the desktop login manager.

Software centers are expected to detect the running desktop environment and disable uninstallation for compulsory components of that desktop, so users will not be able to damage their currently running, primary desktop environment.

Multiple occurrences of the `<compulsory_for_desktop>` tag are allowed, so a project can be essential for many desktops. The distributor decides which components should be made compulsory, however it is generally a good idea to follow upstream's recommendations on that matter.

A list of all allowed values for this tag is defined in the [XDG Menu Specification](https://specifications.freedesktop.org/menu-spec/latest/onlyshowin-registry.html). Software center applications will only recognize these values.

\<project_license/\>  
The `<project_license/>` tag is indicating the license of the component (application/library/addon/font/etc.) described in the metadata document. It should be an [SPDX license expression](https://spdx.org/specifications). Please note the SPDX license IDs are case-sensitive in AppStream. Possible values include:

- `GPL-2.0`

- `LGPL-3.0+ AND GPL-3.0+`

- `MIT`

- `CC-BY-SA-2.0`

- `LicenseRef-proprietary=https://example.com/mylicense.html`

A full list of recognized licenses and their identifiers can be found at the [SPDX OpenSource License Registry](https://spdx.org/licenses/).

Custom licenses which are not in the SPDX registry, like proprietary licenses, can be denoted using the `LicenseRef` notation. `LicenseRef-proprietary` can be used to denote a proprietary license, with an optional URL to the license text following after a `=` sign.

The license given in the `project_license` tag should be the ‘main’ license of the project. For a software project, this is typically the license for the code. It is not recommended to include the license for accompanying documentation (for example) in `project_license`, as that could confuse users. In particular, the `CC-BY-SA-3.0` license which is commonly used for documentation is not an (FSF or OSI) approved license for free software, so including it in `project_license` results in the project as a whole being considered non-free.

Although the `project_license` tag is not mandatory, it is highly recommended to include it.

Examples:

``` XML
<project_license>LGPL-3.0+ OR MPL-2.0</project_license>
<project_license>LGPL-3.0+ OR MPL-2.0</project_license>
<project_license>GPL-3.0-or-later</project_license>
<project_license>LicenseRef-proprietary=https://code.visualstudio.com/license</project_license>
```

\<developer/\>  
The `<developer/>` element is designed to represent the developers or project responsible for development of the project described in the metadata. It must appear only once per component.

The element should have a `id` property, containing a unique ID to identify the component developer / development team. It is recommended to use a reverse-DNS name, like `org.gnome` or `io.github.ximion`, or a Fediverse handle (like `@user@example.org`) as ID to achieve a higher chance of uniqueness.

A `developer` element must have one `name` tag as child, which contains a translatable name for the component developer or development team. Values might be for example "The GNOME Foundation" or "The KDE Community". Hyperlinks or emails must not be used in the name; if you want to link to the developer's homepage, use the [varlistentry_title](#tag-url)-tag instead. The `name` tag is translatable, it must only exist once in its untranslated form.

\<developer_name/\>  
The `<developer_name/>` tag is designed to represent the developers or project responsible for development of the project described in the metadata.

> [!IMPORTANT]
> This tag is deprecated and should not be used for new metadata. Please use [varlistentry_title](#tag-developer) instead.

\<screenshots/\>  
Visual components (like fonts or graphical applications) may choose to add one or multiple screenshots to their metadata. Screenshots can be either a video or a static image.

The `<screenshots/>` tag contains multiple `<screenshot/>` children, where at least one of them must have the property `type="default"` to indicate the primary and most representative screenshot of the software.

Optionally, a `screenshot` may also have an `environment` property. This string property denotes the GUI environment the screenshot was recorded in, in the form of `{env}:{style}`, where `{env}` is a desktop-environment name in lowercase and `{style}` is a specific style that the desktop environment recognizes, e.g. `light` and `dark` for light and dark themes. The `:{style}` part of the environment property may be omitted if the environment's default style is used. See [desktop-style-ids.txt](https://github.com/ximion/appstream/blob/main/data/desktop-style-ids.txt) for a list of currently recognized environment and style combinations.

Software centers displaying the component will usually prefer screenshots of the current environment and style, and display them first, even before the screenshot marked as `default`.

In general, screenshots should be displayed in the order the are defined in in their `screenshots` block for the respective component on a per-environment basis (all screenshots of the same environment/style will be displayed in the order they are listed in the XML, but may be moved to the front of the list as a whole depending on the current environment).

Every `<screenshot/>` element must have at least one `<image/>` *or* `<video/>` child, but never an `image` *and* `video` at the same time.

Screenshots containing videos must not be the default screenshot.

The value of the `<image/>` tag is a direct HTTP/HTTPS URL to a screenshot uploaded to a public location on the web. Images should ideally be provided in the PNG format; using JPEG or WebP is also permitted for images in metainfo files.

The `<image/>` tag may have the following properties:

- `type`

  The type of the image: `source` for the source image, and `thumbnail` for a thumbnail image. In case the type is `thumbnail`, the `width` and `height` properties must be present.

- `width`

  The width of the image in pixels.

- `height`

  The height of the image in pixels.

- `scale`

  A scaling factor for the image, if it is intended for a HiDPI display. If a scaling factor \> 1 is set, the `width`/`height` values are not adjusted to scale. They always represent the exact image dimensions in pixels.

- `xml:lang`

  The language this screenshot image is translated in. This property should only be present if there are multiple images with different locales present.

The value of the `<video/>` tag is a direct HTTP/HTTPS URL to a video uploaded to a public location on the web. The video must be in a [Matroska (.mkv)](https://www.matroska.org/) or [WebM](https://www.webmproject.org/) container and use either the [VP9](https://www.webmproject.org/vp9/) or [AV1](https://aomedia.org/av1-features/) codec. The video should ideally work without any audio, but if audio is needed, the [Opus](https://opus-codec.org/) codec should be used. Software centers may still play the video without any sound though. Additionally, AppStream metadata repositories (like in distributions such as Fedora and Debian) may impose size limitations to video files delivered by their CDN, so it is recommended to keep the video file size below 10MiB. There is also a chance that software centers do not display any video at all, so a video must never be in a default screenshot.

The `<video/>` tag may have the following properties:

- `container`

  The video container that is used, can be `webm` or `matroska`.

- `codec`

  The video codec used, can be `av1` or `vp9`.

- `width`

  The width of the video in pixels.

- `height`

  The height of the video in pixels.

- `xml:lang`

  The language this video is translated in. This property should only be present if there are multiple videos with different locales present.

Optionally, a `<screenshot/>` tag may have a translatable `<caption/>` child, defining a short (ideally not more than 100 characters) description of what the user can see on the referenced screenshot.

A `source` video should be concise, easy to understand and not have an overly large file size. Try to use a reasonably large image for `source` images, as they may be scaled down to `thumbnail` images in metadata processing. It is suggested to have videos and images in 16:9 aspect ratio, as long as that is sensible for the displayed application.

Example:

``` XML
<screenshots>
  <screenshot type="default">
    <caption>The FooBar main window.</caption>
    <image type="source" width="1600" height="900">https://example.com/foobar/screenshot-1.png</image>
  </screenshot>
  <screenshot>
    <caption>Foobar showing the frobnicate functionality.</caption>
    <image type="source" width="1600" height="900">https://example.com/foobar/screenshot-2.png</image>
  </screenshot>
  <screenshot>
    <video codec="av1" width="1600" height="900">https://example.com/foobar/screencast.mkv</video>
  </screenshot>

  <screenshot environment="plasma-mobile">
    <caption>The FooBar main window, but on Plasma Mobile</caption>
    <image type="source" width="1600" height="900">https://example.com/foobar/screenshot-1_plasma-mobile.png</image>
  </screenshot>

  <screenshot environment="gnome:dark">
    <caption>The FooBar main window, on GNOME in dark mode</caption>
    <image type="source" width="1600" height="900">https://example.com/foobar/screenshot-1_gnome_dark.png</image>
  </screenshot>
 </screenshots>
```

\<translation/\>  
The `<translation/>` tag is an optional tag which can be added to specify the translation domain used for this software component. It may be used by the AppStream distro metadata generator to determine the translation status of the respective software (e.g. which languages the software is translated into and how complete the translations are).

The tag must have a `type` property, assuming the value of the translation system which is used. Right now, allowed translation systems and values for `type` are:

- `gettext`

- `qt`

In case a software components gets its translation from multiple translation domains, the `<translation/>` tag may be defined more than once.

The source strings in the component are assumed to be in the `en_US` locale. If that is not the case, specify the source locale in POSIX format using the `source_locale` attribute on the `<translation/>` tag. The metadata generator will use the source locale to synthesize a `<lang/>` tag for the source locale, with 100% translation.

For Gettext translations, localization data will be looked for in `${prefix}/share/locale/${locale}/LC_MESSAGES/${id}.mo`, where `${id}` is replaced with the translation domain specified in the `<translation/>` tag. For Qt translations, if the ID string contains slashes, we will look for translations following either the `${prefix}/share/${id}_${locale}.qm` or the `${prefix}/share/${id}/${locale}.qm` pattern. If no slashes are contained, we will look for translation data in `${prefix}/share/locale/${locale}/LC_MESSAGES/${id}.qm`.

Example:

``` XML
<translation type="gettext">foobar</translation>
<translation type="gettext" source_locale="de_DE">foobar</translation>
<translation type="qt">FooBar/translations/foobar</translation>
```

\<suggests/\>  
The `<suggests/>` tag is an optional tag which can be added to specify the component-ids of other software this components suggests. Software centers might present the suggested software on the installation page of the described component.

The tag may have a `type` property, with the value `upstream`, indicating that this suggestion originates from the upstream project. If no `type` property is given, `upstream` is implicitly assumed as value. Metainfo files must not define other `suggests` types, those are reserved for AppStream catalog XML (see [varlistentry_title](#tag-ct-suggests) in catalog XML).

The `suggests` tag must have one or more `<id/>` tags as children, specifying the IDs of the suggested other software components.

Example:

``` XML
<suggests>
  <id>org.kde.gwenview.desktop</id>
  <id>org.inkscape.inkscape</id>
</suggests>
```

\<content_rating/\>  
The `<content_rating/>` tag is an optional tag which can be added to specify age ratings for the respective software components. These maybe be used for parental control or to display their information in software centers.

The tag must have a `type` property, indicating the type of the rating system that is used. At the moment, the [Open Age Ratings Service](https://hughsie.github.io/oars/) (value `oars-1.0`) is supported natively, but more services might be added in future.

The `<content_rating/>` tag may have `<content_attribute/>` children which each must have an `id` property indicating the specific section that is rated. Their value indicates the intensity of the rated section and can be one of:

- `none` - no rating given

- `mild`

- `moderate`

- `intense`

In case the `<content_rating/>` tag is empty (no `<content_attribute/>` is present), it is assumed that the component was checked for age ratings and no age restrictions apply.

The website of the Open Age Ratings Service provides [an online form](https://hughsie.github.io/oars/generate.html) which will automatically generate AppStream compatible metadata based on a set of questions answered about the content.

Example:

``` XML
<content_rating type="oars-1.0">
  <content_attribute id="drugs-alcohol">moderate</content_attribute>
  <content_attribute id="language-humor">mild</content_attribute>
</content_rating>
```

\<agreement/\>  
The `<agreement/>` tag is an optional tag which can be added to specify agreements the user has to accept or acknowledge before using the software. This tag can appear multiple times, if multiple agreements are required for a software component.

The tag should have a `type` property, indicating the type of the agreement. If the `type` property is missing, an agreement of type `generic` is assumed. Currently recognized agreement types are:

- `eula` - an end-user license agreement the user has to accept before installing the software.

- `privacy` - a privacy statement for the software, usually a [GDPR](https://www.eugdpr.org/) compliant statement

The `<agreement/>` tag must have a `version_id` property, containing a version identifier for the license. It may be used by client applications to determine whether an agreement needs to be shown again after it has been accepted already by the user.

Every `<agreement/>` must have `<agreement_section/>` children which each have an `id` property indicating the specific section that they describe (e.g. `introduction`). These values may be used to automatically jump to a specific section. Each `<agreement_section/>` has a translatable `name` child denoting the name or title of the respective section, and a `description` child that is translated according to the same translation rules that apply to the [varlistentry_title](#tag-description) tag. The `description` contains the content of the respective agreement section.

Example:

``` XML
<agreement type="privacy" version_id="1.0">
    <agreement_section id="introduction">
      <name>Introduction</name>
      <description>
        <p>
          We hold personal data about vendors, administrators, clients and other
          individuals for a variety of purposes.
          [...]
        </p>
      </description>
    </agreement_section>

    <agreement_section id="scope">
      <name>Scope</name>
      <description>
        <p>
          This policy applies to all users who have access to any of the personally
          identifiable data.
        </p>
      </description>
    </agreement_section>

    [...]
</agreement>
```

\<update_contact/\>  
The `<update_contact/>` tag is an optional tag which can be added to provide an email address distributors can use to contact the project about invalid or incomplete metadata or – in case the specification has changed – about old metadata. It can also be used to ask general questions in case of an update of the component described in the metadata file.

The `<update_contact/>` tag must *only be used by distributors*. It is not included in the distribution-provided AppStream XML file, and therefore not exposed to the end user via any kind of UI.

Upstream authors might decide to add an email address in cleartext, but spam protection using `_AT_` is also valid. The value of this tag is generally treated a case-insensitive way.

Example:

``` XML
<update_contact>developer_AT_example.com</update_contact>
```

\<name_variant_suffix/\>  
Variant suffix that software centers may append to the component name on lists in case multiple components have the same name. This is currently primarily used for firmware, where components only need to be distinguished if multiple variants are displayed. A name variant suffix could e.g. be 'Prerelease' or 'China'.

\<branding/\>  
The `<branding/>` tag is an optional tag which defines properties affecting the branding and presentation of the component. It usually affects how the component is displayed in software centers and on websites.

The tag may currently only contain `color` tags as children, defining accent colors for the component. Each `color` element contains an HTML hexadecimal color string as its value. This string must start with a `#` character. An accent color may for example be used as the background behind the logo/icon of an application.

A `color` tag must have a `type` attribute which denotes the color type. The color type may currently only be `primary`. A `color` tag may have an optional `scheme_preference` attribute which denotes a preference for a particular color scheme where this color should be used over other colors. Values for this attribute may either be `light` or `dark` for a light or dark theme preference. Each color type/scheme combination may only appear once.

Example:

``` XML
<branding>
  <color type="primary" scheme_preference="light">#ff00ff</color>
  <color type="primary" scheme_preference="dark">#993d3d</color>
</branding>
```

\<tags/\>  
The `<tags/>` tag is an optional tag which can be used to give the component one or multiple arbitrary labels. For example, it can be used for apps to tag themselves as "featured" in specific software centers, or to group software together by some well-defined criteria.

The interpretation of tags is completely defined by the client application that is reading AppStream metadata. Tags defined in metainfo files may be filtered by catalog metadata generators, and may even be completely ignored by clients. Components must not rely on the presence of specific tags to behave correctly.

The `tags` tag must have `tag` children which must have a value comprised only of lower-case ASCII characters, dots, hyphens and numbers. Spaces are not allowed. The tag must also have a `namespace` attribute to designate a namespace where the particular tag is valid. The namespace is an arbitrary string which has the same character limitations as the tag value. It may for example be the name of the client too that consumes the data, or the name of the organization the tag belongs to.

Example:

``` XML
<tags>
  <tag namespace="lvfs">vendor-2021q1</tag>
  <tag namespace="plasma">featured</tag>
</tags>
```

\<references/\>  
The `<references/>` element is an optional tag to indicate references to this component in other registries. This is primarily used for scientific registries, citation information and DOI ([Digital Object Identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)) associations.

This information is primarily consumed by specialized tools, but may also be shown by software centers or read by the applications themselves to compose references.

The `references` element may have `doi` children containing DOI identifier strings as value, `citation_cff` children containing a link to a citation file in CFF ([Citation File Format](https://citation-file-format.github.io/)) format or `registry` children. A `registry` child must have a `name` property containing the name of a registry referencing this component, while the value of it must be the identification string in the respective registry.

Example:

``` XML
<references>
  <doi>10.1000/182</doi>
  <registry name="SciCrunch">SCR_000000</registry>
  <citation_cff>https://example.org/CITATION.cff</citation_cff>
</references>
```

\<custom/\>  
The `<custom/>` tag is an optional tag which can be used as a key-value store for custom values that are not covered by the AppStream specification. The tag is usually stripped out or filtered by catalog metadata generators, such as `appstream-generator`. When present, the data contained in a `custom` can be read by all tools making use of AppStream metadata, making it an ideal extension point when using an existing AppStream library is desired and some custom additions to the metadata are still required. The `custom` tag is also often used for prototyping new features in AppStream.

The tag must have `value` children which must have a `key` property. The value of the `value` tag denotes a user-defined value, while the key string set for the `key` property denotes a user-specified key string. The key must be unique; multiple keys with the same name are not allowed.

To avoid name conflicts, it is recommended to prefix keys with a vendor prefix, like `GNOME::` or `KDE::`.

> [!NOTE]
> Before using a `custom` tag, please consider if there is a better way to achieve your goal than adding the data to the AppStream metainfo file, or whether AppStream maybe already contains a way to achieve what you want. Additionally, if you think that the purpose you use the `custom` tag for is generally useful, please file a feature request against AppStream, so we can discuss adding the new feature to the specification and make it more usable for a bigger audience.

Example:

``` XML
<custom>
  <value key="MyCorp::app_color">#FF0000</value>
  <value key="MyCorp::special_id">284fd262-6870-42a6-89a4-b189d3109e3e</value>
</custom>
```

An example for a very basic component file could look like this:

``` XML
<?xml version="1.0" encoding="UTF-8"?>
<component>
  <id>com.example.foobar</id>
  <name>Foo Bar</name>
  <summary>A foo-ish bar</summary>
  <url type="homepage">https://www.example.org</url>
  <metadata_license>CC0-1.0</metadata_license>

  <provides>
    <library>libfoobar.so.2</library>
    <font>foo.ttf</font>
    <binary>foobar</binary>
  </provides>
  <releases>
    <release version="1.2" date="2015-02-16" />
  </releases>
  <developer id="org.example">
    <name>FooBar Team</name>
  </developer>
</component>
```

For a component of type `generic`, the minimal amount of required tags is: [varlistentry_title](#tag-id-generic), [varlistentry_title](#tag-name), [varlistentry_title](#tag-summary), [varlistentry_title](#tag-metadata_license).

## Release Information

### Introduction

This section documents the [varlistentry_title](#tag-releases) tag that can be part of a `component` to provide information about releases made for the respective component.

Alternatively to being embedded in a component metainfo file, the data may also be split into a dedicated XML file to be updated separately.

### Locations

Release data may be present directly in a component metainfo file, but also optionally be split out into an external metadata file.

If the `releases` XML is part of a metainfo file, it is embedded into it following the semantics described in the document.

If the `releases` XML is external, the metainfo file must contain a [varlistentry_title](#tag-releases) tag with the `type` property set to `external` as described for component XML. The data described in this section is placed in a separate XML file with `releases` being its root node. The file must be installed as `/usr/share/metainfo/releases/%{cid}.releases.xml`, where `cid` is the component ID of the component the release information belongs to.

### Example data

Release information may look like this:

``` XML
<releases>
  <release version="1.2" date="2014-04-12" urgency="high">
    <description>
      <p>This stable release fixes bugs.</p>
    </description>

    <url>https://example.org/releases/version-1.2.html</url>

    <issues>
      <issue url="https://example.com/bugzilla/12345">bz#12345</issue>
      <issue type="cve">CVE-2019-123456</issue>
    </issues>

    <artifacts>
      <artifact type="binary" platform="x86_64-linux-gnu">
        <location>https://example.com/mytarball.bin.tar.xz</location>
        <checksum type="sha256">....</checksum>
        <checksum type="blake2b">....</checksum>
        <size type="download">12345678</size>
        <size type="installed">42424242</size>
      </artifact>
      <artifact type="binary" platform="x86_64-windows-msvc">
        <location>https://example.com/mytarball.bin.exe</location>
      </artifact>
      <artifact type="source">
        <location>https://example.com/mytarball.tar.xz</location>
        <checksum type="sha256">....</checksum>
      </artifact>
    </artifacts>
  </release>
  <release version="1.1" type="development" date="2013-10-20" />
  <release version="1.0" date="2012-08-26" />
</releases>
```

### Releases tag specification

The `<releases>` tag contains `<release/>` children which contain metadata about individual releases of a component. Each release of the software component should ideally have a `<release/>` tag describing it, but at least one `release` child is recommended to be present for the current release of the software. The `release` children must be sorted in a latest-to-oldest order to simplify reading the metadata file.

A `release` tag can have the properties `version`, `date` and `timestamp`. The `date` property can have any time in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format as its value and should be present for every release. At least day-level granularity is required, which means that the ISO 8601 string must contain at least a full date (e.g. 2020-08-12). The `timestamp` tag contains the release time in the form of a UNIX epoch. This tag should not be used in metainfo files in newly written metadata, but will still be parsed in case it is present. The `timestamp` property is mainly used in generated distro-metadata. In case both release-time tags are present, the `timestamp` tag will take precedence over `date`.

The algorithm used for comparing release version numbers is described at [Version Comparison Algorithm](#sect-AppStream-Misc-VerCmp).

A `release` tag may also have a `date_eol` property that denotes the date when the release stops to receive support from the software developers (end-of-life). Its value can be any complete date or time in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601).

Optionally, the `<release/>` tag may also have an `urgency` property, having one of the following values:

- `low`

- `medium`

- `high`

- `critical`

The `urgency` defines how important it is to install the new release as an update. This is especially important for `type=firmware` components. If no urgency is defined, a `medium` urgency is implicitly assumed. The urgency defines how the update will be presented to the user, and sometimes if it will be installed automatically and immediately, or delayed.

A `release` tag may have a `type` property to classify releases with one of the following values:

- `stable`

- `development`

- `snapshot`

By default, if no release type is defined, `stable` is assumed. A software displaying a listing of releases should only show stable releases and discard any development release if the current version is itself stable. It can show both `stable` and `development` versions when development versions of the software are also distributed. Instead, a `snapshot` release identifies an automated snapshot of the current development status. It should not be shown unless instructed to.

The `release` itself may have the following children:

\<description/\>  
A `description` tag contains a brief description of what is new in the release. The intended audience of the description are the users of the component (who are typically not developers), and so the description should mention only the user visible changes in the release. The `description` tag supports child tags as described in [varlistentry_title](#tag-description).

Descriptions must not contain embedded web links to issue trackers or bug reports, as these typically make no sense to users. If particular issues need to be highlighted (for example, CVEs fixed in this release), they should be listed in the `issues` tag.

\<url/\>  
The `url` tag must point to a web location containing additional information (usually detailed release notes) about this particular release. The `url` tag may have a `type` property with `details` as the only currently allowed value. If the `type` is missing, a URL type of `details` is implicitly assumed.

\<issues/\>  
The `issues` tag contains `issue` children defining issues resolved by this release. It is used most commonly to mention [CVE](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures) IDs. Software which is interpreting the release notes for the component should present the list of issues separately from the release description. They should not be thought of as a bullet-point list of issues which follow straight on in prose from the `description` element’s value.

The value of an `issue` tag must be the bug number, ticket name, or CVE ID and is typically displayed to the user, but may also in case of CVE IDs be read by machines. The content of an `issue` element is not translatable, but can be a string appropriate for the project's bug tracker.

The `issue` tag may have a `type` property, which should have a value of `generic` or `cve`. If the `type` property is missing, a type of `generic` is assumed.

It may also have a `url` property, which should be a URL for a details page on the respective issue.

If `type` is `cve`, the element’s value must be a CVE ID in the [format defined by MITRE](https://www.cve.org/About/Process#cve-id). For example, `CVE-2023-12345`. Software consuming the release data of a component should be able to append the element’s value to `https://nvd.nist.gov/vuln/detail/` to get a page of information about the CVE. If a `url` property is given, its value overrides any URL constructed from the CVE identifier. The `url` property is optional if `type` is `cve`.

For example:

``` XML
<issue url="https://example.com/bugzilla/12345">bz#12345</issue>
```

If `type` is `generic` or unspecified, the element’s value is a free-form issue identifier, and the `url` property must be specified. The issue identifier should be shorthand for an issue in the project’s bug tracker, and it does not have to be globally unique. It should be human readable, but does not have to be appropriate for non-technical audiences.

For example:

``` XML
<issues>
  <issue type="cve">CVE-2021-28153</issue>
  <issue url="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-27218">CVE-2021-27218</issue>
</issues>
```

\<artifacts/\>  
The `artifacts` child tag contains information about downloadable release artifacts. It itself contains the artifacts as `artifact` children. Each artifact tag must have a `type` property with the value of either `binary` or `source` to indicate whether the artifact is the releases' source-code or a binary distribution.

In case of a `binary` type, an optional `platform` property may also be set, containing a platform triplet (also known as normalized GNU triplet), such as `x86_64-linux-gnu`. Refer to [Debian multiarch tuples](https://wiki.debian.org/Multiarch/Tuples#Used_solution) for more information on normalized GNU triplets, and [AppStream's platforms.yml](https://github.com/ximion/appstream/blob/master/data/platforms.yml) for the triplet parts AppStream currently recognizes. Note that AppStream only supports strictly three-part triplets in the form of `arch-oskernel-osenvironment`. Parts of the triplets which do not apply can be replaced with `any`.

Binary artifacts may also have a `bundle` property to indicate the bundling system the binary distribution is made for. Refer to the bundle types in [varlistentry_title](#tag-ct-bundle) for a list of possible values. Each `artifact` can have a number of children:

location  
Each artifact must have a `location` child, denoting the web location (HTTP or HTTPS) where it can be downloaded from. Multiple location tags are allowed to make it possible to have mirror options to download the same artifact from.

checksum  
At least one `checksum` child must be present to contain the checksum of the released artifact. The `<checksum/>` tag has a `type` attribute, containing the name of the hash function that was used to create it. Currently aupported values (and hash sums) are: `sha1`, `sha256`, `sha512`, `blake2b` and `blake3`. For most purposes (on 64-bit machines), using [BLAKE2b](https://blake2.net) via `cksum -ablake2b [FILE]` from GNU Coreutils is a good choice.

size  
One or multiple `size` tags may also be present, which define the installed and download size of this component release artifact. The size type is defined via a `type` property on the `size` tag, and may assume the value `download` or `installed`. The size itself is set as the value and must be given in bytes.

filename  
An artifact may have a `filename` child, containing a non-absolute filename that the artifact may be stored under. The file name is only a naming hint and applications are not required to follow it when downloading the file. If no `filename` tag is present, a file name may be generated from the artifact `location` URL. This tag must only appear once.

\<tags/\>  
The `tags` element can be used to tag releases with user-defined tags. It follows the same semantics as the one for components, as described in [varlistentry_title](#tag-tags).

## Desktop Applications

### Introduction

A desktop application is interactive software that presents a graphical interface to the user. To appear in menus, the desktop application must include a [Freedesktop `.desktop`](https://specifications.freedesktop.org/desktop-entry-spec/latest/) file.

AppStream generators may pull data from the preexisting `.desktop` files to represent an application in the AppStream metadata pool. Upstream projects should ship a metainfo file containing additional metadata to describe their application though, to enhance the available metadata. This data includes things like screenshots, long descriptions, icon information and various other things needed to present the application properly to the user. For some distributions, the presence of this metadata is a prerequisite for the application showing up in the metadata pool and being presented in software centers.

The file described in this document is built upon the generic component metadata with fields specific for desktop applications (see [Generic Component](#sect-Metadata-GenericComponent)).

The metainfo files override any values which are automatically fetched from other sources by the AppStream data generator, which means that its data will always take precedence over data which has already been defined in a `.desktop` file. Applications can ship one or more files in `/usr/share/metainfo/%{id}.metainfo.xml`.

Data will only be fetched from a desktop file if one [varlistentry_title](#tag-dapp-launchable) tag is present to define a .desktop file ID. If multiple `launchable` tags are defined, no data will be merged in from .desktop files.

> [!NOTE]
> If you are looking for some quickstart guide to just get your application to ship AppStream metadata quickly, this document might not be for you. You might want to take a look at [For GUI application upstream maintainers](#sect-Quickstart-DesktopApps) instead.

> [!NOTE]
> While `desktop-application` metadata is commonly stored in `/usr/share/metainfo/%{id}.metainfo.xml` (with a `.metainfo.xml` extension), using a `.appdata.xml` extension is also permitted for this component type for legacy compatibility. AppStream implementations will recognize either file type, as long as it ends up in the right location on the filesystem.

> [!NOTE]
> If you want to hide a desktop-entry file from AppStream metadata generators which synthesize components from desktop-entry data, you may want to add `X-AppStream-Ignore=True` to the `Desktop Entry` section of the .desktop file. Keep in mind that if your .desktop file already has a `NoDisplay=True` key or is not of `Type=Application`, it will always be ignored, unless metainfo file exists that references it (in which case its data may be merged with the metainfo data).

### File specification

The basic structure for a generic component as described at [XML Specification](#spec-component-filespec) applies. Note that the XML root must have the `type` property set to `desktop-application`, while in a generic component this property can be omitted. This clearly identifies this metainfo document as describing an application.

> [!NOTE]
> All tags defined in the `generic` component specification are valid for `desktop-application` components as well. An application is just a specialized component, allowing tools like software centers to filter out the component types they want to display.

> [!NOTE]
> The `desktop-application` component type is the same as the `desktop` component type - `desktop` is the older type identifier for desktop-applications and should not be used for new metainfo files, unless compatibility with very old AppStream tools (pre 2016) is still wanted.

The following list describes the special tags for application upstream metadata and provides some additional information about the values the tags are expected to have. If no information is given about a tag, refer to the respective tag in [Generic Component](#sect-Metadata-GenericComponent).

\<id/\>  
For desktop applications, the `<id/>` tag value must follow the reverse-DNS scheme as described in [varlistentry_title](#tag-id-generic).

> [!NOTE]
> In previous AppStream releases, the `<id/>` was used to associate metainfo files with their .desktop files to merge in data from .desktop files into the AppStream generator's final output. In modern metainfo files, the component-ID for `desktop-application` components can be an arbitrary reverse-DNS string (matching the naming rules applying to all AppStream metadata), while the [varlistentry_title](#tag-dapp-launchable) tag is used to associate .desktop files with their metainfo files.
>
> Note that even though the component-ID can now be any rDNS name, when updating existing applications, do not change their `<id/>` to drop the .desktop suffix. The rules are relaxed when picking a new component-ID for new applications, but when updating older applications they still need to keep their original `<id/>` (when it's otherwise compliant). The ID is used to uniquely identify applications across distributions and releases and should always remain the same for the same application.

\<metadata_license/\>  
The `<metadata_license/>` tag as described in [varlistentry_title](#tag-metadata_license) must be present.

\<name/\>  
The human-readable name of the application. This is the name you want users to see prior to installing the application.

\<summary/\>  
A short summary on what this application does, roughly equivalent to the `Comment` field of the accompanying `.desktop` file of the application.

\<launchable/\>  
It is required that a `<launchable/>` tag is present in `desktop-application` MetaInfo files, unless the MetaInfo data itself contains all required information that a desktop-entry file would have (categories, icon data, ...) and the application can not be launched standalone. This makes the launchable tag a required tag for pretty much all `desktop-application` components, with only very rare exceptions. The tag is described in detail at [varlistentry_title](#tag-launchable).

If only one `launchable` entry of type `desktop-id` is present, AppStream metadata generators might decide to merge metadata from .desktop files referenced by the tag into their final output.

The `launchable` tag is optional, but if omitted software centers will not be able to launch the application directly after it was installed.

\<screenshots/\>  
A screenshot presents your application to the outside world, and could be seen by hundreds or thousands of people.

The `<screenshots/>` tag should look like it is described at [varlistentry_title](#tag-screenshots).

Screenshot size, shape and format recommendations for applications:

- All screenshots should have a 16:9 aspect ratio, and should have a width that is no smaller than 620px (software center applications will be able to fill in the screenshots in the space they provide for that more easily then).

  Ideally the window will be resized to a 16:9 aspect ratio, but screenshots can also be cropped if only a small area of the window needs to be shown.

- Screenshots should ideally be in the PNG format, but JPEG and WebP images are also fine. Keep in mind though that the images are converted into PNG when catalog metadata is generated for a software distribution.

- Do not scale screenshots below their original size.

You can find a lot more information on how to create good screenshots in the [quickstart guide on applications](#qsr-app-screenshots-info).

\<project_group/\>  
This tag is described for generic components at [XML Specification](#spec-component-filespec). You should use it for your application if appropriate.

\<provides/\>  
This tag is described in detail for generic components at [varlistentry_title](#tag-provides).

If your application ships a binary in a location in the default `PATH`, you should add at least a child of type `<binary/>` to make that new executable known to the distribution.

\<icon/\>  
This tag is described in detail for generic components at [varlistentry_title](#tag-icon).

MetaInfo files may provide an icon name for the application explicitly by using the `type="stock"` property on an `icon` tag to reference an icon from the icon stock.

> [!IMPORTANT]
> Many tools will interpret the presence of an explicit `icon` tag in the MetaInfo file as a sign that the file is *complete* and self-sufficient and no data from a desktop-entry file is expected to be merged.
>
> If you use an `icon` tag, ensure that your MetaInfo file contains all the tags that would be merged from a desktop-entry file, and consider generating your desktop-entry file from the MetaInfo file using `appstreamcli make-desktop-file`.

\<releases/\>  
The application metainfo should at least provide one `<releases/>` tag, which has one or more `<release/>` children to define the version and release date of this application. For details, see [varlistentry_title](#tag-releases) .

For a component of type `desktop-application`, the following tags are required and must always be present: [varlistentry_title](#tag-id-desktopapp), [varlistentry_title](#tag-dapp-name), [varlistentry_title](#tag-dapp-summary), [varlistentry_title](#tag-description), [varlistentry_title](#tag-metadata_license), [varlistentry_title](#tag-dapp-launchable).

## Console Applications

### Introduction

A console application is any application that has a command-line or text-based interface and is designed to be used by a human user on the command line. Applications need to be present in the standard `PATH`.

The file described in this document is built upon the generic component metadata with fields specific for applications (see [Generic Component](#sect-Metadata-GenericComponent)). All tags valid for a generic component are valid for a `console-application` component as well.

In order to enhance the available metadata about their application, projects shipping a console application can ship one or more metainfo files in `/usr/share/metainfo/%{id}.metainfo.xml`.

### File specification

The basic structure for a generic component as described at [XML Specification](#spec-component-filespec) applies. Note that the XML root must have the `type` property set to `console-application`, while in a generic component this property can be omitted. This clearly identified this metainfo document as describing an application.

The following list describes tags for `console-application` upstream metadata and provides some additional information about the values the tags are expected to have. If no information is given about a tag, refer to the respective tag in [Generic Component](#sect-Metadata-GenericComponent).

\<id/\>  
For console applications, the `<id/>` tag value must follow the AppStream ID naming conventions (it should be a reverse-DNS name).

\<metadata_license/\>  
The `<metadata_license/>` tag as described in [varlistentry_title](#tag-metadata_license) must be present.

\<name/\>  
A `name` must be present for console applications. See [varlistentry_title](#tag-name) for a detailed description of this tag.

\<summary/\>  
A `summary` must be present for console applications. See [varlistentry_title](#tag-summary) for a detailed description of this tag.

\<provides/\> ↪ \<binary/\>  
This tag is described in detail for generic components at [varlistentry_title](#tag-provides).

For console applications, at least one provided `<binary/>` must be listed in this tag.

For a component of type `console-application`, the following tags are required and must always be present: [varlistentry_title](#tag-id-console-app), [varlistentry_title](#tag-metadata_license), [varlistentry_title](#tag-name), [varlistentry_title](#tag-summary), [varlistentry_title](#tag-consoleapp-provides).

## Web Applications

### Introduction

A web application is an application running remotely that is accessed via a web browser and built on the web platform.

The metadata described in this document is built upon the generic component metadata with fields specific for web-applications (see [Generic Component](#sect-Metadata-GenericComponent)). All tags valid for a generic component are valid for a `web-application` component as well.

A web application metainfo file is special in the regard that it is usually not combined with the software it is describing and that it has no installable. It usually is equivalent to a weblink that gets special treatment by software centers. Web application metainfo files are therefore injected directly into the catalog metadata generation process, or can be installed as usual into `/usr/share/metainfo/%{id}.metainfo.xml`.

Software centers may display web applications in special, chrome-less web browser windows to achieve better desktop integration and make the web application feel more native on the desktop.

### File specification

The basic structure for a generic component as described at [XML Specification](#spec-component-filespec) applies. Note that the XML root must have the `type` property set to `web-application`, while in a generic component this property can be omitted. This clearly identified this metainfo document as describing a web application.

The following list describes tags for `web-application` metainfo files and provides some additional information about the values the tags are expected to have. If no information is given about a tag, refer to the respective tag in [Generic Component](#sect-Metadata-GenericComponent).

\<id/\>  
For web applications, the `<id/>` tag value must follow the AppStream ID naming conventions (it should be a reverse-DNS name).

\<metadata_license/\>  
The `<metadata_license/>` tag as described in [varlistentry_title](#tag-metadata_license) must be present.

\<name/\>  
A `name` must be present for web applications. See [varlistentry_title](#tag-name) for a detailed description of this tag.

\<summary/\>  
A `summary` must be present for web applications. See [varlistentry_title](#tag-summary) for a detailed description of this tag.

\<launchable/\>  
This tag is described in detail for generic components at [varlistentry_title](#tag-launchable).

A `launchable` tag of type `url` must be present for web applications. It is used as the entry point for starting the web application and opened in a browser in case the user wants to "launch" the web application.

\<icon/\>  
This tag is described in detail for generic components at [varlistentry_title](#tag-icon).

A `icon` tag must be present for web applications. Authors of the metainfo files might prefer using the `remote` icon type, but any icon type is allowed here.

For a component of type `web-application`, the following tags are required and must always be present: [varlistentry_title](#tag-id-web-app), [varlistentry_title](#tag-metadata_license), [varlistentry_title](#tag-name), [varlistentry_title](#tag-summary), [varlistentry_title](#tag-webapp-launchable), [varlistentry_title](#tag-webapp-icon), [varlistentry_title](#tag-categories).

## Services

### Introduction

A service component is any software that is started and supervised by the Operating Systems "init" facility, such as systemd.

The metadata described in this document is built upon the generic component metadata with fields specific for services (see [Generic Component](#sect-Metadata-GenericComponent)). All tags valid for a generic component are valid for a `service` component as well.

In order to enhance the available metadata about their services, projects shipping a service can ship one or more metainfo files in `/usr/share/metainfo/%{id}.metainfo.xml`.

### File specification

The basic structure for a generic component as described at [XML Specification](#spec-component-filespec) applies. Note that the XML root must have the `type` property set to `service`, while in a generic component this property can be omitted. This clearly identified this metainfo document as describing a service.

The following list describes tags for `service` upstream metadata and provides some additional information about the values the tags are expected to have. If no information is given about a tag, refer to the respective tag in [Generic Component](#sect-Metadata-GenericComponent).

\<id/\>  
For services, the `<id/>` tag value must follow the AppStream ID naming conventions (it should be a reverse-DNS name).

\<metadata_license/\>  
The `<metadata_license/>` tag as described in [varlistentry_title](#tag-metadata_license) must be present.

\<name/\>  
A `name` must be present for services. See [varlistentry_title](#tag-name) for a detailed description of this tag.

\<summary/\>  
A `summary` must be present for services. See [varlistentry_title](#tag-summary) for a detailed description of this tag.

\<launchable/\>  
This tag is described in detail for generic components at [varlistentry_title](#tag-launchable).

At least one launchable element with type "service" must be present. The value is a name that can be used with the OS init facility to start/stop and monitor the service.

For a component of type `service`, the following tags are required and must always be present: [varlistentry_title](#tag-id-service-app), [varlistentry_title](#tag-metadata_license), [varlistentry_title](#tag-name), [varlistentry_title](#tag-summary).

## Addons

### Introduction

Some components are not standalone, but rather extend existing software installed on the system and can only be used together with it. The `addon` component type exists to reflect that.

Software which provides addons can ship one or more files in `/usr/share/metainfo/%{id}.metainfo.xml`.

### Example file

A addon metainfo file should look like this:

``` XML
<?xml version="1.0" encoding="UTF-8"?>
<component type="addon">
  <id>org.gnome.gedit_code_assistance</id>
  <extends>org.gnome.gedit</extends>
  <name>Code Assistance</name>
  <summary>Code assistance for C, C++ and Objective-C</summary>
  <url type="homepage">http://projects.gnome.org/gedit</url>
  <metadata_license>FSFAP</metadata_license>
  <project_license>GPL-3.0+</project_license>
</component>
```

### File specification

Note that the XML root must have the `type` property set to `addon`. This clearly identifies this metainfo document as describing an addon to existing software.

\<id/\>  
For addons, the component-ID must follow the generic naming conventions (see [varlistentry_title](#tag-id-generic)).

\<extends/\>  
This tag refers to the ID of the component this addon is extending.

For example, if there is a plugin "kipi" which extends the application "Gwenview", it needs to be referred to as:

``` XML
<extends>org.kde.Gwenview</extends>
```

The `<extends/>` tag may be specified multiple times.

For a component of type `addon`, the following tags are required and must be present: [varlistentry_title](#tag-id-addon), [varlistentry_title](#tag-name), [varlistentry_title](#tag-summary), [varlistentry_title](#tag-metadata_license), [varlistentry_title](#tag-extends).

## Fonts

### Introduction

A software center can allow users to install additional fonts using font metadata. Also, applications can use font metadata to find missing fonts (for example, if a special mathematical font is needed) in the distribution's software sources. This metainfo specification describes how metadata for fonts or font collections should be structured.

Font packages can ship one or more files in `/usr/share/metainfo/%{id}.metainfo.xml`.

Font metadata files can – just like all other metainfo files – be translated. See the section about translation for more information.

> [!NOTE]
> A `font` component is in most cases not describing a single font, but rather a collection of fonts that are grouped together, usually by their art style or font-family.
>
> To make the individual fonts known to the system, use the [varlistentry_title](#tag-font-provides) tag.

### Example file

A minimal font metainfo file can look like this:

``` XML
<?xml version="1.0" encoding="UTF-8"?>
<component type="font">
  <id>com.latofonts.Lato</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL-1.1</project_license>

  <name>Lato</name>
  <summary>A sanserif type­face fam­ily</summary>
  <description>
    <p>
      Lato is a sanserif type­face fam­ily designed in the Sum­mer 2010 by Warsaw-​​based designer
      Łukasz Dziedzic (“Lato” means “Sum­mer” in Pol­ish). In Decem­ber 2010 the Lato fam­ily
      was pub­lished under the open-​​source Open Font License by his foundry tyPoland, with
      sup­port from Google.
    </p>
  </description>

  <provides>
    <font>Lato Regular</font>
    <font>Lato Italic</font>
    <font>Lato Bold</font>
    <font>Lato Light</font>
    <font>Lato Light Italic</font>
    ...
  </provides>
</component>
```

### File specification

Note that the XML root must have the `type` property set to `font`. This clearly identifies this metainfo document as describing a font.

\<id/\>  
For fonts, the `%{id}` must follow the reverse-DNS scheme as described for generic components. For the product name part, it is recommended to take the the name of the font or font bundle without whitespace.

\<metadata_license/\>  
The `<metadata_license/>` tag is required. See [varlistentry_title](#tag-metadata_license) for a description of this tag.

\<name/\>  
Set a name for the font or font collection.

\<summary/\>  
A short description of the font described in this metainfo file.

\<description/\>  
Add a long description of your font. Do not assume the format is HTML. Only paragraph, ordered list and unordered list are supported at this time.

See the generic component [varlistentry_title](#tag-description) for a detailed description of this tag.

\<screenshots/\>  
A screenshot presents your font to the outside world.

If the font metadata does not define an own screenshot, the AppStream generator is supposed to render one or multiple sample images using the respective font.

See the generic component [varlistentry_title](#tag-screenshots) for a detailed description of this tag.

\<url/\>  
This is a recommended tag for links of type `homepage`. Links of type `homepage` should be a link to the upstream homepage for the application. See the generic component [varlistentry_title](#tag-url) for a description of this tag.

\<provides/\> ↪ \<font/\>  
This tag is described in detail for generic components at [varlistentry_title](#tag-provides).

You should add one or more children of type `<font/>` to make the font's full-names known. The full-name should be the same as given in the font file for the English language. If no full-name is set, a space-separated combination of the font's `family` and `style` is used instead. The font *must* have a `family` defined to be included.

The full-name entry should show the complete name of a typeface in its “natural” form, including style and character set information (if any), and without abbreviations. This is the name that some systems and applications look at to determine full, unabbreviated font menu names.

If you want to query the full-name and its `family` and `style` to see what needs to be added to this tag, you can use the `fc-query` utility of Fonconfig:

    fc-query --format='FN: %{fullname[0]}\nFS: %{family[0]} %{style[0]}\n' FONT-FILENAME

Examples:

``` XML
<provides>
  <font>Lato Heavy Italic</font>
  <font>Noto Kufi Arabic Bold</font>
  <font>Liberation Serif Bold Italic</font>
  <font>FontAwesome Regular</font>
</provides>
```

If no `<font/>` tags were defined, the AppStream catalog data generator should try to extract them from the actual font files found in the software package/bundle.

In every case, the names given in the provides tag *must* match the metadat the fonts contain themselves. If the data of the font files is incomplete, the data can not be extended by the `<font/>` tag. This is important because the AppStream generator may use the data to pick the right fonts, and because applications expect the exact font they requested via AppStream to be present on the system after the component was installed (and not one which has different metadata).

\<languages/\>  
This tag gives information about the locale a font supports.

This tak allows specifying the main locale (and thereby scripts) the font can be used with. It does not have to contain an extensive list, as the AppStream metadata generator will try get obtain that information from the font files themselves, but it is useful to define to hint the generator in the right direction.

If samples of the font are rendered as screenshots by the catalog metadata generator, the locale mentioned in the metainfo file will be preferred over automatically (or heuristically) defined ones.

You can use the following command to determine which languages a font supports:

    fc-query --format='%{lang}\n' FONT-FILENAME

Tag example:

``` XML
<languages>
  <lang>de</lang>
  <lang>en</lang>
  <lang>cn</lang>
</languages>
```

For a component of type `font`, the following tags are required and must be present: [varlistentry_title](#tag-id-generic), [varlistentry_title](#tag-name), [varlistentry_title](#tag-summary), [varlistentry_title](#tag-metadata_license), [varlistentry_title](#tag-font-provides).

## Icon Themes

### Introduction

Icon themes as defined in the [Freedesktop Icon Theme Specification](https://specifications.freedesktop.org/icon-theme-spec/latest/) can contain `icon-theme` metainfo files to be installed by software centers. This metainfo specification describes how metadata for icon themes should be structured.

Icon theme packages can ship one or more files in `/usr/share/metainfo/%{id}.metainfo.xml`.

Icon theme metadata files can – just like all other metainfo files – be translated. See the section about translation for more information.

### Example file

A minimal icon theme metainfo file can look like this:

``` XML
<?xml version="1.0" encoding="utf-8"?>
<component type="icon-theme">
  <id>io.git.PapirusIconTheme</id>
  <metadata_license>FSFAP</metadata_license>
  <project_license>GPL-3.0</project_license>

  <name>Papirus</name>
  <summary>A free and open source icon theme for Linux, based on the Paper Icon Set</summary>
  <description>
    <p>
      Papirus is a free and open source SVG icon theme for Linux, based on Paper Icon Set
      with a lot of new icons and a few extras, like Hardcode-Tray support, KDE colorscheme
      support, Folder Color support, and others.
      It is available in four variants:
    </p>
    <ul>
      <li>Papirus</li>
      <li>Papirus Dark</li>
      <li>Papirus Light</li>
      <li>ePapirus (for elementary OS and Pantheon Desktop)</li>
    </ul>
  </description>

  <screenshots>
    <screenshot type="default">
      <image type="source">https://raw.githubusercontent.com/PapirusDevelopmentTeam/papirus-icon-theme/master/preview.png</image>
    </screenshot>
  </screenshots>
</component>
```

### File specification

Note that the XML root must have the `type` property set to `icon-theme`. This clearly identifies this metainfo document as describing an icon theme following the Freedesktop specification.

A new metainfo file is required for each variant of the icon theme (one for each `index.theme`) to describe the individual icon themes and allow them to be installed individually. That is, unless all the different theme variants are designed to be installed together (due to symbolic links between themes or `Inherits` fields in the theme description), in which case only one `icon-theme` component is required to describe the whole icon theme set.

\<id/\>  
For fonts, the `%{id}` must follow the reverse-DNS scheme as described for generic components.

\<metadata_license/\>  
The `<metadata_license/>` tag is required. See [varlistentry_title](#tag-metadata_license) for a description of this tag.

\<name/\>  
Set a name for the icon theme or set of icon themes intended to be shipped in one bundle.

\<summary/\>  
A short description of the icon theme.

\<description/\>  
Add a long description of your icon theme.

See the generic component [varlistentry_title](#tag-description) for a detailed description of this tag.

\<screenshots/\>  
A screenshot to show off the icon theme.

A good example on how that may look like is [the preview image of the Papirus icon theme](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme/blob/master/preview.png).

See the generic component [varlistentry_title](#tag-screenshots) for a detailed description of this tag.

\<url/\>  
This is a recommended tag for links of type `homepage`. Links of type `homepage` should be a link to the upstream homepage for the icon theme. See the generic component [varlistentry_title](#tag-url) for a description of this tag.

For a component of type `icon-theme`, the following tags are required and must be present: [varlistentry_title](#tag-id-generic), [varlistentry_title](#tag-name), [varlistentry_title](#tag-summary), [varlistentry_title](#tag-metadata_license).

## Codecs

### Introduction

Software centers might want to special-case codec handling. Therefore, we provide a component type for them.

Codecs can ship one or more files in `/usr/share/metainfo/%{id}.metainfo.xml`.

Codec metadata files can – just like all other metainfo files – be translated. See the section about translation for more information.

### Example file

A codec metainfo file should look like this:

``` XML
<?xml version="1.0" encoding="UTF-8"?>
<component type="codec">
  <id>org.freedesktop.gstreamer.codecs-good</id>
  <metadata_license>CC0</metadata_license>
  <name>GStreamer Multimedia Codecs - Extra</name>
  <description>
    <p>
      This addon includes several additional codecs that are missing
      something - perhaps a good code review, some documentation, a set of
      tests, a real live maintainer, or some actual wide use.
      However, they might be good enough to play your media files.
    </p>
    <p>
      These codecs can be used to encode and decode media files where the
      format is not patent encumbered.
    </p>
    <p>
      A codec decodes audio and video for for playback or editing and is also
      used for transmission or storage.
      Different codecs are used in video-conferencing, streaming media and
      video editing applications.
    </p>
  </description>
  <provides>
    <codec>encoder-audio/mpeg</codec>
    <codec>mpegversion=(int){ 4, 2 }</codec>
    <codec>stream-format=(string){ adts, raw }</codec>
    <codec>encoder-video/mpeg</codec>
    <codec>systemstream=(boolean)false</codec>
    <codec>mpegversion=(int){ 1, 2, 4 }</codec>
    <codec>encoder-video/mpeg</codec>
    <codec>systemstream=(boolean)true</codec>
    <codec>encoder-video/x-xvid</codec>
    <codec>element-faac</codec>
    <codec>element-mpeg2enc</codec>
    <codec>element-mplex</codec>
    <codec>element-xviddec</codec>
    <codec>element-xvidenc</codec>
  </provides>
</component>
```

### File specification

Note that the XML root must have the `type` property set to `codec`. This clearly identifies this metainfo document as describing a codec.

\<id/\>  
For codecs, the `%{id}` must follow the component-id naming conventions (see [varlistentry_title](#tag-id-generic)).

\<metadata_license/\>  
The `<metadata_license/>` tag is required. See [Generic Component](#sect-Metadata-GenericComponent) for a description of this tag.

\<provides/\> ↪ \<codec/\>  
This tag is described for generic components at [Generic Component](#sect-Metadata-GenericComponent) in detail.

You must add one or more children of type `<codec/>` to make it known to the system that your software is able to provide the mentioned codecs. Adding this data is required for all components of `type=codec`.

For a component of type `codec`, the following tags are required and must be present: [varlistentry_title](#tag-id-codec), [varlistentry_title](#tag-name), [varlistentry_title](#tag-summary), [varlistentry_title](#tag-metadata_license), [varlistentry_title](#tag-codec-provides).

## Input Methods

### Introduction

It is a nice feature for a software center to allows users the installation of additional input methods. This metainfo specification describes how metadata about input methods should be structured.

Software components providing an input method can ship one or more files in `/usr/share/metainfo/%{id}.metainfo.xml`.

Input method metadata files can – just like all other metainfo files – be translated. See the section about translation for more information.

### Example file

The input method metainfo file should look like this:

``` XML
<?xml version="1.0" encoding="UTF-8"?>
<component type="inputmethod">
  <id>com.github.ibus.mathwriter-ibus.db</id>
  <metadata_license>FSFAP</metadata_license>
  <name>Mathwriter</name>
  <summary>Math symbols input method</summary>
  <description>
    <p>
      The input method is designed for entering mathematical symbols.
    </p>
    <p>
      Input methods are typing systems allowing users to input complex languages.
      They are necessary because these contain too many characters to simply be laid
      out on a traditional keyboard.
    </p>
  </description>
  <url type="homepage">https://github.com/mike-fabian/ibus-table-others</url>
</component>
```

### File specification

Note that the XML root must have the `type` property set to `inputmethod`. This clearly identifies this metainfo document as describing an input method instead of a generic software component.

\<id/\>  
For input methods, the `%{id}` should follow the standard reverse-domain-name scheme. For the product name part, it is recommended to take the database filename of the input method.

\<metadata_license/\>  
The `<metadata_license/>` tag is required. See [Generic Component](#sect-Metadata-GenericComponent) for a description of this tag.

\<name/\>  
Set a name for your input method.

\<summary/\>  
A short description of the input method described in this metainfo file.

\<description/\>  
Add a long description of the input method.

Do not assume the format is HTML. Only paragraph, ordered list and unordered list are supported at this time.

\<screenshots/\>  
A screenshot may be included, showing the input method in use in an application.

Refer to [varlistentry_title](#tag-screenshots) for a detailed description of this tag.

\<url/\>  
This is a recommended tag for links of type `homepage`. Links of type `homepage` should be a link to the upstream homepage for the application. See See [varlistentry_title](#tag-url) for a description of this tag.

\<provides/\>  
This tag is described for generic components at [varlistentry_title](#tag-provides) in detail.

You can add one or more children of type `<library/>` in case you publish some additional shared libraries. If not, and there are no public binaries involved, you may omit the `provides` tag for input methods.

For a component of type `inputmethod`, the following tags are required and must be present: [varlistentry_title](#tag-id-inputmethod), [varlistentry_title](#tag-name), [varlistentry_title](#tag-summary), [varlistentry_title](#tag-metadata_license).

## Firmware

### Introduction

Device firmware can be accompanied by AppStream upstream metadata, to be incorporated by a distribution. Tools like [fwupd](https://github.com/hughsie/fwupd) make use of this metadata to automatically update flashed firmware of devices found in the machine. Additionally, this component type can also be used for firmware which is loaded onto the device at runtime.

Firmware can ship one or more files in `/usr/share/metainfo/%{id}.metainfo.xml`.

### Example file

A firmware metainfo file should look like this:

``` XML
<?xml version="1.0" encoding="UTF-8"?>
<component type="firmware">
  <id>com.hughski.ColorHug2.firmware</id>
  <name>ColorHugALS Firmware</name>
  <summary>Firmware for the ColorHugALS Ambient Light Sensor</summary>
  <description>
    <p>
      Updating the firmware on your ColorHugALS device improves performance and
      adds new features.
    </p>
  </description>
  <url type="homepage">http://www.hughski.com/</url>
  <metadata_license>CC0-1.0</metadata_license>
  <project_license>GPL-2.0+</project_license>
  <developer id="hughski.com">
    <name>Hughski Limited</name>
  </developer>
  <provides>
    <firmware type="flashed">84f40464-9272-4ef7-9399-cd95f12da696</firmware>
  </provides>
  <releases>
    <release version="3.0.2" date="2015-02-16">
      <artifacts>
        <artifact type="binary">
          <location>http://www.hughski.com/downloads/colorhug-als/firmware/colorhug-als-3.0.2.cab</location>
        </artifact>
      </artifacts>
      <description>
        <p>This stable release fixes the following bugs:</p>
        <ul>
          <li>Fix the return code from GetHardwareVersion</li>
          <li>Scale the output of TakeReadingRaw by the datasheet values</li>
        </ul>
      </description>
    </release>
  </releases>
</component>
```

You can find additional information on how to create a complete firmware package for flashed firmware upstream in the [README document of fwupd](https://github.com/hughsie/fwupd/blob/master/README.md).

### File specification

Note that the XML root must have the `type` property set to `firmware`. This clearly identifies this metainfo document as describing firmware.

\<id/\>  
For firmware, the value of the `<id/>` tag must follow the reverse-DNS scheme as described for generic components. It is sometimes useful to suffix the ID with `.firmware` to make it more unique. For example `com.hughski.ColorHug2.firmware`.

\<releases/\>  
This tag is identical to the generic [varlistentry_title](#tag-releases) tag. Additional to the generic tag, for each `<release/>` child at least one `<artifact/>` tag is required in case the component describes flashed firmware.

The `<location/>` tag of the binary artifact specifies a remote location where the firmware `.cab` can be downloaded from. The download location needs to be accessible via HTTP, HTTPS or FTP.

Example:

``` XML
<releases>
  <release version="3.0.2" date="2015-02-16">
    <artifacts>
      <artifact type="binary">
        <location>http://www.hughski.com/downloads/colorhug-als/firmware/colorhug-als-3.0.2.cab</location>
      </artifact>
    </artifacts>
    <description>
      <p>This stable release fixes bugs.</p>
    </description>
  </release>
</releases>
```

\<provides/\> ↪ \<firmware/\>  
The `provides/firmware` tag describes the technical information needed to associate a firmware with a device, or describes which runtime firmware file it makes available to the kernel.

For runtime-loadable firmware, the `type` property of the `firmware` tag needs to be set to `runtime`, and its value needs to define the filename of a firmware below `/lib/firmware` to the firmware file in question, like the firmware value exported from Linux kernel modules.

Example:

``` XML
<provides>
  <firmware type="runtime">ipw2200-bss.fw</firmware>
</provides>
```

For flashed firmware, the `type` property of the tag needs to be set to `flashed`. Its value needs to define the GUID of the device the firmware should be flashed onto.

Example:

``` XML
<provides>
  <firmware type="flashed">84f40464-9272-4ef7-9399-cd95f12da696</firmware>
</provides>
```

For a component of type `firmware`, the following tags are required and must be present for a valid document: [varlistentry_title](#tag-id-firmware), [varlistentry_title](#tag-name), [varlistentry_title](#tag-summary), [varlistentry_title](#tag-metadata_license), [varlistentry_title](#tag-firmware-provides).

## Driver

### Introduction

The `driver` component type describes drivers for hardware devices as well as other Linux kernel drivers for e.g. virtualization support. It usually `provides` one or multiple modaliases.

Drivers can ship one or more files in `/usr/share/metainfo/%{id}.metainfo.xml`.

### Example file

A driver metainfo file can look like this:

``` XML
<?xml version="1.0" encoding="UTF-8"?>
<component type="driver">
  <id>com.nvidia.GeForce</id>
  <name>NVIDIA GeForce</name>
  <summary>NVIDIA Graphics Driver</summary>
  <description>
    <p>
      The NVIDIA Accelerated Linux Graphics Driver brings accelerated 2D
      functionality and high-performance OpenGL support to Linux x86 with the
      use of NVIDIA graphics processing units.
    </p>
    ...
  </description>
  <url type="homepage">http://www.nvidia.com/Download/index.aspx</url>
  <metadata_license>CC0-1.0</metadata_license>
  <project_license>LicenseRef-proprietary:NVIDIA</project_license>

  <developer id="nvidia.com">
    <name>NVIDIA Corporation</name>
  </developer>

  <provides>
    <modalias>pci:v000010DEd*sv*sd*bc03sc00i00*</modalias>
    ...
  </provides>
</component>
```

### File specification

Note that the XML root must have the `type` property set to `driver`. This clearly identifies this metainfo document as describing a driver.

\<id/\>  
For drivers, the value of the `<id/>` tag must follow the reverse-DNS scheme as described for generic components. It is sometimes useful to suffix the ID with `.driver` to make it more unique.

\<provides/\> ↪ \<modalias/\>  
The `provides/modalias` tags contain all the modaliases the described driver supports and allow to automatically offer installation of the described driver on systems where hardware matching the modalias has been detected.

Using wildcards for modaliases is permitted.

Example:

``` XML
<provides>
  <modalias>pci:v000010DEd00001194sv*sd*bc03sc*i*</modalias>
  <modalias>pci:v000010DEd00001199sv*sd*bc03sc*i*</modalias>
</provides>
```

For a component of type `driver`, the following tags are required and must be present for a valid document: [varlistentry_title](#tag-id-driver), [varlistentry_title](#tag-name), [varlistentry_title](#tag-summary), [varlistentry_title](#tag-metadata_license), [varlistentry_title](#tag-driver-provides).

## Localization

### Localization

The `localization` component type describes language packs for individual software components or groups of software components. A language pack includes anything necessary to localize a software component for a specific language and/or country. This is usually translations, but may also be translated media content, currency information and other things. A `localization` component `extends` one or multiple other components and defines the languages it provides via its `languages` tag.

Language packs can ship one or more metainfo files as `/usr/share/metainfo/%{id}.metainfo.xml`.

Do not confuse language packs with the catalog metadata [varlistentry_title](#tag-ct-languages) tag, used to identify bundled translations.

### Example file

A localization metainfo file can look like this:

``` XML
<?xml version="1.0" encoding="UTF-8"?>
<component type="localization">
  <id>org.kde.l10n.de</id>
  <name>KDE German Language</name>
  <summary>German localization for the KDE desktop and apps</summary>

  <extends>org.kde.plasmashell</extends>
  <extends>org.kde.gwenview.desktop</extends>
  <extends>org.kde.dolphin.desktop</extends>
  ...

  <url type="homepage">http://i18n.kde.org/team-infos.php?teamcode=de</url>
  <metadata_license>FSFAP</metadata_license>

  <developer id="kde">
    <name>The KDE German L10N team</name>
  </developer>

  <languages>
    <lang>de_DE</lang>
    <lang percentage="96">de_AT</lang>
    <lang percentage="100">de</lang>
    ...
  </languages>
</component>
```

### File specification

Note that the XML root must have the `type` property set to `localization`. This clearly identifies this metainfo document as describing a language pack.

\<id/\>  
For localizations, the value of the `<id/>` tag must follow the reverse-DNS scheme as described for generic components. Ideally, the name of the component this language pack is for should be suffixed with `.l10n.%{lang}`, where `%{lang}` is the language code of the language pack.

For example, if your applications component-id is `org.gimp.gimp` the ID of the German language pack for GIMP should be `org.gimp.gimp.l10n.de`.

\<extends/\>  
The `extends` tags contain all the components this language pack can be used with.

\<languages/\>  
This tag gives information about the locale a localization component provides support for.

The tag is allowed to only occur once per component, and contains multiple `<lang/>` child nodes, which have a [language code](https://www.gnu.org/software/gettext/manual/html_node/Language-Codes.html) as value. Each `<lang/>` node may have a `percentage` property, which describes the percentage value to which a component has been translated.

Tag example:

``` XML
<languages>
  <lang>de_DE</lang>
  <lang percentage="94">de_AT</lang>
</languages>
```

For a component of type `localization`, the following tags are required and must be present for a valid document: [varlistentry_title](#tag-id-l10n), [varlistentry_title](#tag-name), [varlistentry_title](#tag-summary), [varlistentry_title](#tag-metadata_license), [varlistentry_title](#tag-l10n-extends), [varlistentry_title](#tag-l10n-languages).

## Repositories

### Introduction

A repository component describes a remote archive of digital content, usually other software or additional data (e.g. themes, icons, books, music, ...). Upon installation of a component of this type, the repective repository is added to the system and activated, letting the user access the new content.

The metadata described in this document is built upon the generic component metadata (see [Generic Component](#sect-Metadata-GenericComponent)). All tags valid for a generic component are valid for a `repository` component as well.

In order to add metadata about a software repository, projects can provide one or more metainfo files in `/usr/share/metainfo/%{id}.metainfo.xml`.

### File specification

The basic structure for a generic component as described at [XML Specification](#spec-component-filespec) applies. Note that the XML root must have the `type` property set to `repository`, while in a generic component this property can be omitted. This clearly identified this metainfo document as describing a repository.

The following list describes tags for `repository` upstream metadata and provides some additional information about the values the tags are expected to have. If no information is given about a tag, refer to the respective tag in [Generic Component](#sect-Metadata-GenericComponent).

\<id/\>  
For repositories, the `<id/>` tag value must follow the AppStream ID naming conventions (it should be a reverse-DNS name).

\<metadata_license/\>  
The `<metadata_license/>` tag as described in [varlistentry_title](#tag-metadata_license) must be present.

\<name/\>  
A `name` must be present for repositories. See [varlistentry_title](#tag-name) for a detailed description of this tag.

\<summary/\>  
A `summary` must be present for repositories. See [varlistentry_title](#tag-summary) for a detailed description of this tag.

\<extends/\>  
This tag is refers to the ID of the component this repository is added to, similarly to how components of type `addon` work.

Adding an `extends` tag ensures the respective repository is tied to its main component, e.g. a source for firmware downloads is tied to the firmware update service, or a repository for a site-specific package manager is tied to the tool that can actually install pieces from the repository.

The `<extends/>` tag may be specified multiple times.

\<agreement/\>  
It is recommended to add a [GDPR](https://www.eugdpr.org/) compliant privacy statement to `repository` components, in case any personal data is acquired when the repository is accessed.

The `agreement` tag allows to add a privacy statement and other agreements easily. Refer to the [varlistentry_title](#tag-agreement) tag as described for generic components for information on how to use agreements in AppStream.

For a component of type `repository`, the following tags are required and must always be present: [varlistentry_title](#tag-id-repo), [varlistentry_title](#tag-metadata_license), [varlistentry_title](#tag-name), [varlistentry_title](#tag-summary).

## Operating System

### Introduction

The `operating-system` component type describes a whole operating system such as GNU/Linux distributions like Debian, Fedora, RHEL, etc. or Windows and macOS.

Operating systems can ship metainfo files in `/usr/share/metainfo/%{id}.metainfo.xml`.

### Example file

An `operating-system` metainfo file can look like this:

``` XML
<?xml version="1.0" encoding="UTF-8"?>
<component type="operating-system">
  <id>org.debian.debian</id>
  <name>Debian GNU/Linux</name>
  <summary>The universal operating system</summary>
  <description>
    <p>
      Debian is a free operating system (OS) for your computer.
      An operating system is the set of basic programs and utilities that make your computer run.
    </p>
    ...
  </description>
  <url type="homepage">https://www.debian.org/</url>
  <metadata_license>FSFAP</metadata_license>
  <developer id="debian">
    <name>The Debian Project</name>
  </developer>
  ...

  <releases>
    <release version="10.0" type="development">
      <description>
        <p>The next release of Debian.</p>
      </description>
    </release>

    <release version="9.0" date="2017-07-17" date_eol="2020-07-17">
      <description>
        <p>Now contains the Linux kernel 4.9, GNOME 3.22, KDE Plasma 5, LibreOffice 5.2 and Qt 5.7. LXQt has been added.</p>
      </description>
    </release>
    ...
  </releases>
</component>
```

### File specification

Note that the XML root must have the `type` property set to `operating-system`. This clearly identifies this metainfo document as describing an operating system.

\<id/\>  
For operating systems, the value of the `<id/>` tag must follow the reverse-DNS scheme as described for generic components. In order for AppStream consumers to determine which component is describing the operating system they are currently running on, on Linux distributions the component ID must follow the data provided in the operating system's `/etc/os-release` file. This means the reversed-DNS `HOME_URL` value from `/etc/os-release` (without any https/www parts) combined with the `ID` of the operating system will produce the operating system's component id.

E.g. if `HOME_URL` is `https://www.debian.org/` and `ID` is `debian`, the resulting AppStream component-ID will be `org.debian.debian`.

\<releases/\>  
The `<releases/>` tag as described in [varlistentry_title](#tag-releases) must be present and contain the individual releases of the operating system. It is also recommended to set the `date_eol` property on individual releases, to allow software to determine whether the current operating system release is still supported.

For a component of type `operating-system`, the following tags are required and must be present for a valid document: [varlistentry_title](#tag-id-os), [varlistentry_title](#tag-name), [varlistentry_title](#tag-summary), [varlistentry_title](#tag-metadata_license), [varlistentry_title](#tag-os-releases).

## Runtime

### Introduction

Components of type `runtime` describe a collection of interdependent software components that are required to run other software. They set a baseline of dependencies that other software can rely on and link against. A very simple runtime may for example be a chroot environment of a minimal Linux system bootstrap. Runtimes are often employed by software distribution systems such as [Flatpak](https://flatpak.org/) or Valve's Steam, but may be used by others and may even be directly distributed as part of tranditional Linux distributions.

Runtimes can ship metainfo files in `/usr/share/metainfo/%{id}.metainfo.xml`.

### Example file

A `runtime` metainfo file can look like this:

``` XML
<?xml version="1.0" encoding="UTF-8"?>
<component type="runtime">
  <id>org.freedesktop.Platform</id>
  <metadata_license>FSFAP</metadata_license>
  <project_license>LicenseRef-free=https://freedesktop-sdk.gitlab.io/</project_license>

  <name>Freedesktop Platform</name>
  <summary>Basic libraries to run Linux desktop applications</summary>

  <description>
    <p>
      The Freedesktop Platform is a runtime that contains the most basic libraries
      and files needed to run a Linux desktop application.
      ...
    </p>
  </description>
  <url type="homepage">https://freedesktop-sdk.gitlab.io/</url>

  <releases>
    <release version="10.0" />
    <release version="9.0" date="2020-01-12" />
    ...
  </releases>
</component>
```

### File specification

Note that the XML root must have the `type` property set to `runtime`. This clearly identifies this metainfo document as describing a runtime.

\<id/\>  
For runtimes, the value of the `<id/>` tag must follow the AppStream ID naming conventions (it should be a reverse-DNS name).

\<requires/\>  
The `requires` tag may be used if multiple runtimes are based on top of each other, or if the runtime actually describes a software development kit (SDK) that wants to require its base runtime. See [varlistentry_title](#tag-relations) for a detailed description of this tag.

In order to depend on other runtimes, their component-ID should be referenced in a `requires` tag. Example:

``` XML
<requires>
  <id version="1.0" compare="ge">org.freedesktop.Sdk</id>
</requires>
```

\<project_license/\>  
The `<project_license/>` tag usually indicates the license of the component (refer to [varlistentry_title](#tag-project_license) for details). This is tricky for runtimes, as they are usually comprised of many individual pieces of software under different licenses, which would create a very long and complex SPDX license expression. It is therefore recommended to have the tool that builds the runtime collect all the licenses and generate a document or website containing. This document can then be linked using `LicenseRef-free=URL` if the runtime is free software, or `LicenseRef-proprietary=URL` in case it contains non-free elements.

Example:

``` XML
<project_license>LicenseRef-free=https://example.com/licenses.html</project_license>
```

\<provides/\>  
This tag is described in detail for generic components at [varlistentry_title](#tag-provides).

The runtime may use the `<provides/>` tag to denote the individual modules it is comprised of, using their component IDs.

For a component of type `runtime`, the following tags are required and must be present for a valid document: [varlistentry_title](#tag-id-runtime), [varlistentry_title](#tag-name), [varlistentry_title](#tag-summary), [varlistentry_title](#tag-metadata_license), [varlistentry_title](#tag-project_license).

# Catalog Metadata

Additionally to the metainfo files shipped by upstream projects, AppStream also provides an XML and YAML format to make information about not installed software components known to the system.

This chapter documents this catalog metadata format and icon cache used on the client side.

## AppStream Catalog XML

### Introduction

AppStream catalog XML files are text files describing all available software components a software repository (usually from a Linux distributor) offers for installation. The XML files might be compressed with GZip.

### File naming and location

The XML files must have a unique name, which is usually the distribution's name and version, combined with the name of the repository/origin. For example in Debian 8 (Jessie), the filename for the main repository component would be `debian-jessie-main.xml.gz`. For Fedora 20 (Heisenbug) updates it would be `fedora-20-updates.xml.gz`. 3rd-party repositories use a vendor name and repository-name combination, for example Ubuntu PPAs might get `ppa-ubuntu12.04-username-foobar.xml`.

There are two valid locations to store AppStream XML data. `/usr/share/swcatalog/xml` stores all AppStream data which has been installed via software packages, while `/var/lib/swcatalog/xml` stores application data which was downloaded by the package manager or placed there by other tools (for example, Limba). The `/var/cache/swcatalog/xml` location however can be used for any data that was locally generated from other sources. The XML files can either be plain files or be compressed with gzip. It is always a good idea to compress the files, because they tend to become quite large.

> [!IMPORTANT]
> Prior to version 1.0, AppStream tools scanned the paths `/usr/share/app-info/(xml|xmls)` and `/var/lib/app-info/(xml|xmls)` path for legacy compatibility as well. Legacy path support was dropped in version 1.0. The old locations should not be used anymore. The modern locations are supported by both the AppStream 1.x as well as AppStream 0.16.x series.

### General XML structure

The XML starts with a `<components>` tag as the root element. It has all the `<component>` tags of different `type`s as children.

Data to fill the different component elements is usually taken from their [Desktop files](https://specifications.freedesktop.org/desktop-entry-spec/latest/) and package data. However, if an upstream project ships metainfo files (see [Upstream Metadata](#chap-Metadata)), values defined there should override data from any other source.

All child elements of the `<components>` element, no matter of which type they are, must at least have an `id`, `name`, `summary` and `pkgname` tag. For applications, a `icon` tag is also required.

The `<components>` root node has these properties, where the first two are required:

version  
This property declares the AppStream spec version this file is based on (currently 0.14). The property is required.

origin  
Defines the repository ID this AppStream XML file belongs to. This usually matches the filename without extension (see the explanation on how to pick a good filename above). It is also used to associate the right cached icons with AppStream metadata. This property is required.

media_baseurl  
The base URL for media (screenshots, icons, ...) referenced in the metadata file. If this is set, all urls in the document referencing media will be treated relative to the base url.

architecture  
Defines the architecture this data belongs to. This information is useful to resolve AppStream-ID conflicts on multiarch systems, which appear if the user has metadata for two architectures installed. This property is optional.

### Valid tags for all component types

These tags can be applied to every component type (application, component, font, inputmethod) which is described in the AppStream metadata.

Additionally to the `type` property, every `<component/>` tag in AppStream catalog data may have a `priority` property, defining the priority of this specific metadata over other metadata from different AppStream XML files (for example, from a different repository) which have the same component-id. The value of this tag is an integer, if the property is missing, a value of `"0"` is assumed.

In order to *merge* metadata, each component in catalog data may also have a `merge` property, assuming the values `append`, `replace` or `remove-component`. If the value is `append`, all data this component describes will be appended to data of the component with the same ID. If the value is `replace` the fields of the target component will be replaced with the ones present in the merge component. If the merge type is `remove-component`, the entore component matching the ID of the merge-component should be removed from the metadata pool. Merge-components with a higher priority take precedence. If a component has a `merge` property, the only tag that must be present for it is the `<id/>` tag, any other metadata is optional.

\<id/\>  
The `<id/>` tag is a short unique and usually lower-cases identifier for the component. Depending on the component's type, different naming conventions apply.

\<pkgname/\>  
The name of the package which needs to be installed in order to make this component available on the system.

This tag can be defined multiple times, if a component is split across multiple packages.

> [!IMPORTANT]
> The preferred way is to create metapackages containing the component metadata, and referencing them from the catalog metadata, and not to use multiple `pkgname` tags. They should only be used multiple times as a workaround or if there is no sensible way of creating a matching metapackage.

\<source_pkgname/\>  
This optional tag is used to specify the source package the binary package this component belongs to was built from.

The tag can be used by software center applications to group components. It is otherwise useful for the distributor to assign components to a source package and to fetch additional information about a package from the web.

\<name/\>  
A human-readable name for this software.

In case of a component of type `desktop-application`, the application name as defined in the application's [desktop file](https://specifications.freedesktop.org/desktop-entry-spec/latest/) is used.

\<project_license/\>  
The `<project_license/>` tag is indicating the license of the component. It should be a [SPDX license expression](https://spdx.org/specifications). A full list of recognized licenses and their identifiers can be found at the [SPDX OpenSource License Registry](https://spdx.org/licenses/).

You can find more information about this tag at the metainfo description for [varlistentry_title](#tag-project_license).

\<summary/\>  
The tag contains a short summary of the purpose and function of this component. In case the component is of type `desktop`, it is usually taken from a Desktop file, if the application does not ship an upstream metadata file.

For more information about this tag, take a look at the tag's definition at [varlistentry_title](#tag-summary).

\<description/\>  
A long description of the component. It is usually taken from the package descriptions or metainfo files, if they were provided. The description might use markup. Right now, only paragraph, ordered list and unordered list are supported. An example description element might look like this:

``` XML
<description>
  <p>
   Power Statistics is a program used to view historical and current battery
   information and will show programs running on your computer using power.
  </p>
  <p>Example list:</p>
  <ul>
   <li>First item</li>
   <li>Second item</li>
  </ul>
  <p>
  You probably only need to install this application if you are having problems
  with your laptop battery, or are trying to work out what programs are using
  significant amounts of power.
  </p>
</description>
```

As opposed to the by-paragraph translation used in metainfo files, this tag is translated "as a whole", meaning that the `<description/>` tag itself has a language property and contains the translated paragraphs for the given language. This allows faster parsing of the Appstream XML file, and does not increase it's size much, as long as it is compressed.

For more information about this tag, take a look at the tag's definition at [varlistentry_title](#tag-description).

\<url/\>  
Defines URLs for this component. This tag can be present multiple times.

For a list of possible url types and what they are expected to do, take a look at the tag's description at [varlistentry_title](#tag-url).

\<project_group/\>  
The `<project_group>` tag identifies a project with a specific upstream umbrella project. Known values include `GNOME, KDE, XFCE, LXDE, Mozilla` and `MATE`, although other umbrella projects like `Yorba` would make sense too.

> [!NOTE]
> Components should only identify with an umbrella project if you use all their infrastructure and policies, for instance string freezes dates, bugtracker and source control instance.

\<icon/\>  
The `<icon/>` tag describes the component icon. It is mostly used for GUI applications (component-type `desktop-application`). It can be of the type `stock`, `cached`, `local`, or `url`.

`stock` icons are loaded from stock. The icon name should never include any file-extension or path.

`cached` icons are loaded from the AppStream icon cache. The icon tag should contain the icon file name, including its extension. It must not contain a full or relative path to the icon file. This icon type may have `width` and `height` properties. If targeting a hi-DPI screen, this icon type may have a `scale` property.

`local` icons are reserved for AppStream data installed by local applications or via 3rd-party application installers. They should specify a full file path. This icon type may have `width` and `height` properties. If targeting a hi-DPI screen, this icon type may have a `scale` property.

`remote` icons loaded from a remote URL. Currently, only HTTP urls are supported. This icon type should have `width` and `height` properties. If targeting a hi-DPI screen, this icon type may have a `scale` property.

If specified, the `scale` property is defined as in the [Freedesktop Icon Theme Specification](https://specifications.freedesktop.org/icon-theme-spec/latest/#definitions). It’s an integer value ≥1 indicating how many pixels in the image represent a logical pixel on the display, in each dimension. This allows icons for hi-DPI screens to be displayed at the same logical size as on lower resolution screens, but without upscaling artifacts.

Examples of the different methods to specify an icon:

``` XML
<icon type="stock">gimp</icon>
<icon type="cached">firefox.png</icon>
<icon type="cached" width="128" height="128" scale="2">firefox.png</icon>
<icon type="remote" width="64" height="64">https://example.com/icons/foobar.png</icon>
<icon type="local" width="64" height="64">/usr/share/pixmaps/foobar.png</icon>
```

Multiple `<icon/>` tags might be combined for one application, for example to define a `stock` icon and a `cached` icon. Software-Centers should always prefer the stock icon, if it is available, and fall back to the other icon types if they can not find it. The *libappstream* library makes it easy to do that.

The AppStream library will prefer `cached` over `local` over `remote` icons when setting the non-stock icon for the application.

\<categories/\>  
This tag can contain one or more `<category>` tags, describing the categories this component is located in. This tag is usually applied to components of type `desktop-application`, although it might be used by others later. This data is usually taken from Desktop files, a list of categories can be found in the [Freedesktop menu spec](https://specifications.freedesktop.org/menu-spec/latest/category-registry.html). Example:

``` XML
<categories>
    <category>Science</category>
    <category>Network</category>
    <category>Telephony</category>
</categories>
```

> [!NOTE]
> The tag `<appcategories>` with its `<appcategory>` child elements is deprecated API. AppStream parsers should handle these tags just like the `category` tags, there is no difference except for the name.

\<keywords/\>  
This tag can contain one or more `<keyword>` tags, describing keywords for the component, to make it easier to find in a software center.

This tag behaves like the [varlistentry_title](#tag-keywords) tag used in metainfo files, but is translated "as a whole", unlike its metainfo counterpart that has individual keywords translated. This means that the `<keywords/>` tag itself has a language property and contains only the translated keywords for the given language.

In case of type `desktop-application` components, this data is taken from .desktop files. For `addon` components, the upstream metadata file usually provides this tag.

Example:

``` XML
<keywords>
  <keyword>IDE</keyword>
  <keyword>development</keyword>
  <keyword>programming</keyword>
</keywords>
<keywords xml:lang="de">
  <keyword>IDE</keyword>
  <keyword>entwicklung</keyword>
  <keyword>programmierung</keyword>
</keywords>
```

\<screenshots/\>  
This tag can contain one or more `<screenshot>` tags, describing screenshots which are available for the software. A screenshot tag my have the attribute `type="default"`, marking it as the software's default screenshot, which primarily represents it in a software center.

The `screenshots` tag is described for metainfo files in [varlistentry_title](#tag-screenshots). In catalog metadata, the tag has the exact same format as in metainfo files. The metadata generator may add an arbitrary number of resized thumbnails for `image` type screenshots though.

Every static-image `<screenshot>` is defined by several images of different sizes. All images should have their width and hight set as arguments. Also, one of the images should be marked as `type="source"`, indicating that it is the unscaled version of the screenshot. Images of `type="thumbnail"` define thumbnails of the screenshot.

The metadata generator should scale the source image down to several thumbnails useful for the client to load. The recommended widths for thumbnail images are:

- *752* (large)

- *624* (normal)

- *112* (small)

- *1504* (large, HiDPI)

- *1248* (normal, HiDPI)

- *224* (small, HiDPI)

In order to support HiDPI screens, the thumbnails should also be available in their bigger sizes. A metadata generator should, however, never attempt to scale up a smaller image to a larger size, and just ship the smaller sizes instead. When scaling images to the respective thumbnail width, the image aspect ratio must be preserved, padding, cropping or stretching should not happen.

Optionally, a screenshot can contain a `<caption>` tag, describing the screenshot's caption. This is usually what the user can see on the image shown. The tag is translatable.

For `<screenshot>` tags that contain `video` elements, a catalog metadata generator may impose any restrictions to them, including completely removing them from the output, imposing filesize limits, etc. Upstream metainfo files should not rely on the videos being present and must always have a static screenhot for the software component as well.

Every image or video should have a full remote url set, usually pointing to a cache of images maintained by the repository vendor. Example:

``` XML
<screenshots>
  <screenshot type="default">
    <caption>FooBar showing kitchen-sink functionality.</caption>
    <caption xml:lang="de">FooBar beim Ausführen der Spühlbecken-Funktion.</caption>
    <image type="source" width="800" height="600">https://www.example.org/en_US/main.png</image>
    <image type="thumbnail" width="752" height="423">https://www.example.org/en_US/main-large.png</image>
    <image type="thumbnail" width="112" height="63">https://www.example.org/en_US/main-small.png</image>
  </screenshot>
  <screenshot>
    <video container="matroska" codec="av1" width="800" height="600">https://www.example.org/en_US/screencast.mkv</video>
  </screenshot>
  <screenshot>
     ....
  </screenshot>
</screenshots>
```

\<compulsory_for_desktop/\>  
The `<compulsory_for_desktop>` tag indicates that the component which the metadata belongs to is essential for the functionality of the defined desktop environment.

This tag is described in detail at [varlistentry_title](#tag-compulsory_for_desktop).

\<provides/\>  
This tag is described in detail at [Generic Component](#sect-Metadata-GenericComponent).

Distributors and software repository vendors must ensure that all things described in this tag are present in the package referenced in the associated `pkgname` tag (or in dependencies of it).

\<developer/\>  
The `<developer/>` tag as described in the specification for a generic component. See [varlistentry_title](#tag-developer) for more information.

\<launchable/\>  
This tag follows the same schema as described for metainfo files in [varlistentry_title](#tag-launchable).

\<releases/\>  
The `releases` tag and its `release` children are structured as described in [Release Information](#sect-Metadata-Releases).

Each `release` tag may have a `description` tag as child, containing a brief description of what is new in the release. The `description` tag is structured as described in [varlistentry_title](#tag-ct-description). This also applies to its translation rules.

The AppStream catalog XML generator may shorten overlong lists of releases to a smaller list, for example of 4 `release` tags. It may also convert ISO 8601 `date` properties of the metainfo file into an UNIX timestamp `timestamp` property. It should avoid generating metadata containing both properties on a `release` tag.

If a [varlistentry_title](#tag-releases) tag in a metainfo file references an `external` release description, the release description should be read either from the release file provided locally, or, if possible and provided, be downloaded from the URL referenced in the component's `releases` tag.

Example for a valid releases tag:

``` XML
<releases>
  <release version="1.8" timestamp="1424116753">
    <description>
      <p>This stable release fixes the following bug:</p>
      <ul>
        <li>CPU no longer overheats when you hold down spacebar</li>
      </ul>
    </description>
    <size type="download">12345678</size>
    <size type="installed">42424242</size>
  </release>
  <release version="1.2" timestamp="1397253600" />
  <release version="1.0" timestamp="1345932000" />
</releases>
```

In case a `<release/>` tag has a `<description/>` tag as parameter, describing the new release briefly, distributors are encouraged to provide 2-4 `<release/>` release tags for every component. If no description is provided, one tag is enough.

\<languages/\>  
This tag gives information about the translations a component provides, and to which extent the software is translated.

The tag is allowed to only occur once per component, and contains multiple `<lang/>` child nodes, which have a [language code](https://www.gnu.org/software/gettext/manual/html_node/Language-Codes.html) as value. Each `<lang/>` node may have a `percentage` property, which describes the percentage value to which a component has been translated.

The language data is expected to be extracted by the AppStream XML generator, and is not provided upstream. Generators may obtain the information from processing GNU Gettext files, which should cover most translation methods.

Tag example:

``` XML
<languages>
  <lang percentage="96">gu</lang>
  <lang percentage="94">ca@valencia</lang>
  <lang percentage="91">de</lang>
  <lang percentage="93">eo</lang>
</languages>
```

\<bundle/\>  
The optional `bundle` tag indicates that the described software is available as a software bundle via a 3rd-party application installer. The value of this tag is an identification string for the bundle.

Software centers may use the information of this tag to offer the user to install the software from 3rd-party sources, or just update an already installed software automatically via the normal update procedure. The `bundle` tag can coexist with the `pkgname` tag, in case a component is available from multiple sources.

The `type` property of this tag indicates which 3rd-party software installation solution the bundle belongs to. Currently supported solutions are:

- `package` - For distribution package names.

- `limba` - For [Limba Project](https://people.freedesktop.org/~mak/limba/) bundles.

- `flatpak` - For [Flatpak](https://flatpak.org/) bundles.

- `appimage` - For [AppImageKit](https://appimage.org/) bundles.

- `snap` - For [Snappy](https://snapcraft.io/) snap bundles.

- `tarball` - For plain and possibly compressed tarballs.

- `cabinet` - For cabinet firmware deployments.

- `linglong` - For [Linglong](https://linglong.dev/) bundles.

- `sysupdate` - For [systemd-sysupdate](https://www.freedesktop.org/software/systemd/man/latest/systemd-sysupdate.html) bundles.

Example:

``` XML
<bundle type="limba">foobar-1.0.2</bundle>
```

\<suggests/\>  
The optional `suggests` tag provides suggestions of other software made by this component. It follows the same schema as described for metainfo files in [varlistentry_title](#tag-suggests).

Additionally to the `upstream` type allowed for metainfo files, the catalog data also allows a `heuristic` type, which is added by automatic recommendation services, and might be based on the user's preferences. It is commonly injected into existing metadata via a `merge` pseudo-component.

Example:

``` XML
<suggests type="upstream">
  <id>org.kde.gwenview.desktop</id>
  <id>org.inkscape.Inkscape</id>
</suggests>
<suggests type="heuristic">
  <id>org.gimp.gimp.desktop</id>
</suggests>
```

\<content_rating/\>  
This optional tag follows the same schema as described for metainfo files in [varlistentry_title](#tag-content_rating).

\<agreement/\>  
This optional tag follows the same schema as described for metainfo files in [varlistentry_title](#tag-agreement), with the exception of `description` tags in its `agreement_section` child tags now following the same translation rules as the toplevel [varlistentry_title](#tag-ct-description) tag in catalog metadata.

### Example file

This is an example AppStream metadata file:

``` XML
<?xml version="1.0"?>
<components version="0.10">
  <component type="desktop-application">
    <id>org.mozilla.Firefox</id>
    <pkgname>firefox-bin</pkgname>
    <name>Firefox</name>
    <name lang="en_GB">Firefoux</name>
    <summary>Web browser</summary>
    <summary lang="fr_FR">Navigateur web</summary>
    <project_license>MPL-2.0</project_license>
    <keywords>
      <keyword>internet</keyword>
      <keyword>web</keyword>
      <keyword>browser</keyword>
      <keyword lang="fr_FR">navigateur</keyword>
    </keywords>
    <icon type="stock">web-browser</icon>
    <icon type="cached">firefox.png</icon>
    <categories>
      <category>network</category>
      <category>web</category>
    </categories>
    <url type="homepage">https://www.mozilla.com</url>
    <screenshots>
      <screenshot type="default">
        <image type="source" width="800" height="600">https://www.awesomedistro.example.org/en_US/firefox.desktop/main.png</image>
        <image type="thumbnail" width="200" height="150">https://www.awesomedistro.example.org/en_US/firefox.desktop/main-small.png</image>
      </screenshot>
    </screenshots>
    <provides>
      <binary>firefox</binary>

      <mediatype>text/html</mediatype>
      <mediatype>text/xml</mediatype>
      <mediatype>application/xhtml+xml</mediatype>
      <mediatype>application/vnd.mozilla.xul+xml</mediatype>
      <mediatype>text/mml</mediatype>
      <mediatype>application/x-xpinstall</mediatype>
      <mediatype>x-scheme-handler/http</mediatype>
      <mediatype>x-scheme-handler/https</mediatype>
    </provides>
  </component>
  <component>
    <id>org.freedesktop.PulseAudio</id>
    <name>PulseAudio</name>
    <summary>The PulseAudio sound server</summary>
    <url type="homepage">https://www.freedesktop.org/wiki/Software/PulseAudio/</url>
    <project_license>GPL-2.0+</project_license>
    <provides>
      <library>libpulse-simple.so.0</library>
      <library>libpulse.so.0</library>
      <binary>start-pulseaudio-kde</binary>
      <binary>start-pulseaudio-x11</binary>
    </provides>
    <release version="2.0"/>
  </component>
  <component type="font">
    <id>org.linuxlibertine.LinuxLibertine</id>
    <name>Linux Libertine</name>
    <summary>Linux Libertine Open fonts</summary>
    <provides>
      <font>LinLibertine_M.otf</font>
    </provides>
  </component>
  <!-- more components here! -->
</components>
```

## AppStream Catalog YAML

### Introduction

DEP-11 is a YAML implementation of the AppStream catalog specification, which is primarily used by Debian and its derivatives. This document describes the DEP-11 YAML. All AppStream support libraries available today are able to read both the YAML and the XML specification.

> [!IMPORTANT]
> If you want to use AppStream in your distribution, and are not based on Debian, please use the XML specification (unless you have strong reasons for preferring YAML). XML is the official format for AppStream catalog metadata.

Fields not mentioned in this document are not recognized by DEP-11 YAML parsers.

### File naming and location

Take a look at [File naming and location](#spec-asxml-filenaming) for AppStream XML files for reference. While the XML data belongs into the `xml` subdirectory in `/usr/share/swcatalog` (or `/var/(lib|cache)/swcatalog`), the YAML data is stored in the `yaml` subdirectory. All other rules affecting the XML apply the DEP-11 YAML as well, including the recommendation to compress the files with gzip and the icon search logic.

### General DEP-11 YAML structure

Each YAML file starts with a header document, which defines the basic properties of the metadata, which is followed by the actual metadata in form of one YAML document per AppStream component.

The header document contains the following fields, all of them are required or at least strongly recommended.

File  
This field identifies the file as DEP-11 file. Its value is always `DEP-11`.

    Field info: value-type:str, required:yes

Version  
The version of the AppStream specification this file was built for.

    Field info: value-type:str, required:yes

Origin  
Defines the repository-id this file belongs to. This usually matches the filename without extension. On Debian systems, it is the `<suite>-<component>` combination, e.g. `jessie-main`.

    Field info: value-type:str, required:yes

MediaBaseUrl  
The base URL for media (screenshots, icons, ...) referenced in the metadata file. If this is set, all urls in the document referencing media will be treated relative to the base url.

    Field info: value-type:str, required:no

Architecture  
Defines the architecture this data belongs to. This information is useful to resolve AppStream-ID conflicts on multiarch systems, which appear if the user has metadata for two architectures installed.

    Field info: value-type:str, required:no

Priority  
The priorization of this metadata file over other metadata.

    Field info: value-type:int, required:no

### Translated fields

Fields with translated values follow the following conventions:

1.  They are of type *dict*

2.  They must contain a key `C`, with the untranslated string as value

3.  All languages are represented with their locale name as key in the dict and the translated content as value (which is of type *str*, unless explicitly stated otherwise)

In this document, the type *localized* is used to indicate that the field contains translated values following this schema.

Example for a translated `Name` field:

``` YAML
Name:
  C: I am the untranslated string.
  be@latin: Redaktar naładaŭ
  bg: Настройки на програмите
  pl: Edytor konfiguracji
```

### Valid fields

This document describes all valid fields in the DEP-11 YAML specification. The requirements for the values are exactly the same as in the XML specification, and each field links to its correspondent XML tag for reference.

ID  
The `ID` field is a short unique and usually lower-cases identifier for the component. Depending on the component's type, different naming conventions apply.

See [varlistentry_title](#tag-ct-component-id).

    Field info: value-type:str, required:yes

Priority  
The `Priority` field sets the priority this component's metadata should have over other meadata in the pool. Data with a higher priority replaces data with a lower priority.

See [Valid tags for all component types](#spec-asxml-tags).

    Field info: value-type:int, required:no

Type  
The type of this component. Allowed values are:

- `generic` for [Generic Component](#sect-Metadata-GenericComponent)

- `desktop-application` for [Desktop Applications](#sect-Metadata-Application)

- `console-application` for [Console Applications](#sect-Metadata-ConsoleApplication)

- `addon` for [Addons](#sect-Metadata-Addon)

- `codec` for [Codecs](#sect-Metadata-Codec)

- `inputmethod` for [Input Methods](#sect-Metadata-InputMethod)

- `firmware` for [Firmware](#sect-Metadata-Firmware)

    Field info: value-type:str, required:yes

Merge  
The optional `Merge` field describes the merge strategy that should be applied when merging data of this component into its base. It may assume the values `append`, `replace` or `remove-component`.

See [Valid tags for all component types](#spec-asxml-tags) for a description on how merging works.

    Field info: value-type:str, required:no

Package  
The name of the package which needs to be installed in order to make this component available on the system.

See [varlistentry_title](#tag-ct-pkgname).

    Field info: value-type:str, required:yes

SourcePackage  
See [varlistentry_title](#tag-ct-source_pkgname).

    Field info: value-type:str

Name  
See [varlistentry_title](#tag-ct-name).

    Field info: value-type:localized, required:yes

Summary  
See [varlistentry_title](#tag-ct-summary).

    Field info: value-type:localized, required:yes

ProjectLicense  
See [varlistentry_title](#tag-ct-project_license).

    Field info: value-type:str

Description  
See [varlistentry_title](#tag-ct-description).

The markup for the description is the same as in the XML specification, so it can be read by anything parsing basic HTML markup.

    Field info: value-type:localized

Url  
See [varlistentry_title](#tag-ct-url).

The `Url` field contains the different url types as keys in its dict. Valid url types are defined in the main AppStream XML specification. All URL types must be lowercased.

Example:

``` YAML
Url:
  homepage: https://example.org
  faq: https://example.org/faq
  bugtracker: https://bugs.example.org/report-issue
```

    Field info: value-type:dict

ProjectGroup  
See [varlistentry_title](#tag-ct-project_group).

    Field info: value-type:str

Icon  
See [varlistentry_title](#tag-ct-icon).

The `Icon` field has the different icon types as keys for its dict.

stock  
Contains the stock icon name.

    Field info: value-type:str

cached  
Contains a list of dictionaries with the keys `width` and `height` of type *int* specifying the dimensions of the icon, as well as the key `name` of type *str* specifying the name of the icon in the cache.

    Field info: value-type:list ➟ dict

local  
Contains a list of dictionaries with the keys `width` and `height` of type *int* specifying the dimensions of the icon, as well as the key `name` of type *str* specifying the absolute filename pointing to the right icon.

    Field info: value-type:list ➟ dict

remote  
Contains a list of dictionaries with the keys `width` and `height` of type *int* specifying the dimensions of the icon, as well as the key `url` of type *str* which contains a HTTP(S) or FTP URL to the icon.

    Field info: value-type:list ➟ dict

    Field info: value-type:dict

Categories  
See [varlistentry_title](#tag-ct-categories).

This field follows its XML counterpart in almost all regards. The different XDG menu category names are encoded in the list, and are of type *str*.

Example:

``` YAML
Categories:
  - Network
  - Telephony
```

    Field info: value-type:list

Keywords  
See [varlistentry_title](#tag-ct-keywords).

This field contains the keywords for this component. The keys define the locales for the respective language, the values are of type *list* and contain the list of keywords for the respective language. An unlocalized `C` key must be present.

Example:

``` YAML
Keywords:
  C:
    - IDE
    - development
    - programming
  de:
    - IDE
    - entwicklung
    - programmierung
```

    Field info: value-type:translated(list)

Screenshots  
See [varlistentry_title](#tag-ct-screenshots).

The `Screenshots` field contains a list of screenshots. A screenshot is of type *dict* and contains the following keys:

default  
If `default` is `true`, the screenshot is selected as default screenshot. There has to be at least one screenshot which is marked as default.

    Field info: value-type:bool

source-image  
Describes the source image for this screenshot. If this field is present, `videos` must not be present as well. The field valus is a dictionary with the following keys:

- `height`

  The image height (value-type:*int*)

- `width`

  The image width (value-type:*int*)

- `url`

  The full image url, or the url component added to `MediaBaseUrl`, if defined (value-type:*str*).

- `lang`

  The language this screenshot image is translated in. The value is a locale string. (value-type:*str*, required:*no*)

    Field info: value-type:dict, required:conditional

thumbnails  
A list of an arbitrary number of screenshots. All screenshots are of type *dict* and must contain the same keys as described for `source-image`. This key must not be present if `videos` is present.

    Field info: value-type:list, required:no

videos  
Contains a list of video dicts for this screenshot. If this field is present, `source-image` must not be present as well. The field valus is a dictionary with the following keys:

- `container`

  The video container format (value-type:*str*, values as described in the XML specification)

- `codec`

  The video codec format (value-type:*str*, values as described in the XML specification)

- `height`

  The video height (value-type:*int*)

- `width`

  The video width (value-type:*int*)

- `url`

  The full video url, or the url component added to `MediaBaseUrl`, if defined (value-type:*str*).

- `lang`

  The language this screenshot video is translated in. The value is a locale string. (value-type:*str*, required:*no*)

    Field info: value-type:list(dict), required:conditional

caption  
A caption for this screenshot.

    Field info: value-type:localized

Example for a `Screenshots` field containing one screenshot:

``` YAML
Screenshots:
  - default: true
    caption:
      C: Foobar showing kitchen-sink functionality
      si: Foobar shoeewing kischän-sünk funzionality
    source-image:
      height: 800
      url: https://www.example.org/en_US/main.png
      width: 600
    thumbnails:
      - height: 423
        width: 752
        url: https://www.example.org/en_US/main-large.png
      - height: 63
        width: 112
        url: https://www.example.org/en_US/main-small.png
  - source-video:
      container: matroska
      codec: av1
      height: 900
      url: https://www.example.org/en_US/screencast.mkv
      width: 1600
```

    Field info: value-type:list

CompulsoryForDesktop  
See [varlistentry_title](#tag-ct-compulsory_for_desktop).

    Field info: value-type:str

Provides  
See [varlistentry_title](#tag-ct-provides).

The `Provides` field is of type *dict* and can have the following keys set with the described allowed values:

libraries  
A list of provided library names.

    Field info: value-type:list(str)

binaries  
A list of provided binaries in `PATH`.

    Field info: value-type:list(str)

fonts  
A list of provided fonts. Each font entry is of type *dict* and has a `name` key.

    Field info: value-type:list(dict)

modaliases  
A list of modalias globs representing the hardware types this component handles.

    Field info: value-type:list(str)

mediatypes  
A list of media types (MIME types) this component can handle.

    Field info: value-type:list(str)

firmware  
A list of provided firmware. Each firmware entry is of type *dict* and has a `type` key, which has either `runtime` or `flashed` as value. Firmware of type `flashed` has a `guid` key, containing the GUID of the device the firmware is flashed on, while firmware of type `runtime` has a `file` key, containing the firmware filename which the kernel is looking for.

    Field info: value-type:list(dict)

python3  
A list of Python 3 modules this component provides.

    Field info: value-type:list(str)

dbus  
A list of provided DBus services. Each service entry in the list is of type *dict* and has a `type` key, which has either `system` or `user` as value. `user` means the DBus service name is for a user/session service, while `system` means it describes a system service. The `service` key contains the name of the DBus service file. All dict values are of type *str*.

    Field info: value-type:list(dict)

ids  
A list of component-IDs that this component is able to provide all functionality of.

    Field info: value-type:list(str)

    Field info: value-type:dict

DeveloperName  
See [varlistentry_title](#tag-ct-developer).

    Field info: value-type:dict

Launchable  
See [varlistentry_title](#tag-ct-launchable).

A dictionary containing the launchable-type as key, and a list of IDs used for launching the application as value.

Example:

``` YAML
Launchable:
  desktop-id:
    - org.gnome.Sysprof2.desktop
```

    Field info: value-type:dict(list)

Releases  
See [varlistentry_title](#tag-ct-releases).

The `Releases` contains a list of releases sorted latest-to-oldest, where each list items contains the following fields/keys:

version  
The version number of this release.

    Field info: value-type:str, required:yes

type  
The release type. Allowed values are:

- `stable`

- `development`

By default, if no release type is defined, `stable` is assumed.

    Field info: value-type:str, required:no

urgency  
How important it is to install the new release as an update. Allowed values are:

- `low`

- `medium`

- `high`

- `critical`

If no urgency is defined, a `medium` urgency is implicitly assumed.

    Field info: value-type:str, required:no

unix-timestamp  
The UNIX timestamp of when this software was released.

One of the `unix-timestamp` or `date` fields must be present.

    Field info: value-type:int, required:maybe

date  
The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) complete date of when this software was released.

One of the `unix-timestamp` or `date` fields must be present.

    Field info: value-type:str, required:maybe

description  
A description of this release. May contain allowed HTML markup.

    Field info: value-type:localized

issues  
A list of dictionaries describing the issues resolved by this release. The dictionaries contain a `id` key for the value of an issue as described in the XML specification, as well as a `type` and `url` key for the tag properties of the same name described in the XML AppStream specification.

    Field info: value-type:list(dict)

artifacts  
A list of dictionaries describing the artifacts published for this release. Refer to the XML specification for details, which is mapped to YAML following the usual scheme.

    Field info: value-type:list(dict)

It is recommended to order this list starting with the latest timestamp to the oldest one.

Example:

``` YAML
Releases:
  - version: '1.8'
    unix-timestamp: 1424116753
    description:
      C: |
        <p>This stable release fixes the following bug:</p>
        <ul>
          <li>CPU no longer overheats when you hold down spacebar</li>
        </ul>
  - version: '1.2'
    unix-timestamp: 1397253600
  - version: '1.0'
    unix-timestamp: 1345932000
```

    Field info: value-type:list(dict)

Languages  
See [varlistentry_title](#tag-ct-languages).

The languages list is a list of dictionaries. They must contain a `percentage` key, indicating the completion of translation for this language, and a `locale` key, with the locale string as value.

Example:

``` YAML
Languages:
  - locale: gu
    percentage: 96
  - locale: ca@valencia
    percentage: 94
  - locale: de
    percentage: 91
  - locale: eo
    percentage: 93
```

    Field info: value-type:list(dict)

Bundles  
See [varlistentry_title](#tag-ct-bundle).

The `Bundles` contains a list of dictionaries with the keys `type`, having the ID for a specific bundling system (e.g. `flatpak` or `limba`) as value, and `id` for the associated bundle-id. See the XML tag description for information on all valid bundling systems.

Example:

``` YAML
Bundles:
  - type: limba
    id: foobar-1.0.2
```

    Field info: value-type:list

Extends  
See [varlistentry_title](#tag-extends).

Contains a list of AppStream IDs of the other component extended by the described component. This field may only be used with component-type `addon`.

    Field info: value-type:list(str)

Suggests  
See [varlistentry_title](#tag-ct-suggests).

A list of dictionaries containing suggested software components. The dictionaries must have a `type` key with the string value `upstream` or `heuristic` depending on where the suggestion originates from. The also must have a `ids` key containing a list of component-ids of the suggested software.

Example:

``` YAML
Suggests:
  - type: upstream
    ids:
      - org.example.Awesome
  - type: heuristic
    ids:
      - org.example.Test1
      - org.example.Test2
```

    Field info: value-type:list(dict)

ContentRating  
See [varlistentry_title](#tag-ct-content_rating).

A dictionary containing the rating system as key, and a dictionary of rating-values as value. The value-dictionary itself has the content rating IDs as keys and the intensity values as values. The intensity values as well as IDs and rating system names match the values from the XML exactly.

Example:

``` YAML
ContentRating:
  oars-1.0:
    drugs-alcohol: moderate
    language-humor: mild
```

    Field info: value-type:dict(dict)

Requires, Recommends & Supports  
See [varlistentry_title](#tag-relations).

A list of dictionaries containing the referenced items. The dictionaries in the list must have one key denoting the item type, which has the respective item value as value. Refer to the XML description for a list of possible types.

Each dictionary may have a `version` field with contains a version comparison string. The first two characters denote the version comparison operation, and are followed by the version number to be compared with. The comparison operation may be one of:

- `==` - Equal to

- `!=` - Not equal to

- `<<` - Less than

- `>>` - Greater than

- `<=` - Less than or equal to

- `>=` - Greater than or equal to

Example:

``` YAML
Recommends:
- memory: '2500'
- modalias: usb:v1130p0202d*
Requires:
- kernel: Linux
  version: '>= 4.15'
- id: org.example.TestDependency
  version: == 1.2
```

    Field info: value-type:list(dict)

Agreements  
See [varlistentry_title](#tag-ct-agreement).

A list containing the agreements as dictionaries, with a `sections` key containing a list of sections. All dict values are the same as the respective XML tag values / properties.

Example:

``` YAML
Agreements:
- type: eula
  version_id: 1.2.3a
  sections:
  - type: intro
    name:
      C: Intro\n"
    description:
      C: >-
        <p>If it breaks, you get to keep both pieces.</p>
```

    Field info: value-type:list(dict)

Tags  
See [varlistentry_title](#tag-tags).

    Field info: value-type:list(dict)

Example:

``` YAML
Tags:
- namespace: lvfs
  tag: vendor-2021q1
- namespace: plasma
  tag: featured
```

References  
See [varlistentry_title](#tag-references).

    Field info: value-type:list(dict)

Example:

``` YAML
References:
- type: doi
  value: 10.1000/182
- type: citation_cff
  value: https://example.org/CITATION.cff
- type: registry
  value: SCR_000000
  registry: SciCrunch
```

Custom  
See [varlistentry_title](#tag-custom).

    Field info: value-type:list(dict)

### Example YAML file

This is an example AppStream DEP-11 metadata file:

``` YAML
---
File: DEP-11
Version: '0.8'
Origin: chromodoris-main
MediaBaseUrl: https://metadata.tanglu.org/appstream/media/
---
Type: desktop-application
ID: gconf-editor.desktop
Icon:
  cached: gconf-editor_gconf-editor.png
Name:
  C: Configuration Editor
  be@latin: Redaktar naładaŭ
  bg: Настройки на програмите
  pl: Edytor konfiguracji
Package: gconf-editor
Summary:
  C: Directly edit your entire configuration database
  ar: حرّر مباشرة كامل قاعدة بيانات الإعدادات.
  de: Direkten Zugriff auf Ihre gesamte Konfigurationsdatenbank erlangen
Categories:
  - GNOME
  - GTK
  - System
---
Type: desktop-application
ID: kmplayer.desktop
Icon:
  cached: kmplayer_kmplayer.png
Name:
  C: KMPlayer
  hi: केएम-प्लेयर
  hne: केएम-प्लेयर
  ku: KMLêdar
  pa: KM-ਪਲੇਅਰ
  sr: КМ‑плејер
  sr@ijekavian: КМ‑плејер
  sv: Kmplayer
Package: kmplayer
Summary:
  C: KDE interface for MPlayer
Categories:
  - Qt
  - KDE
  - AudioVideo
  - Player
Provides:
  mediatypes:
    - application/ogg
    - application/smil
    - application/vnd.ms-asf
    - application/vnd.rn-realmedia
    - application/x-kmplayer
    - video/webm
    - video/x-avi
---
ID: texstudio.desktop
Type: desktop-application
Package: texstudio
Name:
  C: TeXstudio
Summary:
  C: LaTeX development environment
  fr: Environnement de développement LaTeX
Description:
  C: <p>TeXstudio is an integrated writing environment for creating LaTeX documents. It integrates editing,
    building and viewing into a single frontend.</p><p>Our goal is to make writing LaTeX as easy and comfortable
    as possible. This is achieved through a rich feature set including:</p>
Icon:
  cached: texstudio_texstudio.png
Keywords:
  C:
    - editor
    - latex
    - pdflatex
    - xelatex
    - lualatex
    - context
    - bibtex
ProjectLicense: GPL-2.0
Url:
  homepage: https://texstudio.sourceforge.net/
Categories:
  - Office
  - Publishing
Provides:
  mediatypes:
    - text/x-tex
Screenshots:
  - default: true
    source-image:
      height: 756
      url: texstudio_2.8.4+debian-3_amd64/screenshots/source/screenshot-1.png
      width: 1344
    thumbnails:
      - height: 423
        url: texstudio_2.8.4+debian-3_amd64/screenshots/752x423/screenshot-1.png
        width: 752
      - height: 351
        url: texstudio_2.8.4+debian-3_amd64/screenshots/624x351/screenshot-1.png
        width: 624
      - height: 63
        url: texstudio_2.8.4+debian-3_amd64/screenshots/112x63/screenshot-1.png
        width: 112
```

## Icon Cache

### Introduction

In order to display icons in software-centers, distributors should offer a repository of cached icons for applications defined in their AppStream XML files. The icons should be PNG files or vectorgraphics (PNG is preferred) and match the name referenced in the applications .desktop file. Their size should be 64x64px, it is okay to just provide one size.

### Filesystem locations

All icons of type `cached` must be placed in `/usr/share/swcatalog/icons/%{origin}/%{size}/` or `/var/(lib|cache)/swcatalog/icons/%{origin}/%{size}/`, where `origin` is the AppStream data origin defined in the AppStream data file (see [General XML structure](#spec-asxml-general)), and `size` is `64x64` or `128x128` depending on the size of the icon. And icon might be present with different sizes in both directories. When finding cached icons, they must only be searched for in the same location where the accompanying catalog metadata is located. For example, icons for `/var/lib/swcatalog/xml/debian-jessie-main.xml.gz` must only be looked up in `/var/lib/swcatalog/icons/debian-jessie-main/` and not also in locations in `/var/cache/` or elsewhere.

For example the cache icon `krita.png` of a component in a data file with the origin `jessie` should be stored in `/usr/share/swcatalog/icons/jessie/64x64/krita.png` (or in the `/var/cache` location).

Icon scaling factors commonly used for HiDPI display support are part of the size-directory filename and are separated from the regular size via an `@` sign. If the scaling factor is 1, it must be omitted from the directory name. For example, if the icon scaling factor is `2` for icons of size `64x64` from origin `jessie`, the icon must be placed in `/usr/share/swcatalog/icons/jessie/64x64@2/`.

> [!NOTE]
> In order to support the old icon cache layout, client applications may also look for icons in the folder below the size-directories, assuming that the icons placed there are of size `64x64` pixels.

# Miscellaneous

This chapter describes additional features AppStream provides that are related to the metadata specification.

## Version Comparison Algorithm

### Introduction

The AppStream specification requires the presence of version numbers in various locations, and AppStream-using clients will occasionally need to compare version numbers in order to determine the latest version. This document describes how version comparisons should be performed.

### Algorithm

AppStream's version comparison algorithm is a compromise between the ones used by the Fedora and Debian Linux distributions (after RPM's algorithm was extended to handle the tilde character like Debian). It should compare most versions like DPKG/RPM, except for letters after a dot, so e.g. `1.0 << 1.a` (like in Debian, but unlike in RPM). Unfortunately due to differences between the RPM and DPKG worlds, this issue can not be resolved without breakage. The algorithm is described for Debian [here](https://manpages.debian.org/unstable/dpkg-dev/deb-version.5.en.html#Sorting_algorithm), the description is also reproduced below:

The version strings are compared from left to right.

First the initial part of each string consisting entirely of non-digit characters is determined. These two parts (one of which may be empty) are compared lexically. If a difference is found it is returned. The lexical comparison is a comparison of ASCII values modified so that all the letters sort earlier than all the non-letters and so that a tilde sorts before anything, even the end of a part. For example, the following parts are in sorted order: `~~`, `~~a`, `~`, the empty part, `a`.

Then the initial part of the remainder of each string which consists entirely of digit characters is determined. The numerical values of these two parts are compared, and any difference found is returned as the result of the comparison. For these purposes an empty string (which can only occur at the end of one or both version strings being compared) counts as zero.

These two steps (comparing and removing initial non-digit strings and initial digit strings) are repeated until a difference is found or both strings are exhausted.

### Recommendations

For meaningful version numbers, consider following [semantic versioning](https://semver.org/).

A version number should always start with a number. Do not start version numbers with a letter or make them consist entirely of letters, e.g. `BETA` is not a version number.

If you want to denote a prerelease, consider appending the prerelease identifier string after a tidle. For example use `1.0~alpha1` for an alpha release of the upcoming `1.0` release. The alpha release will then considered lower than the final release.

Avoid using any epochs (colons) in your upstream version numbers. Versions like `1:2.4` will cause problems with downstreams.

### Implementation

You can read AppStream's code for version comparisons [here](https://github.com/ximion/appstream/blob/master/src/as-vercmp.c).

If you want to quickly test version comparisons for your software and arbitrary versions, consider using the `vercmp` subcommand of the `appstreamcli` utility.

Examples:

    $ appstreamcli vercmp 1.0 2.0
    1.0 << 2.0
    $ appstreamcli vercmp 2.0 2.0~a1
    2.0 >> 2.0~a1
    $ appstreamcli vercmp 2.4 lt 2.1
    false: 2.4 >> 2.1
    $ appstreamcli vercmp 1.2.4 gt 1.2.3
    true: 1.2.4 >> 1.2.3

## URI Handler

### Introduction

In order to allow installation of AppStream components from websites, software-centers implementing AppStream may choose to also support the `appstream:` URIs.

This allows upstream projects to trigger an installation of their application from their homepage on any supporting distribution. It also is helpful for web-based software-centers.

### URI schema

Software centers handling `appstream:` URIs should provide a handler for the `x-scheme-handler/appstream` mimetype. An AppStream URI follows the schema `appstream:%{component-id}`.

If a component is known by multiple alternative IDs, more component IDs may be defined in a comma-separated list in the query component of the URI using the `alt` key. This may be necessary if an application has switched its ID, but the same URI may be called on systems which still only know the old ID. Software centers must try to find the initial ID first and, failing to find it in their catalog, may try the alternative IDs in order of appearance in the query.

Example HTML code:

``` HTML
<a href="appstream:org.kde.discover.desktop">Install KDE Discover</a>
<a href="appstream:org.gnome.Software.desktop">Install GNOME-Software</a>
<a href="appstream:org.freedesktop.appstream.cli">Install AppStreamCLI</a>
<a href="appstream:org.example.foo?alt=com.github.darthvader.foo,net.launchpad.vader.foo">Install Foo</a>
```

### AppStream Buttons

If you want to allow users to open your software in their local software center from your website, you might want to use one of the easily recognizable AppStream buttons for your `appstream:` link.

![[SVG](https://github.com/ximion/appstream/blob/master/docs/images/src/svg/appstream-button1.svg)](appstream-button1.svg)

![[SVG](https://github.com/ximion/appstream/blob/master/docs/images/src/svg/appstream-button2.svg)](appstream-button2.svg)

# Metadata Quickstart

These pages are designed to give upstream authors compressed information on how to write metadata for their applications. The documents describe just the basic information, and don't resemble the whole specification, to give upstreams an easy way to get started with AppStream.

## For GUI application upstream maintainers

### Introduction

Every software center that exists allows the user to look at screenshots and a long description of the application before it is installed. For most users it allows them to answer the question “Do I want to install this application?”. Traditionally in Linux distributions, we have none of this data for the vast majority of our desktop user-installable applications. The packages-descriptions are describing all contents of a package, and not just a single application. They are also often written in a technical language and refer to other packages, which makes it hard for beginners to understand what the application they want to install really does. Additionally, if you are not using Debian or Ubuntu, the package descriptions are often untranslated. Also, packages do not provide some metadata users might be interested in before installing an application.

To solve this, we have defined a new data file, which the upstream project can optionally translate using the same technique as [Desktop Entry files](https://specifications.freedesktop.org/desktop-entry-spec/latest/) or GSetting schemas. The application metainfo specification is a subset of the AppStream metadata (see [AppStream Catalog XML](#sect-AppStream-XML)) and extends the generic component metadata with fields specific for applications (see [Generic Component](#sect-Metadata-GenericComponent)).

The application-metainfo files override any values which are automatically fetched by the AppStream data generator. Applications can ship one or more files in `/usr/share/metainfo/%{id}.metainfo.xml`.

Application metainfo files can - just like all other metainfo files - be translated. See the section about translation for more information about that.

> [!NOTE]
> All tags defined in the generic component specification are valid for components of type `desktop-application` as well, an application is just defined as a specialized component, which has the additional benefit of being displayed in a software-center application.

> [!TIP]
> To get you started quickly, the AppStream project provides a web-based form to quickly generate valid metainfo XML for some of the most common use cases. Check it out on [freedesktop.org/software/appstream/metainfocreator](https://www.freedesktop.org/software/appstream/metainfocreator/#/).

### Example file

The file should contain something like this:

``` XML
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2013 First Lastname <your@email.com> -->
<component type="desktop-application">
  <id>org.gnome.gnome-power-statistics</id>
  <metadata_license>FSFAP</metadata_license>
  <project_license>GPL-2.0+</project_license>
  <name>Power Statistics</name>
  <summary>Observe power management</summary>

  <description>
    <p>
      Power Statistics is a program used to view historical and current battery
      information and will show programs running on your computer using power.
    </p>
    <p>Example list:</p>
    <ul>
      <li>First item</li>
      <li>Second item</li>
    </ul>
    <p>
      You probably only need to install this application if you are having problems
      with your laptop battery, or are trying to work out what programs are using
      significant amounts of power.
    </p>
  </description>

  <launchable type="desktop-id">org.gnome.gnome-power-statistics.desktop</launchable>

  <screenshots>
    <screenshot type="default">
      <caption>The options dialog</caption>
      <image>http://www.hughsie.com/en_US/main.png</image>
    </screenshot>
    <screenshot>
      <image>http://www.hughsie.com/en_US/preferences.png</image>
    </screenshot>
  </screenshots>

  <url type="homepage">http://www.gnome.org/projects/en_US/gnome-power-manager</url>
  <project_group>GNOME</project_group>

  <provides>
    <binary>gnome-power-statistics</binary>
  </provides>

  <releases>
    <release version="3.12.2" date="2013-04-12">
      <description>
        <p>Fixes issues X, Y and Z</p>
      </description>
    </release>
  </releases>
</component>
```

### Recommended metadata file contents

This is a list of tags you might want to define for your application. For a full list of all possible tags, take a look at the definition of a generic component ([XML Specification](#spec-component-filespec)) and an application-component ([File specification](#spec-appdata-filespec)).

\<id/\>  
The `<id/>` tag value contains the unique identifier for this application. It is usually modeled after the .desktop filename and follows a reverse-DNS scheme. For the full naming guidelines see [varlistentry_title](#tag-id-generic).

Example: If your application's `.desktop` file is named `org.example.FooBar.desktop`, a good component-id would be `org.example.FooBar`.

\<metadata_license/\>  
The `<metadata_license/>` tag is indicating the content license that you are releasing the one metainfo file under. This is not typically the same as the project license. Omitting the license value can result in your data not being incorporated into the distribution metadata (so this is a required tag).

A [permissive](https://en.wikipedia.org/wiki/Permissive_software_licence) license ensures your data can be combined with arbitrary other data in one file, without license conflics (this means copyleft licenses like the GPL are not suitable as metadata license). Possible license identifiers include:

- FSFAP

- CC0-1.0

- CC-BY-3.0

- CC-BY-SA-3.0

- GFDL-1.3

- MIT

The license codes correspond to the identifiers found at the [SPDX OpenSource License Registry](http://spdx.org/licenses/). Take a look at [varlistentry_title](#tag-metadata_license) for more details about this tag.

If you are unsure about which license to pick, the [FSFAP](https://spdx.org/licenses/FSFAP.html) or FSFUL license statement is usually a good choice, as it is short and safe to combine with other licenses.

\<project_license/\>  
The `<project_license/>` tag is indicating the license(s) this application is released under. Take a look at the specification of the [varlistentry_title](#tag-project_license) tag for details on how to properly use it.

\<name/\>  
It is highly recommended to have this tag present and contain a name of your application as value.

In theory you can omit this tag and have the AppStream generator of a Linux distribution automatically use the `Name` field of the associated `.desktop` file (In which case one [varlistentry_title](#qsr-app-launchable-info) tag must be present). However, a large amount of tools expect the metainfo file to be complete and self-sufficient now, which is why omitting this tag will render it invalid for tools like Flatpak and others use cases which do not involve a metadata preprocessing step.

If no `name` tag (and no `Name` desktop-entry field) is present, the metadata is considered invalid and will be ignored by the AppStream generator.

\<summary/\>  
It is highly recommended to have this tag present and contain a brief summary of what your application is about.

In theory you can omit this tag and have the AppStream generator of a Linux distribution automatically use the `Comment` field of the associated `.desktop` file (In which case one [varlistentry_title](#qsr-app-launchable-info) tag must be present). However, a large amount of tools expect the metainfo file to be complete and self-sufficient now, which is why omitting this tag will render it invalid for tools like Flatpak and others use cases which do not involve a metadata preprocessing step.

If no `summary` tag (and no `Comment` desktop-entry field) is present, the metadata is considered invalid and will be ignored by the AppStream generator.

\<description/\>  
The long description is an important part of the file. Important things to consider when writing the application description:

- Include 2-3 paragraphs of interesting easy to read prose.

- Ensure you provide a description of what the application actually does.

- Describe any important features.

- Do not use possily trademarked product names when refering to competitors.

- Break down each paragraph into easily translated paragraphs.

- Use lists sparingly.

- Never refer to installable items as packages.

- Never start the first sentence with "This application..."

- Try not use more than 100 words.

- Do not be too geeky. Aim for an intelligent semi-technical reader.

- Don't mention what language an application is written in, users don't care

- Only mention what the application can do now, rather than what is planned

Do not assume the format is HTML. Only paragraph, ordered list and unordered list are supported at this time, as well as emphasis and inline code. See [varlistentry_title](#tag-description) for more information.

In metainfo files, this tag should be translated by-paragraph, meaning that in a translated file, each translated `<p/>` child has a language property.

\<launchable/\>  
This tag indicates a possible method to launch the software. Usually you want the application to be launchable by its .desktop file ID.

The tag makes it possible for software centers to offer launching an application immediately after installation. It also connects the metainfo file with a .desktop file, so AppStream metadata generators and the distribution can absorb its metadata into the final AppStream output.

See [varlistentry_title](#tag-launchable) for a detailed description of the tag. Example:

``` XML
<launchable type="desktop-id">org.gnome.Sysprof2.desktop</launchable>
```

\<screenshots/\>  
A screenshot presents your application to the outside world, and could be seen by hundreds or thousands of people.

The `<screenshots/>` tag contains multiple `<screenshot/>` children, where at least one of them must have the property `type="default"` to indicate the application's primary screenshot. Every `<screenshot/>` tag must have at least one `<image/>` child, which may define the width and height of the referenced image in it's properties. The value of the `<image/>` tag is a direct URL to a screenshot uploaded to a public location on the web.

Optionally, a `<screenshot/>` tag may have a `<caption/>` child, defining a short (not more than 180 characters!) description of what the user can see on the referenced screenshot.

Screenshots are an important part of how people choose which applications to install, so it's important to get them right. Consistent, good looking screenshots will make your application look more attractive and will expand your userbase. Consistent screenshots also provide a more predictable experience for people using the software center.

Screenshot size, shape and format:

- Use an aspect ratio that works for the applications's UI, use 16:9 as long as that is sensible.

- Screenshots should ideally be in the PNG format, but JPEG and WebP images are also fine. Keep in mind though that the images are converted into PNG in any case by the distributor of a software collection.

- Do not scale screenshots below their original size.

- Generally try to keep any window size small to make the content more visible when it is scaled down in software center frontends

Basic guidelines for things to include (and not include) in your screenshots:

- Use the default theme, icon set, font, and window decorations of your desktop environment. Avoid including your own tweaks to the standard distribution offering.

- Screenshots should be taken with English as the display language.

- Your default screenshot should give an overview of your application, and should show an entire application window. It can be combined with screenshots which show specific aspects of the application.

- Screenshots should not show anything outside the application's windows (including the background wallpaper). If you are taking a screenshot of the whole window, use your screenshot tool's "window" mode (including any window borders in the screenshot, and ensuring that the resulting image has an alpha mask for the rounded corners).

- Some applications, such as games, primarily run full screen. Screenshots of these applications should be taken with the application running full screen - there should be no visible window controls in the screenshot.

- Use window screenshots with baked-in default shadows

- Do not include content that might be considered offensive or controversial, and avoid showing personal information. Remember that your screenshots will be visible to the internet at large.

Additional advice on how to take effective screenshots:

- Each of your screenshots should focus on one thing and one thing only. Screenshot one window at a time, and avoid having overlapping windows or user interface elements. This will make it much easier for people to understand what you are showing them.

- If a screenshot is demonstrating a single feature or aspect of the application, crop it to exclude irrelevant detail.

- Screenshots often need to feature content, such as images, documents, web pages or videos. Don’t show your application in an ‘empty’ state, and try and use high quality content which has positive associations and broad appeal.

- In general, you shouldn't include the mouse pointer in your screenshots.

Some advice for a good screenshot caption:

- The caption should be short. Try not to use more than a few words to describe the image.

- Try not to state the obvious: "Main window displaying an image" is something the user can see on the screenshot already.

- Try not to repeat the application's name in the caption.

- Do not end your caption with a fullstop.

Some examples of good and bad screenshot choices:

|  |  |
|----|----|
| ![**BAD:** Not on Linux](screxample_xterm-bad.png) | ![**GOOD**](screxample_geany-good.png) |
| ![**BAD:** Not 16:9, shows the whole desktop and too many small windows](screxample_xmedcon-bad.png) | ![**GOOD:** No window border required for fullscreen game](screxample_xonotic-good.png) |
| ![**BAD:** Uses custom font, custom color theme and is not 16:9](screxample_gameconqueror-bad.png) | ![**GOOD**](screxample_wireshark-good.png) |

\<url/\>  
This is a recommended tag for links of type `homepage`. Links of type `homepage` should be a link to the upstream homepage for the application.

For other possible values, tage a look at the tag's description at [varlistentry_title](#tag-url).

\<project_group/\>  
This tag is described for generic components at [varlistentry_title](#tag-project_group). You should use it for your application if appropriate.

\<developer/\>  
The `<developer/>` tag is designed to represent the developers or project responsible for development of the project described in the metadata.

See [varlistentry_title](#tag-developer) for its detailed generic description.

\<update_contact/\>  
The `<update_contact/>` tag is an optional tag which can be added to provide an email address distributors can use to contact the project about invalid or incomplete metadata, or in case the specification has changed, about old metadata. It can also be used to ask general questions in case of an update of the component described in the metadata file. Spam protection using `_AT_` is valid.

Example:

``` XML
<update_contact>developer_AT_example.com</update_contact>
```

### Suggested metadata file contents

It is useful to add these tags as well if they make sense for the described application. They are not strictly required to be present though.

\<releases/\>  
The application metainfo may include one `<releases/>` tag, which has one or multiple `<release/>` subnodes to define the version and release date of this application. For details, see [varlistentry_title](#tag-releases) .

It is very useful to attach short release-notes to a `<release/>` using the `<description/>` subnode. These release-notes should contain brief information about what is new in the release, in a way which is understandable by non-technical users.

\<provides/\>  
This tag is described in detail for generic components at [varlistentry_title](#tag-provides).

If your application ships a binary in a location in the default `PATH`, it is useful to add at least a child of type `<binary/>` to make it easily possible to find your application's metadata using the name of its binary.

## For upstream projects providing addons

### Introduction

Some software installed on the system is extensible via addons. To allow the user to install addons for software that is already available on the system, AppStream defines an `addon` component type. Software centers will usually group these components together with their host component and display them for installation. Extensible software may also access the AppStream data pool provided by the distribution or other software source directly, to offer installing missing addons from within the application.

Software which provides addons can ship one or more files in `/usr/share/metainfo/%{id}.metainfo.xml`.

> [!TIP]
> To get you started quickly, the AppStream project provides a web-based form to quickly generate valid metainfo XML for some of the most common use cases. Check it out on [freedesktop.org/software/appstream/metainfocreator](https://www.freedesktop.org/software/appstream/metainfocreator/#/).

### Example file

The file should contain something like this:

``` XML
<?xml version="1.0" encoding="UTF-8"?>
<component type="addon">
  <id>org.gnome.gedit.gedit_bookmarks</id>
  <extends>org.gnome.gedit</extends>
  <name>Bookmarks</name>
  <summary>Easy document navigation with bookmarks</summary>
  <url type="homepage">https://wiki.gnome.org/Apps/Gedit/ShippedPlugins</url>
  <url type="bugtracker">https://bugzilla.gnome.org/enter_bug.cgi?product=gedit&amp;component=Plugins</url>
  <metadata_license>FSFAP</metadata_license>
  <project_license>GPL-2.0+</project_license>
</component>
```

### Metadata file contents

This is a list of tags you might want to define for your application. For a full list of possible tags, take a look at the definition of a generic component ([XML Specification](#spec-component-filespec)) and an addon component ([File specification](#spec-addondata-filespec)).

\<id/\>  
For addons, there is no strict rule for the component-ID. You should just ensure that you pick a unique name.

It is highly recommended to apply a `application_name-plugin_name` naming scheme for your addon-id.

\<extends/\>  
This tag is refers to the ID of the component this addon is extending. For desktop applications, this is usually the name of their `.desktop` file.

This tag is described in detail for addon components at [varlistentry_title](#tag-extends).

\<name/\>  
Each addon component needs a `<name/>` tag, giving the addon a human-readable name.

> [!NOTE]
> Don't put the application name you are extending in the `<name/>` - so you want to use `Bookmarks` rather than `GEdit Bookmarks`

\<summary/\>  
The `<summary/>` tag follows the basic structure of a [varlistentry_title](#tag-summary) as described in the specification. It is a required tag for an addon component.

Some useful hints for finding a good addon summary:

- Don't put the application name you are extending in the `<summary/>` - so you want to use `Easy document navigation with bookmarks` rather than `Easy document navigation with bookmarks in GEdit`.

- Don't use long or short descriptions. Ideally `<summmary/>` should be less than `101` and more than `8`.

\<url/\>  
It is recommended to include links of types `homepage` and `bugtracker`. You can omit the `<url/>` if it's the same as the upstream project.

Links of type `homepage` should be a link to the upstream homepage for the addon.

Links of type `bugtracker` should be a link to the upstream bugtracker.

> [!NOTE]
> It is highly recommended to be a link to the upstream bugzilla with filed component and product.

> [!WARNING]
> It might be necessary to escape URLs. For example replacing of `&` with `&amp;`.

For other possible values, take a look at the tag's description in [varlistentry_title](#tag-url).

\<metadata_license/\>  
The `<metadata_license/>` tag is indicating the content license that you are releasing the one metadata file as. This is not typically the same as the project license. By ommitting the license value would probably mean your data would not be incorporated into the distribution metadata. Permissible license codes include:

The license codes correspond to the identifiers found at the [SPDX OpenSource License Registry](http://spdx.org/licenses/). Take a look at [varlistentry_title](#tag-metadata_license) for more details about this tag.

\<project_license/\>  
The `<project_license/>` tag is indicating the license(s) this addon is released under. Take a look at the specification of the [varlistentry_title](#tag-project_license) tag for details on how to properly use it.

\<update_contact/\>  
You might want to include an update-contact email address. Take a look at the specification of the [varlistentry_title](#tag-update_contact) tag for more details on how to use this tag.

## For distributors packaging Appstream metadata

### Guidelines for distributors

Distributors of projects with AppStream metadata perform an important role by making the software available to more people. There are a few guidelines distributors should follow in order for software centers to present the correct information to users.

### Guidelines for distributors

A binary package that contains AppStream desktop metadata ([Desktop Applications](#sect-Metadata-Application)) must also contain both the .desktop file for the application and the application itself.

A binary package must not contain more than one AppStream metadata file. The one exception is that it is permissable for a binary package that is extended by addons to include those addons ([Addons](#sect-Metadata-Addon)) and their AppStream metadata files. Note that users will be unable to remove those addons separately.

Except for the extended package, no other package may contain more than one Appstream addon metadata file.

## Translating Metadata

### Introduction

Most AppStream metadata can be translated, This page contains some practical instructions how to translate the metadata.

> [!NOTE]
> If you are a KDE developer and using the KDE infrastructure with it's localization support, you need to do nothing to get translated metadata. Just place your `*.metainfo.xml*` (or `*.appdata.xml*` file) at a sane place, and the l10n-script will translate the file in-place automatically.

### Selecting strings for translation

By default, all strings in a MetaInfo file that are in translatable elements will be marked for translation. If you are using `xgettext`, `itstool` or any other tool that uses ITS rules for translation, and have AppStream or AppStream's ITS rules installed, you can exclude any element from being translated by adding a `translate="no"` attribute to it.

One special case is the `description` block in MetaInfo files and release metadata. In MetaInfo files, each individual paragraph of a description (or enumerated entry) is translated individually, however you can only exclude the complete block from being translated by adding `translate="no"` to the `description` element. It is generally discouraged to not translate component descriptions, so please use this with care!

### Translating using Itstool

One good way to translate MetaInfo files besides using plain Gettext is using Itstool for translation. In order to translate an XML file with it, you need an `.its` file with translation definitions. This file is installed with Gettext, but a more recent version is also shipped by AppStream, so make sure `appstream` itself is installed to get more complete translations.

To extract a GNU Gettext `.pot` file from your XML file, run itstool with the following arguments (replacing "foo" with your project name):

``` Bash
itstool -o $podir/foo_metadata.pot data/foo.metainfo.xml
```

You can then translate the `.pot` file using the standard methods for translating files like these. You obtain `.po` files, which you can convert into `.mo` files (using msgfmt) like you would do with any other localization. Then, you need to call `itstool` again, to create a translated version of the original XML file:

``` Bash
itstool -j data/foo.metainfo.xml -o output/foo.metainfo.xml $modir/*.mo
```

Please ensure that the `.mo` files in `$modir` are named with their language codes.

> [!NOTE]
> You can find more information about Itstool [on their homepage](http://itstool.org/).

#### Integrating with Meson

First add your MetaInfo file to your `POTFILES.in` file and use Gettext for extraction of translatable elements:

``` Meson
i18n = import('i18n')

i18n_result = i18n.gettext(gettext_domain,
    preset : 'glib',
)
```

To then apply the translated data to the MetaInfo XML file, you can use the built-in `itstool_join` function:

``` Meson
metainfo_dir = join_paths(get_option ('datadir'), 'metainfo')

metainfo_i18n = i18n.itstool_join(
    input:  'org.example.myapp.metainfo.xml',
    output: 'org.example.myapp.metainfo.xml',
    mo_targets: i18n_result[0],
    install: true,
    install_dir: metainfo_dir,
)
```
