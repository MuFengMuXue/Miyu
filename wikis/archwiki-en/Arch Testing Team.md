# Arch Testing Team

The Arch Testing Team is a group within the Arch community in charge of making sure that packages submitted to the testing repositories are functional. This includes, making sure that the package installs correctly, that it does not cause breakage with packages of which it depends on, among others.

Arch Testers sign off packages after vouching for their correctness so that they can be moved from the testing repositories into the core or extra repositories.

## Guidelines
In order to test an arch package, keep the following aspects in mind:

* If you are testing a kernel or a package that relies on kernel modules, you should restart the machine and ensure that it boots correctly.
* Although testing on virtualization software is not prohibited, it may not be as useful as testing a package in a bare-metal installation. This applies specially to packages that are susceptible to different types of hardware, such as kernel packages.
* If you are testing a library, you may want to execute a binary that uses such library (which can be found using pactree's  flag). Make sure the shared object file is loaded using ldd.
* Likewise, if there is a package that ships executables, testing their basic functionality is encouraged.
* If you notice an error when testing a package, follow the Bug reporting guidelines to create an issue.

## Coordination
You can coordinate with other testers on the #archlinux-testing IRC channel.
