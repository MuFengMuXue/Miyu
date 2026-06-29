# Upside Down Ternet

This article explains how to create a transparent Squid proxy server using 's mogrify to flip the images upside down.

## Installation
Install the , ,  and  packages.

## Configuration
Create , place it in your  folder and make it executable:
{{hc|/usr/local/bin/flip.pl|
#!/usr/bin/perl
$|=1;
$count = 0;
$pid = $$;
while (<>) {
       @splitted=split(/ /,$_);
       chomp $_;
       if ($_ =~ /(.*\.jpg)/i) {
               $url = $1;
               system("/usr/bin/wget", "-q", "-O","/srv/http/images/$pid-$count.jpg", "$url");
               system("/usr/bin/mogrify", "-flip","/srv/http/images/$pid-$count.jpg");
               print "http://127.0.0.1/images/$pid-$count.jpg\n";
       }
       elsif ($_ =~ /(.*\.gif)/i) {
               $url = $1;
               system("/usr/bin/wget", "-q", "-O","/srv/http/images/$pid-$count.gif", "$url");
               system("/usr/bin/mogrify", "-flip","/srv/http/images/$pid-$count.gif");
               print "http://127.0.0.1/images/$pid-$count.gif\n";
       }
       elsif ($_ =~ /(.*\.png)/i) {
               $url = $1;
               system("/usr/bin/wget", "-q", "-O","/srv/http/images/$pid-$count.png", "$url");
               system("/usr/bin/mogrify", "-flip","/srv/http/images/$pid-$count.png");
               print "http://127.0.0.1/images/$pid-$count.png\n";
       }
       else {
               print "$splitted}
       $count++;
}
}}

Next, while not necessary, does clean up the Squid configuration file a lot making it easier on the eyes

Now, edit your squid.conf file and append this to the bottom

Also find the line for  and make it now read

Finally, we have to create the folders for the images to be flipped in and set their permissions

The directory where the images are to be stored must be owned by the proxy user.

Finally, add the http user to the proxy group

Verify that the http user is a member of the proxy group

or

## Router setup
You will need to edit the firewall on your router or gateway to redirect HTTP traffic to your proxy.

## Starting
Start/enable  and .
