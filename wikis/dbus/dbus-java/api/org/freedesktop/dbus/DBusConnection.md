## org.freedesktop.dbus Class DBusConnection

    java.lang.Object
      org.freedesktop.dbus.AbstractConnection
          org.freedesktop.dbus.DBusConnection

    public class DBusConnectionextends AbstractConnection

Handles a connection to DBus.

This is a Singleton class, only 1 connection to the SYSTEM or SESSION busses can be made. Repeated calls to getConnection will return the same reference.

Signal Handlers and method calls from remote objects are run in their own threads, you MUST handle the concurrency issues.

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
<td style="text-align: right;" data-valign="top" width="1%"><code> class</code></td>
<td><strong><code>DBusConnection.PeerSet</code></strong><br />
          Add addresses of peers to a set which will watch for them to disappear and automatically remove them from the set.</td>
</tr>
</tbody>
</table>

 

| **Nested classes/interfaces inherited from class org.freedesktop.dbus.AbstractConnection** |
|----|
| `AbstractConnection._thread``, ``AbstractConnection._workerthread``, ``AbstractConnection.FallbackContainer` |

 

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
<td style="text-align: right;" data-valign="top" width="1%"><code>static </code><code>String</code></td>
<td><strong><code>DEFAULT_SYSTEM_BUS_ADDRESS</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>SESSION</code></strong><br />
          Session Bus</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>SYSTEM</code></strong><br />
          System Bus</td>
</tr>
</tbody>
</table>

 

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
<th colspan="2" style="text-align: left;"><strong>Method Summary</strong></th>
</tr>
</thead>
<tbody>
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
<td><strong><code>addSigHandler</code></strong><code>(</code><code>Class</code><code>&lt;T&gt; type, </code><code>String</code><code> source, </code><code>DBusInterface</code><code> object, </code><code>DBusSigHandler</code><code>&lt;T&gt; handler)</code><br />
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
<td><strong><code>addSigHandler</code></strong><code>(</code><code>Class</code><code>&lt;T&gt; type, </code><code>String</code><code> source, </code><code>DBusSigHandler</code><code>&lt;T&gt; handler)</code><br />
          Add a Signal Handler.</td>
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
<td><strong><code>addSigHandler</code></strong><code>(</code><code>DBusMatchRule</code><code> rule, </code><code>DBusSigHandler</code><code>&lt;T&gt; handler)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>disconnect</code></strong><code>()</code><br />
          Disconnect from the Bus.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static </code><code>DBusConnection</code></td>
<td><strong><code>getConnection</code></strong><code>(int bustype)</code><br />
          Connect to the BUS.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static </code><code>DBusConnection</code></td>
<td><strong><code>getConnection</code></strong><code>(</code><code>String</code><code> address)</code><br />
          Connect to the BUS.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code><code>[]</code></td>
<td><strong><code>getNames</code></strong><code>()</code><br />
          Returns all the names owned by this connection.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>DBusInterface</code></td>
<td><strong><code>getPeerRemoteObject</code></strong><code>(</code><code>String</code><code> busname, </code><code>String</code><code> objectpath)</code><br />
          Return a reference to a remote object.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code>
<table data-border="0" data-cellpadding="0" data-cellspacing="0" data-summary="">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr data-align="right" data-valign="">
<td data-nowrap=""><code>&lt;I extends </code><code>DBusInterface</code><code>&gt;</code><br />
<code>I</code></td>
</tr>
</tbody>
</table></td>
<td><strong><code>getPeerRemoteObject</code></strong><code>(</code><code>String</code><code> busname, </code><code>String</code><code> objectpath, </code><code>Class</code><code>&lt;I&gt; type)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code>
<table data-border="0" data-cellpadding="0" data-cellspacing="0" data-summary="">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr data-align="right" data-valign="">
<td data-nowrap=""><code>&lt;I extends </code><code>DBusInterface</code><code>&gt;</code><br />
<code>I</code></td>
</tr>
</tbody>
</table></td>
<td><strong><code>getPeerRemoteObject</code></strong><code>(</code><code>String</code><code> busname, </code><code>String</code><code> objectpath, </code><code>Class</code><code>&lt;I&gt; type, boolean autostart)</code><br />
          Return a reference to a remote object.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>DBusInterface</code></td>
<td><strong><code>getRemoteObject</code></strong><code>(</code><code>String</code><code> busname, </code><code>String</code><code> objectpath)</code><br />
          Return a reference to a remote object.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code>
