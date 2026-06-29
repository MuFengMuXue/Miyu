# Man / Esdcompat

.
-->


     esdcompat [ options ]
     esdcompat  --help
     esdcompat  --version


      esdcompat  is a compatibility script that takes the
    same arguments as the ESD sound daemon  , but uses them to start a the PulseAudio sound server with the appropriate parameters. It is
    required to make PulseAudio a drop-in replacement for esd, i.e. it
    can be used to make
    start up PulseAudio instead of esd.

     It is recommended to make  esd  a symbolic link to this script.


        -h | --help

        Show help.


        --version

        Show version information.


        -tcp | -promiscuous | -d | -b | -r | -as | -unix | -public | -terminate | -nobeeps | -trust | -port | -bind

        These options understood by the original
       esd  are ignored by
       esdcompat .


        -spawnpid | -spawnfd

        These internally used options understood by the
      original  esd  are properly handled by
       esdcompat , however are not to be used
      manually.


     The PulseAudio Developers  ; PulseAudio is available from


       ,
