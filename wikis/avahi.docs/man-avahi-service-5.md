# Man / Avahi.service

@servicedir@/*.service


        @servicedir@/*.service  are XML
      fragments containing static DNS-SD service data. Every service
      file can contain multiple service definitions which share the
      same name. This is useful for publishing service data for
      services which implement multiple protocols. (i.e. a printer
      implementing _ipp._tcp and _printer._tcp)


             The document tag of avahi
        service files. Should contain one     and one or more
            elements.


             The
        service name. If  replace-wildcards  is "yes", any
        occurrence of the string "%h" will be replaced by the local
        host name. This can be used for service names like "Remote
        Terminal on %h". If  replace-wildcards  is not
        specified, defaults to "no".


        Contains the service information for exactly one service
        type. Should contain one     and one
            element. Optionally it may contain one
           , one
           , any number of
            and any number of
            elements. The attribute
         protocol  specifies the protocol to advertise the
        service on. If  any  is used (which is the default),
        the service will be advertised on both IPv4 and IPv6.


             Contains the DNS-SD service type for this service. e.g. "_http._tcp".


             Contains an additional DNS-SD service subtype for this service. e.g. "_anon._sub._ftp._tcp".


             The domain name this service
        should be registered. If omitted defaults to the default domain
        of the avahi daemon. (probably .local)


             The host name of the host that
        provides this service. This should be a host that is
        resolvable by multicast or unicast DNS. Please note that you
        need to specify a fully-qualified domain name (FQDN) here,
        i.e. .local is not appended implicitly! The host name doesn't
        need to be part of the domain specified in
           . See   for more information how to publish additional
        host name mappings.


             The IP port number the service listens on.


             DNS-SD
        TXT record data. If  value-format  is "text", the
        value of the TXT record is taken verbatim. If
         value-format  is "binary-hex" then the value of TXT
        record is decoded by taking pairs of characters after the "="
        char and interpreting them as the textual representation of
        the two-digit hexadecimal number. Both uppercase and lowercase
        hexadecimal digits are allowed. The 0x or 0X prefix is not
        allowed. This requires the length of the value to be even. If
         value-format  is "binary-base64" then the value of
        TXT record is decoded with a base64 decoder. The character set
        used is A-Za-z0-9+/. This requires the length of the value to
        be a multiple of 4, with "=" as padding at the end. If
         value-format  is not specified, defaults to
        "text". Examples (all the values are decoded to the string
        "value" without quotes):

          key=value
          key=value
          key=76616c7565
          key=dmFsdWU=


	   The Avahi Developers  ; Avahi is
	  available from


         ,


	   This man page was written using   by Oliver
	  Kurth.
