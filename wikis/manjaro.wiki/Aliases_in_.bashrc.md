Other languages:

[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Aliases_in_.bashrc/tr ".bashrc'deki takma adlar (100% translated)") • ‎[português do Brasil](//wiki.manjaro.org/index.php?title=Aliases_in_.bashrc/pt-br "Aliases no .bashrc (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Aliases_in_.bashrc/ru "Альясы в .bashrc (100% translated)")

## Contents

-   [[1] [What\'s a bashrc? What\'s a alias?]](#What.27s_a_bashrc.3F_What.27s_a_alias.3F)
-   [[2] [Backup your current \~/.bashrc]](#Backup_your_current_.7E.2F.bashrc)
-   [[3] [Note]](#Note)
-   [[4] [Aliases Examples]](#Aliases_Examples)
    -   [[4.1] [Standard syntax]](#Standard_syntax)
    -   [[4.2] [For updating your system]](#For_updating_your_system)
    -   [[4.3] [For editing commonly used files]](#For_editing_commonly_used_files)
    -   [[4.4] [To update GRUB]](#To_update_GRUB)
-   [[5] [Creating Bash Aliases with Arguments (Bash Functions)]](#Creating_Bash_Aliases_with_Arguments_.28Bash_Functions.29)
-   [[6] [Keeping bash alias in a different file]](#Keeping_bash_alias_in_a_different_file)
-   [[7] [Conclusion]](#Conclusion)
-   [[8] [See Also]](#See_Also)

## [][What\'s a bashrc? What\'s a alias?]

-   **.bashrc** is the *configuration file* for bash, a linux shell/command interpreter.
-   An **alias** is a *substitute for a (complete) command*. It can be thought of as a shortcut.
-   **.bashrc** is found in the *home folder* of a user ( \~ ) . It is a hidden file, to see it show hidden files in your file manager or use **ls -a**

## [][Backup your current \~/.bashrc]

It can be useful to backup the \~/.bashrc before editing it, as it allows one to be able to easily recover from the unexpected. To make a backup of your current .bashrc . Open a terminal and execute:

[user \$ ][ cp \~/.bashrc \~/.bashrc.bak [COPY TO CLIPBOARD]]

\

The original .bashrc can be restored with by executing

[user \$ ][ cp -i \~/.bashrc.bak \~/.bashrc [COPY TO CLIPBOARD]]

\

## [Note]

Any changes made to the \~/.bashrc will have no effect on any currently open terminal windows. To test newly updated changes in your \~/.bashrc open a new terminal or use the command:

[user \$ ][ source \~/.bashrc [COPY TO CLIPBOARD]]

\

## [Aliases Examples]

Aliases can turn a complex command string into a simple custom made command that one can type in the Terminal.

### [Standard syntax]

Creating aliases in bash is very straight forward. The syntax is as follows:

\~/.bashrc

    ...
    alias alias_name="command_to_run"
    ...

### [For updating your system]

To upgrade the system via pacman, the command used is

[user \$ ][ sudo pacman -Syu [COPY TO CLIPBOARD]]

\

This can be aliased in \~/.bashrc with

\~/.bashrc

    ...
    alias pacup="sudo pacman -Syu"
    ...

To upgrade packages installed from the AUR via pamac, the command used is

[user \$ ][ pamac upgrade \--aur [COPY TO CLIPBOARD]]

\

This can be aliased with

\~/.bashrc

    ...
    alias aup="pamac upgrade --aur"
    ...

### [For editing commonly used files]

To edit **\~/.bashrc** itself and automatically reload bash configuration file (so that changes made to .bashrc can be implemented in current terminal session)

\~/.bashrc

    ...
    alias bashrc="nano ~/.bashrc && source ~/.bashrc"
    ...

To edit **/etc/fstab**

\~/.bashrc

    ...
    alias fstab="sudo nano /etc/fstab"
    ...

To edit **/etc/default/grub**

\~/.bashrc

    ...
    alias grub="sudo nano /etc/default/grub"
    ...

### [To update GRUB]

To update your grub bootloader using the **sudo update-grub**

\~/.bashrc

    ...
    alias grubup="sudo update-grub"
    ...

## [][Creating Bash Aliases with Arguments (Bash Functions)]

Sometimes you may need to create an alias that accepts one or more arguments. That's where bash functions come in handy.

The syntax for creating a bash function is very easy. They can be declared in two different formats:

\~/.bashrc

    ...
    function_name ()
    ...

or

\~/.bashrc

    ...
    function function_name
    ...

To pass any number of arguments to the bash function simply, put them right after the function's name, separated by a space. The passed parameters are \$1, \$2, \$3, etc., corresponding to the position of the parameter after the function's name. The \$0 variable is reserved for the function name.

Let's create a simple bash function which will create a directory and then navigate into it:

\~/.bashrc

    ...
    mkcd ()

    ...

Now instead of using mkdir to create a new directory and then cd to move into that directory , you can simply type:

[user \$ ][ mkcd new_directory [COPY TO CLIPBOARD]]

\

## [Keeping bash alias in a different file]

Bash allows you to add local aliases in your \~/.bashrc file. To do this create a file called \~/.bash_aliases and add these contents in your \~/.bashrc file:

\~/.bashrc

    ...
    if [ -e $HOME/.bash_aliases ]; then
        source $HOME/.bash_aliases
    fi
    ...

Now you can add any aliases in your \~/.bash_aliases file and then load them into your Bash session with the source \~/.bashrc command.

## [Conclusion]

This list is not comprehensive. Almost anything that is commonly used can be shortened with an alias

## [See Also]

[Bash documentation](https://www.gnu.org/software/bash/manual/html_node/index.html) [ArchWiki](https://wiki.archlinux.org/title/bash#Aliases)