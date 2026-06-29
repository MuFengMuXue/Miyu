[[]][Package information](https://packages.gentoo.org/packages/sys-devel/dc)

[[]][Wikipedia](https://en.wikipedia.org/wiki/https://en.wikipedia.org/wiki/Dc_(computer_program) "wikipedia:https://en.wikipedia.org/wiki/Dc (computer program)")

**[dc]** is a robust Reverse Polish Notation (RPN) based desktop calculator. RPN, a notation system established in 1920 by Jan Lukasiewicz, enables the execution of mathematical expressions without requiring parentheses or brackets. It\'s straightforward to learn and presents a superior method to conventional algebraic calculation.

RPN pocket calculators became popular with the release of HP calculators. HP spearheaded the application of this computation method, introducing it with their inaugural calculator in 1968. These HP calculators have garnered a loyal fanbase, with plentiful resources available for enthusiasts. Many of these calculators have turned into collectors\' items, often selling for much higher than their initial price. This article delves into an array of RPN desktop calculators available for Linux, encompassing both HP emulators and independent RPN calculators.

## Contents

-   [[1] [Features of dc]](#Features_of_dc)
-   [[2] [Installation]](#Installation)
-   [[3] [Why Use RPN?]](#Why_Use_RPN.3F)
-   [[4] [RPN Calculation Examples]](#RPN_Calculation_Examples)
    -   [[4.1] [Using dc]](#Using_dc)
    -   [[4.2] [Reading and Performing Calculations from a File]](#Reading_and_Performing_Calculations_from_a_File)
    -   [[4.3] [Advanced Examples]](#Advanced_Examples)
-   [[5] [Performing Basic Arithmetic Operations]](#Performing_Basic_Arithmetic_Operations)
    -   [[5.1] [Multiplication]](#Multiplication)
    -   [[5.2] [Addition]](#Addition)
    -   [[5.3] [Subtraction]](#Subtraction)
    -   [[5.4] [Division]](#Division)
-   [[6] [Conditionals]](#Conditionals)
    -   [[6.1] [Conditionals and Loops]](#Conditionals_and_Loops)
-   [[7] [Registers]](#Registers)
-   [[8] [Extra]](#Extra)
-   [[9] [See also]](#See_also)
-   [[10] [Resources]](#Resources)

## [Features of dc]

-   **Advanced Mathematical Functions**: Besides facilitating basic arithmetic operations, [dc] incorporates advanced mathematical functions like trigonometric, exponential, logarithmic, and power functions.

<!-- -->

-   **Control Structures**: [dc] accommodates simple control structures such as loops and conditionals, making it possible to conduct complex calculations and automate repetitive tasks.

<!-- -->

-   **RPN Entry Method**: [dc] employs a stack-based approach for computations. The top two elements of the stack serve as operands for mathematical operations, eliminating the need for explicit grouping and simplifying complex computations.

<!-- -->

-   **Floating-Point and Integer Arithmetic**: [dc] enables calculations with both precise decimal values (floating-point arithmetic) and whole numbers (integer arithmetic).

## [Installation]

Use the following command to install dc:

`root `[`#`]`emerge -av app-alternatives/bc-0`

## [][Why Use RPN?]

RPN calculators use a stack-based method where mathematical operations are executed immediately on the lower level of the stack. The stack operates as a storage space for intermediate results, needed for further formula evaluation. A significant advantage of RPN calculators is the absence of brackets or parentheses.

For instance, let\'s consider a calculation: `((3 + 1)^2 + 1) * 4`. To perform this on an RPN calculator, follow these steps:

1.  Enter the number [3] and press [Enter].
2.  Enter the number [1] and press [+]. You will instantly see the result, [4].
3.  Enter the number [2] and press [\^]. The result, [16], is immediately displayed.
4.  Enter the number [1] and press [+]. You\'ll see the result, [17].
5.  Enter the number [4] and press [\*]. The final result, [68], is displayed.

With RPN, you only needed nine keystrokes for this calculation, and you could see all intermediate results. This aligns closely with how you would mentally evaluate a formula without a calculator, making the RPN calculator a natural choice.

Compared to an algebraic calculator where you input the formula as written, requiring twelve keystrokes without visibility of intermediate results, RPN offers:

-   Time and keystroke efficiency: Without parentheses in calculations, RPN aligns with how you learned math on paper.
-   Visibility of intermediate results: This makes it easy to spot and correct errors, following the flow of calculation effortlessly.
-   User-defined priority of operators: This makes entry errors more apparent as compared to algebraic calculators where errors might go unnoticed until evaluation of an entire subexpression.

In conclusion, RPN offers an intuitive and efficient approach to performing calculations. RPN calculators like [dc] operate on these principles, offering a streamlined and intuitive calculation experience.

## [RPN Calculation Examples]

Here are several examples of performing Reverse Polish Notation (RPN) calculations using different tools:

### [Using dc]

To perform addition in dc, you can use the following commands:

[CODE] **Example: Addition using dc**

    dc <<< '5 3 + p q'

[CODE] **Example: Addition using piping**

    echo '5 3 + p q' | dc

Both commands will output the result of the addition, which is 8.

To perform multiplication in dc, you can use the following command:

### [Reading and Performing Calculations from a File]

Assuming you have a file named \`input.txt\` containing the following numbers:

    2
    9
    4
    6
    8
    3
    1
    7
    5
    10

You can read and perform calculations using dc as follows:

`user `[`$`]`dc -f input.txt -e '10 * p'`

In this command, the [-f] option is used to specify the input file (input.txt), and the [-e] option is used to provide the dc expression to be executed. In this example, the expression [10 \* p] is used to multiply the top two numbers on the stack and print the result.

The output of the command will be the result of multiplying the numbers specified in [input.txt], which is 100.

Note: Adjust the file path and expression according to your specific setup and desired calculations.

Feel free to modify the dc expressions and input file as needed to perform different calculations based on your requirements.

### [Advanced Examples]

[CODE] **Example: Exponentiation using dc**

    dc -e '2 3 ^ p q'

This command calculates 2 raised to the power of 3, which is 8.

[CODE] **Example: Division using dc**

    dc -e '10 2 / p q'

This command performs division, dividing 10 by 2, resulting in 5.

[CODE] **Example: Square Root using dc**

    dc -e '16 v p q'

This command calculates the square root of 16, which is 4.

These advanced examples demonstrate the power and versatility of the dc tool for performing complex mathematical operations. Feel free to explore further and adapt the expressions to perform various calculations based on your specific mathematical requirements.

\

## [Performing Basic Arithmetic Operations]

Here are some basic examples, but [dc] allows you to perform complex calculations by pushing more numbers and operators onto the stack in the correct order. Always *ensure* to understand these commands before execution, as [dc] follows Reverse Polish Notation for calculations.

You can perform basic arithmetic operations like addition, subtraction, multiplication, and division in [dc].

### [Multiplication]

To multiply [4] and [5], follow the procedure:

`user `[`$`]`dc -e '4 5 * p'`

The [\*] operation multiplies the top two numbers on the stack, and [p] prints the result.

### [Addition]

To add [7] and [3]:

`user `[`$`]`dc -e '7 3 + p'`

The [+] operation adds the top two numbers on the stack, and [p] prints the result.

### [Subtraction]

To subtract [3] from [7]:

`user `[`$`]`dc -e '7 3 - p'`

The [-] operation subtracts the top number on the stack from the next number, and [p] prints the result.

### [Division]

To divide [10] by [2]:

`user `[`$`]`dc -e '10 2 / p'`

The [/] operation divides the second number on the stack by the top number, and [p] prints the result.

## [Conditionals]

In desktop calculators, conditionals allow you to perform different actions based on certain conditions. A macro mechanism is often used to provide this functionality.

One common conditional command is [=r], which pops two values from the stack and executes the macro stored in register [r] only if they are equal. For example, the following code prints the string \"equal\" only if the top two values on the stack are of equal value:

-   [\>] - Executes the specified macro if the top two values on the stack are in descending order (the first value is greater than the second).
-   [!\<] - Executes the specified macro if the top two values on the stack are not in descending order (the first value is not greater than the second).
-   [\<] - Executes the specified macro if the top two values on the stack are in ascending order (the first value is less than the second).
-   [!\>] - Executes the specified macro if the top two values on the stack are not in ascending order (the first value is not less than the second).
-   [!=] - Executes the specified macro if the top two values on the stack are not equal.

### [Conditionals and Loops]

In dc, you can execute a macro stored in a register and perform conditional execution using certain commands. Here are some examples of conditionals and loops in dc:

**Conditional Execution:** dc can execute a macro stored in a register conditionally using the [\>a] command, where **a** is the register name. It executes the macro stored in register **a** if the top of the stack is greater than the second element of the stack.

**Recursive Macros and Loops:**

dc allows including a macro (string) within another macro, and as dc relies on a stack, recursive macros can be used. Here\'s an example that demonstrates recursion and loops:

[CODE] **Recursive Macro and Loop Example**

    dc << EOF
    [ [Loop End] p      # our macro starts by printing Loop End
      lLx            ]  # and then executes the macro in L
    sL                  # we store it in the register L
    lLx                 # and finally execute it.
    EOF

Additionally, loops can be implemented in dc using conditional execution. Here\'s an example of a loop that decrements an index and prints it until it reaches zero:

[CODE] **Loop Example**

    dc << EOF
    [ li        # put our index i on the stack
      p         # print it to see what's going on
      1 -       # decrement the index by one
      si        # store decremented index (i=i-1)
      0 li >L   # if i > 0 then execute L
    ] sL        # store our macro with the name L

    5 si        # initialize the index with the value 5
    lLx         # start the loop
    EOF

Result:

    5
    4
    3
    2
    1

In the above example, the index **i** is decremented by one in each iteration until it reaches zero. The macro [L] is recursively executed until the condition [i \> 0] is no longer met.

** Tip**\
When writing dc code, it\'s common to remove extra spaces, newlines, and comments to make the code more concise.

## [Registers]

Registers in dc provide a convenient way to store and retrieve values. According to the GNU dc manual, dc has at least 256 registers, which may vary based on the range of unsigned char. Working with registers is relatively straightforward.

To store a value in a register, you can use the following syntax:

[CODE] **Storing a Value in a Register**

    dc <<EOF
    42 # put 42 on the stack
    sb # remove it from the stack (s) and put it in register 'b'
    17 # put 17 on the stack
    lb # read (l) the value of register 'b' and push it on the stack
    -p # subtract the two values and print the result
    EOF

In the above example, the value [42] is placed on the stack, and the [sb] command stores it in register **b**. Then, [17] is placed on the stack, and the *lb* command retrieves the value from register [b] and pushes it onto the stack. Finally, the [-p] command subtracts the two values on the stack and prints the result.

Registers can hold more than a single value; each register acts as its own stack. Consider the following example:

[CODE] **Working with Register Stacks**

    dc <<EOF
    31sb # store 31 in register 'b'
    10Sa # with a capital S, 10 is removed from the main stack and pushed onto the 'b' stack
    lbp # prints 10, the value at the top of the 'b' stack
    lbp # still prints 10
    Lbp # prints 31 as well, but with a capital L; it pushes the value from 'b' to the main stack
    lbp # prints 31, which is now at the top of the stack
    EOF

In this example, [31] is stored in register **b** using the key [31sb]. Then, with [10Sa], the value [10] is removed from the main stack and pushed onto the stack. The [lbp] command, using the key [lbp], prints the top value of the **b** stack, which is [10]. The subsequent [lbp] commands continue to print [10]. However, when using [Lbp], with the key [Lbp], the value from the **b** stack is pushed to the main stack and then printed, resulting in [10]. Finally, after executing [lbp], with the key [lbp], the top value of the main stack is [31], which is also printed.

## [Extra]

In order to showcase the expertise and understanding behind this wiki, a captivating puzzle has been incorporated. This puzzle serves as a demonstration of the comprehensive knowledge possessed by the contributors who have created this wiki with proper permissions. It exemplifies their proficiency in the realm of computing and programming.

As an intriguing addition, an encoded command has been provided. This command, written in the dc language, encompasses a complex calculation. It utilizes the command:

`user `[`$`]`dc -e '16i[q]sa[ln0=aln100%Pln100/snlbx]sb0A0D2178756E694C206F6F746E65472079622064657265776F50snlbxq'`

While the command\'s exact purpose remains a mystery, it demonstrates the depth of knowledge and skill possessed by the individuals involved in this project.

It showcases the unique nature of this wiki, created by knowledgeable individuals who possess a profound understanding of its inner workings.

If you successfully solve the puzzle, we invite you to share the breakdown of the solution! Your contribution will not only enrich the collective knowledge but also highlight your own expertise. Feel free to unravel the mysteries and reveal the secrets behind the command.

## [See also]

-   [bc](https://wiki.gentoo.org/wiki/Bc "Bc") --- arbitrary-precision fixed-point mathematical scripting language
-   [sc-im](https://wiki.gentoo.org/wiki/Sc-im "Sc-im") --- a terminal-based spreadsheet and calculator with [[vim](https://wiki.gentoo.org/wiki/Vim "Vim")]-like key bindings
-   [ledger](https://wiki.gentoo.org/wiki/Ledger "Ledger") --- a scriptable double-entry accounting system for the command-line

## [Resources]

The original manual for the 1971 dc from Bell Labs is available at [http://cm.bell-labs.com/cm/cs/who/dmr/man12.ps](http://cm.bell-labs.com/cm/cs/who/dmr/man12.ps).