# Security

This article contains recommendations and best practices for hardening an Arch Linux system.

## Concepts
* It is possible to tighten security to the point where the system is unusable. Security and convenience must be balanced. The trick is to create a secure and useful system.
* The biggest threat is, and will always be, the user.
* The principle of least privilege: Each part of a system should only be able to access what is strictly required, and nothing more.
* Defense in depth: Security works better in independent layers. When one layer is breached, another should stop the attack.
* Be a little paranoid. And be suspicious. If anything sounds too good to be true, it probably is!
* You can never make a system 100% secure unless you unplug the machine from all networks, turn it off, lock it in a safe, smother it in concrete and never use it.
* Prepare for failure. Create a plan ahead of time to follow when your security is broken.

## Passwords
Passwords are key to a secure system. They secure your user accounts, encrypted filesystems, and SSH/GPG keys. They are the main way a computer chooses to trust the person using it, so a big part of security is just about picking secure passwords and protecting them.

## Choosing secure passwords
Passwords must be complex enough to not be easily guessed from e.g. personal information, or cracked using methods like brute-force attacks. The tenets of strong passwords are based on length and randomness. In cryptography the quality of a password is often referred to as its entropy.

Insecure passwords include those containing or those using as a base before substitution/variation:

* Personally identifiable information (e.g., your dog's name, date of birth, area code, favorite video game)
* Simple character substitutions on words (e.g., ), as modern dictionary attacks can easily work with these
* Root "words" or common strings followed or preceded by added numbers, symbols, or characters (e.g., )
* Common phrases or short strings of common dictionary words (e.g. ) including with character substitution (e.g. ) (See Diceware below for when a combination of dictionary words can be secure)
* Any of the most common passwords

The best choice for a password is something long (the longer, the better) and generated from a random source. It is important to use a long password. Weak hash algorithms allow an 8-character password hash to be compromised in just a few hours.

Tools like  or  can generate random passwords. However, these passwords can be difficult to memorize. One memorization technique (for ones often typed) is to generate a long password and memorize a minimally secure number of characters, temporarily writing down the full generated string. Over time, increase the number of characters typed - until the password is ingrained in muscle memory and need not be remembered. This technique is more difficult, but can provide confidence that a password will not turn up in wordlists or "intelligent" brute force attacks that combine words and substitute characters.

Apart from password management,  offers password/passphrase generation. It is possible to customize the generation in a GUI. Dictionary based passphrases are also supported.

One technique for memorizing a password is to use a mnemonic phrase, where each word in the phrase reminds you of the next character in the password.
Take for instance “the girl is walking down the rainy street” could be translated to  or, less simply, .
This approach could make it easier to remember a password, but note that the various letters have very different probabilities of being found at the start of words (Wikipedia:Letter frequency).

Another effective technique can be to write randomly generated passwords down and store them in a safe place, such as in a wallet, purse, or document safe. Most people do a generally good job of protecting their physical valuables from attack, and it is easier for most people to understand physical security best practices compared to digital security practices.

It is also very effective to combine the mnemonic and random technique by saving long randomly generated passwords with a password manager, which will be in turn accessed with a memorable "master password"/primary password that must be used only for that purpose. The master password must be memorized and never saved. This requires the password manager to be installed on a system to easily access the password (which could be seen as an inconvenience or a security feature, depending on the situation). Some password managers also have smartphone apps which can be used to display passwords for manual entry on systems without that password manager installed (if that is a common use case, you could still use easily typeable but secure passwords for each service instead of completely random ones, see below). Note that a password manager introduces a single point of failure if you ever forget the master password.
Some password managers compute the contained passwords based on the master password and the service name where you want to log in instead of encrypting them, making it possible to use it on a new system without syncing any data.

It can be effective to use a memorable long series of unrelated words as a password. The theory is that if a sufficiently long phrase is used, the gained entropy from the password's length can counter the lost entropy from the use of dictionary words. This xkcd comic demonstrates the entropy tradeoff of this method, taking into account the limited set of possible words for each word in the passphrase. If the set of words you choose from is large (multiple thousand words) and you choose 5-7 or even more random words from it, this method provides great entropy, even assuming the attacker knows the set of possible words chosen from and the number of words chosen. The number of possible passphrases after settling on a set of words and number of words is: (number of words in the set of words to select from) to the power of (the number of words chosen for the passphrase). See e.g. Diceware for more.

See The passphrase FAQ or Wikipedia:Password strength for some additional background.

## Maintaining passwords
Once you pick a strong password, be sure to keep it safe. Watch out for keyloggers (software and hardware), screen loggers, social engineering, shoulder surfing, and avoid reusing passwords so insecure servers cannot leak more information than necessary. Password managers can help manage large numbers of complex passwords: if you are copy-pasting the stored passwords from the manager to the applications that need them, make sure to clear the copy buffer every time, and ensure they are not saved in any kind of log (e.g. do not paste them in plain terminal commands, which would store them in files like ). Note that password managers that are implemented as browser extensions may be vulnerable to side channel attacks. These can be mitigated by using password managers that run as separate applications.

As a rule, do not pick insecure passwords just because secure ones are harder to remember. Passwords are a balancing act. It is better to have an encrypted database of secure passwords, guarded behind a key and one strong master password, than it is to have many similar weak passwords. Writing passwords down is perhaps equally effective avoiding potential vulnerabilities in software solutions while requiring physical security.

Another aspect of the strength of the passphrase is that it must not be easily recoverable from other places.

If you use the same passphrase for disk encryption as you use for your login password (useful e.g. to auto-mount the encrypted partition or folder on login), make sure that  ends up on an encrypted partition or/and uses a strong key derivation function (i.e. yescrypt/argon2 or sha512 with PBKDF2, but not md5 or low iterations in PBKDF2) for the stored password hash (see SHA password hashes for more information).

If you are backing up your password database, make sure that each copy is not stored behind any other passphrase which in turn is stored in it, e.g. an encrypted drive or an authenticated remote storage service, or you will not be able to access it in case of need; a useful trick is to protect the drives or accounts where the database is backed up using a simple cryptographic hash of the master password. Maintain a list of all the backup locations: if one day you fear that the master passphrase has been compromised you will have to change it immediately on all the database backups and the locations protected with keys derived from the master password.

Version-controlling the database in a secure way can be very complicated: if you choose to do it, you must have a way to update the master password of all the database versions. It may not always be immediately clear when the master password is leaked: to reduce the risk of somebody else discovering your password before you realize that it leaked, you may choose to change it on a periodical basis. If you fear that you have lost control over a copy of the database, you will need to change all the passwords contained in it within the time that it may take to brute-force the master password, according to its entropy.

## Password hashes
A hash is a one-way function, i.e. it is designed to make it impossible to deduct the input without computing the hash function with it (example: MD5, SHA).

A password-hash function is designed to make deducting a user-input (password) impossible without computing the hash function with it (example: bcrypt). A key derivation function (KDF; examples: yescrypt, scrypt, PBKDF2) is a cryptographic algorithm designed to derive secret keys (e.g. an AES key, a password hash) from an input (a master key, a password). Hence, a KDF can serve multiple applications, including those of a password-hash function.

By default, Arch stores the hashed user passwords in the root-only-readable  file, separated from the other user parameters stored in the world-readable  file, see Users and groups#User database. See also #Restricting root.

Passwords are set with the passwd command, which stretches them with the system's crypt function and then saves them in . The passwords are also salted in order to defend them against rainbow table attacks. See also [https://www.slashroot.in/how-are-passwords-stored-linux-understanding-hashing-shadow-utils How are passwords stored in Linux (Understanding hashing with shadow utils).

Since password hashes follow a defined format, the method and parameter can be configured for subsequent new invocations of the passwd command. Hence, the individual hashes stored in the  file can be a heterogeneous mix of the hash functions supported by the system.

See  for more information on the format, hashing methods and parameters.

The  file configures the default password hashing method  and its parameter .

For example, an increment of the default  parameter will lead to a logarithmic increase of the compute time required to deduce the hash from a password. This applies, likewise, to a third-party trying to obtain the password secret, and the system to authenticate a user log-in.

In contrast, the compute time for the SHA-512 hash function is configured by a parameter with a linear influence. See SHA password hashes for information on the previous Arch default. Note the yescrypt algorithm internally uses SHA-256, HMAC and PBKDF2 to compute its password-hash. The main reason is to combine positive attributes of these widely used and tested functions for an enhanced resistance to attacks. For example, the usability of SHA for various purposes has resulted in hardware support for the function, i.e. the performance to compute a pure SHA hash has accelerated considerably, making its application as a password-hash function more and more derelict.

## Disallow empty passwords
## Enforcing strong passwords with pam_pwquality
PAM stands for the Pluggable Authentication Modules. pam_pwquality provides protection against Dictionary attacks and helps configure a password policy that can be enforced throughout the system. It is based on pam_cracklib, so it is backwards compatible with its options.

Install the  package.

If for example you want to enforce this policy:

* prompt 2 times for password in case of an error (retry option)
* 10 characters minimum length (minlen option)
* at least 6 characters should be different from old password when entering a new one (difok option)
* at least 1 digit (dcredit option)
* at least 1 uppercase (ucredit option)
* at least 1 lowercase (lcredit option)
* at least 1 other character (ocredit option)
* cannot contain the words "myservice" and "mydomain"
* enforce the policy for root

Edit the  file to read as:

The  instructs the pam_unix module to not prompt for a password but rather to use the one provided by pam_pwquality.

You can refer to the  and  man pages for more information.

## CPU
## Microcode
See microcode for information on how to install important security updates for your CPU's microcode.

## Hardware vulnerabilities
Some CPUs contain hardware vulnerabilities. See the kernel documentation on hardware vulnerabilities for a list of these vulnerabilities, as well as mitigation selection guides to help customize the kernel to mitigate these vulnerabilities for specific usage scenarios.

To check if you are affected by a known vulnerability, run the following:

 $ grep -r . /sys/devices/system/cpu/vulnerabilities/

In most cases, updating the kernel and microcode will mitigate vulnerabilities.

## Simultaneous multithreading (hyper-threading)
Simultaneous multithreading (SMT), also called hyper-threading on Intel CPUs, is a hardware feature that may be a source of L1 Terminal Fault and Microarchitectural Data Sampling vulnerabilities. The Linux kernel and microcode updates contain mitigations for known vulnerabilities, but disabling SMT may still be required on certain CPUs if untrusted virtualization guests are present.

SMT can often be disabled in your system's firmware. Consult your motherboard or system documentation for more information. You can also disable SMT in the kernel by adding the following kernel parameter:

 mitigations=auto,nosmt

## Memory
## Hardened malloc
 is a hardened replacement for glibc's malloc(). The project was originally developed for integration into Android's Bionic and musl by Daniel Micay, of GrapheneOS, but he has also built in support for standard Linux distributions on the x86_64 architecture.

## Storage
## Data-at-rest encryption
Data-at-rest encryption, preferably full-disk encryption with a strong passphrase, is the only way to guard data against physical recovery. This provides data confidentiality when the computer is turned off or the disks in question are unmounted.

Once the computer is powered on and the drive is mounted, however, its data becomes just as vulnerable as an unencrypted drive. It is therefore best practice to unmount data partitions as soon as they are no longer needed.

You may also encrypt a drive with the key stored in a TPM, although it has had vulnerabilites in the past and the key can be extracted by a bus sniffing attack.

Certain programs, like dm-crypt, allow the user to encrypt a loop file as a virtual volume. This is a reasonable alternative to full-disk encryption when only certain parts of the system need to be secure.

While the block-device or filesystem-based encryption types compared in the data-at-rest encryption article are useful at protecting data on physical media, most can not be used to protect data on a remote system that you can not control (such as cloud storage). In some cases, individual file encryption will be useful.

These are some methods to encrypt files:

* Some archiving and compressing tools also provide basic encryption. Some examples are 7-Zip ( flag),  ( flag). The encryption should only be relied on particular care, because the tools may use custom algorithms for cross-platform compatibility.* GnuPG can be used to encrypt files.
*  is a simple and easy to use file encryption tool. It also supports multiple recipients and encryption using SSH keys, which is useful for secure file sharing.

## File systems
The kernel now prevents security issues related to hardlinks and symlinks if the  and  sysctl switches are enabled, so there is no longer a major security benefit from separating out world-writable directories.

File systems containing world-writable directories can still be kept separate as a coarse way of limiting the damage from disk space exhaustion. However, filling  or  is enough to take down services. More flexible mechanisms for dealing with this concern exist (like quotas), and some file systems include related features themselves (Btrfs has quotas on subvolumes).

## Mount options
Following the principle of least privilege, file systems should be mounted with the most restrictive mount options possible (without losing functionality).

Relevant mount options are:

* : Do not interpret character or block special devices on the file system.
* : Do not allow set-user-identifier or set-group-identifier bits to take effect.
* : Do not allow direct execution of any binaries on the mounted file system.
** Setting  on  disallows executable scripts and breaks Wine, Steam, PyCharm, .NET, etc.
*** Wine does not need the  flag for opening Windows binaries. It is only needed when Wine itself is installed in .
*** To keep Steam working you can mount  as  in fstab by adding the following:
** Some packages (building  for example) may require  on .

File systems used for data should always be mounted with ,  and .

Potential file system mounts to consider:

*
*
*
*
*

## Snapshots
When utilizing file system snapshots, e.g. with Btrfs, LVM, or ZFS, it is essential to be aware that snapshots may retain sensitive information that users expect to be deleted. This is especially true when automatic snapshotting tools like Snapper are configured, as they can capture snapshots at regular intervals or in response to system events. Here are some examples of how sensitive information in  can persist within snapshots:

* Deleted files and directories: Even though files or directories are deleted from the file system, they may still exist within older snapshots. This is expected most of the time, but consider whether files and directories such as , , etc. should be retained.
* Temporary files and cache: Temporary files and cached data generated by applications may be included in snapshots. For example, files kept in encrypted directories might generate thumbnails () or work copies when opened, which might in turn be included in snapshots. The same applies e.g. to browsing history (, , etc.), which could have been included in a snapshot before being purged.

If this is supported, consider excluding such directories from snapshots altogether. For example, if using Btrfs, you can create subvolumes for example , , ,  or any other directory according to your use-case.

## File access permissions
The default file permissions allow read access to almost everything and changing the permissions can hide valuable information from an attacker who gains access to a non-root account such as the  or  users. You can use chmod to take away all permissions from the group and others:

 # chmod go-r path_to_hide

Some paths to consider are:

* : The boot directory, which may include traditional vmlinuz and initramfs images, or a Unified kernel image. Note that safe permissions are used by default when using systemd#GPT partition automounting.
* : The nftables configuration, applicable to  and .
* : The legacy iptables configuration, applicable to .

The default umask  can be changed to improve security for newly created files. The [https://apps.nsa.gov/iaarchive/library/ia-guidance/security-configuration/operating-systems/guide-to-the-secure-configuration-of-red-hat-enterprise.cfm NSA RHEL5 Security Guide suggests a umask of  for maximum security, which makes new files not readable by users other than the owner. To change this, see Umask#Set the mask value. If you use sudo, consider configuring it to use the default root umask.

## SUID and SGID files
It is important to be aware of any files with the Setuid or Setgid bit. Examples of relevant files with the SUID bit set:

* unix_chkpwd
* chage, expiry, gpasswd, groupmems, passwd, sg ()
* fusermount3, fusermount2
* pkexec
* ssh-keysign
* chfn, chsh, mount, newgrp, umount, wall, write ()
* sudo, , doas, su, su-rs, ksu
* firejail
* dbus-daemon-launch-helper
* chromium-sandbox
* Xorg.wrap

The prominent risks of such executable files include privilege escalation vulnerabilities, see e.g Wikipedia:Setuid#Security impact.Files with the SUID bit set and not owned by root, or files with the SGID bit set typically have less potential impact but can theoretically still do decent damage if vulnerable. It is usually possible to avoid using SUID or SGID by assigning Capabilities instead.

To search for files with either the SUID or SGID bit:

 $ find / -perm "/u=s,g=s" -type f 2>/dev/null

## Backups
Regularly create backups of important data. Regularly test the integrity of the backups. Regularly test that the backups can be restored.

Make sure that at least one copy of the data is stored offline, i.e. not connected to the system under threat in any way. Ransomware and other destructive attacks may also attack any connected backup systems.

## SATA SSD frozen mode
See Solid state drive#Setting the SATA SSD state to frozen mode after waking up from sleep.

## User setup
## Do not use the root account for daily use
Following the principle of least privilege, do not use the root user for daily use. Create a non-privileged user account for each person using the system. See List of applications/Security#Privilege elevation for ways of temporarily gaining privileged access.

## Enforce a delay after a failed login attempt
Add the following line to  to add a delay of at least 4 seconds between failed login attempts:

 is the time in microseconds to delay.

Other PAM modules besides  can also suggest such a delay; if multiple modules do so, PAM will use the longest one.

In particular, both  and  set a minimum delay of 2 seconds by default.
In order to completely remove this delay, you need to add the  parameter to any  lines of these modules, for example

## Lock out user after three failed login attempts
Since  20200721.1-2,  is enabled by default to lock out users for 10 minutes after 3 failed login attempts in a 15 minute period (see ). The lockout only applies to password authentication (e.g. login and sudo), public key authentication over SSH is still accepted. To prevent complete denial-of-service, this lockout is disabled for the root user by default.

To unlock a user, do:

 $ faillock --user username --reset

By default, the lock mechanism is a file per-user located at . Deleting or emptying the file unlocks that user—the directory is owned by root, but the file is owned by the user, so the  command only empties the file, therefore does not require root.

The module  can be configured with the file . The lockout parameters:

*  — the lockout time (in seconds, default 10 minutes).
*  — the time in which failed logins can cause a lockout (in seconds, default 15 minutes).
*  — the number of failed logins before lockout (default 3).

By default, all user locks are lost after reboot. If your attacker can reboot the machine, it is more secure if locks persist. To make locks persist, change the  parameter in  to .

No restart is required for changes to take effect. See  for further configuration options, such as enabling lockout for the root account, disabling for centralized login (e.g. LDAP), etc.

## Limit amount of processes
On systems with many, or untrusted users, it is important to limit the number of processes each can run at once, therefore preventing fork bombs and other denial of service attacks. The  configuration determines how many processes each user, or group can have open, and is empty (except for useful comments) by default. Adding the following lines to this file will limit all users to 100 active processes, unless they use the  command to explicitly raise their maximum to 200 for that session. These values can be changed according to the appropriate number of processes a user should have running, or the hardware of the box you are administrating.

 * soft nproc 100
 * hard nproc 200

The current number of threads for each user can be found with . This may help with determining appropriate values for the users' limits; see also limits.conf.

## Use Wayland
Prefer using Wayland over Xorg. Xorg's design predates modern security practices and is [https://security.stackexchange.com/questions/4641/why-are-people-saying-that-the-x-window-system-is-not-secure/4646#4646 considered insecure by many. For example, Xorg applications may record keystrokes while inactive.

If you must run Xorg, it is recommended to avoid running it as root. Within Wayland, the Xwayland compatibility layer will automatically use rootless Xorg.

## Restricting root
The root user is, by definition, the most powerful user on a system. It is also difficult to audit the root user account. It is therefore important to restrict usage of the root user account as much as possible. There are a number of ways to keep the power of the root user while limiting its ability to cause harm.

## Use sudo instead of su
Using sudo for privileged access is preferable to su for a number of reasons:

* It keeps a log of which normal privilege user has run each privileged command.
* The root user password need not be given out to each user who requires root access.
*  prevents users from accidentally running commands as root that do not need root access, because a full root terminal is not created. This aligns with the principle of least privilege.
* Individual programs may be enabled per user, instead of offering complete root access just to run one command.

See Sudo#Configuration.

## Editing files using sudo
See Sudo#Editing files. Alternatively, you can use editors like  or  which have restricted capabilities in order to be safe to run as root.

## Restricting root login
Once sudo is properly configured, full root access can be heavily restricted or denied without losing much usability. To disable root, but still allowing to use sudo, you can use  with .

## Allow only certain users
The PAM  lets you allow only users in the group  to login using su. See su#su and wheel.

## Denying SSH login
Even if you do not wish to deny root login for local users, it is always good practice to deny root login via SSH. The purpose of this is to add an additional layer of security before a user can completely compromise your system remotely.

## Specify acceptable login combinations with access.conf
When someone attempts to log in with PAM,  is checked for the first combination that matches their login properties. Their attempt then fails or succeeds based on the rule for that combination.

 +:root:LOCAL
 -:root:ALL

Rules can be set for specific groups and users. In this example, the user archie is allowed to login locally, as are all users in the wheel and adm groups. All other logins are rejected:

 +:archie:LOCAL
 +:(wheel):LOCAL
 +:(adm):LOCAL
 -:ALL:ALL

Read more at

## Mandatory access control
Mandatory access control (MAC) is a type of security policy that differs significantly from the discretionary access control (DAC) used by default in Arch and most Linux distributions. MAC essentially means that every action a program could perform that affects the system in any way is checked against a security ruleset. This ruleset, in contrast to DAC methods, cannot be modified by users. Using virtually any mandatory access control system will significantly improve the security of your computer, although there are differences in how it can be implemented.

## Pathname MAC
Pathname-based access control is a simple form of access control that offers permissions based on the path of a given file. The downside to this style of access control is that permissions are not carried with files if they are moved around the system. On the positive side, pathname-based MAC can be implemented on a much wider range of filesystems, unlike labels-based alternatives.

* AppArmor is a Canonical-maintained MAC implementation seen as an "easier" alternative to SELinux.
* TOMOYO is another simple, easy-to-use system offering mandatory access control. It is designed to be both simple in usage and in implementation, requiring very few dependencies.

## Labels MAC
Labels-based access control means the extended attributes of a file are used to govern its security permissions. While this system is arguably more flexible in its security offerings than pathname-based MAC, it only works on filesystems that support these extended attributes.

* SELinux, based on an NSA project to improve Linux security, implements MAC completely separate from system users and roles. It offers an extremely robust multi-level MAC policy implementation that can easily maintain control of a system that grows and changes past its original configuration.

## Access Control Lists
Access Control Lists (ACLs) are an alternative to attaching rules directly to the filesystem in some way. ACLs implement access control by checking program actions against a list of permitted behavior.

## Kernel hardening
## Kernel self-protection / exploit mitigation
The  package uses a basic kernel hardening patch set and more security-focused compile-time configuration options than the  package. A custom build can be made to choose a different compromise between security and performance than the security-leaning defaults.

However, it should be noted that several packages (such as ) will not work when using this kernel.

If you use an out-of-tree driver such as NVIDIA, you may need to switch to its DKMS package.

## Userspace ASLR comparison
The  package provides an improved implementation of Address Space Layout Randomization for userspace processes. The  command can be used to obtain an estimate of the provided entropy:

## 64-bit processes
## 32-bit processes (on an x86_64 kernel)
## Restricting access to kernel pointers in the proc filesystem
Setting  to 1 will hide kernel symbol addresses in  from regular users without , making it more difficult for kernel exploits to resolve addresses/symbols dynamically. This will not help that much on a pre-compiled Arch Linux kernel, since a determined attacker could just download the kernel package and get the symbols manually from there, but if you are compiling your own kernel, this can help mitigating local root exploits. This will break some  commands when used by non-root users (but many  features require root access anyway). See  for more information.

Setting  to 2 will hide kernel symbol addresses in  regardless of privileges.

## BPF hardening
BPF is a system used to load and execute bytecode within the kernel dynamically during runtime. It is used in a number of Linux kernel subsystems such as networking (e.g. XDP, tc), tracing (e.g. kprobes, uprobes, tracepoints) and security (e.g. seccomp). It is also useful for advanced network security, performance profiling and dynamic tracing.

BPF was originally an acronym of Berkeley Packet Filter since the original classic BPF was used for packet capture tools for BSD. This eventually evolved into Extended BPF (eBPF), which was shortly afterwards renamed to just BPF (not an acronym). BPF should not be confused with packet filtering tools like iptables or netfilter, although BPF can be used to implement packet filtering tools.

BPF code may be either interpreted or compiled using a Just-In-Time (JIT) compiler. The Arch kernel is built with  which disables the BPF interpreter and forces all BPF to use JIT compilation. This makes it harder for an attacker to use BPF to escalate attacks that exploit SPECTRE-style vulnerabilities. See the kernel patch which introduced CONFIG_BPF_JIT_ALWAYS_ON for more details.

The kernel includes a hardening feature for JIT-compiled BPF which can mitigate some types of JIT spraying attacks at the cost of performance and the ability to trace and debug many BPF programs. It may be enabled by setting  to  (to enable hardening of unprivileged code) or  (to enable hardening of all code).

See the  settings in the kernel documentation for more details.

## ptrace scope
The  syscall provides a means by which one process (the "tracer") may observe and control the execution of another process (the "tracee"), and examine and change the tracee's memory and registers.  is commonly used by debugging tools including gdb, strace, perf, reptyr and other debuggers. However, it also provides a means by which a malicious process can read data from and take control of other processes.

Arch enables the Yama LSM by default, which provides a  kernel parameter. This parameter is set to  (restricted) by default which prevents tracers from performing a  call on traces outside of a restricted scope unless the tracer is privileged or has the  capability. This is a significant improvement in security compared to the classic permissions. Without this module, there is no separation between processes running as the same user (in the absence of additional security layers such as ).

If you do not need to use debugging tools, consider setting  to  (admin-only) or  (no  possible) to harden the system.

## hidepid
The kernel has the ability to hide other users' processes, normally accessible via , from unprivileged users by mounting the  filesystem with the  and  options documented in https://docs.kernel.org/filesystems/proc.html.

This greatly complicates an intruder's task of gathering information about running processes, whether some daemon runs with elevated privileges, whether other user runs some sensitive program, whether other users run any program at all, makes it impossible to learn whether any user runs a specific program (given the program does not reveal itself by its behaviour), and, as an additional bonus, poorly written programs passing sensitive information via program arguments are now protected against local eavesdroppers.

The  group, provided by the  package, acts as a whitelist of users authorized to learn other users' process information. If users or services need access to  directories beyond their own, add them to the group.

For example, to hide process information from other users except those in the  group:

For user sessions to work correctly, an exception needs to be added for systemd-logind:

## Restricting module loading
The default Arch kernel has  enabled, which signs all kernel modules built as part of the  package. This allows the kernel to only load modules signed with a valid key, i.e. out-of-tree modules compiled locally or provided by packages such as  cannot be loaded. You can use  to verify currently loaded modules have signatures; verifying the signatures by hand is slightly more involved Kernel module loading can be restricted by setting the  kernel parameter. More information can be found in the [https://docs.kernel.org/admin-guide/module-signing.html kernel documentation.

Further, unneeded individual modules can be blacklisted, see secureblue for examples.

## Disable kexec
Kexec allows replacing the current running kernel.

## Kernel lockdown mode
Linux supports an optional lockdown feature, intended to strengthen the boundary between UID 0 (root) and the kernel. When enabled some applications may cease to work which rely on low-level access to either hardware or the kernel.

To use lockdown, its LSM must be initialized and a lockdown mode must be set.

All officially supported kernels initialize the LSM, but none of them enforce any lockdown mode.

Lockdown has two modes of operation:

* : kernel features that allow userland to modify the running kernel are disabled (e.g. kexec, bpf).
* : kernel features that allow userland to extract confidential information from the kernel are also disabled.

It is recommended to use , unless your specific threat model dictates otherwise.

To enable kernel lockdown at runtime, run:

 # echo mode > /sys/kernel/security/lockdown

To enable kernel lockdown on boot, use the kernel parameter .

See also .

## Linux Kernel Runtime Guard (LKRG)
LKRG () is a kernel module which performs integrity checking of the kernel and detection of exploit attempts.

## Disable emergency shell
The emergency shell is used to interactively troubleshoot the machine during the boot process. However, it is also a gadget that an attacker can use to access secure resources such as the TPM. See this article for a practical example. The difficulty of attacks can be increased by disabling the emergency shell, at the tradeoff of removing a tool to troubleshoot early boot failures.

To disable the emergency shell, See systemd#Disable emergency mode on remote machine.

## Sandboxing applications
See also Wikipedia:Sandbox (computer security).

To improve the security of systemd service units, see systemd/Sandboxing.

To mitigate this, either:

* use the  kernel which has the safe default, or
* set the  sysctl to .

Note that this can break applications such as . Chromium based applications need SUID bit for  to work with this setting.

## Firejail
Firejail is an easy to use tool for sandboxing applications and servers alike. It was originally created for browsers and internet facing applications, but supports a large number of applications by now. To establish a sandboxed environment with a variety of features, it is installed as a suid binary and builds a sandboxed runtime environment for the target application based on black and white lists.

## bubblewrap
bubblewrap is a sandbox application developed for unprivileged container tools like Flatpak with a significantly smaller resource footprint and complexity than Firejail. While it lacks certain features such as file path whitelisting, bubblewrap does offer bind mounts as well as the creation of user/IPC/PID/network/cgroup namespaces and can support both simple and complex sandboxes. For the  kernel you will need to to use .

Bubblejail sandbox is based on bubblewrap and provides a resource oriented permission model with a graphical interface to tweak permissions.

## Portable
Portable is a sandboxing framework which utilizes bubblewrap and many other tools to lockdown running applications. It is designed to be simple for packagers and efficient for users, yet cuts off security holes and monitors background processes by default.

See portable-arch for a repository of applications sandboxed by portable.

If a sandboxed application does not utilize the Portal file chooser, portable can pass files to the sandbox (by passing ).

Portable is fully functional on GNOME, while other desktops may lack small amounts of features like advanced background monitoring and ScreenShot portal.

## chroots
Manual chroot jails can also be constructed to build sandboxed process environments. It is much more limited than other sandboxing technologies; the extent of its sandboxing is file path isolation.

## Linux containers
Linux Containers are another good option when you need more separation than the other options (short of full system virtualization) provide. LXC is run on top of the existing kernel in a pseudo-chroot with their own virtual hardware.

## gVisor
The gVisor project, led by Google, is providing a sandboxing application with a focus on containers following the OCI initiative, such as Docker and Kubernetes. It isolates containers and individual applications from the host by intercepting a majority of system calls to the kernel and presenting itself as guest kernel.

A key difference to other intercepting sandboxing projects is that gVisor re-implements system calls in the Go programming language, as described in its design overview. Details for the list of re-implemented syscalls support can be seen in git. For usage examples, limitations and special features see the project documentation.

The application is available as  and .

## Full virtualization options
Using full virtualization options such as VirtualBox, KVM, Xen or Qubes OS (based on Xen) can also improve isolation and security in the event you plan on running risky applications or browsing dangerous websites.

## Network and firewalls
## Firewalls
While the stock Arch kernel is capable of using Netfilter's iptables and nftables, the services are not enabled by default. It is highly recommended to set up some form of firewall to protect the services running on the system. Many resources (including ArchWiki) do not state explicitly which services are worth protecting, so enabling a firewall is a good precaution.

* See iptables and nftables for general information.
* See Simple stateful firewall for a guide on setting up an iptables firewall.
* See Firewalls for other ways of setting up netfilter.
* See Ipset for blocking lists of ip addresses, such as those from Bluetack.
*  is a configurable inbound and outbound firewall with support for configurable rules by application, port, host, etc.

A quick way to setup a basic firewall is to use the tool  (Uncomplicated Fire Wall). Then set  and  and enabling it with  and .

## Open ports
Some services listen for inbound traffic on open network ports. It is important to only bind these services to the addresses and interfaces that are strictly necessary. It may be possible for a remote attacker to exploit flawed network protocols to access exposed services. This can even happen with processes bound to localhost.

In general, if a service only needs to be accessible to the local system, bind to a Unix domain socket () or a loopback address such as  instead of a non-loopback address like .

If a service needs to be accessible to other systems via the network, control the access with strict firewall rules and configure authentication, authorization and encryption whenever possible.

You can list all current open ports with . To show all listening processes and their numeric tcp and udp port numbers:

 # ss -lpntu

See  for more options.

## Kernel parameters
Kernel parameters which affect networking can be set using Sysctl. For how to do this, see Sysctl#TCP/IP stack hardening.

## SSH
To mitigate brute-force attacks it is recommended to enforce key-based authentication. For OpenSSH see OpenSSH#Protection for more recommendations. Alternatively Fail2ban or Sshguard offer lesser forms of protection by monitoring logs and writing firewall rules but open up the potential for a denial of service, since an attacker can spoof packets as if they came from the administrator after identifying their address. Spoofing IP has lines of defense, such as by reverse path filtering and disabling ICMP redirects.

You may want to harden authentication even more by using two-factor authentication. Google Authenticator provides a two-step authentication procedure using one-time passcodes (OTP).

Denying root login is also a good practice, both for tracing intrusions and adding an additional layer of security before root access. For OpenSSH, see OpenSSH#Deny.

Mozilla publishes an OpenSSH configuration guide which configures more verbose audit logging and restricts ciphers.

## DNS
The default domain name resolution (DNS) configuration is highly compatible but has security weaknesses. See DNS privacy and security for more information.

## Proxies
Proxies are commonly used as an extra layer between applications and the network, sanitizing data from untrusted sources. The attack surface of a small proxy running with lower privileges is significantly smaller than a complex application running with the end user privileges.

For example the DNS resolver is implemented in , that is linked with the application (that may be running as root), so a bug in the DNS resolver might lead to a remote code execution. This can be prevented by installing a DNS caching server, such as dnsmasq, which acts as a proxy. === Managing TLS certificates ===

See TLS#Trust management.

## Physical security
Physical access to a computer is root access given enough time and resources. However, a high practical level of security can be obtained by putting up enough barriers.

An attacker can gain full control of your computer on the next boot by simply attaching a malicious IEEE 1394 (FireWire), Thunderbolt or PCI Express device as they are given full memory access by default.[https://web.archive.org/web/20210312083421/http://breaknenter.org/2014/09/inception-metasploit-integration/ For Thunderbolt, you can restrict the direct memory access completely or to known devices, see user device authorization. For Firewire and PCI Express, there is little you can do from preventing this, or modification of the hardware itself - such as flashing malicious firmware onto a drive. However, the vast majority of attackers will not be this knowledgeable and determined.

Data-at-rest encryption will prevent access to your data if the computer is stolen, but malicious firmware can be installed to obtain this data upon your next log in by a resourceful attacker.

## Locking down BIOS
Adding a password to the BIOS prevents someone from booting into removable media, which is basically the same as having root access to your computer. You should make sure your drive is first in the boot order and disable the other drives from being bootable if you can.

## Boot loaders
It is highly important to protect your boot loader. An unprotected boot loader can bypass any login restrictions, e.g. by setting the  kernel parameter to boot directly to a shell.

## Syslinux
Syslinux supports password-protecting your boot loader. It allows you to set either a per-menu-item password or a global boot loader password.

## GRUB
GRUB supports boot loader passwords as well. See GRUB/Tips and tricks#Password protection of GRUB menu for details. It also has support for encrypted /boot, which only leaves some parts of the boot loader code unencrypted. GRUB's configuration, kernel and initramfs are encrypted.

## systemd-boot
systemd-boot disables editing of kernel parameters when Secure Boot is enabled. Alternatively, you can set kernel parameters for password protection in systemd-boot for a more traditional password-based option.

## Secure Boot
Secure Boot is a feature of UEFI that allows authentication of the files your computer boots. This helps preventing some evil maid attacks such as replacing files inside the boot partition. Normally computers come with keys that are enrolled by vendors (OEM). However these can be removed and allow the computer to enter Setup Mode which allows the user to enroll and manage their own keys.

The secure boot page guides you through how to set secure boot up by using your own keys.

## Trusted Platform Module (TPM)
TPMs are hardware microprocessors which have cryptographic keys embedded. This forms the fundamental root of trust of most modern computers and allows end-to-end verification of the boot chain. They can be used as internal smartcards, attest the firmware running on the computer and allow users to insert secrets into a tamper-proof and brute-force resistant store.

## Boot partition on removable flash drive
One popular idea is to place the boot partition on a flash drive in order to render the system unbootable without it. Proponents of this idea often use full-disk encryption alongside, and some also use detached encryption headers placed on the boot partition.

This method can also be merged with encrypting /boot.

## Automatic logout
If you are using Bash or Zsh, you can set  for an automatic logout from shells after a timeout.

For example, the following will automatically log out from virtual consoles (but not terminal emulators in X11):

If you really want EVERY Bash/Zsh prompt (even within X) to timeout, use:

 $ export TMOUT="$(( 60*10 ))";

Note that this will not work if there is some command running in the shell (eg.: an SSH session or other shell without  support). But if you are using VC mostly for restarting frozen GDM/Xorg as root, then this is very useful.

## Protect against rogue USB devices
The kernel has settings to deactivate USB ports to protect your computer against rogue USB devices (a.k.a. BadUSB, PoisonTap or LanTurtle). They can be set at runtime and automated via sysctl.

For more control install USBGuard, which is a software framework implementing basic whitelisting and blacklisting capabilities based on device attributes.

## Volatile data collection
A computer that is powered on may be vulnerable to volatile data collection. It is a best practice to turn a computer completely off at times it is not necessary for it to be on, or if the computer's physical security is temporarily compromised (e.g. when passing through a security checkpoint).

## Packages
## Authentication
Attacks on package managers are possible without proper use of package signing, and can affect even package managers with proper signature systems. Arch uses package signing by default and relies on a web of trust from 5 trusted master keys. See Pacman-key for details.

## Upgrades
It is important to regularly upgrade the system.

## Follow vulnerability alerts
Subscribe to the Common Vulnerabilities and Exposure (CVE) Security Alert updates, made available by National Vulnerability Database, and found on the NVD Download webpage.

The tool  can be used to check for vulnerabilities affecting the running system. A graphical system tray, , can also be used. See also Arch Security Team.

You should also consider subscribing to the release notifications for software you use, especially if you install software through means other than the main repositories or AUR. Some software have mailing lists you can subscribe to for security notifications. Source code hosting sites often offer RSS feeds for new releases.

## Rebuilding packages
Packages can be rebuilt and stripped of undesired functions and features as a means to reduce attack surface. For example,  can be rebuilt without  in an attempt to circumvent CVE-2016-3189. Custom hardening flags can also be applied either manually or via a wrapper.

{| class="wikitable"
! Flag !! Purpose
|-
| -D_FORTIFY_SOURCE=2 || Run-time buffer overflow detection
|-
| -D_GLIBCXX_ASSERTIONS || Run-time bounds checking for C++ strings and containers
|-
| -fasynchronous-unwind-tables || Increased reliability of backtraces
|-
| -fexceptions || Enable table-based thread cancellation
|-
| -fpie -Wl,-pie || Full ASLR for executables
|-
| -fpic -shared || No text relocations for shared libraries
|-
| -fplugin=annobin || Generate data for hardening quality control
|-
| -fstack-clash-protection || Increased reliability of stack overflow detection
|-
| -fstack-protector, -fstack-protector-all or -fstack-protector-strong || Stack smashing protector
|-
| -grecord-gcc-switches || Store compiler flags in debugging information
|-
| -mcet -fcf-protection || Control flow integrity protection
|-
| -Werror=format-security || Reject potentially unsafe format string arguments
|-
| -Werror=implicit-function-declaration || Reject missing function prototypes
|-
| -Wl,-z,defs || Detect and reject underlinking
|-
| -Wl,-z,now || Disable lazy binding
|-
| -Wl,-z,relro || Read-only segments after relocation
|}

* Flags and info source
