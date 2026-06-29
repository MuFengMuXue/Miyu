# Conky/Tips and tricks

## Transparency
Conky supports two different types of transparency. Pseudo-transparency and real transparency that requires a composite manager to be installed and running. If you enable real transparency and do not have a composite manager running your conky will not be alpha transparent with transparency enabled for fonts and images as well as the background.

## Pseudo-transparency
Pseudo-transparency is enabled by default in conky. Pseudo-transparency works by copying the background image from the root window and using the relevant section as the background for conky. Some window managers set the background wallpaper to a level above the root window which can cause conky to have a grey background. To fix this issue you need to set it manually. An example with feh is:

In :

 sleep 1 && feh --bg-center ~/background.png &

## Enable real transparency
To enable real transparency, you must have a composite manager running and the following lines added to  inside the conky.config array:

  conky.config = {
     own_window = true,
     own_window_transparent = true,
     own_window_argb_visual = true,
     own_window_type = 'desktop',
  }

If window type "desktop" does not work try changing it to . If that does not work try the other options: , , or  instead.

## Semi-transparency
To achieve semi-transparency in real transparency mode, the following setup must be used in the conky configuration file:

  conky.config = {
     own_window = true,
     own_window_transparent = false,
     own_window_argb_visual = true,
     own_window_argb_value = 90,
     own_window_type = 'desktop',
  }

To reduce the transparency of the conky window, one can increase the value of  towards 255.

## Display package update information
 provides a script called  which displays package updates from the official repos. Use {{ic|${execi 3600 checkupdates | wc -l}}} to display the total number of packages.

## tail text files
conky is able to  files to your desktop, which is mostly useful for text files. Such as reading  files to display all kinds of log messages. Most of these files can only be read by , but running conky as  is not recommended, so you will need to add yourself to the  user group. In addition, since systemd log files are binary files, this feature is less useful then it used to be. However, it could be accomplished using lua scripts.

## Display weather forecast
It is achieved by reading external web pages, usually pages dedicated to weather forecast. See this thread. Another weather script in lua: here

## Display a countdown timer
ConkyTimer is a simple countdown timer that displays the remaining time of a defined task.

Start the timer using .

