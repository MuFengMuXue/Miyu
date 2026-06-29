# Nyxt

Nyxt is a keyboard-driven web browser designed for hackers. Inspired by Emacs and Vim, it has familiar keybindings (Emacs, vi, CUA), and is infinitely extensible in Common Lisp.

## Installation
Install the  package.

## Usage
When first opened, nyxt provides a short tutorial on how to use the browser, its features and basic keybinds.

For more information, refer to the [https://nyxt.atlas.engineer/documentation manual.

## Configuration
Nyxt can be configured using either in-browser GUI or by directly modifying its config file.

By default all configuration files reside in .

## Tips and tricks
## Change default keybinds
By default nyxt uses the CUA set of keybinds, these can either be changed in the browser settings or by adding this code snippet to :

 ;; emacs keybinds
 (define-configuration buffer
   ((default-modes
     (pushnew 'nyxt/mode/emacs:emacs-mode %slot-value%))))

or if you prefer vi-style keybinds:

 ;; vi keybinds
 (define-configuration buffer
   ((default-modes
     (pushnew 'nyxt/mode/vi:vi-normal-mode %slot-value%))))

## Adblocking
Nyxt comes with a builtin adblocker, to enable it put the following in :

 (define-configuration web-buffer
   ((default-modes
     (pushnew 'nyxt/mode/blocker:blocker-mode %slot-value%))))

## Fingerprinting
## Using tor
To proxy requests over Tor, including downloads:

 (define-configuration nyxt/mode/proxy:proxy-mode
   ((nyxt/mode/proxy:proxy (make-instance 'proxy
                                          :url (quri:uri "socks5://localhost:9050")
                                          :allowlist '("localhost" "localhost:8080")
                                          :proxied-downloads-p t))))

 (define-configuration web-buffer
   ((default-modes (append '(proxy-mode) %slot-value%))))

## Reduce tracking mode
reduce-tracking-mode makes fingerprinting harder by changing the user agent, language, timezone (as to make them more generic) and removing tracking elements from URLs.

To enable it, simply add this to :

 (define-configuration web-buffer
   ((default-modes
     (pushnew 'nyxt/mode/reduce-tracking:reduce-tracking-mode %slot-value%))))

## Troubleshooting
## Videos not playing / Webpages crashing
HTML5 video support requires gstreamer and its associated plugins.

Not having them might prevent the browser from playing video, it also might make those pages crash.

## Blank pages
If you experience blank websites, you may try to disable compositing by adding the following line to
