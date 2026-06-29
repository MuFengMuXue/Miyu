# ext_data_control_v1

## control data devices

This protocol allows a privileged client to control data devices. In particular, the client will be able to manage the current selection and take the role of a clipboard manager. Warning! The protocol described in this file is currently in the testing phase. Backward compatible changes may be added together with the corresponding interface version bump. Backward incompatible changes can only be done by creating a new major version of the extension.

## Interface `ext_data_control_manager_v1` version 1

manager to control data devices

This interface is a manager that allows creating per-seat data device controls.

### Requests

- `create_data_source`: create a new data source
  Create a new data source.
  Arguments: `id` (new_id) - data source to create
- `get_data_device`: get a data device for a seat
  Create a data device that can be used to manage a seat's selection.
  Arguments: `id` (new_id); `seat` (object)
- `destroy`: destroy the manager
  All objects created by the manager will still remain valid, until their appropriate destroy request has been called.

## Interface `ext_data_control_device_v1` version 1

manage a data device for a seat

This interface allows a client to manage a seat's selection. When the seat is destroyed, this object becomes inert.

### Requests

- `set_selection`: copy data to the selection
  This request asks the compositor to set the selection to the data from the source on behalf of the client. The given source may not be used in any further set_selection or set_primary_selection requests. Attempting to use a previously used source triggers the used_source protocol error. To unset the selection, set the source to NULL.
  Arguments: `source` (object)
- `destroy`: destroy this data device
  Destroys the data device object.
- `set_primary_selection`: copy data to the primary selection
  This request asks the compositor to set the primary selection to the data from the source on behalf of the client. The given source may not be used in any further set_selection or set_primary_selection requests. Attempting to use a previously used source triggers the used_source protocol error. To unset the primary selection, set the source to NULL. The compositor will ignore this request if it does not support primary selection.
  Arguments: `source` (object)

### Events

- `data_offer`: introduce a new ext_data_control_offer
  The data_offer event introduces a new ext_data_control_offer object, which will subsequently be used in either the ext_data_control_device.selection event (for the regular clipboard selections) or the ext_data_control_device.primary_selection event (for the primary clipboard selections). Immediately following the ext_data_control_device.data_offer event, the new data_offer object will send out ext_data_control_offer.offer events to describe the MIME types it offers.
  Arguments: `id` (new_id)
- `selection`: advertise new selection
  The selection event is sent out to notify the client of a new ext_data_control_offer for the selection for this device. The ext_data_control_device.data_offer and the ext_data_control_offer.offer events are sent out immediately before this event to introduce the data offer object. The selection event is sent to a client when a new selection is set. The ext_data_control_offer is valid until a new ext_data_control_offer or NULL is received. The client must destroy the previous selection ext_data_control_offer, if any, upon receiving this event. Regardless, the previous selection will be ignored once a new selection ext_data_control_offer is received. The first selection event is sent upon binding the ext_data_control_device object.
  Arguments: `id` (object)
- `finished`: this data control is no longer valid
  This data control object is no longer valid and should be destroyed by the client.
- `primary_selection`: advertise new primary selection
  The primary_selection event is sent out to notify the client of a new ext_data_control_offer for the primary selection for this device. The ext_data_control_device.data_offer and the ext_data_control_offer.offer events are sent out immediately before this event to introduce the data offer object. The primary_selection event is sent to a client when a new primary selection is set. The ext_data_control_offer is valid until a new ext_data_control_offer or NULL is received. The client must destroy the previous primary selection ext_data_control_offer, if any, upon receiving this event. Regardless, the previous primary selection will be ignored once a new primary selection ext_data_control_offer is received. If the compositor supports primary selection, the first primary_selection event is sent upon binding the ext_data_control_device object.
  Arguments: `id` (object)

### Enums

- `error`

## Interface `ext_data_control_source_v1` version 1

offer to transfer data

The ext_data_control_source object is the source side of a ext_data_control_offer. It is created by the source client in a data transfer and provides a way to describe the offered data and a way to respond to requests to transfer the data.

### Requests

- `offer`: add an offered MIME type
  This request adds a MIME type to the set of MIME types advertised to targets. Can be called several times to offer multiple types. Calling this after ext_data_control_device.set_selection is a protocol error.
  Arguments: `mime_type` (string) - MIME type offered by the data source
- `destroy`: destroy this source
  Destroys the data source object.

### Events

- `send`: send the data
  Request for data from the client. Send the data as the specified MIME type over the passed file descriptor, then close it.
  Arguments: `mime_type` (string) - MIME type for the data; `fd` (fd) - file descriptor for the data
- `cancelled`: selection was cancelled
  This data source is no longer valid. The data source has been replaced by another data source. The client should clean up and destroy this data source.

### Enums

- `error`

## Interface `ext_data_control_offer_v1` version 1

offer to transfer data

A ext_data_control_offer represents a piece of data offered for transfer by another client (the source client). The offer describes the different MIME types that the data can be converted to and provides the mechanism for transferring the data directly from the source client.

### Requests

- `receive`: request that the data is transferred
  To transfer the offered data, the client issues this request and indicates the MIME type it wants to receive. The transfer happens through the passed file descriptor (typically created with the pipe system call). The source client writes the data in the MIME type representation requested and then closes the file descriptor. The receiving client reads from the read end of the pipe until EOF and then closes its end, at which point the transfer is complete. This request may happen multiple times for different MIME types.
  Arguments: `mime_type` (string) - MIME type desired by receiver; `fd` (fd) - file descriptor for data transfer
- `destroy`: destroy this offer
  Destroys the data offer object.

### Events

- `offer`: advertise offered MIME type
  Sent immediately after creating the ext_data_control_offer object. One event per offered MIME type.
  Arguments: `mime_type` (string) - offered MIME type
