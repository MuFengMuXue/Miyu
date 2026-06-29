# Data Validation

The AppStream utility `appstreamcli validate` can validate AppStream XML metadata. It emits hints with different priorities: Error hints make data unusable or fail validation; warnings describe likely unintended behavior; info hints are recommendations; pedantic hints are optional nice-to-have checks.

## Validator Issue Tags

| Tag | Severity | Explanation |
| --- | --- | --- |
| `type-property-required` | Error | This tag requires a type property. |
| `invalid-child-tag-name` | Info | Tags of this name are not permitted in this section. |
| `metainfo-localized-description-tag` | Error | A `<description/>` tag must not be localized in metainfo files (upstream metadata). Localize the individual paragraphs instead. |
| `catalog-localized-description-section` | Error | This element (paragraph, list, etc.) of a `<description/>` tag must not be localized individually in catalog metadata. Localize the whole `<description/>` tag instead. The AppStream metadata catalog generator (e.g. `appstream-generator`) will already do the right thing when compiling the data. |
| `description-markup-invalid` | Error | AppStream descriptions support only a limited set of tags to format text: Paragraphs (`<p/>`) and lists (`<ul/>`, `<ol/>`). This description markup contains an invalid XML tag that would not be rendered correctly in applications supporting the metainfo specification. |
| `description-para-markup-invalid` | Error | This description paragraph contains invalid markup. Currently, only `<em/>` and `<code/>` are permitted. |
| `description-enum-item-invalid` | Error | Enumerations must only have list items (`<li/>`) as children. |
| `description-enum-group-translated` | Error | The enumeration must not be translated as a whole. In MetaInfo files, translate individual items (`<li/>` elements) instead. |
| `description-first-para-too-short` | Info | The first `description/p` paragraph of this component might be too short (< 80 characters). Please consider starting with a longer paragraph to improve how the description looks like in software centers and to provide more detailed information on this component immediately in the first paragraph. |
| `description-first-word-not-capitalized` | Info | The description line does not start with a capitalized word, project name or number. |
| `description-has-plaintext-url` | Warning | The description contains a web URL in plain text. This is not allowed, please use the `<url/>` tag instead to share links. |
| `description-no-valid-content` | Warning | The description element does not contain any valid content (paragraphs, enumerations, etc.). |
| `description-spurious-text` | Warning | The description element contains raw text that is not in any paragraph or other permitted tag. This is not allowed and the additional text may be ignored by parsers or raise errors. |
| `tag-not-translatable` | Error | This tag is not translatable. |
| `tag-duplicated` | Error | This tag must only appear once in this context. Having multiple tags of this kind is not valid. |
| `tag-empty` | Warning | The mentioned tag is empty, which is highly likely not intended as it should have content. |
| `tag-invalid-text-content` | Error | The mentioned tag has text content, even though it must not contain text. |
| `cid-is-not-rdns` | Error | The component ID is required to follow a reverse domain-name scheme for its name. See the AppStream specification for details. |
| `cid-desktopapp-is-not-rdns` | Warning | The component ID is not a reverse domain-name. Please update the ID to avoid future issues and be compatible with all AppStream implementations. You may also consider to update the name of the accompanying .desktop file to follow the latest version of the Desktop-Entry specification and use a rDNS name for it as well. In any case, do not forget to mention the new desktop-entry in a `<launchable/>` tag for this component to keep the application launchable from software centers and the .desktop file data associated with the metainfo data. |
| `cid-maybe-not-rdns` | Info | The component ID might not follow the reverse domain-name schema (the TLD used by it is not known to the validator). |
| `cid-invalid-character` | Error | The component ID contains an invalid character. Only ASCII characters, dots and numbers are permitted. |
| `cid-punctuation-prefix` | Error | The component ID starts with punctuation. This is not allowed. |
| `cid-rdns-contains-hyphen` | Warning | The component ID contains a hyphen/minus in its domain part. Using a hyphen is strongly discouraged to improve interoperability with other tools such as D-Bus. A good option is to replace any hyphens with underscores (`_`). Hyphens are only allowed in the last segment of a component ID. |
| `cid-has-number-prefix` | Info | The component ID contains a segment starting with a number. Starting a segment of the reverse-DNS ID with a number is strongly discouraged, to keep interoperability with other tools such as D-Bus. Ideally, prefix these segments with an underscore. |
| `cid-contains-uppercase-letter` | Pedantic | The component ID should only contain lowercase characters. |
| `cid-domain-not-lowercase` | Error | The domain part of the rDNS component ID (first two parts) must only contain lowercase characters. |
| `cid-missing-affiliation-freedesktop` | Warning | The component is part of the Freedesktop project, but its ID does not start with fd.o's reverse-DNS name ("org.freedesktop"). |
| `cid-missing-affiliation-kde` | Warning | The component is part of the KDE project, but its ID does not start with KDE's reverse-DNS name ("org.kde"). |
| `cid-missing-affiliation-gnome` | Info | The component is part of the GNOME project, but its ID does not start with GNOME's reverse-DNS name ("org.gnome"). |
| `spdx-expression-invalid` | Error | The SPDX license expression is invalid and could not be parsed. |
| `spdx-license-unknown` | Warning | The license ID was not found in the SPDX database. Please check that the license ID is written in an SPDX-conformant way and is a valid free software license. |
| `metadata-license-too-complex` | Error | The metadata itself seems to be licensed under a complex collection of licenses. Please license the data under a simple permissive license, like FSFAP, MIT or CC0-1.0 to allow distributors to include it in mixed data collections without the risk of license violations due to mutually incompatible licenses. |
| `metadata-license-invalid` | Error | The metadata itself does not seem to be licensed under a permissive license. Please license the data under a permissive license, like FSFAP, CC0-1.0 or 0BSD to allow distributors to include it in mixed data collections without the risk of license violations due to mutually incompatible licenses. |
| `update-contact-no-mail` | Warning | The update-contact does not appear to be a valid email address (escaping of `@` is only allowed as `_at_` or `_AT_`). |
| `screenshot-invalid-env-style` | Warning | The `environment` property is set to an unrecognized graphical environment/style combination. |
| `screenshot-invalid-width` | Warning | The `width` property must be a positive integer. |
| `screenshot-invalid-height` | Warning | The `height` property must be a positive integer. |
| `screenshot-invalid-scale` | Warning | The `scale` property must be a positive integer. |
| `screenshot-image-invalid-type` | Error | The image type must be either `source` or `thumbnail`. |
| `screenshot-image-missing-width` | Warning | The `width` property must be present if the image type is `thumbnail`. |
| `screenshot-image-missing-height` | Warning | The `height` property must be present if the image type is `thumbnail`. |
| `screenshot-image-source-duplicated` | Error | There can only be one `source` image per screenshot and language. |
| `screenshot-image-no-source` | Error | A screenshot must have at least one untranslated image of type `source`. |
| `screenshot-image-no-source-but-en-locale` | Error | A screenshot must have at least one untranslated image of type `source`, which could not be found. Instead, a tag with an `en` locale (`xml:lang=en`) was found, which is likely intended to be the translatable image. Please remove the XML localization attribute in this case. |
| `screenshot-image-not-found` | Warning | Unable to reach the screenshot image on its remote location - does the image exist? |
| `screenshot-video-not-found` | Warning | Unable to reach the screenshot video on its remote location - does the video file exist? |
| `screenshot-media-url-not-secure` | Info | Consider using a secure (HTTPS) URL to reference this screenshot image or video. |
| `screenshot-no-unscaled-image` | Warning | A screenshot must have at least one image that has a scaling factor of 1. |
| `screenshot-no-media` | Error | A screenshot must contain at least one image or video in order to be useful. Please add an `<image/>` to it. |
| `screenshot-mixed-images-videos` | Error | A screenshot must contain either images or videos, but not both at the same time. Please use this screenshot exclusively for either static images or for videos. |
| `screenshot-no-caption` | Pedantic | The screenshot does not have a caption text. Consider adding one. |
| `screenshot-video-codec-missing` | Info | The screenshot video does not specify which video codec was used in a `codec` property. |
| `screenshot-video-container-missing` | Pedantic | The screenshot video does not specify which container format was used in a `container` property. |
| `screenshot-video-codec-invalid` | Warning | The selected video codec is not supported by AppStream and software centers may not be able to play the video. Only the AV1 and VP9 codecs are currently supported, using `av1` and `vp9` as values for the `codec` property. |
| `screenshot-video-container-invalid` | Warning | The selected video container format is not supported by AppStream and software centers may not be able to play the video. Only the WebM and Matroska video containers are currently supported, using `webm` and `mkv` as values for the `container` property. |
| `screenshot-video-file-wrong-container` | Warning | For videos, only the WebM and Matroska (.mkv) container formats are currently supported. The file extension of the referenced video does not belong to either of these formats. |
| `screenshot-default-contains-video` | Error | The default screenshot of a software component must not be a video. Use a static image as default screenshot and set the video as a secondary screenshot. |
| `screenshot-default-missing` | Warning | No screenshot is marked as default. |
| `relation-invalid-tag` | Warning | Found an unknown tag in a requires/recommends group. This is likely an error, because a component relation of this type is unknown. |
| `relation-item-no-value` | Error | A `requires` or `recommends` item requires a value to denote a valid relation. |
| `relation-item-has-version` | Warning | Found `version` property on required/recommended item of a type that should not have or require a version. |
| `relation-item-missing-compare` | Info | Found `version` property on this required/recommended item, but not `compare` property. It is recommended to explicitly define a comparison operation. |
| `relation-item-invalid-vercmp` | Error | Invalid comparison operation on relation item. Only one of `eq/ne/lt/gt/le/ge` is permitted. |
| `relation-item-has-vercmp` | Info | The relation item has a comparison operation set, but does not support any comparisons. |
| `relation-item-redefined` | Warning | This relation item has already been defined once for this or a different relation type. Please do not redefine relations. |
| `relation-memory-in-requires` | Info | Found a memory size relation in a `requires` tag. This means users will not be able to even install the component without having enough RAM. This is usually not intended and you want to use `memory` in the `recommends` tag instead. |
| `relation-control-in-requires` | Info | Found a user input control relation in a `requires` tag. This means users will not be able to even install the component without having the defined input control available on the system. This is usually not intended and you want to use `control` in the `recommends` tag instead. |
| `relation-control-value-invalid` | Warning | This `control` item defines an unknown input method and is invalid. Check the specification for a list of permitted values. |
| `relation-display-length-value-invalid` | Warning | This `display_length` item contains an invalid display length. Its value must be a positive integer value denoting logical pixels. Please refer to the AppStream specification for more information on this tag. |
| `relation-display-length-side-property-invalid` | Warning | This `side` property of this `display_length` item contains an invalid value. It must either be `shortest` or `longest`, or unset to imply `shortest` to make the item value refer to either the shortest or longest side of the display. |
| `relation-hardware-value-invalid` | Warning | This `hardware` item contains an invalid value. It should be a Computer Hardware ID (CHID) UUID without braces. |
| `relation-memory-value-invalid` | Warning | A `memory` item must only contain a non-zero integer value, depicting a system memory size in mebibyte (MiB) |
| `relation-internet-value-invalid` | Warning | The set tag value is not valid for an `internet` relation. |
| `relation-internet-bandwidth-offline` | Warning | The `bandwidth_mbitps` property is not allowed when using `offline-only` as value. |
| `relation-internet-bandwidth-value-invalid` | Warning | The value of this property must be a positive integer value, describing the minimum required bandwidth in mbit/s. |
| `component-type-invalid` | Error | The set component type is not a recognized, valid AppStream component type. |
| `component-priority-in-metainfo` | Warning | The component has a priority value set. This is not allowed in metainfo files. |
| `component-merge-in-metainfo` | Warning | The component has a `merge` method defined. This is not allowed in metainfo files. |
| `component-id-missing` | Error | The component is missing an ID (`<id/>` tag). |
| `component-name-missing` | Error | The component is missing a name (`<name/>` tag). |
| `component-name-too-long` | Warning | The name of this component is excessively long and can likely not be displayed properly in most layouts. |
| `component-summary-missing` | Error | The component is missing a summary (`<summary/>` tag). |
| `id-tag-has-type` | Info | The `<id/>` tag still contains a `type` property, probably from an old conversion to the recent metainfo format. |
| `multiple-pkgname` | Pedantic | The `pkgname` tag appears multiple times. You should evaluate creating a metapackage containing the metainfo and .desktop files in order to avoid defining multiple package names per component. |
| `name-has-dot-suffix` | Pedantic | The component name should (likely) not end with a dot (`.`). |
| `summary-has-dot-suffix` | Info | The component summary should not end with a dot (`.`). |
| `summary-has-tabs-or-linebreaks` | Error | The component summary must not contain tabs or linebreaks. |
| `summary-has-url` | Error | The summary must not contain any URL. Use the ``<url/>`` tags for links. |
| `summary-first-word-not-capitalized` | Info | The summary text does not start with a capitalized word, project name or number. |
| `summary-too-long` | Warning | The summary text is very long, and will likely not be displayed properly everywhere. It should be <= 90 characters. |
| `icon-stock-cached-has-url` | Error | Icons of type `stock` or `cached` must not contain an URL, a full or an relative path to the icon. Only file basenames or stock names are allowed. |
| `icon-remote-no-url` | Error | Icons of type `remote` must contain an URL to the referenced icon. |
| `icon-remote-not-found` | Warning | Unable to reach remote icon at the given web location - does it exist? |
| `icon-remote-not-secure` | Info | Consider using a secure (HTTPS) URL for the remote icon link. |
| `metainfo-invalid-icon-type` | Error | Metainfo files may only contain icons of type `stock` or `remote`, the set type is not allowed. |
| `url-invalid-type` | Warning | Invalid `type` property for this `url` tag. URLs of this type are not known in the AppStream specification. |
| `url-not-reachable` | Warning | Unable to reach remote location that this URL references - does it exist? |
| `url-not-secure` | Info | Consider using a secure (HTTPS) URL for this web link. |
| `web-url-expected` | Error | A web URL was expected for this value. |
| `url-uses-ftp` | Warning | This web link uses the FTP protocol. Consider switching to HTTP(S) instead. |
| `url-redefined` | Warning | An URL of this type has already been defined. |
| `url-homepage-missing` | Warning | This component is missing an `url` element of type `homepage` to link to the project's homepage. |
| `developer-name-tag-deprecated` | Info | The toplevel `developer_name` element is deprecated. Please use the `name` element in a `developer` block instead. |
| `developer-info-missing` | Info | This component contains no `developer` element with information about its author. |
| `developer-id-missing` | Info | The `developer` element is missing an `id` property, containing a unique string ID for the developer. Consider adding a unique ID. |
| `developer-id-invalid` | Warning | The developer-ID is invalid. It should be an rDNS string identifying the developer, or a Fediverse handle. It must also only contain lowercase ASCII letters, numbers and punctuation. |
| `developer-name-missing` | Warning | The `developer` block does not have a `name` element with a human-readable project author name. |
| `developer-name-has-url` | Warning | The `name` child of a `developer` block must not contain a hyperlink. |
| `unknown-desktop-id` | Error | The set value is not an identifier for a desktop environment as registered with Freedesktop.org. |
| `launchable-unknown-type` | Error | This `launchable` tag has an unknown type and can not be used. |
| `bundle-unknown-type` | Error | This `bundle` tag has an unknown type and can not be used. |
| `update-contact-in-catalog-data` | Warning | The `update_contact` tag should not be included in catalog AppStream XML. |
| `nonstandard-gnome-extension` | Info | This tag is a GNOME-specific extension to AppStream and not part of the official specification. Do not expect it to work in all implementations and in all software centers. |
| `unknown-tag` | Info | Found invalid tag. Non-standard tags should be prefixed with `x-`. AppStream also provides the `<custom/>` tag to add arbitrary custom data to metainfo files. This tag is read by AppStream libraries and may be useful instead of defining new custom toplevel or `x-`-prefixed tags if you just want to add custom data to a metainfo file. |
| `metadata-license-missing` | Error | The essential tag `metadata_license` is missing. A license for the metadata itself always has to be defined. |
| `app-description-required` | Error | The component is missing a long description. Components of this type must have a long description. |
| `font-description-missing` | Info | It would be useful to add a long description to this font to present it better to users. |
| `driver-firmware-description-missing` | Info | It is recommended to add a long description to this component to present it better to users. |
| `description-missing` | Pedantic | This generic component is missing a long description. It may be useful to add one. |
| `untranslated-description-missing` | Error | The component is missing an untranslated long description, but has a translated one for the English locale. You need to provide a locale-less description in English as translation template. |
| `desktop-app-launchable-missing` | Error | This `desktop-application` component is missing a `desktop-id` launchable tag. This means that this application can not be launched and has no association with its desktop-entry file. It also means no icon data or category information from the desktop-entry file will be available, which will result in this application being ignored entirely. |
| `desktop-app-launchable-omitted` | Info | This `desktop-application` component has no `desktop-id` launchable tag, however it contains all the necessary information to display the application. The omission of the launchable entry means that this application can not be launched directly from installers or software centers. If this is intended, this information can be ignored, otherwise it is strongly recommended to add a launchable tag as well. |
| `console-app-no-binary` | Warning | Type `console-application` component, but no information about binaries in $PATH was provided via a `provides/binary` tag. |
| `web-app-no-url-launchable` | Error | This `web-application` component is missing a `launchable` tag of type `url`. |
| `web-app-no-icon` | Error | This `web-application` component is missing a `icon` tag to specify a valid icon. |
| `web-app-no-category` | Warning | This `web-application` component is missing categorizations. A `categories` block is likely missing. |
| `font-no-font-data` | Error | Type `font` component, but no font information was provided via a `provides/font` tag. |
| `driver-no-modalias` | Warning | Type `driver` component, but no modalias information was provided via a `provides/modalias` tag. |
| `extends-not-allowed` | Error | An `extends` tag is specified, but the component is not of type `addon`, `localization` or `repository`. |
| `addon-extends-missing` | Error | The component is an addon, but no `extends` tag was specified. |
| `localization-extends-missing` | Info | This `localization` component is missing an `extends` tag, to specify the components it adds localization to. |
| `localization-no-languages` | Error | This `localization` component does not define any languages this localization is for. |
| `service-no-service-launchable` | Error | This `service` component is missing a `launchable` tag of type `service`. |
| `metainfo-suggestion-type-invalid` | Warning | Suggestions of any type other than `upstream` are not allowed in metainfo files. |
| `category-invalid` | Warning | The category name is not valid. Refer to the XDG Menu Specification for a list of valid category names. |
| `all-categories-ignored` | Warning | All categories for this component have been ignored, either because they were invalid or because they are of low quality (e.g. custom 'X-' prefixed or toolkit ones like 'GTK' or 'Qt'). Please fix your category names, or add more categories. |
| `app-categories-missing` | Error | This component is in no valid categories, even though it should be. Please check its metainfo file and desktop-entry file. |
| `screenshot-caption-too-long` | Info | The screenshot caption is too long (should be <= 100 characters) |
| `file-read-failed` | Error | Unable to read file. |
| `xml-markup-invalid` | Error | The XML of this file is malformed. |
| `component-catalog-tag-invalid` | Error | Invalid tag found in catalog metadata. Only `component` tags are permitted. |
| `metainfo-ancient` | Error | The metainfo file uses an ancient version of the AppStream specification, which can not be validated. Please migrate it to version 0.6 (or higher). Modern files use the `component` root tag and include many other differences, so check for changes carefully when modernizing the data. |
| `root-tag-unknown` | Error | This XML document has an unknown root tag. Maybe this file is not a metainfo document? |
| `metainfo-filename-cid-mismatch` | Warning | The metainfo filename does not match the component ID. |
| `desktop-file-load-failed` | Error | Unable to load the desktop-entry file associated with this component. |
| `desktop-file-not-found` | Warning | This component metadata refers to a non-existing .desktop file. |
| `desktop-entry-category-invalid` | Warning | A category defined in the desktop-entry file is not valid. Refer to the XDG Menu Specification for a list of valid categories. |
| `desktop-entry-bad-data` | Warning | Error while reading some data from the desktop-entry file. |
| `desktop-entry-value-invalid-chars` | Warning | The value of this desktop-entry field contains invalid or non-printable UTF-8 characters, which can not be displayed properly. |
| `desktop-entry-value-quoted` | Warning | This desktop-entry field value is quoted, which is likely unintentional. |
| `desktop-entry-hidden-set` | Warning | This desktop-entry file has the 'Hidden' property set. This is wrong for vendor-installed .desktop files, and nullifies all effects this .desktop file has (including MIME associations), which most certainly is not intentional. |
| `desktop-entry-empty-onlyshowin` | Warning | This desktop-entry file has the 'OnlyShowIn' property set with an empty value. This might not be intended, as this will hide the application from all desktops. If you do want to hide the application from all desktops, using 'NoDisplay=true' is more explicit. |
| `dir-no-metadata-found` | Info | No AppStream metadata was found in this directory or directory tree. |
| `dir-applications-not-found` | Pedantic | No XDG applications directory found. |
| `metainfo-legacy-path` | Warning | The metainfo file is stored in a legacy path. Please place it in `/usr/share/metainfo/`. |
| `metainfo-multiple-components` | Warning | The metainfo file specifies multiple components. This is not allowed. |
| `releases-not-in-order` | Warning | The releases are not sorted in a latest to oldest version order. This is required as some tools will assume that the latest version is always at the top. Sorting releases also increases overall readability of the metainfo file. |
| `releases-type-invalid` | Error | The type of the releases block is invalid. It needs to either `embedded` (the default) or `external`. |
| `releases-url-insecure` | Error | The URL to an external release metadata file is insecure. This is not allowed, please use HTTPS URLs only. |
| `releases-download-failed` | Error | Failed to download release metadata. |
| `releases-external-not-found` | Warning | A local release metadata file was not found. It is strongly recommended to validate this metadata together with the main MetaInfo file. |
| `release-urgency-invalid` | Warning | The value set as release urgency is not a known urgency value. |
| `release-type-invalid` | Warning | The value set as release type is invalid. |
| `release-version-missing` | Error | The release is missing the `version` property. |
| `release-time-missing` | Error | The release entry is missing either the `date` (preferred) or the `timestamp` property. |
| `release-time-missing-for-snapshot` | Info | The release entry is missing the `date` property. Ensure to add it before publishing the snapshot release. |
| `release-timestamp-invalid` | Error | The release timestamp is invalid. |
| `release-description-outside-tag` | Error | The release description must be put inside a `description` tag |
| `artifact-type-invalid` | Error | The value set as artifact type is invalid. Must be either `source` or `binary`. |
| `artifact-bundle-type-invalid` | Warning | The value set as artifact bundle type is invalid. |
| `artifact-invalid-platform-triplet` | Warning | The platform triplet for this release is invalid. It must be in the form of `architecture-oskernel-osenv` - refer to the AppStream documentation or information on normalized GNU triplets for more information and valid fields. |
| `artifact-checksum-type-invalid` | Error | The selected checksumming algorithm is unsupported or unknown. |
| `artifact-size-type-invalid` | Error | The size type is unknown. Must be `download` or `installed`. |
| `artifact-filename-not-basename` | Error | The artifact filename must be a file basename, not a (relative or absolute) path. |
| `release-issue-type-invalid` | Error | The value set as release issue type is invalid. |
| `release-issue-is-cve-but-no-cve-id` | Warning | The issue is tagged at security vulnerability with a CVE number, but its value does not look like a valid CVE identifier. |
| `releases-info-missing` | Pedantic | This component is missing information about releases. Consider adding a `releases` tag to describe releases and their changes. |
| `invalid-iso8601-date` | Warning | The AppStream specification requires a complete, ISO 8601 date string with at least day-granularity to denote dates. Please ensure the date string is valid. |
| `circular-component-relation` | Warning | This component extends, provides, requires or recommends itself, which is certainly not intended and may confuse users or machines dealing with this metadata. |
| `runtime-project-license-no-ref` | Info | Licenses for `runtime` components are usually too complex to reflect them in a simple SPDX expression. Consider using a `LicenseRef` and a web URL as value for this component's `project_license`. E.g. `LicenseRef-free=https://example.com/licenses.html` |
| `runtime-no-provides` | Pedantic | Since a `runtime` component consists of multiple other software components, their component-IDs may be listed in a ``<provides/>`` section for this runtime. |
| `unknown-provides-item-type` | Info | The type of the item that the component provides is not known to AppStream. |
| `mimetypes-tag-deprecated` | Warning | The toplevel `mimetypes` tag is deprecated. Please use `mediatype` tags in a `provides` block instead to indicate that your software provides a media handler for the given types. |
| `content-rating-missing` | Info | This component has no `content_rating` tag to provide age rating information. You can generate the tag data online by answering a few questions at https://hughsie.github.io/oars/ |
| `content-rating-type-missing` | Error | The `type` attribute of this `content_rating` element is missing or empty. |
| `content-rating-type-invalid` | Error | The `type` attribute of the `content_rating` element has an invalid value. |
| `content-rating-invalid-tag` | Error | The `content_rating` tag can only contain `content_attribute` children. |
| `content-attribute-id-missing` | Error | The `id` attribute of the `content_attribute` element is missing or empty. |
| `content-attribute-id-invalid` | Error | The `id` attribute of the `content_attribute` element has an invalid value. |
| `content-attribute-value-empty` | Error | The `content_attribute` tag needs a value. |
| `content-attribute-value-unknown` | Error | The `content_attribute` tag value is unknown. |
| `content-attribute-value-invalid` | Error | The `content_attribute` tag value is invalid for the given id. |
| `content-attribute-id-duplicated` | Error | A `content_attribute` tag with this ID has already been defined. |
| `usertag-missing-namespace` | Info | This `tag` is missing a `namespace` attribute. |
| `usertag-invalid` | Error | This tag or its namespace contains invalid characters. Only lower-cased ASCII letters, numbers, dots, hyphens and underscores are permitted. |
| `branding-color-type-invalid` | Error | The type of this color is not valid. |
| `branding-color-scheme-type-invalid` | Error | The value of this color scheme preference is not valid. |
| `branding-color-scheme-wrong-property` | Error | The name of the color scheme property is wrong. It should be `scheme_preference`. |
| `branding-color-invalid` | Error | This color is not a valid HTML color code. |
| `branding-color-duplicated` | Error | A color for this type/scheme combination was already set. Colors must be unique per type/scheme. |
| `reference-doi-invalid` | Warning | The given DOI (Digital Object Identifier) for this reference item is not valid. |
| `reference-citation-url-invalid` | Warning | The value for this citation reference item must be an URL to a CFF (Citation File Format) file. |
| `reference-registry-name-missing` | Error | This registry reference item is missing the `name` property to denote the name of the registry it is about. |
| `reference-registry-name-unknown` | Warning | The registry for this reference item is unknown. This may be due to a typing error, or the registry needs to be registered with AppStream. |
| `reference-value-missing` | Error | The reference item is missing a value. |
| `custom-invalid-tag` | Error | The `custom` tag can only contain `value` children. |
| `custom-key-missing` | Error | This `custom` tag value is missing a `key` attribute. |
| `custom-key-duplicated` | Error | A key can only be used once. |
| `custom-value-empty` | Info | This custom value is empty. |
| `metainfo-localized-keywords-tag` | Error | A `keywords` tag must not be localized in metainfo files (upstream metadata). Localize the individual keyword entries instead. |

