# 32-bit package guidelines

Legacy 32-bit software can be built and installed on machines of another native architecture, such as x86_64. This article explains the production and conventions of such packages.

## Package naming
* Prefix 32-bit versions of native packages with lib32-.
* Package decriptions should distinguish these from native counterparts, i.e. .

## Variables and parameters
## lib32
Specify these bash variables in a PKGBUILD to tell the compiler to output 32-bit code:

 export CFLAGS+=" -m32"
 export CXXFLAGS+=" -m32"
 export LDFLAGS+=" -m32"
 export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

## File placement
Ensure lib32 package files do not conflict with native package files and include all necessary files, such as architecture-specific includes. For example, if a package builds using GNU Autoconf, specify the following to :

 --program-suffix="-32" \
 --lib{exec,}dir=/usr/lib32 \
 --includedir=/usr/include/"$pkgbase"32 \
 --build=i686-pc-linux-gnu

If a package builds using Meson, specify the following to :

 --cross-file lib32
