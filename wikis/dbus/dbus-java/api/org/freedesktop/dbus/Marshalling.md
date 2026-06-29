## org.freedesktop.dbus Class Marshalling

    java.lang.Object
      org.freedesktop.dbus.Marshalling

    public class Marshallingextends Object

Contains static methods for marshalling values.

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
<td><strong><code>Marshalling</code></strong><code>()</code><br />
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
<td style="text-align: right;" data-valign="top" width="1%"><code>static </code><code>Object</code><code>[]</code></td>
<td><strong><code>convertParameters</code></strong><code>(</code><code>Object</code><code>[] parameters, </code><code>Type</code><code>[] types, </code><code>AbstractConnection</code><code> conn)</code><br />
          Recursively converts types for serialization onto DBus.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static </code><code>String</code><code>[]</code></td>
<td><strong><code>getDBusType</code></strong><code>(</code><code>Type</code><code> c)</code><br />
          Will return the DBus type corresponding to the given Java type.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static </code><code>String</code></td>
<td><strong><code>getDBusType</code></strong><code>(</code><code>Type</code><code>[] c)</code><br />
          Will return the DBus type corresponding to the given Java type.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static </code><code>String</code><code>[]</code></td>
<td><strong><code>getDBusType</code></strong><code>(</code><code>Type</code><code> c, boolean basic)</code><br />
          Will return the DBus type corresponding to the given Java type.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>getJavaType</code></strong><code>(</code><code>String</code><code> dbus, </code><code>List</code><code>&lt;</code><code>Type</code><code>&gt; rv, int limit)</code><br />
          Converts a dbus type string into Java Type objects,</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static </code><code>String</code><code>[]</code></td>
<td><strong><code>recursiveGetDBusType</code></strong><code>(</code><code>Type</code><code> c, boolean basic, int level)</code><br />
           </td>
</tr>
</tbody>
</table>

 

| **Methods inherited from class java.lang.Object** |
|----|
| `clone``, ``equals``, ``finalize``, ``getClass``, ``hashCode``, ``notify``, ``notifyAll``, ``toString``, ``wait``, ``wait``, ``wait` |

 

| **Constructor Detail** |
|------------------------|

### Marshalling

    public Marshalling()

| **Method Detail** |
|-------------------|

### getDBusType

    public static String getDBusType(Type[] c)
                              throws DBusException

Will return the DBus type corresponding to the given Java type. Note, container type should have their ParameterizedType not their Class passed in here.

**Parameters:**  
`c` - The Java types.

**Returns:**  
The DBus types.

**Throws:**  
`DBusException` - If the given type cannot be converted to a DBus type.

### getDBusType

    public static String[] getDBusType(Type c)
                                throws DBusException

Will return the DBus type corresponding to the given Java type. Note, container type should have their ParameterizedType not their Class passed in here.

**Parameters:**  
`c` - The Java type.

**Returns:**  
The DBus type.

**Throws:**  
`DBusException` - If the given type cannot be converted to a DBus type.

### getDBusType

    public static String[] getDBusType(Type c,
                                       boolean basic)
                                throws DBusException

Will return the DBus type corresponding to the given Java type. Note, container type should have their ParameterizedType not their Class passed in here.

**Parameters:**  
`c` - The Java type.

`basic` - If true enforces this to be a non-compound type. (compound types are Maps, Structs and Lists/arrays).

**Returns:**  
The DBus type.

**Throws:**  
`DBusException` - If the given type cannot be converted to a DBus type.

### recursiveGetDBusType

    public static String[] recursiveGetDBusType(Type c,
                                                boolean basic,
                                                int level)
                                         throws DBusException

**Throws:**  
`DBusException`

### getJavaType

    public static int getJavaType(String dbus,
                                  List<Type> rv,
                                  int limit)
                           throws DBusException

Converts a dbus type string into Java Type objects,

**Parameters:**  
`dbus` - The DBus type or types.

`rv` - Vector to return the types in.

`limit` - Maximum number of types to parse (-1 == nolimit).

**Returns:**  
number of characters parsed from the type string.

**Throws:**  
`DBusException`

### convertParameters

    public static Object[] convertParameters(Object[] parameters,
                                             Type[] types,
                                             AbstractConnection conn)
                                      throws DBusException

Recursively converts types for serialization onto DBus.

**Parameters:**  
`parameters` - The parameters to convert.

`types` - The (possibly generic) types of the parameters.

**Returns:**  
The converted parameters.

**Throws:**  
`DBusException` - Thrown if there is an error in converting the objects.
