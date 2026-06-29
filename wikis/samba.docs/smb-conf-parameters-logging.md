# smb.conf Parameters / logging

### `debug class`

Section: logging; Context: G; Type: boolean; Default: `no`

With this boolean parameter enabled, the debug class (DBGC_CLASS) will be displayed in the debug header. For more information about currently available debug classes, see section about .

### `debug hires timestamp`

Section: logging; Context: G; Type: boolean; Default: `yes`

Sometimes the timestamps in the log messages are needed with a resolution of higher that seconds, this boolean parameter adds microsecond resolution to the timestamp message header when turned on. Note that the parameter or must be on for this to have an effect.

### `debug pid`

Section: logging; Context: G; Type: boolean; Default: `no`

When using only one log file for more then one forked smbd 8 -process there may be hard to follow which process outputs which message. This boolean parameter is adds the process-id to the timestamp message headers in the logfile when turned on. Note that the parameter must be on for this to have an effect.

### `debug prefix timestamp`

Section: logging; Context: G; Type: boolean; Default: `no`

With this option enabled, the timestamp message header is prefixed to the debug message without the filename and function information that is included with the parameter. This gives timestamps to the messages without adding an additional line. Note that this parameter overrides the parameter.

### `debug syslog format`

Section: logging; Context: G; Type: enum; Default: `no`

With this option enabled ( yes (alias in_logs ) or always ), debug messages are printed in a single-line format like that traditionally produced by syslog. The timestamp consists of an abbreviated month, space-padded date, and time including seconds. This is followed by the hostname and the program name, with the process-ID in square brackets. The value always produces this log format even to STDOUT or STDERR The value no defers to other parameters and typically produces traditional two-line Samba logs to log files. If is also enabled then an RFC5424 timestamp is used instead.

### `winbind debug traceid`

Section: logging; Context: G; Type: boolean; Default: `yes`

With this boolean parameter enabled, the per request unique traceid will be displayed in the debug header for winbind processes.

### `debug uid`

Section: logging; Context: G; Type: boolean; Default: `no`

Samba is sometimes run as root and sometime run as the connected user, this boolean parameter inserts the current euid, egid, uid and gid to the timestamp message headers in the log file if turned on. Note that the parameter must be on for this to have an effect.

### `ldap debug level`

Section: logging; Context: G; Type: integer; Default: `0`

This parameter controls the debug level of the LDAP library calls. In the case of OpenLDAP, it is the same bit-field as understood by the server and documented in the slapd.conf 5 manpage. A typical useful value will be 1 for tracing function calls. The debug output from the LDAP libraries appears with the prefix [LDAP] in Samba's logging output. The level at which LDAP logging is printed is controlled by the parameter ldap debug threshold .

### `ldap debug threshold`

Section: logging; Context: G; Type: integer; Default: `10`

This parameter controls the Samba debug level at which the ldap library debug output is printed in the Samba logs. See the description of ldap debug level for details.

### `log file`

Section: logging; Context: G; Type: string

This option allows you to override the name of the Samba log file (also known as the debug file). This option takes the standard substitutions, allowing you to have separate log files for each user or machine.

### `logging`

Section: logging; Context: G; Type: string

This parameter configures logging backends. Multiple backends can be specified at the same time, with different log levels for each backend. The parameter is a list of backends, where each backend is specified as backend[:option][@loglevel]. The 'option' parameter can be used to pass backend-specific options. The log level for a backend is optional, if it is not set for a backend, all messages are sent to this backend. The parameter determines overall log levels, while the log levels specified here define what is sent to the individual backends. When is set, it overrides the and parameters. Some backends are only available when Samba has been compiled with the additional libraries. The overall list of logging backends: syslog file systemd lttng gpfs ringbuf The ringbuf backend supports an optional size argument to change the buffer size used, the default is 1 MB: ringbuf:size=NBYTES

### `log level`

Section: logging; Context: G; Type: string; Default: `0`

