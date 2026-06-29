## org.freedesktop.dbus Class MethodReturn

    java.lang.Object
      org.freedesktop.dbus.Message
          org.freedesktop.dbus.MethodReturn

    public class MethodReturnextends Message

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
<td><strong><code>MethodReturn</code></strong><code>(</code><code>MethodCall</code><code> mc, </code><code>String</code><code> sig, </code><code>Object</code><code>... args)</code><br />
           </td>
<td></td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td><strong><code>MethodReturn</code></strong><code>(</code><code>String</code><code> dest, long replyserial, </code><code>String</code><code> sig, </code><code>Object</code><code>... args)</code><br />
           </td>
<td></td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td><strong><code>MethodReturn</code></strong><code>(</code><code>String</code><code> source, </code><code>MethodCall</code><code> mc, </code><code>String</code><code> sig, </code><code>Object</code><code>... args)</code><br />
           </td>
<td></td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td><strong><code>MethodReturn</code></strong><code>(</code><code>String</code><code> source, </code><code>String</code><code> dest, long replyserial, </code><code>String</code><code> sig, </code><code>Object</code><code>... args)</code><br />
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
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>MethodCall</code></td>
<td><strong><code>getCall</code></strong><code>()</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  void</code></td>
<td><strong><code>setCall</code></strong><code>(</code><code>MethodCall</code><code> call)</code><br />
           </td>
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

### MethodReturn

    public MethodReturn(String dest,
                        long replyserial,
                        String sig,
                        Object... args)
                 throws DBusException

**Throws:**  
`DBusException`

### MethodReturn

    public MethodReturn(String source,
                        String dest,
                        long replyserial,
                        String sig,
                        Object... args)
                 throws DBusException

**Throws:**  
`DBusException`

### MethodReturn

    public MethodReturn(MethodCall mc,
                        String sig,
                        Object... args)
                 throws DBusException

**Throws:**  
`DBusException`

### MethodReturn

    public MethodReturn(String source,
                        MethodCall mc,
                        String sig,
                        Object... args)
                 throws DBusException

**Throws:**  
`DBusException`

| **Method Detail** |
|-------------------|

### getCall

    public MethodCall getCall()

### setCall

    protected void setCall(MethodCall call)
