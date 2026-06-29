**Resources**

[[]][Home](https://www.isc.org/kea/)

[[]][Official documentation](https://kea.readthedocs.io/en/latest/arm/config.html)

[[]][Package information](https://packages.gentoo.org/packages/net-misc/kea)

[[]][GitLab](https://gitlab.isc.org/isc-projects/kea)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Kea_(software) "wikipedia:Kea (software)")

**Kea** is a DHCP server developed by the Internet Systems Consortium. It is a newer (next generation) DHCP server from the same authors of ISC DHCP. Kea has several features ISC lacks, including: Modular components, JSON configuration with a REST API, data isolation, and a web based GUI.

** Note**\
The original ISC DHCP server is no longer maintained and ISC recommend moving to Kea.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [interface-config]](#interface-config)
    -   [[2.3] [subnet4]](#subnet4)
        -   [[2.3.1] [subnet]](#subnet)
        -   [[2.3.2] [pools]](#pools)
        -   [[2.3.3] [option-data]](#option-data)
        -   [[2.3.4] [Reservations]](#Reservations)
    -   [[2.4] [control-socket]](#control-socket)
    -   [[2.5] [lease-database]](#lease-database)
    -   [[2.6] [expired-leases-processing]](#expired-leases-processing)
    -   [[2.7] [loggers]](#loggers)
    -   [[2.8] [Service]](#Service)
        -   [[2.8.1] [OpenRC]](#OpenRC)
            -   [[2.8.1.1] [High Availability]](#High_Availability)
            -   [[2.8.1.2] [Starting after the logger]](#Starting_after_the_logger)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Check config]](#Check_config)
    -   [[3.2] [Hook Libraries]](#Hook_Libraries)
        -   [[3.2.1] [Run Script Support]](#Run_Script_Support)
-   [[4] [External resources]](#External_resources)
-   [[5] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [net-misc/kea](https://packages.gentoo.org/packages/net-misc/kea) [[]] [High-performance production grade DHCPv4 & DHCPv6 server]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+openssl`](https://packages.gentoo.org/useflags/+openssl)       Use dev-libs/openssl instead of dev-libs/botan
  [`debug`](https://packages.gentoo.org/useflags/debug)             Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`doc`](https://packages.gentoo.org/useflags/doc)                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`kerberos`](https://packages.gentoo.org/useflags/kerberos)       Add kerberos support
  [`mysql`](https://packages.gentoo.org/useflags/mysql)             Add interface to MySQL for lease, host reservations and/or server config
  [`postgres`](https://packages.gentoo.org/useflags/postgres)       Add interface to PostgreSQL for lease, host reservations and/or server config
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`shell`](https://packages.gentoo.org/useflags/shell)             Install kea-shell text management client for Control Agent
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-26 02:33] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask net-misc/kea`

## [Configuration]

** Note**\
Configurations in this article are represented as fragments which must be combined.

### [Files]

Kea\'s configuration files are located in [/etc/kea]:

-   [/etc/kea/kea-dhcp4.conf] - Configuration for the kea-dhcp4 daemon
-   [/etc/kea/kea-dhcp6.conf] - Configuration for the kea-dhcp6 daemon
-   [/etc/kea/kea-ddns.conf] - Configuration for the kea-ddns daemon
-   [/etc/kea/kea-ctrl-agent.conf] - Configuration for the kea-ctrl-agent daemon

Many configuration directives are similar or shared between files.

### [interface-config]

The **interface-config** directive is used to define which interfaces and IPs Kea listens on:

[FILE] **`/etc/kea/kea-dhcp4.conf`**


        }
    }

** Tip**\
Defining the IP address is unnecessary, but may be done.

** Note**\
Only the interface name must be defined, but an IP address can be specified to force Kea to only listen on that address.

### [subnet4]

IPv4 subnet configuration in Kea is relatively straightforward. Each structure in this list must contain a **subnet**. In most cases, **pools** and **option-data** are also defined. **reservations** allow for advanced configuration, basic usage is described below.

#### [subnet]

The subnet, in */* format is mandatory for each **subnet4** and defines which subnet is defined by the structure:

[FILE] **`/etc/kea/kea-dhcp4.conf`Define subnet 192.168.2.0/24**


            ]
        }
    }

#### [pools]

Although not strictly required, **pools** are typically defined for each subnet, and define where hosts without reservations pull IPs:

[FILE] **`/etc/kea/kea-dhcp4.conf`Define the pool to range from 192.169.2.100 to 192.168.2.200**

     ]
                }
            ]
        }
    }

#### [option-data]

In most cases, at least a *router* is provided by DHCP servers, but other DHCP options/codes can be defined here:

[FILE] **`/etc/kea/kea-dhcp4.conf`Define the router as 192.168.2.1**


                    ]
                }
            ]
        }
    }

#### [Reservations]

Kea offers several options for identifying and configuring hosts:

** See also**\
[KEA: Host Reservations in DHCPv4](https://kea.readthedocs.io/en/kea-2.4.0/arm/dhcp4-srv.html#host-reservations-in-dhcpv4)

[FILE] **`/etc/kea/kea-dhcp4.conf`Reserve 192.168.2.10 for aa:bb:cc:11:22:33 with 1.1.1.1 as a DNS server.**

     ]
                        }
                    ]
                }
            ]
        }
    }

### [control-socket]

Control sockets can be used to reload Kea\'s config at runtime, by default the following **control-socket** is defined:

[FILE] **`/etc/kea/kea-dhcp4.conf`**


        }
    }

### [lease-database]

By default, Kea uses a *memfile* **lease-database** backend. If compiled with the **mysql** *USE* flag, a SQL database can be used as the backend. The default **lease-database** config is as follows:

[FILE] **`/etc/kea/kea-dhcp4.conf`**


        }
    }

### [expired-leases-processing]

As described in the example config:

[FILE] **`/etc/kea/kea-dhcp4.conf`Annotated default config**


        }
    }

### [loggers]

** See also**\
[Kea: Logging](https://kea.readthedocs.io/en/kea-2.4.0/arm/logging.html)

To make Kea log to syslog, the following adjustments can be made:

[FILE] **`/etc/kea/kea-dhcp4.conf`Configure Kea to use syslog**


                    ],

                    "severity": "INFO",  // One of FATAL, ERROR, WARN, INFO, DEBUG
                    "debuglevel": 0  // 0 is least verbose, 99 is most verbose. Kea can generate LOTS of log information
                }
            ]
        }
    }

### [Service]

#### [OpenRC]

After installing, the default configuration files are found in [/etc/kea] and are prefixed with *kea-*, e.g. [kea-dhcp4.conf].

The way services are started in version 3.x (which is yet to be stabilized) has changed from version 2. Each service can be started and stopped individually, whereas with version 2.x there is only [/etc/conf.d/kea] that contains settings for dhcp4, dhcp6, ddns and ctrl-agent. In version 3 there are individual files per service. That is, [/etc/conf.d/kea-dhcp4], [/etc/conf.d/kea-dhcp6], etc.

For example, to start the dhcp4 service in version 3, do the following:

`root `[`#`]`rc-update add kea-dhcp4 `

`root `[`#`]`rc-service kea-dhcp4 start `

And similarly for dhcp6, ddns, etc.

In version 2 there is only one service *kea* and which daemons are launched is dependent on which is enabled in [/etc/conf.d/kea]

`root `[`#`]`rc-update add kea `

`root `[`#`]`rc-service kea start `

** Warning**\
When upgrading from 2.x to 3.x, the previously running service cannot be stopped as the kea service has been replaced with individual kea-dhcp4, kea-dhcp6, etc. The user may find they have to kill the kea deamons as *rc-service kea stop* will not work any more.

##### [High Availability]

To use the high availability feature of Kea, the [kea-ctrl-agent] must be started to allow the primary & standby server(s) to communicate.

##### [Starting after the logger]

To ensure Kea starts after eth0 has started, and logging is available, the following can be added to Kea\'s service configuration:

[FILE] **`/etc/conf.d/kea`**

    # snip
    rc_need="net.eth0 logger"
    # snip

** Tip**\
It is useful to require a logger, so any crash detected by start-stop-daemon is logged.

## [Usage]

### [Check config]

To check a Kea config file, [kea-dhcp4 -t] can be used:

`root `[`#`]`kea-dhcp4 -t /etc/kea/kea-dhcp4.conf`

    2023-08-08 10:41:23.712 INFO  [kea-dhcp4.hosts/4527.140104273917056] HOSTS_BACKENDS_REGISTERED the following host backend types are available:
    2023-08-08 10:41:23.713 INFO  [kea-dhcp4.dhcpsrv/4527.140104273917056] DHCPSRV_CFGMGR_USE_ADDRESS listening on address 192.168.2.1, on interface ethernet2
    2023-08-08 10:41:23.713 INFO  [kea-dhcp4.dhcpsrv/4527.140104273917056] DHCPSRV_CFGMGR_SOCKET_TYPE_DEFAULT "dhcp-socket-type" not specified , using default socket type raw
    2023-08-08 10:41:23.714 INFO  [kea-dhcp4.dhcpsrv/4527.140104273917056] DHCPSRV_CFGMGR_NEW_SUBNET4 a new subnet has been added to configuration: 192.168.2.0/24 with params: t1=900, t2=1800, valid-lifetime=3600

### [Hook Libraries]

#### [Run Script Support]

Kea has a useful interface to run scripts on certain events. For example this can be used to update DNS records when leases are allocated or revoked.

## [External resources]

-   [Kea DHCP - ISC](https://www.isc.org/kea/)

## [References]