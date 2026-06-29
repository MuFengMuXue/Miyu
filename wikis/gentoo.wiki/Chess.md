[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Chess&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Chess "wikipedia:Chess")

This article helps players explore their options for the classic board game chess.

## Contents

-   [[1] [Configuration]](#Configuration)
    -   [[1.1] [Groups]](#Groups)
-   [[2] [Available software]](#Available_software)
    -   [[2.1] [Engines]](#Engines)
    -   [[2.2] [Front-ends]](#Front-ends)
        -   [[2.2.1] [Eboard]](#Eboard)
        -   [[2.2.2] [Gnome Chess]](#Gnome_Chess)
        -   [[2.2.3] [Scid]](#Scid)
        -   [[2.2.4] [Xboard]](#Xboard)
    -   [[2.3] [All in one]](#All_in_one)
        -   [[2.3.1] [PyChess]](#PyChess)
-   [[3] [External resources]](#External_resources)

## [Configuration]

### [Groups]

Games require the user to be in the games group:

** Note**\
Change `$` to the actual login name of the user intending to play games.

`root `[`#`]`gpasswd -a $ games`

## [Available software]

### [Engines]

  ----------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------
  Name        Package                                                                                                                                                                                                                                                                                                                                                                                 Description
  Stockfish   [[[games-board/stockfish]](https://packages.gentoo.org/packages/games-board/stockfish)[]]   Stockfish is one of the strongest chess engines in the world. It is also much stronger than the best human chess grandmasters.
  Sjeng       [[[games-board/sjeng]](https://packages.gentoo.org/packages/games-board/sjeng)[]]               Sjeng is suitable on easy mode for beginners. Its hard mode plays hard, but induces heavy load on the CPU.
  Crafty      [[[games-board/crafty]](https://packages.gentoo.org/packages/games-board/crafty)[]]            Crafty is another very difficult chess engine.
  Phalanx     [[[games-board/phalanx]](https://packages.gentoo.org/packages/games-board/phalanx)[]]         Phalanx is an engine that is more human like than others. It is extremely difficult. This engine is buggy allowing illegal moves to capture pieces.
  Gnuchess    [[[games-board/gnuchess]](https://packages.gentoo.org/packages/games-board/gnuchess)[]]      Gnuchess is impossibly difficult. Gnuchess has a CLI front-end, or the engine itself can be used for other front-ends.
  ----------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------

  : Chess engines

### [Front-ends]

#### [Eboard]

EBoard is a user-friendly chess client to play against a local chess engine, a remote [Internet Chess Server (ICS)](https://en.wikipedia.org/wiki/Internet_chess_server "wikipedia:Internet chess server") or directly against another Eboard user on a remote computer. In relation to ICS, it has a special focus on the [Free Internet Chess Server](https://en.wikipedia.org/wiki/Free_Internet_Chess_Server "wikipedia:Free Internet Chess Server"). It comes with graphical themes and a chat window when playing remotely.

It is possible to automate Eboard actions [using scripts](https://www.bergo.eng.br/eboard/doc.php?d=6). This is an example of an auto login script that is placed at [\~/.eboard/scripts].

[FILE] **`~/.eboard/scripts`FICS auto login script**

    #!/usr/bin/env perl
    STDOUT->autoflush(1);

    # proof of life to avoid hanging
    print "hello\n";

    # while there is input in STDIN, read a line
    while(<>)
    }

`root `[`#`]`emerge --ask games-board/eboard`

#### [Gnome Chess]

Gnome Chess is a high quality front-end that supports multiple chess engines, 2D graphics and 3D graphics.

`root `[`#`]`emerge --ask games-board/gnome-chess`

#### [Scid]

[Shane\'s Chess Information Database](https://en.wikipedia.org/wiki/Shane%27s_Chess_Information_Database "wikipedia:Shane's Chess Information Database") is a powerful Chess Toolkit. It can interface with XBoard engines (such as Crafty and GNU Chess), and UCI engines (eg. Fruit). Using Scid, one may play games against human opponents (on the Free Internet Chess Server), or computer opponents. Database features include a Move Tree with statistics, Player Information and Photos, and General Searches for specific endings (e.g. pawn vs. rook or rook vs. queen), positions or players.

`root `[`#`]`emerge --ask games-board/scid`

#### [Xboard]

Xboard is a lightweight front-end. Among its many options, it can analyse games and have two engines playing against each other.

`root `[`#`]`emerge --ask games-board/xboard`

### [All in one]

#### [PyChess]

PyChess is a client that comes with its own engine but can also interface with UCI and XBoard engines.

The built-in PyChess engine works really well with difficulty scaling. However, as it written in [Python](https://wiki.gentoo.org/wiki/Python "Python"), it loads the CPU, even on the very easy.

`root `[`#`]`emerge --ask games-board/pychess`

## [External resources]

-   [https://www.freechess.org/](https://www.freechess.org/)