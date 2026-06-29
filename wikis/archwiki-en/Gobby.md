# Gobby

From the project web page:
:Gobby is a collaborative editor supporting multiple documents in one session and a multi-user chat.

## Installation
Install the  package.

To run the Infininote server protocol without the Gobby front end install

## Infininote usage
To start the server portion, run

 $ infinoted-0.7 --security-policy=no-tls

The server only needs to be running on one machine.

Then, run the gobby client and connect to the server via IP or localhost.

If you would rather have encryption, TLS is available. Use:

 $ infinoted-0.7 --create-key --create-certificate -k key.pem  -c cert.pem

The keys creation is automatic, and you can launch the server just using:

 $ infinoted-0.7 -k key.pem  -c cert.pem
