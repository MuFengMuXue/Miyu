## org.freedesktop.dbus Class DBusAsyncReply\<ReturnType\>

    java.lang.Object
      org.freedesktop.dbus.DBusAsyncReply<ReturnType>

    public class DBusAsyncReply<ReturnType>extends Object

A handle to an asynchronous method call.

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
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>ReturnType</code></td>
<td><strong><code>getReply</code></strong><code>()</code><br />
          Get the reply.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> boolean</code></td>
<td><strong><code>hasReply</code></strong><code>()</code><br />
          Check if we've had a reply.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static </code><code>Collection</code><code>&lt;</code><code>DBusAsyncReply</code><code>&lt;? extends </code><code>Object</code><code>&gt;&gt;</code></td>
<td><strong><code>hasReply</code></strong><code>(</code><code>Collection</code><code>&lt;</code><code>DBusAsyncReply</code><code>&lt;? extends </code><code>Object</code><code>&gt;&gt; replies)</code><br />
          Check if any of a set of asynchronous calls have had a reply.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>toString</code></strong><code>()</code><br />
           </td>
</tr>
</tbody>
</table>

 

| **Methods inherited from class java.lang.Object** |
|----|
| `clone``, ``equals``, ``finalize``, ``getClass``, ``hashCode``, ``notify``, ``notifyAll``, ``wait``, ``wait``, ``wait` |

 

| **Method Detail** |
|-------------------|

### hasReply

    public static Collection<DBusAsyncReply<? extends Object>> hasReply(Collection<DBusAsyncReply<? extends Object>> replies)

Check if any of a set of asynchronous calls have had a reply.

**Parameters:**  
`replies` - A Collection of handles to replies to check.

**Returns:**  
A Collection only containing those calls which have had replies.

### hasReply

    public boolean hasReply()

Check if we've had a reply.

**Returns:**  
True if we have a reply

### getReply

    public ReturnType getReply()
                        throws DBusExecutionException

Get the reply.

**Returns:**  
The return value from the method.

**Throws:**  
`DBusExecutionException` - if the reply to the method was an error.

`DBus.Error.NoReply` - if the method hasn't had a reply yet

### toString

    public String toString()

**Overrides:**  
`toString` in class `Object`
