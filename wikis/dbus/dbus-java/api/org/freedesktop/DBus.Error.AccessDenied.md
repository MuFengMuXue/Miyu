## org.freedesktop Class DBus.Error.AccessDenied

    java.lang.Object
      java.lang.Throwable
          java.lang.Exception
              java.lang.RuntimeException
                  org.freedesktop.dbus.exceptions.DBusExecutionException
                      org.freedesktop.DBus.Error.AccessDenied

**All Implemented Interfaces:**  
Serializable

<!-- -->

**Enclosing interface:**  
DBus.Error

<!-- -->

    public static class DBus.Error.AccessDeniedextends DBusExecutionException

Thrown if a message is denied due to a security policy

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
<td><strong><code>DBus.Error.AccessDenied</code></strong><code>(</code><code>String</code><code> message)</code><br />
           </td>
<td></td>
</tr>
</tbody>
</table>

 

| **Method Summary** |     |
|--------------------|-----|

 

| **Methods inherited from class org.freedesktop.dbus.exceptions.DBusExecutionException** |
|----|
| `getType``, ``setType` |

 

| **Methods inherited from class java.lang.Throwable** |
|----|
| `fillInStackTrace``, ``getCause``, ``getLocalizedMessage``, ``getMessage``, ``getStackTrace``, ``initCause``, ``printStackTrace``, ``printStackTrace``, ``printStackTrace``, ``setStackTrace``, ``toString` |

 

| **Methods inherited from class java.lang.Object** |
|----|
| `clone``, ``equals``, ``finalize``, ``getClass``, ``hashCode``, ``notify``, ``notifyAll``, ``wait``, ``wait``, ``wait` |

 

| **Constructor Detail** |
|------------------------|

### DBus.Error.AccessDenied

    public DBus.Error.AccessDenied(String message)
