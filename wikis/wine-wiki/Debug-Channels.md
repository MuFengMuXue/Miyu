**WINEDEBUG** is an environment variable that turns debugging messages on or off.

## Syntax

WINEDEBUG=\[\[process:\]class\]+xxx,\[\[process:\]class\]-yyy,...

**process** is optional and can be used to make the debug flag applied to only the specified process to limit output size. For example WINEDEBUG=notepad.exe:+relay only enable relay channel for notepad.exe. You can also do something like WINEDEBUG=+win,notepad.exe:-win to enable win channel for all processes but notepad.exe.

**class** is optional and can be one of the following: **trace**, **warn**, **err**, or **fixme**. These are ordered roughly from least to most severe. **trace** is used for code paths that occur as part of normal operation. **warn** is generally used for code paths that may cause failures, but are likely to be well-handled by a higher-level component. **err** is used for code paths that are likely to cause failures. **fixme** is used for code paths that are unimplemented in Wine. By default, only **err** and **fixme** are enabled. If a channel is specified without a class, all classes are enabled.

Each channel will print messages about a particular component of Wine. The following character can be either + or - to switch the specified channel on or off respectively. If there is no class part before it, a leading + can be omitted. Note that spaces are not allowed any where in the string.

**channel** specifies which debug channel to turn on or off. For complete list of channels run this command in the source directory:

```sh
$ grep -r --include='*.c' --include='*.h' 'WINE_(DEFAULT|DECLARE)_DEBUG_CHANNEL' dlls/ programs/
```

And with some more work we have sorted and formatted list in **bash** (you may want to adjust number 26 near the end of this composite to match your indentation taste):

```sh
for modname in $(find dlls/ programs/ -mindepth 1 -type d | sort); do
  echo $(grep -rE --include='*.[ch]' '^WINE_(DEFAULT|DECLARE)_DEBUG_CHANNEL' $modname \
         | awk -F "[()]" '{print $2}' | sort | uniq) \
         | awk -v modname=$modname '{if (NF>0) printf("%-*s%s\n", 26, modname": ", $0)}';
done
```

## Examples

`WINEDEBUG=warn+all` will turn on WARN messages for all channels, in addition to already enabled ERR and FIXME messages.

`WINEDEBUG=fixme-all,warn+cursor,+relay` will turn off all FIXME messages, turn on cursor WARN messages (in addition to ERR and FIXME messages), and turn on all relay messages (API calls).

`WINEDEBUG=+relay` will turn on all relay messages. For more control on including or excluding functions and dlls from the relay trace look into the `HKCU\Software\Wine\Debug` registry key (See [Useful Registry Keys](Useful-Registry-Keys) and the example below).

`WINEDEBUG=-d3d` will turn off all d3d messages, and additionally disable checking for GL errors after operations. This may improve performance.

## Useful Channels

Some of the debug channels can be particularly useful:

