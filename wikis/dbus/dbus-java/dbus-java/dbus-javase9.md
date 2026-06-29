\[prev\] \[prev-tail\] \[tail\] \[up\]

### 9  DBusSerializable

Some people may want to be able to pass their own objects over D-Bus. Obviously only raw D-Bus types can be sent on the message bus itself, but the Java implementation allows the creation of serializable objects which can be passed to D-Bus functions and will be converted to/from D-Bus types by the library.

To create such a class you must implement the DBusSerializable<sup>18</sup> class and provide two methods and a zero-argument constructor. The first method has the signature public Object

serialize() throws DBusException and the second must be called deserialize, return null and take as it’s arguments exactly all the dbus types that are being serialized to in order and with parameterization. The serialize method should return the class properties you wish to serialize, correctly formatted for the wire (DBusConnection.convertParameters() can help with this), in order in an Object array.

An example of a serializable class can be seen in figure 16.

<table class="figure">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="figure">
<td class="figure">import java.lang.reflect.Type;  <br />
 <br />
import java.util.List;  <br />
import java.util.Vector;  <br />
 <br />
import org.freedesktop.dbus.DBusConnection;  <br />
import org.freedesktop.dbus.DBusSerializable;  <br />
 <br />
public class TestSerializable implements DBusSerializable  <br />
{  <br />
   private int a;  <br />
   private String b;  <br />
   private Vector&lt;Integer&gt; c;  <br />
   public TestSerializable(int a, String b, Vector&lt;Integer&gt; c)  <br />
   {  <br />
      this.a = a;  <br />
      this.b = b.toString();  <br />
      this.c = c;  <br />
   }  <br />
   public TestSerializable() {}  <br />
   public void deserialize(int a, String b, List&lt;Integer&gt; c)  <br />
   {  <br />
      this.a = a;  <br />
      this.b = b;  <br />
      this.c = new Vector&lt;Integer&gt;(c);  <br />
   }  <br />
   public Object[] serialize()  <br />
   {  <br />
      return new Object[] { a, b, c };  <br />
   }  <br />
   public int getInt() { return a; }  <br />
   public String getString() { return b; }  <br />
   public Vector&lt;Integer&gt; getVector() { return c; }  <br />
   public String toString()  <br />
   {  <br />
      return "TestSerializable{"+a+","+b+","+c+"}";  <br />
   }  <br />
}
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Figure 16:</td>
<td class="content">A serializable class</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

\[prev\] \[prev-tail\] \[front\] \[up\]
