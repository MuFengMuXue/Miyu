<table data-border="0" width="100%" data-cellpadding="1" data-cellspacing="0" data-summary="">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td colspan="2" class="NavBarCell1" data-bgcolor="#EEEEFF"><table data-border="0" data-cellpadding="0" data-cellspacing="3" data-summary="">
<tbody>
<tr data-align="center" data-valign="top">
<td class="NavBarCell1" data-bgcolor="#EEEEFF"><strong>Overview</strong> </td>
<td class="NavBarCell1" data-bgcolor="#EEEEFF">Package </td>
<td class="NavBarCell1" data-bgcolor="#EEEEFF">Class </td>
<td class="NavBarCell1Rev" data-bgcolor="#FFFFFF"> <strong>Tree</strong> </td>
<td class="NavBarCell1" data-bgcolor="#EEEEFF"><strong>Deprecated</strong> </td>
<td class="NavBarCell1" data-bgcolor="#EEEEFF"><strong>Index</strong> </td>
<td class="NavBarCell1" data-bgcolor="#EEEEFF"><strong>Help</strong> </td>
</tr>
</tbody>
</table></td>
<td rowspan="2" style="text-align: right;" data-valign="top"><em></em></td>
</tr>
<tr>
<td class="NavBarCell2" data-bgcolor="white"> PREV   NEXT</td>
<td class="NavBarCell2" data-bgcolor="white"><strong>FRAMES</strong>    <strong>NO FRAMES</strong>    
<strong>All Classes</strong></td>
</tr>
</tbody>
</table>

## Hierarchy For All Packages

**Package Hierarchies:**  
org.freedesktop, org.freedesktop.dbus, org.freedesktop.dbus.exceptions, org.freedesktop.dbus.types

## Class Hierarchy

- java.lang.**Object**
  - org.freedesktop.dbus.**AbstractConnection**
    - org.freedesktop.dbus.**DBusConnection**
    - org.freedesktop.dbus.**DirectConnection**
  - org.freedesktop.dbus.**AbstractConnection.FallbackContainer**
  - org.freedesktop.dbus.**BusAddress**
  - org.freedesktop.dbus.**DBusAsyncReply**\<ReturnType\>
  - org.freedesktop.dbus.**DBusCallInfo**
  - org.freedesktop.dbus.**DBusConnection.PeerSet** (implements org.freedesktop.dbus.DBusSigHandler\<T\>, java.util.Set\<E\>)
  - org.freedesktop.dbus.types.**DBusListType** (implements java.lang.reflect.ParameterizedType)
  - org.freedesktop.dbus.types.**DBusMapType** (implements java.lang.reflect.ParameterizedType)
  - org.freedesktop.dbus.**DBusMatchRule**
  - org.freedesktop.dbus.types.**DBusStructType** (implements java.lang.reflect.ParameterizedType)
  - org.freedesktop.dbus.**Gettext**
  - org.freedesktop.dbus.**Marshalling**
  - org.freedesktop.dbus.**Message**
    - org.freedesktop.dbus.**DBusSignal**
      - org.freedesktop.**DBus.Binding.TestClient.Trigger**
      - org.freedesktop.**DBus.Binding.TestSignals.Triggered**
      - org.freedesktop.**DBus.Local.Disconnected**
      - org.freedesktop.**DBus.NameAcquired**
      - org.freedesktop.**DBus.NameLost**
      - org.freedesktop.**DBus.NameOwnerChanged**
    - org.freedesktop.dbus.**Error**
    - org.freedesktop.dbus.**MethodCall**
    - org.freedesktop.dbus.**MethodReturn**
  - org.freedesktop.dbus.**MessageReader**
  - org.freedesktop.dbus.**MessageWriter**
  - java.lang.**Number** (implements java.io.Serializable)
    - org.freedesktop.dbus.**UInt16** (implements java.lang.Comparable\<T\>)
    - org.freedesktop.dbus.**UInt32** (implements java.lang.Comparable\<T\>)
    - org.freedesktop.dbus.**UInt64** (implements java.lang.Comparable\<T\>)
  - org.freedesktop.dbus.**Path** (implements java.lang.Comparable\<T\>)
  - java.lang.ref.**Reference**\<T\>
    - java.lang.ref.**WeakReference**\<T\>
      - org.freedesktop.dbus.**StrongReference**\<T\>
  - org.freedesktop.dbus.**Struct**
    - org.freedesktop.**DBus.Binding.TestStruct**
  - java.lang.**Thread** (implements java.lang.Runnable)
    - org.freedesktop.dbus.**AbstractConnection.\_thread**
    - org.freedesktop.dbus.**AbstractConnection.\_workerthread**
  - java.lang.**Throwable** (implements java.io.Serializable)
    - java.lang.**Exception**
      - org.freedesktop.dbus.exceptions.**DBusException**
        - org.freedesktop.dbus.exceptions.**FatalDBusException** (implements org.freedesktop.dbus.exceptions.FatalException)
        - org.freedesktop.dbus.exceptions.**MarshallingException** (implements org.freedesktop.dbus.exceptions.NonFatalException)
        - org.freedesktop.dbus.exceptions.**MessageFormatException** (implements org.freedesktop.dbus.exceptions.NonFatalException)
        - org.freedesktop.dbus.exceptions.**UnknownTypeCodeException** (implements org.freedesktop.dbus.exceptions.NonFatalException)
      - java.io.**IOException**
        - org.freedesktop.dbus.exceptions.**MessageProtocolVersionException** (implements org.freedesktop.dbus.exceptions.FatalException)
        - org.freedesktop.dbus.exceptions.**MessageTypeException** (implements org.freedesktop.dbus.exceptions.NonFatalException)
      - java.lang.**RuntimeException**
        - org.freedesktop.dbus.exceptions.**DBusExecutionException**
          - org.freedesktop.**DBus.Error.AccessDenied**
          - org.freedesktop.**DBus.Error.MatchRuleInvalid**
          - org.freedesktop.**DBus.Error.NoReply**
          - org.freedesktop.**DBus.Error.ServiceUnknown**
          - org.freedesktop.**DBus.Error.UnknownMethod**
          - org.freedesktop.**DBus.Error.UnknownObject**
          - org.freedesktop.dbus.exceptions.**InternalMessageException** (implements org.freedesktop.dbus.exceptions.NonFatalException)
          - org.freedesktop.dbus.exceptions.**NotConnected** (implements org.freedesktop.dbus.exceptions.FatalException)
  - org.freedesktop.dbus.**Transport**
  - org.freedesktop.dbus.**Transport.SASL**
  - org.freedesktop.dbus.**Transport.SASL.Command**
  - org.freedesktop.dbus.**Tuple**
    - org.freedesktop.**DBus.Binding.Triplet**\<A,B,C\>
  - org.freedesktop.dbus.**TypeSignature**
  - org.freedesktop.dbus.**Variant**\<T\>

