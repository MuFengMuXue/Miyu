## org.freedesktop Class DBus.Binding.Triplet\<A,B,C\>

    java.lang.Object
      org.freedesktop.dbus.Tuple
          org.freedesktop.DBus.Binding.Triplet<A,B,C>

**Enclosing interface:**  
DBus.Binding

<!-- -->

    public static final class DBus.Binding.Triplet<A,B,C>extends Tuple

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
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>A</code></td>
<td><strong><code>a</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>B</code></td>
<td><strong><code>b</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>C</code></td>
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
<td><strong><code>DBus.Binding.Triplet</code></strong><code>(</code><code>A</code><code> a, </code><code>B</code><code> b, </code><code>C</code><code> c)</code><br />
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

    public final A a

### b

    public final B b

### c

    public final C c

| **Constructor Detail** |
|------------------------|

### DBus.Binding.Triplet

    public DBus.Binding.Triplet(A a,
                                B b,
                                C c)

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
