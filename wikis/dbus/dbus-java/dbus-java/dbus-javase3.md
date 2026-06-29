\[next\] \[prev\] \[prev-tail\] \[tail\] \[up\]

### 3  DBusInterface

To call methods or expose methods on D-Bus you need to define them with their exact signature in a Java interface. The full name of this interface must be the same as the D-Bus interface they represent. In addition, D-Bus interface names must contain at least one period. This means that DBusInterfaces cannot be declared without being in a package.

For example, if I want to expose methods on the interface “org.freedesktop.DBus” I would define a Java interface in the package org.freedesktop called DBus. This would be in the file org/freedesktop/DBus.java as normal. Any object wanting to export these methods would implement org.freedesktop.DBus.

Any interfaces which can be exported over D-Bus must extend DBusInterface<sup>7</sup> . A class may implement more than one exportable interface, all public methods declared in an interface which extend DBusInterface will be exported.

A sample interface definition is given in figure 2, and a class which implements it in figure 3. More complicated definitions can be seen in the test classes<sup>8</sup> .

All method calls by other programs on objects you export over D-Bus are executed in their own thread.

DBusInterface itself specifies one method boolean isRemote(). If this is executed on a remote object it will always return true. Local objects implementing a remote interface must implement this method to return false.

<table class="figure">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="figure">
<td class="figure">package org.freedesktop;  <br />
import org.freedesktop.dbus.UInt32;  <br />
import org.freedesktop.dbus.DBusInterface;  <br />
 <br />
public interface DBus extends DBusInterface  <br />
{  <br />
   public boolean NameHasOwner(String name);  <br />
   public UInt32 RequestName(String name, UInt32 flags);  <br />
}
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Figure 2:</td>
<td class="content">An interface which exposes two methods</td>
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
<td class="figure">package my.real.implementation;  <br />
import org.freedesktop.dbus.DBus;  <br />
import org.freedesktop.dbus.UInt32;  <br />
 <br />
public class DBusImpl implements DBus  <br />
{  <br />
   Vector&lt;String&gt; names;  <br />
   public boolean NameHasOwner(String name)  <br />
   {  <br />
      if (names.contains(name)) return true;  <br />
      else return false;  <br />
   }  <br />
   public UInt32 RequestName(String name, UInt32 flags)  <br />
   {  <br />
      names.add(name);  <br />
      return new UInt32(0);  <br />
   }  <br />
   public boolean isRemote() { return false; }  <br />
}
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Figure 3:</td>
<td class="content">A class providing a real implementation which can be exported</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

#### 3.1  Interface name overriding

It is highly recommended that the Java interface and package name match the D-Bus interface. However, if, for some reason, this is not possible then the name can be overridden by use of an Annotation.

To override the Java interface name you should add an annotation to the interface of DBusInterfaceName<sup>9</sup> with a value of the desired D-Bus interface name. An example of this can be seen in figure 4.

<table class="figure">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="figure">
<td class="figure">package my.package;  <br />
import org.freedesktop.dbus.DBusInterface;  <br />
import org.freedesktop.dbus.DBusInterfaceName;  <br />
 <br />
@DBusInterfaceName("my.otherpackage.Remote")  <br />
public interface Remote extends DBusInterface  <br />
{  <br />
   ...  <br />
}
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Figure 4:</td>
<td class="content">Overloading the name of an interface.</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

If you have signals which are declared in a renamed interface (see below for signals) then when adding a signal handler you must use an addSigHandler method which takes a class object corresponding to that signal. If you do not then receiving the signal will fail.

\[next\] \[prev\] \[prev-tail\] \[front\] \[up\]
