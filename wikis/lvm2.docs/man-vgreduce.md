# Man / Vgreduce

```text
VGREDUCE(8)                  System Manager's Manual                 VGREDUCE(8)

NAME
     vgreduce —— Remove physical volume(s) from a volume group

SYNOPSIS
     vgreduce option_args position_args
            [ option_args ]

          -a|--all
          -A|--autobackup y|n
             --commandprofile String
             --config String
          -d|--debug ...
             --devices PV
             --devicesfile String
             --driverloaded y|n
          -f|--force ...
          -h|--help
             --journal String
             --lockopt String
             --longhelp
             --mirrorsonly
             --nohints
             --nolocking
             --profile String
          -q|--quiet ...
             --removemissing
             --reportformat basic|json|json_std
          -t|--test
          -v|--verbose ...
             --version
          -y|--yes

DESCRIPTION
     vgreduce removes one or more unused PVs from a VG.

USAGE
     Remove a PV from a VG.

     vgreduce VG PV ...
            [ COMMON_OPTIONS ]

     ——

     Remove all unused PVs from a VG.

     vgreduce -a|--all VG
            [ COMMON_OPTIONS ]

     ——

     Remove all missing PVs from a VG.

     vgreduce --removemissing VG
            [ --mirrorsonly ]
            [ COMMON_OPTIONS ]

     ——

     Common options for command:
            [ -A|--autobackup y|n ]
            [ -f|--force ... ]
            [ --reportformat basic|json|json_std ]

     Common options for lvm:
            [ -d|--debug ... ]
            [ -h|--help ]
            [ -q|--quiet ... ]
            [ -t|--test ]
            [ -v|--verbose ... ]
            [ -y|--yes ]
            [ --commandprofile String ]
            [ --config String ]
            [ --devices PV ]
            [ --devicesfile String ]
            [ --driverloaded y|n ]
            [ --journal String ]
            [ --lockopt String ]
            [ --longhelp ]
            [ --nohints ]
            [ --nolocking ]
            [ --profile String ]
            [ --version ]

OPTIONS
     -a|--all
            Removes all empty PVs if none are named on the command line.

     -A|--autobackup y|n
            Specifies  if  metadata  should  be  backed up automatically after a
            change.  Enabling this is strongly advised!  See vgcfgbackup(8)  for
            more information.

     --commandprofile String
            The   command   profile  to  use  for  command  configuration.   See
            lvm.conf(5) for more information about profiles.

     --config String
            Config settings for the command.  These  override  lvm.conf(5)  set‐
            tings.   The  String arg uses the same format as lvm.conf(5), or may
            use section/field syntax.   See  lvm.conf(5)  for  more  information
            about config.

     -d|--debug ...
            Set  debug level. Repeat from 1 to 6 times to increase the detail of
            messages sent to the log file and/or syslog (if configured).

     --devices PV
            Restricts the devices that are visible and accessible  to  the  com‐
            mand.  Devices not listed will appear to be missing. This option can
            be  repeated,  or  accepts  a  comma separated list of devices. This
            overrides the devices file.

     --devicesfile String
            A file listing devices that LVM should use.  The file must exist  in
            #DEFAULT_SYS_DIR#/devices/  and  is  managed  with the lvmdevices(8)
            command.  This overrides the lvm.conf(5) devices/devicesfile and de‐
            vices/use_devicesfile settings.

     --driverloaded y|n
            If set to no, the command will not  attempt  to  use  device-mapper.
            For testing and debugging.

     -f|--force ...
            Override  various  checks,  confirmations and protections.  Use with
            extreme caution.

     -h|--help
            Display help text.

     --journal String
            Record information in the systemd journal.  This information  is  in
            addition to information enabled by the lvm.conf log/journal setting.
            command:  record  information about the command.  output: record the
            default command output.  debug: record full command debugging.

     --lockopt String
            Used to pass options for special cases to lvmlockd.  See lvmlockd(8)
            for more information.

     --longhelp
            Display long help text.

     --mirrorsonly
            Only remove missing PVs from mirror LVs.

     --nohints
            Do not use the hints file to locate devices for PVs. A  command  may
            read  more  devices to find PVs when hints are not used. The command
            will still perform standard hint file invalidation  where  appropri‐
            ate.

     --nolocking
            Disable  locking.  Use with caution, concurrent commands may produce
            incorrect results.

     --profile String
            An alias for --commandprofile or --metadataprofile, depending on the
            command.

     -q|--quiet ...
            Suppress output and log messages. Overrides --debug  and  --verbose.
            Repeat once to also suppress any prompts with answer 'no'.

     --removemissing
            Removes  all  missing PVs from the VG, if there are no LVs allocated
            on them. This resumes normal operation of the VG (new LVs may  again
            be created, changed and so on).  If this is not possible because LVs
            are  referencing  the  missing PVs, this option can be combined with
            --force to have the command remove any partial LVs.  In  this  case,
            any  LVs  and  dependent  snapshots  that were partly on the missing
            disks are removed completely, including those parts  on  disks  that
            are  still  present.   If  LVs spanned several disks, including ones
            that are lost, salvaging some data first may be possible by activat‐
            ing LVs in partial mode.

     --reportformat basic|json|json_std
            Overrides current output format for reports which is  defined  glob‐
            ally  by  the report/output_format setting in lvm.conf(5).  basic is
            the original format with columns and rows.  If there  is  more  than
            one report per command, each report is prefixed with the report name
            for  identification.  json  produces  report  output in JSON format.
            json_std produces report output in JSON format which is more compli‐
            ant with JSON standard.  See lvmreport(7) for more information.

     -t|--test
            Run in test mode. Commands will not update metadata.  This is imple‐
            mented by disabling all metadata writing but nevertheless  returning
            success to the calling function. This may lead to unusual error mes‐
            sages  in  multi-stage  operations  if a tool relies on reading back
            metadata it believes has changed but hasn't.

     -v|--verbose ...
            Set verbose level. Repeat from 1 to 4 times to increase  the  detail
            of messages sent to stdout and stderr.

     --version
            Display version information.

     -y|--yes
            Do  not  prompt for confirmation interactively but always assume the
            answer yes. Use with extreme caution.  (For automatic no, see -qq.)

VARIABLES
     VG     Volume Group name.  See lvm(8) for valid names.

     PV     Physical Volume name, a device path under /dev.  For commands manag‐
            ing physical extents, a PV positional arg generally accepts a suffix
            indicating a range (or multiple ranges) of physical  extents  (PEs).
            When  the  first  PE is omitted, it defaults to the start of the de‐
            vice, and when the last PE is omitted it defaults to end.
            Start and end range (inclusive): PV[:PE-PE] ...
            Start and length range (counting from 0): PV[:PE+PE] ...

     String
            See the option description for information about the string content.

     Size[UNIT]
            Size is an input number that accepts an optional unit.  Input  units
            are always treated as base two values, regardless of capitalization,
            e.g.  'k'  and  'K'  both  refer to 1024.  The default input unit is
            specified by letter, followed by |UNIT.  UNIT represents other  pos‐
            sible input units: b|B is bytes, s|S is sectors of 512 bytes, k|K is
            KiB,  m|M  is  MiB,  g|G is GiB, t|T is TiB, p|P is PiB, e|E is EiB.
            (This should not be confused with the output control --units,  where
            capital letters mean multiple of 1000.)

ENVIRONMENT VARIABLES
     See  lvm(8)  for  information about environment variables used by lvm.  For
     example, LVM_VG_NAME can generally be substituted for a required VG parame‐
     ter.

Red Hat, Inc.                  LVM TOOLS #VERSION#                   VGREDUCE(8)
```
