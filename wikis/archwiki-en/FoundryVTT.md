# FoundryVTT

Foundry VTT is a standalone application built for experiencing multiplayer tabletop RPGs using a feature-rich and modern self-hosted application where your players connect directly through the browser.

Foundry VTT is proprietary software. A paid license must be acquired before using the software.

These instructions show one of the possible ways to install Foundry VTT in an Arch Linux system. At the end of the process, the service should be accessible from a browser using a secure connection.

## Installation
## Requirements
Before installing Foundry VTT, you should have a working installation of nginx and Node.js.

## Creating directories
First of all, create these directories to install the software and its data. You can create these directories under /home, for example:

 # mkdir -p /home/foundry/{foundryvtt,foundrydata}

## Creating a system user
Foundry VTT will be run by a system user. First, create a system user with the name foundry or any other name.

 # useradd -r -s /usr/bin/nologin foundry

## Downloading
Once you have registered in foundryvtt.com and have purchased a license, you need to go to the "Purchased Software Licenses" section of your profile page. There you will see different packages for the software.

You may notice a small 'chain' link icon next to the download links on the download page. Clicking this chain icon generates a temporary link which can be used to download Foundry VTT via a terminal or shell interface using wget.

When downloading the link using a command line utility such as wget it is important to wrap the link in double-quotes. This ensures that the link is read correctly by the command. For example:

 # wget -O foundryvtt.zip "https://your-download-link-from-foundry-vtt.com-here/"

The downloaded file must be uncompressed to the foundryvtt directory that you created before. Once this directory is populated, you need to set the proper permissions:

 # unzip foundryvtt.zip -d /home/foundry/foundryvtt
 # chown -R foundry:foundry /home/foundry/foundryvtt
 # chown -R foundry:foundry /home/foundry/foundrydata

## Usage
## Running the software without a proxy
Now you can test if the software works. Run the server as the user foundry:

 node /home/foundry/foundryvtt/main.js --dataPath=/home/foundry/foundrydata

While it is running, you should be able to connect to the server from a browser, using port 30000. If you wish, you can now set your admin password and save your license key.

Now stop the server using .

## Creating a service
One of the ways to run the software is using systemd#Writing unit files. You can create a simple service for Foundry VTT:

 [Unit
 Description=Foundry VTT

 Type=simple
 ExecStart=node /home/foundry/foundryvtt/main.js --dataPath=/home/foundry/foundrydata
 Restart=on-failure
 User=foundry

 [Install
 WantedBy=multi-user.target

As suggested in the installation instructions, edit the software options to prepare it to be accessed through a proxy server:

Set the following options, keeping the other ones, where hostname is e.g :

## Configuring nginx
To configure a nginx proxy server for Foundry VTT you can use this example from the official documentation:

 # This goes in a file within /etc/nginx/sites-available/. By convention,
 # the filename would be either "your.domain.com" or "foundryvtt", but it
 # really does not matter as long as it's unique and descriptive for you.

 # Define Server
 server {

     # Enter your fully qualified domain name or leave blank
     server_name             your.hostname.com;

     # Listen on port 443 using SSL certificates
     listen                  443 ssl;
     listen                  ssl;
     ssl_certificate         "/etc/letsencrypt/live/your.hostname.com/fullchain.pem";
     ssl_certificate_key     "/etc/letsencrypt/live/your.hostname.com/privkey.pem";

     # Sets the Max Upload size to 300 MB
     client_max_body_size 300M;

     # Proxy Requests to Foundry VTT
     location / {

         # Set proxy headers
         proxy_set_header Host $host;
         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
         proxy_set_header X-Forwarded-Proto $scheme;

         # These are important to support WebSockets
         proxy_set_header Upgrade $http_upgrade;
         proxy_set_header Connection "Upgrade";

         # Make sure to set your Foundry VTT port number
         proxy_pass http://localhost:30000;
     }
 }

 # Optional, but recommend. Redirects all HTTP requests to HTTPS for you
 server {
     if ($host = your.hostname.com) {
         return 301 https://$host$request_uri;
     }

     listen 80;
     listen [:::80;

     server_name your.hostname.com;
     return 404;
 }

You can get your certificates using certbot.

## Running the service
Now start/enable both  and .

At this point you should be able to access the service from a browser by pointing it at the hostname set earlier.

## Updating
Minor updates can be performed within FoundryVTT, however, major updates require manual installation.

Stop the  (if running).

Remove the old installation in . This does NOT affect your user/game data which should be in  if following this guide.

 # rm -rf /home/foundry/foundryvtt/*

Download the new Node.js version using the timed URL from your account (see #Downloading):

 # wget -O foundryvtt.zip "https://your-download-link-from-foundry-vtt.com-here/"

Extract and set permissions:

 # unzip foundryvtt.zip -d /home/foundry/foundryvtt
 # chown -R foundry:foundry /home/foundry/foundryvtt
