## org.freedesktop.dbus Class DBusSignal

    java.lang.Object
      org.freedesktop.dbus.Message
          org.freedesktop.dbus.DBusSignal

**Direct Known Subclasses:**  
DBus.Binding.TestClient.Trigger, DBus.Binding.TestSignals.Triggered, DBus.Local.Disconnected, DBus.NameAcquired, DBus.NameLost, DBus.NameOwnerChanged

<!-- -->

    public class DBusSignalextends Message

| **Nested Class Summary** |     |
|--------------------------|-----|

 

| **Nested classes/interfaces inherited from class org.freedesktop.dbus.Message** |
|----|
| `Message.ArgumentType``, ``Message.Endian``, ``Message.Flags``, ``Message.HeaderField``, ``Message.MessageType` |

 

| **Field Summary** |     |
|-------------------|-----|

 

| **Fields inherited from class org.freedesktop.dbus.Message** |
|----|
| `bytecounter``, ``flags``, ``globalserial``, ``headers``, ``PROTOCOL``, ``protover``, ``serial``, ``type``, ``wiredata` |

 

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
<td><strong><code>DBusSignal</code></strong><code>(</code><code>String</code><code> objectpath, </code><code>Object</code><code>... args)</code><br />
          Create a new signal.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code></td>
<td><strong><code>DBusSignal</code></strong><code>(</code><code>String</code><code> source, </code><code>String</code><code> path, </code><code>String</code><code> iface, </code><code>String</code><code> member, </code><code>String</code><code> sig, </code><code>Object</code><code>... args)</code><br />
           </td>
</tr>
</tbody>
</table>

 

| **Method Summary** |     |
|--------------------|-----|

 

| **Methods inherited from class org.freedesktop.dbus.Message** |
|----|
| `align``, ``append``, ``appendByte``, ``appendBytes``, ``appendint``, ``demarshallint``, ``demarshallint``, ``demarshallintBig``, ``demarshallintLittle``, ``extract``, ``extract``, ``getAlignment``, ``getDestination``, ``getFlags``, ``getHeader``, ``getHeaderFieldName``, ``getInterface``, ``getName``, ``getParameters``, ``getPath``, ``getReplySerial``, ``getSerial``, ``getSig``, ``getSource``, ``getWireData``, ``marshallint``, ``marshallintBig``, ``marshallintLittle``, ``pad``, ``setArgs``, ``setSource``, ``toString` |

 

| **Methods inherited from class java.lang.Object** |
|----|
| `clone``, ``equals``, ``finalize``, ``getClass``, ``hashCode``, ``notify``, ``notifyAll``, ``wait``, ``wait``, ``wait` |

 

| **Constructor Detail** |
|------------------------|

### DBusSignal

    public DBusSignal(String source,
                      String path,
                      String iface,
                      String member,
                      String sig,
                      Object... args)
               throws DBusException

**Throws:**  
`DBusException`

### DBusSignal

    protected DBusSignal(String objectpath,
                         Object... args)
                  throws DBusException

Create a new signal. This contructor MUST be called by all sub classes.

**Parameters:**  
`objectpath` - The path to the object this is emitted from.

`args` - The parameters of the signal.

**Throws:**  
`DBusException` - This is thrown if the subclass is incorrectly defined.
