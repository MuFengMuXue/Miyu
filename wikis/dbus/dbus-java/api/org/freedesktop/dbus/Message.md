## org.freedesktop.dbus Class Message

    java.lang.Object
      org.freedesktop.dbus.Message

**Direct Known Subclasses:**  
DBusSignal, Error, MethodCall, MethodReturn

<!-- -->

    public class Messageextends Object

Superclass of all messages which are sent over the Bus. This class deals with all the marshalling to/from the wire format.

<table data-border="1" width="100%" data-cellpadding="3" data-cellspacing="0" data-summary="">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="TableHeadingColor" data-bgcolor="#CCCCFF">
<th colspan="2" style="text-align: left;"><strong>Nested Class Summary</strong></th>
</tr>
</thead>
<tbody>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static interface</code></td>
<td><strong><code>Message.ArgumentType</code></strong><br />
          Defines constants for each argument type.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static interface</code></td>
<td><strong><code>Message.Endian</code></strong><br />
          Defines constants representing the endianness of the message.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static interface</code></td>
<td><strong><code>Message.Flags</code></strong><br />
          Defines constants representing the flags which can be set on a message.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static interface</code></td>
<td><strong><code>Message.HeaderField</code></strong><br />
          Defines constants for each valid header field type.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static interface</code></td>
<td><strong><code>Message.MessageType</code></strong><br />
          Defines constants for each message type.</td>
</tr>
</tbody>
</table>

 

<table data-border="1" width="100%" data-cellpadding="3" data-cellspacing="0" data-summary="">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="TableHeadingColor" data-bgcolor="#CCCCFF">
<th colspan="2" style="text-align: left;"><strong>Field Summary</strong></th>
</tr>
</thead>
<tbody>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  long</code></td>
<td><strong><code>bytecounter</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  byte</code></td>
<td><strong><code>flags</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected static long</code></td>
<td><strong><code>globalserial</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  </code><code>Map</code><code>&lt;</code><code>Byte</code><code>,</code><code>Object</code><code>&gt;</code></td>
<td><strong><code>headers</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static byte</code></td>
<td><strong><code>PROTOCOL</code></strong><br />
          The current protocol major version.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  byte</code></td>
<td><strong><code>protover</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  long</code></td>
<td><strong><code>serial</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  byte</code></td>
<td><strong><code>type</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  byte[][]</code></td>
<td><strong><code>wiredata</code></strong><br />
           </td>
</tr>
</tbody>
</table>

 

<table data-border="1" width="100%" data-cellpadding="3" data-cellspacing="0" data-summary="">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="TableHeadingColor" data-bgcolor="#CCCCFF">
<th colspan="2" style="text-align: left;"><strong>Constructor Summary</strong></th>
</tr>
</thead>
<tbody>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected </code></td>
<td><strong><code>Message</code></strong><code>()</code><br />
          Create a blank message.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected </code></td>
<td><strong><code>Message</code></strong><code>(byte endian, byte type, byte flags)</code><br />
          Create a message; only to be called by sub-classes.</td>
</tr>
</tbody>
</table>

 

<table data-border="1" width="100%" data-cellpadding="3" data-cellspacing="0" data-summary="">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="TableHeadingColor" data-bgcolor="#CCCCFF">
<th colspan="2" style="text-align: left;"><strong>Method Summary</strong></th>
</tr>
</thead>
<tbody>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> int</code></td>
<td><strong><code>align</code></strong><code>(int current, byte type)</code><br />
          Align a counter to the given type.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>append</code></strong><code>(</code><code>String</code><code> sig, </code><code>Object</code><code>... data)</code><br />
          Append a series of values to the message.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  void</code></td>
<td><strong><code>appendByte</code></strong><code>(byte b)</code><br />
          Appends a byte to the buffer list.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  void</code></td>
<td><strong><code>appendBytes</code></strong><code>(byte[] buf)</code><br />
          Appends a buffer to the buffer list.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>appendint</code></strong><code>(long l, int width)</code><br />
          Marshalls an integer of a given width and appends it to the message.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static long</code></td>
<td><strong><code>demarshallint</code></strong><code>(byte[] buf, int ofs, byte endian, int width)</code><br />
          Demarshalls an integer of a given width from a buffer.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> long</code></td>
<td><strong><code>demarshallint</code></strong><code>(byte[] buf, int ofs, int width)</code><br />
          Demarshalls an integer of a given width from a buffer.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static long</code></td>
<td><strong><code>demarshallintBig</code></strong><code>(byte[] buf, int ofs, int width)</code><br />
          Demarshalls an integer of a given width from a buffer using big-endian format.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static long</code></td>
<td><strong><code>demarshallintLittle</code></strong><code>(byte[] buf, int ofs, int width)</code><br />
          Demarshalls an integer of a given width from a buffer using little-endian format.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>Object</code><code>[]</code></td>
