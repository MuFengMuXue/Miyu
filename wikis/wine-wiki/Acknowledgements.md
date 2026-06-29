## Thank You!

Wine is the result of many thousands of hours of work by hundreds of
talented people. Development thus far has been going on for 30 years and
we've seen quite a cast of characters come and go. Many people have left
their mark on Wine over the years and for that we'd like to say ***Thank
You!***

Wine's success is also directly attributable to the benevolence of
commercial development. A lot of companies have paid developers to spend
time working on Wine and they've graciously given that work back to the
community. Not very many free software projects are fortunate enough to
have paid staff tackling tough problems.. we are.

### [CodeWeavers](https://www.codeweavers.com/)

CodeWeavers' mission is to make Linux a Windows® -compatible operating
system. To that end, they've hired some of the best talent in the Wine
community. In fact, many of the large projects recently undertaken by
Wine have started as initiatives by CodeWeavers. Some of the different
areas they've worked on include TrueType fonts support,
internationalization and Unicode, Microsoft Installer support, DCOM
support, DLL separation, and gazillions of bug fixes. In 2004
CodeWeavers hosted WineConf2004 at their offices in St. Paul, Minnesota.

### [Corel](https://www.corel.com/)

Corel dedicated a team of paid engineers to the Wine project in 1999.
They focused on adding functionality to Wine that let Corel
applications, such as WordPerfect, CorelDRAW, and Quattro Pro run on
Linux and be ported as native Linux applications. In the past, Corel had
relied on conventional porting techniques to move some of its
applications (Corel WordPerfect 8) to Linux. This provided a fast way
to get these applications to Linux, but meant that porting had to be
repeated with each new version. Improving Wine and compiling with
Winelib allowed them to consolidate codebases. While Corel ultimately
moved on to other projects, they definitely had a positive effect on
Wine.

### [Google](https://wwww.google.com/)

Google's been involved with Wine since January 2006 when they contracted
CodeWeavers to improve Wine's ability to run Picasa. Google also
contracted CodeWeavers to improve support for Adobe's Photoshop CS2.
Additionally, Google interns have improved many areas of Wine including
widl, gdiplus, msi, crypt32, BITS, oleaut32, and riched20.

