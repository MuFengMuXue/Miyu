# Grafana

Grafana is an open-source, general purpose dashboard and graph composer, which runs as a web application. It supports graphite, InfluxDB, Prometheus or opentsdb as backends.

## Installation
Install the  package.

After that you can enable and start  and access the application on localhost, e.g.: http://127.0.0.1:3000 . The default username is  and password  to access the web frontend.

## Configuration
The default location of the configuration file is .

After making changes, remember to restart .

## Example usage
## InfluxDB
## Installation
Follow the instructions to install InfluxDB.

## Aggregate data
In case of scaleable server monitoring in combination with Grafana and InfluxDB, one could choose software like . More generally any measurement data can be aggregated with InfluxDB and displayed with Grafana. There are modules and libraries for several programming languages to interact with InfluxDB and one could even store data with a simple http post command using the program .

Herefore, create a database named :

 $ curl -G http://localhost:8086/query --data-urlencode "q=CREATE DATABASE example"

Post data into the  database:

 $ curl -i -XPOST 'http://localhost:8086/write?db=example' --data-binary 'cpu_load_short,host=server01,region=us-west value=0.64 1434055562000000000'

## Add a data source
* Click on Data sources in the left menu and then on Add new.
* Name can be something like  and the type should be set to . In this example, the URL for the HTTP settings is . Database name corresponds to the one earlier chosen, e.g. . If not changed, username and password are .
* Click on Test connection to see everything is working and then on Save.

## Creating a dashboard
* Click Home in the left-upper corner and then on New.
* Hover over and click the little green box on the left side, and then choose: Add panel and Graph.
* Click on the title of the new graph and select Edit.
* In the graph settings in Metrics choose  as data source in the lower-right corner.
* Create a query by selecting your aggregated data. Click on select measurement which is located beside FROM. In the drop-down menu should appear a list of "tables" in your database, e.g. the table named . If no suggestions comes up, your connection to InfluxDB might be broken or no data has been aggregated yet.
* Beside the bold text SELECT click on value and choose for example the measurement data .
* To save changes, click Back to dashboard, then the floppy disc icon.
