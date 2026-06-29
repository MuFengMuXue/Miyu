## org.freedesktop.dbus.types Class DBusStructType

    java.lang.Object
      org.freedesktop.dbus.types.DBusStructType

**All Implemented Interfaces:**  
ParameterizedType, Type

<!-- -->

    public class DBusStructTypeextends Objectimplements ParameterizedType

The type of a struct. Should be used whenever you need a Type variable for a struct.

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
<td><strong><code>DBusStructType</code></strong><code>(</code><code>Type</code><code>... contents)</code><br />
          Create a struct type.</td>
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
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>Type</code><code>[]</code></td>
<td><strong><code>getActualTypeArguments</code></strong><code>()</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>Type</code></td>
<td><strong><code>getOwnerType</code></strong><code>()</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>Type</code></td>
<td><strong><code>getRawType</code></strong><code>()</code><br />
           </td>
</tr>
</tbody>
</table>

 

| **Methods inherited from class java.lang.Object** |
|----|
| `clone``, ``equals``, ``finalize``, ``getClass``, ``hashCode``, ``notify``, ``notifyAll``, ``toString``, ``wait``, ``wait``, ``wait` |

 

| **Constructor Detail** |
|------------------------|

### DBusStructType

    public DBusStructType(Type... contents)

Create a struct type.

**Parameters:**  
`contents` - The types contained in this struct.

| **Method Detail** |
|-------------------|

### getActualTypeArguments

    public Type[] getActualTypeArguments()

**Specified by:**  
`getActualTypeArguments` in interface `ParameterizedType`

### getRawType

    public Type getRawType()

**Specified by:**  
`getRawType` in interface `ParameterizedType`

### getOwnerType

    public Type getOwnerType()

**Specified by:**  
`getOwnerType` in interface `ParameterizedType`
