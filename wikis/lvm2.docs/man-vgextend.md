# Man / Vgextend

```text
VGEXTEND(8)                  System Manager's Manual                 VGEXTEND(8)

NAME
     vgextend —— Add physical volumes to a volume group

SYNOPSIS
     vgextend position_args
            [ option_args ]

DESCRIPTION
     vgextend  adds  one or more PVs to a VG. This increases the space available
     for LVs in the VG.

     Also, PVs that have gone missing and then returned, e.g. due to a transient
     device failure, can be added back to the VG  without  re-initializing  them
     (see --restoremissing).

     If  the specified PVs have not yet been initialized with pvcreate, vgextend
     will initialize them. In this case  pvcreate  options  can  be  used,  e.g.
     --labelsector,    --metadatasize,   --metadataignore,   --pvmetadatacopies,
     --dataalignment, --dataalignmentoffset.

USAGE
     vgextend VG PV ...
            [ -A|--autobackup y|n ]
            [ -f|--force ... ]
            [ -M|--metadatatype lvm2 ]
            [ -Z|--zero y|n ]
            [ --dataalignment Size[k|UNIT] ]
            [ --dataalignmentoffset Size[k|UNIT] ]
            [ --labelsector Number ]
            [ --metadataignore y|n ]
            [ --metadatasize Size[m|UNIT] ]
            [ --pvmetadatacopies 0|1|2 ]
            [ --reportformat basic|json|json_std ]
            [ --restoremissing ]
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

     --dataalignment Size[k|UNIT]
            Align the start of a PV data area with a multiple  of  this  number.
            To see the location of the first Physical Extent (PE) of an existing
            PV,  use  pvs  -o  +pe_start.  In  addition, it may be shifted by an
            alignment offset, see --dataalignmentoffset.  Also specify an appro‐
            priate PE size when creating a VG.

     --dataalignmentoffset Size[k|UNIT]
            Shift the start of the PV data area by this additional offset.

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

     -f|--force ...
            Override various checks, confirmations and  protections.   Use  with
            extreme caution.

     -h|--help
            Display help text.

     --journal String
            Record  information  in the systemd journal.  This information is in
            addition to information enabled by the lvm.conf log/journal setting.
            command: record information about the command.  output:  record  the
            default command output.  debug: record full command debugging.

     --labelsector Number
            By  default the PV is labelled with an LVM2 identifier in its second
            sector (sector 1). This lets you use a  different  sector  near  the
            start  of  the disk (between 0 and 3 inclusive - see LABEL_SCAN_SEC‐
            TORS in the source). Use with care.

     --lockopt String
            Used to pass options for special cases to lvmlockd.  See lvmlockd(8)
            for more information.

     --longhelp
            Display long help text.

     --metadataignore y|n
            Specifies the metadataignore property of a PV.  If yes, metadata ar‐
            eas on the PV are ignored, and lvm will not store  metadata  in  the
            metadata areas of the PV.  If no, lvm will store metadata on the PV.

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

     --restoremissing
            Add  a PV back into a VG after the PV was missing and then returned,
            e.g. due to a transient failure. The PV is not reinitialized.

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

     -Z|--zero y|n
            Controls if the first 4 sectors  (2048  bytes)  of  the  device  are
            wiped.   The  default is to wipe these sectors unless either or both
            of --restorefile or --uuid are specified.

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

Red Hat, Inc.                  LVM TOOLS #VERSION#                   VGEXTEND(8)
```
