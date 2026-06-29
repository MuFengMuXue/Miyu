# CURL

cURL is a command line tool and library for transferring data with URLs. The command supports a number of different protocols, including HTTP, HTTPS, FTP, SCP, and SFTP. It is also designed to work without user interaction, like in scripts.

## Installation
Install the  package.

## Usage
## Downloading
A common use case for cURL is to download the resource to a specified file:

 $ curl --output filename URL

If the URL contains the file name, you can save the resource directly to a file of that name:

 $ curl --remote-name URL

Similarly, you can use  to accept a hint from an HTTP server (from the  header) for what the file should be named. If combined with , curl will use the file name specified by the URL if the HTTP server does not return a file name hint in its response.

Alternatively you can print the resource to stdout by omitting the output options:

 $ curl URL

## HTTP POST
You can use cURL to make HTTP POST requests:

 $ curl --data request body URL

If the request body cannot fit on the command line, cURL can read it from a file:

 $ curl --data @filename URL

Sometimes, you may need to specify a custom value for the  header (cURL's default is ). You can do this with . For example, if you wanted to make a POST request with a JSON body:

 $ curl --data json body -H 'Content-Type: application/json' URL
note that curl also has a option to write post data in json and change those headers automatically: :
 $ curl --json '{"key":"value"}' URL

## Tips and tricks
## Following redirects
To follow redirects (e.g. an HTTP to HTTPS redirect):

 $ curl --location URL

## Show download errors
By default curl would ignore errors (e.g. when downloading to a file, if there is a error curl would not notify you, and the file would be created empty) so use  to make it show a message on error:

 $ curl --fail URL

## Compression
If you want to transfer the data compressed, (e.g. in situations where bandwidth is more limited than CPU, curl would download the data compressed then uncompressed it after the download):

 $ curl --compressed URL

## ProgressBar
curl has option to a normal ProgressBar when it download files (e.g.  )
 $ curl --progress-bar URL

## Globbing
You can also use globbing in curl:

 $ curl "example.com/images/$ curl "example.com/{first_page,second_page,third_page}"

## config file
curl also search for a [https://everything.curl.dev/cmdline/configfile.html config file called  in home directory and in . You can just put the command line argument you want to use with curl by default, for example :
