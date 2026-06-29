# Man / Bssh

bssh
       bvnc
       bshell


       bssh/bvnc/bshell browses for SSH/VNC servers on the local
      network, shows them in a GUI for the user to select one and
      finally calls ssh/vncviewer after a selection was made.

       If the binary is called as bssh only ssh servers will be shown. If the binary is called as bvnc only VNC servers will be shown. If the binary is called as bshell both VNC and SSH servers are shown.


	  -s | --ssh
	  Browse for SSH servers (and only SSH servers)  regardless under which name the binary is called.


	  -v | --vnc
	  Browse for VNC servers (and only VNC servers) regardless under which name the binary is called.


	  -S | --shell
	  Browse for both VNC and SSH servers regardless under which name the binary is called.


	  -d | --domain=   DOMAIN
          Browse in the specified domain. If omitted
            bssh/bvnc/bshell will browse in the default browsing domain
            (usually .local)


	  -h | --help
	  Show help.


       The Avahi Developers  ; Avahi is
      available from


         ,  ,


       This man page was written using   by Oliver Kurth.
