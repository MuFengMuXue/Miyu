# Man / Vgchange

```text
VGCHANGE(8)                  System Manager's Manual                 VGCHANGE(8)

NAME
     vgchange —— Change volume group attributes

SYNOPSIS
     vgchange option_args position_args
            [ option_args ]
            [ position_args ]

          -a|--activate y|n|ay
             --activationmode partial|degraded|complete
             --addtag Tag
             --alloc contiguous|cling|cling_by_tags|normal|anywhere|inherit
             --autoactivation String
          -A|--autobackup y|n
             --commandprofile String
             --config String
          -d|--debug ...
             --deltag Tag
             --detachprofile
             --devices PV
             --devicesfile String
             --driverloaded y|n
          -f|--force ...
          -h|--help
          -K|--ignoreactivationskip
             --ignorelockingfailure
             --ignoremonitoring
             --journal String
             --lockopt String
             --lockstart
             --lockstop
             --locktype sanlock|dlm|none
          -l|--logicalvolume Number
             --longhelp
             --majoritypvs
          -p|--maxphysicalvolumes Number
             --metadataprofile String
             --monitor y|n
             --nohints
             --nolocking
             --noudevsync
          -P|--partial
             --persist String
          -s|--physicalextentsize Size[m|UNIT]
             --poll y|n
             --profile String
             --pvmetadatacopies 0|1|2
          -q|--quiet ...
             --readonly
             --refresh
             --removekey String
             --reportformat basic|json|json_std
          -x|--resizeable y|n
          -S|--select String
             --setautoactivation y|n
             --setlockargs String
             --setpersist String
             --sysinit
             --systemid String
          -t|--test
          -u|--uuid
          -v|--verbose ...
             --version
             --[vg]metadatacopies all|unmanaged|Number
          -y|--yes

DESCRIPTION
     vgchange  changes  VG  attributes, changes LV activation in the kernel, and
     includes other utilities for VG maintenance.

USAGE
     Change a general VG attribute.  For options listed in parentheses, any one
     is required, after which the others are optional.

     vgchange
            ( -l|--logicalvolume Number
              -p|--maxphysicalvolumes Number
              -s|--physicalextentsize Size[m|UNIT]
              -u|--uuid
              -x|--resizeable y|n
              --addtag Tag
              --alloc contiguous|cling|cling_by_tags|normal|anywhere|inherit
              --deltag Tag
              --detachprofile
              --metadataprofile String
              --pvmetadatacopies 0|1|2
              --setautoactivation y|n
              --[vg]metadatacopies all|unmanaged|Number )
            [ -A|--autobackup y|n ]
            [ -f|--force ... ]
            [ -S|--select String ]
            [ --ignoremonitoring ]
            [ --noudevsync ]
            [ --poll y|n ]
            [ --reportformat basic|json|json_std ]
            [ COMMON_OPTIONS ]
            [ VG|Tag|Select ... ]

     ——

     Start or stop monitoring LVs from dmeventd.

     vgchange --monitor y|n
            [ -A|--autobackup y|n ]
            [ -f|--force ... ]
            [ -S|--select String ]
            [ --ignorelockingfailure ]
            [ --ignoremonitoring ]
            [ --noudevsync ]
            [ --poll y|n ]
            [ --reportformat basic|json|json_std ]
            [ --sysinit ]
            [ COMMON_OPTIONS ]
            [ VG|Tag|Select ... ]

     ——

     Start or stop processing LV conversions.

     vgchange --poll y|n
            [ -A|--autobackup y|n ]
            [ -f|--force ... ]
            [ -S|--select String ]
            [ --ignorelockingfailure ]
            [ --ignoremonitoring ]
            [ --noudevsync ]
            [ --reportformat basic|json|json_std ]
            [ COMMON_OPTIONS ]
            [ VG|Tag|Select ... ]

     ——

     Activate or deactivate LVs.

     vgchange -a|--activate y|n|ay
            [ -A|--autobackup y|n ]
            [ -f|--force ... ]
            [ -K|--ignoreactivationskip ]
            [ -P|--partial ]
            [ -S|--select String ]
            [ --activationmode partial|degraded|complete ]
            [ --autoactivation String ]
            [ --ignorelockingfailure ]
            [ --ignoremonitoring ]
            [ --monitor y|n ]
            [ --noudevsync ]
            [ --persist String ]
            [ --poll y|n ]
            [ --readonly ]
            [ --reportformat basic|json|json_std ]
            [ --sysinit ]
            [ COMMON_OPTIONS ]
            [ VG|Tag|Select ... ]

     ——

     Reactivate LVs using the latest metadata.

     vgchange --refresh
            [ -A|--autobackup y|n ]
            [ -f|--force ... ]
            [ -S|--select String ]
            [ --ignorelockingfailure ]
            [ --ignoremonitoring ]
            [ --noudevsync ]
            [ --poll y|n ]
            [ --reportformat basic|json|json_std ]
            [ --sysinit ]
            [ COMMON_OPTIONS ]
            [ VG|Tag|Select ... ]

     ——

     Change the system ID of a VG.

     vgchange --systemid String VG|Tag|Select
            [ -S|--select String ]
            [ --majoritypvs ]
            [ --persist String ]
            [ --removekey String ]
            [ COMMON_OPTIONS ]

     ——

     Set or clear flags to control persistent reservation behavior.

     vgchange --setpersist String VG|Tag|Select
            [ -S|--select String ]
            [ --persist start ]
            [ COMMON_OPTIONS ]

     ——

     Perform persistent reservation commands on devices.

     vgchange --persist String VG|Tag|Select
            [ -f|--force ... ]
            [ -S|--select String ]
            [ --majoritypvs ]
            [ --removekey String ]
            [ COMMON_OPTIONS ]

     ——

     Set or clear lock_args flags to control lock manager behavior.

     vgchange --setlockargs String VG|Tag|Select
            [ -S|--select String ]
            [ COMMON_OPTIONS ]

     ——

     Start the lockspace of a shared VG in lvmlockd.

     vgchange --lockstart
            [ -S|--select String ]
            [ --persist start ]
            [ COMMON_OPTIONS ]
            [ VG|Tag|Select ... ]

     ——

     Stop the lockspace of a shared VG in lvmlockd.

     vgchange --lockstop
            [ -S|--select String ]
            [ --persist stop ]
            [ COMMON_OPTIONS ]
            [ VG|Tag|Select ... ]

     ——

     Change the lock type for a shared VG.

     vgchange --locktype sanlock|dlm|none VG
            [ --setlockargs String ]
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
     -a|--activate y|n|ay
            Change the active state of LVs.  An active LV can be used through  a
            block  device,  allowing data on the LV to be accessed.  y makes LVs
            active, or available.  n makes LVs inactive,  or  unavailable.   The
            block  device  for  the LV is added or removed from the system using
            device-mapper in the kernel.   A  symbolic  link  /dev/VGName/LVName
            pointing to the device node is also added/removed.  All software and
            scripts  should  access  the  device  through  the symbolic link and
            present this as the name of the device.  The location  and  name  of
            the  underlying device node may depend on the distribution, configu‐
            ration (e.g. udev), or release version.   ay  specifies  autoactiva‐
            tion,  which is used by system-generated activation commands. By de‐
            fault, LVs are autoactivated.  An autoactivation property can be set
            on a VG or LV to disable autoactivation, see --setautoactivation y|n
            in vgchange, lvchange, vgcreate, and lvcreate.  Display the property
            with vgs or lvs "-o autoactivation".  The  lvm.conf(5)  auto_activa‐
            tion_volume_list includes names of VGs or LVs that should be autoac‐
            tivated,  and  anything  not  listed  is  not  autoactivated.   When
            auto_activation_volume_list is undefined (the default),  it  has  no
            effect.  If auto_activation_volume_list is defined and empty, no LVs
            are  autoactivated.   Items  included by auto_activation_volume_list
            will not be autoactivated if the autoactivation  property  has  been
            disabled.  See lvmlockd(8) for more information about activation op‐
            tions ey and sy for shared VGs.

     --activationmode partial|degraded|complete
            Determines  if  LV  activation is allowed when PVs are missing, e.g.
            because of a device failure.  complete only allows LVs with no miss‐
            ing PVs to be activated, and is the most restrictive mode.  degraded
            allows RAID LVs with missing PVs to be activated.   (This  does  not
            include the "mirror" type, see "raid1" instead.)  partial allows any
            LV with missing PVs to be activated, and should only be used for re‐
            covery  or  repair.   For  default, see lvm.conf(5) activation_mode.
            See lvmraid(7) for more information.

     --addtag Tag
            Adds a tag to a PV, VG or LV. This option can  be  repeated  to  add
            multiple tags at once. See lvm(8) for information about tags.

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

     --autoactivation String
            Specify if autoactivation is being used from an event.  This  allows
            the command to apply settings that are specific to event activation,
            such as device scanning optimizations using pvs_online files created
            by event-based pvscans.

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

     --deltag Tag
            Deletes a tag from a PV, VG or LV. This option can  be  repeated  to
            delete multiple tags at once. See lvm(8) for information about tags.

     --detachprofile
            Detaches  a  metadata  profile from a VG or LV.  See lvm.conf(5) for
            more information about profiles.

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

     -K|--ignoreactivationskip
            Ignore the "activation skip" LV flag during activation to allow  LVs
            with the flag set to be activated.

     --ignorelockingfailure
            Allows  a command to continue with read-only metadata operations af‐
            ter locking failures.

     --ignoremonitoring
            Do not interact with dmeventd unless --monitor is specified.  Do not
            use this if dmeventd is already monitoring a device.

     --journal String
            Record information in the systemd journal.  This information  is  in
            addition to information enabled by the lvm.conf log/journal setting.
            command:  record  information about the command.  output: record the
            default command output.  debug: record full command debugging.

     --lockopt String
            Used to pass options for special cases to lvmlockd.  See lvmlockd(8)
            for more information.

     --lockstart
            Start the lockspace of a shared VG in lvmlockd.  lvmlockd locks  be‐
            come  available  for  the  VG, allowing LVM to use the VG.  See lvm‐
            lockd(8) for more information.

     --lockstop
            Stop the lockspace of a shared VG in lvmlockd.  lvmlockd  locks  be‐
            come  unavailable for the VG, preventing LVM from using the VG.  See
            lvmlockd(8) for more information.

     --locktype sanlock|dlm|none
            Change the VG lock type to or from a shared lock type used with lvm‐
            lockd.  See lvmlockd(8) for more information.

     -l|--logicalvolume Number
            Sets the maximum number of LVs allowed in a VG.

     --longhelp
            Display long help text.

     --majoritypvs
            Change the VG system ID if the majority of PVs in the VG are present
            (one more than half).

     -p|--maxphysicalvolumes Number
            Sets the maximum number of PVs that can belong to the VG.  The value
            0 removes any limitation.  For large numbers of PVs,  also  see  op‐
            tions  --pvmetadatacopies, and --vgmetadatacopies for improving per‐
            formance.

     --metadataprofile String
            The  metadata  profile  to  use  for  command  configuration.    See
            lvm.conf(5) for more information about profiles.

     --monitor y|n
            Start  (yes)  or stop (no) monitoring an LV with dmeventd.  dmeventd
            monitors kernel events for an LV, and performs automated maintenance
            for the LV in response to specific events.  See dmeventd(8) for more
            information.

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

     -P|--partial
            Commands will do their best to activate LVs with missing PV extents.
            Missing  extents may be replaced with error or zero segments accord‐
            ing to the  missing_stripe_filler  setting.   Metadata  may  not  be
            changed with this option.

     --persist String
            Persistent Reservation operation.  start: register local key and ac‐
            quire  reservation.   stop: unregister local key, releasing reserva‐
            tion.  remove: preempt and abort another key.  clear: remove  reser‐
            vation  and keys.  check: check if started.  autostart: start if the
            VG autostart flag is set.  lvmlocal.conf pr_key or host_id  must  be
            configured  to use PR.  For local VGs, Write Exclusive (WE) is used,
            and for shared VGs Write Exclusive, all registrants (WEAR) is  used.
            Use --setpersist to automate and/or require PR.

     -s|--physicalextentsize Size[m|UNIT]
            Sets  the  physical extent size of PVs in the VG.  The value must be
            either a power of 2 of at least 1 sector (where the sector  size  is
            the  largest sector size of the PVs currently used in the VG), or at
            least 128 KiB.  Once this value has been set,  it  is  difficult  to
            change  without  recreating  the  VG, unless no extents need moving.
            Before increasing the physical extent size, you might  need  to  use
            lvresize,  pvresize and/or pvmove so that everything fits. For exam‐
            ple, every contiguous range of extents used in a LV must  start  and
            end on an extent boundary.

     --poll y|n
            When  yes,  start the background transformation of an LV.  An incom‐
            plete transformation, e.g. pvmove or lvconvert interrupted by reboot
            or crash, can be restarted from the last checkpoint with  --poll  y.
            When  no, background transformation of an LV will not occur, and the
            transformation will not complete. It may not be appropriate to imme‐
            diately poll an LV after activation, in which case --poll n  can  be
            used to defer polling until a later --poll y command.

     --profile String
            An alias for --commandprofile or --metadataprofile, depending on the
            command.

     --pvmetadatacopies 0|1|2
            The  number  of  metadata  areas to set aside on a PV for storing VG
            metadata.  When 2, one copy of the VG  metadata  is  stored  at  the
            front of the PV and a second copy is stored at the end.  When 1, one
            copy  of  the VG metadata is stored at the front of the PV.  When 0,
            no copies of the VG metadata are stored on the given PV.   This  may
            be useful in VGs containing many PVs (this places limitations on the
            ability to use vgsplit later.)

     -q|--quiet ...
            Suppress  output  and log messages. Overrides --debug and --verbose.
            Repeat once to also suppress any prompts with answer 'no'.

     --readonly
            Prevent the command from making changes,  including  activation  and
            metadata updates.  (See --permission r for read only LVs.)

     --refresh
            If  the  LV is active, reload its metadata.  In an environment where
            udev is used to manage the /dev content, usage  of  this  option  is
            highly  recommended.  This  is because refresh also regenerates udev
            events for an LV based on which existing udev rules are  applied  to
            set  the  /dev content and permissions.  Also, this operation may be
            useful if something has gone wrong, or if some  form  of  manual  LV
            sharing is being used.

     --removekey String
            A persistent reservation key to remove.

     --reportformat basic|json|json_std
            Overrides  current  output format for reports which is defined glob‐
            ally by the report/output_format setting in lvm.conf(5).   basic  is
            the  original  format  with columns and rows.  If there is more than
            one report per command, each report is prefixed with the report name
            for identification. json produces  report  output  in  JSON  format.
            json_std produces report output in JSON format which is more compli‐
            ant with JSON standard.  See lvmreport(7) for more information.

     -x|--resizeable y|n
            Enables  or disables the addition or removal of PVs to/from a VG (by
            vgextend/vgreduce).

     -S|--select String
            Select objects for processing and reporting based on specified  cri‐
            teria.  The criteria syntax is described by --select help and lvmre‐
            port(7).   For reporting commands, one row is displayed for each ob‐
            ject matching the criteria.  See --options help for  selectable  ob‐
            ject  fields.   Rows  can be displayed with an additional "selected"
            field (-o selected) showing 1 if the row matches the selection and 0
            otherwise.  For non-reporting commands which process  LVM  entities,
            the selection is used to choose items to process.

     --setautoactivation y|n
            Set the autoactivation property on a VG or LV.  Display the property
            with  vgs or lvs "-o autoactivation".  When the autoactivation prop‐
            erty is disabled, the VG or LV will not be activated  by  a  command
            doing autoactivation (vgchange, lvchange, or pvscan using -aay.)  If
            autoactivation  is disabled on a VG, no LVs will be autoactivated in
            that VG, and the LV autoactivation property has no effect.   If  au‐
            toactivation  is enabled on a VG, autoactivation can be disabled for
            individual LVs.

     --setlockargs String
            Add or remove lock_args settings for a shared VG.  The lock_args de‐
            termine lock manager behavior for the VG.  These settings  are  only
            allowed for lock_type sanlock.  persist: use persistent reservations
            for  lock  recovery.   lvmlockd  will  preempt-abort  the persistent
            reservation of a failed lock owner so that the lock can be acquired.
            notimeout: use locks that do not time out when the owner fails.   In
            this  case, a lock owned by a failed host can only be acquired using
            the persist feature.  nopersist: do not  use  the  persist  feature.
            timeout:  do  not  use  the notimeout feature.  The default behavior
            with no settings configured is: nopersist and timeout.

     --setpersist String
            Set or clear flags to control persistent reservation  behavior.   y:
            set  require  and  autostart  flags.  n: clear require and autostart
            flags.  require: set flag, PR will be required to write or  activate
            VG.  norequire: clear require flag.  autostart: set flag, PR will be
            automatically  started.   noautostart:  clear autostart flag.  ptpl:
            set flag, use persist through power loss on devices.  noptpl:  clear
            ptpl flag.  When autostart is enabled, autoactivation and auto-lock‐
            start commands will first start PR.  lvmlocal.conf pr_key or host_id
            must  be configured to use PR.  For local VGs, enabling system_id is
            also recommended.

     --sysinit
            Indicates that vgchange/lvchange is being invoked from early  system
            initialisation  scripts  (e.g.  rc.sysinit  or  an  initrd),  before
            writable filesystems are  available.  As  such,  some  functionality
            needs  to  be  disabled and this option acts as a shortcut which se‐
            lects an appropriate set of options. Currently, this  is  equivalent
            to  using  --ignorelockingfailure, --ignoremonitoring, --poll n, and
            setting     env      var      LVM_SUPPRESS_LOCKING_FAILURE_MESSAGES.
            vgchange/lvchange skip autoactivation, and defer to pvscan autoacti‐
            vation.

     --systemid String
            Changes  the system ID of the VG. Using this option requires caution
            because the VG may become foreign to the host running  the  command,
            leaving  the  host unable to access it.  See lvmsystemid(7) for more
            information.

     -t|--test
            Run in test mode. Commands will not update metadata.  This is imple‐
            mented by disabling all metadata writing but nevertheless  returning
            success to the calling function. This may lead to unusual error mes‐
            sages  in  multi-stage  operations  if a tool relies on reading back
            metadata it believes has changed but hasn't.

     -u|--uuid
            Generate new random UUID for specified VGs.

     -v|--verbose ...
            Set verbose level. Repeat from 1 to 4 times to increase  the  detail
            of messages sent to stdout and stderr.

     --version
            Display version information.

     --[vg]metadatacopies all|unmanaged|Number
            Number  of  copies of the VG metadata that are kept.  VG metadata is
            kept in VG metadata areas on PVs in the VG, i.e. reserved  space  at
            the  start and/or end of the PVs.  Keeping a copy of the VG metadata
            on every PV can reduce performance in VGs containing a large  number
            of PVs.  When this number is set to a non-zero value, LVM will auto‐
            matically  choose  PVs  on  which to store metadata, using the meta‐
            dataignore flags on PVs to achieve the specified number.  The number
            can also be replaced with special string  values:  unmanaged  causes
            LVM  to  not  automatically manage the PV metadataignore flags.  all
            causes LVM to first clear the metadataignore flags on all  PVs,  and
            then to become unmanaged.

     -y|--yes
            Do  not  prompt for confirmation interactively but always assume the
            answer yes. Use with extreme caution.  (For automatic no, see -qq.)

VARIABLES
     VG     Volume Group name.  See lvm(8) for valid names.

     Tag    Tag name.  See lvm(8) for information about tag names and using tags
            in place of a VG, LV or PV.

     Select
            Select indicates that a required positional parameter can be omitted
            if the --select option is used.  No arg appears in this position.

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

Red Hat, Inc.                  LVM TOOLS #VERSION#                   VGCHANGE(8)
```
