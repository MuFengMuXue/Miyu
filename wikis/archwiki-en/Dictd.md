# Dictd

The official website describes dictd as:
:Client/server software, human language dictionary databases, and tools supporting the DICT protocol (RFC:2229).

## Installation
Install the  package.

## Graphical front ends
There are various graphical applications that can access  through the DICT protocol:

*
*
*
*
*

## Usage
Dictionaries can be queried by:

 $ dict word

To query a specific dictionary database, you can use the  flag. To query the English-Spanish database, for example, you can use:

 $ dict -d eng-spa word

Without further configuration, it is likely that dictd will query online databases. See below to set up offline dictionaries.

## Configuration
By default, dictd tries to query offline databases first, then online databases. However, offline databases will not be available unless  is enabled, with locale properly set up and offline dictionaries installed (see below).

The online mode can be disabled by commenting  out in . Conversely, the offline mode can be disabled by commenting  out.

## Locale
By default, dictd comes configured to use the  locale. If your system does not have this locale compiled,  will fail to start without a helpful error message.

It is likely that you want to configure it to use another locale:

## Hosting offline dictionaries
Dictd can be configured to host offline dictionaries by enabling  and dict need to be configured to using  as the server in  or .

First, offline dictionaries need to be installed. Dictionaries are available through the Arch User Repository with the search term . Some popular English dictionaries include:

*  - GNU version of the Collaborative International Dictionary of English
*  - WordNet
*  - Moby Thesaurus

The FreeDict project also provides many bilingual dictionaries compatible with dictd, which are usually available on AUR.

After installation, restart  if needed to access the newly available dictionary. Afterwards, dictionaries can be queried as described above.

## Troubleshooting
## Parse error
The following error:

 /etc/dict/dictd.conf:25: syntax error, unexpected $end
 /etc/dict/dictd.conf:25: #LASTLINE
 /etc/dict/dictd.conf:25:          ^
 dictd (yyerror): parse error
 parse error

Means that  cannot find a dictionary database. These can be added manually to . For example:

 database eng-spa {
 	data /usr/share/dictd/eng-spa.dict.dz
 	index /usr/share/dictd/eng-spa.index
 }

Adds the English-Spanish dictionary installed by . For other dictionaries, copy and paste the above database declaration but make sure to change the database name, i.e. , and also change the  and  paths above to specify the right files.
