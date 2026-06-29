# NAME

cups-oauth - interact with an oauth/openid authorization server

# SYNOPSIS

**cups-oauth** **--help**
**cups-oauth** **--version**
**cups-oauth** \[ **-a** *OAUTH-URI* \] \[ **-s** *SCOPE(S)* \] **authorize** *\[RESOURCE\]*
**cups-oauth** \[ **-a** *OAUTH-URI* \] **clear** *\[RESOURCE\]*
**cups-oauth** \[ **-a** *OAUTH-URI* \] **get-access-token** *\[RESOURCE\]*
**cups-oauth** \[ **-a** *OAUTH-URI* \] **get-client-id**
**cups-oauth** \[ **-a** *OAUTH-URI* \] **get-metadata** *\[NAME\]*
**cups-oauth** \[ **-a** *OAUTH-URI* \] **get-user-id** *\[RESOURCE\]* *\[NAME\]*
**cups-oauth** \[ **-a** *OAUTH-URI* \] **set-access-token** *\[RESOURCE\]* *TOKEN*
**cups-oauth** \[ **-a** *OAUTH-URI* \] **set-client-data** *CLIENT-ID* *CLIENT-SECRET*

# DESCRIPTION

The **cups-oauth** utility interacts with an OAuth/OpenID authorization server. Authorizations are often linked to a resource (a printer URI, web page URL, etc.)

# OPTIONS

The following options are recognized by **cups-oauth:**

**--help**
Show program usage.

**--version**
Show the CUPS version.

**-a** *OAUTH-URI*
Specifies the OAuth/OpenID authorization server URL.

**-s** *SCOPE(S)*
Specifies a space-delimited list of scope names to use when authorizing access. The default is to request authorization for all supported OpenID scopes.

# SUB-COMMANDS

## authorize

Starts an authorization workflow with the default web browser. If a resource URI is specified, the authorization is specific to that resource. The access token is send to the standard output on success.

## clear

Clears any authorization for the specified resource or for all resources if no resource URI is supplied.

## get-access-token

Output the current, unexpired access token, if any, to the standard output.

## get-client-id

Output the client ID string, if any, to the standard output.

## get-metadata

Get the OAuth/OpenID authorization server metadata and send it to the standard output. If a name is specified, the output is just the value for the specified metadata.

## get-user-id

Get the OpenID user ID information and send it to the standard output. If a name is specified, the output is just the named claim from the user ID.

## set-access-token

Set the access token (which is sometimes also called an API key) for the specified resource or for all resources.

## set-client-data

Set the client ID string and secret for an OAuth/OpenID authorization server.

# ENVIRONMENT VARIABLES

The **CUPS_OAUTH_URI** environment variable sets the default OAuth/OpenID authorization server URL.

The **CUPS_OAUTH_SCOPES** environment variable sets the default OAuth/OpenID scopes as a space-delimited list.

# NOTES

CUPS uses a redirect URI of "http://127.0.0.1/" for all authorization on the local system.

# EXAMPLES

Register a client ID and secret for the OAuth server at "https://oauth.example.com/":

         cups-oauth -a https://oauth.example.com/ set-client-data CLIENT-ID CLIENT-SECRET

Save an access token (sometimes called an application or API key) for the OAuth server at "https://oauth.example.com/":

         cups-oauth -a https://oauth.example.com/ set-access-token TOKEN

Authorize against the OAuth server at "https://oauth.example.com/" using your web browser:

         cups-oauth -a https://oauth.example.com/ authorize

# SEE ALSO

**cups**(1)

# COPYRIGHT

Copyright © 2025 by OpenPrinting.
