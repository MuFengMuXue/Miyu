# Identd

The Ident service as specified by RFC 1413 is mostly used by various IRC networks and the occasional old FTP server to ask a remote server which user is making a connection.
This method is quite untrustworthy, as the remote host can simply choose to lie.

So you have two choices:

* Tell the truth (see #oidentd below)
* Tell a little white lie (see #nullIdentd below)

## oidentd
See oidentd.

If all went well, you should have the auth service running on port 113.  A good way of checking this is by installing  (if you do not have it already) and typing:

 $ nmap localhost

## nullIdentd
This Ident server is capable of only returning the same name for any query. With a quick change to a single line of code, it can be customized to return any name you can think.
One use for such a simple service would be for IRC client connections to ensure a degree of privacy (remote IRC server and users do not know your username) as well as allowing a small degree of 'vanity plating' for use in IRC channels.

The original code suffered link rot, but may now be found on GitHub, at this address https://github.com/dxtr/nullidentd.

## systemd activation
Create , Add the following:

Then create , Add the following:

Reload  to make use of the new files:

You can check the unit status of  to test that it is listening successfully.
