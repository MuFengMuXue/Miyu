# Ocrdesktop

OCRdesktop is a useful accessibility tool to grab content from the screen as text via OCR technology.

It takes an image of the current window or workspace, prepares it for better results and uses tesseract to recognize text on it. The result is presented in a caret enabled text area, in a detailed list with coordinates and confidence or in the clipboard. It also can emulate clicks on the text. It consists of two main parts:

# The main window: This is a caret browse-able text area with the recognized content. There is a menu bar with many options. Focus the menu with .
# The Macro executor: this is a window where you can choose to Run, Unload, Load or Save the current stored macros and preclicks. You also can skip running a macro by pressing the cancel button. (See #Macros and the preclick concept.)

## Installation
Install the  package. Make sure that you have the corresponding package for your language from the  group installed.

## Configuration
Assign the command  to a shortcut in your desktop environment. You also can use parameters to expand the function of OCRdesktop. For languages other than english, you need to set your language code . Use the tesseract language codes for

Basically, this should work in any desktop environment.

In Gnome you can do this via the Gnome Control Center in the Keyboard window under the Shortcuts tab.

## Usage
Just press the assigned shortcut. With no parameters, OCRdesktop will recognize just the current window and present it in a caret enabled text area.

## View Modes
OCRdesktop provides different view modes. You can toggle between the modes with .

* Browse mode: show all the text in a caret navigable text box. The view presents the layout of the currently recognized content. You can move the caret with the arrow keys.
* Detail mode: This is basically a list where you can see details for any word on the Browse mode. I.e font size, font color, position on the screen (X, Y), confidence of the OCR process and other attributes. Things like font size or color are approximate values because its calculated by the OCR image. Some characters are visually smaller than others, So there is a little difference.

## OCR Language
OCRdesktop is able to use all available tesseract languages with . If no language is set. OCRdesktop will use English.

 $ ocrdesktop -l deu

You can also set more than one OCR language:

 $ ocrdesktop -l deu+eng

## OCR Options
OCRdesktop always upscales the current screenshot 3 times for better results. Besides this, you can use different types of transformations before OCRdesktop attempts to recognize the text. You can start OCRdesktop with the parameter you want, or select the options in the navigation window via the OCR Options submenu of the OCRdesktop menu. After selecting the options, press  to recognize the text again. This is a little trial and error for better results.

## Invert
Inversion of the colors could lead to better results if the colors in the original image cause problems with the text recognition:

 $ ocrdesktop -i

## Grayscale
Here the color is removed overall. We get a range of different tones of gray, which could lead to less confusion of tesseract.

 $ ocrdesktop -g

## Barrier Black White method
This may be the method that most often leads to the best results. gray scale is always active. The different tones of gray will break on a defined value between 0 (white) and 255 (black). Everything less than the defined point will be converted to black. A gray tone equal or greater is converted into white. This leads to a clean image for OCR. No Colours, no noise, no gray scale, just black and white. With this type of image tesseract could also read really bright color fonts (because they are converted into black). The parameter  activates this feature. The parameter  sets the barrier value.  is a integer between 0 and 255. If  is not set, 200 is the default value.

 $ ocrdesktop -b -t 180

## Help
See  and the  for a little help and the available parameters. You can always mix different parameters.

## Recognize current workspace
If you do not want to restrict recognition to the current window, use the  option.

## Analyze color
Tesseract splits the OCRed text into boxes. You can think about, each word as an box with the background color and its font in another color. OCRdesktop can now analyze this colors for you. Currently the Color analyzing is disabled by default. you can turn it on by adding  flag as parameter.

after OCRdesktop comes up, you can move to the word you are interested in and toggle to detail view (see (see #View Modes)) In the detail view there is now a column Color what looks like that:

this means that the 3 most used colors are White (likely the background), Black (likely the font color) and Gray ( some shadow effect). You may notice that the sum of the 3 colors are not 100%. This is because we limit our result to 3 colors by default. there might be others as well some smaller effect or style stuff. you can change this default limit by .

will just return 2 colors like this

## Emulate mouse events
You can emulate clicks on the word at the current cursor position via the Interact menu.

Shortcuts:

* Single left click (): common for selecting/activating entry's
* Double left click (): common for opening entry's in the same window
* Single right click (): open the context menu for the object under the mouse
* Single middle click (): Usually opens an object in a new tab
* Route the mouse over an Object (): used for mouse over events like tool tips

To perform a mouse operation immediately, place the mouse on the word in the text area or list entry (in the list view) and press on the corresponding shortcut.

## Macros and the preclick concept
The concept of preclicks is not easy to understand at first, but it solves a really easy to understand problem.

In most desktop environments, global shortcuts do not work while a menu is open, (for example the file menu in the menu bar at the top of most programs).

Preclicks are basically macros that can be run before OCRdesktop takes its screen shot. This allows you to close all menus and let OCRdesktop click on the menu before it recognizes the window. Preclicks macros are really easy to use. In the Interact menu is a check box Preclick . Set this check box and choose a mouse click that should be performed before OCRdesktop starts the next time, much the same as doing a normal mouse click emulation ( see #Emulate mouse events). After emulating a mouse click, nothing will happen. The next time you run OCRdesktop, it will ask you what to do. You can press Run, so all stored clicks will execute. After that, OCRdesktop takes its screen shot for OCR (with the opened menu). If you now check the Preclick option again the second click will also be stored, (e.g. for opening a sub menu). You can save as many mouse operations as you want. Choose Unload in the macro window to erase the macro, so its lost. If you press Cancel, no mouse clicks are performed, but the main window opens. The macro will not be deleted and you will be asked next time you start OCRDesktop if you want to run your stored clicks.

You can execute an existing macro file stored anywhere on the hard disk by using the  option.

## Emulate keyboard events
You can also fire keyboard shortcuts into the preclick macros. To enter the shortcut recording mode, press  or select the Send Key menu entry in the Interact menu. Now every keystroke you type is appended to the currently active preclick macro. Pressing  will leave the recording mode. Leaving the shortcut recording mode may have a delay of up to 2 seconds. This is a known issue.

## Handle Macros
You can Save, Load, Unload or Run the current macro from the macro menu.

* Save (): save a macro on the file system, in case you need it more often.
* Load (): loading means that this macro will be started the next time OCRdesktop runs
* Unload (): remove the macro from the buffer and prevent it from running. If you loaded the macro from the file system, the original macro file won´t be used
* Run (): close the window an just run the macro now

## Copy to clipboard
OCRdesktop provides the possibility to send the currently recognized content to the clipboard.

This is easily done by specifying the  option.

This opens the main window and sends the content to the clipboard.
If you dont want to open the main window, you could add the "no GUI" option .

Now you have the recognized text in the clipboard and no window appears.

You can also press  when the GUI is open.

## Debug Mode
You can start the debug mode with the  option.

The debug output is send to the std output. So you have to pipe it.
