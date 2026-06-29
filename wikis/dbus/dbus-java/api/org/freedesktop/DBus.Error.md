## org.freedesktop Interface DBus.Error

**Enclosing interface:**  
DBus

<!-- -->

    public static interface DBus.Error

Contains standard errors that can be thrown from methods.

<table data-border="1" width="100%" data-cellpadding="3" data-cellspacing="0" data-summary="">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="TableHeadingColor" data-bgcolor="#CCCCFF">
<th colspan="2" style="text-align: left;"><strong>Nested Class Summary</strong></th>
</tr>
</thead>
<tbody>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static class</code></td>
<td><strong><code>DBus.Error.AccessDenied</code></strong><br />
          Thrown if a message is denied due to a security policy</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static class</code></td>
<td><strong><code>DBus.Error.MatchRuleInvalid</code></strong><br />
          Thrown if the match rule is invalid</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static class</code></td>
<td><strong><code>DBus.Error.NoReply</code></strong><br />
          Thrown if there is no reply to a method call</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static class</code></td>
<td><strong><code>DBus.Error.ServiceUnknown</code></strong><br />
          Thrown if the requested service was not available</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static class</code></td>
<td><strong><code>DBus.Error.UnknownMethod</code></strong><br />
          Thrown if the method called was unknown on the remote object</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static class</code></td>
<td><strong><code>DBus.Error.UnknownObject</code></strong><br />
          Thrown if the object was unknown on a remote connection</td>
</tr>
</tbody>
</table>

 
