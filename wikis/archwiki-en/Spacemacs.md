# Spacemacs

Spacemacs is an extensible and customizable text editor, built on top of Emacs and using Vim keybindings. The goal of the project is to combine both Vim and Emacs editors, getting the best parts from each. Spacemacs distribution is based on community-driven Emacs config, which greatly extends default Emacs behaviour and adds a lot of additional features.

## Installation
## Install Emacs
Spacemacs is built on top of Emacs, so we need to install Emacs first.
* Install Emacs package

## Backup old Emacs configuration (optional)
If you used Emacs before, be sure to backup your previous config.
 $ mv ~/.emacs.d ~/.emacs.d.bak && mv ~/.emacs ~/.emacs.bak

## Install Spacemacs
To install Spacemacs we need to clone an actual configuration from GitHub, and replace Emacs configuration entirely.
 $ git clone https://github.com/syl20bnr/spacemacs ~/.emacs.d

## Install Adobe Source Pro fonts (optional)
The default font used by Spacemacs is Source Code Pro by Adobe. It is recommended to install it on your system if you wish to use it.
* Install  package
If the specified font is not found, the fallback one will be used.

## Remove Emacs configuration file
Backup (if required) and remove the ~/.emacs file if you have not already. Otherwise Spacemacs will not load since that file prevents Emacs from loading the proper initialization file. You can do this by either renaming it through:
 $ mv ~/.emacs ~/.emacs.bak
Or you can just remove it without backing it up:
 $ rm ~/.emacs

## Run Spacemacs for the first time
Now it is time to launch Spacemacs.
 $ emacs

For the first time you will be asked for features that should be installed. All the choices are alternatives, so something should be selected in any case. This choices affects some Spacemacs behavior and hotkeys. It is recommended to choose default values, just hitting Enter.  Defaults are pretty optimized and you can always change them later.

When you finish with the questions, Spacemacs will download and install all the required packages. It may take a few minutes. Spacemacs may seems frozen at this time, but it is okay.

## Running Spacemacs
To start spacemacs simply run:
 $ emacs
Spacemacs will be ready to work when there are no '...' operations in the bottom bar would be displayed.

## Daemon mode
Spacemacs can also be launched in a daemon mode. Daemon mode allows to initialize editor once, and connect to it later, without re-reading configuration file. It can be useful, when you have massive configuration file, so the initialization sequence would be completed only once. You would be able to connect immediately any time later then.

To run Spacemacs in daemon mode:
 $ emacs --daemon=instance1

Then you can connect to  later, using emacsclient:
 $ emacsclient -nc -s instance1

## systemd module
You may want to create a systemd module to run the emacs daemon. Note, due to security concerns stemming from community ELPA packages among other reasons, running the daemon as a user-privileged systemd user module is recommend as described here.

Create an emacs user systemd service file such as:

Edit your Emacs/Spacemacs desktop file as the following. Please note the changes to Exec. The rest is just nice aesthetics.

Then do a daemon-reload and start the  user unit.

Check to make sure no errors occured. If you have already been mucking around with emacs running as a daemon and get errors, I recommend enabling the user emacs service we just made and reboot. It happened to resolve my issues. It might also be useful to check your user  unit status. Then, if successful, enable the user unit for persistence.

Upon completion, you may start emacs via your DE launcher and enjoy significantly reduced loading times, however emacs still does not instantly open on even very powerful systems. You may also alias the following command if you prefer. "instance1" may also be renamed as well but be sure to match the daemon's name in the service file as well.

 $ emacsclient -nc -s instance1

## Usage
Using Spacemacs may be tricky for the first time, especially for complete beginners. However, your efforts will be rewarded. Only a few key concepts are required to perform basic tasks.

