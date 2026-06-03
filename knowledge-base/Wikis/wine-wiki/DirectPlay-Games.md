The easiest way to work around any DirectPlay issue is to install the
native version
winetricks directplay

This is a list of games known to use DirectPlay and what functions are
needed to be implemented.

### List of games that use DirectPlay 8

| Game                                                                                                              | Comments                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Civilization III](https://appdb.winehq.org/objectManager.php?sClass=application&amp;iId=426)                     | IDirectPlay8Peer -\> Connect, EnumHosts, EnumPlayersAndGroups, Host, ReturnBuffer, Send                                                                           |
| [Chris Sawyer's Locomotion](https://appdb.winehq.org/objectManager.php?sClass=application&amp;iId=2033)           | IDirectPlay8Peer -\> Close, Host                                                                                                                                  |
| [Dangerous Waters](https://appdb.winehq.org/objectManager.php?sClass=application&amp;iId=4414)                    | IDirectPlay8Server -\> EnumServiceProviders<br>IDirectPlay8Server -\> Close, Host                                                                                 |
| [Freelancer](https://appdb.winehq.org/appview.php?appId=1871)                                                     | IDirectPlay8Client -\> CancelAsyncOperation (All DPNCANCEL_ENUM types)<br>Couldn't get a game server running.                                                     |
| [Dungeon Siege 1](https://appdb.winehq.org/objectManager.php?sClass=application&amp;iId=770)                      | IDirectPlay8Client -\> EnumHosts, SetClientInfo, Close<br>IDirectPlay8Server -\> SetServerInfo, Close<br><br>NOTE: Steam Launch option "zonematch=true" required. |
| [Fair Strike](https://appdb.winehq.org/objectManager.php?sClass=application&amp;iId=18318)                        | IDirectPlay8Server -\> Host, SetApplicationDesc, SendTo<br>IDirectPlay8Client -\> EnumHosts                                                                       |
| [Heroes of Might and Magic IV](https://appdb.winehq.org/appview.php?appId=1229)                                   | IDirectPlay8Peer -\> EnumHosts, Host                                                                                                                              |
| [Northland - Cultures 3](https://appdb.winehq.org/objectManager.php?sClass=application&amp;iId=3462)              | IDirectPlay8Peer -\> Close, Host                                                                                                                                  |
| [S.T.A.L.K.E.R.: Shadow of Chernobyl](https://appdb.winehq.org/objectManager.php?sClass=application&amp;iId=4794) | IDirectPlay8Client -\> Enumhost (synchronously), Connect, GetApplicationDesc, Send<br>IDirectPlay8Server -\> Host                                                 |
| [Warlords: Battlecry III](https://appdb.winehq.org/appview.php?versionId=4404)                                    | IDirectPlay8ThreadPool -\> Initialize,SetThreadCount, DoWork<br>IDirectPlay8Peer -\> EnumServiceProviders, CancelAsyncOperation, EnumHosts, Host                  |


### List of games that use DirectPlay

| Game                                                                                                           | DX version | Comments                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|------------|-------------------------------------------------------------------------------------------------------------------------------------|
| [Baldur's Gate II](https://appdb.winehq.org/objectManager.php?sClass=application&amp;iId=272)                  | 7          | DPWSCB_ -\> EnumSessions, Open, ShutdownEx<br>DP_ -\> InvokeEnumSessionCallbacks, SecureOpen<br>NS_ -\> SendSessionRequestBroadcast |
| [Commandos 2: Men of Courage](https://appdb.winehq.org/objectManager.php?sClass=application&amp;iId=1374)      | 5          | DP_ -\> InitializeDPSP, InvokeEnumSessionCallbacks<br>NS_ -\> SendSessionRequestBroadcast                                           |
| [The Tone Rebellion](https://appdb.winehq.org/objectManager.php?sClass=application&iId=13220)      | 5          | Unknown                                          |
| [Star Wars Galactic Battlegrounds](https://appdb.winehq.org/objectManager.php?sClass=application&amp;iId=2587) | 5          | DP_ -\> InitializeDPSP, InvokeEnumSessionCallbacks<br>NS_ -\> SendSessionRequestBroadcast                                           |
| [STAR WARS™ Rebellion](https://appdb.winehq.org/objectManager.php?sClass=application&amp;iId=124)              | 4          | DP_ -\> EnumGroupPlayers                                                                                                            |
| [Worms 2](https://appdb.winehq.org/objectManager.php?sClass=application&amp;iId=585)                           | 5          | CreateCompoundAddress -\> Don't error on unknown GUIDS                                                                              |

### Games to Confirm

- Age of Wonders Shadow Magic
- Bandits
- Besieger
- Condor
- Deer Hunter 2004 and 2005
- Dungeon Siege 1 and 2
- DXQuake 3
- FSHost
- G.I. Combat Episode I
- Gekkeiju
- Giants: Citizen Kabuto
- Hidden " Dangerous 2 / SS
- Homeworld 2
- Il rosso e il nero
- John Deere North American Farmer
- Jolt3D
- Judge Dredd vs Death
- Monopoly Tycoon
- New World Order
- No brakes 4x4 racing
- O.R.B
- Operation Blockade
- Operation Flashpoint
- Perimeter
- Pro Bass Fishing 2003
- Pro Rugby Manager 2004
- Robot Arena 2
- S.W.I.N.E.
- Sacrifice
- Scorch an Island
- SkyTracks
- State of Emergency
- Steel Tide
- Supreme Ruler 2010
- Trophy Hunter 2003
- True Crime Streets of LA
- Vietcong
- Warrior Kings
- Wings of War


A list of [Affected
Applications](https://appdb.winehq.org/viewbugs.php?iBugId=4066) that
caused by missing directplay implementation.
