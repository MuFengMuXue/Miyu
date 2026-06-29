\[prev\] \[prev-tail\] \[tail\] \[up\]

### 5  DBusExecutionException

If you wish to report an error condition in a method call you can throw an instance of DBusExecutionException<sup>12</sup> . This will be sent back to the caller as an error message, and the error name is taken from the class name of the exception. For example, if you wanted to report an unknown method you would define an exception as in figure 6 and then throw it in your method as in figure 7.

<table class="figure">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="figure">
<td class="figure">package org.freedesktop.DBus.Error;  <br />
import org.freedesktop.dbus.exceptions.DBusExecutionException;  <br />
 <br />
public class UnknownMethod extends DBusExecutionException  <br />
{  <br />
   public UnknownMethod(String message)  <br />
   {  <br />
      super(message);  <br />
   }  <br />
}
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Figure 6:</td>
<td class="content">An Exception</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

<table class="figure">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="figure">
<td class="figure">...  <br />
public void throwme() throws org.freedesktop.DBus.Error.UnknownMethod  <br />
{  <br />
   throw new org.freedesktop.DBus.Error.UnknownMethod("hi");  <br />
}  <br />
...
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Figure 7:</td>
<td class="content">Throwing An Exception</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

If you are calling a remote method and you want to handle such an error you can simply catch the exception as in figure 8.

<table class="figure">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="figure">
<td class="figure">...  <br />
try {  <br />
   remote.throwme();  <br />
} catch (org.freedesktop.DBus.Error.UnknownMethod UM) {  <br />
   ...  <br />
}  <br />
...
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Figure 8:</td>
<td class="content">Catching An Exception</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

\[prev\] \[prev-tail\] \[front\] \[up\]
