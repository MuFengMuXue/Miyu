# PuTTY

PuTTY is a port of the popular GUI SSH, Telnet, Rlogin and serial port connection client for Windows. It has support for advanced logging and termcap options, as well as a very configurable appearance and the ability to forward ports or create a SOCKS tunnel through an SSH destination. To start, simply run PuTTY, type the hostname of the host you would like to connect to and hit Open.

## Installation
Install .

## Configuration
The settings can be modified through the tabs on the left; however, they will be reset if not saved. To save your settings, type a name into the box under Saved Sessions and click save. To load it again later, click the name of your save and click load. This allows you to persist your visual, termcap and connection settings between connections and also lets you keep one save per regularly used host. The save "Default Settings" is automatically loaded every time you start PuTTY, so save under that name with care.

## Importing keys
PuTTY uses its own format to store the private keys on the client side. To import a key that you had previously generated, you need to use the  command.

 $ puttygen keyfile -o output-keyfile.ppk

where  is an existent private keyfile, and  is the file that will receive the key.

If the  is protected with a passphrase, you will be prompted to input it, but the key will still be protected afterwards in the .

After that, you can import it to make an SSH connection: Connection > SSH > Auth > Private key file for authentication and click on Browse... to add it.

## 256 color support
Settings > Connection > Data : Terminal-type string = putty-256color

To test color support, execute the following commandfor code in {0..255}; do echo -e "\e[38;05;${code}m $code: Test"; done

See [https://www.robmeerman.co.uk/unix/256colours 256colours for details.
