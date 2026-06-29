# Tailscale

Tailscale builds on top of WireGuard and provides OAuth2 (SSO), OpenID, and SAML authentication for peers to build a mesh network. It is crossplatform, has ACL settings and internal DNS.

## Installation
Install  and reboot your system.

It is also possible to run tailscale as a Docker container. This way, one can run multiple exit nodes on a single machine, each with its own tailnet.

## System tray application
Introduced with v1.88, tailscale ships with the systray application. To launch the systray run:

 # tailscale systray

To run the systray at startup as a systemd user service:

 # tailscale configure systray --enable-startup=systemd

More information is available at tailscale's official documentation.

## Third-party clients
*
*
*
*

## Usage
To use tailscale, enable/start  and run the server as follows:

 # tailscale up

You can authenticate a headless machine by specifying the auth key:

 # tailscale up --authkey=tskey-KEY

## Advanced usage
## Using a custom Control Server
Using a custom control server like headscale is possible.

To login run

 # tailscale up --login-server https://example.com

On headless systems a non-interactive login using a token is possible.

 # tailscale up --login-server https://example.com --authkey your_auth_key

You may create user and auth-key using following commands after starting :

 # headscale users create USER -e email@example.com
 # headscale users list
 # headscale preauthkeys create -u  --reusable

## Share nodes between users
Create file with policy:
 {
  "tagOwners": {
    "tag:shared": },
  "groups": {
    "group:all": ["user1@", "user2@", "user3@"
  },
  "acls": [
    {
      "action": "accept",
      "src": "dst": ["tag:shared:*"
    }
  ]
 }

Point this file in config.yaml:
 policy:
  mode: file
  path: "/etc/headscale/policy.json"

Advertise tag:
  tailscale up --advertise-tags=tag:shared --login-server=https://headscale.localdomain/

## Integration with nextcloud or another OIDC provider
Install  and create client key, use https://headscale.localdomain/oidc/callback as redirection uri.

Add following snippet into config.yaml:
 oidc:
  issuer: "https://cloud.example.com"
  client_id: ""
  client_secret: ""
  scope: "profile", "email"
  user_map:
    name: "preferred_username"
    email: "email"

## Running as a Docker container
Follow this guide for a general idea of how to run tailscale as a docker container.

## As an exit node
In order to be able to use a tailscale instance running as a docker container as an exit node, we need to use a smaller MTU for the container's network. This is due to an MTU-related issue.

If you do not have one already, create a custom network:

 # docker network create --opt com.docket.network.driver.mtu=1280 my_custom_network

Then, use that network for the container instance:

 # docker run --detach --name=my_tailscale_container --network=my_custom_network --volume /var/lib/tailscale-exitnode-1:/var/lib/tailscale --env TS_STATE_DIR=/var/lib/tailscale --env TS_USERSPACE=1 --env TS_AUTHKEY=tskey-auth-XXX --env TS_EXTRA_ARGS='--advertise-exit-node' tailscale/tailscale

Note that:
* By default, docker will create a network of type , so no need to specify it here.
* Use an auth key to authenticate the node. Authenticating with the regular SSO method usually takes too long, and the process may time out before initial authentication is successful.
* Define  so that the container does not need elevated permissions ( and ).
* Bind mount an unused directory on the host () to  inside the container, and also define , so that tailscale will use a persistent state file. Without these, the exit node will use volatile memory to keep state, and thus get a new ID and tailnet IP address every time the container is restarted.

## Tips and tricks
## Using with NetworkManager
If you use NetworkManager, you may notice connection issues with other devices within your tailnet. This is due to a management conflict that is happening between NetworkManager and tailscaled.

To clear this up, we need NetworkManager to unmanage the tailscale network devices (e.g. ).

To do so, simply create a config like  with the contents of:

 unmanaged-devices=interface-name:tailscale0

Then restart  and .

You may also need to cycle tailscale:

 # tailscale down
 # tailscale up

After this, you should be able to  other devices on your tailnet.

## Magic DNS
Tailscale expects system with working systemd-resolved to set up DNS server and search suffixes from tailnet configuration, otherwise it [https://tailscale.com/blog/sisyphean-dns-client-linux tries to overwrite .

## Security Hardening
Tailscale can be made to run in its own user and with just the capabilities it needs to operate. See the official knowledge base article for detail.

## Troubleshooting
## Tailscale crash on launch
After starting , it may crash and get stuck on a restart loop. This may be due to the absence of the tun kernel module. To verify that this is indeed the case, view the logs of  via systemd

 # systemctl status tailscaled.service

Or, run the binary as root in your terminal

 # /usr/sbin/tailscaled

The following, or similar error may appear in systemctl status or by running the binary:

 ...is CONFIG_TUN enabled in your kernel? modprobe tun failed with: modprobe: FATAL: Module tun not found in directory /lib/modules/5.17.4-arch1-1 kernel/drivers/net/tun.ko found on disk, but not for current kernel; are you in middle of a system update and haven't rebooted? found: /lib/modules/5.17.8-arch1-1/kernel/drivers/net/tun.ko.zst wgengine.NewUserspaceEngine(tun "tailscale0") error: tstun.New("tailscale0"): no such device

If so, simply reboot your system and observe if  is active instead of loaded with systemctl status.
