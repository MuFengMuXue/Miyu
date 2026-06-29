# Bash/Prompt customization

Bash has several prompts which can be customized to increase productivity, aesthetic appeal, and nerd cred.

## Prompts
Bash has five prompt strings that can be customized:

*  is displayed after each command, before any output.
*  is the primary prompt which is displayed before each command, thus it is the one most people customize.
*  is the secondary prompt displayed when a command needs more input (e.g. a multi-line command).
*  is not very commonly used. It is the prompt displayed for Bash's  built-in which displays interactive menus. Unlike the other prompts, it does not expand Bash escape sequences. Usually you would customize it in the script where the  is used rather than in your .
*  is also not commonly used. It is displayed when debugging bash scripts to indicate levels of indirection. The first character is repeated to indicate deeper levels.

All of the prompts are customized by setting the corresponding variable to the desired string (usually in ), for example

 PS2='> '

## Techniques
While one can simply set their prompt to a plain string, there are a variety of techniques for making the prompt more dynamic and useful.

## Bash escape sequences
When printing the prompt string, Bash looks for certain backslash-escaped characters and will expand them into special strings. For example,  is expanded into the current username and  is expanded to the current time. So a PS1 of  would be printed like .

See the man page  or the Bash reference manual for a complete list of escape sequences.

## Terminfo escape sequences
Aside from the escape characters recognized by Bash, most terminals recognize special escape sequences that affect the terminal itself rather than printing characters. For example they might change the color of subsequent printed characters, move the cursor to an arbitrary location, or clear the screen. These escape sequences can be somewhat illegible and can vary from terminal to terminal, so they are documented in the terminfo database. To see what capabilities your terminal supports, run

 $ infocmp

The capability names (the part before the =) can be looked up in  for a description of what they do. For example,  sets the foreground color of whatever text is printed after it. To get the escape code for a capability, you can use the  command. For example

 $ tput setaf 2

Prints the escape sequence to set the foreground color to green.

To practically incorporate these capabilities into your prompt, you can use Bash's command substitution and string interpolation. For example

{{bc|
GREEN="\setaf 2)\"
RESET="\sgr0)\"

PS1="${GREEN}my prompt${RESET}> "
}}

my prompt>

## ANSI escape sequences
Unfortunately, valid ANSI escape sequences may be missing from your terminal's terminfo database. This is especially common with escape sequences for newer features such as 256 color support. In that case you cannot use tput, you must input the escape sequence manually.

See Wikipedia:ANSI escape code for examples of escape sequences. Every escape sequence starts with a literal escape character, which you can input using the Bash escape sequence . So for example, sets the background to a peachy color (if you have 256 color support) and  moves the cursor near the top-left corner of the screen.

In cases where Bash escape sequences are not supported (such as PS3) you can get a literal escape character using Bash's printf builtin:

 ESC=$(printf "\e")
 PEACH="$ESC=== Embedding commands ===

If you want to add the output of some command to your prompt, you might be tempted to use command substitution. For example, to add the amount of free memory to your prompt you might try:
{{hc|1=PS1="$(awk '/MemFree/{print $2}' /proc/meminfo) prompt > "|2=53718 prompt >
53718 prompt >
53718 prompt >}}

But this does not work; the amount of memory shown is the same every time! This is because the command is run once, when PS1 is first set, and never again. The trick is to simply prevent the substitution either by escaping the  or by defining it in single quotes — either way it will be substituted when the prompt is actually displayed:

 PS1="\$(awk '/MemFree/{print \$2}' /proc/meminfo) prompt > "
 # or
 PS1='$(awk "/MemFree/{print \$2}" /proc/meminfo) prompt > '

To prevent long commands from making your PS1 huge, you can define functions:

{{bc|1=
free_mem()
{
    awk '/MemFree/{print $2}' /proc/meminfo
}

PS1='$(free_mem) prompt > '
}}

## PROMPT_COMMAND
If the  variable or array is set, it will be evaluated right before PS1 is displayed. This can be used to achieve quite powerful effects. For example it can reassign PS1 based on some condition, or perform some operation on your Bash history every time you run a command.

## Escapes between command input and output
You can affect your input text in Bash by not resetting the text properties at the end of your PS1. For example, inserting  at the end of your PS1 will make your typed commands blink. However this effect will also continue through the command's output since the text properties are not reset when you hit Enter.

In order to insert escape sequences after you type a command but before the output is displayed, you can set PS0. Alternatively, you can trap Bash's DEBUG signal, which is sent right before each command is executed:

 $ trap 'tput sgr0' DEBUG

## Customizing root prompts
To ensure that you know when you are running as root, you can customize your root prompt to make it clearly stand out (perhaps blinking red?). This is done by customizing the Bash prompt as usual but in root's home directory, . Start off by copying the skeleton files  and  to , then edit  as desired.

## Examples
## Colors
To see the full range of colors your terminal supports, you can use a simple loop with tput (change  to  for text foregrounds):

{{bc|
for C in {0..255}; do
    tput setab $C
    echo -n "$C "
done
tput sgr0
echo
}}

If that does not work (and you cannot fix it by setting the correct TERM value), you can test the different manual escape sequences:

