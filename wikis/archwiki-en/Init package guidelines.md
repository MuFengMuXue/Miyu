# Init package guidelines

This document covers standards and guidelines on writing PKGBUILDs for init scripts, e.g. .

## Package naming
For init scripts, use . For example: , , , .

## Architecture
See PKGBUILD#arch.

A init script should be architecture-independent.

## Depends
All scripts should depend on its init, i.e.  requires  for it to work.
