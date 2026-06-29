[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Docker/Compose&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][GitHub](https://github.com/docker/compose)

[[]][Official documentation](https://docs.docker.com/compose)

[[]][Package information](https://packages.gentoo.org/packages/app-containers/docker-compose)

**Docker Compose** is a tool for running multi-container applications on [Docker](https://wiki.gentoo.org/wiki/Docker "Docker") defined using the Compose file format.

A Compose file is used to define how one or more containers that make up how the application is configured. Once a Compose file has been created, the application can be started with a single command: `docker compose up`.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Starting Docker Compose]](#Starting_Docker_Compose)

## [Installation]

### [USE flags]

### [USE flags for] [app-containers/docker-compose](https://packages.gentoo.org/packages/app-containers/docker-compose) [[]] [Multi-container orchestration for Docker]

  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`test`](https://packages.gentoo.org/useflags/test)   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-14 18:49] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-containers/docker-compose`

## [Usage]

### [Starting Docker Compose]

To start Docker Compose with a file named [docker-compose.yml] in the current directory, run:

`user `[`$`]`docker compose up`