# text_input_unstable_v1

## Interface `zwp_text_input_v1` version 1

text input

An object used for text input. Adds support for text input and input methods to applications. A text_input object is created from a wl_text_input_manager and corresponds typically to a text entry in an application. Requests are used to activate/deactivate the text_input object and set state information like surrounding and selected text or the content type. The information about entered text is sent to the text_input object via the pre-edit and commit events. Using this interface removes the need for applications to directly process hardware key events and compose text out of them. Text is generally UTF-8 encoded, indices and lengths are in bytes. Serials are used to synchronize the state between the text input and an input method. New serials are sent by the text input in the commit_state request and are used by the input method to indicate the known text input state in events like preedit_string, commit_string, and keysym. The text input can then ignore events from the input method which are based on an outdated state (for example after a reset). Warning! The protocol described in this file is experimental and backward incompatible changes may be made. Backward compatible changes may be added together with the corresponding interface version bump. Backward incompatible changes are done by bumping the version number in the protocol and interface names and resetting the interface version. Once the protocol is to be declared stable, the 'z' prefix and the version number in the protocol and interface names are removed and the interface version number is reset.

### Requests

- `activate`: request activation
  Requests the text_input object to be activated (typically when the text entry gets focus). The seat argument is a wl_seat which maintains the focus for this activation. The surface argument is a wl_surface assigned to the text_input object and tracked for focus lost. The enter event is emitted on successful activation.
  Arguments: `seat` (object); `surface` (object)
- `deactivate`: request deactivation
  Requests the text_input object to be deactivated (typically when the text entry lost focus). The seat argument is a wl_seat which was used for activation.
  Arguments: `seat` (object)
- `show_input_panel`: show input panels
  Requests input panels (virtual keyboard) to show.
- `hide_input_panel`: hide input panels
  Requests input panels (virtual keyboard) to hide.
- `reset`: reset
  Should be called by an editor widget when the input state should be reset, for example after the text was changed outside of the normal input method flow.
- `set_surrounding_text`: sets the surrounding text
  Sets the plain surrounding text around the input position. Text is UTF-8 encoded. Cursor is the byte offset within the surrounding text. Anchor is the byte offset of the selection anchor within the surrounding text. If there is no selected text anchor, then it is the same as cursor.
  Arguments: `text` (string); `cursor` (uint); `anchor` (uint)
- `set_content_type`: set content purpose and hint
  Sets the content purpose and content hint. While the purpose is the basic purpose of an input field, the hint flags allow to modify some of the behavior. When no content type is explicitly set, a normal content purpose with default hints (auto completion, auto correction, auto capitalization) should be assumed.
  Arguments: `hint` (uint); `purpose` (uint)
- `set_cursor_rectangle`
  Arguments: `x` (int); `y` (int); `width` (int); `height` (int)
- `set_preferred_language`: sets preferred language
  Sets a specific language. This allows for example a virtual keyboard to show a language specific layout. The "language" argument is an RFC-3066 format language tag. It could be used for example in a word processor to indicate the language of the currently edited document or in an instant message application which tracks languages of contacts.
  Arguments: `language` (string)
- `commit_state`
  Arguments: `serial` (uint) - used to identify the known state
- `invoke_action`
  Arguments: `button` (uint); `index` (uint)

### Events

- `enter`: enter event
  Notify the text_input object when it received focus. Typically in response to an activate request.
  Arguments: `surface` (object)
- `leave`: leave event
  Notify the text_input object when it lost focus. Either in response to a deactivate request or when the assigned surface lost focus or was destroyed.
- `modifiers_map`: modifiers map
  Transfer an array of 0-terminated modifier names. The position in the array is the index of the modifier as used in the modifiers bitmask in the keysym event.
  Arguments: `map` (array)
- `input_panel_state`: state of the input panel
  Notify when the visibility state of the input panel changed.
  Arguments: `state` (uint)
- `preedit_string`: pre-edit
  Notify when a new composing text (pre-edit) should be set around the current cursor position. Any previously set composing text should be removed. The commit text can be used to replace the preedit text on reset (for example on unfocus). The text input should also handle all preedit_style and preedit_cursor events occurring directly before preedit_string.
  Arguments: `serial` (uint) - serial of the latest known text input state; `text` (string); `commit` (string)
- `preedit_styling`: pre-edit styling
  Sets styling information on composing text. The style is applied for length bytes from index relative to the beginning of the composing text (as byte offset). Multiple styles can be applied to a composing text by sending multiple preedit_styling events. This event is handled as part of a following preedit_string event.
  Arguments: `index` (uint); `length` (uint); `style` (uint)
- `preedit_cursor`: pre-edit cursor
  Sets the cursor position inside the composing text (as byte offset) relative to the start of the composing text. When index is a negative number no cursor is shown. This event is handled as part of a following preedit_string event.
  Arguments: `index` (int)
- `commit_string`: commit
  Notify when text should be inserted into the editor widget. The text to commit could be either just a single character after a key press or the result of some composing (pre-edit). It could also be an empty text when some text should be removed (see delete_surrounding_text) or when the input cursor should be moved (see cursor_position). Any previously set composing text should be removed.
  Arguments: `serial` (uint) - serial of the latest known text input state; `text` (string)
- `cursor_position`: set cursor to new position
  Notify when the cursor or anchor position should be modified. This event should be handled as part of a following commit_string event.
  Arguments: `index` (int); `anchor` (int)
- `delete_surrounding_text`: delete surrounding text
  Notify when the text around the current cursor position should be deleted. Index is relative to the current cursor (in bytes). Length is the length of deleted text (in bytes). This event should be handled as part of a following commit_string event.
  Arguments: `index` (int); `length` (uint)
- `keysym`: keysym
  Notify when a key event was sent. Key events should not be used for normal text input operations, which should be done with commit_string, delete_surrounding_text, etc. The key event follows the wl_keyboard key event convention. Sym is an XKB keysym, state a wl_keyboard key_state. Modifiers are a mask for effective modifiers (where the modifier indices are set by the modifiers_map event)
  Arguments: `serial` (uint) - serial of the latest known text input state; `time` (uint); `sym` (uint); `state` (uint); `modifiers` (uint)
- `language`: language
  Sets the language of the input text. The "language" argument is an RFC-3066 format language tag.
  Arguments: `serial` (uint) - serial of the latest known text input state; `language` (string)
- `text_direction`: text direction
  Sets the text direction of input text. It is mainly needed for showing an input cursor on the correct side of the editor when there is no input done yet and making sure neutral direction text is laid out properly.
  Arguments: `serial` (uint) - serial of the latest known text input state; `direction` (uint)

### Enums

- `content_hint`: content hint
  Content hint is a bitmask to allow to modify the behavior of the text input.
- `content_purpose`: content purpose
  The content purpose allows to specify the primary purpose of a text input. This allows an input method to show special purpose input panels with extra characters or to disallow some characters.
- `preedit_style`
- `text_direction`

## Interface `zwp_text_input_manager_v1` version 1

text input manager

A factory for text_input objects. This object is a global singleton.

### Requests

- `create_text_input`: create text input
  Creates a new text_input object.
  Arguments: `id` (new_id)
