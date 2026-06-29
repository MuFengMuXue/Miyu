The Gentoo infrastructure project provides a notification service (AKA devaway) for alerting the community when a developer is unavailable. It is typical for other organizations to handle away notifications via an out-of-office (OoO) notification integrated into an email provider or chat suite. Because Gentoo infrastructure utilizes open source tools (which do not include this functionality), the devaway system was created to fulfills this niche.

The notification is controlled by an [\~/.away] file that is manually created and removed at the beginning and end of the unavailability period. The content of the file should be a string of text with no line breaks. An automatically generated, UTC/Zulu timestamp will be displayed at the end of the message. The timestamp is based off file modification time (visible using [ls -lc] and updatable using the [touch] command).

This developer away notification is hooked in to [unavailable developers page](https://www.gentoo.org/inside-gentoo/developers/unavailable-developers.html) on www.g.o (updated every 15 minutes) and the [special devaway page](https://dev.gentoo.org/devaway/) on dev.g.o.

If a developer is not responding to email, IRC, or another communication, it is a good idea to remember to check the devaway system to see if the developer has left a note concerning their absence.

## Contents

-   [[1] [Usage]](#Usage)
    -   [[1.1] [Creating the .away file]](#Creating_the_.away_file)
    -   [[1.2] [Removing the file]](#Removing_the_file)
-   [[2] [Limitations]](#Limitations)
    -   [[2.1] [Line breaks]](#Line_breaks)
-   [[3] [See also]](#See_also)

## [Usage]

### [Creating the .away file]

The following steps are also documented on [dev.g.o/devaway](https://dev.gentoo.org/devaway/).

`woodpecker $``touch ~/.away # Updates the timestamp on the file to the current time `

`woodpecker $``echo "I'll be away until Aug 14, contact $dev1 or $dev2 in my absence. I will return Aug 30." > ~/.away `

The file of course can be modified using standard text editors such as [nano] or [vim].

### [Removing the file]

After the away period has ended, be sure to remove the file:

`woodpecker $``rm ~/.away`

## [Limitations]

### [Line breaks]

The away message content should not contain line breaks (newline) characters. When a line break character is encountered it will signal the end of the away message and concatenate the rest of the message.

## [See also]

-   [Project:ComRel#Leaves_of_Absence](https://wiki.gentoo.org/wiki/Project:ComRel#Leaves_of_Absence "Project:ComRel")
-   [Project:Infrastructure/Developer webspace](https://wiki.gentoo.org/wiki/Project:Infrastructure/Developer_webspace "Project:Infrastructure/Developer webspace") --- documents how a Gentoo developer can configure their personal webspace on dev.gentoo.org.