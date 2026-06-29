# Saber

Saber is an open source cross platform handwritten notes app licensed under GPLv3.0.

## Installation
Install the  package, please read #Building for steps to successfully build the saber package.

## Building
Due to complications with flutter, saber requires manual intervention to build the package.

# Install  and .
# Set the stable toolchain as the default, to prevent flutter throwing an error:
#:
# Fix known flutter issues on Arch Linux:
#:
#: See User:Gromit/Flutter package guidelines#Ownership problems, or permission denial for more information.

## Configuration
Saber is a graphical User Interface (GUI), all configuration is done via the settings menu on the left sidebar.

## Integration with nextcloud
Saber provides an integration with nextcloud to allow synchronisation of notes between multiple devices. It also provides redundancy which removes the worry of notes being lost due to device failure.

By default, Saber is configured to use saber's official instance provided by the upstream developer Adil Hanney.

## Using the default nextcloud instance
* Register an account (if you have not done so already)
* Open the Settings menu on the right toolbar (settings icon)
* Click the Logged out widget at the top of the settings page, this will bring you to the Login page
* Enter the email address and password you used when you registered your account, the encryption password should be a password unique to you, which will only be stored on your client, this is used as a key to encrypt and decrypt the notes you write for privacy, you must remember this otherwise you will not be able to decrypt your notes on other devices.

## Using a third party nextcloud instance
Nextcloud has multiple providers which you can pick from, or use a provider which is not listed here.

Saber's official nextcloud instance is stock and contains no modifications to the API, allowing you to use any provider which has not modified nextcloud's protocol.

To use a third party nextcloud provider, register an account on the corresponding web interface, and then follow the same login instructions in #Using the default nextcloud instance, ensure to check the I want to use a Custom Nextcloud Server box, and then enter the providers url in the Custom server URL box, otherwise you will not be able to authenticate.

## Self hosting a nextcloud instance
If you would like to self host the nextcloud instance for saber, follow the installation guide Nextcloud#Installation and then the setup/configuration guide Nextcloud#Configuration.

After your instance is setup, create yourself a user and follow the same login instructions in #Using the default nextcloud instance, ensure you check I want to use a Custom Nextcloud Server, and enter the url of your nextcloud instance in the Custom server URL box.
