## Appendix J. Application Profiles

## Introduction

The NVIDIA Linux driver supports configuring various driver settings on a per-process basis through the use of "application profiles": collections of settings that are only applied if the current process matches attributes detected by the driver when it is loaded into the process. This mechanism allows users to selectively override global driver settings for a particular application without the need to set environment variables on the command line prior to running the application.

Application profiles consist of "rules" and "profiles". A "profile" defines what settings to use, and a "rule" identifies an application and defines what profile should be used with that application.

A rule identifies an application by describing various features of the application; for example, the name of the application binary (e.g. "glxgears") or a shared library loaded into the application (e.g. "libpthread.so.0"). The particular features supported by this NVIDIA Linux implementation are listed below in the "Supported Features" section.

Currently, application profiles are only supported by the NVIDIA Linux GLX implementation, but other NVIDIA driver components may use them in the future.

Application profiles can be configured using the nvidia-settings control panel. To learn more, consult the online help text by clicking the "Help" button under the "Application Profiles" page in nvidia-settings.

## Enabling Application Profiles in the OpenGL Driver

Note: if HOME is unset, then any configuration files listed below located under \$HOME will not be loaded by the driver.

To enable application profile support globally on a system, edit the file \$HOME/.nv/nvidia-application-profile-globals-rc to contain a JSON object with a member "enabled" set to true or false. For example, if this file contains the following string:

``` screen
{ "enabled" : true }
```

application profiles will be enabled globally in the driver. If this file does not exist or cannot be read by the parser, application profiles will be enabled by default.

Application profile support in the driver can be toggled for an individual application by using the \_\_GL_APPLICATION_PROFILE environment variable. Setting this to 1 enables application profile support, and setting this to 0 disables application profile support. If this environment variable is set, this overrides any setting specified in \$HOME/.nv/nvidia-application-profile-globals-rc.

Additionally, the application profile parser can log debugging information to stderr if the \_\_GL_APPLICATION_PROFILE_LOG environment variable is set to 1. Conversely, setting \_\_GL_APPLICATION_PROFILE_LOG to 0 disables logging of parse information to stderr.

## Application Profile Search Path

By default, when the driver component ("libGL.so.1" in the case of GLX) is loaded by a process, the driver looks for files in the following search path:

- `$HOME/.nv/nvidia-application-profiles-rc`

- `$HOME/.nv/nvidia-application-profiles-rc.d`

- `/etc/nvidia/nvidia-application-profiles-rc`

- `/etc/nvidia/nvidia-application-profiles-rc.d`

- `/usr/share/nvidia/nvidia-application-profiles-580.105.08-rc`

By convention, the `*-rc.d` files are directories and the `*-rc` files are regular files, but the driver places no restrictions on file type, and any of the above files can be a directory or regular file, or a symbolic link which resolves to a directory or regular file. Files of other types (e.g. character or block devices, sockets, and named pipes) will be ignored.

If a file in the search path is a directory, the parser will examine all regular files (or symbolic links which resolve to regular files) in that directory in alphanumeric order, as determined by strcoll(3). Files in the directory of other types (e.g. other directories, character or block devices, sockets, and named pipes) will be ignored.

## Configuration File Syntax

When application profiles are enabled in the driver, the driver configuration is defined by a set of *profiles* and *rules*. Profiles are collections of driver settings given as key/value pairs, and rules are mappings between one or more *patterns* which match against some feature of the process and a profile.

