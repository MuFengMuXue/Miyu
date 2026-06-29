[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Avidemux+-+Cutting+out+sections+of+video&language=en&action=page&filter= "Special:Translate")

Other languages:

[Deutsch](//wiki.manjaro.org/index.php?title=Avidemux_-_Cutting_out_sections_of_video/de "Avidemux - Cutting out sections of video/de (6% translated)") • ‎[English](//wiki.manjaro.org/index.php?title=Avidemux_-_Cutting_out_sections_of_video "Avidemux - Cutting out sections of video (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Avidemux_-_Cutting_out_sections_of_video/tr "Avidemux - Videonun bölümlerini kesme (17% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Avidemux_-_Cutting_out_sections_of_video/ru "Avidemux - Вырезание фрагментов видео (100% translated)")

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Installation]](#Installation)
-   [[3] [Preparation]](#Preparation)
-   [[4] [Method]](#Method)
    -   [[4.1] [Load the video into Avidemux]](#Load_the_video_into_Avidemux)
    -   [[4.2] [Set your Markers]](#Set_your_Markers)
    -   [[4.3] [A second cut]](#A_second_cut)
    -   [[4.4] [Cut some more video]](#Cut_some_more_video)
-   [[5] [Tips & Tricks]](#Tips_.26_Tricks)
    -   [[5.1] [You can also easily use Avidemux to transcode videos]](#You_can_also_easily_use_Avidemux_to_transcode_videos)
-   [[6] [See also]](#See_also)

## [Introduction]

Avidemux is by the intention of its author a fairly limited piece of video editing software. What it does do, is some things in quite a simple fashion, especially when compared to most of the other far more capable members of the video editing fraternity.

This how-to is about cutting one or more sections from a video. Which, when using Avidemux is a pretty simple process.

## [Installation]

Both the console tool \'avidemux-cli\' and qt-based GUI \'avidemux-qt\' are in the official repositories. To install one of them you can use Either

[user \$ ][ sudo pacman -S avidemux-cli [COPY TO CLIPBOARD]]

\

Or

[user \$ ][ sudo pacman -S avidemux-qt [COPY TO CLIPBOARD]]

\

## [Preparation]

Before we start editing, it should be known that the only setting that we need be concerned about out of all of the options showing in the left hand section (top to bottom) of the Avidemux GUI, is the **Output Format**.

You can set this (in the drop down menu under that sections **Output Format** title) to the same format as that of the video that is being edited.

## [Method]

### [Load the video into Avidemux]

Open the file you wish to edit in Avidemux using **Menu File \> Open** & then source the video file that you want to start snipping up.

Once choosen, the video will take some time (not that long really) to be processed & loaded into Avidemux.

### [Set your Markers]

After the video is loaded it can then be edited. So the first thing is to drag the bar that you\'ll find down near the bottom of the Avidemux screen, through the timeline of the video until you get as close as you can to the start of the part of the video that you want to cut out. If you want to start cutting from the beginning of the video, if should default to that position. Next go to the **Menu Edit \> Set Marker A** to indicate that this is the point you want to begin cutting from.

Once there, you can use the curser control arrows on your keyboard to much more slowly & accurately move to the point where you want to set **Menu Edit \> Set Marker B** *so that we can mark the **end*** of the section that we want to cut out of the video (this is the method we are using with Avidemux).

Once **Marker B** has been set, we then choose **Menu Edit \> Cut** & as quick as that our **Marker B** point has now moved to the original position of **Marker A**.

### [A second cut]

Now, if we so choose, we can use the *timeline bar* near the bottom of the Avidemux window to again scroll to as close as we can get to that point in the movie\'s timeline where the end of the section of video that we want to cut out is situated.

Again we use the left & right cursor control keys on our keyboard to accurately position the point where we want to set our marker. Once found, go to **Menu Edit \> Set Marker A**, then (unless you want to remove a section & retain another in the video) we slide the video\'s timeline to the very end *(use the cursor control right arrow to be sure that you are at the very end of the video - this often matters)* & then we go to **Menu Edit \> Set Marker B**.

### [Cut some more video]

After that we go to **Menu Edit \> Cut** & now we may have the snippet of video that we have been working to isolate.

Next we go to **Menu File \> Save** & **be sure to change the file\'s name from the original** & save it where we choose. Add the file extension *.mkv .avi .mp4* that I have chosen from the Output Format drop down menu down near the bottom right of the Avidemux window.

## [][Tips & Tricks]

### [You can also easily use Avidemux to transcode videos]

Another easy trick of Avidemux is the ability to easily change a video\'s format from one to another - with no other editing involved whatsoever.

To do this, choose your desired format & select the **Menu File \> Save** being sure to at least change the file format suffix in the name to the format that you\'ve chosen (.avi .mp4 .mkv \...), just doing that will save you from overwriting your original video file.

## [See also]