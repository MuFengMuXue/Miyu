## org.freedesktop.dbus Class Error

    java.lang.Object
      org.freedesktop.dbus.Message
          org.freedesktop.dbus.Error

    public class Errorextends Message

Error messages which can be sent over the bus.

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
<td><strong><code>Error</code></strong><code>(</code><code>Message</code><code> m, </code><code>Throwable</code><code> e)</code><br />
           </td>
<td></td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td><strong><code>Error</code></strong><code>(</code><code>String</code><code> source, </code><code>Message</code><code> m, </code><code>Throwable</code><code> e)</code><br />
           </td>
<td></td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td><strong><code>Error</code></strong><code>(</code><code>String</code><code> dest, </code><code>String</code><code> errorName, long replyserial, </code><code>String</code><code> sig, </code><code>Object</code><code>... args)</code><br />
           </td>
<td></td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td><strong><code>Error</code></strong><code>(</code><code>String</code><code> source, </code><code>String</code><code> dest, </code><code>String</code><code> errorName, long replyserial, </code><code>String</code><code> sig, </code><code>Object</code><code>... args)</code><br />
           </td>
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
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>DBusExecutionException</code></td>
<td><strong><code>getException</code></strong><code>()</code><br />
          Turns this into an exception of the correct type</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>throwException</code></strong><code>()</code><br />
          Throw this as an exception of the correct type</td>
</tr>
</tbody>
</table>

 

| **Methods inherited from class org.freedesktop.dbus.Message** |
|----|
| `align``, ``append``, ``appendByte``, ``appendBytes``, ``appendint``, ``demarshallint``, ``demarshallint``, ``demarshallintBig``, ``demarshallintLittle``, ``extract``, ``extract``, ``getAlignment``, ``getDestination``, ``getFlags``, ``getHeader``, ``getHeaderFieldName``, ``getInterface``, ``getName``, ``getParameters``, ``getPath``, ``getReplySerial``, ``getSerial``, ``getSig``, ``getSource``, ``getWireData``, ``marshallint``, ``marshallintBig``, ``marshallintLittle``, ``pad``, ``setArgs``, ``setSource``, ``toString` |

 

| **Methods inherited from class java.lang.Object** |
|----|
| `clone``, ``equals``, ``finalize``, ``getClass``, ``hashCode``, ``notify``, ``notifyAll``, ``wait``, ``wait``, ``wait` |

 

| **Constructor Detail** |
|------------------------|

### Error

    public Error(String dest,
                 String errorName,
                 long replyserial,
                 String sig,
                 Object... args)
          throws DBusException

**Throws:**  
`DBusException`

### Error

    public Error(String source,
                 String dest,
                 String errorName,
                 long replyserial,
                 String sig,
                 Object... args)
          throws DBusException

**Throws:**  
`DBusException`

### Error

    public Error(String source,
                 Message m,
                 Throwable e)
          throws DBusException

**Throws:**  
`DBusException`

### Error

    public Error(Message m,
                 Throwable e)
          throws DBusException

**Throws:**  
`DBusException`

| **Method Detail** |
|-------------------|

### getException

    public DBusExecutionException getException()

Turns this into an exception of the correct type

### throwException

    public void throwException()
                        throws DBusExecutionException

Throw this as an exception of the correct type

**Throws:**  
`DBusExecutionException`
