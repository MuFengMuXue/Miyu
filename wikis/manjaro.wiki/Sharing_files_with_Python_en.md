[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Sharing+files+with+Python&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Sharing_files_with_Python "Sharing files with Python (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Sharing_files_with_Python/ru "Общий доступ к файлам с помощью Python (100% translated)")

## Contents

-   [[1] [Introduction]](#Introduction)
    -   [[1.1] [Installing]](#Installing)
    -   [[1.2] [Using it]](#Using_it)
    -   [[1.3] [Sharing from other systems with your Manjaro computer]](#Sharing_from_other_systems_with_your_Manjaro_computer)
    -   [[1.4] [stopping the server]](#stopping_the_server)
    -   [[1.5] [Some final remarks]](#Some_final_remarks)
-   [[2] [Creating a permanent file server (still the easy way)]](#Creating_a_permanent_file_server_.28still_the_easy_way.29)
    -   [[2.1] [Installation]](#Installation)
    -   [[2.2] [Using it]](#Using_it_2)
    -   [[2.3] [Stopping the server]](#Stopping_the_server_2)

## [Introduction]

There are many ways to share files in a network. Samba is commonly used for interop sharing. These methods will be easier and faster to set up. They can be used to share files between your computer your Smartphone or Tab/Pad.

You can share with:

-   OSX
-   Windows
-   Android

it will work on all platforms.

This is for the situation that you need to share something fast and is not advisable as part of your regular infrastructure.

\

### [Installing]

That is the beauty of it - there is nothing to install. This method will work right out of the box because Manjaro comes with Python 3 which makes it easy to share files rapidly in your network.

\

### [Using it]

Open a terminal on the computer that contains the files you want to share and navigate to the directory where the files you want to share are like ˝/home; then type:

    python -m http.server

Now go to the computer, phone or tab that should receive the files and open a browser.

[![Sharing.jpg](/images/thumb/4/45/Sharing.jpg/375px-Sharing.jpg)](//wiki.manjaro.org/index.php?title=File:Sharing.jpg)

[](//wiki.manjaro.org/index.php?title=File:Sharing.jpg "Enlarge")

In the url field of the browser you type

    http://the_IP_of_the_sharing_computer:8000

To find the IP of the computer you want to share from you type:

    ip addr

Something like this:

    http://192.168.0.123:8000

This will list all the files in the directory of the sharing computer.:

\

Now you can download or open the files. - It is as easy as that.

### [Sharing from other systems with your Manjaro computer]

Since you might want to share files from other computers with your Manjaro computer; they may have Python2 (This is the case for Debian,, Mageia and several other distros. In Windows you need to install Python first)

Here you have to write a different command. Open a terminal and write:

    python -m SimpleHTTPServer

Go to your Manjaro computer and open the url as described above and you will have access to the files.

If you want to use another port than the default 8000 - say 9000 - you can enter it like this:

    python -m http.server 9000

### [stopping the server]

Once you have shared the files; just stop the server with

    CTRL+c

It is as easy as that!

### [Some final remarks]

This server will live in your terminal and occupy it until you cancel it. You can see every transaction. You can only share with one computer at the time. It is a fast and super easy solution for that.

**Note**

------------------------------------------------------------------------

This is not a permanent file server.

## [][Creating a permanent file server (still the easy way)]

You would not want to use the sharing solution above (permanently) on an internet connected machine. It will share your files quick and easy to one person. If 10 persons try to access the files at the same time it will not work - it is a one at the time solution. So let\'s work some magic to fix that!

### [Installation]

Install python-twisted and python-service-identity (they are in the extra repo).

    sudo pacman -S python-twisted python-service-identity

### [Using it]

To make a permanent server on port 8080 with python; you can go to the directory you want to share and type:

    twistd3 web --path .

[![Twisted.jpg](/images/thumb/3/35/Twisted.jpg/375px-Twisted.jpg)](//wiki.manjaro.org/index.php?title=File:Twisted.jpg)

[](//wiki.manjaro.org/index.php?title=File:Twisted.jpg "Enlarge")

twistd web will then start and you can access in the browser with:

    http://localhost:8080/

It looks a bit better and your terminal will not be occupied with \"live action\". Here all people can access the files at the same time.

If you need to set the server to a different port then you can start the server like this:

    twistd3 web --port "tcp:port=9000" --path .

In this case the server will be on port 9000.

\

\
Python is often updated so if you get any errors running the command above you can alternatively try:

    python -c 'from twisted.web.server import Site; from twisted.web.static import File; from twisted.internet import reactor; reactor.listenTCP(8000, Site(File("."))); reactor.run()'

break it off with **CTRL+Z** and then type **bg** to start it in the background.

Here the server will be on port 8000 you can change it to your liking.

### [Stopping the server]

To stop this server you can type:

    kill `cat twistd.pid`

Now you have a permanent file server.

**Note**

------------------------------------------------------------------------

If you want to share from other servers to (not from) Manjaro then you may need to install **python2-twisted** and start the server with **twistd web \--path .** systems

It\'s as easy as that!