<table data-border="0" data-cellpadding="0" data-cellspacing="0" data-summary="">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr data-align="right" data-valign="">
<td data-nowrap=""><code>&lt;I extends </code><code>DBusInterface</code><code>&gt;</code><br />
<code>I</code></td>
</tr>
</tbody>
</table></td>
<td><strong><code>getRemoteObject</code></strong><code>(</code><code>String</code><code> busname, </code><code>String</code><code> objectpath, </code><code>Class</code><code>&lt;I&gt; type)</code><br />
          Return a reference to a remote object.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code>
<table data-border="0" data-cellpadding="0" data-cellspacing="0" data-summary="">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr data-align="right" data-valign="">
<td data-nowrap=""><code>&lt;I extends </code><code>DBusInterface</code><code>&gt;</code><br />
<code>I</code></td>
</tr>
</tbody>
</table></td>
<td><strong><code>getRemoteObject</code></strong><code>(</code><code>String</code><code> busname, </code><code>String</code><code> objectpath, </code><code>Class</code><code>&lt;I&gt; type, boolean autostart)</code><br />
          Return a reference to a remote object.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>getUniqueName</code></strong><code>()</code><br />
          Returns the unique name of this connection.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>releaseBusName</code></strong><code>(</code><code>String</code><code> busname)</code><br />
          Release a bus name.</td>
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
<td><strong><code>removeSigHandler</code></strong><code>(</code><code>Class</code><code>&lt;T&gt; type, </code><code>String</code><code> source, </code><code>DBusInterface</code><code> object, </code><code>DBusSigHandler</code><code>&lt;T&gt; handler)</code><br />
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
<td><strong><code>removeSigHandler</code></strong><code>(</code><code>Class</code><code>&lt;T&gt; type, </code><code>String</code><code> source, </code><code>DBusSigHandler</code><code>&lt;T&gt; handler)</code><br />
          Remove a Signal Handler.</td>
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
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>requestBusName</code></strong><code>(</code><code>String</code><code> busname)</code><br />
          Request a bus name.</td>
</tr>
</tbody>
</table>

 

| **Methods inherited from class org.freedesktop.dbus.AbstractConnection** |
|----|
| `addFallback``, ``addSigHandler``, ``addSigHandler``, ``addSigHandlerWithoutMatch``, ``callMethodAsync``, ``callWithCallback``, ``changeThreadCount``, ``exportObject``, ``finalize``, ``getAddress``, ``getCallInfo``, ``getError``, ``listen``, ``removeFallback``, ``removeSigHandler``, ``removeSigHandler``, ``sendMessage``, ``sendSignal``, ``setWeakReferences``, ``unExportObject` |

 

| **Methods inherited from class java.lang.Object** |
|----|
| `clone``, ``equals``, ``getClass``, ``hashCode``, ``notify``, ``notifyAll``, ``toString``, ``wait``, ``wait``, ``wait` |

 

| **Field Detail** |
|------------------|

### SYSTEM

    public static final int SYSTEM

System Bus

**See Also:**  
Constant Field Values

### SESSION

    public static final int SESSION

Session Bus

**See Also:**  
Constant Field Values

### DEFAULT_SYSTEM_BUS_ADDRESS

    public static final String DEFAULT_SYSTEM_BUS_ADDRESS

**See Also:**  
Constant Field Values

| **Method Detail** |
|-------------------|

### getConnection

    public static DBusConnection getConnection(String address)
                                        throws DBusException

Connect to the BUS. If a connection already exists to the specified Bus, a reference to it is returned.

**Parameters:**  
`address` - The address of the bus to connect to

**Throws:**  
`DBusException` - If there is a problem connecting to the Bus.

### getConnection

    public static DBusConnection getConnection(int bustype)
                                        throws DBusException

Connect to the BUS. If a connection already exists to the specified Bus, a reference to it is returned.

**Parameters:**  
`bustype` - The Bus to connect to.

**Throws:**  
`DBusException` - If there is a problem connecting to the Bus.

**See Also:**  
`SYSTEM`, `SESSION`

### releaseBusName

    public void releaseBusName(String busname)
                        throws DBusException

Release a bus name. Releases the name so that other people can use it

**Parameters:**  
`busname` - The name to release. MUST be in dot-notation like "org.freedesktop.local"

**Throws:**  
`DBusException` - If the busname is incorrectly formatted.

### requestBusName

    public void requestBusName(String busname)
                        throws DBusException

Request a bus name. Request the well known name that this should respond to on the Bus.

