# Man / Pvmove

```text
PVMOVE(8)                    System Manager's Manual                   PVMOVE(8)

NAME
     pvmove —— Move extents from one physical volume to another

SYNOPSIS
     pvmove position_args
            [ option_args ]
            [ position_args ]

DESCRIPTION
     pvmove  moves the allocated physical extents (PEs) on a source PV to one or
     more destination PVs.  You can optionally specify a source LV in which case
     only extents used by that LV will be moved to free (or  specified)  extents
     on  the destination PV. If no destination PV is specified, the normal allo‐
     cation rules for the VG are used.

     If pvmove is interrupted for any reason (e.g. the machine crashes) then run
     pvmove again without any PV arguments to restart any operations  that  were
     in  progress  from the last checkpoint. Alternatively, use the abort option
     at any time to abort the operation. The resulting location of LVs after  an
     abort depends on whether the atomic option was used.

     More than one pvmove can run concurrently if they are moving data from dif‐
     ferent  source  PVs,  but additional pvmoves will ignore any LVs already in
     the process of being changed, so some data might not get moved.

USAGE
     Move PV extents.

     pvmove PV
            [ -A|--autobackup y|n ]
            [ -n|--name String ]
            [ --alloc contiguous|cling|cling_by_tags|normal|anywhere|inherit ]
            [ --atomic ]
            [ --noudevsync ]
            [ --reportformat basic|json|json_std ]
            [ COMMON_OPTIONS ]
            [ PV ... ]

     ——

     Continue or abort existing pvmove operations.

     pvmove
            [ COMMON_OPTIONS ]

     ——

     Common options for command:
            [ -b|--background ]
            [ -i|--interval [+]Number ]
            [ --abort ]

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
     --abort
            Abort any pvmove operations in progress. If  a  pvmove  was  started
            with the --atomic option, then all LVs will remain on the source PV.
            Otherwise, segments that have been moved will remain on the destina‐
            tion PV, while unmoved segments will remain on the source PV.

     --alloc contiguous|cling|cling_by_tags|normal|anywhere|inherit
            Determines  the  allocation  policy when a command needs to allocate
            Physical Extents (PEs) from the VG. Each VG and LV has an allocation
            policy which can be changed with vgchange/lvchange, or overridden on
            the command line.  normal applies common sense  rules  such  as  not
            placing  parallel  stripes  on  the same PV.  inherit applies the VG
            policy to an LV.  contiguous requires new PEs to be placed  adjacent
            to  existing  PEs.   cling places new PEs on the same PV as existing
            PEs in the same stripe of the LV.  If there are sufficient  PEs  for
            an  allocation, but normal does not use them, anywhere will use them
            even if it reduces performance, e.g. by placing two stripes  on  the
            same  PV.   Optional positional PV args on the command line can also
            be used to limit which PVs the command will use for allocation.  See
            lvm(8) for more information about allocation.

     --atomic
            Makes a pvmove operation atomic, ensuring that all affected LVs  are
            moved  to  the  destination  PV,  or  none  are  if the operation is
            aborted.

     -A|--autobackup y|n
            Specifies if metadata should be  backed  up  automatically  after  a
            change.   Enabling this is strongly advised!  See vgcfgbackup(8) for
            more information.

     -b|--background
            If the operation requires polling, this option causes the command to
            return before the operation is complete, and polling is done in  the
            background.

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

     -h|--help
            Display help text.

     -i|--interval [+]Number
            Report  progress at regular intervals.  With a '+' prefix, the first
            check is delayed by the given number of seconds, allowing background
            operations to start before polling begins.

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

     -n|--name String
            Move only the extents belonging to the named LV.

     --nohints
            Do not use the hints file to locate devices for PVs. A  command  may
            read  more  devices to find PVs when hints are not used. The command
            will still perform standard hint file invalidation  where  appropri‐
            ate.

     --nolocking
            Disable  locking.  Use with caution, concurrent commands may produce
            incorrect results.

     --noudevsync
            Disables udev synchronization. The process will not wait for notifi‐
            cation from udev. It will continue irrespective of any possible udev
            processing in the background. Only use this if udev is  not  running
            or has rules that ignore the devices LVM creates.

     --profile String
            An alias for --commandprofile or --metadataprofile, depending on the
            command.

     -q|--quiet ...
            Suppress  output  and log messages. Overrides --debug and --verbose.
            Repeat once to also suppress any prompts with answer 'no'.

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

Red Hat, Inc.                  LVM TOOLS #VERSION#                     PVMOVE(8)
```
