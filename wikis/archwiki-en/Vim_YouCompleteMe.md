# Vim/YouCompleteMe

YouCompleteMe (shortened as YCM) is a code-completion engine for Vim. It supports the following languages:

* C/C++/Objective-C/Objective-C++
* Python
* C#
* Go
* Rust
* Java
* JavaScript
* TypeScript
* Other languages (Ruby, PHP etc.) through the use of omnicompletion system

## Installation
Install the  package. For an alternative manual way of installing YouCompleteMe see upstream instructions.

## Configuration
## C/C++
YCM uses a python script called  to set project wide settings, needed to provide completion and syntax check. A brief introduction to essential configuration follows, for details and advanced options see the upstream documentation.

Alternatively, provide a  in the project's root.

## Extra conf structure
A sample  may be found in You should save a copy of this file in your project folder and customize it with adequate settings for your source files.

The most important settings (which usually suffices for a minimal configuration) are the  and  options, which respectively tells the syntax checker the language used in the project and the standard followed. The  value may be set to  or , while common values for the  are , , ,  and their respective c++ version. The standard parameter will determine the warning and the errors in the syntax check (e.g., a line commented with  will be marked as unallowed in C89, but not under following versions of the standard).

A third party script and vim plugin for the automatic generation of the  is available on [https://github.com/rdnetto/YCM-Generator this repo.

## Extra conf location
The program searches for the  file on startup in the current source file directory and in its parent folders. If the file is not found, YCM features are not available. A global file (used as fallback when a local extra conf file is not found) may be set adding the following to :

Being the extra conf file a python script, when a file is found a confirmation is asked for security reason before to load it. This behaviour may be disabled adding the following to :

For a less unsecure solution, when the confirmation is enabled an extra conf file blacklist/whitelist may be set assigning a list of patterns to the  variable. A file matching one pattern is blacklisted if the pattern begins with , whitelisted otherwise, confirmation is asked if the file does not match any pattern. Rule precedence is determined by the order, and the first match is applied. Some glob pattern rules are available:

* * matches everything
*? matches any single character
* matches any character in seq
* [!seq matches any char not in seq

In example, with the following setting

any file in  will be whitelisted, any in  will be blacklisted, and due to order precedence any file in  excepted the  folder will be blacklisted.

## Java
YCM has integrated support for jdt.ls which can be installed by passing  to the  script.

## C#
Before starting work with a C# project, ensure that  is installed on your system as it is a required dependency of Omnisharp-Roslyn, the C# completion engine used by YouCompleteMe. More information can be found in Omnisharp-Roslyn's README and the following Github issue.

First create a solution file:

{{hc|SOLUTION.sln|
Microsoft Visual Studio Solution File, Format Version 11.00
# Visual Studio 2010
Project("{00000000-0000-0000-0000-000000000000}") = "PROJECT", "PROJECT\PROJECT.csproj", "{11111111-1111-1111-1111-111111111111}"
EndProject
EndProject
Global
	GlobalSection(SolutionConfigurationPlatforms) = preSolution
		Debug|x86 = Debug|x86
		Release|x86 = Release|x86
	EndGlobalSection
	GlobalSection(ProjectConfigurationPlatforms) = postSolution
		{11111111-1111-1111-1111-111111111111}.Debug|x86.ActiveCfg = Debug|x86
		{11111111-1111-1111-1111-111111111111}.Debug|x86.Build.0 = Debug|x86
		{11111111-1111-1111-1111-111111111111}.Release|x86.ActiveCfg = Release|x86
		{11111111-1111-1111-1111-111111111111}.Release|x86.Build.0 = Release|x86
	EndGlobalSection
EndGlobal}}

Then create a directory named  and in it a file named :

{{hc|1=PROJECT/PROJECT.csproj|2=

    Debug
    x86
    10.0.0
    2.0
    {11111111-1111-1111-1111-111111111111}
    Exe
    PROJECT
    PROJECT

    true
    full
    false
    bin\Debug
    DEBUG;
    prompt
    4
    false
    x86

    full
    true
    bin\Release
    prompt
    4
    false
    x86

}}

Place your C# files in  directory and do not forget to manually add them at the bottom of .

Now YouCompleteMe should work for C# files in that directory and you can build the project. To compile the project from inside Vim:

 :!xbuild

## Troubleshooting
Remember that it might take some time for YouCompleteMe to generate a list of completion strings.

The following commands are available for diagnostics:

*  - show previous errors or messages from Vim
*
*

## E764: Option 'omnifunc' is not set
If this happens for Java files, you forgot to put this in your .vimrc:

## No completion in Java files
Make sure  daemon is running:

 $ ps -ax|grep eclimd

and that you have first generated project files.

## URLError:
This error appears when you do not have a  file in current or parent directory.

## RuntimeError: Error starting OmniSharp server: no solutionfile found
Same as above.
