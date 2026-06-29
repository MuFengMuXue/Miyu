# NFS/Kerberos

Kerberos is one of the few security mechanisms available for NFS. It provides strong per-user authentication, strong data encryption, and (with NFSv4) removes the requirement for matching UIDs/GIDs between client and server.

NFSv4 is recommended for Kerberos. Although it is possible to enable Kerberos in NFSv3, it will not provide 100% coverage as the auxiliary NFSv3 protocols (e.g. the "mount" protocol) remain insecure, and the lack of idmapping in NFSv3 severely reduces the usability of Kerberos as well.

## Prerequisites
Kerberos requires a KDC (Key Distribution Center) service to be running somewhere. The  that comes with MIT Kerberos () is a good option for small setups that do not warrant the complexity of Active Directory or FreeIPA. The second option is Heimdal, found on some BSDs and as  on Arch.

NFSv4 idmapping becomes much more important to have with Kerberos. Both the server and the clients should have the same idmapping domain configured:

## Server configuration
Each NFS server needs a Kerberos principal for  to be created on the KDC, and its keys added to the server's .

 fileserv# kadmin -p frob/admin
 Password for frob/admin@EXAMPLE.COM: *********
 kadmin:  addprinc -nokey nfs/fs.example.com
 kadmin:  ktadd nfs/fs.example.com

 must be enabled and started on the server.

gssproxy comes pre-configured with NFS server support (the  file is part of the standard package) and does not need any tweaking, other than placing the NFS service keytab in the standard location.

Your  should offer the Kerberos authentication flavors in the  option:

 /home    *(rw,sec=krb5p)
 /usr     10.147.0.0/16(rw,sec=krb5p:krb5i:krb5:sys) *(rw,sec=krb5p)

The available flavors are:

*  provides 'privacy' (Kerberos-based encryption). It is sufficiently secure to be used over Internet, but might provide poor throughput over a LAN – consider using  inside RPC-with-TLS instead.
*  provides 'integrity' (Kerberos-based MAC) but not encryption. It might be useful for serving static data as it still protects against packet tampering.
*  provides only authentication, without data integrity or encryption. It is a good choice if you have RPC-over-TLS enabled via  or if Kerberos is being run over an otherwise "secure" LAN (e.g. over a WireGuard tunnel), but certainly not in the clear over public networks.
*  is the traditional UID-based (non-Kerberos) NFS security mode.

## Client configuration
In addition to users, each NFS client should have a machine Kerberos principal in , which will be used in situations where user Kerberos tickets are not yet available – in particular, it will be needed to actually mount the filesystem at boot time before any users have logged in yet (or if mounting is done via autofs). More generally, all operations done "as root" will be authenticated as the machine principal.

Unlike in the server case, the client machine does not need an  principal specifically – it is enough to have the generic  principal. (See the rpc.gssd manual page for what it looks for.)

The client must have  active (i.e. the  daemon).

Options used when mounting the filesystems are very similar to the options used in ; you can specify one or more flavors using the  option. Although the client will automatically use the strongest mode offered, it is nevertheless recommended to explicitly require e.g.  to prevent downgrade attacks.

Once the filesystem has been mounted, root may already access it (using the machine's Kerberos credentials), but every non-root user needs their own Kerberos tickets to be present. This means either having the user manually run  for themselves, or setting up  to acquire tickets during login (which only works for password-based logins), or using  or  (from ) to acquire tickets from a keytab file.
