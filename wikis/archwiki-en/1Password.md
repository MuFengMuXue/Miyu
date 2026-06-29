# 1Password

1Password is a password manager developed by the Canadian software company AgileBits Inc. It supports multiple platforms such as iOS, Android, Windows, Linux, and macOS. It provides a place for users to store various passwords, software licenses, and other sensitive information in a virtual vault that is locked with a PBKDF2-guarded master password. By default, the user’s encrypted vault is hosted on 1Password’s servers for a monthly fee.

## Installation
Install , and optionally for terminal based access  can be installed too.

## Tips and tricks
## Global shortcut to open the app window
In your desktop environment settings you may bind a key combination of your choice to the command , which will cause your already opened app to bring-up its window (starting itself up if not yet running).

If using KDE desktop, the current default focus stealing prevention rules will normally prevent an already opened window from bringing itself up again, if it's minimized and not closed to system tray. To correct this behavior, add a window rule for the app (setting Window class (application) to Exact match  and Focus stealing prevention to Force None). The config equivalent of the rule is:

## Troubleshooting
In general, you can increase debugging verbosity with the following:

 $ pkill -f 1password || true
 $ OP_UNREDACTED_LOGS=1 OP_LOG_LEVEL=trace 1password

## If MFA does not work
If you see experience issues with 1Password not being able to store the MFA token and stay "online", and you see similar error messages:

 INFO  Verifying device secret (MFA) with server...
 DEBUG [1P:op-b5-client/src/internal/keyed_server_connection.rs:227 Session Session ID: ABCDEFGHIJKLMNOPQRSTUVXYZA
 INFO  Device secret was verified
 TRACE [1P:foundation/op-linux/src/ipc/desktop_keyring/mod.rs:45 using kwallet fallback for this session
 WARN  Failed to save an account's 2FA token with an error of SystemKeyringError(LinuxError(DBus(MethodError(OwnedErrorName(ErrorName(Str(Owned("org.freedesktop.DBus.Error.ServiceUnknown")))), Some("The name is not activatable"), Msg { type: Error, sender: UniqueName(Str(Borrowed("org.freedesktop.DBus"))), reply-serial: 2, body: Signature("s") })))). 2FA will only be valid for this unlock session!

A most likely solution is that you are missing a wallet. For instance installing KDE Wallet by installing  and  is one way of solving the issue.

## SSH Agent not working
If you have enabled the 1Password SSH agent but the agent refuses operation when trying to use it, and you see error messages such as:

 INFO  [1P:ssh/op-agent-controller/src/lib.rs:761 SSH Agent has started.
 INFO  Starting filesystem watcher for SSH agent configuration directories...
 ERROR [1P:/mnt/ephemeral/builds/dev/core/core/ssh/op-agent-controller/src/lib.rs:578 Io(Os { code: 2, kind: NotFound, message: "No such file or directory" })

Then most likely it's the pinentry and/or policykit agent not being installed. You can fix this by installing  as well as , and after this make sure you start the lxqt policykit agent:

 $ /usr/bin/lxqt-policykit-agent &
