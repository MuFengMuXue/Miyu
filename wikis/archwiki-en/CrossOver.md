# CrossOver

CrossOver is the paid, commercialized version of Wine which provides more comprehensive end-user support. It includes scripts, patches, a GUI, and third-party software which may never be accepted in the Wine Project. This combination makes running Windows programs considerably easier for those less tech-savvy.

## Installation
In this article it is suggested that you install the trial version of crossover.
Install  package.

## Usage
If installed by a user in single user mode, Crossover binaries will be located in . Windows applications and configuration files will be placed in .

If installed with root privileges in multi-user shared mode, Crossover binaries will be located in . Each user's bottles will be placed in .

Some desktop environments like KDE may have automatically placed menu entries as part of the installation process.

Installed programs should be located under a new menu entry called Window Applications.

## Troubleshooting
There is also a way to generate a log file to assist you in tracking down errors that may be preventing you from running your desired Windows application(s). Follow the menu path CrossOver > Run a Windows Command > Debug Options and click the "+" sign to expand the options. Click the "Create log file" checkbox. Enter the command you would use to run your Windows application in the "Command" text box. You can use the browse button, if you are not sure what to enter, to navigate to your Windows application. CrossOver will prompt you for a location to save the log file. Choose your location and press enter to have Crossover generate the log file in it.

Although the  library was not shown in the cxdiag list of missing libraries - it did appear in the log file. The library belongs to the  package. If you are having problems getting your application to run, check its installation status.
