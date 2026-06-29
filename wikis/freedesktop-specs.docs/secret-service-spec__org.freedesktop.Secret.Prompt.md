## `org.freedesktop.Secret.Prompt`

org.freedesktop.Secret.Prompt — A prompt necessary to complete an operation.

## Synopsis

### Methods

|                     |                           |
|---------------------|---------------------------|
| ` `**`Prompt`**` (` | IN String `window-id``)`; |

 

|                      |          |     |
|----------------------|----------|-----|
| ` `**`Dismiss`**` (` | `void)`; |     |

 

### Signals

|                        |                          |
|------------------------|--------------------------|
| ` `**`Completed`**` (` | OUT Boolean `dismissed`, |
|                        | OUT Variant `result``)`; |

 

## Methods

### `org.freedesktop.Secret.Prompt.Prompt`

|                     |                           |
|---------------------|---------------------------|
| ` `**`Prompt`**` (` | IN String `window-id``)`; |

 

Perform the prompt.

`window-id`  
Platform specific window handle to use for showing the prompt.

### `org.freedesktop.Secret.Prompt.Dismiss`

|                      |          |     |
|----------------------|----------|-----|
| ` `**`Dismiss`**` (` | `void)`; |     |

 

Dismiss the prompt.

## Signals

### `org.freedesktop.Secret.Prompt.Completed`

|                        |                          |
|------------------------|--------------------------|
| ` `**`Completed`**` (` | OUT Boolean `dismissed`, |
|                        | OUT Variant `result``)`; |

 

The prompt and operation completed.

`dismissed`  
Whether the prompt and operation were dismissed or not.

`result`  
The possibly empty, operation specific, result.
