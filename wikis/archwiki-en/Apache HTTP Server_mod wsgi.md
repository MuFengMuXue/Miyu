# Apache HTTP Server/mod wsgi

According to the project's site:
:The aim of mod_wsgi is to implement a simple to use Apache module which can host any Python application which supports the Python WSGI interface. The module would be suitable for use in hosting high performance production web sites, as well as your average self managed personal sites running on web hosting services.

mod_wsgi is an Apache HTTP Server module that embeds a Python application within the server and allow them to communicate through the Python WSGI interface as defined in the Python PEP 333. WSGI is one of the Python ways to produce high quality and high performance web applications.

WSGI provide a standard way to interface different web-apps without hassle. Several well-known python applications or frameworks provide wsgi for easy deployment and embedding. It means that you can embed your Django-powered blog and your project's Trac into a single Pylons application that wraps around them to deals with, say, authentication without modifying the formers.

Example:
* Pylons
* Django
* Turbo-gear
* Trac
* Moin-moin
* Zope

## Installation
Install  which provides the module working with all common versions of Python (3.x).

## Apache configuration
As indicated during installation, add the following line to the configuration file of Apache:

Restart .

Check that Apache is running properly. If the previous command returned nothing, it means that the launch of Apache went well. Otherwise, you can see errors with the  unit status.

## Module test
Add this line in Apache configuration file:

Create a test file:

Restart

You can check the proper functioning by going to the following address : http://localhost/wsgi_app
