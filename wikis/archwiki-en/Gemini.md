# Gemini

Gemini is a new, collaboratively designed internet protocol, which explores the space inbetween gopher and the web, striving to address (perceived) limitations of one while avoiding the (undeniable) pitfalls of the other.

## agate server
agate is a simple server for the Gemini hypertext protocol, written in Rust. Agate has very few features, and can only serve static files. It uses async I/O, and should be quite efficient even when running on low-end hardware and serving many concurrent requests.

## Installation
Install the  package.

## Configuration
Generate a self-signed TLS certificate and private key. For example, if you have OpenSSL 1.1 installed, you can use a command like the following. (Replace the hostname  with the address of your Gemini server.)

 $ openssl req -x509 -newkey rsa:4096 -keyout key.rsa -out cert.pem \
      -days 3650 -nodes -subj "/CN=example.com"

Run the server. You can use the following arguments to specify the locations of the content directory, certificate and key files, IP address and port to listen on, host name to expect in request URLs, and default language code(s) to include in the MIME type for for text/gemini files: (Again replace the hostname  with the address of your Gemini server.)

 $ agate --content path/to/content/ \
        --key key.rsa \
        --cert cert.pem \
        --addr \
        --addr 0.0.0.0:1965 \
        --hostname example.com \
        --lang en-US

## Gemini clients
## Terminal clients
*  (Go), a "fancy" terminal client.
*  (Rust), an NCurses-based terminal client.
*  (Python), a terminal client derived from the popular VF-1 Gopher client.
*  (Go), a combined Gopher and Gemini terminal client with vim-inspired key mappings.
* [https://thelambdalab.xyz/elpher/ Elpher (Emacs), a combined Gopher and Gemini client for the popular text editor / operating system.

## Graphical clients
*  (Rust, GTK), one of the earliest GUI clients, supporting Gemini, Gopher and finger.
*  (C++, Qt), a combined Gopher and Gemini GUI client.
*  (C, SDL), a beautiful tabbed GUI client with prebuilt binaries for Windows and MacOS.

## Web proxies
You can use one of the web proxies below to explore Geminispace from your web browser.

* Mozz.us portal
* geminize (Firefox extension)
