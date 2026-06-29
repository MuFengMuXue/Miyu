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
<td class="NavBarCell1Rev" data-bgcolor="#FFFFFF"> <strong>Package</strong> </td>
<td class="NavBarCell1" data-bgcolor="#EEEEFF">Class </td>
<td class="NavBarCell1" data-bgcolor="#EEEEFF"><strong>Tree</strong> </td>
<td class="NavBarCell1" data-bgcolor="#EEEEFF"><strong>Deprecated</strong> </td>
<td class="NavBarCell1" data-bgcolor="#EEEEFF"><strong>Index</strong> </td>
<td class="NavBarCell1" data-bgcolor="#EEEEFF"><strong>Help</strong> </td>
</tr>
</tbody>
</table></td>
<td rowspan="2" style="text-align: right;" data-valign="top"><em></em></td>
</tr>
<tr>
<td class="NavBarCell2" data-bgcolor="white"> <strong>PREV PACKAGE</strong>   <strong>NEXT PACKAGE</strong></td>
<td class="NavBarCell2" data-bgcolor="white"><strong>FRAMES</strong>    <strong>NO FRAMES</strong>    
<strong>All Classes</strong></td>
</tr>
</tbody>
</table>

## Package org.freedesktop.dbus

| **Interface Summary** |  |
|----|----|
| **CallbackHandler\<ReturnType\>** | Interface for callbacks in async mode |
| **DBusInterface** | Denotes a class as exportable or a remote interface which can be called. |
| **DBusSerializable** | Custom classes may be sent over DBus if they implement this interface. |
| **DBusSigHandler\<T extends DBusSignal\>** | Handle a signal on DBus. |
| **Message.ArgumentType** | Defines constants for each argument type. |
| **Message.Endian** | Defines constants representing the endianness of the message. |
| **Message.Flags** | Defines constants representing the flags which can be set on a message. |
| **Message.HeaderField** | Defines constants for each valid header field type. |
| **Message.MessageType** | Defines constants for each message type. |

 

| **Class Summary** |  |
|----|----|
| **AbstractConnection** | Handles a connection to DBus. |
| **BusAddress** |   |
| **DBusAsyncReply\<ReturnType\>** | A handle to an asynchronous method call. |
| **DBusCallInfo** | Holds information on a method call |
| **DBusConnection** | Handles a connection to DBus. |
| **DBusMatchRule** |   |
| **DBusSignal** |   |
| **DirectConnection** | Handles a peer to peer connection between two applications withou a bus daemon. |
| **Error** | Error messages which can be sent over the bus. |
| **Gettext** |   |
| **Marshalling** | Contains static methods for marshalling values. |
| **Message** | Superclass of all messages which are sent over the Bus. |
| **MessageReader** |   |
| **MessageWriter** |   |
| **MethodCall** |   |
| **MethodReturn** |   |
| **Path** |   |
| **StrongReference\<T\>** | An alternative to a WeakReference when you don't want that behaviour. |
| **Struct** | This class should be extended to create Structs. |
| **Transport** |   |
| **Transport.SASL** |   |
| **Transport.SASL.Command** |   |
| **Tuple** | This class should be extended to create Tuples. |
| **TypeSignature** |   |
| **UInt16** | Class to represent 16-bit unsigned integers. |
| **UInt32** | Class to represent unsigned 32-bit numbers. |
| **UInt64** | Class to represent unsigned 64-bit numbers. |
| **Variant\<T\>** | A Wrapper class for Variant values. |

 

| **Annotation Types Summary** |  |
|----|----|
| **DBusInterfaceName** | Force the interface name to be different to the Java class name. |
| **DBusMemberName** | Force the member (method/signal) name on the bus to be different to the Java name. |
| **Position** | Position annotation, to annotate Struct fields to be sent over DBus. |

 

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
<td class="NavBarCell1Rev" data-bgcolor="#FFFFFF"> <strong>Package</strong> </td>
<td class="NavBarCell1" data-bgcolor="#EEEEFF">Class </td>
<td class="NavBarCell1" data-bgcolor="#EEEEFF"><strong>Tree</strong> </td>
<td class="NavBarCell1" data-bgcolor="#EEEEFF"><strong>Deprecated</strong> </td>
<td class="NavBarCell1" data-bgcolor="#EEEEFF"><strong>Index</strong> </td>
<td class="NavBarCell1" data-bgcolor="#EEEEFF"><strong>Help</strong> </td>
</tr>
</tbody>
</table></td>
<td rowspan="2" style="text-align: right;" data-valign="top"><em></em></td>
</tr>
<tr>
<td class="NavBarCell2" data-bgcolor="white"> <strong>PREV PACKAGE</strong>   <strong>NEXT PACKAGE</strong></td>
<td class="NavBarCell2" data-bgcolor="white"><strong>FRAMES</strong>    <strong>NO FRAMES</strong>    
<strong>All Classes</strong></td>
</tr>
</tbody>
</table>