<td><strong><code>extract</code></strong><code>(</code><code>String</code><code> sig, byte[] buf, int ofs)</code><br />
          Demarshall values from a buffer.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>Object</code><code>[]</code></td>
<td><strong><code>extract</code></strong><code>(</code><code>String</code><code> sig, byte[] buf, int[] ofs)</code><br />
          Demarshall values from a buffer.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>getAlignment</code></strong><code>(byte type)</code><br />
          Return the alignment for a given type.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>getDestination</code></strong><code>()</code><br />
          Returns the destination of the message.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> int</code></td>
<td><strong><code>getFlags</code></strong><code>()</code><br />
          Returns the message flags.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>Object</code></td>
<td><strong><code>getHeader</code></strong><code>(byte type)</code><br />
          Returns the value of the header field of a given field.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static </code><code>String</code></td>
<td><strong><code>getHeaderFieldName</code></strong><code>(byte field)</code><br />
          Returns the name of the given header field.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>getInterface</code></strong><code>()</code><br />
          Returns the interface of the message.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>getName</code></strong><code>()</code><br />
          Returns the member name or error name this message represents.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>Object</code><code>[]</code></td>
<td><strong><code>getParameters</code></strong><code>()</code><br />
          Parses and returns the parameters to this message as an Object array.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>getPath</code></strong><code>()</code><br />
          Returns the object path of the message.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> long</code></td>
<td><strong><code>getReplySerial</code></strong><code>()</code><br />
          If this is a reply to a message, this returns its serial.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> long</code></td>
<td><strong><code>getSerial</code></strong><code>()</code><br />
          Returns the message serial ID (unique for this connection)</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>getSig</code></strong><code>()</code><br />
          Returns the dbus signature of the parameters.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>getSource</code></strong><code>()</code><br />
          Returns the Bus ID that sent the message.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> byte[][]</code></td>
<td><strong><code>getWireData</code></strong><code>()</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>marshallint</code></strong><code>(long l, byte[] buf, int ofs, int width)</code><br />
          Marshalls an integer of a given width into a buffer.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static void</code></td>
<td><strong><code>marshallintBig</code></strong><code>(long l, byte[] buf, int ofs, int width)</code><br />
          Marshalls an integer of a given width into a buffer using big-endian format.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static void</code></td>
<td><strong><code>marshallintLittle</code></strong><code>(long l, byte[] buf, int ofs, int width)</code><br />
          Marshalls an integer of a given width into a buffer using little-endian format.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>pad</code></strong><code>(byte type)</code><br />
          Pad the message to the proper alignment for the given type.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>protected  void</code></td>
<td><strong><code>setArgs</code></strong><code>(</code><code>Object</code><code>[] args)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>setSource</code></strong><code>(</code><code>String</code><code> source)</code><br />
          Warning, do not use this method unless you really know what you are doing.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>toString</code></strong><code>()</code><br />
          Formats the message in a human-readable format.</td>
</tr>
</tbody>
</table>

 

| **Methods inherited from class java.lang.Object** |
|----|
| `clone``, ``equals``, ``finalize``, ``getClass``, ``hashCode``, ``notify``, ``notifyAll``, ``wait``, ``wait``, ``wait` |

 

| **Field Detail** |
|------------------|

### PROTOCOL

    public static final byte PROTOCOL

The current protocol major version.

**See Also:**  
Constant Field Values

### wiredata

    protected byte[][] wiredata

### bytecounter

    protected long bytecounter

### headers

    protected Map<Byte,Object> headers

### globalserial

    protected static long globalserial

### serial

    protected long serial

### type

    protected byte type

### flags

    protected byte flags

### protover

    protected byte protover

| **Constructor Detail** |
|------------------------|

### Message

    protected Message(byte endian,
                      byte type,
                      byte flags)
               throws DBusException

Create a message; only to be called by sub-classes.

**Parameters:**  
`endian` - The endianness to create the message.

`type` - The message type.

`flags` - Any message flags.

**Throws:**  
`DBusException`

### Message

    protected Message()

Create a blank message. Only to be used when calling populate.

| **Method Detail** |
|-------------------|

### getHeaderFieldName

    public static String getHeaderFieldName(byte field)

Returns the name of the given header field.

### appendBytes

    protected void appendBytes(byte[] buf)

Appends a buffer to the buffer list.

### appendByte

    protected void appendByte(byte b)

Appends a byte to the buffer list.

### demarshallint

    public long demarshallint(byte[] buf,
                              int ofs,
                              int width)

Demarshalls an integer of a given width from a buffer. Endianness is determined from the format of the message.

**Parameters:**  
`buf` - The buffer to demarshall from.

`ofs` - The offset to demarshall from.

`width` - The byte-width of the int.

### demarshallint

    public static long demarshallint(byte[] buf,
                                     int ofs,
                                     byte endian,
                                     int width)

Demarshalls an integer of a given width from a buffer.

**Parameters:**  
`buf` - The buffer to demarshall from.

`ofs` - The offset to demarshall from.

`endian` - The endianness to use in demarshalling.

