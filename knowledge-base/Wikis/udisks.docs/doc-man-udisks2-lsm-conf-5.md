# Doc / Man / Udisks2 Lsm.conf

udisks2_lsm.conf

     August 2018
     udisks2


     udisks2_lsm.conf
     5
     UDisks2 LSM Module Configuration
     udisks2_lsm.conf


udisks2_lsm.conf


The UDisks2 LSM Module configuration file


DESCRIPTION


      The lsm module of UDisks2 uses  LibStorageMgmt [1]
      API to provides  org.freedesktop.UDisks2.Drive.LSM
      interface with RAID information for external(DAS or SAN) Linux disk
      drive. Please refer to storage interface document for detail.


      Some storage systems require extra configuration in
       @sysconfdir@/udisks2/modules.conf.d/udisks2_lsm.conf .


CONFIGURATION FILE


 refresh_interval =


            This option controls how often the RAID information cache should be
            refreshed. If not defined, the default value is 30 (seconds).


 enable_sim = true|false


            This option indicates whether the lsm module should try simulator of
            LibStorageMgmt. This is only for developers. If not defined,
            the default value is false (do not enable simulator of
            LibStorageMgmt).  If enabled, the
             sim://  URI will be
            used to query LibStorageMgmt simulator plugin.


 enable_hpsa = true|false


            This option indicates whether the lsm module should check HP
            SmartArray.  If not defined, the default value is true (check HP
            SmartArray).


            To be functional this also requires the
             libstoragemgmt-hpsa-plugin
            package to be installed and configured properly. Please refer to the
             hpsa_lsmplugin(1)  manpage for detail.


            If enabled, the  hpsa://  URI will
            be used to query LibStorageMgmt HP SmartArray plugin.


 extra_uris= ["uri_string_1", "uri_string_2"]


            This option defines extra LibStorageMgmt URI list here. Please
            refer to  LibStorageMgmt User Guide[3]  for the URI
            format.


            Requires double quoted string separated by comma, for example:


              extra_uris = ["ontap+ssl://root@ontap.a.ip", "ontap+ssl://root@ontap.b.ip"]


            If not defined, empty list (no extra URI loaded) will be used.


 extra_passwords = ["password_string_1", "password_string_2"]


            This options defines the passwords of above URI list. Please use
            double quoted string separated by comma, for example:


              extra_paasswords = ["password1", "password2"]


HARDWARE SUPPORT STATUS


      Any hardware which is supported in LibStorageMgmt with these capabilities
      will get fully supported by the UDisks2 LSM module:


          *  VOLUMES capabilities
          with valid VPD83 information,


          *  VOLUME_RAID_INFO
          capabilities.


      Please refer to LibStorageMgmt document website[2] for support status.


      Tested hardware:


 HP SmartArray


          Using  libstoragemgmt-hpsa-plugin
          package.


 NetApp ONTAP


          Using  libstoragemgmt-netapp-plugin
          package.


AUTHOR


      Gris Ge


BUGS


      Please send bug reports to either the distribution bug tracker
      or the upstream bug tracker at
       .


SEE ALSO


       lsmd (1),
         udisksd  8   ,
       hpsa_lsmplugin (1),
       ontap_lsmplugin (1),


          [1]:


          [2]:


          [3]:
