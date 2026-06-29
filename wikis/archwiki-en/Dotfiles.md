# Dotfiles

User-specific application configuration is traditionally stored in so called dotfiles (files whose filename starts with a dot). It is common practice to track dotfiles with a version control system such as Git to keep track of changes and synchronize dotfiles across various hosts. There are various approaches to managing dotfiles (e.g. directly tracking dotfiles in the home directory v.s. storing them in a subdirectory and symlinking/copying/generating files with a shell script or a dedicated tool). Apart from explaining how to manage dotfiles this article also contains a list of dotfile repositories from Arch Linux users.

## Tracking dotfiles directly with Git
The benefit of tracking dotfiles directly with Git is that it only requires Git and does not involve symlinks. The disadvantage is that host-specific configuration generally requires merging changes into multiple branches.

The simplest way to achieve this approach is to initialize a Git repository directly in your home directory and ignoring all files by default with a  pattern of . This method however comes with two drawbacks: it can become confusing when you have other Git repositories in your home directory (e.g. if you forget to initialize a repository you suddenly operate on your dotfile repository) and you can no longer easily see which files in the current directory are untracked (because they are ignored).

An alternative method without these drawbacks is the "bare repository and alias method" popularized on Ask Hacker News: What do you use to manage your dotfiles?, which just takes three commands to set up:

 $ git init --bare ~/.dotfiles
 $ alias dotfiles='/usr/bin/git --git-dir="$HOME/.dotfiles/" --work-tree="$HOME"'
 $ dotfiles config status.showUntrackedFiles no

Your dotfiles can be replicated on a new system like:

 $ git clone --bare  $HOME/.dotfiles
 $ alias dotfiles='/usr/bin/git --git-dir="$HOME/.dotfiles/" --work-tree="$HOME"'
 $ dotfiles checkout
 $ dotfiles config --local status.showUntrackedFiles no

* To do this without a remote repository, git bundles can be used. To create a git bundle called  on your source computer run:
:

:A bundle can be used similarly to a :
:

* In case of already having some stock dotfiles which might get overwritten, you'll encounter something similar to the following the error:
:

:You could use  which will rewrite the already existing files, or in a safer approach take a backup of all the files with the following script and then using :
:{{bc|
mkdir -p .dotfiles-backup && \
dotfiles checkout 2>&1 | egrep "\s+\." | awk {'print $1'} | \
xargs -I{} mv {} .dotfiles-backup/{}
}}

You can then manage your dotfiles with the created alias. If you are using Bash and would like bash completion for this alias, simply install , then add the alias and the following line to your .

 $ complete -F _complete_alias dotfiles

