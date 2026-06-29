## org.freedesktop Class DBus.Local.Disconnected

    java.lang.Object
      org.freedesktop.dbus.Message
          org.freedesktop.dbus.DBusSignal
              org.freedesktop.DBus.Local.Disconnected

**Enclosing interface:**  
DBus.Local

<!-- -->

    public static class DBus.Local.Disconnectedextends DBusSignal

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
<td><strong><code>DBus.Local.Disconnected</code></strong><code>(</code><code>String</code><code> path)</code><br />
           </td>
<td></td>
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

### DBus.Local.Disconnected

    public DBus.Local.Disconnected(String path)
                            throws DBusException

**Throws:**  
`DBusException`
