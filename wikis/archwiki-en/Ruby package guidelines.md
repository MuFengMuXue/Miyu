# Ruby package guidelines

This document covers standards and guidelines on writing PKGBUILDs for software that uses .

## Package naming
For libraries, use  (where  is the upstream project name). For applications, use the project name (without the  prefix) and optionally add  to .

## Build and tests
Ruby packages should be built from upstream sources as this provides a transparent chain of trust for the build. To ensure integration with the existing set of Ruby packages, it is expected to run tests using  or .

## Template
{{hc|head=PKGBUILD|output=
prepare() {
  cd "${_name}-${pkgver}"

  # update gemspec/Gemfile to allow newer version of the dependencies
  sed --in-place --regexp-extended 's~>>=g' "${_name}.gemspec"
}

build() {
  cd "${_name}-${pkgver}"

  local _gemdir="$(gem env gemdir)"

  gem build "${_name}.gemspec"

  gem install \
    --local \
    --verbose \
    --ignore-dependencies \
    --build-root "tmp_install" \
    "${_name}-${pkgver}.gem"

  # remove unrepreducible files
  rm --force --recursive --verbose \
    "tmp_install/${_gemdir}/cache/" \
    "tmp_install/${_gemdir}/gems/${_name}-${pkgver}/vendor/" \
    "tmp_install/${_gemdir}/doc/${_name}-${pkgver}/ri/ext/"

  find "tmp_install/${_gemdir}/gems/" \
    -type f \
    \( \
      -iname "*.o" -o \
      -iname "*.c" -o \
      -iname "*.so" -o \
      -iname "*.time" -o \
      -iname "gem.build_complete" -o \
      -iname "Makefile" \
    \) \
    -delete

  find "tmp_install/${_gemdir}/extensions/" \
    -type f \
    \( \
      -iname "mkmf.log" -o \
      -iname "gem_make.out" \
    \) \
    -delete
}

check() {
  cd "${_name}-${pkgver}"

  local _gemdir="$(gem env gemdir)"

  GEM_HOME="tmp_install/${_gemdir}" rake test
}

package() {
  cd "${_name}-${pkgver}"

  cp --archive --verbose tmp_install/* "${pkgdir}"

  install --verbose -D --mode=0644 LICENSE --target-directory "${pkgdir}/usr/share/licenses/${pkgname}"
  install --verbose -D --mode=0644 *.md --target-directory "${pkgdir}/usr/share/doc/${pkgname}"
}
}}

## Tips and tricks
## The gem is deriving the files to add with "git ls-files"
In this case you can add the following  command to the  function:

{{bc|
# we don't build from a git checkout
sed --in-place --regexp-extended 'sgit ls-filesfind . -type f -not -path "*/\.git/*"' "${_name}.gemspec"
}}

## The upstream project is using "rspec" to run tests
In this case you can replace the code line in the  function with the following:

 GEM_HOME="tmp_install/${_gemdir}" rspec
