# Python package guidelines

This document covers standards and guidelines on writing PKGBUILDs for Python software.

## Package naming
For Python 3 library modules, use . Also use the prefix if the package provides a program that is strongly coupled to the Python ecosystem (e.g. pip or tox). For other applications, use only the program name.

## Architecture
See PKGBUILD#arch.

A Python package that contains C extensions is architecture-dependent. Otherwise it is most likely architecture-independent.

Packages built using setuptools define their C extensions using the  keyword in .

## Source
Download URLs linked from the PyPI website include an unpredictable hash that needs to be fetched from the PyPI website each time a package must be updated. This makes them unsuitable for use in a PKGBUILD. PyPI provides an alternative stable scheme: PKGBUILD#source  array should use the following URL templates:

;Source package:
:{{ic|https://files.pythonhosted.org/packages/source/${_name::1}/${_name//-/_}/${_name//-/_}-$pkgver.tar.gz}}
;Pure Python wheel package
:{{ic|https://files.pythonhosted.org/packages/py2.py3/${_name::1}/$_name/${_name//-/_}-$pkgver-py2.py3-none-any.whl}} (Bilingual – Python 2 and Python 3 compatible)
:{{ic|https://files.pythonhosted.org/packages/py3/${_name::1}/$_name/${_name//-/_}-$pkgver-py3-none-any.whl}} (Python 3 only)
:Note that the distribution name can contain dashes, while its representation in a wheel filename cannot (they are converted to underscores).
;Architecture specific wheel package
:Additional architecture-specific arrays can be added by appending an underscore and the architecture name, e.g.  . Also  can be used to not repeat the Python version:
:{{ic|https://files.pythonhosted.org/packages/$_py/${_name::1}/$_name/${_name//-/_}-$pkgver-$_py-${_py}m-manylinux1_x86_64.whl}}

Note that a custom  variable is used instead of  since Python packages are generally prefixed with . This variable can generically be defined as follows:

 _name=${pkgname#python-}

## Installation methods
Python packages are generally installed using language-specific package manager such as pip, which fetches packages from an online repository (usually PyPI, the Python Package Index) and tracks the relevant files.

However, for managing Python packages from within s, one needs to "install" the Python package to the temporary location .

For Python packages using standard metadata to specify their build backend in , this can most easily achieved using  and .
Old packages might fail to specify that they use setuptools, and only offer a  that has to be invoked manually.

## Standards based (PEP 517)
A standards based workflow is straightforward: Build a wheel using  and install it to  using :

{{bc|1=
makedepends=(python-build python-installer python-wheel)

build() {
    cd $_name-$pkgver
    python -m build --wheel --no-isolation
}

package() {
    cd $_name-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}
}}

where:

*  results in only a wheel file to be built, no source distribution.
*  means that the package is built using what is installed on your system (which includes packages you specified in ), by default the tool creates an isolated virtual environment and performs the build there.
*  prevents trying to directly install in the host system instead of inside the package file, which would result in a permission error
*  or  can be passed to , but the default is sensibly picked, so this should not be necessary.

{{Tip|If your package is a VCS package (), include the command {{ic|1=git -C "${srcdir}/${pkgname}" clean -dfx}} in your  function. This removes stale wheels along with other build artifacts, and helps prevent issues further down the road. See also upstream issues for setuptools and Poetry.}}

## setuptools or distutils
If no  can be found or it fails to contain a  table, it means the project is using the old legacy format, where the project provides a setup.py file, which invokes the  function from setuptools or distutils.core.

Such packages usually can also be built and installed using the method described above using  and , and this is the preferred method. But they will also additionally need  in .

You can still build and install these packages using the old, deprecated way of running setup.py directly, which is shown below and it is described here for those cases, where the pep-517 compliant way does not work for some reason.

But note that you will get the following warning in the output of the  step, when building a package using this method:

Also note that Python versions from 3.12 onwards do not include distutils in the standard library any more, which means that packages for projects still using setup.py generally need to have  in , since that provides its own version of distutils.

{{bc|1=
makedepends=('python-setuptools')

build() {
    cd $_name-$pkgver
    python setup.py build
}

package() {
    cd $_name-$pkgver
    python setup.py install --root="$pkgdir" --optimize=1
}
}}

where:

*  works like  above
*  compiles optimized bytecode files (.opt-1.pyc) so they can be tracked by pacman instead of being created on the host system on demand.
* Adding  optimizes away the unnecessary attempt to re-run the build steps already run in the  function, if that is the case.

If a package uses , the package most likely will not build with an error such as:

To get it building  has to be exported as an environment variable with  as the value:

 export SETUPTOOLS_SCM_PRETEND_VERSION=$pkgver

## Check
Most Python projects providing a testsuite use the unittest runner or nosetests or pytest (provided by  and  and , respectively) to run tests with  in the name of the file or directory containing the testsuite. In general, simply running  or  is enough to run the testsuite.

{{bc|
check(){
    cd $_name-$pkgver

    # Builtin unittest
    python -m unittest discover -v

    # For nosetests
    nosetests

    # For pytest
    pytest
}
}}

If there is a compiled C extension, the tests need to be run using a , that reflects the current major and minor version of Python in order to find and load it.

{{bc|1=
check(){
    cd $_name-$pkgver
    local python_version=$(python -c 'import sys; print("".join(map(str, sys.version_info# Builtin unittest
    PYTHONPATH="$PWD/build/lib.linux-$CARCH-cpython-$python_version" python -m unittest discover -vs .

    # For nosetests
    PYTHONPATH="$PWD/build/lib.linux-$CARCH-cpython-$python_version" nosetests

    # For pytest
    PYTHONPATH="$PWD/build/lib.linux-$CARCH-cpython-$python_version" pytest
}
}}

## Tips and tricks
## Using Python version
Sometimes during preparing, building, testing or installation it is required to refer to the system's major and minor Python version (e.g.  or ). Do not hardcode this and instead use a call to the Python interpreter to retrieve the information and store it in a local variable:

{{bc|1=
check(){
  local python_version=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2)))')
  ...
}
}}

## Using site-packages
Sometimes during building, testing or installation it is required to refer to the system's  directory. Do not hardcode this directory and use a call to the Python interpreter instead to retrieve the path and store it in a local variable:

{{bc|1=
check(){
  local site_packages=$(python -c "import site; print(site.getsitepackages()...
}
}}

## Test directory in site-package
Make sure to not install a directory named just  directly under  (i.e. ). Doing so could lead to conflicts between packages. Python package projects using setuptools are sometimes misconfigured to include the directory containing its tests as a top level Python package. If you encounter this, you can help by filing an issue with the package project and ask them to fix this, e.g. [https://github.com/Lightning-AI/lightning/issues/10335 like this.

## Disable pytest options
When running pytest, it is mostly desirable to not run with additional plugins. Especially plugins for linting and coverage are counterproductive in packaging, as changes in behavior may have tests fail.
To disable pytest options such as  it is preferred to use an option override on the command line over patching any configuration files used by pytest due to the maintenance overhead.

To unset all additional options use

 pytest -o addopts=""

## Fix reproducibility issue with meson-python
When using  as a PEP 517 build backend it uses randomized folder paths that create reproducibility issues. This can be circumvented by hardcoding the used folder with the  flag:
 python -m build --wheel --no-isolation -Cbuild-dir=build

## Running tests with an installed package
Some packages require being installed to have the tests run successfully. In such cases, such as for example , you can create a virtual environment to install the built package and run the tests there:

 python -m venv --system-site-packages test-env
 test-env/bin/python -m installer dist/*.whl
 test-env/bin/python -P -m pytest
