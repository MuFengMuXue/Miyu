## org.freedesktop.dbus Class AbstractConnection

    java.lang.Object
      org.freedesktop.dbus.AbstractConnection

**Direct Known Subclasses:**  
DBusConnection, DirectConnection

<!-- -->

    public abstract class AbstractConnectionextends Object

Handles a connection to DBus.

<table data-border="1" width="100%" data-cellpadding="3" data-cellspacing="0" data-summary="">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="TableHeadingColor" data-bgcolor="#CCCCFF">
<th colspan="2" style="text-align: left;"><strong>Nested Class Summary</strong></th>
</tr>
</thead>
<tbody>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  class</code></td>
<td><strong><code>AbstractConnection._thread</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  class</code></td>
<td><strong><code>AbstractConnection._workerthread</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  class</code></td>
<td><strong><code>AbstractConnection.FallbackContainer</code></strong><br />
           </td>
</tr>
</tbody>
</table>

 

<table data-border="1" width="100%" data-cellpadding="3" data-cellspacing="0" data-summary="">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="TableHeadingColor" data-bgcolor="#CCCCFF">
<th colspan="2" style="text-align: left;"><strong>Field Summary</strong></th>
</tr>
</thead>
<tbody>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  boolean</code></td>
<td><strong><code>_run</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  </code><code>String</code></td>
<td><strong><code>addr</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  boolean</code></td>
<td><strong><code>connected</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static boolean</code></td>
<td><strong><code>EXCEPTION_DEBUG</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  </code><code>Map</code><code>&lt;</code><code>String</code><code>,org.freedesktop.dbus.ExportedObject&gt;</code></td>
<td><strong><code>exportedObjects</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  </code><code>AbstractConnection.FallbackContainer</code></td>
<td><strong><code>fallbackcontainer</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  </code><code>Map</code><code>&lt;org.freedesktop.dbus.SignalTuple,</code><code>Vector</code><code>&lt;</code><code>DBusSigHandler</code><code>&lt;? extends </code><code>DBusSignal</code><code>&gt;&gt;&gt;</code></td>
<td><strong><code>handledSignals</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  </code><code>Map</code><code>&lt;</code><code>DBusInterface</code><code>,org.freedesktop.dbus.RemoteObject&gt;</code></td>
<td><strong><code>importedObjects</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  </code><code>Map</code><code>&lt;</code><code>MethodCall</code><code>,</code><code>DBusAsyncReply</code><code>&lt;? extends </code><code>Object</code><code>&gt;&gt;</code></td>
<td><strong><code>pendingCallbackReplys</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  </code><code>Map</code><code>&lt;</code><code>MethodCall</code><code>,</code><code>CallbackHandler</code><code>&lt;? extends </code><code>Object</code><code>&gt;&gt;</code></td>
<td><strong><code>pendingCallbacks</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  org.freedesktop.dbus.EfficientMap</code></td>
<td><strong><code>pendingCalls</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  </code><code>LinkedList</code><code>&lt;</code><code>Runnable</code><code>&gt;</code></td>
<td><strong><code>runnables</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  org.freedesktop.dbus.AbstractConnection._sender</code></td>
<td><strong><code>sender</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  </code><code>AbstractConnection._thread</code></td>
<td><strong><code>thread</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected static int</code></td>
<td><strong><code>TIMEOUT</code></strong><br />
          Timeout in us on checking the BUS for incoming messages and sending outgoing messages</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  </code><code>Transport</code></td>
<td><strong><code>transport</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  boolean</code></td>
<td><strong><code>weakreferences</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  </code><code>LinkedList</code><code>&lt;</code><code>AbstractConnection._workerthread</code><code>&gt;</code></td>
<td><strong><code>workers</code></strong><br />
           </td>
</tr>
</tbody>
</table>

 

<table data-border="1" width="100%" data-cellpadding="3" data-cellspacing="0" data-summary="">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="TableHeadingColor" data-bgcolor="#CCCCFF">
<th colspan="2" style="text-align: left;"><strong>Constructor Summary</strong></th>
</tr>
</thead>
<tbody>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected </code></td>
<td><strong><code>AbstractConnection</code></strong><code>(</code><code>String</code><code> address)</code><br />
           </td>
</tr>
</tbody>
</table>

 

<table data-border="1" width="100%" data-cellpadding="3" data-cellspacing="0" data-summary="">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="TableHeadingColor" data-bgcolor="#CCCCFF">
<th colspan="2" style="text-align: left;"><strong>Method Summary</strong></th>
</tr>
</thead>
<tbody>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>addFallback</code></strong><code>(</code><code>String</code><code> objectprefix, </code><code>DBusInterface</code><code> object)</code><br />
          Export an object as a fallback object.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code>