Another way to get completion in bash is adding the following to your  (taken from source /usr/share/bash-completion/completions/git
 __git_complete dotfiles __git_main

## Host-specific configuration
A common problem with synchronizing dotfiles across various machines is host-specific configuration.

With Git this can be solved by maintaining a master branch for all shared configuration, while each individual machine has a machine-specific branch checked out. Host-specific configuration can be committed to the machine-specific branch; when shared configuration is modified in the master branch, the per-machine branches need to be rebased on top of the updated master.

In configuration scripts like shell configuration files conditional logic can be used. For example, Bash scripts (i.e. ) can apply different configuration depending on the machine name (or type, custom variable, etc.):

 if  "$(hostname)" == "archlaptop" ; then
     # laptop specific commands here
 else
     # desktop or server machine commands
 fi

Similar can also be achieved with .Xresources.[https://jnrowe.github.io/articles/tips/Sharing_Xresources_between_systems.html

If you find rebasing Git branches too cumbersome, you may want to use a tool that supports file grouping, or if even greater flexibility is desired, a tool that does processing.

## Tools
;File grouping
:How configuration files can be grouped to configuration groups (also called profiles or packages).
;Processing
:Some tools process configuration files to allow them to be customized depending on the host.

{| class="wikitable sortable" style="text-align: center;"
! Name !! Package !! Written in !! File grouping !! Processing
|-
! dotbot
|  || Python || configuration file ||
|-
! chezmoi
|  || Go || directory-based || Go templates
|-
! dot-templater
|  || Rust || directory-based || custom syntax
|-
! toml-bombadil
|  || Rust || configuration file || tera
|-
! dotdrop
|  || Python || configuration file || Jinja2
|-
! dotfiles
|  || Python ||  ||
|-
! dotter
|  || Rust || configuration file || Handlebars
|-
! dt-cli
|  || Rust || configuration file || Handlebars
|-
! GNU Stow
|  || Perl || directory-based||
|-
! [https://github.com/lra/mackup Mackup
|  || Python || automatic per application ||
|-
! mir.qualia
|  || Python ||  || custom blocks
|-
! rcm
|  || Shell || directory-based (by host or tag) ||
|-
! yas-bdsm
|  || Shell || directory-based ||
|-
! dotbackup
|  || Rust || configuration file || Shell script
|-
! Nix home-manager
|  || Nix || flexible (configured in Nix language) || flexible (configured in Nix language)
|}

## Tools wrapping Git
If you are uncomfortable with Git, you may want to use one of these tools, which abstract the version control system away (more or less).

{| class="wikitable sortable" style="text-align:center;"
! Name !! Package !! Written in !! File grouping !! Processing
|-
! dotbare
|  || Shell () || repository-wise ||
|-
! dotgit
|  || Python || filename-based ||
|-
! homeshick
|  || Bash || repository-wise ||
|-
! homesick
|  || Ruby || repository-wise ||
|-
! Pearl
|  || Python || repository-wise ||
|-
! vcsh
|  || Shell || repository-wise ||
|-
! yadm(1)
|  || Shell || filename-based(by class/OS/distro/hostname/user)||Built-in templates/Jinja2/ESH[https://yadm.io/docs/templates(optional)
|-
! dfm
|  || Perl || repository-wise ||
|}

# Supports encryption of confidential files with GPG or OpenSSL. == User repositories ==

{| class="wikitable sortable" style="text-align:center"
! Author || Shell (Shell framework) || WM / DE || Editor || Terminal || Multiplexer || Audio || Monitor || Mail || IRC || File Manager || RSS reader
|-
! [https://github.com/adamperkowski/dwm adamperkowski
| Zsh || dwm || Neovim || st || tmux || mpv || custom || || WeeChat || ||
|-
! ananthu
| Zsh || bspwm || Neovim || Alacritty ||  || mpv || htop, Polybar || neomutt || WeeChat || ranger ||
|-
! ayekat
| Zsh || karuiwm || Vim || rxvt-unicode || tmux || ncmpcpp / mpd || karuibar || mutt || Irssi || ||
|-
! bachoseven
| Zsh || dwm || Neovim || st || tmux || ncmpcpp || bottom || neomutt || WeeChat || Lf || Newsboat
|-
! bamos
| Zsh || i3 / xmonad || Vim / Emacs || rxvt-unicode || tmux || mpv / cmus || conky / xmobar || mutt || ERC || ||
|-
! brisbin33
| zsh || xmonad || vim || rxvt-unicode || GNU Screen || || dzen || mutt || irssi || ||
|-
! christian-heusel
| Zsh || i3 || Neovim || st / Terminator || byobu / tmux || || htop || neomutt / Thunderbird || WeeChat || Nemo / ranger ||
|-
! CuterThanYou
| Zsh || i3 / Hyprland || Neovim || Alacritty / Foot || || mpv || Polybar / Yambar || || || Lf / Thunar ||Newsboat
|-
! dikiaap
| Zsh || i3-gaps || Neovim || Alacritty || tmux || || i3blocks || || || nnn ||
|-
! Earnestly
| Zsh || i3 / orbment || Vim / Emacs || termite || tmux || mpd || conky || mutt || WeeChat || ||
|-
! egnrse
| Zsh / Bash || Hyprland || Neovim || Alacritty || || VLC || bottom / mission-center || || || Dolphin ||
|-
! ErikBjare
| Zsh || xmonad / Xfce4 || Vim || Terminator || tmux || || xfce4-panel || || WeeChat || ||
|-
! erikw
| Zsh / Bash || dwm / macOS || Neovim || urxvtc || tmux || mpd ||  || mutt || Irssi || ||
|-
! filiparag
| fish || bspwm || Vim || Alacritty || tmux || mpv / playerctl || htop, Polybar || mail-notification || || PCManFM ||
|-
! Freed-Wu
| Zsh || openbox || Neovim || wezterm || tmux || cmus || bottom || neomutt || WeeChat || Neovim || Newsboat
|-
! graysky
| Zsh || Xfce || Vim || terminal || || ncmpcpp || custom || Thunderbird || || ||

|-
! insanum
| Bash || Herbstluftwm || Vim || evilvte || tmux || || dzen || mutt-kz || || ||
|-
! isti115
| pwsh
|| sway
|| neovim
|| alacritty
|| tmux
|| mpv / playerctl
|| waybar / htop / ytop
||
||
|| ranger
||
|-
! itsme
| Zsh || Niri || Helix || kitty || tmux || mpv || Waybar || || || yazi ||
|-
! jasonwryan
| Bash / Zsh || dwm || Vim || rxvt-unicode || tmux || ncmpcpp || custom || mutt || Irssi || ||
|-
! jdevlieghere
| Zsh || xmonad || Vim || terminal || tmux || || htop || mutt || WeeChat || ||
|-
! jelly
| Zsh || i3 || Vim || termite || tmux || ncmpcpp || || mutt-kz-git || WeeChat || ||
|-
! jl2
| Zsh || swayfx || geany || foot || || || mission-center / eww (bar) || || srain || Thunar ||
|-
! karras
| Zsh || Wayfire || Neovim || Terminator || || || Waybar || || || ||
|-
! MarkusZoppelt
| Zsh || GNOME || Neovim || Alacritty || tmux || ||  ||  || || ||
|-
! maximbaz
| Zsh || Sway || kakoune || kitty || || || Waybar || neomutt || || nnn ||
|-
! neersighted
| fish || i3 || Neovim || Alacritty || tmux || ncmpcpp || || || || ||
|-
! nimaipatel
| fish || awesome || Neovim || Alacritty || || ncmpcpp || || || || ||
|-
! oibind
| fish || awesome || Neovim || st || tmux || || htop-vim || || WeeChat || Lf ||
|-
! orhun
| Bash || i3-gaps || Neovim || Alacritty || || || i3status || || WeeChat || tere ||
|-
! patri9ck
| Zsh || bspwm || Vim || kitty || || || || || || Thunar ||
|-
! peterzuger
| Zsh || i3-gaps || Emacs || rxvt-unicode || GNU Screen || MOC || htop || || || ||
|-
! polyzen
| Zsh || i3 || Neovim || Alacritty || tmux || mpv || i3status / htop || himalaya || || ranger || Newsboat
|-
! potamides
| Bash || awesome || Neovim || termite || tmux || ncmpcpp || conky / htop || mutt || WeeChat || ranger ||
|-

! sistematico
| Zsh / fish / Bash || i3-gaps || Vim / nano || termite || tmux || ncmpcpp || Polybar || mutt || WeeChat || ||
|-
! thecashewtrader
| Eshell || EXWM || Emacs || Emacs (VTerm) || Emacs || Bongo || htop || mu4e || ERC || Dired || Elfeed
|-
! thiagowfx
| Bash / Zsh || i3 || Vim || Alacritty || tmux || playerctl || i3status || || || ranger ||
|-
! tplasdio
| bash (ble.sh) || awesome || neovim || alacritty || tmux || mpv, mpvs || htop || neomutt || WeeChat || lf ||
|-
! tuurep
| Zsh || openbox || Neovim || Alacritty || || || Polybar || || || ||
|-
! unrealapex
| Zsh || dwm || Neovim || st || || ncmpcpp || htop || neomutt || Irssi || fff || Newsboat
|-
! w0ng
| Zsh || dwm || Vim || rxvt-unicode || tmux || ncmpcpp || custom || mutt || Irssi || ||
|-
! whitelynx
| fish || i3 || Neovim || kitty || || || i3pystatus || || || ||
|-
! whynothugo
| Zsh || Sway || Neovim || Alacritty || || mpv || Waybar / top || neomutt || || Nemo ||
|-
|}
