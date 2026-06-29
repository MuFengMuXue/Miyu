# PHP/pthreads extension

If you wish to have POSIX multi-threading you will need the pthreads extension (or the parallel extension for PHP 7.4+). To install the pthreads or parallel extension using  you are required to use a compiled version of PHP with the thread safety support flag  for PHP 8, or  for PHP 7.

Check what packages depend on the  package, for example:

Uninstall all those including php.

Use the ABS to acquire the build files for each of them, modify the  in their folder to add , next to the other extensions. It should look like:

Make the new packages with makepkg, then install the rebuild version of the packages you had previously removed:

On some versions of PHP,  is missing and it is needed to run . As adding  in the file above does not solve it, you will need to install it separately.

Then install pthreads:

 $ pecl install pthreads

or install parallel for recent PHP versions:

 $ pecl install parallel

If you installed parallel, you will need to edit  and add the  extension, it should look like:

Install the  package for APC support back.