Configuration files are written in a superset of JSON (http://www.json.org/) with the following additional features:

- A hash mark ('#') appearing outside of a JSON string denotes a comment, and any text appearing between the hash mark and the end of the line inclusively is ignored.

- Integers can be specified in base 8 or 16, in addition to base 10. Numbers beginning with '0' and followed by a digit are interpreted to be octal, and numbers beginning with '0' and followed by 'x' or 'X' are interpreted to be hexadecimal.

Each file consists of a root object with two optional members:

- "rules", which contains an array of rules, and

- "profiles", which contains an array of profiles.

Each rule is an object with the following members:

- "pattern", which contains either a string, a pattern object, or an array of zero or more pattern objects. If a string is given, it is interpreted to be a pattern object with the "feature" member set to "procname" and the "matches" member set to the value of the string. During application detection, the driver determines if each pattern in the rule matches the running process, and only applies the rule if all patterns in the rule match. If an empty array is given, the rule is unconditionally applied.

- "profile", which contains either a string, array, or profile. If a string is given, it is interpreted to be the name of some profile in the configuration. If a profile is given, it is implicitly defined as part of the rule. If an array is given, the array is interpreted to be an inline profile with its "settings" member set to the contents of the array.

Each profile is an object with the following members:

- "name", a string which names the profile for use in a rule. This member is mandatory if the profile is specified as part of the root object's profiles array, but optional if the profile is defined inline as part of a rule.

- "settings", an array of settings which can be given in two different formats:

  1.  As an array of keys and values, e.g.

``` screen
      [ "key1", "value1", "key2", 3.14159, "key3", 0xF00D ]

```

      Keys must be specified as strings, while a value may be a string, number, or true/false.

  2.  as an array of JSON setting objects.

Each setting object contains the following members:

- "k" (or "key"), the key given as a string

- "v" (or "value"), the value, given as a string, number, or true/false.

A pattern object may consist of a pattern primitive, or a logical operation on pattern objects. A pattern primitive is an object containing the following members:

- "feature", the feature to match the pattern against. Supported features are listed in the "Supported Features" section below.

- "matches", the string to match.

A pattern operation is an object containing the following members:

- "op", a string describing the logical operation to apply to the subpatterns. Valid values are "and", "or", or "not".

- "sub": a pattern object or array of one or more pattern objects, to serve as the operands. Note that the "not" operator expects exactly one object; any other number of objects will cause the pattern to fail to match.

If the pattern is an operation, then the pattern matches if and only if the logical operation applied to the subpatterns is true. For example,

``` screen
    {
        "op" : "or",
        "sub" : [ { "feature" : "procname", "matches" : "foo" },
                  { "feature" : "procname", "matches" : "bar" } ]
    }
```

matches all processes with the name "foo" \*or\* "bar". Similarly,

``` screen
    {
        "op" : "and",
        "sub" : [ { "feature" : "procname", "matches" : "foo" },
                  { "feature" : "dso", "matches" : "bar.so" } ]
    }
```

matches all processes with the name "foo" that load DSO "bar.so", and

``` screen
    {
        "op" : "not",
        "sub" : { "feature" : "procname", "matches" : "foo" }
    }
```

matches a process which is \*not\* named "foo". Nested operations are possible; for example:

``` screen
    {
        "op" : "and",
        "sub" : [
            { "feature" : "dso", "matches" : "foo.so" },
            { "op" : "not", "sub" : { "feature" : "procname", "matches" : "bar" } }
         ]
    }
```

matches processes that are \*not\* named "bar" that load DSO "foo.so".

## Extended Backus-Naur Form (EBNF) grammar

Note: this definition omits the presence of whitespace or comments, which can be inserted between any pair of symbols.

This is written in an "EBNF-like" grammar based on ISO/IEC 14977, using the following (non-EBNF) extensions:

- object(A, B, ...) indicates that each symbol A, B, etc. must appear exactly once in any order, delimited by commas and bracketed by curly braces, unless the given symbol expands to an empty string.

  For example, assuming A and B are nonempty symbols:

``` screen
  object(A, B) ;

```

  is equivalent to:

``` screen
  '{',  (A, ',', B) | (B, ',', A), '}' ;

```

  Also,

``` screen
  object([A], [B]);

```

  is equivalent to:

``` screen
  '{', [ A | B | (A, ',', B) | (B, ',', A) ], '}' ;

```

- attr(str, A) is shorthand for:

``` screen
  ( '"str"' | "'str'" ), ':', A

```

- array(A) is shorthand for:

``` screen
  '[', [ array_A ], ']'

```

  where array_A is defined as:

``` screen
  array_A = (array_A, ',' A) | A

```

The grammar follows.

``` screen
    config_file = object( [ attr(rules, array(rule)) ] ,
                          [ attr(profiles, array(profile)) ] ) ;
    rule = object(attr(pattern, pattern_object | array(pattern_object)),
                  attr(profile, profile_ref)) ;
    pattern_object = pattern_op | pattern_primitive ;
    pattern_op = object(attr(op, string),
                        attr(sub, pattern_object | array(pattern_object))) ;
    pattern_primitive = object(attr(feature, string),
                               attr(matches, string)) ;
    profile_ref = string | settings | rule_profile ;
    profile = object(attr(name, string),
                     attr(settings,
                          (array(setting_kv) | array(setting_obj)))) ;
    rule_profile = object([ attr(name, string) ],
                          attr(settings,
                          (array(setting_kv) | array(setting_obj)))) ;
    setting_kv = string ',' value ;
    setting_obj = object(attr(k,string) | attr(key,string),
                         attr(v,value) | attr(value,value)) ;
    string = ? any valid json string ? ;
    value = ? any valid json number ? | 'true' | 'false' |
            hex_value | oct_value ;
    hex_value = '0', ('x' | 'x'), hex_digit, { hex_digit } ;
    oct_value = '0', oct_digit, { oct_digit } ;
    hex_digit = ? any character in the range [0-9a-fA-F] ? ;
    oct_digit = ? any character in the range [0-7] ? ;

```

## Rule Precedence

Profiles may be specified in any order, and rules defined in files earlier in the search path may refer to profiles defined later in the search path.

Rules are prioritized based on the order in which they are defined: each rule has precedence over rules defined after it in the same file, and rules defined in a file have precedence over rules defined in files that come after that file in the search path.

For example, if there are two files A and B, such that A comes before B in the search path, with the following contents:

``` screen
    # File A
    {
        "rules" : [ { "pattern" : "foo",
                      "profile" : [ "a", 1 ] },
                    { "pattern" : "foo",
                      "profile" : [ "a", 0, "b", 2 ] } ]
    }

    # File B
    {
        "rules" : [ { "pattern" : "foo",
                      "profile" : [ "a", 0, "b", 0, "c", 3 ] } ]
    }

```

and the driver is loaded into a process with the name "foo", it will apply the settings "a" = 1, "b" = 2, and "c" = 3.

Settings specified via application profiles have higher precedence than global settings specified in nvidia-settings, but lower precedence than settings specified directly via environment variables.

## Configuration File Example

The following is a sample configuration file which demonstrates the various ways one can specify application profiles and rules for different processes.

``` screen
    {
    "rules" : [

        # Define a rule with an inline profile, (implicitly) using
        # feature "procname".
        { "pattern" : "glxgears", "profile" : [ "GLSyncToVBlank", "1" ] },

        # Define a rule with a named profile, (implicitly) using feature
        # "procname".
        { "pattern" : "gloss", "profile" : "p0" },

        # Define a rule with a named profile, using feature "dso".
        { "pattern" : { "feature" : "dso", "matches" : "libpthread.so.0" },
          "profile" : "p1" },

        # Define a rule with a named, inline profile, using feature "true";
        # patterns using this feature will always match, and can be used
        # to write catch-all rules.
        { "pattern" : { "feature" : "true", "matches" : "" },
          "profile" : { "name" : "p2",
                        "settings" : [ "GLSyncToVBlank", 1 ] } },

        # Define a rule with multiple patterns. This rule will only be
        # applied if the current process is named "foo" and has loaded
        # "bar.so".
        { "pattern" : [ { "feature" : "procname", "matches" : "foo" },
                        { "feature" : "dso", "matches" : "bar.so" } ],
          "profile" : "p1" },

        # Define a rule with no patterns. This rule will always be applied.
        { "pattern" : [], "profile" : "p1" }

    ],
    "profiles" : [

        # define a profile with settings defined in a key/value array
        { "name" : "p0", "settings" : [ "GLSyncToVBlank", 0 ] },

        # define a profile with settings defined in an array of setting
        # objects
        { "name" : "p1", "settings" : [ { "k" : "GLDoom3", "v" : false } ] }

    ]
    }

```

## Supported Features

This NVIDIA Linux driver supports detection of the following features:

- "true": patterns using this feature will always match, regardless of the contents of the string provided by "matches".

- "procname": patterns using this feature compare the string provided by "matches" against the pathname of the current process with the leading directory components removed and match if they are equal.

- "commname": patterns using this feature compare the string provided by "matches" against the commandname of the current process, as stored in /proc/self/comm.

- "cmdline": patterns using this feature compare the string provided by "matches" against the argument 0 of the command line for the current process, as stored in /proc/self/cmdline (with leading directory components removed, separated by slashes and backslashes).

  This is useful for applications and games running through Wine. For example "glxgears" would match a process started with "/usr/bin/glxgears" or "notepad.exe" would match a process started with "wine C:\Windows\notepad.exe".

- "dso": patterns using this feature compare the string provided by "matches" against the list of currently loaded libraries in the current process and match if the string matches one of the entries in the list (with leading directory components removed).

  Please note that application detection occurs when the driver component ("libGL.so.1" in the case of GLX) is first loaded by a process, so a pattern using this feature may fail to match if the library specified by the pattern is loaded after the component is loaded. A potential workaround for this on Linux is to set the LD_PRELOAD environment variable (see ld-linux(8)) to include the component, as in the following example:

``` screen
      LD_PRELOAD="libGL.so.1" glxgears

```

  Note this defeats one of the objectives of application detection (namely the need to set environment variables on the command line before running the application), but this may be useful when there is a need to frequently change driver settings for a particular application: one can write a wrapper script to set LD_PRELOAD once, then modify the JSON configuration repeatedly without needing to edit the wrapper script later on.

  Also note that the pattern matches against library names as they appear in the maps file of that process (see proc(5)), and not the names of symbolic links to these libraries.

- "findfile": patterns using this feature should provide a colon-separated list of filenames in the "matches" argument. At runtime, the driver scans the directory of the process executable and matches the pattern if every file specified in this list is present in the same directory. Please note there is currently no support for matching against files in other paths than the process executable directory.

## List of supported application profile settings

The list of supported application profile settings and their equivalent environment variable names (if any) is as follows:

- "GLFSAAMode" : see \_\_GL_FSAA_MODE

- "GLLogMaxAniso" : see \_\_GL_LOG_MAX_ANISO

- "GLNoDsoFinalizer" : see \_\_GL_NO_DSO_FINALIZER

- "GLSingleThreaded" : see \_\_GL_SINGLE_THREADED

- "GLSyncDisplayDevice" : see \_\_GL_SYNC_DISPLAY_DEVICE

- "GLSyncToVblank" : see \_\_GL_SYNC_TO_VBLANK

- "GLSortFbconfigs" : see \_\_GL_SORT_FBCONFIGS

- "GLAllowUnofficialProtocol" : see \_\_GL_ALLOW_UNOFFICIAL_PROTOCOL

- "GLSELinuxBooleans" : see \_\_GL_SELINUX_BOOLEANS

- "GLShaderDiskCache" : see \_\_GL_SHADER_DISK_CACHE

- "GLShaderDiskCachePath" : see \_\_GL_SHADER_DISK_CACHE_PATH

- "GLYield" : see \_\_GL_YIELD

- "GLThreadedOptimizations" : see \_\_GL_THREADED_OPTIMIZATIONS

- "GLDoom3" : see \_\_GL_DOOM3

- "GLExtensionStringVersion" : see \_\_GL_ExtensionStringVersion

- "GLConformantBlitFramebufferScissor" : see \_\_GL_ConformantBlitFramebufferScissor

- "GLAllowFXAAUsage" : see \_\_GL_ALLOW_FXAA_USAGE

- "GLVRRAllowed" : see \_\_GL_VRR_ALLOWED

- "GLWriteTextSection" : see \_\_GL_WRITE_TEXT_SECTION

- "GLIgnoreGLSLExtReqs" : see \_\_GL_IGNORE_GLSL_EXT_REQS

- "EGLVisibleDGPUDevices"

  On a multi-device system, this option can be used to make EGL ignore certain devices. This setting takes a 32-bit mask encoding a whitelist of visible devices. The bit position matches the minor number of the device to make visible.

  For instance, the profile

``` screen
      {
          "rules" : [
              { "pattern" : [],
                "profile" : [ "EGLVisibleDGPUDevices", 0x00000002 ] }
          ]
      }

```

  would only make the device with minor number 1 visible (i.e. /dev/nvidia1).

- "EGLVisibleTegraDevices" : Same semantics as EGLVisibleDGPUDevices

- "GLShowGraphicsOSD" : see \_\_GL_SHOW_GRAPHICS_OSD

- "GLSharpenEnable" : see \_\_GL_SHARPEN_ENABLE

- "GLSharpenValue" : see \_\_GL_SHARPEN_VALUE

- "GLSharpenIgnoreFilmGrain" : see \_\_GL_SHARPEN_IGNORE_FILM_GRAIN
