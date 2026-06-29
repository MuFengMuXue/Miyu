# Man / Pulse Cli Syntax

.
-->


      $HOME/.config/pulse/default.pa
      @PA_DEFAULT_CONFIG_DIR@/default.pa
      @PA_DEFAULT_CONFIG_DIR@/system.pa


      PulseAudio provides a simple command line language used by configuration
      scripts, the pacmd interactive shell, and the modules module-cli and
      module-cli-protocol-{unix,tcp}. Empty lines and lines beginning with a
      hashmark (#) are silently ignored. Several commands are supported.


      Note that any boolean arguments can be given positively as '1', 't', 'y',
      'true', 'yes' or 'on'. Likewise, negative values can be given as '0',
      'f', 'n', 'false', 'no' or 'off'. Case is ignored.


        help
        Show a quick help on the commands available.


        list-modules
        Show all currently loaded modules with their arguments.


        list-cards
        Show all currently registered cards


        list-sinks  or  list-sources
        Show all currently registered sinks (resp. sources).


        list-clients
        Show all currently active clients.


        list-sink-inputs  or  list-source-outputs
        Show all currently active inputs to sinks a.k.a. playback
      streams (resp. outputs of sources a.k.a. recording streams).


        stat
        Show some simple statistics about the allocated memory blocks and the space used by them.


        info  or  ls  or  list
        A combination of all status commands described above (all
      three commands are synonyms).


        load-module   name  [ arguments... ]
        Load a module specified by its name and arguments. For most
      modules it is OK to be loaded more than once.


        unload-module   index|name
        Unload a module, specified either by its index in the module
      list or its name.


        describe-module   name
        Give information about a module specified by its name.


        set-sink-volume|set-source-volume   index|name   volume
        Set the volume of the specified sink (resp. source). You may
      specify the sink (resp. source) either by its index in the sink/source list
      or by its name. The volume should be an integer value greater or equal than
      0 (muted). Volume 65536 (0x10000) is 'normal' volume a.k.a. 100%. Values
      greater than this amplify the audio signal (with clipping).


        set-sink-mute|set-source-mute   index|name   boolean
        Mute or unmute the specified sink (resp. source). You may
      specify the sink (resp. source) either by its index or by its name.
      The mute value is either 0 (not muted) or 1 (muted).


        set-sink-input-volume|set-source-output-volume   index   volume
        Set the volume of a sink input (resp. source output) specified
      by its index. The same volume rules apply as with set-sink-volume.


        set-sink-input-mute|set-source-output-mute   index   boolean
        Mute or unmute a sink input (resp. source output) specified
      by its index. The same mute rules apply as with set-sink-mute.


        set-default-sink|set-default-source   index|name
        Make a sink (resp. source) the default. You may specify the
      sink (resp. source) by its index in the sink (resp. source) list or by its
      name. Use the special name \@NONE@ to unset the user defined default sink or
      source. In this case, pulseaudio will return to the default sink or source
      selection based on priority.  Note that defaults may be overridden by
      various policy modules or by specific stream configurations.


        set-card-profile   index|name   profile-name
        Change the profile of a card.


        set-sink-port|set-source-port   index|name   port-name
        Change the profile of a sink (resp. source).


        set-port-latency-offset   card-index|card-name   port-name   offset
        Change the latency offset of a port belonging to the specified card


        suspend-sink|suspend-source   name|index
         true|false

        Suspend or resume the specified sink or source (which may be
        specified either by its name or index), depending whether true
        (suspend) or false (resume) is passed as last argument. Suspending
        a sink will pause all playback and suspending a source will pause all
        capturing. Depending on the module implementing the sink or source this
        might have the effect that the underlying device is closed, making it
        available for other applications to use. The exact behaviour depends on
        the module.


        suspend   boolean
        Suspend all sinks and sources.


        move-sink-input|move-source-output   index   sink-index|sink-name
        Move sink input (resp. source output) to another sink
      (resp. source).


        update-sink-proplist|update-source-proplist   index|name   properties
        Update the properties of a sink (resp. source) specified by
      name or index. The property is specified as e.g. device.description="My
      Preferred Name"


        update-sink-input-proplist|update-source-output-proplist   index   properties
        Update the properties of a sink input (resp. source output)
      specified by index. The properties are specified as above.


        list-samples
        Lists the contents of the sample cache.


        play-sample   name   sink-index|sink-name
        Play a sample cache entry to a sink.


        remove-sample   name
        Remove an entry from the sample cache.


        load-sample   name   filename
        Load an audio file to the sample cache.


        load-sample-lazy   name   filename
        Create a new entry in the sample cache, but don't load the
      sample immediately. The sample is loaded only when it is first used.
      After a certain idle time it is freed again.


        load-sample-dir-lazy   path
        Load all entries in the specified directory into the sample
      cache as lazy entries. A shell globbing expression (e.g. *.wav) may be
      appended to the path of the directory to add.


        kill-client   index
        Remove a client forcibly from the server. There is no protection
      against the client reconnecting immediately.


        kill-sink-input|kill-source-output   index
        Remove a sink input (resp. source output) forcibly from the
      server. This will not remove the owning client or any other streams opened
      by the same client from the server.


        set-log-level   numeric-level
        Change the log level.


        set-log-meta   boolean
        Show source code location in log messages.


        set-log-target   target
        Change the log target (null, auto, journal, syslog, stderr,
      file:PATH, newfile:PATH).


        set-log-time   boolean
        Show timestamps in log messages.


        set-log-backtrace   num-frames
        Show backtrace in log messages.


        play-file   filename   sink-index|sink-name
        Play an audio file to a sink.


        dump
        Dump the daemon's current configuration in CLI commands.


        dump-volumes
        Debug: Shows the current state of all volumes.


        shared
        Debug: Show shared properties.


        send-message   recipient   message   message_parameters
        Send a message to the specified recipient object. If applicable an additional string containing
      message parameters can be specified. A string is returned as a response to the message. For available messages
      see https://cgit.freedesktop.org/pulseaudio/pulseaudio/tree/doc/messaging_api.txt.


        exit
        Terminate the daemon. If you want to terminate a CLI
      connection ("log out") you might want to use ctrl+d


      In addition to the commands described above there are a few meta directives
      supported by the command line interpreter.


        .include   filename|folder
        Executes the commands from the specified script file or in all
      of the *.pa files within the folder.


        .fail  and  .nofail
        Enable (resp. disable) that following failing commands will
      cancel the execution of the current script file. This is ignored when
      used on the interactive command line.


        .ifexists   filename
        Execute the subsequent block of commands only if the specified
      file exists. Typically  filename  indicates a module. Relative
      paths are resolved using the module directory as the base. By using an
      absolute path, the existence of other files can be checked as well.


        .else  and  .endif
        A block of commands is delimited by an  .else  or
       .endif  meta command. Nesting conditional commands is not
      supported.


     The PulseAudio Developers  ;
    PulseAudio is available from


       ,
       ,
