# Systemd-creds

systemd-creds is a utility and service provided by systemd, designed to securely store and retrieve credentials used by systemd units. It aims to simplify the management of sensitive information, such as usernames, passwords, API keys, and other authentication data, required by various services and applications.

See https://systemd.io/CREDENTIALS/ and  for more information.

## Credential encryption
Credentials may optionally be encrypted and authenticated, either with a key derived from a local TPM2 chip, or one stored in , or both (the default) if available. To check if your system uses TPM2 encryption or only the key stored in , run

To encrypt a secret stored in , run

 # systemd-creds --name=foobar encrypt plaintext.txt ciphertext.cred

Encrypted credentials carry the intended name in them, so they cannot be mispurposed. If you omit , then the filename will be used as credential name.

You can check that encryption was successful with

 # shred -u plaintext.txt
 # systemd-run --pipe --wait --property=LoadCredentialEncrypted=foobar:$(pwd)/ciphertext.cred systemd-creds cat foobar

Without using  above, the correct command would be

 # systemd-run --pipe --wait --property=LoadCredentialEncrypted=ciphertext.cred:$(pwd)/ciphertext.cred systemd-creds cat ciphertext.cred

Alternatively, you can use  to provide the secret without first writing it to disk. The  switch allows outputting a credential in a format ready to be included in a service file:

 # systemd-ask-password -n | systemd-creds encrypt --name=mysql-password -p - -
 🔐 Password: ***************
 SetCredentialEncrypted=mysql-password: \
        k6iUCUh0RJCQyvL8k8q1UyAAAAABAAAADAAAABAAAAD42X4T5h86ynMHG5MAAAAAgAAAA \
        AAAAAALACMA8AAAACAAAAAAngAgws4cwpkrOvpxVf4/GSyOYCoQ4dmPs3Vcfg3D0eH/Ov \
        cAEC/U9JTyeHgktYBDl8U5jOq/NqFX3IPc24EX7aeTevsL6OKwlTDcF04W1M6eodqngRo \
        1JfRqHWnSfVHHYVXgMjIkWT4AcC0OoqAzQobK5e5G1zjTPygiG/ewGttY9sueKCL/INUu \
        n1e6/QB6D9T0x9Sl18CeBtoASepCAE4ACAALAAAAEgAgY9RHOefBR+mMgV/Frr+UzQX1S \
        IsLFItIbfB6Ep76It0AEAAgKH2Tduip205Dw0GVkME+yvOUNYVhnSHYqWHQoxelKrdj1E \
        c558FH6YyBX8Wuv5TNBfVIiwsUi0ht8HoSnvoi3QAAAAA3WzuXTYG2OFX9wFo740b3YjE \
        ZtiCWakoAOxzX+D/vIFyB3INROxpfXUCV7LY4eRITI9PJZiE6lGn4kjZBnbUf47yo1WDG \
        Wg==

Edit the service file to include the relevant credential

## User credential encryption
The systemd-creds utility can also be used by a regular user.

 $ echo -n hunter2 | systemd-creds --user encrypt - ciphertext.cred
 $ systemd-creds --user decrypt ciphertext.cred
 hunter2

As mentioned in , the user's scope and the  are used to encrypt the credential. For example, a root user may decrypt it, but only matching the user scope:

 $ systemd-creds --uid anotheruser decrypt ciphertext.cred
 Failed to decrypt: io.systemd.InteractiveAuthenticationRequired
 # systemd-creds decrypt ciphertext.cred
 Encrypted file is scoped to a user, but no user selected.
 # systemd-creds --uid user decrypt ciphertext.cred
 hunter2
