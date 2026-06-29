# Firefox/Privacy

This article overviews how to configure Firefox to enhance security and privacy.

## Configuration
The following are privacy-focused tweaks to prevent browser fingerprinting and tracking.

## Tracking protection
Firefox gained an option for Enhanced Tracking Protection. It can be enabled in different levels via the GUI Settings > Privacy & Security, or by setting :

*

Apart from privacy benefits, enabling tracking protection may also reduce load time by 44%.

Note that this is not a replacement for ad blocking extensions such as uBlock Origin and it may or may not work with Firefox forks. If you are already running such an ad blocker with the correct lists, tracking protection might be redundant.

## Anti-fingerprinting
The Firefox tracking protection blocks a list of known "fingerprinters" when your privacy settings are set to Standard (the default) or Strict. Fingerprinting Protection is a different, experimental feature under heavy development in Firefox.

Mozilla has started an anti-fingerprinting project in Firefox, as part of a project to upstream features from Tor Browser. Many of these anti-fingerprinting features are enabled by this setting in the :

*

For more information see: Firefox's protection against fingerprinting.

## Change browser time zone
The time zone of your system can be used in browser fingerprinting. To set Firefox's time zone to UTC launch it as:

 $ TZ=UTC firefox

Or, set a script to launch the above (for example, at ).

## Change user agent and platform
You can override Firefox's user agent with the  preference in .

The value for the key is your browser's user agent. Select a known common one.

To change the platform for firefox, add the following  key in :

 general.platform.override

Select a known common platform that corresponds with your user agent.

## WebRTC exposes LAN IP address
To prevent websites from getting your local IP address via WebRTC's peer-to-peer (and JavaScript), open  and set:

*  to
*  to . (only if you want to completely disable WebRTC)

You can use this WebRTC test page and WebRTC IP Leak VPN / Tor IP Test to confirm that your internal/external IP address is no longer leaked.

## Disable HTTP referer
HTTP referer is an optional HTTP header field that identifies the address of the previous webpage from which a link to the currently requested page was followed.

Set  to  or , depending on your preferences.

## Disable connection tests
By default Firefox attempts to connect to Amazon and/or Akamai servers at regular intervals, to test your connection. For example a hotel, restaurant or other business might require you to enter a password to access the internet. If such a Captive portal exists and is blocking traffic this feature blocks all other connection attempts. This may leak your usage habits.

To disable Captive Portal testing, in  set:

*  to

## Disable telemetry
Set  to  and/or disable it under Preferences > Privacy & Security > Firefox Data Collection and Use.

## Enable "Do Not Track" header
Set  to  or toggle it in Preferences > Privacy & Security > Tracking Protection

## Disable/enforce 'Trusted Recursive Resolver'
Firefox 60 introduced a feature called Trusted Recursive Resolver (TRR). It circumvents DNS servers configured in your system, instead sending all DNS requests over HTTPS to Cloudflare servers. While this is significantly more secure (as "classic" DNS requests are sent in plain text over the network, and everyone along the way can snoop on these), this also makes all your DNS requests readable by Cloudflare, providing TRR servers.

* If you trust DNS servers you have configured yourself more than Cloudflare's, you can disable TRR in  by setting  (integer, create it if it does not exist) to . (A value of 0 means disabled by default, and might be overridden by future updates - a value of 5 is disabled by choice and will not be overridden.)
* If you trust Cloudflare DNS servers and would prefer extra privacy (thanks to encrypted DNS requests), you can enforce TRR by setting  to  (which completely disables classic DNS requests) or  (uses TRR by default, falls back to classic DNS requests if that fails). Keep in mind that if you are using any intranet websites or trying to access computers in your local networks by their hostnames, enabling TRR may break name resolving in such cases.
* If you want to encrypt your DNS requests but not use Cloudflare servers, you can point to a new DNS over HTTPS server by setting  to your resolver URL. A list of currently available resolvers can be found in the curl wiki, along with other configuration options for TRR.

