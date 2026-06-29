# Node.js package guidelines

This document covers standards and guidelines on writing PKGBUILDs for Node.js packages.

## Package naming
{{Tip|1=A custom  variable can be used instead of . This variable can generically be defined as follows: {{ic|1=_pkgname=${pkgname#nodejs-} }} }}

Package names for Node.js libraries should start with a  prefix. For standalone applications, just use the program name.

## Source
npm provides a stable naming scheme for download URLs. PKGBUILD#source  array can use the following URL template:

 https://registry.npmjs.org/$_pkgname/-/$_pkgname-$pkgver.tgz

## Using npm
When installing with npm, add it as a build dependency:

 makedepends=('npm')

There is also usually no need to extract the tarball:

 noextract=("${_pkgname}-${pkgver}.tgz")

This is a minimal package function:

{{bc|
package() {
    npm install -g --prefix "${pkgdir}/usr" "${srcdir}/${_pkgname}-${pkgver}.tgz"
}
}}

## Setting temporary cache
When npm processes  in order to build a package it downloads dependencies to its default cache folder at . To avoid littering user's home folder we can temporarily set a different cache folder with  flag.

Download dependencies to {{ic|${srcdir}/npm-cache}} and install them in package directory:

 npm install --cache "${srcdir}/npm-cache"

Continue with packaging as usual:

 npm run packager

## Package contains reference to $srcdir/$pkgdir
npm unfortunately creates references to the source dir and the pkg dir, this is a known issue. However, you may remove those references manually since they are not used in any way.

All dependencies will contain a reference to , in the  attribute. You can usually remove those attributes with some sed magic as follows:

 find "$pkgdir" -name package.json -print0 | xargs -r -0 sed -i '/_where/d'

Your main package will have some other references too. The easiest way to remove those is to remove all underscored properties, but that is not as easy with sed. Instead, you can use  for similar results as follows:

Another place where you may find references to  is the  attributes of packages. If you do not care about man pages (they will not be installed for dependencies anyway), you may delete them like this:

An example of all three of these techniques can be seen in nodejs-readability-cli's PKGBUILD.

## Using nvm
When a node.js-based application requires different version for building or packaging, then  can be leveraged.

Add it as a build dependency:

 makedepends=('npm' 'nvm')

 uses  environment variable to look for its prefix, which is set to  if not specified before  initialization.

You can use the following function to create and isolate your custom prefix from user's location:

{{bc|
_ensure_local_nvm() {
    # let's be sure we are starting clean
    which nvm >/dev/null 2>&1 && nvm deactivate && nvm unload
    export NVM_DIR="${srcdir}/.nvm"

    # The init script returns 3 if version specified
    # in ./.nvmrc is not (yet) installed in $NVM_DIR
    # but nvm itself still gets loaded ok
    source /usr/share/nvm/init-nvm.sh ||  $? != 1
}
}}

This function should be called before interacting with ,  or any other Node.js based programs that should use the specified version.

## Example PKGBUILD usage
{{bc|
prepare() {
    _ensure_local_nvm
    nvm install 14.15.0
}

build() {
    _ensure_local_nvm
    npm install
}
}}

Alternatively, bare  will look for a version string in  file in the current directory.

An example of this usage can be seen in . See PKGBUILD for more information.
