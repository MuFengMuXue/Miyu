# Translating EasyEffects

## Weblate

You can translate EasyEffects [using weblate](https://hosted.weblate.org/engage/easyeffects/) which makes it possible to translate from your browser. Simply register and start translating.

If you would like to follow a more manual process, and directly interact with the files and make changes with git, continue reading.

## Adding a New Language

Base the new language on the `easyeffects.pot` file. Substitute "`langcode`" with your [language code](https://www.gnu.org/software/gettext/manual/html_node/Language-Codes.html). For more information about the preferred language code format see: [ISO 639](https://en.wikipedia.org/wiki/ISO_639).

### More specific language codes

There are situation when a more specific language code can be used; that is for subsets of languages. For example, there is a locale for [Swedish-speaking Finns](https://en.wikipedia.org/wiki/Swedish-speaking_population_of_Finland): `sv_FI`.

In this example the regular Swedish translation would most likely be be sufficient. It does not matter that there is no `sv_FI` translation available, because the system will fallback to the main one: `sv`.

When should I use it? Simple, when you know there are strings that differ with your subset language, compared to the main one.

## Download

Clone the git repository, then create a new branch for the pull request. One suggestion is to call it `add-langcode` and substitute `langcode` with your language code.

```
git clone https://github.com/wwmm/easyeffects.git
cd easyeffects
git checkout -b add-langcode
```

## Translate EasyEffects

### Using Poedit

You can use a program such as [poedit](https://poedit.net/), which is most likely available in your distribution repositories.

The application should be pretty straight forward to use. When you first launch it, simply choose to add a new translation based upon an existing POT template. You can find the template under `po/easyeffects.pot` in the git repository.

### Manually (Not recommended)

Alternatively, if you really know what you are doing, you could just copy the template, open it in your editor of choice and fill in all lines with `msgstr` in them. Again, substitute `langcode` with your language code.

```
cp po/easyeffects.pot po/langcode.po
vim po/langcode.po
```

## Add copyright (Optional)

If you open the file in your text editor of choice you will find a copyright template at the top:

```
# SOME DESCRIPTIVE TITLE.
# Copyright (C) YEAR THE PACKAGE'S COPYRIGHT HOLDER
# This file is distributed under the same license as the PACKAGE package.
# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
#
```

Simply substitute all of the CAPITALIZED letters with the relevant data. If you don't want to expose your email address, a common anti-spam method is to used `_AT_` instead of `@`

## Do a Pull Request on Github

This is outside the scope of this guide. Here are some links to GitHub documentation:

- https://help.github.com/articles/about-pull-requests/

## Updating your translations

When developers update EasyEffects there may be new strings or old ones might have changed. If not immediately apparent, it will be when you launch the application and notice that some strings are not translated.

### Using Poedit
The simplest way to update is to once again open Poedit, then edit your existing translation file. Go to Catalog > Update from POT-file... and select the original template file. Fill in everything like before and do a new pull request.

### Manually
When adding new English labels to the interface the translation template has to be regenerated through **meson** and **ninja** (if meson is failing on Arch Linux, try **arch-meson**):
```
meson _build
cd _build
ninja easyeffects-pot
```
Now you have to update each translation file with the changes in the new template:
```
ninja easyeffects-update-po
```

A similar procedure has to be done when updating the help:
```
cd _build
ninja help-easyeffects-pot
ninja help-easyeffects-update-po
```