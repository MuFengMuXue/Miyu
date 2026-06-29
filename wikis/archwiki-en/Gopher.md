# Gopher

Gopher is a protocol for information transfer over the internet that was very popular before HTTP took over as the dominant protocol, but there is still a community of gopher users that prefer the simplicity of the protocol over the more complex and large protocols more often encountered. Note that not all browsers support gopher, or have incomplete support.

## Gopher clients
Browsing gopherspace requires a client. Lynx can handle the gopher protocol; there are also a number to choose from in the AUR, including:

*
*
*
*
*
*

Search the AUR for a full list.

A good starting point to explore gopherspace is http://gopher.quux.org:70/

## Gopher server
Creating your own gopherspace is relatively straightforward. Install and configure a gopher server, and add your own content.

There are a number of gopher servers, including:

*
*
*
*

## Adding content
Gopher is a plain text protocol. Begin by creating a gophermap that defines the homepage of your gopherhole and includes links to the rest of your content. A  includes item types that describe the content in the file. An example might look like this:

The format for the file is the item type as the very first character, the display string (i.e., the description text to display), a selector (i.e., a file-system pathname), host name (i.e., the domain name of the server on which the item resides), and port (i.e., the port number used by that server). The item type and display string are joined without a space; the other fields are separated by the tab character.

A full list of the available item types can be found on Wikipedia:Gopher (protocol)#Item types.

## Overbite for Firefox
The Overbite Project enables gopherspace in some browsers and devices, including Mozilla Firefox. Check the  or overbitewx add-on.

## HTTP access via Gopher proxy
You can use https://gopher.floodgap.com/gopher/gw to browse the Gopher network via HTTP, e.g. using a browser not Gopher-enabled.
