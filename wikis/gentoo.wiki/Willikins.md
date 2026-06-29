**Willikins** is a bot on the Gentoo IRC channels. It has been built from the [rbot](https://ruby-rbot.org/) scripts and is run by [Robin Johnson (robbat2)](https://wiki.gentoo.org/wiki/User:Robbat2 "User:Robbat2") .

## [Usage]

Use the commands in the private chat with Willikins to reduce the noise on the Gentoo channels, if the answer should not be sent to all.

Either use [/msg willikins help], or **open a query window with Willikins first** and write there [!help].

### [List of common commands Willikins can recognize]

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Command                                                                                                                                                                 Willikins reaction / Explanation
  [!expn cowgroup]                                                             Willikins will list the members of the mail alias cowgroup@gentoo.org
  [!meta app-shells/bash]                                                      List the bash maintainers. Example output: \"app-shells/bash; maintainers: base-system\"
  [!meta -v app-shells/bash]                                                   List the bash maintainers and projects and expands the project members.
  [!note larry I am still working on the patch, it will be ready on Monday.]   Willikins will post a note to larry in query when he sees that larry posts a message.
  [!proj fonts ]                                                               List all members of the project fonts.
  [!devaway larry]                                                             bob: larry has no [devaway](https://www.gentoo.org/inside-gentoo/developers/unavailable-developers.html)!
  [!ddep app-arch/star]                                                        No packages have a reverse DEPEND on app-arch/star.
  [!pdep app-arch/star]                                                        No packages have a reverse PDEPEND on app-arch/star.
  [!rdep app-arch/star]                                                        No packages have a reverse RDEPEND on app-arch/star.
  [!time set Europe/Berlin]                                                    Willikins will set the timezone and reply: Ok, I\'ll remember that larry is on the Europe/Berlin time zone
  [!bug 27727 *ANYTEXT*]                                                       Returns a link and short info to the **Gentoo Bugzilla**: [https://bugs.gentoo.org/27727](https://bugs.gentoo.org/27727) \"Larry can NOT be a Cow.\"; \[OLD\] Docs-user, Other; RESO, WONT;jensthiede:docs-team
  [!bugl mozilla 12345]                                                        Returns a link and short info on a bug on **other Bugzilla tracker** like the one of mozilla: [https://bugzilla.mozilla.org/show_bug.cgi?id=12345](https://bugzilla.mozilla.org/show_bug.cgi?id=12345) \"\[DOGFOOD\] Unable to Forward a message received as an Inline page or an attachment\"; MailNews Core, Backend; VERI, FIXE; marina:jefft
  [*ANYTEXT* bug 27727 *ANYTEXT*]                                              In #gentoo-\* channels only, watches normal text for bug references and returns a link and short info to the **Gentoo Bugzilla**: [https://bugs.gentoo.org/27727](https://bugs.gentoo.org/27727) \"Larry can NOT be a Cow.\"; \[OLD\] Docs-user, Other; RESO, WONT;jensthiede:docs-team
  [zilla instance list]                                                        **Lists all bugtrackers which are prepared for the bugl command:** gentoo, xine, sourcemage, redhat, mozilla, kernel, fdo, abisource, apache, kde, gnome, xfce, gcc, binutils, and llvm (some of which don\'t work anymore because they didn\'t add some XML stuff).
  [!help]                                                                      Print the help overview.
  [!help COMMAND]                                                              Print the help for COMMAND.
  [!karma USER]                                                                Print the \"karma\" for USER.
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

** Note**\
Some commands depend on external services and may not respond, if there is a problem with the service.

### [Retired commands]

  ---------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Command                                                                                                    Willikins reaction / Explanation                                                       Notes
  [!seen larry]   larry was last seen 1 year, 3 months, 19 days, 5 hours, 2 minutes and 47 seconds ago   [!seen] was retired because of database corruption but has not been revived (yet?) because of GDPR compliance concerns.
  ---------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------