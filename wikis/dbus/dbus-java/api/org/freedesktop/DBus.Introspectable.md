## org.freedesktop Interface DBus.Introspectable

**All Superinterfaces:**  
DBusInterface

<!-- -->

**Enclosing interface:**  
DBus

<!-- -->

    public static interface DBus.Introspectableextends DBusInterface

Objects can provide introspection data via this interface and method. See the Introspection Format.

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
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>Introspect</code></strong><code>()</code><br />
           </td>
</tr>
</tbody>
</table>

 

| **Methods inherited from interface org.freedesktop.dbus.DBusInterface** |
|-------------------------------------------------------------------------|
| `isRemote`                                                              |

 

| **Method Detail** |
|-------------------|

### Introspect

    String Introspect()

**Returns:**  
The XML introspection data for this object
