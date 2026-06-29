# Man / Vgcreate

```text
VGCREATE(8)                  System Manager's Manual                 VGCREATE(8)

NAME
     vgcreate —— Create a volume group

SYNOPSIS
     vgcreate position_args
            [ option_args ]

DESCRIPTION
     vgcreate  creates a new VG on block devices. If the devices were not previ‐
     ously initialized as PVs with pvcreate(8), vgcreate will  initialize  them,
     making  them  PVs.  The  pvcreate options for initializing devices are also
     available with vgcreate.

     When vgcreate uses an existing PV, that PV's existing values  for  metadata
     size,  PE  start, etc., are used, even if different values are specified in
     the vgcreate command.  To change these values, first use  pvremove  on  the
     device.

USAGE
     vgcreate VG_new PV ...
            [ -A|--autobackup y|n ]
            [ -c|--clustered y|n ]
            [ -f|--force ... ]
            [ -l|--maxlogicalvolumes Number ]
            [ -M|--metadatatype lvm2 ]
            [ -p|--maxphysicalvolumes Number ]
            [ -s|--physicalextentsize Size[m|UNIT] ]
            [ -Z|--zero y|n ]
            [ --addtag Tag ]
            [ --alloc contiguous|cling|cling_by_tags|normal|anywhere|inherit ]
            [ --dataalignment Size[k|UNIT] ]
            [ --dataalignmentoffset Size[k|UNIT] ]
            [ --labelsector Number ]
            [ --locktype sanlock|dlm|none ]
            [ --metadataprofile String ]
            [ --metadatasize Size[m|UNIT] ]
            [ --persist start ]
            [ --pvmetadatacopies 0|1|2 ]
            [ --reportformat basic|json|json_std ]
            [ --setautoactivation y|n ]
            [ --setlockargs String ]
            [ --setpersist String ]
            [ --shared ]
            [ --systemid String ]
            [ --[vg]metadatacopies all|unmanaged|Number ]
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
     --addtag Tag
            Adds  a  tag  to  a PV, VG or LV. This option can be repeated to add
            multiple tags at once. See lvm(8) for information about tags.

     --alloc contiguous|cling|cling_by_tags|normal|anywhere|inherit
            Determines the allocation policy when a command  needs  to  allocate
            Physical Extents (PEs) from the VG. Each VG and LV has an allocation
            policy which can be changed with vgchange/lvchange, or overridden on
            the  command  line.   normal  applies common sense rules such as not
            placing parallel stripes on the same PV.   inherit  applies  the  VG
            policy  to an LV.  contiguous requires new PEs to be placed adjacent
            to existing PEs.  cling places new PEs on the same  PV  as  existing
            PEs  in  the same stripe of the LV.  If there are sufficient PEs for
            an allocation, but normal does not use them, anywhere will use  them
            even  if  it reduces performance, e.g. by placing two stripes on the
            same PV.  Optional positional PV args on the command line  can  also
            be used to limit which PVs the command will use for allocation.  See
            lvm(8) for more information about allocation.

     -A|--autobackup y|n
            Specifies  if  metadata  should  be  backed up automatically after a
            change.  Enabling this is strongly advised!  See vgcfgbackup(8)  for
            more information.

     -c|--clustered y|n
            This option was specific to clvm and is now replaced by the --shared
            option with lvmlockd(8).

     --commandprofile String
            The   command   profile  to  use  for  command  configuration.   See
            lvm.conf(5) for more information about profiles.

     --config String
            Config settings for the command.  These  override  lvm.conf(5)  set‐
            tings.   The  String arg uses the same format as lvm.conf(5), or may
            use section/field syntax.   See  lvm.conf(5)  for  more  information
            about config.

     --dataalignment Size[k|UNIT]
            Align  the  start  of a PV data area with a multiple of this number.
            To see the location of the first Physical Extent (PE) of an existing
            PV, use pvs -o +pe_start. In addition,  it  may  be  shifted  by  an
            alignment offset, see --dataalignmentoffset.  Also specify an appro‐
            priate PE size when creating a VG.

     --dataalignmentoffset Size[k|UNIT]
            Shift the start of the PV data area by this additional offset.

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

     --labelsector Number
            By default the PV is labelled with an LVM2 identifier in its  second
            sector  (sector  1).  This  lets you use a different sector near the
            start of the disk (between 0 and 3 inclusive -  see  LABEL_SCAN_SEC‐
            TORS in the source). Use with care.

     --lockopt String
            Used to pass options for special cases to lvmlockd.  See lvmlockd(8)
            for more information.

     --locktype sanlock|dlm|none
            Specify  the  VG lock type directly in place of using --shared.  See
            lvmlockd(8) for more information.

     --longhelp
            Display long help text.

     -l|--maxlogicalvolumes Number
            Sets the maximum number of LVs allowed in a VG.

     -p|--maxphysicalvolumes Number
            Sets the maximum number of PVs that can belong to the VG.  The value
            0 removes any limitation.  For large numbers of PVs,  also  see  op‐
            tions  --pvmetadatacopies, and --vgmetadatacopies for improving per‐
            formance.

     --metadataprofile String
            The  metadata  profile  to  use  for  command  configuration.    See
            lvm.conf(5) for more information about profiles.

     --metadatasize Size[m|UNIT]
            The approximate amount of space used for each VG metadata area.  The
            size may be rounded.

     -M|--metadatatype lvm2
            Specifies  the type of on-disk metadata to use.  lvm2 (or just 2) is
            the current, standard format.  lvm1 (or just 1) is no longer used.

     --nohints
            Do not use the hints file to locate devices for PVs. A  command  may
            read  more  devices to find PVs when hints are not used. The command
            will still perform standard hint file invalidation  where  appropri‐
            ate.

     --nolocking
            Disable  locking.  Use with caution, concurrent commands may produce
            incorrect results.

     --persist String
            Persistent Reservation operation.  start: register local key and ac‐
            quire reservation.  stop: unregister local key,  releasing  reserva‐
            tion.   remove: preempt and abort another key.  clear: remove reser‐
            vation and keys.  check: check if started.  autostart: start if  the
            VG  autostart  flag is set.  lvmlocal.conf pr_key or host_id must be
            configured to use PR.  For local VGs, Write Exclusive (WE) is  used,
            and  for shared VGs Write Exclusive, all registrants (WEAR) is used.
            Use --setpersist to automate and/or require PR.

     -s|--physicalextentsize Size[m|UNIT]
            Sets the physical extent size of PVs in the VG.  The value  must  be
            either  a  power of 2 of at least 1 sector (where the sector size is
            the largest sector size of the PVs currently used in the VG), or  at
            least  128  KiB.   Once  this value has been set, it is difficult to
            change without recreating the VG, unless no extents need moving.

     --profile String
            An alias for --commandprofile or --metadataprofile, depending on the
            command.

     --pvmetadatacopies 0|1|2
            The number of metadata areas to set aside on a  PV  for  storing  VG
            metadata.   When  2,  one  copy  of the VG metadata is stored at the
            front of the PV and a second copy is stored at the end.  When 1, one
            copy of the VG metadata is stored at the front of the PV.   When  0,
            no  copies  of the VG metadata are stored on the given PV.  This may
            be useful in VGs containing many PVs (this places limitations on the
            ability to use vgsplit later.)

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
            Set flags to control persistent reservation behavior.   y:  set  re‐
            quire and autostart flags.  require: PR will be required to write or
            activate  VG.   autostart:  PR will be automatically started.  ptpl:
            use persist through power loss on devices.  When  autostart  is  en‐
            abled,  autoactivation  and auto-lockstart commands will first start
            PR.  lvmlocal.conf pr_key or host_id must be configured to  use  PR.
            For local VGs, enabling system_id is also recommended.

     --shared
            Create a shared VG using lvmlockd if LVM is compiled with lockd sup‐
            port.   lvmlockd  will  select lock type sanlock or dlm depending on
            which lock manager is running. This allows multiple hosts to share a
            VG on shared devices. lvmlockd and a lock manager must be configured
            and running.  See lvmlockd(8) for more information about shared VGs.

     --systemid String
            Specifies the system ID that will be given to the new VG, overriding
            the system ID of the host running the command. A VG is normally cre‐
            ated without this option, in which case the new VG is given the sys‐
            tem ID of the host creating it. Using this option  requires  caution
            because  the  system ID of the new VG may not match the system ID of
            the host running the command, leaving the  VG  inaccessible  to  the
            host.  See lvmsystemid(7) for more information.

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

     --[vg]metadatacopies all|unmanaged|Number
            Number of copies of the VG metadata that are kept.  VG  metadata  is
            kept  in  VG metadata areas on PVs in the VG, i.e. reserved space at
            the start and/or end of the PVs.  Keeping a copy of the VG  metadata
            on  every PV can reduce performance in VGs containing a large number
            of PVs.  When this number is set to a non-zero value, LVM will auto‐
            matically choose PVs on which to store  metadata,  using  the  meta‐
            dataignore flags on PVs to achieve the specified number.  The number
            can  also  be  replaced with special string values: unmanaged causes
            LVM to not automatically manage the PV  metadataignore  flags.   all
            causes  LVM  to first clear the metadataignore flags on all PVs, and
            then to become unmanaged.

     -y|--yes
            Do not prompt for confirmation interactively but always  assume  the
            answer yes. Use with extreme caution.  (For automatic no, see -qq.)

     -Z|--zero y|n
            Controls  if  the  first  4  sectors  (2048 bytes) of the device are
            wiped.  The default is to wipe these sectors unless either  or  both
            of --restorefile or --uuid are specified.

VARIABLES
     VG     Volume Group name.  See lvm(8) for valid names.

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

Red Hat, Inc.                  LVM TOOLS #VERSION#                   VGCREATE(8)
```