`width` - The byte-width of the int.

### demarshallintBig

    public static long demarshallintBig(byte[] buf,
                                        int ofs,
                                        int width)

Demarshalls an integer of a given width from a buffer using big-endian format.

**Parameters:**  
`buf` - The buffer to demarshall from.

`ofs` - The offset to demarshall from.

`width` - The byte-width of the int.

### demarshallintLittle

    public static long demarshallintLittle(byte[] buf,
                                           int ofs,
                                           int width)

Demarshalls an integer of a given width from a buffer using little-endian format.

**Parameters:**  
`buf` - The buffer to demarshall from.

`ofs` - The offset to demarshall from.

`width` - The byte-width of the int.

### appendint

    public void appendint(long l,
                          int width)

Marshalls an integer of a given width and appends it to the message. Endianness is determined from the message.

**Parameters:**  
`l` - The integer to marshall.

`width` - The byte-width of the int.

### marshallint

    public void marshallint(long l,
                            byte[] buf,
                            int ofs,
                            int width)

Marshalls an integer of a given width into a buffer. Endianness is determined from the message.

**Parameters:**  
`l` - The integer to marshall.

`buf` - The buffer to marshall to.

`ofs` - The offset to marshall to.

`width` - The byte-width of the int.

### marshallintBig

    public static void marshallintBig(long l,
                                      byte[] buf,
                                      int ofs,
                                      int width)

Marshalls an integer of a given width into a buffer using big-endian format.

**Parameters:**  
`l` - The integer to marshall.

`buf` - The buffer to marshall to.

`ofs` - The offset to marshall to.

`width` - The byte-width of the int.

### marshallintLittle

    public static void marshallintLittle(long l,
                                         byte[] buf,
                                         int ofs,
                                         int width)

Marshalls an integer of a given width into a buffer using little-endian format.

**Parameters:**  
`l` - The integer to marshall.

`buf` - The buffer to demarshall to.

`ofs` - The offset to demarshall to.

`width` - The byte-width of the int.

### getWireData

    public byte[][] getWireData()

### toString

    public String toString()

Formats the message in a human-readable format.

**Overrides:**  
`toString` in class `Object`

### getHeader

    public Object getHeader(byte type)

Returns the value of the header field of a given field.

**Parameters:**  
`type` - The field to return.

**Returns:**  
The value of the field or null if unset.

### pad

    public void pad(byte type)

Pad the message to the proper alignment for the given type.

### getAlignment

    public static int getAlignment(byte type)

Return the alignment for a given type.

### append

    public void append(String sig,
                       Object... data)
                throws DBusException

Append a series of values to the message.

**Parameters:**  
`sig` - The signature(s) of the value(s).

`data` - The value(s).

**Throws:**  
`DBusException`

### align

    public int align(int current,
                     byte type)

Align a counter to the given type.

**Parameters:**  
`current` - The current counter.

`type` - The type to align to.

**Returns:**  
The new, aligned, counter.

### extract

    public Object[] extract(String sig,
                            byte[] buf,
                            int ofs)
                     throws DBusException

Demarshall values from a buffer.

**Parameters:**  
`sig` - The D-Bus signature(s) of the value(s).

`buf` - The buffer to demarshall from.

`ofs` - The offset into the data buffer to start.

**Returns:**  
The demarshalled value(s).

**Throws:**  
`DBusException`

### extract

    public Object[] extract(String sig,
                            byte[] buf,
                            int[] ofs)
                     throws DBusException

Demarshall values from a buffer.

**Parameters:**  
`sig` - The D-Bus signature(s) of the value(s).

`buf` - The buffer to demarshall from.

`ofs` - An array of two ints, the offset into the signature and the offset into the data buffer. These values will be updated to the start of the next value ofter demarshalling.

**Returns:**  
The demarshalled value(s).

**Throws:**  
`DBusException`

### getSource

    public String getSource()

Returns the Bus ID that sent the message.

### getDestination

    public String getDestination()

Returns the destination of the message.

### getInterface

    public String getInterface()

Returns the interface of the message.

### getPath

    public String getPath()

Returns the object path of the message.

### getName

    public String getName()

Returns the member name or error name this message represents.

### getSig

    public String getSig()

Returns the dbus signature of the parameters.

### getFlags

    public int getFlags()

Returns the message flags.

### getSerial

    public long getSerial()

Returns the message serial ID (unique for this connection)

**Returns:**  
the message serial.

### getReplySerial

    public long getReplySerial()

If this is a reply to a message, this returns its serial.

**Returns:**  
The reply serial, or 0 if it is not a reply.

### getParameters

    public Object[] getParameters()
                           throws DBusException

Parses and returns the parameters to this message as an Object array.

**Throws:**  
`DBusException`

### setArgs

    protected void setArgs(Object[] args)

### setSource

    public void setSource(String source)
                   throws DBusException

Warning, do not use this method unless you really know what you are doing.

**Throws:**  
`DBusException`
