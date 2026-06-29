## org.freedesktop.dbus Interface DBusInterface

**All Known Subinterfaces:**  
DBus, DBus.Binding.SingleTests, DBus.Binding.TestClient, DBus.Binding.Tests, DBus.Binding.TestSignals, DBus.Introspectable, DBus.Local, DBus.Peer, DBus.Properties

<!-- -->

    public interface DBusInterface

Denotes a class as exportable or a remote interface which can be called.

Any interface which should be exported or imported should extend this interface. All public methods from that interface are exported/imported with the given method signatures.

All method calls on exported objects are run in their own threads. Application writers are responsible for any concurrency issues.

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
<td><strong><code>isRemote</code></strong><code>()</code><br />
          Returns true on remote objects.</td>
</tr>
</tbody>
</table>

 

| **Method Detail** |
|-------------------|

### isRemote

    boolean isRemote()

Returns true on remote objects. Local objects implementing this interface MUST return false.
