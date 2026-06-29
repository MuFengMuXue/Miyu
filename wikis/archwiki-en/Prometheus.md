# Prometheus

Prometheus is an open-source metrics collection and processing tool. It consists primarily of a timeseries database and a query language to access and process the metrics it stores. Separate services perform metric exposure, from which the Prometheus server can pull. It provides a very minimal web UI out of the box. To get a functional dashboard system, third-party tools like Grafana can be used.

## Installation
Install the  package. After that you can enable and start  and access the application via HTTP on port 9090 by default.

The default configuration monitors the  process itself, but not much beyond that. To perform system monitoring, you can install  which performs metric scraping from the local system. You can start and enable the  service. It will open port 9100 by default. Once the service is running, you will need to configure  to scrape the exporter service periodically in order actually to collect the data. Do this by following the steps to add metrics as shown below.

## Configuration
The Prometheus configuration is done through YAML files, the main one being located at .

## Adding metrics
You can add new places to scrape metrics from by adding them to the  array. To add the local node exporter as a source, next to the prometheus process itself, the configuration would look like this:

  scrape_configs:
    - job_name: 'prometheus'
      static_configs:
        - targets: - job_name: 'node'
      static_configs:
        - targets: ['localhost:9100'

## Exporters
The Arch Linux repository contains a subset of the available exporters:

*  - system metrics
*  - blackbox probing of endpoints over HTTP, HTTPS, DNS, TCP and ICMP
*  - memcached metrics
*  – MySQL server metrics

The exporters are implemented as services. For example to run the node exporter, enable and start .

## Using the UI
Prometheus comes with a very limited web UI to verify configuration, query and graph metrics. You can reach it at http://localhost:9090 by default. You can find an in-depth explanation of Prometheus' query language in the Prometheus documentation.

## Alerting
 can send out custom alerts when certain conditions are met configured in  and what alert to send out is configured in . Alertmanager supports various ways to notify users such as email, slack, and more. To configure email alerts add the following snippet:

For prometheus to send alerts to alertmanager include the following snippet in :

To configure an alert for when a systemd unit fails add the following snippet to . For more rules read the alerting rules documentation.

{{bc|
- name: systemd_unit
  interval: 15s
  rules:
  - alert: systemd_unit_failed
    expr: |
      node_systemd_unit_state{state="failed"} > 0
    for: 3m
    labels:
      severity: critical
    annotations:
      description: 'Instance : Service failed'
      summary: 'Systemd unit failed'
}}

## Tips and tricks
## Telegraf instead of exporters
Telegraf can be used instead of multiple exporters when used with Prometheus Output Plugin. This reduces metrics collection into a single binary and offers more flexible configuration when compared to standard Prometheus exporters.
