# Papermerge

Papermerge is an open source document management system for digital archives.

## Installation
Install the  package. Installation and updates of the package automatically run the database migrations.

## Start
Start/enable  and
Your papermerge instance should now be available at port 9001.

## Configuration
For details on papermerge configuration, visit its official documentation. The main configuration file is located at .

Do not forget to restart  and  after changing configurations.

## Create admin user
After initial installation, you should create an admin user for your papermerge instance using the papermerge UNIX user:

 papermerge-manage createsuperuser

## Nginx
Install Nginx and use the following configuration as a starting point for the papermerge virtual host:
{{hc|/etc/nginx/sites-available/papermerge.domain.tld|2=
server {
    server_name papermerge.domain.tld;
    listen 80;
    listen [:::80;

    location /static/ {
        alias /var/lib/papermerge/static/;
    }

    location /media/ {
        alias /var/lib/papermerge/media/;
    }

    location / {
        proxy_pass http://127.0.0.1:9001;
    }
}
}}

## Redis
It is recommended to use Redis as a message broker instead of the default filesystem-based approach.

Install  and  and start/enable . In  replace
{{hc|/usr/lib/python3.9/site-packages/config/settings/base.py|2=
CELERY_BROKER_URL = "filesystem://"
CELERY_BROKER_TRANSPORT_OPTIONS = {
    'data_folder_in': PAPERMERGE_TASK_QUEUE_DIR,
    'data_folder_out': PAPERMERGE_TASK_QUEUE_DIR,
}
}}
with
{{hc|/usr/lib/python3.9/site-packages/config/settings/base.py|2=
CELERY_BROKER_URL = "redis://"
CELERY_BROKER_TRANSPORT_OPTIONS = {}
CELERY_RESULT_BACKEND = "redis://localhost/0"
}}
and restart  and
