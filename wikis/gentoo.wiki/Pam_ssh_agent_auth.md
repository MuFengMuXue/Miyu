**Resources**

[[]][Home](https://pamsshagentauth.sourceforge.net)

[[]][Package information](https://packages.gentoo.org/packages/sys-auth/pam_ssh_agent_auth)

**pam_ssh_agent_auth** is the [PAM](https://wiki.gentoo.org/wiki/PAM "PAM") module that allows a locally installed [SSH](https://wiki.gentoo.org/wiki/SSH "SSH") key to authenticate for [sudo](https://wiki.gentoo.org/wiki/Sudo "Sudo").

This is useful for those who are not happy with completely passwordless sudo, but do not want to be frequently typing passwords.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Create SSH keys]](#Create_SSH_keys)
    -   [[2.2] [PAM sudo file]](#PAM_sudo_file)
    -   [[2.3] [Add desired user\'s public key]](#Add_desired_user.27s_public_key)
    -   [[2.4] [Extra: Launch ssh-agent at login]](#Extra:_Launch_ssh-agent_at_login)
-   [[3] [See also]](#See_also)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask pam_ssh_agent_auth`

## [Configuration]

** Warning**\
This PAM module does not support FIDO2 keys.

### [Create SSH keys]

Have each user that would like this capability to follow the guide on the [SSH page](https://wiki.gentoo.org/wiki/SSH#Create_keys "SSH") to create SSH keys.

### [PAM sudo file]

Configure sudo to try using public keys, then fall back to normal password authentication:

[FILE] **`/etc/pam.d/sudo`**

    ...
    auth    sufficient  pam_ssh_agent_auth.so file=/etc/ssh/sudo_authorized_keys
    auth    include     system-auth
    account include     system-auth
    session include     system-auth
    ...

Configure sudoers to preserve the environment variable `SSH_AUTH_SOCK`:

[FILE] **`/etc/sudoers`**

    ...
    Defaults env_keep += "SSH_AUTH_SOCK"
    ...

### [][Add desired user\'s public key]

Repeat this process for each user desired for sudo authentication:

`root `[`#`]`cat /home/<user>/.ssh/*.pub >> /etc/ssh/sudo_authorized_keys`

### [Extra: Launch ssh-agent at login]

`user `[`$`]`echo "ssh-add" >> ~/.bash_profile`

## [See also]

-   [PAM](https://wiki.gentoo.org/wiki/PAM "PAM") --- allows (third party) services to provide an authentication module for their service which can then be used on PAM enabled systems.