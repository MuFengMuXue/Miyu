## org.freedesktop.dbus Class DBusCallInfo

    java.lang.Object
      org.freedesktop.dbus.DBusCallInfo

    public class DBusCallInfoextends Object

Holds information on a method call

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
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>ASYNC</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>NO_REPLY</code></strong><br />
          Indicates the caller won't wait for a reply (and we won't send one).</td>
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
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>getDestination</code></strong><code>()</code><br />
          Returns the name with which we were addressed on the Bus</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> int</code></td>
<td><strong><code>getFlags</code></strong><code>()</code><br />
          Returns any flags set on this method call</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>getInterface</code></strong><code>()</code><br />
          Returns the interface this method was called with</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>getMethod</code></strong><code>()</code><br />
          Returns the method name used to call this method</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>getObjectPath</code></strong><code>()</code><br />
          Returns the object path used to call this method</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>getSource</code></strong><code>()</code><br />
          Returns the BusID which called the method</td>
</tr>
</tbody>
</table>

 

| **Methods inherited from class java.lang.Object** |
|----|
| `clone``, ``equals``, ``finalize``, ``getClass``, ``hashCode``, ``notify``, ``notifyAll``, ``toString``, ``wait``, ``wait``, ``wait` |

 

| **Field Detail** |
|------------------|

### NO_REPLY

    public static final int NO_REPLY

Indicates the caller won't wait for a reply (and we won't send one).

**See Also:**  
Constant Field Values

### ASYNC

    public static final int ASYNC

**See Also:**  
Constant Field Values

| **Method Detail** |
|-------------------|

### getSource

    public String getSource()

Returns the BusID which called the method

### getDestination

    public String getDestination()

Returns the name with which we were addressed on the Bus

### getObjectPath

    public String getObjectPath()

Returns the object path used to call this method

### getInterface

    public String getInterface()

Returns the interface this method was called with

### getMethod

    public String getMethod()

Returns the method name used to call this method

### getFlags

    public int getFlags()

Returns any flags set on this method call
