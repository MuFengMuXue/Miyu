## org.freedesktop.dbus Class Transport.SASL

    java.lang.Object
      org.freedesktop.dbus.Transport.SASL

**Enclosing class:**  
Transport

<!-- -->

    public static class Transport.SASLextends Object

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
<td style="text-align: right;" data-valign="top" width="1%"><code>static class</code></td>
<td><strong><code>Transport.SASL.Command</code></strong><br />
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
<th colspan="2" style="text-align: left;"><strong>Field Summary</strong></th>
</tr>
</thead>
<tbody>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>AUTH_ANON</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>AUTH_EXTERNAL</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>AUTH_NONE</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>AUTH_SHA</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>AUTHENTICATED</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>challenge</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>COMMAND_AUTH</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>COMMAND_BEGIN</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>COMMAND_CANCEL</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>COMMAND_DATA</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>COMMAND_ERROR</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>COMMAND_OK</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>COMMAND_REJECTED</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>CONTINUE</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code></td>
<td><strong><code>cookie</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static </code><code>String</code></td>
<td><strong><code>COOKIE_CONTEXT</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>COOKIE_TIMEOUT</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>ERROR</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>EXPIRE_KEYS_TIMEOUT_SECONDS</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>FAILED</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>INITIAL_STATE</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>LOCK_TIMEOUT</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>MAX_TIME_TRAVEL_SECONDS</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>MODE_CLIENT</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>MODE_SERVER</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>NEW_KEY_TIMEOUT_SECONDS</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>OK</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>REJECT</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>WAIT_AUTH</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>WAIT_BEGIN</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>WAIT_DATA</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>WAIT_OK</code></strong><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code>static int</code></td>
<td><strong><code>WAIT_REJECT</code></strong><br />
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
<td><strong><code>Transport.SASL</code></strong><code>()</code><br />
           </td>
<td></td>
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
<td style="text-align: right;" data-valign="top" width="1%"><code> boolean</code></td>
<td><strong><code>auth</code></strong><code>(int mode, int types, </code><code>String</code><code> guid, </code><code>OutputStream</code><code> out, </code><code>InputStream</code><code> in, cx.ath.matthew.unix.UnixSocket us)</code><br />
          performs SASL auth on the given streams.</td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> int</code></td>
<td><strong><code>do_challenge</code></strong><code>(int auth, </code><code>Transport.SASL.Command</code><code> c)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> int</code></td>
<td><strong><code>do_response</code></strong><code>(int auth, </code><code>String</code><code> Uid, </code><code>String</code><code> kernelUid, </code><code>Transport.SASL.Command</code><code> c)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>String</code><code>[]</code></td>
<td><strong><code>getTypes</code></strong><code>(int types)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> </code><code>Transport.SASL.Command</code></td>
<td><strong><code>receive</code></strong><code>(</code><code>InputStream</code><code> s)</code><br />
           </td>
</tr>
<tr class="TableRowColor" data-bgcolor="white">
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>send</code></strong><code>(</code><code>OutputStream</code><code> out, int command, </code><code>String</code><code>... data)</code><br />
           </td>
</tr>
</tbody>
</table>

 

| **Methods inherited from class java.lang.Object** |
|----|
| `clone``, ``equals``, ``finalize``, ``getClass``, ``hashCode``, ``notify``, ``notifyAll``, ``toString``, ``wait``, ``wait``, ``wait` |

 

| **Field Detail** |
|------------------|

### LOCK_TIMEOUT

    public static final int LOCK_TIMEOUT

**See Also:**  
Constant Field Values

### NEW_KEY_TIMEOUT_SECONDS

    public static final int NEW_KEY_TIMEOUT_SECONDS

**See Also:**  
Constant Field Values

### EXPIRE_KEYS_TIMEOUT_SECONDS

    public static final int EXPIRE_KEYS_TIMEOUT_SECONDS

**See Also:**  
Constant Field Values

### MAX_TIME_TRAVEL_SECONDS

    public static final int MAX_TIME_TRAVEL_SECONDS

