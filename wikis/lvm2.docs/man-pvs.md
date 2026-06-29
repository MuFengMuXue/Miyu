# Man / Pvs

```text
PVS(8)                       System Manager's Manual                      PVS(8)

NAME
     pvs —— Display information about physical volumes

SYNOPSIS
     pvs    [ option_args ]
            [ position_args ]

DESCRIPTION
     pvs produces formatted output about PVs.

USAGE
     pvs
            [ -a|--all ]
            [ -A|--allpvs ]
            [ -o|--options String ]
            [ -O|--sort String ]
            [ -S|--select String ]
            [ --aligned ]
            [ --binary ]
            [ --configreport log|vg|lv|pv|pvseg|seg ]
            [ --foreign ]
            [ --headings none|abbrev|full|0|1|2 ]
            [ --ignorelockingfailure ]
            [ --logonly ]
            [ --nameprefixes ]
            [ --noheadings ]
            [ --nosuffix ]
            [ --readonly ]
            [ --reportformat basic|json|json_std ]
            [ --rows ]
            [ --segments ]
            [ --separator String ]
            [ --shared ]
            [ --unbuffered ]
            [ --units [Number]r|R|h|H|b|B|s|S|k|K|m|M|g|G|t|T|p|P|e|E ]
            [ --unquoted ]
            [ COMMON_OPTIONS ]
            [ PV|Tag ... ]

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
     --aligned
            Use with --separator to align the output columns.

     -a|--all
            Show  information  about  devices  that have not been initialized by
            LVM, i.e. they are not PVs.

     -A|--allpvs
            Show information about PVs outside the devices file.   Combine  with
            -a|--all to include devices that are not PVs.

     --binary
            Use  binary  values "0" or "1" instead of descriptive literal values
            for columns that have exactly two valid values to report (not count‐
            ing the "unknown" value which denotes that the value  could  not  be
            determined).

     --commandprofile String
            The   command   profile  to  use  for  command  configuration.   See
            lvm.conf(5) for more information about profiles.

     --config String
            Config settings for the command.  These  override  lvm.conf(5)  set‐
            tings.   The  String arg uses the same format as lvm.conf(5), or may
            use section/field syntax.   See  lvm.conf(5)  for  more  information
            about config.

     --configreport log|vg|lv|pv|pvseg|seg
            See lvmreport(7).

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

     --foreign
            Report/display  foreign  VGs  that  would otherwise be skipped.  See
            lvmsystemid(7) for more information about foreign VGs.

     --headings none|abbrev|full|0|1|2
            Type of headings to use in report output.  none or 0:  No  headings.
            abbrev  or  1:  Column  name  abbreviations.  full or 2: Full column
            names.

     -h|--help
            Display help text.

     --ignorelockingfailure
            Allows a command to continue with read-only metadata operations  af‐
            ter locking failures.

     --journal String
            Record  information  in the systemd journal.  This information is in
            addition to information enabled by the lvm.conf log/journal setting.
            command: record information about the command.  output:  record  the
            default command output.  debug: record full command debugging.

     --lockopt String
            Used to pass options for special cases to lvmlockd.  See lvmlockd(8)
            for more information.

     --logonly
            Suppress command report and display only log report.

     --longhelp
            Display long help text.

     --nameprefixes
            Add an "LVM2_" prefix plus the field name to the output. Useful with
            --noheadings to produce a list of field=value pairs that can be used
            to set environment variables (for example, in udev rules).

     --noheadings
            Suppress  the  headings line that is normally the first line of out‐
            put.  Useful if grepping the output.

     --nohints
            Do not use the hints file to locate devices for PVs. A  command  may
            read  more  devices to find PVs when hints are not used. The command
            will still perform standard hint file invalidation  where  appropri‐
            ate.

     --nolocking
            Disable  locking.  Use with caution, concurrent commands may produce
            incorrect results.

     --nosuffix
            Suppress the suffix on output sizes. Use with --units (except h  and
            H) if processing the output.

     -o|--options String
            Comma-separated,  ordered  list  of  fields  to  display in columns.
            String arg syntax is: [+|-|#]Field1[,Field2 ...]  The prefix +  will
            append the specified fields to the default fields, - will remove the
            specified  fields from the default fields, and # will compact speci‐
            fied fields (removing them when empty for all rows.)  Use -o help to
            view the list of all available fields.  Use separate lists of fields
            to  add,  remove  or   compact   by   repeating   the   -o   option:
            -o+field1,field2 -o-field3,field4 -o#field5.  These lists are evalu‐
            ated  from  left  to  right.   Use  field name lv_all to view all LV
            fields, vg_all all VG fields, pv_all all PV fields, seg_all  all  LV
            segment  fields,  and  pvseg_all  all  PV  segment  fields.  See the
            lvm.conf(5) report section for  more  config  options.   See  lvmre‐
            port(7) for more information about reporting.

     --profile String
            An alias for --commandprofile or --metadataprofile, depending on the
            command.

     -q|--quiet ...
            Suppress  output  and log messages. Overrides --debug and --verbose.
            Repeat once to also suppress any prompts with answer 'no'.

     --readonly
            Prevent the command from making changes,  including  activation  and
            metadata updates.  (See --permission r for read only LVs.)

     --reportformat basic|json|json_std
            Overrides  current  output format for reports which is defined glob‐
            ally by the report/output_format setting in lvm.conf(5).   basic  is
            the  original  format  with columns and rows.  If there is more than
            one report per command, each report is prefixed with the report name
            for identification. json produces  report  output  in  JSON  format.
            json_std produces report output in JSON format which is more compli‐
            ant with JSON standard.  See lvmreport(7) for more information.

     --rows
            Output columns as rows.

     --segments
            Produces  one line of output for each contiguous allocation of space
            on each PV, showing the start (pvseg_start) and length  (pvseg_size)
            in units of physical extents.

     -S|--select String
            Select  objects for processing and reporting based on specified cri‐
            teria.  The criteria syntax is described by --select help and lvmre‐
            port(7).  For reporting commands, one row is displayed for each  ob‐
            ject  matching  the criteria.  See --options help for selectable ob‐
            ject fields.  Rows can be displayed with  an  additional  "selected"
            field (-o selected) showing 1 if the row matches the selection and 0
            otherwise.   For  non-reporting commands which process LVM entities,
            the selection is used to choose items to process.

     --separator String
            String to use to separate each column. Useful if grepping  the  out‐
            put.

     --shared
            Report/display  shared VGs that would otherwise be skipped when lvm‐
            lockd is not being used on the host.  See lvmlockd(8) for  more  in‐
            formation about shared VGs.

     -O|--sort String
            Comma-separated ordered list of columns to sort by. Replaces the de‐
            fault  selection.  Precede  any  column with - for a reverse sort on
            that column.

     -t|--test
            Run in test mode. Commands will not update metadata.  This is imple‐
            mented by disabling all metadata writing but nevertheless  returning
            success to the calling function. This may lead to unusual error mes‐
            sages  in  multi-stage  operations  if a tool relies on reading back
            metadata it believes has changed but hasn't.

     --unbuffered
            Produce output immediately without sorting or aligning  the  columns
            properly.

     --units [Number]r|R|h|H|b|B|s|S|k|K|m|M|g|G|t|T|p|P|e|E
            All  sizes  are  output  in  these  units: human-(r)eadable with '<'
            rounding   indicator,    (h)uman-readable,    (b)ytes,    (s)ectors,
            (k)ilobytes,  (m)egabytes,  (g)igabytes,  (t)erabytes,  (p)etabytes,
            (e)xabytes.  Capitalise to use multiples of 1000 (S.I.)  instead  of
            1024.  Custom units can be specified, e.g. --units 3M.

     --unquoted
            When  used  with  --nameprefixes,  output  values in the field=value
            pairs are not quoted.

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

     Tag    Tag name.  See lvm(8) for information about tag names and using tags
            in place of a VG, LV or PV.

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

Red Hat, Inc.                  LVM TOOLS #VERSION#                        PVS(8)
```
