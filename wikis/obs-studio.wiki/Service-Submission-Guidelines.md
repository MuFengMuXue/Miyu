# Preamble

This document contains basic guidelines for submitting a new service for inclusion, or an update to an existing service in OBS.

While the same requirements apply to services that wish to add a deeper integration (e.g. OAuth) to OBS those types of PRs will require more in-depth work and are not covered by this document.

# General Rules & Requirements

1. <ins>**You must be a representative of the service being added/updated**</ins>
2. PRs must follow our [contribution guidelines](https://github.com/obsproject/obs-studio/blob/master/CONTRIBUTING.rst) and [code of conduct](https://github.com/obsproject/obs-studio/blob/master/COC.rst)
3. Only RTMP, RTMPS, and HLS based ingests are currently allowed. FTL has been deprecated and PRs for new services will no longer be accepted.
4. If your service is available to the public, some adoption should be visible to warrant the inclusion in OBS
5. Your service must be released and have documentation available
    1. *For public/user-generated content services:* Final release or open alpha/beta/etc., closed testing stages are not permitted
    2. *For non-public/commercial services:* Reached [general availability](https://en.wikipedia.org/wiki/Software_release_life_cycle#General_availability_(GA))
    3. Exemptions may be made at the OBS Project's discretion. You may submit a PR in draft stage before release for review and to accelerate merge once your service becomes available

We reserve the right to reject service submissions on any reason, including but not limited to the promotion of illegal activities (e.g. piracy), harmful behaviour (e.g. harassment, hate speech), or other objectionable content.

# Adding your service

Adding your service is relatively simple, and consists of the following steps:

0. Fork and clone the [obs-studio](https://github.com/obsproject/obs-studio) repository
1. Add service entry to `plugins/rtmp-services/data/services.json`
2. Increment package version in `plugins/rtmp-services/data/package.json`
3. Test changes locally (build OBS or replace the JSON files in your existing install)
4. Commit and push your changes to your fork, then submit a Pull Request

See the following sections for details on the JSON format and commit guidelines.

## 1. Adding your service entry

The JSON file currently does not use automatic formatting or checks, however we ask you to follow some simple rules:

* 4-space wide indentation (spaces, not tabs)
* Objects in a list have their opening and closing braces on the previous and subsequent line
* Properties with Objects as values have the opening bracket on the same line as the property name
* The JSON file must be valid (you can use an online validator to check)

A full reference for the JSON format is provided [in the section below](#json-format-reference).

For most services `name`, `servers[]` (with at least one entry), and `recommended.max video bitrate` as well as `recommended.keyint` are sufficient.

**Note:** *If your service uses RTMP/RTMPS `supported video codecs` must be present and set to `["h264"]` unless the service implements [enhanced-rtmp v1](https://github.com/veovera/enhanced-rtmp) (or later).*

To illustrate the format, here is an example containing all required and the two optional-but-recommended properties:

#### Minimal RTMP example
```json
        {
            "name": "Example Service Name",
            "servers": [
                {
                    "name": "RTMP Example",
                    "url": "rtmp://ingest.example.com/live"
                }
            ],
            "supported video codecs": [
                "h264"
            ],
            "recommended": {
                "keyint": 2,
                "max video bitrate": 6000
            }
        }
```

This entry can simply be copy-pasted to the end of the list in `plugins/rtmp-services/data/services.json` and then adjusted to fit your needs. Just remember to add a `,` after the closing bracket (`}`) of the previous entry.

#### Please note:
* Your service **must not** have `common` set (to true) unless it already is, the decision to mark services as common lies at the sole descretion of the OBS Project
* While you can add your service at any point in the list, we recommend simply adding them at the end since they're presented in an alphabetical order to the user
* Ingests with different protocols (aside from RTMP and RTMPS) cannot be mixed in one service entry
* HLS services must use the `{stream_key}` variable in server URLs and the `recommended.output` property must be set to `ffmpeg_hls_muxer`

## 2. Incrementing the package version

The `rtmp-services` package version needs to be incremented for OBS to know that there has been an update, simply increment the version numbers in `plugins/rtmp-services/data/package.json` by 1.

## 3. Local testing

To test your changes locally you can replace the `services.json` and `package.json` in `%APPDATA%\obs-studio\plugin_config\rtmp-services` with your updated ones and run OBS to verify that your service is now listed/the listing has been updated.

## 4. Commit and PR

Commits must be prefixed with `rtmp-services: ` and should be in present-tense. In General `rtmp-services: Add <service name>` is sufficient when adding a new service.
When updating you may specify what is being updated, for example `rtmp-services: Update <service name> recommendations` or `rtmp-services: Update <service name> ingests`.

When making the PR be sure to follow the PR guidelines outlined in the PR template.

# JSON Format Reference

### Full list of available properties

| Property Name                              | Description                                                                                                           |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `name`                                     | **(Required)** The name of the service as shown in the dropdown                                                       |
| `common`                                   | Whether or not the service is shown in the list before it is expanded to all services by the user                     |
| `more_info_link`                           | Link that provides additional info about the service, presented in the UI as a button next to the services dropdown   |
| `stream_key_link`                          | Link where a logged-in user can find the "stream key", presented as a button below the stream key field               |
| `alt_names[]`                              | Previous names of the service used for migrating existing users to the updated entry                                  |
| `protocol`                                 | **(Required if not RTMP/RTMPS)** The streaming protocol that the service use                                          |
| `servers[]`                                | **(Required)** List of servers                                                                                        |
| `servers[].url`                            | **(Required)** RTMP(S) or HLS URL of the ingest server                                                                |
| `servers[].name`                           | **(Required)** Name of the server (e.g. location, primary/backup)                                                     |
| `supported video codecs`                   | **(Required for RTMP/RTMPS)** List of supported video codecs. Valid options: h264, hevc, av1                                    |
| `supported audio codecs`                   | List of supported audio codecs. If none default to aac. Valid options: aac, opus                                      |
| `recommended`                              | Object containing recommended service settings                                                                        |
| `recommended.keyint`                       | Keyframe interval (seconds)                                                                                           |
| `recommended.profile`                      | H.264 Profile                                                                                                         |
| `recommended.max fps`                      | Maximum supported framerate (integer)                                                                                 |
| `recommended.max video bitrate`            | Highest supported video bitrate (kbps)                                                                                |
| `recommended.max audio bitrate`            | Highest supported audio bitrate (kbps)                                                                                |
| `recommended.bframes`                      | Maximum allowed number of B-Frames                                                                                    |
| `recommended.x264opts`                     | Additional x264 encoder options                                                                                       |
| `recommended.output`                       | **(Required if not RTMP/RTMPS)** OBS output module used (`rtmp_output` or `ffmpeg_hls_muxer`)                         |
| `recommended.supported resolutions[]`      | List of supported resolutions in format `{width}x{height}`                                                            |
| `recommended.bitrate matrix[]`             | List of resolutions and frame rate combinations with their recommended maximum bitrate                                |
| `recommended.bitrate matrix[].res`         | Resolution in format `{width}x{height}`                                                                               |
| `recommended.bitrate matrix[].fps`         | Framerate (integer)                                                                                                   |
| `recommended.bitrate matrix[].max bitrate` | Maximum bitrate in kbps                                                                                               |

**Note:** The default for `supported video codecs` depends on the outputs. For RTMP this is AV1, HEVC, and H.264 as of [PR 8522](https://github.com/obsproject/obs-studio/pull/8522), for SRT/RIST/HLS output this is HEVC and H.264, and for FTL this is H.264 only. If your service does not support all of these codecs this key must be specified and only include supported ones.

### Full example utilising all properties
```json
        {
            "name": "Example Service Name",
            "common": false,
            "more_info_link": "https://example.com/documentation/more-info",
            "stream_key_link": "https://example.com/page/with/stream/key",
            "alt_names": [
                "Previous Example Service Name"
            ],
            "servers": [
                {
                    "name": "RTMPS Example",
                    "url": "rtmps://ingest.example.com:443/live"
                },
                {
                    "name": "RTMP Example",
                    "url": "rtmp://ingest.example.com/live"
                }
            ],
            "protocol": "RTMPS",
            "supported video codecs": [
                "h264",
                "hevc"
            ],
            "supported audio codecs": [
                "aac",
                "opus"
            ],
            "recommended": {
                "keyint": 2,
                "profile": "high",
                "supported resolutions": [
                    "1920x1080",
                    "1280x720",
                    "852x480",
                    "640x360"
                ],
                "bitrate matrix": [
                    {
                        "res": "1920x1080",
                        "fps": 30,
                        "max bitrate": 6000
                    },
                    {
                        "res": "1920x1080",
                        "fps": 60,
                        "max bitrate": 9000
                    }
                ],
                "max fps": 60,
                "max video bitrate": 9000,
                "max audio bitrate": 320,
                "bframes": 2,
                "x264opts": "scenecut=0",
                "output": "rtmp_output"
            }
        }
```
