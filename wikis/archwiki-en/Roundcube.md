# Roundcube

Roundcube is a full-featured, PHP web-based mail client.

## Installation
Install the  package.
Further you will need a database (e.g. MariaDB) and a web server with PHP-support.

## Configuration
## MariaDB
Here is an example on how you could setup a database for Roundcube with MariaDB called  for the user  identified by the password :

For any database you use, you will need to initialize the roundcubemail database tables.  Here is an example of how to do this with MariaDB:

 $ mysql -u root -p roundcubemail
     Options -FollowSymLinks
     AllowOverride None
     Require all denied

}}

## Tips and tricks
## Setting Roundcube up for use with an IMAP/SMTP server that only allows TLS authentication
It is quite common for modern IMAP/SMTP servers to only allow secured (encrypted) connection, say using STARTTLS. If you are setting Roundcube up for TLS connection, the web-based installer will not help you. You will need to edit the  by hand, adding the following lines:

  $config= 'tls://mail.my_domain.org';
  // For STARTTLS IMAP
  $config['imap_conn_options' = [
      'ssl' => [
        'cafile'  => '/etc/ssl/certs/Your_CA_certificate.pem',
        // For Letsencrypt use the following line if ISRG_Root_X1 is indeed the corresponding root certificate:
        //'cafile' => '/etc/ssl/certs/ISRG_Root_X1.pem',
        // Needed for example if you're using `localhost` as imap_host but your imap server presents another host name:
        //'peer_name'         => 'mail.my_domain.org',
      ],
  ];
  // For STARTTLS SMTP
  $config= [
      'ssl' => [
        'cafile'  => '/etc/ssl/certs/Your_CA_certificate.pem',
        // For Letsencrypt use the following line if ISRG_Root_X1 is indeed the corresponding root certificate:
        //'cafile' => '/etc/ssl/certs/ISRG_Root_X1.pem',
        // Needed for example if you're using `localhost` as imap_host but your imap server presents another host name:
        //'peer_name'         => 'mail.my_domain.org',
      ,
  ];

where  is the  host name in your SSL certificate (i.e. the hostname of your IMAP server), and  is the path to your SSL certificate.

A complete list of PHP SSL configuration options can be found here. For example you might need to adjust the  element to correspond to the ciphers allowed by your IMAP server.

## Update the roundcube database
 # mysql -u root -p roundcubemail : Recipient address rejected: Access denied

If that happens try adding the following lines to config.inc.php:

 $config= '%u';
 $config['smtp_pass' = '%p';
