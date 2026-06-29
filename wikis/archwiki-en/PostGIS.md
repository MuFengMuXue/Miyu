# PostGIS

PostGIS adds support for geographic objects in the PostgreSQL database. This document describes the process for installing PostGIS and creating a template PostGIS database. It is assumed that PostgreSQL has been installed. If it has not, please refer to the PostgreSQL page.

## Installing PostGIS
Install the  package.

## Installing PostGIS Extension
Since PostgreSQL 9.1, the preferred approach is to install PostGIS and enable postgis extension for each spatial database.

You do not need to do the below "Creating a Template PostGIS Database" step if you use PostGIS extension.

* upgrade postgis extension

* migrate spatial database created with postgis_template
Dump and drop the spatial database, re-create a spatial database with extension, and restore the dumped database.  Follow https://www.postgis.net/docs/postgis_installation.html#hard_upgrade for specific commands.

## Creating a Template PostGIS Database
* Become the postgres user.
 # su - postgres
* If you have not created a superuser for accessing PostgreSQL, you may want do that now. You will be prompted for granting permissions to that user.
 $ createuser * Create a new database called "template_postgis".
 $ createdb -O [username template_postgis -E UTF-8
* Load the PostGIS spatial types for PostgreSQL and spatial reference systems. "postgis.sql" and "spatial_ref_sys.sql" are part of the installation of PostGIS, and may reside somewhere else besides "/usr/sharepostgresql/contrib/postgis-2.1/" depending on the installation. (Below is for default postgis 2.1 installation)
 $ psql -d template_postgis -f /usr/share/postgresql/contrib/postgis-2.1/postgis.sql
 $ psql -d template_postgis -f /usr/share/postgresql/contrib/postgis-2.1/spatial_ref_sys.sql
* Make it a real template.

## Creating a PostGIS Database From the Template
It is common practice to reserve a bare template for creating new PostGIS databases. As a PostgreSQL superuser, the following command will create a new database:
 $ createdb -T template_postgis == Upgrading PostgreSQL with PostGIS ==
If you want to upgrade PostgreSQL using  with , you can install  before upgrade.

## More Resources
For additional resources concerning PostGIS, check out the [https://postgis.net/documentation/ PostGIS Documentation.

## PostGIS failing with json_tokener_error
This happends when adding postgis as an extension.  The libjson-c package has changed, and PostGIS has not put out a stable release with this yet.  It is in 2.1.0rc1, though.  The bug-report is https://trac.osgeo.org/postgis/ticket/2213

The fix is to download the postgis PKGBUILD and then change the version to '2.1.0rc1'.  Do not forget to change the sha256sum.
