# Anki

Anki is a spaced repetition system (SRS), a program which allows you to create, manage and review flashcards. Anki is very flexible and also allows the creation of templates. Apps for Android and iOS as well as a web interface can be used to interact with the user's flashcard database. Anki supports addons, written in Python.

## Installation
Install the  package.

By default, cards are synchronized using Anki's web server. Anki 2.1.57+ includes a built-in sync server.

## Flashcards
Flashcards can be obtained by:

* Creating them inside Anki, organized in decks and possibly tagged. Cards can contain audio, pictures and even TeX formulas;
* Downloading them, grouped in an existing shared deck (e.g. top 1000 words in a language);
* Generating them as a .csv file that will be imported in Anki.

## Addons
Anki makes many addons available, which can perform a variety of functions, expanding and personalizing your use of Anki or even setting collaborative decks with AnkiHub. These are third-party and are not checked or vetted by Anki, so only use addons you trust. To install an addon, copy the code from the addon page, go to Tools > Add-ons > Get Add-ons... and paste the code. To manually install an addon file (with a  extension) from sources like github, go to Tools > Add-ons > Install from file.... Some popular addons include Image Occlusion Enhanced and Review Heatmap.

## Tips and tricks
## Free Spaced Repetition Scheduler algorithm (FSRS)
Since version 23.10, Anki natively supports the use of a new scheduling algorithm, based on a variant of the DSR (Difficulty, Stability, Retrievability) model, which is used to predict memory states.

The default FSRS parameters are based on 738 million reviews from 20.000 users and are more accurate in comparison to the standard SM2 algorithm, according to benchmarks.

You can find more information about FSRS in the following GitHub repository Open Spaced Repetition

## Kanji stroke support
Install the  package if you want to display kanji stroke orders in Anki. You have to select this font inside Anki in your deck properties after installation.

## Asian language support
Install the  package and the  package.

Launch Anki, and inside Anki use File > Download > Shared Plugin to download and install the "Japanese Support" plugin, restart.

After creating a new deck, you need to select "Japanese" as the deck model in "deck properties" to have Japanese support. Make sure that the Japanese Support plugin is installed, otherwise you cannot select "Japanese" as the model.

## Self-hosted sync server
AnkiWeb is a proprietary service. If you prefer a self-hosted free (as in freedom) alternative, you can host your own anki-sync server.

Install  and configure it through the  file, according to the instructions at https://docs.ankiweb.net/sync-server.html.

Start and enable .

Configure the Anki client in Tools > Preferences > Syncing. At the bottom of the page enter the URL which your service is listening on.

## Dark theme
Anki UI may be unreadable with dark GTK theme. You may want to enable night mode to fix that (Tools > Preferences... > Night mode).

If you have an older version you may need to install an addon (e.g. 1496166067 and View > Night mode > Enable night mode).

## Troubleshooting
## Unable to launch
The display driver can be adjusted by writing either  or  to  (Qt6) or  (Qt5). If Anki core dumps at launch with error qt: No suitable graphics backend found then setting it to  may resolve:

 $ echo auto > ~/.local/share/Anki2/gldriver

When using the Nouveau driver, only  is supported and it is known to be buggy (see === Wayland ===

Wayland support is available in Anki since [https://github.com/ankitects/anki/releases/tag/2.1.48 v2.1.48. However it is not stable yet and disabled by default. If you want to use it in Wayland anyway, then set some environment variables.

 QT_QPA_PLATFORM=wayland
 ANKI_WAYLAND=1

It may also be necessary to install the  package.

Related bug report: Github issue #1767

## Images falsely showing up in unused media
Anki has a feature to check for unused media and delete them to free up space. When copying images from webpages and pasting them into the card editor, the image is often pasted along with an  attribute inside the  tag. If this or any other attribute which is placed before the  attribute contains a  character, this image will show up in unused media and might get accidentally deleted even if it is still being used.

For example, this image will show up in unused media:

 text" src="image.jpg">

To prevent this, remove any  characters or place the  attribute after the  attribute:

 text">

See the bug report and forum post.

## Official
* Anki manual
* FAQs
* Forums
* Old forums archive
* Knowledge base

## Other
* Guide for creating good cards
* Mnemosyne - Another open-source flashcard program using spaced repetition.
* org-drill - A spaced repetition extension for Emacs org-mode.
