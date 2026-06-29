[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** Most of this article has not been translated（在 [Talk:CurlFtpFS#](<../zh-cn/Talk:CurlFtpFS.html>) 中讨论）

**注意：** As of February 2015, curlftpfs is reported to be extremely slow, see for example [a Ubuntu bug report](<https://bugs.launchpad.net/ubuntu/+source/curlftpfs/+bug/1267749>) and a [stackoverflow.com question](<https://stackoverflow.com/questions/24360479/ftp-with-curlftpfs-is-extremely-slow-to-the-point-it-is-impossible-to-work-with>).

[CurlFtpFS](<http://curlftpfs.sourceforge.net/>) is a filesystem for accessing FTP hosts based on [FUSE](<../zh-cn/FUSE.html> "FUSE") and libcurl. 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [curlftpfs](<https://archlinux.org/packages/?name=curlftpfs>)包。 

有必要的话，加载fuse内核模块 
    
    # modprobe fuse
    
## Mount FTP folder as root

Create the mount point and then mount the FTP folder. 
    
    # mkdir /mnt/ftp
    # curlftpfs ftp.yourserver.com /mnt/ftp/ -o user=username:password
    
If you want to give other (regular) users access right, use the `allow_other` option: 
    
    # curlftpfs ftp.yourserver.com /mnt/ftp/ -o user=username:password,allow_other
    
Do not add space after the comma or the `allow_other` argument will not be recognized. 

To use FTP in active mode add the option 'ftp_port=-': 
    
    # curlftpfs ftp.yourserver.com /mnt/ftp/ -o user=username:password,allow_other,ftp_port=-
    
You can add this line to /etc/fstab to mount automatically. 
    
    curlftpfs#USER:PASSWORD@ftp.domain.org /mnt/mydomainorg fuse auto,user,uid=1000,allow_other,_netdev 0 0
    
**提示：** You can use codepage="_string_ " when having problems with non-US English characters on servers that do not support UTF8, e.g. codepage="iso8859-1"

To prevent the password to be shown in the process list, create a `.netrc` file in the home directory of the user running curlftpfs and `chmod 600` with the following content: 
    
    machine ftp.yourserver.com
    login username
    password mypassword
    
## Mount FTP folder as normal user

You can also mount as normal user (always use the `.netrc` file for the credentials and ssl encryption!): 
    
    $ mkdir ~/my-server
    $ curlftpfs -o ssl,utf8 ftp://my-server.tld/ ~/my-server
    
if the answer is 
    
    Error connecting to ftp: QUOT command failed with 500
    
then the server does not support the `utf8` option. Leave it out and all will be fine. 

**提示：** If need be try setting the encoding with for example -o codepage="iso8859-1"

To unmount: 
    
    $ fusermount -u ~/my-server
    
## Connect to encrypted server

In its default settings, CurlFtpFS will authenticate in cleartext when connecting to a non encrypted connection port. If the remote server is configured to refuse non encrypted authentification method / force encrypted authentification, CurlFtpFS will return a 
    
    # Error connecting to ftp: Access denied: 530
    
To authenticate to the ftp server using explicit encrypted authentification, you must specify the ssl or tsl option. 
    
    # curlftpfs ftp.yourserver.com /mnt/ftp/ -o ssl,user=username:password
    
If your server uses a self-generated certificate not thrusted by your computer, you can specify to ignore it 
    
    # curlftpfs ftp.yourserver.com /mnt/ftp/ -o ssl,no_verify_peer,no_verify_hostname,user=username:password
    
An implicit tsl mode is also available. For more details, check the manual page. 

##  乱码

如果中文出现乱码，你可能需要指定编码： 
    
    sudo curlftpfs -o codepage=gbk -o rw,allow_other <ftp://username:password@ftp.yourserver.com> /mnt/ftp
    