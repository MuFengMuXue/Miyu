# CurlFtpFS

CurlFtpFS is a filesystem for accessing FTP hosts based on FUSE and libcurl.

## Installation
Install the  package.

Make sure the kernel module has been loaded.

 # modprobe fuse

## Mount FTP folder as root
Create the mount point and then mount the FTP folder.

 # mkdir /mnt/ftp
 # curlftpfs ftp.example.com /mnt/ftp/ -o user=username:password

If you want to give other (regular) users access right, use the  option:

 # curlftpfs ftp.example.com /mnt/ftp/ -o user=username:password,allow_other

Do not add space after the comma or the  argument will not be recognized.

To use FTP in active mode add the option :

 # curlftpfs ftp.example.com /mnt/ftp/ -o user=username:password,allow_other,ftp_port=-

You can add this line to  to mount automatically.

 curlftpfs#USER:PASSWORD@ftp.example.com /mnt/exampleorg fuse auto,user,uid=1000,allow_other,_netdev 0 0

To prevent the password to be shown in the process list, create a  file in the home directory of the user running curlftpfs and  with the following content:

 machine ftp.example.com
 login username
 password mypassword

## Mount FTP folder as normal user
You can also mount as normal user (always use the  file for the credentials and ssl encryption!):

 $ mkdir ~/example
 $ curlftpfs -o ssl,utf8 ftp://example.com/ ~/example
if the answer is

 Error connecting to ftp: QUOT command failed with 500

then the server does not support the  option. Leave it out and all will be fine.

To unmount:
 $ fusermount -u ~/example

## Connect to encrypted server
In its default settings, CurlFtpFS will authenticate in cleartext when connecting to a non encrypted connection port. If the remote server is configured to refuse non encrypted authentication method / force encrypted authentication, CurlFtpFS will return a
 # Error connecting to ftp: Access denied: 530

To authenticate to the ftp server using explicit encrypted authentication, you must specify the ssl option.
 # curlftpfs ftp.example.com /mnt/ftp/ -o ssl,user=username:password

If your server uses a self-generated certificate not trusted by your computer, you can specify to ignore it
 # curlftpfs ftp.example.com /mnt/ftp/ -o ssl,no_verify_peer,no_verify_hostname,user=username:password

For more details, see the  man page.

## Troubleshooting
## Unable to access files with non percent-encoded characters in their filename
This is a bug which has been initially reported in Launchpad bug 783033 in 2011 regarding paths with "#", confirmed in 2013 with no further activity. An upstream bug report links to a potential patch, which also fixes a breaking change in .
