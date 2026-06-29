## org.freedesktop.dbus Interface DBusSerializable

    public interface DBusSerializable

Custom classes may be sent over DBus if they implement this interface.

In addition to the serialize method, classes **MUST** implement a deserialize method which returns null and takes as it's arguments all the DBus types the class will be serialied to *in order* and *with type parameterisation*. They **MUST** also provide a zero-argument constructor.

The serialize method should return the class properties you wish to serialize, correctly formatted for the wire (DBusConnection.convertParameters() can help with this), in order in an Object array.

The deserialize method will be called once after the zero-argument constructor. This should contain all the code to initialise the object from the types.

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
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>Object</code><code>[]</code></td>
<td><strong><code>serialize</code></strong><code>()</code><br />
           </td>
</tr>
</tbody>
</table>

 

| **Method Detail** |
|-------------------|

### serialize

    Object[] serialize()
                       throws DBusException

**Throws:**  
`DBusException`
