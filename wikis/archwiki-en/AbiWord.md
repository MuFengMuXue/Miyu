# AbiWord

AbiWord is a word processor that provides a lighter alternative for LibreOffice Writer and OpenOffice Writer, while at the same time providing great functionality. AbiWord supports many standard document types, such as ODF documents, Microsoft Word documents, WordPerfect documents, Rich Text Format documents and HTML web pages.

## Installation
Install the  package.

AbiWord can use multiple spell checking dictionaries, see Language checking.

To fix tiny cursor and misaligned text issues, install either  or  and .

## Templates
AbiWord provides a template system that enables to speed up writing common documents. Templates are provided as .awt files, for AbiWord Template.

Template files are searched inside of  and  folders.

## Using templates
In a new document, choose File > New using Template..., then, in the "New Document" dialog, select one of the templates found and listed, or click "Open" to browse your files for an AbiWord file (not necessarily a .awt file).

## Creating or changing templates
AbiWord allows to make your own template files, with the desired style, text, tables etc.

In order to create/change a template file, simply open a new/existent document, and make the desired changes to this file. Then, use "Save As" menu option to name it as you want, with .awt as extension (e.g. foobar.awt) and save it in  folder. Now, your new template can be accessed in File > New using Template... by its filename (foobar.awt in the given example).

## Mail Merge
You can create a CSV file with your data to be used, and run Abiword from the command line against a template to directly render your final files. See this guide for more details.

## Grammar checking
Enable grammar checking from Edit > Preferences > Spell Checking > Automatic grammar checking.

## Change keybindings
You can change the default keyboard bindings in AbiWord using KeyBindings.

In order to set keybindings, edit  and, inside the  tag, add the desired KeyBindings. For instance, you can add  or

## LaTeX fonts
The package  comes with a function which allows user to insert LaTeX codes in a document. To display mathematics symbols properly, install a font which provides them: see Fonts#Math.
