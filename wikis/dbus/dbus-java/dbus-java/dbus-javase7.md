\[prev\] \[prev-tail\] \[tail\] \[up\]

### 7  D-Bus Types

D-Bus supports a number of types in its messages, some which Java supports natively, and some which it doesn’t. This library provides a way of modelling the extra D-Bus Types in Java. The full list of types and what D-Bus type they map to is in table 1.

#### 7.1  Basic Types

All of Java’s basic types are supported as parameters and return types to methods, and as parameters to signals. These can be used in either their primitive or wrapper types.

##### 7.1.1  Unsigned Types

D-Bus, like C and similar languages, has a notion of unsigned numeric types. The library supplies UInt16<sup>14</sup> , UInt32 and UInt64 classes to represent these new basic types.

#### 7.2  Strings

D-Bus also supports sending Strings. When mentioned below, Strings count as a basic type.

##### 7.2.1  String Comparisons

There may be some problems with comparing strings received over D-Bus with strings generated locally when using the String.equals method. This is due to how the Strings are generated from a UTF8 encoding. The recommended way to compare strings which have been sent over D-Bus is with the java.text.Collator class. Figure 10 demonstrates its use.

<table class="figure">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="figure">
<td class="figure">String rname = remote.getName();  <br />
Collator col = Collator.getInstance();  <br />
col.setDecomposition(Collator.FULL_DECOMPOSITION);  <br />
col.setStrength(Collator.PRIMARY);  <br />
if (0 != col.compare("Name", rname))  <br />
   fail("getName return value incorrect");
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Figure 10:</td>
<td class="content">Comparing strings with java.text.Collator.</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

#### 7.3  Arrays

You can send arrays of any valid D-Bus Type over D-Bus. These can either be declared in Java as arrays (e.g. Integer\[\] or int\[\]) or as Lists (e.g. List\<String\>). All lists must be parameterised with their type in the source (reflection on this is used by the library to determine their type). Also note that arrays cannot be used as part of more complex type, only Lists (for example List\<List\<String\>\>).

#### 7.4  Maps

D-Bus supports a dictionary type analogous to the Java Map type. This has the additional restriction that only basic types can be used as the key (including String). Any valid D-Bus type can be the value. As with lists, maps must be fully parameterised. (e.g. Map\<Integer, String\>).

#### 7.5  Variants

D-Bus has support for a Variant type. This is similar to declaring that a method takes a parameter of type Object, in that a Variant may contain any other type. Variants can either be declared using the Variant<sup>15</sup> class, or as a Type Variable. In the latter case the value is automatically unwrapped and passed to the function. Variants in compound types (Arrays, Maps, etc) must be declared using the Variant class with the full type passed to the Variant constructor and manually unwrapped.

Both these methods use variants:

public void display(Variant v);    
public \<T\> int hash(T v);

#### 7.6  Structs

D-Bus has a struct type, which is a collection of other types. Java does not have an analogue of this other than fields in classes, and due to the limitation of Java reflection this is not sufficient. The library declares a Struct<sup>16</sup> class which can be used to create structs. To define a struct you extend the Struct class and define fields for each member of the struct. These fields then need to be annotated in the order which they appear in the struct (class fields do not have a defined order). You must also define a single constructor which takes the contents of he struct in order. This is best demonstrated by an example. Figure 11 shows a Struct definition, and figure 12 shows this being used as a parameter to a method.

<table class="figure">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="figure">
<td class="figure">package org.freedesktop.dbus.test;  <br />
 <br />
import org.freedesktop.dbus.DBusException;  <br />
import org.freedesktop.dbus.Position;  <br />
import org.freedesktop.dbus.Struct;  <br />
 <br />
