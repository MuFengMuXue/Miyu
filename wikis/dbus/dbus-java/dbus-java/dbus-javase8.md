\[prev\] \[prev-tail\] \[tail\] \[up\]

### 8  Annotations

You can annotate your D-Bus methods as in figure 15 to provide hints to other users of your API. Common annotations are listed in table 2.

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
@org.freedesktop.DBus.Description("Some Methods");  <br />
public interface DBus extends DBusInterface  <br />
{  <br />
   @org.freedesktop.DBus.Description("Check if the name has an owner")  <br />
   public boolean NameHasOwner(String name);  <br />
   @org.freedesktop.DBus.Description("Request a name")  <br />
   @org.freedesktop.DBus.Deprecated()  <br />
   public UInt32 RequestName(String name, UInt32 flags);  <br />
}
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Figure 15:</td>
<td class="content">An annotated method</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

<table class="float">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="float">
<td class="float"><table id="TBL-3" class="tabular" data-cellspacing="0" data-cellpadding="0" data-rules="groups">
<tbody>
<tr id="TBL-3-1-" style="vertical-align:baseline;">
<td id="TBL-3-1-1" class="td11" style="text-align: left; white-space: nowrap;">Name </td>
<td id="TBL-3-1-2" class="td11" style="text-align: left; white-space: nowrap;">Meaning </td>
</tr>
<tr class="hline">
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr id="TBL-3-2-" style="vertical-align:baseline;">
<td id="TBL-3-2-1" class="td11" style="text-align: left; white-space: nowrap;">org.freedesktop.DBus.Description</td>
<td id="TBL-3-2-2" class="td11" style="text-align: left; white-space: nowrap;">Provide a short 1-line description</td>
</tr>
<tr id="TBL-3-3-" style="vertical-align:baseline;">
<td id="TBL-3-3-1" class="td11" style="text-align: left; white-space: nowrap;"></td>
<td id="TBL-3-3-2" class="td11" style="text-align: left; white-space: nowrap;">of the method or interface.</td>
</tr>
<tr id="TBL-3-4-" style="vertical-align:baseline;">
<td id="TBL-3-4-1" class="td11" style="text-align: left; white-space: nowrap;">org.freedesktop.DBus.Deprecated</td>
<td id="TBL-3-4-2" class="td11" style="text-align: left; white-space: nowrap;">This method or interface is Deprecated.</td>
</tr>
<tr id="TBL-3-5-" style="vertical-align:baseline;">
<td id="TBL-3-5-1" class="td11" style="text-align: left; white-space: nowrap;">org.freedesktop.DBus.Method.NoReply</td>
<td id="TBL-3-5-2" class="td11" style="text-align: left; white-space: nowrap;">This method may be called and returned</td>
</tr>
<tr id="TBL-3-6-" style="vertical-align:baseline;">
<td id="TBL-3-6-1" class="td11" style="text-align: left; white-space: nowrap;"></td>
<td id="TBL-3-6-2" class="td11" style="text-align: left; white-space: nowrap;">without waiting for a reply.</td>
</tr>
<tr id="TBL-3-7-" style="vertical-align:baseline;">
<td id="TBL-3-7-1" class="td11" style="text-align: left; white-space: nowrap;">org.freedesktop.DBus.Method.Error</td>
<td id="TBL-3-7-2" class="td11" style="text-align: left; white-space: nowrap;">This method may throw the listed Exception</td>
</tr>
<tr id="TBL-3-8-" style="vertical-align:baseline;">
<td id="TBL-3-8-1" class="td11" style="text-align: left; white-space: nowrap;"></td>
<td id="TBL-3-8-2" class="td11" style="text-align: left; white-space: nowrap;">in addition to the standard ones.</td>
</tr>
<tr id="TBL-3-9-" style="vertical-align:baseline;">
<td id="TBL-3-9-1" class="td11" style="text-align: left; white-space: nowrap;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Table 2:</td>
<td class="content">Common Annotations</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

\[prev\] \[prev-tail\] \[front\] \[up\]
