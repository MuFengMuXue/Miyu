# SHA hashes

The Secure Hash Algorithms (SHA) are a set of hash functions, frequently used for a large variety of purposes.

Some examples of usage of the SHA hash functions in Arch Linux are:
* Verifying the integrity of the Arch Linux ISO and packages,
* Pinning software revisions with git,
* Securing and verifying cryptographic keys, for example disc encryption,
* Data integrity and resource management of file systems, for example btrfs, and
* Password verification, covered in Security#Password hashes and this article for SHA hashes.

## SHA password hashes
By default Arch Linux used SHA-512 for passwords with package  releases from 4.1.4.3-3 (see bug 13591) to 4.14.0 (see yescrypt ). It replaced the older MD5 hash function, which has been found compromised by collision vulnerabilities. See wikipedia:Secure Hash Algorithms#Comparison of SHA functions for more information.

## Configuration
The SHA-512 password hashing can be configured with the
 option to improve key strengthening. For example,  means that an attacker has to compute 65536 hashes for each password they test against the hash in the  password file.

Therefore the attacker will be delayed by a factor of 65536. This also means that your computer must compute 65536 hashes every time you log in, but even on slow computers that takes less than one second.

Since  release 1.6.0 the SHA-512  option can be configured by either editing the  file and setting an value for the  parameter, or editing  and adding the  with an appropriate value.If you do not use the  option, PAM will use a [https://github.com/linux-pam/linux-pam/blob/1e2c6cecf81dcaeea0c2c9d37bc35eea120cd77d/modules/pam_unix/support.c#L222-L241C15 default different to the  rounds example commented in .

For example:

For a more detailed explanation of the  password options check the  man page.

## Usage
Even though you have changed the encryption settings, your passwords are not automatically re-hashed. To fix this, you must reset all user passwords so that they can be re-hashed.

As root issue the following command,

 # passwd username

where  is the name of the user whose password you are changing. Then re-enter their current password, and it will be re-hashed.

To verify that your passwords have been re-hashed, check the  file as root. Passwords hashed with SHA-256 begin with a , passwords hashed with SHA-512 will begin with  and yescrypt hashes with .
