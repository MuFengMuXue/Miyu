# MinIO

MinIO offers high-performance, S3 compatible object storage.

## Installation
Install the  package. The  is optional.

## Configuration
The configuration file is located in .

## Credentials
Uncomment  and  and set them to a value of your choice.

## Single server with 1 disk
The default configuration will start a single server with a single disk. MinIO objects will be stored in . Change the value of  to update the path.

 might contains extra parameters that will be given to the MinIO server when started.

Start MinIO by starting . Check that MinIO has been started by checking the service's unit status; example output is as follows:

## Single server with 4 disks
Edit :

 MINIO_VOLUMES="/srv/minio/data{0...3}"

or

 MNIO_VOLUMES="/srv/minio/foobar /srv/minio/barfoo /srv/minio/faabor /srv/minio/borfaa"

Start . Verify that MinIO is running by checking its unit status; example output is as follows:

{{bc|
● minio.service - Minio
     Loaded: loaded (/etc/systemd/system/minio.service; disabled; vendor preset: disabled)
     Active: active (running) since Fri 2021-10-29 18:28:12 CEST; 2s ago
       Docs: https://docs.minio.io
    Process: 123 ExecStartPre=/bin/bash -c { [ -z "${MINIO_VOLUMES}" ] && echo "Variable MINIO_VOLUMES not set in /etc/minio/minio.conf" && exit 1; } == true (code=exited, status=0/SUCCESS
   Main PID: 124 (minio)
      Tasks: 15 (limit: 18994)
     Memory: 90.0M
        CPU: 673ms
     CGroup: /system.slice/minio.service
             └─123 /usr/bin/minio server --address 192.168.0.1:9000 --console-address localhost:7890 /srv/minio/foobar /srv/minio/barfoo /srv/minio/faabor /srv/minio/borfaa

systemdStarting Minio...
systemd[1: Started Minio.
minioYou are running an older version of MinIO released 1 month ago
minio[124:  Update: Run `mc admin update`
minioAutomatically configured API requests per node based on available memory on the system: 104
minio[124: Status:         4 Online, 0 Offline.
minioAPI: http://192.168.0.1:9000
minio[124: Console: http://localhost:7890
minio124: Documentation: https://docs.min.io
}}