## Encrypted Client Hello
To enable Encrypted Client Hello (ECH) (formerly encrypted Server Name Indicator (eSNI)), so that nobody listening on the wire can see the server name you made a TLS connection to, set:

*  to
*  to

You may also need to set  to  or .

## Disable geolocation
Set  to  in .

## Disable 'Safe Browsing' service
Safe Browsing offers phishing protection and malware checks, however it may send user information (e.g. URL, file hashes, etc.) to third parties like Google.

To disable the Safe Browsing service, in  set:

*  to
*  to

In addition disable download checking, by setting  to .

## Disable WebGL
WebGL is a potential security risk.Set  to  in  if you want to disable it.

## Extensions
See Browser extensions#Privacy.

## Disable WebAssembly (and JavaScript)
WebAssembly, also known as Wasm, is a relatively new language. Unlike JavaScript, Wasm executes pre-compiled code natively in browsers for high-performance simulations and applications. It has been criticized for hiding pathways for malware and [https://trac.torproject.org/projects/tor/ticket/21549 as with JavaScript, can be used to track users. Tor Browser blocks both JavaScript and Wasm.

See NoScript in Browser extensions#Privacy to block JavaScript the way Tor Browser does, which enables quick access when needed.  To disable Wasm, in  set:

*  to
*  to
*  to

## Remove system-wide hidden extensions
Some extensions are hidden and installed by default in . Many can be safely removed via . They might not be enabled by default and may have a menu option for enabling or disabling. Note that any files removed will return upon update of the  package. To keep these extensions removed, add the directories to NoExtract in . Some extensions include:

*  - DoH Roll-Out (do not remove if you chose to use #Disable/enforce 'Trusted Recursive Resolver' above).
*  - Firefox Screenshots.
*  - For reporting sites that are compromised in Firefox, so Mozilla can improve Firefox or patch the site dynamically using the  extension.
* All combined user and system extensions are listed in . See for a full list of system extensions including README files describing their functions.

Firefox installations to paths such as the default release installed to  have system extensions installed at .

## Web search over Searx
Privacy can be boosted by reducing the amount of information you give to a single entity. For example, sending each new web search via a different, randomly selected proxy makes it near impossible for a single search engine to build a profile of you. We can do this using public instances (or sites) of [https://searx.me/ Searx. Searx is an AGPL-3.0, open-source site-builder, that produces site, known as an 'instances'. Each public 'instance' can act as a middle-man between you and a myriad of different search engines.

From this list of public instances and others, bookmark as many Searx sites as you wish (if JavaScript is disabled you will need to enable it temporarily to load the list). For fast access to these bookmarks, consider adding ,  ...  to the bookmark's Name field, with  being the number of searx instances you bookmark.

After this bookmarking, simply typing , a number and  in the URL bar will load an instance.

See https://www.privacyguides.org/en/search-engines/ for other options.

## Watch videos over Invidious
Invidious instances act as an alternative front-end to YouTube. They are websites built from open-source code. It has typically been difficult to limit the amount of information a user sent to YouTube (Google) in order to access content.

Benefits of using Invidious include:

* Videos are accessible without running scripts. YouTube forces users to run scripts.
* Videos can be saved for future viewing, or for viewing by others, including when offline. This reduces feedback sent to Google about when content is viewed or re-viewed.
* An optional audio-only mode that reduces bandwidth usage. When combined with a browser like Tor, using fewer data packets on a more lightweight website is likely to improve your anonymity.
* Invidious is a free and open-source interface that makes setting up an independent, private, video-hosting service easier. As such there are website that exist that are using Invidious to serve their own content or content removed from YouTube. Therefore it may help limit the profile-building capabilities of YouTube into the future (see note).

Bookmark as many functioning invidious instances from the following lists as possible (here, here). Note that some of these instances may be hosted by Cloudflare.

You can change any YouTube video URL to an Invidious one by simply replacing the  part with the domain of the instance you want to use.

## Enterprise policies
Network and system-wide policies may be established through the use of enterprise policies which both supplements and overrides user configuration preferences. For example, there is no documented user preference to disable the checking of updates for beta channel releases. However, there exists an enterprise policy which can be effectively deployed as a workaround. Single and/or multiple policies may be administered through  as follows:

* Disable application updates
* Force-enable hardware acceleration

 {
  "policies": {
   "DisableAppUpdate": true,
   "HardwareAcceleration": true
  }
 }

Verify that  is set to  in  and review release-specific policies in .

## Sanitized profiles
## prefs.js
Files which constitute a Firefox profile can be stripped of certain metadata. For example, a typical  contains strings which identify the client and/or the user.

 user_pref("app.normandy.user_id", "6f469186-12b8-50fb-bdf2-209ebc482c263");
 user_pref("security.sandbox.content.tempDirSuffix", "2a02902b-f25c-a9df-17bb-501350287f27");
 user_pref("toolkit.telemetry.cachedClientID", "22e251b4-0791-44f5-91ec-a44d77255f4a");

There are multiple approaches by which these strings can be reset with the caveat that a master  must first be created without such identifiers and synced into a working profile. The simplest solution is close Firefox before copying its  to a separate location:

 $ cp ~/.mozilla/firefox/example.default-release/prefs.js ~/prefs.sanitized.js

Strip out any and all identfier strings and date codes by either setting them to 0 or removing the entries outright from the copied . Sync the now sanitized  to the working profile as required:

 $ rsync -v ~/.prefs.sanitized.js ~/.mozilla/firefox/example.default-release/prefs.js

A secondary privacy effect is also incurred which can be witnessed by examining the string results between a sanitized  versus a working  at Fingerprint JS API Demo.

## extensions.json
Assuming that extensions are installed, the  file lists all profile extensions and their settings. Of note is the location of the user home directory where the  and  folder exist by default. Unwanted background updates may be disabled by setting  to the appropriate  value. Of minor note are  and . Bubblewrap can effectively mask the username and location of the home directory at which time the  file may be sanitized and modified to point to the sandboxed  location.

 {"schemaVersion":31,"addons":Removal of similar metadata from  and  can also be accomplished. [https://github.com/jusw85/mozlz4 mozlz4 is a command-line tool which provides compression/decompression support for Mozilla (non-standard) LZ4 files.

## Removal of subsystems
Telemetry related to crash reporting may be disabled by removing the following:

 /usr/lib/firefox/crashreporter
 /usr/lib/firefox/minidump-analyzer
 /usr/lib/firefox/pingsender

Those deleted files will be back after upgrading the package, add them to NoExtract for persistence.

For those who have opted to install Firefox manually from official Mozilla sources, the updater system may be disabled by removing  in the  directory.

## Editing the contents of omni.ja
The file  contains most of the default configuration settings used by Firefox. As an example, starting from Firefox 73, network calls to  and/or  cannot be blocked by extensions or by setting preference URLs to . Aside from using a DNS sinkhole or firewalling resolved IP blocks, one solution is to  through the extracted contents of  before removing all references to  and/or . Extraneous modules such as unused dictionaries and hyphenation files can also be removed in order to reduce the size of  for both security and performance reasons.

To repack/rezip, use the command  and make sure that your working directory is the root directory of the files from the  file.

## Hardened user.js templates
Several active projects maintain comprehensive hardened Firefox configurations in the form of a  config that can be dropped to Firefox profile directory:

* arkenfox/user.js ()
* pyllyukko/user.js
* ffprofile.com (github) - online user.js generator. You select which features you want to enable and disable and in the end you get a download link for a zip-file with your profile template. You can for example disable some functions, which send data to Mozilla and Google, or disable several annoying Firefox functions like Mozilla Hello or the Pocket integration.