public final class TestStruct extends Struct  <br />
{  <br />
   @Position(0)  <br />
   public final String a;  <br />
   @Position(1)  <br />
   public final int b;  <br />
   @Position(2)  <br />
   public final String c;  <br />
   public Struct3(String a, int b, String c)  <br />
   {  <br />
      this.a = a;  <br />
      this.b = b;  <br />
      this.c = c;  <br />
   }  <br />
}
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Figure 11:</td>
<td class="content">A Struct with three elements</td>
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
<td class="figure">public void do(TestStruct data);
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Figure 12:</td>
<td class="content">A struct as a parameter to a method</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

Section 10 describes how these can be automatically generated from D-Bus introspection data.

#### 7.7  Objects

You can pass references to exportable objects round using their object paths. To do this in Java you declare a type of DBusInterface. When the library receive- an object path it will automatically convert it into the object you are exporting with that object path. You can pass remote objects back to their processes in a similar fashion.

Using a parameter of type DBusInterface can cause the automatic creation of a proxy object using introspection. If the remote app does not support introspection, or the object does not exist at the time you receive the message then this will fail. In that case the parameter can be declared to be of type Path. In this case no automatic creation will be performed and you can get the path as a string with either the getPath or toString methods on the Path object.

#### 7.8  Multiple Return Values

D-Bus also allows functions to return multiple values, a concept not supported by Java. This has been solved in a fashion similar to the struct, using a Tuple<sup>17</sup> class. Tuples are defined as generic tuples which can be parameterised for different types and just need to be defined of the appropriate length. This can be seen in figure 13 and a call in figure 14. Again, these can be automatically generated from introspection data.

<table class="figure">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="figure">
<td class="figure">import org.freedesktop.dbus.Tuple;  <br />
 <br />
public final class TestTuple&lt;A, B, C&gt; extends Tuple  <br />
{  <br />
   public final A a;  <br />
   public final B b;  <br />
   public final C c;  <br />
   public TestTuple(A a, B b, C c)  <br />
   {  <br />
      this.a = a;  <br />
      this.b = b;  <br />
      this.c = c;  <br />
   }  <br />
}
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Figure 13:</td>
<td class="content">A 3-tuple</td>
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
<td class="figure">public ThreeTuple&lt;String, Integer, Boolean&gt; status(int item);
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Figure 14:</td>
<td class="content">A Tuple being returned from a method</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

#### 7.9  Full list of types

Table 1 contains a full list of all the Java types and their corresponding D-Bus types.

