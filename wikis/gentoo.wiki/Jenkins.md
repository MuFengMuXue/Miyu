**Resources**

[[]][Home](https://jenkins.io/)

[[]][Blog](https://jenkins.io/node)

[[]][GitHub](https://github.com/jenkinsci/jenkins)

[[]][[#jenkins](ircs://irc.libera.chat/#jenkins)] ([[webchat](https://web.libera.chat/#jenkins)])

[[]][Official documentation](https://jenkins.io/doc/)

[[]][Package information](https://packages.gentoo.org/packages/dev-util/jenkins-bin)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Jenkins_(software) "wikipedia:Jenkins (software)")

**Jenkins** is an open source automation server written in [Java](https://wiki.gentoo.org/wiki/Java "Java"). The project was forked from [Hudson](https://en.wikipedia.org/wiki/Hudson_(software) "wikipedia:Hudson (software)") after a dispute with [Oracle](https://en.wikipedia.org/wiki/Oracle_Corporation "wikipedia:Oracle Corporation")^[\[1\]](#cite_note-1)^.

Common use case of Jenkins is automation of [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration "wikipedia:Continuous integration") (CI) and [continuous delivery](https://en.wikipedia.org/wiki/Continuous_delivery "wikipedia:Continuous delivery") (CD) related tasks.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [First configuration]](#First_configuration)
    -   [[2.2] [General configuration]](#General_configuration)
    -   [[2.3] [Security]](#Security)
        -   [[2.3.1] [Allow remote command-line interface]](#Allow_remote_command-line_interface)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Service]](#Service)
        -   [[3.1.1] [systemd]](#systemd)
    -   [[3.2] [Access from the command-line]](#Access_from_the_command-line)
-   [[4] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [dev-util/jenkins-bin](https://packages.gentoo.org/packages/dev-util/jenkins-bin) [[]] [The leading open source automation server]

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-05 14:38] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask dev-util/jenkins-bin`

## [Configuration]

### [First configuration]

Open [http://localhost:8080](http://localhost:8080) with a [web browser](https://wiki.gentoo.org/wiki/Category:Web_browser "Category:Web browser") and follow the first configuration steps.

### [General configuration]

The main configuration dashboard is at [http://localhost:8080/manage](http://localhost:8080/manage).

### [Security]

The security configuration page is accessible on the configuration dashboard, or directly on [http://localhost:8080/configureSecurity/](http://localhost:8080/configureSecurity/).

#### [Allow remote command-line interface]

To allow anyone to connect with [Command-line interface](https://en.wikipedia.org/wiki/Command-line_interface "wikipedia:Command-line interface") (CLI), activate two options:

1.  \"Allow anonymous read access\" in \"Authorisations\" section,
2.  \"Enable CLI over Remoting\" in the \"CLI\" section.

## [Usage]

### [Service]

#### [systemd]

For a oneshot start:

`root `[`#`]`systemctl start jenkins`

To enable the service at each startup:

`root `[`#`]`systemctl enable jenkins`

### [Access from the command-line]

You must have remote CLI option activated.

Download [http://localhost:8080/jnlpJars/jenkins-cli.jar](http://localhost:8080/jnlpJars/jenkins-cli.jar).

To obtain the list of possible commands, open a console or a terminal and enter:

`user `[`$`]`java -jar jenkins-cli.jar -s http://localhost:8080/ help`

## [References]

1.  [[[↑](#cite_ref-1)] [[Continuous Integration: Hudson vs. Jenkins - DevTeam.Space](https://www.devteam.space/blog/continuous-integration-hudson-vs-jenkins/), devteam.space. Retrieved on December 1, 2018]]