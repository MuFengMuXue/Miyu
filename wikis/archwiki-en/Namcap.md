# Namcap

Namcap is an Arch Linux tool to check binary packages and source PKGBUILDs for common packaging mistakes.

## Installation
Install the  package.

## Usage
To run namcap on a file, where file_name is  or the name of a package binary :

 $ namcap file_name

If you want to see extra informational messages, then invoke namcap with the  () flag:

 $ namcap --info file_name

Namcap uses a system of tags of three types to classify the output:

*  — Errors —  are things that namcap is very sure are wrong and need to be fixed. An error is important and should be fixed immediately; mostly they relate to insufficient security, missing licenses or permission problems.
*  — Warnings — are things that namcap thinks should be changed, but if you know what you are doing then you can leave them.
*  — Information — are only shown when you use the  argument. Information messages give information that might be helpful but is not anything that needs changing—think of them as notes or comments.

Normally namcap prints a human-readable explanation (sometimes with suggestions on how to fix the problem). If you want output which can be easily parsed by a program, then pass the  () flag to namcap.

See , README and NEWS for more information.

To filter unneeded namcap messages you can use , for example:

 namcap --info file_name \
   | grep \
       --invert-match \
       --perl-regexp \
       --regexp=" W: Package was :digit:+% docs by size; maybe you should split out a docs package|\
  I: Dependency .* detected and satisfied \(libraries \needed in files \['.*'\\)|\
  I: Dependency .* detected and satisfied \(programs \needed in scripts \['.*'\\)|\
  I: Link-level dependence .* in file \I: Script link detected \(.*\) in file \['.*'\|\
  I: Soname dependency '.*\.so=.*' provided by .* is satisfied \(needed in files \== Tag file ==

The  [https://gitlab.archlinux.org/pacman/namcap/-/blob/master/namcap-tags tag file consists of lines specifying the human-readable form of the hyphenated machine-parsable tags used in the namcap code:

 # The comment
 machine-parsable-tag %s :: The human-readable description for the tag %s

## Creating a module
The main namcap program  takes as parameters the filename of a package or a  and makes a pkginfo object, which it passes to a list of rules defined in  and . Once your module is finalized, remember to add it to the appropriate array:

*  defines the rules which process binary packages,
*  defines the rules which process s.

A sample namcap module is like this:

Each namcap module must have the following methods:

*  — returns a string containing a short name of the module. Usually, this is the same as the  of the module file.

*  — returns a string containing a concise description of the module. This description is used when listing all the rules using .

*  — returns a string containing the prerequisites needed for the module to operate properly. Usually empty string () for modules processing s and  for modules processing package files.  should be specified if the package contents should be extracted to a temporary directory before further processing.

*  — should return a list comprising in turn of three lists: error, warning and information tags respectively. Each member of these tag lists should be a tuple consisting of two components: the short — hyphenated — form of the tag with the appropriate format specifiers (like ) and the parameters.

*  — returns  for a module processing s, and  for a module processing a binary package file.

## Troubleshooting
## W: Directory (usr/src/debug/…) is empty
Machine-parsable message: .

You may silence this warning by applying  in your PKGBUILD. This might be useful for Arch User Repository (AUR) packages which use Debian packages as the source.

## I: Soname … is not specified as provides by … yet (needed in files …)
Machine-parsable tag: .

The dependency provides array does not contain the soname—i.e. the dependency's  file should be changed and the dependecy should be rebuilded.

## I: Soname dependency … provided by … detected and not included (needed in files …)
Machine-parsable tag: .

Include the soname in the depends array.

 can add soname dependency automatically, but the dependency must be built with  first. For more information, see:

*
*
* Library dependencies.
