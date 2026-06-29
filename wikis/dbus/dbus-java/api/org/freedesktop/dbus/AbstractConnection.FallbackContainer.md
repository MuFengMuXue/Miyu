## org.freedesktop.dbus Class AbstractConnection.FallbackContainer

    java.lang.Object
      org.freedesktop.dbus.AbstractConnection.FallbackContainer

**Enclosing class:**  
AbstractConnection

<!-- -->

    protected class AbstractConnection.FallbackContainerextends Object

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
<td style="text-align: right;" data-valign="top" width="1%"><code>protected </code></td>
<td><strong><code>AbstractConnection.FallbackContainer</code></strong><code>()</code><br />
           </td>
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
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>add</code></strong><code>(</code><code>String</code><code> path, org.freedesktop.dbus.ExportedObject eo)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> org.freedesktop.dbus.ExportedObject</code></td>
<td><strong><code>get</code></strong><code>(</code><code>String</code><code> path)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>remove</code></strong><code>(</code><code>String</code><code> path)</code><br />
           </td>
</tr>
</tbody>
</table>

 

| **Methods inherited from class java.lang.Object** |
|----|
| `clone``, ``equals``, ``finalize``, ``getClass``, ``hashCode``, ``notify``, ``notifyAll``, ``toString``, ``wait``, ``wait``, ``wait` |

 

| **Constructor Detail** |
|------------------------|

### AbstractConnection.FallbackContainer

    protected AbstractConnection.FallbackContainer()

| **Method Detail** |
|-------------------|

### add

    public void add(String path,
                    org.freedesktop.dbus.ExportedObject eo)

### remove

    public void remove(String path)

### get

    public org.freedesktop.dbus.ExportedObject get(String path)