<table data-border="0" data-cellpadding="0" data-cellspacing="0" data-summary="">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr data-align="right" data-valign="">
<td data-nowrap=""><code>&lt;T extends </code><code>DBusSignal</code><code>&gt;</code><br />
<code>void</code></td>
</tr>
</tbody>
</table></td>
<td><strong><code>addSigHandler</code></strong><code>(</code><code>Class</code><code>&lt;T&gt; type, </code><code>DBusInterface</code><code> object, </code><code>DBusSigHandler</code><code>&lt;T&gt; handler)</code><br />
          Add a Signal Handler.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code>
<table data-border="0" data-cellpadding="0" data-cellspacing="0" data-summary="">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr data-align="right" data-valign="">
<td data-nowrap=""><code>&lt;T extends </code><code>DBusSignal</code><code>&gt;</code><br />
<code>void</code></td>
</tr>
</tbody>
</table></td>
<td><strong><code>addSigHandler</code></strong><code>(</code><code>Class</code><code>&lt;T&gt; type, </code><code>DBusSigHandler</code><code>&lt;T&gt; handler)</code><br />
          Add a Signal Handler.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected abstract </code>
<table data-border="0" data-cellpadding="0" data-cellspacing="0" data-summary="">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr data-align="right" data-valign="">
<td data-nowrap=""><code>&lt;T extends </code><code>DBusSignal</code><code>&gt;</code><br />
<code>void</code></td>
</tr>
</tbody>
</table></td>
<td><strong><code>addSigHandler</code></strong><code>(</code><code>DBusMatchRule</code><code> rule, </code><code>DBusSigHandler</code><code>&lt;T&gt; handler)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected </code>
<table data-border="0" data-cellpadding="0" data-cellspacing="0" data-summary="">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr data-align="right" data-valign="">
<td data-nowrap=""><code>&lt;T extends </code><code>DBusSignal</code><code>&gt;</code><br />
<code>void</code></td>
</tr>
</tbody>
</table></td>
<td><strong><code>addSigHandlerWithoutMatch</code></strong><code>(</code><code>Class</code><code>&lt;? extends </code><code>DBusSignal</code><code>&gt; signal, </code><code>DBusSigHandler</code><code>&lt;T&gt; handler)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>DBusAsyncReply</code></td>
<td><strong><code>callMethodAsync</code></strong><code>(</code><code>DBusInterface</code><code> object, </code><code>String</code><code> m, </code><code>Object</code><code>... parameters)</code><br />
          Call a method asynchronously and get a handle with which to get the reply.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code>
<table data-border="0" data-cellpadding="0" data-cellspacing="0" data-summary="">
<tbody>
<tr data-align="right" data-valign="">
<td data-nowrap=""><code>&lt;A&gt; void</code></td>
</tr>
</tbody>
</table></td>
<td><strong><code>callWithCallback</code></strong><code>(</code><code>DBusInterface</code><code> object, </code><code>String</code><code> m, </code><code>CallbackHandler</code><code>&lt;A&gt; callback, </code><code>Object</code><code>... parameters)</code><br />
          Call a method asynchronously and set a callback.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>changeThreadCount</code></strong><code>(byte newcount)</code><br />
          Change the number of worker threads to receive method calls and handle signals.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>disconnect</code></strong><code>()</code><br />
          Disconnect from the Bus.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>exportObject</code></strong><code>(</code><code>String</code><code> objectpath, </code><code>DBusInterface</code><code> object)</code><br />
          Export an object so that its methods can be called on DBus.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>finalize</code></strong><code>()</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>BusAddress</code></td>
<td><strong><code>getAddress</code></strong><code>()</code><br />
          Returns the address this connection is connected to.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static </code><code>DBusCallInfo</code></td>
<td><strong><code>getCallInfo</code></strong><code>()</code><br />
          Returns a structure with information on the current method call.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>DBusExecutionException</code></td>
<td><strong><code>getError</code></strong><code>()</code><br />
          Return any DBus error which has been received.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  void</code></td>
<td><strong><code>listen</code></strong><code>()</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>removeFallback</code></strong><code>(</code><code>String</code><code> objectprefix)</code><br />
          Remove a fallback</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code>
<table data-border="0" data-cellpadding="0" data-cellspacing="0" data-summary="">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr data-align="right" data-valign="">
<td data-nowrap=""><code>&lt;T extends </code><code>DBusSignal</code><code>&gt;</code><br />
<code>void</code></td>
</tr>
</tbody>
</table></td>
<td><strong><code>removeSigHandler</code></strong><code>(</code><code>Class</code><code>&lt;T&gt; type, </code><code>DBusInterface</code><code> object, </code><code>DBusSigHandler</code><code>&lt;T&gt; handler)</code><br />
          Remove a Signal Handler.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code>
