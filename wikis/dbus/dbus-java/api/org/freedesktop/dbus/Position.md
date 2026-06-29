## org.freedesktop.dbus Annotation Type Position

    @Retention(value=RUNTIME)
    @Target(value=FIELD)
    public @interface Position

Position annotation, to annotate Struct fields to be sent over DBus.

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
<td style="text-align: right;" data-valign="top" width="1%"><code> int</code></td>
<td><strong><code>value</code></strong><br />
          The order of this field in the Struct.</td>
</tr>
</tbody>
</table>

 

| **Element Detail** |
|--------------------|

### value

    public abstract int value

The order of this field in the Struct.
