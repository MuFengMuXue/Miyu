**Resources**

[[]][Home](https://www.gnu.org/software/bc/)

[[]][Official documentation](https://www.gnu.org/software/bc/manual/bc.html)

[[]][Package information](https://packages.gentoo.org/packages/sys-devel/bc)

[[]][Wikipedia](https://en.wikipedia.org/wiki/bc_(programming_language) "wikipedia:bc (programming language)")

[[]][Man page](http://man7.org/linux/man-pages/man1/bc.1p.html)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/bc)

**[bc]** is an arbitrary-precision fixed-point mathematical scripting language with a C-like syntax. In modern usage, [bc] is typically used to overcome the limitations of shell scripting languages which are often restricted to integer arithmetic. In this capacity it is usually embedded into an existing shell script with either a pipe or a HERE-DOCUMENT statement. Use cases requiring floating-point calculations embedded into shell scripts typically call for [Perl](https://wiki.gentoo.org/wiki/Perl "Perl"), [Ruby](https://wiki.gentoo.org/wiki/Ruby "Ruby"), or [Raku](https://wiki.gentoo.org/wiki/Raku "Raku") in place of [bc] as all three are one-liner friendly languages.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Environment variables]](#Environment_variables)
-   [[2] [Usage]](#Usage)
-   [[3] [Advanced Math Calculation]](#Advanced_Math_Calculation)
    -   [[3.1] [Functions]](#Functions)
    -   [[3.2] [Math Library Functions]](#Math_Library_Functions)
    -   [[3.3] [Relational Expressions]](#Relational_Expressions)
    -   [[3.4] [Boolean Expressions]](#Boolean_Expressions)
    -   [[3.5] [Special Variables]](#Special_Variables)
    -   [[3.6] [Special Expression]](#Special_Expression)
-   [[4] [Examples]](#Examples)
    -   [[4.1] [Convert Decimal to Hexadecimal]](#Convert_Decimal_to_Hexadecimal)
    -   [[4.2] [Decimal to Binary]](#Decimal_to_Binary)
    -   [[4.3] [Declare Variables]](#Declare_Variables)
    -   [[4.4] [Specify Input Files]](#Specify_Input_Files)
    -   [[4.5] [Fahrenheit to Celsius]](#Fahrenheit_to_Celsius)
    -   [[4.6] [Calculate π]](#Calculate_.CF.80)
    -   [[4.7] [Arithmetic Calculator]](#Arithmetic_Calculator)
-   [[5] [Removal]](#Removal)
    -   [[5.1] [Unmerge]](#Unmerge)
-   [[6] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [sys-devel/bc](https://packages.gentoo.org/packages/sys-devel/bc) [[]] [Handy console-based calculator utility]

  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------
  [`libedit`](https://packages.gentoo.org/useflags/libedit)     Use the libedit library (replacement for readline)
  [`readline`](https://packages.gentoo.org/useflags/readline)   Enable support for libreadline, a GNU line-editing library that almost everyone wants
  [`static`](https://packages.gentoo.org/useflags/static)       !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically
  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Emerge [[[sys-devel/bc]](https://packages.gentoo.org/packages/sys-devel/bc)[]]:

`root `[`#`]`emerge --ask sys-devel/bc`

### [Environment variables]

-   `POSIXLY_CORRECT` follow the POSIX standard to the letter. The `-s` switch has the same effect.
-   `BC_ENV_ARGS` arguments to be passed into [bc] by default.
-   `BC_LINE_LENGTH` An integer specifying the number of characters per line of output.

## [Usage]

`user `[`$`]`bc --help`

    usage: bc [options] [file ...]
      -h  --help         print this usage and exit
      -i  --interactive  force interactive mode
      -l  --mathlib      use the predefined math routines
      -q  --quiet        don't print initial banner
      -s  --standard     non-standard bc constructs are errors
      -w  --warn         warn about non-standard bc constructs
      -v  --version      print version information and exit

## [Advanced Math Calculation]

All the standard mathematical operators are available in bc and it is possible to use relational expressions and boolean expressions.

`user `[`$`]`echo "a=1; b=2; b<a || a==2;" |bc `

    0

`user `[`$`]`echo "a=1; b=2; b>a || a==2;" |bc `

    1

The GNU [bc] command line also support various statements like if, print, while, and for.

### [Functions]

Functions provide a method of defining a computation that can be executed later. Functions in bc always compute a value and return it to the caller. Function definitions are \"dynamic\" in the sense that a function is undefined until a definition is encountered in the input. That definition is then used until another definition function for the same name is encountered. The new definition then replaces the older definition. A function is defined as follows:

[bc] allows you to define your own user-defined functions which makes the language very powerful as you can create all the mathematical functions that may be needed

`define name ( parameters )  `

` define d (n) `

`  `

### [Math Library Functions]

In order to use bc advanced math libraries (*mathlib*)- If bc is invoked with the [-l] option, a math library is preloaded and the default scale is set to *20*. The math functions will calculate their results to the scale set at the time of their call. The math library defines the following functions:

  ---------------------- -------------------------------------------------------
  Predefined functions   Description
  `s (*x*)`              The sine of x, x is in radians.
  `c (*x*)`              The cosine of x, x is in radians.
  `a (*x*)`              The arctangent of x, arctangent returns radians.
  `l (*x*)`              The natural logarithm of x.
  `e (*x*)`              The exponential function of raising e to the value x.
  `j (*n*,*x*)`          The bessel function of integer order n of x.
  ---------------------- -------------------------------------------------------

`user `[`$`]`bc -l <<< "l(3)" `

    1.09861228866810969139

### [Relational Expressions]

Relational expressions are a special kind of expression that always evaluate to 0 or 1, 0 if the relation is false and 1 if the relation is true. These may appear in any legal expression. (POSIX bc requires that relational expressions are used only in if, while, and for statements and that only one relational test may be done in them.) The relational operators are

  ------------------------ ------------------------------------------------------------
  Relational Expressions   Description
  `expr1 < expr2`          The result is 1 if expr1 is strictly less than expr2
  `expr1 <= expr2`         The result is 1 if expr1 is less than or equal to expr2
  `expr1 > expr2`          The result is 1 if expr1 is strictly greater than expr2
  `expr1 >= expr2`         The result is 1 if expr1 is greater than or equal to expr2
  `expr1 == expr2`         The result is 1 if expr1 is equal to expr2
  `expr1 != expr2`         The result is 1 if expr1 is not equal to expr2
  ------------------------ ------------------------------------------------------------

### [Boolean Expressions]

Boolean operations are also legal. (POSIX bc does NOT have boolean operations). The result of all boolean operations are 0 and 1 (for false and true) as in relational expressions. The boolean operators are:

  --------------------- -------------------------------------------------------------
  Boolean Expressions   Description
  `!expr`               The result is 1 if expr is 0.
  `expr && expr`        The result is 1 if both expressions are non-zero.
  `expr1 >= expr2`      The result is 1 if expr1 is greater than or equal to expr2.
  `expr1 == expr2`      The result is 1 if expr1 is equal to expr2.
  `expr1 != expr2`      The result is 1 if expr1 is not equal to expr2.
  --------------------- -------------------------------------------------------------

### [Special Variables]

There are a few more special expressions that are provided in bc. These have to do with user-defined functions and standard functions. They all appear as \"name(parameters)\". The [bc] command line provide four special variables with specific meaning and behavior on the arithmetic expression to be evaluated. The standard functions are:

  ------------------ ----------------------------------------------------------------------------------------------------------------------------------------------
  Special Variable   Description
  `scale`            Defines how some operations use digits after the decimal point. Default value is 0 unless bc is used with the -l option, then default is 20.
  `ibase`            Defines the conversion base for input numbers. Default is to use base 10.
  `obase`            Defines the conversion base four output numbers. Default is to use base 10.
  `last`             Contains the value of the last printed number. It is a GNU bc extension.
  ------------------ ----------------------------------------------------------------------------------------------------------------------------------------------

### [Special Expression]

GNU [bc] provide few special expressions, i.e. standard functions, that allows to perform common operations easily and make the language richer.

  ----------------------------------- ------------------------------------------------------------------------------------------------------------------------------------
  Standard functions !! Description
  `length ( expression )`             The sine of x, x is in radians.
  `read ( )`                          The read function (an extension) will read a number from the standard input, regardless of where the function occurs. Beware,
  `scale ( )`                         The value of the scale function is the number of digits after the decimal point in the expression.
  `sqrt ( expression )`               The value of the sqrt function is the square root of the expression. If the expression is negative, a run time error is generated.
  ----------------------------------- ------------------------------------------------------------------------------------------------------------------------------------

The value of the sqrt function is the square root of the expression. If the expression is negative, a run time error is generated.

`user `[`$`]`bc -l <<< "sqrt(3)i `

    1.73205080756887729352

## [Examples]

### [Convert Decimal to Hexadecimal]

Use [bc] to convert values from one number system to another. The command achieves that using two special variables - ibase (input base) and obase (output base). The variables define the conversion base for input and output numbers. The legitimate obase values range from 2 to 999, while legitimate ibase values range from 2 to 16.

For example, the following command converts 255 from base 10 to base 16:

`user `[`$`]`echo 'obase=16;255' |bc`

### [Decimal to Binary]

Using - ibase and obase, bc allows users to convert decimals to binary numbers. For example, the following command converts the number 12 from base 10 to base 2:

`user `[`$`]`echo '=2;12' |bc`

### [Declare Variables]

Use shell variables with bc to store a value in a variable, which is useful when writing shell scripts.

`user `[`$`]`VAR=10 ; echo "$VAR^2" |bc`

### [Specify Input Files]

Using bc with files allows users to repeat complex calculations multiple times. To provide the input from a file or multiple files, specify the file path when running the bc command. The file must be a text file readable by bc. Multiple files are supported.

For example, the following file contains several lines of simple mathematical operations, as shown in the cat command output:

`user `[`$`]`bc -l <<< $(printf '%s\n%s\n' 10+10 100*100 1000-900 1000+9000`

### [Fahrenheit to Celsius]

Create a shell script to reuse an existing calculation. For example, create a simple Fahrenheit to Celsius temperature conversion script

[FILE] **`fahr2cels.bc`Fahrenheit to Celsius temperature conversion**

    #!/usr/bin/bc -q

    scale=2
    print "\nConvert Fahrenheit degrees to Celsius\n\n"
    print "Enter temperature in Fahrenheit: " ; fah = read()
    print "\n"
    print "The equivalent Temperature in Celsius is: "
    (fah - 32.0) * 5.0 / 9.0
    quit

### [][Calculate π]

The number Pi *π* is always equal to the circumference divided by the diameter of a circle. So, use the [bc] math library with the arctangent function of 1 and multiply it by 4 to get the Pi value.

`user `[`$`]`pi=$(echo "scale=50; 4*a(1)" | bc -l) `

`user `[`$`]`echo $pi `

    3.14159265358979323846264338327950288419716939937508

It is also possible to write it in the following way in a [bc] script

`user `[`$`]`bc -l <<< "scale=5000; 4*a(1)"`

### [Arithmetic Calculator]

[FILE] **`simple_bc_calculator.bc`A Simple Arithmetic Calculator using bc**

    #!/usr/bin/bc -q

    scale=2
    print "\nA Simple Arithmetic Calculator using bc\n"
    print "  Enter x and y value then select an operation.\n\n"

    while (1)
    quit

Below is output of running the previous [bc] shell script in a bash terminal.

`user `[`$`]`bc -q bash_simple_bc_calculator.bc `

    A Simple Arithmetic Calculator using bc
     Enter x and y value then select an operation.

    x=? 51
    y=? 23
    Choose an operation: addition (1),  subtraction (2), multipltication (3), division (4) 3
    Multiplication: 51*23=1173

## [Removal]

### [Unmerge]

Uninstall [[[sys-devel/bc]](https://packages.gentoo.org/packages/sys-devel/bc)[]]:

`root `[`#`]`emerge --ask --depclean --verbose sys-devel/bc`

## [See also]

-   [dc](https://wiki.gentoo.org/wiki/Dc "Dc") - is a robust Reverse Polish Notation (RPN) based desktop calculator
-   [sc-im](https://wiki.gentoo.org/wiki/Sc-im "Sc-im") --- a terminal-based spreadsheet and calculator with [[vim](https://wiki.gentoo.org/wiki/Vim "Vim")]-like key bindings
-   [ledger](https://wiki.gentoo.org/wiki/Ledger "Ledger") --- a scriptable double-entry accounting system for the command-line