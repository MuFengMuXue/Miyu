\[prev\] \[prev-tail\] \[tail\] \[up\]

### 6  DBusSigHandler

To handle incoming signals from other programs on the Bus you must register a signal handler. This must implement DBusSigHandler<sup>13</sup> and provide an implementation for the handle method. An example Signal Handler is in figure 9. Signal handlers should be parameterised with the signal they are handling. If you want a signal handler to handle multiple signals you can leave out the parameterisation and use instanceof to check the type of signal you are handling. Signal handlers will be run in their own thread.

<table class="figure">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="figure">
<td class="figure">import org.freedesktop.dbus.DBusSignal;  <br />
import org.freedesktop.dbus.DBusSigHandler;  <br />
 <br />
public class Handler extends DBusSigHandler&lt;DBus.NameAcquired&gt;  <br />
{  <br />
   public void handle(DBus.NameAcquired sig)  <br />
   {  <br />
         ...  <br />
   }  <br />
}
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Figure 9:</td>
<td class="content">A Signal Handler</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

\[prev\] \[prev-tail\] \[front\] \[up\]
