## org.freedesktop.dbus Class UInt32

    java.lang.Object
      java.lang.Number
          org.freedesktop.dbus.UInt32

**All Implemented Interfaces:**  
Serializable, Comparable\<UInt32\>

<!-- -->

    public class UInt32extends Numberimplements Comparable<UInt32>

Class to represent unsigned 32-bit numbers.

**See Also:**  
Serialized Form

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
<td style="text-align: right;" data-valign="top" width="1%"><code>static long</code></td>
<td><strong><code>MAX_VALUE</code></strong><br />
          Maximum allowed value</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static long</code></td>
<td><strong><code>MIN_VALUE</code></strong><br />
          Minimum allowed value</td>
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
<td><strong><code>UInt32</code></strong><code>(long value)</code><br />
          Create a UInt32 from a long.</td>
<td></td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td><strong><code>UInt32</code></strong><code>(</code><code>String</code><code> value)</code><br />
          Create a UInt32 from a String.</td>
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
<td style="text-align: right;" data-valign="top" width="1%"><code> byte</code></td>
<td><strong><code>byteValue</code></strong><code>()</code><br />
          The value of this as a byte.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> int</code></td>
<td><strong><code>compareTo</code></strong><code>(</code><code>UInt32</code><code> other)</code><br />
          Compare two UInt32s.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> double</code></td>
<td><strong><code>doubleValue</code></strong><code>()</code><br />
          The value of this as a double.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> boolean</code></td>
<td><strong><code>equals</code></strong><code>(</code><code>Object</code><code> o)</code><br />
          Test two UInt32s for equality.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> float</code></td>
<td><strong><code>floatValue</code></strong><code>()</code><br />
          The value of this as a float.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> int</code></td>
<td><strong><code>hashCode</code></strong><code>()</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> int</code></td>
<td><strong><code>intValue</code></strong><code>()</code><br />
          The value of this as a int.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> long</code></td>
<td><strong><code>longValue</code></strong><code>()</code><br />
          The value of this as a long.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> short</code></td>
<td><strong><code>shortValue</code></strong><code>()</code><br />
          The value of this as a short.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>toString</code></strong><code>()</code><br />
          The value of this as a string</td>
</tr>
</tbody>
</table>

 

| **Methods inherited from class java.lang.Object** |
|----|
| `clone``, ``finalize``, ``getClass``, ``notify``, ``notifyAll``, ``wait``, ``wait``, ``wait` |

 

| **Field Detail** |
|------------------|

### MAX_VALUE

    public static final long MAX_VALUE

Maximum allowed value

**See Also:**  
Constant Field Values

### MIN_VALUE

    public static final long MIN_VALUE

Minimum allowed value

**See Also:**  
Constant Field Values

| **Constructor Detail** |
|------------------------|

### UInt32

    public UInt32(long value)

Create a UInt32 from a long.

**Parameters:**  
`value` - Must be a valid integer within MIN_VALUE–MAX_VALUE

**Throws:**  
`NumberFormatException` - if value is not between MIN_VALUE and MAX_VALUE

### UInt32

    public UInt32(String value)

Create a UInt32 from a String.

**Parameters:**  
`value` - Must parse to a valid integer within MIN_VALUE–MAX_VALUE

**Throws:**  
`NumberFormatException` - if value is not an integer between MIN_VALUE and MAX_VALUE

| **Method Detail** |
|-------------------|

### byteValue

    public byte byteValue()

The value of this as a byte.

**Overrides:**  
`byteValue` in class `Number`

### doubleValue

    public double doubleValue()

The value of this as a double.

**Specified by:**  
`doubleValue` in class `Number`

### floatValue

    public float floatValue()

The value of this as a float.

**Specified by:**  
`floatValue` in class `Number`

### intValue

    public int intValue()

The value of this as a int.

**Specified by:**  
`intValue` in class `Number`

### longValue

    public long longValue()

The value of this as a long.

**Specified by:**  
`longValue` in class `Number`

### shortValue

    public short shortValue()

The value of this as a short.

**Overrides:**  
`shortValue` in class `Number`

### equals

    public boolean equals(Object o)

Test two UInt32s for equality.

**Overrides:**  
`equals` in class `Object`

### hashCode

    public int hashCode()

**Overrides:**  
`hashCode` in class `Object`

### compareTo

    public int compareTo(UInt32 other)

Compare two UInt32s.

**Specified by:**  
`compareTo` in interface `Comparable``<``UInt32``>`

<!-- -->

**Returns:**  
0 if equal, -ve or +ve if they are different.

### toString

    public String toString()

The value of this as a string

**Overrides:**  
`toString` in class `Object`
