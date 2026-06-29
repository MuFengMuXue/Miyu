# UnrealIRCd

UnrealIRCd (Unreal IRC daemon) is an open source IRC server. Development of UnrealIRCd began in May of 1999. Unreal was created from the Dreamforge IRCd that was formerly used by the DALnet IRC Network. Over the years, many new and exciting features have been added to Unreal. It is hard to even see a resemblance between the current Unreal and Dreamforge.

## Installation
Install the  package.

## Configuration
From there you will want to follow the UnrealIRCd Configuration docs making sure to configure all of the required fields such as , , , etc.

Place your TLS key/cert at  and . You can use Certbot to obtain a key and certificate, or generate a self-signed one as explained at Apache HTTP Server#TLS.

The  module .so is not built, but referenced in the default upstream config. add  to the config file.

Besides following the default config files instructions, admin careful with privacy may want to set the following config option : . Setting this will avoid leaking users hosts.

## Usage
You can start and stop the UnrealIRCd daemon with the  systemd unit.

If you run into problems where the daemon will not start, try running it as the ircd user manually:

 ircd$ unrealircd

It will print out the errors and what line they occur on. Often errors are due to problems in your configuration.