**Parameters:**  
`busname` - The name to respond to. MUST be in dot-notation like "org.freedesktop.local"

**Throws:**  
`DBusException` - If the register name failed, or our name already exists on the bus. or if busname is incorrectly formatted.

### getUniqueName

    public String getUniqueName()

Returns the unique name of this connection.

### getNames

    public String[] getNames()

Returns all the names owned by this connection.

### getPeerRemoteObject

    public <I extends DBusInterface> I getPeerRemoteObject(String busname,
                                                           String objectpath,
                                                           Class<I> type)
                                                throws DBusException

**Throws:**  
`DBusException`

### getPeerRemoteObject

    public DBusInterface getPeerRemoteObject(String busname,
                                             String objectpath)
                                      throws DBusException

Return a reference to a remote object. This method will resolve the well known name (if given) to a unique bus name when you call it. This means that if a well known name is released by one process and acquired by another calls to objects gained from this method will continue to operate on the original process. This method will use bus introspection to determine the interfaces on a remote object and so **may block** and **may fail**. The resulting proxy object will, however, be castable to any interface it implements. It will also autostart the process if applicable. Also note that the resulting proxy may fail to execute the correct method with overloaded methods and that complex types may fail in interesting ways. Basically, if something odd happens, try specifying the interface explicitly.

**Parameters:**  
`busname` - The bus name to connect to. Usually a well known bus name in dot-notation (such as "org.freedesktop.local") or may be a DBus address such as ":1-16".

`objectpath` - The path on which the process is exporting the object.\$

**Returns:**  
A reference to a remote object.

**Throws:**  
`ClassCastException` - If type is not a sub-type of DBusInterface

`DBusException` - If busname or objectpath are incorrectly formatted.

### getRemoteObject

    public DBusInterface getRemoteObject(String busname,
                                         String objectpath)
                                  throws DBusException

Return a reference to a remote object. This method will always refer to the well known name (if given) rather than resolving it to a unique bus name. In particular this means that if a process providing the well known name disappears and is taken over by another process proxy objects gained by this method will make calls on the new proccess. This method will use bus introspection to determine the interfaces on a remote object and so **may block** and **may fail**. The resulting proxy object will, however, be castable to any interface it implements. It will also autostart the process if applicable. Also note that the resulting proxy may fail to execute the correct method with overloaded methods and that complex types may fail in interesting ways. Basically, if something odd happens, try specifying the interface explicitly.

**Parameters:**  
`busname` - The bus name to connect to. Usually a well known bus name name in dot-notation (such as "org.freedesktop.local") or may be a DBus address such as ":1-16".

`objectpath` - The path on which the process is exporting the object.

**Returns:**  
A reference to a remote object.

**Throws:**  
`ClassCastException` - If type is not a sub-type of DBusInterface

`DBusException` - If busname or objectpath are incorrectly formatted.

### getPeerRemoteObject

    public <I extends DBusInterface> I getPeerRemoteObject(String busname,
                                                           String objectpath,
                                                           Class<I> type,
                                                           boolean autostart)
                                                throws DBusException

Return a reference to a remote object. This method will resolve the well known name (if given) to a unique bus name when you call it. This means that if a well known name is released by one process and acquired by another calls to objects gained from this method will continue to operate on the original process.

**Parameters:**  
`busname` - The bus name to connect to. Usually a well known bus name in dot-notation (such as "org.freedesktop.local") or may be a DBus address such as ":1-16".

`objectpath` - The path on which the process is exporting the object.\$

`type` - The interface they are exporting it on. This type must have the same full class name and exposed method signatures as the interface the remote object is exporting.

`autostart` - Disable/Enable auto-starting of services in response to calls on this object. Default is enabled; when calling a method with auto-start enabled, if the destination is a well-known name and is not owned the bus will attempt to start a process to take the name. When disabled an error is returned immediately.

**Returns:**  
A reference to a remote object.

**Throws:**  
`ClassCastException` - If type is not a sub-type of DBusInterface

`DBusException` - If busname or objectpath are incorrectly formatted or type is not in a package.

### getRemoteObject

    public <I extends DBusInterface> I getRemoteObject(String busname,
                                                       String objectpath,
                                                       Class<I> type)
                                            throws DBusException

Return a reference to a remote object. This method will always refer to the well known name (if given) rather than resolving it to a unique bus name. In particular this means that if a process providing the well known name disappears and is taken over by another process proxy objects gained by this method will make calls on the new proccess.

**Parameters:**  
`busname` - The bus name to connect to. Usually a well known bus name name in dot-notation (such as "org.freedesktop.local") or may be a DBus address such as ":1-16".

