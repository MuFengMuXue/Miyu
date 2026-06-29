# Game Mode

## Description

Portal for accessing GameMode

Interface for accessing GameMode from within the sandbox. It is analogous to the com.feralinteractive.GameMode interface and will proxy request there, but with additional permission checking and pid mapping. The latter is necessary in the case that sandbox has pid namespace isolation enabled. See the man page for pid_namespaces(7) for more details, but briefly, it means that the sandbox has its own process id namespace which is separated from the one on the host. Thus there will be two separate process ids (PID) within two different namespaces that both identify same process. One id from the PID namespace inside the sandbox and one id from the host PID namespace. Since org.freedesktop.portal.GameMode expects pids from the host PID namespace but programs inside the sandbox can only know PID from the sandbox namespace, process ids need to be translated from the portal to the host namespace. The portal will do that transparently for all calls where this is necessary.

Note: [org.freedesktop.portal.GameMode](#org-freedesktop-portal-gamemode) will monitor active clients, i.e. games and other programs that have successfully called [org.freedesktop.portal.GameMode.RegisterGame](#org-freedesktop-portal-gamemode-registergame). In the event that a client terminates without a call to the [org.freedesktop.portal.GameMode.UnregisterGame](#org-freedesktop-portal-gamemode-unregistergame) method, GameMode will automatically un-register the client. This might happen with a (small) delay.

This documentation describes version 4 of this interface.

## Properties

### org.freedesktop.portal.GameMode:Active

    Active readable b

Whether any pid on the system has enabled Game Mode.

### org.freedesktop.portal.GameMode:version

    version readable u

## Methods

### org.freedesktop.portal.GameMode.QueryStatus

    QueryStatus (
      IN pid i,
      OUT result i
    )

Query the GameMode status for a process.

If the caller is running inside a sandbox with PID namespace isolation, the `pid` will be translated to the respective host PID.

See the general introduction for details.

The `result` will be one of:

- 0 if GameMode is inactive

- 1 if GameMode is active

- 2 if GameMode is active and `pid` is registered

- -1 if the query failed inside GameMode

pid  
Process id to query the GameMode status of

result  
The GameMode status for `pid`

### org.freedesktop.portal.GameMode.RegisterGame

    RegisterGame (
      IN pid i,
      OUT result i
    )

Register a game with GameMode and thus request GameMode to be activated.

If the caller is running inside a sandbox with PID namespace isolation, the `pid` will be translated to the respective host PID.

See the general introduction for details.

If the GameMode has already been requested for `pid` before, this call will fail, i.e. result will be -1.

The `result` will be one of:

- 0 if the game with `pid` was successfully registered

- -1 if the request was rejected by GameMode

pid  
Process id of the game to register

result  
Status of the request: 0 for success, -1 indicates an error

### org.freedesktop.portal.GameMode.UnregisterGame

    UnregisterGame (
      IN pid i,
      OUT result i
    )

Un-register a game from GameMode.

If the call is successful and there are no other games or clients registered, GameMode will be deactivated.

If the caller is running inside a sandbox with PID namespace isolation, the `pid` will be translated to the respective host PID.

The `result` will be one of:

- 0 if the game with `pid` was successfully un-registered

- -1 if the request was rejected by GameMode

pid  
Process id of the game to un-register

result  
Status of the request: 0 for success, -1 indicates an error

### org.freedesktop.portal.GameMode.QueryStatusByPid

    QueryStatusByPid (
      IN target i,
      IN requester i,
      OUT result i
    )

Query the GameMode status for a process.

Like [org.freedesktop.portal.GameMode.QueryStatus](#org-freedesktop-portal-gamemode-querystatus) but `requester` acting on behalf of `target`.

target  
Process id to query the GameMode status of

requester  
Process id of the process requesting the information

result  
The GameMode status for `target`

### org.freedesktop.portal.GameMode.RegisterGameByPid

    RegisterGameByPid (
      IN target i,
      IN requester i,
      OUT result i
    )

Register a game with GameMode.

Like [org.freedesktop.portal.GameMode.RegisterGame](#org-freedesktop-portal-gamemode-registergame) but `requester` acting on behalf of `target`.

target  
Process id of the game to register

requester  
Process id of the process requesting the registration

result  
Status of the request: 0 for success, -1 indicates an error

### org.freedesktop.portal.GameMode.UnregisterGameByPid

    UnregisterGameByPid (
      IN target i,
      IN requester i,
      OUT result i
    )

Un-register a game with GameMode.

Like [org.freedesktop.portal.GameMode.UnregisterGame](#org-freedesktop-portal-gamemode-unregistergame) but `requester` acting on behalf of `target`.

target  
Process id of the game to un-register

requester  
Process id of the process requesting the un-registration

result  
Status of the request: 0 for success, -1 indicates an error

### org.freedesktop.portal.GameMode.QueryStatusByPIDFd

    QueryStatusByPIDFd (
      IN target h,
      IN requester h,
      OUT result i
    )

Query the GameMode status for a process.

Like [org.freedesktop.portal.GameMode.QueryStatusByPid](#org-freedesktop-portal-gamemode-querystatusbypid) but `requester` and `target` are pidfds representing the processes.

target  
Pidfd to query the GameMode status of

requester  
Pidfd of the process requesting the information

result  
The GameMode status for `target`

### org.freedesktop.portal.GameMode.RegisterGameByPIDFd

    RegisterGameByPIDFd (
      IN target h,
      IN requester h,
      OUT result i
    )

Register a game with GameMode.

Like [org.freedesktop.portal.GameMode.RegisterGameByPid](#org-freedesktop-portal-gamemode-registergamebypid) but `requester` and `target` are pidfds representing the processes.

target  
Pidfd of the game to register

requester  
Pidfd of the process requesting the registration

result  
Status of the request: 0 for success, -1 indicates an error

### org.freedesktop.portal.GameMode.UnregisterGameByPIDFd

    UnregisterGameByPIDFd (
      IN target h,
      IN requester h,
      OUT result i
    )

Un-register a game with GameMode.

Like [org.freedesktop.portal.GameMode.UnregisterGameByPid](#org-freedesktop-portal-gamemode-unregistergamebypid) but `requester` and `target` are pidfds representing the processes.

target  
Pidfd of the game to un-register

requester  
Pidfd of the process requesting the un-registration

result  
Status of the request: 0 for success, -1 indicates an error
