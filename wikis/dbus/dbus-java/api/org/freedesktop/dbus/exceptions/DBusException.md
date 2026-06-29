## org.freedesktop.dbus.exceptions Class DBusException

    java.lang.Object
      java.lang.Throwable
          java.lang.Exception
              org.freedesktop.dbus.exceptions.DBusException

**All Implemented Interfaces:**  
Serializable

<!-- -->

**Direct Known Subclasses:**  
FatalDBusException, MarshallingException, MessageFormatException, UnknownTypeCodeException

<!-- -->

    public class DBusExceptionextends Exception

An exception within DBus.

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
<td><strong><code>DBusException</code></strong><code>(</code><code>String</code><code> message)</code><br />
          Create an exception with the specified message</td>
<td></td>
</tr>
</tbody>
</table>

 

| **Method Summary** |     |
|--------------------|-----|

 

| **Methods inherited from class java.lang.Throwable** |
|----|
| `fillInStackTrace``, ``getCause``, ``getLocalizedMessage``, ``getMessage``, ``getStackTrace``, ``initCause``, ``printStackTrace``, ``printStackTrace``, ``printStackTrace``, ``setStackTrace``, ``toString` |

 

| **Methods inherited from class java.lang.Object** |
|----|
| `clone``, ``equals``, ``finalize``, ``getClass``, ``hashCode``, ``notify``, ``notifyAll``, ``wait``, ``wait``, ``wait` |

 

| **Constructor Detail** |
|------------------------|

### DBusException

    public DBusException(String message)

Create an exception with the specified message
