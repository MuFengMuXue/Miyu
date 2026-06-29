# Scripts / Desc / Xdg Email

xdg-email Manual


       2006


       Kevin
       Krammer

      kevin.krammer@gmx.at

       Jeremy
       White

      jwhite@codeweavers.com
     xdg-utils 1.0


     xdg-email
     1


xdg-email


command line tool for sending mail using the user's preferred e-mail composer


xdg-email


--utf8


--cc

address


--bcc

address


--subject

text


--body

text


--attach

file


mailto-uri


address(es)


xdg-email


--help


--manual


--version


Description


      xdg-email opens the user's preferred e-mail composer in order to send
      a mail to
address(es)
 or

mailto-uri
. RFC2368 defines mailto:
      URIs. xdg-email limits support to, cc, subject and body fields in

mailto-uri
, all other fields are silently
      ignored.
address(es)
 must follow the
      syntax of RFC822. Multiple addresses may be provided as
      separate arguments.


      All information provided on the command line is used to
      prefill corresponding fields in the user's e-mail composer. The user
      will have the opportunity to change any of this information before
      actually sending the e-mail.


      Do not use xdg-email as the default handler for  mailto:  links.
      Its main purpose is to assemble  mailto:  links and hand them over
      to a capable program (usually the defult handler for  mailto:  links.


      xdg-email is for use inside a desktop session only.
      It is not recommended to use xdg-email as root.


Options


--utf8


	    Indicates that all command line options that follow are in utf8.
	    Without this option, command line options are expected to be
	    encoded according to locale.
            If the locale already specifies utf8 this option has no effect.
            This option does not affect mailto URIs that are passed on the
            command line.


--cc

address


	    Specify a recipient to be copied on the e-mail.


--bcc

address


	    Specify a recipient to be blindly copied on the e-mail.


--subject

text


	    Specify a subject for the e-mail.


--body

text


	    Specify a body for the e-mail. Since the user will be able to
	    make changes before actually sending the e-mail, this can be
	    used to provide the user with a template for the e-mail.

text
 may contain linebreaks.


--attach

file


	    Specify an attachment for the e-mail.
file

	    must point to an existing file.


	    Some e-mail applications require the file to remain present
            after xdg-email returns.


         The attach option currently is only implemented for Thunderbird and Icedove on Gnome, Cinnamon, Lxde, Mate, Deepin, KDE, Lxqt and generic desktops with thunderbird as the mailclient or through a custom
xdg-email-hook.sh
. It will not work with the  MAILER  environment variable.


--help


	    Show command synopsis.


--manual


	    Show this manual page.


--version


            Show the xdg-utils version information.


Environment Variables


      xdg-email honours the following environment variables:


 XDG_UTILS_DEBUG_LEVEL


	    Setting this environment variable to a non-zero numerical value
	    makes xdg-email do more verbose reporting on stderr.
	    Setting a higher value increases the verbosity.


 MAILER


	      With this variable a custom command can be set as opener
	      for  mailto:  links, when set it will be preferred
	      over desktop specific behavior unless a
xdg-email-hook.sh
 is present.


	      The set command will be run with the URI appended as the last argument.


	      The  MAILER  is not standardized, keep the command as simple as possible.


Hook Script


      If a
xdg-email-hook.sh
 command is present, it will
      be used as the opener.


      It is called with the URL as it's first argument:

xdg-email-hook.sh

mailto_URL


      If an attachment is specified it will be called
      with an additional
--attach-files
 option
      followed by a list of one or more URI-encoded, comma seperated filepaths.
      (This is compatible with the
thunderbird

-compose
 option)


      Like this:
xdg-email-hook.sh

mailto_URL


--attach-files

file-list


Exit Codes


      An exit code of 0 indicates success while a non-zero exit code
      indicates failure. The following failure codes can be returned:


1


	    Error in command line syntax.


2


	    One of the files passed on the command line did not exist.


3


	    A required tool could not be found.


4


	    The action failed.


5


	    No permission to read one of the files passed on the command
            line.


See Also


         xdg-open
         1
       ,

         xdg-mime
         1
       ,

         xdg-utils-common
         7
       ,
       MIME applications associations specification ,
       RFC 6068 - The 'mailto' URI Scheme


Examples


xdg-email 'Jeremy White  '


xdg-email --attach /tmp/logo.png \
          --subject 'Logo contest' \
          --body 'Attached you find the logo for the contest.' \
          'jwhite@example.com'


xdg-email --subject 'Your password is about to expire' \
          'jwhite@example.com' 'bastian@example.com' 'whipple@example.com'
