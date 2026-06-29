## org.freedesktop.dbus Class AbstractConnection.\_thread

    java.lang.Object
      java.lang.Thread
          org.freedesktop.dbus.AbstractConnection._thread

**All Implemented Interfaces:**  
Runnable

<!-- -->

**Enclosing class:**  
AbstractConnection

<!-- -->

    protected class AbstractConnection._threadextends Thread

| **Nested Class Summary** |     |
|--------------------------|-----|

 

| **Nested classes/interfaces inherited from class java.lang.Thread** |
|---------------------------------------------------------------------|
| `Thread.State``, ``Thread.UncaughtExceptionHandler`                 |

 

| **Field Summary** |     |
|-------------------|-----|

 

| **Fields inherited from class java.lang.Thread**    |
|-----------------------------------------------------|
| `MAX_PRIORITY``, ``MIN_PRIORITY``, ``NORM_PRIORITY` |

 

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
<td><strong><code>AbstractConnection._thread</code></strong><code>()</code><br />
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
<td style="text-align: right;" data-valign="top" width="1%"><code> void</code></td>
<td><strong><code>run</code></strong><code>()</code><br />
           </td>
</tr>
</tbody>
</table>

 

| **Methods inherited from class java.lang.Thread** |
|----|
| `activeCount``, ``checkAccess``, ``countStackFrames``, ``currentThread``, ``destroy``, ``dumpStack``, ``enumerate``, ``getAllStackTraces``, ``getContextClassLoader``, ``getDefaultUncaughtExceptionHandler``, ``getId``, ``getName``, ``getPriority``, ``getStackTrace``, ``getState``, ``getThreadGroup``, ``getUncaughtExceptionHandler``, ``holdsLock``, ``interrupt``, ``interrupted``, ``isAlive``, ``isDaemon``, ``isInterrupted``, ``join``, ``join``, ``join``, ``resume``, ``setContextClassLoader``, ``setDaemon``, ``setDefaultUncaughtExceptionHandler``, ``setName``, ``setPriority``, ``setUncaughtExceptionHandler``, ``sleep``, ``sleep``, ``start``, ``stop``, ``stop``, ``suspend``, ``toString``, ``yield` |

 

| **Methods inherited from class java.lang.Object** |
|----|
| `clone``, ``equals``, ``finalize``, ``getClass``, ``hashCode``, ``notify``, ``notifyAll``, ``wait``, ``wait``, ``wait` |

 

| **Constructor Detail** |
|------------------------|

### AbstractConnection.\_thread

    public AbstractConnection._thread()

| **Method Detail** |
|-------------------|

### run

    public void run()

**Specified by:**  
`run` in interface `Runnable`

**Overrides:**  
`run` in class `Thread`
