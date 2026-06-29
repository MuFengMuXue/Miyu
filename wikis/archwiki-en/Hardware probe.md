# Hardware probe

hw-probe (hardware probe) is a Perl program which is able to:

* collect output from a number of utilities—such as  and —and some other logs,
* analyze collected data:
** check if drivers were loaded,
** check for driver or hardware operability status (partially),
* benchmark (quick and simple)—by using several tools such as 7-Zip and hdparm,
* contribute this information to the Linux Hardware Database.

Statistics that is based on the database data—both current and historical one—can be viewed at Trends.

## Installation
Install the  package. Additional packages that might be useful:

*  — benchmarking (with  or  option),
*  — probing and benchmarking storage devices,
*  — memory testing during benchmarking,
*  — probing and benchmarking OpenGL on X,
*  — JSON-formatted  output file.

## Usage
Make a probe:

 # hw-probe --all --upload

Decode ACPI tables (requires  package):

 # hw-probe --all --upload --decode-acpi

## Benchmarking
Specific benchmarking options:

*  — test CPU and RAM with ,
*  — test CPU by applying  to 512 MB of zeroes from ,
*  — test GPU with glxgears,
*  — test storage devices with ,
:*  — limit number of drives to be tested—i.e. test only the first number of them,
*  — test 8 megabytes of RAM with .

Perform all benchmarking tests mentioned above, including 7-Zip one:

 # hw-probe --check-extended
