## org.freedesktop.dbus Class UInt64

    java.lang.Object
      java.lang.Number
          org.freedesktop.dbus.UInt64

**All Implemented Interfaces:**  
Serializable, Comparable\<UInt64\>

<!-- -->

    public class UInt64extends Numberimplements Comparable<UInt64>

Class to represent unsigned 64-bit numbers. Warning: Any functions which take or return a `long` are restricted to the range of a signed 64bit number. Use the BigInteger methods if you wish access to the full range.

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
<td style="text-align: right;" data-valign="top" width="1%"><code>static </code><code>BigInteger</code></td>
<td><strong><code>MAX_BIG_VALUE</code></strong><br />
          Maximum allowed value (when accessed as a BigInteger)</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static long</code></td>
<td><strong><code>MAX_LONG_VALUE</code></strong><br />
          Maximum allowed value (when accessed as a long)</td>
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
<td><strong><code>UInt64</code></strong><code>(</code><code>BigInteger</code><code> value)</code><br />
          Create a UInt64 from a BigInteger</td>
<td></td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td><strong><code>UInt64</code></strong><code>(long value)</code><br />
          Create a UInt64 from a long.</td>
<td></td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td><strong><code>UInt64</code></strong><code>(long top, long bottom)</code><br />
          Create a UInt64 from two longs.</td>
<td></td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td><strong><code>UInt64</code></strong><code>(</code><code>String</code><code> value)</code><br />
          Create a UInt64 from a String.</td>
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
<td style="text-align: right;" data-valign="top" width="1%"><code> long</code></td>
<td><strong><code>bottom</code></strong><code>()</code><br />
          Least significant 4 bytes.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> byte</code></td>
<td><strong><code>byteValue</code></strong><code>()</code><br />
          The value of this as a byte.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> int</code></td>
<td><strong><code>compareTo</code></strong><code>(</code><code>UInt64</code><code> other)</code><br />
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
          Test two UInt64s for equality.</td>
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
<td style="text-align: right;" data-valign="top" width="1%"><code> long</code></td>
<td><strong><code>top</code></strong><code>()</code><br />
          Most significant 4 bytes.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>toString</code></strong><code>()</code><br />
          The value of this as a string.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>BigInteger</code></td>
<td><strong><code>value</code></strong><code>()</code><br />
          The value of this as a BigInteger.</td>
</tr>
</tbody>
</table>

 

| **Methods inherited from class java.lang.Object** |
|----|
| `clone``, ``finalize``, ``getClass``, ``notify``, ``notifyAll``, ``wait``, ``wait``, ``wait` |

 

| **Field Detail** |
|------------------|

### MAX_LONG_VALUE

    public static final long MAX_LONG_VALUE

Maximum allowed value (when accessed as a long)

**See Also:**  
Constant Field Values

### MAX_BIG_VALUE

    public static final BigInteger MAX_BIG_VALUE

Maximum allowed value (when accessed as a BigInteger)

### MIN_VALUE

    public static final long MIN_VALUE

Minimum allowed value

**See Also:**  
Constant Field Values

| **Constructor Detail** |
|------------------------|

### UInt64

    public UInt64(long value)

Create a UInt64 from a long.

**Parameters:**  
`value` - Must be a valid integer within MIN_VALUE–MAX_VALUE

**Throws:**  
`NumberFormatException` - if value is not between MIN_VALUE and MAX_VALUE

### UInt64

    public UInt64(long top,
                  long bottom)

Create a UInt64 from two longs.

**Parameters:**  
`top` - Most significant 4 bytes.

`bottom` - Least significant 4 bytes.

### UInt64

    public UInt64(BigInteger value)

Create a UInt64 from a BigInteger

**Parameters:**  
`value` - Must be a valid BigInteger between MIN_VALUE–MAX_BIG_VALUE

**Throws:**  
`NumberFormatException` - if value is not an integer between MIN_VALUE and MAX_BIG_VALUE

### UInt64

    public UInt64(String value)

Create a UInt64 from a String.

**Parameters:**  
`value` - Must parse to a valid integer within MIN_VALUE–MAX_BIG_VALUE

**Throws:**  
`NumberFormatException` - if value is not an integer between MIN_VALUE and MAX_BIG_VALUE

| **Method Detail** |
|-------------------|

### value

    public BigInteger value()

The value of this as a BigInteger.

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

Test two UInt64s for equality.

**Overrides:**  
`equals` in class `Object`

### hashCode

    public int hashCode()

**Overrides:**  
`hashCode` in class `Object`

### compareTo

    public int compareTo(UInt64 other)

Compare two UInt32s.

**Specified by:**  
`compareTo` in interface `Comparable``<``UInt64``>`

<!-- -->

**Returns:**  
0 if equal, -ve or +ve if they are different.

### toString

    public String toString()

The value of this as a string.

**Overrides:**  
`toString` in class `Object`

### top

    public long top()

Most significant 4 bytes.

### bottom

    public long bottom()

Least significant 4 bytes.
