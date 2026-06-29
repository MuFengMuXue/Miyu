## org.freedesktop Class DBus.Binding.TestSignals.Triggered

    java.lang.Object
      org.freedesktop.dbus.Message
          org.freedesktop.dbus.DBusSignal
              org.freedesktop.DBus.Binding.TestSignals.Triggered

**Enclosing interface:**  
DBus.Binding.TestSignals

<!-- -->

    public static class DBus.Binding.TestSignals.Triggeredextends DBusSignal

| **Nested Class Summary** |     |
|--------------------------|-----|

 

| **Nested classes/interfaces inherited from class org.freedesktop.dbus.Message** |
|----|
| `Message.ArgumentType``, ``Message.Endian``, ``Message.Flags``, ``Message.HeaderField``, ``Message.MessageType` |

 

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
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>UInt64</code></td>
<td><strong><code>a</code></strong><br />
           </td>
</tr>
</tbody>
</table>

 

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
<td><strong><code>DBus.Binding.TestSignals.Triggered</code></strong><code>(</code><code>String</code><code> path, </code><code>UInt64</code><code> a)</code><br />
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

 

| **Field Detail** |
|------------------|

### a

    public final UInt64 a

| **Constructor Detail** |
|------------------------|

### DBus.Binding.TestSignals.Triggered

    public DBus.Binding.TestSignals.Triggered(String path,
                                              UInt64 a)
                                       throws DBusException

**Throws:**  
`DBusException`
