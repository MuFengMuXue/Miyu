\[next\] \[prev\] \[prev-tail\] \[tail\] \[up\]

### 2  DBusConnection

The DBusConnection<sup>4</sup> class provides methods for connecting to the bus, exporting objects, sending signals and getting references to remote objects.

DBusConnection is a singleton class, multiple calls to getConnection will return the same bus connection.

conn = DBusConnection.getConnection(DBusConnection.SESSION);

This creates a connection to the session bus, or returns the existing connection.

conn.addSigHandler(TestSignalInterface.TestSignal.class,    
                   new SignalHandler());

This sets up a signal handler for the given signal type. SignalHandler.handle will be called in a new thread with an instance of TestSignalInterface.TestSignal when that signal is recieved.

conn.sendSignal(new TestSignalInterface.TestSignal(    
                     "/foo/bar/com/Wibble",    
                     "Bar",    
                     new UInt32(42)));

This sends a signal of type TestSignalInterface.TestSignal, from the object “/foo/bar/com/Wibble” with the arguments “Bar” and UInt32(42).

conn.exportObject("/Test", new testclass());

This exports the testclass object on the path “/Test”

Introspectable intro = (Introspectable) conn.getRemoteObject(    
                              "foo.bar.Test", "/Test",    
                              Introspectable.class);

This gets a reference to the “/Test” object on the process with the name “foo.bar.Test” . The object implements the Introspectable interface, and calls may be made to methods in that interface as if it was a local object.

String data = intro.Introspect();

The Runtime Exception DBusExecutionException may be thrown by any remote method if any part of the execution fails.

#### 2.1  Asynchronous Calls

Calling a method on a remote object is synchronous, that is the thread will block until it has a reply. If you do not want to block you can use an asynchronous call.

There are two ways of making asynchronous calls. You can either call the callMethodAsync function on the connection object, in which case you are returned a DBusAsyncReply<sup>5</sup> object which can be used to check for a reply and get the return value. This is demonstrated in figure 1.

<table class="figure">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="figure">
<td class="figure">DBusAsyncReply&lt;Boolean&gt; stuffreply =  <br />
   conn.callMethodAsync(remoteObject, "methodname", arg1, arg2);  <br />
...  <br />
if (stuffreply.hasReply()) {  <br />
   Boolean b = stuffreply.getReply();  <br />
   ...  <br />
}
<br />
&#10;<table class="caption">
<tbody>
<tr class="caption" style="vertical-align:baseline;">
<td class="id">Figure 1:</td>
<td class="content">Calling an asynchronous method</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

Alternatively, you can register a callback with the connection using the callWithCallback function on the connection object. In this case, your callback class (implementing the CallbackHandler<sup>6</sup> interface will be called when the reply is returned from the bus.

\[next\] \[prev\] \[prev-tail\] \[front\] \[up\]
