# Lenovo ThinkPad P16s (AMD) Gen 2

## S3 sleep not available
This laptop does not support S3 sleep, but only S2idle. For short suspend phases, this is probably fine. For prolonged suspension, you might want to consider hibernating instead.

## Accessibility in firmware setup
High contrast black on white with large type. Unfortunately the selected menu item is indicated with faint dotted lines, which would make it hard to read for those with visual limitations. There is also no Setup UI option to make the graphical BIOS setup text-mode again, unlike previous models.

This device has no diagnostic LEDs but relies on audible beep codes.

## Unreliable mic mute LED
The mic mute LED on key  likes to be permanently on. Installing  and  resolves this. Still, check the actual mic setting before saying something embarrassing into a voice chat.

## Hang on resume
While fixed in firmware for the T14s models, the P16s (and P16v) still needs a workaround for an issue with the ath11k_pci module that occurs when resuming from either suspend or hibernation. Unloading the module prior to suspend/hibernate and loading it again on resume resolves the issue. You should also restart your network manager to avoid issues after resuming.

Put this executable script at the path /usr/lib/systemd/system-sleep/ath11k_pci, and adjust if you use a different network manager than systemd-networkd or NetworkManager:
{{bc |
#!/bin/sh

start_nm() {
	systemctl is-enabled NetworkManager.service && systemctl start NetworkManager.service
}

start_systemd_networkd() {
	systemctl is-enabled systemd-networkd.socket && systemctl start systemd-networkd.socket
	systemctl is-enabled systemd-networkd.service && systemctl start systemd-networkd.service
}

case $1 in
	pre) /usr/bin/systemctl stop NetworkManager.service systemd-networkd.service systemd-networkd.socket; /usr/bin/modprobe -r ath11k_pci ;;
	post) start_nm; start_systemd_networkd; /usr/bin/modprobe ath11k_pci || exit 0 ;;
esac
}}
