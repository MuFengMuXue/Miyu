## org.freedesktop.dbus Class DirectConnection

    java.lang.Object
      org.freedesktop.dbus.AbstractConnection
          org.freedesktop.dbus.DirectConnection

    public class DirectConnectionextends AbstractConnection

Handles a peer to peer connection between two applications withou a bus daemon.

Signal Handlers and method calls from remote objects are run in their own threads, you MUST handle the concurrency issues.

| **Nested Class Summary** |     |
|--------------------------|-----|

 

| **Nested classes/interfaces inherited from class org.freedesktop.dbus.AbstractConnection** |
|----|
| `AbstractConnection._thread``, ``AbstractConnection._workerthread``, ``AbstractConnection.FallbackContainer` |

 

| **Field Summary** |     |
|-------------------|-----|

 

| **Fields inherited from class org.freedesktop.dbus.AbstractConnection** |
|----|
| `_run``, ``addr``, ``connected``, ``EXCEPTION_DEBUG``, ``exportedObjects``, ``fallbackcontainer``, ``handledSignals``, ``importedObjects``, ``pendingCallbackReplys``, ``pendingCallbacks``, ``pendingCalls``, ``runnables``, ``sender``, ``thread``, ``TIMEOUT``, ``transport``, ``weakreferences``, ``workers` |

 

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
<td><strong><code>DirectConnection</code></strong><code>(</code><code>String</code><code> address)</code><br />
          Create a direct connection to another application.</td>
<td></td>
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
<td><strong><code>addSigHandler</code></strong><code>(</code><code>DBusMatchRule</code><code> rule, </code><code>DBusSigHandler</code><code>&lt;T&gt; handler)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static </code><code>String</code></td>
<td><strong><code>createDynamicSession</code></strong><code>()</code><br />
          Creates a bus address for a randomly generated abstract unix socket.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static </code><code>String</code></td>
<td><strong><code>createDynamicTCPSession</code></strong><code>()</code><br />
          Creates a bus address for a randomly generated tcp port.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>DBusInterface</code></td>
<td><strong><code>getRemoteObject</code></strong><code>(</code><code>String</code><code> objectpath)</code><br />
          Return a reference to a remote object.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>DBusInterface</code></td>
<td><strong><code>getRemoteObject</code></strong><code>(</code><code>String</code><code> objectpath, </code><code>Class</code><code>&lt;? extends </code><code>DBusInterface</code><code>&gt; type)</code><br />
          Return a reference to a remote object.</td>
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
<td><strong><code>removeSigHandler</code></strong><code>(</code><code>DBusMatchRule</code><code> rule, </code><code>DBusSigHandler</code><code>&lt;T&gt; handler)</code><br />
           </td>
</tr>
</tbody>
</table>

 

| **Methods inherited from class org.freedesktop.dbus.AbstractConnection** |
|----|
| `addFallback``, ``addSigHandler``, ``addSigHandler``, ``addSigHandlerWithoutMatch``, ``callMethodAsync``, ``callWithCallback``, ``changeThreadCount``, ``disconnect``, ``exportObject``, ``finalize``, ``getAddress``, ``getCallInfo``, ``getError``, ``listen``, ``removeFallback``, ``removeSigHandler``, ``removeSigHandler``, ``sendMessage``, ``sendSignal``, ``setWeakReferences``, ``unExportObject` |

 

| **Methods inherited from class java.lang.Object** |
|----|
| `clone``, ``equals``, ``getClass``, ``hashCode``, ``notify``, ``notifyAll``, ``toString``, ``wait``, ``wait``, ``wait` |

 

| **Constructor Detail** |
|------------------------|

### DirectConnection

    public DirectConnection(String address)
                     throws DBusException

Create a direct connection to another application.

**Parameters:**  
`address` - The address to connect to. This is a standard D-Bus address, except that the additional parameter 'listen=true' should be added in the application which is creating the socket.

**Throws:**  
`DBusException`

| **Method Detail** |
|-------------------|

### createDynamicTCPSession

    public static String createDynamicTCPSession()

Creates a bus address for a randomly generated tcp port.

**Returns:**  
a random bus address.

### createDynamicSession

    public static String createDynamicSession()

Creates a bus address for a randomly generated abstract unix socket.

**Returns:**  
a random bus address.

### getRemoteObject

    public DBusInterface getRemoteObject(String objectpath)
                                  throws DBusException

Return a reference to a remote object. This method will always refer to the well known name (if given) rather than resolving it to a unique bus name. In particular this means that if a process providing the well known name disappears and is taken over by another process proxy objects gained by this method will make calls on the new proccess. This method will use bus introspection to determine the interfaces on a remote object and so **may block** and **may fail**. The resulting proxy object will, however, be castable to any interface it implements. It will also autostart the process if applicable. Also note that the resulting proxy may fail to execute the correct method with overloaded methods and that complex types may fail in interesting ways. Basically, if something odd happens, try specifying the interface explicitly.

**Parameters:**  
`objectpath` - The path on which the process is exporting the object.

**Returns:**  
A reference to a remote object.

**Throws:**  
`ClassCastException` - If type is not a sub-type of DBusInterface

`DBusException` - If busname or objectpath are incorrectly formatted.

### getRemoteObject

    public DBusInterface getRemoteObject(String objectpath,
                                         Class<? extends DBusInterface> type)
                                  throws DBusException

Return a reference to a remote object. This method will always refer to the well known name (if given) rather than resolving it to a unique bus name. In particular this means that if a process providing the well known name disappears and is taken over by another process proxy objects gained by this method will make calls on the new proccess.

**Parameters:**  
`objectpath` - The path on which the process is exporting the object.

`type` - The interface they are exporting it on. This type must have the same full class name and exposed method signatures as the interface the remote object is exporting.

**Returns:**  
A reference to a remote object.

**Throws:**  
`ClassCastException` - If type is not a sub-type of DBusInterface

`DBusException` - If busname or objectpath are incorrectly formatted or type is not in a package.

### removeSigHandler

    protected <T extends DBusSignal> void removeSigHandler(DBusMatchRule rule,
                                                           DBusSigHandler<T> handler)
                             throws DBusException

**Specified by:**  
`removeSigHandler` in class `AbstractConnection`

<!-- -->

**Throws:**  
`DBusException`

### addSigHandler

    protected <T extends DBusSignal> void addSigHandler(DBusMatchRule rule,
                                                        DBusSigHandler<T> handler)
                          throws DBusException

**Specified by:**  
`addSigHandler` in class `AbstractConnection`

<!-- -->

**Throws:**  
`DBusException`