The value of the parameter (a string) allows the debug level (logging level) to be specified in the smb.conf file. This parameter has been extended since the 2.2.x series, now it allows one to specify the debug level for multiple debug classes and distinct logfiles for debug classes. This is to give greater flexibility in the configuration of the system. The following debug classes are currently implemented: all tdb printdrivers lanman smb rpc_parse rpc_srv rpc_cli passdb sam auth winbind vfs idmap quota acls locking msdfs dmapi registry scavenger dns ldb tevent auth_audit auth_json_audit kerberos drs_repl smb2 smb2_credits dsdb_audit dsdb_json_audit dsdb_password_audit dsdb_password_json_audit dsdb_transaction_audit dsdb_transaction_json_audit dsdb_group_audit dsdb_group_json_audit ldapsrv Various modules register dynamic debug classes at first usage: catia dfs_samba4 extd_audit fileid fruit full_audit media_harmony preopen recycle shadow_copy shadow_copy unityed_media virusfilter To configure the logging for specific classes to go into a different file then , you can append @PATH to the class, eg log level = 1 full_audit:1@/var/log/audit.log . Authentication and authorization audit information is logged under the auth_audit , and if Samba was not compiled with --without-json, a JSON representation is logged under auth_json_audit . Support is comprehensive for all authentication and authorisation of user accounts in the Samba Active Directory Domain Controller, as well as the implicit authentication in password changes. In the file server, NTLM authentication, SMB and RPC authorization is covered. Log levels for auth_audit and auth_audit_json are: 2: Authentication Failure 3: Authentication Success 4: Authorization Success 5: Anonymous Authentication and Authorization Success Changes to the AD DC sam.ldb database are logged under the dsdb_audit and a JSON representation is logged under dsdb_json_audit . Group membership changes to the AD DC sam.ldb database are logged under the dsdb_group_audit and a JSON representation is logged under dsdb_group_json_audit . Log levels for dsdb_audit , dsdb_json_audit , dsdb_group_audit , dsdb_group_json_audit and dsdb_json_audit are: 5: Database modifications 5: Replicated updates from another DC In the AD DC, password changes, password resets, and certain authentication related attribute changes are logged under dsdb_password_audit and a JSON representation is logged under the dsdb_password_json_audit . Password changes will also appears as authentication events via auth_audit and auth_audit_json . Log levels for dsdb_password_audit and dsdb_password_json_audit are: 5: Successful password changes and resets, and authentication related attribute changes. Changes to the following attributes are logged: altSecurityIdentities dNSHostName msDS-AdditionalDnsHostName msDS-KeyCredentialLink servicePrincipalName In the dsdb_password_json_audit log these are given the value "Auth info change" in the "action" field. Password changes and resets have the value "change" and "reset" in this field, respectively. Transaction rollbacks and prepare commit failures are logged under the dsdb_transaction_audit and a JSON representation is logged under the dsdb_transaction_json_audit . Log levels for dsdb_transaction_audit and dsdb_transaction_json are: 5: Transaction failure (rollback) 10: Transaction success (commit) Transaction roll-backs are possible in Samba, and whilst they rarely reflect anything more than the failure of an individual operation (say due to the add of a conflicting record), they are possible. Audit logs are already generated and sent to the system logs before the transaction is complete. Logging the transaction details allows the identification of password and sam.ldb operations that have been rolled back, and so have not actually persisted. Changes to sam.ldb made locally by the root user with direct access to the database are not logged to the system logs, but to the administrator's own console. While less than ideal, any user able to make such modifications could disable the audit logging in any case.

### `max log size`

Section: logging; Context: G; Type: bytes; Default: `5000`

This option (an integer in kilobytes) specifies the max size the log file should grow to. Samba periodically checks the size and if it is exceeded it will rename the file, adding a .old extension. A size of 0 means no limit.

### `syslog`

Section: logging; Context: G; Type: integer; Default: `1`

This parameter maps how Samba debug messages are logged onto the system syslog logging levels. Samba debug level zero maps onto syslog LOG_ERR , debug level one maps onto LOG_WARNING , debug level two maps onto LOG_NOTICE , debug level three maps onto LOG_INFO. All higher levels are mapped to LOG_DEBUG . This parameter sets the threshold for sending messages to syslog. Only messages with debug level less than this value will be sent to syslog. There still will be some logging to log.[sn]mbd even if syslog only is enabled. The parameter should be used instead. When is set, it overrides the parameter.

### `syslog only`

Section: logging; Context: G; Type: boolean; Default: `no`

If this parameter is set then Samba debug messages are logged into the system syslog only, and not to the debug log files. There still will be some logging to log.[sn]mbd even if syslog only is enabled. The parameter should be used instead. When is set, it overrides the parameter.

### `timestamp logs`

Section: logging; Context: G; Type: boolean; Default: `yes`

Samba debug log messages are timestamped by default. If you are running at a high these timestamps can be distracting. This boolean parameter allows timestamping to be turned off.
