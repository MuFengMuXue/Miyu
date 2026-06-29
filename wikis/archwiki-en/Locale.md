# Locale

Locales are used by  and other locale-aware programs or libraries for rendering text, correctly displaying regional monetary values, time and date formats, alphabetic idiosyncrasies, and other locale-specific standards.

## Generating locales
Locale names are typically of the form , where language is an ISO 639 language code, territory is an ISO 3166 country code, and codeset is a character set or encoding identifier like ISO-8859-1 or UTF-8. See .

For a list of enabled locales, run:

 $ locale --all-locales

Before a locale can be enabled on the system, it must be generated. This can be achieved by uncommenting applicable entries in , and running locale-gen. Equivalently, commenting entries disables their respective locales. While making changes, consider any localisations required by other users on the system, as well as specific #Variables.

For example for German, uncomment  (in addition to  which is commonly used as a fallback for various tools):

Save the file, and generate the locale:

 # locale-gen

## Setting the locale
To display the currently set locale and its related environmental settings, type:

 $ locale

The locale to be used, chosen among the previously generated ones, is set in  files. Each of these files must contain a new-line separated list of environment variable assignments, having the same format as output by locale.

To list available locales which have been previously generated, run:

 $ localedef --list-archive

Alternatively, using :

 $ localectl list-locales

## Setting the system locale
To set the system locale, write the  variable to , where  belongs to the first column of an uncommented entry in :

Alternatively, run:

 # localectl set-locale LANG=en_US.UTF-8

See #Variables and  for details.

## Overriding system locale per user session
The system-wide locale can be overridden in each user session by creating or editing  (usually ).

The precedence of these  files is defined in .

## Make locale changes immediate
Once system and user  files have been created or edited, their new values will take effect for new sessions at login. To have the current environment use the new settings unset  and source :

 $ unset LANG
 $ source /etc/profile.d/locale.sh

## Other uses
Locale variables can also be defined with the standard methods as explained in Environment variables.

For example, in order to test or debug a particular application during development, it could be launched with something like:

 $ LC_ALL=C.UTF-8 ./my_application.sh

Similarly, to set the locale for all processes run from the current shell (for example, during system installation):

 $ export LC_ALL=C.UTF-8

## Variables
 files support the following environment variables.

* LANG
* LANGUAGE
*
* LC_COLLATE
*
*
*
*
*
*
*
*
*
* LC_TIME

Full meaning of the above  variables can be found on manpage , whereas details of their definition are described on .

## LANG: default locale
The locale set for this variable will be used for all the  variables that are not explicitly set.

## LANGUAGE: fallback locales
Programs which use  for translations respect the  option in addition to the usual variables. This allows users to specify a list of locales that will be used in that order. If a translation for the preferred locale is unavailable, another from a similar locale will be used instead of the default. For example, an Australian user might want to fall back to British rather than US spelling:

## LC_TIME: date and time format
If  is set to , for example, the date format will be "MM/DD/YYYY".  If wanting to use the ISO 8601 date format of "YYYY-MM-DD" use:

You can print the current timestamp using your locale date and time format with .

 2.29 fixed a bug,  started showing in 12-hour format, as was intended.  If wanting to use 24-hour format, use .

## LC_COLLATE: collation
This variable governs the collation rules used for sorting and regular expressions.

Setting the value to  can for example make the ls command sort dotfiles first, followed by uppercase and lowercase filenames:

See also === LC_ALL: troubleshooting ===

The locale set for this variable will always override  and all the other  variables, whether they are set or not. If  is set to  or , it will also override .

 is the only  variable which cannot be set in  files: it is meant to be used only for testing or troubleshooting purposes, for example in .

## Troubleshooting
For encoding problems, check Character encoding#Troubleshooting.

## My system is still using wrong language
It is possible that the environment variables are redefined in other files than . See Environment variables#Defining variables for details.

If you are using a desktop environment, such as GNOME, its language settings may be overriding the settings in .

KDE Plasma also allows to change the UI's language through the system settings. If the desktop environment is still using the default language after the modification, [https://bbs.archlinux.org/viewtopic.php?pid=1435219#p1435219 deleting the file at  (previously: ) should resolve the issue.

If you are using a display manager in combination with , follow the instructions in Display manager#Set language for user session.

LightDM will automatically use  to set a user's locale if it is installed. Otherwise, LightDM stores the user session configuration in . It is possible that an unwanted locale setting is retrieved from there as well.

## Using a custom locale causes problems
When installing a locale that is not officially supported (e.g., ), some problems can occur, like dead/compose keys not working in some applications or applications reporting missing locales.
After installing a custom locale, manual intervention is required to resolve these problems.
There are two approaches (replace  with the identifier of your custom locale):

## Set LC_CTYPE
Set  to an officially supported locale (like ), e.g.:

## Modify the Xlib database
Modify the Xlib database by adding the following:

## Metric measurements with US locale
In some tools, like , the unit type is selected based on the  settings; hence, temperatures are shown in Fahrenheit if US locales are used. If you wish to use Metric measurements with a US locale, to get temperatures in Celsius for example, adding  to  should work if the tool searches for  rather than simply the country. == See also ==

* [https://sourceware.org/glibc/wiki/Locales Locales - glibc wiki
* Gentoo:Localization/Guide
* Supposedly 2008, or earlier, Gentoo wiki article
* ICU's interactive collation testing
* Free Standards Group Open Internationalisation Initiative
* The POSIX definition of a locale
* Locale environment variables
