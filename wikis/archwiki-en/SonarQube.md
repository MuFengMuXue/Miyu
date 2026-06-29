# SonarQube

SonarQube is code quality tool for better code and published under the LGPL3 license.

## Installation
Install the  package.

SonarQube uses H2 database by default (not recommended).
Or requires the use of a database backend, the following are supported:

* PostgreSQL
* Oracle
* MSSQL

## Configuration
The user configuration file is located at .

See the SonarQube docs for more configuration examples.

## PostgreSQL
Install and configure PostgreSQL.

SonarQube seems to support only TCP Socket

## With TCP socket
Connect do postgresql:

 psql

Create the new user while connecting to the server as  user (you will be prompted for a password for the new user):

 postgres=# CREATE USER sonarqube WITH PASSWORD password;

Create the  database, owned by  user:

 postgres=# CREATE DATABASE sonarqube OWNER sonarqube;
 postgres=#GRANT ALL PRIVILEGES ON DATABASE sonarqube TO sonarqube;

PostgreSQL#Configure PostgreSQL to be accessible from remote hosts

Verify it works:

 $ psql --host=ip_address --dbname=sonarqube --username=sonarqube --password

Configure SonarQube through the update :

## Upgrade
After upgrading SonarQube, follow these steps:

* Update the  file to match the new version.
* Once SonarQube is running, a page will appear prompting you to upgrade. For detailed instructions, visit the [https://docs.sonarsource.com/sonarqube/latest/setup-and-upgrade/upgrade-the-server/upgrade/ upgrade guide.
* Navigate to the setup page of your SonarQube server at  and click the upgrade button.
* Once the upgrade process is complete, the normal login page will be displayed.

## Usage
Start/enable , the webinterface should listen on .

Default credentials are .

## Usage with maven
 $ mvn clean verify sonar:sonar -Dsonar.projectKey=project key -Dsonar.projectName=project -Dsonar.host.url=http://localhost:9000 -Dsonar.token=token

## Usage with sonar-scanner
There is a package . Usage is:

 $ /opt/sonar-scanner/bin/sonar-scanner -Dsonar.projectKey=project key -Dsonar.sources=. -Dsonar.host.url=http://localhost:9000 -Dsonar.token=token

## Troubleshooting
You can check the unit status or the journal.

And there are sonarqube logs in:

 # /var/log/sonarqube/

If sonarqube is not active, one of these logs will contain an error.