`objectpath` - The path on which the process is exporting the object.

`type` - The interface they are exporting it on. This type must have the same full class name and exposed method signatures as the interface the remote object is exporting.

**Returns:**  
A reference to a remote object.

**Throws:**  
`ClassCastException` - If type is not a sub-type of DBusInterface

`DBusException` - If busname or objectpath are incorrectly formatted or type is not in a package.

### getRemoteObject

    public <I extends DBusInterface> I getRemoteObject(String busname,
                                                       String objectpath,
                                                       Class<I> type,
                                                       boolean autostart)
                                            throws DBusException

Return a reference to a remote object. This method will always refer to the well known name (if given) rather than resolving it to a unique bus name. In particular this means that if a process providing the well known name disappears and is taken over by another process proxy objects gained by this method will make calls on the new proccess.

**Parameters:**  
`busname` - The bus name to connect to. Usually a well known bus name name in dot-notation (such as "org.freedesktop.local") or may be a DBus address such as ":1-16".

`objectpath` - The path on which the process is exporting the object.

`type` - The interface they are exporting it on. This type must have the same full class name and exposed method signatures as the interface the remote object is exporting.

`autostart` - Disable/Enable auto-starting of services in response to calls on this object. Default is enabled; when calling a method with auto-start enabled, if the destination is a well-known name and is not owned the bus will attempt to start a process to take the name. When disabled an error is returned immediately.

**Returns:**  
A reference to a remote object.

**Throws:**  
`ClassCastException` - If type is not a sub-type of DBusInterface

`DBusException` - If busname or objectpath are incorrectly formatted or type is not in a package.

### removeSigHandler

    public <T extends DBusSignal> void removeSigHandler(Class<T> type,
                                                        String source,
                                                        DBusSigHandler<T> handler)
                          throws DBusException

Remove a Signal Handler. Stops listening for this signal.

**Parameters:**  
`type` - The signal to watch for.

`source` - The source of the signal.

**Throws:**  
`DBusException` - If listening for the signal on the bus failed.

`ClassCastException` - If type is not a sub-type of DBusSignal.

### removeSigHandler

    public <T extends DBusSignal> void removeSigHandler(Class<T> type,
                                                        String source,
                                                        DBusInterface object,
                                                        DBusSigHandler<T> handler)
                          throws DBusException

Remove a Signal Handler. Stops listening for this signal.

**Parameters:**  
`type` - The signal to watch for.

`source` - The source of the signal.

`object` - The object emitting the signal.

**Throws:**  
`DBusException` - If listening for the signal on the bus failed.

`ClassCastException` - If type is not a sub-type of DBusSignal.

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

    public <T extends DBusSignal> void addSigHandler(Class<T> type,
                                                     String source,
                                                     DBusSigHandler<T> handler)
                       throws DBusException

Add a Signal Handler. Adds a signal handler to call when a signal is received which matches the specified type, name and source.

**Parameters:**  
`type` - The signal to watch for.

`source` - The process which will send the signal. This **MUST** be a unique bus name and not a well known name.

`handler` - The handler to call when a signal is received.

**Throws:**  
`DBusException` - If listening for the signal on the bus failed.

`ClassCastException` - If type is not a sub-type of DBusSignal.

### addSigHandler

    public <T extends DBusSignal> void addSigHandler(Class<T> type,
                                                     String source,
                                                     DBusInterface object,
                                                     DBusSigHandler<T> handler)
                       throws DBusException

Add a Signal Handler. Adds a signal handler to call when a signal is received which matches the specified type, name, source and object.

**Parameters:**  
`type` - The signal to watch for.

`source` - The process which will send the signal. This **MUST** be a unique bus name and not a well known name.

`object` - The object from which the signal will be emitted

`handler` - The handler to call when a signal is received.

**Throws:**  
`DBusException` - If listening for the signal on the bus failed.

`ClassCastException` - If type is not a sub-type of DBusSignal.

### addSigHandler

    protected <T extends DBusSignal> void addSigHandler(DBusMatchRule rule,
                                                        DBusSigHandler<T> handler)
                          throws DBusException

**Specified by:**  
`addSigHandler` in class `AbstractConnection`

<!-- -->

**Throws:**  
`DBusException`

### disconnect

    public void disconnect()

Disconnect from the Bus. This only disconnects when the last reference to the bus has disconnect called on it or has been destroyed.

**Overrides:**  
`disconnect` in class `AbstractConnection`
