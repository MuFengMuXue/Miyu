# Phrik

phrik is an IRC bot present in most Arch IRC channels. It is a Limnoria (formerly a supybot) with loads of handy factoids and utilities for things like quoting oft-repeated phrases, quickly giving people useful links and other janitorial tasks. Custom "commands", called factoids, can be edited or added once registered (not to be confused with NickServ registration.)

## Account
## Registering
To make new or change already existing factoids you need to have a phrik account, which does not have to be named the same as your IRC nick.

 register name password

Example:  to register an account named  with the password

## Identifying
To identify with phrik for the current session, or until you , you need to run the following command:

 identify name password

Example:

## Identify with hostname
If you do not want to have to identify with phrik every time you connect you can add a hostmask to your phrik account which will make it identify you automatically every time you connect from that host. They are in the form of .

Be careful what hostmask you add though, since anyone connecting with that hostmask will be identified as you so you do not want to add the host from your ISP since that will likely change a lot. To be autoidentified with a hostmask you will want to either IRC from a server or have a cloak, otherwise the host will likely change a lot and thus others might get identified as you. If you are going to get identified with a host you might also want to run an ident server so that others connecting from the same server will not be able to fake being you.

Two good examples are  or .

## Adding a new hostmask
To add a hostmask send the following command to phrik in private:

 hostmask add hostmask

Example:

## Removing a hostmask
 hostmask remove name hostmask

 hostmask remove demize demize!kyrias@theos.kyriasis.com

## Listing hostmasks
 hostmask list

## Factoids
phrik has the MoobotFactoids plugins, meaning users can create, recall and give others factoids, which are small messages.

To make phrik recall a factoid you can either send the key of the factoid prefixed with an exclamation mark either to a channel where it is in or in private, like this:

 !welcome

## Searching factoids
To search existing factoids, you can use the listkeys and listvalues commands:

 !listkeys welcome

or

 !listvalues welcome

## Listing factoids by creator
Use  to find all factoids a nick created. This is great when someone accidentally created a factoid since phrik does not return the name of the created factoid.

 !listauth phrik

## Finding out info about factoids
If you want to find the creator and creation time of a factoid, you can use the factinfo command:

 !factinfo welcome

## Creating new factoids
Creating a new factoid is as easy as typing the key you want the factoid to be recalled by,  and then the message. Often you want to prepend the message with  so that phrik will just write the message exactly as you give it, instead of printing .

Making a factoid like this:

 !example is "This is an example factoid"

Will make phrik send  to the channel or pm whenever someone says  in the channel. If the  is omitted phrik will instead say .

## Factoid locking
Factoids can be locked to prevent other people from removing or overwriting a factoid, but there is generally no need for that as it is just in the way if there ends up being a good reason for the factoid being changed. Normally locking and unlocking would be done by calling the commands from the  plugin, but  is aliased to  for convenience.

If a factoid you think should be changed is locked, firstly contact the person who locked it ( will tell you), and if the person is either unavailable or refuses to change it but you still think it should be, due to breaking the rules or similar, feel free to contact the ops. (To get a list of ops send  to phrik in a pm.)

 !fact lock factoid_key

or

 !fact unlock factoid_key

## Modifying factoids
For modifying a factoid there are two alternatives, the first is using a regex substitute and the second is replacing it completely. Regex replaces have the good property of keeping the original creator info and who last modified it.

## Regex substitute
To replace the word "This" in the example factoid with the word "That" you can use regex replace like this:

 !example =~ s/This/That/

## Replacing a factoid
Completely replacing a factoid with something new can be done with the no command like this:

 !no example is "a really bad example factoid"

## Deleting factoids
Removing a factoid is done with , but since that is too long, there exists an alias for convenience called . Do not delete others factoids without a good reason, and do ask first if you are unsure.

 !rmfact factoid_key

## Quotes
phrik uses the QuoteGrabs plugin to provide an easy to use system for storing and retrieving things users say. You do not need to be identified with phrik to grab/retrieve quotes. All the QuoteGrabs commands can be listed using the command .

(The  argument does not seem to make any difference to the result of any of the commands listed below.)

## Grab
The  command is used to "grab" a quote. This means that the last thing  said will be stored in phrik's internal database. Example:

 !grab Arch-TK

 is synonymous to .

## Quote
The  command is used to view the last grabbed quote.

 is synonymous to , and so is

## Random
The  command is used to view a random selection of quotes. Given a  the selection is narrowed to just one user.

The alias  can be used in place of  and the alias  gives a selection of 5 random quotes instead of just 1.

## Search
The  command is used to search phrik's quote database for a quote containing a given string. This command does a literal search, this means that searching for "Arch-TK broken" will not return any search results unless that literal result is found. For example:

 !QuoteGrabs search "Arch-TK Windows"

Will not return .

The alias  can be used in place of .

## List
The  command is used to list all the quotes for a given user.

The alias  can be used in place of .

## Say
The  command is used to view the full quote text using an ID returned by the search and list functions.

For example:

 !QuoteGrabs say 34656

Will return:

  ew you might as well be using windows

The alias  can be used in place of .

## Get
The  command is very similar to the Say command. It returns the full text of the quote along with additional information.

For example:

 !QuoteGrabs get 34656

Will return:

  ew you might as well be using windows (Said by: sudokode!~ponies@unaffiliated/sudokode; grabbed by quantum-mechanic!~neutrino@unaffiliated/electron/x-8286743 at 11:21 AM, November 12, 2014

The alias  can be used in place of  but does not permit using a  argument.
