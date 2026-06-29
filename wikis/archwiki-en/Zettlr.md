# Zettlr

Zettlr is a cross-platform markdown editor for writing articles, ebooks, and general content. It is inspired by the Zettelkasten system for note-taking and personal knowledge management. It supports autocorrection, snippets, localization, math formulae, citations, presentations (through reveal.js framework), and custom templates.

## Installation
Install the  package.

## LaTeX
Zettlr makes use of  for exporting from the default markdown to plenty of different formats. That includes PDFs but the exporting is limited to not overtly-complex files. For more elaborate PDFs and better control on the final output, a LaTeX distribution like  is an advised optional dependency.

## Configuration
At first start a directory will be copied into your local Documents directory containing a tutorial. You may follow it by opening the files inside or delete it in case you want to start using Zettlr right away.

Nearly everything can be configured using the menus and the toolbar's buttons. For reference, check an explanation of all the settings. The configuration files are located at .

## Features
## Snippets
Zettlr supports snippets since version 2.0. They allow you to define chunks of text that you need to type often or dynamic variables. Snippets follow the syntax of TextMate and can be then shared with other editors supporting it as well (like VisualStudio Code).

A partial list of snippets is available on the documentation.

## Citations
Zettlr comes with support for citations with the citeproc-js library, similar to 's citeproc-engine or Zotero. Both CLJSON and BibTex citation formats are supported.

For a full tutorial on how to use citations in Zettlr, refer to the relative chapter in the documentation.

## Projects
To facilitate the exporting to PDF or other formats of multiple, connected files, Zettlr uses Projects. Directories where the files of text are present can be converted to Projects' directories by right-clicking on them in the sidebar and selecting "Enable project" from their properties.

## Spell checking and custom dictionaries
Spell checking is supported and enabled by default in Zettlr. Moreover, custom dictionaries in the form of a pair of .dic and .aff files can be added in the preferences. A pretty comprehensive list of dictionaries can be downloaded from this Github page. The supported languages are here.

## Tips and tricks
## AutoCorrect
Autocorrection is supported by default in Zettlr. Some definitions are already present at installation; others can be added in the preferences.

Zettlr supports two autocorrection modes: Word and LibreOffice. The first is more aggressive and automatically attempt to replace words and punctuation that it finds wrong. LibreOffice requires instead the user to press  or  to accept a correction.

## MagicQuotes
MagicQuotes are a feature to use typographically correct quotation marks instead of the default  or . The desired quotation marks can be either chosen from a dropdown menu or pre-selected according to the language with a button.

MagicQuotes are automatically enabled if AutoCorrect is. If it is not desired, but the latter is, set the quotation marks to either  or  so the change will have no effect.

## YAML frontmatter
A default YAML frontmatter can be set by starting a file with three dashes (---) and everything till the closing three dashes will be considered the frontmatter.

Further info can be obtained at the official documentation

## Pomodoro timer
Zettlr comes with an integrated Pomodoro timer, for those who want to write according to the Pomodoro technique, the length of the work, break and short break phases can be selected directly from the button on the toolbar. A set of sound effects to signal the end of each phase is also shipped with Zettlr.

## Readability
A series of indexes of readability is included in Zettlr to analyze the clarity and difficulty of the text of each article. Depending on the type of content you are writing, you can check the Dale-Chall Readability Formula, the Gunning fog index, the Coleman-Liau index, or the Automated Readability Index (ARI)
