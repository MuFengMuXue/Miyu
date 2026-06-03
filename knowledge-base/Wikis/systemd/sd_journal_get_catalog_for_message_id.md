## Name

sd_journal_get_catalog, sd_journal_get_catalog_for_message_id — Retrieve message catalog entry

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-journal.h>
```

|                                       |                    |
|---------------------------------------|--------------------|
| `int `**`sd_journal_get_catalog`**`(` | sd_journal \*`j`,  |
|                                       | char \*\*`ret``)`; |

 

|                                                      |                    |
|------------------------------------------------------|--------------------|
| `int `**`sd_journal_get_catalog_for_message_id`**`(` | sd_id128_t `id`,   |
|                                                      | char \*\*`ret``)`; |

 

## Description

`sd_journal_get_catalog()` retrieves a message catalog entry for the current journal entry. This will look up an entry in the message catalog by using the "`MESSAGE_ID=`" field of the current journal entry. Before returning the entry all journal field names in the catalog entry text enclosed in "@" will be replaced by the respective field values of the current entry. If a field name referenced in the message catalog entry does not exist, in the current journal entry, the "@" will be removed, but the field name otherwise left untouched.

`sd_journal_get_catalog_for_message_id()` works similar to `sd_journal_get_catalog()` but the entry is looked up by the specified message ID (no open journal context is necessary for this), and no field substitution is performed.

For more information about the journal message catalog please refer to the Journal Message Catalogs documentation page.

## Return Value

`sd_journal_get_catalog()` and `sd_journal_get_catalog_for_message_id()` return 0 on success or a negative errno-style error code. If no matching message catalog entry is found, -ENOENT is returned.

On successful return, *`ret`* points to a new string, which must be freed with free(3).

## Notes

Function `sd_journal_get_catalog()` is thread-agnostic and only a single thread may operate on a given object at any given time. Multiple independent objects may be used from different threads in parallel.

Function `sd_journal_get_catalog_for_message_id()` is thread-safe and may be called from multiple threads in parallel.

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

## History

`sd_journal_get_catalog()` and `sd_journal_get_catalog_for_message_id()` were added in version 196.

## See Also

systemd(1), systemd.journal-fields(7), sd-journal(3), sd_journal_open(3), sd_journal_next(3), sd_journal_get_data(3), malloc(3)
