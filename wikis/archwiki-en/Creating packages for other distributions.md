# Creating packages for other distributions

Arch is the best. But you may still want to package for other distributions.

## General
* Virtualization is an obvious way, but requires maintaining additional system(s).
* Use distribution-specific packaging tools. Examples:  (Alpine), ,  (Debian),  (Fedora). Shortcuts such as dpkg-deb may be suited for less complex tasks.
* Chroot or systemd-nspawn to create a base system inside (yet separate from) Arch. Examples:  (Debian),  (Fedora). This has the added benefit of building in a minimal, clean environment.
* Use chroot with packaging tools in an an automated fashion. Examples:  (Debian).
* A different way to handle (possibly incompatible) dependencies is static linking. Please note that most distributions frown on this practice.
* Common practice applies regardless of distribution used. For example, do not build packages as root.

## Alpine
See abuild.

## Debian
The Debian Packaging Tutorial explains the groundwork. It describes use of the following tools:

*
*
*
*
*
*
*
*
*
*
*
*

## Tips and tricks about Debian
## Override dependency handling
dpkg does not recognize dependencies installed by pacman. This means  will generally fail with errors such as:

 dpkg-checkbuilddeps: Unmet build dependencies: build-essential:native debhelper (>= 8.0.0)
 dpkg-buildpackage: warning: build dependencies/conflicts unsatisfied; aborting

To override this, use the -d flag:

 $ dpkg-buildpackage -d -us -uc

You may also need to override  by adding the following lines to :

 override_dh_shlibdeps:
    dh_shlibdeps --dpkg-shlibdeps-params=--ignore-missing-info

{{Note|Any run-time dependencies (and matching version numbers) should be added manually to
, where {{ic|${shlibs:Depends}}} now has no meaning.}}

## Set up a chroot
See the Pbuilder How-To for an introduction to pbuilder-ubuntu. Using cowdancer in addition is recommended as copy-on-write offers a significant performance benefit.

* ,  and  are required.
* eatmydata is available as . To prevent  errors, it must be installed both inside and outside the chroot. As the paths are different in Arch and Debian, create the following symbolic links:
 # ln -s /usr/lib/libeatmydata.so.1.1.1 /usr/lib/libeatmydata/libeatmydata.so
 # ln -s /usr/lib/libeatmydata.so.1.1.1 /usr/lib/libeatmydata/libeatmydata.so.1
* Sample pbuilderrc
* To create a source package for pbuilder to handle:
 $ dpkg-buildpackage -d -us -uc -S

## See also about Debian
* Debian Policy
* New Maintainers' Guide
* Quilt in Debian packaging

## Fedora
Fedora Packaging Tutorial

*
*

## See also about Fedora
* Copr

## openSUSE
The Open Build Service (OBS) is a generic system to build and distribute packages from sources in an automatic, consistent and reproducible way. It supports at least .deb, .rpm and Arch packages.

## Creating Arch packages in OBS with OSC
## Creating a package
# Create an account in # Install the  package. Upstream documentation is available [https://en.opensuse.org/openSUSE:OSC here.
# Create an example  project.
# Create an example  subproject (optional, but recommended).
# Create a new  example package with . Save the created XML then exit.
# Switch to a clean working directory then checkout the project you have just created: .
# Now cd into it: .

## Managing a package
Now it is time to decide how we will manage our project. There are two practical ways to do this:

# Maintain a PKGBUILD plus its helper files (such as *.install scripts) in a version control system (such as git, hg) then just make OBS track it;
# Maintain a package entirely in OBS itself.

The first version is more flexible and dynamic. To proceed:

* From your project directory, create a  file with the following contents:

Here is an example for :

* Make OBS track it:
* If you have any other files to include into the repo, just proceed as before: add the files in the project directory, then make OBS track them (OBS uses subversion as its underlying SCM, so this process might already be familiar for you)
* Check-in (=upload) your files into the repo .

Now, after a while, OBS will begin building your package.

## Tips and tricks about openSUSE
* To see the build progress of your package, cd into its working directory, then: .
* There are three repositories, Arch:Core, Arch:Extra and Arch:Community. can be appended as a "repository path" after adding the main Arch repository to the project.

## ca-certificates-utils package problem
If OBS build fails because of the ca-certificates-utils package, you can add this line to your project config (from your project page, go to Advanced -> Project Config).
 Prefer: ca-certificates-utils ca-certificates

## See also about openSUSE
* Example repo: [https://build.opensuse.org/package/show/home:metakcahura/cpu-x-git arch-cpu-x-git
* openSUSE packaging guidelines
* Portal:Packaging from openSUSE wiki

## Multi-distribution
## Pacur
Some tools such as Pacur allow building packages for multiple Linux distributions with a consistent package specification format.
The package format is very similar to PKGBUILD so it is easy to re-use an existing PKGBUILD and add a few distribution-specific variables to be able to build debian and rpm packages effortlessly.
By quickly adapting a PKGBUILD one is able to build package for Amazon Linux, Centos, Debian, Oracle Linux, Fedora and Ubuntu.