You can always exit Spacemacs by typing ''':q=== Built-in Tutorial ===

You can always run Spacemacs built-in tutorial by pressing  when in Spacemacs.

## Basic Concepts
## Prerequisites
In order to explain the basic concepts we need some text to play with. Let us generate it first. Please, do not mind if the commands are unclear right now, you do not need to know them at the moment.

# Run Spacemacs
# Press  to create new empty buffer
# Press  to insert some text

You should see nine lines of generated text as the result. Use them to experiment with the commands described in the next sections.

Now we can move closer to a concept named states.

## Editor states
The major difference between Spacemacs and regular text editor is states. Each state changes the way how the editor works. For example, there is an insert state, where you are able to enter text (like in a regular text editor), and there is a normal state, where all your key presses are used as commands, without changing the actual text.
Only one state can be active at a time. Switching between the states is the key skill to use Spacemacs successfully.

The current editor state is displayed in the left bottom corner. It has the form of a colored rectangle with text "1" (by default). The color describes the current state. There are a lot of states, but only a few of them are used regularly:

* Orange. This is normal state. Used for entering commands and text navigation.
* Green. This is insert state. Used for text input.
* Grey. This is visual state. Used for selecting chunks of text and controlling them.

You can also check the cursor color for the current state.

## Normal state
Normal state is used for text navigation and running commands. You cannot directly enter text in this mode. Instead, you are able to quickly navigate and make any sort of corrections there. Normal state is the default state and its color is orange.

You can always return to normal state by pressing  key or  key sequence if you accidentally leave it.

## Navigation
For basic navigation, the following keys are used:
*  - move cursor by one symbol left
*  - move cursor by one line down
*  - move cursor by one line up
*  - move cursor by one symbol right

It is also possible to navigate between words or even sentences with a single key:
*  - move to next word (beginning)
*  - move to previous word (beginning)
*  - move to the beginning of current sentence
*  - move to the beginning of next sentence
*  - move to beginning of line
*  - move to the end of line

To scroll the pages, use the following commands:
*  - move one page down
*  - move one page up
*  - goto first line of the document
*  - goto last line of the document

You can also use numbers with commands, so they would repeat n times:
*  - move cursor five lines down
*  - move cursor seven words forward
*  - move three pages down
*  - move cursor to line with number 20

There are a lot of commands to be uncovered. Basically, you can navigate between everything in Spacemacs, thanks to Vim-like flow. Check the additional resources to get the details.

## Text manipulation
You can modify text with the following commands:

*  - cut the symbol under cursor
*  - cut the word under cursor
*  - cut the line under cursor
*  - copy (yank) the word under cursor
*  - copy (yank) the line under cursor
*  - paste copied/cut text
*  - replace the symbol under cursor to a

You can also use numeric arguments there.

## Undo/Redo
You can undo and redo changes with the following commands:
*  - undo last change
*  - redo last change

## Insert state
Insert state is used for the text input. It is very close to regular editor behavior. However, the ability to modify text is limited. You will need to switch back to the normal state in order to make corrections. The color of insert state is green.

## Entering
To enter the insert state, press  from the normal state. Your cursor will change to being a green thin line. Now you can type something. When you are done, just leave the insert state by pressing  key or  key sequence.

There are a lot of ways to enter insert mode. The difference, however, is only related to the initial cursor position. It is enough to know just the  hotkey for the first time. But there are also others and they will be very useful once you master them:

*  - enter insert mode before the cursor
*  - enter insert mode after the cursor
*  - enter insert mode at the beginning of the line
*  - enter insert mode at the end of the line
*  - enter insert mode at next line
*  - enter insert mode at previous line

## Leaving
To leave the insert state press  key or  key sequence. You will return to normal state and cursor will change to orange.

## Visual state
This state used for visual text selection. It allows to select text chunks and cut/copy them. The state color is grey.

To enter visual state press  hotkey from the normal mode. Then you can navigate around using normal mode hotkeys with only one difference: text selection. Cursor movements would select text, based on initial cursor position, and you can ank (copy) or elete it later. Remember, that you can use commands like  or  to quickly select words or sentences. Check the  section to get the idea.

You can also press  to quickly select the whole line.

## Visual block state
Visual block state is more powerful version of visual state. It allows to select text in columns. It is similar to multi-cursor concept on regular editors and IDEs. This state can be entered by pressing  hotkey. Then you can navigate with  keys to see the difference.

There is lots of stuff that can be done in visual block state. Refer to the additional resources for this information. This feature is called vim visual block mode in Vim parlance.

## Buffers (Tabs)
Text in Spacemacs is located in areas called buffers. They are very similar to regular editor tabs. You can switch between buffers and create new ones. Buffers are also used by the editor itself to store some information you can inspect later.

## Navigation
To show the list of current buffers press . You will see a new window at the bottom. This is the place where you can inspect, filter, and navigate buffers. Some buffers already exist there, like *Messages* and *scratch*. They are created by the editor and contain some useful information.

The first thing you can do with the bottom window is to type anything into the  field. This will filter buffers. If there are no buffers left after the filtering, you can create a new one by simply pressing "Enter" after your input. The new buffer will be created and opened.

You can also open any buffer by hand. Press  or  to navigate between the lines. Then press  or  to confirm your choice. The selected buffer will be opened.

You can also use some hotkeys from normal state to control buffers:
*  - list buffers
*  - switch to last viewed buffer
*  - switch to next buffer (one forward)
*  - switch to previous buffer (one backward)
*  - save the current buffer to file
*  - close current buffer

## Files
Spacemacs provides two options for file navigation: inline navigation and built-in file manager. Inline navigation is used in Spacemacs confirmation dialogs and it is very similar to the shell one. Build-in file manager is more user-friendly and allows to check the file details. Learning the basics of each is the essential key of mastering Spacemacs.

There also advanced options available, like more powerful file manager and file tree. They are covered in  section.

## Inline (Helm)
Inline navigation available with  hotkey. It uses the window very similar to buffer-navigation one. You can filter and select files there. Just type anything to narrow results, or press  or  for moving the line down and up. Press  to open file or directory, and press  for going backward. Press  to autocomplete the input.

## File manager (Dired)
If you need more visual method, run built-in file manager by pressing  . You can navigate, using + keys, and press  to enter directories and open files.

There are some hotkeys available (refer to dired documentation for more):
*  - quit dired
*  - rename file
*  - copy file
*  - create new directory

## Exiting
Exiting the editor can be achieved with  this will show the multiple exiting methods.

Some available are:

*  Quit current frame -  good for emacsclient frames
*  Quit emacs Kill-emacs
*  Quit emacs and restart resuming layouts
*  Quit emacs and restart
*  Quit emacs and restart with --debug-init

## Advanced concepts
At this step you are able to open files, make changes and save them successfully. Half the way is done, and now you can choose what to master next. There are some sections you may be interested.

## Layers
Layers are one of the strongest features in Spacemacs. Layer is a set of packages and configuration options that greatly extends editor functionality in some way. There are layers for different programming languages, for example, or layers, providing additional tools (like IRC messaging, or integrated web browser). The full list of layers can be found at [https://www.spacemacs.org/layers/LAYERS.html Layers documentation page.

Some layers are already shipped with Spacemacs, the others can be added manually. To do this, open Spacemacs configuration file (), and find  section there. Then simply add selected layer to the list and restart Spacemacs. It will download all the required files on the next start.

Spacemacs will also offer you to install a new layer when you open a file with an already known extension. For example, if you open a  file, the installation of the  layer is offered.

You can customize layer behaviour by overriding some layer-specific variables in your Spacemacs configuration file. Check the appropriate layer documentation to get the details.

## File Navigation
There are some additional tools for file navigation. They may greatly increase the way you use Spacemacs on a daily basis.

## File tree (Neotree)
You can run file tree by pressing . New window opens, accessible with . Standard  navigation is available there. You can change root folder with  and toggle hidden files with . Create new files with  and rename the old ones with . Check Neotree documentation for the details.

## File manager (Ranger)
If you need a full-featured file manager then Ranger may be the best choice. A lot of useful features are available there, like an instant  navigation, inline file preview and ability to manipulate files. It also improves default Dired behaviour () a bit. Install  layer and run it with . Check Ranger documentation for the details. Along with customization options, there are a lot of useful hotkeys.

## Windows
Spacemacs allows you to split the screen into the separate windows. Each window has a personal number and can be accessed with  hotkey, where the  is a selected number. Windows can be splitted individually, so it gives an ability to create complex layouts.

Some of windows hotkeys are presented below. Check the inline help () to get more.

*  - focus window with number 3
*  - split window horizontally
*  - split window vertically
*  - delete window
*  - undo last window action
*  - toggle window fullscreen
*  - enter window transient state

## Configuration
## Troubleshooting
## Slow startup time
If startup time exceeds 10 seconds, there may be a problem with  module. It can be safely disabled on linux systems. Complete the following steps:
# Open Spacemacs configuration file by pressing
# Find  section
# Add  module here, so the final entry would be like
# Save changes with  and restart Spacemacs

## Incorrect minor mode icon fonts
If you see 24ba 24c0 symbols instead of ⒺⓀ or they are too ugly,
then you have to install a good unicode fallback font for these symbols, or disable them by setting  to .
