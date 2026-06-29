\[prev\] \[prev-tail\] \[tail\] \[up\]

### 14  Examples

As an example here are a complete set of interfaces for the bluemon<sup>24</sup> daemon, which communicates over D-Bus. These interfaces were all created by querying introspection data over the bus.

<table class="figure">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="figure">
<td class="figure">package cx.ath.matthew.bluemon;  <br />
import org.freedesktop.dbus.DBusInterface;  <br />
import org.freedesktop.dbus.UInt32;  <br />
public interface Bluemon extends DBusInterface  <br />
{  <br />
  public Triplet&lt;String, Boolean, UInt32&gt;  <br />
  Status(String address);  <br />
}
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Figure 21:</td>
<td class="content">cx/ath/matthew/bluemon/Bluemon.java</td>
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
<td class="figure">package cx.ath.matthew.bluemon;  <br />
import org.freedesktop.dbus.DBusInterface;  <br />
import org.freedesktop.dbus.DBusSignal;  <br />
import org.freedesktop.dbus.exceptions.DBusException;  <br />
public interface ProximitySignal extends DBusInterface  <br />
{  <br />
   public static class Connect extends DBusSignal  <br />
   {  <br />
      public final String address;  <br />
      public Connect(String path, String address)  <br />
                                 throws DBusException  <br />
      {  <br />
         super(path, address);  <br />
         this.address = address;  <br />
      }  <br />
   }  <br />
   public static class Disconnect extends DBusSignal  <br />
   {  <br />
      public final String address;  <br />
      public Disconnect(String path, String address)  <br />
                                 throws DBusException  <br />
      {  <br />
         super(path, address);  <br />
         this.address = address;  <br />
      }  <br />
   }  <br />
}
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Figure 22:</td>
<td class="content">cx/ath/matthew/bluemon/ProximitySignal.java</td>
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
<td class="figure">package cx.ath.matthew.bluemon;  <br />
import org.freedesktop.dbus.Tuple;  <br />
/** Just a typed container class */  <br />
public final class Triplet &lt;A,B,C&gt; extends Tuple  <br />
{  <br />
   public final A a;  <br />
   public final B b;  <br />
   public final C c;  <br />
   public Triplet(A a, B b, C c)  <br />
   {  <br />
      super(a, b, c);  <br />
      this.a = a;  <br />
      this.b = b;  <br />
      this.c = c;  <br />
   }  <br />
}
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Figure 23:</td>
<td class="content">cx/ath/matthew/bluemon/Triplet.java</td>
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
<td class="figure">package cx.ath.matthew.bluemon;  <br />
import org.freedesktop.dbus.DBusConnection;  <br />
import org.freedesktop.dbus.DBusSigHandler;  <br />
import org.freedesktop.dbus.DBusSignal;  <br />
import org.freedesktop.dbus.UInt32;  <br />
import org.freedesktop.dbus.exceptions.DBusException;  <br />
 <br />
public class Query {  <br />
   public static void main(String[] args) {  <br />
      String btid;  <br />
      Triplet&lt;String, Boolean, UInt32&gt; rv = null;  <br />
 <br />
      if (0 == args.length) btid = "";  <br />
      else btid = args[0];  <br />
 <br />
      DBusConnection conn = null;  <br />
      try {  <br />
         conn = DBusConnection.getConnection(DBusConnection.SYSTEM);  <br />
      } catch (DBusException De) {  <br />
         System.exit(1);  <br />
      }  <br />
      Bluemon b = (Bluemon) conn.getRemoteObject(  <br />
            "cx.ath.matthew.bluemon.server",  <br />
            "/cx/ath/matthew/bluemon/Bluemon", Bluemon.class);  <br />
      try {  <br />
         rv = b.Status(btid);  <br />
      } catch (RuntimeException Re) {  <br />
         System.exit(1);  <br />
      }  <br />
      String address = rv.a;  <br />
      boolean status = rv.b;  <br />
      int level = rv.c.intValue();  <br />
 <br />
      if (status)  <br />
         System.out.println("Device "+address+  <br />
                            " connected with level "+level);  <br />
      else  <br />
         System.out.println("Device "+address+" not connected");  <br />
      conn.disconnect();  <br />
   }  <br />
}
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Figure 24:</td>
<td class="content">cx/ath/matthew/bluemon/Query.java</td>
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
<td class="figure">/* cx/ath/matthew/bluemon/Client.java */  <br />
package cx.ath.matthew.bluemon;  <br />
 <br />
import org.freedesktop.dbus.DBusConnection;  <br />
import org.freedesktop.dbus.DBusSigHandler;  <br />
import org.freedesktop.dbus.DBusSignal;  <br />
import org.freedesktop.dbus.exceptions.DBusException;  <br />
 <br />
public class Client implements DBusSigHandler  <br />
{  <br />
   public void handle(DBusSignal s)  <br />
   {  <br />
      if (s instanceof ProximitySignal.Connect)  <br />
         System.out.println("Got a connect for "  <br />
               +((ProximitySignal.Connect) s).address);  <br />
      else if (s instanceof ProximitySignal.Disconnect)  <br />
         System.out.println("Got a disconnect for "  <br />
               +((ProximitySignal.Disconnect) s).address);  <br />
   }  <br />
   public static void main(String[] args)  <br />
   {  <br />
      System.out.println("Creating Connection");  <br />
      DBusConnection conn = null;  <br />
      try {  <br />
         conn = DBusConnection  <br />
                  .getConnection(DBusConnection.SYSTEM);  <br />
      } catch (DBusException DBe) {  <br />
         System.out.println("Could not connect to bus");  <br />
         System.exit(1);  <br />
      }  <br />
 <br />
      try {  <br />
         conn.addSigHandler(ProximitySignal.Connect.class,  <br />
         new Client());  <br />
         conn.addSigHandler(ProximitySignal.Disconnect.class,  <br />
         new Client());  <br />
      } catch (DBusException DBe) {  <br />
         conn.disconnect();  <br />
         System.exit(1);  <br />
      }  <br />
   }  <br />
}
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Figure 25:</td>
<td class="content">cx/ath/matthew/bluemon/Client.java</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

\[prev\] \[prev-tail\] \[front\] \[up\]
