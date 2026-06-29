# OpenVPN/Checklist guide

This article summarizes the install process required for OpenVPN. See OpenVPN instead for a walkthrough.

## Install
Install the packages  and .

## Prepare data
* Copy  to  and cd there
* Edit the  file with the information you want. Read Create a Public Key Infrastructure Using the easy-rsa Scripts for details.
* Clean up any previous keys:

## Generate the certificates
* Create a seed for the CA creation

* Create the "certificate authority" key

* Create certificate and private key for the server

* Create the Diffie-Hellman pem file for the server.

* Create a certificate for each client.

All certificates are stored in  directory. If you mess up, you can start all over by doing a

Copy to each client the , and their respective crt and key files.

## Setting up the server
Create  with a content like this:

Start and optionally enable the service. In this example, it is .

## Setting up the clients
Create a .conf file for each client like this:

Start and optionally enable the service. In this example the unit is .

## Troubleshooting
If the openvpn server can be started manually as root but not using systemd, you can try fixing the permissions:

 # chown -R openvpn:network /etc/openvpn/*
