# Chuncord

Chuncord is a free and open source command line tool, licensed under EUPLv1.2 (European Union Public License) which allows uploading files larger than the 25MB upload limit to Discord's content delivery network (CDN) by splitting them into parts. These files can be downloaded using Chuncord as well.

## Installation
Install the  package.

## Configuration
Configuration for Chuncord is stored under , in TOML format.

## Usage
Chuncord uploads file parts using webhooks. Then, it uploads an index file that contains the filename, file size, and a list of all the file parts. Chuncord can then download the file using that index.

## Adding a Discord webhook
Chuncord allows you to add and manage Discord webhooks to upload files to different channels. Before you are able to upload, you must add a webhook:

 $ chuncord webhook add

## Default webhook
You can also select a default webhook to use when no webhook is specified.

 $ chuncord webhook default

The default webhook can be changed at any time.

## Uploading files to Discord
Simply run this command:

 $ chuncord upload -w

Or, if you have set a default webhook, you can omit the  flag:

 $ chuncord upload

Once the file is uploaded, Chuncord will print index file URL and the MID (message ID). The MID is used to delete an uploaded file. If you want to share the file with someone, you only need to provide the index URL.

## Downloading uploaded files
 $ chuncord download -o

You can omit the file path in order to use the original filename.

Note that to download, you do not need to specify any webhook.

## Deleting uploaded files
 $ chuncord delete -w

As with uploading, you can omit the webhook in order to use the default one. You need to use the same webhook that the file was uploaded with.
