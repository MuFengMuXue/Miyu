# Kate

Kate is a text editor for KDE.

## Installation
Install the  package.

To get an integrated terminal install .

The package  activates the git-blame plugin.

For additional programming language support, see Language Server Protocol.

See language checking for installing additional dictionaries to check spellings.

## Configuration
Kate can open folders and if it detects a .kateproject JSON file it will load the configuration. The format of this file is documented here.

This example will read all files tracked by git and add support for Make build system.
{{hc|1=.kateproject|2=
{
  "name": "Project",
  "files": [ { "git": 1 } ],
  "build": {
  "directory": ".",
    "build": "make all",
    "clean": "make clean"
  }
}
}}
