## org.freedesktop.dbus Class DBusMatchRule

    java.lang.Object
      org.freedesktop.dbus.DBusMatchRule

    public class DBusMatchRuleextends Object

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
<td><strong><code>DBusMatchRule</code></strong><code>(</code><code>Class</code><code>&lt;? extends </code><code>DBusInterface</code><code>&gt; c, </code><code>String</code><code> method)</code><br />
           </td>
<td></td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td><strong><code>DBusMatchRule</code></strong><code>(</code><code>Class</code><code>&lt;? extends </code><code>Object</code><code>&gt; c)</code><br />
           </td>
<td></td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td><strong><code>DBusMatchRule</code></strong><code>(</code><code>Class</code><code>&lt;? extends </code><code>Object</code><code>&gt; c, </code><code>String</code><code> source, </code><code>String</code><code> object)</code><br />
           </td>
<td></td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td><strong><code>DBusMatchRule</code></strong><code>(</code><code>DBusExecutionException</code><code> e)</code><br />
           </td>
<td></td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td><strong><code>DBusMatchRule</code></strong><code>(</code><code>Message</code><code> m)</code><br />
           </td>
<td></td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td><strong><code>DBusMatchRule</code></strong><code>(</code><code>String</code><code> type, </code><code>String</code><code> iface, </code><code>String</code><code> member)</code><br />
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
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>getInterface</code></strong><code>()</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>getMember</code></strong><code>()</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>getObject</code></strong><code>()</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>getSource</code></strong><code>()</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>getType</code></strong><code>()</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>toString</code></strong><code>()</code><br />
           </td>
</tr>
</tbody>
</table>

 

| **Methods inherited from class java.lang.Object** |
|----|
| `clone``, ``equals``, ``finalize``, ``getClass``, ``hashCode``, ``notify``, ``notifyAll``, ``wait``, ``wait``, ``wait` |

 

| **Constructor Detail** |
|------------------------|

### DBusMatchRule

    public DBusMatchRule(String type,
                         String iface,
                         String member)

### DBusMatchRule

    public DBusMatchRule(DBusExecutionException e)
                  throws DBusException

**Throws:**  
`DBusException`

### DBusMatchRule

    public DBusMatchRule(Message m)

### DBusMatchRule

    public DBusMatchRule(Class<? extends DBusInterface> c,
                         String method)
                  throws DBusException

**Throws:**  
`DBusException`

### DBusMatchRule

    public DBusMatchRule(Class<? extends Object> c,
                         String source,
                         String object)
                  throws DBusException

**Throws:**  
`DBusException`

### DBusMatchRule

    public DBusMatchRule(Class<? extends Object> c)
                  throws DBusException

**Throws:**  
`DBusException`

| **Method Detail** |
|-------------------|

### toString

    public String toString()

**Overrides:**  
`toString` in class `Object`

### getType

    public String getType()

### getInterface

    public String getInterface()

### getMember

    public String getMember()

### getSource

    public String getSource()

### getObject

    public String getObject()
