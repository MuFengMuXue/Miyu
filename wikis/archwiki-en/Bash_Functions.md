# Bash/Functions

Bash also supports functions. Add the functions to , or a separate file which is sourced from . More Bash function examples can be found in BBS#30155.

## Display error codes
To set  to intercept a non-zero return code of the last program run:

 EC() {
 	echo -e '\e$?'\e[m\n'
 }
 trap EC ERR

## Compile and execute a C source on the fly
The following function will compile (within the  directory) and execute the C source argument on the fly (and the execution will be without arguments). And finally, after program terminates, will remove the compiled file.

{{bc|# Compile and execute a C source on the fly
csource() {
	 $1     || { echo "Missing operand" >&2; return 1; }
	 -r $1  || { printf "File %s does not exist or is not readable\n" "$1" >&2; return 1; }
	local output_path=${TMPDIR:-/tmp}/${1##*/};
	gcc "$1" -o "$output_path" && "$output_path";
	rm "$output_path";
	return 0;
}}}

## Extract
The following function will extract a wide range of compressed file types. Use it with the syntax

{{bc|
extract() {
    local c e i

    (($#)) || return

    for i; do
        c=''
        e=1

        if  ! -r $i ; then
            echo "$0: file is unreadable: \`$i'" >&2
            continue
        fi

        case $i in
            *.t@(gz|lz|xz|b@(2|z?(2))|a@(z|r?(.@(Z|bz?(2)|gz|lzma|xz|zst)))))
                   c=(bsdtar xvf);;
            *.7z)  c=(7z x);;
            *.Z)   c=(uncompress);;
            *.bz2) c=(bunzip2);;
            *.exe) c=(cabextract);;
            *.gz)  c=(gunzip);;
            *.rar) c=(unrar x);;
            *.xz)  c=(unxz);;
            *.zip) c=(unzip);;
            *.zst) c=(unzstd);;
            *)     echo "$0: unrecognized file extension: \`$i'" >&2
                   continue;;
        esac

        command "${c[@}" "$i"
        ((e = e || $?))
    done
    return "$e"
}
}}

Another way to do this is to install a specialized package, see Archiving and compression tools#Convenience tools.

## cd and ls in one
Very often changing to a directory is followed by the  command to list its contents. Therefore it is helpful to have a second function doing both at once.
In this example we will name it  (change list) and show an error message if the specified directory does not exist.

{{bc|
cl() {
	local dir="$1"
	local dir="${dir:=$HOME}"
	if  -d "$dir" ; then
		cd "$dir" >/dev/null; ls
	else
		echo "bash: cl: $dir: Directory not found"
	fi
}
}}

Of course the ls command can be altered to fit your needs, for example .

## Simple note taker
{{bc|
note () {
    # if file doesn't exist, create it
    if  ! -f $HOME/.notes ; then
        touch "$HOME/.notes"
    fi

    if ! (($#)); then
        # no arguments, print file
        cat "$HOME/.notes"
    elif  "$1" == "-c" ; then
        # clear file
        printf "%s" > "$HOME/.notes"
    else
        # add all arguments to file
        printf "%s\n" "$*" >> "$HOME/.notes"
    fi
}
}}

## Simple task utility
Inspired by #Simple note taker

{{bc|
todo() {
    if  ! -f $HOME/.todo ; then
        touch "$HOME/.todo"
    fi

    if ! (($#)); then
        cat "$HOME/.todo"
    elif  "$1" == "-l" ; then
        nl -b a "$HOME/.todo"
    elif  "$1" == "-c" ; then
        > $HOME/.todo
    elif  "$1" == "-r" ; then
        nl -b a "$HOME/.todo"
        eval printf %.0s- '{1..'"${COLUMNS:-$(tput cols)}"\}; echo
        read -p "Type a number to remove: " number
        sed -i ${number}d $HOME/.todo "$HOME/.todo"
    else
        printf "%s\n" "$*" >> "$HOME/.todo"
    fi
}
}}

## Calculator
 calc() {
     echo "scale=3;$@" | bc -l
 }

## IP info
Detailed information on an IP address or hostname in bash via https://ipinfo.io:

 ipif() {
     if grep -P "((1-9\d{0,2})\.){3}(?2)" /dev/null | sort -hr
 }