| Channel | Usage |
|---------|-------|
| +all | Logs everything, probably gives too much information in most cases, but may come in handy for subtle issues |
| +heap | Traces all heap activity in the program and switches on constant integrity checks. If an app is trashing the heap, doing a +relay,+heap trace will let you narrow down exactly where it's happening. If an inconsistency is detected, Wine will dump the contents of the heap and terminate the program. Although many things can lead to trashing the heap, the most common is Wine overrunning an internal buffer. Be sure to remember this channel; all Wine code uses the HeapAlloc/HeapFree APIs internally, and a primary reason is that Wine's built in heap debugging is so useful. Be warned that +heap can make a program extremely slow, and generate very large log files. If you're concerned that Wine may be corrupting the heap but are not sure, warn+heap will enable heap validation but will not trace every allocation and free. |
| +loaddll | Reports each DLL as it is loaded. |
| +module | Like +loaddll but more verbose. |
| +pid | Prefixes each debug output line with the ID of the process that generated it. This can be helpful when debugging multiprocess applications. |
| +relay | Logs every call that crosses the DLL boundary of Wine's built-in modules, including calls between (non-native) DLLs. This channel is often the first port of call when you have no idea what's going wrong. It shows you each call into and out of Wine modules at the DLL boundaries. If you're being overwhelmed by certain functions, look into setting the RelayInclude and RelayExclude strings in the Wine registry (under \[HKCU\\Software\\Wine\\Debug\]). Note that this string is already pre-populated with some functions which are frequently called but don't usually give any clues as to why a program might be failing. **Never use +relay or +snoop with native DLLs!** This will show you the implementation of those DLLs, which means that any code you write to implement them violates our clean room reverse-engineering rules. |
| +seh | Logs Windows exceptions (Structured Exception Handling). These are invoked either when an application performs an illegal operation (i.e. crashes), or if a program throws its own exceptions. Wine converts UNIX signals into SEH exceptions and outputs them using this channel. This can be useful because applications will often trap their own crash, in order to perform an emergency save for instance. The most common exception to watch for is STATUS_ACCESS_VIOLATION or **0xC0000005** which is the closest equivalent in Win32 to a segfault. You may also see codes which don't appear in the headers; these are typically language-specific exceptions used by whichever compiler was used to produce the EXE. E.g. **0xEEDFADE** is the code for a Delphi internal exception, and **0xE06D7363** is a Microsoft Visual C++ exception, which has a magic value (info\[0\]) of **0x19930520**, which is easy to remember because it looks like a date (and probably is). If you see any of these exceptions, it may mean a Win32 API call returned a non-zero error code somewhere. |
| +server | Shows each wineserver RPC. You don't normally need this but it may prove helpful when debugging wineserver issues. |
| +snoop | Logs every function call between native DLLs. This is similar to +relay but works between two native DLLs, although this channel provides poorer information because parameters aren't reported. +snoop may also break or destabilize an application as it inspects the stack and disassembles function prologues to try and guess parameters. **Never use +relay or +snoop with native DLLs!** This will show you the implementation of those DLLs, which means that any code you write to implement them violates our clean room reverse-engineering rules. (This feature may be broken and only works for i386) |
| +synchronous | Forces X11 into synchronous mode |
| +timestamp | Prefixes each debug output line with the timestamp when that line executed. This is invaluable for debugging performance issue. |
| +fps | Prints the number of frames per second in the terminal for OpenGL, D3D, or Vulkan applications. |
| +debugstr | Prints strings, sent to OutputDebugStringA and vDbgPrintExWithPrefix. |
| +threadname | Shows thread names when they are set or changed. |

## Other Debugging Tips

- If a program is displaying a message box when it fails, and you don't know what is causing the problem, try performing a +relay,+msgbox trace. Then open the debug log in your favourite editor or text viewer (less is quite good) and search for trace:msgbox. Look at the relay data before the MessageBox API call, although the problem may not be caused by a call that happens _immediately_ before the error. Keep an eye out for failing API calls in particular, and remember that there's little consistency in the Windows API as to what return codes mean. You just have to get used to what the specific API uses, and while many return non-zero for success and zero for fail, some use the opposite convention.
- If a program fails at startup with nothing to suggest why, you can use an +all trace. If your program seems to be failing a long way from an API call, you might also try [disassembling](Disassembly) it to see if it's accessing some of the parameters passed in to its entry point (for instance, Dungeon Keeper crashes if you run it without an absolute path for argv\[0\]).

### Making +relay less verbose

If you're looking for a problem that happens a couple minutes into the run of an app, +relay can be too verbose. In that case, run it once, then send the log through a script like

```sh
# Make grep go fast
LANG=C
# Find top ten calls
freq=`grep ':Ret ' | sed 's/(.*//;s/.* //' | sort | uniq -c | sort -n | tail | awk '{print $2}' | tr '\012' ';'`
cat > quiet.reg << _EOF
REGEDIT4

[HKEY_CURRENT_USER\Software\Wine\Debug]
"RelayExclude"="ntdll.RtlEnterCriticalSection;ntdll.RtlTryEnterCriticalSection;ntdll.RtlLeaveCriticalSection;kernel32.48;kernel32.49;kernel32.94;kernel32.95;kernel32.96;kernel32.97;kernel32.98;kernel32.TlsGetValue;kernel32.TlsSetValue;kernel32.FlsGetValue;kernel32.FlsSetValue;kernel32.SetLastError;$freq"

_EOF

wine regedit quiet.reg
```

This will tell Wine to not log the ten most frequent calls in your app, which should make your +relay log much more managable in size.

You can also specify process name to enable relay only for the specified process, for example: `WINEDEBUG=notepad.exe:+relay`

## See Also

- [Environment Variables: WINEDEBUG](Wine-User's-Guide#winedebug-channels) - chapter of the [Wine User's Guide](Wine-User's-Guide)
- [WineAPI documentation](https://source.winehq.org/WineAPI/) - For each function the used debug channels are listed.