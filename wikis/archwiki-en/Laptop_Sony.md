# Laptop/Sony

## Model list
| Vaio VGN-C2Z || 2007-07-11 ||  ||  ||  ||  ||  ||  ||  ||
|-
| Vaio VGN-NR320FH || 2008-11-06 ||  ||  ||  ||  ||  ||  ||  || Fn keys need sony-laptop and sonypid.
|-
| Vaio VGN-SA/SB || 2014-02-08 ||  ||  ||  ||  ||  ||  || ||
|-
| Vaio SV-S1511X9E/B || 2018-01-01 || * ||  ||  ||  ||  ||  || || *nouveau needs
|-
| Vaio SVT13 Touch || 2020-01-03 ||  ||  ||  ||  ||  ||  ||  || Action keys: only WEB is mapped to browser, ASSIST sends tilde(~) and VAIO does nothing.Touchpad disable seems to do nothing.
|-
| Vaio SVF14 Touch || 2022-05-21 ||  ||  ||  ||  ||  ||  ||  || keyboard backlight needs  set to 1 not -1fix mouse and keyboard after hibernation with kernel parameters Display backlight only works with kernel parameters . you might also want to use
|-
| Vaio VGN-FW140E || 2025-06-05 ||  ||  ||  ||  ||  ||  ||  || Fix resume after suspend with kernel parameters Fix extremely slow boot due to bad clocksource with kernel parameters .
|-
| Vaio VGN-NR220E || 2025-07-06 ||  ||  ||  ||  ||  ||  ||  ||
|-
|}

## Troubleshooting
If you encounter issues with power management, in particular regarding suspend and hibernate, you might have to add the kernel parameter  to your boot loader.
