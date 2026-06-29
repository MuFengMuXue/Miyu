Welcome to the [WineHQ Forums](https://forum.winehq.org/)! We hope you
find your stay here both enjoyable and productive. To that end, the Wine
community has a few guidelines users should *read and heed* before
posting.

## DO

1.  **Read the FAQ.** The [FAQ (**F**requently **A**sked
    **Q**uestions)](FAQ) contains useful information that new Wine
    users typically ask about. Try to make sure your question is not
    already answered in the FAQ before posting. Additionally, see the
    [Wiki Main Page](home) for more sources of information.

2.  **Search the AppDB.** The [Application
    Database](https://appdb.winehq.org/), or AppDB, contains information
    about how specific applications works under Wine. Useful guides,
    tips, and tricks for getting your program working can often be found
    in the AppDB. **Note:** The AppDB is *community driven* and relies
    on feedback from Wine users. Please contribute by providing your own
    test data for applications you've tried under Wine!

3.  **Use Meaningful Subject Lines.** A good subject line can decrease
    the amount of time you spend waiting for a response. Similarly, a
    bad subject line can increase response time or even eliminate
    responses altogether. A good subject line includes at least some
    details about the problems you are experiencing.

    **Examples:**
    - Poor: Please Help!!!
    - Good: GuberChat Deluxe 2.3 hangs when I mouse over the smiley face
    button.

4.  **Include Details.** Basic details to include:
    - Your Wine version (`wine --version`)

      **Time saver:** Get the latest version of Wine and try your
      application with it before posting. You may be told that you
      need a newer version of Wine before further assistance can be
      provided. (Try the [Wine Download Page](Download).)
    - Your operating System (MacOS X, Fedora 7, FreeBSD 5.3, etc)
    - Terminal output. Capture this by running your program in terminal
      with:

      ```sh
      $ wine your_app.exe &> /tmp/log.txt 2>&1
      ```

    - What the problem is. State what is the expected behavior of the
      software is and what the experienced behavior is.
    - What you've tried. Include any changes you may have made to your
      wine configuration such as:
      - Library or DLL Overrides in [winecfg](Commands/winecfg)
      - Non-default registry settings
      - Used [winetricks](Winetricks)
      - If possible, include a URL to a freely (and legally) available
        version of the software, such as a demo, which exhibits the same
        issues.

5.  **Treat others with respect.** This should go without saying and in
    doing so you help promote an atmosphere of excellence within the
    community. See [The Golden
    Rule](https://en.wikipedia.org/wiki/Ethic_of_reciprocity).

## DO NOT

- Post topics which have little or nothing to do with Wine. **The Wine
  HQ Forum is not a general Linux/FreeBSD/Mac OS X/Solaris help forum.**
  You should be familiar and comfortable with your operating system of
  choice and its command line interface.

- Post topics that include Links, references, questions, or information
  about any illegal activity. These include (but are not limited to)
  obtaining pirated software or circumventing DRM. **Your post will be
  summarily deleted, and you could potentially be banned!**

- Post questions about third party applications used to install and/or
  manage Wine. Such applications should provide their own support
  channels. If you have used one, retest in plain Wine before posting
  here.

- Hijack threads. Before posting in an existing thread, please read the
  entire thread. If the problem you are experiencing is not identical to
  the one originally reported, start a new thread for your problem.

- Use excessive punctuation or capitalization, profanity, or so-called
  "[leet speak](https://en.wikipedia.org/wiki/Leet)". Generally these
  things annoy readers and as a result they might be less inclined to
  respond to your question. You could also potentially be banned and
  have your posts deleted. The following examples are frowned upon:

  - MOST IF NOT ALL THE MESSAGE IS IN CAPITAL LETTERS. Please don't.
  - Extra punctuation does not make your plea for help any more
    effective!!!!! Ok?????
  - no 1 wll help u f u do this 4 itz r34lly annoying, take your haxorz
    elsewhere.

## See Also

- [Frequently Asked Questions](FAQ)
- [Wine Wiki Main Page](home)
- [The Application Database](https://appdb.winehq.org/)
- [Wine Documentation](Documentation)