<table data-border="0" data-cellpadding="0" data-cellspacing="0" data-summary="">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr data-align="right" data-valign="">
<td data-nowrap=""><code>&lt;T extends </code><code>DBusSignal</code><code>&gt;</code><br />
<code>void</code></td>
</tr>
</tbody>
</table></td>
<td><strong><code>removeSigHandler</code></strong><code>(</code><code>Class</code><code>&lt;T&gt; type, </code><code>DBusSigHandler</code><code>&lt;T&gt; handler)</code><br />
          Remove a Signal Handler.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected abstract </code>
<table data-border="0" data-cellpadding="0" data-cellspacing="0" data-summary="">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr data-align="right" data-valign="">
<td data-nowrap=""><code>&lt;T extends </code><code>DBusSignal</code><code>&gt;</code><br />
<code>void</code></td>
</tr>
</tbody>
</table></td>
<td><strong><code>removeSigHandler</code></strong><code>(</code><code>DBusMatchRule</code><code> rule, </code><code>DBusSigHandler</code><code>&lt;T&gt; handler)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  void</code></td>
<td><strong><code>sendMessage</code></strong><code>(</code><code>Message</code><code> m)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>sendSignal</code></strong><code>(</code><code>DBusSignal</code><code> signal)</code><br />
          Send a signal.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>setWeakReferences</code></strong><code>(boolean weakreferences)</code><br />
          If set to true the bus will not hold a strong reference to exported objects.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>unExportObject</code></strong><code>(</code><code>String</code><code> objectpath)</code><br />
          Stop Exporting an object</td>
</tr>
</tbody>
</table>

 

| **Methods inherited from class java.lang.Object** |
|----|
| `clone``, ``equals``, ``getClass``, ``hashCode``, ``notify``, ``notifyAll``, ``toString``, ``wait``, ``wait``, ``wait` |

 

| **Field Detail** |
|------------------|

### TIMEOUT

    protected static final int TIMEOUT

Timeout in us on checking the BUS for incoming messages and sending outgoing messages

**See Also:**  
Constant Field Values

### exportedObjects

    protected Map<String,org.freedesktop.dbus.ExportedObject> exportedObjects

### importedObjects

    protected Map<DBusInterface,org.freedesktop.dbus.RemoteObject> importedObjects

### handledSignals

    protected Map<org.freedesktop.dbus.SignalTuple,Vector<DBusSigHandler<? extends DBusSignal>>> handledSignals

### pendingCalls

    protected org.freedesktop.dbus.EfficientMap pendingCalls

### pendingCallbacks

    protected Map<MethodCall,CallbackHandler<? extends Object>> pendingCallbacks

### pendingCallbackReplys

    protected Map<MethodCall,DBusAsyncReply<? extends Object>> pendingCallbackReplys

### runnables

    protected LinkedList<Runnable> runnables

### workers

    protected LinkedList<AbstractConnection._workerthread> workers

### fallbackcontainer

    protected AbstractConnection.FallbackContainer fallbackcontainer

### \_run

    protected boolean _run

### thread

    protected AbstractConnection._thread thread

### sender

    protected org.freedesktop.dbus.AbstractConnection._sender sender

### transport

    protected Transport transport

### addr

    protected String addr

### weakreferences

    protected boolean weakreferences

### EXCEPTION_DEBUG

    public static final boolean EXCEPTION_DEBUG

### connected

    protected boolean connected

| **Constructor Detail** |
|------------------------|

### AbstractConnection

    protected AbstractConnection(String address)
                          throws DBusException

**Throws:**  
`DBusException`

| **Method Detail** |
|-------------------|

### listen

    protected void listen()

### changeThreadCount

    public void changeThreadCount(byte newcount)

Change the number of worker threads to receive method calls and handle signals. Default is 4 threads

**Parameters:**  
`newcount` - The new number of worker Threads to use.

### getCallInfo

    public static DBusCallInfo getCallInfo()

Returns a structure with information on the current method call.

**Returns:**  
the DBusCallInfo for this method call, or null if we are not in a method call.

### setWeakReferences

    public void setWeakReferences(boolean weakreferences)

If set to true the bus will not hold a strong reference to exported objects. If they go out of scope they will automatically be unexported from the bus. The default is to hold a strong reference, which means objects must be explicitly unexported before they will be garbage collected.

### exportObject

    public void exportObject(String objectpath,
                             DBusInterface object)
                      throws DBusException

Export an object so that its methods can be called on DBus.

**Parameters:**  
`objectpath` - The path to the object we are exposing. MUST be in slash-notation, like "/org/freedesktop/Local", and SHOULD end with a capitalised term. Only one object may be exposed on each path at any one time, but an object may be exposed on several paths at once.

`object` - The object to export.

**Throws:**  
`DBusException` - If the objectpath is already exporting an object. or if objectpath is incorrectly formatted,

### addFallback

    public void addFallback(String objectprefix,
                            DBusInterface object)
                     throws DBusException

