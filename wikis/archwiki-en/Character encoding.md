# Character encoding

Character encoding is the process of interpreting bytes to readable characters. UTF-8 is the dominant encoding since 2009 and is promoted as a de-facto standard https://utf8everywhere.org/.

## UTF-8
## Terminal
Most terminals use UTF-8 by default. However, some (e.g: , ) need to be launched from a UTF-8 locale. To do that, set the codeset part of your locale to  and reload your session. See Locale#Setting the locale for instructions.

* xterm - Run with the argument  or configure resource .

## Unicode character insertion
See List of applications/Utilities#Text input.

* LibreOffice includes a built-in charmap in Insert > Special Character showing character block, hex, and decimal encodings.
* Compose Key: XCompose can be set up to insert special characters.
* AltGr can be set up to access additional keyboard levels providing extra characters as well as Unicode control characters such as ZWNJ and RTL mark.
* Vim: using   in insert mode, where  is the hexadecimal code point.

## URL encoding
URIs accept US-ASCII characters only and use percent-encoding to encode non-ASCII characters. This can result in very long and human-unreadable URIs.

In Firefox, it is possible to copy decoded URLs by enabling the  flag in , or by inserting a space to the start of the URL, then selecting it (with the space) and copying it. However, this trick does not work on Chromium, and there is no equivalent flag. Alternatively, select starting at the end of the URL until right after the  part, then copy.

For command line usage, you can use  to translate encoded URLs from stdin.

 $ python3 -c "import sys; from urllib.parse import unquote; print(unquote(sys.stdin.read().strip()))"

## Troubleshooting
Encoding problems are usually due to two programs communicating with different encodings, with one side typically not using UTF-8, resulting in mojibake.

## Incorrect archive encoding
Zip archives sometimes use encodings other than Unicode for the filenames. This issue is most commonly seen with archives created in legacy versions of Windows (XP, Vista, and 7), where File Explorer will prioritize a character set that more closely matches the system locale even if it uses a non-Latin writing system.

 is built with patches to enable character set conversion.  of  has same feature. However, it won't do so automatically and will still default to the assumption that filenames are UTF8-encoded. To properly extract an archive with non-UTF8 filenames, use  followed by the target encoding, e.g. CP936 is a common Simplified Chinese charset in old versions of Windows:

 $ unzip -O CP936 file.zip

Other common charsets include GBK, also for Simplified Chinese:

 $ unzip -O gbk file.zip

And CP932 (not Shift-JIS), for Japanese:

 $ bsdunzip -O CP932 file.zip

If unsure about which charset you need, you can list an archive's files without extracting them by adding the  flag, which allows you to verify that the filenames are printed correctly:

 $ unzip -lO shift-jis file.zip

Alternatively,  detects encoding for file names automatically.

 of  may be used for some non zip archives encoded without UTF-8.

## Incorrect file name encoding
Use  for encoding-conversion :

 $ convmv -f SOURCE_ENCODING -t UTF-8 --nosmart file

By default, convmv shows what would be done without actual moving. After figuring out the original encoding using  (e.g: for Chinese ), add the  option to proceed with the move operation.

By default, convmv skips file name conversion if it is already UTF8-encoded. Use the  option to force the conversion.

Use  to find the supported encodings.

## Incorrect file encoding
Use the  command to convert the format. For example:

 $ iconv -f SOURCE_ENCODING -t UTF-8 -o new-file origin-file

 specifies the original encoding and  specifies the output encoding. Use  to query all supported encodings and  to specify the output file.

## Vim
If the locale is UTF-8, opening other char-encoded files may be garbled. You can add a fallback adding to vimrc a line similar to:

 set fileencodings=utf8,cp936,gb18030,big5

Alternatively, you can explicitly set it by . Vim will do the conversion via iconv automatically. See .

## Incorrect MP3 ID3 tag encoding
To modify the MP3 file tag, convert using  or :

 $ mid3iconv -e SOURCE_ENCODING file.mp3

If file modification is undesired, you can tweak the behavior of media players. For players that use GStreamer as the backend, such as Rhythmbox and totem, set the environment variable:

 GST_ID3_TAG_ENCODING=GBK:UTF-8:GB18030

 supports tag editing and setting ID3v2 encoding. Go to File > Preferences > Advanced, click I know what I'm doing! and enter a space-separated list of encodings in the ID3 encodings field. You can also edit the configuration file manually:

## Incorrect mount encoding
Generally, the mounted character set is different from the locales, which can be set by modifyinig fstab. If the locale is utf8, modify the line to:

If the locale is GBK, it should be:

## Incorrect Samba encoding
When using Arch as a Samba server, adding the following line to  can solve the garbled problem of Windows clients:

## Incorrect FTP encoding
If you use UTF8 locale, the downloaded file name from a non-Unicode-encoded server might be garbled. For lftp, make the following settings under :

For gftp, you can do the following settings in :

However, the downloaded file name is still garbled and needs to be patched and compiled. The patch address is: https://www.teatime.com.tw/%7Etommy/linux/gftp_remote_charsets.patch
