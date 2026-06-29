# Abduco

abduco is a lightweight utility letting programs run independently of the controlling terminal. In that matter it is similar to tmux and GNU Screen, but without multiplexing capability.

## Installation
Install the  package.

## Session management
To start  in a session named  (which may be later referenced), run

 $ abduco -c session_name command...

To detach, either press  or close the controlling terminal. In both cases the process will remain alive.

To reattach to a , run

 $ abduco -a session_name

Invoking  with no options prints the list of sessions.

## Limitations
The process started in an abduco session retains the  variable it has been invoked with. While reattaching, a compatible type of terminal must be used.

abduco does not provide multiple windows and multiplexing. If that is needed, use dvtm, tmux, or GNU Screen.
