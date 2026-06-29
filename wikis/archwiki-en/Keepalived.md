# Keepalived

Keepalived is a failover and monitoring daemon for Linux virtual server (LVS) clusters that provides high availability functionality and load balancing using the Virtual Router Redundancy Protocol (VRRP).

## Installation
Install the  package.

Enable .

## Configuration
The service is configured in .

## Master and backup failover setup
The following provides a basic configuration to setup a high availability cluster with two servers/routers sharing a virtual IP address. Both need to be running keepalived.

On host A:

{{hc|/etc/keepalived/keepalived.conf|
vrrp_instance VI_1 {
    state MASTER
    interface eth0
    virtual_router_id 101
    priority 255
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass pass1234
    }
    virtual_ipaddress {
        172.16.0.100
    }
}
}}

On host B:

{{hc|/etc/keepalived/keepalived.conf|
vrrp_instance VI_1 {
    state BACKUP
    interface eth0
    virtual_router_id 101
    priority 150
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass pass1234
    }
    virtual_ipaddress {
        172.16.0.100
    }
}
}}

The state sets the initial role of the host when the service is started and before multicast advertisements are processed to determine the host with the highest priority which will take the master role. This setup means that the host A with the higher priority will manage the VIP (virtual IP address) and only if host A stops responding will host B take over the VIP. The default transition time until takeover is one second.

## Failover setup with monitoring
The following provides a failover cluster for service (sshd) running on the same hosts as keepalived.

This setup provides a more dynamic cluster for the sshd service running on the failover host itself. Both servers start in the backup state and the nopreempt option allows the server with the lower priority to keep the master role even when the server with the higher priority returns after a failure. This prevents the interruption of connections to the VIP when the former master server comes back alive. The configuration also includes process tracking to reduce the priority of a server when the target service crashes. Since the weight option in the process section is omitted, the server enters the failed state as soon as the tracked process is no longer available and the delay timer has run out.

On host A:

{{hc|/etc/keepalived/keepalived.conf|
global_defs {
   notification_email {
     admin@example.net
   }
   notification_email_from lb1@example.net
   smtp_server mail.example.net
   smtp_connect_timeout 30
}

# enter failed state when the sshd process is down
vrrp_track_process track_sshd {
    process sshd
    delay 1
}

vrrp_instance VI_1 {
    state BACKUP
    nopreempt
    interface eth0
    virtual_router_id 101
    priority 200
    advert_int 1
    authentication {
        auth_type AH
        auth_pass key12345
    }
    virtual_ipaddress {
        172.16.0.100
    }
    track_process {
        track_sshd
    }
    smtp_alert
}
}}

On host B:

{{hc|/etc/keepalived/keepalived.conf|
global_defs {
   notification_email {
     admin@example.net
   }
   notification_email_from lb2@example.net
   smtp_server mail.example.net
   smtp_connect_timeout 30
}

# enter failed state when the sshd process is down
vrrp_track_process track_sshd {
    process sshd
    delay 1
}

vrrp_instance VI_1 {
    state BACKUP
    nopreempt
    interface eth0
    virtual_router_id 101
    priority 150
    advert_int 1
    authentication {
        auth_type AH
        auth_pass key12345
    }
    virtual_ipaddress {
        172.16.0.100
    }
    track_process {
        track_sshd
    }
    smtp_alert
}
}}

## Failover with load-balancing
Keepalived also provides load balancing with a number of possible algorithms (see ).

This would be a simple example for HTTP load balancing that can be added to the above configuration:

{{hc|/etc/keepalived/keepalived.conf|
virtual_server 172.16.0.100 80 {
    delay_loop 6
    lvs_sched rr
    lvs_method NAT
    protocol TCP

    real_server 172.16.1.20 80 {
        TCP_CHECK {
                connect_timeout 10
        }
    }
    real_server 172.16.1.21 80 {
        TCP_CHECK {
                connect_timeout 10
        }
    }
    real_server 172.16.1.22 80 {
        TCP_CHECK {
                connect_timeout 10
        }
    }
    real_server 172.16.1.23 80 {
        TCP_CHECK {
                connect_timeout 10
        }
    }
}
}}

Alternatively, keepalived can also be used for failover with HAproxy acting as the loadbalancer.

## Security considerations
The VRRP protocol used by keepalived does not provide significant security against attackers who are already on the same subnet. The main benefit of using authentication in this service is to protect against accidentally adding servers that disrupt an existing cluster. When using , the password is sent in plaintext over the local subnet with every multicast packet. Using  (IP Authentication Header) will provide slightly better resilience against attacks but basic disruption and attacks such as ARP spoofing are still possible. Use network restrictions to protect the VRRP traffic if security is a high priority for you, e.g. use an isolated subnet for the cluster and block VRRP traffic from other networks in your firewall.
