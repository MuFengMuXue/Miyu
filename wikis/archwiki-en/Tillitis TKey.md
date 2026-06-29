# Tillitis TKey

The TKey is an Open-source hardware and open source software USB security key that can support use cases such as SSH login, Ed25519 digital signing, Root of Trust, FIDO2, and more.
The software, and board designs, FPGA verilog and firmware for the TKey are released by Tillitis.

The threat model, such as assumptions on trust and attack vectors, for the TKey is specified by Tillitis.

As the TKey has no persistent storage its output are calculated from any input and a unique device secret (UDS), see Tillitis TKey Developer Handbook.
Every time the TKey is plugged into the computer a device app has to be loaded onto it.
When the device app is loaded, the TKey calculates a Compound Device Identifier (CDI) based on a hash of the device app binary code, the UDS and possibly a User Supplied Secret (USS). The CDI is then available for use by the device app, for example to derive a private key from.

## First usage
The TKey identifies with the device signature:

and is accessible at a serial port like .
To use the TKey, add yourself to the  user group.

It is preferred to use a udev rule for the vendor  and the product  instead that makes the device writable for a user.

## Verification with tkey-verification
To test if the device is properly set-up, it is recommended to run the
vendor provided tkey-verification program, packaged in .
Apart from a functionality check of the TKey, the software also verifies that the TKey contains the same firmware as at the time of production so the firmware on the TKey has not been altered.

## Applications
This section describes usage of some available tools.

## tkey-ssh-agent
The TKey may authenticate SSH agent requests with . To print its public ssh key:

 $ tkey-ssh-agent --show-pubkey

An additional user supplied secret (USS) can be provided either with  (requiring a pinentry program) or with  command-line arguments to tkey-ssh-agent.
The USS determines the ssh public key, that means providing a different USS will output a different key.
If, for instance, the USS that was used to generate a public ssh key is , this USS shall be typed into the pinentry prompt when authenticating to the server that uses this public key.

To start the ssh agent:

 $ tkey-ssh-agent --agent-socket $XDG_RUNTIME_DIR/tkey_ssh_agent.sock

## Use both tkey-ssh-agent and ssh-agent
Openssh can be configured (see ) to authenticate only some connections with  and default to  for other ssh connections.
To use the TKey to authenticate a connection to a certain host set the ssh configuration option  to the socket path of the tkey-ssh-agent:

The above example would ask to authenticate to  with the TKey, assuming its  is the above configured  path.

If  is started/managed with the  (provided as part of the  package) as a Systemd/User unit, then the socket path is the value of .
