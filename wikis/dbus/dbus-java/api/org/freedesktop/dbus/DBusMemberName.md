## org.freedesktop.dbus Annotation Type DBusMemberName

    @Retention(value=RUNTIME)
    @Target(value={TYPE,METHOD})
    public @interface DBusMemberName

Force the member (method/signal) name on the bus to be different to the Java name.

<table data-border="1" width="100%" data-cellpadding="3" data-cellspacing="0" data-summary="">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="TableHeadingColor" data-bgcolor="#CCCCFF">
<th colspan="2" style="text-align: left;"><strong>Required Element Summary</strong></th>
</tr>
</thead>
<tbody>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>value</code></strong><br />
          The replacement member name.</td>
</tr>
</tbody>
</table>

 

| **Element Detail** |
|--------------------|

### value

    public abstract String value

The replacement member name.
