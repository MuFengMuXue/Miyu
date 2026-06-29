Under certain circumstances it might be convenient to set a default root password. For example when deploying Gentoo cross-platform trying to [chroot in the common way](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Chrooting "Handbook:AMD64/Installation/Base") may return an [exec format error]. If the [respective entry in the Knowledge Base](https://wiki.gentoo.org/wiki/Knowledge_Base:Chrooting_returns_exec_format_error "Knowledge Base:Chrooting returns exec format error") does not apply chances are that using a [QEMU user chroot](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Compiling_with_qemu_user_chroot "Embedded Handbook/General/Compiling with qemu user chroot") instead of the standard procedure is indicated. In that case circumventing the necessity of chrooting may spare a lot of efforts. Setting a default root password is integral to that circumvention.

** Warning**\
Don\'t do this lightheartedly as it always carries a certain security risk should one forget to change the root password as soon as indicated adequate. At least consider using a [QEMU user chroot](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Compiling_with_qemu_user_chroot "Embedded Handbook/General/Compiling with qemu user chroot").

To set a default root password the file [TARGET/etc/shadow] needs to be manipulated.

## [Hash the password]

Since passwords may not be stored in plaintext use [openssl] to convert the password:

`user `[`$`]`openssl passwd -6`

    Password:
    Verifying - Password:
    $6$I9Q9AyTL$Z76H7wD8mT9JAyrp/vaYyFwyA5wRVN0tze8pvM.MqScC7BBm2PU7pLL0h5nSxueqUpYAlZTox4Ag2Dp5vchjJ0

In this example the string corresponds to the password \"gentoo\".

** Note**\
The `-6` option produces a SHA512 password hash which is only available with \>=[[[dev-libs/openssl]](https://packages.gentoo.org/packages/dev-libs/openssl)[]]-1.1.1. Older versions can only produce an insecure MD5 password hash with the `-1` option.

## [Option 1: Edit shadow by hand]

** Note**\
[TARGET] needs to be replaced by the mountpoint of the target root filesystem.

The resulting string needs to be placed in [TARGET/etc/shadow]. In that file replace the line beginning with `root:` with the line shown below, substituting [SHADOW_COMMAND_OUTPUT] with the string obtained before.

[FILE] **`/etc/shadow`**

    root:SHADOW_COMMAND_OUTPUT:14698:0:::::

In case of the example above it would look like that:

[FILE] **`/etc/shadow`**

    root:$6$I9Q9AyTL$Z76H7wD8mT9JAyrp/vaYyFwyA5wRVN0tze8pvM.MqScC7BBm2PU7pLL0h5nSxueqUpYAlZTox4Ag2Dp5vchjJ0:14698:0:::::

## [Option 2: Use sed to manipulate shadow]

The resulting string needs to be placed in [TARGET/etc/shadow]. First escape [Basic Regular Expressions](https://en.wikipedia.org/wiki/Regular_expression#POSIX_basic_and_extended) in the string provided by the [openssl] command above, that is precede each of the characters `$.*[\^/&` by `\`.

In the following command substitute [MODIFIED_SHADOW_COMMAND_OUTPUT] with that modified string.

** Note**\
[TARGET] needs to be replaced by the mountpoint of the target root filesystem.

`root `[`#`]`sed -i 's/root\:\*/root\:MODIFIED_SHADOW_COMMAND_OUTPUT/' TARGET/etc/shadow `

In case of the example above this would look like that:

`root `[`#`]`sed -i 's/root\:\*/root\:\$6\$I9Q9AyTL\$Z76H7wD8mT9JAyrp\/vaYyFwyA5wRVN0tze8pvM\.MqScC7BBm2PU7pLL0h5nSxueqUpYAlZTox4Ag2Dp5vchjJ0/' TARGET/etc/shadow `