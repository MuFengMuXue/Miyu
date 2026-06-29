# Fonts

```ini
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "urn:fontconfig:fonts.dtd">
<fontconfig>
	<description>Default configuration file</description>


@FC_DEFAULT_FONTS@
	@FC_FONTPATH@
	<dir prefix="xdg">fonts</dir>
	<dir>$HOME/.fonts</dir>

	<match target="pattern">
		<test qual="any" name="family">
			<string>mono</string>
		</test>
		<edit name="family" mode="assign" binding="same">
			<string>monospace</string>
		</edit>
	</match>

	<match target="pattern">
		<test qual="any" name="family">
			<string>sans serif</string>
		</test>
		<edit name="family" mode="assign" binding="same">
			<string>sans-serif</string>
		</edit>
	</match>

	<match target="pattern">
		<test qual="any" name="family">
			<string>sans</string>
		</test>
		<edit name="family" mode="assign" binding="same">
			<string>sans-serif</string>
		</edit>
	</match>
	<match target="pattern">
		<test qual="any" name="family">
			<string>system ui</string>
		</test>
		<edit name="family" mode="assign" binding="same">
			<string>system-ui</string>
		</edit>
	</match>

	<include ignore_missing="yes">@CONFIGDIR@</include>


	<cachedir>@FC_CACHEDIR@</cachedir>
	<cachedir prefix="xdg">fontconfig</cachedir>
	<cachedir>$HOME/.fontconfig</cachedir>

	<config>
		<rescan>
			<int>30</int>
		</rescan>
	</config>

</fontconfig>
```
