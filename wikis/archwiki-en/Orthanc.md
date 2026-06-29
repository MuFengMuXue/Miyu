# Orthanc

Orthanc is a lightweight open-source standalone DICOM server which can be extended via its RESTful API and plugin mechanism allowing new modules to be developed. Orthanc is built on top of . A Web viewer, a PostgreSQL database back-end, a MySQL database back-end, and a reference implementation of DICOMweb are currently freely available as plugins. == Installation ==

Install the  package.

The latter will require  which is a collection of libraries and applications implementing large parts the DICOM standard.

Each time the lib  is updated, you will have to rebuild , otherwise  will complain.

To launch Orthanc, simply start/enable .

* The DICOM files you upload to the Orthanc application are stored in .
* The JSON server configuration file is stored as .

## Plugins
Orthanc is provided with a bunch of [https://book.orthanc-server.com/plugins.html plugins, whose some of the official ones are packaged for Arch Linux as well.

## Web viewer
This official plugin extends Orthanc with a Web viewer of medical images.Install

Add the path to the lib in the  node of the JSON server configuration

Restart the  for the changes to take effect.

## DICOMweb
This official plugin extends Orthanc with support of the DICOMweb protocols. More precisely, the plugin introduces a basic, reference implementation of WADO-URI, WADO-RS, QIDO-RS and STOW-RS, following DICOM PS3.18. The plugin simultaneously turns Orthanc into a DICOMweb server and into a DICOMweb client.[https://book.orthanc-server.com/plugins/dicomweb.html

Install

Add the path to the lib in the  node of the JSON server configuration

Restart the  for the changes to take effect.
