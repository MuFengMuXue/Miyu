# Request

## Description

Shared request interface

The Request interface is shared by all portal backend interfaces. When a backend method is called, the backend exports a Request object on the object path that was sent with the method call. The Request will stay alive for the duration of the user interaction related to the method call.

The portal can abort the interaction calling [org.freedesktop.impl.portal.Request.Close](#org-freedesktop-impl-portal-request-close) on the Request object.

## Methods

### org.freedesktop.impl.portal.Request.Close

    Close ()

Ends the user interaction to which this object refers. Dialogs and other UIs related to the request should be closed.
