# XDG Base Directory

This article summarizes the XDG Base Directory specification in #Specification and tracks software support in #Support.

## Specification
Please read the full specification. This section will attempt to break down the essence of what it tries to achieve.

Only  is set by default through . It is up to the user to explicitly define the other variables according to the specification. Changing it might cause issues with pipewire and screen sharing on chromium.

See Environment variables#Globally for information on defining variables.

## User directories
*
** Where user-specific configurations should be written (analogous to ).
** Should default to .

*
** Where user-specific non-essential (cached) data should be written (analogous to ).
** Should default to .

*
** Where user-specific data files should be written (analogous to ).
** Should default to .

*
** Where user-specific state files should be written (analogous to ).
** Should default to .

*
** Used for non-essential, user-specific data files such as sockets, named pipes, etc.
** Not required to have a default value; warnings should be issued if not set or equivalents provided.
** Must be owned by the user with an access mode of .
** Filesystem fully featured by standards of OS.
** Must be on the local filesystem.
** May be subject to periodic cleanup.
** Modified every 6 hours or set sticky bit if persistence is desired.
** Can only exist for the duration of the user's login.
** Should not store large files as it may be mounted as a tmpfs.
** pam_systemd sets this to .

## System directories
*
** List of directories separated by  (analogous to ).
** Should default to .

*
** List of directories separated by  (analogous to ).
** Should default to .

## Support
This section exists to catalog the growing set of software using the XDG Base Directory Specification introduced in 2003.
This is here to demonstrate the viability of this specification by listing commonly found dotfiles and their support status.
For those not currently supporting the Base Directory Specification, workarounds will be demonstrated to emulate it instead.

The workarounds will be limited to anything not involving patching the source, executing code stored in environment variables or compile-time options.
The rationale for this is that configurations should be portable across systems and having compile-time options prevent that.

Hopefully this will provide a source of information about exactly what certain kinds of dotfiles are and where they come from.

