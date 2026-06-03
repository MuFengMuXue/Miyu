## Name

systemd-report — Generate report of system facts and metrics

## Synopsis

`systemd-report` \[OPTIONS...\]

## Description

*Note: this command is experimental for now. While it is likely to become a regular component of systemd, it might still change in behaviour and interface.*

**systemd-report** requests facts and metrics from the system and writes them to standard output.

## Commands

The following commands are understood:

**metrics** \[MATCH...\]  
Acquire a list of metrics values from all local services providing them, and write them to standard output. Optionally takes one or more match expressions for filtering the metrics to show. The expression either may be a literal metric family name to search for, or a prefix of one (which will be matched only at dot boundaries). If multiple matches are specified as multiple parameters, any metric matching *any* of the specified matches are shown.

Added in version 260.

**describe-metrics** \[MATCH...\]  
Acquire a list of metric families from all local services providing them, and write them to standard output. This returns primarily static information about metrics, their data types and human readable description, without values.

Match expressions similar to those supported by **metrics** are supported for **describe-metrics**, too.

Added in version 260.

**list-sources**  
Show list of known metrics sources.

Added in version 260.

## Options

The following options are understood:

`--system`, `--user`  
Query per-system metrics sources (the default), or the per-user metrics sources.

Added in version 260.

`--no-pager`  
Do not pipe output into a pager.

`--json=`*`MODE`*  
Shows output formatted as JSON. Expects one of "`short`" (for the shortest possible output without any redundant whitespace or line breaks), "`pretty`" (for a pretty version of the same, with indentation and line breaks) or "`off`" (to turn off JSON output, the default).

`-j`  
Equivalent to `--json=pretty` if running on a terminal, and `--json=short` otherwise.

`--no-legend`  
Do not print the legend, i.e. column headers and the footer with hints.

`-h`, `--help`  
Print a short help text and exit.

`--version`  
Print a short version string and exit.

## Exit status

On success, 0 is returned, a non-zero failure code otherwise.

## See Also

systemd(1)
