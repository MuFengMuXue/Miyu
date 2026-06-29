# Fbpad

fbpad is a small framebuffer terminal that manages many terminals through single character tags. It is exceptionally lightweight, being written in C and using its own font format, tinyfont, which avoids xorg font dependencies. fbpad optionally supports 256 colors, bold fonts, and saving the framebuffer contents to memory, all which combined make fbpad a viable alternative to the X server for many purposes.

## Installation
Install the  package, which by default imports the "bold" and "scrsnap" branches of fbpad, which add in 256-colors and bold fonts, and saving the contents of the framebuffer, respectively. fbpad is customized via a  file, and edits to the  file are incorporated into fbpad after recompiling fbpad, using the command .

## Configuration
Users most likely will want to edit the definitions in the  for fonts (more on this later), , , and  prior to use, to their preferred programs.

dwm users should have no problems accustoming to fbpad. fbpad-specific keybindings are initiated with the modifier key, which is hardcoded as the  key, just like in dwm.  and  switch between terminals in an open tag,  switches to the last open tag, and  shows the list of open tags, to name a few. Users comfortable with manually patching source code can edit the  file to edit/add keybindings.

If you re-compile fbpad often, you would probably like to be able to reload fbpad without having to manually re-launch it. The following code starts fbpad post login in tty1 and will reload it if you quit fbpad with .

Place this at the end of your shellrc file.

## Tag Colors
The default background of the list of tags is hardcoded as white, the foreground of empty tags as black, the foreground of fully occupied tags as green (each tag may contain two terminals), and the foreground of tags that are not fully occupied as blue. This color scheme clearly is not for everyone, but this is easily remedied with the following patch:

{{bc|1=
--- a/fbpad.c	2011-11-11 13:02:22.834825518 -0500
+++ b/fbpad.c	2011-11-11 13:04:07.016043271 -0500
@@ -110,7 +110,7 @@

 static void showtags(void)
 {
-	int colors= {15, 4, 2};
+	int colors[ = {8, 2, 9};
 	int c = 0;
 	int r = pad_rows() - 1;
 	int i;
@@ -128,7 +128,7 @@
 			nt++;
 		pad_put(i == ctag ? '(' : ' ', r, c++, FGCOLOR, BGCOLOR);
 		if (TERMSNAP(i))
-			pad_put(tagsr, c++, !nt ? BGCOLOR : colors[nt, 15);
+			pad_put(tagsr, c++, !nt ? 8 : colors[nt, BGCOLOR);
 		else
 			pad_put(tagsr, c++, colors[nt, BGCOLOR);
 		pad_put(i == ctag ? ')' : ' ', r, c++, FGCOLOR, BGCOLOR);
}}

To use, replace "8" with the desired color for empty tags (in both instances), "2" with the desired color for not fully occupied tags, and "9" with the desired color for fully occupied tags, where the colors 0-15 are defined in the  file. This patch also makes the default background color the background color of your terminal, which the writer finds to be a more natural choice.

Note that the second "8" is the color for tags for which fbpad saves the framebuffer contents. If you choose to define  as , then you will want your default foreground color and the color for saved tags to be the same, i.e. "8" in both instances. Otherwise, you may define  as a concatenated string of the tags to be saved, and change the second "8" to the color you wish to indicate saved tags by. The writer herself saves all tags for convenience.

Save the patch as , add  to your source array, and the following line to the  after the line that copies the  file:

 patch -p1 -i "${srcdir}/${_gitname}-tagcolor.diff" || return 1

## Fonts
The font format for fbpad is the "tinyfont", and there exists a utility, , which converts TTF files to the tinyfont format. You will need to edit the  file in the fbpad-mkfn build directory to point to the TTF file of your desired font. For instance, if the font file  was located in  directory, you would edit line 10 of the  to look like the following:

 {"/home/archie/.fonts/MonteCarloFixed12.ttf", 6},

if your username was "archie", and the font size of Monte Carlo you wished to create was size 6. Delete other font lines you see other than this one, unless you wish to supplement your font with the glyphs from another font, in which case, add lines like the one above for your other TTF fonts.

Then, rebuild and reinstall the package with your customized settings.

After installing fbpad-mkfn, the following command creates a tinyfont file:

 $ fbpad-mkfn > MyFont.tf

Remember to edit your  to point to the directory where you save your . If your font also has a bold face, repeat the process of editing the fbpad-mkfn  file, this time specifying the location of the boldface TTF file in the ft2tf , rebuilding with makepkg, and adding the final boldface tinyfont location to your fbpad .

Also note that some fonts might require modification of the  and  to have the proper width and height, respectively.

## Color Support
By default, the AUR package installs the custom terminfo for fbpad, but you will need to add  to your shellrc to take advantage of the 256 color support. Clearly, commands not spawned in your default shell (for instance, those for  and ) will not read your shellrc file, so you will need to edit their definitions in your  file to have the commands for  and  run in a parent shell. For instance, the author of this article, who uses zsh, changed the default command for  from:

 #define MAIL		"mailx"

to

 #define MAIL		"zsh -i -c mailx"

Additionally, to have colors with the  command, "fbpad-256" needs to be added to the list of terms that  knows can handle color. Per the , run the following command in your shell:

 $ dircolors --print-database | sed '/^TERM linux$/aTERM fbpad-256' >$HOME/.dircolors

and add  to your shellrc file so that the custom dircolors file, with the fbpad-256 term added, may be loaded.

## Usage
The following are examples of how some general desktop needs may be implemented in fbpad.

## Copying Text
As everything is done mouselessly in fbpad, to copy text, users can make a "screenshot" of all the text on the screen with the  command. This will save all viewable text to the file . Then, if your shell supports editing the commandline with vim (for instance, the edit-command-line ZLE function in zsh), you can open the  file as a new buffer in vim and use its copy keybindings to paste the needed text into your original buffer. Emacs users probably can adopt a similar scheme to copy text.

## Watching YouTube
If one is using MPlayer with the video output driver set to ,  can be used for searching YouTube and watching with MPlayer from the commandline in fbpad. Alternatively, one can add the following script as an external browser in the commandline web browser , and launch playback of videos from YouTube websites with one's media player of choice. The script below employs , a lightweight media player also written by the author of fbpad, and , a simple program, that, rather UNIX-like, functions solely to convert YouTube URLs into directly watchable URLs.

Save the file in your , and add it as an external browser to w3m by opening w3m, hitting the  key to edit options, and edit the "External Browser" field under "External Program Settings" by entering in the field "youtube.sh". Hit "OK", and you are done. Now, when wishing to watch a video, with YouTube open, hit the  key, and the video will begin streaming instantly in fbff.

## Recommended Programs
Here are a few recommendations for programs that enhance the usability of a framebuffer-based desktop:

*  - a dynamic virtual terminal manager (think dwm, but for the console)
*  - a framebuffer screenshot grabber
*  - an ffmpeg-based media player
*  - a MuPDF-based PDF viewer, optionally supports DjVu or rendering via poppler
*  - an image viewer
* GNU Screen - a terminal multiplexer
*  - a commandline web browser
