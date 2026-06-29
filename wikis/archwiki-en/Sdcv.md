# Sdcv

Sdcv is a command line dictionary. It provides access to dictionaries in StarDict's format.

## Installation
Install the  package.

## Usage
 can be started from the command line:

 $ sdcv

This gives you a 'shell-like' command-line from which you can query the database.

## Adding dictionaries
There are various places on the web where you can download StarDict dictionaries (e.g. https://web.archive.org/web/20200702000038/http://download.huzheng.org/).

Once you have the appropriate files you can extract them into .

If you do not have root permission, you can set the  environment variable:

 STARDICT_DATA_DIR=$XDG_DATA_HOME

sdcv will look in the  subdirectory so make sure that it is created and then place your dictionary files inside it.

If all is done correctly, sdcv should be able to output definitions for words passed into it.

## Tips and tricks
## Output Formatting
You can use a wrapper around sdcv to conveniently format its output (Source):

 function def() {
 	sdcv -n --utf8-output --color "$@" 2>&1 | \
 	fold --width=$(tput cols) | \
 	less --quit-if-one-screen -RX
 }

An environment variable can achieve similar formatting functionality without the need of a wrapper, affecting all normal calls of :

 SDCV_PAGER='less --quit-if-one-screen -RX'

Piping also works:

 SDCV_PAGER='lolcat -f | less --quit-if-one-screen -RX'
