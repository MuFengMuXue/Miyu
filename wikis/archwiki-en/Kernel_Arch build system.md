# Kernel/Arch build system

The Arch build system can be used to build a custom kernel based on the official  package. This compilation method can automate the entire process, and is based on a very well tested package. You can edit the PKGBUILD to use a custom kernel configuration or add additional patches.

## Getting the ingredients
Since you will be using makepkg, follow the best practices outlined there first. For example, you cannot run makepkg as the root user. Therefore, create a  directory in your user home first.

 $ mkdir ~/build/
 $ cd ~/build/

Install the  and  package.

You need a clean kernel to start your customization from. Retrieve PKGBUILD source and few other files into your build directory by running:

 $ pkgctl repo clone --protocol=https linux

At this point, the directory tree looks like (there may be a few other files):

Then, get any other file you need (e.g. custom configuration files, patches, etc.) from the respective sources.

## Modifying the PKGBUILD
Edit  and look for the  parameter. Change this to your custom package name, e.g.:

## Avoid creating the doc
A large portion of the lengthy compiling effort is devoted to creating the documentation. To avoid creating the documents:
# Remove  in
# Remove  in

## Changing prepare()
In  function, you can apply needed kernel patches or change kernel build configuration. Since 2018-08-01, the PKGBUILD automatically applies all  files in source.

If you need to change a few configuration options you can edit  in the source.

Or you can use a GUI tool to tweak the options. Comment  in the prepare() function of the PKGBUILD, and add your favorite tool (run  to list all of the possible configuration targets):

## Generate new checksums
#Changing prepare() suggests a possible modification to . Since this path is not where downloading the package files ended, its checksum was not checked by makepkg (which actually checked ).

If you replaced the downloaded  with another one before running makepkg, install the  package and generate new checksums by running:

 $ updpkgsums

## Compiling
You can now proceed to compile your kernel by the usual command .

If you have chosen an interactive program for configuring the kernel parameters (like menuconfig), you need to be there during the compilation.

 $ makepkg -s

The  parameter will download any additional dependencies used by recent kernels such as xml and docs.

## Installing
The compile step will leave two packages in the  folder, one for the kernel and one for the kernel headers. They might have names like:

 linux-custom-5.8.12-x86_64.pkg.tar.zst
 linux-custom-headers-5.8.12-x86_64.pkg.tar.zst

Best practice is to install both packages together as they might be both needed (e.g. DKMS):

 # pacman -U linux-custom-headers-5.8.12-x86_64.pkg.tar.zst linux-custom-5.8.12-x86_64.pkg.tar.zst

(substitute the actual names of the files you have in the folder)

## Boot loader
If you have modified  in order to have your new kernel installed alongside the default kernel you will need to update your boot loader configuration file and add new entries ('default' and 'fallback') for your custom kernel and the associated initramfs images.

## Updating
Assuming one has an arch kernel source that they want to update, one method to do that is with https://github.com/archlinux/linux. In what follows, the top kernel source directory is assumed at .

In general, arch sets an arch kernel source with two local git repositories. The one at  is a local bare git repository pointing to . The other one is at , pulling from the bare repository. Possible local patches, and building, are expected at .

For this example, the HEAD of the locally installed bare git repository source at  was initially pointing to

which is somewhere between v5.2.5-arch1 and v5.2.6-arch1.

 $ git fetch --verbose

One can see it fetched v5.2.7-arch1, which was the newest archlinux tag, because it prints what new tags were obtained. If no new tags were obtained then there is no newer archlinux source available.

Now the source can be updated where the actual build will take place.

 $ cd ~/build/linux/src/archlinux-linux/
 $ git checkout master
 $ git pull
 $ git fetch --tags --verbose
 $ git branch --verbose 5.2.7-arch1 v5.2.7-arch1
 $ git checkout 5.2.7-arch1

You can verify you are on track with something like

This shows few specific archlinux patches between  and .

The up to date PKGBUILD, as well archlinux kernel configuration file, can be pulled in using  in the package directory:

 $ cd ~/build/linux/
 $ git pull

Now you should merge files located in  into . Merging can also done manually, or with specific utilities. Review #Changing prepare(), and run manually most, if not all, the shell commands of PKGBUILD::prepare().

At this point,  should succeed. While #Compiling, make sure to also add  option to the  command, since it should be able to build the packages as if the source was extracted by . And you are back to #Installing.

## Cleanup
One will probably want to remove  after merging. In addition,  will accumulate branches in the form of  if more recent updates are done in this fashion. These can be deleted with

 $ cd ~/build/linux/src/archlinux
 $ git branch --delete --force --verbose 5.2.7-arch1
