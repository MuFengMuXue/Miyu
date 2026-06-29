# Xournal++

Xournal++ is an open source handwriting app written in C++ supporting annotation of PDF files, it is a rewrite of Xournal to be more efficient and to enhance the functionality, while remaining backwards compatible with Xournal and is able to read and edit Xournal files (.xoj).

## Installation
Xournal++ is provided by multiple packages, install either:

*  - Latest stable release.
*  - Latest git commit, built from source.

## Troubleshooting
## Why has the PDF background disappeared after moving files?
Xournal++ currently does not support including the PDF within files, thus both the PDF and .xopp file must be kept together otherwise the PDF background will disappear. This is currently being worked on, find the issue on Github.

## Can Xournal read Xournal++ files (.xopp)?
Theoretically yes, according to the developers the file format is the same however .xopp store new features which are not included on Xournal, thus as long as only features supported in both Xournal and Xournal++ the file should be interchangeable between applications.

However, Xournal++ can export .xopp files as .xoj files to convert from Xournal++ to Xournal.

## Recorder could not be started
Check if the device set in Xournal++ preferences is an actual microphone.https://github.com/xournalpp/xournalpp/issues/1826#issuecomment-608748390
