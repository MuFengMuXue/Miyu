# Professional audio/Examples

This article is dedicated for advanced setups of a professional audio (pro audio) environment like combinations of sound servers or a complex startup procedure to account for special use cases and hybrid systems (e.g pro audio and virtualization host on one machine).

## Advanced sound server setups
Some multimedia applications and especially web browsers and games do not provide a JACK client and thus, either depend on other sound server packages or just do not make a sound when JACK is running. Although you might want a streamlined pro audio system, you cannot do without some of the aforementioned applications. For that reason you would want to run a combination of sound servers and (automatically) route them into one another.

This layout illustrates a layer model some advanced sound server setups to be discussed:

## PulseAudio+JACK
PulseAudio has become a popular sound server as it is easier to use and widely adopted by most desktop applications in contrast to JACK. Thus, you usually need to install it on a desktop system. On the other hand PulseAudio can be cumbersome, if you want to use JACK on demand for pro audio work on a hybrid system.

To maintain desktop audio capabilities a configuration for routing PulseAudio through JACK is employed. Most preferably use the KXStudio method by installing  and  for running Jack2. Graphical management of the bridge between PulseAudio and JACK can be done via .

If you're using  instead, the default sink and source has to be set after JACK startup using the following script:

More information on how to use that script can be found in PulseAudio/Examples#The shell script method.
