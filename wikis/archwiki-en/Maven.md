# Maven

Maven is a build automation tool used by Java developers to compile, build and deploy code, documentation and libraries.

## Installation
Install .

## Configuration
## Creating a new project
Maven provides Archetypes which are project structures which are pulled from Maven repositories.

To create a new project, you can use the following command:

 $ mvn archetype:generate

This will bring up a interactive prompt within the command line, allowing you to chose which archetype to use to create your project.

## Without interactive prompt
You can also create a mvn project without the interactive prompt. Java uses Reverse Domain Name Notation when grouping packages, for example if your domain name is  your  would be , your  should be the name of your project in all lowercase.

 $ mvn -B archetype:generate -DgroupId=com.example  -DartifactId=example -DarchetypeArtifactId=maven-archetype-quickstart

This will create the entire project layout for you, and gives you a basic  file to start out with, which can be modified or added to as needed.

## Contributing to an existing maven project
Maven should automatically fetch its indexes,

## Creating the maven wrapper
Maven allows for the creation of a maven wrapper similar to Gradle, this prevents version mismatch between different developers as the wrapper ensures the same version is used by any developer which is working on the project.

To create the maven wrapper, use the following command within the root directory of the project:

 $ mvn -N wrapper:wrapper -Dmaven=version

Replace  with the desired maven version for the wrapper to use, this is often going to be the latest version of maven, see  to find the current latest version of maven.

## Tips and tricks
## Creating a Maven repository
A lot of developers rely on publicly hosted Maven repositories to deploy their projects to (such as libraries, plugins and archetypes). For a lot of people this would have privacy concerns. Good news, you can host your own. Software which hosts maven repositories are collectively known as Maven Artifact Managers or Maven Repository Managers, however any web server can act as a Maven Repository.

There are MANY Maven Artifact Managers available:
* Reposilite - Free and open source maven artifact manager, written in Java.
* Archiva - Open source maven artifact manager, written in Java, provided by the Apache team.
* Gitea - Open source git server, provides builtin package deployment, supporting Java (Maven).
* ProGet - Proprietary maven artifact manager, designed for enterprise deployments.
* JFrog Artifactory - Comes in two editions, see below:
** Community edition - Open source maven artifact manager, designed for non-commercial use.
** Pro edition - Proprietary maven artifact manager, designed for commercial use.
* Sonatype Nexus - Comes in two editions, see below:
** OSS edition - Open source maven artifact manager, designed for non-commercial use.
** Pro edition - Proprietary maven artifact manager, designed for commercial use.

Any of the above can be used to self-host your own Maven repository, the proprietary (commercial) products are non-free and require a licence in order to use.

## Using nginx
A web server, such as Nginx can be used to host a maven repository. Be aware in the difference in terminology however, this will not be a repository manager, it will just be the repository portion, all management will have to be done manually through command line, or directly editing the structure of the repository. Other web servers may be used, however they must support the WebDAV protocol.

For this guide we will be using  as the directory of choice for the storage of the artifacts.

Ensure that the permissions are set correctly:

 # chmod 750 /var/repository
 # chown http:http /var/repository

For this example, we will not allow any user which is not in the "http" group to view the contents of the repository. This should be good for most cases, as files will be pushed through maven, and not directly added by you.

Next, ensure you have followed the installation steps within Nginx before continuing with this guide.

Next, add the following configuration for nginx:

{{hc|/etc/nginx/sites-enabled/maven|
server {
    listen 80;
    server_name your.domain.name;

    location / {
        root /var/repository;
        create_full_put_path on;
        autoindex on;
        dav_methods PUT DELETE MKCOL COPY MOVE;
        dav_access user:rw group:rw;

        limit_except GET {
                auth_basic "Restricted Area";
                auth_basic_user_file /etc/nginx/.htpasswd;
        }
    }
}
}}

The above example does not provide TLS encryption. This is useful for local maven repositories, however if you want to deploy your repository to be accessed by others, you should use TLS encryption (see below configuration).

{{hc|/etc/nginx/sites-enabled/maven|
server {
    listen 443 ssl;
    server_name your.domain.name;

    ssl_certificate /path/to/your/fullchain;
    ssl_key /path/to/your/key;

    location / {
        root /var/repository;
        create_full_put_path on;
        autoindex on;
        dav_methods PUT DELETE MKCOL COPY MOVE;
        dav_access user:rw group:rw;

        limit_except GET {
                auth_basic "Restricted Area";
                auth_basic_user_file /etc/nginx/.htpasswd;
        }
    }
}
}}

Set the following values:

*  to your hostname you wish to use for your maven repository, if you are running this on a LAN, you can use  and the repository will be accessible by entering the local IP of the server into your web browser.
*  to the path of your fullchain certificate.
*  to the path of your certificate key.

The  section of the nginx configuration prevents unauthorised users from pushing their dependencies to your repository, we will be using BASIC authentication with nginx for this example. BASIC authentication is only secure if HTTPS is used, thus you should not use BASIC auth over HTTP as the password will be leaked.

To aid in creating the  file, we will be using  provided by the  package.

 # htpasswd -c /etc/nginx/.htpasswd username

You will then be prompted to enter a password, this password will be saved against the username you specified within the command.

The user you just created is now authorised to push artifacts to the repository.

Now lets set the permissions for the file:

 # chmod 640 .htpasswd

This will prevent any other users from reading the content of .htpasswd, which would potentially cause a security breach (bare in mind the passwords are hashed, but this should not be relied upon).

Next we need to configure Maven so that it is able to push to the mirror, on the system you would like to push from, and logged in as the user you would like to grant permission to the repository, create and edit the following file .

You will now need the base64 representation of the username and password to add to the HTTP headers for authentication using the following command:

 $ echo -n "username:password" | base64

The returned value is your basic authentication token for your repository.

You must replace  with the username you used when you created  and replace  with the password you entered when prompted to create a password. Both the username and password must be separated by ":".

Now add the following to your maven :

Replace  with the desired id for your repository, this is used to identify the configuration values set within settings.yml for the repository, with the  within your codebases. Then you need to replace  with the token you created from the base64 command above.

You should now have permission to push new builds to your repository, once pushed using  people will be able to pull your artifacts from your repository. (No authentication is needed for pulling of artifacts, only pushing).
