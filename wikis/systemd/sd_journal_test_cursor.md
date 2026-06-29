## Name

sd_journal_get_cursor, sd_journal_test_cursor — Get cursor string for or test cursor string against the current journal entry

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-journal.h>
```

|                                      |                           |
|--------------------------------------|---------------------------|
| `int `**`sd_journal_get_cursor`**`(` | sd_journal \*`j`,         |
|                                      | char \*\*`ret_cursor``)`; |

 

|                                       |                           |
|---------------------------------------|---------------------------|
| `int `**`sd_journal_test_cursor`**`(` | sd_journal \*`j`,         |
|                                       | const char \*`cursor``)`; |

 

## Description

`sd_journal_get_cursor()` returns a cursor string for the current journal entry. A cursor is a serialization of the current journal position formatted as text. The string only contains printable characters and can be passed around in text form. The cursor identifies a journal entry globally and in a stable way and may be used to later seek to it via sd_journal_seek_cursor(3). The cursor string should be considered opaque and not be parsed by clients. Seeking to a cursor position without the specific entry being available locally will seek to the next closest (in terms of time) available entry. The call takes two arguments: a journal context object and a pointer to a string pointer where the cursor string will be placed. The string is allocated via libc malloc(3) and should be freed after use with free(3). The *`ret_cursor`* parameter may be passed as `NULL` in which case the cursor string is not generated, however the return value will indicate whether the journal context is currently positioned on an entry, and thus has a cursor associated.

`sd_journal_test_cursor()` may be used to check whether the current position in the journal matches the specified cursor. This is useful since cursor strings do not uniquely identify an entry: the same entry might be referred to by multiple different cursor strings, and hence string comparing cursors is not possible. Use this call to verify after an invocation of sd_journal_seek_cursor(3), whether the entry being sought to was actually found in the journal or the next closest entry was used instead.

Note that `sd_journal_get_cursor()` and `sd_journal_test_cursor()` will not work before sd_journal_next(3) (or one of the other functions which move to an entry) has been called at least once to position the read pointer at a valid entry.

## Return Value

`sd_journal_get_cursor()` returns 0 on success or a negative errno-style error code. `sd_journal_test_cursor()` returns positive if the current entry matches the specified cursor, 0 if it does not match the specified cursor or a negative errno-style error code on failure.

### Errors

Returned errors may indicate the following problems:

`-EADDRNOTAVAIL`  
The journal context is currently not positioned on any entry, and hence no cursor string can be generated.

`-EINVAL`  
The journal context parameter is `NULL`.

`-ECHILD`  
The journal context object has been allocated in a different process than it is being used in now.

## Notes

All functions listed here are thread-agnostic and only a single thread may operate on a given object at any given time. Different threads may access the same object at different times. Multiple independent objects may be used from different threads in parallel.

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

## History

`sd_journal_get_cursor()` was added in version 187.

`sd_journal_test_cursor()` was added in version 195.

## See Also

systemd(1), sd-journal(3), sd_journal_open(3), sd_journal_seek_cursor(3)
