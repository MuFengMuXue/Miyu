# Unclutter

Unclutter hides your X mouse cursor when you do not need it, to prevent it from getting in the way. You have only to move the mouse to restore the mouse cursor. Unclutter is very useful in tiling window managers where you do not need the mouse often.

The original Unclutter tool was developed in the early 90s and has not been updated since. It worked by creating fake windows or active pointer grabs, both of which often caused problems. The project was later rewritten in unclutter-xfixes using the Xinput2 and Xfixes X11 extensions which provide the cursor hiding functionality without interfering with any application.

## Installation
Install the  package. It provides the unclutter-xfixes rewrite.

## Usage
Use your .xinitrc file or Window manager/Desktop environment to start unclutter. For example, add the following to your .xinitrc:

 unclutter &

## Alternatives
## xbanish
 is another tool similar to unclutter, hiding the cursor during typing using the Xfixes extension.
