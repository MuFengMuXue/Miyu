# Man / Default.pa

.
-->


      $HOME/.config/pulse/default.pa
      @PA_DEFAULT_CONFIG_DIR@/default.pa
      @PA_DEFAULT_CONFIG_DIR@/system.pa


     The PulseAudio sound server interprets a configuration script on
    startup, which is mainly used to define the set of modules to load. When
    PulseAudio runs in the per-user mode and
     $HOME/.config/pulse/default.pa  exists, that file is used. When
    PulseAudio runs in the per-user mode and that file doesn't exist,
     @PA_DEFAULT_CONFIG_DIR@/default.pa  is used. When PulseAudio
    runs as a system service,  @PA_DEFAULT_CONFIG_DIR@/system.pa  is
    used.

     The script should contain directives in the PulseAudio CLI language, as
    documented in  .


     The PulseAudio Developers  ;
    PulseAudio is available from


       ,
       ,
       ,
