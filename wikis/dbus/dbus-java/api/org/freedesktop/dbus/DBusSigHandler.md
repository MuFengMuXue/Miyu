## org.freedesktop.dbus Interface DBusSigHandler\<T extends DBusSignal\>

**All Known Implementing Classes:**  
DBusConnection.PeerSet

<!-- -->

    public interface DBusSigHandler<T extends DBusSignal>

Handle a signal on DBus. All Signal handlers are run in their own Thread. Application writers are responsible for managing any concurrency issues.

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
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>handle</code></strong><code>(</code><code>T</code><code> s)</code><br />
          Handle a signal.</td>
</tr>
</tbody>
</table>

 

| **Method Detail** |
|-------------------|

### handle

    void handle(T s)

Handle a signal.

**Parameters:**  
`s` - The signal to handle. If such a class exists, the signal will be an instance of the class with the correct type signature. Otherwise it will be an instance of DBusSignal