## Display RSS feeds
Conky has the ability to display RSS feeds natively without the need for an outside script to run and output into Conky. For example, to display the titles of the ten most recent Planet Arch updates and refresh the feed every minute, you would put this into your  in the  section:

 ${rss https://planet.archlinux.org/rss20.xml 300 item_titles 10 }
If you want to display Arch Forum rss feed, add this line:
 ${rss https://bbs.archlinux.org/extern.php?action=feed&type=rss 300 item_titles 4}
where 300 is in seconds the refresh interval (15 minutes is default), 4 the number of items you wish to show.

## Display a calendar for the current month
You can use the following lua script to display a calendar. It uses  and the default color from your configuration. It looks best with a monospace font.

  #!/usr/bin/env lua

  conky_color = "${color1}%2d${color}"

  t = os.date('*t', os.time())
  year, month, currentday = t.year, t.month, t.day

  daystart = os.date("*t",os.time{year=year,month=month,day=01}).wday

  month_name = os.date("%B")

  days_in_month = {
      31, 28, 31, 30, 31, 30,
      31, 31, 30, 31, 30, 31
  }

  -- check for leap year
  -- Any year that is evenly divisible by 4 is a leap year
  -- Any year that is evenly divisible by 100 is a leap year if
  -- it is also evenly divisible by 400.
  LeapYear = function (year)
      return year % 4 == 0 and (year % 100 ~= 0 or year % 400 == 0)
  end

  if LeapYear(year) then
      days_in_month= 29
  end

  title_start = (20 - (string.len(month_name) + 5)) / 2

  title = string.rep(" ", math.floor(title_start+0.5)) .. -- add padding to center the title
          (" %s %s\n Su Mo Tu We Th Fr Sa\n"):format(month_name, year)

  io.write(title)

  function seq(a,b)
      if a > b then
          return
      else
          return a, seq(a+1,b)
      end
  end

  days = days_in_month[month

  io.write(
      string.format(
          string.rep("   ", daystart-1) ..
          string.rep(" %2d", days), seq(1,days)
      ):gsub(string.rep(".",21),"%0\n")
       :gsub(("%2d"):format(currentday),
             (conky_color):format(currentday)
       ) .. "\n"
  )

Inside your  you can then place the following, making sure the path matches where you saved the script.

  conky.text =
  ${execpi 3600 ~/.config/conky/cal.lua}

## Display rTorrent stats
See this thread.

## Display your WordPress blog stats
This can be achieved by using the in python written extension named ConkyPress.

## Display number of new emails
Conky has built in support for IMAP and POP3, but does not have support for access over ssl. Conky's FAQ recommends using  for this and has an example configuration here.

Modify  as follows, and then start :

# Service-level configuration for TLS server
 client = yes
 accept  = 143
 connect = imap.gmail.com:143
 protocol = imap
 sslVersion = TLSv1
 # Service-level configuration for SSL server
 [imaps
 client = yes
 accept  = 993
 connect = imap.gmail.com:993

Then add the following to :

 conky.config = {
     imap = "localhost username password 120 'inbox' 993",
 }

 conky.text {
     Inbox: ${imap_unseen}/${imap_messages}
 }

## Gmail
If you use 2-factor authentication, you need to use an App Password.

For method 1, 2 and 3:

Create one of the following files in a convenient location (for example in ).

Then add the following string to your  in order the check your Gmail account for new email every five minutes (300 seconds) and display:
 ${execi 300 python ~/.scripts/gmail.py}

## method 1
This script uses retrieves the number of new email via Gmail's Atom API.
{{hc|gmail.py|
#!/usr/bin/env python3

import urllib.request

email = 'your email'
password = 'your password'

# Set up authentication for gmail
auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(realm='mail.google.com',
                          uri='https://mail.google.com/',
                          user=email,
                          passwd=password)
opener = urllib.request.build_opener(auth_handler)
# ...and install it globally so it can be used with urlopen.
urllib.request.install_opener(opener)

gmailurl = 'https://mail.google.com/gmail/feed/atom'
with urllib.request.urlopen(gmailurl) as page:
    contents = page.read().decode('utf-8')

ifrom = contents.index('') + 11
ito   = contents.index('')

fullcount = contentsprint('{} new emails'.format(fullcount))

}}

## method 2
Same as method 1, but does proper XML parsing.

{{hc|gmail.py|
#!/usr/bin/env python3

import urllib.request
from xml.etree import ElementTree as etree

email = 'your email'
password = 'your password'

# Set up authentication for gmail
auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(realm='mail.google.com',
                          uri='https://mail.google.com/',
                          user=email,
                          passwd=password)
opener = urllib.request.build_opener(auth_handler)
# ...and install it globally so it can be used with urlopen.
urllib.request.install_opener(opener)

gmailurl = 'https://mail.google.com/gmail/feed/atom'
NS = '{http://purl.org/atom/ns#}'
with urllib.request.urlopen(gmailurl) as source:
    tree = etree.parse(source)
fullcount = tree.find(NS + 'fullcount').text

print('{} new emails'.format(fullcount))
}}

## method 3
The same way, but with using ,  and :

replace email and password with your data.

## IMAP + SSL using Perl
Conky has built in support for IMAP accounts but does not support SSL. This can be provided using this script from [https://www.unix.com/shell-programming-scripting/115322-perl-conky-gmail-imap-unread-message-count.html this forum post. This requires the Perl/CPAN Modules Mail::IMAPClient and IO::Socket::SSL which are in the  and  packages

Create a file named  in a location to be read by conky (for example in ). In this file, add (with the appropriate changes):
{{hc|imap.pl|
#!/usr/bin/perl

# by gxmsgx
# description: get the count of unread messages on imap

use strict;
use Mail::IMAPClient;
use IO::Socket::SSL;

my $username = 'example.username';
my $password = 'password123';

my $socket = IO::Socket::SSL->new(
  PeerAddr => 'imap.server',
  PeerPort => 993
 )
 or die "socket(): $@";

my $client = Mail::IMAPClient->new(
  Socket   => $socket,
  User     => $username,
  Password => $password,
 )
 or die "new(): $@";

if ($client->IsAuthenticated()) {
  my $msgct;

  $client->select("INBOX");
  $msgct = $client->unseen_count||'0';
  print "$msgct\n";
}

$client->logout();
}}

Add to :
 ${execi 300 ~/.scripts/imap.pl}
or wherever you saved the file.

If you use Gmail you might need to generate an application specific password.

Alternatively, you can use stunnel as shown above: #Gmail

## IMAP using PHP
Another alternative using PHP. PHP needs to be installed and  must be uncommented in .

Then create a file named  in a location to be read by conky (for example in ). Make the file executable.

In this file, add (with the appropriate changes):

{{hc|imap.php|
#!/usr/bin/php
<?php
// See http://php.net/manual/function.imap-open.php for more information about
// the mailbox string in the first parameter of imap_open.
// This example is ready to use with Office 365 Exchange Mails,
// just replace your username (=email address) and the password.
$mbox = imap_open("{outlook.office365.com:993/imap/ssl/novalidate-cert}", "username", "password");

// Total number of emails
$nrTotal = imap_num_msg($mbox);

// Number of unseen emails. There are other ways using imap_status to count
// unseen messages, but they don't work with Office 365 Exchange. This one does.
$unseen = imap_search($mbox, 'UNSEEN');
$nrUnseen = $unseen ? count($unseen) : 0;

// Display the result, format as you like.
echo $nrUnseen.'/'.$nrTotal;

// Not needed, because the connection is closed after the script end.
// For the sake of clean public available scripts, we are nice to
// the imap server and close the connection manually.
imap_close($mbox);
}}

Add to :

 ${execi 300 ~/.scripts/imap.php}

or wherever you saved the file.

This script displays A/B where A is the number of unseen emails and B is the total number of mails in the mailbox. There are a lot of other information available through a lot of PHP functions like with imap_Status (https://php.net/manual/function.imap-status.php). Just see the PHP docs about IMAP: https://php.net/manual/ref.imap.php.

## Show graphic of active network interface
To test if a network inferface is currently active, you can use the test conky variable  on the  of the interface. Here is an example for wlo1 :

{{bc |draw_graph_borders yes
${if_existing /sys/class/net/wlo1/operstate up}
${color #0077ff}Net Down:$color ${downspeed wlo1}      ${color #0077ff}Net Up:$color ${upspeed wlo1}
${color #0077ff}${downspeedgraph wlo1 32,155 104E8B 0077ff} $alignr${color #0077ff}${upspeedgraph wlo1 32,155 104E8B 0077ff}
${endif}
}}

This is the expected result :

https://i.imgur.com/pQQbsP6.png

## User-contributed configuration examples
* A sample rings script with nvidia support - gist
