## org.freedesktop Interface DBus.Properties

**All Superinterfaces:**  
DBusInterface

<!-- -->

**Enclosing interface:**  
DBus

<!-- -->

    public static interface DBus.Propertiesextends DBusInterface

A standard properties interface.

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
<td style="text-align: right;" data-valign="top" width="1%"><code> </code>
<table data-border="0" data-cellpadding="0" data-cellspacing="0" data-summary="">
<tbody>
<tr data-align="right" data-valign="">
<td data-nowrap=""><code>&lt;A&gt; A</code></td>
</tr>
</tbody>
</table></td>
<td><strong><code>Get</code></strong><code>(</code><code>String</code><code> interface_name, </code><code>String</code><code> property_name)</code><br />
          Get the value for the given property.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>Map</code><code>&lt;</code><code>String</code><code>,</code><code>Variant</code><code>&gt;</code></td>
<td><strong><code>GetAll</code></strong><code>(</code><code>String</code><code> interface_name)</code><br />
          Get all properties and values.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code>
<table data-border="0" data-cellpadding="0" data-cellspacing="0" data-summary="">
<tbody>
<tr data-align="right" data-valign="">
<td data-nowrap=""><code>&lt;A&gt; void</code></td>
</tr>
</tbody>
</table></td>
<td><strong><code>Set</code></strong><code>(</code><code>String</code><code> interface_name, </code><code>String</code><code> property_name, A value)</code><br />
          Set the value for the given property.</td>
</tr>
</tbody>
</table>

 

| **Methods inherited from interface org.freedesktop.dbus.DBusInterface** |
|-------------------------------------------------------------------------|
| `isRemote`                                                              |

 

| **Method Detail** |
|-------------------|

### Get

    <A> A Get(String interface_name,
              String property_name)

Get the value for the given property.

**Parameters:**  
`interface_name` - The interface this property is associated with.

`property_name` - The name of the property.

**Returns:**  
The value of the property (may be any valid DBus type).

### Set

    <A> void Set(String interface_name,
                 String property_name,
                 A value)

Set the value for the given property.

**Parameters:**  
`interface_name` - The interface this property is associated with.

`property_name` - The name of the property.

`value` - The new value of the property (may be any valid DBus type).

### GetAll

    Map<String,Variant> GetAll(String interface_name)

Get all properties and values.

**Parameters:**  
`interface_name` - The interface the properties is associated with.

**Returns:**  
The properties mapped to their values.
