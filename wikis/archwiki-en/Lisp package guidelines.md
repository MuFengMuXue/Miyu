# Lisp package guidelines

At the moment, there are relatively few Lisp packages available in the Arch repositories. This means that at some point or another, more will likely appear. It is useful, therefore, to figure out now, while there are few packages, how they should be packaged.

## Directory structure and naming
There is at least one package in the base repository () that includes lisp files, which are placed in . In keeping with this, other lisp packages should also place their files in .

The package directory should be the name of the lisp package, not what it is called in Arch's official repositories (or AUR). This applies even to single-file packages.

For example, a Lisp package called "cl-ppcre" should be called  in AUR and reside in . A Lisp package called "alexandria" should be called  in AUR and reside in .

## ASDF
Try to avoid the usage of Lisp's ASDF-Install as a means of installing these system-wide packages.

ASDF itself may be necessary or helpful as a means of compiling and/or loading packages. In that case, it is suggested that the directory used for the central registry (the location of all of the symlinks to ) be .

However, I have observed problems with doing the compilation with asdf as a part of the package compilation process. However, it does work during an install, through use of a  file. Such a file might look like this:

{{hc|cl-ppcre.install|
# arg 1:  the new package version
post_install() {
    echo "---> Compiling lisp files  Done compiling lisp files <---"

    cat << EOM

    To load this library, load asdf and then place the following lines
    in your ~/.clisprc.lisp file:

    (push #p"/usr/share/common-lisp/systems/" asdf:*central-registry*)
    (asdf:operate 'asdf:load-op 'cl-ppcre)
EOM
}

post_upgrade() {
    post_install $1
}

pre_remove() {
    rm /usr/share/common-lisp/source/cl-ppcre/{*.fas,*.lib}
}

op=$1
shift

$op $*
}}

Of course, for this example to work, there needs to be a symlink to package.asd in the asdf system directory. During package compilation, a stanza such as this will do the trick...

 pushd ${_lispdir}/systems
 ln -s ../source/cl-ppcre/cl-ppcre.asd .
 ln -s ../source/cl-ppcre/cl-ppcre-test.asd .
 popd

where  is . By linking to a relative, rather than an absolute, path, it is possible to guarantee that the link will not break post-install.

## Lisp-specific packaging
When possible, do not make packages specific to a single lisp implementation; try to be as cross-platform as the package itself will allow. If, however, the package is specifically designed for a single lisp implementation (i.e., the developers have not gotten around to adding support for others yet, or the package's purpose is specifically to provide a capability that is built in to another lisp implementation), it is appropriate to make your Arch package lisp-specific.

If the package is implementation-independent, it should depend on common-lisp. If the package supports multiple but not all implementations, you could (a) not make your package depend on *any* lisp and include a statement in the package.install file telling folks to make sure they have a supported lisp installed (not ideal), or (b) Take direction from the sbcl PKGBUILD and include a conditional statement to figure out which lisp is needed (which is hackish and, again, far from ideal). Other ideas are welcome.

Also note that if ASDF is needed to install/compile/load the package, things could potentially get awkward as far as dependencies go. SBCL and CMUCL come with asdf installed, but clisp does not (but there is an AUR package).

People currently maintaining lisp-specific packages that do not need to be lisp-specific should consider doing at least one of the following:

* Editing their PKGBUILDs to be cross-platform, provided someone else is not already maintaining the same package for a different lisp.
* Offering to take over maintenance or help with maintenance of the same package for a different lisp, and then combining them into a single package.
* Offering up their package to the maintainer of a different lisp's version of the same package, so as to allow that person to combine them into a single package.

## Things you, the reader, can do
* Maintain Lisp packages following these guidelines
* Update and fix problems with these guidelines
* Keep up with what has changed here
* Provide (polite) thoughts, feedback, and suggestions both on this document and to people's work.
* Translate this page and future updates to this page.
