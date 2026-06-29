# Man / Lvreduce

```text
LVREDUCE(8)                  System Manager's Manual                 LVREDUCE(8)

NAME
     lvreduce —— Reduce the size of a logical volume

SYNOPSIS
     lvreduce option_args position_args
            [ option_args ]

DESCRIPTION
     lvreduce  reduces the size of an LV. The freed logical extents are returned
     to the VG to be used by other LVs. A copy-on-write snapshot LV can also  be
     reduced  if  less  space  is needed to hold COW blocks. Use lvconvert(8) to
     change the number of data images in a RAID or mirrored LV.

     Be careful when reducing an LV's size, because data in the reduced area  is
     lost. Ensure that any file system on the LV is resized before running lvre‐
     duce so that the removed extents are not in use by the file system.

     Sizes will be rounded if necessary. For example, the LV size must be an ex‐
     act number of extents, and the size of a striped segment must be a multiple
     of the number of stripes.

     In the usage section below, --size Size can be replaced with --extents Num‐
     ber.  See both descriptions the options section.

USAGE
     lvreduce -L|--size [-]Size[m|UNIT] LV
            [ -l|--extents [-]Number[PERCENT] ]
            [ -A|--autobackup y|n ]
            [ -f|--force ... ]
            [ -n|--nofsck ]
            [ -r|--resizefs ]
            [ --fs String ]
            [ --fsmode String ]
            [ --noudevsync ]
            [ --reportformat basic|json|json_std ]
            [ COMMON_OPTIONS ]

     ——

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

     -l|--extents [-]Number[PERCENT]
            Specifies the new size of the LV in logical extents.  The --size and
            --extents options are alternate methods of specifying size.  The to‐
            tal  number  of physical extents used will be greater when redundant
            data is needed for RAID levels.  An alternate syntax allows the size
            to be determined indirectly as a percentage of the size of a related
            VG, LV, or set of PVs. The suffix %VG denotes the total size of  the
            VG,  the  suffix  %FREE  the remaining free space in the VG, and the
            suffix %PVS the free space in the specified PVs.   For  a  snapshot,
            the  size  can be expressed as a percentage of the total size of the
            origin LV with the suffix %ORIGIN (100%ORIGIN provides space for the
            whole origin).  When expressed as a percentage, the size defines  an
            upper  limit  for  the  number of logical extents in the new LV. The
            precise number of logical extents in the new LV  is  not  determined
            until  the command has completed.  When the plus + or minus - prefix
            is used, the value is not an absolute  size,  but  is  relative  and
            added or subtracted from the current size.

     -f|--force ...
            Override  various  checks,  confirmations and protections.  Use with
            extreme caution.

     --fs String
            Control file system resizing when resizing an LV.  checksize:  Check
            the  fs  size  and  reduce the LV if the fs is not using the reduced
            space (fs reduce is not needed.) If the reduced space is used by the
            fs, then do not resize the fs or LV, and return an  error.   (check‐
            size  only applies when reducing, and does nothing for extend.)  re‐
            size: Resize the fs by calling the fs-specific resize command.  This
            may also include mounting, unmounting, or running fsck. See --fsmode
            to control mounting behavior, and --nofsck  to  disable  fsck.   re‐
            size_fsadm:  Use  the  old  method of calling fsadm to handle the fs
            (deprecated.) Warning: this option does not  prevent  lvreduce  from
            destroying  file  systems  that are unmounted (or mounted if prompts
            are skipped.)  ignore: Resize the LV without checking  for  or  han‐
            dling  a  file  system.   Warning: using ignore when reducing the LV
            size may destroy the file system.

            Note: If resizing an LV without a file system and the  new  LV  size
            matches  the  existing  size,  the command returns a non-zero status
            code (failure).  However, if a file system resize is also  requested
            along  with  the LV resize, and the sizes already match, the command
            returns a zero status code (success). This occurs because the exter‐
            nal commands called to resize the file system return success even if
            the new and old file system sizes are identical.   LVM  follows  the
            command status code behavior in this scenario.

     --fsmode String
            Control  file system mounting behavior for fs resize.  manage: Mount
            or unmount the fs as needed to resize the fs, and attempt to restore
            the original mount state at the end.  nochange: Do not mount or  un‐
            mount  the  fs.  If mounting or unmounting is required to resize the
            fs, then do not resize the fs or the LV and fail the  command.   of‐
            fline:  Unmount  the fs if it is mounted, and resize the fs while it
            is unmounted. If mounting is required to resize the fs, then do  not
            resize the fs or the LV and fail the command.

     -h|--help
            Display help text.

     --journal String
            Record  information  in the systemd journal.  This information is in
            addition to information enabled by the lvm.conf log/journal setting.
            command: record information about the command.  output:  record  the
            default command output.  debug: record full command debugging.

     --lockopt String
            Used to pass options for special cases to lvmlockd.  See lvmlockd(8)
            for more information.

     --longhelp
            Display long help text.

     -n|--nofsck
            Do not perform fsck when resizing the file system with --resizefs.

     --nohints
            Do  not  use the hints file to locate devices for PVs. A command may
            read more devices to find PVs when hints are not used.  The  command
            will  still  perform standard hint file invalidation where appropri‐
            ate.

     --nolocking
            Disable locking. Use with caution, concurrent commands  may  produce
            incorrect results.

     --noudevsync
            Disables udev synchronization. The process will not wait for notifi‐
            cation from udev. It will continue irrespective of any possible udev
            processing  in  the background. Only use this if udev is not running
            or has rules that ignore the devices LVM creates.

     --profile String
            An alias for --commandprofile or --metadataprofile, depending on the
            command.

     -q|--quiet ...
            Suppress output and log messages. Overrides --debug  and  --verbose.
            Repeat once to also suppress any prompts with answer 'no'.

     --reportformat basic|json|json_std
            Overrides  current  output format for reports which is defined glob‐
            ally by the report/output_format setting in lvm.conf(5).   basic  is
            the  original  format  with columns and rows.  If there is more than
            one report per command, each report is prefixed with the report name
            for identification. json produces  report  output  in  JSON  format.
            json_std produces report output in JSON format which is more compli‐
            ant with JSON standard.  See lvmreport(7) for more information.

     -r|--resizefs
            Resize  the  fs  using  the  fs-specific  resize  command  (See: re‐
            size2fs(8), xfs_growfs(8), btrfs(8)).   May  include  mounting,  un‐
            mounting,  or  running fsck. See --fsmode to control mounting behav‐
            ior, and --nofsck to disable fsck. See --fs for more options  (--re‐
            sizefs is equivalent to --fs resize.)

     -L|--size [-]Size[m|UNIT]
            Specifies  the new size of the LV.  The --size and --extents options
            are alternate methods of specifying size.  The total number of phys‐
            ical extents used will be greater when redundant data is needed  for
            RAID  levels.   When the plus + or minus - prefix is used, the value
            is not an absolute size, but is relative  and  added  or  subtracted
            from the current size.

     -t|--test
            Run in test mode. Commands will not update metadata.  This is imple‐
            mented  by disabling all metadata writing but nevertheless returning
            success to the calling function. This may lead to unusual error mes‐
            sages in multi-stage operations if a tool  relies  on  reading  back
            metadata it believes has changed but hasn't.

     -v|--verbose ...
            Set  verbose  level. Repeat from 1 to 4 times to increase the detail
            of messages sent to stdout and stderr.

     --version
            Display version information.

     -y|--yes
            Do not prompt for confirmation interactively but always  assume  the
            answer yes. Use with extreme caution.  (For automatic no, see -qq.)

VARIABLES
     LV     Logical  Volume name.  See lvm(8) for valid names.  An LV positional
            arg generally includes the VG name and LV name, e.g. VG/LV.

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

Red Hat, Inc.                  LVM TOOLS #VERSION#                   LVREDUCE(8)
```
