# Patching packages

This article covers how to create and how to apply patches to packages in the Arch build system (ABS).

A patch describes a set of line changes for one or multiple files. Patches are typically used to automate the changing of source code.

## Creating patches
The diff tool compares files line by line. If you save its output you have a patch, e.g.  (which can be shortened to ). If you pass directories diff will compare the files they contain.

# Delete the  directory if you have already built the package.
# Run / which will download and extract the source files, specified in , but not build them. If the system you are making the patch on does not have the required dependencies, you may have to run / instead.
# Create two copies of the extracted directory in the  directory, one as a pristine copy and one for your altered version. We will call them  and .
# Make your changes in the  directory.
# Run  and check if the patch looks good.
# Run  to create the patch.
# Change into the initial  directory from which you made copies and apply the patch using  (which can be shortened to ). Verify that the patch is working by building and installing the modified package with /.

See  and  for more info.

## Applying patches
This section outlines how to apply patches you created or downloaded from the Internet from within a 's  function. Follow these steps:

# Add an entry to the  array of the  for the patch file, separated from the original source url by a space. If the file is available online, you can provide the full URL and it will automatically be downloaded and placed in the  directory. If it is a patch you created yourself, or is otherwise not available, you should place the patch file in the same directory as the  file, and just add the name of the file to the source array so that it is copied into the  directory. If you redistribute the , you should, of course, include the patch with the .
# Then use  or  (from ) to update the  array. Or manually add an entry to the  array; you can generate the sum of your patch using sha512sum tool.
# Create the  function in the  if one is not already present.
# The first step is to change into the directory that needs to be patched (in the  function, not on your terminal! You want to automate the process of applying the patch).  You can do this with something like .  is often the name of a directory created by untarring a downloaded source file, but not in all cases.
# Now you simply need to apply the patch from within this directory. This is very simply done by adding  to your  function, changing  to the name of the file containing the diff (the file that was automatically copied into your  directory because it was in the  array of the  file).

An example prepare-function:

{{hc|PKGBUILD|
prepare() {
    cd $pkgname-$pkgver
    patch -Np1 -i ../eject.patch
}
}}

Alternatively, you can use the / flag of  without having to cd first. The example above would then become:

{{hc|PKGBUILD|
prepare() {
    patch -d $pkgname-$pkgver -Np1 -i ../eject.patch
}
}}

Run  from the terminal now. If all goes well, the patch will be automatically applied, and your new package will contain whatever changes were included in the patch. If not, you may have to experiment with the / option of patch. While experimenting, you might find ,  or  options usable. Read  for more information.

Basically it works as follows. If the diff file was created to apply patches to files in , the diff files will be applied to . You are running it from within the  directory (because you would cd into that directory in the ), so when patch applies the file, you want it to apply it to the file , taking off the  part.  does this, by removing one directory from the path. However, if the developer patched in , you need to remove two directories, so you use .

If you do not apply a  option, it will take off all directory structure. This is OK if all the files are in the base directory, but if the patch was created on  and one of the edited files was , and you run the patch without a  option from within , it will try to patch a file named .

Most developers create patches from the parent directory of the directory that is being patched, so  will usually be right.

## Using quilt
A simpler way to create patches is using  which provides better support for managing many patches, such as applying patches, refreshing patches, and reverting patched files to original state.  is used on Debian to manage their patches. See Using Quilt for basic information about basic quilt usage to generate, apply patches, and reverting patched files.
