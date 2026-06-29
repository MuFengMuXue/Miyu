## org.freedesktop.dbus Class MethodCall

    java.lang.Object
      org.freedesktop.dbus.Message
          org.freedesktop.dbus.MethodCall

    public class MethodCallextends Message

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
<td><strong><code>MethodCall</code></strong><code>(</code><code>String</code><code> dest, </code><code>String</code><code> path, </code><code>String</code><code> iface, </code><code>String</code><code> member, byte flags, </code><code>String</code><code> sig, </code><code>Object</code><code>... args)</code><br />
           </td>
<td></td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td><strong><code>MethodCall</code></strong><code>(</code><code>String</code><code> source, </code><code>String</code><code> dest, </code><code>String</code><code> path, </code><code>String</code><code> iface, </code><code>String</code><code> member, byte flags, </code><code>String</code><code> sig, </code><code>Object</code><code>... args)</code><br />
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
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>Message</code></td>
<td><strong><code>getReply</code></strong><code>()</code><br />
          Block (if neccessary) for a reply.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>Message</code></td>
<td><strong><code>getReply</code></strong><code>(long timeout)</code><br />
          Block (if neccessary) for a reply.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> boolean</code></td>
<td><strong><code>hasReply</code></strong><code>()</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static void</code></td>
<td><strong><code>setDefaultTimeout</code></strong><code>(long timeout)</code><br />
          Set the default timeout for method calls.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  void</code></td>
<td><strong><code>setReply</code></strong><code>(</code><code>Message</code><code> reply)</code><br />
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

### MethodCall

    public MethodCall(String dest,
                      String path,
                      String iface,
                      String member,
                      byte flags,
                      String sig,
                      Object... args)
               throws DBusException

**Throws:**  
`DBusException`

### MethodCall

    public MethodCall(String source,
                      String dest,
                      String path,
                      String iface,
                      String member,
                      byte flags,
                      String sig,
                      Object... args)
               throws DBusException

**Throws:**  
`DBusException`

| **Method Detail** |
|-------------------|

### setDefaultTimeout

    public static void setDefaultTimeout(long timeout)

Set the default timeout for method calls. Default is 20s.

**Parameters:**  
`timeout` - New timeout in ms.

### hasReply

    public boolean hasReply()

### getReply

    public Message getReply(long timeout)

Block (if neccessary) for a reply.

**Parameters:**  
`timeout` - The length of time to block before timing out (ms).

**Returns:**  
The reply to this MethodCall, or null if a timeout happens.

### getReply

    public Message getReply()

Block (if neccessary) for a reply. Default timeout is 20s, or can be configured with setDefaultTimeout()

**Returns:**  
The reply to this MethodCall, or null if a timeout happens.

### setReply

    protected void setReply(Message reply)
