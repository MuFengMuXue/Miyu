## org.freedesktop.dbus Class MessageReader

    java.lang.Object
      org.freedesktop.dbus.MessageReader

    public class MessageReaderextends Object

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
<td><strong><code>MessageReader</code></strong><code>(</code><code>InputStream</code><code> in)</code><br />
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
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>close</code></strong><code>()</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>Message</code></td>
<td><strong><code>readMessage</code></strong><code>()</code><br />
           </td>
</tr>
</tbody>
</table>

 

| **Methods inherited from class java.lang.Object** |
|----|
| `clone``, ``equals``, ``finalize``, ``getClass``, ``hashCode``, ``notify``, ``notifyAll``, ``toString``, ``wait``, ``wait``, ``wait` |

 

| **Constructor Detail** |
|------------------------|

### MessageReader

    public MessageReader(InputStream in)

| **Method Detail** |
|-------------------|

### readMessage

    public Message readMessage()
                        throws IOException,
                               DBusException

**Throws:**  
`IOException`

`DBusException`

### close

    public void close()
               throws IOException

**Throws:**  
`IOException`