<table class="float">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="float">
<td class="float"><table id="TBL-2" class="tabular" data-cellspacing="0" data-cellpadding="0" data-rules="groups">
<tbody>
<tr id="TBL-2-1-" style="vertical-align:baseline;">
<td id="TBL-2-1-1" class="td11" style="text-align: left; white-space: nowrap;">Java Type </td>
<td id="TBL-2-1-2" class="td11" style="text-align: left; white-space: nowrap;">D-Bus Type </td>
</tr>
<tr class="hline">
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr id="TBL-2-2-" style="vertical-align:baseline;">
<td id="TBL-2-2-1" class="td11" style="text-align: left; white-space: nowrap;">Byte</td>
<td id="TBL-2-2-2" class="td11" style="text-align: left; white-space: nowrap;">DBUS_TYPE_BYTE</td>
</tr>
<tr id="TBL-2-3-" style="vertical-align:baseline;">
<td id="TBL-2-3-1" class="td11" style="text-align: left; white-space: nowrap;">byte</td>
<td id="TBL-2-3-2" class="td11" style="text-align: left; white-space: nowrap;">DBUS_TYPE_BYTE</td>
</tr>
<tr id="TBL-2-4-" style="vertical-align:baseline;">
<td id="TBL-2-4-1" class="td11" style="text-align: left; white-space: nowrap;">Boolean</td>
<td id="TBL-2-4-2" class="td11" style="text-align: left; white-space: nowrap;">DBUS_TYPE_BOOLEAN</td>
</tr>
<tr id="TBL-2-5-" style="vertical-align:baseline;">
<td id="TBL-2-5-1" class="td11" style="text-align: left; white-space: nowrap;">boolean</td>
<td id="TBL-2-5-2" class="td11" style="text-align: left; white-space: nowrap;">DBUS_TYPE_BOOLEAN</td>
</tr>
<tr id="TBL-2-6-" style="vertical-align:baseline;">
<td id="TBL-2-6-1" class="td11" style="text-align: left; white-space: nowrap;">Short</td>
<td id="TBL-2-6-2" class="td11" style="text-align: left; white-space: nowrap;">DBUS_TYPE_INT16</td>
</tr>
<tr id="TBL-2-7-" style="vertical-align:baseline;">
<td id="TBL-2-7-1" class="td11" style="text-align: left; white-space: nowrap;">short</td>
<td id="TBL-2-7-2" class="td11" style="text-align: left; white-space: nowrap;">DBUS_TYPE_INT16</td>
</tr>
<tr id="TBL-2-8-" style="vertical-align:baseline;">
<td id="TBL-2-8-1" class="td11" style="text-align: left; white-space: nowrap;">UInt16</td>
<td id="TBL-2-8-2" class="td11" style="text-align: left; white-space: nowrap;">DBUS_TYPE_UINT16</td>
</tr>
<tr id="TBL-2-9-" style="vertical-align:baseline;">
<td id="TBL-2-9-1" class="td11" style="text-align: left; white-space: nowrap;">int</td>
<td id="TBL-2-9-2" class="td11" style="text-align: left; white-space: nowrap;">DBUS_TYPE_INT32</td>
</tr>
<tr id="TBL-2-10-" style="vertical-align:baseline;">
<td id="TBL-2-10-1" class="td11" style="text-align: left; white-space: nowrap;">Integer</td>
<td id="TBL-2-10-2" class="td11" style="text-align: left; white-space: nowrap;">DBUS_TYPE_INT32</td>
</tr>
<tr id="TBL-2-11-" style="vertical-align:baseline;">
<td id="TBL-2-11-1" class="td11" style="text-align: left; white-space: nowrap;">UInt32</td>
<td id="TBL-2-11-2" class="td11" style="text-align: left; white-space: nowrap;">DBUS_TYPE_UINT32</td>
</tr>
<tr id="TBL-2-12-" style="vertical-align:baseline;">
<td id="TBL-2-12-1" class="td11" style="text-align: left; white-space: nowrap;">long</td>
<td id="TBL-2-12-2" class="td11" style="text-align: left; white-space: nowrap;">DBUS_TYPE_INT64</td>
</tr>
<tr id="TBL-2-13-" style="vertical-align:baseline;">
<td id="TBL-2-13-1" class="td11" style="text-align: left; white-space: nowrap;">Long</td>
<td id="TBL-2-13-2" class="td11" style="text-align: left; white-space: nowrap;">DBUS_TYPE_INT64</td>
</tr>
<tr id="TBL-2-14-" style="vertical-align:baseline;">
<td id="TBL-2-14-1" class="td11" style="text-align: left; white-space: nowrap;">UInt64</td>
<td id="TBL-2-14-2" class="td11" style="text-align: left; white-space: nowrap;">DBUS_TYPE_UINT64</td>
</tr>
<tr id="TBL-2-15-" style="vertical-align:baseline;">
<td id="TBL-2-15-1" class="td11" style="text-align: left; white-space: nowrap;">double</td>
<td id="TBL-2-15-2" class="td11" style="text-align: left; white-space: nowrap;">DBUS_TYPE_DOUBLE</td>
</tr>
<tr id="TBL-2-16-" style="vertical-align:baseline;">
<td id="TBL-2-16-1" class="td11" style="text-align: left; white-space: nowrap;">Double</td>
<td id="TBL-2-16-2" class="td11" style="text-align: left; white-space: nowrap;">DBUS_TYPE_DOUBLE</td>
</tr>
<tr id="TBL-2-17-" style="vertical-align:baseline;">
<td id="TBL-2-17-1" class="td11" style="text-align: left; white-space: nowrap;">String</td>
<td id="TBL-2-17-2" class="td11" style="text-align: left; white-space: nowrap;">DBUS_TYPE_STRING</td>
</tr>
<tr id="TBL-2-18-" style="vertical-align:baseline;">
<td id="TBL-2-18-1" class="td11" style="text-align: left; white-space: nowrap;">Path</td>
<td id="TBL-2-18-2" class="td11" style="text-align: left; white-space: nowrap;">DBUS_TYPE_OBJECT_PATH</td>
</tr>
<tr id="TBL-2-19-" style="vertical-align:baseline;">
<td id="TBL-2-19-1" class="td11" style="text-align: left; white-space: nowrap;">&lt;T&gt; </td>
<td id="TBL-2-19-2" class="td11" style="text-align: left; white-space: nowrap;">DBUS_TYPE_VARIANT</td>
</tr>
<tr id="TBL-2-20-" style="vertical-align:baseline;">
<td id="TBL-2-20-1" class="td11" style="text-align: left; white-space: nowrap;">Variant</td>
<td id="TBL-2-20-2" class="td11" style="text-align: left; white-space: nowrap;">DBUS_TYPE_VARIANT</td>
</tr>
<tr id="TBL-2-21-" style="vertical-align:baseline;">
<td id="TBL-2-21-1" class="td11" style="text-align: left; white-space: nowrap;">? extends Struct</td>
<td id="TBL-2-21-2" class="td11" style="text-align: left; white-space: nowrap;">DBUS_TYPE_STRUCT</td>
</tr>
<tr id="TBL-2-22-" style="vertical-align:baseline;">
<td id="TBL-2-22-1" class="td11" style="text-align: left; white-space: nowrap;">?[ ]</td>
<td id="TBL-2-22-2" class="td11" style="text-align: left; white-space: nowrap;">DBUS_TYPE_ARRAY</td>
</tr>
<tr id="TBL-2-23-" style="vertical-align:baseline;">
<td id="TBL-2-23-1" class="td11" style="text-align: left; white-space: nowrap;">? extends List</td>
<td id="TBL-2-23-2" class="td11" style="text-align: left; white-space: nowrap;">DBUS_TYPE_ARRAY</td>
</tr>
<tr id="TBL-2-24-" style="vertical-align:baseline;">
<td id="TBL-2-24-1" class="td11" style="text-align: left; white-space: nowrap;">? extends Map</td>
<td id="TBL-2-24-2" class="td11" style="text-align: left; white-space: nowrap;">DBUS_TYPE_DICT</td>
</tr>
<tr id="TBL-2-25-" style="vertical-align:baseline;">
<td id="TBL-2-25-1" class="td11" style="text-align: left; white-space: nowrap;">? extends DBusInterface</td>
<td id="TBL-2-25-2" class="td11" style="text-align: left; white-space: nowrap;">DBUS_TYPE_OBJECT_PATH</td>
</tr>
<tr id="TBL-2-26-" style="vertical-align:baseline;">
<td id="TBL-2-26-1" class="td11" style="text-align: left; white-space: nowrap;">Type[ ]</td>
<td id="TBL-2-26-2" class="td11" style="text-align: left; white-space: nowrap;">DBUS_TYPE_SIGNATURE</td>
</tr>
<tr id="TBL-2-27-" style="vertical-align:baseline;">
<td id="TBL-2-27-1" class="td11" style="text-align: left; white-space: nowrap;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Table 1:</td>
<td class="content">Mapping between Java types and D-Bus types</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

##### 7.9.1  float

Currently the D-Bus reference implementation does not support a native single-precision floating point type. Along with the C# implementation of the protocol, the Java implementation supports this extension to the protocol. By default, however, the library operates in compatibility mode and converts all floats to the double type. To disable compatibility mode export the environment variable DBUS\_JAVA\_FLOATS=true.

\[prev\] \[prev-tail\] \[front\] \[up\]
