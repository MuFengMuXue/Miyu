\[prev\] \[prev-tail\] \[tail\] \[up\]

### 13  Low-level API

In very rare circumstances it may be neccessary to deal directly with messages on the bus, rather than with objects and method calls. This implementation gives the programmer access to this low-level API but its use is strongly recommended against.

To use the low-level API you use a different set of classes than with the normal API.

#### 13.1  Transport

The Transport<sup>22</sup> class is used to connect to the underlying transport with a bus address and to send and receive messages.

You connect by either creating a Transport object with the bus address as the parameter, or by calling connect with the address later. Addresses are represented using the BusAddress class.

Messages can be read by calling transport.min.readMessage() and written by using the transport.mout.writeMessage(m) methods.

#### 13.2  Message

Message<sup>23</sup> is the superclass of all the classes representing a message. To send a message you need to create a subclass of this object. Possible message types are: MethodCall, MethodReturn, Error and DBusSignal. Constructors for these vary, but they are basically similar to the MethodCall class.

All the constructors have variadic parameter lists with the last of the parameters being the signature of the message body and the parameters which make up the body. If the message has an empty body then the last parameter must be null. Reading and writing messages is not thread safe.

Messages can be read either in blocking or non-blocking mode. When reading a message in non-blocking mode, if a full message has not yet been read from the transport the method will return null. Messages are instantiated as the correct message type, so instanceof will work on the returned object. Blocking mode can be enabled with an extra parameter to the Transport constructor.

Figure 20 shows how to connect to a bus, send the (required) initial ‘Hello’ message and call a method with two parameters.

<table class="figure">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="figure">
<td class="figure">BusAddress address = new BusAddress(  <br />
         System.getenv("DBUS_SESSION_BUS_ADDRESS"));  <br />
Transport conn = new Transport(address, true);  <br />
 <br />
Message m = new MethodCall("org.freedesktop.DBus", "/org/freedesktop/DBus",  <br />
                           "org.freedesktop. DBus", "Hello", (byte) 0, null);  <br />
conn.mout.writeMessage(m);  <br />
 <br />
m = conn.min.readMessage();  <br />
System.out.println("Response to Hello is: "+m);  <br />
 <br />
m = new MethodCall("org.freedesktop.DBus", "/org/freedesktop/DBus",  <br />
                   "org.freedesktop.DBus", "RequestName", (byte) 0,  <br />
                   "su", "org.testname", 0);  <br />
conn.mout.writeMessage(m);  <br />
 <br />
conn.disconnect();
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Figure 20:</td>
<td class="content">Low-level usage</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

\[prev\] \[prev-tail\] \[front\] \[up\]