For more information regarding Google sponsored improvements to Wine,
see [1](https://code.google.com/opensource/wine.html) and
[2](https://winehq.org/pipermail/wine-devel/2008-February/062550.html).

Even further, Google's [Summer of Code](https://code.google.com/soc/) has
sponsored a number of student projects. See [Previous Summers of
Code](Previous-Summers-of-Code).

### [Macadamian](https://www.macadamian.com/)

Macadamian was subcontracted by Corel to improve several areas of Wine.
For two years engineers spent time improving Wine's windowing, controls
and dialogs.

### [ReactOS](https://www.reactos.org/)

Wine is at the heart of ReactOS' Win32 support. Initial work improved
Wine's portability by cleaning things up so MinGW could compile it. From
there, a considerable amount of effort was spent improving Wine's
shell32 infrastructure and various controls. The ReactOS team is also
responsible for the [regedit](Commands/regedit) and task manager utilities.

### [TransGaming](https://www.transgaming.com/)

Development efforts at TransGaming, mostly in 2002, improved several
critical areas of Wine. Changes to DCOM, DirectDraw and 2D graphics
support helped new types of programs to install. Later, the widl utility
was donated to act as a MIDL replacement.

## ...And a cast of hundreds

If you haven't seen the [Who's Who list](Who's-Who), check that
out for a list of major contributors. In addition, the following
individuals have spent a considerable amount of time and effort
improving Wine. Also note, contributions to "misc" shouldn't be taken
lightly. In most cases those folks have submitted enough patches that
you can't nail down any particular area of focus.

A complete list of
[authors](https://gitlab.winehq.org/wine/wine/-/blob/master/AUTHORS)
can be found in the source code repository.

| Contributor          | Area                               | Year(s)   |
|----------------------|------------------------------------|-----------|
| James Abbatiello     | misc                               | 1999-2001 |
| Guy L. Albertelli    | controls                           | 1999-2008 |
| Bob Amstadt          | started Wine                       | 1993-1994 |
| Jim Aston            | misc                               | 1999-2000 |
| Warren Baird         | portability/Sparc                  | 2002-2004 |
| Francis Beaudet      | controls                           | 1998-2000 |
| Dave Belanger        | fonts                              | 2003-2004 |
| Maxime Bellangé      | controls                           | 2003-2006 |
| Francois Boisvert    | controls                           | 1998-2000 |
| Vincent Beron        | misc                               | 2002-2006 |
| Uwe Bonnes           | misc                               | 1995-2006 |
| Noel Borthwick       | clipboard                          | 1999      |
| Alastair Bridgewater | COM/OLE                            | 2004      |
| Jacek Caban          | misc                               | 2003-2008 |
| Duane Clark          | misc                               | 2001-2006 |
| Richard Cohen        | programs                           | 1999-2006 |
| Christian Costa      | DirectX                            | 2002-2006 |
| Ulrich Czekalla      | misc                               | 1999-2006 |
| Pierre d'Herbemont   | portability/Darwine                | 2003-2006 |
| Huw Davies           | fonts                              | 1996-2006 |
| Marcelo Duarte       | translations                       | 2003-2006 |
| Jason Edmeades       | DirectX                            | 2000-2006 |
| Steven Edwards       | portability/ReactOS                | 2002-2006 |
| Jakob Eriksson       | testing & debugging infrastructure | 2002-2006 |
| Jonathan Ernst       | AppDB/misc                         | 2004-2006 |
| Susan Farley         | controls                           | 2000-2001 |
| Krzysztof Foltman    | misc                               | 2004-2006 |
| Martin Fuchs         | controls                           | 2000-2006 |
| Peter Ganten         | misc                               | 1999-2001 |
| Abey George          | COM/OLE & windowing                | 1999-2000 |
| Francois Gouget      | misc                               | 1998-2006 |
| Jon Griffiths        | misc                               | 2000-2006 |
| Adam Gundy           | misc                               | 2003      |
| Michael Günnewig     | multimedia                         | 2002-2003 |
| Noomen Hamza         | windowing                          | 1999-2000 |
| James Hatheway       | misc                               | 2000-2001 |
| Dave Hawkes          | misc                               | 2000-2002 |
| James Hawkins        | configuration                      | 2004-2006 |
| Mike Hearn           | misc                               | 2002-2006 |
| Jukka Heinonen       | winedos                            | 2001-2004 |
| John Hohm            | DLL self registration              | 2002-2003 |
| Peter Hunnisett      | misc                               | 1998-2003 |
| Serge Ivanov         | controls                           | 1999-2000 |
| György Jeney         | misc                               | 2001-2003 |
| Alexandre Julliard   | everything                         | 1993-2008 |
| Bang Jun-Young       | portability/NetBSD                 | 1997-2002 |
| Michael Jung         | advapi32/crypt.c                   | 2004-2006 |
| Raphael Junqueira    | DirectX                            | 2002-2006 |
| James Juran          | misc                               | 1998-2002 |
| Rolf Kalbermatter    | shell32                            | 2002-2006 |
| Ove Kåven            | misc                               | 1997-2004 |
| Dan Kegel            | misc                               | 1999-2008 |
| Rein Klazes          | kernel32                           | 1998-2006 |
| Eric Kohl            | misc                               | 1998-2006 |
| Kevin Koltzau        | desktop integration/theming        | 2003-2006 |
| Phil Krylov          | misc                               | 2003-2006 |
| Tony Lambregts       | misc                               | 2002-2006 |
| Juan Lang            | misc                               | 2003-2006 |
| Stefan Leichter      | crypt32 & shlwapi                  | 1998-2006 |
| Hans Leidekker       | misc                               | 2003-2006 |
| Karl Lessard         | X11 driver                         | 1999-2000 |
| Pascal Lessard       | controls                           | 1999,2000 |
| Andrew Lewycky       | DirectX                            | 1996-2002 |
| Juergen Lock         | portability/FreeBSD                | 1999-2000 |
| Robert Lunnon        | portability/Solaris                | 2002-2006 |
| Stephane Lussier     | controls & windowing               | 1999-2000 |
| Pierre Mageau        | controls                           | 1999-2000 |
| Rok Mandeljc         | DirectX                            | 2002-2004 |
| Vitaliy Margolen     | controls                           | 2003-2008 |
| Alberto Massari      | Wininet                            | 2002-2003 |
| Gregg Mattinson      | portability/Sparc                  | 2002      |
| Jörg Mayer           | build fixes                        | 1999-2001 |
| Mike McCormack       | misc                               | 1999-2006 |
| Bill Medland         | misc                               | 2001-2006 |
| Marcus Meissner      | misc                               | 1995-2006 |
| Thomas Mertes        | misc                               | 2003      |
| PaulMillar           | testing & debugging infrastructure | 1999-2006 |
| Andi Mohr            | misc                               | 1997-2006 |
| Chris Morgan         | AppDB/misc                         | 1999-2006 |
| Filip Navara         | controls                           | 2003-2006 |
| Dustin Navea         | documentation                      | 2002      |
| Felix Nawothnig      | misc                               | 2003-2006 |
| Jeremy Newman        | webmaster                          | 2000-2006 |
| Thuy Nguyen          | controls                           | 1998-2000 |
| Andriy Palamarchuk   | misc                               | 2001-2002 |
| Alex Pasadyn         | X11 driver                         | 2002-2004 |
| Dimi Paun            | misc                               | 1997-2006 |
| Gerard Patel         | controls                           | 1998-2002 |
| Sylvain Petreolle    | NLS                                | 2002-2006 |
| Gerald Pfeifer       | portability/FreeBSD                | 1999-2012 |
| Dave Pickles         | wcmd.exe                           | 1998-2001 |
| Ian Pilcher          | PostScript driver                  | 2000-2001 |
| Eric Pouech          | misc                               | 1998-2006 |
| Joseph Pranevich     | DOS support                        | 1998-1999 |
| Alex Priem           | controls                           | 1998-2000 |
| Ivan Leo Puoti       | misc                               | 2003-2006 |
| Paul Quinn           | COM/OLE                            | 1998-1999 |
| Robert Reif          | Multimedia & DirectX               | 2003-2006 |
| Douglas Ridgway      | original webmaster                 | 1997-2000 |
| Robert Riggs         | DirectX                            | 1998-1999 |
| Troy Rollo           | misc                               | 2003-2006 |
| Pavel Roskin         | misc                               | 1998-2006 |
| Paul Rupe            | controls                           | 2001-2003 |
| Sylvain St. Germain  | controls                           | 1998-1999 |
| Ian Schmidt          | misc                               | 1998-2000 |
| Juergen Schmied      | misc                               | 1998-2003 |
| Rob Shearman         | misc                               | 2002-2006 |
| John Sheets          | documentation                      | 2000-2001 |
| Shachar Shemesh      | internationalization               | 2002-2004 |
| Jeff Smith           | winemaker fixes                    | 2002      |
| Gavriel State        | DirectX & X11 Driver               | 1998-2002 |
| Michael Stefaniuc    | misc                               | 2001-2006 |
| Norman Stevens       | windowing                          | 1998-1999 |
| Aric Stewart         | misc                               | 2000-2006 |
| OliverStieber        | DirectX                            | 2004-2006 |
| Patrik Stridvall     | tools                              | 1998-2005 |
| Bertho Stultiens     | Wine resource compiler             | 1997-2000 |
| Hidenori Takeshima   | DirectShow                         | 2000-2002 |
| Joshua Thielen       | winemine                           | 1999-2003 |
| Adrian Thurston      | misc                               | 1999      |
| Dmitry Timoshkov     | misc                               | 1999-2008 |
| Luc Tourangeau       | controls                           | 1999-2000 |
| Sergei Turchanov     | misc                               | 1998-2003 |
| Greg Turner          | misc                               | 2002-2004 |
| Lionel Ulmer         | DirectX                            | 1998-2006 |
| Ge van Geldorp       | controls                           | 2003-2006 |
| Klaas van Gend       | print dialogs                      | 1999      |
| Michael Veksler      | build fixes                        | 1995-2000 |
| Brian Vincent        | Wine Weekly News                   | 2001-2006 |
| Paul Vriens          | misc                               | 2004-2006 |
| Ferenc Wagner        | testing & debugging infrastructure | 2003-2006 |
| Thomas Weidenmueller | misc                               | 2004-2006 |
| Ulrich Weigand       | testing & debugging infrastructure | 1998-2001 |
| Jeremy White         | CodeWeavers CEO                    | 1997-2008 |
| Lawson Whitney       | misc                               | 1997-2003 |
| Tom Wickline         | documentation                      | 2002-2006 |
| Martin Wilck         | Winsock                            | 2002-2003 |
| Alexander Yaworsky   | advapi32                           | 2004-2006 |

## See Also

- [Who's Who](Who's-Who)
