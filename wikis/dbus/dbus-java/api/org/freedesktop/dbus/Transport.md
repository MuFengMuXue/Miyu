## org.freedesktop.dbus Class Transport

    java.lang.Object
      org.freedesktop.dbus.Transport

    public class Transportextends Object

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
<td style="text-align: right;" data-valign="top" width="1%"><code>static class</code></td>
<td><strong><code>Transport.SASL</code></strong><br />
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
<th colspan="2" style="text-align: left;"><strong>Field Summary</strong></th>
</tr>
</thead>
<tbody>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>MessageReader</code></td>
<td><strong><code>min</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>MessageWriter</code></td>
<td><strong><code>mout</code></strong><br />
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
<th colspan="2" style="text-align: left;"><strong>Constructor Summary</strong></th>
</tr>
</thead>
<tbody>
<tr class="TableRowColor" data-bgcolor="white">
<td><strong><code>Transport</code></strong><code>()</code><br />
           </td>
<td></td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td><strong><code>Transport</code></strong><code>(</code><code>BusAddress</code><code> address)</code><br />
           </td>
<td></td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td><strong><code>Transport</code></strong><code>(</code><code>String</code><code> address)</code><br />
           </td>
<td></td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td><strong><code>Transport</code></strong><code>(</code><code>String</code><code> address, int timeout)</code><br />
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
<td><strong><code>connect</code></strong><code>(</code><code>BusAddress</code><code> address)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>connect</code></strong><code>(</code><code>BusAddress</code><code> address, int timeout)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>connect</code></strong><code>(</code><code>String</code><code> address)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>connect</code></strong><code>(</code><code>String</code><code> address, int timeout)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>disconnect</code></strong><code>()</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static </code><code>String</code></td>
<td><strong><code>genGUID</code></strong><code>()</code><br />
           </td>
</tr>
</tbody>
</table>

 

| **Methods inherited from class java.lang.Object** |
|----|
| `clone``, ``equals``, ``finalize``, ``getClass``, ``hashCode``, ``notify``, ``notifyAll``, ``toString``, ``wait``, ``wait``, ``wait` |

 

| **Field Detail** |
|------------------|

### min

    public MessageReader min

### mout

    public MessageWriter mout

| **Constructor Detail** |
|------------------------|

### Transport

    public Transport()

### Transport

    public Transport(BusAddress address)
              throws IOException

**Throws:**  
`IOException`

### Transport

    public Transport(String address)
              throws IOException,
                     ParseException

**Throws:**  
`IOException`

`ParseException`

### Transport

    public Transport(String address,
                     int timeout)
              throws IOException,
                     ParseException

**Throws:**  
`IOException`

`ParseException`

| **Method Detail** |
|-------------------|

### genGUID

    public static String genGUID()

### connect

    public void connect(String address)
                 throws IOException,
                        ParseException

**Throws:**  
`IOException`

`ParseException`

### connect

    public void connect(String address,
                        int timeout)
                 throws IOException,
                        ParseException

**Throws:**  
`IOException`

`ParseException`

### connect

    public void connect(BusAddress address)
                 throws IOException

**Throws:**  
`IOException`

### connect

    public void connect(BusAddress address,
                        int timeout)
                 throws IOException

**Throws:**  
`IOException`

### disconnect

    public void disconnect()
                    throws IOException

**Throws:**  
`IOException`
