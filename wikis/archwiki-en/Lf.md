# Lf

lf (as in "list files") is a terminal file manager written in Go with a heavy inspiration from ranger.

Outstanding features are server/client architecture (so you can cut in one terminal window and paste in another) and high customization.

Unlike ranger, some features like tabs or windows are intentionally not included and instead left to be handled by window managers or terminal multiplexers.

## Installation
Install the  package.

## Configuration
Copy the default configuration at  to  to use as a template for further customization. Some common features are already included as comments in the configuration example.

For more extensive configurations see the , also see the project wiki.

## Usage
The default keybindings are similar to those of vim with some difference from rangers default, see .

Also see the screencast.

## Tips and tricks
## Transition from ranger to lf
For users who are already used to ranger as a file manager, moving to lf means less default features and a slightly different behavior.

The lf project wiki includes a step by step guide on how to configure lf to add features and defaults from ranger.

## Using rifle file opener
lf can use the file opener rifle which is included in the  package.

Set an environment variable to automatically use rifle to open files in the related applications:

 export OPENER='rifle'

For editing file, you can also set your default editor:

 export EDITOR='vim'

## Previewing files
To automatically preview contents from currently selected files, set a custom previewer script in . It is possible to add a wrapper for the  script from ranger which serves as a good template for customization. There are many other previewers that can be used with lf.

## Sandboxing previews
While the default lf configuration only previews text files, using more complex preview parsers is somewhat dangerous. In case there is a vulnerability in a preview parser like pdftotext, it is possible to use this simple script to sandbox the previewer using  :

Set your previewer to the sandbox script and have your real preview script at :

 set previewer ~/.config/lf/previewSandbox.sh
