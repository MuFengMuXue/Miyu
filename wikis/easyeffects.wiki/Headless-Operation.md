EasyEffects is a GUI application requiring X and Gtk. To run it on a headless machine, for example a Raspberry Pi used to play back music, Xvfb can be used instead of a full X session:
```
Xvfb :1 &
export DISPLAY=:1
easyeffects --gapplication-service &
```
Running a VNC server could give access to the Xvfb session.
The following script can be used to start/stop Xvfb and EasyEffects. `/usr/local/bin/easyeffects-xvfb`: 
```
#!/bin/bash

if [[ "$1" = "start" ]]; then
	pkill Xvfb
	sleep 1
	Xvfb :43 -screen 0 1024x768x16 &
	sleep 3
	export DISPLAY=:43
	easyeffects --gapplication-service
fi
if [[ "$1" = "stop" ]]; then
	easyeffects --quit
	pkill Xvfb
fi

```
An appropriate systemd service can be stored in `.config/systemd/user/easyeffects-xvfb.service`:
```
[Unit]
Description=EasyEffects inside Xvfb

[Service]
Type=simple
ExecStart=/usr/local/bin/easyeffects-xvfb start
ExecStop=/usr/local/bin/easyeffects-xvfb stop
Restart=on-failure

[Install]
WantedBy=default.target
```
Now the service can be started and enabled so EasyEffects is run on user login.
```
systemctl --user daemon-reload
systemctl --user start easyeffects-xvfb
systemctl --user enable easyeffects-xvfb
journalctl --user -u easyeffects-xvfb
```