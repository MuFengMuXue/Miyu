# Eclipse

Eclipse it is an open source community project aimed at providing a universal development platform. The Eclipse project is best known for its multiplatform integrated development environment (IDE). Arch Linux packages (and this guide) are specifically related to the IDE.

Eclipse IDE is largely written in Java, but can be used to develop applications in many languages, including Java, C / C++, PHP, Perl, Rust and Python. The IDE can also provide subversion support and task management.

## Installation
Install one of the following packages:

*  for Java EE Developers
*  for Java Developers
*  for RCP and RAP Developers
*  for C/C++ Developers
*  for PHP Developers
*  for DSL Developers
*  for a base platform suitable for complete per-user customization with the built-in Eclipse package manager

You cannot install several of them at the same time as they conflict, see : choose the package above which meets your needs immediately and add support for the additional languages you need through #Plugins.

## Plugins
Many plugins are easily installed using pacman (look Eclipse plugin package guidelines for more information). This will also keep them updated. Alternatively, you can choose the Eclipse Marketplace or the internal plugin manager.

## Add the default update site
Be sure to verify that the default update site for your version of Eclipse is configured so that plug-in dependencies can be installed automatically. Recent versions of Eclipse should already have the default update site set properly. To verify or update, go to Help > Install New Software. The drop-down list for the field labeled as Work with: should list an option named Eclipse Repository with a site that looks like https://download.eclipse.org/releases/2021-09 (for example for version 2021-09). If a default site is not available, you can choose Add to add one. You can find sites for recent versions under https://download.eclipse.org/releases/. To check your Eclipse version go to Help > About Eclipse Platform (or any About option available in your installation).

## Eclipse Marketplace
To use the Eclipse Marketplace, install it, go to Help > Install new software then, switch to the default update site in the Work with section and go to General Purpose Tools > Marketplace Client. Select it, click next, and follow the instructions until you finish. Restart Eclipse and it will be available in Help > Eclipse Marketplace.

## Plugin manager
Use Eclipse's plugin manager to download and install plugins from their original repositories: in this case you have to find the needed repository in the plugin's website, then go to Help > Install New Software..., enter the repository in the Work with field, select the plugin to install from the list below and follow the instructions.

## Updates via plugin manager
Run Eclipse and select Help > Check for Updates. If you have installed them as root as advised in the section above, you have to run Eclipse as root.

For plugins to be updated, you should check to have their update repositories enabled in Window > Preferences > Install/Update > Available Software Sites: you can find each plugin's repository(es) on the respective project website. To add, edit, remove... repositories just use the buttons on the right of the Available Software Sites panel. For Eclipse 4.5 (Mars), check you have enabled this repository:

:https://download.eclipse.org/releases/mars

To receive update notifications, go to Window > Preferences > Install/Update > Automatic Updates. If you want to receive notifications for plugins installed as root, you should run Eclipse as root, go to Window > Preferences > Install/Update > Available Software Sites, select the repositories related to the installed plugins and Export them, then run Eclipse as normal user and Import them in the same panel.

## List of plugins
*
*
*
*
*
*
*
*
*
*

## List of standalone extensions
*
*
*

## Enable javadoc integration
Enabling the javadoc integration allows you to see documentation on methods and classes when you hover over them with your mouse.

## Online version
If you have constant Internet access on your machine, you can use the on-line documentation:

# Go to Window > Preferences, then go to Java > Installed JREs.
# There should be one named "java" with the type "Standard VM". Select this and click Edit.
# Select the  item under "JRE system libraries:", then click Javadoc Location....
# Enter "https://docs.oracle.com/javase/8/docs/api/" in the "Javadoc location path:" text field.

## Offline version
You can store the documentation locally by installing the  package.  Eclipse may be able to find the javadocs automatically.  If that does not work, set Javadoc location for rt.jar to .

## Troubleshooting
## Dark theme
Eclipse supplies a Dark theme which can be enabled in Window > Preferences > General > Appearance and selecting the Dark theme.

The dark theme uses its own colours rather than the GTK theme colours, if you prefer it to fully respect GTK colour settings, then remove or move to backup sub folder all of the .css files from , replacing the  with the appropriate version number.

## Change Default Window Title Font Size
You cannot change the window title font size using the Eclipse preferences, you must edit the actual theme .css files. These are located under  directory, where  is the actual theme version number.

Use a text editor to edit the appropriate file, e.g.  if you are using the "GTK theme".

In this file, search for , and change the font-size to your desired size:

 .MPartStack {
        font-size: 9;
        swt-simple: false;
        swt-mru-visible: false;
 }

## Freshplayerplugin
Eclipse is not compatible with . See https://github.com/i-rinat/freshplayerplugin/issues/298.

## Show in System Explorer does not work
See this guide. Go to Window > Preferences > General > Workspace and change the command launching system explorer. As Xfce user you may like to change it to {{ic|thunar ${selected_resource_uri} }} to open the selected folder with thunar.
