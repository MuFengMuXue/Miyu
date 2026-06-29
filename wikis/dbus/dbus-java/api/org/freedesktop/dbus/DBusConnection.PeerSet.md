## org.freedesktop.dbus Class DBusConnection.PeerSet

    java.lang.Object
      org.freedesktop.dbus.DBusConnection.PeerSet

**All Implemented Interfaces:**  
Iterable\<String\>, Collection\<String\>, Set\<String\>, DBusSigHandler\<DBus.NameOwnerChanged\>

<!-- -->

**Enclosing class:**  
DBusConnection

<!-- -->

    public class DBusConnection.PeerSetextends Objectimplements Set<String>, DBusSigHandler<DBus.NameOwnerChanged>

Add addresses of peers to a set which will watch for them to disappear and automatically remove them from the set.

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
<td><strong><code>DBusConnection.PeerSet</code></strong><code>()</code><br />
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
<td style="text-align: right;" data-valign="top" width="1%"><code> boolean</code></td>
<td><strong><code>add</code></strong><code>(</code><code>String</code><code> address)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> boolean</code></td>
<td><strong><code>addAll</code></strong><code>(</code><code>Collection</code><code>&lt;? extends </code><code>String</code><code>&gt; addresses)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>clear</code></strong><code>()</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> boolean</code></td>
<td><strong><code>contains</code></strong><code>(</code><code>Object</code><code> o)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> boolean</code></td>
<td><strong><code>containsAll</code></strong><code>(</code><code>Collection</code><code>&lt;?&gt; os)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> boolean</code></td>
<td><strong><code>equals</code></strong><code>(</code><code>Object</code><code> o)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>handle</code></strong><code>(</code><code>DBus.NameOwnerChanged</code><code> noc)</code><br />
          Handle a signal.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> int</code></td>
<td><strong><code>hashCode</code></strong><code>()</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> boolean</code></td>
<td><strong><code>isEmpty</code></strong><code>()</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>Iterator</code><code>&lt;</code><code>String</code><code>&gt;</code></td>
<td><strong><code>iterator</code></strong><code>()</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> boolean</code></td>
<td><strong><code>remove</code></strong><code>(</code><code>Object</code><code> o)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> boolean</code></td>
<td><strong><code>removeAll</code></strong><code>(</code><code>Collection</code><code>&lt;?&gt; os)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> boolean</code></td>
<td><strong><code>retainAll</code></strong><code>(</code><code>Collection</code><code>&lt;?&gt; os)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> int</code></td>
<td><strong><code>size</code></strong><code>()</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>Object</code><code>[]</code></td>
<td><strong><code>toArray</code></strong><code>()</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code>
<table data-border="0" data-cellpadding="0" data-cellspacing="0" data-summary="">
<tbody>
<tr data-align="right" data-valign="">
<td data-nowrap=""><code>&lt;T&gt; T[]</code></td>
</tr>
</tbody>
</table></td>
<td><strong><code>toArray</code></strong><code>(T[] a)</code><br />
           </td>
</tr>
</tbody>
</table>

 

| **Methods inherited from class java.lang.Object** |
|----|
| `clone``, ``finalize``, ``getClass``, ``notify``, ``notifyAll``, ``toString``, ``wait``, ``wait``, ``wait` |

 

| **Constructor Detail** |
|------------------------|

### DBusConnection.PeerSet

    public DBusConnection.PeerSet()

| **Method Detail** |
|-------------------|

### handle

    public void handle(DBus.NameOwnerChanged noc)

**Description copied from interface: `DBusSigHandler`**

Handle a signal.

**Specified by:**  
`handle` in interface `DBusSigHandler``<``DBus.NameOwnerChanged``>`

<!-- -->

**Parameters:**  
`noc` - The signal to handle. If such a class exists, the signal will be an instance of the class with the correct type signature. Otherwise it will be an instance of DBusSignal

### add

    public boolean add(String address)

**Specified by:**  
`add` in interface `Collection``<``String``>`

**Specified by:**  
`add` in interface `Set``<``String``>`

### addAll

    public boolean addAll(Collection<? extends String> addresses)

**Specified by:**  
`addAll` in interface `Collection``<``String``>`

**Specified by:**  
`addAll` in interface `Set``<``String``>`

### clear

    public void clear()

**Specified by:**  
`clear` in interface `Collection``<``String``>`

**Specified by:**  
`clear` in interface `Set``<``String``>`

### contains

    public boolean contains(Object o)

**Specified by:**  
`contains` in interface `Collection``<``String``>`

**Specified by:**  
`contains` in interface `Set``<``String``>`

### containsAll

    public boolean containsAll(Collection<?> os)

**Specified by:**  
`containsAll` in interface `Collection``<``String``>`

**Specified by:**  
`containsAll` in interface `Set``<``String``>`

### equals

    public boolean equals(Object o)

**Specified by:**  
`equals` in interface `Collection``<``String``>`

**Specified by:**  
`equals` in interface `Set``<``String``>`

**Overrides:**  
`equals` in class `Object`

### hashCode

    public int hashCode()

**Specified by:**  
`hashCode` in interface `Collection``<``String``>`

**Specified by:**  
`hashCode` in interface `Set``<``String``>`

**Overrides:**  
`hashCode` in class `Object`

### isEmpty

    public boolean isEmpty()

**Specified by:**  
`isEmpty` in interface `Collection``<``String``>`

**Specified by:**  
`isEmpty` in interface `Set``<``String``>`

### iterator

    public Iterator<String> iterator()

**Specified by:**  
`iterator` in interface `Iterable``<``String``>`

**Specified by:**  
`iterator` in interface `Collection``<``String``>`

**Specified by:**  
`iterator` in interface `Set``<``String``>`

### remove

    public boolean remove(Object o)

**Specified by:**  
`remove` in interface `Collection``<``String``>`

**Specified by:**  
`remove` in interface `Set``<``String``>`

### removeAll

    public boolean removeAll(Collection<?> os)

**Specified by:**  
`removeAll` in interface `Collection``<``String``>`

**Specified by:**  
`removeAll` in interface `Set``<``String``>`

### retainAll

    public boolean retainAll(Collection<?> os)

**Specified by:**  
`retainAll` in interface `Collection``<``String``>`

**Specified by:**  
`retainAll` in interface `Set``<``String``>`

### size

    public int size()

**Specified by:**  
`size` in interface `Collection``<``String``>`

**Specified by:**  
`size` in interface `Set``<``String``>`

### toArray

    public Object[] toArray()

**Specified by:**  
`toArray` in interface `Collection``<``String``>`

**Specified by:**  
`toArray` in interface `Set``<``String``>`

### toArray

    public <T> T[] toArray(T[] a)

**Specified by:**  
`toArray` in interface `Collection``<``String``>`

**Specified by:**  
`toArray` in interface `Set``<``String``>`