## Supported
{| class="wikitable sortable" style="width: 100%"
! Application
! Legacy Path
! Supported Since
! Discussion
! Notes
|-
|
|
| 1656
2195
| |
If present  will be merged with the XDG path config.
|-
| aerc
|
| [https://git.sr.ht/~rjarry/aerc/commit/fff1664 fff1664
|
|
|-
| ALSA
|
| 577df36
1.2.3
| |
|-
|
| , , ,
| [https://github.com/conda/conda/blob/main/CHANGELOG.md#4110-2021-11-22 4.11.0
| [https://github.com/conda/conda/pull/10982
|
|-
| Android Studio
|
| Android Studio 4.1
|
|
 XDG_CONFIG_HOME/Google/AndroidStudioX.X
 XDG_DATA_HOME/Google/AndroidStudioX.X
 XDG_CACHE_HOME/Google/AndroidStudioX.X
Location overview by Google does not mention XDG - paths could be hardcoded instead of using the proper variable, though that is unlikely as Intellij IDEA, which Android Studio is based on, implements it properly as well
|-
| Anki
| ,
|
| [https://github.com/dae/anki/pull/58 | Uses  as default if no older location exists, can be changed by using
|-
|
| ,
| [https://github.com/Antimicrox/antimicrox/commit/edba864 edba864
| |
|-
|
|
| [https://github.com/naihe2010/apvlv/commit/ed0e0112b05b0cafa13ca4e215ee559c82194caf
| | Uses  now if it exist.
|-
| aria2
|
| [https://github.com/tatsuhiro-t/aria2/commit/8bc1d37 8bc1d37
| |
 XDG_CONFIG_HOME/aria2/
 XDG_CACHE_HOME/aria2/
|-
|
|
| [https://littlesvr.ca/bugs/show_bug.cgi?id=31 2.9.0
| | Uses  for  and  for the other 3 files. Legacy paths are not removed after migration, they have to be deleted manually.
|-
| [https://dotnet.microsoft.com/en-us/apps/aspnet ASP.NET Core
|
| |
|
|-
|
|
| [https://github.com/ellie/atuin/commit/156893d774b4da5b541fdbb08428f9ec392949a0 156893d
|
|
 XDG_CONFIG_HOME/atuin/config.toml
 XDG_DATA_HOME/atuin/history.db
|-
|
|
| 3.2.0
| | Uses new locations if legacy do not exist:
 XDG_CONFIG_HOME/audacity
 XDG_DATA_HOME/audacity
|-
|
|
| [https://github.com/ReFirmLabs/binwalk/commit/2051757 2051757
| |
|-
|
|
| [https://github.com/bitwarden/cli/releases/tag/v1.7.1 1.7.1
| |
 XDG_CONFIG_HOME/Bitwarden CLI

The  environment variable takes precedence.

Currently contains a single  file with all the vault data, so it ought to belong in
|-
| Blender
|
| [https://projects.blender.org/blender/blender/commit/4293f47 4293f47
| |
|-
| borgmatic
|
| [https://projects.torsion.org/borgmatic-collective/borgmatic/releases/tag/1.9.0 1.9.0
| |
|-
|
|
| [https://github.com/aristocratos/btop/commit/b5e709d b5e709d
|
|
|-
|
|
| 4.17
| |

Legacy path takes precedence if present, or if  is not set.
|-
| [https://www.haskell.org/cabal cabal
|
| 9f7dc55 v3.10.1.0
| |
|-
|
|
| [https://github.com/lfos/calcurse/commit/04162d 04162d
| [https://github.com/lfos/calcurse/issues/252
|
 XDG_CONFIG_HOME/calcurse
 XDG_DATA_HOME/calcurse

If the legacy path  is present, it will take precedence.
|-
|
|
|
|
|-
|
|
|
| |
 XDG_CONFIG_HOME/celestia/celestiarc
|-
|
|
| [https://gitlab.xfce.org/apps/catfish/-/commit/af65ed25c5d9bd96647664b5f7d4db50551fed8a af65ed25
| |
|-
|
|
| [https://ccache.dev/releasenotes.html#_ccache_4_0 4.0
| |
 XDG_CACHE_HOME/ccache
 XDG_CONFIG_HOME/ccache/ccache.conf
|-
| [https://clangd.llvm.org/config.html clangd
|
| ad38f4b3 11.0.0
| |

Project specific configuration can be specified in .
Configuration is combined when this is sensible. In case of conflicts, user config has the highest precedence, then inner project, then outer project.
|-
|
|
| [https://github.com/leo-arch/clifm/commit/9d6e482a1d100306ea32fec0c088bce5d229f248 9d6e482
|
|
|-
| Composer
|
| 1.0.0-beta1
| |
|-
| crossnote
|
| [https://github.com/shd101wyy/crossnote/commit/d714a8229c3a757d52a34eadabefb0795568e37d d714a82
0.8.13
| |
If the legacy path is present, it will take precedence.
|-
|  (universal-ctags)
|
| [https://github.com/universal-ctags/ctags/commit/68da03a946cf532e51d014bc9b76265612da0189 68da03a
8fb0b04
|Issue 89
Pull request 2384

|At start-up time, Universal-ctags loads files having file`.ctags` as a file extension under:

See Ctags Option files.
|-
|
|
| |
|
|-
| CUPS
|
| [https://github.com/OpenPrinting/libcups/pull/45/commits/23b1be68803128ed701d374981c4583bcf9e7bf6 23b1be6
| | libcups added XDG support in v3 (still in beta). The version in the official repositories is still hardcoded to .
|-
| cURL
|
| [https://curl.se/changes.html#7_73_0 7.73.0
| |
|-
|
|
|
|
|
|-
| Dolphin emulator
|
| [https://github.com/dolphin-emu/dolphin/commit/a498c68 a498c68
| |
|-
|
|
| [https://github.com/simon-r/dr14_t.meter/commit/7e777ca 7e777ca
| |
|-
|
|
| [https://github.com/dunst-project/dunst/commit/78b6e2b 78b6e2b
| |
|-
| Emacs
|
| [https://git.savannah.gnu.org/cgit/emacs.git/commit/?id=4118297ae2fab4886b20d193ba511a229637aea3
27.1
|
|
Legacy paths have precedence over XDG paths.  Emacs will never create .
Workaround for 26.3 or older: It's possible to set , but it has unexpected side effects.
|-
| Firefox
|
| 147
| |
 XDG_CONFIG_HOME/mozilla/
The legacy path is used if  is present. As of Firefox 147.0.2 there is a bug when using the XDG location:
*  do not work [https://bugzilla.mozilla.org/show_bug.cgi?id=2005167.
|-
| fish
|
|
|
|
|-
| freesweep
|
| |
|
|-
|
|
| [https://github.com/fltk/fltk/commit/7308bcdb74e34626c6459699cb57371afd7b343b 7308bcd
| | [https://www.fltk.org/doc-1.4/classFl__Preferences.html#af8418ff8af933d22dbb70a082525a74e
|-
| fontconfig
|
| 8c255fb, |
| Config goes in  or , fonts are stored in
|-
|
|
| [https://github.com/fontforge/fontforge/commit/e4c2cc7 e4c2cc7
|
[https://github.com/fontforge/fontforge/issues/991
|
|-
|
|
| e7e2994ba
0.20.0
| | Defaults to
 XDG_CONFIG_HOME/FreeCAD
 XDG_DATA_HOME/FreeCAD
 XDG_CACHE_HOME/FreeCAD
legacy path can be used with
|-
|
|
| [https://github.com/FreeRDP/FreeRDP/commit/edf6e72 edf6e72
|
|
|-
| Gajim
|
| 3e777ea
| |
|-
|
|
| [https://gitlab.gnome.org/Archive/gconf/commit/fc28caa fc28caa
| |
|-
| GDB
| ,
| [https://lists.gnu.org/archive/html/info-gnu/2021-09/msg00007.html 11.1
|
| ,
|-
|
|
| |
| Supported upstream from 9.4.1 [https://downloads.haskell.org/~ghc/9.4.1/docs/users_guide/9.4.1-notes.html?highlight=xdg.
|-
|
|
| 3b0aac9
| |
|-
| GIMP
|
|
[https://gitlab.gnome.org/GNOME/gimp/commit/60e0cfe 60e0cfe
483505f
|
[https://bugzilla.gnome.org/show_bug.cgi?id=646644
|
|-
| Git
| , , , ,
| 0d94427, dc79687, 684e40f
| Git Config, Git Attributes, Git Credentials, gitk
| , , , ,
|-
| gnuplot
|
| a5562b1
|
|
|-
| Godot Engine
|
| [https://github.com/godotengine/godot/pull/12988/commits/73049d115e190b8c356f0689a9079c3c73cc5765 73049d1
3.0-stable
| |
|-
|
|
| [https://gitlab.com/goobook/goobook/-/blob/master/CHANGES.rst 3.5
| |
|-
| [https://github.com/google/gops gops
|
| 71c4255
|
|
|-
| GoldenDict
|
| |
|
|-
| GStreamer
|
| [https://gitlab.freedesktop.org/gstreamer/gstreamer/-/commit/4e36f93 4e36f93
| |
|-
| GTK 3
|
|
|
|
|-
| Haskell#Stack
|
| [https://github.com/commercialhaskell/stack/releases/tag/v2.9.3 2.9.3
| | Defaults to legacy. Use  to make it compliant with the spec.
The old method of  still works and takes priority [https://docs.haskellstack.org/en/stable/environment_variables/#stack_xdg.
|-
|
|
| 3.0.0
|
|
|-
|
|
| 93233a6
|
|
|-
|
|
| 5af0874
| |
|-
|
|
|
| [https://github.com/hunspell/hunspell/pull/637
|
|-
| i3
|
| 7c130fb
|
|
|-
| ,
|
| |
|
|-
|
|
| [http://code.stapelberg.de/git/i3status/commit/?id=c3f7fc4 c3f7fc4
|
|
|-
|
|
|
|
|
|-
| IdeaVim
|
| 0.54.1-EAP
| |
|-
|
|
|
|
|
|-
| Inkscape
|
| [https://wiki.inkscape.org/wiki/index.php/Release_notes/0.47#Preferences 0.47
| |
|-
|  /
|
| [https://confluence.jetbrains.com/display/IDEADEV/IntelliJ%2BIDEA%2B2020.1%2B%28201.6668.121%2Bbuild%29%2BRelease%2BNotes 2020.1
| |
 XDG_CONFIG_HOME/JetBrains/IntelliJIdeaXXXX.X
 XDG_DATA_HOME/JetBrains/IntelliJIdeaXXXX.X
 XDG_CACHE_HOME/JetBrains/IntelliJIdeaXXXX.X
|-
|
|
|[https://github.com/Tomas-M/iotop/commit/cea6d5c7a41f2e7a842d4f244532759142af98b0
||
|-
| [https://ipython.org ipython
|
| 8.0.0
| | Checks if  (or  if  is unset) exists, otherwise it uses .
|-
| [https://iwd.wiki.kernel.org/ iwd / iwctl
|
| d3e00d7f
|
|
|-
|
|
| 11162
| |
|-
| [https://github.com/jupyter jupyter
|
| opt-in in 5.0, opt-out in 6.0, compulsory in 7.0 (changelog)
|
|
|-
| Kakoune
|
|
|
|
|-
|
|
|
|
|
|-
| latexmk (in )
|
|
|
|

|-
| less
| ,
| 590
full support in 598
| | The environment variables  and  must be set in version 590. In version 598 this is no longer necessary.

 or
|-
|
|
| [https://github.com/lavv17/lftp/commit/21dc400 21dc400
| |
|-
|
|
| [https://github.com/Sude-/lgogdownloader/commit/d430af6 d430af6
| |
|-
|
|
| [https://codeberg.org/librewolf/source/pulls/120/commits/587de521efe95755bee72246ffe6c7f94a95f49a 587de52
| | The legacy path is used if ~/.librewolf is present. As of Librewolf 147.0.2 there is a bug when using the XDG location (upstream Firefox issue listed):
*  do not work [https://bugzilla.mozilla.org/show_bug.cgi?id=2005167.
|-
|
|
| [https://github.com/luarocks/luarocks/pull/1298/commits/cd16cdd5f889024f28cc384e3d721a4f4a3261d3 cd16cdd
| |
 XDG_CONFIG_HOME/luarocks
 XDG_CACHE_HOME/luarocks

If the legacy path  is present, it will take precedence.
|-
|
|
| [https://github.com/flightlessmango/MangoHud/commit/65b90fc 65b90fc
| |
|-
| mc
|
|
[https://github.com/MidnightCommander/mc/commit/1b99570 1b99570
0b71156
ce401d7
| |
|-
| Mercurial
|
|
[https://www.mercurial-scm.org/repo/hg/rev/3540200 3540200
4.2
|
| .
|-
|
|
| 87ab26b
|
|
|-
|
|
| eb487c5
| |
|-
| mlterm
|
| [https://github.com/arakiken/mlterm/commit/71df0714edc7715524092213516790a24178615b 71df071
| |
|-
| mozc
|
| [https://github.com/google/mozc/commit/91cc1e19ef34aeb12888b697fefa52907f1a834d 91cc1e1
| |
|-
| mpd
|
| [https://github.com/MusicPlayerDaemon/MPD/commit/87b7328 87b7328
|
|
|-
| mpv
|
| cb250d4
| |
|-
| msmtp
|
|
[https://github.com/marlam/msmtp-mirror/commit/af2f409 af2f409
v1.6.7+
|
| .
|-
| mutt
|
| b17cd67
| |
|-
|
|
| [https://github.com/mypaint/mypaint/commit/cf723b7 cf723b7
|
|
|-
| nano
|
| c16e79b
| |
|-
| ncmpcpp
|
|
[https://github.com/arybczak/ncmpcpp/commit/38d9f81 38d9f81
27cd86e
|
[https://github.com/arybczak/ncmpcpp/issues/110
|  should be set to avoid an  file in . And  can be set to  to avoid .
|-
| Neovim
|
| [https://github.com/neovim/neovim/commit/1ca5646bb 1ca5646bb
|
[https://github.com/neovim/neovim/pull/3198
|
|-
| Nestopia UE
|
| 610c008 1.51.0
| |
|-
| Networkmanager-openvpn
|
| [https://gitlab.gnome.org/GNOME/NetworkManager-openvpn/-/tags/1.12.1 1.12.1
| |
|-
| newsboat
|
| [https://github.com/akrennmair/newsbeuter/commit/3c57824 3c57824
| | It is required to create both directories [https://man.archlinux.org/man/newsboat.1#FILES:

|-
| Nix
|
| | [https://github.com/NixOS/nix/pull/5588
| Set  in your
|-
| nmcli
|
| 1.52.0
| [https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/merge_requests/2027 |
|-
| [https://github.com/nodejs/node-gyp node-gyp
|
| 2b5ce52a
| |
|-
| notmuch
|
|
| [https://notmuchmail.org/pipermail/notmuch/2011/007007.html
|
|-
|
|
| 56a1cc2
| |
|-
| [https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS NSS
|
| 3.42 (da45424)
| | See Chromium for existing issue.
|-

|
|
| [https://github.com/nteract/nteract/commit/4593e72 4593e72
| [https://github.com/nteract/nteract/pull/3870
| does not recognize workarounds for ipython/jupyter
|-
|
|

| 2.13.0
9729963
| |

|-
| OfflineIMAP
|
| [https://github.com/OfflineIMAP/offlineimap/commit/5150de5 5150de5
| |
|-
|
|
| [https://github.com/kcat/openal-soft/commit/3c90ed95afa1feed70e6c5655cfeec096c00c23b 3c90ed9
|
|
|-
|
|
| 39559c3
| |
|-
|
|
| [https://github.com/openSUSE/osc/commit/6bc2d3f939c2518ae555fbf75e3a11cc16fc5302 6bc2d3f
ebcf3de
|github.com/openSUSE/osc/pull/940
github.com/osc/pull/940
|

Legacy path takes precedence if it exists
|-
| pacman
|
| 80eca94
| |
|-
|
|
| [https://github.com/Yubico/pam-u2f/commit/ad52dd82dead525dab94ded1916dcf6334459106 ad52dd8
| |
|-
|
|
| [https://github.com/panda3d/panda3d/commit/2b537d2 2b537d2
|
|
|-
|
|
| 0bed0ab
| |
|-
| PCManFM
|
| [https://github.com/lxde/libfm/issues/57 1.3.2
|
|
|-
|
|
|
87f1e8f
a9020c6
3b22f0f
0a012ae
| [https://github.com/PCSX2/pcsx2/issues/381
|
|-
|
|
|
|
|
|-
|
|
| [https://github.com/pnpm/pnpm/pull/4522
| |
|-
|
|
|
|
|
|-
|
|
| [https://docs.microsoft.com/en-us/powershell/scripting/whats-new/what-s-new-in-powershell-core-60#filesystem 6.0
|
|
|-
|
|
| 132fe47
| |
|-
|
|
| [https://gitlab.com/procps-ng/procps/commit/af53e17 af53e17
|
[https://bugzilla.redhat.com/show_bug.cgi?id=1155265
|
|-
| Pry
|
|
a0be0cc7
15e1fc92
e9d1be0e
| |
|-
| PulseAudio
|
|
[https://gitlab.freedesktop.org/pulseaudio/pulseaudio/-/commit/59a8618 59a8618
87ae830
9ab510a
4c195bc
| |
 XDG_CONFIG_DIR/pulse
 XDG_CONFIG_DIR/pulse/cookie
|-
|
|
|
|
|
|-
|
|
| [https://github.com/lyz-code/autoimport/pull/206 1.2.0
| |
|-
|
|
| [https://github.com/psf/black/pull/1899 21.4b0
| | ,
|-
|
|
| [https://github.com/pypa/pip/blob/548a9136525815dff41acd845c558a0b36eb1c5f/NEWS.rst#60-2014-12-22 6.0
| |
|-
|
|
| [https://github.com/pypa/pipx/pull/1001 c3d8de9
| | For compatibility, pipx will revert to  if it exists. Implemented using
|-
|
|
| [https://github.com/python-poetry/poetry/pull/3706
| |
|-
|
|
| [https://github.com/PyCQA/pylint/pull/4661 2.10
| | Formerly , global config still needs:
|-
|
|
| 3.10.0
| [https://github.com/quodlibet/quodlibet/issues/138
|
|-
| qutebrowser
|
|
|
|
|-
| qtile
|
|
fd8686e
66d704b
51cff01
| | Some optional bar widgets can create files and directories in non-compliant paths, but most often these are still configurable.
|-
|
|
| [https://github.com/ncw/rclone/commit/9d36258 9d36258
| |
|-
|
|
|
|
|
|-
|
|
| [https://github.com/phiresky/ripgrep-all/commit/963524bbf5ec861cc1d9d2b57e119eb60125751a 963524b v0.10.3
| [https://github.com/phiresky/ripgrep-all/issues/102 |
|-
|
|
| [https://github.com/mozilla/rr/commit/02e7d41 02e7d41
| |
|-
| [https://rspec.info RSpec
|
| 5e395e2
| |
|-
| rTorrent
|
| [https://github.com/rakshasa/rtorrent/commit/6a8d332 6a8d332
|
|
|-
| RuboCop
|
| 6fe5956
| |
|-
| Ruby#RubyGems
|
| [https://github.com/ruby/ruby/commit/5c6269c 3.0.0 (5c6269c)
| |
 XDG_CONFIG_HOME/gem/gemrc
 XDG_CONFIG_HOME/irb
 XDG_DATA_HOME/gem
 XDG_DATA_HOME/rdoc
|-
| [https://github.com/benvan/sandboxd sandboxd
|
| | [https://github.com/benvan/sandboxd/issues/11
|
|-
|
|
| 1.5.3
|
|
|-
|
|
| 7d014be
| | It is required to migrate data by hand.

|-
|
|
| [https://github.com/Dushistov/sdcv/commit/958ec35 958ec35
| |
|-
|
|
|[https://github.com/koalaman/shellcheck/commit/581bcc3907ab98e919a7dd60566810a928c46b95 581bcc3
|
|
See Shellcheck RC Files for more info.
|-
|
|
| 93b5f11
| | By default, the configuration file is left blank with intention that the user will fill it at their will (through the gui or manually).
|-
| spectrwm
|
| [https://github.com/conformal/spectrwm/commit/a30bbb a30bbb
| |
|-
|
|
| [https://www.sublimetext.com/dev build 4105
|
| Prior to build 4105, the cache was placed in .
|-
| surfraw
|
|
3e4591d
bd8c427
f57fc71
|
|
|-
| sway
|
| 614393c
| |
|-
| sxhkd
|
|
|
|
|-
|
|
| [https://github.com/symfony-cli/symfony-cli/releases/tag/v5.17.1 5.17.1
|
|
|-
| systemd
|
|
|
|
|-
|
|
| |
|
|-
| termite
|
|
|
|
|-
| Theming (desktop)
| ,
| [https://specifications.freedesktop.org/icon-theme-spec/0.7/#directory_layout
|
|

For Qt programs, GTK or Qt programs on Wayland, to use cursors in , the XCURSOR_PATH environment variable needs to be configured.
|-
|
| ,
| 2.2
| |  directory must exist, writes to  otherwise.
|-
| TigerVNC
|
| [https://github.com/TigerVNC/tigervnc/releases/tag/v1.14.0 1.14.0
| |
|-
| tmux
|
| [https://raw.githubusercontent.com/tmux/tmux/3.1/CHANGES 3.1
| | 3.1 introduced  and in [https://github.com/tmux/tmux/blob/a5f99e14c6f264e568b860692b89d11f5298a3f2/CHANGES#L145 3.2  was added
|-
|
|
| 2636923
| |
|-
| tmuxp
|
| [https://tmuxp.git-pull.com/history.html#tmuxp-1-5-0-2018-10-02 1.5.0
| | Fixed in [https://tmuxp.git-pull.com/history.html#tmuxp-1-5-2-2019-06-02 1.5.2
|-
| Transmission
|
| b71a298
|
|
|-
|
|
| 570b321
|
|
|-
| Uzbl
|
| c6fd63a
| |
|-
|
|
| [https://github.com/errata-ai/vale/releases/tag/v3.0.0 3.0.0
|
|
|-
| Vim
| , ,
| c9df1fb
| [https://github.com/vim/vim/issues/19399
|
See :h xdg-base-dir for more details.
Full XDG support is pending:
|-
|
|
|
|
|
|-
| VirtualBox
|
| [https://www.virtualbox.org/ticket/5099?action=diff&version=7 4.3
| | Clobbers  by writing hundreds of kilobytes of  and  files into it.
|-
|
|
|
[https://github.com/martanne/vis/commit/68a25c7 68a25c7
d138908
| |
|-
| VLC
|
| [https://code.videolan.org/videolan/vlc/-/commit/16f32e1500887c0dcd33cb06ad71759a81a52878 16f32e1
| |
|-
|
|
| [https://github.com/Qfusion/qfusion/commit/98ece3f 98ece3f
| |
|-
| WeeChat
|
| [https://github.com/weechat/weechat/commit/70cdf21681d75090c3df9858c9e7ce5a85433856
3.2
| [https://specs.weechat.org/specs/2021-001-follow-xdg-base-dir-spec.html
|
 XDG_CONFIG_HOME/weechat
 XDG_DATA_HOME/weechat
 XDG_CACHE_HOME/weechat
 XDG_RUNTIME_DIR/weechat
|-
| Wireshark
|
| b0b53fa v2.1.0
|
|
|-
| wxWidgets
|
| |
|
|-
| [https://www.x.org/wiki/XKB/ XKB
|
|
|
| only supported on Wayland |-
| xmobar
|
| [https://github.com/jaor/xmobar/commit/7b0d6bf 7b0d6bf
9fc6b37
eaccf70
| [https://github.com/jaor/xmobar/pull/131
|
|-
| xmonad
|
| 40fc10b
|
[https://code.google.com/p/xmonad/issues/detail?id=484
| All of these must exist, otherwise it gives up and falls back to  for each:
 XDG_CACHE_HOME/xmonad
 XDG_CONFIG_HOME/xmonad
 XDG_DATA_HOME/xmonad
Alternatively, it always respects , , and .
|-
|
|
|
| |
|-
|
|
| [https://github.com/xournalpp/xournalpp/commit/20db937f 20db937f
1.1.0
|[https://github.com/xournalpp/xournalpp/pull/1384
|
|-
|
|
| ee7b481
| |
|-
| Xsettingsd
|
| [https://github.com/derat/xsettingsd/commit/b4999f5 b4999f5
|
|
|-
|
|
| a0b51d2
| |
|-
| Zim
|
| [https://github.com/zim-desktop-wiki/zim-desktop-wiki/commit/e42b8b0 e42b8b0
|
|
  $XDG_CONFIG_HOME/zim/preferences.conf
  $XDG_CONFIG_HOME/zim/notebooks.list
|-
|
|
| 0.3.0
| |
|-
| [https://www.nongnu.org/zutils/zutils.html zutils
|
| 1.12
|
|
 $XDG_CONFIG_HOME/zutils.conf
|}

## Partial
{| class="wikitable sortable" style="width: 100%"
! Application
! Legacy Path
! Supported Since
! Discussion
! Notes
|-
|
|
|
|
|
|-
|
|
|
| |
|-
| Ansible
| ,
| [https://github.com/ansible/ansible/pull/76114 2.14
| [https://github.com/ansible/ansible/issues/68587 | {{bc|1=export ANSIBLE_HOME="${XDG_CONFIG_HOME}/ansible"
export ANSIBLE_CONFIG="${XDG_CONFIG_HOME}/ansible.cfg"
export ANSIBLE_GALAXY_CACHE_DIR="${XDG_CACHE_HOME}/ansible/galaxy_cache"
export ANSIBLE_LOCAL_TEMP="${XDG_CACHE_HOME}/ansible/tmp"
export ANSIBLE_SSH_CONTROL_PATH_DIR="${XDG_CACHE_HOME}/ansible/cp"
export ANSIBLE_ASYNC_DIR="${XDG_CACHE_HOME}/ansible_async"}}
|-
|
| ,
|
| [https://github.com/asdf-vm/asdf/issues/687
| {{ic|1=export ASDF_CONFIG_FILE="${XDG_CONFIG_HOME}/asdf/asdfrc"}}, {{ic|1=export ASDF_DATA_DIR="${XDG_DATA_HOME}/asdf"}}
|-
| aspell
|
|
| | Very incomplete. The following re-locates the  dictionaries, but additional possible dictionaries are not specificed here for brevity.
|-
|
|
| [https://github.com/aws/aws-cli/commit/fc5961ea2cc0b5976ac9f777e20e4236fd7540f5 1.7.45
| | ,
|-
|
|
|
|
|
|-
|
|
|
|
|
|-
|
|
|
|
| Like documented at [https://bashdb.sourceforge.net/bashdb.html#Command-Files, you can specify a file to run commands from. Thus, move the init file to  and create an alias {{ic|1=alias bashdb='bashdb -x ${XDG_CONFIG_HOME:-$HOME/.config}/bashdb/bashdbinit'}}. Unfortunately the history file is hardcoded |-
| bazaar
| ,
| [https://bugs.launchpad.net/bzr/+bug/195397/comments/15 2.3.0
| | Discussion in upstream bug states that bazaar will use  if it exists. The logfile  might still be written.
|-
|
|
|
| [https://github.com/bitwarden/clients/issues/13099
|
|-
|
|
| 0.7.5
| |
|-
|
|
|
| [https://github.com/btpd/btpd/issues/55
|

|-
|
|
|
| | Bun will prioritize using , , and/or  when these have explicitly been set. As an alternative,  can be used to set 's main location for its directories.
|-
|
|
|
|
|
 export CALCHISTFILE="$XDG_CACHE_HOME"/calc_history
|-
| Rust#Cargo
|
|
| [https://github.com/rust-lang/cargo/issues/1734 [https://github.com/rust-lang/cargo/pull/5183  |
|-
|
|
|[https://gitlab.archlinux.org/archlinux/packaging/packages/cataclysm-dda/-/commit/0947de440817c9c418cac615275edbf1cc0abdbb 0.D-1
|| partial support due to required compile time option
|-
| [https://github.com/mollifier/cd-bookmark cd-bookmark
|
|
| |
or use the fork that has native XDG support: [https://github.com/erikw/cd-bookmark/
|-
|
|
| 0.8.0
| [https://github.com/cgdb/cgdb/blob/master/NEWS
| Set  and move the config file to
|-
|
|
|
|
|
|-
| chktex in
|
|
|
| Move the config file to  (mind the leading dot) and
|-
| Chromium
| ,
| 23057 7551836
| [https://code.google.com/p/chromium/issues/detail?id=16976 | Deliberately (according to these sources) clobbers  by writing hundreds of megabytes of cache data into it. Quite unsupported. Chromium /resources/app.asar}}.
|-
| Docker
|
|
|
|
|-
|
|
|
|
|
|-
| DOSBox
|
|
| [https://www.vogons.org/viewtopic.php?t=29599
|
|-
|
|
| v1.30.0-beta.1
|
| Dub uses the  directory for both user settings and caching downloaded packages. The directory can only be moved as a whole, using .
|-
|
|
|
| |
|-
| [https://electrum.org Electrum Bitcoin Wallet
|
| c121230
|
|
|-
| ELinks
|
|
|
|
|-
|
| ,
| afaf889
| [https://github.com/hexpm/hex/pull/841
| Elixir does not fully conform to XDG specs, it will use XDG only if the  variable is set to a special value, otherwise it will by default use legacy path.

|-
| Elm
|
|
|
|
|-
|
| , , ,
|
| | , , ,
|-
|
|
| [https://github.com/erlang/otp/pull/5408
| | Erlang does not fully conform to XDG specs, it looks for its files in  last.

|-
|
|
|
| [https://forums.factorio.com/viewtopic.php?t=30585 | Factorio supports manually specifying data paths with a config file: [https://wiki.factorio.com/Application_directory#Linux

|-
|
|
|
| | . Fceux will create  directory inside .
|-
| FFmpeg
|
|
|
|
|-
|
| , , ,
|
| [https://github.com/flutter/flutter/issues/59430
|
|-
|
|
|
| | The shell init files will be installed to  if the installation script is called with  for example .
|-
|
|
| [https://github.com/google-gemini/gemini-cli/releases/tag/v0.25.0 0.25.0
| |
|-
|
|
|
|
|
|-
| getmail
|
|
|
|
|-
|
|
| [https://gitlab.haskell.org/haskell/ghcup-hs/-/commit/80603662b4fcc42fd936f45608dc3bc924c7e498
| |
The environment variable  can be set to any non-empty value. See [https://www.haskell.org/ghcup/guide/#xdg-support.
|-
|
|
|
| |
|-
|
|
| [https://github.com/sigstore/cosign/commit/32a2d62a9992b1b990f3747e0bbb1533529d7e14
|
|
|-
|
|
|
|
|
|-
| GNU Screen
|

|
|
| , {{ic|1=export SCREENDIR="${XDG_RUNTIME_DIR}/screen"}}
|-
| GnuPG
|
|
| [https://bugs.gnupg.org/gnupg/issue1018
| ,
Note that this currently does not work out-of-the-box using systemd user units and socket-based activation, since the socket directory changes based on the hash of . You can get the new socket directory using  and have to modify the systemd user units to listen on the correct sockets accordingly. You also have to use the following  drop-in file (or otherwise pass the GNUPGHOME env var to the agent running in systemd), or you might experience issues with "missing" private keys:

 Environment="GNUPGHOME=%h/.local/share/gnupg"

If you use GPG as your SSH agent, set  to the output of  instead of some hardcoded value.
|-
|
|
|
| [https://github.com/gnuradio/gnuradio/issues/3631
| GNU Radio:

GNU Radio Companion:

|-
| Go
|
| |
| ,
If  is not set, it defaults to  (see [https://go.dev/ref/mod#environment-variables).
 is supported and defaults to  (see |-
| Google Earth
|
|
|
| Some paths can be changed with the  and  options in
|-
|
|
|
|
| Override settings in :

 is supported only during initialization.
|-
|
|
|
|
|  sets the download folder.  - where config and database files are stored, downloads also if  is not set.
|-
| [https://sourceforge.net/projects/gqclient GQ LDAP client
| ,
| 1.51
|
| , ,
|-
| Gradle
|
|
| [https://github.com/gradle/gradle/issues/8262
|
|-
| GTK 1
|
|
|
|
|-
| GTK 2
|
|
|
|
If Lxappearance is used,  may keep being created because it is where clicking "Apply" customizations writes to. The path is hardcoded in Lxappearance, but simply being an output file, the settings can be repeatedly moved to the location.

To prevent KDE Plasma from creating this file, disable the "GNOME/GTK Settings Synchronization" background service.
|-
|
|
|
| |
|-
| [https://www.sidefx.com/products/houdini/ Houdini
|
|
| [https://www.sidefx.com/docs/houdini/ref/env.html
|
The value of this variable must include the substring , which will be replaced at run time with the current  version string.
|-
|
|
|
|
|
|-
| IPFS
|
|
|
|
|-
| irb
|
|
|
|

|-
| irssi
|
|
| |
|-
| isync
|
|
| [https://sourceforge.net/p/isync/feature-requests/14/
|
|-
| Java#OpenJDK
|
|
| |
|-
| jupyter
|
| [https://github.com/jupyter/jupyter_core/releases/tag/5.0.0rc0 5.0.0rc0
| [https://github.com/jupyter/jupyter_core/pull/292
|  = v6.0.0: full support (via ) enabled by default
|-
|
|
| 0.20.4
| |
|-
| KDE4
| ,
|
| [https://userbase.kde.org/KDE_System_Administration/KDE_Filesystem_Hierarchy#KDEHOME
|

KDE4 uses . It is not recommended to set the variable for newer versions.
|-
|
|
| | [https://github.com/funtoo/keychain/issues/8
|
|-
|
|
| | [https://github.com/xbmc/xbmc/pull/6142
|
|-
|
|
|
| |
|-
| ledger
| ,
|
| [https://github.com/ledger/ledger/issues/1820
|
|-
| Leiningen
| ,
|
| |

to change the m2 repo location used by leiningen look here: Leiningen#m2_repo_location
|-
|
|
|
| [https://mailman.videolan.org/pipermail/libdvdcss-devel/2014-August/001022.html
|
|-
|
|
|
| |
Make sure  is set beforehand to directory user running Xorg has write access to.

Do not use  as it is available after login. Display managers that launch Xorg (like GDM) will repeatedly fail otherwise.
|-
| LibreOffice
|
|
| [https://bugs.documentfoundation.org/show_bug.cgi?id=140039
| Libreoffice stores everything in , including runtime files, user data, cache and extensions. Some of these can be changed unter Tools > Options > LibreOffice > Paths
|-
| libx11
| ,
|
|
| ,
|-
|
|
|
|
|
|-
| Luanti
|
|
| |
|-
|
|
|
|
|
|-
| [https://git.savannah.nongnu.org/cgit/m17n/m17n-db.git m17n-db
|
|
| |
|-
| [https://www.mamedev.org/ MAME
|
|
|
| If using Arch's  package,  will be a wrapper script that automatically creates and forces use of . Run  once to populate this directory, then you can move it to . Edit  to replace all instances of , then you can launch MAME with .
|-
|
|
|
| |
However, no way to change the location of this configuration file.
|-
|
|
|
| [https://issues.apache.org/jira/browse/MNG-6603
| ,
,  and set  as appropriate in settings.xml
|-
| Mathematica
|
|
|
|

Used to be , see Upgrading from Mathematica to Wolfram.
|-
|
|
|
|
|
|-
|
|
|
|
|
|-
|
|
|
| |

Creates a further  directory in  for whatever reason.
|-
|
|
| [https://github.com/minio/mc/pull/4720
|
|
|-
|
|
|
|
| ,
|-
| MOC
|
|
|
| ,
|-
|
|
|
|
|
|-
|
|
|
|
|
|-
| MPlayer
|
|
|
|
|-
|
|
|
| |
|-
|
| , ,
| [https://github.com/python/mypy/pull/6304 v0.670
| [https://github.com/python/mypy/issues/8790
| ,
|-
| MySQL
| , ,
|
|
|

 only supported for mysql-server, not mysql-client unsupported
|-
|
|
|
|
| You can run MySQL Workbench with the  flag, such as . The directory needs to be created manually, since MySQL Workbench default location is  .
|-
|-
| [https://github.com/tj/n n
|
|
|
|
|-
|
|
|
|
|
|-
|
|
|
|
| Precludes system path searching:

,
|-
| Netbeans
|
|
| | {{ic|1=netbeans --userdir "${XDG_CONFIG_HOME}"/netbeans}}
|-
| Node.js
|
|
| [https://nodejs.org/api/repl.html#repl_environment_variable_options
|
|-
|
|
|
|
|
|-
|
| ,
|
| |
{{hc|npmrc|
prefix=${XDG_DATA_HOME}/npm
cache=${XDG_CACHE_HOME}/npm
init-module=${XDG_CONFIG_HOME}/npm/config/npm-init.js
logs-dir=${XDG_STATE_HOME}/npm/logs
}}
 is unnecessary (and unsupported) if Node.js is installed by .
|-
|
|
|
| [https://docs.microsoft.com/en-us/nuget/consume-packages/managing-the-global-packages-and-cache-folders
|
|-
| NVIDIA
|
|
|
| Uses  if set, otherwise improperly falls back to  instead of .
|-
|
|
|
| |
|-
|
|
|
|
|
|-
| Octave
| , ,
|
|
| ,

The  option must be given an absolute path.
|-
|
|
| [https://github.com/OmniSharp/omnisharp-roslyn/commit/e1353fb8ded7070d6e126b0b6030dac5d3d707ea
| |
|-
|
|
|
| [https://github.com/ocaml/opam/issues/3766
|
Both configuration and state data are stored in , so this solution is not fully compliant.
|-
|
|
| 5fc9fc3
| |
|-
|
|
| [https://github.com/openscad/openscad/commit/7c3077b0f 7c3077b0f
| | Does not fully honour XDG Base Directory Specification, see [https://github.com/openscad/openscad/issues/373

Currently it hard-codes .
|-
|
| ,
|
|
| Has GUI config to change PT installation directory,  (Options > Preferences > Administrative > User Folder). This path is written to the file .
Log files may still be written to  regardless of this setting until the  file is recreated manually.
|-
|
|
| 20170422
|
|
|-
| pass
|
|
|
|
|-
| Phive
|
|
| Also [https://github.com/phar-io/phive/issues/286 and | Since 0.14.5, it is possible to move the whole data directory.

|-
| PHP
|
| [https://www.php.net/manual/en/migration84.new-features.php#migration84.new-features.readline PHP 8.4
| |
|-
| Pidgin
|
|
| [https://developer.pidgin.im/ticket/4911
|
|-
|
|
|
| |
|-
| PostgreSQL
| , , ,
| 9.2
| [https://www.postgresql.org/docs/current/static/app-psql.html | , , ,

It is required to create both directories:
|-
| [https://store.steampowered.com/app/108600/Project_Zomboid/ Project Zomboid
|
|
|
| You can use -cachedir="${XDG_DATA_HOME}"/Zomboid/ to change where the game files are stored.

The  script also defines its own game data location with {{ic|GAMEDIR"${HOME}/Zomboid"}}. If you use Steam, the script will be reset when the game updates, so editing it manually is not an option. But you can make a custom script that will always patch the main script if it gets restored by Steam:

{{hc|start.sh|output=
#!/usr/bin/env bash

SCRIPT="$(dirname "$0")/projectzomboid.sh"
sed 'sGAMEDIR"${HOME}/Zomboid"GAMEDIR"${XDG_DATA_HOME}/Zomboid"' -i "$SCRIPT"

exec "$SCRIPT" -cachedir="${XDG_DATA_HOME}"/Zomboid/ "$@"
}}

Name it  and put it where  is, then make Steam execute  instead of the main script with , note that this will also launch the game without Steam Linux Runtime.
|-
| PulseAudio
|
|
|
| Very likely generated by the  module.  It can be configured to use a different location but it makes much more sense to just comment out this module in  or .
|-
| PuTTY
|
| 9952b2d
|
| Will use  if it already exists. Creates  if not. Prioritises  if both exist. Tested in 0.74
|-
|
|
|
| [https://github.com/pyenv/pyenv/issues/1789
|
|-
| python
|
| v3.13
| [https://bugs.python.org/issue20886 | All history from interactive sessions is saved to  by default since [https://bugs.python.org/issue5845 version 3.4 and  since 3.13. For the history file, Python will not create any missing directories and only writes to the file if its directory exists. This can still be customized the same way as in older versions (see this example), including to use a custom path or disable history saving.

PYTHON_HISTORY:
PYTHONPYCACHEPREFIX:
PYTHONUSERBASE:
|-
|
|
|
|
|
|-
|
|
|
|
|
|-
|
|
|
|
|
|-
|
|
|
|
|
|-
|
| ,
|
| |
|-
|
|
|
| [https://github.com/rbenv/rbenv/issues/811 |
|-
| readline
|
|
|
|
|-
|
|
|
|
|
|-
|
| ,
|
|
|,
|-
| [https://www.renpy.org/ Ren'Py
|
| 7.5
| | Save games are stored in . Data that is shared across multiple games (e.g. sequals that let you import saves from previous entries) is stored in .
|-
|
|
|
| [https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md#configuration-file
|
|-
|
|
|
| |
|-
|
|
|[https://github.com/rubygems/rubygems/commit/4a120d82a730c92c78571bf1819a841ca1ac94a2 4a120d8
|Pull request 3545
|
 export BUNDLE_USER_CACHE=$XDG_CACHE_HOME/bundle
 export BUNDLE_USER_CONFIG=$XDG_CONFIG_HOME/bundle/config
 export BUNDLE_USER_PLUGIN=$XDG_DATA_HOME/bundle
For more info see Bundler: bundle config.
|-
|
|
|
| |
|-
|
|
|
| [https://github.com/travis-ci/travis.rb/issues/219
|
|-
|
|
|
| |
|-
| Rust#rustup
|
|
| [https://github.com/rust-lang-nursery/rustup.rs/issues/247
|
|-
| SageMath
|
|
|
|
|-
|
|

|
| |  (beware [https://github.com/sbt/sbt/issues/3598)
|-
|
|
|
| |
Both configuration and data files are stored in , so this solution does not fully conform to the XDG Base Directory Specification.
|-
|
|
| [https://github.com/MaartenBaert/ssr/releases/tag/0.4.3 0.4.3
| [https://github.com/MaartenBaert/ssr/issues/813
| Will use  ONLY if it already was created otherwise defaults to

|-
|
|
| 3.11.4
|
| ,
|-
| spacemacs
| ,
| | [https://github.com/syl20bnr/spacemacs/issues/3589
| Move the  file.

,

Other files need to be configured like Emacs.
|-
|
|
| v4.0.6 (3929cae)
| |
|-
| SQLite
| ,
| [https://github.com/sqlite/sqlite/commit/6e8a33 3.44.0 for the config;history is still in the legacy place
|
| ,
|-
|
| ,
| ([https://github.com/starship/starship/releases/tag/v0.2.0 v0.2.0), ([https://github.com/starship/starship/releases/tag/v0.45.0 v0.45.0)
| | ,
|-
| subversion
|
|
| [https://issues.apache.org/jira/browse/SVN-4599 |
|-
|
|
| [https://www.sudo.ws/stable.html#1.9.6 1.9.6
| [https://www.sudo.ws/repos/sudo/rev/d77c3876fa95
| Only present when activated at compile-time (default none). An admin_flag parameter can be used in /etc/sudoers since 1.9.6.
|-
|
| ,
|
|
| , }}, {{ic|Fully supported in version 2.6 (note $XDG_CONFIG_HOME/task/taskrc must exist, otherwise taskwarrior will offer to create sample config in legacy $HOME/.taskrc location, even if $XDG_CONFIG_HOME is set |-
| Local TeX Live TeXmf tree, TeXmf caches and config
| , ,
|
|
| , ,
|-
| [https://www.texmacs.org/ TeXmacs
|
|
|
|
|-
| Thunderbird
|
|
| | A directory  is created, containing subdirectories with the profile names, then the subdirectories ,  and possibly others. This cache directory may also be set in about:config key browser.cache.disk.parent_directory [https://askubuntu.com/questions/171322/how-to-change-default-location-of-thunderbird-cache-directory.
|-
|
|
|
|
| This will still expect the  file.

|-
|
|
|
|
|
|-
| Unison
|
|
|
|
|-
|
|
|
|
|
|-
| urxvtd
|
|
|
|
|-
| Vagrant
| ,
|
| | ,
|-
|
| , ,
| [https://github.com/Vimjas/vint/pull/235/commits/0f741ac2c 0f741ac2c
| | Undocumented, but the code says  should work
|-
| virtualenv
|
|
|
|
|-
| Visual Studio Code
|
|
| [https://github.com/Microsoft/vscode/issues/3884
| You can use , which is not documented and might break unexpectedly.
Setting this makes the editor look for the contents of  in .

You can also run Visual Studio with the  flag, such as . This is documented and probably will not break as unexpectedly, as it .

|-
| VMware
|
|
|
| The key  in  can be used to set the default location of virtual machines.
|-
|
|
|
| [https://github.com/VSCodium/vscodium/issues/671
| You can run VSCodium with the  flag, such as . This however will not prevent the creation of   directory.
You can also edit the value of  in  file to  or the path you want. But this workaround will have to be applies after every update of the pacakge, so you can install  that does it automatically.
|-
|
|
| 26284ff
| [https://github.com/tats/w3m/issues/130
|
|-
|
| ,
|
|
|

The directory needs to be created manually

|-
| wget
| ,
|
|
|  and add the following as an alias for wget: , or set the  variable with an absolute path as wgetrc does not support environment variables:
|-
| wine
|
|
| | Winetricks uses XDG-alike location below for WINEPREFIX management:
,
|-
|
| ,
|
|
| ,

App also creates  but this is currently unsupported.
|-
| xbindkeys
|
|
|
|
|-
| xinit
| ,
|
| [https://gitlab.freedesktop.org/xorg/app/xinit/issues/14
| ,
|-
| Xorg
| , , ,
|
|
| These can be added as part of your Xorg init script () or Xsession start script (which will often be based on ).
Depending on where you have configured your , you might need to expand the paths yourself.

Unlike most other examples in this table, actual X11 init scripts will vary a lot between installations.
|-
|
|
|
|
|

Note that LightDM does not allow you to change this variable. If you change it nonetheless, you will not be able to login. Use startx instead or configure LightDM. According to SLiM has  hardcoded.

The SDDM Xauthority path can be changed in its own configuration files as shown below. Unfortunately, it is relative to the home directory.

On Wayland, overriding this may cause Xorg programs to fail to connect to the Xwayland server. For example, both  and  use a randomized name, so it cannot be set to a static value.
|-
|
| ,
|
|
| Ultimately you [https://superuser.com/questions/243914/xresources-or-xdefaults should be using  and since these resources are loaded via  you can specify a path such as .
|-
|
| , , ,
| 2d454b5
| [https://github.com/yarnpkg/yarn/issues/2334
|
|-
|
|
|
| |
|-
| zsh
| , , , , , , ,
| [https://www.zsh.org/mla/workers/2013/msg00692.html
| |  to avoid the need of most zsh dotfiles in your home.

Finally, if you use zsh as a login shell and chose to rely on either of the startup files  or,  or,  to set important environment variables such as , to bootstrap, there is no way around having the one file that sets  be in the default location. For context, an exception is if your wider system configuration does set the  environment variable before that.

|}

## Hardcoded
{| class="wikitable sortable" style="width: 100%"
! Application
! Legacy Path
! Discussion
! Notes
|-
| adb & [https://developer.android.com/studio/index.html Android Studio
|
|
| Despite appearances otherwise, adb will always generate , though it will try keys in  as well.
|-
|
|
| |
|-
| alpine
| , , , , , ,
|
|
In the above config file, some locations can be customized using options like  and .
|-
| aMule
|
| [https://bugs.amule.org/view.php?id=1308 [https://github.com/amule-project/amule/issues/254
|
|-
| Apache Directory Studio
|
|
|
|-
| ARandR
|
| |
|-
| Arduino
| ,
| [https://github.com/arduino/Arduino/issues/3915 will not fix
|
|-
|
|
| |
Specify the new directories used by Arduino CLI in arduino-cli.yaml as mentioned in the documentation [https://arduino.github.io/arduino-cli/latest/configuration/ here.

|-
|-
| Avidemux
|
| |
|-
|
|
| [https://github.com/nwg-piotr/azote/issues/154
|
|-
| Barony
|
| |
|-
| Bash
| , , , ,
| [https://savannah.gnu.org/support/?108134 |

 can be sourced from a different location in .
Specify  as an alternative to  for interactive shells.
|-
| Berkshelf
|
|-
|
|
| [https://github.com/chatty/chatty/issues/273
|
|-
|
|
| | Last developer response [https://web.archive.org/web/20210127040026/http://intrepid.danplanet.com/pipermail/chirp_devel/2020-July/005987.html here
|-
| Cinnamon
|
| |
|-
|
|
| [https://gitlab.kitware.com/cmake/cmake/-/issues/22480
| Used for the user package registry , detailed in  and the Package registry wiki page. Looks like it's hardcoded, for example in cmFindPackageCommand.cxx.
|-
|
|
| | [https://github.com/cmus/cmus/issues/1283
|-
|
|
| |  will set the directory in which  is created. It was [https://docs.conan.io/en/latest/reference/env_vars.html#conan-user-home designed to simplify CI, but can be used here too.
|-
| Continue
|
| [https://github.com/continuedev/continue/issues/558 |
|-
| darcs
|
| [https://bugs.darcs.net/issue2453
|
|-
|
| , ,
| |
|-
| dbus
|
| [https://gitlab.freedesktop.org/dbus/dbus/issues/46
| Consider using , as it does not create or use this directory.
|-
|
|
|
| Hardcoded here
|-
| Dia
|
|
|
|-
| dig
|
|
|
|-
|
| ,
| |
|-
| dropbox
|
| [https://github.com/dropbox/nautilus-dropbox/issues/5
|
|-
| Eclipse
|
| | Option  overrides but must be added to  rather than command line which means you must have write access to . (Arch Linux hard-codes  in )
|-
|
|
| [https://github.com/slime/slime/issues/610
|
|-
|
|
| [https://bugs.launchpad.net/equalx/+bug/2014460
|
|-
| feh
|
| |
|-
| [https://www.fetchmail.info/ Fetchmail
|
|
|
|-
| Flatpak
|
| [https://github.com/flatpak/flatpak.github.io/issues/191 will not fix
|
|-
|
|
| |-
|
|
| [https://github.com/GoogleCloudPlatform/gsutil/issues/991
|
|-
|
|
| |
|-
|
|
| [https://gramps-project.org/bugs/view.php?id=8025
| 2022 Support XDG base directory specification (for next release Gramps 5.2 ) - Patch https://github.com/gramps-project/gramps/pull/1368
|-
|
|
|
|
|-
|
|
| |
|-
| [https://recordmydesktop.sourceforge.net/about.php gtk-recordMyDesktop
|
|
|
|-
|
|
| |
|-
|
| ,
| [https://github.com/dvorka/hstr/issues/461
| Recent pull request to fix this
|-
|
|
| |
|-
| [https://www.idris-lang.org/ idris
|
| |
|-
|
|
| [https://github.com/itchio/itch/issues/2356 will not fix
| You can move the Game install location in the app settings.
|-
| Java OpenJDK
|
| [https://bugs.openjdk.org/browse/JDK-8290140
|
|-
| Java OpenJFX
|
|
|
|-
|
|
| [https://github.com/johanmalm/jgmenu/blob/4e45d04502fc5f77392bef0ff33b7bada0cf07d1/src/jgmenu_run#L7
|
|-
|
|
| libjitsi#518
| Download dir hardcoded to  rather than  (from XDG user directories)
|-
| Jmol
|
| |
|-
|
|
| [https://github.com/intoolswetrust/jsignpdf/issues/252
|
|-
| julia
| , ,
| [https://github.com/JuliaLang/julia/issues/10016
| The trailing  is necessary. See export JULIA_DEPOT_PATH="$XDG_DATA_HOME/julia:$JULIA_DEPOT_PATH"
 export JULIAUP_DEPOT_PATH="$XDG_DATA_HOME/julia"
|-
|
|
|
| Related Konan issue: [https://youtrack.jetbrains.com/issue/KT-40763
|-
| Kubernetes
|
| |
 export KUBECONFIG="$XDG_CONFIG_HOME/kube"
 export KUBECACHEDIR="$XDG_CACHE_HOME/kube"
|-
|
|
| [https://github.com/RolandRosenfeld/lbdb/blob/eb162aa9da36f699cf821c6487210c7979fcd8ee/TODO#L18
|
|-
| LightDM
|
| | Usually made by the greeter when setting a session. If you use autologin, you can modify  as explained in LightDM#Enabling autologin
|-
| [https://lldb.llvm.org/ lldb
| , ,
| |
|-
| llpp
|
| [https://github.com/moosotc/llpp/issues/180 (repo was deleted)
| Added in 3ab86f0 but subsequently reverted in old:e253c9f1/new:e253c9f1
|-
| LMMS
|
| |
|-
|
|
|
| Maliit Keyboard uses an old, unmaintained library called Presage that creates . In 2024, Maliit Keyboard [https://github.com/maliit/keyboard/pull/146 dropped their Presage dependency but as of version 2.3.1, this has not yet been included in a release. In the meantime, compile the master branch of .
|-
|
|
| |
|-
| [https://www.mathomatic.org/ mathomatic
| ,
|
| History can be moved by using  with the  environment set appropriately.
|-
| MediaWiki
|  and  (if $HOME is defined)
|
| If $HOME is not defined:  and .

Generated by the maintenance scripts eval.php and sql.php.
|-
|
|
| |
|-
| Minecraft
|
| [https://bugs.mojang.com/browse/MCL-2563 will not fix
| Third-party launcher  does not use the legacy path. Others found in Minecraft#Minecraft_mod_launchers may also use different paths.
|-
|
|
|
| Upstream has a TODO entry for supporting configuration files under . |-
| [https://www.mongodb.org/ mongodb
| ,
| | [https://stackoverflow.com/questions/22348604/the-mongorc-js-is-not-found-but-there-is-one/22349050#22349050 This Stack Overflow thread suggests a partial workaround using command-line switch .
|-
| Mono
|
| |
|-
|
|
|
| Like , many programs expect this file to be here.  These include projects like curl (), ftp (), s-nail (), etc.  While some of them offer alternative configurable locations, many do not such as w3m, wget and lftp.
|-
|
|
| [https://github.com/nim-lang/nimble/issues/217
| Nimble will [https://github.com/nim-lang/nimble/#configuration try to load  at startup, set  there. You will have to change  in the Nim compiler configuration file as well.
|-
|
|
|
| The project is not currently maintained
|-
|
|
|
|
|-
| Ollama
|
| | Model locations can be set with:

Source: [https://github.com/jmorganca/ollama/pull/897
|-
|
|
| [https://github.com/OpenShot/openshot-qt/issues/4477
|
|-
| OpenSSH
|
| won't fix
| Assumed to be present by many ssh daemons and clients such as DropBear and OpenSSH.
|-
| palemoon
|
| |
|-
|
|
|
|
|-
|
|
|
| A  flag exists, but can only be set relative to .
|-
| [https://perf.wiki.kernel.org/index.php/Main_Page perf
|
|
| Hardcoded in tools/perf/util/config.c. Commit: |-
| perl
| ,
| [https://github.com/andk/cpanpm/issues/149
| Perl5's CPAN expects
|-
|
|
| | Partial workaround: [https://github.com/phoronix-test-suite/phoronix-test-suite/blob/ebcde81fcd5cd63956e5f8db5664262b5fd4ceb9/pts-core/pts-core.php#L123
|-
|
|
| |
|-
| various shells and display managers
|
|
|
|-
|
|
| [https://gitlab.com/jeanfi/psensor/-/issues/38
|
|-
|
|
| |
|-
|
|
| [https://github.com/streamlit/streamlit/issues/2068
|
|-
|
|
| |
|-
|
|
| [https://github.com/tensorflow/tensorflow/issues/38831
| The issues is for  module
|-
|
|
|
| Fallback to  if  does not exist.
|-
| Qt Designer
|
| | Fixed in upstream, scheduled for release with QT 7 (see Discussion link)
|-
| R
|
|
|
 R_HOME_USER="$HOME/.config/R"
 R_PROFILE_USER="$HOME/.config/R/profile"
 R_HISTFILE="$HOME/.config/R/history"
|-
| [https://rednotebook.sourceforge.net/ RedNotebook
|
| |
|-
| [https://remarkableapp.github.io/linux.html Remarkable
|
|
|
|-
|
|
| will not fix
|
|-
| repo
|
| |
|-
| rpm
|
| [https://github.com/rpm-software-management/rpm/issues/2153 Backlog
| Workaround is to use --rcfile and --macros however this come with sideeffects.
|-
|
|
|
|
|-
| SANE
|
|
|  creates a  file there
|-
|
|
|
|

Note that this requires root privileges and will change the location of  for all users. This can be mitigated by checking for an existing  inside the  form.
|-
| SeaMonkey
|
| |
|-
| [https://signal.org/ Signal Desktop
|
| | Currently keeps messages in
|-
| Snap
|
| [https://bugs.launchpad.net/ubuntu/+source/snapd/+bug/1575053
|
|-
| Solfege
| , ,
| |
|-
| [https://spamassassin.apache.org/ SpamAssassin
|
|
|
|-
| Steam
| , ,
| | Many game engines (Unity 3D, Unreal) follow the specification, but then individual game publishers hardcode the paths in [https://www.ctrl.blog/entry/flatpak-steamcloud-xdg Steam Auto-Cloud causing game-saves to sync to the wrong directory.
|-
|
|
| |
|-
| [https://storybook.js.org Storybook
|
| |
|-
|
|
| [https://github.com/Stremio/stremio-features/issues/268
|
|-
| sts4
|
| | Pass JVM arg
|-
|
|
| [https://sourceforge.net/p/sweethome3d/bugs/1256/
|
|-
| TeamSpeak
|
|
|
|-
|
|
| |
|-
|
|
|
|
|-
| [https://gitlab.archlinux.org/remy/texlive-localmanager tllocalmgr
|
|
|
|-
|
|
|
| Use fork  instead. The fork will use
|-
|
|
|
|
|-
| vimperator
|
| |

|-
|
|
| [https://github.com/saulpw/visidata/issues/487
|
|-
|
|
| |
|-
| [https://github.com/TibixDev/winboat winboat
|
| |
|-
| [https://w1.fi/ wpa_cli
|
|
|
|-
|
|
|
|
|-
|
|
| |
|-
|
|
|
| For the directory , you may consider editing  and modifying the section  following the example config.
|-
| [https://github.com/XVimProject/XVim2 XVim2
|
| |
|-
|
| , ,
| [https://github.com/robbert-vdh/yabridge/issues/191 will not fix
|
|-
| YARD
|
| | Would accept Pull Request if anyone want to implement it.
|-
| [https://nmap.org/zenmap/ zenmap
|
| [https://github.com/nmap/nmap/issues/590
|
|-
|
|
|
| Unrecommended: setting the following variable moves the contents of .zoom but the directory itself always gets created. Moreover, it breaks some functionalities eg. being able to start a meeting.
|-
|
|
| |  default location for data can be changed from GUI: Edit -> Preferences -> Advanced -> Data Directory Location -> Custom
|}

## Tools
The tool  detects unwanted files/directories in  which can be moved to XDG base directories. See [https://github.com/b3nj5m1n/xdg-ninja#xdg-ninja README for examples.

The tool  can be used to wrap applications which do not respect the XDG base directories and redirect any unwanted files.

The tool ephemeral can be used to link chromium/electron caches that normally live in  to locations in .

## Libraries
; C
: libXDGdirs
: libxdg-basedir
: C99: Cloudef's simple implementation.

; C#
: Xdg.Directories

; C++
: xdg-utils-cxx
: xdgpp

; Go
: adrg/xdg
: go-appdir (deprecated, archived)
: configdir (deprecated, abandoned)
: kyoh86/xdg (deprecated, archived)

; Haskell
: Officially in directory since 1.2.3.0 ab9d0810ce.
: xdg-basedir

; JVM: Java, Kotlin, Clojure, Scala, ...
: directories-jvm

; Perl
: File-BaseDir (old spec 0.6)
: File-XDG

; Python
: pyxdg
: appdirs (abandoned)
: platformdirs

; Ruby
: bkuhlmann/xdg
: rubyworks/xdg (deprecated, abandoned)

; Rust
: directories-rs
: rust-xdg

; Swift
: swift-xdg

; Vala
: Builtin support via GLib.Environment.
: See , , , etc.

## Tips and tricks
## Hiding unwanted directories
For directories which cannot be relocated, some desktop environments such as KDE allow you to hide them:

 $ echo path >> ~/.hidden

path is the path of the file/directory, relative to the parent directory of .