{{bc|
# standard colors
for C in {40..47}; do
    echo -en "\e[${C}m$C "
done
# high intensity colors
for C in {100..107}; do
    echo -en "\e[${C}m$C "
done
# 256 colors
for C in {16..255}; do
    echo -en "\e[48;5;${C}m$C "
done
echo -e "\e(B\e[m"
}}

To change the manual escapes from background to foreground, the standard color range is , the high intensity range is , and the 48 should be changed to 38 for 256 colors.

## Common capabilities
The following terminfo capabilities are useful for prompt customization and are supported by many terminals. #1 and #2 are placeholders for numeric arguments.

{| class="wikitable"
! Capability !! Escape sequence !! Description
|-
!colspan="3"| Text attributes
|-
| blink || \e[5m || blinking text on
|-
| bold || \e[1m || bold text on
|-
| dim || \e[2m || dim text on
|-
| rev || \e[7m || reverse video on (switch text/background colors)
|-
| sitm || \e[3m || italic text on
|-
| ritm || \e[23m || italic text off
|-
| smso || \e[7m || highlighted text on
|-
| rmso || \e[27m || highlighted text off
|-
| smul || \e[4m || underlined text on
|-
| rmul || \e[24m || underlined text off
|-
| setab #1 || \e[4#1m || set background color #1 (0-7)
|-
| setaf #1 || \e[3#1m || set text color #1 (0-7)
|-
| sgr0 || \e(B\e[m || reset text attributes
|-
!colspan="3"| Cursor movement
|-
| sc || \e7 || save cursor position
|-
| rc || \e8 || restore saved cursor position
|-
| clear || \e[H\e[2J || clear screen and move cursor to top left
|-
| cuu #1 || \e[#1A || move cursor up #1 rows
|-
| cud #1 || \e[#1B || move cursor down #1 rows
|-
| cuf #1 || \e[#1C || move cursor right #1 columns
|-
| cub #1 || \e[#1D || move cursor left #1 columns
|-
| home || \e[H || move cursor to top left
|-
| hpa #1 || \e[#1G || move cursor to column #1
|-
| vpa #1 || \e[#1d || move cursor to row #1, first column
|-
| cup #1 #2 || \e[#1;#2H || move cursor to row #1, column #2
|-
!colspan="3"| Removing characters
|-
| dch #1 || \e#1P || remove #1 characters (like backspacing)
|-
| dl #1 || \e#1M || remove #1 lines
|-
| ech #1 || \e#1X || clear #1 characters (without moving cursor)
|-
| ed || \eE[J || clear to bottom of screen
|-
| el || \e[K || clear to end of line
|-
| el1 || \e[1K || clear to beginning of line
|}

## Visualizing exit codes
Using the same trick from embedding commands you can delay the interpolation of special Bash variables like . So the following prompt shows the exit code of the previous command:

 PS1="\$? > "
 # or
 PS1='$? > '

0 > true0 > false1 >

This can be made more interesting using conditionals and functions:

{{bc|
exitstatus()
{
    if  $? == 0 ; then
        echo ':)'
    else
        echo 'D:'
    fi
}
PS1='$(exitstatus) > '
}}

:) > true:) > falseD: >

## Positioning the cursor
It is possible to move the cursor around the screen inside of PS1 to make different parts of the prompt appear in different locations. However, to ensure that Bash positions the cursor and output in the right position, you must move the cursor back to the original position after you are done printing elsewhere. This can be done using the tput capabilities  and  to save and restore the cursor position. The general pattern for a prompt that moves the cursor is

 PS1="\[$(tput sc; cursor-moving code) positioned prompt stuff $(tput rc)\ normal prompt stuff"

where the entire block of repositioned prompt is wrapped in  to prevent Bash from counting it as part of the regular prompt.

## Right-justified text
The simplest way to print text on the right side of the screen is to use printf

{{bc|1=
rightprompt()
{
    printf "%*s" $COLUMNS "right prompt"
}

PS1='\sc; rightprompt; tput rc)\left prompt > '
}}

left prompt > right prompt

This creates a right-justified variable-sized field  and sets its size to the current number of columns of the terminal .

## Arbitrary positioning
The  capability moves the cursor to a specific position on the screen, for example  moves the cursor to line 20, column 5 (where 0 0 is the top left corner). , , , and  (up, down, forward, back) move the cursor relative to its current position. For example  moves the cursor 10 characters to the right. You can use the  and  variables in the arguments to move the cursor relative to the bottom and right edges. For example, to move 10 lines and 5 columns away from the bottom right corner:

 $ tput cup $((LINES - 11)) $((COLUMNS - 6))

## Customizing the terminal window title
The terminal window title can be customized in much the same way as the prompt: by printing escape sequences in the shell. Thus it is common for users to include window title customizations in their prompt. Although this is technically a feature of xterm, many modern terminals support it. The escape sequence to use is  where  and  are the escape and bell characters. Using #Bash escape sequences, changing the title in your prompt looks like

 PS1='\title''\a\prompt > '

Of course your window title string can include output from embedding commands or variables such as , so that the title changes with each command.
