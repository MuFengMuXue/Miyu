\[prev\] \[prev-tail\] \[tail\] \[up\]

### 12  Peer to Peer

It is possible to connect two applications together directly without using a bus. D-Bus calls this a peer-to-peer connection.

The Java implementation provides an alternative to the DBusConnection class, the DirectConnection<sup>21</sup> class. This allows you to connect two applications together directly without the need of a bus.

When using a DirectConnection rather than a DBusConnection most operations are the same. The only things which differ are how you connect and the operations which depend on a bus. Since peer connections are only one-to-one there is no destination or source address to messages. There is also no org.freedesktop.DBus service running on the bus.

#### 12.1  Connecting to another application

To connect with a peer connection one of the two applications must be listening on the socket and the other connecting. Both of these use the same method to instantiate the DirectConnection but with different addresses. To listen rather than connect you add the “listen=true” parameter to the address. Listening and connecting can be seen in figures 17 and 18 respectively. Listening will block at creating the connection until the other application has connected.

DirectConnection also provides a createDynamicSession method which generates a random abstract unix socket address to use.

<table class="figure">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="figure">
<td class="figure">DirectConnection dc = new DirectConnection("unix:path=/tmp/dbus-ABCXYZ,listen=true");
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Figure 17:</td>
<td class="content">Listening for a peer connection</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

<table class="figure">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="figure">
<td class="figure">DirectConnection dc = new DirectConnection("unix:path=/tmp/dbus-ABCXYZ");
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Figure 18:</td>
<td class="content">Connecting to a peer connection</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

#### 12.2  Getting Remote Objects

Getting a remote object is essentially the same as with a bus connection, except that you do not have to specify a bus name, only an object path. There is also no getPeerRemoteObject method, since there can only be one peer on this connection.

<table class="figure">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="figure">
<td class="figure">RemoteInterface remote = dc.getRemoteObject("/Path");  <br />
remote.doStuff();
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Figure 19:</td>
<td class="content">Getting a remote object on a peer connection</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

The rest of the API is the same for peer connections as bus connections, ommiting any bus addresses.

\[prev\] \[prev-tail\] \[front\] \[up\]
