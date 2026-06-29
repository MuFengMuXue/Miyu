# input_method_unstable_v1

## Interface `zwp_input_method_context_v1` version 1

input method context

Corresponds to a text input on the input method side. An input method context is created on text input activation on the input method side. It allows receiving information about the text input from the application via events. Input method contexts do not keep state after deactivation and should be destroyed after deactivation is handled. Text is generally UTF-8 encoded, indices and lengths are in bytes. Serials are used to synchronize the state between the text input and an input method. New serials are sent by the text input in the commit_state request and are used by the input method to indicate the known text input state in events like preedit_string, commit_string, and keysym. The text input can then ignore events from the input method which are based on an outdated state (for example after a reset). Warning! The protocol described in this file is experimental and backward incompatible changes may be made. Backward compatible changes may be added together with the corresponding interface version bump. Backward incompatible changes are done by bumping the version number in the protocol and interface names and resetting the interface version. Once the protocol is to be declared stable, the 'z' prefix and the version number in the protocol and interface names are removed and the interface version number is reset.

### Requests

- `destroy`
- `commit_string`: commit string
  Send the commit string text for insertion to the application. The text to commit could be either just a single character after a key press or the result of some composing (pre-edit). It could be also an empty text when some text should be removed (see delete_surrounding_text) or when the input cursor should be moved (see cursor_position). Any previously set composing text will be removed.
  Arguments: `serial` (uint) - serial of the latest known text input state; `text` (string)
- `preedit_string`: pre-edit string
  Send the pre-edit string text to the application text input. The commit text can be used to replace the pre-edit text on reset (for example on unfocus). Previously sent preedit_style and preedit_cursor requests are also processed by the text_input.
  Arguments: `serial` (uint) - serial of the latest known text input state; `text` (string); `commit` (string)
- `preedit_styling`: pre-edit styling
  Set the styling information on composing text. The style is applied for length in bytes from index relative to the beginning of the composing text (as byte offset). Multiple styles can be applied to a composing text. This request should be sent before sending a preedit_string request.
  Arguments: `index` (uint); `length` (uint); `style` (uint)
- `preedit_cursor`: pre-edit cursor
  Set the cursor position inside the composing text (as byte offset) relative to the start of the composing text. When index is negative no cursor should be displayed. This request should be sent before sending a preedit_string request.
  Arguments: `index` (int)
- `delete_surrounding_text`: delete text
  Remove the surrounding text. This request will be handled on the text_input side directly following a commit_string request.
  Arguments: `index` (int); `length` (uint)
- `cursor_position`: set cursor to a new position
  Set the cursor and anchor to a new position. Index is the new cursor position in bytes (when >= 0 this is relative to the end of the inserted text, otherwise it is relative to the beginning of the inserted text). Anchor is the new anchor position in bytes (when >= 0 this is relative to the end of the inserted text, otherwise it is relative to the beginning of the inserted text). When there should be no selected text, anchor should be the same as index. This request will be handled on the text_input side directly following a commit_string request.
  Arguments: `index` (int); `anchor` (int)
- `modifiers_map`
  Arguments: `map` (array)
- `keysym`: keysym
  Notify when a key event was sent. Key events should not be used for normal text input operations, which should be done with commit_string, delete_surrounding_text, etc. The key event follows the wl_keyboard key event convention. Sym is an XKB keysym, state is a wl_keyboard key_state.
  Arguments: `serial` (uint) - serial of the latest known text input state; `time` (uint); `sym` (uint); `state` (uint); `modifiers` (uint)
- `grab_keyboard`: grab hardware keyboard
  Allow an input method to receive hardware keyboard input and process key events to generate text events (with pre-edit) over the wire. This allows input methods which compose multiple key events for inputting text like it is done for CJK languages.
  Arguments: `keyboard` (new_id)
- `key`: forward key event
  Forward a wl_keyboard::key event to the client that was not processed by the input method itself. Should be used when filtering key events with grab_keyboard. The arguments should be the ones from the wl_keyboard::key event. For generating custom key events use the keysym request instead.
  Arguments: `serial` (uint) - serial from wl_keyboard::key; `time` (uint) - time from wl_keyboard::key; `key` (uint) - key from wl_keyboard::key; `state` (uint) - state from wl_keyboard::key
- `modifiers`: forward modifiers event
  Forward a wl_keyboard::modifiers event to the client that was not processed by the input method itself. Should be used when filtering key events with grab_keyboard. The arguments should be the ones from the wl_keyboard::modifiers event.
  Arguments: `serial` (uint) - serial from wl_keyboard::modifiers; `mods_depressed` (uint) - mods_depressed from wl_keyboard::modifiers; `mods_latched` (uint) - mods_latched from wl_keyboard::modifiers; `mods_locked` (uint) - mods_locked from wl_keyboard::modifiers; `group` (uint) - group from wl_keyboard::modifiers
- `language`
  Arguments: `serial` (uint) - serial of the latest known text input state; `language` (string)
- `text_direction`
  Arguments: `serial` (uint) - serial of the latest known text input state; `direction` (uint)

### Events

- `surrounding_text`: surrounding text event
  The plain surrounding text around the input position. Cursor is the position in bytes within the surrounding text relative to the beginning of the text. Anchor is the position in bytes of the selection anchor within the surrounding text relative to the beginning of the text. If there is no selected text then anchor is the same as cursor.
  Arguments: `text` (string); `cursor` (uint); `anchor` (uint)
- `reset`
- `content_type`
  Arguments: `hint` (uint); `purpose` (uint)
- `invoke_action`
  Arguments: `button` (uint); `index` (uint)
- `commit_state`
  Arguments: `serial` (uint) - serial of text input state
- `preferred_language`
  Arguments: `language` (string)

## Interface `zwp_input_method_v1` version 1

input method

An input method object is responsible for composing text in response to input from hardware or virtual keyboards. There is one input method object per seat. On activate there is a new input method context object created which allows the input method to communicate with the text input.

### Events

- `activate`: activate event
  A text input was activated. Creates an input method context object which allows communication with the text input.
  Arguments: `id` (new_id)
- `deactivate`: deactivate event
  The text input corresponding to the context argument was deactivated. The input method context should be destroyed after deactivation is handled.
  Arguments: `context` (object)

## Interface `zwp_input_panel_v1` version 1

interface for implementing keyboards

Only one client can bind this interface at a time.

### Requests

- `get_input_panel_surface`
  Arguments: `id` (new_id); `surface` (object)

## Interface `zwp_input_panel_surface_v1` version 1

### Requests

- `set_toplevel`: set the surface type as a keyboard
  Set the input_panel_surface type to keyboard. A keyboard surface is only shown when a text input is active.
  Arguments: `output` (object); `position` (uint)
- `set_overlay_panel`: set the surface type as an overlay panel
  Set the input_panel_surface to be an overlay panel. This is shown near the input cursor above the application window when a text input is active.

### Enums

- `position`