**See Also:**  
Constant Field Values

### COOKIE_TIMEOUT

    public static final int COOKIE_TIMEOUT

**See Also:**  
Constant Field Values

### COOKIE_CONTEXT

    public static final String COOKIE_CONTEXT

**See Also:**  
Constant Field Values

### MODE_SERVER

    public static final int MODE_SERVER

**See Also:**  
Constant Field Values

### MODE_CLIENT

    public static final int MODE_CLIENT

**See Also:**  
Constant Field Values

### AUTH_NONE

    public static final int AUTH_NONE

**See Also:**  
Constant Field Values

### AUTH_EXTERNAL

    public static final int AUTH_EXTERNAL

**See Also:**  
Constant Field Values

### AUTH_SHA

    public static final int AUTH_SHA

**See Also:**  
Constant Field Values

### AUTH_ANON

    public static final int AUTH_ANON

**See Also:**  
Constant Field Values

### COMMAND_AUTH

    public static final int COMMAND_AUTH

**See Also:**  
Constant Field Values

### COMMAND_DATA

    public static final int COMMAND_DATA

**See Also:**  
Constant Field Values

### COMMAND_REJECTED

    public static final int COMMAND_REJECTED

**See Also:**  
Constant Field Values

### COMMAND_OK

    public static final int COMMAND_OK

**See Also:**  
Constant Field Values

### COMMAND_BEGIN

    public static final int COMMAND_BEGIN

**See Also:**  
Constant Field Values

### COMMAND_CANCEL

    public static final int COMMAND_CANCEL

**See Also:**  
Constant Field Values

### COMMAND_ERROR

    public static final int COMMAND_ERROR

**See Also:**  
Constant Field Values

### INITIAL_STATE

    public static final int INITIAL_STATE

**See Also:**  
Constant Field Values

### WAIT_DATA

    public static final int WAIT_DATA

**See Also:**  
Constant Field Values

### WAIT_OK

    public static final int WAIT_OK

**See Also:**  
Constant Field Values

### WAIT_REJECT

    public static final int WAIT_REJECT

**See Also:**  
Constant Field Values

### WAIT_AUTH

    public static final int WAIT_AUTH

**See Also:**  
Constant Field Values

### WAIT_BEGIN

    public static final int WAIT_BEGIN

**See Also:**  
Constant Field Values

### AUTHENTICATED

    public static final int AUTHENTICATED

**See Also:**  
Constant Field Values

### FAILED

    public static final int FAILED

**See Also:**  
Constant Field Values

### OK

    public static final int OK

**See Also:**  
Constant Field Values

### CONTINUE

    public static final int CONTINUE

**See Also:**  
Constant Field Values

### ERROR

    public static final int ERROR

**See Also:**  
Constant Field Values

### REJECT

    public static final int REJECT

**See Also:**  
Constant Field Values

### challenge

    public String challenge

### cookie

    public String cookie

| **Constructor Detail** |
|------------------------|

### Transport.SASL

    public Transport.SASL()

| **Method Detail** |
|-------------------|

### receive

    public Transport.SASL.Command receive(InputStream s)
                                   throws IOException

**Throws:**  
`IOException`

### send

    public void send(OutputStream out,
                     int command,
                     String... data)
              throws IOException

**Throws:**  
`IOException`

### do_challenge

    public int do_challenge(int auth,
                            Transport.SASL.Command c)
                     throws IOException

**Throws:**  
`IOException`

### do_response

    public int do_response(int auth,
                           String Uid,
                           String kernelUid,
                           Transport.SASL.Command c)

### getTypes

    public String[] getTypes(int types)

### auth

    public boolean auth(int mode,
                        int types,
                        String guid,
                        OutputStream out,
                        InputStream in,
                        cx.ath.matthew.unix.UnixSocket us)
                 throws IOException

performs SASL auth on the given streams. Mode selects whether to run as a SASL server or client. Types is a bitmask of the available auth types. Returns true if the auth was successful and false if it failed.

**Throws:**  
`IOException`
