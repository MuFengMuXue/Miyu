[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Yt-dlp&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][GitHub](https://github.com/yt-dlp/yt-dlp)

[[]][Official documentation](https://github.com/yt-dlp/yt-dlp/blob/master/README.md)

yt-dlp is a youtube-dl fork based on the now inactive youtube-dlc. The main focus of this project is adding new features and patches while also keeping up to date with the original project.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Downloading a video]](#Downloading_a_video)
    -   [[2.2] [Output format]](#Output_format)
    -   [[2.3] [Extracting audio]](#Extracting_audio)
    -   [[2.4] [Adding metadata]](#Adding_metadata)
    -   [[2.5] [Subtitles]](#Subtitles)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Default arguments]](#Default_arguments)
    -   [[3.2] [Encoding]](#Encoding)

## [Installation]

### [USE flags]

### [USE flags for] [net-misc/yt-dlp](https://packages.gentoo.org/packages/net-misc/yt-dlp) [[]] [youtube-dl fork with additional features and fixes]

  ------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+deno`](https://packages.gentoo.org/useflags/+deno)   Pull in dev-lang/deno-bin by default needed for proper YouTube support (if this USE is masked on your profile, refer to yt-dlp\'s documentation for lesser supported alternatives which are not supported out-of-the-box due to security concerns)
  [`man`](https://packages.gentoo.org/useflags/man)       Build and install man pages
  [`test`](https://packages.gentoo.org/useflags/test)     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-10 16:22] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask net-misc/yt-dlp`

## [Usage]

### [Downloading a video]

The easiest way to download a video from YouTube with [yt-dlp] is by passing it as the only argument:

`user `[`$`]`yt-dlp `[`https://www.youtube.com/watch?v=t09IbcxAJlU`](https://www.youtube.com/watch?v=t09IbcxAJlU)

### [Output format]

To output the video in a different format, use the `-f,--format` flags:

`user `[`$`]`yt-dlp -f mp4 `[`https://www.youtube.com/watch?v=t09IbcxAJlU`](https://www.youtube.com/watch?v=t09IbcxAJlU)

### [Extracting audio]

To download just the audio of a video, use `-x,--extract-audio`:

`user `[`$`]`yt-dlp -x `[`https://www.youtube.com/watch?v=t09IbcxAJlU`](https://www.youtube.com/watch?v=t09IbcxAJlU)

Or, if a format other than `.opus` is required, use `--audio-format`

`user `[`$`]`yt-dlp -x --audio-format mp3 `[`https://www.youtube.com/watch?v=t09IbcxAJlU`](https://www.youtube.com/watch?v=t09IbcxAJlU)

In order for the encoding to mp3 to work, the package media-video/ffmpeg must be installed with the `lame` USE flag (which is no longer the default). A check with [ffmpeg -version] should show `--enable-libmp3lame`.

### [Adding metadata]

To add chapters and infojson to a downloaded video, use `--embed-metadata`:

`user `[`$`]`yt-dlp --embed-metadata `[`https://www.youtube.com/watch?v=t09IbcxAJlU`](https://www.youtube.com/watch?v=t09IbcxAJlU)

### [Subtitles]

To list available subtiles for a video, use `--list-subs`:

`user `[`$`]`yt-dlp --list-subs `[`https://www.youtube.com/watch?v=t09IbcxAJlU`](https://www.youtube.com/watch?v=t09IbcxAJlU)

If a video provides subtitles then the ones provided by the channel will be listed below the auto-generated ones by YouTube.

Downloading a video with subtitles can then be done using `--write-subs/--write-auto-subs` if the manual or auto-generated subtitles wish to be used, respectively.

`user `[`$`]`yt-dlp --write-subs/--write-auto-subs --sub-lang en `[`https://www.youtube.com/watch?v=t09IbcxAJlU`](https://www.youtube.com/watch?v=t09IbcxAJlU)

** Note**\
The default subtitle language is English

## [Configuration]

yt-dlp\'s system-wide configuration files are located at: [/etc/yt-dlp.conf], [/etc/yt-dlp/config], [/etc/yt-dlp/config.txt] and the recommended path for user configuration is [\$/yt-dlp/config]

### [Default arguments]

Adding default arguments to yt-dlp can be done by using the configuration file, for example, in [\$/yt-dlp/config]

[FILE] **`$/yt-dlp/config`**

    # Lines starting with # are comments

    # Always extract audio
    -x

    # Do not copy the mtime
    --no-mtime

    # Use this proxy
    --proxy 127.0.0.1:3128

    # Save all videos under YouTube directory in your home directory
    -o ~/YouTube/%(title)s.%(ext)s

### [Encoding]

The default encoding yt-dlp uses for configuration files is UTC BOM, if that is not present then the system locale.

To use a encoding format other than these, add the comment `# coding: ENCODING` to the top of the configuration file.