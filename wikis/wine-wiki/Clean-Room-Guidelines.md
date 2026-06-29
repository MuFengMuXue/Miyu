Wine developers often run into undocumented behavior or
interfaces in Windows. When this happens, they use [clean-room
design](https://en.wikipedia.org/wiki/Clean_room_design) techniques to
work around the problem without infringing on any Microsoft copyrights.

### Do

Here are some techniques believed to be safe for Wine contributors:

  - :white_check_mark: When trying to understand a Windows API function, write a test
    program that verifies its behavior, and contribute it to Wine's
    conformance test suite.
  - :white_check_mark: It's also ok to look at MSDN (but take it with a grain of salt).
  - :white_check_mark: But play it safe - if a test program will do, don't look at any
    Microsoft doc or headers.
  - :white_check_mark: When in doubt, ask on the wine-devel mailing list!

### Don't

Here's a short list of things for Wine contributors to avoid. It is by
no means a complete list; all contributors need to be thoughtful about
copyrights and avoid violating any law.

  - :x: Don't write a test program that prints out the values of an internal
    table.
  - :x: Don't disassemble Microsoft code.
  - :x: Don't look at any Microsoft source code, even if it's made "public"
    under some license, e.g. don't look at the C runtime library source
    code that ships with their C compiler. Note that as an exception,
    code that is released under the MIT license (or another
    LGPL-compatible license) is OK to look at and copy from (with proper
    attribution).
  - :x: Don't use +relay with native components. In general, try to avoid
    debugging with native components, as that leaks information about
    what function calls those components make.
  - :x: Don't examine debug symbols for Microsoft code.
  - :x: Don't look at ReactOS code either (not even header files). A lot of
    it was reverse-engineered using methods that are not appropriate for
    Wine, and it's therefore not a usable source of information for us[^1].
  - :x: Don't use an LLM tool to generate code. There's no guarantee
    that the training material of that LLM respects our Clean Room
    Guidelines, or that its output is compatible with the LGPL.

[^1]: https://bugs.winehq.org/show_bug.cgi?id=50464#c6

### Quotes

#### Henri Verbeet

*"For what it's worth, the policy I've personally been using has been to
simply avoid unnecessary risk."*

------
