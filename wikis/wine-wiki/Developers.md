If you're interested in contributing code to Wine, getting started can
be daunting. Wine is an ambitious project, with a large codebase, a lot
of history, and a strong emphasis on code quality. The resources below
should give you an idea of how to start making your way through both the
source code and the development protocols that have evolved over the
years.

## Getting Started

### References and FAQs

- The [Developer FAQ](Developer-FAQ), and [Developer
  Hints](Developer-Hints) are quick reads and a good place to
  begin.
- The [Wine Developer's Guide](Wine-Developer's-Guide) is a
  very-comprehensive guide and the ultimate reference for working on
  Wine.
- Also, all developers should be careful not to violate the [Clean Room
  Guidelines](Clean-Room-Guidelines) (also see relevant
  sections of the [Developer FAQ](Developer-FAQ)). Submitting
  patches based on disassembled Microsoft code or dumped implementation
  details is simply **not acceptable**.

### Working with Other Developers

Sometimes the best way to get some help is to talk with other
developers. While other contributors are often busy, *focused,
well-informed* discussions and questions are encouraged and should not
be ignored.

- Discussions primarily take place on Wine's [mailing
  lists](Forums). The [developers'
  list](https://list.winehq.org/mailman3/postorius/lists/wine-devel.winehq.org/) in particular
  is the place to discuss changes to the software (be sure to subscribe
  before emailing a list, or else your mail will probably be filtered
  out as spam).
- There are a couple of [IRC](IRC) channels, although depending on
  timing and urgency, you may not always get a response.
- You can see what some of the other contributors are working on by
  reading the [Who's Who](Who's-Who) or
  [Acknowledgements](Acknowledgements).
- The Wine project has been overseen by Alexandre Julliard for many
  years now, and as a result, a Wine hacker's informal reputation for
  writing quality code is known eponymously as a Julliard Rank. Although
  earning and maintaining this good reputation is key to becoming a
  successful contributor, the community tries to be helpful and does not
  expect anyone to be perfect, so don't feel discouraged :smiley:
- If you're interested in possibly meeting other programmers in person,
  WineConf is a regular, offline meeting for Wine developers.
- If you are a student with an interesting feature or solution to a
  problem, you might consider applying to work on Wine as part of
  Google's Summer Of Code too.

### Working with the Code

- Wine currently uses [Gitlab](https://gitlab.winehq.org) to manage
  all source code, in order to grab your own copy of the code, look at
  the [Git Wine Tutorial](Git-Wine-Tutorial).
- There is also a short page about browsing the [Source
  Code](Source-Code) online and downloading code for other
  portions of the project.

### Building from Source

You probably want to see the page on [Building Wine](Building-Wine) or
[Building on MacOSX](MacOS-Building).

### Submitting your work

When you're ready to share your changes with everyone, be sure to follow
the guidelines for [Submitting Patches](Submitting-Patches).

## Other Aspects

There are other aspects of the project besides the main program itself,
and these can also sometimes use a programmer's touch.

- For info specifically on testing and bug-hunting, try visiting
  [Debugging Hints](Debugging-Hints) and the
  [Bugs](Bugs) page, especially the section "for developers."
- Things such as the website and documentation also have moving parts
  besides content. For more details, see the pages for
  [Designers](Designers) and [Writers](Writers).
- There are some tips for those interested in [Packaging](Packaging)
  Wine for different distros and platforms.
- Interested in porting the source code of your Windows-native
  application to Unix? Consider looking into
  [Winelib](Winelib-User's-Guide).
