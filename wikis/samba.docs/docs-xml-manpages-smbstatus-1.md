# Docs Xml / Manpages / smbstatus.1

smbstatus
	 1
	 Samba
	 User Commands


smbstatus


report on current Samba connections


smbstatus

		 -p|--processes
		 -v|--verbose
		 -L|--locks
		 -S|--shares
		 -N|--notify
		 -u|--user=STRING
		 -b|--brief
		 -P|--profile
		 -R|--profile-rates
		 -B|--byterange
		 -n|--numeric
		 -f|--fast
		 -j|--json
		 --resolve-uids
		 -?|--help
		 --usage
		 -d|--debuglevel=DEBUGLEVEL
		 --debug-stdout
		 --configfile=CONFIGFILE
		 --option=name=value
		 -l|--log-basename=LOGFILEBASE
		 --leak-report
		 --leak-report-full


DESCRIPTION


This tool is part of the   samba
	 7   suite.


smbstatus
 is a very simple program to
	list the current Samba connections.


OPTIONS


-P|--profile


If samba has been compiled with the
		profiling option, print only the contents of the profiling
		shared memory area.


-R|--profile-rates


If samba has been compiled with the
		profiling option, print the contents of the profiling
		shared memory area and the call rates.


-b|--brief


gives brief output.


-v|--verbose


gives verbose output.


-L|--locks


causes smbstatus to only list locks.


-B|--byterange


causes smbstatus to include byte range locks.


-p|--processes


print a list of   smbd
		 8   processes and exit.
		Useful for scripting.


-S|--shares


causes smbstatus to only list shares.


-N|--notify


causes smbstatus to display registered file
		notifications


-f|--fast


causes smbstatus to not check if the status data
		is valid by checking if the processes that the status data refer to all still
		exist. This speeds up execution on busy systems and clusters but
		might display stale data of processes that died without cleaning up properly.


-u|--user=


selects information relevant to
username  only.


-n|--numeric


causes smbstatus to display numeric UIDs and GIDs instead of
				resolving them to names.


-j|--json


Output more detailed information in JSON format instead
				of human readable.
				The output has the following format:


{
  "timestamp": "2022-04-15T18:25:15.364891+0200",
  "version": "4.17.0pre1-GIT-a0f12b9c80b",
  "smb_conf": "/opt/samba/etc/smb.conf",
  "sessions": {
    "3639217376": {
      "session_id": "3639217376",
      "server_id": {
        "pid": "69650",
        "task_id": "0",
        "vnn": "4294967295",
        "unique_id": "10756714984493602300"
      },
      "uid": 1000,
      "gid": 1000,
      "username": "johndoe",
      "groupname": "johndoe",
      "remote_machine": "127.0.0.1",
      "hostname": "ipv4:127.0.0.1:59944",
      "session_dialect": "SMB3_11",
      "encryption": {
        "cipher": "",
        "degree": "none"
      },
      "signing": {
        "cipher": "AES-128-GMAC",
        "degree": "partial"
      }
    }
  },
  "tcons": {
    "3813255619": {
      "service": "sharename",
      "server_id": {
        "pid": "69650",
        "task_id": "0",
        "vnn": "4294967295",
        "unique_id": "10756714984493602300"
      },
      "tcon_id": "3813255619",
      "session_id": "3639217376",
      "machine": "127.0.0.1",
      "connected_at": "2022-04-15T17:30:37+0200",
      "encryption": {
        "cipher": "AES-128-GMAC",
        "degree": "full"
      },
      "signing": {
        "cipher": "",
        "degree": "none"
      }
    }
  },
  "open_files": {
    "/home/johndoe/testfolder/sample": {
      "service_path": "/home/johndoe/testfolder",
      "filename": "sample",
      "fileid": {
        "devid": 59,
        "inode": 11404245,
        "extid": 0
      },
      "num_pending_deletes": 0,
      "opens": {
        "56839/2": {
          "server_id": {
            "pid": "69650",
            "task_id": "0",
            "vnn": "4294967295",
            "unique_id": "10756714984493602300"
          },
          "uid": 1000,
          "share_file_id": 2,
          "sharemode": {
            "hex": "0x00000003",
            "NONE": false,
            "READ": true,
            "WRITE": true,
            "DELETE": false,
            "text": "RW"
          },
          "access_mask": {
            "hex": "0x00000003",
            "READ_DATA": true,
            "WRITE_DATA": true,
            "APPEND_DATA": false,
            "READ_EA": false,
            "WRITE_EA": false,
            "EXECUTE": false,
            "READ_ATTRIBUTES": false,
            "WRITE_ATTRIBUTES": false,
            "DELETE_CHILD": false,
            "DELETE": false,
            "READ_CONTROL": false,
            "WRITE_DAC": false,
            "SYNCHRONIZE": false,
            "ACCESS_SYSTEM_SECURITY": false,
            "text": "RW"
          },
          "caching": {
            "READ": false,
            "WRITE": false,
            "HANDLE": false,
            "hex": "0x00000000",
            "text": ""
          },
          "oplock": {},
          "lease": {},
          "opened_at": "2022-04-15T17:30:38+0200"
        }
      }
    }
  }
}


