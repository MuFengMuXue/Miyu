## org.freedesktop Interface DBus

**All Superinterfaces:**  
DBusInterface

<!-- -->

    public interface DBusextends DBusInterface

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
<td style="text-align: right;" data-valign="top" width="1%"><code>static interface</code></td>
<td><strong><code>DBus.Binding</code></strong><br />
          Contains Binding-test interfaces</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static interface</code></td>
<td><strong><code>DBus.Deprecated</code></strong><br />
          Indicates that a DBus interface or method is deprecated</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static interface</code></td>
<td><strong><code>DBus.Description</code></strong><br />
          Description of the interface or method, returned in the introspection data</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static interface</code></td>
<td><strong><code>DBus.Error</code></strong><br />
          Contains standard errors that can be thrown from methods.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static interface</code></td>
<td><strong><code>DBus.GLib</code></strong><br />
          Contains GLib-specific annotations</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static interface</code></td>
<td><strong><code>DBus.Introspectable</code></strong><br />
          Objects can provide introspection data via this interface and method.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static interface</code></td>
<td><strong><code>DBus.Local</code></strong><br />
          Messages generated locally in the application.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static interface</code></td>
<td><strong><code>DBus.Method</code></strong><br />
          Contains method-specific annotations</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static class</code></td>
<td><strong><code>DBus.NameAcquired</code></strong><br />
          Signal sent to a connection when it aquires a name</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static class</code></td>
<td><strong><code>DBus.NameLost</code></strong><br />
          Signal sent to a connection when it loses a name</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static class</code></td>
<td><strong><code>DBus.NameOwnerChanged</code></strong><br />
          Signal sent when the owner of a name changes</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static interface</code></td>
<td><strong><code>DBus.Peer</code></strong><br />
          All DBus Applications should respond to the Ping method on this interface</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static interface</code></td>
<td><strong><code>DBus.Properties</code></strong><br />
          A standard properties interface.</td>
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
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>DBUS_NAME_FLAG_ALLOW_REPLACEMENT</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>DBUS_NAME_FLAG_DO_NOT_QUEUE</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>DBUS_NAME_FLAG_REPLACE_EXISTING</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>DBUS_RELEASE_NAME_REPLY_NON_EXISTANT</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>DBUS_RELEASE_NAME_REPLY_NOT_OWNER</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>DBUS_RELEASE_NAME_REPLY_RELEASED</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>DBUS_REQUEST_NAME_REPLY_ALREADY_OWNER</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>DBUS_REQUEST_NAME_REPLY_EXISTS</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>DBUS_REQUEST_NAME_REPLY_IN_QUEUE</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>DBUS_REQUEST_NAME_REPLY_PRIMARY_OWNER</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>DBUS_START_REPLY_ALREADY_RUNNING</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>DBUS_START_REPLY_SUCCESS</code></strong><br />
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
<td><strong><code>AddMatch</code></strong><code>(</code><code>String</code><code> matchrule)</code><br />
          Add a match rule.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>Byte</code><code>[]</code></td>
<td><strong><code>GetConnectionSELinuxSecurityContext</code></strong><code>(</code><code>String</code><code> a)</code><br />
          Does something undocumented.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>UInt32</code></td>
<td><strong><code>GetConnectionUnixProcessID</code></strong><code>(</code><code>String</code><code> connection_name)</code><br />
          Returns the proccess ID associated with a connection.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>UInt32</code></td>
<td><strong><code>GetConnectionUnixUser</code></strong><code>(</code><code>String</code><code> connection_name)</code><br />
          Get the Unix UID that owns a connection name.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>GetNameOwner</code></strong><code>(</code><code>String</code><code> name)</code><br />
          Get the connection unique name that owns the given name.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>Hello</code></strong><code>()</code><br />
          Initial message to register ourselves on the Bus.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code><code>[]</code></td>
<td><strong><code>ListNames</code></strong><code>()</code><br />
          Lists all connected names on the Bus.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code><code>[]</code></td>
<td><strong><code>ListQueuedOwners</code></strong><code>(</code><code>String</code><code> name)</code><br />
          List the connections currently queued for a name.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> boolean</code></td>
<td><strong><code>NameHasOwner</code></strong><code>(</code><code>String</code><code> name)</code><br />
          Determine if a name has an owner.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>UInt32</code></td>
<td><strong><code>ReleaseName</code></strong><code>(</code><code>String</code><code> name)</code><br />
          Release a name on the bus.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>ReloadConfig</code></strong><code>()</code><br />
          Does something undocumented.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>RemoveMatch</code></strong><code>(</code><code>String</code><code> matchrule)</code><br />
          Remove a match rule.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>UInt32</code></td>
<td><strong><code>RequestName</code></strong><code>(</code><code>String</code><code> name, </code><code>UInt32</code><code> flags)</code><br />
          Request a name on the bus.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>UInt32</code></td>
<td><strong><code>StartServiceByName</code></strong><code>(</code><code>String</code><code> name, </code><code>UInt32</code><code> flags)</code><br />
          Start a service.</td>
</tr>
</tbody>
</table>

 

| **Methods inherited from interface org.freedesktop.dbus.DBusInterface** |
|-------------------------------------------------------------------------|
| `isRemote`                                                              |

 

| **Field Detail** |
|------------------|

