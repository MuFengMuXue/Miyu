# Karma

Karma is an alert dashboard for Alertmanager. It allows the aggregation and deduplication of alerts, as well as the possibility of silencing alerts.

## Installation
Install the  or  package.

## Configuration
Karma configuration is done by editing  and starting .

## Changing alertmanager protocol, address and port
The default configuration assumes that alertmanager runs on .
Change the  parameter to match your configuration.

## Changing listening address and port
You may want to change the default address and port on which karma listens. To do so, edit  and add the following parameters:

## Starting karma
After starting and enabling , the application can be reached via HTTP on  by default.
