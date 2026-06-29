# Ansible

From www.ansible.com:

:Ansible is a radically simple IT automation engine that automates cloud provisioning, configuration management, application deployment, intra-service orchestration, and many other IT needs.

## Installation
On the control machine (master), install the  package. Additionally, you can install the  package, which provides a range of community curated collections.

On the managed machines (nodes),  where you want to automate deployment or configuration tasks,  is required and it may be necessary to indicate the specific #Python binary location in some circumstances.  A way to communicate with the node is also necessary, this is usually SSH. Note that a functioning SSH key setup eases the use of Ansible but is not required.

## Basic usage
## Configuration
Ansible parameters are set in the configuration file which can either be  in the current directory,  in the home directory or , whichever it finds first.

A base config can be generated with:

 $ ansible-config init --disabled > ansible.cfg

## Inventory
The infrastructure is listed in the Ansible inventory file, which defaults to being saved in the location  or one can specify a different inventory file using the  command line switch. For instance, the following inventory defines a cluster with 7 nodes organized into two groups:

One can assign specific attributes to every node in the infrastructure file at the corresponding line or in the  configuration file.
By default Ansible executes playbooks over SSH, the  parameter extends the connection to:

*  to deploy the playbook to the control machine itself
*  deploys the playbook directly into Docker containers

Check Ansible - intro inventory for details.

## Ping
You may check if all the nodes listed in the inventory are alive by

 $ ansible all -m ping

## Playbook
Playbooks are the main organizational unit to configure and deploy the whole infrastructure.  Check the official document for more details.  Here is an extremely simple demonstration, where the administrator of the above inventory wants to perform a full system upgrade on a set of Arch Linux hosts. First, create a playbook file, with YAML formatting (always 2 spaces indentation):

Then, run the playbook script:

 $ ansible-playbook --ask-become-pass syu.yml

## Vault
A vault can be used to keep sensitive data in an encrypted form in playbooks or roles, rather than in plaintext.  The vault password can be stored in plaintext in a file, for example  containing , to be used later on as a command parameter:

 $ ansible-playbook site.yml --vault-id vault_pass.txt

In order to encrypt the content  of a variable named  using the password stored in , the following command should be used:

 $ ansible-vault encrypt_string --vault-id vault_pass.txt 'the var content' --name varname

More securely, to avoid inputting the variable content in the command line and be prompted for it instead, one can use:

The command returns directly the protected variable that can be inserted into a playbook. Encrypted and non-encrypted variables can coexist in a YAML file as illustrated below:

## Package management
## Official repositories
Ansible has a pacman module (provided by the  package) to handle installation, removal and system upgrades with pacman.

## AUR
For the Arch User Repository (AUR), it is required to use the external module ansible-aur. See the README for use and installation instructions.

While Ansible expects to ssh as root, AUR helpers do not allow executing operations as root, they all fail with "you cannot perform this operation as root". For Ansible automation, it is therefore recommended to create a user, for example named aur_builder, that has no need for password with pacman in sudoers. This can be done in Ansible with the following actions:

Then, AUR helpers or makepkg can be used associated with the Ansible parameters  and

## Tips and tricks
## User account creation
Ansible can manage user accounts and in particular it is able to create new ones. This is achieved in playbooks with the user module which takes an optional  argument to set the user's password. It is the hashed value of the password that needs to be provided to the module.

The hashing can simply be performed on the fly within Ansible using one of its internal hash-filters:

 - user:
   name: user_name
   password: ""
   shell: /usr/bin/nologin

With this approach it is recommended to vault-encrypt user_password so that it does not appear in plain text, see #Vault. However, an encrypted variable cannot be piped directly and will first need to be assigned to another one that will be piped.

Alternatively, the hashing can be performed outside Ansible. The following commands return respectively the MD5 and the SHA512 hashed values of user_password:

 $ openssl passwd -1 user_password

 $ python -c 'import crypt; print(crypt.crypt("user_password", crypt.mksalt(crypt.METHOD_SHA512)))'

## Python binary location
Ansible requires Python on the target machine. By default Ansible assumes it can find a  on the remote system that is a 2.X or 3.X version, specifically 2.6 or higher.

If some of your modules specifically require Python2, you need to inform Ansible about its location by setting the  variable in the inventory file. This can be done by using host groups in the inventory:

More information about Python version support in Ansible is available in [https://docs.ansible.com/ansible/latest/reference_appendices/faq.html#how-do-i-handle-not-having-a-python-interpreter-at-usr-bin-python-on-a-remote-machine and == Troubleshooting ==

## Unarchive
The  module unpacks an archive. However tar files are not well supported and several outstanding issues are reported in [https://github.com/ansible/ansible/labels/m%3Aunarchive GitHub - unarchive. In particular when the parameter  is set to , idempotence is not observed. In case you face an issue with the module, you can use instead the zip format which is better integrated in Ansible.
