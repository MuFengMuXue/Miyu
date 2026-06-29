# Vivaldi

Vivaldi is a proprietary web browser from former Opera founder & team members, based on Chromium and focused on personalization aspects.

## Installation
Consult this blog post for information on differences between stable and snapshot versions; then, install one of the following packages:

*
*

A pre-built package for the snapshot build can be found in the herecura unofficial repository.

## Extensions
Vivaldi is compatible with most of Chrome's extensions.
These can be installed directly from the Chrome Web Store.

To see which extensions are installed/enabled, type  in the address bar.

See also Wikipedia:Google Chrome Extension.

## Media playback
Vivaldi automatically downloads  and add support of proprietary codecs e.g. H.264, AAC, etc...

If you don't believe binary downloaded from somewhere, install ,  (chromium source) or  (ffmpeg.org source).

Or install  and
 ln -sf /usr/lib/libavformat.so.62 .local/lib/vivaldi/media-codecs-7.7/libffmpeg.so
This avoids crushing external media player Restart Vivaldi after downloading libffmpeg.so or installing those packages.

## Making flags persistent
You can put your flags in a  file under  (or under  if you have configured that environment variable).

No special syntax is used; flags are defined as if they were written in a terminal.

* The arguments are split on whitespace and shell quoting rules apply, but no further parsing is performed.
* Flags can be placed in separate lines for readability, but this is not required.

Below is an example  file that disables hardware media keys for the browser:

The  package can get its flags set with the  file.

## Modding
Vivaldi has [https://forum.vivaldi.net/topic/10549/modding-vivaldi?lang=en-US modding capabilities through its  (pre Vivaldi 6.2: ) file.

The file can be found at:

Another way to find the  path is through the Executable Path section at .

You can also use . It can help you manage mods: add or remove them from , and redo changes at vivaldi updates. For usage, visit the project page.

## Tips and tricks
## Transfer your profile to snapshot version
If you switched to snapshot version because of lacking features of stable version, you want to also use your user profile. Copy the  to .

## Google search suggestions
Vivaldi cannot be shipped with enabled suggestions for google search. The user must manually add the suggestion url https://www.google.com/complete/search?client=chrome&q=%s in search settings.

## Keep picture-in-picture window above other windows
When viewing some video, you can press the picture-in-picture button to detach it to a separate window. By default this window is not kept above others and it is inconvenient. To fix it in KDE, create a window rule to keep it above others. See KDE#Using window rules.

## Troubleshooting
## Chromium page
Some troubleshooting is common for Vivaldi and Chromium, such as for example, force enabling hardware acceleration. For such, consult the Chromium#Troubleshooting.

## Certificates management
Currently (Vivaldi 6.2.3105.54 (Stable channel)), the certificates management setting is missing. To workaround that, manually type the address . Note, that the address will be changed to , but you cannot type it in the first place (otherwise you will see vivaldi settings where cert management it is missing). See here for more details.

## Sync failing due to dropped ICMP Fragmentation Needed packets
For some users, Vivaldi's Sync feature will consistently fail to work. Navigate to  in your browser and check the error code in the "GetUpdates Response" entry under the "Sync Protocol Log" section of the page. If you see "Network error (ERR_TIMED_OUT)" then your sync is failing due to some network device (yours, your ISP's, or some other intermediary's) dropping "ICMP Fragmentation Needed" packets. To work around this issue, you can enable Packetization Layer Path MTU Discovery (PLPMTUD). See this post on the Vivaldi forums for more details. Follow the steps below to enable PLPMTUD:

Verify that PLPMTUD is currently disabled:

 # sysctl net.ipv4.tcp_mtu_probing

Should output  if it is disabled. If you see any other value, then you should stop here as your sync issue is not the same as what is covered by the workaround below.

Create:

Restart , then restart Vivaldi if you already had it open.
