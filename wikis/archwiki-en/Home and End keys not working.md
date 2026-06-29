# Home and End keys not working

A frequent problem in command line programs is that keys like Home and End do not work as expected. This is usually because the terminal emulator sends multi-character escape codes when such keys are pressed, which the running program (such as your shell) does not know how to interpret correctly. Usually this problem can be fixed by configuring the offending program to perform the correct action when receiving certain escape codes. Thus the solution varies from program to program.

First you should check the common culprits that can affect the behavior of many programs.

## TERM
The number one cause of broken keys is overriding the TERM environment variable to something that conflicts with your shell. All modern terminals are smart enough to set their own TERM variable, so before you go delving into program configurations ensure that you are not incorrectly overriding it (for example, in your ). Again, do not set TERM manually - let the terminal do it.

If you do not like the TERM value chosen by your terminal (e.g. 'xterm' when you want 'xterm-256color'), there is typically a way to configure your terminal to properly override it without changing the TERM variable.

For xterm and urxvt, it can be set in the X resources:

For GNU Screen, it can be set in :

For Tmux, it can be set in  (see tmux#Configuration):

## Shell prompt
Another possible reason for misbehaving Home and End keys is malformed custom shell prompt. The shell tries to calculate actual length of the prompt contained in  environment variable, but if  contains some escape sequences (e.g. for colored text), shell may assume that they are actual printable characters with non-zero length. This will obviously result in text rendering mistakes.

{{Expansion|The following instructions are Bash-specific. Add instructions for other shells, e.g. Zsh—{{ic|%{...%}}}.}}

To avoid that, you should enclose your non-printable stuff in  with  and  so that shell can understand that it is actually non-printable. For example, this line in your

 PS1="\e\e[34m\w \e[37m\$ \e[0m"

should become this:

 PS1="\[\e[32m\\u \\[\e[37m\\$ \\e[0m\"

For more info, please refer to Bash/Prompt customization.

## Readline
Many command line applications use the Readline library to read input. So properly configuring Readline can fix Home and End in many cases. Readline maintains mappings for more obscure keys in  and  for global and per-user mappings, respectively.

In the default , there are several lines that attempt to handle common Home/End escape codes:

 "\e[1~": beginning-of-line
 "\e[4~": end-of-line
 "\e[7~": beginning-of-line
 "\e[8~": end-of-line
 "\eOH": beginning-of-line
 "\eOF": end-of-line
 "\e[H": beginning-of-line
 "\e[F": end-of-line

If your keys are not working, it could be because your particular terminal sends escape codes not in this list. First you need to find out what escape codes are being sent. To see them, you can use a Readline command called "quoted-insert" or run the command  which outputs the value of a key verbatim. The default binding for quoted-insert is .

For example, you could give the following series of inputs in your terminal:
#
#
#
#
#

And get as output:

 ^1~ ^[[4~

The  indicates an escape character in your shell, so this means that your Home key has an escape code of  and you End key has an escape code of . Since these escape codes are not listed in the default Readline configuration, you will need to add them:

 "\e[1~": beginning-of-line
 "\e[4~": end-of-line

Note that Readline uses  to indicate an escape character.

## Terminfo
For programs that do not use Readline (e.g. ncurses), you can try editing your terminfo to change which escape codes are sent to the terminal for certain actions.

First save your existing terminfo to a file

 $ infocmp $TERM > terminfo.src

Then edit it to change the escape codes. For example change  and :

 khome=\E[1~, kend=\E[4~,

Then compile the new terminfo (which saves it to your  directory)

 $ tic terminfo.src

And lastly specify the new terminfo in your shell's [[environment variables:

 export TERMINFO=~/.terminfo

## Other applications
If the above steps do not resolve the issue, it is probably a program-specific problem rather than a system-wide one. You may have to consult the documentation for the given program on how to fix it. Below are fixes for common programs.

## Lynx
You can add key binds using the same quoted-insert characters as used for Readline, but use  to represent an escape character:

## URxvt/Rxvt
Add escape code binds to your X resources using the same escape sequence format as for Lynx:

Where  and  are the numpad  and  keys. These binds might also fix programs running within URxvt e.g. nano.

Another solution is to add the following section to

 # those two are for rxvt
 "\e[7~":beginning-of-line
 "\e[8~":end-of-line

## Zsh
Use the  database to set the correct key bindings, see Zsh#Key bindings.

## Less
## lesskey source file
For less version 582 and later, is it possible to use a plain text configuration file under  or  or .
