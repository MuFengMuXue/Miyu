# GNOME/Web

Web is the default web browser for GNOME.  Web provides a simple and minimalist interface for accessing the internet. Whilst it is developed primarily for GNOME, Web works acceptably in other desktop environments as well.

## Installation
Web can be installed with the  package. If you want to save login passwords, install .

## Configuration
## Blocking advertisements
Enabled by default, one can disable it by unchecking Block Advertisements in Preferences. EasyList is the default blocking list. All lists are periodically refreshed.

To get list of currently enabled filters:

 $ gsettings get org.gnome.Epiphany content-filters

The filters can be modified using a JSON-formatted resource following examples at https://gitlab.com/eyeo/filterlists/contentblockerlists:

 $ gsettings set org.gnome.Epiphany content-filters "'https://gitlab.com/eyeo/filterlists/contentblockerlists/-/raw/master/easylist+easylistchina-minified.json'"

## Tracking Prevention
Web includes Intelligent Tracker Prevention, which can be enabled in Preferences.

## Firefox Sync
Web allows the usage of Firefox Sync to sync bookmarks, history, passwords and open tabs. It can be configured in the Import and Export dropdown menu.

## Web applications
Web can create web applications out of websites and add them to desktop menu. To configure and remove them enter  in the address bar.

## Custom stylesheet
Web supports custom stylesheet you can enable under Fonts and style in Preferences.

Use example below to set new tab page layout and colors according to Adwaita dark variant:

{{hc|~/.config/epiphany/user-stylesheet.css|
#overview {
  background-color: #2E3436 !important;
  max-width: 100% !important;
  max-height: 100% !important;
  position: fixed !important;
}

#overview .overview-title {
  color: white !important;
}
}}

## Fonts
Web does not check GNOME font settings, but checks Font configuration.

## Video
See GStreamer for required plugin installation.

To enable hardware accelerated video decoding, see GStreamer#Hardware video acceleration and #Hardware accelerated compositing.

## Hardware accelerated compositing
By default hardware accelerated compositing is only used when required (on-demand) to display 3D transforms.

To force enable hardware accelerated compositing:

 $ gsettings set org.gnome.Epiphany.web:/ hardware-acceleration-policy 'always'

## Proxy configuration
Web doesn't respect socks_proxy, instead, you can set http_proxy to a  :
 export http_proxy=socks://127.0.0.1:1080

More information: Proxy server#Environment variables

## Spell checking
By default, Web should work with your system language if the Spell Checking option is enabled in Preferences and relevant dictionaries are installed on your system. Additional languages have to be added to the Languages list in Web's preferences from a list of available ones. That list only shows languages for which the Locale has been enabled on your system. The selection of languages in Preferences controls both spell checking and also the Accept-Language header.
