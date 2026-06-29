\[prev\] \[prev-tail\] \[tail\] \[up\]

### 4  DBusSignal

Signals are also declared as part of an interface. The Java API models these as inner classes within an interface. The containing interface must extend DBusInterface, and the inner classes representing the signals must extend DBusSignal<sup>10</sup> . The Signal name is derived from the name of this inner class, and the interface from its containing interface.

Signals can take parameters as methods can (although they cannot return anything). For the reflection to work, a Signal declare a single constructor of the correct type. The constructor must take the object path they are being emitted from as their first (String) argument, followed by the other parameters in order. They must also call the superclass constructor with the same parameters. A full definition of a signal can be seen in figure 5. Again, more complicated definitions are available in the test classes<sup>11</sup> .

<table class="figure">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="figure">
<td class="figure">package org.freedesktop;  <br />
import org.freedesktop.dbus.DBusInterface;  <br />
import org.freedesktop.dbus.DBusSignal;  <br />
import org.freedesktop.dbus.exceptions.DBusException;  <br />
 <br />
public interface DBus extends DBusInterface  <br />
{  <br />
   public class NameAcquired extends DBusSignal  <br />
   {  <br />
      public final String name;  <br />
      public NameAcquired(String path, String name)  <br />
                              throws DBusException  <br />
      {  <br />
         super(path, name);  <br />
         this.name = name;  <br />
      }  <br />
   }  <br />
}
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Figure 5:</td>
<td class="content">A Signal with one parameter</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

\[prev\] \[prev-tail\] \[front\] \[up\]
