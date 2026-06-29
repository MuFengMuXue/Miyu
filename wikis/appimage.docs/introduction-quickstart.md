# Quickstart

This page contains information for users new to AppImage, and want to get started.

## How to run an AppImage

It's quite simple to run AppImages. All you have to do is download them, make them executable and run them. This can either be done using the GUI or via the command line.

### Using the GUI

1.  Open your file manager and browse to the location of the AppImage
2.  Right-click on the AppImage and click the ‘Properties’ entry
3.  Switch to the Permissions tab and
4.  Click the ‘Allow executing file as program’ checkbox if you are using a Nautilus-based file manager (Files, Nemo, Caja), or click the ‘Is executable’ checkbox if you are using Dolphin, or change the ‘Execute’ drop down list to ‘Anyone’ if you are using PCManFM
5.  Close the dialog
6.  Double-click on the AppImage file to run

### Using the Terminal

1.  Open a terminal
2.  Change to the directory containing the AppImage, e.g., using `cd /path/to/directory`
3.  Make the AppImage executable: `chmod +x my.AppImage`
4.  Run the AppImage: `./my.AppImage`

That's it! The AppImage should now be executed.
