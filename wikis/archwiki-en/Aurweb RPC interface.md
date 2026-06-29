# Aurweb RPC interface

The Aurweb RPC interface is a lightweight RPC interface for the AUR. Queries are sent as HTTP GET requests and the server responds with JSON.

## API usage
## Query types
There are two query types:

* search
* info

## search
Package searches can be performed by issuing requests of the form:

 /rpc/v5/search/keyword?by=field

where  is the search argument and  is one of the following values:

*  (search by package name only)
*  (search by package name and description)
*  (search by package maintainer)
*  (search by package comaintainers)
*  (search for packages that depend on keywords)
*  (search for packages that makedepend on keywords)
*  (search for packages that optdepend on keywords)
*  (search for packages that checkdepend on keywords)
*  (search by package that provides keyword)
*  (search by package that conflicts with keyword)
*  (search by package that replaces keyword)
*  (search by package groups)
*  (search by package submitter)

The  parameter can be skipped and defaults to .
Possible return types are  and .

If a maintainer search is performed and the search argument is left empty, a list of orphan packages is returned.

Examples:

Search for package:
 https://aur.archlinux.org/rpc/v5/search/package

Search for packages maintained by user:
 https://aur.archlinux.org/rpc/v5/search/user?by=maintainer

Search for packages that have package as `makedepends`:
 https://aur.archlinux.org/rpc/v5/search/package?by=makedepends

Search with callback:
 https://aur.archlinux.org/rpc/v5/search/package?callback=jsonp1192244621103

## info
Package information can be retrieved by issuing requests of the form:

 /rpc/v5/info?arg%5B%5D=pkg1&arg%5B%5D=pkg2&…

where , , … are the exact matches of names of packages to retrieve package details for.

Possible return types are  and .

Examples:

Info for a single package:
 https://aur.archlinux.org/rpc/v5/info?argInfo for multiple packages:
 https://aur.archlinux.org/rpc/v5/info?arg[=pkg1&arg=== Return types ===

The return payload is of one format and currently has three main types. The response will always return a type so that the user can determine if the result of an operation was an error or not.

The format of the return payload is:
 {"version":5,"type":ReturnType,"resultcount":0,"results":ReturnData}

 is a string, and the value is one of:

*
*
*

## return data
The type of  is an array of dictionary objects for the  and  , and an empty array for  .

For the  ,  may contain the following fields:

*
*
*
*
*
*
*
*
*
*
*
*
*
*

For the   and ,  may additionally contain the following fields:

*
*
*
*
*
*
*
*
*
*

Fields that a package does not contain will be omitted from the output.

## error
The error type has an error response string as the return value. An error response can be returned from either a  or an  query type.

Example of  :
 {"version":5,"type":"error","resultcount":0,"results":[,"error":"Incorrect by field specified."}

## search
The search type is the result returned from a search request operation.

Example of  :
 {"version":5,"type":"search","resultcount":2,"results":...}}

## info
The info type is the result returned from an info request operation.

Example of  :

 {
    "version":5,
    "type":"multiinfo",
    "resultcount":1,
    "results":"ID":229417,
        "Name":"cower",
        "PackageBaseID":44921,
        "PackageBase":"cower",
        "Version":"14-2",
        "Description":"A simple AUR agent with a pretentious name",
        "URL":"http:\/\/github.com\/falconindy\/cower",
        "NumVotes":590,
        "Popularity":24.595536,
        "OutOfDate":null,
        "Maintainer":"falconindy",
        "FirstSubmitted":1293676237,
        "LastModified":1441804093,
        "URLPath":"\/cgit\/aur.git\/snapshot\/cower.tar.gz",
        "Depends":[
            "curl",
            "openssl",
            "pacman",
            "yajl"
        ,
        "MakeDepends":[
            "perl"
        ],
        "License":[
            "MIT"
        ],
        "Keywords":}
 }

## jsonp
If you are working with a javascript page, and need a JSON callback mechanism, you can do it.
You just need to provide an additional callback variable. This callback is usually handled via the javascript library, but here is an example.

Example Query:
 https://aur.archlinux.org/rpc/v5/search/foobar?callback=jsonp1192244621103

Example Result:
 /**/jsonp1192244621103({"version":5,"type":"search","resultcount":1,"results":advanced freeware audio player (uses Wine).","URL":"http:\/\/www.foobar2000.org\/","NumVotes":39,"Popularity":0.425966,"OutOfDate":null,"Maintainer":"supermario","FirstSubmitted":1273255356,"LastModified":1448326415,"URLPath":"\/cgit\/aur.git\/snapshot\/foobar2000.tar.gz"}})

This would automatically call the JavaScript function  with the parameter set to the results of the RPC call.

## Limitations
* HTTP GET requests are limited to URI of 8190 bytes maximum length. However, the official AUR instance running on a nginx server with HTTP/2 uses the default URI maximum length limit of 4443 bytes. Info requests with more than about 200 packages as an argument will need to be split.
* Search queries must be at least two characters long.
* Searches will fail if they contain 5000 or more results.
* The API rate is limited to a maximum of 4000 requests per day per IP.

## Reference clients
Sometimes things are easier to understand with examples. A few reference implementations (jQuery, python2, ruby) for old specification and without specifying "v" parameter are available here.

The new path-based version of the /rpc v5 API implementation on python 3.12 is available here.

## AUR metadata archives
In addition to pre-existing archives, we have introduced two new archives that can be used instead of bulk queries against the RPC. All archives are available for download at https://aur.archlinux.org/archive-name.gz

Using these archives will drastically help the AUR with the amount of traffic required for API clients. Particularly with clients who are able to query by themselves en masse.

All archives support Last-Modified and ETag. Each archive is updated on a rough ~5 minute interval. For any bulk users of the RPC, we ask that you consider these archives as a solution to repeated searches or bulk "multiinfo" requests.

## Pre-existing archives
* Listing of all packages separated by line break: https://aur.archlinux.org/packages.gz
* Listing of all package bases separated by line break: https://aur.archlinux.org/pkgbase.gz
* Listening of all users separated by line break: https://aur.archlinux.org/users.gz

## Metadata archives
* A complete  formatted JSON package archive: https://aur.archlinux.org/packages-meta-v1.json.gz
* A complete  formatted JSON package archive: https://aur.archlinux.org/packages-meta-ext-v1.json.gz
