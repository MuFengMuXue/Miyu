## org.freedesktop.dbus Class StrongReference\<T\>

    java.lang.Object
      java.lang.ref.Reference<T>
          java.lang.ref.WeakReference<T>
              org.freedesktop.dbus.StrongReference<T>

    public class StrongReference<T>extends WeakReference<T>

An alternative to a WeakReference when you don't want that behaviour.

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
<td><strong><code>StrongReference</code></strong><code>(</code><code>T</code><code> referant)</code><br />
           </td>
<td></td>
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
<td><strong><code>clear</code></strong><code>()</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> boolean</code></td>
<td><strong><code>enqueue</code></strong><code>()</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>T</code></td>
<td><strong><code>get</code></strong><code>()</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> boolean</code></td>
<td><strong><code>isEnqueued</code></strong><code>()</code><br />
           </td>
</tr>
</tbody>
</table>

 

| **Methods inherited from class java.lang.Object** |
|----|
| `clone``, ``equals``, ``finalize``, ``getClass``, ``hashCode``, ``notify``, ``notifyAll``, ``toString``, ``wait``, ``wait``, ``wait` |

 

| **Constructor Detail** |
|------------------------|

### StrongReference

    public StrongReference(T referant)

| **Method Detail** |
|-------------------|

### clear

    public void clear()

**Overrides:**  
`clear` in class `Reference``<``T``>`

### enqueue

    public boolean enqueue()

**Overrides:**  
`enqueue` in class `Reference``<``T``>`

### get

    public T get()

**Overrides:**  
`get` in class `Reference``<``T``>`

### isEnqueued

    public boolean isEnqueued()

**Overrides:**  
`isEnqueued` in class `Reference``<``T``>`
