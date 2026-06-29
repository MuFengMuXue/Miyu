Other languages:

[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Worker_-_An_Introduction/tr "Worker - Giriş (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Worker_-_An_Introduction/ru "Worker - введение (100% translated)")

[![A.Worker.Setup.png](/images/thumb/e/e7/A.Worker.Setup.png/650px-A.Worker.Setup.png)](//wiki.manjaro.org/index.php?title=File:A.Worker.Setup.png)

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Installing Worker]](#Installing_Worker)
-   [[3] [What can this Filemanager called Worker do?]](#What_can_this_Filemanager_called_Worker_do.3F)
-   [[4] [Select your Colours, Fonts]](#Select_your_Colours.2C_Fonts)
-   [[5] [Paths & Bookmarked locations]](#Paths_.26_Bookmarked_locations)
-   [[6] [Custom Button Configuration]](#Custom_Button_Configuration)
    -   [[6.1] [Use external applications on files]](#Use_external_applications_on_files)
-   [[7] [Worker is built for those that like to customise]](#Worker_is_built_for_those_that_like_to_customise)
    -   [[7.1] [Backup your worker config & use it elsewhere]](#Backup_your_worker_config_.26_use_it_elsewhere)
    -   [[7.2] [Edit the worker config file directly]](#Edit_the_worker_config_file_directly)
-   [[8] [Making Worker work how you want it to]](#Making_Worker_work_how_you_want_it_to)
    -   [[8.1] [Options, Options\...]](#Options.2C_Options...)
    -   [[8.2] [Built-in Commands]](#Built-in_Commands)
    -   [[8.3] [Sequencing Commands]](#Sequencing_Commands)
    -   [[8.4] [Summary]](#Summary)
-   [[9] [See Also]](#See_Also)

\

# [Overview]

Unfortunately the documentation on Ralf Hoffmann\'s site (he is the creator of Worker, among other app\'s) is incomplete and parts at least are somewhat out of date. You basically work much of how Worker is configured out for yourself without having your hand held. That said, the GUI Worker Configuration Manager is pretty self explanatory.

\

[![Worker.configuration.main.png](/images/thumb/0/07/Worker.configuration.main.png/650px-Worker.configuration.main.png)](//wiki.manjaro.org/index.php?title=File:Worker.configuration.main.png)

\
The Worker Configuration screen shown above, will give you an inkling of the types of configuration options that are available inside of it. Worker is an extremely capable file manager, that may have been inspired by Jonathan Potter\'s brilliant Amiga file manager - Directory Opus 4.\*\*. In many ways Worker exceeds the capabilities of DOpus, though it doesn\'t internally multi-task to quite the same extent that DOpus did.

Ralf has been developing Worker for many years now. You get an introduction to its power on [this page](http://www.boomerangsworld.de/cms/worker/index.html)

\

# [Installing Worker]

Worker is available in the [AUR](//wiki.manjaro.org/index.php?title=Arch_User_Repository "Arch User Repository") as the package `worker`. You can install it in your favorite graphical package manager or by using the command:

    pamac build worker

\

# [][What can this Filemanager called Worker do?]

Worker is usually installed with a pretty bare bones button setup. It is then up to the user to make Worker the way that they want Worker to be. This is done by using the Worker Configuration panel. Which is found by hitting the *C* - **Configuration** in the top left of the Worker window, it is right next to the *A* - **About**.

Worker is incredibly versatile, following is a short list of some of the things that Worker can do:

-   Has buttons that you can configure (the number of too) to run built-in commands.

<!-- -->

-   Run external applications that you have set up to work on one or multiple files that you have selected in one of Worker\'s file list display.

<!-- -->

-   Worker can call applications that don\'t have anything to do with the files that are showing in Worker\'s file list displays.

<!-- -->

-   You can run short or complex scripts that you or others have created.

<!-- -->

-   Combine any number of the aforementioned different types of commands to execute in sequence.

The above barely scratches the surface of what Worker can be configured to do. It is very quick and has barely any other dependencies than X.org.

Custom tasks, ranging from the very simple to the extremely complex all fall within the capacity of Worker.

\

# [][Select your Colours, Fonts]

A good number of screenshots of Worker can be found here: [\[1\]](http://www.boomerangsworld.de/cms/worker/screenshots.html)

As informative as the screenshots shown at the above link are, they don\'t show you what can be done colour wise with Worker. Using various colours to suit your eyes/taste & to make Worker more easily used & more practical, as you can use certain colours to good effect (especially where there is danger, as in the case of commands such as DELETE , Reboot , Shutdown & any buttons that you have set up to use sudo or root privileges one way or another. The first screenshot on this page is a reasonably good example of the use of colours in this way.

Apart from being able to select the main interface colours as shown in the following image, you can also set the number of colours to be used & also modify the colours to suit you.

\

[![Worker.user.interface.colours.png](/images/thumb/c/c1/Worker.user.interface.colours.png/650px-Worker.user.interface.colours.png)](//wiki.manjaro.org/index.php?title=File:Worker.user.interface.colours.png)

\
When you set Worker up, you can select the font & font size that you would like to use. Choosing fonts seems to be the most pre-historic part of Worker, though as of this edit, the choice of font is now much better than it was. Fortunately if you do need/want to do it, after you have done it once, there isn\'t much to do when it comes to resizing fonts thereafter. See this page of the Worker documentation for more on the subject of choosing sizing Worker\'s fonts: [\[2\]](http://www.boomerangsworld.de/cms/worker/documentation/features/fonts.html)

\

[![Worker.font.settings2.png](/images/thumb/3/35/Worker.font.settings2.png/650px-Worker.font.settings2.png)](//wiki.manjaro.org/index.php?title=File:Worker.font.settings2.png)

\

# [][Paths & Bookmarked locations]

You can setup custom Path buttons (the Path bank of buttons is the left hand column in the main button bank) you can have as many **path button banks** as you want, you cycle through these banks by using the right mouse button (RMB).

\

[![Worker.path.button.bank.config.png](/images/thumb/c/c5/Worker.path.button.bank.config.png/650px-Worker.path.button.bank.config.png)](//wiki.manjaro.org/index.php?title=File:Worker.path.button.bank.config.png)

\
Whilst we are on the Path subject, I should mention that you can also use bookmarks to bounce between oft used locations (paths) in your system. The tabs go across the top of each file list window, you move to a list of files in a different part of your system by hitting the tab that will show that list with your mouse pointer & the left mouse button (LMB).

\

# [Custom Button Configuration]

You also can set up the Worker command button bank(s) to suit you. Choose how many rows of them and how many banks (each bank will have the same number of buttons) as well. You cycle to the next main button bank by hitting the bottom bar in the Worker window - it holds the date/time, free RAM, swap usage - though this is somewhat configurable too.

\

[![Worker.button.panel.config.png](/images/thumb/d/d2/Worker.button.panel.config.png/650px-Worker.button.panel.config.png)](//wiki.manjaro.org/index.php?title=File:Worker.button.panel.config.png)

\

It is possible to use the buttons that came as part of the initial Worker install, though it is more common to edit your config to suit your needs. When you see a button in a screenshot that has a \"dog eared\" top right corner, that means that if you use your RMB on it, you will have access to another button option that is hiding underneath. (You could for example have the top button saying **Edit** for editing existing files, & the button accessed via the RMB, underneath, saying **Edit New** for creating new files.)

\

[![Worker.configure.button.own.command.png](/images/thumb/2/21/Worker.configure.button.own.command.png/650px-Worker.configure.button.own.command.png)](//wiki.manjaro.org/index.php?title=File:Worker.configure.button.own.command.png)

\

\

[![Worker.configure.button.own.command.Options.png](/images/thumb/7/7b/Worker.configure.button.own.command.Options.png/650px-Worker.configure.button.own.command.Options.png)](//wiki.manjaro.org/index.php?title=File:Worker.configure.button.own.command.Options.png)

\

## [Use external applications on files]

Even though Worker comes with inbuilt text & image viewing abilities, you can also set Worker up to use more powerful external programs. For exmaple, you could use Geegie to view images. By associating Geegie with the various types of image file types available (using the Worker Configuration GUI), when you double click on an image file in the Worker display, Geegie displays it(you could set different image types to be opened by different image viewing or editing programs if you had the need).

\

[![Worker.file.type.config.png](/images/thumb/0/02/Worker.file.type.config.png/650px-Worker.file.type.config.png)](//wiki.manjaro.org/index.php?title=File:Worker.file.type.config.png)

\
You can then view all of the images in that directory by scrolling the mouse wheel, or tell Geegie to go full screen and play a slide show of the images, or do whatever else Geegie will allow you to do with any of the images in that directory.

If you **R**MB click on the **F3 - Show Pics** button (yes you can easily set up function keys too), you will see, **Edit Pics** (the RMB buttons are all in different colours than the top LMB accessed buttons). If you have an image file highlighted in Worker, then your editor of choice will open up with the highlighted file ready to edit.

This can be done for any type of file on your system that you have a program that you want to use to edit/view it. The **File Type** list included in the Worker Configuration GUI (the list is part shown in an the preceding image) is huge, very highly configurable (something like fourteen different custom user options can be set up) plus you can add custom file types quite easily.

For example, you could use Evince for .pdf files, Firefox for .html files and Leafpad for .txt files. It is possible to setup sudo Leafpad buttons for both creating **New** files & of course to work on existing files. So you can select a config file in the `/etc` and then use the Worker **sudo Leafpad** button on it, which will cause Worker to throw up a terminal window where you have to input your sudo password, then the config file from /etc will be showing in Leafpad & available for me to edit & then save the changes.

You can of course use the buttons to call programs that have nothing to do with any of the files in your Worker display. You can run scripts, simple or complex from a button, as normal user or with root privileges, you can combine applications & scripts & most anything else you can come up with to work in sequence. It is up to your imagination to do what you want to do with Worker.

\

# [Worker is built for those that like to customise]

This is a part of what I really love about Worker. You can make Worker do what you want it to do & not have to put up with having to do things the way someone else wants you to do it.

This is all fine & good, unless you are someone who loves working with windows & icons. Under those circumstances you would find Worker to be just exactly what you don\'t want (you may even think that Worker is pre-historic!).

\

## [][Backup your worker config & use it elsewhere]

You can save your custom `~/.worker/config` file *(it is a **REALLY** good idea to keep a backup of this file)*. Apart from saving your configuration from being lost to corruption or whatever, you can transfer your `~/.worker/config` file to other installations of Linux. You can also edit the `~/.worker/config` file directly with a text editor, which can be useful sometimes.

\

## [Edit the worker config file directly]

For example, if you transfer worker config file to another system that is using a lower resolution monitor, when you then run Worker with your transferred custom config on that machine, the display will be very wrong making Worker pretty unusable. You may not be access the GUI config to modify the font size, as the large fonts have made it impossible to do so (can\'t see/access all the necessary parts of the Worker Configuration GUI).

So you can directly edit the `~/.worker/config` file with a text editor, scroll down to the font section & change the sizes. Save it, restart Worker, go into the Worker Configuration GUI and adjust/fine tune the config to suit the new machine.

If you ever strike this problem, this is the part of the `~/.worker/config` file you need to edit.

    fonts
            xftfonts

By looking at the above you can see that it is the **xfgfonts** section that is where the large 18 -\> 24 size fonts are, so you just make all those numbers suitably smaller, then you can use the Worker Configuration GUI to fine tune your imported settings to suit the new machine.

\

\

# [Making Worker work how you want it to]

The above will hopefully give you more of an idea about how Worker functions, you have to make Worker your own, this doesn\'t happen quickly, but it does get easier once you have understood the basics. You really have to get into the Worker Configuration GUI & have a look around to start to get familiar with it.

For setting up buttons, look at how other buttons are setup, you will start to see that there are certain options that are native to Worker (like the **** in the coming example) that are commonly used when you want to open a file that you have highlighted in the Worker display. The following example (is much clearer & simpler than it looks here, when you are actually looking at it in Worker running on your own system).

\

\

## [][Options, Options\...]

[![Worker.button.config.Option.flags.png](/images/thumb/6/60/Worker.button.config.Option.flags.png/650px-Worker.button.config.Option.flags.png)](//wiki.manjaro.org/index.php?title=File:Worker.button.config.Option.flags.png)

\
There are currently 47 Option flags that can be seen when you hit the **O** at the end of the **program:** field, where you enter in your own command as seen in the above two examples, it is right before **leafpad** .

Of those 47 Options, you probably won\'t to need to use all of them. When you look at what the options can do, you will see that you can get very sophisticated but it isn\'t a requirement.

The previous image shows some of those 47 Option flags in the window on the right hand side of the image.

\

## [Built-in Commands]

Worker currently also has 61 commands built into it. They are listed when you wish to create a new button (and choose the **Add Command** button. The following screenshot shows some of those 61 commands.

\

[![Worker.built.in.commands.png](/images/thumb/5/58/Worker.built.in.commands.png/650px-Worker.built.in.commands.png)](//wiki.manjaro.org/index.php?title=File:Worker.built.in.commands.png)

\

## [Sequencing Commands]

You can also have more than one command listed in sequence. Meaning that when setting up a button to do what you want, after the creation of a command, instead of OK\'ing out of that window, you can add another command. You can continue to repeat this as desired.

The above image already has a command (it uses Geegie to show an image that has been selected in one of Worker\'s file lists), you can add more commands if you need to sequence them for some reason. The commands can be any mixture of both built-in commands and external programs.

\

## [Summary]

The Worker filemanager is certainly not one that everyone would want to set up & use. Though for those of us that it does suit, the more we use it, the more we get to know Worker, the more we configure it to be just the way we want it to be.

It is very easy to change the applications that we call from inside of Worker, that we use to work on whatever kind of files in whichever way we have chosen. Worker doesn\'t mind, that is what it is made for (well, a part of what it is made for).

\

# [See Also]

You can post any related feedback in the related [Forum Topic](https://forum.manjaro.org/t/wiki-worker-an-introduction-to-the-highly-configurable-file-manager/17667)