### DBUS_NAME_FLAG_ALLOW_REPLACEMENT

    static final int DBUS_NAME_FLAG_ALLOW_REPLACEMENT

**See Also:**  
Constant Field Values

### DBUS_NAME_FLAG_REPLACE_EXISTING

    static final int DBUS_NAME_FLAG_REPLACE_EXISTING

**See Also:**  
Constant Field Values

### DBUS_NAME_FLAG_DO_NOT_QUEUE

    static final int DBUS_NAME_FLAG_DO_NOT_QUEUE

**See Also:**  
Constant Field Values

### DBUS_REQUEST_NAME_REPLY_PRIMARY_OWNER

    static final int DBUS_REQUEST_NAME_REPLY_PRIMARY_OWNER

**See Also:**  
Constant Field Values

### DBUS_REQUEST_NAME_REPLY_IN_QUEUE

    static final int DBUS_REQUEST_NAME_REPLY_IN_QUEUE

**See Also:**  
Constant Field Values

### DBUS_REQUEST_NAME_REPLY_EXISTS

    static final int DBUS_REQUEST_NAME_REPLY_EXISTS

**See Also:**  
Constant Field Values

### DBUS_REQUEST_NAME_REPLY_ALREADY_OWNER

    static final int DBUS_REQUEST_NAME_REPLY_ALREADY_OWNER

**See Also:**  
Constant Field Values

### DBUS_RELEASE_NAME_REPLY_RELEASED

    static final int DBUS_RELEASE_NAME_REPLY_RELEASED

**See Also:**  
Constant Field Values

### DBUS_RELEASE_NAME_REPLY_NON_EXISTANT

    static final int DBUS_RELEASE_NAME_REPLY_NON_EXISTANT

**See Also:**  
Constant Field Values

### DBUS_RELEASE_NAME_REPLY_NOT_OWNER

    static final int DBUS_RELEASE_NAME_REPLY_NOT_OWNER

**See Also:**  
Constant Field Values

### DBUS_START_REPLY_SUCCESS

    static final int DBUS_START_REPLY_SUCCESS

**See Also:**  
Constant Field Values

### DBUS_START_REPLY_ALREADY_RUNNING

    static final int DBUS_START_REPLY_ALREADY_RUNNING

**See Also:**  
Constant Field Values

| **Method Detail** |
|-------------------|

### Hello

    String Hello()

Initial message to register ourselves on the Bus.

**Returns:**  
The unique name of this connection to the Bus.

### ListNames

    String[] ListNames()

Lists all connected names on the Bus.

**Returns:**  
An array of all connected names.

### NameHasOwner

    boolean NameHasOwner(String name)

Determine if a name has an owner.

**Parameters:**  
`name` - The name to query.

**Returns:**  
true if the name has an owner.

### GetNameOwner

    String GetNameOwner(String name)

Get the connection unique name that owns the given name.

**Parameters:**  
`name` - The name to query.

**Returns:**  
The connection which owns the name.

### GetConnectionUnixUser

    UInt32 GetConnectionUnixUser(String connection_name)

Get the Unix UID that owns a connection name.

**Parameters:**  
`connection_name` - The connection name.

**Returns:**  
The Unix UID that owns it.

### StartServiceByName

    UInt32 StartServiceByName(String name,
                              UInt32 flags)

Start a service. If the given service is not provided by any application, it will be started according to the .service file for that service.

**Parameters:**  
`name` - The service name to start.

`flags` - Unused.

**Returns:**  
DBUS_START_REPLY constants.

### RequestName

    UInt32 RequestName(String name,
                       UInt32 flags)

Request a name on the bus.

**Parameters:**  
`name` - The name to request.

`flags` - DBUS_NAME flags.

**Returns:**  
DBUS_REQUEST_NAME_REPLY constants.

### ReleaseName

    UInt32 ReleaseName(String name)

Release a name on the bus.

**Parameters:**  
`name` - The name to release.

**Returns:**  
DBUS_RELEASE_NAME_REPLY constants.

### AddMatch

    void AddMatch(String matchrule)
                  throws DBus.Error.MatchRuleInvalid

Add a match rule. Will cause you to receive messages that aren't directed to you which match this rule.

**Parameters:**  
`matchrule` - The Match rule as a string. Format Undocumented.

**Throws:**  
`DBus.Error.MatchRuleInvalid`

### RemoveMatch

    void RemoveMatch(String matchrule)
                     throws DBus.Error.MatchRuleInvalid

Remove a match rule. Will cause you to stop receiving messages that aren't directed to you which match this rule.

**Parameters:**  
`matchrule` - The Match rule as a string. Format Undocumented.

**Throws:**  
`DBus.Error.MatchRuleInvalid`

### ListQueuedOwners

    String[] ListQueuedOwners(String name)

List the connections currently queued for a name.

**Parameters:**  
`name` - The name to query

**Returns:**  
A list of unique connection IDs.

### GetConnectionUnixProcessID

    UInt32 GetConnectionUnixProcessID(String connection_name)

Returns the proccess ID associated with a connection.

**Parameters:**  
`connection_name` - The name of the connection

**Returns:**  
The PID of the connection.

### GetConnectionSELinuxSecurityContext

    Byte[] GetConnectionSELinuxSecurityContext(String a)

Does something undocumented.

### ReloadConfig

    void ReloadConfig()

Does something undocumented.
