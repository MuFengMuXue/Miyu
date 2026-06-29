[[]][Official documentation](https://docs.searxng.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/SearXNG "wikipedia:SearXNG")

[[]][GitHub](https://github.com/searxng/searxng)

**SearXNG** (or \"searching\") is a free internet metasearch engine which aggregates results from various search services and databases. SearXNG allows users to specify which search engines they want to include in their search results, group engines in categories, specify engine timeouts, and more. SearXNG can be used via someone else\'s instance^[\[1\]](#cite_note-1)^ or a self-hosted instance. This wiki page teaches users how to host an instance.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
    -   [[1.2] [Make the SearXNG user]](#Make_the_SearXNG_user)
    -   [[1.3] [Make the virtual environment]](#Make_the_virtual_environment)
        -   [[1.3.1] [Update the boilerplate]](#Update_the_boilerplate)
        -   [[1.3.2] [Install SearXNG into the virtual environment]](#Install_SearXNG_into_the_virtual_environment)
    -   [[1.4] [(Optional) Install uWSGI]](#.28Optional.29_Install_uWSGI)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
        -   [[2.1.1] [SearXNG]](#SearXNG)
        -   [[2.1.2] [uWSGI]](#uWSGI)
    -   [[2.2] [Service]](#Service)
        -   [[2.2.1] [OpenRC]](#OpenRC)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Manual]](#Manual)
    -   [[3.2] [uWSGI]](#uWSGI_2)
-   [[4] [Upgrade]](#Upgrade)
-   [[5] [Removal]](#Removal)
    -   [[5.1] [SearXNG]](#SearXNG_2)
    -   [[5.2] [uWSGI]](#uWSGI_3)
-   [[6] [See also]](#See_also)
-   [[7] [References]](#References)

## [Installation]

### [Emerge]

We will use [Git](https://wiki.gentoo.org/wiki/Git "Git") ([[[dev-vcs/git]](https://packages.gentoo.org/packages/dev-vcs/git)[]]) to download the SearXNG repository. If Git isn\'t installed, install it now.

`root `[`#`]`emerge --ask dev-vcs/git`

### [Make the SearXNG user]

The SearXNG server will be running as user [searxng]; technically, we can name this user anything. We also specify several other options:

-   `--shell /bin/bash` \-- Specify the shell of this user.
-   `--system` \-- Make a system account; this user is intended to be ran by the machine and not by a human (this user will be given numeric identifiers that represent system identifiers).
-   `-m` \-- Make a home directory for this user.
-   `--home-dir /usr/local/searxng` \-- Specify the home directory.
-   `--comment 'Privacy-respecting metasearch engine'` \-- Add a comment to describe this user.

`root `[`#`]`useradd --shell /bin/bash --system -m --home-dir /usr/local/searxng --comment 'Privacy-respecting metasearch engine' searxng`

Most of the following commands will need to be ran by the [searxng] user; switch to this user now.

`root `[`#`]`sudo -u searxng -i`

### [Make the virtual environment]

SearXNG uses several [Python](https://wiki.gentoo.org/wiki/Python "Python") packages installed with [pip](https://wiki.gentoo.org/wiki/Pip "Pip"). We need to make a virtual environment for pip to install packages into so that they don\'t conflict with system packages.

`searxng $``python -m venv /usr/local/searxng/searx-pyenv`

At this point, the virtual environment is installed, but it must be activated to use it; this is done by sourcing the file [/usr/local/searxng/searx-pyenv/bin/activate]. It can get tiresome to source this file every time we need to manage SearXNG; to fix this, we can append a command to searxng\'s [.bashrc] file so that it gets sourced every time we switch to this user.

`searxng $``echo ". /usr/local/searxng/searx-pyenv/bin/activate" >>/usr/local/searxng/.bashrc`

We can go ahead and source the file that activates the virtual environment. The result of this command should prefix \"[(searx-pyenv)]\" to [PS1] (the prompt); this is how we can tell the virtual environment is activated.

`searxng $``. /usr/local/searxng/searx-pyenv/bin/activate`

#### [Update the boilerplate]

With the user and virtual environment set up, we can now use pip to install packages.

`(searx-pyenv) searxng $``pip install -U pip setuptools wheel pyyaml msgspec`

#### [Install SearXNG into the virtual environment]

We can combine the cloning of the SearXNG repository and it\'s installation into the Python virtual environment in a single command; this will clone the repository into [/usr/local/searxng/searx-pyenv/src/searxng].

`(searx-pyenv) searxng $``pip install --use-pep517 --no-build-isolation -e "git+`[`https://github.com/searxng/searxng#egg=searxng`](https://github.com/searxng/searxng#egg=searxng)`"`

** Tip**\
To list all installed Python packages for the **\*\*current\*\*** environment, run `pip freeze`.

`(searx-pyenv) searxng $``pip freeze`

    anyio==4.9.0
    async-timeout==5.0.1
    babel==2.17.0
    blinker==1.9.0
    Brotli==1.1.0
    certifi==2025.4.26
    click==8.1.8
    fasttext-predict==0.9.2.4
    Flask==3.1.0
    flask-babel==4.0.0
    h11==0.14.0
    h2==4.2.0
    hpack==4.1.0
    httpcore==0.17.3
    httpx==0.24.1
    httpx-socks==0.7.7
    hyperframe==6.1.0
    idna==3.10
    isodate==0.7.2
    itsdangerous==2.2.0
    Jinja2==3.1.6
    lxml==5.4.0
    markdown-it-py==3.0.0
    MarkupSafe==3.0.2
    mdurl==0.1.2
    msgspec==0.19.0
    Pygments==2.19.1
    python-dateutil==2.9.0.post0
    python-socks==2.7.1
    pytz==2025.2
    PyYAML==6.0.2
    redis==5.0.8
    -e git+https://github.com/searxng/searxng@0315988f5ab9d5d55693bc9a0eca045bf9220506#egg=searxng
    setproctitle==1.3.6
    setuptools==80.3.1
    six==1.17.0
    sniffio==1.3.1
    typer-slim==0.15.3
    typing_extensions==4.13.2
    uvloop==0.21.0
    Werkzeug==3.1.3
    wheel==0.45.1

The special package, `-e git+https ... #egg=searxng`, in the list is how [pip] can upgrade SearXNG.

Run `exit` to return to the root user.

`(searx-pyenv) searxng $``exit`

### [][(Optional) Install uWSGI]

SearXNG can be started manually by logging in as [searxng] and running a Python script. To have SearXNG start at boot, we can set up a Python web server; in this case, we will be using uWSGI.

** Note**\
There is a difference between **uWSGI** and **uwsgi** (all lowercase)^[\[2\]](#cite_note-2)^:

-   **uWSGI** is the name of the application.
-   **uwsgi** is the name of the protocol.

To run SearXNG, uWSGI will need to be installed with the `python` USE flag enabled because SearXNG is made in Python.

[FILE] **`/etc/portage/package.use/uwsgi`**

    www-servers/uwsgi python

** Note**\
\

-   When the `embedded` USE flag is enabled, most plugins are built-in to uWSGI; if we want to set specific plugins for uWSGI to use, disable the `embedded` USE flag and list them in the [/etc/searxng/searxng.ini] file explained later.

<!-- -->

-   More plugins can be installed when uWSGI is installed by adding `UWSGI_PLUGINS:` and the plugins to our USE flags.

[FILE] **`/etc/portage/package.use/uwsgi`**

    www-servers/uwsgi python -embedded UWSGI_PLUGINS: pam

Install uWSGI ([[[www-servers/uwsgi]](https://packages.gentoo.org/packages/www-servers/uwsgi)[]]).

`root `[`#`]`emerge --ask www-servers/uwsgi`

## [Configuration]

### [Files]

#### [SearXNG]

Make the directory that will contain the configuration files for SearXNG.

`root `[`#`]`mkdir -p /etc/searxng`

SearXNG can be customized via two methods:

-   Visiting the SearXNG webpage and selecting the \"[Preferences]\" button to make changes and saving those changes in our browser\'s cookies.
-   Making changes to the [/etc/searxng/settings.yml] file directly.

Customizing SearXNG via a browser will only affect the user of that browser; customizing the configuration file will affect all users that visit the SearXNG webpage. The following command gets the latest default configuration file for SearXNG from the official repository and puts it in the correct location:

`root `[`#`]`wget -O /etc/searxng/settings.yml "`[`https://raw.githubusercontent.com/searxng/searxng/refs/heads/master/searx/settings.yml`](https://raw.githubusercontent.com/searxng/searxng/refs/heads/master/searx/settings.yml)`"`

Substitute the text \"`ultrasecretkey`\" with a random hexadecimal 16 bytes long.

`root `[`#`]`sed -i -e "s/ultrasecretkey/$(openssl rand -hex 16)/g" /etc/searxng/settings.yml`

#### [uWSGI]

The default configuration file for a uWSGI service is located at [/etc/conf.d/uwsgi]. We can make a copy of this file to [/etc/conf.d/uwsgi.searxng] and customize it to our needs. We can use the following configuration file for uWSGI to have it run our SearXNG instance:

[FILE] **`/etc/conf.d/uwsgi.searxng`**

    # SearXNG has its uWSGI config in the 'ini' format.
    UWSGI_EXTRA_OPTIONS="--ini /etc/searxng/searxng.ini"

Next, we need to tell uWSGI how to run SearXNG, answering questions:

-   What user/group does SearXNG run as?
-   How many threads do we use?
-   What plugins do we use?
-   Etc\...

We can copy a template provided when we installed SearXNG and put it in the correct location.

`root `[`#`]`cp /usr/local/searxng/searx-pyenv/src/searxng/utils/templates/etc/uwsgi/apps-available/searxng.ini /etc/searxng/searxng.ini`

Most of the content in [/etc/searxng/searxng.ini] is already correct, but some modifications will need to be made.

[FILE] **`/etc/searxng/searxng.ini`Changes to this file**

    uid = searxng
    gid = searxng
    chdir = /usr/local/searxng/searx-pyenv/src/searxng/searx
    env = SEARXNG_SETTINGS_PATH=/etc/searxng/settings.yml
    virtualenv = /usr/local/searxng/searx-pyenv
    pythonpath = /usr/local/searxng/searx-pyenv/src/searxng
    http = 127.0.0.1:8888
    static-map = /static=/usr/local/searxng/searx-pyenv/src/searxng/searx/static

The variable `plugin` in [/etc/searxng/searxng.ini] will also need to be changed, but the value can vary depending on the version of Python installed on the system. The list of available uWSGI modules is in [/usr/lib64/uwsgi]; remember that the number of modules available depends on whether or not the `embedded` USE flag is enabled.

`user `[`$`]`ls -1 /usr/lib64/uwsgi`

    asyncio312_plugin.so
    cache_plugin.so
    carbon_plugin.so
    cheaper_busyness_plugin.so
    corerouter_plugin.so
    fastrouter_plugin.so
    http_plugin.so
    logfile_plugin.so
    logsocket_plugin.so
    mongodblog_plugin.so
    nagios_plugin.so
    pam_plugin.so
    ping_plugin.so
    python312_plugin.so
    rawrouter_plugin.so
    redislog_plugin.so
    router_basicauth_plugin.so
    router_cache_plugin.so
    router_expires_plugin.so
    router_hash_plugin.so
    router_http_plugin.so
    router_memcached_plugin.so
    router_metrics_plugin.so
    router_redirect_plugin.so
    router_redis_plugin.so
    router_rewrite_plugin.so
    router_static_plugin.so
    router_uwsgi_plugin.so
    rpc_plugin.so
    rrdtool_plugin.so
    rsyslog_plugin.so
    signal_plugin.so
    spooler_plugin.so
    sslrouter_plugin.so
    symcall_plugin.so
    syslog_plugin.so
    transformation_chunked_plugin.so
    transformation_gzip_plugin.so
    transformation_offload_plugin.so
    transformation_tofile_plugin.so
    ugreen_plugin.so
    zergpool_plugin.so

SearXNG needs the [python] and [http] plugins at a bare minimum because that is how we will be using it. We can add other plugins for more features:

-   [asyncio] for increased performance.
-   [pam] to use [PAM](https://wiki.gentoo.org/wiki/PAM "PAM").
-   Etc\...

Some plugins have numbers after them specifying a specific version, these numbers must be included in the name of the plugin.

[FILE] **`/etc/searxng/searxng.ini`Changes to this file**

    # This will **NOT** work!
    plugin = python,asyncio,http

    # This will work.
    plugin = python312,asyncio312,http

** Note**\
We are using [http] (`http = 127.0.0.1:8888`) in this setup to host SearXNG so that we don\'t need additional software; this is fine because we will be the only ones using this SearXNG instance. If the plan is to host this instance for public use, then it\'s better to use a [socket] (`socket = /usr/local/searxng/run/socket`). Sockets can provide higher performance when paired with a load balancer/server such as [nginx](https://wiki.gentoo.org/wiki/Nginx "Nginx"), allowing thousands of users.

### [Service]

#### [OpenRC]

If we try to run `rc-service uwsgi start`, [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") will tell us that we should make a symlink to the uWSGI service we want; so, we do exactly that.

`root `[`#`]`ln -s /etc/init.d/uwsgi `

Don\'t forget to add the service to the default run level.

`root `[`#`]`rc-update add uwsgi.searxng default`

## [Usage]

### [Manual]

SearXNG can be started manually by running the Python executable as the [searxng] user.

`user `[`$`]`sudo -u searxng -i`

`(searx-pyenv) searxng $``python searx-pyenv/src/searxng/searx/webapp.py`

Now, open any web browser from Links to [Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox") and visit [`http://127.0.0.1:8888`](http://127.0.0.1:8888); we should be met with the SearXNG search engine.

### [uWSGI]

If uWSGI isn\'t already running, run the following command:

`root `[`#`]`rc-service uwsgi.searxng start`

If everything is working, use any web browser from Links to Firefox and visit [`http://127.0.0.1:8888`](http://127.0.0.1:8888); we should be met with the SearXNG search engine.

## [Upgrade]

Upgrading SearXNG involves upgrading several components: the Python packages installed in the virtual environment (this includes SearXNG itself), and the virtual environment itself. First, switch to the [searxng] user.

`user `[`$`]`sudo -u searxng -i`

Upgrade the virtual environment.

`(searx-pyenv) searxng $``python -m venv --upgrade /usr/local/searxng/searx-pyenv`

Upgrade all Python packages (this includes SearXNG) installed in the virtual environment.

`(searx-pyenv) searxng $``pip install -U --use-pep517 --no-build-isolation $(pip freeze)`

This can be done as any user with a single command; remember that we need to activate the virtual environment before we use `pip`!

`user `[`$`]`sudo -u searxng bash -c '. /usr/local/searxng/searx-pyenv/bin/activate && python -m venv --upgrade /usr/local/searxng/searx-pyenv && pip install -U --use-pep517 --no-build-isolation $(pip freeze)'`

## [Removal]

### [SearXNG]

Delete the [searxng] user; the `-r` option also deletes this user\'s home directory ([/usr/local/searxng]) and everything in it. We don\'t need to uninstall the Python packages because they\'re all contained in the virtual environment \-- which is inside this user\'s home directory.

`root `[`#`]`userdel -r searxng`

Delete the SearXNG configuration directory and everything in it.

`root `[`#`]`rm -rd /etc/searxng`

### [uWSGI]

Stop the uWSGI service.

`root `[`#`]`rc-service uwsgi.searxng stop`

Delete the uWSGI service from all runlevels.

`root `[`#`]`rc-update del -a uwsgi.searxng`

Delete all files associated with uWSGI.

`root `[`#`]`rm /etc/init.d/uwsgi.searxng `

`root `[`#`]`rm /etc/conf.d/uwsgi.searxng `

`root `[`#`]`rm /etc/searxng/searxng.ini `

Uninstall uWSGI.

`root `[`#`]`emerge --ask --depclean --verbose www-servers/uwsgi`

## [See also]

-   [nginx](https://wiki.gentoo.org/wiki/Nginx "Nginx") --- a robust, small, high performance [web server](https://wiki.gentoo.org/wiki/Category:Web_servers "Category:Web servers") and reverse proxy server.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://searx.space](https://searx.space)]]
2.  [[[↑](#cite_ref-2)] [[https://en.wikipedia.org/wiki/UWSGI](https://en.wikipedia.org/wiki/UWSGI)]]