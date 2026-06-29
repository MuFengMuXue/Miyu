## org.freedesktop.dbus.exceptions Class DBusExecutionException

    java.lang.Object
      java.lang.Throwable
          java.lang.Exception
              java.lang.RuntimeException
                  org.freedesktop.dbus.exceptions.DBusExecutionException

**All Implemented Interfaces:**  
Serializable

<!-- -->

**Direct Known Subclasses:**  
DBus.Error.AccessDenied, DBus.Error.MatchRuleInvalid, DBus.Error.NoReply, DBus.Error.ServiceUnknown, DBus.Error.UnknownMethod, DBus.Error.UnknownObject, InternalMessageException, NotConnected

<!-- -->

    public class DBusExecutionExceptionextends RuntimeException

An exception while running a remote method within DBus.

**See Also:**  
Serialized Form

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
<td><strong><code>DBusExecutionException</code></strong><code>(</code><code>String</code><code> message)</code><br />
          Create an exception with the specified message</td>
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
<td><strong><code>getType</code></strong><code>()</code><br />
          Get the DBus type of this exception.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>setType</code></strong><code>(</code><code>String</code><code> type)</code><br />
           </td>
</tr>
</tbody>
</table>

 

| **Methods inherited from class java.lang.Throwable** |
|----|
| `fillInStackTrace``, ``getCause``, ``getLocalizedMessage``, ``getMessage``, ``getStackTrace``, ``initCause``, ``printStackTrace``, ``printStackTrace``, ``printStackTrace``, ``setStackTrace``, ``toString` |

 

| **Methods inherited from class java.lang.Object** |
|----|
| `clone``, ``equals``, ``finalize``, ``getClass``, ``hashCode``, ``notify``, ``notifyAll``, ``wait``, ``wait``, ``wait` |

 

| **Constructor Detail** |
|------------------------|

### DBusExecutionException

    public DBusExecutionException(String message)

Create an exception with the specified message

| **Method Detail** |
|-------------------|

### setType

    public void setType(String type)

### getType

    public String getType()

Get the DBus type of this exception. Use if this was an exception we don't have a class file for.
