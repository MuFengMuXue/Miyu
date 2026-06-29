# Paperless

Paperless is an open source document management system that indexes your scanned documents and allows you to easily search for documents and store metadata alongside your documents. This article refers to Paperless-ngx, a community-maintained fork of Paperless-ng, which in turn is a fork of the original Paperless project that have both been given up.

## Installation
Install the  package.

## Folders
Paperless gets installed to . The persistent storage of Paperless is located at  and contains the  folder, the  folder (by default containing the SQLite database), the  folder for document consumption, the temporary  folder and  convert folder.
The  folder has write permissions for everyone in the  group.

## Consumption folder permissions
If you wish to allow users (e.g. "http") to put documents in the consumption folder, add them to the  user group.

## OCR languages
If you want Paperless to consume documents in a language other than English, you need to install the corresponding tesseract language data package. For German that would be .

## Reduce the size of generated PDF documents
You might want to install the optional dependency  so Paperless can use it to reduce the size of generated PDF documents.

## Migrating from Paperless-ng
If you have paperless-ng installed and wish to migrate to , you can install  and choose to remove paperless-ng when asked. No data will be lost. Still, you will need to run as root:

 # paperless-manage makemigrations

After that, apply the usual database migrations as the paperless user:

 paperless-manage migrate

Finally, restart .

## Start
Start/enable .
Your Paperless instance should now be available at port 8000.

## Configuration
For details on Paperless configuration, visit its official [https://docs.paperless-ngx.com/configuration/ documentation. The configuration file is located at .

Do not forget to restart  after changing configurations.

## Adjust the configuration to your needs
Open the configuration file located at  at adjust the parameters to your needs, especially those concerning OCR. For explanations of the individual settings, refer to the official documentation.

## Set a secret key
After initial installation, you should generate and set a secret key. You do not need to remember it, but since it is used for securing signed data, you should keep it secret. To set a secret key, uncomment and modify the following line:

To generate a key and set it in the configuration file, you can simply run the following command:

 # sed -i /etc/paperless.conf -e "s|#PAPERLESS_SECRET_KEY=change-me|PAPERLESS_SECRET_KEY=$(tr -dc A-Za-z0-9  0.25.0. However, workarounds are discussed [https://github.com/paperless-ngx/paperless-ngx/discussions/7006}}

## Pacman hook
To automatically run migrations for the Paperless database on package updates, you can make use of the included pacman hook:

 # mkdir -vp /etc/pacman.d/hooks
 # ln -sv /usr/share/paperless/docs/paperless.hook /etc/pacman.d/hooks/

## Troubleshooting
## BadSignature errors logged when trying to import documents
If you see  errors when trying to import documents, it is likely that your configuration file located at  is not taken into account because the template configuration file  is given precedence. In that case, remove or rename  and restart .

## Warning about misconfigured retry and timeout
If you see a warning about misconfigured retry and timeout, you can safely ignore it and wait for the simple upstream fix in . The warning would look like this:

## Thumbnail generation with ImageMagick fails
You have to disable a policy rule in . Add  to comment out the following line:

Consider the possible security implications noted at the beginning of the ImageMagick article. Also note that Paperless will fall back to using ghostscript anyway if the ImageMagick policy rule stays active.

## The consumer service keeps one CPU core constantly at 100%
Uncomment the line concerning the  setting in your  configuration file:
