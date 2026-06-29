# Web feed

Certain websites provide web feeds or news feeds in RSS, Atom, or JSON format. News aggregators can check these feeds for updates allowing the user to subscribe to a blog or podcast.

## Obtaining web feeds
Even if a website does not advertise a web feed, it might still provide one. Try appending  or  to the URL. If that fails, open the website's source code by pressing  and then  to search for  or . The Firefox addon Awesome RSS adds a clickable icon to the address bar if a web feed is available.

If a website does not provide a feed, try RSS-Bridge.

The following sections describe how to obtain feeds for certain websites.

## Arch Linux
* News
* Overview page of all feeds

## GitHub
Commits feeds use the following syntax:

 https://github.com/user/repo/commits/branch/path/to/subdir.atom

## Reddit
Reddit provides feeds for subreddits, posts and users: simply add  to the URL. If you have a Reddit account, you can find your personal feeds in the preferences.

## YouTube
Subscribe to a channel:

 https://www.youtube.com/feeds/videos.xml?channel_id=UCxxxxxxxxxxxxxxxxxxxxxx

If the channel has a legacy URL ending in , you can also use:

 https://www.youtube.com/feeds/videos.xml?user=username

You can download your subscriptions list from Google Takeout and convert it to OPML using https://github.com/jeb5/YouTube-Subscriptions-RSS.