Export an object as a fallback object. This object will have it's methods invoked for all paths starting with this object path.

**Parameters:**  
`objectprefix` - The path below which the fallback handles calls. MUST be in slash-notation, like "/org/freedesktop/Local",

`object` - The object to export.

**Throws:**  
`DBusException` - If the objectpath is incorrectly formatted,

### removeFallback

    public void removeFallback(String objectprefix)

Remove a fallback

**Parameters:**  
`objectprefix` - The prefix to remove the fallback for.

### unExportObject

    public void unExportObject(String objectpath)

Stop Exporting an object

**Parameters:**  
`objectpath` - The objectpath to stop exporting.

### sendSignal

    public void sendSignal(DBusSignal signal)

Send a signal.

**Parameters:**  
`signal` - The signal to send.

### removeSigHandler

    public <T extends DBusSignal> void removeSigHandler(Class<T> type,
                                                        DBusSigHandler<T> handler)
                          throws DBusException

Remove a Signal Handler. Stops listening for this signal.

**Parameters:**  
`type` - The signal to watch for.

**Throws:**  
`DBusException` - If listening for the signal on the bus failed.

`ClassCastException` - If type is not a sub-type of DBusSignal.

### removeSigHandler

    public <T extends DBusSignal> void removeSigHandler(Class<T> type,
                                                        DBusInterface object,
                                                        DBusSigHandler<T> handler)
                          throws DBusException

Remove a Signal Handler. Stops listening for this signal.

**Parameters:**  
`type` - The signal to watch for.

`object` - The object emitting the signal.

**Throws:**  
`DBusException` - If listening for the signal on the bus failed.

`ClassCastException` - If type is not a sub-type of DBusSignal.

### removeSigHandler

    protected abstract <T extends DBusSignal> void removeSigHandler(DBusMatchRule rule,
                                                                    DBusSigHandler<T> handler)
                                      throws DBusException

**Throws:**  
`DBusException`

### addSigHandler

    public <T extends DBusSignal> void addSigHandler(Class<T> type,
                                                     DBusSigHandler<T> handler)
                       throws DBusException

Add a Signal Handler. Adds a signal handler to call when a signal is received which matches the specified type and name.

**Parameters:**  
`type` - The signal to watch for.

`handler` - The handler to call when a signal is received.

**Throws:**  
`DBusException` - If listening for the signal on the bus failed.

`ClassCastException` - If type is not a sub-type of DBusSignal.

### addSigHandler

    public <T extends DBusSignal> void addSigHandler(Class<T> type,
                                                     DBusInterface object,
                                                     DBusSigHandler<T> handler)
                       throws DBusException

Add a Signal Handler. Adds a signal handler to call when a signal is received which matches the specified type, name and object.

**Parameters:**  
`type` - The signal to watch for.

`object` - The object from which the signal will be emitted

`handler` - The handler to call when a signal is received.

**Throws:**  
`DBusException` - If listening for the signal on the bus failed.

`ClassCastException` - If type is not a sub-type of DBusSignal.

### addSigHandler

    protected abstract <T extends DBusSignal> void addSigHandler(DBusMatchRule rule,
                                                                 DBusSigHandler<T> handler)
                                   throws DBusException

**Throws:**  
`DBusException`

### addSigHandlerWithoutMatch

    protected <T extends DBusSignal> void addSigHandlerWithoutMatch(Class<? extends DBusSignal> signal,
                                                                    DBusSigHandler<T> handler)
                                      throws DBusException

**Throws:**  
`DBusException`

### disconnect

    public void disconnect()

Disconnect from the Bus.

### finalize

    public void finalize()

**Overrides:**  
`finalize` in class `Object`

### getError

    public DBusExecutionException getError()

Return any DBus error which has been received.

**Returns:**  
A DBusExecutionException, or null if no error is pending.

### callWithCallback

    public <A> void callWithCallback(DBusInterface object,
                                     String m,
                                     CallbackHandler<A> callback,
                                     Object... parameters)

Call a method asynchronously and set a callback. This handler will be called in a separate thread.

**Parameters:**  
`object` - The remote object on which to call the method.

`m` - The name of the method on the interface to call.

`callback` - The callback handler.

`parameters` - The parameters to call the method with.

### callMethodAsync

    public DBusAsyncReply callMethodAsync(DBusInterface object,
                                          String m,
                                          Object... parameters)

Call a method asynchronously and get a handle with which to get the reply.

**Parameters:**  
`object` - The remote object on which to call the method.

`m` - The name of the method on the interface to call.

`parameters` - The parameters to call the method with.

**Returns:**  
A handle to the call.

### sendMessage

    protected void sendMessage(Message m)

### getAddress

    public BusAddress getAddress()
                          throws ParseException

Returns the address this connection is connected to.

**Throws:**  
`ParseException`
