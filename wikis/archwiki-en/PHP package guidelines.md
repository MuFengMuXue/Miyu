# PHP package guidelines

This document covers the creation of PKGBUILDs for PHP libraries. The target audience of this document is intended to be packagers of PHP libraries. For PHP Web applications, see Web application package guidelines

## Package names
For modules the package name should begin with  and the rest of the name should be constructed from the library name by converting it to lowercase and separate words with hyphens. For example the package name corresponding to  will be .

## Package file placement
PHP packages should install files into . This path should be in the   or  directive in order to be able to include libraries files in PHP web applications.

## Architecture
In most cases, the  array should contain  because most PHP packages are architecture independent.
