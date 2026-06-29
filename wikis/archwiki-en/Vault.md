# Vault

Vault is an open-source tool from HashiCorp for securely managing secrets and protecting sensitive data. It provides encryption as a service, access control, and detailed audit logging.

## Installation
Install the  package.

## Configuration
Vault can be run in development mode for testing or configured as a production server with enhanced security settings.
The configuration is defined in a file using the "Hashicorp Command Language" (HCL) format.

## Development mode
For testing, Vault can be run in development mode, which starts with an in-memory storage backend and automatically unseals itself.

To start Vault in development mode, run the following command:

 $ vault server -dev

## Production configuration
To set up a production-ready Vault server, create a configuration file:

 # mkdir /etc/vault
 # touch /etc/vault/config.hcl

Then, add your desired configuration settings to .

## Storage configuration
Vault supports multiple storage backends. For a simple file-based backend, use:

{{bc|1=
storage "file" {
    path = "/opt/vault/data"
}
}}

For high-availability or heavy usage environments, consider using , , or other supported storage solutions that offer scalability and reliability.

## Listener configuration
Vault listens on a TCP port for API requests. For basic configurations without TLS, use:

{{bc|1=
listener "tcp" {
    address     = "127.0.0.1:8200"
    tls_disable = "true"
}
}}

If TLS is required for secure communication, configure it as follows:

{{bc|1=
listener "tcp" {
    address     = "127.0.0.1:8200"
    tls_disable = "false"
    tls_cert_file = "/etc/vault/vault-cert.pem"
    tls_key_file  = "/etc/vault/vault-key.pem"
}
}}

## UI configuration
To enable the Vault web interface, add:

 ui = true

## API and cluster addresses
Set the API and cluster addresses for proper networking:

 api_addr = "http://127.0.0.1:8200"
 cluster_addr = "http://127.0.0.1:8201"

If using TLS:

 api_addr = "https://127.0.0.1:8200"
 cluster_addr = "https://127.0.0.1:8201"

## Security considerations
By default, Vault locks memory to prevent sensitive data from being swapped to disk. This enhances security by ensuring that secrets do not end up in the swap space, where they could be accessed by unauthorized users or forensic tools.

However, using mlock requires ensuring that the system has sufficient memory and allows unlimited memory locking. If the system lacks adequate RAM or has restrictive memory limits, enabling mlock could cause Vault to fail unexpectedly. To safely use mlock, ensure:

* The system has enough free RAM to accommodate Vault’s memory usage.
* The systemd service is configured with:

 AmbientCapabilities=CAP_IPC_LOCK
 LimitMEMLOCK=infinity

If your system does not meet these requirements, you may need to disable . To do so (not recommended for production environments):

 disable_mlock = true

## Audit logging configuration
Vault uses audit devices to log client requests and responses for security and troubleshooting purposes. The audit logs help track access patterns, detect anomalies, and ensure compliance.

## Configuring a file-based audit log
To enable a file-based audit log, configure an audit device in Vault:

{{bc|1=
audit_device "file" {
    path   = "/var/log/vault-audit.log"
    format = "json"
}
}}

This will log audit events to  in JSON format, making it easier to parse and analyze.

To ensure Vault can write to the audit log securely, set the correct permissions:

## Other audit devices
Vault supports multiple audit logging backends besides files, For a full list of supported audit devices and advanced configuration options, refer to the official documentation.

## Logging configuration
Vault provides logging capabilities to help monitor its operations, troubleshoot issues, and analyze system behavior. By default, logs are sent to stdout, but they can also be written to a file.

To configure Vault to log to a file, specify the log file path and log level in the configuration:

 log_file = "/var/log/vault.log"
 log_level = "info"

To ensure Vault can write logs properly, adjust file permissions:

## Example configuration
Below is a complete example combining the above settings:

{{bc|1=
storage "file" {
    path = "/opt/vault/data"
}

listener "tcp" {
    address     = "127.0.0.1:8200"
    tls_disable = "true"
}

ui = true

api_addr = "http://127.0.0.1:8200"
cluster_addr = "http://127.0.0.1:8201"

disable_mlock = true

audit_device "file" {
    path   = "/var/log/vault-audit.log"
    format = "json"
}

log_file = "/var/log/vault.log"
log_level = "info"
}}

If using TLS:

{{bc|1=
storage "file" {
    path = "/opt/vault/data"
}

listener "tcp" {
    address     = "127.0.0.1:8200"
    tls_disable = "false"
    tls_cert_file = "/etc/vault/vault-cert.pem"
    tls_key_file  = "/etc/vault/vault-key.pem"
}

ui = true

api_addr = "https://127.0.0.1:8200"
cluster_addr = "https://127.0.0.1:8201"

disable_mlock = true

audit_device "file" {
    path   = "/var/log/vault-audit.log"
    format = "json"
}

log_file = "/var/log/vault.log"
log_level = "info"
}}

## Creating the storage directory
 # mkdir -p /opt/vault/data
 # chown -R vault:vault /opt/vault

## Running Vault as a systemd service
Optionally, Vault can be run as a systemd service to ensure it starts automatically at boot, restarts upon failure, and integrates well with process management on Linux. This approach is particularly useful in production environments where Vault needs to remain available without manual intervention.

## Creating the systemd service file
Create a unit file:

Next, enable/start the .

## Usage
## Setting environment variables
Set the environment variable to specify the Vault address. This ensures that Vault commands interact with the correct server instance without requiring the address to be manually specified each time.

 $ export VAULT_ADDR='http://127.0.0.1:8200'

To make this persistent across reboots:

## Initializing vault
Vault encrypts and protects secrets, requiring an "unsealing" process to decrypt and access them after a restart. When initialized, Vault generates multiple unseal keys, and a minimum threshold of these keys is needed to unseal the Vault. This ensures that no single person has full access, adding an extra layer of security.

To initialize Vault, run:

 $ vault operator init

This will output 5 unseal keys and an initial root token. Save these securely!

## Unseal the vault and login
## Automatic unsealing
Vault can be configured to auto-unseal using cloud-based KMS services (such as AWS KMS, GCP KMS) or hardware security modules (HSMs). This eliminates the need for manual key entry upon startup. For more info refer to the official Vault auto-unseal documentation.

## Manual unsealing
For manual unsealing, Vault must be unsealed with at least three different keys:

 $ vault operator unseal unseal-key-1
 $ vault operator unseal unseal-key-2
 $ vault operator unseal unseal-key-3

## Login to the vault
 $ vault login root-token

## Accessing the UI
Open http://127.0.0.1:8200 in your browser.

You will see a login screen where you can use your root token to access the Vault UI.
