# Sup

Sup is a powerful new mail client developed for people who manage lots of mail. It can be viewed as a cross between Mutt and Gmail, with very fast operation and search, tagging, automatic contact management, support for a wide variety of accounts at once, and more.

## Installation
## Automated
Install .

## Manual
Sup can instead be installed via RubyGems with system Ruby, as follows:

Install the dependencies: , , , and .

Install  gem first, and then  gem:

 $ gem install xapian-ruby
 $ gem install sup

Launch :

 $ sup

## Configuration
Sup comes with an easy to use configuration tool called . To use it, start it in the console and walk through the steps, which are as follows:

# Enter your full name.
# Enter your primary e-mail address, as well as any alternate e-mail addresses.
# Enter the path to your signature file, if you have one.
# Enter the editor that should be used to compose new mail, as well as any arguments that should be passed to it.
# Add sources for your mail, including:
## mbox files
## maildir directories

Support for remote sources (POP3, IMAP, IMAPS, and mbox+ssh) was removed in the 0.12 release.

Sup is for the most part only an MUA (mail user agent) and cannot handle downloading mail on its own. You can use tools like offlineimap, fetchmail, and rsync to transfer email to the local system mbox or maildir folders.

The sup wiki has an example for configuring a gmail+imap source using offlineimap. The Mutt#POP3 subsection shows some additional mail transfer methods.

After the email sources have been added,  will execute the  command to import mail into your mailbox.

## Filtering mail
sup works by having all relevant mail in one view at a time and no folders. To control exactly what is viewed and what is not mail needs filtering.

There are many ways to filter mail. Depending on how you access your mail you might want to filter on the serverside (with e.g.  or on the clientside.

To decide which way to go consider these two scenarios:
* you always check mail on the same computer using sup -> go for local filtering
* you want to be able to read your (uncluttered) email (through webmail) when using other computers -> filter on the server

## Local filtering
The sup hook before-add-message.rb enables you with a little ruby knowledge to filter your mail and applying labels, archive, mark read etc. to mail easily.

## Filter serverside
Sup only hides from view so to keep the serverside clean you have to resort to another tool.  is a popular mailfilter. Set it up starting from the example.config.

## sup sources
Sup uses the file  to get sync your mail with its index and supports adding one or more labels to all mail from a source.

As seen in the example the Pulse folder has 2 labels: pulse and cruft. All the mail from Pulse is archived on import and hidden from view avoiding a cluttered screen. See the sup wiki for details on labels and ids.

## sup hooks
sup has to types of hooks: interactive and non-interactive to enable the user to easily customize the program. See details in the sup wiki on hooks for details.

## before-poll hook
To activate the filtering and syncing automatically we set up a non-interactive startup hook using before-poll:
  File: ~/.sup/hooks/before-poll.rb
  Executes immediately before a poll for new messages commences.
  No variables.

Here is a simple example (without filtering)
  say "Running offlineimap..."
  system "offlineimap", "-o", "-u", "quiet"

Here is a simple example (with filtering)
  say "Running imapfilter..."
  system "imapfilter", "-c", "path-to-config.lua"
  say "Running offlineimap..."
  system "offlineimap", "-o", "-u", "quiet"

Now running sup will start filtering and then synching mail when sup starts or whenever you poll mail manually. See details in the sup wiki on before-poll

## Viewing HTML attachments
create  with
    require 'shellwords'
    unless sibling_types.member? "text/plain"
      case content_type
      when "text/html"
        `/usr/bin/w3m -dump -T #{content_type} #{Shellwords.escape filename}`
      end
    end
Or
{{bc|    require 'shellwords'
    unless sibling_types.member? "text/plain"
      case content_type
      when "text/html"
	`/usr/bin/links -dump #{Shellwords.escape filename}`
      end
    end}}
Note the difference in program executed.
See details on the sup wiki

## Viewing non-text attachments
Create the following hook:

See details on the sup wiki

## Usage
Execute the  command to start the Sup mail client. The program should show the messages imported by .

The most important key for new users to remember is the  key. This will display a full list of keyboard commands at any point, reminding new users how to navigate the program.

To navigate between threads, use the arrow keys or the  and  keys ( and  work like the Page Up and Page Down keys). To jump between threads with new messages, press the Tab key. Sup does not load all threads by default; press  to load more (more messages will automatically load to fill the window).

To view a thread, select it and press the  key. To expand or collapse an individual message while viewing a thread, select the message and press the  key. Press  to expand only new messages (the default view) or  to toggle the state of all messages. Press  to show or hide hidden parts of a message (such as signatures).

To navigate between messages in a thread, press the  and  keys. To display the headers on a message, press the  key.

To cycle through buffers, press the  key, or press the  key to view a list of all of the open buffers. To kill a buffer, press the  key.

To archive a thread, press the  key. This will hide it from the inbox until someone replies to it, at which point it will reappear. To kill a thread, press the  key. This is equivalent to Gmail's "mute" function, which hides a message even if people reply to it. It will never re-appear in the inbox, but it will still show up in search results.

To star a thread, press the  key. To mark a thread as spam, press the  key. Sup does not have any built-in spam filter; for that, consider a program such as .

To tag a thread, press the  key. To label the messages in a thread, press the  key. To search labels, press the  key.  a label for which to search or press the  key to call up a list of labels. To perform a full text search, press the  key.

To view a list of contacts, press the  key. To e-mail one of the people on the list, select their name and press the  key.

## Back-up and Restore
Backing-up e-mail is very important. To ensure that you do not lose anything, first back up the sources, such as mbox files and maildir directories, then run:

 $ sup-dump > filename

This will back-up all message states in a text file. To restore your message states from this text file, simply run:

 $ sup-sync --restored --restore filename

Just remember that the commands above only back-up and restore message states. The messages themselves will need to be backed-up separately.
