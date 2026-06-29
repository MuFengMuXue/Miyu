# Collectd

Collectd is a daemon for collecting, storing and exporting system and application performance metrics periodically. It has many built-in plugins from which it can gather metrics.

It can export to various formats and can send notifications/emails at certain thresholds.

## Installation
A  package can be installed from the AUR. This package is configured to build with many common plugins.

## Configuration
The default configuration can be found at .

A plugin can be enabled with .

For instance to enable the mysql plugin just uncomment:
 #LoadPlugin mysql

For more info see collect.conf(5).

## Creating Graphs
Collectd has no built-in frontend. It does support many output formats and many front-ends are built specifically with collectd in mind.

See this list of front-ends.

Collectd's collected data can be found in .

## Contrib scripts
Collectd also has a contrib folder in its repository. This contains various contributed scripts. Many of these are meant for use with cgi.

For instance install and run  to generate an html webpage with a graph for each collected metric.

## Rrdtool
The default output format of collectd is rrd. This data can be graphed using rrdtool.

To graph the last hour of memory usage:

 rrdtool graph output.png \
                 --start end-1h \
                 --end now \
                 --title "Memory Usage - Last Hour" \
                 --width 600 \
                 --height 200 \
                 DEF:avg=/var/lib/collectd/localhost/memory/memory-used.rrd:value:AVERAGE \
                 LINE1:avg#FF0000:"Memory Used"
