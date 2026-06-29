# Shell package guidelines

## Install
For users to change shells, the shell must appear in . Most shell packages have install scripts like below:

{{hc|shellname.install|
post_install() {
    grep -Fqx /bin/shellname /etc/shells  echo /bin/shellname >>/etc/shells
    grep -Fqx /usr/bin/shellname /etc/shells  echo /usr/bin/shellname >>/etc/shells
}

post_upgrade() {
    post_install
}

post_remove() {
    sed -i -r '/^(\/usr)?\/bin\/shellname$/d' etc/shells
}
}}

## Shell completions
Most shells provide a built in set of completions for a few common commands while also scanning at least one system directory for functions that may be supplied by other packages. The following table is a summary of where packages may place completion files and what the files should be named.

{| class="wikitable"
! Shell !! Directory !! File
|-
| Bash ||  ||
|-
| Elvish ||  ||
|-
| Fish ||  ||
|-
| Zsh ||  ||
|}

Other shells:

* Nushell provides some default completions, but does not have a system-wide directory where completions can be provided yethttps://github.com/nushell/nushell/issues/11337. For packages that generate Nushell completion functions, one solution would be to package them  and use a  function to print a tip for users to add a  statement to their configs.

## Shell functions or modules
{| class="wikitable"
! Shell !! Directory !! File
|-
| Elvish ||  ||
|-
| Fish ||  ||
|-
| Zsh ||  ||
|}
