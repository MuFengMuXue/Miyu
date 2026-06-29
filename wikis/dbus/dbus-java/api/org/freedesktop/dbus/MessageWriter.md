## org.freedesktop.dbus Class MessageWriter

    java.lang.Object
      org.freedesktop.dbus.MessageWriter

    public class MessageWriterextends Object

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
<td><strong><code>MessageWriter</code></strong><code>(</code><code>OutputStream</code><code> out)</code><br />
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
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>writeMessage</code></strong><code>(</code><code>Message</code><code> m)</code><br />
           </td>
</tr>
</tbody>
</table>

 

| **Methods inherited from class java.lang.Object** |
|----|
| `clone``, ``equals``, ``finalize``, ``getClass``, ``hashCode``, ``notify``, ``notifyAll``, ``toString``, ``wait``, ``wait``, ``wait` |

 

| **Constructor Detail** |
|------------------------|

### MessageWriter

    public MessageWriter(OutputStream out)

| **Method Detail** |
|-------------------|

### writeMessage

    public void writeMessage(Message m)
                      throws IOException

**Throws:**  
`IOException`

### close

    public void close()
               throws IOException

**Throws:**  
`IOException`
