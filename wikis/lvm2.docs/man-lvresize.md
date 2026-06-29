# Man / Lvresize

```text
LVRESIZE(8)                  System Manager's Manual                 LVRESIZE(8)

NAME
     lvresize —— Resize a logical volume

SYNOPSIS
     lvresize option_args position_args
            [ option_args ]
            [ position_args ]

             --alloc contiguous|cling|cling_by_tags|normal|anywhere|inherit
          -A|--autobackup y|n
             --commandprofile String
             --config String
          -d|--debug ...
             --devices PV
             --devicesfile String
             --driverloaded y|n
          -l|--extents [+|-]Number[PERCENT]
          -f|--force ...
             --fs String
             --fsmode String
          -h|--help
             --journal String
             --lockopt String
             --longhelp
          -n|--nofsck
             --nohints
             --nolocking
             --nosync
             --noudevsync
             --poolmetadatasize [+]Size[m|UNIT]
             --profile String
          -q|--quiet ...
             --reportformat basic|json|json_std
          -r|--resizefs
          -L|--size [+|-]Size[m|UNIT]
          -i|--stripes Number
          -I|--stripesize Size[k|UNIT]
          -t|--test
             --type linear|striped|snapshot|raid|mirror|thin|thin-pool|vdo|
          vdo-pool|cache|cache-pool|writecache
          -v|--verbose ...
             --version
          -y|--yes

DESCRIPTION
     lvresize  resizes an LV in the same way as lvextend and lvreduce. See lvex‐
     tend(8) and lvreduce(8) for more information.

     In the usage section below, --size Size can be replaced with --extents Num‐
     ber.  See both descriptions the options section.

USAGE
     Resize an LV by a specified size.

     lvresize -L|--size [+|-]Size[m|UNIT] LV
            [ -l|--extents [+|-]Number[PERCENT] ]
            [ -r|--resizefs ]
            [ --fs String ]
            [ --fsmode String ]
            [ --poolmetadatasize [+]Size[m|UNIT] ]
            [ COMMON_OPTIONS ]
            [ PV ... ]

     ——

     Resize an LV by specified PV extents.

     lvresize LV PV ...
            [ -r|--resizefs ]
            [ --fs String ]
            [ --fsmode String ]
            [ COMMON_OPTIONS ]

     ——

     Resize a pool metadata SubLV by a specified size.

     lvresize --poolmetadatasize [+]Size[m|UNIT] LV1
            [ COMMON_OPTIONS ]
            [ PV ... ]

            LV1 types: linear thinpool

     ——

     Common options for command:
            [ -A|--autobackup y|n ]
            [ -f|--force ... ]
            [ -n|--nofsck ]
            [ -i|--stripes Number ]
            [ -I|--stripesize Size[k|UNIT] ]
            [ --alloc contiguous|cling|cling_by_tags|normal|anywhere|inherit ]
            [ --nosync ]
            [ --noudevsync ]
            [ --reportformat basic|json|json_std ]
            [     --type linear|striped|snapshot|raid|mirror|thin|thin-pool|vdo|
            vdo-pool|cache|cache-pool|writecache ]

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

     -A|--autobackup y|n
            Specifies if metadata should be  backed  up  automatically  after  a
            change.   Enabling this is strongly advised!  See vgcfgbackup(8) for
            more information.

     --commandprofile String
            The  command  profile  to  use  for  command   configuration.    See
            lvm.conf(5) for more information about profiles.

     --config String
            Config  settings  for  the  command. These override lvm.conf(5) set‐
            tings.  The String arg uses the same format as lvm.conf(5),  or  may
            use  section/field  syntax.   See  lvm.conf(5)  for more information
            about config.

     -d|--debug ...
            Set debug level. Repeat from 1 to 6 times to increase the detail  of
            messages sent to the log file and/or syslog (if configured).

     --devices PV
            Restricts  the  devices  that are visible and accessible to the com‐
            mand.  Devices not listed will appear to be missing. This option can
            be repeated, or accepts a comma  separated  list  of  devices.  This
            overrides the devices file.

     --devicesfile String
            A  file listing devices that LVM should use.  The file must exist in
            #DEFAULT_SYS_DIR#/devices/ and is  managed  with  the  lvmdevices(8)
            command.  This overrides the lvm.conf(5) devices/devicesfile and de‐
            vices/use_devicesfile settings.

     --driverloaded y|n
            If  set  to  no,  the command will not attempt to use device-mapper.
            For testing and debugging.

     -l|--extents [+|-]Number[PERCENT]
            Specifies the new size of the LV in logical extents.  The --size and
            --extents options are alternate methods of specifying size.  The to‐
            tal number of physical extents used will be greater  when  redundant
            data is needed for RAID levels.  An alternate syntax allows the size
            to be determined indirectly as a percentage of the size of a related
            VG,  LV, or set of PVs. The suffix %VG denotes the total size of the
            VG, the suffix %FREE the remaining free space in  the  VG,  and  the
            suffix  %PVS  the  free space in the specified PVs.  For a snapshot,
            the size can be expressed as a percentage of the total size  of  the
            origin LV with the suffix %ORIGIN (100%ORIGIN provides space for the
            whole  origin).  When expressed as a percentage, the size defines an
            upper limit for the number of logical extents in  the  new  LV.  The
            precise  number  of  logical extents in the new LV is not determined
            until the command has completed.  When the plus + or minus -  prefix
            is  used,  the  value  is  not an absolute size, but is relative and
            added or subtracted from the current size.

     -f|--force ...
            Override various checks, confirmations and  protections.   Use  with
            extreme caution.

     --fs String
            Control  file system resizing when resizing an LV.  checksize: Check
            the fs size and reduce the LV if the fs is  not  using  the  reduced
            space (fs reduce is not needed.) If the reduced space is used by the
            fs,  then  do not resize the fs or LV, and return an error.  (check‐
            size only applies when reducing, and does nothing for extend.)   re‐
            size: Resize the fs by calling the fs-specific resize command.  This
            may also include mounting, unmounting, or running fsck. See --fsmode
            to  control  mounting  behavior,  and --nofsck to disable fsck.  re‐
            size_fsadm: Use the old method of calling fsadm  to  handle  the  fs
            (deprecated.)  Warning:  this  option does not prevent lvreduce from
            destroying file systems that are unmounted (or  mounted  if  prompts
            are  skipped.)   ignore:  Resize the LV without checking for or han‐
            dling a file system.  Warning: using ignore  when  reducing  the  LV
            size may destroy the file system.

            Note:  If  resizing  an LV without a file system and the new LV size
            matches the existing size, the command  returns  a  non-zero  status
            code  (failure).  However, if a file system resize is also requested
            along with the LV resize, and the sizes already match,  the  command
            returns a zero status code (success). This occurs because the exter‐
            nal commands called to resize the file system return success even if
            the  new  and  old file system sizes are identical.  LVM follows the
            command status code behavior in this scenario.

     --fsmode String
            Control file system mounting behavior for fs resize.  manage:  Mount
            or unmount the fs as needed to resize the fs, and attempt to restore
            the  original mount state at the end.  nochange: Do not mount or un‐
            mount the fs. If mounting or unmounting is required  to  resize  the
            fs,  then  do not resize the fs or the LV and fail the command.  of‐
            fline: Unmount the fs if it is mounted, and resize the fs  while  it
            is  unmounted. If mounting is required to resize the fs, then do not
            resize the fs or the LV and fail the command.

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

     -n|--nofsck
            Do not perform fsck when resizing the file system with --resizefs.

     --nohints
            Do not use the hints file to locate devices for PVs. A  command  may
            read  more  devices to find PVs when hints are not used. The command
            will still perform standard hint file invalidation  where  appropri‐
            ate.

     --nolocking
            Disable  locking.  Use with caution, concurrent commands may produce
            incorrect results.

     --nosync
            Causes the creation of mirror, raid1, raid4,  raid5  and  raid10  to
            skip  the  initial  synchronization.  In  case  of mirror, raid1 and
            raid10, any data written afterwards will be mirrored, but the origi‐
            nal contents will not be copied. In case of raid4 and raid5, no par‐
            ity blocks will be written, though any data written afterwards  will
            cause parity blocks to be stored.  This is useful for skipping a po‐
            tentially  long and resource intensive initial sync of an empty mir‐
            ror/raid1/raid4/raid5 and raid10 LV.  This option is not  valid  for
            raid6, because raid6 relies on proper parity (P and Q Syndromes) be‐
            ing  created  during initial synchronization in order to reconstruct
            proper user data in case of device failures.  raid0  and  raid0_meta
            do  not  provide  any  data copies or parity support and thus do not
            support initial synchronization.

     --noudevsync
            Disables udev synchronization. The process will not wait for notifi‐
            cation from udev. It will continue irrespective of any possible udev
            processing in the background. Only use this if udev is  not  running
            or has rules that ignore the devices LVM creates.

     --poolmetadatasize [+]Size[m|UNIT]
            Specifies  the  new size of the pool metadata LV.  The plus prefix +
            can be used, in which case the value is added to the current size.

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

     -L|--size [+|-]Size[m|UNIT]
            Specifies  the new size of the LV.  The --size and --extents options
            are alternate methods of specifying size.  The total number of phys‐
            ical extents used will be greater when redundant data is needed  for
            RAID  levels.   When the plus + or minus - prefix is used, the value
            is not an absolute size, but is relative  and  added  or  subtracted
            from the current size.

     -i|--stripes Number
            Specifies  the number of stripes in a striped LV. This is the number
            of PVs (devices) that a striped LV is spread across. Data  that  ap‐
            pears  sequential  in  the  LV  is spread across multiple devices in
            units of the stripe size (see --stripesize). This  does  not  change
            existing  allocated space, but only applies to space being allocated
            by the command.  When creating a RAID 4/5/6 LV, this number does not
            include the extra devices that are required for parity. The  largest
            number depends on the RAID type (raid0: 64, raid10: 32, raid4/5: 63,
            raid6:  62),  and  when unspecified, the default depends on the RAID
            type (raid0: 2, raid10: 2, raid4/5: 3, raid6: 5.)  To stripe  a  new
            raid   LV  across  all  PVs  by  default,  see  lvm.conf(5)  alloca‐
            tion/raid_stripe_all_devices.

     -I|--stripesize Size[k|UNIT]
            The amount of data that is written to one device  before  moving  to
            the next in a striped LV.

     -t|--test
            Run in test mode. Commands will not update metadata.  This is imple‐
            mented  by disabling all metadata writing but nevertheless returning
            success to the calling function. This may lead to unusual error mes‐
            sages in multi-stage operations if a tool  relies  on  reading  back
            metadata it believes has changed but hasn't.

     --type linear|striped|snapshot|raid|mirror|thin|thin-pool|vdo|vdo-pool|
     cache|cache-pool|writecache
            The  LV  type, also known as "segment type" or "segtype".  See usage
            descriptions for the specific ways to use these types.  For more in‐
            formation  about  redundancy  and  performance   (raid<N>,   mirror,
            striped, linear) see lvmraid(7).  For thin provisioning (thin, thin-
            pool)  see  lvmthin(7).  For performance caching (cache, cache-pool)
            see lvmcache(7).  For copy-on-write snapshots (snapshot)  see  usage
            definitions.  For VDO (vdo) see lvmvdo(7).  Several commands omit an
            explicit type option because the type is inferred from other options
            or  shortcuts (e.g. --stripes, --mirrors, --snapshot, --virtualsize,
            --thin, --cache, --vdo).  Use inferred types with  care  because  it
            can lead to unexpected results.

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
            arg generally includes the VG name and LV name, e.g. VG/LV.  LV1 in‐
            dicates the LV must have a specific  type,  where  the  accepted  LV
            types are listed. (raid represents raid<N> type).

     PV     Physical Volume name, a device path under /dev.  For commands manag‐
            ing physical extents, a PV positional arg generally accepts a suffix
            indicating  a  range (or multiple ranges) of physical extents (PEs).
            When the first PE is omitted, it defaults to the start  of  the  de‐
            vice, and when the last PE is omitted it defaults to end.
            Start and end range (inclusive): PV[:PE-PE] ...
            Start and length range (counting from 0): PV[:PE+PE] ...

     String
            See the option description for information about the string content.

     Size[UNIT]
            Size  is an input number that accepts an optional unit.  Input units
            are always treated as base two values, regardless of capitalization,
            e.g. 'k' and 'K' both refer to 1024.   The  default  input  unit  is
            specified  by letter, followed by |UNIT.  UNIT represents other pos‐
            sible input units: b|B is bytes, s|S is sectors of 512 bytes, k|K is
            KiB, m|M is MiB, g|G is GiB, t|T is TiB, p|P is  PiB,  e|E  is  EiB.
            (This  should not be confused with the output control --units, where
            capital letters mean multiple of 1000.)

ENVIRONMENT VARIABLES
     See lvm(8) for information about environment variables used  by  lvm.   For
     example, LVM_VG_NAME can generally be substituted for a required VG parame‐
     ter.

Red Hat, Inc.                  LVM TOOLS #VERSION#                   LVRESIZE(8)
```
