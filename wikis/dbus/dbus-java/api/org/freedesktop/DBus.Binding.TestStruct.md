## org.freedesktop Class DBus.Binding.TestStruct

    java.lang.Object
      org.freedesktop.dbus.Struct
          org.freedesktop.DBus.Binding.TestStruct

**Enclosing interface:**  
DBus.Binding

<!-- -->

    public static final class DBus.Binding.TestStructextends Struct

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
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>a</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>UInt32</code></td>
<td><strong><code>b</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>Short</code></td>
<td><strong><code>c</code></strong><br />
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
<td><strong><code>DBus.Binding.TestStruct</code></strong><code>(</code><code>String</code><code> a, </code><code>UInt32</code><code> b, </code><code>Short</code><code> c)</code><br />
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
<td style="text-align: right;" data-valign="top" width="1%"><code> boolean</code></td>
<td><strong><code>equals</code></strong><code>(</code><code>Object</code><code> other)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>Object</code><code>[]</code></td>
<td><strong><code>getParameters</code></strong><code>()</code><br />
          Returns the struct contents in order.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>toString</code></strong><code>()</code><br />
          Returns this struct as a string.</td>
</tr>
</tbody>
</table>

 

| **Methods inherited from class java.lang.Object** |
|----|
| `clone``, ``finalize``, ``getClass``, ``hashCode``, ``notify``, ``notifyAll``, ``wait``, ``wait``, ``wait` |

 

| **Field Detail** |
|------------------|

### a

    public final String a

### b

    public final UInt32 b

### c

    public final Short c

| **Constructor Detail** |
|------------------------|

### DBus.Binding.TestStruct

    public DBus.Binding.TestStruct(String a,
                                   UInt32 b,
                                   Short c)

| **Method Detail** |
|-------------------|

### getParameters

    public final Object[] getParameters()

Returns the struct contents in order.

**Throws:**  
`DBusException` - If there is a problem doing this.

### toString

    public final String toString()

Returns this struct as a string.

**Overrides:**  
`toString` in class `Object`

### equals

    public final boolean equals(Object other)

**Overrides:**  
`equals` in class `Object`
