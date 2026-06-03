# Writing Tasks for Wine

In the long run, documentation and coordinating development can be just
as important to a software project as coding. Even if you don't feel
comfortable programming, there are still many places where Wine could
use your help. Language skills are the primary need for maintaining the
wiki, translating different portions of the project, and writing good
documentation. Understanding the actual code that makes up Wine should
only be necessary if you want to help make documentation for developers.

## Writing Documentation

### README and Manpages

Documentation included in Wine's source code includes the README file
(included in the top level of the [Wine git
tree](http://gitlab.winehq.org/wine/wine)), translations of the
README in the documentation/ directory of the Wine source tree, and
various manpages, which can be found in the same folder as the component
they document (most can be found in the tools/ directory, but the
manpage for wine itself is located in loader/).

### Wiki

Much of Wine's documentation for both users and developers has been
ported to this wiki, including the various
[guides](Documentation). Keeping the wiki
up-to-date by clearing out abandoned and out-dated content, or
resolving contradictory statements, gives the wiki a much higher
signal-to-noise ratio and makes it easier for both developers and
users to find what they're looking for. Editing the wiki just requires
writing in Markdown syntax. Follow the instructions below to request
edit access to the wiki.

#### Getting access to the Wiki

To edit Wiki pages, you will need to request Developer access to the
corresponding project on Gitlab.

To do this, first [create an
account](https://gitlab.winehq.org/users/sign_up). You'll need to
validate your email address.

Note: Wine uses a **real name** policy on committed changes, and this
also applies for Wiki changes. Please use your real name when creating
your Gitlab account. Accounts using an alias will not be approved.

You can then request Developer access
[here](https://gitlab.winehq.org/wine/wine/-/project_members/request_access).

#### Editing the Wiki

Once you have edit access, you can modify Wiki pages or create new
ones. Please see the [Gitlab
documentation](https://docs.gitlab.com/ee/user/project/wiki/) for more
information about Gitlab Wikis.

## Translating

Translating Wine and its documentation are a high priority. See
[Translating](Translating) for more information on
translating Wine's dialogs and internal resources. In addition,
translations are needed for documentation on the website, including this
wiki.

### Translating Static Web Content

Translating static web content requires some comfort with the terminal.

The procedure for updating the website (eg adding a translation) is to
first create a fork of the [git repo of the
website](http://gitlab.winehq.org/winehq/winehq):

```sh
git clone https://gitlab.winehq.org/winehq/winehq.git
```

Translate individual pages located in **templates/en** and place them
in **templates/xx** (where xx is the language code). After that, make
a series of git commits (one per page is probably good), push it to
your fork, and [submit a merge request](Submitting-Patches).

For help with git, see the [Git Wine Tutorial](Git-Wine-Tutorial)

### Translating the Wiki

To translate a Wiki page to a new language, you need to work from a
git clone of the Wiki repository. The command to do this is:

```sh
git clone git@gitlab.winehq.org:wine/wine.wiki.git
```

See the [Gitlab
documentation](https://docs.gitlab.com/ee/user/project/wiki/#create-or-edit-wiki-pages-locally)
for more details about cloning the repository.

Once you have a local clone, you should make a copy of the English
version of the page you want to translate, into the appropriate
subdirectory for your language. For instance, to translate the
[Download](Download) page to Japanese, you would do

```sh
cp Download.md ja/Download.md
```

It is important to keep the exact same file name as the English
version. You can create the directory for your language if it doesn't
exist yet.

You should then run the `update-translations` tool in the top
directory to update the **Translations** link at the top of all the
translations of that page:

```sh
./update-translations Download.md
```

This will add a link like :flag_jp: 日本語 at the top of all the other
translations, and it will add links to the other translations at the
top of your newly created file. You should then commit all the changed
files, and your new file, and push the changes:

```sh
git add Download.md */Download.md
git commit -a -m "Adding Japanese translation of Download page"
git push origin
```

You can now work on translating your new Japanese page.

#### Adding a new language

If you are translating the Wiki to a completely new language that
isn't supported yet, you'll need to add the language to the various
variables at the top of the `update-translations` script
itself. Hopefully the existing contents are self-explanatory.

Don't forget to commit your modified `update-translations` script
along with your new pages.

## See Also

- A site with automated stats on Wine's translation progress: <https://fgouget.free.fr/wine-po/>.
