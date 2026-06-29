# Arch Linux AMIs for Amazon Web Services

## Public community Arch AMIs
## AMIs
Arch Linux AMIs are listed here: http://arch-ami-list.drzee.net/

AMIs are build twice a month (the 1st and the 15th - 2:00am UTC) and are available for all regions that to do not explicitly require 'Opt-in' - see Region List. If an AMI is needed in a region where its currently not available, an AMI can be copied to that region.

The AMIs are EBS HVM AMIs and are available with two different kernels:
*std - using the Standard Arch Linux Kernel from the default Arch repositories configured with the necessary modules for EC2 usage. The scheduler and I/O is not optimized for Cloud. A complete list of packages in the AMI: *lts - using the Standard Arch Linux LTS Kernel from the default Arch repositories configured with the necessary modules for EC2 usage. The scheduler and I/O is not optimized for Cloud. A complete list of packages in the AMI: [http://arch-ami-list.drzee.net/package_list.html?packagelist=lts.

Both kernels have been tested on many different EC2 instance types (t2, t3, t3a, m/r/c5, m/r/c6 and advanced hardware with GPUs) and are booting fine.

## REST API to List AMIs
An REST API is available to get a JSON of available AMIs:

* Get all AMIs:
* Get list of latest AMI in each region:  (this produces the same list as http://arch-ami-list.drzee.net/ but in JSON)
* Get all AMIs in region:  - replace  with the desired region: , ,  etc.
* Get all AMIs in region for CPU architecture:  - replace  with
* Get all AMIs in region for CPU architecture and kernel-type:  - replace  with  or
* Get Latest AMI in region for in region for CPU architecture and kernel-type:  - replace ,  and

## First Run
After booting the AMI it is recommended/required to execute the following steps to initialize pacman and select fast local repositories:

 # pacman-key --init
 # pacman-key --populate
 # reflector --country "ISO 3166-1 Alpha-2 Country Code" --protocol https,http --score 20 --sort rate --save /etc/pacman.d/mirrorlist
 # pacman -Syu

The Reflector package is preinstalled in the AMIs.

It is recommended to set a proper configuration for reflector in  and enable the timer services to regularly refresh the mirror list. For details see the Reflector package documentation.

For convenience, a script is included: .

Executing the script with  will automatically run the above  commands and setup Reflector by writing . Finally it will run Reflector to generate a mirrorlist.

Country selection for Reflector is done based on the AWS region where the instance is running. The following shows mapping between region and country codes (only regions where the AMIs are distributed to are supported):

 # region_to_country# region_to_country['eu-west-2'='UK,IE,DE'
 # region_to_country# region_to_country['eu-central-1'='DE,FR,UK'
 # region_to_country# region_to_country['us-east-1'='US,CA'
 # region_to_country# region_to_country['us-west-1'='US,CA'
 # region_to_country# region_to_country['ap-south-1'='IN,SG,US'
 # region_to_country# region_to_country['ap-northeast-2'='KR,JP,TW,US'
 # region_to_country# region_to_country['ap-southeast-1'='SG,ID,TH,US'
 # region_to_country# region_to_country['ca-central-1'='CA,US'
 # region_to_countryFor EMEA Regions, "DE" (Germany), and for US/APAC/South America Regions, "US" (United States), is always included as a last resort should in country or "neighbor" country repositories be unavailable.

Alternative provide your own mirrorlist and do not use the Reflector package.

## Build process
The entire build process runs on AWS and is fully automated.

Overall the automated build procedure is managed by a AWS Step Function that is executed at regular intervals using a Amazon EventBridge timed event.

The step function will initiate the build process and uses a combination of native calls and AWS Lambda functions for more complex elements.

A new set of AMIs is build, by booting an EC2 instance with the previous AMI and using it as the work or build machine. The build machine is bootstrapped with a special build script that essentially uses pacstrap and some additional steps to build the image, the basics are outlined in section (2) below.

Following the build of the AMI the new AMI is test booted on an EC2 instance to verify that it starts up correctly. If successful the AMI is distributed to the regions and registered in a DynamoDB database. The database can be queried using the API REST endpoint. Old AMIs are deleted from the regions and the DynamoDB database.

## Credits
Thanks to Steven from UplinkLabs for helping to understand the build process and test the initial quality of the images. Also thanks to Mathcom for an excellent shells script to help me get started (unfortunately the link to that has been removed), which accelerate putting the basic build process together.

You may send comments and suggestions (without any promise that they will be looked at) to: arch-ami 'at' drzee.net

## Wishlist
* Create official EC2/Cloud optimized kernels in the Standard Arch Linux repositories.

## Building Arch AMIs
You can also build your own Arch Linux AMI. See [http://arch-ami-list.drzee.net/ami_build_howto.html for details.
