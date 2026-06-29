## org.freedesktop.dbus Interface CallbackHandler\<ReturnType\>

    public interface CallbackHandler<ReturnType>

Interface for callbacks in async mode

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
<td><strong><code>handle</code></strong><code>(</code><code>ReturnType</code><code> r)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>handleError</code></strong><code>(</code><code>DBusExecutionException</code><code> e)</code><br />
           </td>
</tr>
</tbody>
</table>

 

| **Method Detail** |
|-------------------|

### handle

    void handle(ReturnType r)

### handleError

    void handleError(DBusExecutionException e)
