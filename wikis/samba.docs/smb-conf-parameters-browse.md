# smb.conf Parameters / browse

### `administrative share`

Section: browse; Context: S; Type: boolean; Default: `no`

If this parameter is set to yes for a share, then the share will be an administrative share. The Administrative Shares are the default network shares created by all Windows NT-based operating systems. These are shares like C$, D$ or ADMIN$. The type of these shares is STYPE_DISKTREE_HIDDEN. See the section below on for more information about this option.

### `browseable`

Section: browse; Context: S; Type: boolean; Default: `yes`

This controls whether this share is seen in the list of available shares in a net view and in the browse list.

### `browse list`

Section: browse; Context: G; Type: boolean; Default: `yes`

This controls whether smbd 8 will serve a browse list to a client doing a NetServerEnum call. Normally set to yes . You should never need to change this.

### `domain master`

Section: browse; Context: G; Type: enum; Default: `auto`

Tell smbd 8 to enable WAN-wide browse list collation. Setting this option causes nmbd to claim a special domain specific NetBIOS name that identifies it as a domain master browser for its given . Local master browsers in the same on broadcast-isolated subnets will give this nmbd their local browse lists, and then ask smbd 8 for a complete copy of the browse list for the whole wide area network. Browser clients will then contact their local master browser, and will receive the domain-wide browse list, instead of just the list for their broadcast-isolated subnet. Note that Windows NT Primary Domain Controllers expect to be able to claim this specific special NetBIOS name that identifies them as domain master browsers for that by default (i.e. there is no way to prevent a Windows NT PDC from attempting to do this). This means that if this parameter is set and nmbd claims the special name for a before a Windows NT PDC is able to do so then cross subnet browsing will behave strangely and may fail. If yes , then the default behavior is to enable the parameter. If is not enabled (the default setting), then neither will be enabled by default. When Yes the default setting for this parameter is Yes, with the result that Samba will be a PDC. If No , Samba will function as a BDC. In general, this parameter should be set to 'No' only on a BDC.

### `enhanced browsing`

Section: browse; Context: G; Type: boolean; Default: `yes`

This option enables a couple of enhancements to cross-subnet browse propagation that have been added in Samba but which are not standard in Microsoft implementations. The first enhancement to browse propagation consists of a regular wildcard query to a Samba WINS server for all Domain Master Browsers, followed by a browse synchronization with each of the returned DMBs. The second enhancement consists of a regular randomised browse synchronization with all currently known DMBs. You may wish to disable this option if you have a problem with empty workgroups not disappearing from browse lists. Due to the restrictions of the browse protocols, these enhancements can cause a empty workgroup to stay around forever which can be annoying. In general you should leave this option enabled as it makes cross-subnet browse propagation much more reliable.

### `lm announce`

Section: browse; Context: G; Type: enum; Default: `auto`

This parameter determines if nmbd 8 will produce Lanman announce broadcasts that are needed by OS/2 clients in order for them to see the Samba server in their browse list. This parameter can have three values, yes , no , or auto . The default is auto . If set to no Samba will never produce these broadcasts. If set to yes Samba will produce Lanman announce broadcasts at a frequency set by the parameter . If set to auto Samba will not send Lanman announce broadcasts by default but will listen for them. If it hears such a broadcast on the wire it will then start sending them at a frequency set by the parameter .

### `lm interval`

Section: browse; Context: G; Type: integer; Default: `60`

If Samba is set to produce Lanman announce broadcasts needed by OS/2 clients (see the parameter) then this parameter defines the frequency in seconds with which they will be made. If this is set to zero then no Lanman announcements will be made despite the setting of the parameter.

### `local master`

Section: browse; Context: G; Type: boolean; Default: `yes`

This option allows nmbd 8 to try and become a local master browser on a subnet. If set to no then nmbd will not attempt to become a local master browser on a subnet and will also lose in all browsing elections. By default this value is set to yes . Setting this value to yes doesn't mean that Samba will become the local master browser on a subnet, just that nmbd will participate in elections for local master browser. Setting this value to no will cause nmbd never to become a local master browser.

### `os level`

Section: browse; Context: G; Type: integer; Default: `20`

This integer value controls what level Samba advertises itself as for browse elections. The value of this parameter determines whether nmbd 8 has a chance of becoming a local master browser for the in the local broadcast area. Note: By default, Samba will win a local master browsing election over all Microsoft operating systems except a Windows NT 4.0/2000 Domain Controller. This means that a misconfigured Samba host can effectively isolate a subnet for browsing purposes. This parameter is largely auto-configured in the Samba-3 release series and it is seldom necessary to manually override the default setting. Please refer to the chapter on Network Browsing in the Samba-3 HOWTO document for further information regarding the use of this parameter. Note: The maximum value for this parameter is 255. If you use higher values, counting will start at 0!

### `preferred master`

Section: browse; Context: G; Type: enum; Default: `auto`

This boolean parameter controls if nmbd 8 is a preferred master browser for its workgroup. If this is set to yes , on startup, nmbd will force an election, and it will have a slight advantage in winning the election. It is recommended that this parameter is used in conjunction with yes , so that nmbd can guarantee becoming a domain master. Use this option with caution, because if there are several hosts (whether Samba servers, Windows 95 or NT) that are preferred master browsers on the same subnet, they will each periodically and continuously attempt to become the local master browser. This will result in unnecessary broadcast traffic and reduced browsing capabilities.

### `server addresses`

Section: browse; Context: S; Type: cmdlist

This is a per-share parameter to limit share visibility and accessibility to specific server IP addresses. Multi-homed servers can offer a different set of shares per interface. An empty list means to offer a share on all interfaces.