## Compose Hints

`appstreamcli compose` can construct AppStream catalog metadata from directories and other sources containing MetaInfo files. While composing final data, it can emit the following hints.

| Tag | Severity | Explanation |
| --- | --- | --- |
| `internal-unknown-tag` | Error | The given tag was unknown. Please file an issue against AppStream. |
| `internal-error` | Error | A fatal problem appeared in appstream-compose. Please file an issue against AppStream. Error: {{msg}} |
| `x-dev-testsuite-error` | Error | Dummy error hint for the testsuite. Var1: {{var1}}. |
| `x-dev-testsuite-info` | Info | Dummy info hint for the testsuite. Var1: {{var1}}. |
| `unit-read-error` | Error | Error while reading data from unit `{{name}}`: {{msg}} |
| `ancient-metadata` | Warning | The AppStream metadata should be updated to follow a more recent version of the specification. Please consult the MetaInfo quickstart guides (https://www.freedesktop.org/software/appstream/docs/chap-Quickstart.html) for more information. |
| `metainfo-parsing-error` | Error | Unable to parse AppStream MetaInfo file `{{fname}}`, the data is likely malformed. Error: {{error}} |
| `metainfo-no-id` | Error | Could not determine an ID for the component in `{{fname}}`. The AppStream MetaInfo file likely lacks an `&lt;id/&gt;` tag. The identifier tag is essential for AppStream metadata, and must not be missing. |
| `metainfo-no-name` | Error | Component has no name specified. Ensure that the AppStream MetaInfo file or the .desktop file (if there is any) specify a component name. |
| `metainfo-no-summary` | Error | Component does not contain a short summary. Ensure that the component's MetaInfo file has a `summary` tag, or that its .desktop file has a `Comment=` field set. More information can be found in the Desktop Entry specification (https://specifications.freedesktop.org/desktop-entry-spec/latest/localized-keys.html) and the MetaInfo specification (https://www.freedesktop.org/software/appstream/docs/sect-Metadata-Application.html#tag-dapp-summary). |
| `metainfo-license-invalid` | Error | The MetaInfo file does not seem to be licensed under a permissive license that is in the allowed set for AppStream metadata. Valid permissive licenses include FSFAP, CC0-1.0 or MIT. Using one of the vetted permissive licenses is required to allow distributors to include the metadata in mixed data collections without the risk of license violations due to mixing incompatible licenses.We only support a limited set of licenses that went through legal review. Refer to the specification documentation (https://www.freedesktop.org/software/appstream/docs/chap-Metadata.html#tag-metadata_license) for information on how to make '{{license}}' a valid expression, or consider replacing the license with one of the recognized licenses directly. |
| `metainfo-unknown-type` | Error | The component has an unknown type. Please make sure this component type is mentioned in the specification, and that the`type=` property of the component root-node in the MetaInfo XML file does not contain a spelling mistake. |
| `metainfo-releases-download-failed` | Warning | Unable to download release information from `{{url}}`. The error message was: {{msg}}. |
| `metainfo-releases-read-failed` | Error | Unable to read release information from `{{path}}`. The error message was: {{msg}}. |
| `file-read-error` | Error | Unable to read data from file `{{fname}}`: {{msg}} |
| `desktop-file-error` | Error | Unable to read data from .desktop file: {{msg}} |
| `desktop-entry-hidden-set` | Warning | The desktop-entry file `{{location}}` has the 'Hidden' property set. This is wrong for vendor-installed .desktop files, and nullifies all effects this .desktop file has (including MIME associations), which most certainly is not intentional. See the specification (https://specifications.freedesktop.org/desktop-entry-spec/latest/recognized-keys.html) for details. |
| `desktop-entry-empty-onlyshowin` | Warning | The desktop-entry file `{{location}}` has the 'OnlyShowIn' property set with an empty value. This might not be intended, as this will hide the application from all desktops. If you do want to hide the application from all desktops, using 'NoDisplay=true' is more explicit. See the specification (https://specifications.freedesktop.org/desktop-entry-spec/latest/recognized-keys.html) for details. |
| `missing-launchable-desktop-file` | Warning | The MetaInfo file references a .desktop file with ID '{{desktop_id}}' in its `launchable` tag, but the file was not found in the same source tree. In order to be able to launch the software once it was installed, please place the MetaInfo file and its .desktop files in the same package. |
| `translation-status-error` | Warning | Unable to read translation status data: {{msg}} |
| `translations-not-found` | Warning | Unable to add languages information, even though a `translation` tag was present in the MetaInfo file. Please check that its value is set correctly, and all locale files are placed in the right directories (e.g. `/usr/share/locale/*/LC_MESSAGES/` for Gettext .mo files). |
| `icon-not-found` | Error | The icon `<em>`{{icon_fname}}`</em>` was not found in the archive. This issue can have multiple reasons, like the icon being in a wrong directory or not being available in a suitable size (at least 64x64px). To make the icon easier to find, place it in `/usr/share/icons/hicolor/&lt;size&gt;/apps` and ensure the `Icon=` valueof the desktop-entry file is set correctly. |
| `no-stock-icon` | Error | The component has no stock icon set, even though it requires one (or a `local` icon) to be valid. |
| `icon-write-error` | Error | Unable to store icon `{{fname}}`: {{msg}} |
| `duplicate-component` | Error | A component with this ID already exists. AppStream IDs must be unique, any subsequent components have been ignored. Please resolve the ID conflict! |
| `metainfo-screenshot-but-no-media` | Warning | A screenshot has been found for this component, but apparently it does not have any images or videos defined. The screenshot entry has been ignored. |
| `screenshot-download-error` | Warning | Error while downloading screenshot from '{{url}}': {{error}} This might be a temporary server issue, or the screenshot is no longer available. |
| `screenshot-image-is-svg` | Warning | The screenshot image at '{{url}}' is a vector graphic. Vector graphics are not allowed as screenshot images. |
| `screenshot-save-error` | Warning | Unable to store screenshot for '{{url}}': {{error}} |
| `screenshot-no-thumbnails` | Info | No thumbnails have been generated for screenshot '{{url}}'. This could mean that the original provided screenshot is too small to generate thumbnails from. |
| `screenshot-video-check-failed` | Warning | Unable to inspect video file '{{fname}}'. This may have been caused by a configuration or network issue, or the supplied video file was faulty. The error message was: {{msg}} |
| `screenshot-video-has-audio` | Info | The video '{{fname}}' contains an audio track. The audio may not be played by software centers, so ideally you should avoid using audio, or at least make the audio non-essential for understanding the screencast. |
| `screenshot-video-audio-codec-unsupported` | Warning | The video '{{fname}}' contains an audio track using the '{{codec}}' codec. The only permitted audio codec is Opus (https://opus-codec.org/). |
| `screenshot-video-format-unsupported` | Warning | The video codec '{{codec}}' or container '{{container}}' of '{{fname}}' are not supported. Please encode the video as VP9 or AV1 using the WebM or Matroska container. |
| `screenshot-video-too-big` | Warning | The video '{{fname}}' exceeds the maximum allowed file size of {{max_size}} (its size is {{size}}). Please try to make a shorter screencast. |
| `screenshot-image-too-big` | Warning | The image '{{fname}}' exceeds the maximum allowed file size of {{max_size}} (its size is {{size}}). Please create a smaller screenshot image. |
| `font-load-error` | Error | Unable to load font '{{fname}}' from unit '{{unit_name}}: {{error}} |
| `font-metainfo-but-no-font` | Error | A MetaInfo file with component-type `font` was found, but we could not find any matching font file (TrueType or OpenType) in the package. This can mean that the `&lt;provides&gt; - &lt;font&gt;` tags contain wrong values that we could not map to the actual fonts, or that the package simply contained no fonts at all. Fonts in this package: `<em>`{{font_names}}`</em>` |
| `font-render-error` | Warning | Unable to render image for font '{{name}}': {{error}} |
| `gui-app-without-icon` | Error | The component is a GUI application (application which has a .desktop file for the XDG menu and `Type=Application`), but we could not find a matching icon for this application. |
| `web-app-without-icon` | Error | The component is a GUI web application, but it either has no icon set in its MetaInfo file, or we could not find a matching icon for this application. |
| `font-without-icon` | Warning | The component is a font, but somehow we failed to automatically generate an icon for it, and no custom icon was set explicitly. Is there a font file in the analyzed package, and does the MetaInfo file set the right font name to look for? |
| `os-without-icon` | Info | The component is an operating system, but no icon was found for it. Setting an icon would improve the look of this component in GUIs. |
| `no-valid-category` | Error | This software component is no member of any valid category (note that custom categories and toolkit categories like 'Qt' or 'GTK' are ignored). |
| `description-missing` | Error | Software components of type '{{kind}}' require a long description, and we were unable to find one. Please add one via a MetaInfo file. |
| `no-metainfo` | Warning | This software component is missing a MetaInfo file (https://www.freedesktop.org/software/appstream/docs/chap-Metadata.html#sect-Metadata-GenericComponent) as metadata source. To synthesize suitable metadata anyway, we took some data from its desktop-entry file. This has many disadvantages, like low-quality and incomplete metadata. Therefore clients may ignore this component entirely due to poor metadata. Additionally, a lot of software from desktop-entry files should either not be installable and searchable via the software catalog (like desktop-specific settings applications) or be tagged accordingly via MetaInfo files. Please consider to either hide this .desktop file from AppStream by adding a `X-AppStream-Ignore=true` field to it, or to write a MetaInfo file for this component. You can consult the MetaInfo quickstart guides (https://www.freedesktop.org/software/appstream/docs/chap-Quickstart.html) for more information on how to write a MetaInfo file, or file a bug with the upstream author of this software component. |
| `filters-but-no-output` | Error | Component filters were set, but no output was generated at all. Likely none of the filtered components were found, try to relax the filters and ensure the input data is valid. |
