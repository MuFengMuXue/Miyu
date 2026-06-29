## org.freedesktop.dbus Class Struct

    java.lang.Object
      org.freedesktop.dbus.Struct

**Direct Known Subclasses:**  
DBus.Binding.TestStruct

<!-- -->

    public abstract class Structextends Object

This class should be extended to create Structs. Any such class may be sent over DBus to a method which takes a Struct. All fields in the Struct which you wish to be serialized and sent to the remote method should be annotated with the org.freedesktop.dbus.Position annotation, in the order they should appear in to Struct to DBus.

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
<td><strong><code>Struct</code></strong><code>()</code><br />
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

 

| **Constructor Detail** |
|------------------------|

### Struct

    public Struct()

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
