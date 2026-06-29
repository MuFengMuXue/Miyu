# Arch Linux on a VPS

From Wikipedia:Virtual private server:

:Virtual private server (VPS) is a term used by Internet hosting services to refer to a virtual machine. The term is used for emphasizing that the virtual machine, although running in software on the same physical computer as other customers' virtual machines, is in many respects functionally equivalent to a separate physical computer, is dedicated to the individual customer's needs, has the privacy of a separate physical computer, and can be configured to run server software.

This article discusses the use of Arch Linux on Virtual Private Servers, and includes some fixes and installation instructions specific to VPSes.

## Official Arch Linux cloud image
Arch Linux provides an official cloud image as part of the arch-boxes project. The image comes with Cloud-init preinstalled and should work with most cloud providers.

The image can be downloaded from the mirrors under the  directory. Instructions for tested providers is listed below.

## DigitalOcean
Website: Digital Ocean

Locations: Global

Steps to create an Arch Linux virtual machine:

# Find the cloud image on a mirror, e.g.: https://fastly.mirror.pkgbuild.com/images/latest/Arch-Linux-x86_64-cloudimg.qcow2
# Add the image as a custom image by importing it
# Create a new virtual machine from the custom image
# SSH to the virtual machine:

## Hetzner Cloud
Website: Hetzner Cloud

Locations: Nuremberg (Germany), Falkenstein (Germany), Helsinki (Finland), Singapur, Hillsboro (US West), Ashburn (US East)

Steps to create an Arch Linux virtual machine:

# Create a new virtual machine with this user data: {{bc|#cloud-configvendor_data: {'enabled': false}}} The  from Hetzner overrides the  and sets the default user to  without setting , meaning you cannot login.
# Boot the virtual machine in rescue mode
# SSH to the virtual machine and download the cloud image from a mirror, e.g.:
# Write the image to the disk:
# Reboot the virtual machine
# SSH to the virtual machine:

## Linode
Website: Linode

Locations: Multiple international locations

Steps to create an Arch Linux virtual machine:

# Create a new virtual machine and select Arch as the distribution (to use the Linode-provided image, stop here; otherwise proceed with the rest of the steps)
# Boot the virtual machine in rescue mode
# Connect to the virtual machine via the Lish console and download the basic image from a mirror, e.g.:
# Install the qemu-utils package:
# Write the image to the disk:
# In the Linode manager, go to the virtual machine's configurations menu and edit the configuration to change the kernel option to "Direct Disk"
# Reboot the virtual machine
# SSH to the virtual machine:

## OVH Eco
Website: Kimsufi OVH Eco

Locations: Canada, France

Steps to create an Arch Linux virtual machine, paraphrasing the official documentation:

# Navigate to the Dedicated Servers section in your OVH management panel, then select the server you want to deploy Arch Linux to.
# Click the ... button next to "Last operating system (OS) installed by OVHcloud" and choose "Install"
# Select "Bring Your Own Image (64bits)"
# Enter your "Server host name" and your public "SSH key"
# For "Image URL" put
# For "Image type" select
# For "Checksum type" select
# For "Image checksum" put the fingerprint value from https://fastly.mirror.pkgbuild.com/images/latest/Arch-Linux-x86_64-cloudimg.qcow2.SHA256
# For "Path of the EFI bootloader" put
# Optional: You can also add Cloud-init Instructions under section "Config Drive UserData". This is also useful to change the user passwords or to disable password logins via SSH for security reasons and use SSH Keys instead.
# Click "Install the system"
# Wait (it takes a while) for an email from OVH titled "Installation of your image", it will say "Congratulations! Your dedicated server has just been installed! Connect to your server with ssh key provided during your installation."
# Use  to log in.

## Proxmox
Website: Proxmox

Locations: N/A

Steps to create an Arch Linux virtual machine:

# Create a new virtual machine.
# Select "Do not use any media" in OS section.
# Remove the created hard disk from your virtual machine after the virtual machine creation completes.
# Add the downloaded image to your virtual machine using , e.g.: .
# Under Options, edit the boot order and add the newly-created disk.
# Add a cloudinit drive and make your configurations in Cloud-Init section.
# Start the virtual machine!
