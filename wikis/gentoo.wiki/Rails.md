**Resources**

[[]][Home](http://rubyonrails.org)

[[]][Official documentation](http://guides.rubyonrails.org/)

[[]][Package information](https://packages.gentoo.org/packages/dev-ruby/rails)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Ruby_on_Rails "wikipedia:Ruby on Rails")

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/rails)

**Rails** or **Ruby on Rails** is an [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller "wikipedia:Model–view–controller") web application framework written in [Ruby](https://wiki.gentoo.org/wiki/Ruby "Ruby").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Setup]](#Setup)
        -   [[1.3.1] [Configuration]](#Configuration)
    -   [[1.4] [Passenger via apache]](#Passenger_via_apache)
    -   [[1.5] [See also]](#See_also)
    -   [[1.6] [External resources]](#External_resources)

# [Installation]

## [USE flags]

### [USE flags for] [dev-ruby/rails](https://packages.gentoo.org/packages/dev-ruby/rails) [[]] [ruby on rails is a web-application and persistence framework]

  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`doc`](https://packages.gentoo.org/useflags/doc)     Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`test`](https://packages.gentoo.org/useflags/test)   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-01-27 20:12] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

## [Emerge]

Install [[[dev-ruby/rails]](https://packages.gentoo.org/packages/dev-ruby/rails)[]]:

`root `[`#`]`emerge --ask dev-ruby/rails`

## [Setup]

`root /var/www #``rails new ror `

`root /var/www #``cd ror `

`root /var/www/ror #``rails server `

Point a web browser to [http://0.0.0.0:3000](http://0.0.0.0:3000). are now riding rails via WEBrick. This is only for testing, not production. WEBrick could probably be used for production if it were behind [nginx](https://wiki.gentoo.org/wiki/Nginx "Nginx") or an accelerator proxy such as [varnish](https://wiki.gentoo.org/wiki/Varnish "Varnish").

### [Configuration]

Rails is not [eselect] aware, this might come in handy to resolving some issues, but be aware that bundle install will blast things away.

`root `[`#`]`eselect rails list`

`root `[`#`]`eselect rails set 1`

## [Passenger via apache]

Emerge passenger:

`root `[`#`]`emerge --ask www-apache/passenger`

Add `-D PASSENGER` to the `APACHE2_OPTS` variable in Apache\'s config:

[FILE] **`/etc/conf.d/apache2`add -D PASSENGER to apache\'s config**

    APACHE2_OPTS="-D PASSENGER"

Passenger needs Apache to relax the rules a little bit. Edit the [/etc/apache2/modules.d/30_mod_passenger.conf] file and insert relaxed settings before the closing \</IfDefine\> tag:

[FILE] **`/etc/apache2/modules.d/30_mod_passenger.conf`apache 2.2**

    <Directory />
        Options FollowSymLinks
        AllowOverride all
        Order allow,deny
        Allow from all
    </Directory>
    </IfDefine>

[FILE] **`/etc/apache2/modules.d/30_mod_passenger.conf`apache 2.4**

    <Directory />
        Options FollowSymLinks
        AllowOverride all
        Require all granted
    </Directory>
    </IfDefine>

Backup the original Apache vhost:

`root `[`#`]`mv /etc/apache2/vhosts.d/00_default_vhost.conf /etc/apache2/vhosts.d/00_default_vhost.conf.backup`

Drop in the passenger vhost file for Apache:

[FILE] **`/etc/apache2/vhosts.d/00_default_vhost.conf`**

    <IfDefine DEFAULT_VHOST>
    Listen 80
    NameVirtualHost *:80
    <VirtualHost *:80>
          DocumentRoot /var/www/ror/public
    #  RailsBaseURI /
      RailsEnv development
          <Directory /var/www/ror/public>
    Options -MultiViews
          </Directory>
    </VirtualHost>
    </IfDefine>

`root `[`#`]`/etc/init.d/apache2 restart`

Point a web browser to [http://0.0.0.0](http://0.0.0.0) or [http://127.0.0.1](http://127.0.0.1) or [http://localhost](http://localhost) and your riding rails via passenger now.

## [See also]

-   [Ruby](https://wiki.gentoo.org/wiki/Ruby "Ruby") - The programming language used to build Rails.

## [External resources]

-   [http://guides.rubyonrails.org/](http://guides.rubyonrails.org/)
-   [http://planetrubyonrails.com/](http://planetrubyonrails.com/)
-   [http://api.rubyonrails.org/](http://api.rubyonrails.org/)
-   [http://rubyonrails.org/screencasts](http://rubyonrails.org/screencasts)
-   [http://railstutorial.org](http://railstutorial.org)
-   [http://railscasts.com/](http://railscasts.com/)