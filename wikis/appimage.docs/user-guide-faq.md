# Frequently Asked Questions

The most common questions are answered directly here to save you from having to read the entire user guide.

## ![question](/_static/img/question.png) What is an AppImage?

An AppImage is a downloadable file for Linux that contains an application and everything the application needs to run (e.g., libraries, icons, fonts, translations, etc.) that cannot be reasonably expected to be part of each target system.

## ![question](/_static/img/question.png) How do I run an AppImage?

Make it executable and double-click it.

## ![question](/_static/img/question.png) How can I integrate AppImages with the system?

Using the optional appimaged daemon, you can easily integrate AppImages with the system. The daemon puts AppImages into the menus, registers MIME types, icons, all on the fly. You can download it from this repository. But it is entirely optional.

## ![question](/_static/img/question.png) Where can I download AppImages?

See the "repository" of upstream-generated AppImages.

## ![question](/_static/img/question.png) Where do I store my AppImages?

An important point about the AppImage format is that you can store AppImage files wherever you want. This includes your home directory, your downloads directory, a dedicated applications directory, a USB thumb drive, a CD-ROM or DVD, or even a network file share. No matter where you keep your AppImages, you are still able to run them. This is very similar to how applications work on macOS. Unlike with traditional Linux packages, you do not need to install AppImages or put them into some special location in order for them to work.

If you don't want to leave them in `$HOME/Downloads`, then `$HOME/Applications` is a good choice. Many third-party tools (especially the ones managing desktop integration) use this location, too. Other options involve `$HOME/.local/bin` and `$HOME/bin`, which are useful mainly for CLI tools.

**On CentOS/RHEL and Fedora:** When you login, the script `$HOME/.bash_profile` is executed and this script adds `$HOME/.local/bin:$HOME/bin` to your path.

**On Ubuntu:** When you login, the script `$HOME/.profile` is executed and this script adds `"$HOME/bin:$HOME/.local/bin"` to your path.

Besides, every other location works, e.g., a USB thumbdrive, a network location, or a CD-ROM, but then the AppImages won't be on your path, which means that you cannot simply type their name into a terminal but have to use the full path.

## ![question](/_static/img/question.png) Where can I request AppImages?

For example, if you would like to see an AppImage of Mozilla Firefox, then please leave a comment at <https://bugzilla.mozilla.org/show_bug.cgi?id=1249971>. The more people request an AppImage from the upstream authors, the more likely is that an AppImage will be provided.

## ![question](/_static/img/question.png) Where do I get support?