## Interface Hierarchy

- org.freedesktop.dbus.**CallbackHandler**\<ReturnType\>
- org.freedesktop.**DBus.Binding**
- org.freedesktop.**DBus.Error**
- org.freedesktop.**DBus.GLib**
- org.freedesktop.**DBus.Method**
- org.freedesktop.dbus.**DBusInterface**
  - org.freedesktop.**DBus**
  - org.freedesktop.**DBus.Binding.SingleTests**
  - org.freedesktop.**DBus.Binding.TestClient**
  - org.freedesktop.**DBus.Binding.Tests**
  - org.freedesktop.**DBus.Binding.TestSignals**
  - org.freedesktop.**DBus.Introspectable**
  - org.freedesktop.**DBus.Local**
  - org.freedesktop.**DBus.Peer**
  - org.freedesktop.**DBus.Properties**
- org.freedesktop.dbus.**DBusSerializable**
- org.freedesktop.dbus.**DBusSigHandler**\<T\>
- org.freedesktop.dbus.exceptions.**FatalException**
- org.freedesktop.dbus.**Message.ArgumentType**
- org.freedesktop.dbus.**Message.Endian**
- org.freedesktop.dbus.**Message.Flags**
- org.freedesktop.dbus.**Message.HeaderField**
- org.freedesktop.dbus.**Message.MessageType**
- org.freedesktop.dbus.exceptions.**NonFatalException**

## Annotation Type Hierarchy

- org.freedesktop.**DBus.Description** (implements java.lang.annotation.Annotation)
- org.freedesktop.**DBus.Deprecated** (implements java.lang.annotation.Annotation)
- org.freedesktop.**DBus.Method.NoReply** (implements java.lang.annotation.Annotation)
- org.freedesktop.**DBus.Method.Error** (implements java.lang.annotation.Annotation)
- org.freedesktop.**DBus.GLib.CSymbol** (implements java.lang.annotation.Annotation)
- org.freedesktop.dbus.**DBusInterfaceName** (implements java.lang.annotation.Annotation)
- org.freedesktop.dbus.**DBusMemberName** (implements java.lang.annotation.Annotation)
- org.freedesktop.dbus.**Position** (implements java.lang.annotation.Annotation)

<table data-border="0" width="100%" data-cellpadding="1" data-cellspacing="0" data-summary="">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td colspan="2" class="NavBarCell1" data-bgcolor="#EEEEFF"><table data-border="0" data-cellpadding="0" data-cellspacing="3" data-summary="">
<tbody>
<tr data-align="center" data-valign="top">
<td class="NavBarCell1" data-bgcolor="#EEEEFF"><strong>Overview</strong> </td>
<td class="NavBarCell1" data-bgcolor="#EEEEFF">Package </td>
<td class="NavBarCell1" data-bgcolor="#EEEEFF">Class </td>
<td class="NavBarCell1Rev" data-bgcolor="#FFFFFF"> <strong>Tree</strong> </td>
<td class="NavBarCell1" data-bgcolor="#EEEEFF"><strong>Deprecated</strong> </td>
<td class="NavBarCell1" data-bgcolor="#EEEEFF"><strong>Index</strong> </td>
<td class="NavBarCell1" data-bgcolor="#EEEEFF"><strong>Help</strong> </td>
</tr>
</tbody>
</table></td>
<td rowspan="2" style="text-align: right;" data-valign="top"><em></em></td>
</tr>
<tr>
<td class="NavBarCell2" data-bgcolor="white"> PREV   NEXT</td>
<td class="NavBarCell2" data-bgcolor="white"><strong>FRAMES</strong>    <strong>NO FRAMES</strong>    
<strong>All Classes</strong></td>
</tr>
</tbody>
</table>
