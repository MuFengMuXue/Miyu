## org.freedesktop.dbus Class Variant\<T\>

    java.lang.Object
      org.freedesktop.dbus.Variant<T>

    public class Variant<T>extends Object

A Wrapper class for Variant values. A method on DBus can send or receive a Variant. This will wrap another value whose type is determined at runtime. The Variant may be parameterized to restrict the types it may accept.

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
<td><strong><code>Variant</code></strong><code>(</code><code>T</code><code> o)</code><br />
          Create a Variant from a basic type object.</td>
<td></td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td><strong><code>Variant</code></strong><code>(</code><code>T</code><code> o, </code><code>String</code><code> sig)</code><br />
          Create a Variant.</td>
<td></td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td><strong><code>Variant</code></strong><code>(</code><code>T</code><code> o, </code><code>Type</code><code> type)</code><br />
          Create a Variant.</td>
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
          Compare this Variant with another by comparing contents</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>getSig</code></strong><code>()</code><br />
          Return the dbus signature of the wrapped value.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>Type</code></td>
<td><strong><code>getType</code></strong><code>()</code><br />
          Return the type of the wrapped value.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>T</code></td>
<td><strong><code>getValue</code></strong><code>()</code><br />
          Return the wrapped value.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>toString</code></strong><code>()</code><br />
          Format the Variant as a string.</td>
</tr>
</tbody>
</table>

 

| **Methods inherited from class java.lang.Object** |
|----|
| `clone``, ``finalize``, ``getClass``, ``hashCode``, ``notify``, ``notifyAll``, ``wait``, ``wait``, ``wait` |

 

| **Constructor Detail** |
|------------------------|

### Variant

    public Variant(T o)
            throws IllegalArgumentException

Create a Variant from a basic type object.

**Parameters:**  
`o` - The wrapped value.

**Throws:**  
`IllegalArugmentException` - If you try and wrap Null or an object of a non-basic type.

`IllegalArgumentException`

### Variant

    public Variant(T o,
                   Type type)
            throws IllegalArgumentException

Create a Variant.

**Parameters:**  
`o` - The wrapped value.

`type` - The explicit type of the value.

**Throws:**  
`IllegalArugmentException` - If you try and wrap Null or an object which cannot be sent over DBus.

`IllegalArgumentException`

### Variant

    public Variant(T o,
                   String sig)
            throws IllegalArgumentException

Create a Variant.

**Parameters:**  
`o` - The wrapped value.

`sig` - The explicit type of the value, as a dbus type string.

**Throws:**  
`IllegalArugmentException` - If you try and wrap Null or an object which cannot be sent over DBus.

`IllegalArgumentException`

| **Method Detail** |
|-------------------|

### getValue

    public T getValue()

Return the wrapped value.

### getType

    public Type getType()

Return the type of the wrapped value.

### getSig

    public String getSig()

Return the dbus signature of the wrapped value.

### toString

    public String toString()

Format the Variant as a string.

**Overrides:**  
`toString` in class `Object`

### equals

    public boolean equals(Object other)

Compare this Variant with another by comparing contents

**Overrides:**  
`equals` in class `Object`