If oplocks are used:


          "oplock": {
            "EXCLUSIVE": false,
            "BATCH": false,
            "LEVEL_II": true,
            "LEASE": false,
            "text": "LEVEL_II"
          }


If leases are used:


          "lease": {
            "lease_key": "29316055-f55c-de10-c813-af7bf5a430bb",
            "hex": "0x00000005",
            "READ": true,
            "WRITE": true,
            "HANDLE": false,
            "text": "RW"
          }


With byte-range locks (-B, --byterange):


  "byte_range_locks": {
    "/home/johndoe/testfolder/sample": {
      "fileid": {
        "devid": 59,
        "inode": 11404245,
        "extid": 0
      },
      "file_name": "sample",
      "share_path": "/home/johndoe/testfolder",
      "locks": [
        {
          "server_id": {
            "pid": "69650",
            "task_id": "0",
            "vnn": "4294967295",
            "unique_id": "10756714984493602300"
          },
          "type": "R",
          "flavour": "Posix",
          "start": 0,
          "size": 16
        }
      ]
    }


 With notifies (-N, --notify):


  "notify": {
    "77247": {
      "server_id": {
        "pid": "69650",
        "task_id": "0",
        "vnn": "4294967295",
        "unique_id": "10756714984493602300"
      },
      "path": "/home/johndoe/testfolder/testdir",
      "filter": 4095,
      "subdir_filter": 4095,
      "creation_time": "1970-01-01T01:00:14.326582+01:00"
    }
  }


 For profiling (-P, --profile):


{
  "timestamp": "2022-04-15T18:40:43.112216+0200",
  "version": "4.17.0pre1-GIT-a0f12b9c80b",
  "smb_conf": "/opt/samba/etc/smb.conf",
  "SMBD loop": {
    "connect": {
      "count": 2
    },
    "disconnect": {
      "count": 1
    },
    ...
  },
  "System Calls": {
    "syscall_opendir": {
      "count": 0,
      "time": 0
    },
    ...
  },
  "ACL Calls": {
    "get_nt_acl": {
      "count": 0,
      "time": 0
    },
    ...
  },
  "Stat Cache": {
    "statcache_lookups": {
      "count": 2
    },
    ...
  },
  "SMB Calls": {
    "SMBmkdir": {
      "count": 0,
      "time": 0
    },
    ...
  },
  "Trans2 Calls": {
    "Trans2_open": {
      "count": 0,
      "time": 0
    },
    ...
  },
  "NT Transact Calls": {
    "NT_transact_create": {
      "count": 0,
      "time": 0
    },
    ...
  },
  "SMB2 Calls": {
    "smb2_negprot": {
      "count": 2,
      "time": 3060,
      "idle": 0,
      "inbytes": 452,
      "outbytes": 568
    },
    ...
  }
}


VERSION


This man page is part of version  of
	the Samba suite.


SEE ALSO


  smbd
	 8   and   smb.conf
	 5  .


AUTHOR


The original Samba software and related utilities
	were created by Andrew Tridgell. Samba is now developed
	by the Samba Team as an Open Source project similar
	to the way the Linux kernel is developed.
