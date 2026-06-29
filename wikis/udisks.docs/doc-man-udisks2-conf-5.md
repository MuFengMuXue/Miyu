# Doc / Man / Udisks2.conf

udisks2.conf

     August 2018
     udisks


     udisks2.conf
     5
     UDisks Daemon Configuration
     udisks2.conf


udisks2.conf


The udisks2 configuration file


DESCRIPTION


      The udisks project provides additional functionality via pluggable
      modules. These plugins can be inserted into the daemon either by D-Bus
      call  org.freedesktop.UDisks2.Manager.EnableModules()
      or by running the udisks daemon with
       --force-load-modules  command line option.


      It is also possible to configure the modules loading behavior via
      the configuration file placed at
       @sysconfdir@/udisks2/udisks2.conf .


CONFIGURATION FILE


      The default configuration file  udisks2.conf  looks like this:


    [udisks2]
    modules=*
    modules_load_preference=ondemand

    [defaults]
    encryption=luks1


 modules =


            This variable controls what modules should be loaded. It may
            contain either a comma-separated list of modules to load or a
            single asterisk which stands for all the modules.


 modules_load_preference = ondemand|onstartup


            This key tells udisksd when to load the plugins: either at startup
            or on demand by D-Bus
             org.freedesktop.UDisks2.Manager.EnableModules() .


 encryption = luks1|luks2


            This variable controls which encryption technology will be used
            by default when creating an encrypted filesystem.


AUTHOR


BUGS


      Please send bug reports to either the distribution bug tracker
      or the upstream bug tracker at
       .


SEE ALSO


         udisks  8   ,
         udisksctl  1   ,
         umount.udisks2  8
